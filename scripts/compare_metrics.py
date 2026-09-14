#!/usr/bin/env python3
"""
compare_metrics.py - Compare PR-branch metrics against a stored baseline.

Usage:
    python3 scripts/compare_metrics.py \
        --current  metrics/<branch>.json \
        --baseline /path/to/develop.json \
        --baseline-name develop \
        --output   metrics-report.md
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


# (json_key, display_label, higher_is_better)
# higher_is_better=True  → increase is good (green)
# higher_is_better=False → increase is bad  (red)
# higher_is_better=None  → neutral / informational
METRICS = [
    # CStyleCheck violations
    ("errors",             "Errors",               False),
    ("warnings",           "Warnings",              False),
    ("info_count",         "Info violations",       False),
    ("total_violations",   "Total violations",      False),
    # Tool stats
    ("test_count",         "Test count",            True),
    ("rule_count",         "Rule count",            True),
    # Lines of code
    ("loc_sloc",           "SLOC",                  None),
    ("loc_physical",       "Physical lines",        None),
    ("loc_comment",        "Comment lines",         None),
    ("loc_doxygen",        "Doxygen lines",         None),
    ("loc_comment_density","Comment density",       True),
    ("loc_blank_ratio",    "Blank ratio",           None),
    # Function metrics
    ("func_count",         "Function count",        None),
    ("func_length_max",    "Max function length",   False),
    ("func_length_avg",    "Avg function length",   False),
    ("func_over_length",   "Functions over 60 LOC", False),
    ("func_param_max",     "Max parameters",        False),
    ("func_over_params",   "Functions over 6 params", False),
    # Cyclomatic complexity
    ("cc_max",             "CC max",                False),
    ("cc_avg",             "CC avg",                False),
    ("cc_over_threshold",  "Functions CC > 10",     False),
    ("nesting_max",        "Max nesting depth",     False),
    # Documentation / variables
    ("dox_coverage",       "Doxygen coverage",      True),
    ("static_vars",        "Static variables",      None),
    ("file_length_max",    "Max file length",       False),
    # Quality index
    ("defect_density",     "Defect density (v/KLOC)", False),
]


def _load_last(path):
    """Return the last data_point from a branch JSON, or {} if unavailable."""
    p = Path(path)
    if not p.exists():
        return {}
    try:
        h = json.loads(p.read_text())
        pts = h.get("data_points", [])
        return pts[-1] if pts else {}
    except Exception:
        return {}


def _fmt(v):
    if v is None:
        return "—"
    if isinstance(v, float):
        return f"{v:.3f}" if abs(v) < 10 else f"{v:.1f}"
    return str(v)


def _delta_str(current, baseline, higher_is_better):
    """Return (delta_str, emoji) for a numeric change."""
    if current is None or baseline is None:
        return "—", ""
    if not isinstance(current, (int, float)) or not isinstance(baseline, (int, float)):
        return "—", ""

    diff = current - baseline
    if diff == 0:
        return "0", "="

    sign = "+" if diff > 0 else ""
    if isinstance(diff, float):
        delta = f"{sign}{diff:.3f}" if abs(diff) < 10 else f"{sign}{diff:.1f}"
    else:
        delta = f"{sign}{diff}"

    if higher_is_better is None:
        emoji = "→"
    elif (diff > 0) == higher_is_better:
        emoji = "✅"
    else:
        emoji = "⚠️"

    return delta, emoji


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--current",       required=True,
                    help="Path to current branch JSON (e.g. metrics/my-branch.json)")
    ap.add_argument("--baseline",      required=True,
                    help="Path to baseline JSON (e.g. /tmp/develop.json)")
    ap.add_argument("--baseline-name", default="develop",
                    help="Label for the baseline branch")
    ap.add_argument("--output",        default="metrics-report.md")
    args = ap.parse_args()

    current  = _load_last(args.current)
    baseline = _load_last(args.baseline)
    now      = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    cur_commit  = current.get("commit",    "?")
    base_commit = baseline.get("commit",   "?")
    cur_ts      = current.get("timestamp", "")[:10]
    base_ts     = baseline.get("timestamp","")[:10]

    improvements = 0
    regressions  = 0
    neutral      = 0
    rows         = []

    for key, label, hib in METRICS:
        cv = current.get(key)
        bv = baseline.get(key)
        delta, emoji = _delta_str(cv, bv, hib)
        rows.append((label, _fmt(bv), _fmt(cv), delta, emoji))
        if emoji == "✅":
            improvements += 1
        elif emoji == "⚠️":
            regressions += 1
        else:
            neutral += 1

    lines = [
        "# CStyleCheck — Metrics comparison report",
        "",
        f"*Generated {now}*",
        "",
        "| | |",
        "|---|---|",
        f"| **PR branch** | `{cur_commit}` ({cur_ts}) |",
        f"| **Baseline** (`{args.baseline_name}`) | `{base_commit}` ({base_ts}) |",
        "",
        "---",
        "",
        "## Summary",
        "",
        f"- ✅ **{improvements}** improvements",
        f"- ⚠️ **{regressions}** regressions",
        f"- = **{neutral}** unchanged / neutral",
        "",
    ]

    if regressions:
        lines += [
            "### Regressions",
            "",
            "| Metric | Baseline | PR | Delta |",
            "|---|---|---|---|",
        ]
        for label, bv, cv, delta, emoji in rows:
            if emoji == "⚠️":
                lines.append(f"| {label} | {bv} | {cv} | ⚠️ {delta} |")
        lines.append("")

    lines += [
        "---",
        "",
        "## Full comparison",
        "",
        f"| Metric | {args.baseline_name} | PR branch | Delta | |",
        "|---|---|---|---|---|",
    ]
    for label, bv, cv, delta, emoji in rows:
        lines.append(f"| {label} | {bv} | {cv} | {delta} | {emoji} |")

    lines += [
        "",
        "---",
        "",
        "*Legend: ✅ improvement · ⚠️ regression · → neutral change · = no change*",
        "",
        "*Generated by `scripts/compare_metrics.py` "
        "via `.github/workflows/metrics.yml`.*",
    ]

    Path(args.output).write_text("\n".join(lines), encoding="utf-8")
    print(f"[compare] Wrote {args.output} "
          f"({improvements} improvements, {regressions} regressions)")


if __name__ == "__main__":
    main()
