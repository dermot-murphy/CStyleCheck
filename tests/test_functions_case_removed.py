"""test_functions_case_removed.py — ``functions.case`` removed (issue #424).

``functions.case`` was written by the presets and the --init wizard and
validated as a case-style key by #422, but the checker never read it.
Function-name casing is controlled by ``functions.style``.  The key is no
longer generated; a config that still contains it loads normally (same exit
code) but prints a WARNING on stderr telling the user to use
``functions.style`` instead.
"""
import contextlib
import io
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))

import yaml  # noqa: E402

from harness import run_preset, run_wizard, PRESETS, rules  # noqa: E402
from cstylecheck import (  # noqa: E402
    _CASE_STYLE_KEYS, _DEPRECATED_KEYS, WIZARD_CASE_CHOICES,
    deprecated_key_warnings, load_config, validate_case_styles,
)
from cstylecheck import config as config_mod  # noqa: E402

_HERE    = Path(__file__).resolve().parent
_ROOT    = _HERE.parent
_SRC     = _ROOT / "src"
_CHECKER = str(_SRC / "cstylecheck.py")

_FN_CFG_WITH_CASE = (
    "functions:\n  enabled: true\n  severity: error\n"
    "  case: lower_snake\n  style: lower_snake\n")

_CLEAN_SRC = "void uart_read_byte(void)\n{\n}\n"


