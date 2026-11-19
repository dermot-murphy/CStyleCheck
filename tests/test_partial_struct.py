"""
test_partial_struct.py — misc.partial_struct_assignment and
misc.partial_struct_initialiser (#456).

UV-PSI-001  Struct definition table (collect_struct_defs)
UV-PSI-002  misc.partial_struct_assignment — flagged cases
UV-PSI-003  misc.partial_struct_assignment — not-flagged cases
UV-PSI-004  misc.partial_struct_initialiser
UV-PSI-005  Cross-file struct definitions (CLI pre-pass)
UV-PSI-006  Preprocessor conditionals in struct bodies (#463)
UV-PSI-007  Definition-only files: definition_paths / --definitions (#461)
UV-PSI-008  report_unknown_types (#462)
"""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from harness import cfg_only, run, rules  # noqa: E402

from cstylecheck.checker import (  # noqa: E402
    collect_macros, collect_struct_defs, collect_typedef_names,
    eval_pp_condition, struct_definition_paths, struct_rules_enabled,
)

RULE_PSA = "misc.partial_struct_assignment"
RULE_PSI = "misc.partial_struct_initialiser"

_TYPES = (
    "typedef struct { int baud; int parity; int stop; } uart_cfg_t;\n"
    "struct pt { int x; int y; };\n"
)


def _psa_cfg(enabled=True, severity="warning", **extra):
    return cfg_only(misc={"partial_struct_assignment":
                          {"enabled": enabled, "severity": severity, **extra}})


def _psi_cfg(enabled=True, severity="info"):
    return cfg_only(misc={"partial_struct_initialiser":
                          {"enabled": enabled, "severity": severity}})


def _fn(body: str) -> str:
    return _TYPES + "void f(void)\n{\n" + body + "\n}\n"


# ---------------------------------------------------------------------------
# UV-PSI-001  Struct definition table
# ---------------------------------------------------------------------------

class TestCollectStructDefs(unittest.TestCase):

    def test_typedef_and_tag(self):
        defs = collect_struct_defs(
            "typedef struct cfg_s { int a; char b[4]; } cfg_t;")
        self.assertEqual(defs["cfg_t"], (("a",), ("b",)))
        self.assertEqual(defs["struct cfg_s"], (("a",), ("b",)))

    def test_tagged_struct_without_typedef(self):
        self.assertEqual(collect_struct_defs("struct pt { int x, y; };")
                         ["struct pt"], (("x",), ("y",)))

    def test_function_pointer_and_bitfields(self):
        defs = collect_struct_defs(
            "struct s { void (*cb)(int n); unsigned en : 1; unsigned : 3; };")
        self.assertEqual(defs["struct s"], (("cb",), ("en",)))

    def test_anonymous_union_is_one_entry(self):
        defs = collect_struct_defs(
            "struct s { int a; union { int i; float f; }; };")
        self.assertEqual(defs["struct s"], (("a",), ("i", "f")))

    def test_anonymous_struct_members_flattened(self):
        defs = collect_struct_defs(
            "struct s { int a; struct { int p; int q; }; };")
        self.assertEqual(defs["struct s"], (("a",), ("p",), ("q",)))

    def test_named_nested_struct_is_one_member(self):
        defs = collect_struct_defs(
            "struct s { struct in_s { int z; } inner; int b; };")
        self.assertEqual(defs["struct s"], (("inner",), ("b",)))
        self.assertEqual(defs["struct in_s"], (("z",),))

    def test_typedef_alias_of_tag(self):
        defs = collect_struct_defs(
            "struct pt { int x; int y; };\ntypedef struct pt pt_t;")
        self.assertEqual(defs["pt_t"], "struct pt")

    def test_pointer_typedef_not_recorded(self):
        defs = collect_struct_defs("typedef struct { int a; } s_t, *s_p;")
        self.assertIn("s_t", defs)
        self.assertNotIn("s_p", defs)

    def test_union_not_recorded(self):
        self.assertEqual(collect_struct_defs("union u { int a; float b; };"),
                         {})

    def test_struct_rules_enabled(self):
        self.assertFalse(struct_rules_enabled({}))
        self.assertFalse(struct_rules_enabled(_psa_cfg(enabled=False)))
        self.assertTrue(struct_rules_enabled(_psa_cfg()))
        self.assertTrue(struct_rules_enabled(_psi_cfg()))


# ---------------------------------------------------------------------------
# UV-PSI-002  misc.partial_struct_assignment — flagged
# ---------------------------------------------------------------------------

