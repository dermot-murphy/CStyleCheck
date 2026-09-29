"""test_init_wizard.py — Tests for --init wizard and --preset (issue #190)."""
import sys
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from harness import run_wizard, run_preset, PRESETS  # noqa: E402

_HERE    = Path(__file__).resolve().parent
_SRC     = _HERE.parent / "src"
_CHECKER = str(_SRC / "cstylecheck.py")


def _cli(*args):
    r = subprocess.run(
        [sys.executable, _CHECKER, *args],
        capture_output=True, text=True,
    )
    return r.returncode, r.stdout + r.stderr


# ---------------------------------------------------------------------------
class TestRunPreset(unittest.TestCase):

    def test_barr_c_writes_file(self):
        with tempfile.TemporaryDirectory() as td:
            out = str(Path(td) / "out.yml")
            rc = run_preset("barr-c", output_path=out)
            self.assertEqual(rc, 0)
            content = Path(out).read_text()
            self.assertIn("lower_snake", content)
            self.assertIn("g_prefix", content)

    def test_minimal_writes_file(self):
        with tempfile.TemporaryDirectory() as td:
            out = str(Path(td) / "out.yml")
            rc = run_preset("minimal", output_path=out)
            self.assertEqual(rc, 0)
            content = Path(out).read_text()
            self.assertIn("magic_numbers", content)

    def test_misra_writes_file(self):
        with tempfile.TemporaryDirectory() as td:
            out = str(Path(td) / "out.yml")
            rc = run_preset("misra", output_path=out)
            self.assertEqual(rc, 0)
            content = Path(out).read_text()
            self.assertIn("unsigned_suffix", content)
            self.assertIn("octal_constant", content)

    def test_unknown_preset_returns_1(self):
        with tempfile.TemporaryDirectory() as td:
            out = str(Path(td) / "out.yml")
            msgs = []
            rc = run_preset("nonexistent", output_path=out,
                            print_fn=msgs.append)
            self.assertEqual(rc, 1)

    def test_existing_file_not_overwritten_without_flag(self):
        with tempfile.TemporaryDirectory() as td:
            out = str(Path(td) / "out.yml")
            Path(out).write_text("existing")
            rc = run_preset("minimal", output_path=out)
            self.assertEqual(rc, 1)
            self.assertEqual(Path(out).read_text(), "existing")

    def test_overwrite_flag_replaces_file(self):
        with tempfile.TemporaryDirectory() as td:
            out = str(Path(td) / "out.yml")
            Path(out).write_text("old")
            rc = run_preset("minimal", output_path=out, overwrite=True)
            self.assertEqual(rc, 0)
            self.assertNotEqual(Path(out).read_text(), "old")

    def test_all_presets_produce_valid_yaml(self):
        import yaml
        for name in PRESETS:
            with tempfile.TemporaryDirectory() as td:
                out = str(Path(td) / "out.yml")
                run_preset(name, output_path=out)
                data = yaml.safe_load(Path(out).read_text())
                self.assertIsInstance(data, dict, f"preset {name} produced invalid YAML")

    def test_output_contains_header_comment(self):
        with tempfile.TemporaryDirectory() as td:
            out = str(Path(td) / "out.yml")
            run_preset("minimal", output_path=out)
            content = Path(out).read_text()
            self.assertIn("# CStyleCheck configuration", content)
            self.assertIn("--preset minimal", content)


# ---------------------------------------------------------------------------
class TestRunWizard(unittest.TestCase):

    def _answers(self, *responses):
        """Return a prompt_fn that yields pre-canned responses."""
        it = iter(responses)
        def _prompt(msg):
            try:
                return next(it)
            except StopIteration:
                return ""
        return _prompt

    def test_wizard_writes_file_with_defaults(self):
        with tempfile.TemporaryDirectory() as td:
            out = str(Path(td) / "out.yml")
            # All defaults: just press Enter to every question
            rc = run_wizard(output_path=out,
                            prompt_fn=self._answers(*[""] * 20))
            self.assertEqual(rc, 0)
            self.assertTrue(Path(out).exists())

    def test_wizard_respects_var_case_choice(self):
        import yaml
        with tempfile.TemporaryDirectory() as td:
            out = str(Path(td) / "out.yml")
            # Answer camelCase for the first question, defaults for rest
            rc = run_wizard(output_path=out,
                            prompt_fn=self._answers("camelCase", *[""] * 20))
            self.assertEqual(rc, 0)
            data = yaml.safe_load(Path(out).read_text())
            # The on-screen label camelCase is stored as canonical "camel" (#422)
            self.assertEqual(data["variables"]["case"], "camel")

    def test_wizard_aborts_if_file_exists_and_user_says_no(self):
        with tempfile.TemporaryDirectory() as td:
            out = str(Path(td) / "out.yml")
            Path(out).write_text("original")
            msgs = []
            rc = run_wizard(output_path=out,
                            prompt_fn=self._answers("n", *[""] * 20),
                            print_fn=msgs.append)
            self.assertEqual(rc, 1)
            self.assertEqual(Path(out).read_text(), "original")

    def test_wizard_overwrites_if_user_confirms(self):
        with tempfile.TemporaryDirectory() as td:
            out = str(Path(td) / "out.yml")
            Path(out).write_text("original")
            rc = run_wizard(output_path=out,
                            prompt_fn=self._answers("y", *[""] * 20))
            self.assertEqual(rc, 0)
            self.assertNotEqual(Path(out).read_text(), "original")

    def test_wizard_overwrite_flag_skips_prompt(self):
        with tempfile.TemporaryDirectory() as td:
            out = str(Path(td) / "out.yml")
            Path(out).write_text("original")
            rc = run_wizard(output_path=out, overwrite=True,
                            prompt_fn=self._answers(*[""] * 20))
            self.assertEqual(rc, 0)
            self.assertNotEqual(Path(out).read_text(), "original")


