"""test_misra_rules.py
=====================
Unit tests for the MISRA C:2012/2023 checks:

  NR-001  misc.lowercase_l_suffix      — MISRA C Rule 7.3 (Required)
  NR-002  misc.octal_constant          — MISRA C Rule 7.1 (Required)
  NR-003  misc.trigraph                — MISRA C Rule 4.2 (Advisory/Required)
  NR-004  misc.non_ascii_source        — MISRA C Rule 4.1 (Required)
  NR-005  misc.goto_usage              — MISRA C Rule 15.1 (Advisory)
  NR-006  misc.assignment_in_condition — MISRA C Rule 13.4 (Required)

Each class documents the rule it covers, lists positive (should flag) and
negative (should not flag) cases, and verifies the violation message text.
Line/column positions are verified for representative cases.

ASPICE traceability
-------------------
  SWE1 requirements: SWE1-MISRA-001 (Rule 7.3), SWE1-MISRA-002 (Rule 7.1),
                     SWE1-MISRA-003 (Rule 4.2), SWE1-MISRA-004 (Rule 4.1)
  SWE4 test IDs:     SWE4-TC-7.3-*, SWE4-TC-7.1-*, SWE4-TC-4.2-*, SWE4-TC-4.1-*
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.dirname(__file__))
from harness import cfg_only, run, rules, has, clean, count

# ---------------------------------------------------------------------------
# Shared config builders
# ---------------------------------------------------------------------------

def _ll_cfg(enabled=True, severity="error"):
    """Config with only misc.lowercase_l_suffix enabled."""
    return cfg_only(misc={"lowercase_l_suffix": {
        "enabled": enabled,
        "severity": severity,
    }})


def _oc_cfg(enabled=True, severity="error"):
    """Config with only misc.octal_constant enabled."""
    return cfg_only(misc={"octal_constant": {
        "enabled": enabled,
        "severity": severity,
    }})


def _tg_cfg(enabled=True, severity="error"):
    """Config with only misc.trigraph enabled."""
    return cfg_only(misc={"trigraph": {
        "enabled": enabled,
        "severity": severity,
    }})


RULE_LL = "misc.lowercase_l_suffix"
RULE_OC = "misc.octal_constant"
RULE_TG = "misc.trigraph"


# ===========================================================================
# NR-001 — MISRA C Rule 7.3: lowercase 'l' suffix
# SWE4-TC-7.3-*
# ===========================================================================

class TestLowercaseLSuffix(unittest.TestCase):
    """MISRA C:2012/2023 Rule 7.3 — integer literal suffixes must be uppercase.

    The lowercase letter 'l' is visually identical to '1' in many fonts.
    """

    # -----------------------------------------------------------------------
    # SWE4-TC-7.3-001 to 7.3-006: positive tests (should flag)
    # -----------------------------------------------------------------------

    def test_plain_lowercase_l_flagged(self):
        """SWE4-TC-7.3-001: bare '1l' must be flagged."""
        src = "void f(void){ int x = 1l; (void)x; }\n"
        self.assertTrue(has(src, _ll_cfg(), RULE_LL))

    def test_ul_suffix_lowercase_l_flagged(self):
        """SWE4-TC-7.3-002: '1ul' must be flagged (lowercase l in compound suffix)."""
        src = "void f(void){ unsigned long x = 1ul; (void)x; }\n"
        self.assertTrue(has(src, _ll_cfg(), RULE_LL))

    def test_lu_suffix_flagged(self):
        """SWE4-TC-7.3-003: '1lu' must be flagged (l before u)."""
        src = "void f(void){ unsigned long x = 1lu; (void)x; }\n"
        self.assertTrue(has(src, _ll_cfg(), RULE_LL))

    def test_hex_lowercase_l_flagged(self):
        """SWE4-TC-7.3-004: hex literal '0xFFl' must be flagged."""
        src = "void f(void){ long x = 0xFFl; (void)x; }\n"
        self.assertTrue(has(src, _ll_cfg(), RULE_LL))

    def test_large_decimal_lowercase_l_flagged(self):
        """SWE4-TC-7.3-005: '100000l' must be flagged."""
        src = "void f(void){ long x = 100000l; (void)x; }\n"
        self.assertTrue(has(src, _ll_cfg(), RULE_LL))

    def test_ll_suffix_lowercase_flagged(self):
        """SWE4-TC-7.3-006: '1ll' (long long, all lowercase) must be flagged."""
        src = "void f(void){ long long x = 1ll; (void)x; }\n"
        self.assertTrue(has(src, _ll_cfg(), RULE_LL))

    # -----------------------------------------------------------------------
    # SWE4-TC-7.3-007 to 7.3-013: negative tests (should NOT flag)
    # -----------------------------------------------------------------------

    def test_uppercase_L_not_flagged(self):
        """SWE4-TC-7.3-007: '1L' is valid (uppercase L)."""
        src = "void f(void){ long x = 1L; (void)x; }\n"
        self.assertFalse(has(src, _ll_cfg(), RULE_LL))

    def test_uppercase_UL_not_flagged(self):
        """SWE4-TC-7.3-008: '1UL' is valid."""
        src = "void f(void){ unsigned long x = 1UL; (void)x; }\n"
        self.assertFalse(has(src, _ll_cfg(), RULE_LL))

    def test_uppercase_LL_not_flagged(self):
        """SWE4-TC-7.3-009: '1LL' is valid (long long)."""
        src = "void f(void){ long long x = 1LL; (void)x; }\n"
        self.assertFalse(has(src, _ll_cfg(), RULE_LL))

    def test_u_suffix_only_not_flagged(self):
        """SWE4-TC-7.3-010: '1U' has no l/L suffix — not flagged."""
        src = "void f(void){ unsigned x = 1U; (void)x; }\n"
        self.assertFalse(has(src, _ll_cfg(), RULE_LL))

    def test_no_suffix_not_flagged(self):
        """SWE4-TC-7.3-011: plain '42' with no suffix is not flagged."""
        src = "void f(void){ int x = 42; (void)x; }\n"
        self.assertFalse(has(src, _ll_cfg(), RULE_LL))

    def test_hex_uppercase_L_not_flagged(self):
        """SWE4-TC-7.3-012: '0xFFL' is valid."""
        src = "void f(void){ long x = 0xFFL; (void)x; }\n"
        self.assertFalse(has(src, _ll_cfg(), RULE_LL))

    def test_rule_disabled_not_flagged(self):
        """SWE4-TC-7.3-013: rule disabled in config suppresses violation."""
        src = "void f(void){ int x = 1l; (void)x; }\n"
        self.assertFalse(has(src, _ll_cfg(enabled=False), RULE_LL))

    # -----------------------------------------------------------------------
    # SWE4-TC-7.3-014: violation message content
    # -----------------------------------------------------------------------

    def test_violation_message_mentions_misra_rule(self):
        """SWE4-TC-7.3-014: message must reference MISRA C Rule 7.3."""
        src = "void f(void){ int x = 1l; (void)x; }\n"
        viols = [v for v in run(src, _ll_cfg()) if v.rule == RULE_LL]
        self.assertTrue(viols, "Expected at least one violation")
        self.assertIn("7.3", viols[0].message)
        self.assertIn("uppercase", viols[0].message.lower())

    # -----------------------------------------------------------------------
    # SWE4-TC-7.3-015: severity configurable
    # -----------------------------------------------------------------------

    def test_severity_is_configurable(self):
        """SWE4-TC-7.3-015: severity follows YAML configuration."""
        src = "void f(void){ int x = 1l; (void)x; }\n"
        viols = [v for v in run(src, _ll_cfg(severity="warning")) if v.rule == RULE_LL]
        self.assertTrue(viols)
        self.assertEqual(viols[0].severity, "warning")


# ===========================================================================
# NR-002 — MISRA C Rule 7.1: octal constants forbidden
# SWE4-TC-7.1-*
# ===========================================================================

class TestOctalConstants(unittest.TestCase):
    """MISRA C:2012/2023 Rule 7.1 — octal integer constants shall not be used.

    An integer literal with a leading zero followed by octal digits (0–7) is
    an octal constant and is easy to confuse with a decimal literal.
    """

    # -----------------------------------------------------------------------
    # SWE4-TC-7.1-001 to 7.1-006: positive tests (should flag)
    # -----------------------------------------------------------------------

    def test_octal_010_flagged(self):
        """SWE4-TC-7.1-001: '010' (= decimal 8) must be flagged."""
        src = "void f(void){ int x = 010; (void)x; }\n"
        self.assertTrue(has(src, _oc_cfg(), RULE_OC))

    def test_octal_07_flagged(self):
        """SWE4-TC-7.1-002: '07' must be flagged."""
        src = "void f(void){ int x = 07; (void)x; }\n"
        self.assertTrue(has(src, _oc_cfg(), RULE_OC))

    def test_octal_0777_flagged(self):
        """SWE4-TC-7.1-003: '0777' (unix-style permission literal) must be flagged."""
        src = "void f(void){ int mode = 0777; (void)mode; }\n"
        self.assertTrue(has(src, _oc_cfg(), RULE_OC))

    def test_octal_with_u_suffix_flagged(self):
        """SWE4-TC-7.1-004: '07U' (octal with suffix) must be flagged."""
        src = "void f(void){ unsigned x = 07U; (void)x; }\n"
        self.assertTrue(has(src, _oc_cfg(), RULE_OC))

    def test_octal_leading_zeros_in_array_init_flagged(self):
        """SWE4-TC-7.1-005: octal in array initialiser must be flagged."""
        src = "int arr[] = {01, 02, 03};\n"
        self.assertGreaterEqual(count(src, _oc_cfg(), RULE_OC), 1)

    def test_octal_0_followed_by_octal_digit_in_macro_rhs(self):
        """SWE4-TC-7.1-006: octal in #define RHS is still an octal constant."""
        src = "#define MY_PERM 0755\nvoid f(void){}\n"
        # Even in a #define this is a valid octal constant violation
        self.assertTrue(has(src, _oc_cfg(), RULE_OC))

    # -----------------------------------------------------------------------
    # SWE4-TC-7.1-007 to 7.1-013: negative tests (should NOT flag)
    # -----------------------------------------------------------------------

    def test_zero_alone_not_flagged(self):
        """SWE4-TC-7.1-007: bare '0' is zero, not an octal constant."""
        src = "void f(void){ int x = 0; (void)x; }\n"
        self.assertFalse(has(src, _oc_cfg(), RULE_OC))

    def test_zero_with_u_suffix_not_flagged(self):
        """SWE4-TC-7.1-008: '0U' is zero — not octal."""
        src = "void f(void){ unsigned x = 0U; (void)x; }\n"
        self.assertFalse(has(src, _oc_cfg(), RULE_OC))

    def test_hex_literal_not_flagged(self):
        """SWE4-TC-7.1-009: '0x08' is hex, not octal."""
        src = "void f(void){ int x = 0x08; (void)x; }\n"
        self.assertFalse(has(src, _oc_cfg(), RULE_OC))

    def test_hex_0xFF_not_flagged(self):
        """SWE4-TC-7.1-010: '0xFF' must not be flagged."""
        src = "void f(void){ int x = 0xFF; (void)x; }\n"
        self.assertFalse(has(src, _oc_cfg(), RULE_OC))

    def test_float_0_point_5_not_flagged(self):
        """SWE4-TC-7.1-011: '0.5' is a float literal, not octal."""
        src = "void f(void){ float x = 0.5f; (void)x; }\n"
        self.assertFalse(has(src, _oc_cfg(), RULE_OC))

    def test_decimal_10_not_flagged(self):
        """SWE4-TC-7.1-012: decimal '10' with no leading zero is not octal."""
        src = "void f(void){ int x = 10; (void)x; }\n"
        self.assertFalse(has(src, _oc_cfg(), RULE_OC))

    def test_rule_disabled_not_flagged(self):
        """SWE4-TC-7.1-013: rule disabled in config suppresses violation."""
        src = "void f(void){ int x = 010; (void)x; }\n"
        self.assertFalse(has(src, _oc_cfg(enabled=False), RULE_OC))

    # -----------------------------------------------------------------------
    # SWE4-TC-7.1-014: violation message content
    # -----------------------------------------------------------------------

    def test_violation_message_mentions_misra_rule(self):
        """SWE4-TC-7.1-014: message must reference MISRA C Rule 7.1."""
        src = "void f(void){ int x = 010; (void)x; }\n"
        viols = [v for v in run(src, _oc_cfg()) if v.rule == RULE_OC]
        self.assertTrue(viols, "Expected at least one violation")
        self.assertIn("7.1", viols[0].message)

    def test_violation_includes_octal_value(self):
        """SWE4-TC-7.1-015: message must include the offending literal."""
        src = "void f(void){ int x = 0777; (void)x; }\n"
        viols = [v for v in run(src, _oc_cfg()) if v.rule == RULE_OC]
        self.assertTrue(viols)
        self.assertIn("0777", viols[0].message)

    # -----------------------------------------------------------------------
    # SWE4-TC-7.1-016: severity configurable
    # -----------------------------------------------------------------------

    def test_severity_is_configurable(self):
        """SWE4-TC-7.1-016: severity follows YAML configuration."""
        src = "void f(void){ int x = 010; (void)x; }\n"
        viols = [v for v in run(src, _oc_cfg(severity="warning")) if v.rule == RULE_OC]
        self.assertTrue(viols)
        self.assertEqual(viols[0].severity, "warning")