class TestPartialStructAssignmentFlagged(unittest.TestCase):

    def test_partial_then_address_passed(self):
        src = _fn("    uart_cfg_t cfg;\n    cfg.baud = 1;\n    Uart_Init(&cfg);")
        self.assertIn(RULE_PSA, rules(src, _psa_cfg()))

    def test_partial_then_passed_by_value(self):
        src = _fn("    struct pt p;\n    p.x = 1;\n    Draw(p);")
        self.assertIn(RULE_PSA, rules(src, _psa_cfg()))

    def test_partial_then_returned(self):
        src = _TYPES + ("uart_cfg_t g(void)\n{\n    uart_cfg_t c;\n"
                        "    c.baud = 1;\n    return c;\n}\n")
        self.assertIn(RULE_PSA, rules(src, _psa_cfg()))

    def test_partial_then_copied(self):
        src = _fn("    struct pt p;\n    struct pt q = {0};\n    p.y = 2;\n"
                  "    q = p;\n    Draw(q);")
        self.assertIn(RULE_PSA, rules(src, _psa_cfg()))

    def test_reported_at_declaration_with_missing_members(self):
        src = _fn("    uart_cfg_t cfg;\n    cfg.baud = 1;\n    Uart_Init(&cfg);")
        viols = [v for v in run(src, _psa_cfg()) if v.rule == RULE_PSA]
        self.assertEqual(len(viols), 1)
        self.assertEqual(viols[0].line, 5)            # declaration line
        self.assertIn("line 7", viols[0].message)     # first whole use
        self.assertIn("parity, stop", viols[0].message)
        self.assertIn("1 of 3", viols[0].message)

    def test_one_of_two_declarators(self):
        src = _fn("    struct pt a, b;\n    a.x = 1;\n    a.y = 2;\n"
                  "    b.x = 3;\n    Draw(a);\n    Draw(b);")
        msgs = [v.message for v in run(src, _psa_cfg()) if v.rule == RULE_PSA]
        self.assertEqual(len(msgs), 1)
        self.assertIn("'b'", msgs[0])

    def test_struct_tag_via_typedef_alias(self):
        src = (_TYPES + "typedef struct pt pt_t;\n"
               "void f(void)\n{\n    pt_t p;\n    p.x = 1;\n    Draw(p);\n}\n")
        self.assertIn(RULE_PSA, rules(src, _psa_cfg()))

    def test_severity_configurable(self):
        src = _fn("    struct pt p;\n    p.x = 1;\n    Draw(p);")
        viols = [v for v in run(src, _psa_cfg(severity="error"))
                 if v.rule == RULE_PSA]
        self.assertEqual(viols[0].severity, "error")


# ---------------------------------------------------------------------------
# UV-PSI-003  misc.partial_struct_assignment — not flagged
# ---------------------------------------------------------------------------

