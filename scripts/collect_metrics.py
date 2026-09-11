#!/usr/bin/env python3
"""
collect_metrics.py - Gather CStyleCheck trend-analysis metrics and append
a data point to the branch's JSON history file.

Usage:
    python3 scripts/collect_metrics.py --branch <main|develop> \
        [--output-dir <path>]

Output files (written to --output-dir, default: metrics/):
    <branch>.json   - cumulative data points (appended each run)

The script is idempotent: if the current commit is already recorded it
updates the existing entry rather than duplicating it.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# --------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------
REPO_ROOT   = Path(__file__).resolve().parent.parent
SRC_DIR     = REPO_ROOT / "src"
EXAMPLES    = REPO_ROOT / "examples"
RULES_CFG   = REPO_ROOT / "scripts" / "metrics_rules.yml"
CHECKER     = SRC_DIR / "cstylecheck.py"


def _run(cmd, **kwargs):
    """Run a command, return stdout as a string (empty on failure)."""
    try:
        r = subprocess.run(cmd, capture_output=True, text=True,
                           cwd=REPO_ROOT, **kwargs)
        return r.stdout.strip()
    except Exception:
        return ""


# --------------------------------------------------------------------------
# Git statistics
# --------------------------------------------------------------------------

def _git_commit_info():
    commit  = _run(["git", "rev-parse", "--short", "HEAD"])
    full    = _run(["git", "rev-parse", "HEAD"])
    ts_str  = _run(["git", "log", "-1", "--format=%cI"])
    try:
        ts = datetime.fromisoformat(ts_str).astimezone(timezone.utc).isoformat()
    except Exception:
        ts = datetime.now(timezone.utc).isoformat()
    return commit, full, ts


def _count_source_files():
    """Count tracked source files by category."""
    out = _run(["git", "ls-files"])
    lines = [l for l in out.splitlines() if l]
    c_h   = sum(1 for l in lines if l.endswith((".c", ".h")))
    py    = sum(1 for l in lines if l.endswith(".py"))
    total = len(lines)
    return total, c_h, py


def _git_diff_stats():
    """
    Compare HEAD to HEAD~1.
    Returns (new_files, deleted_files, lines_added, lines_deleted).
    Falls back to zeros on the initial commit.
    """
    out = _run(["git", "diff", "--numstat", "HEAD~1", "HEAD"])
    if not out:
        return 0, 0, 0, 0

    new_files = deleted_files = lines_added = lines_deleted = 0
    for line in out.splitlines():
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        added_s, deleted_s = parts[0], parts[1]
        # Binary files show '-' for counts
        if added_s == "-" or deleted_s == "-":
            continue
        added   = int(added_s)
        deleted = int(deleted_s)
        lines_added   += added
        lines_deleted += deleted
        if added   > 0 and deleted == 0:
            new_files += 1
        elif deleted > 0 and added == 0:
            deleted_files += 1

    return new_files, deleted_files, lines_added, lines_deleted


def _test_and_rule_counts():
    """Return (test_count, rule_count) from pytest and rules.yml."""
    # Test count
    out = _run([sys.executable, "-m", "pytest", "tests/",
                "--collect-only", "-q", "--no-header"],
               timeout=60)
    m = re.search(r"(\d+)\s+tests?\s+collected", out)
    test_count = int(m.group(1)) if m else 0

    # Rule count from rules.yml — count top-level section entries that
    # correspond to enabled rules (heuristic: count rule keys with sub-keys)
    rule_count = 0
    try:
        import yaml
        with open(REPO_ROOT / "src" / "rules.yml") as f:
            cfg = yaml.safe_load(f)
        # Each top-level key is a rule group; count by running the checker
        # with --list-rules if available, otherwise approximate from YAML
        rule_count = _count_rule_ids(cfg)
    except Exception:
        pass

    return test_count, rule_count


def _count_rule_ids(cfg):
    """Approximate rule count from the YAML config structure."""
    known_groups = {
        "variables", "functions", "constants", "typedefs",
        "enums", "structs", "include_guards", "misc"
    }
    # A more robust approach: scan Python source for rule_id strings
    count = 0
    for py_file in (REPO_ROOT / "src" / "cstylecheck").glob("*.py"):
        try:
            src = py_file.read_text(encoding="utf-8", errors="replace")
            # Match both "rule.id" string literals and f-string patterns
            count += len(re.findall(r'"(?:variable|function|misc|constant|typedef|enum|struct|include)[a-z._]+"', src))
        except Exception:
            pass
    # Deduplicate by treating unique literal strings
    rule_ids = set()
    for py_file in (REPO_ROOT / "src" / "cstylecheck").glob("*.py"):
        try:
            src = py_file.read_text(encoding="utf-8", errors="replace")
            rule_ids.update(re.findall(
                r'"((?:variable|function|misc|constant|typedef|enum|struct|include)[a-z._]+)"',
                src))
        except Exception:
            pass
    # Add dynamically constructed ones (variable.{scope}.case / .prefix)
    dynamic = {"variable.global.case", "variable.global.prefix",
                "variable.local.case", "variable.local.prefix",
                "variable.static.case", "variable.static.prefix",
                "variable.parameter.case", "variable.parameter.prefix"}
    rule_ids.update(dynamic)
    return len(rule_ids)


# --------------------------------------------------------------------------
# CStyleCheck scan of examples/
# --------------------------------------------------------------------------

def _cstylecheck_metrics():
    """
    Run CStyleCheck on examples/*.c and examples/*.h.
    Returns dict with errors, warnings, info counts and per-rule breakdown.
    """
    c_files = sorted(EXAMPLES.glob("*.c")) + sorted(EXAMPLES.glob("*.h"))
    if not c_files:
        return {"errors": 0, "warnings": 0, "info": 0, "total": 0,
                "files_checked": 0, "rules_violated": []}

    cmd = [sys.executable, str(CHECKER),
           "--config", str(RULES_CFG),
           "--exit-zero",
           "--output-format", "json"] + [str(p) for p in c_files]

    raw = _run(cmd, timeout=120)
    # Strip the banner (first two lines) before parsing JSON
    lines = raw.splitlines()
    json_start = next(
        (i for i, l in enumerate(lines) if l.strip().startswith("{") or l.strip().startswith("[")),
        0)
    try:
        data = json.loads("\n".join(lines[json_start:]))
    except Exception:
        return {"errors": 0, "warnings": 0, "info": 0, "total": 0,
                "files_checked": 0, "rules_violated": []}

    summary    = data.get("summary", {})
    violations = data.get("violations", [])

    from collections import Counter
    by_rule = Counter(v.get("rule", "unknown") for v in violations)

    return {
        "errors":        summary.get("errors",   0),
        "warnings":      summary.get("warnings", 0),
        "info":          summary.get("info",     0),
        "total":         summary.get("total",    0),
        "files_checked": summary.get("files_checked", 0),
        "rules_violated": [{"rule": r, "count": c}
                           for r, c in by_rule.most_common()],
    }


# --------------------------------------------------------------------------
# Comment / whitespace ratios (raw scan of examples/)
# --------------------------------------------------------------------------

def _source_ratios():
    """
    Scan examples/*.c (not headers) to compute:
      - comment_ratio  : non-doxygen comment lines / total non-blank lines
      - whitespace_ratio: blank lines / total lines
    """
    c_files = sorted(EXAMPLES.glob("*.c"))
    total_lines = comment_lines = blank_lines = code_lines = 0
    in_block_comment = False

    for path in c_files:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        for line in text.splitlines():
            stripped = line.strip()
            total_lines += 1

            if not stripped:
                blank_lines += 1
                continue

            # Doxygen block start — skip until end
            if stripped.startswith("/**"):
                in_block_comment = True
                # Still count as a line but NOT as a regular comment
                code_lines += 1
                if "*/" in stripped[3:]:
                    in_block_comment = False
                continue

            if in_block_comment:
                code_lines += 1
                if "*/" in stripped:
                    in_block_comment = False
                continue

            # Non-doxygen block comment
            if stripped.startswith("/*"):
                in_block_comment = stripped.count("*/") == 0 or (
                    stripped.startswith("/*") and not stripped.startswith("/**")
                    and "*/" not in stripped)
                comment_lines += 1
                if in_block_comment:
                    in_block_comment = True
                continue

            # Line comment
            if stripped.startswith("//"):
                comment_lines += 1
                continue

            # Inline comment (code line with trailing comment)
            if "//" in stripped or "/*" in stripped:
                code_lines += 1
                comment_lines += 1  # count inline comments separately? No — count as code
                comment_lines -= 1  # revert: inline ≠ comment-only line
                code_lines += 0     # (already counted above)

            code_lines += 1

    non_blank = total_lines - blank_lines
    comment_ratio   = round(comment_lines / non_blank,  4) if non_blank  else 0.0
    whitespace_ratio = round(blank_lines  / total_lines, 4) if total_lines else 0.0

    return {
        "comment_ratio":   comment_ratio,
        "whitespace_ratio": whitespace_ratio,
        "total_lines":      total_lines,
        "blank_lines":      blank_lines,
        "comment_lines":    comment_lines,
        "code_lines":       code_lines,
    }