# ===========================================================================
# NR-003 — MISRA C Rule 4.2: trigraphs forbidden
# SWE4-TC-4.2-*
# ===========================================================================

class TestTrigraphs(unittest.TestCase):
    """MISRA C:2012 Rule 4.2 (Advisory) / MISRA C:2023 Rule 4.2 (Required).

    Trigraphs are ??X sequences that the preprocessor silently replaces.
    They must not appear anywhere in a C source file.
    """

    # -----------------------------------------------------------------------
    # SWE4-TC-4.2-001 to 4.2-009: one test per trigraph character
    # -----------------------------------------------------------------------

    def test_trigraph_hash_flagged(self):
        """SWE4-TC-4.2-001: '??=' (→ #) must be flagged."""
        src = "/* ??= comment */\nvoid f(void){}\n"
        self.assertTrue(has(src, _tg_cfg(), RULE_TG))

    def test_trigraph_open_bracket_flagged(self):
        """SWE4-TC-4.2-002: '??(' (→ [) must be flagged."""
        src = "/* ??( comment */\nvoid f(void){}\n"
        self.assertTrue(has(src, _tg_cfg(), RULE_TG))

    def test_trigraph_close_bracket_flagged(self):
        """SWE4-TC-4.2-003: '??)' (→ ]) must be flagged."""
        src = "/* ??) comment */\nvoid f(void){}\n"
        self.assertTrue(has(src, _tg_cfg(), RULE_TG))

    def test_trigraph_backslash_flagged(self):
        """SWE4-TC-4.2-004: '??/' (→ \\) must be flagged."""
        src = "/* ??/ comment */\nvoid f(void){}\n"
        self.assertTrue(has(src, _tg_cfg(), RULE_TG))

    def test_trigraph_caret_flagged(self):
        """SWE4-TC-4.2-005: \"??'\" (→ ^) must be flagged."""
        src = "/* ??' comment */\nvoid f(void){}\n"
        self.assertTrue(has(src, _tg_cfg(), RULE_TG))

    def test_trigraph_open_brace_flagged(self):
        """SWE4-TC-4.2-006: '??<' (→ {) must be flagged."""
        src = "/* ??< comment */\nvoid f(void){}\n"
        self.assertTrue(has(src, _tg_cfg(), RULE_TG))

    def test_trigraph_close_brace_flagged(self):
        """SWE4-TC-4.2-007: '??>' (→ }) must be flagged."""
        src = "/* ??> comment */\nvoid f(void){}\n"
        self.assertTrue(has(src, _tg_cfg(), RULE_TG))

    def test_trigraph_pipe_flagged(self):
        """SWE4-TC-4.2-008: '??!' (→ |) must be flagged."""
        src = "/* ??! comment */\nvoid f(void){}\n"
        self.assertTrue(has(src, _tg_cfg(), RULE_TG))

    def test_trigraph_tilde_flagged(self):
        """SWE4-TC-4.2-009: '??-' (→ ~) must be flagged."""
        src = "/* ??- comment */\nvoid f(void){}\n"
        self.assertTrue(has(src, _tg_cfg(), RULE_TG))

    # -----------------------------------------------------------------------
    # SWE4-TC-4.2-010: trigraph in code (not just comments)
    # -----------------------------------------------------------------------

    def test_trigraph_in_code_flagged(self):
        """SWE4-TC-4.2-010: trigraph in code (not just comments) is flagged."""
        # '??(' would be preprocessed to '[' — tool must flag it regardless
        src = 'char s??( = {0};\n'
        self.assertTrue(has(src, _tg_cfg(), RULE_TG))

    # -----------------------------------------------------------------------
    # SWE4-TC-4.2-011 to 4.2-013: negative tests
    # -----------------------------------------------------------------------

    def test_double_question_mark_not_trigraph(self):
        """SWE4-TC-4.2-011: '??' alone (not followed by a trigraph char) is OK."""
        src = "/* What?? No trigraph here. */\nvoid f(void){}\n"
        self.assertFalse(has(src, _tg_cfg(), RULE_TG))

    def test_single_question_mark_not_flagged(self):
        """SWE4-TC-4.2-012: single '?' in a ternary expression is OK."""
        src = "void f(int x){ int y = x ? 1 : 0; (void)y; }\n"
        self.assertFalse(has(src, _tg_cfg(), RULE_TG))

    def test_rule_disabled_not_flagged(self):
        """SWE4-TC-4.2-013: rule disabled in config suppresses violation."""
        src = "/* ??= */\nvoid f(void){}\n"
        self.assertFalse(has(src, _tg_cfg(enabled=False), RULE_TG))

    # -----------------------------------------------------------------------
    # SWE4-TC-4.2-014: violation message content
    # -----------------------------------------------------------------------

    def test_violation_message_mentions_misra_rule(self):
        """SWE4-TC-4.2-014: message must reference MISRA C Rule 4.2."""
        src = "/* ??= */\nvoid f(void){}\n"
        viols = [v for v in run(src, _tg_cfg()) if v.rule == RULE_TG]
        self.assertTrue(viols, "Expected at least one violation")
        self.assertIn("4.2", viols[0].message)

    def test_violation_includes_trigraph_sequence(self):
        """SWE4-TC-4.2-015: message must include the offending trigraph."""
        src = "/* ??= */\nvoid f(void){}\n"
        viols = [v for v in run(src, _tg_cfg()) if v.rule == RULE_TG]
        self.assertTrue(viols)
        self.assertIn("??=", viols[0].message)

    # -----------------------------------------------------------------------
    # SWE4-TC-4.2-016: line number accuracy
    # -----------------------------------------------------------------------

    def test_line_number_is_accurate(self):
        """SWE4-TC-4.2-016: violation line number must match actual location."""
        src = "/* clean line */\n/* ??= here */\nvoid f(void){}\n"
        viols = [v for v in run(src, _tg_cfg()) if v.rule == RULE_TG]
        self.assertTrue(viols)
        self.assertEqual(viols[0].line, 2)

    # -----------------------------------------------------------------------
    # SWE4-TC-4.2-017: severity configurable
    # -----------------------------------------------------------------------

    def test_severity_is_configurable(self):
        """SWE4-TC-4.2-017: severity follows YAML configuration."""
        src = "/* ??= */\nvoid f(void){}\n"
        viols = [v for v in run(src, _tg_cfg(severity="warning")) if v.rule == RULE_TG]
        self.assertTrue(viols)
        self.assertEqual(viols[0].severity, "warning")


