"""test_cli_requirements.py — dedicated unit tests for CLI requirements that
previously had no unit test (issue #407, RR-003-001, AUD9-F-004).

Covers:
  SWE1-015  each source file is read from disk exactly once per invocation and
            the cached text is shared by Checker and SignChecker
            (UV-CLI-014 to UV-CLI-016).
  SWE1-094  main() writes the two-line startup banner ("<tool> <version>",
            then the copyright line) to stderr (and the --log file), never
            to stdout, before processing begins; it is emitted even when
            stdout is piped and cannot be suppressed (UV-CLI-017 to
            UV-CLI-019).
  SWE1-096  violation paths use the OS-native separator (os.sep) in
            Violation.__str__() and the other emitted output
            (UV-CLI-020 to UV-CLI-022).

The main() tests run in-process so the read path and the output streams can be
patched.  The separator tests swap the ``os`` module seen by cli.py for one
whose ``path`` is ``ntpath`` or ``posixpath``, so both the Windows (``\\``) and
POSIX (``/``) behaviour are asserted on any host.
"""
import io
import json
import ntpath
import os
import posixpath
import subprocess
import sys
import tempfile
import types
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

sys.path.insert(0, os.path.dirname(__file__))
from harness import Checker, SignChecker, cfg_only  # noqa: E402

import cstylecheck as _mod  # noqa: E402
from cstylecheck import cli as _cli  # noqa: E402
from cstylecheck import _TOOL_NAME, _VERSION, _VERSION_STRING, _COPYRIGHT  # noqa: E402

_HERE = Path(__file__).resolve().parent
_SRC = _HERE.parent / "src"
_CHECKER = str(_SRC / "cstylecheck.py")
_YAML = str(_HERE / "rules.yml")

# Cross-file sign-compatibility fixture: the call in mod.c passes an unsigned
# literal to a signed parameter declared in mod.h.
_MOD_H = ("typedef signed char int8_t;\n"
          "void mod_Write(int8_t p_val);\n")
_MOD_C = "void mod_DoWork(void){ mod_Write(100U); }\n"
_UTIL_C = "void util_Nop(void){ }\n"


def _write(td, name, content):
    p = Path(td) / name
    p.write_text(content, encoding="utf-8")
    return p


def _run_main(*argv):
    """Run cli.main() in-process; return (rc, stdout, stderr)."""
    out, err = io.StringIO(), io.StringIO()
    with mock.patch.object(sys, "argv", ["cstylecheck", *argv]), \
            redirect_stdout(out), redirect_stderr(err):
        rc = _mod.main()
    return rc, out.getvalue(), err.getvalue()


class _ReadCounter:
    """Count disk reads of the given source files through Path.read_text and open()."""

    def __init__(self, paths):
        self.watch = {os.path.abspath(str(p)) for p in paths}
        self.counts = {p: 0 for p in self.watch}
        self._orig_read_text = Path.read_text
        self._orig_open = open

    def _hit(self, path):
        key = os.path.abspath(str(path))
        if key in self.counts:
            self.counts[key] += 1

    def __enter__(self):
        counter = self

        def read_text(self_path, *a, **kw):
            counter._hit(self_path)
            return counter._orig_read_text(self_path, *a, **kw)

        def open_(file, mode="r", *a, **kw):
            if isinstance(file, (str, os.PathLike)) and "r" in mode:
                counter._hit(file)
            return counter._orig_open(file, mode, *a, **kw)

        self._patches = [
            mock.patch.object(Path, "read_text", read_text),
            mock.patch("builtins.open", open_),
        ]
        for p in self._patches:
            p.start()
        return self

    def __exit__(self, *exc):
        for p in reversed(self._patches):
            p.stop()
        return False


