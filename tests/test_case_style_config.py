"""test_case_style_config.py — case-style names in configs (issue #422).

Presets and the --init wizard must write canonical case-style names (keys of
``_CASE_PATTERNS``); aliases such as ``PascalCase`` / ``UPPER_SNAKE`` are
normalised at config load; an unknown case style is a config error (exit 2)
naming the key and the allowed values.  Before #422 an unknown style made
``matches_case`` return True, so naming checks silently passed.
"""
import re
import subprocess
import sys
import os
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))

import yaml  # noqa: E402

from harness import run_preset, run_wizard, PRESETS, rules  # noqa: E402
from cstylecheck import (  # noqa: E402
    _CASE_PATTERNS, _CASE_STYLE_KEYS, WIZARD_CASE_CHOICES,
    load_config, matches_case, normalize_case_style, validate_case_styles,
)

_HERE    = Path(__file__).resolve().parent
_ROOT    = _HERE.parent
_SRC     = _ROOT / "src"
_CHECKER = str(_SRC / "cstylecheck.py")

# Source whose typedef, enum type and enum member are wrongly cased for the
# barr-c preset (lower_snake types with _t, upper_snake members).
_BAD_NAMES_SRC = """\
typedef unsigned int UartCount_t;

typedef enum
{
    uart_state_idle,
    UART_STATE_BUSY
} UartState_t;
"""