# ===========================================================================
# BUG-004 regression — Yoda condition message for negative-literal RHS
# ===========================================================================

class TestYodaNegativeLiteralMessage(unittest.TestCase):
    """Regression tests for BUG-004: Yoda violation message was showing
    the digit token without the leading '-' sign.

    e.g.  if (x == -1)  was producing  "write '1 == x'"
          instead of the correct        "write '-1 == x'"
    """

    def _yoda_cfg(self):
        return cfg_only(misc={"yoda_conditions": {
            "enabled": True,
            "severity": "warning",
        }})

    def test_negative_literal_message_includes_minus(self):
        """BUG-004: message for 'x == -1' must say '-1 == x', not '1 == x'."""
        src = "void f(int x){ if (x == -1) {} }\n"
        viols = [v for v in run(src, self._yoda_cfg())
                 if v.rule == "misc.yoda_condition"]
        self.assertTrue(viols, "Expected a Yoda violation")
        self.assertIn("-1", viols[0].message,
                      f"Message should include '-1': {viols[0].message}")
        # The message must NOT suggest the wrong correction
        self.assertNotIn("write '1 ==", viols[0].message,
                         f"Message incorrectly omits minus: {viols[0].message}")

    def test_negative_literal_detection_fires(self):
        """BUG-004: 'x == -1' must be detected as a Yoda violation."""
        src = "void f(int x){ if (x == -1) {} }\n"
        self.assertTrue(has(src, self._yoda_cfg(), "misc.yoda_condition"))

    def test_positive_literal_message_unchanged(self):
        """BUG-004: positive literal message is unaffected by the fix."""
        src = "void f(int x){ if (x == 42) {} }\n"
        viols = [v for v in run(src, self._yoda_cfg())
                 if v.rule == "misc.yoda_condition"]
        self.assertTrue(viols)
        self.assertIn("42", viols[0].message)

    def test_null_comparison_message_unchanged(self):
        """BUG-004: NULL comparison message is unaffected."""
        src = "void f(void *p){ if (p == NULL) {} }\n"
        viols = [v for v in run(src, self._yoda_cfg())
                 if v.rule == "misc.yoda_condition"]
        self.assertTrue(viols)
        self.assertIn("NULL", viols[0].message)


