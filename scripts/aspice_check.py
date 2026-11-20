#!/usr/bin/env python3
"""
aspice_check.py - Merge-time ASPICE work-product consistency checks.

Usage:
    python scripts/aspice_check.py [--fix-citations] [--skip-tests]

Checks (one "PASS/FAIL <check>: <detail>" line each, mismatches listed
below the line as file:line entries):

    citations   Current-state document-version citations in the ASPICE work
                products (docs/aspice/CStyleCheck_*.md) match the version in
                the cited document's header (or review-record footer).
    sys2-rtm    CSC-SYS2-001 §6 RTM SWE.1 column matches the parent column
                of CSC-SWE1-001 §4, in both directions.
    swe4-counts CSC-SWE4-001 §6 per-module test counts and total match
                `pytest --collect-only` (skipped with --skip-tests).
    rule-ids    README "Rule IDs" table lists exactly the rule IDs emitted
                by the checker source (src/cstylecheck/*.py).
    swe3-lines  CSC-SWE3-001 §4 unit catalogue `file.py:NNN` references are
                within +/-2 lines of the named def/class.
    ci-coverage Every `git ls-files` path is covered by a CSC-SUP8-001 §6.1
                configuration-item path or glob.

--fix-citations rewrites stale citations in place (the SUP8 §9 resync) and
reports how many lines were changed; the check is then re-run.

Exit status: 0 if every check passes, 1 otherwise.

Stdlib only (plus PyYAML via requirements.txt, not needed by these checks).
"""

import argparse
import ast
import re
import subprocess
import sys
from pathlib import Path

# --------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
ASPICE    = REPO_ROOT / "docs" / "aspice"
PKG_DIR   = REPO_ROOT / "src" / "cstylecheck"
README    = REPO_ROOT / "README.md"
SWE1_DOC  = ASPICE / "CStyleCheck_SWE1_SW_Requirements.md"
SYS2_DOC  = ASPICE / "CStyleCheck_SYS2_System_Requirements.md"
SWE3_DOC  = ASPICE / "CStyleCheck_SWE3_Detailed_Design.md"
SWE4_DOC  = ASPICE / "CStyleCheck_SWE4_Unit_Verification.md"
SUP8_DOC  = ASPICE / "CStyleCheck_SUP8_CM_Plan.md"

BOM = b"\xef\xbb\xbf"


def _read(path):
    """Return the text of *path* (UTF-8, BOM stripped)."""
    return path.read_text(encoding="utf-8-sig")


def _rel(path):
    """Return *path* relative to the repository root, POSIX style."""
    return path.relative_to(REPO_ROOT).as_posix()


def _section(lines, start_pat, end_pat):
    """Yield (lineno, line) for lines after *start_pat* up to *end_pat*."""
    inside = False
    for i, line in enumerate(lines, 1):
        if re.match(start_pat, line):
            inside = True
            continue
        if inside and re.match(end_pat, line):
            return
        if inside:
            yield i, line


def _cells(line):
    """Split a Markdown table row into stripped cells."""
    return [c.strip() for c in line.strip().strip("|").split("|")]


# --------------------------------------------------------------------------
# (a) Document-version citations
# --------------------------------------------------------------------------
HDR_RE = re.compile(
    r"\*\*Document ID\*\* \| (CSC-[A-Z0-9-]+) \| \*\*Version\*\* \| "
    r"(\d+\.\d+) \|")
FOOTER_RE = re.compile(r"\*Document: (CSC-REVIEW-\d+) · Version (\d+\.\d+)")
HIST_RE = re.compile(r"^\| \d+\.\d+ \| 20\d\d-")
COL1_RE = re.compile(
    r"^(\|\s*)(CSC-[A-Z0-9-]+)(\s*\|[^|]*\|\s*)(\d+\.\d+)(\s*\|.*)$")
COL2_RE = re.compile(
    r"^(\|[^|]*\|\s*)(CSC-[A-Z0-9-]+)(\s*\|\s*)(\d+\.\d+)(\s*\|.*)$")