def _cli(*args):
    r = subprocess.run([sys.executable, _CHECKER, *args],
                       capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr


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
class TestGeneratedConfigsOmitFunctionsCase(unittest.TestCase):
    """UV-FCASE-001: presets, --init and repo configs write no functions.case."""

    def _assert_no_functions_case(self, cfg, label):
        fn = cfg.get("functions") or {}
        self.assertNotIn("case", fn, label)

    def test_presets(self):
        for name in PRESETS:
            with self.subTest(preset=name):
                self._assert_no_functions_case(_preset_yaml(name), name)

    def test_init_wizard_every_naming_choice(self):
        for label in WIZARD_CASE_CHOICES:
            with self.subTest(choice=label):
                cfg = _wizard_yaml(label)
                self.assertIn("functions", cfg)
                self._assert_no_functions_case(cfg, label)

    def test_preset_via_cli(self):
        for name in PRESETS:
            with self.subTest(preset=name), tempfile.TemporaryDirectory() as td:
                out = Path(td) / "cfg.yml"
                rc, _, _ = _cli("--preset", name, "--init-output", str(out))
                self.assertEqual(rc, 0)
                text = out.read_text(encoding="utf-8")
                self._assert_no_functions_case(yaml.safe_load(text), name)

    def test_repo_configs(self):
        paths = [_SRC / "rules.yml", _HERE / "rules.yml",
                 _ROOT / "scripts" / "metrics_rules.yml",
                 *sorted((_ROOT / "examples").rglob("config/*.yml"))]
        for path in paths:
            with self.subTest(config=str(path.relative_to(_ROOT))):
                cfg = yaml.safe_load(path.read_text(encoding="utf-8"))
                self._assert_no_functions_case(cfg, path.name)


# ---------------------------------------------------------------------------
class TestFunctionsCaseDeprecated(unittest.TestCase):
    """UV-FCASE-002: functions.case is deprecated, not a case-style key."""

    def test_not_a_case_style_key(self):
        self.assertNotIn(("functions", "case"), _CASE_STYLE_KEYS)
        self.assertIn(("functions", "object_case"), _CASE_STYLE_KEYS)
        self.assertIn(("functions", "verb_case"), _CASE_STYLE_KEYS)
        self.assertIn(("functions", "case"), _DEPRECATED_KEYS)

    def test_validate_case_styles_ignores_it(self):
        # Any value is left untouched and is not a config error.
        for value in ("lower_snake", "PascalCase", "kebab", 3):
            cfg = {"functions": {"case": value}}
            with self.subTest(value=value):
                self.assertEqual(validate_case_styles(cfg, "cfg.yml"), [])
                self.assertEqual(cfg["functions"]["case"], value)

    def test_deprecated_key_warnings_message(self):
        msgs = deprecated_key_warnings(
            {"functions": {"case": "lower_snake"}}, "cfg.yml")
        self.assertEqual(len(msgs), 1)
        self.assertIn("cfg.yml", msgs[0])
        self.assertIn("'functions.case'", msgs[0])
        self.assertIn("not used", msgs[0])
        self.assertIn("functions.style", msgs[0])

    def test_no_warning_without_the_key(self):
        for cfg in ({}, {"functions": {"style": "any"}}, {"functions": None},
                    None, {"variables": {"case": "lower_snake"}}):
            with self.subTest(cfg=cfg):
                self.assertEqual(deprecated_key_warnings(cfg), [])


# ---------------------------------------------------------------------------
class TestFunctionsCaseWarning(unittest.TestCase):
    """UV-FCASE-003: a config with functions.case warns on stderr only."""

    def test_load_config_warns_and_keeps_value(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "cfg.yml"
            path.write_text(_FN_CFG_WITH_CASE, encoding="utf-8")
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                cfg = load_config(str(path))
        self.assertEqual(cfg["functions"]["case"], "lower_snake")
        text = err.getvalue()
        self.assertIn("WARNING:", text)
        self.assertIn("'functions.case'", text)
        self.assertIn("functions.style", text)

    def test_warning_printed_once_per_source(self):
        config_mod._WARNED_DEPRECATED.clear()
        err = io.StringIO()
        cfg = {"functions": {"case": "lower_snake"}}
        with contextlib.redirect_stderr(err):
            config_mod._warn_deprecated_keys(cfg, "x.yml")
            config_mod._warn_deprecated_keys(cfg, "x.yml")
            config_mod._warn_deprecated_keys(cfg, "y.yml")
        self.assertEqual(err.getvalue().count("WARNING:"), 2)

    def test_cli_root_config_warns_exit_code_unchanged(self):
        with tempfile.TemporaryDirectory() as td:
            with_case = Path(td) / "with.yml"
            with_case.write_text(_FN_CFG_WITH_CASE, encoding="utf-8")
            without = Path(td) / "without.yml"
            without.write_text(
                _FN_CFG_WITH_CASE.replace("  case: lower_snake\n", ""),
                encoding="utf-8")
            src = Path(td) / "uart.c"
            src.write_text(_CLEAN_SRC, encoding="utf-8")
            rc_with, out_with, err_with = _cli("--config", str(with_case),
                                               str(src))
            rc_without, _, err_without = _cli("--config", str(without),
                                              str(src))
        self.assertEqual(rc_with, rc_without)
        self.assertNotIn("Traceback", err_with)
        self.assertEqual(err_with.count("WARNING:"), 1)
        self.assertIn("'functions.case'", err_with)
        self.assertIn(str(with_case), err_with)
        self.assertNotIn("'functions.case'", out_with)
        self.assertNotIn("functions.case", err_without)

    def test_cli_per_dir_config_warns_once(self):
        # One .cstylecheck.yml above two source directories is walked for
        # each directory but warns only once.
        with tempfile.TemporaryDirectory() as td:
            top = Path(td) / "proj"
            (top / "a").mkdir(parents=True)
            (top / "b").mkdir()
            (top / ".cstylecheck.yml").write_text(
                "root: true\n" + _FN_CFG_WITH_CASE, encoding="utf-8")
            (top / "a" / "uart.c").write_text(_CLEAN_SRC, encoding="utf-8")
            (top / "b" / "uart.c").write_text(_CLEAN_SRC, encoding="utf-8")
            rc, _, err = _cli("--config", str(_SRC / "rules.yml"),
                              "--per-dir-config",
                              str(top / "a" / "uart.c"),
                              str(top / "b" / "uart.c"))
        self.assertNotEqual(rc, 2)
        self.assertNotIn("Traceback", err)
        self.assertEqual(err.count("WARNING:"), 1, err)
        self.assertIn("'functions.case'", err)
        self.assertIn(".cstylecheck.yml", err)


# ---------------------------------------------------------------------------
class TestFunctionStyleStillEnforced(unittest.TestCase):
    """UV-FCASE-004: function naming is enforced by functions.style."""

    @staticmethod
    def _cfg(style, case=None):
        fn = {"enabled": True, "severity": "error", "style": style}
        if case is not None:
            fn["case"] = case
        return {"functions": fn}

    def test_lower_snake_style_flags_wrong_case(self):
        found = rules("void uart_ReadByte(void)\n{\n}\n",
                      self._cfg("lower_snake"), filepath="uart.c")
        self.assertIn("function.style", found)

    def test_lower_snake_style_passes_right_case(self):
        found = rules(_CLEAN_SRC, self._cfg("lower_snake"), filepath="uart.c")
        self.assertNotIn("function.style", found)

    def test_object_verb_style_flags_snake(self):
        found = rules(_CLEAN_SRC, self._cfg("object_verb"), filepath="uart.c")
        self.assertIn("function.style", found)

    def test_functions_case_has_no_effect(self):
        src_bad = "void uart_ReadByte(void)\n{\n}\n"
        for case in ("upper_snake", "pascal", "lower_snake"):
            with self.subTest(case=case):
                self.assertEqual(
                    rules(src_bad, self._cfg("lower_snake", case),
                          filepath="uart.c"),
                    rules(src_bad, self._cfg("lower_snake"),
                          filepath="uart.c"))
                self.assertEqual(
                    rules(_CLEAN_SRC, self._cfg("any", case),
                          filepath="uart.c"),
                    rules(_CLEAN_SRC, self._cfg("any"), filepath="uart.c"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