# ---------------------------------------------------------------------------
class TestCLIInit(unittest.TestCase):

    def test_preset_cli_writes_file(self):
        with tempfile.TemporaryDirectory() as td:
            out = str(Path(td) / "out.yml")
            rc, out_text = _cli("--preset", "minimal",
                                "--init-output", out, "--overwrite")
            self.assertEqual(rc, 0)
            self.assertTrue(Path(out).exists())

    def test_preset_help_lists_presets(self):
        rc, out_text = _cli("--help")
        self.assertEqual(rc, 0)
        self.assertIn("barr-c", out_text)
        self.assertIn("minimal", out_text)
        self.assertIn("misra", out_text)


# ---------------------------------------------------------------------------
# Issue #420 — presets / --init wizard enable the standard-specific opt-in
# (#418) rules.
# ---------------------------------------------------------------------------

_OPT_IN_RULES = (
    "goto_usage", "assignment_in_condition", "multiple_statements_per_line",
    "void_pointer", "recursive_function", "sizeof_type",
    "boolean_comparison", "empty_else",
)
_MISRA_RULES  = {"goto_usage", "assignment_in_condition", "void_pointer",
                 "recursive_function", "empty_else"}
_BARR_C_RULES = {"multiple_statements_per_line", "sizeof_type", "empty_else"}

# One snippet that triggers every opt-in rule when it is enabled.
_TRIGGER_SRC = """\
#include <stdint.h>
#include <stdbool.h>
static int fact(int n)
{
    int x = 0; int y = 1;
    void *p = 0;
    if (x = n) { x = 1; }
    if (n == true) { x = 2; } else {}
    x = (int)sizeof(uint32_t);
    goto done;
done:
    return n * fact(n - 1);
}
"""


def _shipped_severity(rule):
    import yaml
    data = yaml.safe_load((_SRC / "rules.yml").read_text(encoding="utf-8"))
    return data["misc"][rule]["severity"]


def _enabled_opt_in(cfg):
    misc = cfg.get("misc", {})
    return {r for r in _OPT_IN_RULES if misc.get(r, {}).get("enabled", False)}


def _preset_cfg(name):
    import yaml
    with tempfile.TemporaryDirectory() as td:
        out = str(Path(td) / "out.yml")
        assert run_preset(name, output_path=out, print_fn=lambda *_: None) == 0
        return yaml.safe_load(Path(out).read_text(encoding="utf-8"))


def _fired_opt_in(cfg):
    from harness import rules
    return {r.split(".", 1)[1] for r in rules(_TRIGGER_SRC, cfg)
            if r.startswith("misc.") and r.split(".", 1)[1] in _OPT_IN_RULES}


