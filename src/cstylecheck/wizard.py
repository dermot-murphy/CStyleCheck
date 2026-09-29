"""
wizard.py — Interactive --init wizard for CStyleCheck.

Walks the user through a short Q&A and generates a commented
.cstylecheck.yml starter config tailored to their project.

Also provides built-in presets (barr-c, minimal, misra) for quick
starts without the interactive wizard.
"""
from __future__ import annotations

from pathlib import Path


# ---------------------------------------------------------------------------
# Preset configurations
# ---------------------------------------------------------------------------

# Opt-in (#418) rules each standard-specific preset / wizard answer enables
# (#420).  Order is the order the keys are written to the generated YAML.
# misc.boolean_comparison is a style rule and belongs to no preset.
MISRA_OPT_IN_RULES: tuple[str, ...] = (   # 15.1, 13.4, 11.5, 17.2, 15.7
    "goto_usage", "assignment_in_condition", "void_pointer",
    "recursive_function", "empty_else",
)
BARR_C_OPT_IN_RULES: tuple[str, ...] = (  # §3.2, §5.7, §8.3
    "multiple_statements_per_line", "sizeof_type", "empty_else",
)
# Shipped rules.yml default severities (unchanged by presets / wizard).
_OPT_IN_SEVERITY: dict[str, str] = {
    "goto_usage":                   "error",
    "assignment_in_condition":      "warning",
    "multiple_statements_per_line": "warning",
    "void_pointer":                 "warning",
    "recursive_function":           "error",
    "sizeof_type":                  "info",
    "empty_else":                   "warning",
}


# --init wizard naming-convention choices: on-screen label -> canonical
# case-style name written to the config (a key of utils._CASE_PATTERNS).
# Label order is the prompt order (#422).
WIZARD_CASE_CHOICES: dict[str, str] = {
    "lower_snake": "lower_snake",
    "camelCase":   "camel",
    "PascalCase":  "pascal",
}


def _opt_in(rules: tuple[str, ...]) -> dict:
    """Return ordered ``misc`` entries enabling *rules* at shipped severity."""
    return {r: {"enabled": True, "severity": _OPT_IN_SEVERITY[r]} for r in rules}


_PRESET_BARR_C = {
    "file_prefix":  {"enabled": True,  "severity": "error",
                     "separator": "_", "case": "lower",
                     "exempt_main": True, "exempt_patterns": ["^main$", "^ISR$"]},
    "variables":    {"enabled": True,  "severity": "error", "case": "lower_snake",
                     "min_length": 3, "max_length": 40,
                     "allow_single_char_loop_vars": True,
                     "global":    {"g_prefix": {"enabled": True, "prefix": "g_"}},
                     "static":    {"s_prefix": {"enabled": True, "prefix": "s_"}},
                     "pointer_prefix": {"enabled": True, "prefix": "p_"},
                     "bool_prefix":    {"enabled": True, "prefix": "b_"}},
    "functions":    {"enabled": True,  "severity": "error", "case": "lower_snake",
                     "min_length": 3, "max_length": 40},
    "typedefs":     {"enabled": True,  "severity": "error",
                     # Barr-C §5.1.a: type names are lower-case with an
                     # _t suffix.  Canonical case names only (#422); the
                     # old "PascalCase" was unknown (silently passed) and
                     # is unsatisfiable together with the _t suffix.
                     "case": "lower_snake",
                     # nested {enabled, suffix} form per rules.yml; a bare
                     # string crashed the checker (#420)
                     "suffix": {"enabled": True, "suffix": "_t"}},
    "enums":        {"enabled": True,  "severity": "error",
                     "type_case": "lower_snake",   # Barr-C §5.1.a (#422)
                     "type_suffix": {"enabled": True, "suffix": "_t"},
                     "member_case": "upper_snake"},
    "misc": {
        "line_length":        {"enabled": True,  "severity": "warning", "max": 120},
        "magic_numbers":      {"enabled": True,  "severity": "warning",
                               "exempt_values": [0, 1, -1, 2, 8, 16, 32, 64, 128, 256]},
        "unsigned_suffix":    {"enabled": True,  "severity": "info",
                               "require_on_unsigned_constants": True},
        "lowercase_l_suffix": {"enabled": True,  "severity": "error"},
        "eof_comment":        {"enabled": False},
        # Opt-in rules (#418) enabled by this preset (#420): §3.2, §5.7, §8.3.
        **_opt_in(BARR_C_OPT_IN_RULES),
    },
    "sign_compatibility": {"enabled": True, "severity": "warning"},
}