# ---------------------------------------------------------------------------
# SWE1-015 — single read per file, shared by Checker and SignChecker
# ---------------------------------------------------------------------------
class TestSingleReadPerFile(unittest.TestCase):
    """UV-CLI-014 to UV-CLI-016 (SWE1-015)."""

    def _ingest_spy(self):
        ingested = []
        orig = SignChecker.ingest

        def spy(self_sc, filepath, source):
            ingested.append((filepath, source))
            return orig(self_sc, filepath, source)

        return ingested, mock.patch.object(SignChecker, "ingest", spy)

    # UV-CLI-014
    def test_each_file_read_once_with_cross_file_sign_check(self):
        with tempfile.TemporaryDirectory() as td:
            files = [_write(td, "mod.h", _MOD_H),
                     _write(td, "mod.c", _MOD_C),
                     _write(td, "util.c", _UTIL_C)]
            ingested, spy = self._ingest_spy()
            with spy, _ReadCounter(files) as rc:
                _, out, _ = _run_main("--config", _YAML, *map(str, files))
        # The cross-file check really ran and found the mod.h/mod.c mismatch.
        self.assertIn("[sign_compatibility]", out)
        self.assertEqual(sorted(rc.counts.values()), [1, 1, 1],
                         f"read counts: {rc.counts}")

    # UV-CLI-014
    def test_sign_checker_ingests_cached_text_for_every_file(self):
        with tempfile.TemporaryDirectory() as td:
            files = {_write(td, "mod.h", _MOD_H): _MOD_H,
                     _write(td, "mod.c", _MOD_C): _MOD_C}
            ingested, spy = self._ingest_spy()
            with spy:
                _run_main("--config", _YAML, *map(str, files))
        self.assertEqual(len(ingested), 2)
        by_path = {os.path.abspath(p): s for p, s in ingested}
        for path, text in files.items():
            self.assertEqual(by_path[os.path.abspath(path)], text)

    # UV-CLI-015
    def test_read_once_with_declared_not_defined_and_dry_run_fix(self):
        """The other cache consumers (declared_not_defined, --fix --dry-run)
        also use the cached text and add no further reads."""
        with tempfile.TemporaryDirectory() as td:
            cfg_text = Path(_YAML).read_text(encoding="utf-8").replace(
                "declared_not_defined:\n    enabled: false",
                "declared_not_defined:\n    enabled: true", 1)
            self.assertIn("declared_not_defined:\n    enabled: true", cfg_text)
            cfg = _write(td, "rules.yml", cfg_text)
            files = [_write(td, "mod.h", _MOD_H),
                     _write(td, "mod.c", "\t" + _MOD_C)]
            with _ReadCounter(files) as rc:
                _run_main("--config", str(cfg), "--fix", "--dry-run",
                          *map(str, files))
        self.assertEqual(list(rc.counts.values()), [1, 1],
                         f"read counts: {rc.counts}")

    # UV-CLI-015 (negative: sign check disabled)
    def test_read_once_when_sign_check_disabled(self):
        with tempfile.TemporaryDirectory() as td:
            cfg_text = Path(_YAML).read_text(encoding="utf-8").replace(
                "sign_compatibility:\n  enabled: true",
                "sign_compatibility:\n  enabled: false", 1)
            cfg = _write(td, "rules.yml", cfg_text)
            files = [_write(td, "mod.h", _MOD_H), _write(td, "mod.c", _MOD_C)]
            ingested, spy = self._ingest_spy()
            with spy, _ReadCounter(files) as rc:
                _, out, _ = _run_main("--config", str(cfg), *map(str, files))
        self.assertEqual(ingested, [])
        self.assertNotIn("[sign_compatibility]", out)
        self.assertEqual(list(rc.counts.values()), [1, 1])

    # UV-CLI-016 (negative: unreadable file)
    def test_unreadable_file_not_retried_or_ingested(self):
        with tempfile.TemporaryDirectory() as td:
            good = _write(td, "util.c", _UTIL_C)
            missing = Path(td) / "missing.c"
            ingested, spy = self._ingest_spy()
            with spy, _ReadCounter([good, missing]) as rc:
                _, out, _ = _run_main("--config", _YAML, str(good), str(missing))
        self.assertIn("ERROR: Cannot read", out)
        self.assertEqual(rc.counts[os.path.abspath(str(missing))], 1)
        self.assertEqual(rc.counts[os.path.abspath(str(good))], 1)
        self.assertEqual([os.path.abspath(p) for p, _ in ingested],
                         [os.path.abspath(str(good))])

    # UV-CLI-016 (sanity check of the counter itself)
    def test_counter_detects_a_second_read(self):
        with tempfile.TemporaryDirectory() as td:
            f = _write(td, "util.c", _UTIL_C)
            with _ReadCounter([f]) as rc:
                f.read_text(encoding="utf-8")
                with open(f, encoding="utf-8") as fh:
                    fh.read()
        self.assertEqual(rc.counts[os.path.abspath(str(f))], 2)


