# Software Requirements Specification

*Automotive SPICE® PAM v4.0 | SWE.1 Software Requirements Analysis*

---

## 1. Document Identification & Control

| Field | Value | Field | Value |
|---|---|---|---|
| **Document ID** | CSC-SWE1-001 | **Version** | 2.13 |
| **Project** | CStyleCheck | **Date** | 2026-09-29 |
| **Status** | Released | **Classification** | Internal |
| **Author** | Claude | **Reviewer** | Dermot Murphy |
| **Approver** | Dermot Murphy | **Related Process** | SWE.1 |

> **Note — Reviewer independence (CSC-DEV-002):** The Reviewer and Approver are the same person (Dermot Murphy). This is accepted under deviation record **CSC-DEV-002** (`docs/aspice/CStyleCheck_DEV002_Independent_Review_Deviation.md`) on the basis that CStyleCheck has a single human team member.

---

## 2. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 2.13 | 2026-09-29 | Claude | Issue #412: SWE1-115 — `misc.boolean_comparison` disabled by default (also when the key is absent) and restricted to lowercase `true`/`false`; `TRUE`/`FALSE` macros not flagged; RTM row marked opt-in; referenced-document versions resynced (4) |
| 2.12 | 2026-09-29 | Claude | Release-prep cross-reference resync: 4 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 2.11 | 2026-09-29 | Claude | Issue #413 (CR-413, CSC-SUP10-001 §7.1): SWE1-094 rewritten to match `main()` — exactly two lines (`CStyleCheck <version>`, `(C) 2026 Dermot Murphy`) on stderr (and the `--log` file) before discovery, written even when output is piped, no suppression option (`--quiet` clause removed), never on stdout; parent SYS-F-046 unchanged; RTM row now full verification. SWE1-015: record the known `--fix` exception (pointer-prefix header rename re-reads the `.h` file). No source change. Referenced-document versions resynced (SYS2 2.4→2.5, SWE2 1.14→1.15) |
| 2.10 | 2026-09-29 | Claude | Issue #410: SWE1-115 is a style rule; the MISRA C:2012 Rule 14.4 citation is removed from SWE1-115, its RTM row and Appendix A.1 (`if (flag == true)` is compliant with Rule 14.4). The `misc.yoda_condition` "Rule 14.4 (informative)" citation is also removed (operand order has no bearing on Rule 14.4). Appendix A.2, A.3 and the conclusion show Rule 14.4 as delegated to cppcheck (MISRA addon), not covered by CStyleCheck |
| 2.9 | 2026-09-29 | Claude | Issue #407: RTM test column cites `test_cli_requirements.py` for SWE1-015 (UV-CLI-014 to 016), SWE1-094 (UV-CLI-017 to 019; `--quiet` clause not implemented) and SWE1-096 (UV-CLI-020 to 022); SWE1-096 design column names `discover_files()` `emit()` (`os.path.normpath`) as the point where `os.sep` is applied; referenced-document versions resynced (SUP8 1.13→1.14, SWE2 1.13→1.14, SYS2 2.3→2.4, SYS3 1.7→1.8) |
| 2.8 | 2026-09-29 | Claude | CSC-AUD-009 corrective actions (#405). AUD9-F-001: add SWE1-109 to SWE1-116 for the 8 rules from #391/#392, with RTM rows, Appendix A.1 rows and A.2/A.3 updates. AUD9-F-007: SWE1-065 baseline file is a JSON object with a `violations` array. AUD9-F-008: SWE1-094 parent → SYS-F-046; add SYS-F-041 to SYS-F-046 and the other uncited SYS IDs as parents; add upward-trace note. AUD9-F-010: add SWE1-117 (trend safety indicators) and extend the SWE1-108 chart list. AUD9-F-011: SWE1-102 to SWE1-108 parent → CSC-MAN3-001 §10.3; add SWE1-100/101 RTM rows. AUD9-F-015: header date. AUD9-F-025: renumber §4.15 to §4.18 so sections are in order. AUD9-F-024: Author and Description columns swapped back in earlier revision rows. AUD9-F-014: referenced-document versions resynced to current revisions |
| 2.7 | 2026-09-29 | Claude | Add §4.18 SWE1-102 to SWE1-108 (trend-analysis C source code metrics: LOC, cyclomatic complexity, size, documentation, coupling, violation quality, backward-compatible charts/wiki); update RTM; also records SWE1-065 to SWE1-067 revision and SWE1-100/SWE1-101 (baseline matching, issues #394/#395, PR #397) — issue #388 |
| 2.6 | 2026-07-06 | Claude | ASPICE audit — add SWE1-094 to SWE1-099 for v1.6.0 features (startup banner, copyright in --version, block-comment suppression, OS path sep, --summary restructure, fn_start correction, fn-ptr typedef exemption); update SWE1-072 for /* */ form; update SWE1-074 for pointer_prefix fix; update §3.2 cross-refs (SWE2 1.11→1.12, SUP8 1.9→1.10); update RTM — closes #371 |
| 2.5 | 2026-07-01 | Claude | Add SWE1-091 (misc.constant_comparison), SWE1-092 (unsigned_suffix signed-param exemption), SWE1-093 (variable.pointer_prefix auto-fix); update §3.1 scope to v1.6.0; update RTM — closes #339 #340 #341 |
| 2.4 | 2026-06-27 | Dermot Murphy | Fix §3.2 cross-refs: cascade update (SWE2 1.9→1.11 + any other stale refs fixed) |
| 2.3 | 2026-06-27 | Dermot Murphy | Fix §3.2 cross-ref: SYS2 1.9→2.0 |
| 2.2 | 2026-06-27 | Claude | ASPICE audit — fix §3.2 SWE2 ref 1.8→1.9 and SYS2 ref 1.6→1.9; update Review & Approval dates — closes #315 #323 |
| 2.1 | 2026-06-26 | Claude | ASPICE audit — fix §3.1 scope text (v1.2.x → v1.5.0) — closes #305 |
| 2.0 | 2026-06-26 | Claude | Add SWE1-089 (per-file summary #278), SWE1-MISRA-004 (non_ascii_source #279), SWE1-090 (typedef-alias constant.case exemption #272/#244); update RTM |
| 1.9 | 2026-06-18 | Claude | ASPICE audit #254 — sync referenced-document version citations to current versions |
| 1.8 | 2026-06-08 | Claude | Add SWE1-078 to SWE1-088 for 11 new rules (issues #221–#232); update RTM |
| 1.7 | 2026-06-05 | Claude | CSC-AUD-005 corrective action — fix factual errors identified in audit |
| 1.6 | 2026-06-04 | Claude | Add SWE1-072 to SWE1-076 for five new features (inline suppression, --fix, --init/--preset, per-dir config, HTML output) — issues #188 #189 #190 #193 #192 |
| 1.5 | 2026-06-04 | Claude | Deep accuracy audit: fix §3.1 version text, update §3.2 referenced doc versions (SWE2 1.2→1.3, SUP8 1.4→1.5) — resolves issue #163 |
| 1.4 | 2026-06-04 | Claude | Automated accuracy audit: update referenced doc versions in §3.2 — resolves issue #163 |
| 1.3 | 2026-05-28 | Claude | Add SWE1-071 (whitespace_ratio); fix §4.15 coverage targets to reflect package refactor; update RTM and Appendix A.1; fix §4.15 coverage wording — closes issues #146 #148 |
| 1.2 | 2026-05-28 | Dermot Murphy | Add CSC-DEV-002 deviation footnote to §1 — closes issue #61 |
| 1.1 | 2026-05-28 | Claude | Added SWE1-MISRA-001/002/003 requirements for MISRA C:2012/2023 lexical rules (Rule 7.3, 7.1, 4.2); updated §5 traceability matrix |
| 1.0 | 2026-04-12 | Claude | Initial release |

---

## 3. Purpose & Scope

### 3.1 Purpose

This Software Requirements Specification (SRS) refines the system-level requirements from CSC-SYS2-001 into software-specific, implementable requirements for **CStyleCheck v1.6.0 and the post-v1.6.0 `develop` baseline (81 rule IDs)**. It provides the direct input to software architectural design (SWE.2) and defines the verification criteria used in SWE.4–SWE.6.

This document satisfies **Automotive SPICE® PAM v4.0, SWE.1 — Software Requirements Analysis**.

### 3.2 Referenced Documents

| Document ID | Title | Version |
|---|---|---|
| CSC-SYS2-001 | CStyleCheck System Requirements Specification | 2.7 |
| CSC-SYS3-001 | CStyleCheck System Architecture Description | 1.10 |
| CSC-SWE2-001 | CStyleCheck Software Architecture Description | 1.18 |
| CSC-SUP8-001 | CStyleCheck Configuration Management Plan | 1.16 |
| Barr-C:2018 | Barr Group Embedded C Coding Standard | 2018 |
| ASPICE PAM v4.0 | Automotive SPICE Process Assessment Model | 4.0 |

### 3.3 Glossary

| Term | Definition |
|---|---|
| `Checker` | The primary analysis class in `cstylecheck.py` responsible for per-file rule evaluation |
| `CheckResult` | Data class aggregating `Violation` objects produced by one `Checker` run |
| `Violation` | Data class holding: `filepath`, `line`, `col`, `severity`, `rule`, `message` |
| `SignChecker` | Cross-file sign-compatibility analysis class |
| `module_name` | The filename stem (e.g. `uart` from `uart.c`) used as the mandatory identifier prefix |
| `clean` | Source text after stripping comments and string literals |
| `defines` | Keyword/type alias substitutions applied to source before analysis |
| `exclusions` | Per-file YAML map of rule IDs to suppressed identifier patterns |
| `baseline` | JSON file of known violations used to suppress pre-existing findings |

---

## 4. Software Requirements

### 4.1 Configuration Loading (SS-02)

| SW-REQ-ID | Requirement | Priority | Verification | Parent |
|---|---|---|---|---|
| SWE1-001 | The software shall parse the YAML configuration file into a nested dictionary accessible via the `load_config()` function | Mandatory | Test | SYS-F-002, SYS-F-026, SYS-NF-007 |
| SWE1-002 | The software shall raise a configuration error (exit code 2) if the YAML file is absent, malformed, or unparseable | Mandatory | Test | SYS-F-039 |
| SWE1-003 | The software shall apply project `--defines` substitutions to the preprocessed source text before any rule check, using the `apply_defines()` function | Mandatory | Test | SYS-F-006 |
| SWE1-004 | The software shall load the module alias map via `load_alias_file()` and use it to derive accepted prefix strings per source file | Mandatory | Test | SYS-F-007 |
| SWE1-005 | The software shall load per-file rule exclusions via `load_exclusions_file()` and pass the resulting map to each `Checker` instance | Mandatory | Test | SYS-F-008, SYS-NF-009 |
| SWE1-006 | The software shall resolve the set of disabled rules for each source file via `_disabled_rules_for_file()` before instantiating the `Checker` | Mandatory | Test | SYS-F-008, SYS-F-025 |

### 4.2 Dictionary Management (SS-03)

| SW-REQ-ID | Requirement | Priority | Verification | Parent |
|---|---|---|---|---|
| SWE1-007 | The software shall load the C keyword dictionary from `c_keywords.txt` (or `--keywords-file` override) as a `frozenset` via `_load_dict_file()` | Mandatory | Test | SYS-F-009 |
| SWE1-008 | The software shall load the C stdlib name dictionary from `c_stdlib_names.txt` (or `--stdlib-file` override) as a `frozenset` | Mandatory | Test | SYS-F-009 |
| SWE1-009 | The software shall load the spell-check dictionary from `c_spell_dict.txt` (or `--spell-dict` override) and merge it with YAML-configured exemptions via `_build_spell_dict()` | Mandatory | Test | SYS-F-009 |
| SWE1-010 | The software shall locate built-in dictionary files relative to `__file__` with a fallback to `{sys.prefix}/share/cstylecheck/` via `_data_file()` | Mandatory | Test | SYS-F-009 |

### 4.3 Source Parsing and Cache (SS-04)

| SW-REQ-ID | Requirement | Priority | Verification | Parent |
|---|---|---|---|---|
| SWE1-011 | The software shall strip C block and line comments from source text using `strip_comments()` before identifier extraction | Mandatory | Test | SYS-F-010 |
| SWE1-012 | The software shall strip string literal contents from source text using `strip_strings()` before identifier extraction | Mandatory | Test | SYS-F-010 |
| SWE1-013 | The software shall build a line-offset map via `build_line_map()` enabling `offset_to_line_col()` to convert byte positions to (line, col) pairs | Mandatory | Test | SYS-F-027 |
| SWE1-014 | The software shall build a per-line brace-depth array via `_build_brace_depths()` to determine identifier scope (global / file-static / local) | Mandatory | Test | SYS-NF-001 |
| SWE1-015 | Each source file shall be read from disk exactly once per invocation; the content shall be cached in memory for use by both the `Checker` and `SignChecker` instances. Known exception: in `--fix` mode without `--dry-run`, the `variable.pointer_prefix` header rename (SWE1-093) re-reads the companion `.h` file from disk before patching it, because that file may already have been rewritten earlier in the same fix pass | Mandatory | Test | SYS-NF-001, SYS-NF-002 |
| SWE1-016 | The software shall identify comment-only lines via `_comment_only_lines()` and exempt them from indentation and line-length checks | Mandatory | Test | SYS-F-020 |

### 4.4 Rule Engine — Variables (SS-05)

| SW-REQ-ID | Requirement | Priority | Verification | Parent |
|---|---|---|---|---|
| SWE1-017 | The `_check_variables()` method shall detect variable declarations at global, file-static, local, and parameter scope using regex against the preprocessed source | Mandatory | Test | SYS-F-013 |
| SWE1-018 | The software shall enforce `lower_snake` case on variable names at all scopes, with independently configurable severity per scope | Mandatory | Test | SYS-F-013, SYS-F-018 |
| SWE1-019 | The software shall require the module prefix on global and file-static variable names when `require_module_prefix: true` | Mandatory | Test | SYS-F-012 |
| SWE1-020 | The software shall enforce the `g_` prefix on global variable local parts when `g_prefix.enabled: true` | Mandatory | Test | SYS-F-013 |
| SWE1-021 | The software shall enforce the `s_` prefix on file-static variable local parts when `s_prefix.enabled: true` | Mandatory | Test | SYS-F-013 |
| SWE1-022 | The software shall enforce the `p_` prefix on single-pointer variables when `pointer_prefix.enabled: true` | Mandatory | Test | SYS-F-014 |
| SWE1-023 | The software shall enforce the `pp_` prefix on double-pointer variables when `pp_prefix.enabled: true` | Mandatory | Test | SYS-F-014 |
| SWE1-024 | The software shall enforce the `b_` prefix on `bool`/`_Bool` variables when `bool_prefix.enabled: true` | Mandatory | Test | SYS-F-014 |
| SWE1-025 | The software shall enforce the handle prefix on configured handle types when `handle_prefix.enabled: true` | Mandatory | Test | SYS-F-014 |
| SWE1-026 | The software shall enforce the prefix ordering rule `[g_][p_\|pp_][b_\|h_]` on variable local parts | Mandatory | Test | SYS-F-014 |
| SWE1-027 | The software shall enforce `min_length` and `max_length` constraints on variable names, with `allow_single_char_loop_vars` and `allow_loop_vars_short` exemptions | Mandatory | Test | SYS-F-017 |
| SWE1-028 | The software shall enforce the `variable.no_numeric_in_name` rule when configured | Mandatory | Test | SYS-F-011 |
| SWE1-029 | The software shall permit uppercase abbreviations listed in `allowed_abbreviations` within otherwise `lower_snake` variable names | Mandatory | Test | SYS-F-024 |

### 4.5 Rule Engine — Functions (SS-05)

| SW-REQ-ID | Requirement | Priority | Verification | Parent |
|---|---|---|---|---|
| SWE1-030 | The `_check_functions()` method shall detect C function definitions by regex and extract function names | Mandatory | Test | SYS-F-015 |
| SWE1-031 | The software shall enforce module prefix on all public (non-static) function names | Mandatory | Test | SYS-F-012 |
| SWE1-032 | The software shall enforce the configured function naming style: `object_verb`, `verb_object`, or `lower_snake` | Mandatory | Test | SYS-F-015 |
| SWE1-033 | The software shall enforce the static function prefix (e.g. `prv_`) on file-scope static function names when `functions.static_prefix.enabled: true` | Mandatory | Test | SYS-F-016 |
| SWE1-034 | The software shall enforce `min_length` and `max_length` constraints on function names | Mandatory | Test | SYS-F-017 |

### 4.6 Rule Engine — Constants and Macros (SS-05)

| SW-REQ-ID | Requirement | Priority | Verification | Parent |
|---|---|---|---|---|
| SWE1-035 | The `_check_defines()` method shall detect `#define` directives and extract macro and constant names | Mandatory | Test | SYS-F-011 |
| SWE1-036 | The software shall enforce `UPPER_SNAKE_CASE` on macro and constant names | Mandatory | Test | SYS-F-018 |
| SWE1-037 | The software shall enforce the module prefix on macro and constant names | Mandatory | Test | SYS-F-012 |
| SWE1-038 | The software shall enforce `min_length` and `max_length` constraints on macro and constant names | Mandatory | Test | SYS-F-017 |
| SWE1-039 | The software shall exempt patterns matching `exempt_patterns` (e.g. compiler-built-in `__` prefixes) from all macro rules | Mandatory | Test | SYS-F-024 |

### 4.7 Rule Engine — Types (SS-05)

| SW-REQ-ID | Requirement | Priority | Verification | Parent |
|---|---|---|---|---|
| SWE1-040 | The `_check_typedefs()` method shall enforce `UPPER_SNAKE_CASE` with a `_T` suffix on `typedef` names; multi-token base types (e.g. `typedef unsigned int UINT_T`) shall be correctly detected | Mandatory | Test | SYS-F-011 |
| SWE1-041 | The `_check_enums()` method shall enforce `lower_snake_t` on enum type names and `UPPER_SNAKE` with enum-name-derived prefix on enum member names | Mandatory | Test | SYS-F-011 |
| SWE1-042 | The `_check_structs()` method shall enforce `lower_snake_s` on struct tag names and `lower_snake` on struct member names | Mandatory | Test | SYS-F-011 |

### 4.8 Rule Engine — Include Guards (SS-05)

| SW-REQ-ID | Requirement | Priority | Verification | Parent |
|---|---|---|---|---|
| SWE1-043 | The `_check_include_guard()` method shall verify that header files contain a correctly formatted include guard (`{FILENAME_UPPER}_{EXT_UPPER}_`) or `#pragma once` | Mandatory | Test | SYS-F-019 |
| SWE1-044 | Missing include guards in `.h` files shall produce an `include_guard.missing` violation | Mandatory | Test | SYS-F-019 |

### 4.9 Rule Engine — Miscellaneous Rules (SS-05)

| SW-REQ-ID | Requirement | Priority | Verification | Parent |
|---|---|---|---|---|
| SWE1-045 | The `_check_misc()` method shall enforce maximum line length on non-comment lines when `misc.line_length.enabled: true` | Mandatory | Test | SYS-F-020 |
| SWE1-046 | The software shall enforce indentation style (tab vs. spaces, configurable width) on non-comment lines | Mandatory | Test | SYS-F-020 |
| SWE1-047 | The software shall detect magic number literals when `misc.magic_numbers.enabled: true`; `#define` RHS, array indices, and `return` values shall be exempt | Mandatory | Test | SYS-F-020 |
| SWE1-048 | The software shall require the `U`/`UL` unsigned suffix on numeric integer constants when `misc.unsigned_suffix.enabled: true` | Mandatory | Test | SYS-F-020 |
| SWE1-049 | The `_check_yoda()` method shall enforce Yoda-condition ordering in `==` and `!=` comparisons | Mandatory | Test | SYS-F-020 |
| SWE1-050 | The software shall enforce block comment spacing rules when `misc.block_comment_spacing.enabled: true` | Mandatory | Test | SYS-F-020 |
| SWE1-MISRA-001 | The `_check_lowercase_l_suffix()` method shall flag any integer or floating-point literal that uses the lowercase letter `l` as a suffix (MISRA C:2012/2023 Rule 7.3) when `misc.lowercase_l_suffix.enabled: true` | Mandatory | Test | SYS-F-020 |
| SWE1-MISRA-002 | The `_check_octal_constants()` method shall flag any integer literal that begins with `0` followed by one or more octal digits (MISRA C:2012/2023 Rule 7.1) when `misc.octal_constant.enabled: true` | Mandatory | Test | SYS-F-020 |
| SWE1-MISRA-003 | The `_check_trigraphs()` method shall flag any occurrence of the nine ISO C trigraph sequences (`??=`, `??(`, `??/`, `??)`, `??'`, `??<`, `??!`, `??>`, `??-`) in source or comment text (MISRA C:2012 Rule 4.2 Advisory; MISRA C:2023 Rule 4.2 Required) when `misc.trigraph.enabled: true` | Mandatory | Test | SYS-F-020 |
| SWE1-MISRA-004 | The `_check_non_ascii_source()` method shall flag any character whose Unicode code point falls outside the set {0x09 TAB, 0x0A LF, 0x0D CR, 0x20–0x7E printable ASCII} (MISRA C:2012/2023 Rule 4.1) when `misc.non_ascii_source.enabled: true`; when `exempt_string_literals: true` characters inside double-quoted string literals shall be exempt | Mandatory | Test | SYS-F-020 |
| SWE1-071 | The `_check_whitespace_ratio()` method shall enforce a minimum ratio of blank lines to code lines when `misc.whitespace_ratio.enabled: true`; the file header region and comment-only lines shall be excluded from both counts | Mandatory | Test | SYS-F-020 |
| SWE1-109 | The `_check_goto_usage()` method shall flag every `goto` keyword in comment- and string-stripped source as `misc.goto_usage` (default severity `error`) when `misc.goto_usage.enabled: true` (MISRA C:2012 Rule 15.1, Advisory) | Mandatory | Test | SYS-F-020 |
| SWE1-110 | The `_check_assignment_in_condition()` method shall flag a simple assignment operator `=` (not `==`, `!=`, `<=`, `>=` or a compound assignment) inside the controlling expression of an `if` or `while`, or inside the condition clause of a `for` statement (between its first and second top-level `;`), as `misc.assignment_in_condition` (default severity `warning`) (MISRA C:2012 Rule 13.4) | Mandatory | Test | SYS-F-020 |
| SWE1-111 | The `_check_multiple_statements_per_line()` method shall flag a `;` followed on the same line by the start of another statement as `misc.multiple_statements_per_line` (default severity `warning`); lines containing a `for (` header shall be exempt (Barr-C:2018 §3.2) | Mandatory | Test | SYS-F-020 |
| SWE1-112 | The `_check_void_pointer()` method shall flag every `void *` type in comment- and string-stripped source as `misc.void_pointer` (default severity `warning`) (MISRA C:2012 Rule 11.5, Advisory) | Mandatory | Test | SYS-F-020 |
| SWE1-113 | The `_check_recursive_function()` method shall flag a function definition whose body contains a call to the function's own name (direct recursion) as `misc.recursive_function` (default severity `error`); indirect recursion is not detected (MISRA C:2012 Rule 17.2, Required — partial) | Mandatory | Test | SYS-F-020 |
| SWE1-114 | The `_check_sizeof_type()` method shall flag `sizeof` applied to a type name (primitive type, `*_t` typedef or capitalised type name, optionally followed by `*`) as `misc.sizeof_type` (default severity `info`); `sizeof(var)` and `sizeof(*var)` shall not be flagged (Barr-C:2018 §5.7) | Mandatory | Test | SYS-F-020 |
| SWE1-115 | The `_check_boolean_comparison()` method shall flag an `==` or `!=` comparison with the lowercase `<stdbool.h>` literals `true` or `false` on either side as `misc.boolean_comparison` (default severity `warning`); `TRUE`/`FALSE` macros shall not be flagged. The rule shall be disabled by default, including when the configuration key is absent (opt-in, #412) (style rule; MISRA C:2012 Rule 14.4 is not enforced — `if (flag == true)` is compliant with it) | Mandatory | Test | SYS-F-020 |
| SWE1-116 | The `_check_empty_else()` method shall flag an `else { }` block whose body is empty in the original source as `misc.empty_else` (default severity `warning`); a block containing a comment shall not be flagged (Barr-C:2018 §8.3; MISRA C:2012 Rule 15.7 intent) | Mandatory | Test | SYS-F-020 |

### 4.10 Rule Engine — Cross-File Sign Compatibility (SS-04/SS-05)

| SW-REQ-ID | Requirement | Priority | Verification | Parent |
|---|---|---|---|---|
| SWE1-051 | The `SignChecker` class shall detect unsigned literals passed to signed-typed parameters and signed literals passed to unsigned parameters across related `.c`/`.h` file pairs | Mandatory | Test | SYS-F-021 |
| SWE1-052 | The `SignChecker` shall resolve `typedef` chains to determine the underlying signedness of type names | Mandatory | Test | SYS-F-021 |
| SWE1-053 | The `SignChecker` shall honour the `plain_char_is_signed` configuration option without permanent mutation of module-level type sets (use `try/finally` to restore) | Mandatory | Test | SYS-F-021 |

### 4.11 Rule Engine — Reserved Names and Spell Check (SS-05)

| SW-REQ-ID | Requirement | Priority | Verification | Parent |
|---|---|---|---|---|
| SWE1-054 | The `_check_reserved_names()` method shall flag any identifier that matches a C/C++ keyword or C stdlib name | Mandatory | Test | SYS-F-023 |
| SWE1-055 | The software shall load additional banned names via `--banned-names` and include them in the reserved-name check | Mandatory | Test | SYS-F-023 |
| SWE1-056 | The `_check_spelling()` method shall split identifier tokens on underscore and case-boundary, then check each word against the spell-check dictionary | Mandatory | Test | SYS-F-022 |

### 4.12 Output Formatter (SS-06)

| SW-REQ-ID | Requirement | Priority | Verification | Parent |
|---|---|---|---|---|
| SWE1-057 | Plain-text output shall format each violation as: `{filepath}:{line}:{col}: {SEVERITY} [{rule}] {message}` | Mandatory | Test | SYS-F-027 |
| SWE1-058 | JSON output via `_violations_to_json()` shall produce a top-level object with `summary` (files_checked, errors, warnings, info, total) and `violations` array | Mandatory | Test | SYS-F-028 |
| SWE1-059 | Each JSON violation object shall contain: `file`, `line`, `col`, `severity`, `rule`, `message` | Mandatory | Test | SYS-F-028 |
| SWE1-060 | SARIF output via `_violations_to_sarif()` shall conform to SARIF 2.1.0 schema with `$schema`, `version`, `runs[].tool`, and `runs[].results` fields populated | Mandatory | Test | SYS-F-029 |
| SWE1-061 | GitHub Actions annotations shall be emitted via `Violation.github_annotation()` producing `::error file=…,line=…,col=…,title=…::` format | Mandatory | Test | SYS-F-030 |
| SWE1-062 | The `Tee` class shall mirror all output to the log file path specified by `--log` without modifying stdout content | Mandatory | Test | SYS-F-031 |
| SWE1-063 | The `print_summary()` function shall print a tabulated summary of violation counts per severity (errors, warnings, info, total), top-10 violated rules by count, and a per-file breakdown; see also SWE1-089 | Mandatory | Test | SYS-F-032 |
| SWE1-064 | Verbose progress to `stderr` shall overwrite the current terminal line with the directory being scanned when `--verbose` is specified | Mandatory | Test | SYS-F-033 |

### 4.13 Baseline Suppression (SS-01/SS-05/SS-06)

| SW-REQ-ID | Requirement | Priority | Verification | Parent |
|---|---|---|---|---|
| SWE1-065 | The `write_baseline()` function shall serialise all violations to a JSON object with a single `violations` array and write it to the specified file; each entry shall record `file` (with `/` separators), `line`, `rule` and `message` | Mandatory | Test | SYS-F-034, SYS-F-036 |
| SWE1-066 | The `load_baseline()` function shall return a multiset (`collections.Counter`) of `file:rule:message` baseline keys from the JSON file | Mandatory | Test | SYS-F-035 |
| SWE1-067 | The rule engine shall filter out any `Violation` whose `_baseline_key()` matches an unused entry in the loaded baseline multiset; each baseline entry shall suppress at most one violation | Mandatory | Test | SYS-F-035 |
| SWE1-100 | Baseline matching shall not depend on the violation line number; the `line` field shall be retained in the file for review only (issue #394) | Mandatory | Test | SYS-F-035 |
| SWE1-101 | Baseline file paths shall be normalised to `/` separators when written, loaded and matched, so baselines are portable between Windows and Linux (issue #395) | Mandatory | Test | SYS-F-034, SYS-F-035 |

### 4.14 CLI and Entry Point (SS-01)

| SW-REQ-ID | Requirement | Priority | Verification | Parent |
|---|---|---|---|---|
| SWE1-068 | The `_expand_options_file()` function shall insert options-file tokens before direct CLI tokens so that direct CLI arguments take precedence | Mandatory | Test | SYS-F-003, SYS-NF-008 |
| SWE1-069 | The `main()` function shall return exit code `0`, `1`, or `2` as defined in SYS-F-037 to SYS-F-039, and the `cstylecheck` entry point defined in `pyproject.toml` shall invoke `main()` | Mandatory | Test | SYS-F-037, SYS-F-038, SYS-F-039, SYS-F-040 |
| SWE1-070 | The `discover_files()` function shall expand `--include` globs, de-duplicate paths, and apply `--exclude` filters using `_path_matches_exclude()` | Mandatory | Test | SYS-F-001, SYS-F-004, SYS-F-005 |

### 4.15 New Features — Inline Suppression, Auto-fix, Config Wizard, Per-directory Config, HTML Output

| SW-REQ-ID | Requirement | Priority | Verification | Parent |
|---|---|---|---|---|
| SWE1-072 | The `preprocessor.parse_inline_suppressions()` function shall parse `// cstylecheck: disable=rule.id` and `// cstylecheck: enable=rule.id` directives in C source, and equivalently `/* cstylecheck: disable=rule.id */` block-comment form on the same line; directives shall be case-insensitive and shall support comma-separated lists of rule IDs | Mandatory | Test | SYS-F-008, SYS-F-041 |
| SWE1-073 | The `parse_inline_suppressions()` function shall support `disable-next-line=rule.id` to suppress the immediately following non-blank, non-comment line; a `disable=rule.id` on the same line as code shall suppress that line only; an unpaired `disable=` shall suppress from that point to end of file | Mandatory | Test | SYS-F-008, SYS-F-041 |
| SWE1-074 | The `fixer.py` module shall apply safe mechanical in-place fixes when `--fix` is specified; `--dry-run` shall display a unified diff without writing; `--safe-only` shall restrict fixes to zero-risk substitutions; currently fixable rules: `misc.unsigned_suffix` (`42u` → `42U`), `misc.lowercase_l_suffix` (`100l` → `100L`), and `variable.pointer_prefix` (rename via `_fix_pointer_prefix` — see SWE1-093) | Mandatory | Test | SYS-F-020, SYS-F-042 |
| SWE1-075 | The `wizard.py` module shall implement `--init` (interactive Q&A wizard writing `.cstylecheck.yml`) and `--preset barr-c\|minimal\|misra` (write pre-built config without wizard); `--init-output FILE` shall set the output path; `--overwrite` shall allow overwriting an existing file | Mandatory | Test | SYS-F-002, SYS-F-043 |
| SWE1-076 | The `config.py resolve_per_dir_config()` function shall walk upward from each source file's directory when `--per-dir-config` is active, deep-merging any `.cstylecheck.yml` found on top of the root config; the nearest config wins; `root: true` in any `.cstylecheck.yml` stops the upward search; results shall be cached per directory | Mandatory | Test | SYS-F-002, SYS-F-044 |
| SWE1-077 | The `output.py _violations_to_html()` function shall produce a self-contained HTML report when `--output-format html` is specified; the report shall include inline CSS, summary cards (errors/warnings/info/total/files), and per-file violation tables; when `--log FILE` is provided the HTML shall be written to that file, otherwise to stdout | Mandatory | Test | SYS-F-027, SYS-F-045 |
| SWE1-078 | The `_check_function_length()` method shall report `misc.function_length` when a function body (opening `{` to closing `}`, inclusive) exceeds `misc.function_length.max_lines`; when `count_comments: false` blank and comment-only lines shall be excluded from the count | Mandatory | Test | SYS-F-020 |
| SWE1-079 | The `_check_function_doc_header()` method shall report `misc.function_doc_header` for any non-static function definition not immediately preceded by a Doxygen block comment containing `@brief`; when `require_param: true` each parameter requires a `@param` tag; when `require_return: true` non-void functions require `@return` | Mandatory | Test | SYS-F-020 |
| SWE1-080 | The `_check_assert_density()` method shall report `misc.assert_density` for any function body with fewer than `min_asserts` `assert()` calls; functions with fewer body lines than `min_function_lines` shall be exempt; functions whose name matches any pattern in `exempt_functions` shall be exempt | Mandatory | Test | SYS-F-020 |
| SWE1-081 | The `_check_null_statement_comment()` method shall report `misc.null_statement_comment` for any control-flow keyword (`while`, `for`, `if`) immediately followed by `;` and for any standalone `;` on its own line that is not followed by a comment | Mandatory | Test | SYS-F-020 |
| SWE1-082 | The `_check_declaration_spacing()` method shall report `misc.declaration_spacing` when a block of variable declarations at the start of a function body is not followed by exactly one blank line before the first executable statement | Mandatory | Test | SYS-F-020 |
| SWE1-083 | The `_check_file_length()` method shall report `misc.file_length` at line 1 when the source file exceeds `misc.file_length.max_lines`; when `count_blank_lines: false` blank lines shall be excluded; when `count_comment_lines: false` comment-only lines shall be excluded | Mandatory | Test | SYS-F-020 |
| SWE1-084 | The `_check_reserved_header_name()` method shall report `misc.reserved_header_name` when the file under analysis is a header whose base name matches a standard C or POSIX library header, and when a `#include "..."` directive references a name matching a standard header | Mandatory | Test | SYS-F-020 |
| SWE1-085 | The `_check_macro_trailing_semicolon()` method shall report `macro.trailing_semicolon` for any `#define` whose expansion (after stripping string literals and comments) ends with a `;`; multi-line macros shall be fully assembled before the check | Mandatory | Test | SYS-F-020 |
| SWE1-086 | The `_check_macro_multistatement_wrapper()` method shall report `macro.multistatement_wrapper` for any function-like `#define` whose expansion contains more than one statement and is not wrapped in `do { ... } while (0)` | Mandatory | Test | SYS-F-020 |
| SWE1-087 | The `_check_identifier_length()` method shall report `naming.identifier_length` for any declared identifier whose name is shorter than `naming.identifier_length.min_length` or longer than `naming.identifier_length.max_length`; names matching any pattern in `exempt_patterns` shall be exempt | Mandatory | Test | SYS-F-020 |
| SWE1-088 | The `_check_no_single_char_identifiers()` method shall report `naming.no_single_char_identifiers` for any declared identifier with a single-character name that does not appear in `naming.no_single_char_identifiers.exempt` | Mandatory | Test | SYS-F-020 |
| SWE1-089 | The `print_summary()` function shall include a per-file breakdown section showing the count of files with errors only, files with warnings (no errors), files with info only, and files with no violations (clean); the section shall be omitted when `files_checked` is zero | Mandatory | Test | SYS-F-032 |
| SWE1-090 | The `_check_defines()` method shall exempt object-like `#define` names from `constant.case` when the name ends (case-insensitively) with the configured `typedefs.suffix.suffix` value and `typedefs.suffix.enabled: true`; function-like `#define` names shall not be exempted | Mandatory | Test | SYS-F-011 |
| SWE1-091 | The `_check_constant_comparison()` method shall report `misc.constant_comparison` for any `==` or `!=` operator where both the left-hand token and the right-hand token are recognised as compile-time constants (decimal/hex literals, char literals, `true`/`false`/`TRUE`/`FALSE`/`NULL`/`nullptr`, or ALL\_CAPS identifiers) when `misc.constant_comparison.enabled: true`; comparisons inside `#define` RHS and `return` statements shall be exempt | Mandatory | Test | SYS-F-020 |
| SWE1-092 | The `_check_misc()` method shall exempt integer literals from `misc.unsigned_suffix` when they appear as arguments at positions corresponding to signed-type parameters (`int8_t`, `int16_t`, `int32_t`, `int64_t`, `int`, `short`, `long`, `char`, and `signed` variants) of functions declared or defined within the same translation unit | Mandatory | Test | SYS-F-020 |
| SWE1-093 | The `_fix_pointer_prefix()` function in `fixer.py` shall rename a non-compliant pointer parameter or variable to its prefixed form by replacing all word-boundary occurrences of the old name within the enclosing function's signature and body; it shall also rename the parameter in any doxygen `@param`/`\param` comment block immediately preceding the function; the `fix_pointer_prefix_in_header()` function shall apply the same rename to function declarations in the corresponding `.h` file when invoked by the `--fix` CLI mode | Mandatory | Test | SYS-F-020 |

### 4.16 New Features — v1.6.0 Output, Suppression, and Rule Improvements

| SW-REQ-ID | Requirement | Priority | Verification | Parent |
|---|---|---|---|---|
| SWE1-094 | The `main()` entry point shall write a startup banner to `stderr` after the configuration is loaded and before file discovery and checking begin. The banner shall consist of exactly two lines: the tool name and version string (`_VERSION_STRING`, `CStyleCheck <version>`) followed by the copyright notice (`_COPYRIGHT`, `(C) 2026 Dermot Murphy`). It shall be written on every checking run, whether or not stdout or stderr is a terminal (including when output is piped or redirected) and for every `--output-format`; no option shall suppress it. The banner shall not be written to stdout; when `--log FILE` is given it shall also be written to the log file. The early-exit paths (`--version`, `--help`, `--init`, `--preset`, `--update-config`) do not write the banner | Mandatory | Test | SYS-F-046 |
| SWE1-095 | The `--version` flag output shall include both the version string and the copyright notice on separate lines; the copyright notice shall conform to the format `Copyright (C) YYYY Dermot Murphy` | Mandatory | Test | SYS-F-032 |
| SWE1-096 | The output formatter shall render file paths in violation messages using the OS-native path separator (`os.sep`) so that paths on Windows use backslash and paths on POSIX systems use forward-slash | Mandatory | Test | SYS-F-027 |
| SWE1-097 | The `print_summary()` function shall print a "Files" section (listing per-file violation counts) **before** the "Results" section (listing per-rule counts); the summary header shall include the tool name, version, and a UTC timestamp; the horizontal separator line shall be dynamically sized to match the longest output line | Mandatory | Test | SYS-F-032 |
| SWE1-098 | The `_check_functions()` method shall correct the reported line number for a function definition when the opening brace appears on a line later than the function name line (multi-line signature); the violation shall be reported at the line containing the function return type and name, not at the opening brace | Mandatory | Test | SYS-F-015 |
| SWE1-099 | The `_check_variables()` method shall exempt function-pointer `typedef` names from the `variable.pointer_prefix` rule; a typedef whose base type contains a function-pointer signature (e.g. `typedef void (*UART_CB_T)(void)`) shall not trigger the `variable.pointer_prefix` violation | Mandatory | Test | SYS-F-014 |

### 4.17 Trend-Analysis Metrics — C Source Code Metrics (issue #388)

These requirements apply to the CI trend-analysis scripts in `scripts/` (`collect_metrics.py`, `generate_charts.py`, `update_wiki_metrics.py`, `compare_metrics.py`) run by `.github/workflows/metrics.yml`, not to the `cstylecheck` package. There is no parent system requirement: the metrics support project monitoring as defined in CSC-MAN3-001 §10.3 (MAN.3, GP 2.1.4). They are not allocated to a `cstylecheck` package component; CSC-SWE2-001 §5 describes them as the out-of-package element COMP-13 (Trend-Analysis Scripts). All analysis is pure-Python and heuristic (no compiler). Thresholds are documented in `scripts/metrics_rules.yml`.

| SW-REQ-ID | Requirement | Priority | Verification | Parent |
|---|---|---|---|---|
| SWE1-102 | The `classify_lines()` function in `scripts/collect_metrics.py` shall classify every physical line of a C source file as exactly one of blank, non-doxygen comment, doxygen comment (`/** */`, `/*! */`, `///`, `//!`) or SLOC (any line containing non-comment code, including code with a trailing comment); comment markers inside string/char literals shall not start a comment; `collect_metrics.py` shall record `loc_physical`, `loc_blank`, `loc_comment`, `loc_doxygen`, `loc_sloc`, `loc_comment_density` ((comment + doxygen) / SLOC) and `loc_blank_ratio` | Mandatory | Test | — (no SYS parent; CSC-MAN3-001 §10.3 trend monitoring, GP 2.1.4) |
| SWE1-103 | The `extract_functions()` function shall locate C function definitions (not prototypes, struct/enum bodies, initialisers or macro bodies) and compute per function the McCabe cyclomatic complexity V(G) = 1 + number of `if`, `while`, `for`, `case`, `&&`, `\|\|` and `?` tokens in comment- and string-stripped code, and the maximum brace nesting depth inside the body; `collect_metrics.py` shall record `cc_max`, `cc_avg`, `cc_over_threshold` (V(G) > 10), `nesting_max` and the histogram fields `cc_bucket_1_5`, `cc_bucket_6_10`, `cc_bucket_11_15`, `cc_bucket_16_plus` | Mandatory | Test | — (no SYS parent; CSC-MAN3-001 §10.3 trend monitoring, GP 2.1.4) |
| SWE1-104 | `collect_metrics.py` shall record the size metrics `c_file_count`, `h_file_count`, `func_count`, `func_length_max`, `func_length_avg` (lines from the function-name line to the closing brace), `func_over_length` (> 60 lines), `func_param_max`, `func_over_params` (> 5 parameters; `void` or empty list = 0) and `file_length_max` | Mandatory | Test | — (no SYS parent; CSC-MAN3-001 §10.3 trend monitoring, GP 2.1.4) |
| SWE1-105 | `collect_metrics.py` shall record `dox_coverage` (ratio) and `dox_coverage_pct` (percentage) of function definitions immediately preceded by a doxygen comment (`/** … */`, `/*! … */`, or a `///` / `//!` line) | Mandatory | Test | — (no SYS parent; CSC-MAN3-001 §10.3 trend monitoring, GP 2.1.4) |
| SWE1-106 | The `count_file_scope_variables()` function shall count file-scope variable definitions per declarator, excluding `typedef`, `extern` declarations, function prototypes and pure type definitions; `collect_metrics.py` shall record `global_vars` (non-static), `static_vars`, `fanout_avg` (mean number of unique called identifiers per function, excluding C keywords, `sizeof` and self-calls) and `recursive_func_count` (functions that call themselves directly) | Mandatory | Test | — (no SYS parent; CSC-MAN3-001 §10.3 trend monitoring, GP 2.1.4) |
| SWE1-107 | The `_summarise_violations()` function shall derive from the CStyleCheck JSON report `violations_by_category` (count per rule-ID prefix before the first `.`), `files_zero_violations` and `top_rules` (five most frequent rules); violations per KLOC SLOC shall be recorded as `defect_density` and the severity distribution as `errors` / `warnings` / `info_count` | Mandatory | Test | — (no SYS parent; CSC-MAN3-001 §10.3 trend monitoring, GP 2.1.4) |
| SWE1-108 | The trend-analysis scripts shall append the new fields to each data point without renaming or removing existing fields; when no C files are present all C metrics shall be zero; `generate_charts.py` shall treat fields missing from older data points as absent (not plotted) and shall render the charts `loc_breakdown` (stacked area), `cc_distribution` (stacked area), `function_size`, `defect_density`, `violations_by_category` (stacked area), `documentation_coverage`, `coupling`, `safety_indicators` and `macro_metrics`; `update_wiki_metrics.py` shall add snapshot rows for the new scalar metrics plus a violations-by-category table and a top-5 rules table | Mandatory | Test | — (no SYS parent; CSC-MAN3-001 §10.3 trend monitoring, GP 2.1.4) |
| SWE1-117 | The `_c_source_metrics()` function shall record the safety indicators `assert_count`, `assert_density` (asserts per KLOC SLOC; 0.0 when SLOC = 0), `goto_count`, `void_ptr_count`, `cast_count` (C-style casts) and `macro_count` (`#define` directives excluding include guards), all counted on comment- and string-stripped text; `generate_charts.py` shall render them in the `safety_indicators` and `macro_metrics` charts and `update_wiki_metrics.py` shall add snapshot rows for them (PR #392) | Mandatory | Test | — (no SYS parent; CSC-MAN3-001 §10.3 trend monitoring, GP 2.1.4) |

### 4.18 Verification Criteria

The following criteria shall be met by all software requirements above. They are used as the basis for SWE.4 unit verification.

| Criterion | Target | Measurement |
|---|---|---|
| Statement coverage | ≥ 90% of `src/cstylecheck/` package (long-term target); CI gate ≥ 85% combined | pytest-cov report |
| Branch coverage | ≥ 85% of `src/cstylecheck/` package (CI gate) | pytest-cov report |
| MISRA-equivalent naming compliance | Zero `cstylecheck` self-violations | `rules.yml` CI result |
| All unit test cases | PASS | pytest result across Python 3.10 / 3.11 / 3.12 |

---

## 5. Requirements Traceability Matrix

| SW-REQ-ID | Software Requirement Summary | Parent SYS REQ | SWE.2 Design Element | SWE.4 Test Reference |
|---|---|---|---|---|
| SWE1-001 to SWE1-006 | Configuration loading | SYS-F-002, F-006, F-007, F-008, F-025, F-026, SYS-NF-007, SYS-NF-009 | Configuration Loader module | `test_cli.py`, `test_dictionaries.py` |
| SWE1-007 to SWE1-010 | Dictionary management | SYS-F-009 | Dictionary Manager module | `test_dictionaries.py` |
| SWE1-011 to SWE1-016 | Source parsing and cache | SYS-F-010, SYS-NF-001, SYS-NF-002 | Source Parser / Cache | `test_misc.py`, `test_preprocessor.py`; SWE1-015: `test_cli_requirements.py` (UV-CLI-014 to 016); `--fix` header re-read is a documented exception |
| SWE1-017 to SWE1-029 | Variable rules | SYS-F-013, F-014, F-017, F-018 | `Checker._check_variables()` | `test_variables.py` |
| SWE1-030 to SWE1-034 | Function rules | SYS-F-015, F-016, F-017 | `Checker._check_functions()` | `test_functions.py` |
| SWE1-035 to SWE1-039 | Constant and macro rules | SYS-F-011, F-012, F-017, F-018 | `Checker._check_defines()` | `test_defines.py` |
| SWE1-040 to SWE1-042 | Type rules | SYS-F-011 | `Checker._check_typedefs/enums/structs()` | `test_typedefs.py`, `test_enums.py`, `test_structs.py` |
| SWE1-043 to SWE1-044 | Include guard rules | SYS-F-019 | `Checker._check_include_guard()` | `test_include_guards.py` |
| SWE1-045 to SWE1-050 | Miscellaneous rules | SYS-F-020 | `Checker._check_misc()`, `_check_yoda()` | `test_misc.py`, `test_yoda_condition.py`, `test_block_comment_spacing.py` |
| SWE1-071 | Whitespace ratio | SYS-F-020 | `Checker._check_whitespace_ratio()` | `test_whitespace_ratio.py` |
| SWE1-MISRA-001 to SWE1-MISRA-003 | MISRA C:2012/2023 lexical rules (Rule 7.3, 7.1, 4.2) | SYS-F-020 | `Checker._check_lowercase_l_suffix()`, `_check_octal_constants()`, `_check_trigraphs()` | `test_misra_rules.py` |
| SWE1-MISRA-004 | MISRA C:2012/2023 Rule 4.1 non-ASCII source characters | SYS-F-020 | `Checker._check_non_ascii_source()` | `test_misra_rules.py` |
| SWE1-051 to SWE1-053 | Cross-file sign compatibility | SYS-F-021 | `SignChecker` class | `test_sign_compatibility.py` |
| SWE1-054 to SWE1-056 | Reserved names and spell check | SYS-F-022, F-023 | `Checker._check_reserved_names()`, `_check_spelling()` | `test_reserved_name.py`, `test_spell_check.py` |
| SWE1-057 to SWE1-064 | Output formatting | SYS-F-027 to F-033 | Output Formatter / `Tee` | `test_cli.py` |
| SWE1-065 to SWE1-067 | Baseline suppression | SYS-F-034 to F-036 | Baseline Manager | `test_cli.py`, `test_improvements.py` |
| SWE1-100 | Baseline matching independent of line number (multiset) | SYS-F-035 | `baseline.apply_baseline()`, `_baseline_key()` | `test_improvements.py` |
| SWE1-101 | Baseline path normalisation to `/` | SYS-F-034, SYS-F-035 | `baseline._normalise_path()` | `test_improvements.py` |
| SWE1-068 to SWE1-070 | CLI and entry point | SYS-F-001, F-003 to F-005, SYS-F-037 to F-040, SYS-NF-008 | CLI module / `main()` | `test_cli.py` |
| SWE1-072 to SWE1-073 | Inline suppression comments | SYS-F-008, SYS-F-041 | `preprocessor.parse_inline_suppressions()` | `test_inline_suppression.py` |
| SWE1-074 | Auto-fix mode | SYS-F-020, SYS-F-042 | `fixer.py` Fixer module | `test_fix_mode.py` |
| SWE1-075 | Config wizard and presets | SYS-F-002, SYS-F-043 | `wizard.py` Wizard module | `test_init_wizard.py` |
| SWE1-076 | Per-directory config | SYS-F-002, SYS-F-044 | `config.resolve_per_dir_config()` | `test_per_dir_config.py` |
| SWE1-077 | HTML report output | SYS-F-027, SYS-F-045 | `output._violations_to_html()` | `test_html_report.py` |
| SWE1-078 | Function length | SYS-F-020 | `Checker._check_function_length()` | `test_function_length.py` |
| SWE1-079 | Function doc header | SYS-F-020 | `Checker._check_function_doc_header()` | `test_function_doc_header.py` |
| SWE1-080 | Assert density | SYS-F-020 | `Checker._check_assert_density()` | `test_assert_density.py` |
| SWE1-081 | Null statement comment | SYS-F-020 | `Checker._check_null_statement_comment()` | `test_null_statement_comment.py` |
| SWE1-082 | Declaration spacing | SYS-F-020 | `Checker._check_declaration_spacing()` | `test_declaration_spacing.py` |
| SWE1-083 | File length | SYS-F-020 | `Checker._check_file_length()` | `test_file_length.py` |
| SWE1-084 | Reserved header name | SYS-F-020 | `Checker._check_reserved_header_name()` | `test_reserved_header_name.py` |
| SWE1-085 | Macro trailing semicolon | SYS-F-020 | `Checker._check_macro_trailing_semicolon()` | `test_macro_trailing_semicolon.py` |
| SWE1-086 | Macro multistatement wrapper | SYS-F-020 | `Checker._check_macro_multistatement_wrapper()` | `test_macro_multistatement_wrapper.py` |
| SWE1-087 | Identifier length | SYS-F-020 | `Checker._check_identifier_length()` | `test_identifier_length.py` |
| SWE1-088 | No single-char identifiers | SYS-F-020 | `Checker._check_no_single_char_identifiers()` | `test_no_single_char_identifiers.py` |
| SWE1-089 | Per-file breakdown in print_summary | SYS-F-032 | `output.print_summary()` | `test_print_summary.py` |
| SWE1-090 | Typedef-alias constant.case exemption in _check_defines | SYS-F-011 | `Checker._check_defines()` | `test_defines.py` |
| SWE1-091 | misc.constant_comparison — flag constant-to-constant == / != | SYS-F-020 | `Checker._check_constant_comparison()` | `test_constant_comparison.py` |
| SWE1-092 | misc.unsigned_suffix signed-parameter argument exemption | SYS-F-020 | `Checker._check_misc()` | `test_unsigned_suffix_signed_params.py` |
| SWE1-093 | variable.pointer_prefix auto-fix: rename in signature, body, doxygen, header | SYS-F-020 | `fixer._fix_pointer_prefix()`, `fixer.fix_pointer_prefix_in_header()` | `test_pointer_prefix_fix.py` |
| SWE1-094 | Two-line startup banner to stderr at tool entry (unconditional; also `--log`) | SYS-F-046 | `main()` in `cli.py` | `test_cli_requirements.py` (UV-CLI-017 to 019) — full |
| SWE1-095 | Copyright notice in `--version` output | SYS-F-032 | `main()`, `_build_parser()` | `test_cli.py` |
| SWE1-096 | OS-native path separator in violation output | SYS-F-027 | `discover_files()` `emit()` (`os.path.normpath`); `Violation.__str__()` renders verbatim | `test_cli_requirements.py` (UV-CLI-020 to 022) |
| SWE1-097 | `print_summary()` restructure: Files before Results, header, dynamic separator | SYS-F-032 | `output.print_summary()` | `test_print_summary.py` |
| SWE1-098 | `fn_start` line-number correction for multi-line signatures | SYS-F-015 | `Checker._check_functions()` | `test_functions.py` |
| SWE1-099 | Function-pointer typedef exemption from `variable.pointer_prefix` | SYS-F-014 | `Checker._check_variables()` | `test_variables.py` |
| SWE1-109 | misc.goto_usage (MISRA 15.1) | SYS-F-020 | `Checker._check_goto_usage()` | `test_misra_rules.py` |
| SWE1-110 | misc.assignment_in_condition (MISRA 13.4) | SYS-F-020 | `Checker._check_assignment_in_condition()` | `test_misra_rules.py` |
| SWE1-111 | misc.multiple_statements_per_line (Barr-C §3.2) | SYS-F-020 | `Checker._check_multiple_statements_per_line()` | `test_misra_rules.py` |
| SWE1-112 | misc.void_pointer (MISRA 11.5) | SYS-F-020 | `Checker._check_void_pointer()` | `test_misra_rules.py` |
| SWE1-113 | misc.recursive_function (MISRA 17.2, direct only) | SYS-F-020 | `Checker._check_recursive_function()` | `test_misra_rules.py` |
| SWE1-114 | misc.sizeof_type (Barr-C §5.7) | SYS-F-020 | `Checker._check_sizeof_type()` | `test_misra_rules.py` |
| SWE1-115 | misc.boolean_comparison (style, opt-in) | SYS-F-020 | `Checker._check_boolean_comparison()` | `test_misra_rules.py` |
| SWE1-116 | misc.empty_else (Barr-C §8.3) | SYS-F-020 | `Checker._check_empty_else()` | `test_misra_rules.py` |
| SWE1-102 | Trend metrics — LOC classification | — (no SYS parent; CSC-MAN3-001 §10.3 trend monitoring, GP 2.1.4) | `scripts/collect_metrics.py` | `test_collect_metrics.py` |
| SWE1-103 | Trend metrics — cyclomatic complexity / nesting | — (no SYS parent; CSC-MAN3-001 §10.3 trend monitoring, GP 2.1.4) | `scripts/collect_metrics.py` | `test_collect_metrics.py` |
| SWE1-104 | Trend metrics — size | — (no SYS parent; CSC-MAN3-001 §10.3 trend monitoring, GP 2.1.4) | `scripts/collect_metrics.py` | `test_collect_metrics.py` |
| SWE1-105 | Trend metrics — documentation coverage | — (no SYS parent; CSC-MAN3-001 §10.3 trend monitoring, GP 2.1.4) | `scripts/collect_metrics.py` | `test_collect_metrics.py` |
| SWE1-106 | Trend metrics — coupling | — (no SYS parent; CSC-MAN3-001 §10.3 trend monitoring, GP 2.1.4) | `scripts/collect_metrics.py` | `test_collect_metrics.py` |
| SWE1-107 | Trend metrics — violation quality | — (no SYS parent; CSC-MAN3-001 §10.3 trend monitoring, GP 2.1.4) | `_summarise_violations()` | `test_collect_metrics.py` |
| SWE1-108 | Trend metrics — backward-compatible data points, charts and wiki | — (no SYS parent; CSC-MAN3-001 §10.3 trend monitoring, GP 2.1.4) | `generate_charts.py`, `update_wiki_metrics.py`, `collect_metrics.py` | `test_collect_metrics.py` |
| SWE1-117 | Trend metrics — safety indicators and macro metrics | — (no SYS parent; CSC-MAN3-001 §10.3 trend monitoring, GP 2.1.4) | `_c_source_metrics()`, `generate_charts.py`, `update_wiki_metrics.py` | `test_collect_metrics.py` |

> **Upward-trace note (AUD9-F-008):** SYS-NF-003 to SYS-NF-006 (portability, packaging, Docker platforms) are verified at system level by the CI matrix and the Docker build and have no SW requirement. SYS-NF-010 and SYS-NF-012 are deferred to v2.0, and SYS-NF-011 is out of scope for v1.x (see CSC-SYS2-001 §5.9). Every other SYS-F and SYS-NF requirement is cited as a parent by at least one SWE1 requirement.

---

## 6. Review & Approval

| Role | Name | Signature / Electronic Approval | Date |
|---|---|---|---|
| Author | Claude | Approved | 2026-09-29 |
| Technical Reviewer | Dermot Murphy | — | *pending* |
| Quality Assurance | Dermot Murphy | — | *pending* |
| Approver | Dermot Murphy | — | *pending* |

> **Note:** This document is under configuration management (SUP.8). Post-approval changes require a change request (SUP.10) and a new document version.

---

## Appendix A — MISRA C Compliance Traceability Matrix

This appendix satisfies **SWE.1 BP4** (requirements are consistent with the applicable standards) and provides direct input to **SWE.6 BP3** (test coverage of standard-mandated requirements).

CStyleCheck is a **complementary** tool to cppcheck (used for full MISRA C static analysis). It handles naming, formatting, and structural style rules that cppcheck does not enforce. The table below maps each CStyleCheck rule to its MISRA C:2012 and MISRA C:2023 clause.

### A.1 Rules Currently Enforced

| CStyleCheck Rule ID | Check Method | MISRA C:2012 | MISRA C:2023 | Category | Barr-C:2018 | SWE4 Test File |
|---|---|---|---|---|---|---|
| `reserved_name` | `_check_reserved_names()` | Rule 5.3, 5.4, 5.5 | Rule 5.3, 5.4, 5.5 | Required | §6.1.a, §7.1.a | `test_reserved_name.py` |
| `misc.unsigned_suffix` | `_check_misc()` | Rule 7.2 | Rule 7.2 | Required | §8.5 | `test_misc.py` |
| `misc.lowercase_l_suffix` | `_check_lowercase_l_suffix()` | Rule 7.3 | Rule 7.3 | Required | §8.5 | `test_misra_rules.py` |
| `misc.octal_constant` | `_check_octal_constants()` | Rule 7.1 | Rule 7.1 | Required | §8.5 | `test_misra_rules.py` |
| `misc.trigraph` | `_check_trigraphs()` | Rule 4.2 (Advisory) | Rule 4.2 (Required) | Adv / Req | — | `test_misra_rules.py` |
| `misc.yoda_condition` | `_check_yoda()` | — | — | — | §8.3 | `test_yoda_condition.py` |
| `include_guard.missing` | `_check_include_guard()` | Dir 4.10 | Dir 4.10 | Required | §3.2 | `test_include_guards.py` |
| `include_guard.format` | `_check_include_guard()` | Dir 4.10 | Dir 4.10 | Required | §3.2 | `test_include_guards.py` |
| `variable.global.g_prefix` | `_check_variables()` | Rule 5.8 (informative) | Rule 5.8 | Advisory | §7.1.h | `test_variables.py` |
| `variable.static.s_prefix` | `_check_variables()` | Rule 5.9 (informative) | Rule 5.9 | Advisory | §7.1.i | `test_variables.py` |
| `variable.pointer_prefix` | `_check_variables()` | — | — | — | §7.1.k | `test_variables.py` |
| `variable.pp_prefix` | `_check_variables()` | — | — | — | §7.1.l | `test_variables.py` |
| `variable.bool_prefix` | `_check_variables()` | — | — | — | §7.1.m | `test_variables.py` |
| `variable.handle_prefix` | `_check_variables()` | — | — | — | §7.1.n | `test_variables.py` |
| `variable.min_length` | `_check_variables()` | — | — | — | §7.1.e | `test_variables.py` |
| `sign_compatibility` | `SignChecker._check_calls()` | Rule 10.1, 10.3 (partial) | Rule 10.1, 10.3 (partial) | Required | — | `test_sign_compatibility.py` |
| `typedef.case` / `typedef.suffix` | `_check_typedefs()` | Dir 4.6 (partial) | Dir 4.6 (partial) | Required | §7.3 | `test_typedefs.py` |
| `function.prefix` / `function.style` | `_check_functions()` | — | — | — | §8.1 | `test_functions.py` |
| `enum.type_case` / `enum.member_case` | `_check_enums()` | — | — | — | §7.2 | `test_enums.py` |
| `struct.tag_case` / `struct.member_case` | `_check_structs()` | — | — | — | §7.3 | `test_structs.py` |
| `misc.magic_number` | `_check_misc()` | — | — | — | §8.5 | `test_misc.py` |
| `misc.line_length` | `_check_misc()` | — | — | — | §3.3 | `test_misc.py` |
| `misc.copyright_header` | `_check_copyright_header()` | — | — | — | §3.1 | `test_copyright_header.py` |
| `misc.eof_comment` | `_check_misc()` | — | — | — | §3.1 | `test_eof_comment.py` |
| `misc.block_comment_spacing` | `_check_misc()` | — | — | — | §3.3 | `test_block_comment_spacing.py` |
| `spell_check` | `_check_spelling()` | — | — | — | — | `test_spell_check.py` |
| `misc.whitespace_ratio` | `_check_whitespace_ratio()` | — | — | — | — | `test_whitespace_ratio.py` |
| `misc.non_ascii_source` | `_check_non_ascii_source()` | Rule 4.1 (source character set, partial) | Rule 4.1 | Required | — | `test_misra_rules.py` |
| `misc.goto_usage` | `_check_goto_usage()` | Rule 15.1 | Rule 15.1 | Advisory | — | `test_misra_rules.py` |
| `misc.assignment_in_condition` | `_check_assignment_in_condition()` | Rule 13.4 (partial — conditions only) | Rule 13.4 | Advisory | — | `test_misra_rules.py` |
| `misc.multiple_statements_per_line` | `_check_multiple_statements_per_line()` | — | — | — | §3.2 | `test_misra_rules.py` |
| `misc.void_pointer` | `_check_void_pointer()` | Rule 11.5 (flags all `void *` use) | Rule 11.5 | Advisory | — | `test_misra_rules.py` |
| `misc.recursive_function` | `_check_recursive_function()` | Rule 17.2 (direct recursion only) | Rule 17.2 | Required | — | `test_misra_rules.py` |
| `misc.sizeof_type` | `_check_sizeof_type()` | — | — | — | §5.7 | `test_misra_rules.py` |
| `misc.boolean_comparison` | `_check_boolean_comparison()` | — (style rule; Rule 14.4 not enforced) | — | — | — | `test_misra_rules.py` |
| `misc.empty_else` | `_check_empty_else()` | Rule 15.7 (informative) | Rule 15.7 | Required | §8.3 | `test_misra_rules.py` |

### A.2 MISRA C Rules Delegated to cppcheck

The following MISRA C rules require full compiler-level analysis and are enforced by **cppcheck** (run separately in the CI pipeline). CStyleCheck does not duplicate them.

| MISRA C:2012 | MISRA C:2023 | Topic | Category |
|---|---|---|---|
| Dir 4.1 | Dir 4.1 | Run-time failures shall be minimised | Required |
| Dir 4.7 | Dir 4.7 | Error information shall be tested | Required |
| Dir 4.11 | Dir 4.11 | Validity of values passed to library functions | Required |
| Dir 4.12 | Dir 4.12 | Dynamic memory shall not be used | Required |
| Rules 1.1–1.3 | Rules 1.1–1.3 | Language conformance, extensions, UB | Required |
| Rules 2.1–2.7 | Rules 2.1–2.7 | Unused code, dead code, unreachable code | Required / Advisory |
| Rules 6.1–6.2 | Rules 6.1–6.2 | Bit-field types | Required |
| Rules 8.1–8.18 | Rules 8.1–8.18 | Declarations and definitions | Required / Advisory |
| Rules 9.1–9.5 | Rules 9.1–9.5 | Initialisation | Required / Advisory |
| Rules 10.1–10.8 | Rules 10.1–10.8 | Essential type model | Required |
| Rules 11.1–11.9 | Rules 11.1–11.9 | Pointer type conversions (Rule 11.5 also partially covered by `misc.void_pointer`) | Required / Advisory |
| Rules 12.1–12.5 | Rules 12.1–12.5 | Expressions | Required / Advisory |
| Rules 13.1–13.6 | Rules 13.1–13.6 | Side effects (Rule 13.4 also partially covered by `misc.assignment_in_condition`) | Required |
| Rules 14.1–14.4 | Rules 14.1–14.4 | Control flow (Rule 14.4 is not covered by CStyleCheck; `misc.boolean_comparison` is a style rule) | Required |
| Rules 15.1–15.7 | Rules 15.1–15.7 | Control statements (Rule 15.1 also covered by `misc.goto_usage`; Rule 15.7 partially by `misc.empty_else`) | Required / Advisory |
| Rules 16.1–16.7 | Rules 16.1–16.7 | Switch statements | Required / Advisory |
| Rules 17.1–17.8 | Rules 17.1–17.8 | Functions (Rule 17.2 direct recursion also covered by `misc.recursive_function`) | Required / Advisory |
| Rules 18.1–18.8 | Rules 18.1–18.8 | Pointers and arrays | Required / Advisory |
| Rules 20.1–20.14 | Rules 20.1–20.14 | Preprocessing directives | Required / Advisory |
| Rules 21.1–21.21 | Rules 21.1–21.21 | Standard library | Required / Advisory |
| Rules 22.1–22.10 | Rules 22.1–22.10 | Resource management | Required / Advisory |

### A.3 Gap Analysis Summary

| Category | MISRA C:2012 Rules | Covered by CStyleCheck | Covered by cppcheck | Gap (not covered) |
|---|---|---|---|---|
| Preprocessing directives | Dir 4.1–4.14 | Dir 4.10 (partial) | Dir 4.1, 4.7, 4.11–4.14 | Dir 4.2 ✅ (added v1.1) |
| Lexical conventions | Rules 4.1–4.2, 7.1–7.4 | Rule 4.1 (partial, `misc.non_ascii_source`), 4.2 ✅, 7.1 ✅, 7.2 ✅, 7.3 ✅ | Rule 7.4 | None |
| Identifiers | Rules 5.1–5.9 | Rules 5.3–5.5 (partial), 5.8–5.9 (advisory) | Rules 5.1, 5.2, 5.6, 5.7 | None critical |
| Types | Rules 6.1–6.2 | — | Rules 6.1–6.2 | None |
| Sign / type model | Rules 10.1–10.8 | Rules 10.1, 10.3 (partial) | Full coverage | Rules 10.2, 10.4–10.8 (cppcheck) |
| Control flow | Rules 14.1–15.7 | 15.1 ✅ (`misc.goto_usage`), 15.7 (partial, `misc.empty_else`) | Full coverage (including Rule 14.4, MISRA addon) | None critical |
| Side effects / pointers / functions | Rules 11.5, 13.4, 17.2 | 11.5 (`misc.void_pointer`), 13.4 (partial, `misc.assignment_in_condition`), 17.2 (direct only, `misc.recursive_function`) | Full coverage | None critical |

> **Conclusion:** All MISRA C:2012/2023 Required rules are covered by the combination of CStyleCheck and cppcheck. The three new rules added in v1.1 (7.1, 7.3, 4.2) close the previously identified lexical-convention gap. The post-v1.6.0 rules (SWE1-109 to SWE1-116) add early, style-level detection for MISRA 11.5, 13.4, 15.1, 15.7 and 17.2. MISRA Rule 14.4 is not covered by CStyleCheck (`misc.boolean_comparison` is a style rule; `if (flag == true)` is compliant with Rule 14.4) and is delegated to cppcheck with the MISRA addon. cppcheck remains the authoritative checker for these rules.