class TestPartialStructAssignmentClean(unittest.TestCase):

    def _clean(self, body, cfg=None):
        self.assertNotIn(RULE_PSA, rules(_fn(body), cfg or _psa_cfg()))

    def test_zero_initialiser(self):
        self._clean("    uart_cfg_t cfg = {0};\n    cfg.baud = 1;\n"
                    "    Uart_Init(&cfg);")

    def test_every_member_assigned(self):
        self._clean("    uart_cfg_t cfg;\n    cfg.baud = 1;\n"
                    "    cfg.parity = 0;\n    cfg.stop = 1;\n    Uart_Init(&cfg);")

    def test_memset_first(self):
        self._clean("    uart_cfg_t cfg;\n    (void)memset(&cfg, 0, sizeof(cfg));\n"
                    "    cfg.baud = 1;\n    Uart_Init(&cfg);")

    def test_custom_fill_function(self):
        body = ("    uart_cfg_t cfg;\n    Uart_Defaults(&cfg);\n"
                "    cfg.baud = 1;\n    Uart_Init(&cfg);")
        # Out-parameter call before any member write: not flagged anyway.
        self._clean(body)
        body2 = ("    uart_cfg_t cfg;\n    cfg.baud = 1;\n"
                 "    Uart_Defaults(&cfg);\n    Uart_Init(&cfg);")
        self.assertIn(RULE_PSA, rules(_fn(body2), _psa_cfg()))
        # Listed as a fill function: the call writes every member.
        self._clean(body2, _psa_cfg(fill_functions=["Uart_Defaults"]))

    def test_whole_struct_assignment_first(self):
        self._clean("    struct pt p;\n    p = Origin();\n    p.x = 1;\n"
                    "    Draw(p);")

    def test_out_parameter_before_member_write(self):
        self._clean("    uart_cfg_t cfg;\n    Read_Config(&cfg);\n"
                    "    cfg.baud = 1;\n    Uart_Init(&cfg);")

    def test_member_reads_only_never_used_whole(self):
        self._clean("    struct pt p;\n    p.x = 1;\n    Plot(p.x);")

    def test_sizeof_is_not_a_use(self):
        self._clean("    struct pt p;\n    p.x = sizeof(p);\n    p.y = 0;\n"
                    "    Draw(p);")

    def test_address_of_member_counts_as_assigned(self):
        self._clean("    struct pt p;\n    Read_Int(&p.x);\n    p.y = 0;\n"
                    "    Draw(p);")

    def test_static_local_is_zeroed(self):
        self._clean("    static struct pt p;\n    p.x = 1;\n    Draw(p);")

    def test_pointer_and_array_not_checked(self):
        self._clean("    struct pt *p_pt;\n    struct pt pts[2];\n"
                    "    pts[0].x = 1;\n    Draw_All(pts);\n    (void)p_pt;")

    def test_unknown_struct_type_not_checked(self):
        self._clean("    other_t o;\n    o.x = 1;\n    Use(&o);")

    def test_union_member_of_anonymous_union(self):
        src = ("struct v { int tag; union { int i; float f; }; };\n"
               "void f(void)\n{\n    struct v val;\n    val.tag = 1;\n"
               "    val.f = 2.0f;\n    Put(&val);\n}\n")
        self.assertNotIn(RULE_PSA, rules(src, _psa_cfg()))

    def test_member_of_other_object_not_counted(self):
        # "other.p" is not a use of local 'p'.
        self._clean("    struct pt p = {0};\n    struct pt q;\n"
                    "    q.x = p.x;\n    q.y = 0;\n    Draw(q);")

    def test_shadowing_block_skipped(self):
        # PR #457 review R3: the inner 'c' is another object.
        self._clean("    uart_cfg_t c;\n    c.baud = 1;\n"
                    "    { int c = 3; Use_Int(c); }\n"
                    "    c.parity = 1;\n    c.stop = 1;\n    Uart_Init(&c);")

    def test_for_init_shadow_skipped(self):
        # PR #457 re-review S1: 'c' declared in a for initialiser.
        self._clean("    uart_cfg_t c;\n    c.baud = 1;\n"
                    "    for (int c = 0; c < 3; c++) { Use_Int(c); }\n"
                    "    c.parity = 1;\n    c.stop = 1;\n    Uart_Init(&c);")

    def test_use_after_for_init_shadow_still_checked(self):
        src = _fn("    uart_cfg_t c;\n    c.baud = 1;\n"
                  "    for (int c = 0; c < 3; c++)\n        Use_Int(c);\n"
                  "    Uart_Init(&c);")
        viols = [v for v in run(src, _psa_cfg()) if v.rule == RULE_PSA]
        self.assertEqual(len(viols), 1)
        self.assertIn("line 9", viols[0].message)

    def test_use_after_shadowing_block_still_checked(self):
        src = _fn("    uart_cfg_t c;\n    c.baud = 1;\n"
                  "    { uart_cfg_t c = {0}; Uart_Init(&c); }\n"
                  "    Uart_Init(&c);")
        viols = [v for v in run(src, _psa_cfg()) if v.rule == RULE_PSA]
        self.assertEqual(len(viols), 1)
        self.assertIn("line 8", viols[0].message)

    def test_disabled(self):
        src = _fn("    struct pt p;\n    p.x = 1;\n    Draw(p);")
        self.assertNotIn(RULE_PSA, rules(src, _psa_cfg(enabled=False)))

    def test_table_not_built_when_rules_disabled(self):
        # PR #457 review N3: no struct-table cost when both rules are off.
        from cstylecheck.checker import Checker
        c = Checker("test_module.c", _fn("    struct pt p;"), cfg_only())
        self.assertEqual(c._struct_defs, {})

    def test_in_comment_not_flagged(self):
        self._clean("    /* struct pt p; p.x = 1; Draw(p); */\n    return;")


# ---------------------------------------------------------------------------
# UV-PSI-004  misc.partial_struct_initialiser
# ---------------------------------------------------------------------------