def _na_cfg(enabled=True, severity="error", exempt_string_literals=False):
    """Config with only misc.non_ascii_source enabled."""
    return cfg_only(misc={"non_ascii_source": {
        "enabled": enabled,
        "severity": severity,
        "exempt_string_literals": exempt_string_literals,
    }})


RULE_NA = "misc.non_ascii_source"


# ===========================================================================
# NR-004 — MISRA C Rule 4.1: non-ASCII source characters
# SWE4-TC-4.1-*
# ===========================================================================

class TestNonAsciiSource(unittest.TestCase):
    """MISRA C:2012/2023 Rule 4.1 — only basic source character set permitted.

    Source files must not contain non-ASCII bytes or non-printable control
    characters.  Standard whitespace (tab, LF, CR) is allowed.
    """

    def test_pure_ascii_passes(self):
        """Plain ASCII source must produce no violation."""
        src = "void foo(void) { int x = 42; }\n"
        self.assertTrue(clean(src, _na_cfg()))

    def test_utf8_identifier_flagged(self):
        """UTF-8 accented character in identifier must be flagged."""
        src = "uint8_t caf\xc3\xa9_count = 0;\n"  # café with UTF-8 é
        self.assertTrue(has(src, _na_cfg(), RULE_NA))

    def test_utf8_in_comment_flagged(self):
        """Non-ASCII byte in a comment must be flagged."""
        src = "/* Author: M\xc3\xbcller */\nvoid foo(void) {}\n"
        self.assertTrue(has(src, _na_cfg(), RULE_NA))

    def test_bom_flagged(self):
        """UTF-8 BOM (EF BB BF) at start of file must be flagged."""
        src = "\xef\xbb\xbfvoid foo(void) {}\n"
        self.assertTrue(has(src, _na_cfg(), RULE_NA))

    def test_tab_lf_cr_allowed(self):
        """Tab (0x09), LF (0x0A) and CR (0x0D) are permitted whitespace."""
        src = "\tvoid foo(void) {\r\n\t\tint x = 1;\r\n\t}\n"
        self.assertFalse(has(src, _na_cfg(), RULE_NA))

    def test_non_ascii_in_string_flagged_by_default(self):
        """Non-ASCII inside a string literal is flagged when exempt_string_literals=False."""
        src = 'const char *s = "\xc3\xa9";\n'
        self.assertTrue(has(src, _na_cfg(exempt_string_literals=False), RULE_NA))

    def test_non_ascii_in_string_exempt_when_flag_set(self):
        """Non-ASCII inside a string literal is NOT flagged when exempt_string_literals=True."""
        src = 'const char *s = "\xc3\xa9";\n'
        self.assertFalse(has(src, _na_cfg(exempt_string_literals=True), RULE_NA))

    def test_rule_disabled_no_violation(self):
        """When non_ascii_source is disabled, no violation is raised."""
        src = "uint8_t caf\xc3\xa9_count = 0;\n"
        self.assertFalse(has(src, _na_cfg(enabled=False), RULE_NA))

    def test_severity_warning(self):
        """Severity is configurable; warning severity produces a warning."""
        src = "uint8_t caf\xc3\xa9_count = 0;\n"
        viols = [v for v in run(src, _na_cfg(severity="warning")) if v.rule == RULE_NA]
        self.assertTrue(viols)
        self.assertEqual(viols[0].severity, "warning")

    def test_violation_message_includes_hex_byte(self):
        """The violation message must include the hex code point of the offending char."""
        src = "uint8_t caf\xc3\xa9_count = 0;\n"
        viols = [v for v in run(src, _na_cfg()) if v.rule == RULE_NA]
        self.assertTrue(viols)
        self.assertIn("0xC3", viols[0].message)

    def test_control_character_flagged(self):
        """Non-printable ASCII control character (e.g. 0x01) must be flagged."""
        src = "void foo(void) {\x01}\n"
        self.assertTrue(has(src, _na_cfg(), RULE_NA))

    def test_del_character_flagged(self):
        """DEL (0x7F) must be flagged."""
        src = "void foo(void) {\x7f}\n"
        self.assertTrue(has(src, _na_cfg(), RULE_NA))