INLINE_RE = re.compile(r"(CSC-[A-Z0-9]+-\d{3}) v(\d+\.\d+)")
INLINE_LINE_RE = re.compile(r"; (in CM|CI evidence) \|")
ALIAS = {"CSC-DEV001": "CSC-DEV-001", "CSC-DEV002": "CSC-DEV-002"}
EXCLUDED_NAMES = ("Review_Record", "Review_Template", "Analysis_Report")


def document_registry():
    """Return {document ID: current version} for every ASPICE work product."""
    reg = {}
    for path in sorted(ASPICE.glob("CStyleCheck_*.md")):
        text = _read(path)
        m = HDR_RE.search(text)
        if m:
            reg[m.group(1)] = m.group(2)
        m = FOOTER_RE.search(text)
        if m:
            reg[m.group(1)] = m.group(2)
    return reg


def _fix_line(line, reg):
    """Return *line* with every current-state citation set to *reg*."""
    if HIST_RE.match(line) or "**Affected documents**" in line:
        return line

    def cur(doc_id):
        return reg.get(ALIAS.get(doc_id, doc_id))

    m = COL1_RE.match(line)
    if m and cur(m.group(2)):
        line = m.group(1) + m.group(2) + m.group(3) + cur(m.group(2)) + \
            m.group(5)
    m = COL2_RE.match(line)
    if m and cur(m.group(2)):
        line = m.group(1) + m.group(2) + m.group(3) + cur(m.group(2)) + \
            m.group(5)
    if INLINE_LINE_RE.search(line) or line.startswith("*End of"):
        line = INLINE_RE.sub(
            lambda k: f"{k.group(1)} v{cur(k.group(1)) or k.group(2)}", line)
    return line


def check_citations(fix=False):
    """Check (and optionally fix) document-version citations."""
    reg = document_registry()
    issues = []
    fixed = 0
    for path in sorted(ASPICE.glob("CStyleCheck_*.md")):
        if any(x in path.name for x in EXCLUDED_NAMES):
            continue
        raw = path.read_bytes()
        has_bom = raw.startswith(BOM)
        lines = raw.decode("utf-8-sig").split("\n")
        changed = False
        for i, line in enumerate(lines):
            new = _fix_line(line, reg)
            if new == line:
                continue
            old_ids = INLINE_RE.findall(line) + \
                [(m.group(2), m.group(4)) for m in
                 (COL1_RE.match(line), COL2_RE.match(line)) if m]
            what = ", ".join(f"{d} {v}->{reg.get(ALIAS.get(d, d))}"
                             for d, v in old_ids
                             if reg.get(ALIAS.get(d, d)) not in (None, v))
            issues.append(f"{_rel(path)}:{i + 1}: {what}")
            if fix:
                lines[i] = new
                changed = True
                fixed += 1
        if changed:
            data = "\n".join(lines).encode("utf-8")
            path.write_bytes((BOM if has_bom else b"") + data)
    if fix:
        print(f"FIXED citations: {fixed} line(s) rewritten")
        return check_citations(fix=False)
    detail = (f"{len(reg)} documents in registry, all citations current"
              if not issues else f"{len(issues)} stale citation line(s)")
    return not issues, detail, issues


# --------------------------------------------------------------------------
# (b) SYS2 §6 RTM vs SWE1 §4 parents
# --------------------------------------------------------------------------
def _expand_sys(text):
    """Expand SYS-F/NF IDs and ranges (also bare F-/NF- shorthand)."""
    text = text.replace("\\", "")
    text = re.sub(r"(?<!SYS-)\b(F|NF)-(\d+)", r"SYS-\1-\2", text)
    out = set()
    for m in re.finditer(r"SYS-(F|NF)-(\d+)(?:\s*(?:to|–|-)\s*"
                         r"SYS-(?:F|NF)-(\d+))?", text):
        kind, a = m.group(1), int(m.group(2))
        b = int(m.group(3)) if m.group(3) else a
        out |= {f"SYS-{kind}-{n:03d}" for n in range(a, b + 1)}
    return out


