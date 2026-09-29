"""test_enums.py — tests for enum.type_case, enum.type_suffix,
enum.member_case, enum.member_prefix rules.

Every enumerator is checked, including the last one with or without a
trailing comma (issue #423).
"""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
import unittest
from harness import cfg_only, has, clean, run

ENUM_CFG = cfg_only(
    enums={"enabled": True, "severity": "error",
           "type_case": "lower_snake",
           "type_suffix": {"enabled": True, "suffix": "_t"},
           "member_case": "upper_snake",
           "member_prefix_from_type": {"enabled": True, "severity": "warning"}},
)

class TestEnumTypeCase(unittest.TestCase):
    def test_lower_snake_type_passes(self):
        src = "typedef enum { UART_STATE_IDLE, UART_STATE_BUSY } uart_state_t;\n"
        self.assertFalse(has(src, ENUM_CFG, "enum.type_case"))

    def test_upper_snake_type_fails(self):
        src = "typedef enum { UART_STATE_IDLE, UART_STATE_BUSY } UART_STATE_T;\n"
        self.assertTrue(has(src, ENUM_CFG, "enum.type_case"))

    def test_camel_type_fails(self):
        src = "typedef enum { UART_STATE_IDLE, UART_STATE_BUSY } UartState_t;\n"
        self.assertTrue(has(src, ENUM_CFG, "enum.type_case"))

class TestEnumTypeSuffix(unittest.TestCase):
    def test_correct_suffix_passes(self):
        src = "typedef enum { UART_STATE_IDLE, UART_STATE_BUSY } uart_state_t;\n"
        self.assertFalse(has(src, ENUM_CFG, "enum.type_suffix"))

    def test_missing_suffix_fails(self):
        src = "typedef enum { UART_STATE_IDLE, UART_STATE_BUSY } uart_state;\n"
        self.assertTrue(has(src, ENUM_CFG, "enum.type_suffix"))

class TestEnumMemberCase(unittest.TestCase):
    def test_upper_snake_members_pass(self):
        src = "typedef enum { UART_STATE_IDLE, UART_STATE_BUSY } uart_state_t;\n"
        self.assertFalse(has(src, ENUM_CFG, "enum.member_case"))

    def test_lower_snake_member_fails(self):
        src = "typedef enum { uart_state_idle, uart_state_busy } uart_state_t;\n"
        self.assertTrue(has(src, ENUM_CFG, "enum.member_case"))

class TestEnumMemberPrefix(unittest.TestCase):
    def test_correct_prefix_passes(self):
        src = "typedef enum { UART_STATE_IDLE, UART_STATE_BUSY } uart_state_t;\n"
        self.assertFalse(has(src, ENUM_CFG, "enum.member_prefix"))

    def test_wrong_prefix_fails(self):
        """Members that don't start with the derived prefix are flagged."""
        src = "typedef enum { STATE_IDLE, STATE_BUSY } uart_state_t;\n"
        self.assertTrue(has(src, ENUM_CFG, "enum.member_prefix"))

    def test_prefix_derived_from_type_name(self):
        """Different type name → different required prefix."""
        src = "typedef enum { MOTOR_CTRL_STOP, MOTOR_CTRL_RUN } motor_ctrl_t;\n"
        self.assertFalse(has(src, ENUM_CFG, "enum.member_prefix"))

def _named(src, rule):
    """Return the member names quoted in *rule* messages for *src*."""
    return [v.message.split("'")[1] for v in run(src, ENUM_CFG)
            if v.rule == rule]


class TestEnumLastMember(unittest.TestCase):
    """Issue #423: the last enumerator is checked in every layout."""

    def _assert_last_flagged(self, src, name="badLast"):
        self.assertIn(name, _named(src, "enum.member_case"))
        self.assertIn(name, _named(src, "enum.member_prefix"))

    def test_last_member_without_trailing_comma(self):
        self._assert_last_flagged(
            "typedef enum { COLOUR_GOOD, badLast } colour_t;\n")

    def test_last_member_with_trailing_comma(self):
        self._assert_last_flagged(
            "typedef enum { COLOUR_GOOD, badLast, } colour_t;\n")

    def test_last_member_with_initialiser(self):
        self._assert_last_flagged(
            "typedef enum { COLOUR_GOOD, badLast = 5 } colour_t;\n")

    def test_last_member_with_trailing_comment(self):
        src = ("typedef enum {\n"
               "    COLOUR_GOOD,  /* first */\n"
               "    badLast       /* last member */\n"
               "} colour_t;\n")
        self._assert_last_flagged(src)

    def test_last_member_with_line_comment(self):
        src = ("typedef enum {\n"
               "    COLOUR_GOOD,\n"
               "    badLast // last member\n"
               "} colour_t;\n")
        self._assert_last_flagged(src)

    def test_single_line_two_member_enum(self):
        src = "typedef enum { COLOUR_A, b } colour_t;\n"
        self._assert_last_flagged(src, "b")

    def test_single_member_enum(self):
        self._assert_last_flagged("typedef enum { badLast } colour_t;\n")

    def test_prefix_reported_for_last_member_only(self):
        """A correctly-cased last member with the wrong prefix is reported."""
        src = "typedef enum { COLOUR_GOOD, BAD_LAST } colour_t;\n"
        self.assertEqual(_named(src, "enum.member_prefix"), ["BAD_LAST"])
        self.assertEqual(_named(src, "enum.member_case"), [])

    def test_prefix_reported_for_last_member_trailing_comma(self):
        src = "typedef enum { COLOUR_GOOD, BAD_LAST, } colour_t;\n"
        self.assertEqual(_named(src, "enum.member_prefix"), ["BAD_LAST"])

    def test_valid_last_member_not_flagged(self):
        src = ("typedef enum {\n"
               "    COLOUR_RED = 1,\n"
               "    COLOUR_BLUE = 5  /* last */\n"
               "} colour_t;\n")
        self.assertEqual(_named(src, "enum.member_case"), [])
        self.assertEqual(_named(src, "enum.member_prefix"), [])

    def test_initialiser_identifier_not_treated_as_member(self):
        """Names on the right of '=' are values, not enumerators."""
        src = ("typedef enum { COLOUR_RED = OTHER_BASE, "
               "COLOUR_BLUE = (SHIFT_A | SHIFT_B) } colour_t;\n")
        self.assertEqual(_named(src, "enum.member_prefix"), [])

    def test_preprocessor_lines_in_body_ignored(self):
        src = ("typedef enum {\n"
               "    COLOUR_RED,\n"
               "#if defined(HAS_BLUE)\n"
               "    COLOUR_BLUE,\n"
               "#endif\n"
               "    badLast\n"
               "} colour_t;\n")
        self.assertEqual(_named(src, "enum.member_case"), ["badLast"])
        self.assertEqual(_named(src, "enum.member_prefix"), ["badLast"])

    def test_last_member_reported_on_its_own_line(self):
        src = ("typedef enum {\n"
               "    COLOUR_GOOD,\n"
               "    badLast\n"
               "} colour_t;\n")
        lines = [v.line for v in run(src, ENUM_CFG)
                 if v.rule == "enum.member_case"]
        self.assertEqual(lines, [3])


class TestEnumDisabled(unittest.TestCase):
    def test_disabled_produces_no_violations(self):
        cfg = cfg_only(enums={"enabled": False})
        src = "typedef enum { bad, WRONG } BadType;\n"
        self.assertTrue(clean(src, cfg))

if __name__ == "__main__":
    unittest.main(verbosity=2)
