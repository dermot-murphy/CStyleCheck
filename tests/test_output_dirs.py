"""test_output_dirs.py — missing parent folders of output files are created
(issue #441).

Covers:
  SWE1-062  --log FILE: the parent folder of the log file, and any missing
            folders above it, are created before the file is opened
            (UV-OUT-001).
  SWE1-065  --write-baseline FILE: write_baseline() creates the missing
            parent folders (UV-OUT-002).
  SWE1-075  --init / --preset with --init-output FILE: the wizard and the
            preset writer create the missing parent folders (UV-OUT-003).
  SWE1-062, SWE1-065, SWE1-075 (negative): a parent folder that cannot be
            created (a path component is an existing file) is a
            configuration error — exit 2, message names the path, no
            traceback (UV-OUT-004).
"""
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

sys.path.insert(0, os.path.dirname(__file__))
from harness import run_wizard, run_preset  # noqa: E402

import cstylecheck as _mod  # noqa: E402
from cstylecheck.baseline import write_baseline  # noqa: E402
from cstylecheck.models import Violation  # noqa: E402

_HERE = Path(__file__).resolve().parent
_CHECKER = str(_HERE.parent / "src" / "cstylecheck.py")
_YAML = str(_HERE / "rules.yml")


def _run_main(*argv):
    """Run cli.main() in-process; return (rc, stdout, stderr)."""
    out, err = io.StringIO(), io.StringIO()
    with mock.patch.object(sys, "argv", ["cstylecheck", *argv]), \
            redirect_stdout(out), redirect_stderr(err):
        rc = _mod.main()
    return rc, out.getvalue(), err.getvalue()


def _write_src(td):
    p = Path(td) / "main.c"
    p.write_text("\tvoid f(void){}\n", encoding="utf-8")
    return str(p)


class TestLogFolderCreated(unittest.TestCase):
    """UV-OUT-001 (SWE1-062)."""

    def test_log_nested_missing_folders_created(self):
        with tempfile.TemporaryDirectory() as td:
            src = _write_src(td)
            log = Path(td) / "out" / "a" / "b" / "results.log"
            rc, out, _ = _run_main("--config", _YAML, "--log", str(log), src)
            self.assertEqual(rc, 0)
            self.assertTrue(log.is_file())
            self.assertIn("main.c:1:", log.read_text(encoding="utf-8"))
            self.assertIn("main.c:1:", out)

    def test_log_existing_folder_unchanged_behaviour(self):
        with tempfile.TemporaryDirectory() as td:
            src = _write_src(td)
            log = Path(td) / "results.log"
            rc, _, _ = _run_main("--config", _YAML, "--log", str(log), src)
            self.assertEqual(rc, 0)
            self.assertTrue(log.is_file())

    def test_log_relative_path_in_cwd(self):
        """A bare file name (parent '.') needs no folder and still works."""
        with tempfile.TemporaryDirectory() as td:
            src = _write_src(td)
            old = os.getcwd()
            os.chdir(td)
            try:
                rc, _, _ = _run_main("--config", _YAML,
                                     "--log", "results.log", src)
            finally:
                os.chdir(old)
            self.assertEqual(rc, 0)
            self.assertTrue((Path(td) / "results.log").is_file())


class TestBaselineFolderCreated(unittest.TestCase):
    """UV-OUT-002 (SWE1-065)."""

    def test_write_baseline_function_creates_folders(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "base" / "line" / "baseline.json"
            v = Violation("src/main.c", 1, 1, "error", "misc.indentation",
                          "Tab used for indentation")
            write_baseline([v], str(path))
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(len(data["violations"]), 1)

    def test_write_baseline_cli_creates_folders(self):
        with tempfile.TemporaryDirectory() as td:
            src = _write_src(td)
            path = Path(td) / "ci" / "baseline.json"
            rc, _, _ = _run_main("--config", _YAML,
                                 "--write-baseline", str(path), src)
            self.assertEqual(rc, 0)
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertIsInstance(data["violations"], list)


class TestConfigOutputFolderCreated(unittest.TestCase):
    """UV-OUT-003 (SWE1-075)."""

    def test_preset_creates_folders(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "cfg" / "nested" / ".cstylecheck.yml"
            rc = run_preset("minimal", output_path=str(out),
                            print_fn=lambda *a, **k: None)
            self.assertEqual(rc, 0)
            self.assertTrue(out.is_file())

    def test_wizard_creates_folders(self):
        answers = iter([""] * 40)
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "cfg" / ".cstylecheck.yml"
            rc = run_wizard(output_path=str(out),
                            prompt_fn=lambda _p: next(answers),
                            print_fn=lambda *a, **k: None)
            self.assertEqual(rc, 0)
            self.assertTrue(out.is_file())

    def test_preset_cli_init_output_creates_folders(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "cfg" / "barr.yml"
            rc, _, _ = _run_main("--preset", "barr-c",
                                 "--init-output", str(out))
            self.assertEqual(rc, 0)
            self.assertTrue(out.is_file())


class TestUncreatableFolder(unittest.TestCase):
    """UV-OUT-004 (negative: SWE1-062, SWE1-065, SWE1-075)."""

    def _blocked(self, td):
        """Return a path whose parent 'blocker' is an existing file."""
        blocker = Path(td) / "blocker"
        blocker.write_text("x", encoding="utf-8")
        return blocker / "sub" / "file.out"

    def _run_cli(self, *argv):
        return subprocess.run([sys.executable, _CHECKER, *argv],
                              capture_output=True, text=True)

    def test_log_uncreatable_folder_exits_2(self):
        with tempfile.TemporaryDirectory() as td:
            src = _write_src(td)
            bad = self._blocked(td)
            r = self._run_cli("--config", _YAML, "--log", str(bad), src)
        self.assertEqual(r.returncode, 2)
        self.assertIn("Cannot open log file", r.stderr)
        self.assertIn(str(bad), r.stderr)
        self.assertNotIn("Traceback", r.stderr)

    def test_baseline_uncreatable_folder_exits_2(self):
        with tempfile.TemporaryDirectory() as td:
            src = _write_src(td)
            bad = self._blocked(td)
            r = self._run_cli("--config", _YAML,
                              "--write-baseline", str(bad), src)
        self.assertEqual(r.returncode, 2)
        self.assertIn("Cannot write baseline file", r.stderr)
        self.assertNotIn("Traceback", r.stderr)

    def test_preset_uncreatable_folder_exits_2(self):
        with tempfile.TemporaryDirectory() as td:
            bad = self._blocked(td)
            r = self._run_cli("--preset", "minimal", "--init-output", str(bad))
        self.assertEqual(r.returncode, 2)
        self.assertIn("Cannot write config file", r.stderr)
        self.assertNotIn("Traceback", r.stderr)


if __name__ == "__main__":
    unittest.main()