def _expand_swe1(text):
    """Expand SWE1 / SWE1-MISRA IDs and 'X to Y' ranges."""
    out = set()
    for m in re.finditer(r"SWE1-(MISRA-)?(\d+)(?:\s+to\s+SWE1-(?:MISRA-)?"
                         r"(\d+))?", text.replace("\\", "")):
        pre = "SWE1-" + (m.group(1) or "")
        a = int(m.group(2))
        b = int(m.group(3) or a)
        out |= {f"{pre}{n:03d}" for n in range(a, b + 1)}
    return out


def check_sys2_rtm():
    """SYS2 §6 SWE.1 column must equal the SWE1 §4 children of each row."""
    parents = {}
    for _, line in _section(_read(SWE1_DOC).split("\n"),
                            r"## 4\. Software Requirements", r"## 5\. "):
        if line.startswith("| SWE1-"):
            c = _cells(line)
            parents[c[0]] = _expand_sys(c[-1])
    issues = []
    covered = set()
    rows = 0
    rel = _rel(SYS2_DOC)
    for i, line in _section(_read(SYS2_DOC).split("\n"),
                            r"## 6\. Requirements Traceability",
                            r"## 7\. "):
        if not line.startswith("| SYS-"):
            continue
        rows += 1
        c = _cells(line)
        sys_ids = _expand_sys(c[0])
        covered |= sys_ids
        want = {k for k, v in parents.items() if v & sys_ids}
        have = _expand_swe1(c[4])
        if want != have:
            missing = sorted(want - have)
            extra = sorted(have - want)
            issues.append(f"{rel}:{i}: {c[0]}: missing {missing or '-'}, "
                          f"extra {extra or '-'}")
    for req, pset in parents.items():
        for sid in sorted(pset - covered):
            issues.append(f"{_rel(SWE1_DOC)}: {req} parent {sid} has no "
                          f"SYS2 §6 RTM row")
    detail = (f"{rows} RTM rows consistent with {len(parents)} SWE1 "
              f"requirements" if not issues
              else f"{len(issues)} RTM mismatch(es)")
    return not issues, detail, issues


# --------------------------------------------------------------------------
# (c) SWE4 §6 per-module test counts
# --------------------------------------------------------------------------
def check_swe4_counts():
    """SWE4 §6 table counts must match pytest collection."""
    r = subprocess.run(
        [sys.executable, "-m", "pytest", "--collect-only", "-q", "tests"],
        capture_output=True, text=True, cwd=REPO_ROOT)
    actual = {}
    for line in r.stdout.splitlines():
        m = re.match(r"^tests/(test_\w+\.py)::", line)
        if m:
            actual[m.group(1)] = actual.get(m.group(1), 0) + 1
    if r.returncode != 0 or not actual:
        return False, "pytest collection failed", \
            [line for line in (r.stdout + r.stderr).splitlines()[-10:]]
    issues = []
    doc = {}
    total = None
    rel = _rel(SWE4_DOC)
    for i, line in _section(_read(SWE4_DOC).split("\n"),
                            r"## 6\. ", r"## 7\. "):
        m = re.match(r"^\| `(test_\w+\.py)` \| (\d+) \|", line)
        if m:
            doc[m.group(1)] = (int(m.group(2)), i)
        m = re.match(r"^\| \*\*Total\*\* \| \*\*(\d+)\*\* \|", line)
        if m:
            total = (int(m.group(1)), i)
    for mod, n in sorted(actual.items()):
        if mod not in doc:
            issues.append(f"{rel}: {mod} ({n} tests) missing from §6")
        elif doc[mod][0] != n:
            issues.append(f"{rel}:{doc[mod][1]}: {mod} lists {doc[mod][0]}, "
                          f"collected {n}")
    for mod, (n, i) in sorted(doc.items()):
        if mod not in actual:
            issues.append(f"{rel}:{i}: {mod} listed but not collected")
    n_act = sum(actual.values())
    if total is None:
        issues.append(f"{rel}: §6 Total row not found")
    elif total[0] != n_act:
        issues.append(f"{rel}:{total[1]}: Total {total[0]}, collected "
                      f"{n_act}")
    detail = (f"{len(actual)} modules, {n_act} tests match §6"
              if not issues else f"{len(issues)} count mismatch(es)")
    return not issues, detail, issues