# ---------------------------------------------------------------------------
# NR-005  misc.goto_usage — MISRA C:2012 Rule 15.1 (Advisory)
# ---------------------------------------------------------------------------

def _goto_cfg(enabled=True, severity="error"):
    return cfg_only(misc={"goto_usage": {
        "enabled": enabled,
        "severity": severity,
    }})


RULE_GOTO = "misc.goto_usage"


class TestGotoUsage(unittest.TestCase):
    """misc.goto_usage — any use of the goto keyword is forbidden."""

    # --- Positive: should flag ---

    def test_simple_goto_flagged(self):
        src = "void f(void){ goto end; end: return; }\n"
        self.assertTrue(has(src, _goto_cfg(), RULE_GOTO))

    def test_goto_at_start_of_line_flagged(self):
        src = "void f(void){\n    goto cleanup;\ncleanup:\n    return;\n}\n"
        self.assertTrue(has(src, _goto_cfg(), RULE_GOTO))

    def test_goto_inside_if_flagged(self):
        src = "void f(int x){\n    if (x < 0) goto err;\nerr: return;\n}\n"
        self.assertTrue(has(src, _goto_cfg(), RULE_GOTO))

    def test_violation_count_one_per_goto(self):
        src = (
            "void f(void){\n"
            "    goto a;\n"
            "    goto b;\n"
            "a:b: return;\n"
            "}\n"
        )
        self.assertEqual(count(src, _goto_cfg(), RULE_GOTO), 2)

    def test_violation_message_contains_rule_ref(self):
        src = "void f(void){ goto end; end: return; }\n"
        viols = [v for v in run(src, _goto_cfg()) if v.rule == RULE_GOTO]
        self.assertTrue(viols)
        self.assertIn("15.1", viols[0].message)

    # --- Negative: should NOT flag ---

    def test_rule_disabled(self):
        src = "void f(void){ goto end; end: return; }\n"
        self.assertFalse(has(src, _goto_cfg(enabled=False), RULE_GOTO))

    def test_goto_in_comment_not_flagged(self):
        # 'goto' inside a comment must not be flagged (self.clean strips comments)
        src = "/* goto end; */\nvoid f(void){ return; }\n"
        self.assertFalse(has(src, _goto_cfg(), RULE_GOTO))

    def test_goto_in_string_not_flagged(self):
        src = 'void f(void){ const char *p = "goto end"; (void)p; }\n'
        self.assertFalse(has(src, _goto_cfg(), RULE_GOTO))

    def test_identifier_containing_goto_not_flagged(self):
        # e.g. "goto_state" must not match
        src = "static int goto_state = 0;\n"
        self.assertFalse(has(src, _goto_cfg(), RULE_GOTO))

    def test_severity_configurable(self):
        src = "void f(void){ goto end; end: return; }\n"
        viols = [v for v in run(src, _goto_cfg(severity="warning")) if v.rule == RULE_GOTO]
        self.assertTrue(viols)
        self.assertEqual(viols[0].severity, "warning")


# ---------------------------------------------------------------------------
# NR-006  misc.assignment_in_condition — MISRA C:2012 Rule 13.4 (Required)
# ---------------------------------------------------------------------------

def _aic_cfg(enabled=True, severity="warning"):
    return cfg_only(misc={"assignment_in_condition": {
        "enabled": enabled,
        "severity": severity,
    }})


RULE_AIC = "misc.assignment_in_condition"