# --------------------------------------------------------------------------
# C source metrics (issue #388)
# ISO 26262-6, IEC 61508-3, MISRA C:2012, ASPICE SWE.3/4, Barr-C:2018
# --------------------------------------------------------------------------

def _empty_c_metrics():
    return {
        "loc_physical": 0, "loc_blank": 0, "loc_comment": 0, "loc_doxygen": 0,
        "loc_sloc": 0, "loc_comment_density": 0.0, "loc_blank_ratio": 0.0,
        "func_count": 0, "func_length_max": 0, "func_length_avg": 0.0,
        "func_over_length": 0, "func_param_max": 0, "func_over_params": 0,
        "cc_max": 0, "cc_avg": 0.0, "cc_over_threshold": 0,
        "nesting_max": 0, "dox_coverage": 0.0,
        "global_vars": 0, "static_vars": 0, "file_length_max": 0,
        "defect_density": 0.0,
    }


def _cat_lines(lines):
    """Categorise source lines → (physical, blank, comment, doxygen, sloc)."""
    physical = len(lines)
    blank = comment = doxygen = 0
    in_block = False
    in_dox   = False

    for raw in lines:
        s = raw.strip()
        if not s:
            blank += 1
            continue
        if in_dox:
            doxygen += 1
            if "*/" in s:
                in_dox = False
            continue
        if in_block:
            comment += 1
            if "*/" in s:
                in_block = False
            continue
        if s.startswith("/**"):
            in_dox = True
            doxygen += 1
            if "*/" in s[3:]:
                in_dox = False
            continue
        if s.startswith("/*"):
            in_block = True
            comment += 1
            if "*/" in s[2:]:
                in_block = False
            continue
        if s.startswith("//"):
            comment += 1
            continue
        # code / SLOC line

    sloc = physical - blank - comment - doxygen
    return physical, blank, comment, doxygen, max(0, sloc)