# --------------------------------------------------------------------------
# (d) README Rule IDs table vs checker source
# --------------------------------------------------------------------------
RULE_ID_RE = re.compile(r"^[a-z_]+(\.[a-z_]+)*$")
EMITTERS = ("_v", "Violation", "_require_module_prefix")
SEVERITIES = ("error", "warning", "info", "notice")


def source_rule_ids():
    """Return the rule IDs passed to violation emitters in the package.

    Plain string literals are taken as-is; f-strings such as
    ``f"{rule_pfx}.case"`` are expanded with every string literal assigned
    to the interpolated name in the enclosing function.
    """
    ids = set()
    for path in sorted(PKG_DIR.glob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for fn in ast.walk(tree):
            if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            assigned = {}
            for node in ast.walk(fn):
                if isinstance(node, ast.Assign):
                    strs = {c.value for c in ast.walk(node.value)
                            if isinstance(c, ast.Constant)
                            and isinstance(c.value, str)}
                    for tgt in node.targets:
                        if isinstance(tgt, ast.Name):
                            assigned.setdefault(tgt.id, set()).update(strs)
            for node in ast.walk(fn):
                if not isinstance(node, ast.Call):
                    continue
                func = node.func
                name = func.attr if isinstance(func, ast.Attribute) \
                    else getattr(func, "id", "")
                if name not in EMITTERS:
                    continue
                for arg in node.args + [k.value for k in node.keywords]:
                    if isinstance(arg, ast.Constant) and \
                            isinstance(arg.value, str):
                        if RULE_ID_RE.match(arg.value) and \
                                arg.value not in SEVERITIES:
                            ids.add(arg.value)
                    elif isinstance(arg, ast.JoinedStr):
                        vals = [""]
                        for part in arg.values:
                            if isinstance(part, ast.Constant):
                                vals = [v + part.value for v in vals]
                            elif isinstance(part.value, ast.Name) and \
                                    part.value.id in assigned:
                                vals = [v + x for v in vals
                                        for x in assigned[part.value.id]]
                            else:
                                vals = []
                        ids |= {v for v in vals if RULE_ID_RE.match(v)}
    return ids


def check_rule_ids():
    """README Rule IDs table must list exactly the source rule IDs."""
    lines = _read(README).split("\n")
    listed = set()
    stated = None
    for i, line in enumerate(lines, 1):
        m = re.match(r"^## Rule IDs \((\d+) total\)", line)
        if m:
            stated = (int(m.group(1)), i)
    if stated is None:
        return False, "README '## Rule IDs (N total)' section not found", []
    for i, line in _section(lines, r"## Rule IDs", r"## |---$"):
        if line.startswith("|") and not line.startswith("|---"):
            listed |= set(re.findall(r"`([a-z_.]+)`", line))
    src = source_rule_ids()
    issues = [f"README.md: {x} listed but not emitted by the checker"
              for x in sorted(listed - src)]
    issues += [f"README.md: {x} emitted by the checker but not listed"
               for x in sorted(src - listed)]
    if stated[0] != len(src):
        issues.append(f"README.md:{stated[1]}: heading states {stated[0]} "
                      f"rule IDs, source defines {len(src)}")
    detail = (f"{len(src)} rule IDs match" if not issues
              else f"{len(issues)} rule ID mismatch(es)")
    return not issues, detail, issues


# --------------------------------------------------------------------------
# (e) SWE3 §4 unit catalogue line references
# --------------------------------------------------------------------------
def check_swe3_lines():
    """SWE3 §4 `file.py:NNN` must be within +/-2 lines of the def/class."""
    defs = {}
    for path in PKG_DIR.glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef,
                                 ast.ClassDef)):
                defs.setdefault((path.name, node.name), []).append(
                    node.lineno)
    issues = []
    ok = 0
    rel = _rel(SWE3_DOC)
    unit_re = re.compile(
        r"\| (UNIT-\d+) \| `([^`]+)`[^|]*\| `(\w+\.py):(\d+)` \|")
    for i, line in _section(_read(SWE3_DOC).split("\n"),
                            r"## 4\. ", r"## 5\. "):
        m = unit_re.match(line)
        if not m:
            continue
        unit, name, fname, ln = m.group(1), m.group(2), m.group(3), \
            int(m.group(4))
        cands = defs.get((fname, name.split(".")[-1]), [])
        if any(abs(c - ln) <= 2 for c in cands):
            ok += 1
        else:
            issues.append(f"{rel}:{i}: {unit} `{name}` cites {fname}:{ln}, "
                          f"defined at {cands or 'nowhere'}")
    detail = (f"{ok} unit references current" if not issues
              else f"{len(issues)} stale unit reference(s)")
    return not issues, detail, issues


