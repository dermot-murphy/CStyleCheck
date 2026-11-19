"""
test_partial_struct.py — misc.partial_struct_assignment and
misc.partial_struct_initialiser (#456).

UV-PSI-001  Struct definition table (collect_struct_defs)
UV-PSI-002  misc.partial_struct_assignment — flagged cases
UV-PSI-003  misc.partial_struct_assignment — not-flagged cases
UV-PSI-004  misc.partial_struct_initialiser
UV-PSI-005  Cross-file struct definitions (CLI pre-pass)
"""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from harness import cfg_only, run, rules  # noqa: E402

from cstylecheck.checker import (  # noqa: E402
    collect_struct_defs, struct_rules_enabled,
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

    def test_disabled(self):
        src = _fn("    struct pt p;\n    p.x = 1;\n    Draw(p);")
        self.assertNotIn(RULE_PSA, rules(src, _psa_cfg(enabled=False)))

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


if __name__ == "__main__":
    unittest.main()
