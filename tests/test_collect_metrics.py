"""test_collect_metrics.py — tests for the trend-analysis C source metrics
(scripts/collect_metrics.py, scripts/generate_charts.py,
scripts/update_wiki_metrics.py; issue #388)."""
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"


def _load(name):
    spec = importlib.util.spec_from_file_location(name, _SCRIPTS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


cm = _load("collect_metrics")
gc = _load("generate_charts")
wm = _load("update_wiki_metrics")


def _funcs(src):
    return {f["name"]: f for f in cm.extract_functions(src)}


# --------------------------------------------------------------------------
# Lexical helpers
# --------------------------------------------------------------------------

class TestStripCommentsAndStrings(unittest.TestCase):

    def test_length_and_newlines_preserved(self):
        src = 'int a; /* x\ny */ // z\nchar *s = "if (a)";\n'
        out = cm.strip_comments_and_strings(src)
        self.assertEqual(len(out), len(src))
        self.assertEqual(out.count("\n"), src.count("\n"))

    def test_comments_removed(self):
        out = cm.strip_comments_and_strings("a; /* if while */ b; // for\n")
        self.assertNotIn("if", out)
        self.assertNotIn("for", out)
        self.assertIn("a;", out)
        self.assertIn("b;", out)

    def test_string_contents_blanked(self):
        out = cm.strip_comments_and_strings('x = "goto /* not */ a";')
        self.assertNotIn("goto", out)
        self.assertIn('"', out)

    def test_escaped_quote_in_string(self):
        out = cm.strip_comments_and_strings('s = "a\\"if"; if (x) {}')
        self.assertEqual(out.count("if"), 1)

    def test_char_literals(self):
        out = cm.strip_comments_and_strings("c = '{'; d = '\\'';")
        self.assertNotIn("{", out)

    def test_comment_markers_inside_string_ignored(self):
        out = cm.strip_comments_and_strings('s = "//"; t = 1;')
        self.assertIn("t = 1;", out)

    def test_blank_preprocessor_lines(self):
        code = "#define M(x) \\\n  do { x; } while (0)\nint a;\n"
        out = cm.blank_preprocessor_lines(code)
        self.assertNotIn("do", out)
        self.assertIn("int a;", out)
        self.assertEqual(out.count("\n"), code.count("\n"))


# --------------------------------------------------------------------------
# LOC classification
# --------------------------------------------------------------------------

class TestClassifyLines(unittest.TestCase):

    def test_basic_categories(self):
        src = (
            "/** Brief.\n"          # doxygen
            " * detail\n"           # doxygen
            " */\n"                 # doxygen
            "\n"                    # blank
            "/* plain */\n"         # comment
            "// line\n"             # comment
            "/// dox line\n"        # doxygen
            "int a; // trailing\n"  # sloc
            "   \n"                 # blank
            "int b;\n"              # sloc
        )
        c = cm.classify_lines(src)
        self.assertEqual(c["physical"], 10)
        self.assertEqual(c["blank"], 2)
        self.assertEqual(c["doxygen"], 4)
        self.assertEqual(c["comment"], 2)
        self.assertEqual(c["sloc"], 2)

    def test_sum_invariant(self):
        src = "a;\n/*\n x\n*/ b;\n\n//c\n"
        c = cm.classify_lines(src)
        self.assertEqual(c["physical"],
                         c["blank"] + c["comment"] + c["doxygen"] + c["sloc"])

    def test_code_after_block_comment_end_is_sloc(self):
        c = cm.classify_lines("/* a\n b */ int x;\n")
        self.assertEqual(c["comment"], 1)
        self.assertEqual(c["sloc"], 1)

    def test_comment_marker_in_string_is_code(self):
        c = cm.classify_lines('char *s = "/* not a comment";\nint y;\n')
        self.assertEqual(c["sloc"], 2)
        self.assertEqual(c["comment"], 0)

    def test_empty_block_and_banner_not_doxygen(self):
        c = cm.classify_lines("/**/\n/*****************/\n")
        self.assertEqual(c["doxygen"], 0)
        self.assertEqual(c["comment"], 2)

    def test_qt_style_doxygen(self):
        c = cm.classify_lines("/*! brief */\n//! more\n")
        self.assertEqual(c["doxygen"], 2)

    def test_empty_text(self):
        c = cm.classify_lines("")
        self.assertEqual(c["physical"], 0)
        self.assertEqual(c["sloc"], 0)

    def test_cat_lines_compat_wrapper(self):
        self.assertEqual(cm._cat_lines(["int a;", "", "// c"]), (3, 1, 1, 0, 1))


# --------------------------------------------------------------------------
# Function extraction / complexity
# --------------------------------------------------------------------------

class TestExtractFunctions(unittest.TestCase):

    def test_prototype_not_counted(self):
        src = "int foo(int a);\nint foo(int a)\n{\n    return a;\n}\n"
        f = cm.extract_functions(src)
        self.assertEqual(len(f), 1)
        self.assertEqual(f[0]["name"], "foo")

    def test_struct_enum_and_initialiser_not_functions(self):
        src = ("struct s { int a; };\n"
               "enum e { A, B };\n"
               "typedef struct { int b; } t_s;\n"
               "int arr[] = { 1, 2 };\n"
               "void f(void) { }\n")
        self.assertEqual(list(_funcs(src)), ["f"])

    def test_length_counts_name_line_to_closing_brace(self):
        src = "static int\nfoo(int a,\n    int b)\n{\n    return a + b;\n}\n"
        f = _funcs(src)["foo"]
        self.assertEqual(f["start_line"], 1)
        self.assertEqual(f["length"], 6)

    def test_param_counting(self):
        src = ("void a(void) {}\n"
               "void b() {}\n"
               "void c(int x, int y, int z) {}\n"
               "void d(void (*cb)(int, int), int n) {}\n"
               "int e(const char *fmt, ...) { return 0; }\n")
        f = _funcs(src)
        self.assertEqual(f["a"]["params"], 0)
        self.assertEqual(f["b"]["params"], 0)
        self.assertEqual(f["c"]["params"], 3)
        self.assertEqual(f["d"]["params"], 2)
        self.assertEqual(f["e"]["params"], 2)

    def test_braces_in_strings_and_comments_ignored(self):
        src = ('void f(void)\n{\n    char *s = "}}}";\n    /* { */\n'
               '    int x = 0;\n}\nvoid g(void) { }\n')
        f = _funcs(src)
        self.assertEqual(set(f), {"f", "g"})
        self.assertEqual(f["f"]["length"], 6)

    def test_extern_c_block_is_transparent(self):
        src = 'extern "C" {\nvoid f(void) { }\n}\n'
        self.assertEqual(list(_funcs(src)), ["f"])

    def test_macro_with_braces_ignored(self):
        src = "#define WRAP(x) do { x; } while (0)\nvoid f(void) { }\n"
        self.assertEqual(list(_funcs(src)), ["f"])


class TestCyclomaticComplexity(unittest.TestCase):

    def test_straight_line_is_one(self):
        self.assertEqual(_funcs("void f(void) { int a = 1; }")["f"]["complexity"], 1)

    def test_decision_points(self):
        src = """
int f(int a, int b)
{
    if (a && b) { a++; }
    else if (a || b) { b++; }
    else { }
    while (a > 0) { a--; }
    for (;;) { break; }
    do { b--; } while (b > 0);
    switch (a) { case 1: break; case 2: break; default: break; }
    return a ? 1 : 0;
}
"""
        # if, &&, if (else-if), ||, while, for, while (do), case, case, ?
        self.assertEqual(_funcs(src)["f"]["complexity"], 11)

    def test_keywords_in_comments_and_strings_not_counted(self):
        src = ('void f(void)\n{\n    /* if while for && */\n'
               '    // case ? ||\n    puts("if (a && b) ?");\n}\n')
        self.assertEqual(_funcs(src)["f"]["complexity"], 1)

    def test_identifier_containing_keyword_not_counted(self):
        src = "void f(void) { int iffy = 0; int format = 0; notify(); }"
        self.assertEqual(_funcs(src)["f"]["complexity"], 1)

    def test_helper_directly(self):
        self.assertEqual(cm.cyclomatic_complexity("{ if (a) {} }"), 2)


class TestNesting(unittest.TestCase):

    def test_flat_body_is_zero(self):
        self.assertEqual(_funcs("void f(void) { a(); }")["f"]["nesting"], 0)

    def test_nested_blocks(self):
        src = ("void f(void)\n{\n  if (a) {\n    while (b) {\n"
               "      if (c) { d(); }\n    }\n  }\n  if (e) { }\n}\n")
        self.assertEqual(_funcs(src)["f"]["nesting"], 3)

    def test_braces_in_string_ignored(self):
        self.assertEqual(_funcs('void f(void) { s = "{{{"; }')["f"]["nesting"], 0)


class TestDoxygenCoverage(unittest.TestCase):

    def test_detects_doxygen_block(self):
        src = ("/** @brief f */\nvoid f(void) { }\n"
               "/* plain */\nvoid g(void) { }\n"
               "void h(void) { }\n"
               "/*! qt */\nvoid i(void) { }\n"
               "/// line\nvoid j(void) { }\n")
        f = _funcs(src)
        self.assertTrue(f["f"]["has_dox"])
        self.assertFalse(f["g"]["has_dox"])
        self.assertFalse(f["h"]["has_dox"])
        self.assertTrue(f["i"]["has_dox"])
        self.assertTrue(f["j"]["has_dox"])

    def test_multiline_doxygen_with_blank_gap(self):
        src = "/**\n * @brief f\n * @return none\n */\n\nstatic void f(void)\n{\n}\n"
        self.assertTrue(_funcs(src)["f"]["has_dox"])


class TestCoupling(unittest.TestCase):

    def test_fanout_excludes_keywords_and_sizeof(self):
        src = ("void f(void)\n{\n    if (a) { g(); }\n    h(sizeof(int));\n"
               "    g();\n    while (k(1)) { }\n    return;\n}\n")
        self.assertEqual(_funcs(src)["f"]["calls"], {"g", "h", "k"})

    def test_fanout_ignores_calls_in_comments(self):
        src = "void f(void) { /* g(); */ const char *s = \"h()\"; }"
        self.assertEqual(_funcs(src)["f"]["calls"], set())

    def test_direct_recursion(self):
        src = ("int fact(int n) { return n ? n * fact(n - 1) : 1; }\n"
               "int other(int n) { /* other(n) */ return n; }\n")
        f = _funcs(src)
        self.assertTrue(f["fact"]["recursive"])
        self.assertFalse(f["other"]["recursive"])

    def test_file_scope_variables(self):
        src = """
#include <stdint.h>
#define N 4
int g_a;
int g_b = 1, g_c;
static int s_a;
static const uint8_t s_tab[N] = { 1, 2, 3, 4 };
extern int e_x;
typedef int my_t;
struct pt { int x; int y; };
struct pt g_pt;
enum mode { M_A, M_B } g_mode;
void (*g_cb)(int) = 0;
int proto(int a);
static void sproto(void);
void f(void)
{
    int local = 0;
    static int fn_static = 0;
}
"""
        self.assertEqual(cm.count_file_scope_variables(src), (6, 2))

    def test_static_vars_compat_wrapper(self):
        self.assertEqual(cm._count_static_vars("static int a;\nint b;\n"), 1)


# --------------------------------------------------------------------------
# Directory-level aggregation
# --------------------------------------------------------------------------

_SAMPLE_C = """/**
 * @file sample.c
 */
#include "sample.h"

static int s_count;
int g_total;

/** @brief add */
int add(int a, int b)
{
    return a + b;
}

int many(int a, int b, int c, int d, int e, int f)
{
    if (a) { return b; }
    return add(c, d) + e + f;
}

static int rec(int n)
{
    /* goto in a comment is not counted */
    assert(n >= 0);
    return (n > 0) ? rec(n - 1) : 0;
}
"""

_SAMPLE_H = """#ifndef SAMPLE_H
#define SAMPLE_H
#define SAMPLE_MAX 10
int add(int a, int b);
#endif
"""


class TestCSourceMetrics(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def test_empty_dir_returns_zeros(self):
        m = cm._c_source_metrics(total_violations=5, source_dir=self.dir)
        self.assertEqual(m, cm._empty_c_metrics())
        self.assertEqual(m["func_count"], 0)
        self.assertEqual(m["cc_bucket_16_plus"], 0)
        self.assertEqual(m["defect_density"], 0.0)

    def test_header_only_dir(self):
        (self.dir / "sample.h").write_text(_SAMPLE_H)
        m = cm._c_source_metrics(source_dir=self.dir)
        self.assertEqual(m["c_file_count"], 0)
        self.assertEqual(m["h_file_count"], 1)
        self.assertEqual(m["func_count"], 0)
        self.assertEqual(m["func_length_avg"], 0.0)
        self.assertEqual(m["dox_coverage_pct"], 0.0)

    def test_sample_project(self):
        (self.dir / "sample.c").write_text(_SAMPLE_C)
        (self.dir / "sample.h").write_text(_SAMPLE_H)
        m = cm._c_source_metrics(total_violations=3, source_dir=self.dir)
        self.assertEqual(m["c_file_count"], 1)
        self.assertEqual(m["h_file_count"], 1)
        self.assertEqual(m["func_count"], 3)
        self.assertEqual(m["func_param_max"], 6)
        self.assertEqual(m["func_over_params"], 1)
        self.assertEqual(m["func_over_length"], 0)
        self.assertEqual(m["cc_max"], 2)
        self.assertEqual(m["cc_bucket_1_5"], 3)
        self.assertEqual(m["cc_bucket_6_10"], 0)
        self.assertAlmostEqual(m["dox_coverage"], 0.333)
        self.assertAlmostEqual(m["dox_coverage_pct"], 33.3)
        self.assertEqual(m["global_vars"], 1)
        self.assertEqual(m["static_vars"], 1)
        self.assertEqual(m["recursive_func_count"], 1)
        # fan-out: add→0, many→{add}, rec→{assert} (self-call excluded)
        self.assertAlmostEqual(m["fanout_avg"], 0.67)
        self.assertEqual(m["goto_count"], 0)
        self.assertEqual(m["assert_count"], 1)
        self.assertEqual(m["macro_count"], 1)      # include guard excluded
        self.assertEqual(m["loc_physical"],
                         m["loc_blank"] + m["loc_comment"]
                         + m["loc_doxygen"] + m["loc_sloc"])
        self.assertEqual(m["defect_density"],
                         round(3 / (m["loc_sloc"] / 1000.0), 2))
        self.assertEqual(m["file_length_max"], len(_SAMPLE_C.splitlines()))

    def test_cc_histogram_buckets(self):
        def ifs(k):
            return "".join(f"    if (a == {i}) {{ }}\n" for i in range(k))

        src = "".join(f"void f{k}(int a)\n{{\n{ifs(k)}}}\n" for k in (0, 6, 12, 20))
        (self.dir / "cc.c").write_text(src)
        m = cm._c_source_metrics(source_dir=self.dir)
        self.assertEqual((m["cc_bucket_1_5"], m["cc_bucket_6_10"],
                          m["cc_bucket_11_15"], m["cc_bucket_16_plus"]),
                         (1, 1, 1, 1))
        self.assertEqual(m["cc_max"], 21)
        self.assertEqual(m["cc_over_threshold"], 2)

    def test_long_function_counted(self):
        body = "".join(f"    x{i}();\n" for i in range(65))
        (self.dir / "long.c").write_text(f"void f(void)\n{{\n{body}}}\n")
        m = cm._c_source_metrics(source_dir=self.dir)
        self.assertEqual(m["func_over_length"], 1)
        self.assertEqual(m["func_length_max"], 68)

    def test_all_new_fields_present_in_empty(self):
        e = cm._empty_c_metrics()
        for key in ("c_file_count", "h_file_count", "cc_bucket_1_5",
                    "cc_bucket_6_10", "cc_bucket_11_15", "cc_bucket_16_plus",
                    "dox_coverage_pct", "global_vars", "fanout_avg",
                    "recursive_func_count"):
            self.assertIn(key, e)


# --------------------------------------------------------------------------
# Violation quality
# --------------------------------------------------------------------------

class TestSummariseViolations(unittest.TestCase):

    def test_categories_top_rules_and_clean_files(self):
        data = {
            "summary": {"files_checked": 4, "errors": 1, "warnings": 2,
                        "info": 4, "total": 7},
            "violations": (
                [{"file": "a.c", "rule": "misc.line_length", "severity": "info"}] * 3
                + [{"file": "a.c", "rule": "variable.global.case", "severity": "warning"}] * 2
                + [{"file": "b.c", "rule": "function.prefix", "severity": "error"}]
                + [{"file": "b.c", "rule": "misc.yoda_condition", "severity": "info"}]
            ),
        }
        s = cm._summarise_violations(data)
        self.assertEqual(s["violations_by_category"],
                         {"function": 1, "misc": 4, "variable": 2})
        self.assertEqual(s["files_zero_violations"], 2)
        self.assertEqual(s["top_rules"][0], {"rule": "misc.line_length", "count": 3})
        self.assertEqual(len(s["top_rules"]), 4)
        self.assertEqual((s["errors"], s["warnings"], s["info"]), (1, 2, 4))

    def test_top_rules_capped_at_five(self):
        data = {"summary": {"files_checked": 1},
                "violations": [{"file": "a.c", "rule": f"misc.r{i}"} for i in range(8)]}
        self.assertEqual(len(cm._summarise_violations(data)["top_rules"]), 5)

    def test_empty_report(self):
        s = cm._summarise_violations({})
        self.assertEqual(s["violations_by_category"], {})
        self.assertEqual(s["files_zero_violations"], 0)
        self.assertEqual(s["top_rules"], [])

    def test_empty_default_has_new_keys(self):
        e = cm._empty_cstylecheck_metrics()
        self.assertEqual(e["violations_by_category"], {})
        self.assertEqual(e["top_rules"], [])


# --------------------------------------------------------------------------
# Charts and wiki page — old data points without the new fields must work
# --------------------------------------------------------------------------

_OLD_POINT = {"timestamp": "2026-07-01T00:00:00+00:00", "commit": "aaa",
              "errors": 1, "warnings": 2, "info_count": 3,
              "loc_sloc": 100, "loc_comment": 10, "loc_doxygen": 5,
              "loc_blank": 20, "dox_coverage": 0.5, "loc_comment_density": 0.15}
_NEW_POINT = dict(_OLD_POINT, timestamp="2026-07-02T00:00:00+00:00", commit="bbb",
                  cc_bucket_1_5=4, cc_bucket_6_10=1, cc_bucket_11_15=0,
                  cc_bucket_16_plus=0, func_count=5, func_length_avg=12.0,
                  dox_coverage_pct=50.0, global_vars=1, static_vars=2,
                  fanout_avg=1.5, recursive_func_count=0,
                  violations_by_category={"misc": 3, "variable": 2},
                  files_zero_violations=1,
                  top_rules=[{"rule": "misc.line_length", "count": 3}])


class TestChartsAndWiki(unittest.TestCase):

    def test_stack_series_skips_all_missing(self):
        out = gc._stack_series([("a", [None, 1, 2]), ("b", [None, None, 3])])
        self.assertEqual(out, [("a", [None, 1, 2]), ("b", [None, 1, 5])])

    def test_category_series_old_points_none(self):
        series = dict(gc._category_series([_OLD_POINT, _NEW_POINT]))
        self.assertEqual(series["misc"], [None, 3])
        self.assertEqual(series["variable"], [None, 2])

    def test_category_series_other_bucket(self):
        p = {"violations_by_category": {f"c{i}": i + 1 for i in range(10)}}
        series = gc._category_series([p], max_categories=3)
        self.assertEqual([s[0] for s in series], ["c9", "c8", "c7", "other"])
        self.assertEqual(series[-1][1], [sum(range(1, 8))])

    def test_stacked_chart_renders_polygons(self):
        svg = gc._make_chart("t", ["2026-07-01T00:00:00+00:00", "2026-07-02T00:00:00+00:00"],
                             [("a", [1, 2]), ("b", [3, 4])], ["#000", "#111"],
                             stacked=True)
        self.assertIn("<polygon", svg)

    def test_generate_all_with_mixed_old_and_new_points(self):
        with tempfile.TemporaryDirectory() as d:
            written = gc._generate_all([_OLD_POINT, _NEW_POINT], d, "develop")
            names = {Path(p).name for p in written}
        for chart in ("loc_breakdown", "cc_distribution", "function_size",
                      "defect_density", "violations_by_category",
                      "documentation_coverage", "coupling"):
            if chart == "defect_density":
                continue            # no defect_density in the fixtures
            self.assertIn(f"develop_{chart}.svg", names)

    def test_generate_all_only_old_points(self):
        with tempfile.TemporaryDirectory() as d:
            written = gc._generate_all([_OLD_POINT], d, "main")
            names = {Path(p).name for p in written}
        # Charts for metrics absent from old points are simply skipped.
        self.assertNotIn("main_violations_by_category.svg", names)
        self.assertNotIn("main_cc_distribution.svg", names)
        self.assertIn("main_loc_breakdown.svg", names)
        self.assertIn("main_documentation_coverage.svg", names)

    def test_wiki_page_contains_new_rows(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "main.json").write_text(json.dumps({"data_points": [_OLD_POINT]}))
            (Path(d) / "develop.json").write_text(json.dumps({"data_points": [_NEW_POINT]}))
            out = Path(d) / "Trend-Analysis.md"
            argv = sys.argv
            sys.argv = ["x", "--data-dir", d, "--charts-url-base", "http://x",
                        "--output", str(out)]
            try:
                wm.main()
            finally:
                sys.argv = argv
            text = out.read_text(encoding="utf-8")
        self.assertIn("| Avg fan-out | — | 1.500 |", text)
        self.assertIn("| Funcs CC 1-5 | — | 4 |", text)
        self.assertIn("### Violations by rule category", text)
        self.assertIn("| `misc` | — | 3 |", text)
        self.assertIn("### Top 5 violated rules", text)
        self.assertIn("develop_violations_by_category.svg", text)
        self.assertIn("main_coupling.svg", text)


if __name__ == "__main__":
    unittest.main()