_DECISION_RE = re.compile(
    r'\b(?:if|while|for|case|do)\b|&&|\|\||\?'
)
_CTRL_KWS = frozenset({
    "if", "else", "while", "for", "do", "switch", "return",
    "break", "continue", "goto", "typedef", "struct", "enum", "union",
})


def _is_func_def(lines, i):
    """Heuristic: does line i start a C function definition?"""
    s = lines[i].strip()
    if not s or s[0] in ("#", "/", "*", "}"):
        return False
    first_tok = re.split(r"\W+", s)[0]
    if first_tok in _CTRL_KWS:
        return False
    if "(" not in s:
        return False
    if s.startswith(("typedef", "struct", "enum", "union")):
        return False
    if s.endswith(";"):
        return False
    n = len(lines)
    for j in range(i, min(i + 6, n)):
        l = lines[j].strip()
        if "{" in l:
            return True
        if ";" in l and j > i:
            return False
    return False


def _func_sig_info(lines, i):
    """Return (name, param_count) from function signature at line i."""
    n = len(lines)
    parts = []
    for j in range(i, min(i + 6, n)):
        parts.append(lines[j])
        if "{" in lines[j]:
            break
    sig = " ".join(parts)
    m = re.search(r"(\w+)\s*\(([^)]*)\)", sig)
    if not m:
        return "unknown", 0
    name = m.group(1)
    ps   = m.group(2).strip()
    params = 0 if (not ps or ps.lower() == "void") else ps.count(",") + 1
    return name, params


def _has_dox_before(lines, i):
    """Return True if a /** … */ block immediately precedes line i."""
    j = i - 1
    while j >= 0 and not lines[j].strip():
        j -= 1
    if j < 0:
        return False
    if "*/" in lines[j]:
        k = j
        while k >= 0 and (j - k) < 40:
            if lines[k].strip().startswith("/**"):
                return True
            k -= 1
    return False


def _func_complexity(body_lines):
    """McCabe cyclomatic complexity = 1 + decision points in function body."""
    cc = 1
    for raw in body_lines:
        s = raw.strip()
        if s.startswith(("//", "*", "/*")):
            continue
        cc += len(_DECISION_RE.findall(s))
    return cc


