# Software Detailed Design

*Automotive SPICE® PAM v4.0 | SWE.3 Software Detailed Design and Unit Construction*

---

## 1. Document Identification & Control

| Field | Value | Field | Value |
|---|---|---|---|
| **Document ID** | CSC-SWE3-001 | **Version** | 1.23 |
| **Project** | CStyleCheck | **Date** | 2026-09-29 |
| **Status** | Released | **Classification** | Internal |
| **Author** | Claude | **Reviewer** | Dermot Murphy |
| **Approver** | Dermot Murphy | **Related Process** | SWE.3 |

---

## 2. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.23 | 2026-09-29 | Claude | Issue #412: UNIT-134 algorithm — disabled by default (also when the key is absent), lowercase `true`/`false` only; §6.1 `misc.boolean_comparison.enabled` default `true`→`false`; referenced-document versions resynced (3) |
| 1.22 | 2026-09-29 | Claude | Release-prep cross-reference resync: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.21 | 2026-09-29 | Claude | Issue #413 (CR-413): UNIT-46 step 3 specifies the two-line, unconditional stderr/log banner (SWE1-094); step 5 records the `--fix` header re-read (SWE1-015 exception); §8 SWE1-094 row; referenced-document versions resynced (SWE1 2.9→2.10, SWE2 1.14→1.15, SWE4 1.24→1.25) |
| 1.20 | 2026-09-29 | Claude | Issue #410: UNIT-134 purpose and §6.1 `misc.boolean_comparison` row — style rule; MISRA C:2012 Rule 14.4 citation removed; message suffix "(redundant comparison with a Boolean literal)" |
| 1.19 | 2026-09-29 | Claude | Issue #407: UNIT-03 algorithm records the `os.path.normpath()` step (SWE1-096); UNIT-41 note and §8 SWE1-096 row corrected (separator applied by UNIT-03; `Violation.__str__()` renders the path verbatim); referenced-document versions resynced (SWE1 2.8→2.9, SWE2 1.13→1.14, SWE4 1.22→1.24) |
| 1.18 | 2026-09-29 | Claude | CSC-AUD-009 corrective actions (#405). AUD9-F-002: add UNIT-128 to UNIT-135 (8 new checker methods from #391/#392) to the §4 catalogue, §5 specs and §8 RTM, and add the §6.1 config keys. AUD9-F-007: correct the §6.3 baseline file format to {"violations":[{file,line,rule,message}]}. AUD9-F-010: UNIT-125/127 specify the safety indicators and the safety_indicators/macro_metrics charts; add a SWE1-117 RTM row. AUD9-F-011: UNIT-121 to UNIT-127 component → COMP-13. AUD9-F-012: regenerate every §4 source line reference (43 corrected, 24 added). AUD9-F-013: add §5 specs for the 35 catalogued units that had none (UNIT-06 to UNIT-94). AUD9-F-004: §8 RTM rows for SWE1-062 and SWE1-MISRA-001 to 003. AUD9-F-015: header date. AUD9-F-024: Author and Description columns swapped back in earlier revision rows. AUD9-F-014: referenced-document versions resynced to current revisions |
| 1.17 | 2026-09-29 | Claude | Add UNIT-121 to UNIT-127 (trend-analysis C source metric helpers in `scripts/collect_metrics.py`, stacked charts in `scripts/generate_charts.py`); update §3.1 refs (SWE1 2.6→2.7, SWE4 1.20→1.21); update §8 RTM for SWE1-102 to SWE1-108; also records UNIT-37 revision and UNIT-119/UNIT-120 (baseline, issues #394/#395, PR #397) — issue #388 |
| 1.16 | 2026-07-06 | Claude | ASPICE audit — update scope to v1.6.0; §3.1 refs (SWE1 2.4→2.6, SWE2 1.11→1.12, SWE4 1.17→1.20); add UNIT-116 (_check_constant_comparison), UNIT-117 (_fix_pointer_prefix), UNIT-118 (fix_pointer_prefix_in_header); update UNIT-95 for block-comment form, UNIT-22 run_all order, UNIT-86 Tee; update §8 RTM — closes #373 |
| 1.15 | 2026-06-27 | Dermot Murphy | Fix §3.1 cross-refs: SWE1 2.3→2.4, SWE2 1.9→1.11, SWE4 1.16→1.17 |
| 1.14 | 2026-06-27 | Dermot Murphy | Fix §3.1 cross-refs: SWE1 2.1→2.3, SWE4 1.14→1.16 |
| 1.13 | 2026-06-27 | Claude | ASPICE audit — approve §9 Review & Approval (3 roles were Pending) — closes #316 #323 |
| 1.12 | 2026-06-26 | Claude | ASPICE audit corrections: fix §3 scope text (v1.2.x→v1.5.0); update §3.1 SWE1/SWE4 version refs; correct UNIT-102–113 Component from COMP-01 to COMP-05f/COMP-05h; add _check_non_ascii_source to UNIT-22 run_all() order — closes #308 |
| 1.11 | 2026-06-26 | Claude | Add UNIT-113 (_check_non_ascii_source), UNIT-114 (print_summary per-file breakdown), UNIT-115 (_check_defines typedef-alias exemption); update §8 traceability — issues #279 #278 #272 #244 |
| 1.10 | 2026-06-18 | Claude | ASPICE audit #254 — sync referenced-document version citations to current versions |
| 1.9 | 2026-06-08 | Claude | Add UNIT-102 to UNIT-112 for 11 new rules (issues #221–#232); update §8 traceability |
| 1.8 | 2026-06-05 | Claude | CSC-AUD-005 corrective action — fix factual errors identified in audit |
| 1.6 | 2026-06-04 | Claude | Add UNIT-95 to UNIT-101 for five new features (inline suppression, fixer, wizard, per-dir config, HTML output); update §4.1 package structure; update §8 traceability — issues #188 #189 #190 #193 #192 |
| 1.5 | 2026-06-04 | Claude | Deep accuracy audit: correct 48 stale line numbers, add 4 missing config.py units (UNIT-91 to UNIT-94), update §4.1 package structure, update §3.1 referenced doc versions — resolves issue #163 |
| 1.4 | 2026-06-04 | Claude | Automated accuracy audit: update referenced doc versions in §3.1 — resolves issue #163 |
| 1.3 | 2026-05-28 | Claude | Update all 89 Source Location values to reflect package refactor (issue #144); add UNIT-90 (_check_whitespace_ratio); update §4.1 to show completed refactor; update run_all order — closes issues #146 #147 #148 |
| 1.2 | 2026-05-28 | Claude | Added ~25 units missing from v1.1 (load_spell_words, load_banned_names_file, load_copyright_file, to_case, is_exempt, _cfg, extract_comments, all Checker helper methods, _check_copyright_header, _body_is_object_verb, _check_comment_ratio, _check_lowercase_l_suffix, _check_octal_constants, _check_trigraphs, _is_reserved, _check_name_reserved, _ParamSig, _FuncSig, sign-checker helpers, SignChecker, DeclaredNotDefinedChecker, _strip_module_prefix, Tee, parse_args, _build_parser, _github_annotation_category, _is_constant_token, _is_variable_token). Updated all source line numbers to match v1.2.x source. Added Section 4.1 Target Package Structure documenting planned refactor (issue #65). Updated purpose to reference v1.2.x. |
| 1.1 | 2026-05-28 | Claude | Reviewed and updated for v1.1.0 release; revision history maintained per ASPICE GP 2.2.4 |
| 1.0 | 2026-04-12 | Claude | Initial release |

---

## 3. Purpose & Scope

This document defines the detailed design of each software unit (UNIT-01 to UNIT-135) in **CStyleCheck v1.6.0 and the post-v1.6.0 `develop` baseline**, providing the algorithmic specification, interface contracts, and data design required for unit construction and verification. It satisfies **Automotive SPICE® PAM v4.0, SWE.3 — Software Detailed Design and Unit Construction**.

### 3.1 Referenced Documents

| Document ID | Title | Version |
|---|---|---|
| CSC-SWE1-001 | CStyleCheck Software Requirements Specification | 2.13 |
| CSC-SWE2-001 | CStyleCheck Software Architecture Description | 1.18 |
| CSC-SWE4-001 | CStyleCheck Unit Verification Specification | 1.28 |

---

## 4. Unit Catalogue

All source locations refer to the current package layout under `src/cstylecheck/` (post-package-split, issue #144). The **Target Module** column is now the **actual** module; the old monolithic `src/cstylecheck.py` no longer exists.

| Unit ID | Unit Name | Source Location | Component | Module |
|---|---|---|---|---|
| UNIT-01 | `_read_options_file` | `config.py:30` | COMP-01 | `config.py` |
| UNIT-02 | `_expand_options_file` | `config.py:61` | COMP-01 | `config.py` |
| UNIT-03 | `discover_files` | `cli.py:118` | COMP-01 | `cli.py` |
| UNIT-04 | `_path_matches_exclude` | `cli.py:44` | COMP-01 | `cli.py` |
| UNIT-05 | `load_config` | `config.py:251` | COMP-02 | `config.py` |
| UNIT-06 | `load_alias_file` | `config.py:294` | COMP-02 | `config.py` |
| UNIT-07 | `load_exclusions_file` | `config.py:340` | COMP-02 | `config.py` |
| UNIT-08 | `_disabled_rules_for_file` | `config.py:389` | COMP-02 | `config.py` |
| UNIT-09 | `load_defines_file` | `config.py:418` | COMP-02 | `config.py` |
| UNIT-10 | `apply_defines` | `config.py:467` | COMP-02 | `config.py` |
| UNIT-11 | `_load_dict_file` | `config.py:484` | COMP-03 | `config.py` |
| UNIT-12 | `_data_file` | `config.py:503` | COMP-03 | `config.py` |
| UNIT-13 | `_build_spell_dict` | `config.py:642` | COMP-03 | `config.py` |
| UNIT-14 | `strip_comments` | `preprocessor.py:19` | COMP-04 | `preprocessor.py` |
| UNIT-15 | `strip_strings` | `preprocessor.py:29` | COMP-04 | `preprocessor.py` |
| UNIT-16 | `preprocess` | `preprocessor.py:44` | COMP-04 | `preprocessor.py` |
| UNIT-17 | `build_line_map` | `preprocessor.py:202` | COMP-04 | `preprocessor.py` |
| UNIT-18 | `offset_to_line_col` | `preprocessor.py:209` | COMP-04 | `preprocessor.py` |
| UNIT-19 | `_build_brace_depths` | `preprocessor.py:182` | COMP-04 | `preprocessor.py` |
| UNIT-20 | `_comment_only_lines` | `preprocessor.py:48` | COMP-04 | `preprocessor.py` |
| UNIT-21 | `Checker.__init__` | `checker.py:173` | COMP-05 | `checker.py` |
| UNIT-22 | `Checker.run_all` | `checker.py:323` | COMP-05 | `checker.py` |
| UNIT-23 | `Checker._check_variables` | `checker.py:463` | COMP-05a | `checker.py` |
| UNIT-24 | `Checker._check_functions` | `checker.py:969` | COMP-05b | `checker.py` |
| UNIT-25 | `Checker._check_defines` | `checker.py:384` | COMP-05c | `checker.py` |
| UNIT-26 | `Checker._check_typedefs` | `checker.py:1067` | COMP-05d | `checker.py` |
| UNIT-27 | `Checker._check_enums` | `checker.py:1091` | COMP-05d | `checker.py` |
| UNIT-28 | `Checker._check_structs` | `checker.py:1155` | COMP-05d | `checker.py` |
| UNIT-29 | `Checker._check_include_guard` | `checker.py:1297` | COMP-05e | `checker.py` |
| UNIT-30 | `Checker._check_misc` | `checker.py:1330` | COMP-05f | `checker.py` |
| UNIT-31 | `Checker._check_yoda` | `checker.py:2038` | COMP-05f | `checker.py` |
| UNIT-32 | `Checker._check_reserved_names` | `checker.py:2755` | COMP-05f | `checker.py` |
| UNIT-33 | `Checker._check_spelling` | `checker.py:2019` | COMP-05f | `checker.py` |
| UNIT-34 | `SignChecker._check_calls` | `sign_checker.py:273` | COMP-05g | `sign_checker.py` |
| UNIT-35 | `load_baseline` | `baseline.py:47` | COMP-06 | `baseline.py` |
| UNIT-36 | `write_baseline` | `baseline.py:85` | COMP-06 | `baseline.py` |
| UNIT-37 | `_baseline_key` | `baseline.py:36` | COMP-06 | `baseline.py` |
| UNIT-38 | `_violations_to_json` | `output.py:47` | COMP-07 | `output.py` |
| UNIT-39 | `_violations_to_sarif` | `output.py:79` | COMP-07 | `output.py` |
| UNIT-40 | `print_summary` | `output.py:269` | COMP-07 | `output.py` |
| UNIT-41 | `Violation.__str__` | `models.py:59` | COMP-07 | `models.py` |
| UNIT-42 | `Violation.github_annotation` | `models.py:45` | COMP-07 | `models.py` |
| UNIT-43 | `matches_case` | `utils.py:48` | COMP-05 (shared) | `utils.py` |
| UNIT-44 | `matches_case_abbrev` | `utils.py:53` | COMP-05 (shared) | `utils.py` |
| UNIT-45 | `module_name` | `utils.py:84` | COMP-05 (shared) | `utils.py` |
| UNIT-46 | `main` | `cli.py:367` | Entry point | `cli.py` |
| UNIT-47 | `append_trend_record` (script) | `scripts/ci/append_trend_record.py` | CI script | (unchanged) |
| UNIT-48 | `generate_trend` (script) | `scripts/ci/generate_trend.py` | CI script | (unchanged) |
| UNIT-49 | `update_readme_badge` (script) | `scripts/ci/update_readme_badge.py` | CI script | (unchanged) |
| UNIT-50 | `load_spell_words` | `config.py:277` | COMP-02 | `config.py` |
| UNIT-51 | `load_banned_names_file` | `config.py:540` | COMP-02 | `config.py` |
| UNIT-52 | `load_copyright_file` | `config.py:575` | COMP-02 | `config.py` |
| UNIT-53 | `to_case` | `utils.py:75` | COMP-05 (shared) | `utils.py` |
| UNIT-54 | `is_exempt` | `utils.py:88` | COMP-05 (shared) | `utils.py` |
| UNIT-55 | `_cfg` | `utils.py:98` | COMP-05 (shared) | `utils.py` |
| UNIT-56 | `extract_comments` | `preprocessor.py:158` | COMP-04 | `preprocessor.py` |
| UNIT-57 | `Checker._violation` | `checker.py:250` | COMP-05 | `checker.py` |
| UNIT-58 | `Checker._v` | `checker.py:254` | COMP-05 | `checker.py` |
| UNIT-59 | `Checker._prefix` | `checker.py:261` | COMP-05 | `checker.py` |
| UNIT-60 | `Checker._require_module_prefix` | `checker.py:267` | COMP-05 | `checker.py` |
| UNIT-61 | `Checker._depth_at` | `checker.py:300` | COMP-05 | `checker.py` |
| UNIT-62 | `Checker._strip_any_prefix` | `checker.py:305` | COMP-05 | `checker.py` |
| UNIT-63 | `Checker._check_copyright_header` | `checker.py:1196` | COMP-05f | `checker.py` |
| UNIT-64 | `Checker._body_is_object_verb` | `checker.py:937` | COMP-05b | `checker.py` |
| UNIT-65 | `Checker._check_comment_ratio` | `checker.py:1754` | COMP-05f | `checker.py` |
| UNIT-66 | `Checker._check_lowercase_l_suffix` | `checker.py:2269` | COMP-05f | `checker.py` |
| UNIT-67 | `Checker._check_octal_constants` | `checker.py:2307` | COMP-05f | `checker.py` |
| UNIT-68 | `Checker._check_trigraphs` | `checker.py:2346` | COMP-05f | `checker.py` |
| UNIT-69 | `Checker._is_reserved` | `checker.py:2737` | COMP-05f | `checker.py` |
| UNIT-70 | `Checker._check_name_reserved` | `checker.py:2747` | COMP-05f | `checker.py` |
| UNIT-71 | `Checker._is_constant_token` | `checker.py:2151` | COMP-05f | `checker.py` |
| UNIT-72 | `Checker._is_variable_token` | `checker.py:2165` | COMP-05f | `checker.py` |
| UNIT-73 | `_ParamSig` | `models.py:106` | COMP-05g | `models.py` |
| UNIT-74 | `_FuncSig` | `models.py:114` | COMP-05g | `models.py` |
| UNIT-75 | `_classify_tokens` | `sign_checker.py:70` | COMP-05g | `sign_checker.py` |
| UNIT-76 | `_signedness_of_type` | `sign_checker.py:95` | COMP-05g | `sign_checker.py` |
| UNIT-77 | `_classify_arg` | `sign_checker.py:110` | COMP-05g | `sign_checker.py` |
| UNIT-78 | `_extract_call_args` | `sign_checker.py:119` | COMP-05g | `sign_checker.py` |
| UNIT-79 | `SignChecker.__init__` | `sign_checker.py:159` | COMP-05g | `sign_checker.py` |
| UNIT-80 | `SignChecker.ingest` | `sign_checker.py:166` | COMP-05g | `sign_checker.py` |
| UNIT-81 | `SignChecker.check` | `sign_checker.py:169` | COMP-05g | `sign_checker.py` |
| UNIT-82 | `SignChecker._build_typedef_map` | `sign_checker.py:192` | COMP-05g | `sign_checker.py` |
| UNIT-83 | `SignChecker._build_signatures` | `sign_checker.py:231` | COMP-05g | `sign_checker.py` |
| UNIT-84 | `DeclaredNotDefinedChecker` (class) | `sign_checker.py:319` | COMP-05g | `sign_checker.py` |
| UNIT-85 | `_strip_module_prefix` | `utils.py:113` | COMP-05 (shared) | `utils.py` |
| UNIT-86 | `Tee` | `output.py:18` | COMP-07 | `output.py` |
| UNIT-87 | `parse_args` | `cli.py:190` | COMP-01 | `cli.py` |
| UNIT-88 | `_build_parser` | `cli.py:195` | COMP-01 | `cli.py` |
| UNIT-89 | `_github_annotation_category` | `utils.py:21` | COMP-07 | `utils.py` |
| UNIT-90 | `Checker._check_whitespace_ratio` | `checker.py:1892` | COMP-05f | `checker.py` |
| UNIT-91 | `_find_default_rules` | `config.py:93` | COMP-02 | `config.py` |
| UNIT-92 | `_deep_merge` | `config.py:114` | COMP-02 | `config.py` |
| UNIT-93 | `_collect_paths` | `config.py:137` | COMP-02 | `config.py` |
| UNIT-94 | `update_config` | `config.py:148` | COMP-02 | `config.py` |
| UNIT-95 | `parse_inline_suppressions` | `preprocessor.py:77` | COMP-04 | `preprocessor.py` |
| UNIT-96 | `apply_fixes` | `fixer.py:337` | COMP-08 | `fixer.py` |
| UNIT-97 | `unified_diff` | `fixer.py:386` | COMP-08 | `fixer.py` |
| UNIT-98 | `run_wizard` | `wizard.py:155` | COMP-09 | `wizard.py` |
| UNIT-99 | `run_preset` | `wizard.py:253` | COMP-09 | `wizard.py` |
| UNIT-100 | `resolve_per_dir_config` | `config.py:686` | COMP-10 | `config.py` |
| UNIT-101 | `_violations_to_html` | `output.py:182` | COMP-07 | `output.py` |
| UNIT-102 | `_check_function_length` | `checker.py:2953` | COMP-05f | `checker.py` |
| UNIT-103 | `_check_function_doc_header` | `checker.py:2987` | COMP-05f | `checker.py` |
| UNIT-104 | `_check_assert_density` | `checker.py:3081` | COMP-05f | `checker.py` |
| UNIT-105 | `_check_null_statement_comment` | `checker.py:3227` | COMP-05f | `checker.py` |
| UNIT-106 | `_check_declaration_spacing` | `checker.py:3111` | COMP-05f | `checker.py` |
| UNIT-107 | `_check_file_length` | `checker.py:3173` | COMP-05f | `checker.py` |
| UNIT-108 | `_check_reserved_header_name` | `checker.py:3206` | COMP-05f | `checker.py` |
| UNIT-109 | `_check_macro_trailing_semicolon` | `checker.py:2827` | COMP-05b | `checker.py` |
| UNIT-110 | `_check_macro_multistatement_wrapper` | `checker.py:2883` | COMP-05b | `checker.py` |
| UNIT-111 | `_check_identifier_length` | `checker.py:3267` | COMP-05h | `checker.py` |
| UNIT-112 | `_check_no_single_char_identifiers` | `checker.py:3323` | COMP-05h | `checker.py` |
| UNIT-113 | `_check_non_ascii_source` | `checker.py:2372` | COMP-05f | `checker.py` |
| UNIT-114 | `print_summary` (per-file breakdown) | `output.py:269` | COMP-07 | `output.py` |
| UNIT-115 | `_check_defines` (typedef-alias exemption) | `checker.py:384` | COMP-05c | `checker.py` |
| UNIT-116 | `Checker._check_constant_comparison` | `checker.py:2176` | COMP-05f | `checker.py` |
| UNIT-117 | `_fix_pointer_prefix` | `fixer.py:92` | COMP-08 | `fixer.py` |
| UNIT-118 | `fix_pointer_prefix_in_header` | `fixer.py:277` | COMP-08 | `fixer.py` |
| UNIT-119 | `apply_baseline` | `baseline.py:67` | COMP-06 | `baseline.py` |
| UNIT-120 | `_normalise_path` | `baseline.py:23` | COMP-06 | `baseline.py` |
| UNIT-121 | `strip_comments_and_strings` | `scripts/collect_metrics.py` | COMP-13 (Trend-Analysis Scripts) | `scripts/collect_metrics.py` |
| UNIT-122 | `classify_lines` | `scripts/collect_metrics.py` | COMP-13 (Trend-Analysis Scripts) | `scripts/collect_metrics.py` |
| UNIT-123 | `extract_functions` | `scripts/collect_metrics.py` | COMP-13 (Trend-Analysis Scripts) | `scripts/collect_metrics.py` |
| UNIT-124 | `count_file_scope_variables` | `scripts/collect_metrics.py` | COMP-13 (Trend-Analysis Scripts) | `scripts/collect_metrics.py` |
| UNIT-125 | `_c_source_metrics` | `scripts/collect_metrics.py` | COMP-13 (Trend-Analysis Scripts) | `scripts/collect_metrics.py` |
| UNIT-126 | `_summarise_violations` | `scripts/collect_metrics.py` | COMP-13 (Trend-Analysis Scripts) | `scripts/collect_metrics.py` |
| UNIT-127 | `_make_chart` (stacked) / `_stack_series` / `_category_series` | `scripts/generate_charts.py` | COMP-13 (Trend-Analysis Scripts) | `scripts/generate_charts.py` |
| UNIT-128 | `Checker._check_goto_usage` | `checker.py:2425` | COMP-05f | `checker.py` |
| UNIT-129 | `Checker._check_assignment_in_condition` | `checker.py:2456` | COMP-05f | `checker.py` |
| UNIT-130 | `Checker._check_multiple_statements_per_line` | `checker.py:2530` | COMP-05f | `checker.py` |
| UNIT-131 | `Checker._check_void_pointer` | `checker.py:2563` | COMP-05f | `checker.py` |
| UNIT-132 | `Checker._check_recursive_function` | `checker.py:2596` | COMP-05f | `checker.py` |
| UNIT-133 | `Checker._check_sizeof_type` | `checker.py:2649` | COMP-05f | `checker.py` |
| UNIT-134 | `Checker._check_boolean_comparison` | `checker.py:2683` | COMP-05f | `checker.py` |
| UNIT-135 | `Checker._check_empty_else` | `checker.py:2710` | COMP-05f | `checker.py` |

---

## 4.1 Package Structure

Issue #144 completed the refactor of `src/cstylecheck.py` into a Python package. The current layout is:

```
src/cstylecheck/
  __init__.py      — public re-exports, version handling
  models.py        — Violation, CheckResult, _ParamSig, _FuncSig
  preprocessor.py  — strip_comments, strip_strings, preprocess,
                     build_line_map, offset_to_line_col,
                     _build_brace_depths, _comment_only_lines,
                     extract_comments, parse_inline_suppressions
  utils.py         — matches_case, matches_case_abbrev, to_case,
                     module_name, is_exempt, _cfg,
                     _strip_module_prefix, _github_annotation_category
  config.py        — _read_options_file, _expand_options_file,
                     _find_default_rules, _deep_merge, _collect_paths,
                     update_config, load_config, load_spell_words,
                     load_alias_file, load_exclusions_file,
                     _disabled_rules_for_file, load_defines_file,
                     apply_defines, _load_dict_file, _data_file,
                     load_banned_names_file, load_copyright_file,
                     _build_spell_dict, _BUILTIN_DICT,
                     resolve_per_dir_config
  checker.py       — Checker class, all regex patterns (RE_DEFINE,
                     RE_VAR_DECL, RE_FUNCTION_DEF, …), all _check_* methods
  sign_checker.py  — SignChecker, DeclaredNotDefinedChecker,
                     sign-analysis helpers (_classify_tokens,
                     _signedness_of_type, _classify_arg,
                     _extract_call_args)
  baseline.py      — load_baseline, write_baseline, apply_baseline, _baseline_key, _normalise_path
  output.py        — Tee, _violations_to_json, _violations_to_sarif,
                     _violations_to_html, print_summary
  fixer.py         — apply_fixes, unified_diff
  wizard.py        — run_wizard, run_preset
  cli.py           — discover_files, _path_matches_exclude, parse_args,
                     _build_parser, main
```

`_version.py` remains a top-level module in `src/` (not inside the package) because it is generated by the build/CI system independently of the package tree. `_read_options_file` and `_expand_options_file` reside in `config.py` (not `cli.py`) in the current implementation.

**Dependency order (no circular imports):**

1. `models.py` — stdlib only
2. `preprocessor.py` — stdlib only
3. `utils.py` — stdlib only
4. `config.py` — imports from `preprocessor`, `utils`, `models`
5. `checker.py` — imports from `models`, `preprocessor`, `utils`, `config`
6. `sign_checker.py` — imports from `models`, `preprocessor`, `checker` (regex patterns)
7. `baseline.py` — imports from `models`
8. `output.py` — imports from `models`
9. `cli.py` — imports from all of the above
10. `__init__.py` — imports from all sub-modules; re-exports the public API

**Backward-compatibility guarantee:** `__init__.py` re-exports every name that was previously at module level in `cstylecheck.py`. The CLI entry point (`cstylecheck = "cstylecheck:main"` in `pyproject.toml`) and the test harness (`import cstylecheck as _mod`) continue to work without modification.

---

## 5. Detailed Unit Design

### UNIT-01 — `_read_options_file(path: str) → list`

**Purpose:** Read an options file and return a flat list of shell-tokenised CLI arguments.

**Algorithm:**
1. Open file at `path`; read all lines
2. For each line: strip whitespace; skip if empty or starts with `#`
3. Apply `shlex.split()` to tokenise shell-quoted values
4. Return concatenated token list

**Error handling:** `FileNotFoundError` → caller receives empty list (non-fatal); `ValueError` (shlex parse error) → emit warning to stderr

**Constraints:** Must not modify `sys.argv` directly

---

### UNIT-02 — `_expand_options_file(argv: list) → list`

**Purpose:** Insert tokens from `--options-file FILE` before remaining argv tokens.

**Algorithm:**
1. Scan `argv` for `--options-file` token (or `--options-file=FILE` form)
2. If found: extract `FILE`; call `_read_options_file(FILE)` → `opts_tokens`
3. Return: `argv_before_flag + opts_tokens + argv_after_flag`
4. If not found: return `argv` unchanged

**Key constraint:** Direct CLI args must follow options-file args to allow override (SWE1-068)

---

### UNIT-03 — `discover_files(includes, excludes) → list[str]`

**Purpose:** Expand glob patterns into a de-duplicated, sorted list of source file paths, applying exclusions.

**Algorithm:**
1. For each include glob: call `glob_mod.glob(pattern, recursive=True)` → file list
2. Filter: keep only `.c` and `.h` files
3. For each file: check `_path_matches_exclude(filepath, excludes)` → discard if True
4. De-duplicate using `dict.fromkeys()` (preserves order)
5. Return sorted list
6. Each path is yielded through `os.path.normpath()`, so it carries the OS-native separator in all later output (SWE1-096; verified by UV-CLI-020 to UV-CLI-022)

---

### UNIT-04 — `_path_matches_exclude(filepath: str, exclude_globs: list) → bool`

**Purpose:** Return `True` if the filepath matches any exclude glob pattern.

**Algorithm:** For each glob in `exclude_globs`: if `fnmatch.fnmatch(filepath, glob)` or `glob in filepath` → return `True`. Return `False`.

---

### UNIT-05 — `load_config(path: str) → dict`

**Purpose:** Load and return the YAML configuration as a Python dictionary.

**Algorithm:**
1. Open `path`; call `yaml.safe_load()`
2. If result is `None` or not a `dict` → `sys.exit(2)` with message
3. Return config dict

---

### UNIT-10 — `apply_defines(text: str, defines: list) → str`

**Purpose:** Substitute project-specific keywords and type aliases before rule checking.

**Algorithm:**
1. For each `(pattern, replacement)` pair in `defines`: apply `re.sub(pattern, replacement, text)`
2. Return substituted text

**Design note:** Substitutions are applied in definition-file order; order matters for overlapping patterns.

---

### UNIT-14 — `strip_comments(source: str) → str`

**Purpose:** Replace C block (`/* */`) and line (`//`) comments with whitespace, preserving line numbers.

**Algorithm:**
1. Use a state-machine regex scan over `source`
2. For each block comment: replace content with spaces (preserve newlines)
3. For each line comment: replace from `//` to end-of-line with spaces
4. Return result with identical line count to input

**Constraint:** Must not alter line count; `build_line_map` depends on unchanged newline positions.

---

### UNIT-16 — `preprocess(source: str) → str`

**Purpose:** Produce clean source text suitable for regex-based rule checks.

**Algorithm:**
1. Call `strip_comments(source)` → comment-free text
2. Call `strip_strings(result)` → string-literal-free text
3. Return result

---

### UNIT-19 — `_build_brace_depths(clean: str) → list[int]`

**Purpose:** Build a per-character brace-depth array used to determine identifier scope.

**Algorithm:**
1. Initialise `depth = 0`; `depths = []`
2. For each character `ch` in `clean`:
   - If `ch == '{'`: append current depth; increment depth
   - If `ch == '}'`: decrement depth; append current depth
   - Else: append current depth
3. Return `depths`

**Usage:** `depths[pos] == 0` → global scope; `depths[pos] == 1` → file-scope static; `depths[pos] > 1` → local scope

---

### UNIT-21 — `Checker.__init__(...)`

**Purpose:** Initialise the checker for a single source file.

**Algorithm:**
1. Store `filepath`, `source`, `cfg`
2. Call `preprocess(source)` → `self.clean`
3. Find and record typedef-close brace positions to exclude from variable detection
4. Apply `apply_defines(self.clean, defines)` if `defines` provided → update `self.clean`
5. Compute `self.module = module_name(filepath)`
6. Call `build_line_map(source)` → `self._line_map`
7. Call `_build_brace_depths(self.clean)` → `self._brace_depths`
8. Call `_comment_only_lines(source)` → `self._comment_only`
9. Store `disabled_rules`, `alias_prefixes`, `spell_dict`

---

### UNIT-22 — `Checker.run_all() → CheckResult`

**Purpose:** Orchestrate all rule checks; return aggregated `CheckResult`.

**Algorithm:** Call each enabled `_check_*` method in fixed order; each appends to `self.result.violations`. Return `self.result`.

**Order:** `_check_copyright_header`, `_check_defines`, `_check_variables`, `_check_functions`, `_check_typedefs`, `_check_enums`, `_check_structs`, `_check_include_guard` (headers only), `_check_misc`, `_check_comment_ratio`, `_check_whitespace_ratio`, `_check_yoda`, `_check_constant_comparison`, `_check_reserved_names`, `_check_lowercase_l_suffix`, `_check_octal_constants`, `_check_trigraphs`, `_check_reserved_header_name`, `_check_non_ascii_source`, `_check_spelling` (when dictionary configured)

---

### UNIT-23 — `Checker._check_variables() → None`

**Purpose:** Detect and validate all variable declarations against configured rules.

**Algorithm:**
1. Apply `RE_VAR_DECL` regex to `self.clean`
2. For each match: determine scope via `self._brace_depths[match.start()]`
3. Skip if position is inside a typedef-struct body (`self._typedef_close_positions`)
4. Determine if static via `static` keyword present in match
5. Extract type, pointer stars, and name
6. Check: module prefix, case, g\_/s\_ prefix, p\_/pp\_/b\_/h\_ prefix, prefix order, min/max length, numeric-in-name
7. Skip if rule in `self._disabled_rules`
8. Emit `Violation` via `self.result.add()`

---

### UNIT-25 — `Checker._check_defines() → None`

**Purpose:** Detect `#define` directives and validate macro/constant names.

**Algorithm:**
1. Apply `RE_DEFINE` regex to `self.clean`
2. Classify each match as constant (no parameters) or macro (has parameters)
3. Skip if name matches `exempt_patterns`
4. Check: UPPER\_SNAKE case, module prefix, min/max length
5. Emit violations as appropriate

---

### UNIT-31 — `Checker._check_yoda() → None`

**Purpose:** Enforce Yoda-condition ordering in equality comparisons (Barr-C 8.4).

**Algorithm:**
1. Apply `RE_YODA` regex to find `==` and `!=` comparisons
2. For each match: determine left and right operands
3. If right operand is a constant/literal and left is a variable → violation (constant must be on left)
4. Emit `misc.yoda_condition` violation with line/col

---

### UNIT-34 — `SignChecker._check_calls() → list[Violation]`

**Purpose:** Detect sign-incompatible literal arguments in function calls.

**Algorithm:**
1. Build function-signature table from all header files in `source_cache`
2. For each `.c` file: find function calls via `_extract_call_args()`
3. For each argument: classify as signed/unsigned literal via `_classify_arg()`
4. Look up parameter type from signature table; resolve typedef chain via `_signedness_of_type()`
5. Handle `plain_char_is_signed` with `try/finally` to avoid mutating `_SIGNED_TYPES` permanently
6. Emit `sign_compatibility` violation if mismatch detected

---

### UNIT-37 — `_baseline_key(v: Violation) → str`

**Purpose:** Produce a stable string key for a violation used in baseline suppression.

**Algorithm:** Return `f"{_normalise_path(v.filepath)}:{v.rule}:{v.message}"`

**Design note:** The line number is excluded (issue #394) so an accepted violation stays suppressed when unrelated edits move it. Duplicate violations are distinguished by multiset counting in UNIT-119 rather than by line.

---

### UNIT-119 — `apply_baseline(violations: list, baseline: Counter) → list`

**Purpose:** Remove baselined violations from the result list.

**Algorithm:**
1. Copy *baseline* into a working `Counter` (the input is not mutated)
2. For each violation in order: if the working count for `_baseline_key(v)` is > 0, decrement it and drop the violation; otherwise keep it
3. Return the kept violations

**Design note:** Each baseline entry suppresses at most one violation, so an additional copy of an accepted violation is reported as new.

---

### UNIT-120 — `_normalise_path(path: str) → str`

**Purpose:** Make baseline file paths platform-independent (issue #395).

**Algorithm:** Replace every `\` with `/`, then apply `posixpath.normpath()` (removes `./` and redundant separators). Empty input is returned unchanged.

**Design note:** Backslashes are converted on every platform so baselines written on Windows by earlier releases are honoured on Linux.

---

### UNIT-38 — `_violations_to_json(violations: list, files_checked: int) → str`

**Purpose:** Serialise violations to a JSON string conforming to the documented schema.

**Algorithm:**
1. Build `summary` dict: `files_checked`, `errors`, `warnings`, `info`, `total`
2. Build `violations` list: one dict per `Violation` with all six fields
3. Return `json.dumps({"summary": summary, "violations": violations}, indent=2)`

---

### UNIT-39 — `_violations_to_sarif(violations: list, tool_version: str) → str`

**Purpose:** Serialise violations to SARIF 2.1.0 JSON.

**Algorithm:**
1. Build SARIF `tool` object with `driver.name = "CStyleCheck"`, `driver.version = tool_version`
2. For each violation: build a SARIF `result` object with `ruleId`, `level`, `message.text`, `locations[0].physicalLocation`
3. Return complete SARIF document as `json.dumps(..., indent=2)`

---

### UNIT-50 — `load_spell_words(path: str) → set`

**Purpose:** Load a plain-text file of exempt spell-check words (one per line).

**Algorithm:**
1. Read file at `path`; for each line strip whitespace, skip blank lines and `#`-comment lines
2. Add the lowercased word to result set
3. Return result set

**Error handling:** `OSError` → `sys.exit` with message

---

### UNIT-51 — `load_banned_names_file(path: str) → frozenset`

**Purpose:** Load additional banned identifier names from a plain-text file.

**Algorithm:**
1. Read file at `path`; for each line strip whitespace, skip blank and `#`-comment lines
2. Add name (case-sensitive) to result set
3. Return `frozenset(result)`

**Error handling:** `OSError` → `sys.exit` with message

---

### UNIT-52 — `load_copyright_file(path: str) → tuple`

**Purpose:** Parse a copyright header template file and return `(template_text, match_re)`.

**Algorithm:**
1. Read file at `path`; normalise line endings (CRLF → LF)
2. Extract first `/* ... */` block comment as the template
3. For each line of the template: escape literally via `re.escape`, except replace the year token on the `(C) Copyright YEAR` line with a flexible pattern `\d{4}(?:[-–]\d{4})?`
4. Compile joined pattern anchored with `\A`
5. Return `(template_text, compiled_re)`

**Error handling:** `OSError` → `sys.exit`; no block comment found → `sys.exit`

---

### UNIT-53 — `to_case(name: str, style: str) → str`

**Purpose:** Convert `name` to the given naming style — used to derive enum member prefixes.

**Algorithm:** `upper_snake`/`upper` → `name.upper()`; `lower_snake`/`lower`/`camel` → `name.lower()`; `pascal`/other → `name` unchanged.

---

### UNIT-54 — `is_exempt(name: str, patterns: list) → bool`

**Purpose:** Return `True` if `name` matches any of the exempt regex patterns.

**Algorithm:** For each pattern `p` in `patterns`: if `re.match(p, name)` matches → return `True`. Silently skip malformed patterns. Return `False`.

---

### UNIT-55 — `_cfg(cfg: dict, *keys, default=None)`

**Purpose:** Safe nested dict traversal — retrieve `cfg[k1][k2]…` returning `default` on any missing key or non-dict node.

**Algorithm:** Iteratively descend into `cfg` using each key; if any step is not a dict or key is absent, return `default`.

---

### UNIT-56 — `extract_comments(source: str) → list`

**Purpose:** Return `[(lineno, text)]` for all comments in `source`, stripped of Doxygen markers.

**Algorithm:**
1. Build line map via `build_line_map(source)`
2. Find all `/* … */` block comments via regex; strip `@\word` and leading `*` markers from text; record `(lineno, text)`
3. Find all `// …` line comments; strip Doxygen markers; record `(lineno, text)`
4. Return combined list

---

### UNIT-57 — `Checker._violation(pos, sev, rule, msg) → Violation`

**Purpose:** Helper — construct a `Violation` from a character-offset position by converting it to `(line, col)` via the line map.

---

### UNIT-58 — `Checker._v(pos, sev, rule, msg) → None`

**Purpose:** Helper — emit a `Violation` after checking per-identifier exclusions. Skips emission if the identifier name found in `msg` (quoted with `'...'`) has `rule` disabled in `self._ident_disabled`.

---

### UNIT-59 — `Checker._prefix() → str`

**Purpose:** Return the canonical module prefix string (e.g. `"uart_"`) for the current file, respecting `file_prefix.separator` and `file_prefix.case` from config.

---

### UNIT-60 — `Checker._require_module_prefix(name, pos, rule) → None`

**Purpose:** Emit a violation if `name` does not start with the module prefix or any registered alias prefix.

**Algorithm:**
1. Return immediately if `file_prefix.enabled` is false, or if module is `main` and `exempt_main` is true, or if `name` matches `exempt_patterns`
2. Build accepted prefix list (canonical + aliases)
3. If `name.lower()` starts with any accepted prefix → return (pass)
4. Emit violation with canonical prefix in message and alias hint if aliases exist

---

### UNIT-61 — `Checker._depth_at(pos: int) → int`

**Purpose:** Return the brace depth at character position `pos` in `self.clean`.

---

### UNIT-62 — `Checker._strip_any_prefix(name: str) → str`

**Purpose:** Return `name` with the longest matching module prefix (canonical or alias) removed.

---

### UNIT-63 — `Checker._check_copyright_header() → None`

**Purpose:** Verify the file begins with the configured copyright block comment template.

**Algorithm:**
1. If `self._copyright` is `None` → return (check not configured)
2. Match `compiled_re` against `self.source` at position 0
3. If no match → emit `misc.copyright_header` violation at line 1

---

### UNIT-64 — `Checker._body_is_object_verb(body, object_exclusions, abbrevs) → bool`

**Purpose:** Check whether a function name body (after the module prefix) satisfies the object_verb (or verb_object) convention.

**Algorithm:**
1. Split `body` on `_` into segments
2. If any segment appears in `object_exclusions` → return `True` (waived)
3. Otherwise every segment must be PascalCase or appear in `abbrevs`; a single-segment body (verb only) is also accepted

---

### UNIT-65 — `Checker._check_comment_ratio() → None`

**Purpose:** Enforce a minimum ratio of comment lines to code lines (issue #68).

**Algorithm:**
1. Skip if `misc.comment_ratio.enabled` is false
2. Identify and exclude the file header region (leading comment/blank lines before first code line)
3. Classify remaining lines as comment, code, blank, or Doxygen (excluded from count)
4. Skip if `code_lines < min_code_lines`
5. Compute `ratio = comment_lines / code_lines`
6. Emit `misc.comment_ratio` violation if ratio is below the warning or error threshold

---

### UNIT-66 — `Checker._check_lowercase_l_suffix() → None`

**Purpose:** Detect integer literals with lowercase `l` suffix (MISRA C:2012 Rule 7.3).

**Algorithm:** Scan `self.clean` for numeric literals ending with `l` or `L` followed by `u`/`U` in the wrong order or a bare `l`; emit `misc.lowercase_l_suffix` violation.

---

### UNIT-67 — `Checker._check_octal_constants() → None`

**Purpose:** Detect octal integer constants (leading `0` followed by digits) (MISRA C:2012 Rule 7.1).

**Algorithm:** Scan `self.clean` for tokens matching `0[0-7]+` not preceded by `0x`; emit `misc.octal_constant` violation.

---

### UNIT-68 — `Checker._check_trigraphs() → None`

**Purpose:** Detect ANSI C trigraph sequences (MISRA C:2012 Rule 4.2).

**Algorithm:** Scan `self.source` (raw, not preprocessed) for `??` followed by a trigraph character; emit `misc.trigraph` violation for each occurrence.

---

### UNIT-69 — `Checker._is_reserved(name: str) → tuple`

**Purpose:** Return `(is_reserved: bool, reason: str)` indicating whether `name` is a reserved C identifier (keyword, stdlib name, or banned name).

---

### UNIT-70 — `Checker._check_name_reserved(name, pos, sev) → None`

**Purpose:** Emit a `reserved_name` violation if `name` is reserved, using `_is_reserved()`.

---

### UNIT-71 — `Checker._is_constant_token(tok: str) → bool`

**Purpose:** Return `True` if `tok` is a constant expression token (numeric literal, `NULL`, `true`, `false`, character literal, or macro-like ALL_CAPS name).

---

### UNIT-72 — `Checker._is_variable_token(tok: str) → bool`

**Purpose:** Return `True` if `tok` looks like a variable identifier (lowercase or mixed-case, not a keyword).

---

### UNIT-73 — `_ParamSig`

**Purpose:** Dataclass holding signedness information for one function parameter: `name`, `type_str` (as written), and `signedness` (`signed` | `unsigned` | `unknown`).

---

### UNIT-74 — `_FuncSig`

**Purpose:** Dataclass holding the resolved signature of a declared function: `name` and `params` (list of `_ParamSig`).

---

### UNIT-75 — `_classify_tokens(tokens, signed_types, unsigned_types) → str`

**Purpose:** Return sign classification (`signed` | `unsigned` | `unknown`) from a list of C type/qualifier tokens.

**Algorithm:** If `unsigned` in tokens → `unsigned`; if `signed` in tokens → `signed`; otherwise look each token up in the explicit signed/unsigned type sets; return `unknown` if no match.

---

### UNIT-76 — `_signedness_of_type(type_str, tmap, signed_types, unsigned_types) → str`

**Purpose:** Resolve a full C type string to a sign classification, following typedef chains via `tmap`.

---

### UNIT-77 — `_classify_arg(expr: str) → str`

**Purpose:** Classify one call-site argument expression as `signed`, `unsigned`, `neutral` (plain positive integer, no suffix), or `unknown`.

---

### UNIT-78 — `_extract_call_args(source, paren_pos) → list | None`

**Purpose:** Extract comma-separated argument strings from a function call starting at `paren_pos` (the `(` character). Returns `None` if the call cannot be parsed.

---

### UNIT-79 — `SignChecker.__init__(cfg: dict)`

**Purpose:** Initialise the cross-file sign compatibility checker with the YAML config.

---

### UNIT-80 — `SignChecker.ingest(filepath, source) → None`

**Purpose:** Ingest one file into the checker — stores `(filepath, source, preprocess(source))` for later analysis.

---

### UNIT-81 — `SignChecker.check() → list[Violation]`

**Purpose:** Build typedef and signature tables then check every `.c` call site; return all sign-compatibility violations.

**Algorithm:** Build thread-safe local copies of sign-type sets respecting `plain_char_is_signed`; call `_build_typedef_map`, `_build_signatures`, `_check_calls` in order.

---

### UNIT-82 — `SignChecker._build_typedef_map(signed_types, unsigned_types) → None`

**Purpose:** Parse all typedef scalar declarations from ingested files and resolve each typedef name to a sign classification (following chains up to depth 8).

---

### UNIT-83 — `SignChecker._build_signatures(signed_types, unsigned_types) → None`

**Purpose:** Parse function declarations (ending with `;`) from all ingested files and build the signature table `_sigs`.

---

### UNIT-84 — `DeclaredNotDefinedChecker` (class)

**Purpose:** Cross-file declared-but-not-defined checker. Identifies C objects (`extern` variables, extern functions, forward typedef structs/enums) that are declared but for which no definition is found across all ingested files.

**Key methods:**
- `__init__(cfg)` — initialise declaration/definition sets
- `ingest(filepath, source)` — scan one file for declarations and definitions
- `check() → list[Violation]` — compare declarations against definitions; emit `misc.declared_not_defined` for unresolved items; always returns `[]` for single-file runs

---

### UNIT-85 — `_strip_module_prefix(name: str, prefix: str) → str`

**Purpose:** Return `name` with the module prefix removed (case-insensitive). Returns `name` unchanged if it does not start with `prefix`.

---

### UNIT-86 — `Tee`

**Purpose:** Write to stdout and optionally a log file simultaneously.

**Methods:**
- `__init__(log_fh=None)` — store optional file handle
- `print(*args, **kwargs)` — call built-in `print` to stdout, and to `log_fh` if set
- `log_print(*args, **kwargs)` — write only to `log_fh` (not stdout); used for content that must appear in the log file but not on the terminal
- `close()` — close and release `log_fh`

---

### UNIT-87 — `parse_args() → argparse.Namespace`

**Purpose:** Parse the process command-line arguments using `_build_parser()`.

---

### UNIT-88 — `_build_parser() → argparse.ArgumentParser`

**Purpose:** Construct and return the fully configured `ArgumentParser` for the tool.

**Key argument groups:** help/version, positional files, config/output, include/exclude globs, defines/aliases/exclusions, copyright/banned-names, spell-check, baseline, logging, sign-compatibility, and diagnostics flags.

---

### UNIT-89 — `_github_annotation_category(rule: str) → str`

**Purpose:** Return the GitHub Actions annotation title category for a violation rule.

**Algorithm:** Map `misc.trigraph`, `misc.octal_constant`, `misc.lowercase_l_suffix` → `"MISRA"`; `sign_compatibility` → `"SignCompat"`; `spell_check` → `"SpellCheck"`; naming-convention prefixes (variable, function, constant, …) → `"NamingConvention"`; everything else → `"Misc"`.

---

### UNIT-95 — `parse_inline_suppressions(source: str) → dict`

**Purpose:** Parse `// cstylecheck: disable=…` / `enable=…` / `disable-next-line=…` directives from raw C source and return a mapping of line numbers to the set of suppressed rule IDs at that line.

**Algorithm:**
1. Scan `source` line by line; detect `cstylecheck:` directives in both line comments (`// cstylecheck: …`) and block-comment form (`/* cstylecheck: … */`) on the same source line (case-insensitive)
2. For `disable=rule.a,rule.b` on the same line as code: add the rule IDs to that line's suppressed set only
3. For `disable-next-line=rule.id`: add rule IDs to the next non-blank, non-comment line's suppressed set
4. For a standalone `disable=rule.id` line: open a block suppression; accumulate affected rule IDs per line until a matching `enable=rule.id` is found; unpaired `disable=` suppresses to end of file
5. Multiple rules are comma-separated in any directive form
6. Return `dict[int, frozenset[str]]` mapping 1-based line numbers to suppressed rule IDs

---

### UNIT-96 — `apply_fixes(source: str, violations: list, safe_only: bool = False) → tuple[str, int]`

**Purpose:** Module-level function. Scans source string for fixable violations and returns (new_source, fix_count).

**Algorithm:**
1. Iterate over violations; for each fixable rule apply the mechanical substitution to the source string
2. Currently supported: `misc.unsigned_suffix` (`u`/`l` → `U`/`L`) and `misc.lowercase_l_suffix`
3. If `safe_only` flag is set: skip any fix not classified as zero-risk (currently all fixes qualify)
4. Return `(new_source, fix_count)` where `fix_count` is the number of substitutions applied

---

### UNIT-97 — `unified_diff(original: str, fixed: str, filepath: str) → str`

**Purpose:** Module-level function. Returns unified diff string comparing original and fixed source.

**Algorithm:** Call `difflib.unified_diff()` between `original` and `fixed` strings; use `filepath` as the filename label in the diff header; return the combined diff string.

---

### UNIT-98 — `run_wizard(output_path=None, prompt_fn=input, print_fn=print, overwrite=False) → int`

**Purpose:** Interactive Q&A wizard that prompts the user for project preferences, writes `.cstylecheck.yml` directly, and returns 0 on success or 1 on abort.

**Algorithm:**
1. Present a short series of prompts (project name, preferred naming style, which rule categories to enable)
2. Build a YAML-serialisable config dict based on user answers
3. Write the config to `output_path` (default `.cstylecheck.yml`); if the file exists and `overwrite` is False → return 1 (abort)
4. Return 0 on success

---

### UNIT-99 — `run_preset(preset_name: str, output_path: str | None = None, print_fn=print, overwrite: bool = False) → int`

**Purpose:** Write a pre-built config file for the named preset without running the wizard; returns 0 on success or 1 on error.

**Algorithm:**
1. Look up `preset_name` (`barr-c`, `minimal`, or `misra`) from the built-in `PRESETS` dict
2. If `output_path` exists and `overwrite` is false → emit error via `print_fn`; return 1
3. Write YAML to `output_path` (default `.cstylecheck.yml`); return 0

---

### UNIT-100 — `resolve_per_dir_config(filepath: str, root_cfg: dict, cache: dict) → dict`

**Purpose:** Walk upward from `filepath`'s directory looking for `.cstylecheck.yml` files and return a deep-merged config for that file.

**Algorithm:**
1. Check `cache[dir]`; if found return cached result
2. Walk upward from `os.dirname(filepath)`; for each directory check for `.cstylecheck.yml`
3. If found: load and collect; stop if `root: true` is present; continue otherwise
4. Deep-merge collected configs (nearest wins) on top of `root_cfg`
5. Store in `cache[dir]` and return merged result

---

### UNIT-101 — `_violations_to_html(violations: list, files_checked: int) → str`

**Purpose:** Serialise violations to a self-contained HTML report string with inline CSS.

**Algorithm:**
1. Compute counts: errors, warnings, info, total, files checked
2. Render summary cards (one per count)
3. Group violations by file; render a per-file `<table>` with line, column, severity, rule, message columns
4. Wrap in a full HTML document with embedded CSS; return the document string

---

### UNIT-102 — `Checker._check_function_length() → None`

**Purpose:** Enforce a maximum function body line count (`misc.function_length`, issue #221).

**Algorithm:**
1. Skip if `misc.function_length.enabled` is false
2. Call `_iter_function_bodies()` to yield `(fn_def_pos, fn_name, body_start, body_end)`
3. For each function body: split lines between `body_start` and `body_end`
4. If `count_comments: false`, exclude blank and comment-only lines before counting
5. If line count exceeds `max_lines`, emit `misc.function_length` at the function definition line

---

### UNIT-103 — `Checker._check_function_doc_header() → None`

**Purpose:** Require a Doxygen block comment before each non-static function (`misc.function_doc_header`, issue #222).

**Algorithm:**
1. Skip if `misc.function_doc_header.enabled` is false
2. For each function definition found via `RE_FUNCTION_DEF`: scan backwards for a block comment
3. Verify comment contains `@brief` (or `\brief`)
4. If `require_param: true`: verify each parameter has a corresponding `@param` tag
5. If `require_return: true` and return type is not `void`: verify `@return` tag is present
6. Emit `misc.function_doc_header` on any missing element

---

### UNIT-104 — `Checker._check_assert_density() → None`

**Purpose:** Enforce minimum `assert()` calls per function (`misc.assert_density`, issue #225).

**Algorithm:**
1. Skip if `misc.assert_density.enabled` is false
2. Call `_iter_function_bodies()` to yield function bodies
3. For each body: count lines; if below `min_function_lines`, skip
4. Check function name against `exempt_functions` regex patterns; skip if matched
5. Count `assert(` occurrences in body
6. If count < `min_asserts`, emit `misc.assert_density`

---

### UNIT-105 — `Checker._check_null_statement_comment() → None`

**Purpose:** Require a comment alongside null statements (`misc.null_statement_comment`, issue #227).

**Algorithm:**
1. Skip if `misc.null_statement_comment.enabled` is false
2. Scan `self.clean` for control-flow keywords immediately followed by `;` using a regex that handles one level of nested parentheses; emit violation for each match
3. Scan `self.source.splitlines()` for standalone `;` on its own line; emit violation if no comment present

---

### UNIT-106 — `Checker._check_declaration_spacing() → None`

**Purpose:** Enforce a blank line between declarations and first executable statement (`misc.declaration_spacing`, issue #224).

**Algorithm:**
1. Skip if `misc.declaration_spacing.enabled` is false
2. Call `_iter_function_bodies()` to yield function bodies
3. Within each body: identify trailing declaration lines (lines starting with a type keyword or typedef)
4. Verify the line immediately following the declaration block is blank; emit `misc.declaration_spacing` if not

---

### UNIT-107 — `Checker._check_file_length() → None`

**Purpose:** Enforce a maximum source-file line count (`misc.file_length`, issue #232).

**Algorithm:**
1. Skip if `misc.file_length.enabled` is false
2. Split `self.source` into lines
3. If `count_blank_lines: false`, exclude blank lines
4. If `count_comment_lines: false`, exclude comment-only lines
5. If remaining count > `max_lines`, emit `misc.file_length` at line 1

---

### UNIT-108 — `Checker._check_reserved_header_name() → None`

**Purpose:** Flag files and `#include` directives using standard C/POSIX header names (`misc.reserved_header_name`, issue #230).

**Algorithm:**
1. Skip if `misc.reserved_header_name.enabled` is false
2. Check `os.path.basename(self.filename)` against `_STANDARD_C_HEADERS`; emit violation at line 1 if matched
3. Scan `self.source` for `#include "..."` directives; check the included name against `_STANDARD_C_HEADERS`; emit violation at the directive line if matched

---

### UNIT-109 — `Checker._check_macro_trailing_semicolon() → None`

**Purpose:** Detect `#define` macros ending with `;` (`macro.trailing_semicolon`, issue #228).

**Algorithm:**
1. Skip if `macros.trailing_semicolon.enabled` is false
2. Iterate source lines; collect multi-line macros (continuation `\`)
3. Strip string literals, character literals, and comments from the assembled body
4. If the resulting body text ends with `;`, emit `macro.trailing_semicolon`

---

### UNIT-110 — `Checker._check_macro_multistatement_wrapper() → None`

**Purpose:** Enforce `do { ... } while (0)` for multi-statement macros (`macro.multistatement_wrapper`, issue #229).

**Algorithm:**
1. Skip if `macros.multistatement_wrapper.enabled` is false
2. Collect function-like macros; assemble multi-line bodies
3. Count `;` statement terminators in the body (excluding trailing `;` already caught by UNIT-109)
4. If count > 1 and the body is not a `do { ... } while (0)` block, emit `macro.multistatement_wrapper`

---

### UNIT-111 — `Checker._check_identifier_length() → None`

**Purpose:** Uniform min/max identifier length across all categories (`naming.identifier_length`, issue #223).

**Algorithm:**
1. Skip if `naming.identifier_length.enabled` is false
2. For each declared identifier found by the declaration scanner: check length against `[min_length, max_length]`
3. Skip names matching any pattern in `exempt_patterns`
4. Emit `naming.identifier_length` for out-of-range names

---

### UNIT-112 — `Checker._check_no_single_char_identifiers() → None`

**Purpose:** Flag single-character variable names not in the exempt list (`naming.no_single_char_identifiers`, issue #231).

**Algorithm:**
1. Skip if `naming.no_single_char_identifiers.enabled` is false
2. For each declared identifier with `len(name) == 1`: check against `exempt` list
3. Emit `naming.no_single_char_identifiers` for non-exempt single-character names

---

### UNIT-113 — `Checker._check_non_ascii_source() → None`

**Purpose:** Flag source characters outside the basic ASCII set (MISRA C:2012/2023 Rule 4.1, issue #279).

**Algorithm:**
1. Skip if `misc.non_ascii_source.enabled` is false
2. If `exempt_string_literals: true`, build a set of character offsets that lie inside double-quoted string literals
3. Iterate over every character in `self.source`; allow: tab (0x09), LF (0x0A), CR (0x0D), printable ASCII (0x20–0x7E)
4. For each disallowed character not in the exempt set, emit `misc.non_ascii_source` with the Unicode code point value in hex

---

### UNIT-114 — `output.print_summary()` (per-file breakdown)

**Purpose:** Extend `print_summary()` with a per-file breakdown section (issue #278).

**Algorithm:**
1. Collect file paths from all violations into three sets: `files_with_errors`, `files_with_warnings`, `files_with_infos`
2. Count files in each bucket using highest-severity wins: warnings bucket excludes files already in errors; info bucket excludes files in errors or warnings
3. Clean files = `files_checked` minus total files with any violation
4. Emit the breakdown section only when `files_checked > 0`

---

### UNIT-115 — `Checker._check_defines()` (typedef-alias exemption)

**Purpose:** Prevent `constant.case` false positives on object-like `#define` type aliases (issues #272, #244).

**Algorithm:**
1. Read `typedefs.suffix.suffix` and `typedefs.suffix.enabled` from config
2. For each object-like `#define` (non-function-like): compute `is_typedef_alias` = name ends (case-insensitively) with the configured suffix when suffix is enabled
3. Skip `constant.case` check when `is_typedef_alias` is true; continue all other checks (`max_length`, `min_length`, `prefix`)

---

---

### UNIT-116 — `Checker._check_constant_comparison() → None`

**Purpose:** Detect comparisons where both operands are compile-time constants (`misc.constant_comparison`, SWE1-091).

**Algorithm:**
1. Skip if `misc.constant_comparison.enabled` is false
2. Scan `self.clean` for `==` and `!=` operators using a token-based regex
3. For each match: extract the left-hand and right-hand tokens
4. Call `_is_constant_token()` on both tokens
5. Skip if comparison is inside a `#define` RHS or a `return` statement
6. If both tokens are constants, emit `misc.constant_comparison` warning

---

### UNIT-117 — `_fix_pointer_prefix(source, fn_name, old_param, new_param) → str`

**Purpose:** Rename a pointer parameter from `old_param` to `new_param` within a function's signature and body (SWE1-093).

**Algorithm:**
1. Locate the function definition for `fn_name` in `source`
2. Find the extent of the function signature (up to opening `{`) and body (up to matching `}`)
3. In the signature: replace `old_param` at word boundaries
4. In the body: replace `old_param` at word boundaries
5. Search for a Doxygen block comment immediately preceding the function; replace `@param old_param` and `\param old_param` occurrences
6. Return the modified `source` string

---

### UNIT-118 — `fix_pointer_prefix_in_header(header_source, fn_name, old_param, new_param) → str`

**Purpose:** Apply the same rename to a function declaration in the corresponding `.h` file (SWE1-093).

**Algorithm:**
1. Locate the function declaration for `fn_name` in `header_source` (declaration ends with `;`)
2. Replace `old_param` at word boundaries within the declaration
3. Return the modified header source

---

### UNIT-121 — `strip_comments_and_strings(text) → str`

**Purpose:** Blank out comments and string/char literal contents so that keyword, brace and call counting never matches text inside comments or strings (SWE1-102 to SWE1-106, issue #388). Located in `scripts/collect_metrics.py`.

**Algorithm:**
1. Single-pass state machine with states NORMAL, LINE_CMT, BLOCK_CMT, STRING, CHAR
2. Replace every comment character (including delimiters) and every literal content character with a space; keep newlines and the literal delimiters
3. A backslash inside a literal consumes the following character; an unterminated literal ends at end of line
4. The result has the same length as the input so offsets and line numbers map 1:1

The companion `blank_preprocessor_lines(code)` blanks `#` directives (including `\` continuations) so macro bodies are not mistaken for code.

---

### UNIT-122 — `classify_lines(text) → dict`

**Purpose:** Classify each physical line as blank, comment, doxygen or SLOC (SWE1-102).

**Algorithm:**
1. Whitespace-only line → blank
2. Otherwise scan the line, tracking block-comment state (and whether the open block is doxygen: `/**` but not `/**/` or `/***`, or `/*!`) and multi-line literal state
3. Any non-comment, non-whitespace character (including literal text) marks the line as SLOC
4. A comment-only line is doxygen if its comment is a doxygen block or a `///` / `//!` line, otherwise comment
5. Invariant: `physical = blank + comment + doxygen + sloc`

---

### UNIT-123 — `extract_functions(text) → list[dict]`

**Purpose:** Locate function definitions and compute per-function metrics (SWE1-103 to SWE1-106).

**Algorithm:**
1. Strip comments/strings (UNIT-121) and blank preprocessor lines
2. Scan at file-scope brace depth 0; the text since the last `;` or `}` is the candidate header
3. `extern "C" {` braces are transparent; a header is a function definition if it ends with `name(params)`, contains no `=`, the name is not a control keyword and it does not start with `typedef`/`struct`/`union`/`enum`
4. Find the matching `}` and record: name; start line (name line); length (name line → closing brace, inclusive); `count_params()` (top-level commas, `void`/empty = 0); `cyclomatic_complexity()` (1 + `if`/`while`/`for`/`case`/`&&`/`||`/`?`); `max_brace_nesting()` (maximum depth − 1); `has_dox` (original text immediately before the header ends in a `/**`/`/*!` block or a `///`/`//!` line); `calls` (identifiers followed by `(` excluding `C_KEYWORDS`); `recursive` (own name in `calls`)
5. Non-function brace blocks (struct/enum/initialiser) are skipped without ending the current statement

---

### UNIT-124 — `count_file_scope_variables(text) → (int, int)`

**Purpose:** Count file-scope global and static variable definitions (SWE1-106).

**Algorithm:**
1. Strip comments/strings and preprocessor lines; iterate `;`-terminated statements at file scope, skipping function bodies
2. Skip `typedef`, `extern`, `_Static_assert` and `asm` statements
3. Replace an aggregate type body (`struct s {…} v`) by a placeholder type; a statement with nothing after the closing brace is a pure type definition and is skipped
4. Split into declarators on top-level commas; a declarator containing `name(` without `(*` is a prototype and is skipped
5. Add the remaining declarators to the `static` or global total

---

### UNIT-125 — `_c_source_metrics(total_violations=0, source_dir=None) → dict`

**Purpose:** Aggregate all C source metrics over `examples/*.c` and `*.h` (or `source_dir`) (SWE1-102 to SWE1-108, SWE1-117).

**Algorithm:**
1. If no `.c`/`.h` files exist, return `_empty_c_metrics()` (all zero)
2. Per file: accumulate `classify_lines()`, the maximum file length and the safety counters (SWE1-117) on `strip_comments_and_strings()` text: `assert(` calls (`_RE_ASSERT`), `goto` (`_RE_GOTO_MET`), `void *` (`_RE_VOID_PTR`), C-style casts (`_RE_C_CAST`, on text with preprocessor lines blanked) and `#define` names (`_RE_MACRO_DEF`), excluding include-guard names that match `_RE_INC_GUARD`
3. For `.c` files only: `extract_functions()` and `count_file_scope_variables()`
4. Derive max/avg/over-threshold values using `FUNC_LENGTH_LIMIT` (60), `FUNC_PARAM_LIMIT` (5), `CC_LIMIT` (10) and `CC_BUCKETS`; densities (including `assert_density` = asserts per KLOC SLOC) are 0.0 when SLOC = 0
5. Return the metrics dict, including `assert_count`, `assert_density`, `goto_count`, `void_ptr_count`, `cast_count` and `macro_count`

---

### UNIT-126 — `_summarise_violations(data) → dict`

**Purpose:** Derive severity totals and violation-quality metrics from the CStyleCheck JSON report (SWE1-107).

**Algorithm:**
1. Read `summary` and `violations` (missing keys → empty)
2. Count violations per rule, per category (rule-ID prefix before the first `.`) and collect the set of files with violations
3. `files_zero_violations = max(0, files_checked − |files with violations|)`; `top_rules` = the five most common rules

---

### UNIT-127 — `generate_charts._make_chart(…, stacked=False)`, `_stack_series()`, `_category_series()`

**Purpose:** Render the new trend charts, including stacked-area charts, while tolerating data points recorded before issue #388 (SWE1-108). Located in `scripts/generate_charts.py`.

**Algorithm:**
1. `_stack_series()` accumulates the series in order; an index where every component is missing stays `None` (not plotted), otherwise a missing component counts as 0
2. With `stacked=True`, `_make_chart()` draws a filled polygon between consecutive cumulative series before drawing the boundary lines
3. `_category_series()` builds one series per rule category from `violations_by_category` (top 8 by total, the rest merged into `other`); points without the field yield `None`
4. A chart whose series contain no values is not written
5. The `safety_indicators` chart plots `goto_count`, `void_ptr_count`, `cast_count` and `assert_count`, and the `macro_metrics` chart plots `macro_count` and `assert_density` (SWE1-117, PR #392)

---

### UNIT-90 — `Checker._check_whitespace_ratio() → None`

**Purpose:** Enforce a minimum ratio of blank lines to code lines (issue #143), measuring code "airiness".

**Algorithm:**
1. Skip if `misc.whitespace_ratio.enabled` is false
2. Identify and exclude the file header region (leading comment/blank lines before first code line)
3. Classify remaining lines as blank, comment-only, or code; exclude comment-only lines from both counts
4. Skip if `code_lines < min_lines` (configurable minimum)
5. Compute `ratio = blank_lines / code_lines`
6. Emit `misc.whitespace_ratio` violation if ratio is below the error or warning threshold

---

### UNIT-06 — `load_alias_file(path: str) → dict`

**Purpose:** Load the module-alias map for `--aliases` (SWE1-004).

**Algorithm:**
1. Read the file as UTF-8 (`errors="replace"`); on `OSError` call `sys.exit()` with a message
2. Skip blank lines and lines starting with `#`
3. Split each line on whitespace; lines with fewer than 2 words produce a stderr warning and are skipped
4. Lower-case both stems and register each as an alias of the other (bidirectional, no duplicates)
5. Return `{stem_lower: [alias_stem_lower, …]}`

---

### UNIT-07 — `load_exclusions_file(path: str) → dict`

**Purpose:** Load the per-file rule exclusion YAML for `--exclusions` (SWE1-005).

**Algorithm:**
1. `yaml.safe_load()` the file; on `OSError` call `sys.exit()`; a non-mapping document returns `{}`
2. For each `pattern → body` mapping: `file_rules` = frozenset of `body.disabled_rules` (empty if not a list)
3. For each `body.identifiers.<ident>.disabled_rules` list, build `ident_rules[ident]` = frozenset
4. Return `{pattern: {"file_rules": …, "ident_rules": …}}`

---

### UNIT-08 — `_disabled_rules_for_file(filepath: str, exclusions: dict) → tuple`

**Purpose:** Resolve the rules disabled for one source file (SWE1-006).

**Algorithm:**
1. Take the file basename
2. For every exclusion pattern that matches with `fnmatch`, union its `file_rules` (or a legacy bare frozenset) into the file set and union its `ident_rules` per identifier
3. Return `(frozenset(file_disabled), {ident: frozenset(rules)})`

---

### UNIT-09 — `load_defines_file(path: str) → list`

**Purpose:** Load the project defines file for `--defines` (SWE1-003).

**Algorithm:**
1. Read the file; on `OSError` call `sys.exit()`
2. Skip blank and `#` lines; split each line on the first whitespace run into `token` and `expansion`
3. Lines without an expansion, or with a token that fails to compile, produce a stderr warning and are skipped
4. Compile `\btoken\b` (whole-word) and append `(pattern, expansion)` in file order
5. Return the list (applied by UNIT-10 `apply_defines()`)

---

### UNIT-11 — `_load_dict_file(path: str) → frozenset`

**Purpose:** Load a one-token-per-line dictionary (keywords, stdlib names, banned names) (SWE1-007, SWE1-008).

**Algorithm:** Read the file line by line, strip each line, skip blank and `#` lines and add the rest to a set. A missing file (`FileNotFoundError`) yields an empty set. Return `frozenset(tokens)`.

---

### UNIT-12 — `_data_file(name: str) → Path`

**Purpose:** Resolve a bundled data file for source checkouts and pip installs (SWE1-007 to SWE1-010).

**Algorithm:** Return the first existing candidate: `<package>/../name` (i.e. `src/name`), then `<package>/name`. Otherwise return `sysconfig.get_path("data")/share/cstylecheck/name` without checking that it exists (UNIT-11 tolerates a missing file).

---

### UNIT-13 — `_build_spell_dict(cfg_exempt: list, extra_words: set, base_dict=None) → set`

**Purpose:** Build the effective spell-check word set (SWE1-009, SWE1-056).

**Algorithm:** Start from a copy of *base_dict* (or `_BUILTIN_DICT` when `None`), add every `cfg_exempt` word and every `extra_words` word lower-cased, and return the combined set. The inputs are not mutated.

---

### UNIT-15 — `strip_strings(source: str) → str`

**Purpose:** Blank string literal contents while preserving offsets (SWE1-011).

**Algorithm:**
1. Replace each double-quoted literal (escape-aware) with `""` followed by spaces, so the length is unchanged
2. Replace each single-quoted character literal with `'x'`, keeping the char-literal shape for the yoda checker and hiding digits from the suffix checks

---

### UNIT-17 — `build_line_map(source: str) → list`

**Purpose:** Build the offset → line lookup table (SWE1-012).

**Algorithm:** Return `[0]` followed by the offset just after every `\n` in *source*. Element *k* is the start offset of line *k*+1.

---

### UNIT-18 — `offset_to_line_col(offsets: list, pos: int) → (int, int)`

**Purpose:** Convert a character offset into a 1-based `(line, col)` (SWE1-012).

**Algorithm:** Binary-search *offsets* (UNIT-17) for the last line start ≤ *pos*, then return `(index + 1, pos − offsets[index] + 1)`. Complexity: O(log L).

---

### UNIT-20 — `_comment_only_lines(source: str) → set`

**Purpose:** Identify lines that contain only comments or whitespace, which are exempt from line-length and indentation checks (SWE1-045, SWE1-046).

**Algorithm:** Scan the lines, tracking whether a `/* … */` block is open. A line is exempt if it is inside an open block, starts with `/*` (opening a block when `*/` does not follow on that line), starts with `//`, or is blank. Return the set of 1-based line numbers.

---

### UNIT-24 — `Checker._check_functions() → None`

**Purpose:** Enforce the `function.*` rules on function definitions (SWE1-030 to SWE1-034, SWE1-098).

**Algorithm:**
1. Return if `functions.enabled` is false
2. For each `RE_FUNCTION_DEF` match in the clean source: skip ISR-suffixed names (`isr_suffix`), `main.c` helpers (`file_prefix.exempt_main`) and `exempt_patterns`
3. Compute `fn_start` (advance past a leading `\n`) so violations are reported on the function-name line (SWE1-098)
4. Static functions: emit `function.static_prefix` when `static_prefix.enabled` and the name lacks the prefix
5. Call `_require_module_prefix()` (`function.prefix`); check `function.max_length` / `function.min_length`
6. If the name carries the module prefix, check the body: `object_verb` / `verb_object` style via `_body_is_object_verb()`, or `lower_snake`; emit `function.style` on mismatch

---

### UNIT-26 — `Checker._check_typedefs() → None`

**Purpose:** Enforce `typedef.case` and `typedef.suffix` (SWE1-040).

**Algorithm:** Return if disabled. For each `RE_TYPEDEF_SIMPLE` match, emit `typedef.case` when the name does not match `typedefs.case` (default `upper_snake`), and emit `typedef.suffix` when `suffix.enabled` and the name does not end with the configured suffix (default `_T`).

---

### UNIT-27 — `Checker._check_enums() → None`

**Purpose:** Enforce the `enum.*` rules (SWE1-041).

**Algorithm:**
1. Return if disabled. For each `RE_TYPEDEF_ENUM` match, check `enum.type_case` and `enum.type_suffix` on the type name
2. Derive the member prefix: strip the type suffix case-insensitively, then convert with `to_case()` to the member case
3. For each member (`RE_ENUM_MEMBER`): emit `enum.member_case` on a case mismatch, and `enum.member_prefix` (own severity) when `member_prefix_from_type.enabled` and the member does not start with `<prefix>_` (case-insensitive)

---

### UNIT-28 — `Checker._check_structs() → None`

**Purpose:** Enforce the `struct.*` rules (SWE1-042).

**Algorithm:** Return if disabled. For each `RE_TYPEDEF_STRUCT` match: if a tag is present, check `struct.tag_case` and (when enabled) `struct.tag_suffix`. Then, for each member name (identifier followed by `;` or `[`), emit `struct.member_case` unless `matches_case_abbrev()` accepts it with `structs.allowed_abbreviations`.

---

### UNIT-29 — `Checker._check_include_guard() → None`

**Purpose:** Enforce `include_guard.missing` and `include_guard.format` on header files (SWE1-043, SWE1-044).

**Algorithm:**
1. Return if disabled, or if `allow_pragma_once` is set and `#pragma once` is present
2. Build the expected guard from `include_guards.pattern` (default `{FILENAME_UPPER}_{EXT_UPPER}_`)
3. If there is no `#ifndef` or no `#define` guard, emit `include_guard.missing` at offset 0 and return
4. If the `#ifndef` symbol does not start with the expected guard (trailing `_` ignored), emit `include_guard.format`

---

### UNIT-30 — `Checker._check_misc() → None`

**Purpose:** Enforce the line-oriented and literal `misc.*` rules (SWE1-045 to SWE1-048, SWE1-050, SWE1-092).

**Algorithm:**
1. `misc.line_length` and `misc.indentation`: per non-comment line (UNIT-20), check the maximum length and the tab/space style
2. Build the exempt-offset set for literals: array subscripts, preprocessor lines, `return` expressions, `const` declarations, `exempt_function_args`, and signed-parameter call arguments of functions declared in the same translation unit (SWE1-092)
3. `misc.magic_number`: flag numeric literals outside the exempt set and not in the allowed list
4. `misc.unsigned_suffix`: when `require_on_unsigned_constants` is set, flag unsuffixed non-negative integer literals outside the exempt set
5. `misc.block_comment_spacing` and `misc.eof_comment` (template match on the last non-blank line followed by exactly one blank line), when enabled

---

### UNIT-32 — `Checker._check_reserved_names() → None`

**Purpose:** Enforce `reserved_name` (SWE1-054, SWE1-055).

**Algorithm:** Return if disabled. Call `_check_name_reserved()` (UNIT-70) for every variable name (`RE_VAR_DECL` group 4), every function definition name (`RE_FUNCTION_DEF`) and every `#define` name that has a replacement body (bare include-guard defines are skipped).

---

### UNIT-33 — `Checker._check_spelling() → None`

**Purpose:** Enforce `spell_check` on comment text (SWE1-056).

**Algorithm:** Return if disabled. For each `(lineno, text)` from `extract_comments(self.source)` (UNIT-56) and each word matched by `RE_COMMENT_WORD`, lower-case the word and strip a trailing `'s`. If the result is not in `self._spell_dict`, add a `spell_check` violation at `(lineno, 1)`.

---

### UNIT-35 — `load_baseline(path: str) → Counter`

**Purpose:** Load a baseline file as a multiset of keys (SWE1-066, SWE1-100, SWE1-101).

**Algorithm:**
1. Parse the JSON; on `OSError` or `JSONDecodeError` call `sys.exit()`
2. For each entry in `data["violations"]`, build the key `_normalise_path(file):rule:message` (line ignored) and increment its count
3. Return the `collections.Counter`

---

### UNIT-36 — `write_baseline(violations: list, path: str) → None`

**Purpose:** Serialise the current violations as a baseline (SWE1-065, SWE1-101).

**Algorithm:** Build `{"violations": [{"file": _normalise_path(v.filepath), "line": v.line, "rule": v.rule, "message": v.message}, …]}` and write it with `json.dumps(indent=2)` as UTF-8. On `OSError` call `sys.exit()`. The format is shown in §6.3.

---

### UNIT-40 — `print_summary(all_violations, files_checked, tee, version_string="", copyright_string="") → None`

**Purpose:** Print the `--summary` report (SWE1-063, SWE1-089, SWE1-097).

**Algorithm:**
1. Count errors, warnings and info; print the header with the run timestamp
2. When `files_checked > 0`, print the `Files:` block, counting each file only in its highest-severity bucket (errors, then warnings, then info) plus clean files
3. Print the `Results:` block, with a separator width derived from the digit count of the largest value
4. If any violations exist, print the top 10 rules by count

---

### UNIT-41 — `Violation.__str__() → str`

**Purpose:** Plain-text violation line (SWE1-057).

**Algorithm:** Return `f"{filepath}:{line}:{col}: {SEVERITY} [{rule}] {message}"`. The path is rendered verbatim; the OS-native path separator (SWE1-096) is applied earlier, when `discover_files()` (UNIT-03) yields each path through `os.path.normpath()`.

---

### UNIT-42 — `Violation.github_annotation() → str`

**Purpose:** GitHub Actions workflow-command annotation (SWE1-061).

**Algorithm:** Map the severity to `error`/`warning`, or `notice` for anything else; take the title from `_github_annotation_category(rule)` (UNIT-89); return `::{level} file=…,line=…,col=…,title={title}[{rule}]::{message}`.

---

### UNIT-43 — `matches_case(name: str, style: str) → bool`

**Purpose:** Test an identifier against a named case style (used by all naming rules).

**Algorithm:** Look up the compiled regex for *style* in `_CASE_PATTERNS` (`lower_snake`, `upper_snake`, `camel`, `pascal`, `lower`, `upper`) and return whether it matches. An unknown style returns `True`.

---

### UNIT-44 — `matches_case_abbrev(name: str, style: str, abbrevs: set) → bool`

**Purpose:** Case check that tolerates allowed upper-case abbreviations (e.g. `read_FIFO_count`).

**Algorithm:** For styles other than `lower_snake` / `lower`, or when *abbrevs* is empty, delegate to UNIT-43. Otherwise split on `_`: each non-empty segment must either be an allowed abbreviation (any case) or match `^[a-z0-9]+$`.

---

### UNIT-45 — `module_name(filepath: str) → str`

**Purpose:** Derive the module name used for prefix rules (SWE1-017 onwards).

**Algorithm:** Return the lower-cased file stem (`Path(filepath).stem.lower()`).

---

### UNIT-46 — `main() → int`

**Purpose:** CLI entry point (SWE1-068 to SWE1-070, SWE1-094, SWE1-095).

**Algorithm:**
1. Fast path for `--version` / `--help`; expand `--options-file` (UNIT-02) and parse arguments
2. Handle `--update-config` (UNIT-94), `--preset` and `--init` (UNIT-98/99), then exit
3. Load the configuration, dictionaries, defines, banned names, copyright template, aliases and exclusions; open `--log`; write the two-line startup banner (`_VERSION_STRING`, then `_COPYRIGHT`) to stderr and to the log via `Tee.log_print()`, never to stdout; the write is unconditional (no TTY check, no suppression option) (SWE1-094)
4. Discover files (UNIT-03); for each file, resolve the per-directory config (UNIT-100), run `Checker.run_all()` (UNIT-22) and emit violations (with verbose progress when requested)
5. Run the cross-file checks (`SignChecker`, `DeclaredNotDefinedChecker`); apply `--fix` / `--dry-run` (UNIT-96). Without `--dry-run`, the `variable.pointer_prefix` header rename (UNIT-118) re-reads each companion `.h` file from disk, because it may already have been rewritten in this fix pass — the documented exception to SWE1-015
6. `--write-baseline`: write (UNIT-36) and return 0. `--baseline-file`: filter with UNIT-35 and UNIT-119
7. Apply `--warnings-as-errors`; emit JSON, SARIF or HTML output; print the summary (UNIT-40)
8. Return 1 if any error-severity violation remains, otherwise 0; configuration errors exit with 2

---

### UNIT-47 — `scripts/ci/append_trend_record.py` (script)

**Purpose:** Append one CI run record to `cstylecheck/trend.jsonl` on `gh-pages` (the naming-convention trend used by `cstylecheck_rules.yml`).

**Algorithm:** Read `RUN_NUMBER`, `SHA` (truncated to 8 characters), `ERRORS`, `WARNINGS`, `INFOS` and `FILES` from the environment set by the workflow step, build a JSON record and append it as one line to `trend.jsonl`.

---

### UNIT-48 — `scripts/ci/generate_trend.py` (script)

**Purpose:** Generate the gh-pages naming-convention trend dashboard (`cstylecheck/index.html`) and the shields.io badge JSON (`cstylecheck/badge.json`).

**Algorithm:** Read `trend.jsonl` and the latest-run counts from the environment, render the HTML trend page, and write a badge JSON whose message and colour reflect the latest error and warning counts.

---

### UNIT-49 — `scripts/ci/update_readme_badge.py` (script)

**Purpose:** Update the Naming Convention badge link in `README.md` of the source-branch worktree.

**Algorithm:** Take the worktree path (positional argument; exit 1 if it is missing) and `REPO` (environment), then build the shields.io endpoint badge and the gh-pages trend link. If `README.md` is missing, exit 0. Replace an existing `[![Naming Convention](…)](…)` badge, or insert one after the first heading, and write the file.

---

### UNIT-91 — `_find_default_rules() → Path`

**Purpose:** Locate the bundled default `rules.yml` for `--update-config`.

**Algorithm:** Return the first existing candidate: `src/rules.yml` (package parent), then `<package>/rules.yml`. Otherwise return `sysconfig data/share/cstylecheck/rules.yml` (the caller checks whether it exists).

---

### UNIT-92 — `_deep_merge(base: dict, override: dict) → dict`

**Purpose:** Pure recursive dictionary merge (user values win).

**Algorithm:** Copy *base*. For each key in *override*: if both values are dicts, recurse; otherwise take the *override* value. Return the new dict; the inputs are not mutated.

---

### UNIT-93 — `_collect_paths(d: dict, prefix: str = "") → list`

**Purpose:** List every dotted key path in a nested dict, used to report added and unknown keys.

**Algorithm:** Depth-first walk that appends `prefix.key` for every key and recurses into dict values. Return the paths sorted.

---

### UNIT-94 — `update_config(config_path: str) → int`

**Purpose:** Implement `--update-config`: add newly introduced default keys to a user `rules.yml`.

**Algorithm:**
1. Load the user config (return 2 if it is missing, unreadable, unparsable or not a mapping) and the bundled default (UNIT-91)
2. `added` = default paths − user paths; `unknown` = user paths − default paths (UNIT-93)
3. `merged = _deep_merge(default, user)` (UNIT-92); write it back with `yaml.dump(sort_keys=True)` (comments are not preserved)
4. Print the added keys and warn about unknown keys; return 0

---

### UNIT-128 — `Checker._check_goto_usage() → None`

**Purpose:** Enforce `misc.goto_usage` (SWE1-109, MISRA C:2012 Rule 15.1).

**Algorithm:** Return if `misc.goto_usage.enabled` is false. For each `\bgoto\b` match in `self.clean` (comments and strings already blanked), emit `misc.goto_usage` at the match offset with the configured severity (default `error`).

---

### UNIT-129 — `Checker._check_assignment_in_condition() → None`

**Purpose:** Enforce `misc.assignment_in_condition` (SWE1-110, MISRA C:2012 Rule 13.4).

**Algorithm:**
1. Return if disabled. For each `if (`, `while (` or `for (` in `self.clean`, find the matching `)` by paren-depth counting
2. For `for`, the condition is the text between the first and second top-level `;`; for `if` and `while`, it is the whole parenthesised text
3. Flag each `=` in the condition that is not part of `==`, `!=`, `<=`, `>=` or a compound assignment (lookbehind excludes `!<>=+-*/%&|^~`, lookahead excludes `=`); default severity `warning`

---

### UNIT-130 — `Checker._check_multiple_statements_per_line() → None`

**Purpose:** Enforce `misc.multiple_statements_per_line` (SWE1-111, Barr-C §3.2).

**Algorithm:** Return if disabled. For each line of `self.clean` that does not contain a `for (` header, flag every `;` followed (after optional whitespace) by an identifier start, `*` or `(`. Offsets are accumulated per line; default severity `warning`.

---

### UNIT-131 — `Checker._check_void_pointer() → None`

**Purpose:** Enforce `misc.void_pointer` (SWE1-112, MISRA C:2012 Rule 11.5).

**Algorithm:** Return if disabled. Flag every `\bvoid\s*\*` match in `self.clean` (declarations, parameters and casts alike); default severity `warning`.

---

### UNIT-132 — `Checker._check_recursive_function() → None`

**Purpose:** Enforce `misc.recursive_function` for direct recursion (SWE1-113, MISRA C:2012 Rule 17.2).

**Algorithm:**
1. Return if disabled. For each `name(…) {` function-definition match in `self.clean` where `name` is not a C keyword, find the matching `}` by brace-depth counting
2. Search the body for `\bname\s*\(`; on the first match emit `misc.recursive_function` at the call offset (default severity `error`)
3. Indirect recursion (A → B → A) is not detected (design limitation)

---

### UNIT-133 — `Checker._check_sizeof_type() → None`

**Purpose:** Enforce `misc.sizeof_type` (SWE1-114, Barr-C §5.7).

**Algorithm:** Return if disabled. Flag each `sizeof ( T [*…] )` where `T` is a primitive type (optionally `signed`/`unsigned`/`short`/`long`), a `*_t` typedef or a capitalised type name. Lower-case variable operands (`sizeof(buf)`, `sizeof(*p)`) do not match. Default severity `info`.

---

### UNIT-134 — `Checker._check_boolean_comparison() → None`

**Purpose:** Enforce `misc.boolean_comparison` (SWE1-115), a style rule against redundant comparison with a Boolean literal. It does not enforce MISRA C:2012 Rule 14.4 (`if (flag == true)` is compliant with it).

**Algorithm:** Return if disabled; `enabled` defaults to `false` when the key is absent (opt-in, #412). Flag each `==` or `!=` with the lowercase literal `true` or `false` on either side in `self.clean`; `TRUE`/`FALSE` macros are not matched (comparing an integer flag against `TRUE` is not redundant). Default severity `warning`. The message ends with "(redundant comparison with a Boolean literal)".

---

### UNIT-135 — `Checker._check_empty_else() → None`

**Purpose:** Enforce `misc.empty_else` (SWE1-116, Barr-C §8.3).

**Algorithm:** Return if disabled. For each `else { }` in `self.clean` whose braces contain only whitespace, re-examine the same span in the original `self.source`. If the original block contains anything other than whitespace (e.g. an `/* intentionally empty */` comment), skip it; otherwise emit `misc.empty_else` (default severity `warning`).

---

## 6. Data Design

### 6.1 Configuration Schema (YAML)

The top-level configuration keys and their types:

| Key | Type | Default | Purpose |
|---|---|---|---|
| `file_prefix.enabled` | `bool` | `true` | Master enable for module-prefix rules |
| `file_prefix.separator` | `str` | `"_"` | Separator between module prefix and identifier |
| `variables.enabled` | `bool` | `true` | Master enable for variable rules |
| `variables.case` | `str` | `"lower_snake"` | Default case for all variable scopes |
| `variables.min_length` | `int` | `3` | Minimum identifier length (Barr-C 7.1.e) |
| `variables.max_length` | `int` | `40` | Maximum identifier length |
| `variables.global.g_prefix.enabled` | `bool` | `true` | Enforce `g_` prefix on globals |
| `variables.static.s_prefix.enabled` | `bool` | `true` | Enforce `s_` prefix on file-statics |
| `variables.pointer_prefix.enabled` | `bool` | `true` | Enforce `p_` on single-pointer variables |
| `functions.style` | `str` | `"object_verb"` | Function naming style |
| `functions.static_prefix.enabled` | `bool` | `false` | Enforce static function prefix |
| `misc.line_length.max` | `int` | `120` | Maximum line length in characters |
| `misc.magic_numbers.enabled` | `bool` | `true` | Detect magic number literals |
| `misc.comment_ratio.enabled` | `bool` | `false` | Enforce minimum comment-to-code ratio |
| `misc.comment_ratio.warning_threshold` | `float` | `0.15` | Ratio below which a warning is emitted |
| `misc.comment_ratio.error_threshold` | `float` | `0.05` | Ratio below which an error is emitted |
| `misc.whitespace_ratio.enabled` | `bool` | `false` | Enforce minimum blank-line-to-code-line ratio |
| `misc.whitespace_ratio.warning_threshold` | `float` | `0.10` | Ratio below which a warning is emitted |
| `misc.whitespace_ratio.error_threshold` | `float` | `0.02` | Ratio below which an error is emitted |
| `misc.whitespace_ratio.min_lines` | `int` | `10` | Minimum code lines before ratio is enforced |
| `misc.lowercase_l_suffix.enabled` | `bool` | `true` | Detect `l` suffix on integer literals (MISRA 7.3) |
| `misc.octal_constant.enabled` | `bool` | `true` | Detect octal constants (MISRA 7.1) |
| `misc.trigraph.enabled` | `bool` | `true` | Detect trigraph sequences (MISRA 4.2) |
| `misc.declared_not_defined.enabled` | `bool` | `false` | Cross-file declared-but-not-defined check |
| `misc.goto_usage.enabled` / `.severity` | `bool` / `str` | `true` / `error` | Flag `goto` (MISRA 15.1) |
| `misc.assignment_in_condition.enabled` / `.severity` | `bool` / `str` | `true` / `warning` | Flag `=` in conditions (MISRA 13.4) |
| `misc.multiple_statements_per_line.enabled` / `.severity` | `bool` / `str` | `true` / `warning` | One statement per line (Barr-C §3.2) |
| `misc.void_pointer.enabled` / `.severity` | `bool` / `str` | `true` / `warning` | Flag `void *` (MISRA 11.5) |
| `misc.recursive_function.enabled` / `.severity` | `bool` / `str` | `true` / `error` | Flag direct recursion (MISRA 17.2) |
| `misc.sizeof_type.enabled` / `.severity` | `bool` / `str` | `true` / `info` | Flag `sizeof(type)` (Barr-C §5.7) |
| `misc.boolean_comparison.enabled` / `.severity` | `bool` / `str` | `false` / `warning` | Flag `== true/false`, lowercase literals only (style rule, opt-in, #412) |
| `misc.empty_else.enabled` / `.severity` | `bool` / `str` | `true` / `warning` | Flag empty `else {}` (Barr-C §8.3) |
| `sign_compatibility.enabled` | `bool` | `true` | Cross-file sign-compatibility check |
| `sign_compatibility.plain_char_is_signed` | `bool` | `true` | Treat plain `char` as signed |
| `spell_check.enabled` | `bool` | `false` | Enable comment spell-check |

### 6.2 Violation Data Class

```
Violation:
  filepath : str   — absolute or relative path to source file
  line     : int   — 1-based line number
  col      : int   — 1-based column number
  severity : str   — one of: "error" | "warning" | "info"
  rule     : str   — dot-separated rule ID (e.g. "variable.global.case")
  message  : str   — human-readable description of the violation
```

### 6.3 Baseline File Format

```json
{
  "violations": [
    {
      "file": "src/uart.c",
      "line": 42,
      "rule": "variable.global.case",
      "message": "'UartGlobalCount' should be lower_snake"
    }
  ]
}
```

Written by `write_baseline()` (UNIT-36) and read by `load_baseline()` (UNIT-35). `file` is normalised to `/` separators (UNIT-120). `line` is informational only and is not used for matching (SWE1-100). Matching uses the key `file:rule:message` as a multiset (UNIT-37, UNIT-119).

---

## 7. Resource Usage

| Resource | Usage | Notes |
|---|---|---|
| Memory | O(N) where N = total source characters | Source cache holds raw text for all files |
| CPU | O(N × R) where R = number of enabled rules | Each rule applies one or more regex passes |
| Disk I/O | One read per source file | Cache eliminates second read for sign-compatibility check |
| File handles | One at a time (sequential) | No concurrent file access |

---

## 8. Traceability: SW Requirements → Units

| SW-REQ-ID | Requirement Area | Implementing Units |
|---|---|---|
| SWE1-001 to SWE1-002 | Config loading | UNIT-05 |
| SWE1-003 | Defines substitution | UNIT-09, UNIT-10 |
| SWE1-004 | Alias file | UNIT-06 |
| SWE1-005 to SWE1-006 | exclusions | UNIT-07, UNIT-08 |
| SWE1-007 to SWE1-010 | Dictionary management | UNIT-11, UNIT-12, UNIT-13, UNIT-50 |
| SWE1-011 to SWE1-016 | Source parsing | UNIT-14, UNIT-15, UNIT-16, UNIT-17, UNIT-18, UNIT-19, UNIT-20, UNIT-56 |
| SWE1-017 to SWE1-029 | Variable rules | UNIT-23, UNIT-43, UNIT-44, UNIT-45, UNIT-53, UNIT-54, UNIT-55 |
| SWE1-030 to SWE1-034 | Function rules | UNIT-24, UNIT-64 |
| SWE1-035 to SWE1-039 | Constant/macro rules | UNIT-25 |
| SWE1-040 to SWE1-042 | Type rules | UNIT-26, UNIT-27, UNIT-28 |
| SWE1-043 to SWE1-044 | Include guard rules | UNIT-29 |
| SWE1-045 to SWE1-050, SWE1-071 | Miscellaneous rules | UNIT-30, UNIT-31, UNIT-65, UNIT-66, UNIT-67, UNIT-68, UNIT-90 |
| SWE1-051 to SWE1-053 | Cross-file sign check | UNIT-34, UNIT-73, UNIT-74, UNIT-75, UNIT-76, UNIT-77, UNIT-78, UNIT-79, UNIT-80, UNIT-81, UNIT-82, UNIT-83 |
| SWE1-054 to SWE1-056 | Reserved names / spell | UNIT-32, UNIT-33, UNIT-51, UNIT-69, UNIT-70 |
| SWE1-057 | Text output | UNIT-41 |
| SWE1-058 to SWE1-059 | JSON output | UNIT-38 |
| SWE1-060 | SARIF output | UNIT-39 |
| SWE1-061 | GitHub annotations | UNIT-42, UNIT-89 |
| SWE1-062 | Log file mirroring (`Tee`) | UNIT-86 |
| SWE1-063 | Summary | UNIT-40 |
| SWE1-064 | Copyright header check | UNIT-52, UNIT-63 |
| SWE1-065 to SWE1-067, SWE1-100, SWE1-101 | Baseline | UNIT-35, UNIT-36, UNIT-37, UNIT-119, UNIT-120 |
| SWE1-068 to SWE1-070 | CLI / entry point | UNIT-01, UNIT-02, UNIT-03, UNIT-04, UNIT-46, UNIT-87, UNIT-88 |
| SWE1-072 to SWE1-073 | Inline suppression comments | UNIT-95 |
| SWE1-074 | Auto-fix mode | UNIT-96, UNIT-97 |
| SWE1-075 | Config wizard and presets | UNIT-98, UNIT-99 |
| SWE1-076 | Per-directory config | UNIT-100 |
| SWE1-077 | HTML report output | UNIT-101 |
| SWE1-078 | Function length | UNIT-102 |
| SWE1-079 | Function doc header | UNIT-103 |
| SWE1-080 | Assert density | UNIT-104 |
| SWE1-081 | Null statement comment | UNIT-105 |
| SWE1-082 | Declaration spacing | UNIT-106 |
| SWE1-083 | File length | UNIT-107 |
| SWE1-084 | Reserved header name | UNIT-108 |
| SWE1-085 | Macro trailing semicolon | UNIT-109 |
| SWE1-086 | Macro multistatement wrapper | UNIT-110 |
| SWE1-087 | Identifier length | UNIT-111 |
| SWE1-088 | No single-char identifiers | UNIT-112 |
| SWE1-MISRA-001 to SWE1-MISRA-003 | MISRA lexical rules (Rule 7.3, 7.1, 4.2) | UNIT-66, UNIT-67, UNIT-68 |
| SWE1-MISRA-004 | Non-ASCII source characters (Rule 4.1) | UNIT-113 |
| SWE1-089 | Per-file breakdown in print_summary | UNIT-114 |
| SWE1-090 | Typedef-alias constant.case exemption | UNIT-115 |
| SWE1-091 | `misc.constant_comparison` | UNIT-116 |
| SWE1-092 | `misc.unsigned_suffix` signed-param exemption | UNIT-30 (extended) |
| SWE1-093 | `variable.pointer_prefix` auto-fix | UNIT-117, UNIT-118 |
| SWE1-094 | Two-line startup banner to stderr (and `--log`), unconditional | UNIT-46 (extended) |
| SWE1-095 | Copyright in `--version` output | UNIT-88 (extended) |
| SWE1-096 | OS-native path separator | UNIT-03 (`os.path.normpath` in `discover_files`), UNIT-41 (extended) |
| SWE1-097 | `print_summary()` restructure | UNIT-40 (extended) |
| SWE1-098 | `fn_start` line correction | UNIT-24 (extended) |
| SWE1-099 | Function-pointer typedef exemption | UNIT-23 (extended) |
| SWE1-102 | Trend metrics — LOC classification | UNIT-121, UNIT-122, UNIT-125 |
| SWE1-103 | Trend metrics — cyclomatic complexity / nesting | UNIT-121, UNIT-123, UNIT-125 |
| SWE1-104 | Trend metrics — size | UNIT-123, UNIT-125 |
| SWE1-105 | Trend metrics — documentation coverage | UNIT-123, UNIT-125 |
| SWE1-106 | Trend metrics — coupling | UNIT-123, UNIT-124, UNIT-125 |
| SWE1-107 | Trend metrics — violation quality | UNIT-126 |
| SWE1-108 | Trend metrics — backward-compatible data points, charts, wiki | UNIT-125, UNIT-127 |
| SWE1-109 | misc.goto_usage | UNIT-128 |
| SWE1-110 | misc.assignment_in_condition | UNIT-129 |
| SWE1-111 | misc.multiple_statements_per_line | UNIT-130 |
| SWE1-112 | misc.void_pointer | UNIT-131 |
| SWE1-113 | misc.recursive_function | UNIT-132 |
| SWE1-114 | misc.sizeof_type | UNIT-133 |
| SWE1-115 | misc.boolean_comparison | UNIT-134 |
| SWE1-116 | misc.empty_else | UNIT-135 |
| SWE1-117 | Trend metrics — safety indicators and macro metrics | UNIT-125, UNIT-127 |

> **Note (UNIT-84):** `DeclaredNotDefinedChecker` (UNIT-84) is traced via the cross-file check requirement (SWE1-051 to SWE1-053 range). SWE1-071 maps exclusively to `_check_whitespace_ratio` (UNIT-90) as shown in the `SWE1-045 to SWE1-050, SWE1-071` row above; the duplicate mapping of SWE1-071 → UNIT-84 has been removed as a CSC-AUD-005 corrective action.

---

## 9. Review & Approval

| Role | Name | Signature / Electronic Approval | Date |
|---|---|---|---|
| Author | Claude | Approved | 2026-09-29 |
| Technical Reviewer | Dermot Murphy | — | *pending* |
| Quality Assurance | Dermot Murphy | — | *pending* |
| Approver | Dermot Murphy | — | *pending* |

> **Note:** This document is under configuration management (SUP.8). Post-approval changes require a change request (SUP.10) and a new document version.
