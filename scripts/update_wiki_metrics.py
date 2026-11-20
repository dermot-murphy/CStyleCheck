#!/usr/bin/env python3
"""
update_wiki_metrics.py - Write/update the Trend-Analysis wiki page.

Usage:
    python3 scripts/update_wiki_metrics.py \
        --data-dir <path> \
        --charts-url-base <base-url-to-raw-svgs>

The script writes Trend-Analysis.md to the current directory.
Run this inside a checkout of the wiki repo:
    git clone https://github.com/dermot-murphy/CStyleCheck.wiki.git wiki
    cd wiki
    python3 ../scripts/update_wiki_metrics.py ...
    git add Trend-Analysis.md && git commit -m "chore: update metrics"
    git push
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


BRANCHES = ["main", "develop"]


def _fmt_val(v):
    if v is None:
        return "—"
    if isinstance(v, float):
        return f"{v:.3f}"
    return str(v)


def _last_point(data_dir, branch):
    p = Path(data_dir) / f"{branch}.json"
    if not p.exists():
        return None
    try:
        h = json.loads(p.read_text())
        pts = h.get("data_points", [])
        return pts[-1] if pts else None
    except Exception:
        return None


def _table_row(label, *vals):
    cells = " | ".join(_fmt_val(v) for v in vals)
    return f"| {label} | {cells} |"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-dir",         required=True)
    ap.add_argument("--charts-url-base",  required=True,
                    help="Base URL for raw SVG files, e.g. "
                         "https://raw.githubusercontent.com/dermot-murphy/"
                         "CStyleCheck/gh-pages/metrics/charts")
    ap.add_argument("--output", default="Trend-Analysis.md")
    args = ap.parse_args()

    base = args.charts_url_base.rstrip("/")
    now  = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# CStyleCheck — Trend Analysis",
        "",
        f"*Auto-generated {now}. Updated after every PR merge to `main` or `develop`.*",
        "",
        "---",
        "",
        "## Latest snapshot",
        "",
    ]

    # Summary table
    headers = ["Metric"] + BRANCHES
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join("---" for _ in headers) + " |")

    points = {b: _last_point(args.data_dir, b) for b in BRANCHES}

    metrics = [
        ("Total files",       "total_files"),
        ("Python files",      "py_files"),
        ("C/H example files", "c_h_files"),
        ("Lines added",       "lines_added"),
        ("Lines deleted",     "lines_deleted"),
        ("New files",         "new_files"),
        ("Deleted files",     "deleted_files"),
        ("Errors (CStyleCheck)", "errors"),
        ("Warnings (CStyleCheck)", "warnings"),
        ("Info violations",   "info_count"),
        ("Comment ratio",     "comment_ratio"),
        ("Whitespace ratio",  "whitespace_ratio"),
        ("Test count",        "test_count"),
        ("Rule count",        "rule_count"),
        # C source metrics (issue #388)
        ("SLOC",              "loc_sloc"),
        ("Physical lines",    "loc_physical"),
        ("Comment lines",     "loc_comment"),
        ("Doxygen lines",     "loc_doxygen"),
        ("Comment density",   "loc_comment_density"),
        ("Blank ratio",       "loc_blank_ratio"),
        ("Function count",    "func_count"),
        ("Max func length",   "func_length_max"),
        ("Avg func length",   "func_length_avg"),
        ("Funcs over 60 LOC", "func_over_length"),
        ("Max params",        "func_param_max"),
        ("CC max",            "cc_max"),
        ("CC avg",            "cc_avg"),
        ("Nesting depth max", "nesting_max"),
        ("Doxygen coverage",  "dox_coverage"),
        ("Static vars",       "static_vars"),
        ("Max file length",   "file_length_max"),
        ("Defect density (v/KLOC)", "defect_density"),
        ("Assert count",            "assert_count"),
        ("Assert density (/KLOC)",  "assert_density"),
        ("Goto count",              "goto_count"),
        ("Void pointer count",      "void_ptr_count"),
        ("C-style cast count",      "cast_count"),
        ("Macro count",             "macro_count"),
        # Extended C source metrics (issue #388)
        (".c files",                "c_file_count"),
        (".h files",                "h_file_count"),
        ("Funcs over 5 params",     "func_over_params"),
        ("Funcs CC > 10",           "cc_over_threshold"),
        ("Funcs CC 1-5",            "cc_bucket_1_5"),
        ("Funcs CC 6-10",           "cc_bucket_6_10"),
        ("Funcs CC 11-15",          "cc_bucket_11_15"),
        ("Funcs CC 16+",            "cc_bucket_16_plus"),
        ("Doxygen coverage %",      "dox_coverage_pct"),
        ("Global vars",             "global_vars"),
        ("Avg fan-out",             "fanout_avg"),
        ("Recursive functions",     "recursive_func_count"),
        ("Files with 0 violations", "files_zero_violations"),
    ]

    for label, key in metrics:
        vals = [points[b].get(key) if points[b] else None for b in BRANCHES]
        lines.append(_table_row(label, *vals))

    lines += [""]

    # Violations by rule category (issue #388)
    cats = sorted({c for b in BRANCHES if points[b]
                   for c in (points[b].get("violations_by_category") or {})})
    if cats:
        lines += ["### Violations by rule category", ""]
        lines.append("| " + " | ".join(["Category"] + BRANCHES) + " |")
        lines.append("| " + " | ".join("---" for _ in range(len(BRANCHES) + 1)) + " |")
        for cat in cats:
            vals = [((points[b].get("violations_by_category") or {}).get(cat, 0)
                     if points[b] and points[b].get("violations_by_category") is not None
                     else None) for b in BRANCHES]
            lines.append(_table_row(f"`{cat}`", *vals))
        lines.append("")

    # Top-5 violated rules (issue #388)
    if any(points[b] and points[b].get("top_rules") for b in BRANCHES):
        lines += ["### Top 5 violated rules", ""]
        lines.append("| Rank | " + " | ".join(BRANCHES) + " |")
        lines.append("| " + " | ".join("---" for _ in range(len(BRANCHES) + 1)) + " |")
        for rank in range(5):
            cells = []
            for b in BRANCHES:
                tr = (points[b] or {}).get("top_rules") or []
                cells.append(f"`{tr[rank]['rule']}` ({tr[rank]['count']})"
                             if rank < len(tr) else "—")
            lines.append(f"| {rank + 1} | " + " | ".join(cells) + " |")
        lines.append("")

    lines += ["---", ""]

    # Charts per branch
    chart_keys = [
        ("errors_warnings",       "Violation counts"),
        ("file_stats",            "Repository file counts"),
        ("line_churn",            "Line churn per commit"),
        ("file_churn",            "File churn per commit"),
        ("ratios",                "Comment & whitespace ratios"),
        ("test_rule_counts",      "Test & rule counts"),
        ("loc_breakdown",         "LOC composition (SLOC / comment / doxygen / blank, stacked)"),
        ("cyclomatic_complexity", "Cyclomatic complexity & nesting depth"),
        ("cc_distribution",       "Cyclomatic complexity distribution (stacked)"),
        ("function_size",         "Function count & average length"),
        ("defect_density",        "Defect density (violations per KLOC SLOC)"),
        ("violations_by_category", "Violations by rule category (stacked)"),
        ("documentation_coverage", "Documentation coverage (comment density % & doxygen coverage %)"),
        ("coupling",              "Coupling (global/static vars, fan-out, recursion)"),
        ("func_metrics",          "Function count, max length & static variables"),
        ("safety_indicators",     "Safety indicators (goto, void ptr, casts, asserts)"),
        ("macro_metrics",         "Macro count & assert density"),
    ]

    for branch in BRANCHES:
        lines.append(f"## {branch.capitalize()} branch")
        lines.append("")
        pt = points[branch]
        if pt:
            commit = pt.get("commit", "?")
            ts     = pt.get("timestamp", "?")[:10]
            lines.append(f"*Last updated: commit `{commit}` on {ts}*")
        lines.append("")

        for key, title in chart_keys:
            svg_url = f"{base}/{branch}_{key}.svg"
            lines.append(f"### {title}")
            lines.append("")
            lines.append(f"![{title}]({svg_url})")
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("*Generated by `scripts/update_wiki_metrics.py` "
                 "via `.github/workflows/metrics.yml`.*")

    Path(args.output).write_text("\n".join(lines), encoding="utf-8")
    print(f"[wiki] Wrote {args.output}")


if __name__ == "__main__":
    main()