# --------------------------------------------------------------------------
# (f) SUP8 §6.1 configuration-item coverage
# --------------------------------------------------------------------------
def _glob_to_re(pattern):
    """Translate a CI path glob (`*`, `**`, trailing `/`) to a regex."""
    if pattern.endswith("/"):
        pattern += "**"
    out = ""
    i = 0
    while i < len(pattern):
        if pattern.startswith("**", i):
            out += ".*"
            i += 2
        elif pattern[i] == "*":
            out += "[^/]*"
            i += 1
        elif pattern[i] == "?":
            out += "[^/]"
            i += 1
        else:
            out += re.escape(pattern[i])
            i += 1
    return re.compile(out + "$")


def check_ci_coverage():
    """Every tracked file must match a SUP8 §6.1 CI path or glob."""
    patterns = []
    for _, line in _section(_read(SUP8_DOC).split("\n"),
                            r"### 6\.1 ", r"##"):
        if line.startswith("| CI-"):
            c = _cells(line)
            patterns += re.findall(r"`([^`]+)`", c[2])
    regexes = [_glob_to_re(p) for p in patterns]
    r = subprocess.run(["git", "ls-files"], capture_output=True, text=True,
                       cwd=REPO_ROOT)
    if r.returncode != 0:
        return False, "git ls-files failed", [r.stderr.strip()]
    files = [f for f in r.stdout.splitlines() if f]
    issues = [f"{f}: not covered by any SUP8 §6.1 CI path"
              for f in files if not any(rx.match(f) for rx in regexes)]
    detail = (f"{len(files)} tracked files covered by {len(patterns)} CI "
              f"paths" if not issues
              else f"{len(issues)} tracked file(s) not under a CI")
    return not issues, detail, issues


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def main(argv=None):
    """Run every check and return the process exit status."""
    ap = argparse.ArgumentParser(
        description="ASPICE work-product consistency checks (#437).")
    ap.add_argument("--fix-citations", action="store_true",
                    help="rewrite stale document-version citations in place")
    ap.add_argument("--skip-tests", action="store_true",
                    help="skip the SWE4 pytest-collection count check")
    args = ap.parse_args(argv)

    checks = [
        ("citations", lambda: check_citations(fix=args.fix_citations)),
        ("sys2-rtm", check_sys2_rtm),
        ("swe4-counts", None if args.skip_tests else check_swe4_counts),
        ("rule-ids", check_rule_ids),
        ("swe3-lines", check_swe3_lines),
        ("ci-coverage", check_ci_coverage),
    ]
    failed = 0
    for name, fn in checks:
        if fn is None:
            print(f"SKIP {name}: --skip-tests")
            continue
        ok, detail, issues = fn()
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")
        for item in issues:
            print(f"    {item}")
        failed += not ok
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