def _extract_functions(text):
    """Return list of {name, length, params, complexity, nesting, has_dox} dicts."""
    lines = text.splitlines()
    n = len(lines)
    funcs = []
    i = 0
    while i < n:
        if not _is_func_def(lines, i):
            i += 1
            continue

        name, params = _func_sig_info(lines, i)
        has_dox = _has_dox_before(lines, i)

        brace_line = i
        while brace_line < n and "{" not in lines[brace_line]:
            brace_line += 1
        if brace_line >= n:
            i += 1
            continue

        depth = 0
        max_depth = 0
        end_line = brace_line
        for j in range(brace_line, n):
            for ch in lines[j]:
                if ch == "{":
                    depth += 1
                    if depth > max_depth:
                        max_depth = depth
                elif ch == "}":
                    depth -= 1
            if depth == 0:
                end_line = j
                break

        body = lines[brace_line:end_line + 1]
        funcs.append({
            "name":       name,
            "length":     len(body),
            "params":     params,
            "complexity": _func_complexity(body),
            "nesting":    max(0, max_depth - 1),
            "has_dox":    has_dox,
        })
        i = end_line + 1

    return funcs


def _count_static_vars(text):
    """Count static variable declarations at file scope in a .c file."""
    static_v = 0
    depth = 0
    in_block = False

    for raw in text.splitlines():
        s = raw.strip()
        if in_block:
            if "*/" in s:
                in_block = False
            continue
        if s.startswith("/*") and "*/" not in s[2:]:
            in_block = True
            continue
        if s.startswith(("//", "*", "#")):
            continue

        # At file scope, a static var starts with 'static' and ends with ';'
        # but has no '(' (which would make it a function declaration)
        if depth == 0 and s.startswith("static ") and s.endswith(";") and "(" not in s:
            static_v += 1

        depth += s.count("{") - s.count("}")
        depth = max(0, depth)

    return static_v


def _c_source_metrics(total_violations=0):
    """
    Analyse examples/*.c and *.h for industry-standard C source metrics.
    total_violations is passed in to compute defect density.
    """
    c_files = sorted(EXAMPLES.glob("*.c"))
    h_files = sorted(EXAMPLES.glob("*.h"))
    all_files = c_files + h_files

    if not all_files:
        return _empty_c_metrics()

    total_phys = total_blank = total_cmt = total_dox = total_sloc = 0
    all_funcs = []
    total_static_v = 0
    max_file_len = 0

    for fpath in all_files:
        try:
            text = fpath.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        file_lines = text.splitlines()
        if len(file_lines) > max_file_len:
            max_file_len = len(file_lines)

        ph, bl, cm, dx, sl = _cat_lines(file_lines)
        total_phys  += ph
        total_blank += bl
        total_cmt   += cm
        total_dox   += dx
        total_sloc  += sl

        if fpath.suffix == ".c":
            all_funcs.extend(_extract_functions(text))
            total_static_v += _count_static_vars(text)

    n = len(all_funcs)
    lengths      = [f["length"]     for f in all_funcs]
    complexities = [f["complexity"] for f in all_funcs]
    params_list  = [f["params"]     for f in all_funcs]
    nestings     = [f["nesting"]    for f in all_funcs]
    dox_covered  = sum(1 for f in all_funcs if f["has_dox"])

    sloc = total_sloc
    kloc = sloc / 1000.0 if sloc else 0.001

    return {
        # Lines of code (IEC 61508-3 Annex B, ISO 26262-6)
        "loc_physical":        total_phys,
        "loc_blank":           total_blank,
        "loc_comment":         total_cmt,
        "loc_doxygen":         total_dox,
        "loc_sloc":            sloc,
        "loc_comment_density": round((total_cmt + total_dox) / sloc, 3) if sloc else 0.0,
        "loc_blank_ratio":     round(total_blank / total_phys, 3) if total_phys else 0.0,
        # Function metrics (MISRA C:2012 Rule 15.4, Barr-C §2)
        "func_count":          n,
        "func_length_max":     max(lengths, default=0),
        "func_length_avg":     round(sum(lengths) / n, 1) if n else 0.0,
        "func_over_length":    sum(1 for l in lengths if l > 60),
        "func_param_max":      max(params_list, default=0),
        "func_over_params":    sum(1 for p in params_list if p > 6),
        # Cyclomatic complexity (McCabe, ISO 26262-6 §8.4.4)
        "cc_max":              max(complexities, default=0),
        "cc_avg":              round(sum(complexities) / n, 2) if n else 0.0,
        "cc_over_threshold":   sum(1 for c in complexities if c > 10),
        # Control-flow nesting depth (MISRA C:2012 Rule 15.5)
        "nesting_max":         max(nestings, default=0),
        # Documentation coverage (ASPICE SWE.3/SWE.4)
        "dox_coverage":        round(dox_covered / n, 3) if n else 0.0,
        # Variables (AUTOSAR BSW, JSF AV Rule 137)
        "static_vars":         total_static_v,
        # File-level metrics
        "file_length_max":     max_file_len,
        # Defect density (violations per KLOC) — ASPICE SWE.4 maturity index
        "defect_density":      round(total_violations / kloc, 2),
    }


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def _load_history(path):
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            pass
    return {"branch": "", "data_points": []}