_PRESET_MINIMAL = {
    "file_prefix":  {"enabled": False},
    "variables":    {"enabled": True,  "severity": "warning", "case": "lower_snake",
                     "min_length": 2, "max_length": 40,
                     "allow_single_char_loop_vars": True},
    "functions":    {"enabled": False},
    "typedefs":     {"enabled": False},
    "enums":        {"enabled": False},
    "misc": {
        "line_length":   {"enabled": True,  "severity": "warning", "max": 120},
        "magic_numbers": {"enabled": True,  "severity": "warning",
                          "exempt_values": [0, 1, -1, 2, 8, 16, 32, 64, 128, 256, 1024]},
    },
    "sign_compatibility": {"enabled": False},
}

_PRESET_MISRA = {
    "file_prefix":  {"enabled": True,  "severity": "warning"},
    "variables":    {"enabled": True,  "severity": "warning", "case": "lower_snake",
                     "min_length": 2, "max_length": 31},
    "functions":    {"enabled": True,  "severity": "warning", "case": "lower_snake"},
    "misc": {
        "magic_numbers":      {"enabled": True,  "severity": "warning",
                               "exempt_values": [0, 1]},
        "unsigned_suffix":    {"enabled": True,  "severity": "error",
                               "require_on_unsigned_constants": True},
        "lowercase_l_suffix": {"enabled": True,  "severity": "error"},
        "octal_constant":     {"enabled": True,  "severity": "error"},
        "trigraph":           {"enabled": True,  "severity": "error"},
        # Opt-in rules (#418) enabled by this preset (#420): 15.1, 13.4,
        # 11.5, 17.2 and empty else (related to 15.7).
        **_opt_in(MISRA_OPT_IN_RULES),
    },
    "sign_compatibility": {"enabled": True, "severity": "error"},
}

PRESETS: dict[str, dict] = {
    "barr-c":  _PRESET_BARR_C,
    "minimal": _PRESET_MINIMAL,
    "misra":   _PRESET_MISRA,
}


# ---------------------------------------------------------------------------
# YAML renderer (no Jinja2 / PyYAML required for output — hand-built)
# ---------------------------------------------------------------------------

def _render_yaml(cfg: dict, preset_name: str | None = None) -> str:
    """Render *cfg* as a commented YAML string."""
    header_comment = (
        "# CStyleCheck configuration\n"
        "# Generated by: cstylecheck --init"
        + (f" --preset {preset_name}" if preset_name else "")
        + "\n"
        "# Docs: https://github.com/dermot-murphy/CStyleCheck\n"
        "#\n"
        "# Toggle any rule with  enabled: true / false\n"
        "# Severity levels:      error | warning | info\n\n"
    )

    import yaml  # Only needed for output; already a hard dependency
    body = yaml.dump(cfg, default_flow_style=False, sort_keys=False, allow_unicode=True)
    return header_comment + body


# ---------------------------------------------------------------------------
# Interactive wizard
# ---------------------------------------------------------------------------

def _ask(prompt: str, default: str, prompt_fn=input) -> str:
    """Ask a question; return *default* if the user just presses Enter."""
    try:
        answer = prompt_fn(f"{prompt} [{default}]: ").strip()
    except EOFError:
        return default
    return answer if answer else default


def _ask_bool(prompt: str, default: bool, prompt_fn=input) -> bool:
    """Ask a yes/no question."""
    default_hint = "Y/n" if default else "y/N"
    try:
        answer = prompt_fn(f"{prompt} [{default_hint}]: ").strip().lower()
    except EOFError:
        return default
    if not answer:
        return default
    return answer.startswith("y")


def _ask_choice(prompt: str, choices: list, default: str, prompt_fn=input) -> str:
    """Ask a multiple-choice question; return choice or default."""
    choice_str = " / ".join(
        f"[{c}]" if c == default else c for c in choices
    )
    try:
        answer = prompt_fn(f"{prompt} ({choice_str}): ").strip()
    except EOFError:
        return default
    if not answer:
        return default
    # Accept prefix matching
    answer_lower = answer.lower()
    for ch in choices:
        if ch.lower().startswith(answer_lower) or answer_lower == ch.lower():
            return ch
    return default