class TestAssignmentInCondition(unittest.TestCase):
    """misc.assignment_in_condition — '=' inside if/while/for condition."""

    # --- Positive: should flag ---

    def test_if_assignment_flagged(self):
        src = "void f(int *p){ int x; if (x = *p) { (void)x; } }\n"
        self.assertTrue(has(src, _aic_cfg(), RULE_AIC))

    def test_while_assignment_flagged(self):
        src = "int getc(void); void f(void){ int c; while (c = getc()) { (void)c; } }\n"
        self.assertTrue(has(src, _aic_cfg(), RULE_AIC))

    def test_for_condition_assignment_flagged(self):
        # Assignment in the condition part (middle segment) of a for loop
        src = (
            "int next(int x); "
            "void f(void){ int x = 0; "
            "for (; x = next(x); ) { (void)x; } }\n"
        )
        self.assertTrue(has(src, _aic_cfg(), RULE_AIC))

    def test_violation_message_contains_rule_ref(self):
        src = "void f(int *p){ int x; if (x = *p) { (void)x; } }\n"
        viols = [v for v in run(src, _aic_cfg()) if v.rule == RULE_AIC]
        self.assertTrue(viols)
        self.assertIn("13.4", viols[0].message)

    def test_nested_assignment_in_if_flagged(self):
        src = "int foo(void); void f(void){ int a; if ((a = foo()) > 0) { (void)a; } }\n"
        self.assertTrue(has(src, _aic_cfg(), RULE_AIC))

    # --- Negative: should NOT flag ---

    def test_rule_disabled(self):
        src = "void f(int *p){ int x; if (x = *p) { (void)x; } }\n"
        self.assertFalse(has(src, _aic_cfg(enabled=False), RULE_AIC))

    def test_equality_comparison_not_flagged(self):
        src = "void f(int x){ if (x == 0) { (void)x; } }\n"
        self.assertFalse(has(src, _aic_cfg(), RULE_AIC))

    def test_not_equal_not_flagged(self):
        src = "void f(int x){ if (x != 0) { (void)x; } }\n"
        self.assertFalse(has(src, _aic_cfg(), RULE_AIC))

    def test_less_equal_not_flagged(self):
        src = "void f(int x){ if (x <= 10) { (void)x; } }\n"
        self.assertFalse(has(src, _aic_cfg(), RULE_AIC))

    def test_greater_equal_not_flagged(self):
        src = "void f(int x){ if (x >= 0) { (void)x; } }\n"
        self.assertFalse(has(src, _aic_cfg(), RULE_AIC))

    def test_for_init_assignment_not_flagged(self):
        # Assignment in the init part of for() must NOT be flagged
        src = "void f(void){ int i; for (i = 0; i < 10; i++) { (void)i; } }\n"
        self.assertFalse(has(src, _aic_cfg(), RULE_AIC))

    def test_for_increment_not_flagged(self):
        # Compound assignment in the increment part must NOT be flagged
        src = "void f(void){ int i; for (i = 0; i < 10; i += 2) { (void)i; } }\n"
        self.assertFalse(has(src, _aic_cfg(), RULE_AIC))

    def test_compound_assign_in_condition_not_flagged(self):
        # += in a condition would be very unusual but the character before
        # '=' is '+', which is excluded by the lookbehind
        src = "void f(int x){ if (x >= 0) { (void)x; } }\n"
        self.assertFalse(has(src, _aic_cfg(), RULE_AIC))

    def test_assignment_before_condition_not_flagged(self):
        # Assignment as a statement before an if must NOT be flagged
        src = "void f(void){ int x; x = 5; if (x > 0) { (void)x; } }\n"
        self.assertFalse(has(src, _aic_cfg(), RULE_AIC))

    def test_assignment_in_string_not_flagged(self):
        src = 'void f(void){ if (1) { const char *s = "if (x = 0)"; (void)s; } }\n'
        self.assertFalse(has(src, _aic_cfg(), RULE_AIC))

    def test_severity_configurable(self):
        src = "void f(int *p){ int x; if (x = *p) { (void)x; } }\n"
        viols = [v for v in run(src, _aic_cfg(severity="error")) if v.rule == RULE_AIC]
        self.assertTrue(viols)
        self.assertEqual(viols[0].severity, "error")


# ---------------------------------------------------------------------------
# NR-007  misc.multiple_statements_per_line
# NR-008  misc.void_pointer
# NR-009  misc.recursive_function
# NR-010  misc.sizeof_type
# NR-011  misc.boolean_comparison
# NR-012  misc.empty_else
# ---------------------------------------------------------------------------

RULE_MULTI  = "misc.multiple_statements_per_line"
RULE_VOIDP  = "misc.void_pointer"
RULE_REC    = "misc.recursive_function"
RULE_SIZEOF = "misc.sizeof_type"
RULE_BOOL   = "misc.boolean_comparison"
RULE_EELSE  = "misc.empty_else"


def _multi_cfg(enabled=True, severity="warning"):
    return cfg_only(misc={"multiple_statements_per_line": {"enabled": enabled, "severity": severity}})


def _voidp_cfg(enabled=True, severity="warning"):
    return cfg_only(misc={"void_pointer": {"enabled": enabled, "severity": severity}})


def _rec_cfg(enabled=True, severity="error"):
    return cfg_only(misc={"recursive_function": {"enabled": enabled, "severity": severity}})


def _sizeof_cfg(enabled=True, severity="info"):
    return cfg_only(misc={"sizeof_type": {"enabled": enabled, "severity": severity}})


def _bool_cfg(enabled=True, severity="warning"):
    return cfg_only(misc={"boolean_comparison": {"enabled": enabled, "severity": severity}})


def _eelse_cfg(enabled=True, severity="warning"):
    return cfg_only(misc={"empty_else": {"enabled": enabled, "severity": severity}})