class TestPresetOptInRules(unittest.TestCase):
    """#420: preset contents for the opt-in (#418) rules."""

    def test_misra_enables_exactly_five_rules(self):
        self.assertEqual(_enabled_opt_in(_preset_cfg("misra")), _MISRA_RULES)

    def test_barr_c_enables_exactly_three_rules(self):
        self.assertEqual(_enabled_opt_in(_preset_cfg("barr-c")), _BARR_C_RULES)

    def test_minimal_enables_none(self):
        self.assertEqual(_enabled_opt_in(_preset_cfg("minimal")), set())

    def test_boolean_comparison_in_no_preset(self):
        for name in PRESETS:
            self.assertNotIn("boolean_comparison",
                             _preset_cfg(name).get("misc", {}), name)

    def test_enabled_rules_carry_shipped_severity(self):
        for name in ("misra", "barr-c"):
            misc = _preset_cfg(name)["misc"]
            for rule in _enabled_opt_in({"misc": misc}):
                self.assertIs(misc[rule]["enabled"], True)
                self.assertEqual(misc[rule]["severity"],
                                 _shipped_severity(rule), f"{name}:{rule}")

    def test_preset_output_is_deterministic(self):
        for name in PRESETS:
            with tempfile.TemporaryDirectory() as td:
                a, b = Path(td) / "a.yml", Path(td) / "b.yml"
                run_preset(name, output_path=str(a), print_fn=lambda *_: None)
                run_preset(name, output_path=str(b), print_fn=lambda *_: None)
                self.assertEqual(a.read_text(), b.read_text(), name)

    def test_yaml_lists_rules_with_enabled_true_and_severity(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "out.yml"
            run_preset("misra", output_path=str(out), print_fn=lambda *_: None)
            text = out.read_text()
            self.assertIn("  goto_usage:\n    enabled: true\n    severity: error\n",
                          text)

    def test_checker_fires_exactly_the_enabled_rules(self):
        expected = {"misra": _MISRA_RULES, "barr-c": _BARR_C_RULES,
                    "minimal": set()}
        for name, want in expected.items():
            with self.subTest(preset=name):
                self.assertEqual(_fired_opt_in(_preset_cfg(name)), want)

    def test_cli_with_generated_config_fires_enabled_rules(self):
        expected = {"misra": _MISRA_RULES, "barr-c": _BARR_C_RULES,
                    "minimal": set()}
        for name, want in expected.items():
            with self.subTest(preset=name), tempfile.TemporaryDirectory() as td:
                cfg = str(Path(td) / "cfg.yml")
                src = Path(td) / "test_module.c"
                src.write_text(_TRIGGER_SRC, encoding="utf-8")
                rc, _ = _cli("--preset", name, "--init-output", cfg)
                self.assertEqual(rc, 0)
                _, out = _cli("--config", cfg, str(src))
                self.assertNotIn("Traceback", out)
                fired = {r for r in _OPT_IN_RULES if f"[misc.{r}]" in out}
                self.assertEqual(fired, want)


class TestWizardOptInRules(unittest.TestCase):
    """#420: --init wizard MISRA / Barr-C opt-in rule prompts."""

    # Answers to the 8 questions that precede the #420 prompts.
    _PRE = [""] * 8

    def _run(self, *answers, eof_after=None):
        import yaml
        prompts = []
        it = iter(answers)

        def _prompt(msg):
            prompts.append(msg)
            if eof_after is not None and len(prompts) > eof_after:
                raise EOFError
            try:
                return next(it)
            except StopIteration:
                return ""
        with tempfile.TemporaryDirectory() as td:
            out = str(Path(td) / "out.yml")
            rc = run_wizard(output_path=out, prompt_fn=_prompt,
                            print_fn=lambda *_: None)
            self.assertEqual(rc, 0)
            return yaml.safe_load(Path(out).read_text()), prompts

    def test_prompts_are_asked_last_with_default_no(self):
        _, prompts = self._run()
        self.assertEqual(len(prompts), 10)
        self.assertIn("Enable MISRA C:2012 rules", prompts[8])
        self.assertIn("15.1", prompts[8])
        self.assertTrue(prompts[8].endswith("[y/N]: "))
        self.assertIn("Enable Barr-C rules", prompts[9])
        self.assertIn("§3.2", prompts[9])
        self.assertTrue(prompts[9].endswith("[y/N]: "))

    def test_defaults_enable_none(self):
        cfg, _ = self._run()
        self.assertEqual(_enabled_opt_in(cfg), set())

    def test_explicit_no_enables_none(self):
        cfg, _ = self._run(*self._PRE, "n", "N")
        self.assertEqual(_enabled_opt_in(cfg), set())

    def test_eof_keeps_default_no(self):
        cfg, _ = self._run(eof_after=0)
        self.assertEqual(_enabled_opt_in(cfg), set())

    def test_yes_to_misra_enables_misra_rules(self):
        cfg, _ = self._run(*self._PRE, "y", "")
        self.assertEqual(_enabled_opt_in(cfg), _MISRA_RULES)

    def test_yes_to_barr_c_enables_barr_c_rules(self):
        cfg, _ = self._run(*self._PRE, "", "y")
        self.assertEqual(_enabled_opt_in(cfg), _BARR_C_RULES)

    def test_yes_to_both_enables_union(self):
        cfg, _ = self._run(*self._PRE, "y", "yes")
        self.assertEqual(_enabled_opt_in(cfg), _MISRA_RULES | _BARR_C_RULES)

    def test_rules_listed_with_shipped_severity(self):
        cfg, _ = self._run()
        misc = cfg["misc"]
        for rule in _MISRA_RULES | _BARR_C_RULES:
            self.assertIn(rule, misc)
            self.assertEqual(misc[rule]["severity"], _shipped_severity(rule))
        self.assertNotIn("boolean_comparison", misc)

    def test_wizard_config_fires_enabled_rules(self):
        cfg, _ = self._run(*self._PRE, "y", "y")
        self.assertEqual(_fired_opt_in(cfg), _MISRA_RULES | _BARR_C_RULES)
        cfg, _ = self._run()
        self.assertEqual(_fired_opt_in(cfg), set())


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    unittest.main()