class TestPartialStructInitialiser(unittest.TestCase):

    def test_short_positional_flagged(self):
        src = _fn("    uart_cfg_t cfg = { 9600 };\n    Uart_Init(&cfg);")
        viols = [v for v in run(src, _psi_cfg()) if v.rule == RULE_PSI]
        self.assertEqual(len(viols), 1)
        self.assertEqual(viols[0].severity, "info")
        self.assertIn("1 of 3", viols[0].message)
        self.assertIn("parity, stop", viols[0].message)

    def test_full_positional_clean(self):
        src = _fn("    struct pt p = { 1, 2 };\n    Draw(p);")
        self.assertNotIn(RULE_PSI, rules(src, _psi_cfg()))

    def test_trailing_comma_counted_correctly(self):
        src = _fn("    struct pt p = { 1, 2, };\n    Draw(p);")
        self.assertNotIn(RULE_PSI, rules(src, _psi_cfg()))

    def test_zero_and_empty_clean(self):
        src = _fn("    struct pt p = {0};\n    struct pt q = { };\n    Draw(p);"
                  "\n    Draw(q);")
        self.assertNotIn(RULE_PSI, rules(src, _psi_cfg()))

    def test_zero_literal_variants_clean(self):
        # PR #457 review R1: {0U}, {false}, {0x0}, {NULL}, {0.0f} zero the
        # whole struct just like {0}.
        for init in ("0U", "0UL", "false", "0x0", "NULL", "0.0f", "0,"):
            with self.subTest(init=init):
                src = _fn(f"    struct pt p = {{ {init} }};\n    Draw(p);")
                self.assertNotIn(RULE_PSI, rules(src, _psi_cfg()))

    def test_conditional_member_counted_once(self):
        # PR #457 review R2: both #if / #else branches declare 'b'.
        src = ("typedef struct { int a;\n#if X\n    int b;\n#else\n"
               "    long b;\n#endif\n    int c; } cond_t;\n"
               "void f(void)\n{\n    cond_t s = { 1, 2, 3 };\n    Put(&s);\n}\n")
        self.assertNotIn(RULE_PSI, rules(src, _psi_cfg()))

    def test_designated_clean(self):
        src = _fn("    struct pt p = { .x = 1 };\n    Draw(p);")
        self.assertNotIn(RULE_PSI, rules(src, _psi_cfg()))

    def test_nested_braces_count_as_one(self):
        src = ("struct box { struct pt { int x; int y; } a; int w; };\n"
               "void f(void)\n{\n    struct box b = { { 1, 2 } };\n"
               "    Put(b);\n}\n")
        msgs = [v.message for v in run(src, _psi_cfg()) if v.rule == RULE_PSI]
        self.assertEqual(len(msgs), 1)
        self.assertIn("1 of 2", msgs[0])

    def test_static_local_also_checked(self):
        src = _fn("    static const struct pt p = { 1 };\n    Draw(p);")
        self.assertIn(RULE_PSI, rules(src, _psi_cfg()))

    def test_file_scope_not_checked(self):
        src = _TYPES + "static struct pt g_origin = { 1 };\n"
        self.assertNotIn(RULE_PSI, rules(src, _psi_cfg()))

    def test_copy_initialiser_not_checked(self):
        src = _fn("    struct pt p = Origin();\n    Draw(p);")
        self.assertNotIn(RULE_PSI, rules(src, _psi_cfg()))

    def test_disabled(self):
        src = _fn("    struct pt p = { 1 };\n    Draw(p);")
        self.assertNotIn(RULE_PSI, rules(src, _psi_cfg(enabled=False)))


# ---------------------------------------------------------------------------
# UV-PSI-005  Cross-file struct definitions (CLI pre-pass)
# ---------------------------------------------------------------------------