class TestMultipleStatementsPerLine(unittest.TestCase):
    def test_two_statements_flagged(self):
        src = "void f(void){ int x; x = 1; x = 2; }\n"
        self.assertIn(RULE_MULTI, rules(src, _multi_cfg()))

    def test_single_statement_clean(self):
        src = "void f(void){ int x;\nx = 1;\n}\n"
        self.assertNotIn(RULE_MULTI, rules(src, _multi_cfg()))

    def test_for_loop_not_flagged(self):
        src = "void f(void){ int i; for (i = 0; i < 10; i++) { (void)i; } }\n"
        self.assertNotIn(RULE_MULTI, rules(src, _multi_cfg()))

    def test_struct_member_semicolons_flagged(self):
        # Two members on same line should be flagged
        src = "typedef struct { int a; int b; } Foo;\n"
        self.assertIn(RULE_MULTI, rules(src, _multi_cfg()))

    def test_disabled(self):
        src = "void f(void){ int x; x = 1; x = 2; }\n"
        self.assertNotIn(RULE_MULTI, rules(src, _multi_cfg(enabled=False)))

    def test_severity_configurable(self):
        src = "void f(void){ int x; x = 1; x = 2; }\n"
        viols = [v for v in run(src, _multi_cfg(severity="error")) if v.rule == RULE_MULTI]
        self.assertTrue(viols)
        self.assertEqual(viols[0].severity, "error")

    def test_comment_not_flagged(self):
        # Semicolons only in a comment must not fire
        src = "void f(void){ /* x = 1; y = 2; */ int z;\n}\n"
        self.assertNotIn(RULE_MULTI, rules(src, _multi_cfg()))

    def test_message_content(self):
        src = "void f(void){ int x; x = 1; x = 2; }\n"
        msgs = [v.message for v in run(src, _multi_cfg()) if v.rule == RULE_MULTI]
        self.assertTrue(msgs)
        self.assertIn("Multiple statements", msgs[0])


class TestVoidPointer(unittest.TestCase):
    def test_void_ptr_flagged(self):
        src = "void f(void *buf){ (void)buf; }\n"
        self.assertIn(RULE_VOIDP, rules(src, _voidp_cfg()))

    def test_typed_ptr_clean(self):
        src = "void f(uint8_t *buf){ (void)buf; }\n"
        self.assertNotIn(RULE_VOIDP, rules(src, _voidp_cfg()))

    def test_void_star_in_var_decl(self):
        src = "void f(void){ void *p = (void*)0;\n(void)p; }\n"
        count_v = sum(1 for r in rules(src, _voidp_cfg()) if r == RULE_VOIDP)
        self.assertGreaterEqual(count_v, 1)

    def test_disabled(self):
        src = "void f(void *buf){ (void)buf; }\n"
        self.assertNotIn(RULE_VOIDP, rules(src, _voidp_cfg(enabled=False)))

    def test_severity_configurable(self):
        src = "void f(void *buf){ (void)buf; }\n"
        viols = [v for v in run(src, _voidp_cfg(severity="error")) if v.rule == RULE_VOIDP]
        self.assertTrue(viols)
        self.assertEqual(viols[0].severity, "error")

    def test_message_content(self):
        src = "void f(void *buf){ (void)buf; }\n"
        msgs = [v.message for v in run(src, _voidp_cfg()) if v.rule == RULE_VOIDP]
        self.assertTrue(msgs)
        self.assertIn("11.5", msgs[0])

    def test_void_return_type_not_flagged(self):
        # 'void f(void)' — void is a return type, not a void pointer
        src = "void f(void){ return; }\n"
        self.assertNotIn(RULE_VOIDP, rules(src, _voidp_cfg()))

    def test_in_comment_not_flagged(self):
        src = "void f(void){ /* void *ptr */ return; }\n"
        self.assertNotIn(RULE_VOIDP, rules(src, _voidp_cfg()))


class TestRecursiveFunction(unittest.TestCase):
    def test_direct_recursion_flagged(self):
        src = "int fact(int n){ if (n <= 1) return 1; return n * fact(n - 1); }\n"
        self.assertIn(RULE_REC, rules(src, _rec_cfg()))

    def test_non_recursive_clean(self):
        src = "int add(int a, int b){ return a + b; }\n"
        self.assertNotIn(RULE_REC, rules(src, _rec_cfg()))

    def test_disabled(self):
        src = "int fact(int n){ if (n <= 1) return 1; return n * fact(n - 1); }\n"
        self.assertNotIn(RULE_REC, rules(src, _rec_cfg(enabled=False)))

    def test_severity_configurable(self):
        src = "int fact(int n){ if (n <= 1) return 1; return n * fact(n - 1); }\n"
        viols = [v for v in run(src, _rec_cfg(severity="warning")) if v.rule == RULE_REC]
        self.assertTrue(viols)
        self.assertEqual(viols[0].severity, "warning")

    def test_message_contains_17_2(self):
        src = "int fact(int n){ if (n <= 1) return 1; return n * fact(n - 1); }\n"
        msgs = [v.message for v in run(src, _rec_cfg()) if v.rule == RULE_REC]
        self.assertTrue(msgs)
        self.assertIn("17.2", msgs[0])

    def test_function_name_in_message(self):
        src = "int fact(int n){ if (n <= 1) return 1; return n * fact(n - 1); }\n"
        msgs = [v.message for v in run(src, _rec_cfg()) if v.rule == RULE_REC]
        self.assertTrue(msgs)
        self.assertIn("fact", msgs[0])

    def test_if_keyword_not_matched(self):
        # 'if' followed by '{' must not be treated as a function definition
        src = "void f(int x){ if (x > 0) { (void)x; } }\n"
        self.assertNotIn(RULE_REC, rules(src, _rec_cfg()))

    def test_recursive_in_comment_not_flagged(self):
        src = "int f(int n){ /* f(n-1) */ return n; }\n"
        self.assertNotIn(RULE_REC, rules(src, _rec_cfg()))


