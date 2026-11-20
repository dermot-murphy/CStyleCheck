"""test_exit_code_entry_points.py — config/usage errors exit 2 (issue #425).

The documented exit codes are 0 = clean, 1 = violations, 2 = config/usage
error.  Before #425 the config/usage error paths called ``sys.exit("msg")``,
which exits with code 1; only the ``src/cstylecheck.py`` wrapper converted
that to 2, so the installed ``cstylecheck`` console script (which calls
``cstylecheck:main`` directly) exited 1 and a CI job could not tell a broken
config from a run that found violations.

Each error path is run through both entry points:

* the console-script target named in ``[project.scripts]`` of pyproject.toml,
  invoked exactly as the generated script does (``sys.exit(main())``);
* the ``python src/cstylecheck.py`` wrapper.

Both must exit 2 and print the error message on stderr.
"""
import io
import os
import re
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

sys.path.insert(0, os.path.dirname(__file__))

import harness  # noqa: E402,F401  (puts src/ on sys.path)
import cstylecheck as _mod  # noqa: E402
from cstylecheck import cli as _cli  # noqa: E402
from cstylecheck.utils import config_error, EXIT_CONFIG_ERROR  # noqa: E402

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent
_SRC = _ROOT / "src"
_WRAPPER = str(_SRC / "cstylecheck.py")
_YAML = str(_HERE / "rules.yml")


def _console_script_target():
    """Return (module, function) of the ``cstylecheck`` console script."""
    text = (_ROOT / "pyproject.toml").read_text(encoding="utf-8")
    m = re.search(r'^\[project\.scripts\]\s*\ncstylecheck\s*=\s*"([^"]+)"',
                  text, re.MULTILINE)
    assert m, "cstylecheck console script not found in pyproject.toml"
    module, func = m.group(1).split(":")
    return module, func


def _run_console_script(*args, cwd=None):
    """Run the console-script entry point the way the generated script does."""
    module, func = _console_script_target()
    code = (f"import sys; sys.path.insert(0, {str(_SRC)!r}); "
            f"from {module} import {func} as _entry; "
            f"sys.argv[0] = 'cstylecheck'; sys.exit(_entry())")
    r = subprocess.run([sys.executable, "-c", code, *args],
                       capture_output=True, text=True, cwd=cwd)
    return r.returncode, r.stderr


def _run_wrapper(*args, cwd=None):
    r = subprocess.run([sys.executable, _WRAPPER, *args],
                       capture_output=True, text=True, cwd=cwd)
    return r.returncode, r.stderr


_ENTRY_POINTS = {
    "console-script": _run_console_script,
    "src/cstylecheck.py": _run_wrapper,
}


class TestConfigErrorHelper(unittest.TestCase):
    """config_error() prints to stderr and exits with code 2."""

    def test_exit_code_constant(self):
        self.assertEqual(EXIT_CONFIG_ERROR, 2)

    def test_prints_message_and_exits_two(self):
        err = io.StringIO()
        with redirect_stderr(err), self.assertRaises(SystemExit) as cm:
            config_error("Config file not found: x.yml")
        self.assertEqual(cm.exception.code, 2)
        self.assertEqual(err.getvalue(), "Config file not found: x.yml\n")


class TestMainMapsStringExitToTwo(unittest.TestCase):
    """main() converts a stray ``sys.exit("msg")`` to exit code 2."""

    def _main_with(self, side_effect):
        err = io.StringIO()
        with mock.patch.object(_cli, "_main", side_effect=side_effect), \
                redirect_stdout(io.StringIO()), redirect_stderr(err), \
                self.assertRaises(SystemExit) as cm:
            _mod.main()
        return cm.exception.code, err.getvalue()

    def test_string_exit_becomes_two(self):
        code, err = self._main_with(SystemExit("Cannot read something"))
        self.assertEqual(code, 2)
        self.assertIn("Cannot read something", err)

    def test_integer_exit_is_preserved(self):
        for value in (0, 1, 2):
            code, _ = self._main_with(SystemExit(value))
            self.assertEqual(code, value)

    def test_normal_return_is_preserved(self):
        with mock.patch.object(_cli, "_main", return_value=1):
            self.assertEqual(_mod.main(), 1)


class TestConfigErrorsExitTwoOnBothEntryPoints(unittest.TestCase):
    """Each config/usage error path exits 2 with its message on stderr."""

    @classmethod
    def setUpClass(cls):
        cls._td = tempfile.TemporaryDirectory()
        td = Path(cls._td.name)
        cls.src = td / "mod.c"
        cls.src.write_text("void mod_Init(void){ }\n", encoding="utf-8")
        cls.bad_yaml = td / "bad.yml"
        cls.bad_yaml.write_text("variables: [unclosed\n  case: : :\n",
                                encoding="utf-8")
        cls.non_utf8 = td / "latin1.yml"
        cls.non_utf8.write_bytes(b"# caf\xe9\nvariables:\n  enabled: true\n")
        cls.bad_case = td / "bad_case.yml"
        cls.bad_case.write_text("variables:\n  case: NotACase\n",
                                encoding="utf-8")
        cls.bad_baseline = td / "baseline.json"
        cls.bad_baseline.write_text("{ not json", encoding="utf-8")
        cls.no_comment = td / "copyright.txt"
        cls.no_comment.write_text("no block comment here\n", encoding="utf-8")
        cls.missing = str(td / "does_not_exist.yml")

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    def _cases(self):
        src = str(self.src)
        return {
            "missing config": (
                ["--config", self.missing, src],
                "Config file not found"),
            "malformed YAML": (
                ["--config", str(self.bad_yaml), src],
                "Cannot parse config file"),
            "non-UTF-8 config": (
                ["--config", str(self.non_utf8), src],
                "contains a non-UTF-8 byte"),
            "unknown case style": (
                ["--config", str(self.bad_case), src],
                "invalid case style 'NotACase'"),
            "bad baseline": (
                ["--config", _YAML, "--baseline-file",
                 str(self.bad_baseline), src],
                "Cannot read baseline file"),
            "missing aliases file": (
                ["--config", _YAML, "--aliases", self.missing, src],
                "Cannot read alias file"),
            "missing options file": (
                ["--options-file", self.missing, src],
                "Cannot read options file"),
            "options file without path": (
                ["--options-file"],
                "--options-file requires a path argument"),
            "copyright file without block comment": (
                ["--config", _YAML, "--copyright", str(self.no_comment), src],
                "contains no block comment"),
        }

    def test_error_paths_exit_two(self):
        for entry_name, run in _ENTRY_POINTS.items():
            for case_name, (args, message) in self._cases().items():
                with self.subTest(entry=entry_name, case=case_name):
                    rc, err = run(*args)
                    self.assertEqual(rc, 2, f"stderr was:\n{err}")
                    self.assertIn(message, err)

    def test_entry_points_agree(self):
        """Both entry points give the same exit code and stderr message."""
        args, _ = self._cases()["missing config"]
        results = {name: run(*args) for name, run in _ENTRY_POINTS.items()}
        self.assertEqual(len(set(results.values())), 1, results)

    def test_violations_still_exit_one(self):
        """Exit 1 (violations) is unchanged on both entry points."""
        with tempfile.TemporaryDirectory() as td:
            bad = Path(td) / "mod.c"
            bad.write_text("void BadFunc(void){}\n", encoding="utf-8")
            for entry_name, run in _ENTRY_POINTS.items():
                with self.subTest(entry=entry_name):
                    rc, _ = run("--config", _YAML, str(bad))
                    self.assertEqual(rc, 1)


if __name__ == "__main__":
    unittest.main()