class TestCrossFileStructDefs(unittest.TestCase):

    def _cli(self, td, *names):
        import contextlib
        import io
        from unittest import mock
        from cstylecheck.cli import main
        out = io.StringIO()
        argv = ["cstylecheck", "--config", str(Path(td) / "c.yml")]
        argv += [str(Path(td) / n) for n in names]
        with mock.patch.object(sys, "argv", argv), \
                contextlib.redirect_stdout(out):
            main()
        return out.getvalue()

    def _write(self, td):
        Path(td, "uart.h").write_text(
            "typedef struct { int baud; int parity; } uart_cfg_t;\n",
            encoding="utf-8")
        Path(td, "app.c").write_text(
            '#include "uart.h"\nvoid App_Start(void)\n{\n'
            "    uart_cfg_t cfg;\n    cfg.baud = 9600;\n"
            "    Uart_Init(&cfg);\n}\n", encoding="utf-8")
        Path(td, "c.yml").write_text(
            "misc:\n  partial_struct_assignment:\n    enabled: true\n",
            encoding="utf-8")

    def test_struct_defined_in_scanned_header(self):
        with tempfile.TemporaryDirectory() as td:
            self._write(td)
            out = self._cli(td, "app.c", "uart.h")
            self.assertIn(f"app.c:4:16: WARNING [{RULE_PSA}]", out)

    def test_header_not_scanned_struct_unknown(self):
        with tempfile.TemporaryDirectory() as td:
            self._write(td)
            out = self._cli(td, "app.c")
            self.assertNotIn(RULE_PSA, out)

    def test_inline_suppression(self):
        with tempfile.TemporaryDirectory() as td:
            self._write(td)
            app = Path(td, "app.c")
            app.write_text(app.read_text().replace(
                "uart_cfg_t cfg;",
                "uart_cfg_t cfg;  /* cstylecheck: disable misc.partial_struct_assignment */"),
                encoding="utf-8")
            out = self._cli(td, "app.c", "uart.h")
            self.assertNotIn(RULE_PSA, out)


# ---------------------------------------------------------------------------
# UV-PSI-006  Preprocessor conditionals in struct bodies (#463)
# ---------------------------------------------------------------------------

_COND_STRUCT = ("typedef struct\n{\n    int a;\n    int b;\n"
                "#if EXT\n    int c;\n    int d;\n#endif\n} cfg_t;\n")
_COND_USE = ("void f(void)\n{\n    cfg_t cfg;\n    cfg.a = 1;\n"
             "    cfg.b = 2;\n    Apply(&cfg);\n}\n")


class TestPreprocessorConditionals(unittest.TestCase):

    def _members(self, src, macros=None):
        return [e[0] for e in collect_struct_defs(src, macros)["cfg_t"]]

    def test_condition_false_members_excluded(self):
        src = "#define EXT 0\n" + _COND_STRUCT + _COND_USE
        self.assertEqual(self._members(src), ["a", "b"])
        self.assertNotIn(RULE_PSA, rules(src, _psa_cfg()))

    def test_condition_true_members_counted(self):
        src = "#define EXT 1\n" + _COND_STRUCT + _COND_USE
        self.assertEqual(self._members(src), ["a", "b", "c", "d"])
        msgs = [v.message for v in run(src, _psa_cfg()) if v.rule == RULE_PSA]
        self.assertEqual(len(msgs), 1)
        self.assertIn("2 of 4", msgs[0])
        self.assertIn("c, d", msgs[0])

    def test_condition_unknown_members_excluded(self):
        src = _COND_STRUCT + _COND_USE
        self.assertEqual(self._members(src), ["a", "b"])
        self.assertNotIn(RULE_PSA, rules(src, _psa_cfg()))

    def test_macro_from_other_file(self):
        self.assertEqual(
            self._members(_COND_STRUCT, collect_macros("#define EXT 1\n")),
            ["a", "b", "c", "d"])

    def test_this_file_macro_fills_gaps_only(self):
        # The project-wide table wins (#463 review); this file's own
        # #defines are used only for names the table lacks.
        src = "#define EXT 0\n" + _COND_STRUCT
        self.assertEqual(self._members(src, {"EXT": (None, "1")}),
                         ["a", "b", "c", "d"])
        self.assertEqual(self._members(src, {"OTHER": (None, "1")}),
                         ["a", "b"])

    def test_ifdef_ifndef_else_elif(self):
        src = ("#define HAVE_X 1\ntypedef struct {\n#ifdef HAVE_X\n int x;\n"
               "#endif\n#ifndef HAVE_X\n int nx;\n#endif\n#if 0\n int z;\n"
               "#elif HAVE_X == 1\n int e;\n#else\n int f;\n#endif\n} cfg_t;\n")
        self.assertEqual(self._members(src), ["x", "e"])

    def test_member_in_every_branch_counted_when_unknown(self):
        src = ("typedef struct {\n#if UNKNOWN\n int a;\n int p;\n#else\n"
               " long a;\n#endif\n int b; } cfg_t;\n")
        self.assertEqual(sorted(self._members(src)), ["a", "b"])

    def test_no_else_member_not_counted_when_unknown(self):
        src = ("typedef struct {\n#ifdef OPT\n int a;\n#endif\n"
               " int b; } cfg_t;\n")
        self.assertEqual(self._members(src), ["b"])

    def test_nested_conditionals(self):
        src = ("#define A 1\n#define B 0\ntypedef struct {\n#if A\n int a;\n"
               "#if B\n int b;\n#else\n int nb;\n#endif\n#endif\n} cfg_t;\n")
        self.assertEqual(self._members(src), ["a", "nb"])

    def test_eval_function_like_macro_and_defined(self):
        macros = collect_macros(
            "#define CHECK(x) (x)\n#define FEATURE 1\n#define OFF 0\n")
        self.assertTrue(eval_pp_condition(
            "CHECK(FEATURE) || defined(__DOXYGEN__)", macros))
        self.assertFalse(eval_pp_condition("CHECK(OFF) && defined(X)", macros))
        self.assertIsNone(eval_pp_condition("CHECK(OFF) || defined(X)", macros))
        self.assertTrue(eval_pp_condition("defined FEATURE && !OFF", macros))
        self.assertTrue(eval_pp_condition("(0x10U >> 4) == 1UL", macros))
        self.assertIsNone(eval_pp_condition("UNDEFINED_NAME", macros))
        self.assertIsNone(eval_pp_condition("1 / 0", macros))
        self.assertIsNone(eval_pp_condition('"str"', macros))
        self.assertTrue(eval_pp_condition("1 ? 2 : 0", macros))

    def test_initialiser_uses_resolved_count(self):
        src = ("#define EXT 0\n" + _COND_STRUCT
               + "void f(void)\n{\n    cfg_t c = { 1, 2 };\n    Put(&c);\n}\n")
        self.assertNotIn(RULE_PSI, rules(src, _psi_cfg()))