def _cli(*args):
    r = subprocess.run([sys.executable, _CHECKER, *args],
                       capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def _case_values(cfg):
    """Yield (dotted_key, value) for every case-style key present in *cfg*."""
    for path in _CASE_STYLE_KEYS:
        node = cfg
        for k in path:
            node = node.get(k) if isinstance(node, dict) else None
        if node is not None:
            yield ".".join(path), node


def _all_case_keys(node, prefix=""):
    """Yield (dotted_key, value) for every key named 'case' or '*_case'."""
    if isinstance(node, dict):
        for k, v in node.items():
            key = f"{prefix}.{k}" if prefix else str(k)
            if isinstance(v, dict):
                yield from _all_case_keys(v, key)
            elif str(k) == "case" or str(k).endswith("_case"):
                yield key, v


def _preset_yaml(name):
    with tempfile.TemporaryDirectory() as td:
        out = str(Path(td) / "out.yml")
        assert run_preset(name, output_path=out, print_fn=lambda *_: None) == 0
        return yaml.safe_load(Path(out).read_text(encoding="utf-8"))


def _wizard_yaml(first_answer):
    answers = iter([first_answer])

    def _prompt(_msg):
        return next(answers, "")
    with tempfile.TemporaryDirectory() as td:
        out = str(Path(td) / "out.yml")
        assert run_wizard(output_path=out, prompt_fn=_prompt,
                          print_fn=lambda *_: None) == 0
        return yaml.safe_load(Path(out).read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
class TestGeneratedConfigsUseCanonicalNames(unittest.TestCase):
    """UV-CASE-001: presets and wizard write only _CASE_PATTERNS keys."""

    _NON_NAMING = {"file_prefix.case"}   # module-name case: lower|upper|as_is

    def test_every_preset_case_value_is_canonical(self):
        for name in PRESETS:
            cfg = _preset_yaml(name)
            found = [(k, v) for k, v in _all_case_keys(cfg)
                     if k not in self._NON_NAMING]
            with self.subTest(preset=name):
                self.assertTrue(found, name)
                for key, value in found:
                    self.assertIn(value, _CASE_PATTERNS, f"{name}: {key}")

    def test_misra_barr_c_minimal_all_covered(self):
        self.assertEqual(set(PRESETS), {"misra", "barr-c", "minimal"})

    def test_barr_c_preset_type_and_member_cases(self):
        cfg = _preset_yaml("barr-c")
        self.assertEqual(cfg["typedefs"]["case"], "lower_snake")
        self.assertEqual(cfg["enums"]["type_case"], "lower_snake")
        self.assertEqual(cfg["enums"]["member_case"], "upper_snake")

    def test_every_wizard_choice_writes_canonical_case(self):
        for label, canon in WIZARD_CASE_CHOICES.items():
            cfg = _wizard_yaml(label)
            with self.subTest(choice=label):
                self.assertEqual(cfg["variables"]["case"], canon)
                self.assertEqual(cfg["functions"]["case"], canon)
                for key, value in _all_case_keys(cfg):
                    if key not in self._NON_NAMING:
                        self.assertIn(value, _CASE_PATTERNS, key)

    def test_wizard_choice_labels_and_order_unchanged(self):
        self.assertEqual(list(WIZARD_CASE_CHOICES),
                         ["lower_snake", "camelCase", "PascalCase"])

    def test_wizard_prefix_answer_still_accepted(self):
        self.assertEqual(_wizard_yaml("pas")["variables"]["case"], "pascal")
        self.assertEqual(_wizard_yaml("c")["variables"]["case"], "camel")

    def test_generated_configs_validate_cleanly(self):
        cfgs = {f"preset {n}": _preset_yaml(n) for n in PRESETS}
        cfgs.update({f"wizard {c}": _wizard_yaml(c) for c in WIZARD_CASE_CHOICES})
        for label, cfg in cfgs.items():
            with self.subTest(config=label):
                self.assertEqual(validate_case_styles(cfg, label), [])


# ---------------------------------------------------------------------------
class TestAliasNormalisation(unittest.TestCase):
    """UV-CASE-002: aliases map to canonical names, case-insensitively."""

    _ALIASES = {
        "pascal":        ["PascalCase", "Pascal", "pascal_case", "PASCALCASE", "pascal"],
        "camel":         ["camelCase", "camel_case", "CamelCase", "camel"],
        "upper_snake":   ["UPPER_SNAKE", "UPPER_SNAKE_CASE", "SCREAMING_SNAKE",
                          "SCREAMING_SNAKE_CASE", "upper_snake"],
        "lower_snake":   ["snake_case", "lower_snake_case", "snake", "Lower_Snake"],
    }

    def test_each_alias_normalises(self):
        for canon, aliases in self._ALIASES.items():
            for alias in aliases:
                with self.subTest(alias=alias):
                    self.assertEqual(normalize_case_style(alias), canon)

    def test_lower_and_upper_stay_distinct_styles(self):
        # 'lower' / 'upper' are canonical no-underscore styles (#74), not
        # aliases of lower_snake / upper_snake.
        self.assertEqual(normalize_case_style("lower"), "lower")
        self.assertEqual(normalize_case_style("UPPER"), "upper")

    def test_unknown_returned_unchanged(self):
        self.assertEqual(normalize_case_style("kebab"), "kebab")

    def test_matches_case_accepts_aliases(self):
        self.assertTrue(matches_case("UartConfig", "PascalCase"))
        self.assertFalse(matches_case("uart_config", "PascalCase"))
        self.assertTrue(matches_case("UART_OK", "SCREAMING_SNAKE_CASE"))
        self.assertFalse(matches_case("uartOk", "UPPER_SNAKE"))

    def test_matches_case_unknown_style_raises(self):
        with self.assertRaises(ValueError):
            matches_case("anything", "PascalCaes")

    def test_validate_normalises_in_place(self):
        cfg = {"typedefs": {"case": "PascalCase"},
               "enums": {"type_case": "camelCase", "member_case": "UPPER_SNAKE"},
               "variables": {"case": "snake_case", "local": {"case": "Camel"}},
               "functions": {"style": "Snake_Case"}}
        self.assertEqual(validate_case_styles(cfg), [])
        self.assertEqual(cfg["typedefs"]["case"], "pascal")
        self.assertEqual(cfg["enums"]["type_case"], "camel")
        self.assertEqual(cfg["enums"]["member_case"], "upper_snake")
        self.assertEqual(cfg["variables"]["case"], "lower_snake")
        self.assertEqual(cfg["variables"]["local"]["case"], "camel")
        self.assertEqual(cfg["functions"]["style"], "lower_snake")

    def test_load_config_normalises_aliases(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "cfg.yml"
            p.write_text("structs:\n  tag_case: PascalCase\n"
                         "  member_case: camelCase\n", encoding="utf-8")
            cfg = load_config(str(p))
        self.assertEqual(cfg["structs"], {"tag_case": "pascal",
                                          "member_case": "camel"})


# ---------------------------------------------------------------------------
class TestUnknownCaseStyleIsConfigError(unittest.TestCase):
    """UV-CASE-003: unknown style -> exit 2 naming the key and allowed values."""

    def test_every_case_key_rejects_unknown(self):
        for path in _CASE_STYLE_KEYS:
            cfg: dict = {}
            node = cfg
            for k in path[:-1]:
                node = node.setdefault(k, {})
            node[path[-1]] = "Pascl"
            errors = validate_case_styles(cfg, "cfg.yml")
            with self.subTest(key=".".join(path)):
                self.assertEqual(len(errors), 1)
                self.assertIn(f"'{'.'.join(path)}'", errors[0])
                self.assertIn("'Pascl'", errors[0])
                self.assertIn("lower_snake, upper_snake, camel, pascal", errors[0])

    def test_non_naming_style_keys_rejected(self):
        cfg = {"functions": {"style": "objectverb"},
               "file_prefix": {"case": "titlecase"},
               "misc": {"eof_comment": {"filename_case": "keep"}}}
        errors = validate_case_styles(cfg, "cfg.yml")
        self.assertEqual(len(errors), 3)
        self.assertIn("'functions.style'", errors[0])
        self.assertIn("object_verb, verb_object, lower_snake, any", errors[0])
        self.assertIn("'file_prefix.case'", errors[1])
        self.assertIn("'misc.eof_comment.filename_case'", errors[2])

    def test_non_string_value_rejected(self):
        errors = validate_case_styles({"typedefs": {"case": 3}}, "cfg.yml")
        self.assertEqual(len(errors), 1)

    def test_load_config_exits_2(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "cfg.yml"
            p.write_text("enums:\n  member_case: SHOUTY\n", encoding="utf-8")
            with self.assertRaises(SystemExit) as cm:
                load_config(str(p))
        self.assertEqual(cm.exception.code, 2)

    def test_cli_exit_2_with_key_in_message(self):
        with tempfile.TemporaryDirectory() as td:
            cfg = Path(td) / "cfg.yml"
            cfg.write_text("typedefs:\n  case: PascalCaes\n", encoding="utf-8")
            src = Path(td) / "mod.c"
            src.write_text("int mod_x;\n", encoding="utf-8")
            rc, out = _cli("--config", str(cfg), str(src))
        self.assertEqual(rc, 2)
        self.assertIn("'typedefs.case'", out)
        self.assertIn("PascalCaes", out)
        self.assertIn("allowed:", out)
        self.assertNotIn("Traceback", out)

    def test_per_dir_config_unknown_style_exits_2(self):
        with tempfile.TemporaryDirectory() as td:
            sub = Path(td) / "sub"
            sub.mkdir()
            (sub / ".cstylecheck.yml").write_text(
                "root: true\nvariables:\n  case: kebab\n", encoding="utf-8")
            src = sub / "mod.c"
            src.write_text("int mod_x;\n", encoding="utf-8")
            rc, out = _cli("--config", str(_SRC / "rules.yml"),
                           "--per-dir-config", str(src))
        self.assertEqual(rc, 2)
        self.assertIn("'variables.case'", out)


# ---------------------------------------------------------------------------
class TestRepoConfigsValidate(unittest.TestCase):
    """UV-CASE-004: repo-owned configs and doc YAML snippets are valid."""

    def _assert_valid(self, path):
        cfg = yaml.safe_load(path.read_text(encoding="utf-8"))
        self.assertEqual(validate_case_styles(cfg, str(path)), [])

    def test_shipped_rules_yml(self):
        self._assert_valid(_SRC / "rules.yml")

    def test_tests_rules_yml(self):
        self._assert_valid(_HERE / "rules.yml")

    def test_example_configs(self):
        found = sorted((_ROOT / "examples").rglob("config/*.yml"))
        self.assertTrue(found)
        for path in found:
            with self.subTest(config=path.name):
                self._assert_valid(path)

    def test_doc_yaml_snippets(self):
        for doc in ("README.md", "Rules-and-Configuration.md"):
            text = (_ROOT / doc).read_text(encoding="utf-8")
            for i, block in enumerate(
                    re.findall(r"```ya?ml\n(.*?)```", text, re.DOTALL)):
                try:
                    cfg = yaml.safe_load(block)
                except yaml.YAMLError:
                    continue   # illustrative fragment, not a config
                with self.subTest(doc=doc, block=i):
                    self.assertEqual(validate_case_styles(cfg, doc), [])


# ---------------------------------------------------------------------------
class TestGeneratedConfigReportsWrongCase(unittest.TestCase):
    """UV-CASE-005: end to end — findings that silently passed before #422."""

    _EXPECTED = {"typedef.case", "enum.type_case", "enum.member_case"}

    def test_barr_c_preset_via_cli(self):
        with tempfile.TemporaryDirectory() as td:
            cfg = str(Path(td) / "cfg.yml")
            rc, _ = _cli("--preset", "barr-c", "--init-output", cfg)
            self.assertEqual(rc, 0)
            src = Path(td) / "uart.c"
            src.write_text(_BAD_NAMES_SRC, encoding="utf-8")
            rc, out = _cli("--config", cfg, str(src))
        self.assertNotIn("Traceback", out)
        for rule in self._EXPECTED:
            self.assertIn(f"[{rule}]", out, rule)
        self.assertIn("UartCount_t", out)
        self.assertIn("uart_state_idle", out)
        self.assertEqual(rc, 1)

    def test_barr_c_preset_correct_names_pass(self):
        good = ("typedef unsigned int uart_count_t;\n\n"
                "typedef enum\n{\n    UART_STATE_IDLE,\n"
                "    UART_STATE_BUSY\n} uart_state_t;\n")
        found = rules(good, _preset_yaml("barr-c"), filepath="uart.c")
        self.assertFalse(self._EXPECTED & set(found), found)

    def test_legacy_alias_config_now_reports(self):
        # The pre-#422 barr-c preset spelling: PascalCase / UPPER_SNAKE were
        # unknown and silently passed; now they normalise and are enforced.
        with tempfile.TemporaryDirectory() as td:
            cfg = Path(td) / "cfg.yml"
            cfg.write_text(
                "typedefs:\n  enabled: true\n  severity: error\n"
                "  case: PascalCase\n"
                "enums:\n  enabled: true\n  severity: error\n"
                "  type_case: PascalCase\n  member_case: UPPER_SNAKE\n",
                encoding="utf-8")
            src = Path(td) / "uart.c"
            src.write_text("typedef unsigned int uart_count;\n"
                           "typedef enum\n{\n    uartIdle,\n    UART_BUSY\n} uart_state;\n",
                           encoding="utf-8")
            _, out = _cli("--config", str(cfg), str(src))
        for rule in self._EXPECTED:
            self.assertIn(f"[{rule}]", out, rule)
        self.assertIn("must be pascal", out)
        self.assertIn("must be upper_snake", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