def run_wizard(
    output_path: str | None = None,
    prompt_fn=input,
    print_fn=print,
    overwrite: bool = False,
) -> int:
    """Run the interactive wizard.  Returns 0 on success, 1 on abort."""
    output_file = Path(output_path or ".cstylecheck.yml")

    if output_file.exists() and not overwrite:
        answer = _ask_bool(
            f"'{output_file}' already exists. Overwrite?",
            default=False,
            prompt_fn=prompt_fn,
        )
        if not answer:
            print_fn("Aborted - existing config preserved.")
            return 1

    print_fn("\nCStyleCheck config wizard - press Enter to accept defaults.\n")

    # ---- Naming convention ----
    # Friendly labels on screen; the canonical _CASE_PATTERNS name is
    # what gets written to the config (#422).
    var_case_label = _ask_choice(
        "Variable naming convention?",
        list(WIZARD_CASE_CHOICES),
        "lower_snake",
        prompt_fn=prompt_fn,
    )
    var_case = WIZARD_CASE_CHOICES[var_case_label]

    min_len_str = _ask("Minimum variable name length?", "2", prompt_fn=prompt_fn)
    try:
        min_len = max(1, int(min_len_str))
    except ValueError:
        min_len = 2

    max_line_str = _ask("Maximum line length?", "120", prompt_fn=prompt_fn)
    try:
        max_line = max(40, int(max_line_str))
    except ValueError:
        max_line = 120

    g_prefix  = _ask_bool("Enforce g_ prefix on global variables?", False, prompt_fn)
    p_prefix  = _ask_bool("Enforce p_ prefix on pointer variables?", False, prompt_fn)
    copyright = _ask_bool("Require copyright header in every file?",  False, prompt_fn)
    misra     = _ask_bool("Enable MISRA-C checks (unsigned suffix, octal, trigraph)?", False, prompt_fn)
    sign      = _ask_bool("Enable sign-compatibility checks across TUs?",             False, prompt_fn)
    # Opt-in standard-specific rules (#420).  Asked last so the order of the
    # earlier questions (and any scripted stdin answering them) is unchanged;
    # EOF / Enter keeps the default of No.
    misra_rules = _ask_bool(
        "Enable MISRA C:2012 rules (goto 15.1, assignment in condition 13.4, "
        "void pointer 11.5, recursion 17.2, empty else 15.7)?",
        False, prompt_fn)
    barr_rules = _ask_bool(
        "Enable Barr-C rules (one statement per line §3.2, "
        "sizeof on objects §5.7, empty else §8.3)?",
        False, prompt_fn)

    # ---- Build config ----
    cfg: dict = {}

    cfg["file_prefix"] = {
        "enabled": True, "severity": "error",
        "separator": "_", "case": "lower",
        "exempt_main": True, "exempt_patterns": ["^main$"],
    }

    var_cfg: dict = {
        "enabled": True, "severity": "warning", "case": var_case,
        "min_length": min_len, "max_length": 40,
        "allow_single_char_loop_vars": True,
    }
    if g_prefix:
        var_cfg["global"] = {"g_prefix": {"enabled": True, "severity": "warning", "prefix": "g_"}}
    if p_prefix:
        var_cfg["pointer_prefix"] = {"enabled": True, "severity": "warning", "prefix": "p_"}
    cfg["variables"] = var_cfg

    cfg["functions"] = {
        "enabled": True, "severity": "warning", "case": var_case,
        "min_length": 3, "max_length": 40,
    }

    cfg["misc"] = {
        "line_length": {"enabled": True, "severity": "warning", "max": max_line},
        "magic_numbers": {
            "enabled": True, "severity": "warning",
            "exempt_values": [0, 1, -1, 2, 8, 16, 32, 64, 128, 256, 1024],
        },
        "unsigned_suffix": {
            "enabled": misra, "severity": "info",
            "require_on_unsigned_constants": True,
        },
        "lowercase_l_suffix": {"enabled": misra, "severity": "error"},
        "octal_constant":     {"enabled": misra, "severity": "error"},
        "trigraph":           {"enabled": misra, "severity": "error"},
        "copyright_header":   {"enabled": copyright, "severity": "error"},
    }
    # Opt-in rules (#418/#420): always listed so they can be toggled later;
    # enabled only when the matching question was answered yes.  empty_else
    # is shared by both standards.
    for rule in dict.fromkeys(MISRA_OPT_IN_RULES + BARR_C_OPT_IN_RULES):
        on = ((misra_rules and rule in MISRA_OPT_IN_RULES)
              or (barr_rules and rule in BARR_C_OPT_IN_RULES))
        cfg["misc"][rule] = {"enabled": on, "severity": _OPT_IN_SEVERITY[rule]}

    cfg["sign_compatibility"] = {"enabled": sign, "severity": "warning"}

    yaml_text = _render_yaml(cfg)

    output_file.write_text(yaml_text, encoding="utf-8")
    print_fn(f"\nWriting {output_file} ... done.")
    print_fn("Run `cstylecheck src/` to check your first files.")
    return 0


def run_preset(preset_name: str, output_path: str | None = None,
               print_fn=print, overwrite: bool = False) -> int:
    """Write a preset config without interactive prompts.  Returns 0 on success."""
    if preset_name not in PRESETS:
        print_fn(f"Unknown preset '{preset_name}'. "
                 f"Available: {', '.join(PRESETS)}")
        return 1

    output_file = Path(output_path or ".cstylecheck.yml")
    if output_file.exists() and not overwrite:
        print_fn(f"'{output_file}' already exists. Use --overwrite to replace it.")
        return 1

    yaml_text = _render_yaml(PRESETS[preset_name], preset_name=preset_name)
    output_file.write_text(yaml_text, encoding="utf-8")
    print_fn(f"Wrote {preset_name} preset to {output_file}")
    print_fn("Run `cstylecheck src/` to check your first files.")
    return 0