# ---------------------------------------------------------------------------
# UV-PSI-007  Definition-only files (#461)
# ---------------------------------------------------------------------------

class TestDefinitionPaths(unittest.TestCase):

    def _cli(self, td, *args):
        import contextlib
        import io
        import os
        from unittest import mock
        from cstylecheck.cli import main
        out = io.StringIO()
        argv = ["cstylecheck", "--config", "c.yml", *args]
        cwd = os.getcwd()
        try:
            os.chdir(td)
            with mock.patch.object(sys, "argv", argv), \
                    contextlib.redirect_stdout(out):
                main()
        finally:
            os.chdir(cwd)
        return out.getvalue()

    def _write(self, td, config_extra=""):
        sdk = Path(td, "sdk")
        sdk.mkdir()
        Path(sdk, "drv.h").write_text(
            "typedef struct\n{\n    int pin;\n    int freq;\n"
            "#if DRV_EXTENDED\n    int delay;\n#endif\n} drv_cfg_t;\n",
            encoding="utf-8")
        Path(sdk, "sdk_config.h").write_text("#define DRV_EXTENDED 0\n",
                                             encoding="utf-8")
        Path(td, "app_config.h").write_text("#define DRV_EXTENDED 1\n",
                                            encoding="utf-8")
        Path(td, "app.c").write_text(
            "void App_Start(void)\n{\n    drv_cfg_t cfg;\n"
            "    cfg.pin = 1;\n    cfg.freq = 2;\n    Drv_Init(&cfg);\n}\n",
            encoding="utf-8")
        Path(td, "c.yml").write_text(
            "misc:\n  partial_struct_assignment:\n    enabled: true\n"
            + config_extra, encoding="utf-8")

    def test_without_definitions_not_checked(self):
        with tempfile.TemporaryDirectory() as td:
            self._write(td)
            out = self._cli(td, "--include", "app.c", "--exclude", "sdk/**")
            self.assertNotIn(RULE_PSA, out)

    def test_definition_paths_config_reads_excluded_header(self):
        with tempfile.TemporaryDirectory() as td:
            self._write(td, "    definition_paths:\n"
                            "      - app_config.h\n      - sdk/*.h\n")
            out = self._cli(td, "--include", "app.c", "--exclude", "sdk/**")
            self.assertIn(f"WARNING [{RULE_PSA}]", out)
            self.assertIn("2 of 3", out)
            self.assertIn("delay", out)
            self.assertNotIn("drv.h", out)        # never checked

    def test_earlier_definition_path_wins_for_macros(self):
        with tempfile.TemporaryDirectory() as td:
            self._write(td, "    definition_paths:\n"
                            "      - sdk/*.h\n      - app_config.h\n")
            out = self._cli(td, "--include", "app.c")
            # sdk/sdk_config.h (DRV_EXTENDED 0) is read first: 2 members,
            # both assigned, so nothing is reported.
            self.assertNotIn(RULE_PSA, out)

    def test_definitions_option(self):
        with tempfile.TemporaryDirectory() as td:
            self._write(td)
            out = self._cli(td, "--include", "app.c",
                            "--definitions", "app_config.h",
                            "--definitions", "sdk/**/*.h")
            self.assertIn("2 of 3", out)

    def test_struct_definition_paths_helper(self):
        cfg = {"misc": {
            "partial_struct_assignment": {
                "enabled": True, "definition_paths": ["a/*.h", "b/*.h"]},
            "partial_struct_initialiser": {
                "enabled": True, "definition_paths": ["b/*.h", "c/*.h"]},
        }}
        self.assertEqual(struct_definition_paths(cfg),
                         ["a/*.h", "b/*.h", "c/*.h"])
        # A disabled rule still contributes (per-directory configs may
        # enable it).
        cfg["misc"]["partial_struct_initialiser"]["enabled"] = False
        self.assertEqual(struct_definition_paths(cfg),
                         ["a/*.h", "b/*.h", "c/*.h"])
        self.assertEqual(struct_definition_paths({}), [])

    def test_checked_config_beats_header_ifndef_default(self):
        with tempfile.TemporaryDirectory() as td:
            self._write(td, "    definition_paths:\n      - sdk/drv.h\n")
            Path(td, "sdk", "drv.h").write_text(
                "#ifndef DRV_EXTENDED\n#define DRV_EXTENDED 0\n#endif\n"
                + Path(td, "sdk", "drv.h").read_text(), encoding="utf-8")
            out = self._cli(td, "--include", "app.c",
                            "--include", "app_config.h")
            self.assertIn("2 of 3", out)

    def test_definitions_ignored_warning(self):
        import contextlib
        import io
        with tempfile.TemporaryDirectory() as td:
            self._write(td)
            Path(td, "c.yml").write_text("misc: {}\n", encoding="utf-8")
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                self._cli(td, "--include", "app.c",
                          "--definitions", "sdk/*.h")
            self.assertIn("--definitions is ignored", err.getvalue())


