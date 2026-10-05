﻿﻿﻿﻿﻿﻿﻿# Software Unit Verification Specification

*Automotive SPICE® PAM v4.0 | SWE.4 Software Unit Verification*

---

## 1. Document Identification & Control

| Field | Value | Field | Value |
|---|---|---|---|
| **Document ID** | CSC-SWE4-001 | **Version** | 1.39 |
| **Project** | CStyleCheck | **Date** | 2026-09-30 |
| **Status** | Released | **Classification** | Internal |
| **Author** | Claude | **Reviewer** | Dermot Murphy |
| **Approver** | Dermot Murphy | **Related Process** | SWE.4 |

> **Note — Reviewer independence (CSC-DEV-002):** The Reviewer and Approver are the same person (Dermot Murphy). This is accepted under deviation record **CSC-DEV-002** (`docs/aspice/CStyleCheck_DEV002_Independent_Review_Deviation.md`) on the basis that CStyleCheck has a single human team member.

---

## 2. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.39 | 2026-10-05 | Claude | Issue #441 (CR-441): add §5.22 catalogue for `test_output_dirs.py` (UV-OUT-001 to UV-OUT-004, 11 tests: missing parent folders of `--log`, `--write-baseline` and `--init-output` files are created; an uncreatable folder exits 2); §6 new module row, total 1546→1557 (59 modules); coverage-gate text 1546→1557; §7 SWE1-062, SWE1-065 and SWE1-075 rows cite UV-OUT |
| 1.38 | 2026-10-05 | Claude | Issue #439: UV-CLI-019 adds `test_structured_log_file_has_no_banner` — with `--output-format json`, `sarif` or `html` and `--log FILE`, the log file equals the stdout document and has no banner (JSON and SARIF parse with `json.loads`); §6 `test_cli_requirements.py` 21→22; total 1545→1546; coverage-gate text 1545→1546; §7 SWE1-094 row notes the text-only `--log` copy |
| 1.37 | 2026-09-30 | Claude | Cross-reference version resync (#437): referenced-document versions set to the current baseline after the merge-time process-control changes; no technical content change |
| 1.36 | 2026-09-30 | Claude | Cross-reference version resync (#435): all referenced-document versions set to the current baseline (every controlled work product bumped once in this change set); no technical content change |
| 1.35 | 2026-09-29 | Claude | CSC-AUD-010 corrective actions (#430). AUD10-F-007: UV-CLI-018 `test_copyright_line_format` also asserts the `--version` output (version line, then `(C) <year> <holder>` on its own line); UV-CLI-018 traces to SWE1-095 as well; §7 SWE1-095 row cites UV-CLI-018 for the copyright text (test total unchanged, 1545). AUD10-F-027: §6 `test_case_style_config.py`, `test_functions_case_removed.py` and `test_enums.py` rows name `validate_case_styles`, `deprecated_key_warnings`, `normalize_case_style` and `_enum_members` as sub-units of UNIT-05, UNIT-43 and UNIT-27 (SWE3 §4); referenced-document versions resynced (SWE3 1.29→1.30); approval-by-merge policy (CSC-DEV-002 §5.2) |
| 1.34 | 2026-09-29 | Claude | Issue #423: add UV-TYP-005a (`TestEnumLastMember`, 13 tests: last enum member checked for `enum.member_case` and `enum.member_prefix` with and without trailing comma, with initialiser, trailing comment, single-line and one-member enums; initialiser identifiers and `#if` lines not treated as members); §5.4 heading and §6 `test_enums.py` 11→24; total 1532→1545 (58 modules); coverage-gate text 1532→1545; §7 SWE1-040 to 042 row cites UV-TYP-005a; referenced-document versions resynced (4) |
| 1.33 | 2026-09-29 | Claude | Issue #425: add §5.21 catalogue for `test_exit_code_entry_points.py` (UV-EXIT-001 to UV-EXIT-003, 8 tests: `config_error()`, string-exit mapping in `main()`, nine config/usage error paths exit 2 through the console-script target and `src/cstylecheck.py`); `test_config_loading.py` patches `config_error`; §6 new module row, total 1524→1532 (58 modules); coverage-gate text 1524→1532; §7 SWE1-001/002 and SWE1-068 to 070 rows cite UV-EXIT; referenced-document versions resynced (4) |
| 1.32 | 2026-09-29 | Claude | Issue #424: add §5.20 catalogue for `test_functions_case_removed.py` (UV-FCASE-001 to UV-FCASE-004, 16 tests: no `functions.case` in presets, wizard or repo configs; not a case-style key; `WARNING` on `stderr` with unchanged exit code, once per root or per-directory config; function naming still set by `functions.style`); UV-CASE-003 — 15→14 case-style keys; §6 new module row, total 1508→1524 (57 modules); coverage-gate text 1508→1524; §7 SWE1-001/002, SWE1-030 to 034 and SWE1-075 rows cite UV-FCASE; referenced-document versions resynced (4) |
| 1.31 | 2026-09-29 | Claude | Issue #422: add §5.19 catalogue for `test_case_style_config.py` (UV-CASE-001 to UV-CASE-005, 27 tests: canonical case names in presets and wizard output, alias normalisation, unknown style → exit 2, repo configs validate, end-to-end findings from a generated config); UV-WIZ-002 — `camelCase` stored as `camel`; §6 new module row, total 1481→1508 (56 modules); coverage-gate text 1481→1508; §7 SWE1-001/002 SWE1-040 to 042 and SWE1-075 rows cite UV-CASE; referenced-document versions resynced (4) |
| 1.30 | 2026-09-29 | Claude | Issue #420: add §5.18 catalogue for `test_init_wizard.py` (UV-WIZ-001 to UV-WIZ-005; UV-WIZ-004/005 are the 18 new preset and wizard opt-in rule tests); §6 `test_init_wizard.py` 15→33; total 1463→1481 (55 modules); coverage-gate text 1463→1481; §7 SWE1-075 cites UV-WIZ-001 to UV-WIZ-005; referenced-document versions resynced (4) |
| 1.29 | 2026-09-29 | Claude | Issue #418 (CR-418): add UV-MSR-009 (11 opt-in policy tests: 7 key-absent tests, one per rule made opt-in; shipped-disabled check for all 8 rules; empty-`misc` no-fire test; code-default vs shipped-default check; `--update-config` adds the keys as `false`); §5.14 heading 140→160; §6 `test_misra_rules.py` 149→160; total 1452→1463 (55 modules); coverage-gate text 1452→1463; §7 SWE1-109 to SWE1-116 also cite UV-MSR-009; referenced-document versions resynced (4) |
| 1.28 | 2026-09-29 | Claude | Issue #412: UV-MSR-007 10→18 tests (key absent, `misc` absent, shipped default, explicit enable, `TRUE == flag`, `flag != FALSE`, `true == x`, `x == false`); `test_uppercase_true_flagged` changed to `test_uppercase_true_not_flagged`; §6 `test_misra_rules.py` 141→149; total 1444→1452 (55 modules); coverage-gate text 1444→1452; referenced-document versions resynced (4) |
| 1.27 | 2026-09-29 | Claude | Release-prep cross-reference resync: 4 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.26 | 2026-09-29 | Claude | Issue #413 (CR-413): SWE1-094 now matches the code, so UV-CLI-017 to UV-CLI-019 verify it in full; 5 tests added (piped stdout, `--log` copy, exactly two lines, copyright line format, no `--quiet` option); §5.17 and §6 `test_cli_requirements.py` 16→21; total 1439→1444; coverage-gate text 1439→1444; §7 SWE1-094 row full and the partial-verification note removed; referenced-document versions resynced (SWE1 2.9→2.10, SWE3 1.19→1.20, SWE5 1.16→1.17) |
| 1.25 | 2026-09-29 | Claude | #410: UV-MSR-007 no longer cites MISRA C:2012 Rule 14.4 (`misc.boolean_comparison` is a style rule) |
| 1.24 | 2026-09-29 | Claude | Issue #407 (RR-003-001, AUD9-F-004): add §5.17 `test_cli_requirements.py` (16 tests, UV-CLI-014 to UV-CLI-022) giving SWE1-015 (single read per file), SWE1-094 (startup banner on stderr) and SWE1-096 (OS-native path separator) dedicated unit tests; §6 row (total 1423→1439, modules 54→55); coverage-gate text 1423→1439; §7 rows for SWE1-015, SWE1-094 and SWE1-096 now cite the UV IDs (SWE1-094 `--quiet` suppression and one-line form not implemented — see §7 note); §3.1 referenced-document versions resynced (SUP8 1.13→1.14, SWE1 2.8→2.9, SWE3 1.18→1.19, SWE5 1.15→1.16) |
| 1.23 | 2026-09-29 | Claude | #408: add `test_message_cites_barr_c_only` to UV-MSR-003 (8→9 tests); `test_misra_rules.py` 140→141; total 1422→1423 |
| 1.22 | 2026-09-29 | Claude | CSC-AUD-009 corrective actions (#405). AUD9-F-003: catalogue the 76 tests from #391/#392 (UV-MSR-001 to UV-MSR-008); `test_misra_rules.py` 64→140; total 1346→1422 (54 modules); coverage-gate text 1279→1422; scope text. AUD9-F-004: §7 rows for SWE1-001 to 006, 011 to 016, 057 to 064, 094 to 099 and SWE1-MISRA-001 to 003 (SWE1-015, 094 and 096 have no dedicated unit test and are recorded as gaps). AUD9-F-001/F-010: §7 rows for SWE1-109 to SWE1-117. AUD9-F-015: header date. AUD9-F-024: Author and Description columns swapped back in earlier revision rows. AUD9-F-014: referenced-document versions resynced to current revisions |
| 1.21 | 2026-09-29 | Claude | Add §5.16 `test_collect_metrics.py` (54 tests, UV-MET-001 to UV-MET-010) for trend-analysis C source metrics; add §6 row (total 1279→1333, modules 53→54); add SWE1-102 to SWE1-108 to §7; update §3.1 refs (SWE1 2.6→2.7, SWE3 1.16→1.17); also records UV-CLI-011 to UV-CLI-013 and §5.13 and §6 test_improvements 67→80, §6 total 1333→1346 (baseline, issues #394/#395, PR #397) — issue #388 |
| 1.20 | 2026-07-06 | Claude | ASPICE audit — update §6 per-row test counts for 8 modules (+56 total): test_defines.py 22→30, test_yoda_condition.py 37→46, test_inline_suppression.py 15→24, test_constant_comparison.py 21→27, test_parameter_prefix.py 47→51, test_pointer_prefix_fix.py 10→20, test_print_summary.py 7→11, test_unsigned_suffix_signed_params.py 9→15; update §3.1 refs (SWE1 2.4→2.6, SWE3 1.15→1.16, SWE5 1.11→1.14); add SWE1-091/092/093 to §7 traceability — closes #374 |
| 1.19 | 2026-07-06 | Claude | v1.6.0 RC — update test total 1223→1279 (+56 across 8 modules: yoda_condition 37→46, inline_suppression 15→24, constant_comparison 21→27, defines 22→30, parameter_prefix 47→51, pointer_prefix_fix 10→20, print_summary 7→11, unsigned_suffix_signed_params 9→15); update coverage comment; update §5.5 SVD→1.22 |
| 1.18 | 2026-07-01 | Claude | v1.6.0 — add test_constant_comparison.py (21 tests), test_unsigned_suffix_signed_params.py (9 tests), test_pointer_prefix_fix.py (10 tests); update §3.1 refs (SWE1 2.4→2.5, SWE5 1.11→1.12); update test total 1183→1223, modules 50→53; update coverage comment — closes #339 #340 #341 |
| 1.17 | 2026-06-27 | Dermot Murphy | Fix §3.1 cross-refs: SWE1 2.3→2.4, SWE3 1.14→1.15, SWE5 1.9→1.11 |
| 1.16 | 2026-06-27 | Dermot Murphy | Fix §3.1 cross-refs: SWE1 2.1→2.3, SWE3 1.12→1.14 |
| 1.15 | 2026-06-27 | Claude | ASPICE audit — fix §4.2 test count 1041→1183; fix §6 COMP-01→COMP-05f/h for 11 modules; update coverage ref to v1.5.0; update Review & Approval dates — closes #317 #323 |
| 1.14 | 2026-06-26 | Claude | ASPICE audit — fix §3 scope text (v1.2.x→v1.5.0); update §3.1 refs (SWE1 1.9→2.1, SWE3 1.10→1.12, SWE5 1.5→1.9); correct §6 total 52→50 modules; update test_null_statement_comment count 10→11 and total 1182→1183 — closes #305 #306 #309 #312 |
| 1.13 | 2026-06-26 | Claude | Add NR-004 tests (12 tests, test_misra_rules.py 52→64), typedef-alias tests (6 tests, test_defines.py 16→22), test_print_summary.py (7 tests, new); update §5 and §6 totals 1157→1182 — issues #279 #278 #272 #244 |
| 1.12 | 2026-06-18 | Claude | v1.4.1 patch (issue #273) — add 5 regression tests to `test_parameter_prefix.py` (42→47); update §6 total 1152→1157 |
| 1.11 | 2026-06-18 | Claude | ASPICE audit #254 — update §6 test total 1143→1152 (49 modules) |
| 1.10 | 2026-06-08 | Claude | ASPICE audit #238 — correct CSC-SWE3 version reference 1.8→1.9 in §3.1 |
| 1.9 | 2026-06-08 | Claude | Add 11 new test modules (102 tests) for issues #221–#232; update §6 totals; update §7 traceability |
| 1.8 | 2026-06-05 | Claude | CSC-AUD-005 corrective action — fix factual errors identified in audit |
| 1.6 | 2026-06-04 | Claude | Automated accuracy audit: add §6 rows for test_preprocessor.py/test_comment_ratio/test_declared_not_defined/test_update_config/test_config_loading; update total 786→965; fix section header counts (§5.4/§5.6/§5.12/§5.13); update referenced doc versions; fix §3 version text; update coverage note — resolves issue #163 |
| 1.5 | 2026-05-28 | Claude | Add §5.7b whitespace_ratio test catalogue (27 tests); fix §5.1 count 32→35; add §6 row for test_whitespace_ratio.py; update total 759→786; update §7 traceability — closes issues #148 #157 |
| 1.4 | 2026-05-28 | Dermot Murphy | §4.2: implement subprocess coverage via COVERAGE_PROCESS_START + sitecustomize.py; raise CI gate to 85% combined; actual v1.2.0 CI: 89.8% stmt, 87.31% combined — closes issue #54 |
| 1.3 | 2026-05-28 | Dermot Murphy | Populate §6 results table: actual test counts, all PASS; coverage 86% stmt / N/A branch (v1.1.0 CI); add 5 missing test modules — closes issue #53 |
| 1.2 | 2026-05-28 | Dermot Murphy | Add CSC-DEV-002 deviation footnote to §1 — closes issue #61 |
| 1.1 | 2026-05-28 | Claude | Added static type check (mypy --ignore-missing-imports) and lint check (ruff) as verification methods in §4.1; updated CI workflow reference |
| 1.0 | 2026-04-12 | Claude | Initial release |

---

## 3. Purpose & Scope

This specification defines the unit verification strategy, coverage criteria, and test case catalogue for **CStyleCheck v1.6.0 and the post-v1.6.0 `develop` baseline**. It satisfies **Automotive SPICE® PAM v4.0, SWE.4 — Software Unit Verification**.

Unit verification covers both dynamic testing (pytest test suite) and static verification (naming convention self-check via `rules.yml` CI workflow).

### 3.1 Referenced Documents

| Document ID | Title | Version |
|---|---|---|
| CSC-SWE1-001 | CStyleCheck Software Requirements Specification | 2.24 |
| CSC-SWE3-001 | CStyleCheck Software Detailed Design | 1.34 |
| CSC-SWE5-001 | CStyleCheck Software Integration Test Specification | 1.28 |
| CSC-SUP8-001 | CStyleCheck Configuration Management Plan | 1.25 |

---

## 4. Unit Verification Strategy

### 4.1 Verification Methods

| Method | Scope | Tool |
|---|---|---|
| Dynamic unit testing | All COMP-05 rule-check methods; COMP-02, COMP-03, COMP-04, COMP-06, COMP-07 utility functions | pytest 7+ |
| Static verification (naming convention) | `src/cstylecheck/` package source files | `cstylecheck` self-hosted via `rules.yml` CI |
| Static type check | `src/cstylecheck/` — import and inferred-type check (`--ignore-missing-imports`; `--strict` deferred until codebase is annotated) | mypy 1.0+ |
| Lint check | `src/` and `tests/` — style and common error detection | ruff 0.1+ |
| Code coverage measurement | `src/cstylecheck/` | pytest-cov |
| Code review / inspection | `SignChecker` try/finally pattern (SWE1-053); `_data_file()` fallback logic | Manual review during PR |

### 4.2 Coverage Criteria

| Coverage Type | Long-term Target | v1.1.0 Baseline (stmt-only, excl. subprocess) | CI Gate | Rationale |
|---|---|---|---|---|
| Statement coverage | ≥ 90% | 89.8% (1,694 stmts, 172 missed — v1.2.0 CI with subprocess) | ≥ 85% combined (see note) | All reachable statements exercised; subprocess coverage via `COVERAGE_PROCESS_START` |
| Branch coverage | ≥ 85% | 87.31% combined stmt+branch (874 branch pts, 96 partial — v1.2.0 CI) | ≥ 85% combined (see note) | All major decision branches covered |
| Function coverage | 100% of public functions | ~95% | reported only | Every unit invoked at least once |

Coverage is measured per CI run on all three Python matrix versions (3.10, 3.11, 3.12) and reported via `coverage.xml` artefact (uploaded as a GitHub Actions artefact, Python 3.11 build).

**CI gate (from v1.2.0+):** `--cov-fail-under=85 --cov-branch` applied across all 1557 tests (2026-10-05 develop baseline, after #408, #407, #413, #412, #418, #420, #422, #424, #425 and #423) including `test_cli.py` subprocess calls. Combined coverage 87.31% ≥ 85% gate ✅

> **Subprocess coverage implementation (issue #54 — resolved):** From v1.2.0 CI onwards, `COVERAGE_PROCESS_START` and `sitecustomize.py` subprocess instrumentation are enabled in `cstylecheck_tests.yml`. This allows `test_cli.py` to contribute coverage of `main()` and the CLI output helpers (`_violations_to_json`, `_violations_to_sarif`, `write_baseline`, `load_baseline`, `print_summary`), which previously accounted for ~14% of unmeasured statements (the v1.1.0 measured baseline was 86% statement-only, excluding subprocess invocations). The CI gate has been raised from 72% statement-only to 85% combined statement + branch. The long-term targets of ≥ 90% statement and ≥ 85% branch remain; the 85% combined gate will be reviewed once the first post-instrumentation CI run reports actual figures (baseline reference: 1279 tests as of v1.6.0).

### 4.3 Test Infrastructure

All dynamic unit tests use the shared test harness in `tests/harness.py`:

```python
from harness import run, rules, has, clean, count, cfg_only

# Inject source string directly — no file I/O in unit tests
violations = run(source="uint32_t BadName = 0U;\n", cfg=cfg, filepath="mymod.c")
assert "variable.global.case" in rules(source, cfg, filepath="mymod.c")
```

Key harness functions:

| Function | Purpose |
|---|---|
| `run(source, cfg, **kw)` | Return `List[Violation]` for given source and config |
| `rules(source, cfg, **kw)` | Return list of rule ID strings |
| `has(source, cfg, rule_id, **kw)` | Return `True` if rule\_id present in violations |
| `clean(source, cfg, **kw)` | Return `True` if zero violations |
| `count(source, cfg, rule_id, **kw)` | Return count of a specific rule ID |
| `cfg_only(**overrides)` | Build config with all rules off except those in overrides |

### 4.4 Naming Convention Self-Check (Static Verification)

CStyleCheck enforces its own naming rules on `src/cstylecheck/` via the `rules.yml` CI workflow. This constitutes a static verification pass satisfying SWE.4 BP3.

| Verification Item | Evidence |
|---|---|
| Zero `error`-level violations on `src/cstylecheck/` | `rules.yml` CI job PASS |
| Workflow trigger | Every push that modifies `src/cstylecheck/` |

---

## 5. Unit Test Catalogue

Tests are organised by test module. Each module maps to one or more COMP-05 sub-checkers.

---

### 5.1 Variable Rules — `test_variables.py` (43 tests)

| TC-ID | Test Name | Rule Verified | Pass Condition |
|---|---|---|---|
| UV-VAR-001 | `test_correct_global_passes` | `variable.global.case` | Clean source; no violation |
| UV-VAR-002 | `test_wrong_module_prefix_fails` | `variable.global.prefix` | `variable.global.prefix` violation raised |
| UV-VAR-003 | `test_g_prefix_warning` | `variable.global.g_prefix` | `variable.global.g_prefix` warning raised |
| UV-VAR-004 | `test_static_s_prefix_required` | `variable.static.s_prefix` | Violation raised for missing `s_` |
| UV-VAR-005 | `test_static_correct_prefix_passes` | `variable.static.s_prefix` | No violation for `s_` prefix |
| UV-VAR-006 | `test_pointer_p_prefix_required` | `variable.pointer_prefix` | Violation for `*data` parameter |
| UV-VAR-007 | `test_double_pointer_pp_prefix` | `variable.pp_prefix` | Violation for `**buf` without `pp_` |
| UV-VAR-008 | `test_bool_prefix_required` | `variable.bool_prefix` | Violation for `bool enabled` without `b_` |
| UV-VAR-009 | `test_prefix_order_enforced` | `variable.prefix_order` | Violation if `p_g_` instead of `g_p_` |
| UV-VAR-010 | `test_min_length_enforced` | `variable.min_length` | Violation for 2-char name when min=3 |
| UV-VAR-011 | `test_loop_var_exemption` | `variable.min_length` | Single-char loop var exempt when configured |
| UV-VAR-012 | `test_max_length_enforced` | `variable.max_length` | Violation for name > max_length |
| UV-VAR-013 | `test_allowed_abbreviations_exempt` | `variable.global.case` | `FIFO` in name does not trigger case violation |
| UV-VAR-014 | `test_local_var_no_prefix_required` | `variable.local.*` | Local var without module prefix passes |
| UV-VAR-015 | `test_parameter_case` | `variable.parameter.case` | `lower_snake` enforced on parameters |

---

### 5.2 Function Rules — `test_functions.py` (14 tests)

| TC-ID | Test Name | Rule Verified | Pass Condition |
|---|---|---|---|
| UV-FUN-001 | `test_correct_function_passes` | `function.prefix` | No violation for `uart_BufferRead()` in `uart.c` |
| UV-FUN-002 | `test_missing_prefix_fails` | `function.prefix` | Violation for `Init()` in `uart.c` |
| UV-FUN-003 | `test_object_verb_style` | `function.style` | `uart_BufferRead` passes; `uart_readBuffer` fails |
| UV-FUN-004 | `test_static_function_prv_prefix` | `function.static_prefix` | Violation for `static int helper()` without `prv_` |
| UV-FUN-005 | `test_function_min_length` | `function.min_length` | Violation for function name below min |
| UV-FUN-006 | `test_function_max_length` | `function.max_length` | Violation for function name above max |
| UV-FUN-007 | `test_main_exempt` | `function.prefix` | `main()` in `main.c` does not require module prefix |

---

### 5.3 Constant and Macro Rules — `test_defines.py` (30 tests)

| TC-ID | Test Name | Rule Verified | Pass Condition |
|---|---|---|---|
| UV-DEF-001 | `test_upper_snake_constant_passes` | `constant.case` | `#define UART_MAX_BAUD 115200U` passes |
| UV-DEF-002 | `test_mixed_case_constant_fails` | `constant.case` | `#define Uart_MaxBaud` raises violation |
| UV-DEF-003 | `test_constant_module_prefix` | `constant.prefix` | Missing module prefix raises violation |
| UV-DEF-004 | `test_macro_with_params` | `macro.case` | Function-like macro checked separately |
| UV-DEF-005 | `test_exempt_pattern_skipped` | `constant.case` | `__FILE__` exempt via `exempt_patterns` |
| UV-DEF-006 | `test_constant_min_length` | `constant.min_length` | Violation for constant name below min |
| UV-DEF-007 | `test_constant_max_length` | `constant.max_length` | Violation for constant name above max |
| UV-DEF-008 | `test_typedef_alias_lower_snake_no_constant_case` | `constant.case` | `#define module_my_type_t uint8_t` NOT flagged when suffix enabled (issue #272) |
| UV-DEF-009 | `test_typedef_alias_mixed_case_no_constant_case` | `constant.case` | Mixed-case typedef alias NOT flagged for `constant.case` |
| UV-DEF-010 | `test_regular_constant_still_flagged` | `constant.case` | Non-`_t` constant with wrong case still flagged |
| UV-DEF-011 | `test_function_like_macro_still_flagged` | `macro.case` | Function-like `_t`-suffixed macro still flagged |
| UV-DEF-012 | `test_typedef_suffix_disabled_alias_flagged` | `constant.case` | When suffix disabled, `_t`-named constant IS flagged |
| UV-DEF-013 | `test_typedef_alias_uppercase_t_suffix` | `constant.case` | Suffix match is case-insensitive (`_T` also exempted) |

---

### 5.4 Type Rules — `test_typedefs.py` (8), `test_enums.py` (24), `test_structs.py` (12)

| TC-ID | Test Name | Rule Verified | Pass Condition |
|---|---|---|---|
| UV-TYP-001 | `test_typedef_t_suffix_required` | `typedef.suffix` | `typedef uint8_t BYTE_T` passes; `BYTE` fails |
| UV-TYP-002 | `test_typedef_upper_snake_case` | `typedef.case` | `typedef uint8_t byte_t` fails |
| UV-TYP-003 | `test_multi_token_typedef` | `typedef.case` | `typedef unsigned int UINT_T` correctly detected |
| UV-TYP-004 | `test_enum_type_suffix` | `enum.type_suffix` | `enum uart_state_t` passes; `uart_state` fails |
| UV-TYP-005 | `test_enum_member_prefix` | `enum.member_prefix` | `UART_STATE_IDLE` passes; `STATE_IDLE` fails |
| UV-TYP-005a | `TestEnumLastMember` (13 tests, #423) | `enum.member_case`, `enum.member_prefix` | The last member is reported for both rules without a trailing comma, with a trailing comma, with an initialiser (`badLast = 5`), with a trailing block or line comment, in a single-line two-member enum and in a one-member enum; a correctly cased last member with the wrong prefix gets `enum.member_prefix` only (with and without trailing comma); valid last members with initialisers and comments pass; identifiers inside an initialiser (`= OTHER_BASE`, `(SHIFT_A \| SHIFT_B)`) are not members; `#if` lines in the body are ignored; the finding is on the member's own line |
| UV-TYP-006 | `test_struct_tag_suffix` | `struct.tag_suffix` | `struct uart_cfg_s` passes |
| UV-TYP-007 | `test_struct_member_case` | `struct.member_case` | `lower_snake` enforced on members |

---

### 5.5 Include Guard Rules — `test_include_guards.py` (8 tests)

| TC-ID | Test Name | Rule Verified | Pass Condition |
|---|---|---|---|
| UV-INC-001 | `test_correct_guard_passes` | `include_guard.format` | `#ifndef UART_H_` passes for `uart.h` |
| UV-INC-002 | `test_missing_guard_fails` | `include_guard.missing` | Header with no guard raises violation |
| UV-INC-003 | `test_pragma_once_accepted` | `include_guard.missing` | `#pragma once` accepted as valid guard |
| UV-INC-004 | `test_wrong_guard_name` | `include_guard.format` | Guard name not matching filename raises violation |
| UV-INC-005 | `test_c_file_no_guard_required` | `include_guard.missing` | `.c` files not checked for guards |

---

### 5.6 Miscellaneous Rules — `test_misc.py` (28), `test_misc_improvements.py` (77), `test_block_comment_spacing.py`

| TC-ID | Test Name | Rule Verified | Pass Condition |
|---|---|---|---|
| UV-MSC-001 | `test_line_too_long` | `misc.line_length` | Line > max raises violation |
| UV-MSC-002 | `test_line_at_limit_passes` | `misc.line_length` | Line exactly at limit passes |
| UV-MSC-003 | `test_comment_line_exempt` | `misc.line_length` | Comment-only line exempt |
| UV-MSC-004 | `test_magic_number_detected` | `misc.magic_number` | Literal `42` in expression raises violation |
| UV-MSC-005 | `test_define_rhs_exempt` | `misc.magic_number` | `#define X 42` RHS is exempt |
| UV-MSC-006 | `test_unsigned_suffix_required` | `misc.unsigned_suffix` | `uint32_t x = 100;` raises violation (needs `100U`) |
| UV-MSC-007 | `test_unsigned_suffix_passes` | `misc.unsigned_suffix` | `100U` passes |

---

### 5.7 Yoda Conditions — `test_yoda_condition.py` (46 tests)

| TC-ID | Test Name | Rule Verified | Pass Condition |
|---|---|---|---|
| UV-YOD-001 | `test_null_on_left_passes` | `misc.yoda_condition` | `if (NULL == p_ptr)` passes |
| UV-YOD-002 | `test_null_on_right_fails` | `misc.yoda_condition` | `if (p_ptr == NULL)` fails |
| UV-YOD-003 | `test_literal_on_left_passes` | `misc.yoda_condition` | `if (0 == count)` passes |
| UV-YOD-004 | `test_two_variables_exempt` | `misc.yoda_condition` | `if (a == b)` no violation |
| UV-YOD-005 | `test_not_equal_enforced` | `misc.yoda_condition` | `!= NULL` also enforced |

---

### 5.7b Whitespace Ratio Rules — `test_whitespace_ratio.py` (27 tests)

| TC-ID | Test Name | Rule Verified | Pass Condition |
|---|---|---|---|
| UV-WSR-001 | `test_disabled_produces_no_violation` | `misc.whitespace_ratio` | No violation when rule disabled |
| UV-WSR-002 | `test_zero_blank_lines_raises_violation` | `misc.whitespace_ratio` | Violation when ratio = 0 |
| UV-WSR-003 | `test_sufficient_blank_lines_passes` | `misc.whitespace_ratio` | No violation when ratio above warning threshold |
| UV-WSR-004 | `test_exactly_at_warning_threshold_passes` | `misc.whitespace_ratio` | No violation at exactly the warning threshold |
| UV-WSR-005 | `test_one_below_warning_threshold_fails` | `misc.whitespace_ratio` | Warning violation when one blank line below threshold |
| UV-WSR-006 | `test_single_violation_emitted_per_file` | `misc.whitespace_ratio` | Exactly one violation emitted per non-compliant file |
| UV-WSR-007 | `test_below_error_threshold_emits_error` | `misc.whitespace_ratio` | Error severity when ratio below error threshold |
| UV-WSR-008 | `test_between_thresholds_emits_configured_severity` | `misc.whitespace_ratio` | Configured severity used when between thresholds |
| UV-WSR-009 | `test_custom_severity_used_between_thresholds` | `misc.whitespace_ratio` | Custom severity key respected |
| UV-WSR-010 | `test_exactly_at_error_threshold_is_warning_not_error` | `misc.whitespace_ratio` | Warning (not error) when exactly at error threshold |
| UV-WSR-011 | `test_fewer_than_min_lines_skipped` | `misc.whitespace_ratio` | No violation when code lines below minimum |
| UV-WSR-012 | `test_exactly_min_lines_is_checked` | `misc.whitespace_ratio` | Checked when code lines equals minimum |
| UV-WSR-013 | `test_custom_min_lines` | `misc.whitespace_ratio` | Custom min_lines config respected |
| UV-WSR-014 | `test_comments_do_not_contribute_to_min_lines` | `misc.whitespace_ratio` | Comment lines excluded from minimum code-line count |
| UV-WSR-015 | `test_blank_lines_in_block_header_not_counted` | `misc.whitespace_ratio` | Header blank lines excluded from ratio |
| UV-WSR-016 | `test_blank_lines_between_header_comments_not_counted` | `misc.whitespace_ratio` | Header region blank lines excluded |
| UV-WSR-017 | `test_blank_lines_in_body_counted_after_header` | `misc.whitespace_ratio` | Body blank lines counted correctly |
| UV-WSR-018 | `test_line_comments_excluded_from_denominator` | `misc.whitespace_ratio` | Line comment lines excluded from code count |
| UV-WSR-019 | `test_block_comments_excluded_from_denominator` | `misc.whitespace_ratio` | Block comment lines excluded from code count |
| UV-WSR-020 | `test_code_line_with_trailing_comment_counts_as_code` | `misc.whitespace_ratio` | Trailing-comment lines count as code |
| UV-WSR-021 | `test_mixed_blanks_and_comments_ratio_correct` | `misc.whitespace_ratio` | Correct ratio when mix of blank, comment, code lines |
| UV-WSR-022 | `test_message_contains_ratio_and_counts` | `misc.whitespace_ratio` | Violation message includes ratio and counts |
| UV-WSR-023 | `test_message_mentions_threshold` | `misc.whitespace_ratio` | Violation message includes threshold value |
| UV-WSR-024 | `test_message_says_error_threshold_when_below_error` | `misc.whitespace_ratio` | Message identifies error threshold when below it |
| UV-WSR-025 | `test_violation_reported_at_line_1` | `misc.whitespace_ratio` | Violation always at line 1 |
| UV-WSR-026 | `test_singular_blank_line_grammar` | `misc.whitespace_ratio` | "1 blank line" (not "1 blank lines") in message |
| UV-WSR-027 | `test_plural_blank_lines_grammar` | `misc.whitespace_ratio` | "N blank lines" (plural) in message |

---

### 5.8 Reserved Names — `test_reserved_name.py` (40 tests)

| TC-ID | Test Name | Rule Verified | Pass Condition |
|---|---|---|---|
| UV-RES-001 | `test_c_keyword_reserved` | `reserved_name` | `int for = 0;` raises violation |
| UV-RES-002 | `test_stdlib_name_reserved` | `reserved_name` | Variable named `printf` raises violation |
| UV-RES-003 | `test_normal_name_passes` | `reserved_name` | `uart_g_count` passes |
| UV-RES-004 | `test_banned_names_extra` | `reserved_name` | Extra banned names via `--banned-names` caught |

---

### 5.9 Spell Check — `test_spell_check.py` (9 tests)

| TC-ID | Test Name | Rule Verified | Pass Condition |
|---|---|---|---|
| UV-SPL-001 | `test_correct_word_passes` | `spell_check` | Known word in dict passes |
| UV-SPL-002 | `test_misspelled_word_fails` | `spell_check` | Unknown word raises violation |
| UV-SPL-003 | `test_possessive_s_stripping` | `spell_check` | `status` not stripped to `statu` (bug fix) |
| UV-SPL-004 | `test_domain_word_exempt` | `spell_check` | `FIFO` in spell dict exempt |

---

### 5.10 Sign Compatibility — `test_sign_compatibility.py` (7 tests)

| TC-ID | Test Name | Rule Verified | Pass Condition |
|---|---|---|---|
| UV-SGN-001 | `test_unsigned_arg_to_signed_param` | `sign_compatibility` | `100U` passed to `int` param raises violation |
| UV-SGN-002 | `test_matching_signs_pass` | `sign_compatibility` | `100U` to `uint32_t` param passes |
| UV-SGN-003 | `test_plain_char_signed_option` | `sign_compatibility` | `plain_char_is_signed: false` changes char treatment |
| UV-SGN-004 | `test_no_global_mutation` | `sign_compatibility` | Second call with different config not affected by first |

---

### 5.11 Dictionary Loading — `test_dictionaries.py` (32 tests)

| TC-ID | Test Name | Unit Verified | Pass Condition |
|---|---|---|---|
| UV-DCT-001 | `test_load_keywords_default` | UNIT-11, UNIT-12 | Built-in keyword file loaded correctly |
| UV-DCT-002 | `test_load_keywords_override` | UNIT-11 | `--keywords-file` replaces built-in |
| UV-DCT-003 | `test_data_file_fallback` | UNIT-12 | Fallback to `sys.prefix/share/cstylecheck/` works |
| UV-DCT-004 | `test_spell_dict_merge` | UNIT-13 | YAML exemptions merged with file dictionary |

---

### 5.12 CLI and Integration — `test_cli.py` (43 tests)

| TC-ID | Test Name | Unit Verified | Pass Condition |
|---|---|---|---|
| UV-CLI-001 | `test_options_file_loaded` | UNIT-02 | Options from file merged before CLI args |
| UV-CLI-002 | `test_cli_overrides_options_file` | UNIT-02 | Direct CLI arg overrides options-file value |
| UV-CLI-003 | `test_exit_code_zero_clean` | UNIT-46 | Exit 0 on clean source |
| UV-CLI-004 | `test_exit_code_one_errors` | UNIT-46 | Exit 1 on errors |
| UV-CLI-005 | `test_exit_code_two_bad_config` | UNIT-46 | Exit 2 on missing config |
| UV-CLI-006 | `test_json_output_valid` | UNIT-38 | JSON output parseable; schema correct |
| UV-CLI-007 | `test_sarif_output_valid` | UNIT-39 | SARIF output parseable |
| UV-CLI-008 | `test_baseline_write_and_load` | UNIT-35, UNIT-36, UNIT-37 | Round-trip: write then suppress |
| UV-CLI-009 | `test_exclude_glob_applied` | UNIT-04 | Excluded files not scanned |
| UV-CLI-010 | `test_version_flag` | UNIT-46 | `--version` outputs version; exit 0 |
| UV-CLI-011 | `TestBaselineSuppression.test_moved_violation_still_suppressed`, `test_key_excludes_line`, `test_baseline_still_records_line` | UNIT-37, UNIT-119 | Violation moved to another line stays suppressed; `line` still written (issue #394) |
| UV-CLI-012 | `TestBaselineSuppression.test_extra_copy_of_baselined_violation_reported`, `test_duplicate_entries_suppress_duplicates`, `test_different_message_not_suppressed`, `test_apply_baseline_does_not_mutate` | UNIT-119 | Multiset matching: one entry suppresses one violation (issue #394) |
| UV-CLI-013 | `TestBaselineSuppression.test_normalise_*`, `test_write_uses_forward_slashes`, `test_windows_baseline_matches_posix_path`, `test_posix_baseline_matches_windows_path` | UNIT-36, UNIT-120 | Paths normalised to `/`; Windows and Linux baselines interchangeable (issue #395) |

---

### 5.13 Bug-Fix and Improvement Tests — `test_improvements.py` (80), `test_barr_c.py` (42), `test_eof_comment.py`, `test_copyright_header.py`, `test_parameter_prefix.py`, `test_exclusions.py`

These test modules provide regression coverage for previously fixed bugs and new rules. Key cases:

| TC-ID | Area | Verified Behaviour |
|---|---|---|
| UV-IMP-001 | Possessive stripping bug | `status` not mangled to `statu` |
| UV-IMP-002 | `plain_char_is_signed: false` | `char` treated as unsigned without mutation |
| UV-IMP-003 | `_SIGNED_TYPES` mutation | Second call to sign checker unaffected by first |
| UV-IMP-004 | Multi-token typedef regex | `typedef unsigned int UINT_T` correctly detected |
| UV-IMP-005 | `function.min_length` | Previously undocumented; now implemented and tested |

---

### 5.14 MISRA C and Barr-C Rule Tests — `test_misra_rules.py` (160 tests)

Covers four MISRA C:2012/2023 lexical rules, one BUG-004 regression, and the 8 MISRA/Barr-C rules added after v1.6.0 by PRs #391 and #392 (76 tests), and the opt-in policy tests for those rules (UV-MSR-009, 11 tests, #418).
ASPICE traceability: SWE1-MISRA-001 (Rule 7.3), SWE1-MISRA-002 (Rule 7.1), SWE1-MISRA-003 (Rule 4.2), SWE1-MISRA-004 (Rule 4.1), SWE1-109 to SWE1-116 (UNIT-128 to UNIT-135).

| TC-ID | MISRA Rule | SWE4 Test ID range | Verified Behaviour |
|---|---|---|---|
| SWE4-TC-7.3-001 to 7.3-015 | Rule 7.3 (lowercase `l`) | 15 tests | Flags `1l`, `0xFFl`, `1ul`; passes `1L`, `1UL`, `0xFFL` |
| SWE4-TC-7.1-001 to 7.1-016 | Rule 7.1 (octal constants) | 16 tests | Flags `010`, `07`, `0777U`; passes `0`, `0U`, `0x08`, `0.5` |
| SWE4-TC-4.2-001 to 4.2-017 | Rule 4.2 (trigraphs) | 17 tests | Flags all 9 trigraph sequences; passes `??` alone, `?` alone |
| BUG-004-001 to 004-004 | Yoda negative literal | 4 tests | `x == -1` message shows `-1`, not `1` |
| SWE4-TC-4.1-001 to 4.1-012 | Rule 4.1 (non-ASCII source) | 12 tests | Flags non-ASCII bytes, BOM, control chars; passes tab/LF/CR/printable ASCII; exempt_string_literals option works |
| UV-MSR-001 | Rule 15.1 — `TestGotoUsage` | 10 tests | `goto` flagged (start of line, inside `if`, one violation per `goto`); not flagged in comments, strings or identifiers containing `goto`; disabled; severity configurable; message cites the rule (SWE1-109) |
| UV-MSR-002 | Rule 13.4 — `TestAssignmentInCondition` | 16 tests | `=` flagged in `if`, `while`, nested `if` and the `for` condition; `==`, `!=`, `<=`, `>=`, compound assignment, `for` init/increment and strings not flagged; disabled; severity; message (SWE1-110) |
| UV-MSR-003 | Barr-C §3.2 — `TestMultipleStatementsPerLine` | 9 tests | Message cites Barr-C §3.2 only, no MISRA (#408); Two statements (and same-line struct members) flagged; single statement, `for` header and comments not flagged; disabled; severity; message (SWE1-111) |
| UV-MSR-004 | Rule 11.5 — `TestVoidPointer` | 8 tests | `void *` flagged in declarations; typed pointer, `void` return type and comments not flagged; disabled; severity; message (SWE1-112) |
| UV-MSR-005 | Rule 17.2 — `TestRecursiveFunction` | 8 tests | Direct recursion flagged with the function name and rule 17.2 in the message; non-recursive code, `if (` keyword and comments not flagged; disabled; severity (SWE1-113) |
| UV-MSR-006 | Barr-C §5.7 — `TestSizeofType` | 7 tests | `sizeof(primitive)` and `sizeof(*_t)` flagged; `sizeof(var)` and `sizeof(*ptr)` not flagged; disabled; severity; message (SWE1-114) |
| UV-MSR-007 | Style rule (no MISRA citation, #410; opt-in, lowercase only, #412) — `TestBooleanComparison` | 18 tests | `== true`, `== false`, `!= true`, `true == x` and `x == false` flagged when enabled; `flag == TRUE`, `TRUE == flag` and `flag != FALSE` not flagged; not reported when the key or `misc` is absent or with the shipped `src/rules.yml`; reported when enabled explicitly; direct use, negation and comments not flagged; disabled; severity; message (SWE1-115) |
| UV-MSR-008 | Barr-C §8.3 — `TestEmptyElse` | 9 tests | `else {}` flagged; `else` with a comment, non-empty `else`, `else if`, no `else` and comments not flagged; disabled; severity; message (SWE1-116) |
| UV-MSR-009 | Opt-in policy (#418) — `test_optin_*` functions | 11 tests | Each of `misc.goto_usage`, `misc.assignment_in_condition`, `misc.multiple_statements_per_line`, `misc.void_pointer`, `misc.recursive_function`, `misc.sizeof_type` and `misc.empty_else` fires when enabled explicitly and is not reported when its key is absent or has no `enabled` flag (7 parametrized tests); all 8 opt-in rules ship `enabled: false` in `src/rules.yml` and `tests/rules.yml`; none of the 8 fires with an empty `misc` config (each fires when enabled); every `misc` rule shipped `enabled: false` reads `.get("enabled", False)` in code; `--update-config` adds the 8 keys as `enabled: false` (SWE1-109 to SWE1-116) |

Each test class verifies: positive detection, negative non-detection, disabled-rule suppression, configurable severity, and violation message content.

### 5.15 Print Summary Per-File Breakdown — `test_print_summary.py` (11 tests)

Added in v1.13. Covers the per-file breakdown extension to `print_summary()` (SWE1-089, issue #278).

| TC-ID | Test Name | Verified Behaviour |
|---|---|---|
| UV-SUM-001 | `test_per_file_section_present` | Output contains "Per-file breakdown" header |
| UV-SUM-002 | `test_files_with_errors_count` | Unique files with errors counted correctly |
| UV-SUM-003 | `test_files_with_warnings_count` | Files with warnings (no errors) in own bucket |
| UV-SUM-004 | `test_files_clean_count` | Files with no violations shown as clean |
| UV-SUM-005 | `test_all_clean` | Zero violations: all files clean |
| UV-SUM-006 | `test_file_counted_once_highest_severity` | File with errors+warnings counted only under errors |
| UV-SUM-007 | `test_no_files_checked_no_breakdown` | No breakdown section emitted when files_checked = 0 |
| UV-IMP-006 | `function.static_prefix` | `prv_` prefix enforced on static functions |
| UV-IMP-007 | `constant.min_length` / `macro.min_length` | Previously undocumented; now implemented |
| UV-IMP-008 | Baseline suppression | Known violations suppressed; new ones reported |

### 5.16 Trend-Analysis C Source Metrics — `test_collect_metrics.py` (54 tests)

Added for issue #388. Covers the pure-Python C source metric helpers in `scripts/collect_metrics.py` and the new charts / wiki rows in `scripts/generate_charts.py` and `scripts/update_wiki_metrics.py` (SWE1-102 to SWE1-108, UNIT-121 to UNIT-127).

| TC-ID | Test Class | Tests | Verified Behaviour |
|---|---|---|---|
| UV-MET-001 | `TestStripCommentsAndStrings` | 7 | Comments/strings blanked, length and newlines preserved, escapes, char literals, preprocessor blanking |
| UV-MET-002 | `TestClassifyLines` | 8 | Blank/comment/doxygen/SLOC classification incl. trailing comments, code after `*/`, comment markers in strings, `/**/` banners, `/*!`/`//!` |
| UV-MET-003 | `TestExtractFunctions` | 7 | Prototypes vs definitions, struct/enum/initialiser exclusion, multi-line signatures, parameter counting, braces in strings/comments, `extern "C"`, macro bodies |
| UV-MET-004 | `TestCyclomaticComplexity` | 5 | V(G) decision points (`if`, else-if, `while`, `do`-`while`, `for`, `case`, `&&`, `\|\|`, `?`); keywords in comments/strings and inside identifiers not counted |
| UV-MET-005 | `TestNesting` | 3 | Flat body = 0, nested blocks, braces in strings ignored |
| UV-MET-006 | `TestDoxygenCoverage` | 2 | `/**`, `/*!`, `///` detected; plain comment / none not counted; blank gap tolerated |
| UV-MET-007 | `TestCoupling` | 5 | Fan-out excludes keywords/`sizeof` and comment text; direct recursion; global/static counting incl. extern, typedef, struct/enum, function pointers, prototypes, function-local statics |
| UV-MET-008 | `TestCSourceMetrics` | 6 | Empty directory → zeros, header-only directory, aggregated sample project, CC histogram buckets, long-function threshold, new keys present, safety counters (`goto_count`, `assert_count`, `macro_count` excluding the include guard — SWE1-117) |
| UV-MET-009 | `TestSummariseViolations` | 4 | Violations by category, files with zero violations, top-5 rules, empty report |
| UV-MET-010 | `TestChartsAndWiki` | 7 | Stacking with missing values, category series for old points, `other` bucket, stacked polygons, chart generation with old/new/mixed points, wiki snapshot rows and tables |

---

### 5.17 CLI Requirement Tests — `test_cli_requirements.py` (21 tests)

Added for issue #407 (closes RR-003-001 in CSC-REVIEW-003 and the remaining part of AUD9-F-004 in CSC-AUD-009). These tests run `main()` in-process so that the file-read path and the output streams can be patched. The path-separator tests replace the `os` module seen by `cli.py` with one whose `path` is `ntpath` or `posixpath`, so both the Windows (`\`) and POSIX (`/`) behaviour are asserted on any CI runner.

| TC-ID | Test Name(s) | SW-REQ | Unit Verified | Pass Condition |
|---|---|---|---|---|
| UV-CLI-014 | `TestSingleReadPerFile.test_each_file_read_once_with_cross_file_sign_check`, `test_sign_checker_ingests_cached_text_for_every_file` | SWE1-015 | UNIT-46, UNIT-80 | 3-file run with a cross-file `sign_compatibility` violation: each file is read exactly once (`Path.read_text` and `open()` counted); `SignChecker.ingest()` receives the cached text of every file |
| UV-CLI-015 | `test_read_once_with_declared_not_defined_and_dry_run_fix`, `test_read_once_when_sign_check_disabled` | SWE1-015 | UNIT-46 | The other cache consumers (`declared_not_defined`, `--fix --dry-run`) add no reads; with `sign_compatibility` disabled nothing is ingested and each file is still read once |
| UV-CLI-016 | `test_unreadable_file_not_retried_or_ingested`, `test_counter_detects_a_second_read` | SWE1-015 | UNIT-46 | Negative: a missing file is attempted once, reported as `ERROR: Cannot read` and not passed to `SignChecker`; the read counter detects a second read (guards against a vacuous pass) |
| UV-CLI-017 | `TestStartupBanner.test_banner_on_stderr_not_stdout`, `test_banner_emitted_when_stdout_piped`, `test_banner_written_to_log_file` | SWE1-094 | UNIT-46 | Subprocess run: version string and copyright on `stderr`, neither on `stdout`, which still carries the violation report; with stdout piped (not a TTY) the first two `stderr` lines are still the banner; with `--log` the log file starts with the same two lines |
| UV-CLI-018 | `test_banner_content`, `test_banner_precedes_processing`, `test_banner_is_exactly_two_lines`, `test_copyright_line_format` | SWE1-094, SWE1-095 | UNIT-46 | `stderr` starts with `CStyleCheck <version>`; on a clean run `stderr` is exactly `CStyleCheck <version>\n(C) 2026 Dermot Murphy\n`; line 2 matches `^\(C\) \d{4} Dermot Murphy$`; with `--verbose` the banner precedes `Found N file(s)` and `Scanning:`; `--version` exits 0 and stdout is exactly `CStyleCheck <version>` then `(C) <year> <holder>` (`(C) 2026 Dermot Murphy`) on its own line (SWE1-095) |
| UV-CLI-019 | `test_json_stdout_not_polluted_by_banner`, `test_structured_log_file_has_no_banner`, `test_no_quiet_option`, `test_version_flag_writes_no_stderr_banner` | SWE1-094 | UNIT-46 | Negative: `--output-format json` stdout parses as JSON (no banner); with `json` / `sarif` / `html` and `--log`, the log file is the stdout document with no banner (#439); `--quiet` is rejected (exit 2), so no option suppresses the banner; `--version` writes to stdout and nothing to stderr |
| UV-CLI-020 | `TestOsPathSeparator.test_windows_backslash_separator`, `test_windows_mixed_separators_normalised` | SWE1-096 | UNIT-03, UNIT-41, UNIT-42 | With `ntpath`: `src/drv/./uart.c` and `src/drv\uart.c` → `src\drv\uart.c`; `Violation.__str__()` and `github_annotation()` use `\` only |
| UV-CLI-021 | `test_posix_forward_slash_separator` | SWE1-096 | UNIT-03, UNIT-41, UNIT-42 | With `posixpath`: `src//drv/./uart.c` → `src/drv/uart.c`; no `\` in the output |
| UV-CLI-022 | `test_emitted_paths_use_host_os_sep`, `test_violation_str_does_not_rewrite_path` | SWE1-096 | UNIT-03, UNIT-41, UNIT-46 | End-to-end on the host OS: reported paths equal `os.path.join(...)` of the file; negative: `Violation.__str__()` renders an already-normalised path verbatim |


### 5.18 Config Wizard and Presets — `test_init_wizard.py` (33 tests)

Tests for `--init` and `--preset` (issue #190). UV-WIZ-004 and UV-WIZ-005 were added for issue #420 (presets and the wizard enable the standard-specific opt-in rules). They use one C snippet that triggers all 8 opt-in rules.

| TC-ID | Test Name(s) | SW-REQ | Unit Verified | Pass Condition |
|---|---|---|---|---|
| UV-WIZ-001 | `TestRunPreset` (8 tests) | SWE1-075 | UNIT-99 | Each preset writes a file; every preset is valid YAML with the header comment; unknown preset → 1; existing file kept without `overwrite`, replaced with it |
| UV-WIZ-002 | `TestRunWizard` (5 tests) | SWE1-075 | UNIT-98 | All-default answers write a file; the `camelCase` answer is stored as canonical `camel` (#422); existing file: `n` aborts (1, file kept), `y` or `overwrite=True` replaces it |
| UV-WIZ-003 | `TestCLIInit` (2 tests) | SWE1-075 | UNIT-46, UNIT-99 | `--preset minimal --init-output` writes the file (exit 0); `--help` lists the three presets |
| UV-WIZ-004 | `TestPresetOptInRules` (9 tests) | SWE1-075 | UNIT-99 | `misra` enables exactly `goto_usage`, `assignment_in_condition`, `void_pointer`, `recursive_function`, `empty_else`; `barr-c` exactly `multiple_statements_per_line`, `sizeof_type`, `empty_else`; `minimal` none; `boolean_comparison` in no preset; each enabled rule written `enabled: true` with the `src/rules.yml` severity; output byte-identical across runs; the checker (in-process and via the CLI `--config`) fires exactly the enabled opt-in rules on the trigger snippet and no others, with no traceback |
| UV-WIZ-005 | `TestWizardOptInRules` (9 tests) | SWE1-075 | UNIT-98 | The MISRA C:2012 and Barr-C questions are asked last (prompts 9 and 10) with `[y/N]`; default, explicit `n`/`N` and end of input enable none; `y` to MISRA enables the 5 MISRA rules, `y` to Barr-C the 3 Barr-C rules, both the union (7); the 7 rules are always listed with the shipped severity and `boolean_comparison` is not; the checker fires exactly the enabled rules |

### 5.19 Case-Style Names in Configs — `test_case_style_config.py` (27 tests)

Added for issue #422. Presets and the wizard write canonical case-style names; aliases are normalised at config load; an unknown case style is a config error (exit 2). Before #422 `matches_case()` returned `True` for an unknown style, so configs generated by `--preset barr-c` or the wizard silently skipped naming checks.

| TC-ID | Test Name(s) | SW-REQ | Unit Verified | Pass Condition |
|---|---|---|---|---|
| UV-CASE-001 | `TestGeneratedConfigsUseCanonicalNames` (7 tests) | SWE1-075 | UNIT-98, UNIT-99 | Every `case` / `*_case` value in the `misra`, `barr-c` and `minimal` presets and in the wizard output for each naming choice is a key of `_CASE_PATTERNS`; `barr-c` writes `lower_snake` typedef / enum type and `upper_snake` members; the wizard labels (`lower_snake`, `camelCase`, `PascalCase`) keep their order and map to `lower_snake` / `camel` / `pascal`, prefix answers included; every generated config passes `validate_case_styles()` |
| UV-CASE-002 | `TestAliasNormalisation` (7 tests) | SWE1-001 | UNIT-05, UNIT-43, UNIT-44 | Each alias (`PascalCase`, `Pascal`, `pascal_case`, `camelCase`, `camel_case`, `UPPER_SNAKE`, `UPPER_SNAKE_CASE`, `SCREAMING_SNAKE`, `SCREAMING_SNAKE_CASE`, `snake_case`, `lower_snake_case`, `snake`) normalises, ignoring letter case; `lower` / `upper` stay distinct styles; `matches_case()` accepts aliases and raises `ValueError` for an unknown style; `validate_case_styles()` and `load_config()` rewrite aliases in place, including per-scope keys and `functions.style` |
| UV-CASE-003 | `TestUnknownCaseStyleIsConfigError` (6 tests) | SWE1-002 | UNIT-05, UNIT-100 | An unknown value in each of the 14 case-style keys gives one error naming the key, the value and the allowed values; unknown `functions.style`, `file_prefix.case`, `misc.eof_comment.filename_case` and a non-string value are rejected; `load_config()` exits 2; the CLI exits 2 with the key in the message and no traceback, also for a per-directory `.cstylecheck.yml` |
| UV-CASE-004 | `TestRepoConfigsValidate` (4 tests) | SWE1-001, SWE1-002 | UNIT-05 | `src/rules.yml`, `tests/rules.yml`, the `examples/embedded_project/config/*.yml` files and every parseable YAML snippet in `README.md` and `Rules-and-Configuration.md` validate with no error |
| UV-CASE-005 | `TestGeneratedConfigReportsWrongCase` (3 tests) | SWE1-040, SWE1-041, SWE1-075 | UNIT-26, UNIT-27, UNIT-43 | End to end via the CLI: a `--preset barr-c` config reports `typedef.case`, `enum.type_case` and `enum.member_case` for wrongly-cased names (exit 1); correctly named `lower_snake_t` types and `UPPER_SNAKE` members pass; a legacy `PascalCase` / `UPPER_SNAKE` config is now enforced (`must be pascal`, `must be upper_snake`) |

### 5.20 `functions.case` Removed — `test_functions_case_removed.py` (16 tests)

Added for issue #424. `functions.case` was written by the presets and the wizard but never read by the checker; function-name casing is set by `functions.style`. The key is no longer generated, is not a case-style key, and a config that still contains it loads with a `WARNING` on `stderr` and an unchanged exit code.

| TC-ID | Test Name(s) | SW-REQ | Unit Verified | Pass Condition |
|---|---|---|---|---|
| UV-FCASE-001 | `TestGeneratedConfigsOmitFunctionsCase` (4 tests) | SWE1-075 | UNIT-98, UNIT-99 | The `misra`, `barr-c` and `minimal` presets (via `run_preset()` and `--preset … --init-output`), the wizard output for each naming choice, `src/rules.yml`, `tests/rules.yml`, `scripts/metrics_rules.yml` and the `examples/embedded_project/config/*.yml` files contain no `functions.case` |
| UV-FCASE-002 | `TestFunctionsCaseDeprecated` (4 tests) | SWE1-001 | UNIT-05 | `functions.case` is not in `_CASE_STYLE_KEYS` (`functions.object_case` / `functions.verb_case` still are) and is in `_DEPRECATED_KEYS`; `validate_case_styles()` returns no error for any value and leaves it untouched; `deprecated_key_warnings()` gives one message naming the file, `'functions.case'`, "not used" and `functions.style`, and nothing when the key is absent |
| UV-FCASE-003 | `TestFunctionsCaseWarning` (4 tests) | SWE1-001 | UNIT-05, UNIT-100 | `load_config()` prints `WARNING:` with the key and `functions.style` to `stderr` and keeps the value; the warning is printed once per file; via the CLI a root config with `functions.case` gives the same exit code as without it and one `WARNING` on `stderr` (none on `stdout`); a per-directory `.cstylecheck.yml` walked for two source directories warns once, no exit 2 |
| UV-FCASE-004 | `TestFunctionStyleStillEnforced` (4 tests) | SWE1-032 | UNIT-24 | `functions.style: lower_snake` reports `function.style` for `uart_ReadByte` and passes `uart_read_byte`; `object_verb` reports `uart_read_byte`; adding `functions.case` (`upper_snake`, `pascal`, `lower_snake`) does not change the findings |

### 5.21 Config-Error Exit Code on Both Entry Points — `test_exit_code_entry_points.py` (8 tests)

Added for issue #425. Config and usage errors called `sys.exit("message")`, which exits with code 1; only the `src/cstylecheck.py` wrapper converted it to 2, so the installed `cstylecheck` console script exited 1. The tests run each error path through the console-script target read from `[project.scripts]` in `pyproject.toml` (invoked as the generated script does, `sys.exit(main())`) and through `python src/cstylecheck.py`.

| TC-ID | Test Name(s) | SW-REQ | Unit Verified | Pass Condition |
|---|---|---|---|---|
| UV-EXIT-001 | `TestConfigErrorHelper` (2 tests) | SWE1-002, SWE1-069 | UNIT-136 | `EXIT_CONFIG_ERROR` is 2; `config_error()` writes the message unchanged to stderr and raises `SystemExit(2)` |
| UV-EXIT-002 | `TestMainMapsStringExitToTwo` (3 tests) | SWE1-069 | UNIT-46 | A `SystemExit` with a string code raised inside `main()` is re-raised as code 2 with the message on stderr; integer codes 0, 1 and 2 and a normal return value pass through unchanged |
| UV-EXIT-003 | `TestConfigErrorsExitTwoOnBothEntryPoints` (3 tests; 20 subtests) | SWE1-002, SWE1-069 | UNIT-01, UNIT-02, UNIT-05, UNIT-06, UNIT-35, UNIT-46, UNIT-52, UNIT-136 | Through both entry points, a missing config, malformed YAML, a non-UTF-8 config, an unknown case style, an unreadable baseline, a missing aliases file, a missing options file, `--options-file` without a path and a copyright file without a block comment each exit 2 with the message on stderr; both entry points give the same exit code and stderr; a naming violation still exits 1 |

### 5.22 Output-File Parent Folders — `test_output_dirs.py` (11 tests)

Added for issue #441. `--log`, `--write-baseline` and `--init-output` (with `--init` / `--preset`) failed with a configuration error when the folder of the output file did not exist. The tests write each output file into nested folders that do not exist, and check that a folder that cannot be created (a path component that is an existing file) is still a configuration error.

| TC-ID | Test Name(s) | SW-REQ | Unit Verified | Pass Condition |
|---|---|---|---|---|
| UV-OUT-001 | `TestLogFolderCreated` (3 tests) | SWE1-062 | UNIT-46, UNIT-137 | `--log out/a/b/results.log` creates the missing folders and writes the log (same content as stdout); an existing folder and a bare file name in the current folder still work |
| UV-OUT-002 | `TestBaselineFolderCreated` (2 tests) | SWE1-065 | UNIT-36, UNIT-137 | `write_baseline()` and `--write-baseline` create the missing folders and write a JSON object with a `violations` array |
| UV-OUT-003 | `TestConfigOutputFolderCreated` (3 tests) | SWE1-075 | UNIT-98, UNIT-99, UNIT-137, UNIT-138 | `run_preset()`, `run_wizard()` and `--preset … --init-output` create the missing folders and write the config |
| UV-OUT-004 | `TestUncreatableFolder` (3 tests) | SWE1-062, SWE1-065, SWE1-075 | UNIT-36, UNIT-46, UNIT-136, UNIT-138 | Negative: when a parent is an existing file, `--log`, `--write-baseline` and `--preset --init-output` each exit 2 with `Cannot open log file` / `Cannot write baseline file` / `Cannot write config file` on stderr and no traceback |

---

## 6. Verification Results Summary

| Test Module | Tests | Pass | Fail | Coverage Contribution |
|---|---|---|---|---|
| `test_variables.py` | 43 | 43 | 0 | `_check_variables` |
| `test_functions.py` | 14 | 14 | 0 | `_check_functions` |
| `test_defines.py` | 30 | 30 | 0 | `_check_defines` (incl. typedef-alias exemption) |
| `test_typedefs.py` | 8 | 8 | 0 | `_check_typedefs` |
| `test_enums.py` | 24 | 24 | 0 | `_check_enums` (UNIT-27, with sub-unit `_enum_members`) |
| `test_structs.py` | 12 | 12 | 0 | `_check_structs` |
| `test_include_guards.py` | 8 | 8 | 0 | `_check_include_guard` |
| `test_misc.py` | 28 | 28 | 0 | `_check_misc` |
| `test_misc_improvements.py` | 77 | 77 | 0 | `_check_misc`, improvements |
| `test_yoda_condition.py` | 46 | 46 | 0 | `_check_yoda` |
| `test_whitespace_ratio.py` | 27 | 27 | 0 | `_check_whitespace_ratio` |
| `test_reserved_name.py` | 40 | 40 | 0 | `_check_reserved_names` |
| `test_spell_check.py` | 9 | 9 | 0 | `_check_spelling` |
| `test_sign_compatibility.py` | 7 | 7 | 0 | `SignChecker` |
| `test_dictionaries.py` | 32 | 32 | 0 | COMP-03 |
| `test_improvements.py` | 80 | 80 | 0 | Multiple |
| `test_barr_c.py` | 42 | 42 | 0 | Multiple |
| `test_cli.py` | 43 | 43 | 0 | COMP-01, COMP-07 |
| `test_exclusions.py` | 28 | 28 | 0 | COMP-02 |
| `test_eof_comment.py` | 33 | 33 | 0 | `_check_eof_comment` |
| `test_copyright_header.py` | 55 | 55 | 0 | `_check_copyright_header` |
| `test_parameter_prefix.py` | 51 | 51 | 0 | `_check_variables` |
| `test_misra_rules.py` | 160 | 160 | 0 | `_check_lowercase_l_suffix`, `_check_octal_constants`, `_check_trigraphs`, `_check_non_ascii_source`, `_check_yoda`, `_check_goto_usage`, `_check_assignment_in_condition`, `_check_multiple_statements_per_line`, `_check_void_pointer`, `_check_recursive_function`, `_check_sizeof_type`, `_check_boolean_comparison`, `_check_empty_else` |
| `test_block_comment_spacing.py` | 29 | 29 | 0 | `_check_block_comment_spacing` |
| `test_workflow_config.py` | 16 | 16 | 0 | CI workflow configuration regression |
| `test_github_annotations.py` | 8 | 8 | 0 | GitHub Actions annotation output |
| `test_case_patterns.py` | 6 | 6 | 0 | Case pattern matching (`_check_case_patterns`) |
| `test_case_style_config.py` | 27 | 27 | 0 | COMP-02 (UNIT-05 `load_config` with sub-unit `validate_case_styles`), COMP-05 (UNIT-43 `matches_case` with sub-unit `normalize_case_style`), COMP-09 (`PRESETS`, `run_wizard`) |
| `test_functions_case_removed.py` | 16 | 16 | 0 | COMP-02 (UNIT-05 `load_config` with sub-units `deprecated_key_warnings` and `validate_case_styles`, `resolve_per_dir_config`), COMP-05 (`_check_functions`), COMP-09 (`PRESETS`, `run_wizard`) |
| `test_exit_code_entry_points.py` | 8 | 8 | 0 | COMP-01 (`main` string-exit mapping, console-script and wrapper entry points), `utils.config_error` |
| `test_output_dirs.py` | 11 | 11 | 0 | COMP-01 (`main` `--log`), `baseline.write_baseline`, `wizard._write_config`, `utils.ensure_parent_dir` |
| `test_thread_safe_globals.py` | 4 | 4 | 0 | Thread-safe global state (`C_KEYWORDS`, `C_STDLIB_NAMES`) |
| `test_preprocessor.py` | 76 | 76 | 0 | COMP-04 (`preprocessor.py`) — strip_comments, strip_strings, preprocess, build_line_map, brace depths, extract_comments |
| `test_comment_ratio.py` | 24 | 24 | 0 | `_check_comment_ratio` |
| `test_declared_not_defined.py` | 39 | 39 | 0 | `DeclaredNotDefinedChecker` |
| `test_config_loading.py` | 13 | 13 | 0 | COMP-02 (`load_config` — UTF-8, missing file, YAML errors; error message captured by patching `config_error`, #425) |
| `test_update_config.py` | 27 | 27 | 0 | COMP-02 (`_deep_merge`) |
| `test_inline_suppression.py` | 24 | 24 | 0 | COMP-04 (`parse_inline_suppressions`) |
| `test_fix_mode.py` | 11 | 11 | 0 | COMP-08 (`apply_fixes`, `unified_diff`) |
| `test_init_wizard.py` | 33 | 33 | 0 | COMP-09 (`run_wizard`, `run_preset`, `PRESETS`) |
| `test_per_dir_config.py` | 15 | 15 | 0 | COMP-10 (`resolve_per_dir_config`) |
| `test_html_report.py` | 20 | 20 | 0 | COMP-07 (`_violations_to_html`) |
| `test_function_length.py` | 11 | 11 | 0 | COMP-05f (`_check_function_length`) |
| `test_function_doc_header.py` | 12 | 12 | 0 | COMP-05f (`_check_function_doc_header`) |
| `test_assert_density.py` | 8 | 8 | 0 | COMP-05f (`_check_assert_density`) |
| `test_null_statement_comment.py` | 11 | 11 | 0 | COMP-05f (`_check_null_statement_comment`) |
| `test_declaration_spacing.py` | 8 | 8 | 0 | COMP-05f (`_check_declaration_spacing`) |
| `test_file_length.py` | 8 | 8 | 0 | COMP-05f (`_check_file_length`) |
| `test_reserved_header_name.py` | 10 | 10 | 0 | COMP-05f (`_check_reserved_header_name`) |
| `test_macro_trailing_semicolon.py` | 9 | 9 | 0 | COMP-05f (`_check_macro_trailing_semicolon`) |
| `test_macro_multistatement_wrapper.py` | 9 | 9 | 0 | COMP-05f (`_check_macro_multistatement_wrapper`) |
| `test_identifier_length.py` | 10 | 10 | 0 | COMP-05h (`_check_identifier_length`) |
| `test_no_single_char_identifiers.py` | 8 | 8 | 0 | COMP-05h (`_check_no_single_char_identifiers`) |
| `test_print_summary.py` | 11 | 11 | 0 | `output.print_summary` (per-file breakdown) |
| `test_constant_comparison.py` | 27 | 27 | 0 | COMP-05f (`_check_constant_comparison`) |
| `test_unsigned_suffix_signed_params.py` | 15 | 15 | 0 | COMP-05f (`_check_misc` signed-param exemption) |
| `test_pointer_prefix_fix.py` | 20 | 20 | 0 | `fixer._fix_pointer_prefix`, `fixer.fix_pointer_prefix_in_header` |
| `test_collect_metrics.py` | 54 | 54 | 0 | CI metrics scripts (UNIT-121 to UNIT-127) |
| `test_cli_requirements.py` | 22 | 22 | 0 | COMP-01 (`main` source cache and startup banner, `discover_files` path normalisation), COMP-07 (`Violation.__str__`) |
| **Total** | **1557** | **1557** | **0** | All 81 rule IDs covered — 59 modules |

**Statement Coverage (v1.1.0 CI — unit tests excl. subprocess):** 86% (1,694 statements, 243 missed)
**Statement Coverage (v1.5.0 CI — 1183 tests incl. subprocess):** 89.8% (1,694 statements, 172 missed)
**Branch Coverage (v1.5.0 CI — 1183 tests incl. subprocess):** 874 branch points, 96 partial → **87.31% combined statement + branch** ≥ 85% gate ✅ (issue #54 resolved)
**v1.6.0 CI coverage:** to be measured after first CI run (expected ≥ 85% combined gate).

**Static Verification (rules.yml):** PASS

---

## 7. Traceability: SW Requirements → Test Cases

| SW-REQ-ID | Requirement | Unit Test(s) |
|---|---|---|
| SWE1-001, SWE1-002 | YAML configuration load / configuration errors | `test_config_loading.py` (13 tests: missing file, bad YAML, UTF-8/non-UTF-8); `test_cli.py` — UV-CLI-005; case-style normalisation and validation: `test_case_style_config.py` — UV-CASE-002 to UV-CASE-004 (#422); `functions.case` warning: `test_functions_case_removed.py` — UV-FCASE-002, UV-FCASE-003 (#424); exit code 2 from both entry points: `test_exit_code_entry_points.py` — UV-EXIT-001, UV-EXIT-003 (#425) |
| SWE1-003 | `--defines` substitution | `test_cli.py` (`--defines` cases) |
| SWE1-004 | Module alias map | `test_cli.py`, `test_improvements.py` (`--aliases` / `load_alias_file` cases) |
| SWE1-005, SWE1-006 | Per-file / per-identifier exclusions | `test_exclusions.py` — `TestLoadExclusionsFile`, `TestDisabledRulesForFile`, end-to-end classes (28 tests) |
| SWE1-011, SWE1-012 | Comment and string stripping | `test_preprocessor.py` — `TestStripComments`, `TestStripStrings`, `TestPreprocess` |
| SWE1-013 | Line map / offset → (line, col) | `test_preprocessor.py` — `TestBuildLineMap`, `TestOffsetToLineCol` |
| SWE1-014 | Brace-depth array | `test_preprocessor.py` — `TestBuildBraceDepths` |
| SWE1-015 | Single read per file (source cache) | `test_cli_requirements.py` — UV-CLI-014 to UV-CLI-016 (#407); also SIT-011 |
| SWE1-016 | Comment-only line detection | `test_preprocessor.py` — `TestCommentOnlyLines` |
| SWE1-017 to SWE1-029 | Variable rules | UV-VAR-001 to UV-VAR-015 |
| SWE1-030 to SWE1-034 | Function rules | UV-FUN-001 to UV-FUN-007; UV-FCASE-004 (`functions.style` only, #424) |
| SWE1-035 to SWE1-039, SWE1-090 | Constant/macro rules | UV-DEF-001 to UV-DEF-013 |
| SWE1-040 to SWE1-042 | Type rules | UV-TYP-001 to UV-TYP-007; UV-TYP-005a (last enum member, #423); UV-CASE-005 (generated-config typedef / enum case findings, #422) |
| SWE1-043 to SWE1-044 | Include guard rules | UV-INC-001 to UV-INC-005 |
| SWE1-045 to SWE1-050 | Miscellaneous rules | UV-MSC-001 to UV-MSC-007 |
| SWE1-071 | Whitespace ratio | UV-WSR-001 to UV-WSR-027 |
| SWE1-049 | Yoda conditions | UV-YOD-001 to UV-YOD-005 |
| SWE1-051 to SWE1-053 | Sign compatibility | UV-SGN-001 to UV-SGN-004 |
| SWE1-054 to SWE1-055 | Reserved names | UV-RES-001 to UV-RES-004 |
| SWE1-056 | Spell check | UV-SPL-001 to UV-SPL-004 |
| SWE1-007 to SWE1-010 | Dictionary management | UV-DCT-001 to UV-DCT-004 |
| SWE1-065 to SWE1-067, SWE1-100, SWE1-101 | Baseline suppression | UV-CLI-008, UV-CLI-011 to UV-CLI-013; `--write-baseline` parent folders created: UV-OUT-002, UV-OUT-004 (#441) |
| SWE1-068 to SWE1-070 | CLI / entry point | UV-CLI-001 to UV-CLI-010; SWE1-069 config/usage errors exit 2 from the console script and `src/cstylecheck.py`: UV-EXIT-001 to UV-EXIT-003 (#425) |
| SWE1-057 | Plain-text violation format | `test_cli.py` (text-output cases) |
| SWE1-058, SWE1-059 | JSON output | UV-CLI-006; `test_improvements.py` (`test_valid_json`, baseline JSON cases) |
| SWE1-060 | SARIF 2.1.0 output | UV-CLI-007; `test_improvements.py` (`test_version_2_1_0`) |
| SWE1-061 | GitHub annotations | `test_github_annotations.py` (8 tests) |
| SWE1-062 | `Tee` log mirroring (`--log`) | `test_cli.py` — `test_log_file_created`, `test_log_file_contains_output`; parent folders created: `test_output_dirs.py` — UV-OUT-001, UV-OUT-004 (#441) |
| SWE1-063 | `--summary` counts | `test_print_summary.py` |
| SWE1-064 | Verbose progress to stderr | `test_cli.py` — `TestVerboseFlag` |
| SWE1-072 to SWE1-073 | Inline suppression comments (`parse_inline_suppressions`, suppression logic) | `test_inline_suppression.py` |
| SWE1-074 | Auto-fix mode (`apply_fixes`, `unified_diff`) | `test_fix_mode.py` |
| SWE1-075 | Config wizard and presets (`run_wizard`, `run_preset`) | `test_init_wizard.py` — UV-WIZ-001 to UV-WIZ-005; `test_case_style_config.py` — UV-CASE-001, UV-CASE-005 (canonical case names, #422); `test_functions_case_removed.py` — UV-FCASE-001 (no `functions.case`, #424); `test_output_dirs.py` — UV-OUT-003, UV-OUT-004 (output parent folders, #441) |
| SWE1-076 | Per-directory config (`resolve_per_dir_config`) | `test_per_dir_config.py` |
| SWE1-077 | HTML report output (`_violations_to_html`) | `test_html_report.py` |
| SWE1-078 | Function length (`_check_function_length`) | `test_function_length.py` |
| SWE1-079 | Function doc header (`_check_function_doc_header`) | `test_function_doc_header.py` |
| SWE1-080 | Assert density (`_check_assert_density`) | `test_assert_density.py` |
| SWE1-081 | Null statement comment (`_check_null_statement_comment`) | `test_null_statement_comment.py` |
| SWE1-082 | Declaration spacing (`_check_declaration_spacing`) | `test_declaration_spacing.py` |
| SWE1-083 | File length (`_check_file_length`) | `test_file_length.py` |
| SWE1-084 | Reserved header name (`_check_reserved_header_name`) | `test_reserved_header_name.py` |
| SWE1-085 | Macro trailing semicolon (`_check_macro_trailing_semicolon`) | `test_macro_trailing_semicolon.py` |
| SWE1-086 | Macro multistatement wrapper (`_check_macro_multistatement_wrapper`) | `test_macro_multistatement_wrapper.py` |
| SWE1-087 | Identifier length (`_check_identifier_length`) | `test_identifier_length.py` |
| SWE1-088 | No single-char identifiers (`_check_no_single_char_identifiers`) | `test_no_single_char_identifiers.py` |
| SWE1-MISRA-001 | Lowercase `l` suffix (`_check_lowercase_l_suffix`) | `test_misra_rules.py` — SWE4-TC-7.3-001 to 7.3-015 |
| SWE1-MISRA-002 | Octal constants (`_check_octal_constants`) | `test_misra_rules.py` — SWE4-TC-7.1-001 to 7.1-016 |
| SWE1-MISRA-003 | Trigraphs (`_check_trigraphs`) | `test_misra_rules.py` — SWE4-TC-4.2-001 to 4.2-017 |
| SWE1-MISRA-004 | Non-ASCII source characters (`_check_non_ascii_source`) | `test_misra_rules.py` — SWE4-TC-4.1-001 to 4.1-012 |
| SWE1-089 | Per-file breakdown in `print_summary` | `test_print_summary.py` — UV-SUM-001 to UV-SUM-007 |
| SWE1-090 | Typedef-alias `constant.case` exemption in `_check_defines` | `test_defines.py` — UV-DEF-008 to UV-DEF-013 |
| SWE1-091 | misc.constant_comparison (`_check_constant_comparison`) | `test_constant_comparison.py` |
| SWE1-092 | misc.unsigned_suffix signed-parameter argument exemption | `test_unsigned_suffix_signed_params.py` |
| SWE1-093 | variable.pointer_prefix auto-fix | `test_pointer_prefix_fix.py` |
| SWE1-094 | Startup banner to stderr (two lines, unconditional) | `test_cli_requirements.py` — UV-CLI-017 to UV-CLI-019 (#407, extended by #413); also SIT-024. Full: stream, two-line content and copyright format, ordering, piped stdout, `--log` copy (text output only; none for json/sarif/html, #439), no suppression option |
| SWE1-095 | Copyright in `--version` | `test_cli_requirements.py` — UV-CLI-018 (`test_copyright_line_format`: `--version` prints the version line then `(C) <year> <holder>` on its own line); `test_cli.py` — `TestVersionAndHelp` (tool name and exit code); also SIT-024 |
| SWE1-096 | OS-native path separator in output | `test_cli_requirements.py` — UV-CLI-020 to UV-CLI-022 (#407); both `\` (Windows) and `/` (POSIX) behaviour asserted. The separator is applied once by `discover_files()` (`os.path.normpath`, UNIT-03); `Violation.__str__()` renders the path verbatim |
| SWE1-097 | `print_summary()` restructure | `test_print_summary.py` |
| SWE1-098 | `fn_start` line correction | `test_functions.py`, `test_inline_suppression.py` |
| SWE1-099 | Function-pointer typedef exemption | `test_variables.py`, `test_parameter_prefix.py` (`test_fn_ptr_typedef_*`) |
| SWE1-102 | Trend metrics — LOC classification | `test_collect_metrics.py` — UV-MET-001, UV-MET-002, UV-MET-008 |
| SWE1-103 | Trend metrics — cyclomatic complexity / nesting | `test_collect_metrics.py` — UV-MET-003 to UV-MET-005, UV-MET-008 |
| SWE1-104 | Trend metrics — size | `test_collect_metrics.py` — UV-MET-003, UV-MET-008 |
| SWE1-105 | Trend metrics — documentation coverage | `test_collect_metrics.py` — UV-MET-006, UV-MET-008 |
| SWE1-106 | Trend metrics — coupling | `test_collect_metrics.py` — UV-MET-007, UV-MET-008 |
| SWE1-107 | Trend metrics — violation quality | `test_collect_metrics.py` — UV-MET-009 |
| SWE1-108 | Trend metrics — backward-compatible data points, charts, wiki | `test_collect_metrics.py` — UV-MET-008, UV-MET-010 |
| SWE1-109 | misc.goto_usage | `test_misra_rules.py` — UV-MSR-001, UV-MSR-009 |
| SWE1-110 | misc.assignment_in_condition | `test_misra_rules.py` — UV-MSR-002, UV-MSR-009 |
| SWE1-111 | misc.multiple_statements_per_line | `test_misra_rules.py` — UV-MSR-003, UV-MSR-009 |
| SWE1-112 | misc.void_pointer | `test_misra_rules.py` — UV-MSR-004, UV-MSR-009 |
| SWE1-113 | misc.recursive_function | `test_misra_rules.py` — UV-MSR-005, UV-MSR-009 |
| SWE1-114 | misc.sizeof_type | `test_misra_rules.py` — UV-MSR-006, UV-MSR-009 |
| SWE1-115 | misc.boolean_comparison | `test_misra_rules.py` — UV-MSR-007, UV-MSR-009 |
| SWE1-116 | misc.empty_else | `test_misra_rules.py` — UV-MSR-008, UV-MSR-009 |
| SWE1-117 | Trend metrics — safety indicators and macro metrics | `test_collect_metrics.py` — UV-MET-008 (`TestCSourceMetrics`: `goto_count`, `assert_count`, `macro_count` with include guard excluded) |

---

## 8. Review & Approval

| Role | Name | Signature / Electronic Approval | Date |
|---|---|---|---|
| Author | Claude | Approved | 2026-09-29 |
| Technical Reviewer | Dermot Murphy | By merge (CSC-DEV-002 §5.2) | On PR merge |
| Quality Assurance | Dermot Murphy | By merge (CSC-DEV-002 §5.2) | On PR merge |
| Approver | Dermot Murphy | By merge (CSC-DEV-002 §5.2) | On PR merge |

> Approval is given by the owner's merge of the pull request that introduces this revision; the merge commit is the approval record (CSC-DEV-002 §5.2).

> **Note:** This document is under configuration management (SUP.8). Post-approval changes require a change request (SUP.10) and a new document version.