def _save_history(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2))


def main():
    ap = argparse.ArgumentParser(description="Collect CStyleCheck trend metrics")
    ap.add_argument("--branch", required=True,
                    help="Branch name (main or develop)")
    ap.add_argument("--output-dir", default="metrics",
                    help="Directory to write JSON history (default: metrics/)")
    args = ap.parse_args()

    branch     = args.branch
    output_dir = REPO_ROOT / args.output_dir

    print(f"[metrics] Collecting for branch: {branch}")

    # --- gather ---
    commit, full_sha, timestamp = _git_commit_info()
    total_files, c_files_count, py_files_count = _count_source_files()
    new_files, deleted_files, lines_added, lines_deleted = _git_diff_stats()
    csc             = _cstylecheck_metrics()
    ratios          = _source_ratios()
    test_count, rule_count = _test_and_rule_counts()
    c_metrics       = _c_source_metrics(total_violations=csc["total"])

    data_point = {
        "timestamp":       timestamp,
        "commit":          commit,
        "full_sha":        full_sha,
        # Repository file stats
        "total_files":     total_files,
        "c_h_files":       c_files_count,
        "py_files":        py_files_count,
        "new_files":       new_files,
        "deleted_files":   deleted_files,
        "lines_added":     lines_added,
        "lines_deleted":   lines_deleted,
        # CStyleCheck scan of examples/
        "errors":          csc["errors"],
        "warnings":        csc["warnings"],
        "info_count":      csc["info"],
        "total_violations": csc["total"],
        "files_checked":   csc["files_checked"],
        "rules_violated":  csc["rules_violated"],
        # Source ratios (examples/*.c, excluding doxygen)
        "comment_ratio":   ratios["comment_ratio"],
        "whitespace_ratio": ratios["whitespace_ratio"],
        "total_lines":     ratios["total_lines"],
        "comment_lines":   ratios["comment_lines"],
        "code_lines":      ratios["code_lines"],
        # Tool stats
        "test_count":      test_count,
        "rule_count":      rule_count,
        # C source metrics (issue #388)
        "loc_physical":        c_metrics["loc_physical"],
        "loc_blank":           c_metrics["loc_blank"],
        "loc_comment":         c_metrics["loc_comment"],
        "loc_doxygen":         c_metrics["loc_doxygen"],
        "loc_sloc":            c_metrics["loc_sloc"],
        "loc_comment_density": c_metrics["loc_comment_density"],
        "loc_blank_ratio":     c_metrics["loc_blank_ratio"],
        "func_count":          c_metrics["func_count"],
        "func_length_max":     c_metrics["func_length_max"],
        "func_length_avg":     c_metrics["func_length_avg"],
        "func_over_length":    c_metrics["func_over_length"],
        "func_param_max":      c_metrics["func_param_max"],
        "func_over_params":    c_metrics["func_over_params"],
        "cc_max":              c_metrics["cc_max"],
        "cc_avg":              c_metrics["cc_avg"],
        "cc_over_threshold":   c_metrics["cc_over_threshold"],
        "nesting_max":         c_metrics["nesting_max"],
        "dox_coverage":        c_metrics["dox_coverage"],
        "static_vars":         c_metrics["static_vars"],
        "file_length_max":     c_metrics["file_length_max"],
        "defect_density":      c_metrics["defect_density"],
    }

    # --- load, upsert, save ---
    hist_path = output_dir / f"{branch}.json"
    history   = _load_history(hist_path)
    history["branch"] = branch

    points = history["data_points"]
    idx = next((i for i, p in enumerate(points) if p.get("full_sha") == full_sha), None)
    if idx is not None:
        points[idx] = data_point
        print(f"[metrics] Updated existing entry for {commit}")
    else:
        points.append(data_point)
        print(f"[metrics] Appended new entry for {commit}")

    _save_history(hist_path, history)
    print(f"[metrics] Saved → {hist_path}")
    print(f"[metrics] Summary: errors={data_point['errors']}, "
          f"warnings={data_point['warnings']}, "
          f"total_files={data_point['total_files']}, "
          f"tests={data_point['test_count']}, "
          f"sloc={data_point['loc_sloc']}, "
          f"funcs={data_point['func_count']}, "
          f"cc_max={data_point['cc_max']}, "
          f"defect_density={data_point['defect_density']}")

    # Print JSON for the workflow to capture if needed
    print(json.dumps(data_point))


if __name__ == "__main__":
    main()