class TestMacroCollection(unittest.TestCase):
    """#463 review: which #defines are used, and their precedence."""

    def test_conditional_define_not_used(self):
        self.assertNotIn("HAS_X", collect_macros(
            "#if defined(NRF51)\n#define HAS_X 0\n#else\n#define HAS_X 1\n"
            "#endif\n"))

    def test_include_guard_contents_are_plain(self):
        m = collect_macros("#ifndef DRV_H\n#define DRV_H\n\n"
                           "#define CHECK(x) (x)\n#endif\n")
        self.assertEqual(m["CHECK"], (("x",), "(x)"))

    def test_ifndef_default_used(self):
        self.assertEqual(collect_macros(
            "#ifndef FEATURE\n#define FEATURE 1\n#endif\n")["FEATURE"],
            (None, "1"))

    def test_plain_beats_default_and_undef_drops(self):
        from cstylecheck.checker import MacroTable, collect_macro_defs
        t = MacroTable()
        t.add(collect_macro_defs("#ifndef F\n#define F 0\n#endif\n"))
        t.add(collect_macro_defs("#define F 1\n#define G 1\n#undef G\n"))
        self.assertEqual(t.table, {"F": (None, "1")})

    def test_global_table_beats_file_default(self):
        src = ("#ifndef EXT\n#define EXT 0\n#endif\n" + _COND_STRUCT)
        members = collect_struct_defs(src, {"EXT": (None, "1")})["cfg_t"]
        self.assertEqual(len(members), 4)

    def test_continued_if_condition(self):
        src = ("#define X 1\n#define Y 0\ntypedef struct {\n int a;\n"
               "#if X \\\n    && Y\n int b;\n#endif\n} cfg_t;\n")
        self.assertEqual(collect_struct_defs(src)["cfg_t"], (("a",),))

    def test_common_member_keeps_declaration_order(self):
        src = ("typedef struct {\n int a;\n#if UNKNOWN\n int b;\n#else\n"
               " long b;\n#endif\n int c;\n} cfg_t;\n")
        self.assertEqual(collect_struct_defs(src)["cfg_t"],
                         (("a",), ("b",), ("c",)))

    def test_true_elif_makes_group_exhaustive(self):
        src = ("typedef struct {\n#if UNKNOWN\n int a;\n#elif 1\n int a;\n"
               "#endif\n} cfg_t;\n")
        self.assertEqual(collect_struct_defs(src)["cfg_t"], (("a",),))

    def test_elifdef(self):
        src = ("#define B 1\ntypedef struct {\n#if 0\n int a;\n#elifdef B\n"
               " int b;\n#endif\n} cfg_t;\n")
        self.assertEqual(collect_struct_defs(src)["cfg_t"], (("b",),))

    def test_macro_body_not_parenthesised(self):
        m = collect_macros("#define X 2 + 3\n#define MUL(a,b) a*b\n")
        self.assertTrue(eval_pp_condition("X * 2 == 8", m))
        self.assertTrue(eval_pp_condition("MUL(1+1,2) == 3", m))

    def test_deep_nesting_is_unknown_not_an_error(self):
        self.assertIsNone(eval_pp_condition("(" * 400 + "1" + ")" * 400, {}))