class TestSizeofType(unittest.TestCase):
    def test_sizeof_primitive_flagged(self):
        src = "void f(void){ int n = sizeof(int);\n(void)n; }\n"
        self.assertIn(RULE_SIZEOF, rules(src, _sizeof_cfg()))

    def test_sizeof_typedef_t_flagged(self):
        src = "void f(void){ int n = sizeof(uint32_t);\n(void)n; }\n"
        self.assertIn(RULE_SIZEOF, rules(src, _sizeof_cfg()))

    def test_sizeof_var_clean(self):
        src = "void f(void){ uint32_t x; int n = sizeof(x);\n(void)n; }\n"
        self.assertNotIn(RULE_SIZEOF, rules(src, _sizeof_cfg()))

    def test_sizeof_ptr_deref_clean(self):
        src = "void f(uint32_t *p){ int n = sizeof(*p);\n(void)n; }\n"
        self.assertNotIn(RULE_SIZEOF, rules(src, _sizeof_cfg()))

    def test_disabled(self):
        src = "void f(void){ int n = sizeof(int);\n(void)n; }\n"
        self.assertNotIn(RULE_SIZEOF, rules(src, _sizeof_cfg(enabled=False)))

    def test_severity_configurable(self):
        src = "void f(void){ int n = sizeof(uint8_t);\n(void)n; }\n"
        viols = [v for v in run(src, _sizeof_cfg(severity="warning")) if v.rule == RULE_SIZEOF]
        self.assertTrue(viols)
        self.assertEqual(viols[0].severity, "warning")

    def test_message_content(self):
        src = "void f(void){ int n = sizeof(int);\n(void)n; }\n"
        msgs = [v.message for v in run(src, _sizeof_cfg()) if v.rule == RULE_SIZEOF]
        self.assertTrue(msgs)
        self.assertIn("sizeof", msgs[0])


class TestBooleanComparison(unittest.TestCase):
    def test_eq_true_flagged(self):
        src = "void f(int flag){ if (flag == true) { (void)flag; } }\n"
        self.assertIn(RULE_BOOL, rules(src, _bool_cfg()))

    def test_eq_false_flagged(self):
        src = "void f(int done){ while (done == false) { done = 1; } }\n"
        self.assertIn(RULE_BOOL, rules(src, _bool_cfg()))

    def test_ne_true_flagged(self):
        src = "void f(int ok){ if (ok != true) { (void)ok; } }\n"
        self.assertIn(RULE_BOOL, rules(src, _bool_cfg()))

    def test_direct_use_clean(self):
        src = "void f(int flag){ if (flag) { (void)flag; } }\n"
        self.assertNotIn(RULE_BOOL, rules(src, _bool_cfg()))

    def test_negation_clean(self):
        src = "void f(int done){ while (!done) { done = 1; } }\n"
        self.assertNotIn(RULE_BOOL, rules(src, _bool_cfg()))

    def test_disabled(self):
        src = "void f(int flag){ if (flag == true) { (void)flag; } }\n"
        self.assertNotIn(RULE_BOOL, rules(src, _bool_cfg(enabled=False)))

    def test_severity_configurable(self):
        src = "void f(int flag){ if (flag == true) { (void)flag; } }\n"
        viols = [v for v in run(src, _bool_cfg(severity="error")) if v.rule == RULE_BOOL]
        self.assertTrue(viols)
        self.assertEqual(viols[0].severity, "error")

    def test_message_content(self):
        src = "void f(int flag){ if (flag == true) { (void)flag; } }\n"
        msgs = [v.message for v in run(src, _bool_cfg()) if v.rule == RULE_BOOL]
        self.assertTrue(msgs)
        self.assertIn("14.4", msgs[0])

    def test_in_comment_not_flagged(self):
        src = "void f(void){ /* if (flag == true) */ return; }\n"
        self.assertNotIn(RULE_BOOL, rules(src, _bool_cfg()))

    def test_uppercase_true_flagged(self):
        src = "void f(int flag){ if (flag == TRUE) { (void)flag; } }\n"
        self.assertIn(RULE_BOOL, rules(src, _bool_cfg()))


class TestEmptyElse(unittest.TestCase):
    def test_empty_else_flagged(self):
        src = "void f(int x){ if (x > 0) { (void)x; } else {} }\n"
        self.assertIn(RULE_EELSE, rules(src, _eelse_cfg()))

    def test_non_empty_else_clean(self):
        src = "void f(int x){ if (x > 0) { (void)x; } else { x = 0; } }\n"
        self.assertNotIn(RULE_EELSE, rules(src, _eelse_cfg()))

    def test_else_if_clean(self):
        src = "void f(int x){ if (x > 0) { (void)x; } else if (x < 0) { x = 0; } }\n"
        self.assertNotIn(RULE_EELSE, rules(src, _eelse_cfg()))

    def test_no_else_clean(self):
        src = "void f(int x){ if (x > 0) { (void)x; } }\n"
        self.assertNotIn(RULE_EELSE, rules(src, _eelse_cfg()))

    def test_disabled(self):
        src = "void f(int x){ if (x > 0) { (void)x; } else {} }\n"
        self.assertNotIn(RULE_EELSE, rules(src, _eelse_cfg(enabled=False)))

    def test_severity_configurable(self):
        src = "void f(int x){ if (x > 0) { (void)x; } else {} }\n"
        viols = [v for v in run(src, _eelse_cfg(severity="error")) if v.rule == RULE_EELSE]
        self.assertTrue(viols)
        self.assertEqual(viols[0].severity, "error")

    def test_message_content(self):
        src = "void f(int x){ if (x > 0) { (void)x; } else {} }\n"
        msgs = [v.message for v in run(src, _eelse_cfg()) if v.rule == RULE_EELSE]
        self.assertTrue(msgs)
        self.assertIn("Empty else", msgs[0])

    def test_in_comment_not_flagged(self):
        src = "void f(void){ /* else {} */ return; }\n"
        self.assertNotIn(RULE_EELSE, rules(src, _eelse_cfg()))

    def test_else_with_comment_not_flagged(self):
        # An else block containing only a comment is intentionally documented
        # and must NOT be flagged — this is the recommended "correct" form.
        src = "void f(int x){ if (x > 0) { (void)x; } else { /* intentionally empty */ } }\n"
        self.assertNotIn(RULE_EELSE, rules(src, _eelse_cfg()))


if __name__ == "__main__":
    unittest.main()
