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
        return _empty_cstylecheck_metrics()

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
        return _empty_cstylecheck_metrics()

    return _summarise_violations(data)


def _empty_cstylecheck_metrics():
    return {"errors": 0, "warnings": 0, "info": 0, "total": 0,
            "files_checked": 0, "rules_violated": [],
            "violations_by_category": {}, "files_zero_violations": 0,
            "top_rules": []}


def _summarise_violations(data):
    """
    Summarise a CStyleCheck JSON report (``{"summary": …, "violations": […]}``).

    Besides the severity totals this derives the violation-quality metrics
    of issue #388: violations by rule category (the rule-ID prefix before
    the first '.'), number of checked files with zero violations and the
    five most frequently violated rules.
    """
    from collections import Counter
    summary    = data.get("summary", {}) or {}
    violations = data.get("violations", []) or []

    by_rule     = Counter(v.get("rule", "unknown") for v in violations)
    by_category = Counter(v.get("rule", "unknown").split(".", 1)[0]
                          for v in violations)
    files_with  = {v.get("file") for v in violations if v.get("file")}
    files_checked = summary.get("files_checked", 0)

    return {
        "errors":        summary.get("errors",   0),
        "warnings":      summary.get("warnings", 0),
        "info":          summary.get("info",     0),
        "total":         summary.get("total",    0),
        "files_checked": files_checked,
        "rules_violated": [{"rule": r, "count": c}
                           for r, c in by_rule.most_common()],
        "violations_by_category": dict(sorted(by_category.items())),
        "files_zero_violations": max(0, files_checked - len(files_with)),
        "top_rules": [{"rule": r, "count": c}
                      for r, c in by_rule.most_common(5)],
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
#
# All analysis is pure-Python and heuristic (regex / lexical state machine);
# no compiler or preprocessor is invoked.  Keyword-based counts are always
# taken from text in which comments and string/char literals have been
# blanked out (see strip_comments_and_strings()), so keywords appearing in
# comments or strings are never counted.
#
# Threshold values below are documented in scripts/metrics_rules.yml.
# --------------------------------------------------------------------------

FUNC_LENGTH_LIMIT = 60      # lines   — Barr-C:2018 §6.x / JPL Power of 10 R4
FUNC_PARAM_LIMIT  = 5       # params  — HIS metric "PARAM" limit
CC_LIMIT          = 10      # V(G)    — McCabe / HIS "v(G)" limit
# Cyclomatic-complexity histogram buckets: (field suffix, low, high)
CC_BUCKETS = (
    ("1_5",     1,  5),
    ("6_10",    6, 10),
    ("11_15",  11, 15),
    ("16_plus", 16, None),
)

# C keywords / operators that look like calls ("if (", "sizeof (") and
# must therefore be excluded from fan-out counting.
C_KEYWORDS = frozenset({
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto", "if",
    "inline", "int", "long", "register", "restrict", "return", "short",
    "signed", "sizeof", "static", "struct", "switch", "typedef", "union",
    "unsigned", "void", "volatile", "while", "_Alignas", "_Alignof",
    "_Atomic", "_Bool", "_Complex", "_Generic", "_Imaginary", "_Noreturn",
    "_Static_assert", "_Thread_local", "alignof", "alignas",
    "static_assert", "defined", "__attribute__", "__asm__", "asm",
    "__declspec", "__typeof__", "typeof",
})

# Words that can never be the name of a function definition header.
_NON_FUNC_NAMES = frozenset({
    "if", "while", "for", "switch", "return", "sizeof", "do", "else",
    "case", "goto", "__attribute__", "__declspec", "_Alignas", "alignas",
    "_Static_assert", "static_assert", "asm", "__asm__",
})


def _empty_c_metrics():
    m = {
        "loc_physical": 0, "loc_blank": 0, "loc_comment": 0, "loc_doxygen": 0,
        "loc_sloc": 0, "loc_comment_density": 0.0, "loc_blank_ratio": 0.0,
        "c_file_count": 0, "h_file_count": 0,
        "func_count": 0, "func_length_max": 0, "func_length_avg": 0.0,
        "func_over_length": 0, "func_param_max": 0, "func_over_params": 0,
        "cc_max": 0, "cc_avg": 0.0, "cc_over_threshold": 0,
        "nesting_max": 0, "dox_coverage": 0.0, "dox_coverage_pct": 0.0,
        "global_vars": 0, "static_vars": 0, "file_length_max": 0,
        "fanout_avg": 0.0, "recursive_func_count": 0,
        "defect_density": 0.0,
        # Safety/style counters
        "assert_count": 0, "assert_density": 0.0,
        "goto_count": 0, "void_ptr_count": 0,
        "cast_count": 0, "macro_count": 0,
    }
    for suffix, _lo, _hi in CC_BUCKETS:
        m[f"cc_bucket_{suffix}"] = 0
    return m


# ---- Lexical helpers -----------------------------------------------------

def strip_comments_and_strings(text):
    """
    Return *text* with every comment and the contents of every string and
    character literal replaced by spaces.

    Newlines are preserved and the result has exactly the same length as the
    input, so character offsets and line numbers map 1:1 onto the original.
    String/char delimiters are kept (``"abc"`` becomes ``"   "``).
    """
    out = list(text)
    n = len(text)
    i = 0
    NORMAL, LINE_CMT, BLOCK_CMT, STRING, CHAR = range(5)
    state = NORMAL
    while i < n:
        c = text[i]
        nxt = text[i + 1] if i + 1 < n else ""
        if state == NORMAL:
            if c == "/" and nxt == "/":
                state = LINE_CMT
                out[i] = out[i + 1] = " "
                i += 2
                continue
            if c == "/" and nxt == "*":
                state = BLOCK_CMT
                out[i] = out[i + 1] = " "
                i += 2
                continue
            if c == '"':
                state = STRING
            elif c == "'":
                state = CHAR
            i += 1
            continue
        if state == LINE_CMT:
            if c == "\n":
                state = NORMAL
            else:
                out[i] = " "
            i += 1
            continue
        if state == BLOCK_CMT:
            if c == "*" and nxt == "/":
                out[i] = out[i + 1] = " "
                state = NORMAL
                i += 2
                continue
            if c != "\n":
                out[i] = " "
            i += 1
            continue
        # STRING / CHAR literal
        quote = '"' if state == STRING else "'"
        if c == "\\" and i + 1 < n:
            out[i] = " "
            if nxt != "\n":
                out[i + 1] = " "
            i += 2
            continue
        if c == quote or c == "\n":     # unterminated literal ends at EOL
            state = NORMAL
        else:
            out[i] = " "
        i += 1
    return "".join(out)


def blank_preprocessor_lines(code):
    """
    Blank out preprocessor directives (including backslash-continued lines)
    in comment-stripped *code*, preserving line structure.
    """
    lines = code.split("\n")
    in_directive = False
    for idx, line in enumerate(lines):
        if in_directive or line.lstrip().startswith("#"):
            in_directive = line.rstrip().endswith("\\")
            lines[idx] = " " * len(line)
    return "\n".join(lines)


def classify_lines(text):
    """
    Classify every physical line of *text*.

    Returns a dict with keys ``physical``, ``blank``, ``comment``,
    ``doxygen`` and ``sloc``:

    * blank   — whitespace only (also inside a block comment)
    * sloc    — contains at least one non-comment, non-whitespace character
    * doxygen — comment-only line belonging to a ``/** */``, ``/*! */``,
                ``///`` or ``//!`` comment
    * comment — any other comment-only line

    ``physical == blank + comment + doxygen + sloc`` always holds.
    """
    counts = {"physical": 0, "blank": 0, "comment": 0, "doxygen": 0, "sloc": 0}
    in_block = False
    block_is_dox = False
    in_str = None                       # quote char of a multi-line literal
    for line in text.splitlines():
        counts["physical"] += 1
        if not line.strip():
            counts["blank"] += 1
            continue
        has_code = has_cmt = has_dox = False
        i, n = 0, len(line)
        while i < n:
            c = line[i]
            nxt = line[i + 1] if i + 1 < n else ""
            if in_block:
                if block_is_dox:
                    has_dox = True
                else:
                    has_cmt = True
                if c == "*" and nxt == "/":
                    in_block = False
                    i += 2
                    continue
                i += 1
                continue
            if in_str:
                has_code = True
                if c == "\\":
                    i += 2
                    continue
                if c == in_str:
                    in_str = None
                i += 1
                continue
            if c == "/" and nxt == "/":
                rest = line[i:]
                if (rest.startswith("///") and not rest.startswith("////")) \
                        or rest.startswith("//!"):
                    has_dox = True
                else:
                    has_cmt = True
                break
            if c == "/" and nxt == "*":
                rest = line[i:]
                block_is_dox = ((rest.startswith("/**") and not rest.startswith("/**/")
                                 and not rest.startswith("/***"))
                                or rest.startswith("/*!"))
                in_block = True
                i += 2
                continue
            if c in "\"'":
                in_str = c
                has_code = True
                i += 1
                continue
            if not c.isspace():
                has_code = True
            i += 1
        # A literal cannot span lines without a backslash continuation.
        if in_str and not line.endswith("\\"):
            in_str = None
        if has_code:
            counts["sloc"] += 1
        elif has_dox:
            counts["doxygen"] += 1
        elif has_cmt:
            counts["comment"] += 1
        else:                           # e.g. a lone "*/" is still a comment
            counts["comment"] += 1
    return counts


def _cat_lines(lines):
    """Backward-compatible wrapper → (physical, blank, comment, doxygen, sloc)."""
    c = classify_lines("\n".join(lines))
    return c["physical"], c["blank"], c["comment"], c["doxygen"], c["sloc"]


def _split_top_level(s, sep=","):
    """Split *s* on *sep* occurring outside (), [] and {}."""
    parts, depth, cur = [], 0, []
    for ch in s:
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth = max(0, depth - 1)
        if ch == sep and depth == 0:
            parts.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    parts.append("".join(cur))
    return parts


def count_params(param_text):
    """Number of parameters in a parameter-list string (``void`` → 0)."""
    p = param_text.strip()
    if not p or p == "void":
        return 0
    return len([x for x in _split_top_level(p) if x.strip()])


_RE_DECISION = re.compile(r"\b(?:if|while|for|case)\b|&&|\|\||\?")


def cyclomatic_complexity(body_code):
    """
    McCabe V(G) = 1 + decision points in comment/string-stripped *body_code*.

    Decision points: ``if`` (so ``else if`` counts once), ``while`` (so a
    ``do … while`` counts once), ``for``, ``case``, ``&&``, ``||`` and ``?``.
    """
    return 1 + len(_RE_DECISION.findall(body_code))


def max_brace_nesting(body_code):
    """
    Maximum brace nesting depth *inside* a function body, where
    *body_code* starts at the function's opening brace.  A body with no
    inner blocks has depth 0.
    """
    depth = max_depth = 0
    for ch in body_code:
        if ch == "{":
            depth += 1
            max_depth = max(max_depth, depth)
        elif ch == "}":
            depth -= 1
    return max(0, max_depth - 1)


_RE_CALL = re.compile(r"\b([A-Za-z_]\w*)\s*\(")


def called_identifiers(body_code):
    """Unique identifiers used in call position, excluding C keywords."""
    return {m.group(1) for m in _RE_CALL.finditer(body_code)
            if m.group(1) not in C_KEYWORDS}


_RE_FUNC_HEADER = re.compile(
    r"([A-Za-z_]\w*)\s*\(((?:[^()]|\([^()]*\))*)\)\s*$", re.S)
_RE_EXTERN_C = re.compile(r'extern\s*"\s*"\s*$')


def _has_doxygen_before(text, pos):
    """True if the original *text* has a doxygen comment ending just before *pos*."""
    before = text[:pos].rstrip()
    if before.endswith("*/"):
        start = before.rfind("/*")
        if start < 0:
            return False
        opener = before[start:start + 3]
        return opener in ("/**", "/*!") and before[start:start + 4] != "/**/"
    last = before.rsplit("\n", 1)[-1].strip()
    return last.startswith("///") or last.startswith("//!")


def extract_functions(text):
    """
    Locate C function *definitions* in *text* (prototypes are ignored).

    Returns a list of dicts with keys: name, start_line (1-based), length
    (lines from the name line to the closing brace, inclusive), params,
    complexity, nesting, has_dox, calls (set of called identifiers) and
    recursive (bool).
    """
    code = blank_preprocessor_lines(strip_comments_and_strings(text))
    funcs = []
    n = len(code)
    depth = 0
    header_start = 0
    i = 0
    while i < n:
        ch = code[i]
        if ch in ";}" and depth == 0:
            header_start = i + 1
        elif ch == "{" and depth == 0:
            header = code[header_start:i]
            if _RE_EXTERN_C.search(header):
                # extern "C" { … } — braces are transparent
                header_start = i + 1
                i += 1
                continue
            m = _RE_FUNC_HEADER.search(header)
            first_tok = header.split()[0] if header.split() else ""
            is_func = (
                m is not None
                and "=" not in header
                and m.group(1) not in _NON_FUNC_NAMES
                and first_tok not in ("typedef", "struct", "union", "enum")
            )
            # find matching close brace
            d = 0
            j = i
            while j < n:
                if code[j] == "{":
                    d += 1
                elif code[j] == "}":
                    d -= 1
                    if d == 0:
                        break
                j += 1
            end = min(j, n - 1)
            if is_func:
                name = m.group(1)
                body = code[i:end + 1]
                lead = len(header) - len(header.lstrip())
                sig_pos = header_start + lead
                start_line = code.count("\n", 0, sig_pos) + 1
                end_line = code.count("\n", 0, end) + 1
                calls = called_identifiers(body)
                funcs.append({
                    "name":       name,
                    "start_line": start_line,
                    "length":     end_line - start_line + 1,
                    "params":     count_params(m.group(2)),
                    "complexity": cyclomatic_complexity(body),
                    "nesting":    max_brace_nesting(body),
                    "has_dox":    _has_doxygen_before(text, sig_pos),
                    "calls":      calls,
                    "recursive":  name in calls,
                })
                header_start = end + 1
                i = end + 1
                continue
            # Not a function (struct/enum/initializer): skip over the braces
            # but keep accumulating the statement until its ';'.
            i = end + 1
            continue
        elif ch == "{":
            depth += 1
        elif ch == "}" and depth > 0:
            depth -= 1
        i += 1
    return funcs


def _extract_functions(text):
    """Backward-compatible alias for extract_functions()."""
    return extract_functions(text)


def count_file_scope_variables(text):
    """
    Count file-scope variable *definitions* in C source *text*.

    Returns ``(global_count, static_count)``: ``global_count`` covers
    non-static, non-extern definitions; ``static_count`` covers ``static``
    ones.  Each declarator counts once (``int a, b;`` → 2).  Typedefs,
    ``extern`` declarations, function prototypes and pure type definitions
    (``struct s { … };``) are not counted.
    """
    code = blank_preprocessor_lines(strip_comments_and_strings(text))
    globals_n = statics_n = 0
    for stmt in _top_level_statements(code):
        s = " ".join(stmt.split())
        if not s:
            continue
        toks = re.findall(r"[A-Za-z_]\w*", s.split("{", 1)[0])
        if not toks or toks[0] in ("typedef",) or "extern" in toks[:3] \
                or toks[0] in ("_Static_assert", "static_assert", "asm", "__asm__"):
            continue
        is_static = "static" in toks
        # Remove brace bodies of struct/union/enum type specifiers so that
        # "struct s { int a; } v;" leaves "struct s v".
        decl = s
        eq = _find_top_level(decl, "=")
        head = decl if eq < 0 else decl[:eq]
        if "{" in head:
            after = head[head.rfind("}") + 1:]
            if not re.search(r"[A-Za-z_]", after):
                continue                # pure type definition
            tail = decl[len(head):] if eq >= 0 else ""
            # Replace the aggregate type by a placeholder type name.
            decl = "T " + after + tail
        count = 0
        for idx, part in enumerate(_split_top_level(decl)):
            p = part.split("=", 1)[0].strip()
            if not p:
                continue
            # function prototype: name directly followed by '(' and not a
            # function pointer declarator "(*name)"
            if re.search(r"[A-Za-z_]\w*\s*\(", p) and not re.search(r"\(\s*\*", p):
                continue
            if idx == 0:
                words = re.findall(r"[A-Za-z_]\w*", p)
                # "struct s" / "enum e" alone → type definition, no variable
                if len(words) <= 2 and words and words[0] in ("struct", "union", "enum"):
                    continue
                if len(words) < 2 and not re.search(r"[*\[(]", p):
                    continue
            count += 1
        if is_static:
            statics_n += count
        else:
            globals_n += count
    return globals_n, statics_n


def _find_top_level(s, ch):
    depth = 0
    for i, c in enumerate(s):
        if c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        elif c == ch and depth == 0:
            return i
    return -1


def _top_level_statements(code):
    """
    Yield the text of each ';'-terminated statement at file scope, skipping
    function bodies entirely.
    """
    depth = 0
    start = 0
    i, n = 0, len(code)
    while i < n:
        c = code[i]
        if c == "{":
            if depth == 0:
                header = code[start:i]
                if _RE_EXTERN_C.search(header):
                    start = i + 1
                    i += 1
                    continue
                m = _RE_FUNC_HEADER.search(header)
                if m and "=" not in header and m.group(1) not in _NON_FUNC_NAMES \
                        and (header.split() or [""])[0] not in ("typedef", "struct",
                                                                "union", "enum"):
                    # function definition — skip its body
                    d = 0
                    while i < n:
                        if code[i] == "{":
                            d += 1
                        elif code[i] == "}":
                            d -= 1
                            if d == 0:
                                break
                        i += 1
                    start = i + 1
                    i += 1
                    continue
            depth += 1
        elif c == "}":
            if depth == 0:              # closing brace of extern "C"
                start = i + 1
            depth = max(0, depth - 1)
        elif c == ";" and depth == 0:
            yield code[start:i]
            start = i + 1
        i += 1


def _count_static_vars(text):
    """Count static variable definitions at file scope in a .c file."""
    return count_file_scope_variables(text)[1]


# Safety/style counters (applied to comment/string-stripped text)
_RE_ASSERT    = re.compile(r'\bassert\s*\(')
_RE_GOTO_MET  = re.compile(r'\bgoto\b')
_RE_VOID_PTR  = re.compile(r'\bvoid\s*\*')
_RE_C_CAST    = re.compile(
    r'\(\s*(?:const\s+)?(?:unsigned\s+|signed\s+)?'
    r'[a-zA-Z_]\w*(?:\s*\*+)?\s*\)\s*(?=[a-zA-Z_(0-9])'
)
_RE_MACRO_DEF = re.compile(r'^\s*#\s*define\s+(\w+)', re.MULTILINE)
_RE_INC_GUARD = re.compile(r'^[A-Z0-9_]+_H(?:_|PP)?(?:_\w+)?$')


def _cc_bucket(cc):
    for suffix, lo, hi in CC_BUCKETS:
        if cc >= lo and (hi is None or cc <= hi):
            return suffix
    return CC_BUCKETS[0][0]


def _c_source_metrics(total_violations=0, source_dir=None):
    """
    Analyse <source_dir>/*.c and *.h (default: examples/) for
    industry-standard C source metrics.  *total_violations* is used to
    compute defect density (violations per KLOC of SLOC).
    """
    src = Path(source_dir) if source_dir is not None else EXAMPLES
    c_files = sorted(src.glob("*.c"))
    h_files = sorted(src.glob("*.h"))
    all_files = c_files + h_files

    if not all_files:
        return _empty_c_metrics()

    loc = {"physical": 0, "blank": 0, "comment": 0, "doxygen": 0, "sloc": 0}
    all_funcs = []
    total_global_v = total_static_v = 0
    max_file_len = 0
    total_assert = total_goto = total_void_ptr = total_cast = total_macro = 0

    for fpath in all_files:
        try:
            text = fpath.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        n_lines = len(text.splitlines())
        max_file_len = max(max_file_len, n_lines)

        for k, v in classify_lines(text).items():
            loc[k] += v

        code = strip_comments_and_strings(text)
        total_assert   += len(_RE_ASSERT.findall(code))
        total_goto     += len(_RE_GOTO_MET.findall(code))
        total_void_ptr += len(_RE_VOID_PTR.findall(code))
        total_cast     += len(_RE_C_CAST.findall(blank_preprocessor_lines(code)))
        for m in _RE_MACRO_DEF.finditer(code):
            if not _RE_INC_GUARD.match(m.group(1)):
                total_macro += 1

        if fpath.suffix == ".c":
            all_funcs.extend(extract_functions(text))
            g, s = count_file_scope_variables(text)
            total_global_v += g
            total_static_v += s

    n = len(all_funcs)
    lengths      = [f["length"]     for f in all_funcs]
    complexities = [f["complexity"] for f in all_funcs]
    params_list  = [f["params"]     for f in all_funcs]
    nestings     = [f["nesting"]    for f in all_funcs]
    fanouts      = [len(f["calls"] - {f["name"]}) for f in all_funcs]
    dox_covered  = sum(1 for f in all_funcs if f["has_dox"])

    sloc = loc["sloc"]
    kloc = sloc / 1000.0
    dox_ratio = round(dox_covered / n, 3) if n else 0.0

    result = {
        # Lines of code (IEC 61508-3 Annex B, ISO 26262-6)
        "loc_physical":        loc["physical"],
        "loc_blank":           loc["blank"],
        "loc_comment":         loc["comment"],
        "loc_doxygen":         loc["doxygen"],
        "loc_sloc":            sloc,
        "loc_comment_density": round((loc["comment"] + loc["doxygen"]) / sloc, 3) if sloc else 0.0,
        "loc_blank_ratio":     round(loc["blank"] / loc["physical"], 3) if loc["physical"] else 0.0,
        # File counts
        "c_file_count":        len(c_files),
        "h_file_count":        len(h_files),
        # Function metrics (Barr-C §6, JPL Power of 10, HIS)
        "func_count":          n,
        "func_length_max":     max(lengths, default=0),
        "func_length_avg":     round(sum(lengths) / n, 1) if n else 0.0,
        "func_over_length":    sum(1 for l in lengths if l > FUNC_LENGTH_LIMIT),
        "func_param_max":      max(params_list, default=0),
        "func_over_params":    sum(1 for p in params_list if p > FUNC_PARAM_LIMIT),
        # Cyclomatic complexity (McCabe, ISO 26262-6 §8.4.4)
        "cc_max":              max(complexities, default=0),
        "cc_avg":              round(sum(complexities) / n, 2) if n else 0.0,
        "cc_over_threshold":   sum(1 for c in complexities if c > CC_LIMIT),
        # Control-flow nesting depth (JSF AV / automotive profiles, <= 5)
        "nesting_max":         max(nestings, default=0),
        # Documentation coverage (ASPICE SWE.3/SWE.4)
        "dox_coverage":        dox_ratio,
        "dox_coverage_pct":    round(dox_ratio * 100, 1),
        # Variables / coupling (AUTOSAR BSW, JSF AV Rule 137, HIS)
        "global_vars":         total_global_v,
        "static_vars":         total_static_v,
        "fanout_avg":          round(sum(fanouts) / n, 2) if n else 0.0,
        "recursive_func_count": sum(1 for f in all_funcs if f["recursive"]),
        # File-level metrics
        "file_length_max":     max_file_len,
        # Defect density (violations per KLOC SLOC) — ASPICE SWE.4 maturity index
        "defect_density":      round(total_violations / kloc, 2) if sloc else 0.0,
        # Safety / style counters (CERT C, MISRA C:2012)
        "assert_count":        total_assert,
        "assert_density":      round(total_assert / kloc, 2) if sloc else 0.0,
        "goto_count":          total_goto,
        "void_ptr_count":      total_void_ptr,
        "cast_count":          total_cast,
        "macro_count":         total_macro,
    }
    for suffix, _lo, _hi in CC_BUCKETS:
        result[f"cc_bucket_{suffix}"] = 0
    for c in complexities:
        result[f"cc_bucket_{_cc_bucket(c)}"] += 1
    return result


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
        # Violation quality (issue #388) — severity distribution is given by
        # errors / warnings / info_count; violations per KLOC SLOC by
        # defect_density below.
        "violations_by_category": csc["violations_by_category"],
        "files_zero_violations":  csc["files_zero_violations"],
        "top_rules":              csc["top_rules"],
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
        # Safety / style counters (CERT C, MISRA C:2012)
        "assert_count":        c_metrics["assert_count"],
        "assert_density":      c_metrics["assert_density"],
        "goto_count":          c_metrics["goto_count"],
        "void_ptr_count":      c_metrics["void_ptr_count"],
        "cast_count":          c_metrics["cast_count"],
        "macro_count":         c_metrics["macro_count"],
        # Extended C source metrics (issue #388)
        "c_file_count":        c_metrics["c_file_count"],
        "h_file_count":        c_metrics["h_file_count"],
        "cc_bucket_1_5":       c_metrics["cc_bucket_1_5"],
        "cc_bucket_6_10":      c_metrics["cc_bucket_6_10"],
        "cc_bucket_11_15":     c_metrics["cc_bucket_11_15"],
        "cc_bucket_16_plus":   c_metrics["cc_bucket_16_plus"],
        "dox_coverage_pct":    c_metrics["dox_coverage_pct"],
        "global_vars":         c_metrics["global_vars"],
        "fanout_avg":          c_metrics["fanout_avg"],
        "recursive_func_count": c_metrics["recursive_func_count"],
    }

    # --- load, upsert, save ---
    branch_safe = branch.replace("/", "-").replace("\\", "-")
    hist_path = output_dir / f"{branch_safe}.json"
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