# ---------------------------------------------------------------------------
# UV-PSI-008  report_unknown_types (#462)
# ---------------------------------------------------------------------------

class TestReportUnknownTypes(unittest.TestCase):

    _SRC = ("typedef enum { MODE_A, MODE_B } mode_t;\n"
            "typedef struct { int a; } known_t;\n"
            "void f(void)\n{\n    vendor_cfg_t cfg;\n    struct ext_s e;\n"
            "    mode_t m;\n    uint8_t n;\n    known_t k;\n    int i;\n"
            "    static vendor_cfg_t s;\n    vendor_cfg_t z = {0};\n"
            "    vendor_cfg_t *p;\n"
            "    Use(&cfg, &e, &m, &n, &k, &i, &s, &z, p);\n}\n")

    def _unknown(self, cfg):
        return [v for v in run(self._SRC, cfg) if "not checked" in v.message]

    def test_off_by_default(self):
        self.assertEqual(self._unknown(_psa_cfg()), [])

    def test_reports_only_unknown_types(self):
        found = self._unknown(_psa_cfg(report_unknown_types=True))
        by_name = {v.message.split("'")[1]: v for v in found}
        self.assertEqual(sorted(by_name), ["cfg", "e"])
        for v in found:
            self.assertEqual(v.rule, RULE_PSA)
            self.assertEqual(v.severity, "info")
        self.assertIn("'vendor_cfg_t'", by_name["cfg"].message)
        self.assertIn("'struct ext_s'", by_name["e"].message)

    def test_initialiser_rule_reports_positional_init(self):
        src = ("void f(void)\n{\n    vendor_cfg_t a = { 1, 2 };\n"
               "    vendor_cfg_t b = {0};\n    vendor_cfg_t c = { .x = 1 };\n"
               "    Use(&a, &b, &c);\n}\n")
        cfg = cfg_only(misc={"partial_struct_initialiser": {
            "enabled": True, "report_unknown_types": True}})
        found = [v for v in run(src, cfg) if "not checked" in v.message]
        self.assertEqual([v.message.split("'")[1] for v in found], ["a"])
        self.assertEqual(found[0].rule, RULE_PSI)

    def test_alias_of_undefined_struct_reported(self):
        src = ("typedef struct foo_s foo_t;\n"
               "void f(void)\n{\n    foo_t a;\n    Use(&a);\n}\n")
        found = [v for v in run(src, _psa_cfg(report_unknown_types=True))
                 if "not checked" in v.message]
        self.assertEqual([v.message.split("'")[1] for v in found], ["a"])

    def test_macro_type_not_reported(self):
        src = ("#define U8 unsigned char\n"
               "void f(void)\n{\n    U8 x;\n    Use(&x);\n}\n")
        self.assertFalse([v for v in run(src, _psa_cfg(report_unknown_types=True))
                          if "not checked" in v.message])

    def test_typedef_names_collected(self):
        self.assertEqual(
            collect_typedef_names(
                "typedef unsigned char BYTE;\n"
                "typedef struct { int a; } s_t, *s_p;\n"
                "typedef enum { X } e_t;\ntypedef void (*cb_t)(int);\n"),
            {"BYTE", "s_t", "s_p", "e_t", "cb_t"})


if __name__ == "__main__":
    unittest.main()