# ---------------------------------------------------------------------------
# SWE1-094 — startup banner on stderr
# ---------------------------------------------------------------------------
class TestStartupBanner(unittest.TestCase):
    """UV-CLI-017 to UV-CLI-019 (SWE1-094)."""

    # UV-CLI-017
    def test_banner_on_stderr_not_stdout(self):
        with tempfile.TemporaryDirectory() as td:
            src = _write(td, "main.c", "\tvoid f(void){}\n")
            r = subprocess.run(
                [sys.executable, _CHECKER, "--config", _YAML, str(src)],
                capture_output=True, text=True)
        self.assertIn(_VERSION_STRING, r.stderr)
        self.assertIn(_COPYRIGHT, r.stderr)
        self.assertNotIn(_VERSION_STRING, r.stdout)
        self.assertNotIn(_COPYRIGHT, r.stdout)
        # stdout still carries the violation report
        self.assertIn("main.c:1:", r.stdout)

    # UV-CLI-018
    def test_banner_content(self):
        with tempfile.TemporaryDirectory() as td:
            src = _write(td, "main.c", "void f(void){}\n")
            _, _, err = _run_main("--config", _YAML, str(src))
        self.assertTrue(err.startswith(_VERSION_STRING), err[:80])
        self.assertIn(_TOOL_NAME, err)
        self.assertIn(_VERSION, err)
        self.assertRegex(err, r"\(C\) \d{4} Dermot Murphy")
        self.assertEqual(_VERSION_STRING, f"{_TOOL_NAME} {_VERSION}")

    # UV-CLI-018
    def test_banner_precedes_processing(self):
        """Banner is written before discovery/scanning progress output."""
        with tempfile.TemporaryDirectory() as td:
            src = _write(td, "main.c", "void f(void){}\n")
            _, _, err = _run_main("--config", _YAML, "--verbose", str(src))
        self.assertIn("Scanning:", err)
        self.assertLess(err.index(_COPYRIGHT), err.index("Found 1 file(s)"))
        self.assertLess(err.index(_COPYRIGHT), err.index("Scanning:"))

    # UV-CLI-019 (negative: structured stdout stays clean)
    def test_json_stdout_not_polluted_by_banner(self):
        with tempfile.TemporaryDirectory() as td:
            src = _write(td, "main.c", "\tvoid f(void){}\n")
            _, out, err = _run_main("--config", _YAML,
                                    "--output-format", "json", str(src))
        json.loads(out)  # raises if the banner leaked into stdout
        self.assertIn(_VERSION_STRING, err)

    # UV-CLI-017 (banner still emitted when stdout is piped, not a TTY)
    def test_banner_emitted_when_stdout_piped(self):
        with tempfile.TemporaryDirectory() as td:
            src = _write(td, "main.c", "void f(void){}\n")
            r = subprocess.run(
                [sys.executable, _CHECKER, "--config", _YAML, str(src)],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                stdin=subprocess.DEVNULL, text=True)
        lines = r.stderr.splitlines()
        self.assertEqual(lines[:2], [_VERSION_STRING, _COPYRIGHT])
        self.assertNotIn(_VERSION_STRING, r.stdout)

    # UV-CLI-017 (banner also written to the --log file)
    def test_banner_written_to_log_file(self):
        with tempfile.TemporaryDirectory() as td:
            src = _write(td, "main.c", "void f(void){}\n")
            log = Path(td) / "run.log"
            _, out, err = _run_main("--config", _YAML, "--log", str(log),
                                    str(src))
            log_text = log.read_text(encoding="utf-8")
        self.assertEqual(log_text.splitlines()[:2],
                         [_VERSION_STRING, _COPYRIGHT])
        self.assertTrue(err.startswith(f"{_VERSION_STRING}\n{_COPYRIGHT}\n"))
        self.assertNotIn(_VERSION_STRING, out)

    # UV-CLI-018 (exactly two banner lines, nothing else on stderr)
    def test_banner_is_exactly_two_lines(self):
        with tempfile.TemporaryDirectory() as td:
            src = _write(td, "main.c", "void f(void){}\n")
            _, _, err = _run_main("--config", _YAML, str(src))
        self.assertEqual(err, f"{_VERSION_STRING}\n{_COPYRIGHT}\n")

    # UV-CLI-018 (copyright line format)
    def test_copyright_line_format(self):
        with tempfile.TemporaryDirectory() as td:
            src = _write(td, "main.c", "void f(void){}\n")
            _, _, err = _run_main("--config", _YAML, str(src))
        line1, line2 = err.splitlines()[:2]
        self.assertEqual(line1, f"{_TOOL_NAME} {_VERSION}")
        self.assertRegex(line2, r"^\(C\) \d{4} Dermot Murphy$")
        self.assertEqual(line2, _COPYRIGHT)

    # UV-CLI-019 (negative: no option suppresses the banner)
    def test_no_quiet_option(self):
        with tempfile.TemporaryDirectory() as td:
            src = _write(td, "main.c", "void f(void){}\n")
            with self.assertRaises(SystemExit) as cm:
                _run_main("--config", _YAML, "--quiet", str(src))
        self.assertEqual(cm.exception.code, 2)

    # UV-CLI-019 (negative: --version prints to stdout, no stderr banner)
    def test_version_flag_writes_no_stderr_banner(self):
        rc, out, err = _run_main("--version")
        self.assertEqual(rc, 0)
        self.assertIn(_VERSION_STRING, out)
        self.assertEqual(err, "")


# ---------------------------------------------------------------------------
# SWE1-096 — OS-native path separator in violation output
# ---------------------------------------------------------------------------
def _os_with(pathmod):
    """A stand-in for the ``os`` module as seen by cli.py."""
    return types.SimpleNamespace(path=pathmod, sep=pathmod.sep, walk=os.walk)


class TestOsPathSeparator(unittest.TestCase):
    """UV-CLI-020 to UV-CLI-022 (SWE1-096)."""

    _SRC = "\tvoid f(void){}\n"          # tab -> misc.indentation
    _CFG = cfg_only(misc={"indentation": {"enabled": True,
                                          "severity": "info"}})

    def _paths_and_output(self, pathmod, given):
        with mock.patch.object(_cli, "os", _os_with(pathmod)):
            paths = list(_cli.discover_files([given], [], [], {}))
        self.assertEqual(len(paths), 1)
        viols = Checker(paths[0], self._SRC, self._CFG).run_all().violations
        self.assertTrue(viols)
        return paths[0], viols

    # UV-CLI-020
    def test_windows_backslash_separator(self):
        path, viols = self._paths_and_output(ntpath, "src/drv/./uart.c")
        self.assertEqual(path, "src\\drv\\uart.c")
        for v in viols:
            self.assertTrue(str(v).startswith("src\\drv\\uart.c:1:"), str(v))
            self.assertIn("file=src\\drv\\uart.c,", v.github_annotation())
            self.assertNotIn("/", str(v).split(":", 1)[0])

    # UV-CLI-020
    def test_windows_mixed_separators_normalised(self):
        path, viols = self._paths_and_output(ntpath, "src/drv\\uart.c")
        self.assertEqual(path, "src\\drv\\uart.c")
        self.assertTrue(all(str(v).startswith("src\\drv\\uart.c:")
                            for v in viols))

    # UV-CLI-021
    def test_posix_forward_slash_separator(self):
        path, viols = self._paths_and_output(posixpath, "src//drv/./uart.c")
        self.assertEqual(path, "src/drv/uart.c")
        for v in viols:
            self.assertTrue(str(v).startswith("src/drv/uart.c:1:"), str(v))
            self.assertIn("file=src/drv/uart.c,", v.github_annotation())
            self.assertNotIn("\\", str(v))

    # UV-CLI-022
    def test_emitted_paths_use_host_os_sep(self):
        """End-to-end on the host OS: every reported path is built with os.sep."""
        with tempfile.TemporaryDirectory() as td:
            sub = Path(td) / "sub"
            sub.mkdir()
            _write(sub, "main.c", self._SRC)
            given = td + "/./sub//main.c"
            _, out, _ = _run_main("--config", _YAML, given)
        expected = os.path.join(td, "sub", "main.c")
        lines = [ln for ln in out.splitlines() if "[misc.indentation]" in ln]
        self.assertTrue(lines, out)
        for ln in lines:
            self.assertTrue(ln.startswith(expected + ":"), ln)
        other = "/" if os.sep == "\\" else "\\"
        self.assertNotIn(other, lines[0].split(":1:", 1)[0].replace(td, ""))

    # UV-CLI-022 (negative: Violation.__str__ renders the path verbatim)
    def test_violation_str_does_not_rewrite_path(self):
        """Normalisation happens once at discovery; Violation.__str__() must not
        alter an already-normalised path."""
        for path in ("a\\b\\c.c", "a/b/c.c"):
            v = _mod.Violation(path, 3, 1, "info", "misc.indentation", "m")
            self.assertEqual(str(v),
                             f"{path}:3:1: INFO [misc.indentation] m")


if __name__ == "__main__":
    unittest.main()
