# Software Version Description

*Automotive SPICE® PAM v4.0 | SUP.8 Configuration Management — Release Artefact*

---

## 1. Document Identification & Control

| Field | Value | Field | Value |
|---|---|---|---|
| **Document ID** | CSC-SVD-001 | **Version** | 1.35 |
| **Project** | CStyleCheck | **Date** | 2026-11-20 |
| **Status** | Released | **Classification** | Internal |
| **Author** | Claude | **Reviewer** | Dermot Murphy |
| **Approver** | Dermot Murphy | **Related Process** | SUP.8 |

---

## 2. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.35 | 2026-11-20 | Claude | v2.0.0 release (Major), CR #443 — §4.1 version, git tag, release date, release type and previous release (v1.6.1); §4.2 classification (breaking changes #422, #423, #424, #425; opt-in rules #412, #418, #420; 83 rule IDs); §5.1 `_version.py` 2.0.0 and 83 rule implementations; §5.2 Docker tags 2.0.0 / 2.0 / 2; §5.3 `update_readme_badge.py` removed (#449), `aspice_check.py` and the trend-metrics scripts added (#437, #388); §5.4 test table 1281→1671 tests, 53→60 modules; §6.7 v2.0.0 change summary (C-001 to C-005, F-026 to F-033, B-013 to B-023, P-001 to P-006, D-014); §7 rule count; §8 CI checks, test count and tag; §9 upgrade notes from v1.6.x with the breaking changes; §10 configuration items 2.0.0; baseline notes; approval by merge (CSC-DEV-002 §5.2) |
| 1.34 | 2026-11-19 | Claude | Cross-reference version resync with the #460 to #463 review fixes (`783b5a4`): referenced-document versions set to the current baseline; no technical content change |
| 1.33 | 2026-11-19 | Claude | Cross-reference version resync with #460 to #463 (CR-461, CR-462): referenced-document versions set to the current baseline; no technical content change |
| 1.32 | 2026-11-19 | Claude | Cross-reference version resync with #458 (CSC-SUP10-001 CR-441 and CR-456 closed) |
| 1.31 | 2026-11-19 | Claude | Cross-reference version resync with #456 |
| 1.30 | 2026-11-19 | Claude | Cross-reference version resync with #453 (CSC-SUP8-001 §7.1/§7.5 ruleset wording) |
| 1.29 | 2026-11-19 | Claude | Cross-reference version resync with #449: referenced-document versions set to the current baseline; no technical content change |
| 1.28 | 2026-10-06 | Claude | Cross-reference version resync with #447: referenced-document versions set to the current baseline; no technical content change |
| 1.27 | 2026-10-06 | Claude | v1.6.1 hotfix back-merge (`main` into `develop`, #439, #444): the v1.6.1 release identification, §4.2 classification, §5.4 test table (`test_cli.py` 45), §6.6 change summary (B-012, D-013), §8 and §9 brought into `develop` from the v1.6.1 release; no change to post-v1.6.0 `develop` content |
| 1.26 | 2026-09-30 | Claude | Cross-reference version resync (#437): referenced-document versions set to the current baseline after the merge-time process-control changes; no technical content change |
| 1.25 | 2026-09-30 | Claude | Cross-reference version resync (#435): all referenced-document versions set to the current baseline (every controlled work product bumped once in this change set); no technical content change; SVD synchronised to the current `develop` baseline, CSC-DEV-001/002 IDs corrected, next release planned as v2.0.0 |
| 1.24 | 2026-09-29 | Claude | Approval-by-merge policy (CSC-DEV-002 §5.2), #430: Review & Approval table entries set to approval by the owner's merge of the introducing PR |
| 1.23 | 2026-07-06 | Claude | ASPICE audit — cascade version updates: SWE1→2.6, SWE2→1.12, SWE3→1.16, SWE4→1.20, SWE5→1.14, SWE6→1.16, SYS2→2.2, SYS3→1.6, SYS4→1.11, SYS5→1.8, SUP8→1.11, SUP1→1.9, MAN3→1.7, PA2→1.22 — closes #379 |
| 1.22 | 2026-07-06 | Claude | v1.6.0 RC doc update — test count 1223→1279 (56 new tests across 8 modules); add D-012–D-016 for startup banner, copyright, path-sep fix, non-ASCII fix, fn_start fix, inline suppression fixes, yoda/constant-case fixes; update CHANGELOG.md ref to v1.6.0 |
| 1.21 | 2026-07-01 | Claude | v1.6.0 release — update version, rule count 72→73, test count 1183→1223, add F-020/F-021/F-022; update §3.1/§5.5/§10 doc version refs |
| 1.20 | 2026-06-27 | Cascade: SYS2→2.1, SUP1→1.8 | Dermot Murphy |
| 1.19 | 2026-06-27 | Cascade cross-ref update: SWE1→2.4, SWE2→1.11, SWE3→1.15, SWE4→1.17, SWE5→1.11, SWE6→1.13, SUP8→1.9 | Dermot Murphy |
| 1.18 | 2026-06-27 | Cascade cross-ref update: SWE1→2.3, SWE2→1.10, SWE3→1.14, SWE4→1.16, SWE5→1.10, SWE6→1.12, SYS4→1.9 | Dermot Murphy |
| 1.17 | 2026-06-27 | Claude | ASPICE audit — update §3.1/§5.5/§10 doc version refs (SWE1 2.1→2.2, SWE3 1.12→1.13, SWE4 1.14→1.15, SWE6 1.10→1.11, SYS2 1.9→2.0, SYS4 1.7→1.8, SUP8 1.7→1.8); update approval dates — closes #315 #316 #317 #318 #319 #320 #321 #322 #323 |
| 1.16 | 2026-06-26 | Claude | ASPICE audit corrections — update §3.1/§5.5/§10 doc version refs (SWE1 2.0→2.1, SWE2 1.8→1.9, SWE3 1.11→1.12, SWE4 1.13→1.14, SWE5 1.8→1.9, SWE6 1.9→1.10, SUP1 1.6→1.7, SYS2 1.6→1.9, SYS4 1.6→1.7); update test count 1182→1183 throughout — closes #302 #303 #304 #305 #306 #307 #308 #309 #310 #311 #312 |
| 1.15 | 2026-06-26 | Claude | v1.5.0 release — update all version identifiers, release summary, change log, upgrade notes |
| 1.14 | 2026-06-26 | Claude | Complete v1.4.1 content (PR #295) — add F-017/F-018/F-019; update rule count 71→72, test count 1157→1182, module count 49→50; sync §3.1/§5.4/§5.5/§6/§8 doc version refs; correct rule count throughout |
| 1.13 | 2026-06-25 | Claude | Doc accuracy — sync §5.5 document version table to v1.4.1 baseline (CSC-SYS5-001/CSC-SWE6-001 → 1.7, CSC-PA2-001 → 1.13, self → 1.13) |
| 1.12 | 2026-06-25 | Claude | Correct rule count 75→71 throughout (§4.2, §5.1, §8.2, §9): 71 is the confirmed count from source-code analysis |
| 1.11 | 2026-06-18 | Claude | v1.4.1 patch release — fix `variable.parameter.p_prefix` false positive on call statements (issue #273); update version identifiers, release summary, change log |
| 1.10 | 2026-06-18 | Claude | v1.4.0 release — update all version identifiers, release summary, change log, upgrade notes |
| 1.9 | 2026-06-18 | Claude | ASPICE audit #254 — fix internally inconsistent test counts: §3/§5.4/§8.2/§9 now all read 1152 tests / 49 modules (previously a mix of 1143 and stale 1041) |
| 1.8 | 2026-06-08 | Claude | ASPICE audit #238 — update SWE1/SWE3/SWE4 version refs; correct rule count 53→64; update test count 1041→1143, 38→49 modules |
| 1.7 | 2026-06-05 | Claude | v1.3.0 release — update all version identifiers, release summary, change log, upgrade notes |
| 1.6 | 2026-06-05 | Claude | CSC-AUD-005 corrective action — fix factual errors identified in audit |
| 1.5 | 2026-06-04 | Claude | Add §6.1 F-008 to F-012 for five new features (inline suppression, --fix, --init/--preset, per-dir config, HTML output); update §5.1 deliverables, §5.5 doc versions, §10 traceability — issues #188 #189 #190 #193 #192 |
| 1.4 | 2026-06-04 | Claude | Deep accuracy audit: update §3.1, §5.5, §10 document version tables to reflect post-audit versions — resolves issue #163 |
| 1.3 | 2026-06-04 | Claude | Automated accuracy audit: test count 839→965 (33 modules), add missing test modules to §5.4, fix SWE6 version in §5.5, update §8.2 and §10 — resolves issue #163 |
| 1.2 | 2026-05-29 | Claude | Updated for v1.2.0 release — package refactor, 3 new rules, 839 tests |
| 1.1 | 2026-05-28 | Claude | Initial SVD document created for v1.1.0 release |

---

## 3. Purpose & Scope

This **Software Version Description (SVD)** formally describes the **CStyleCheck v2.0.0** software release. It identifies the software items delivered, the baseline against which changes are recorded, and the configuration status of all controlled work products.

This document satisfies the release-identification and configuration-status-accounting requirements of **Automotive SPICE® PAM v4.0, SUP.8 — Configuration Management**.

### 3.1 Referenced Documents

> **Baseline note (v2.0.0, 2026-11-20):** the document versions below are the v2.0.0 release baseline (CR #443).

| Document ID | Title | Version |
|---|---|---|
| CSC-SWE1-001 | CStyleCheck Software Requirements Specification | 2.32 |
| CSC-SWE2-001 | CStyleCheck Software Architecture Design | 1.36 |
| CSC-SWE3-001 | CStyleCheck Software Detailed Design | 1.42 |
| CSC-SWE4-001 | CStyleCheck Software Unit Verification Specification | 1.48 |
| CSC-SWE5-001 | CStyleCheck Software Integration Test Specification | 1.37 |
| CSC-SWE6-001 | CStyleCheck Software Qualification Test Specification | 1.40 |
| CSC-SUP8-001 | CStyleCheck Configuration Management Plan | 1.34 |
| CSC-SUP1-001 | CStyleCheck Quality Assurance Plan | 1.30 |
| CSC-MAN3-001 | CStyleCheck Project Management Plan | 1.30 |

---

## 4. Software Version Identification

### 4.1 Release Summary

| Field | Value |
|---|---|
| **Product Name** | CStyleCheck |
| **Version** | 2.0.0 |
| **Release Date** | 2026-11-20 |
| **Release Type** | Major Release |
| **Git Tag** | `v2.0.0` — annotated release baseline tag on the `main` merge commit of `release/2.0.0`, created after the merge (CSC-SUP8-001 §8.2) |
| **Branch** | `main` (from `release/2.0.0`, cut from `develop`) |
| **Previous Release** | v1.6.1 (2026-10-06, tag `v1.6.1` on `be797a5`) |
| **Change Request** | [#443](https://github.com/dermot-murphy/CStyleCheck/issues/443) (release CR) |
| **Repository** | https://github.com/dermot-murphy/CStyleCheck |

### 4.2 Release Classification

This is a **major release** under Semantic Versioning (CSC-SUP10-001 §5.6; decision in
CSC-SUP10-001 §7.2). It is **not fully backward-compatible** with v1.6.x: after upgrading,
a project can see new findings, a configuration error or a different exit code. The
breaking changes are (§6.7.1):

- **Unknown case-style values are rejected (#422)** — a case-style value that is not a
  canonical name or an accepted alias is a configuration error (`ERROR:` on stderr, exit 2).
- **Configuration and usage errors exit 2, not 1 (#425)** — from the installed `cstylecheck`
  command as well as `python src/cstylecheck.py`.
- **The last enum member is checked (#423)** — new `enum.member_case` /
  `enum.member_prefix` findings are possible.
- **`functions.case` is removed (#424)** — the key is ignored with a `WARNING`; use
  `functions.style`.
- **New rules are opt-in (#412, #418, #420)** — the 10 rules added since v1.6.1 ship
  `enabled: false`; `--preset misra` / `--preset barr-c` and `--init` enable the rules of
  the chosen standard.

v2.0.0 adds 10 rule IDs, all disabled by default: 8 MISRA C / Barr-C rules (#391, #392)
and the 2 partially-initialised local struct rules (#456, extended by #460 to #463),
reaching **83 rule IDs** total. It also creates missing output folders (#441), matches
baselines without line numbers (#394, #395), and adds trend-analysis metrics (#388) and
merge-time ASPICE consistency checks (#437). With the shipped defaults, upgrading adds no
findings from the new rules.

v1.6.1 (the previous release, 2026-10-06) was a patch (hotfix) release of v1.6.0 that kept
the startup banner out of a json / sarif / html `--log` file (#439, §6.6); v1.6.0 added
`misc.constant_comparison`, the `misc.unsigned_suffix` signed-parameter exemption and
`--fix` support for `variable.pointer_prefix` (73 rule IDs, §6.5).

---

## 5. Delivered Software Items

### 5.1 Primary Deliverable

| Item | Description | Location |
|---|---|---|
| `src/cstylecheck.py` | Thin CLI shim — backward-compatible entry point | `src/cstylecheck.py` |
| `src/cstylecheck/__init__.py` | Package root — re-exports full public API | `src/cstylecheck/__init__.py` |
| `src/cstylecheck/cli.py` | Argument parsing and file discovery | `src/cstylecheck/cli.py` |
| `src/cstylecheck/config.py` | Rule configuration loading (YAML, defines, aliases, exclusions) | `src/cstylecheck/config.py` |
| `src/cstylecheck/models.py` | Violation, CheckResult, shared constants | `src/cstylecheck/models.py` |
| `src/cstylecheck/preprocessor.py` | Comment/string stripping, token extraction | `src/cstylecheck/preprocessor.py` |
| `src/cstylecheck/utils.py` | Case matching helpers, module-name derivation | `src/cstylecheck/utils.py` |
| `src/cstylecheck/checker.py` | Main Checker class — all 83 rule implementations | `src/cstylecheck/checker.py` |
| `src/cstylecheck/sign_checker.py` | Cross-file sign-compatibility and declared_not_defined | `src/cstylecheck/sign_checker.py` |
| `src/cstylecheck/baseline.py` | Baseline load / write | `src/cstylecheck/baseline.py` |
| `src/cstylecheck/output.py` | Text / JSON / SARIF / HTML formatters, Tee, summary table | `src/cstylecheck/output.py` |
| `src/cstylecheck/fixer.py` | Auto-fix engine: apply_fixes, unified_diff (`--fix`, `--dry-run`, `--safe-only`) | `src/cstylecheck/fixer.py` |
| `src/cstylecheck/wizard.py` | Config wizard and preset writer (`--init`, `--preset`) | `src/cstylecheck/wizard.py` |
| `src/rules.yml` | Rule configuration for the CStyleCheck project | `src/rules.yml` |
| `src/_version.py` | Version string: `2.0.0` (generated by CI: `git describe --tags`) | `src/_version.py` |
| `src/aliases.txt` | Module alias map | `src/aliases.txt` |
| `src/exclusions.yml` | Per-file rule suppressions | `src/exclusions.yml` |
| `src/options.txt` | Project defaults for `--options-file` | `src/options.txt` |
| `src/defines.txt` | Keyword/type aliases for `--defines` | `src/defines.txt` |
| `src/copyright_header.txt` | Copyright block template for `--copyright` | `src/copyright_header.txt` |
| `src/c_keywords.txt` | C/C++ keyword list for `--keywords-file` | `src/c_keywords.txt` |
| `src/c_stdlib_names.txt` | C stdlib name list for `--stdlib-file` | `src/c_stdlib_names.txt` |
| `src/c_spell_dict.txt` | Spell-check dictionary for `--spell-dict` | `src/c_spell_dict.txt` |

### 5.2 Docker Image

| Registry | Image | Tags |
|---|---|---|
| Docker Hub | `dermotmurphy/cstylecheck` | `2.0.0`, `2.0`, `2`, `latest` |
| GitHub Container Registry | `ghcr.io/dermot-murphy/cstylecheck` | `2.0.0`, `2.0`, `2`, `latest` |

Platforms: `linux/amd64`, `linux/arm64`.

### 5.3 CI / Automation Scripts

| Item | Description |
|---|---|
| `scripts/ci/append_trend_record.py` | Appends JSON record to `gh-pages/cstylecheck/trend.jsonl` |
| `scripts/ci/generate_trend.py` | Regenerates `gh-pages/cstylecheck/index.html` and `badge.json` |
| `scripts/aspice_check.py` | ASPICE work-product consistency check, run on every pull request by `aspice_consistency.yml` (#437) |
| `scripts/collect_metrics.py`, `scripts/generate_charts.py`, `scripts/update_wiki_metrics.py`, `scripts/compare_metrics.py` | Trend-analysis metrics and charts (`metrics.yml`, #388) |

`scripts/ci/update_readme_badge.py` was removed in v2.0.0: the README *Naming Convention* badge is a fixed shields.io endpoint URL, so no workflow pushes to `develop` or `main` (#449).

### 5.4 Test Suite

**Total: 1671 tests across 60 modules** — all passing.

| Item | Test Count | Description |
|---|---|---|
| `tests/test_barr_c.py` | 42 | Barr-C naming rules |
| `tests/test_yoda_condition.py` | 46 | misc.yoda_condition |
| `tests/test_reserved_name.py` | 40 | reserved_name |
| `tests/test_dictionaries.py` | 32 | dict file loading and CLI flags |
| `tests/test_misc_improvements.py` | 77 | unsigned_suffix, loop vars, numerics |
| `tests/test_defines.py` | 30 | constant.* / macro.* |
| `tests/test_variables.py` | 43 | all variable.* rules |
| `tests/test_functions.py` | 14 | function.* |
| `tests/test_typedefs.py` | 8 | typedef.* |
| `tests/test_enums.py` | 24 | enum.* (last member checked, v2.0.0, #423) |
| `tests/test_structs.py` | 12 | struct.* |
| `tests/test_include_guards.py` | 8 | include_guard.* |
| `tests/test_misc.py` | 28 | line_length / indentation / magic / suffix |
| `tests/test_spell_check.py` | 9 | spell_check |
| `tests/test_sign_compatibility.py` | 7 | cross-file sign compatibility |
| `tests/test_block_comment_spacing.py` | 29 | misc.block_comment_spacing |
| `tests/test_copyright_header.py` | 55 | misc.copyright_header |
| `tests/test_eof_comment.py` | 33 | misc.eof_comment |
| `tests/test_cli.py` | 45 | CLI flags end-to-end (incl. startup banner in `--log`, v1.6.1) |
| `tests/test_improvements.py` | 80 | bugs + new feature regression tests |
| `tests/test_comment_ratio.py` | 24 | misc.comment_ratio (new in v1.2.0) |
| `tests/test_whitespace_ratio.py` | 27 | misc.whitespace_ratio (new in v1.2.0) |
| `tests/test_declared_not_defined.py` | 39 | misc.declared_not_defined (new in v1.2.0) |
| `tests/test_misra_rules.py` | 168 | MISRA C rule coverage, incl. the 8 opt-in MISRA C / Barr-C rules (v2.0.0) |
| `tests/test_parameter_prefix.py` | 51 | variable.parameter.* rules |
| `tests/test_exclusions.py` | 28 | per-file rule suppression |
| `tests/test_github_annotations.py` | 8 | GitHub Actions annotation output |
| `tests/test_case_patterns.py` | 6 | case-pattern helper functions |
| `tests/test_thread_safe_globals.py` | 4 | thread-safety of shared globals |
| `tests/test_preprocessor.py` | 76 | preprocessor.py — strip_comments, strip_strings, preprocess, build_line_map, etc. |
| `tests/test_config_loading.py` | 13 | config.py — load_config UTF-8 handling, missing file, YAML errors |
| `tests/test_update_config.py` | 27 | config.py — _deep_merge function |
| `tests/test_workflow_config.py` | 21 | CI workflow configuration regression tests |
| `tests/test_inline_suppression.py` | 24 | Inline suppression comments — `//` and `/* */` syntax (`parse_inline_suppressions`) |
| `tests/test_fix_mode.py` | 11 | Auto-fix engine (`apply_fixes`, `unified_diff`) |
| `tests/test_init_wizard.py` | 33 | Config wizard and presets (`run_wizard`, `run_preset`) |
| `tests/test_per_dir_config.py` | 15 | Per-directory config resolution (`resolve_per_dir_config`) |
| `tests/test_html_report.py` | 20 | HTML report output (`_violations_to_html`) |
| `tests/test_function_length.py` | 11 | `misc.function_length` rule |
| `tests/test_function_doc_header.py` | 12 | `misc.function_doc_header` rule |
| `tests/test_assert_density.py` | 8 | `misc.assert_density` rule |
| `tests/test_null_statement_comment.py` | 11 | `misc.null_statement_comment` rule |
| `tests/test_declaration_spacing.py` | 8 | `misc.declaration_spacing` rule |
| `tests/test_file_length.py` | 8 | `misc.file_length` rule |
| `tests/test_reserved_header_name.py` | 10 | `misc.reserved_header_name` rule |
| `tests/test_macro_trailing_semicolon.py` | 9 | `macro.trailing_semicolon` rule |
| `tests/test_macro_multistatement_wrapper.py` | 9 | `macro.multistatement_wrapper` rule |
| `tests/test_identifier_length.py` | 10 | `naming.identifier_length` rule |
| `tests/test_no_single_char_identifiers.py` | 8 | `naming.no_single_char_identifiers` rule |
| `tests/test_print_summary.py` | 11 | `print_summary` per-file breakdown and section labels |
| `tests/test_constant_comparison.py` | 37 | `misc.constant_comparison` rule (new in v1.6.0; `#if` / `#elif` skipped in v2.0.0, #447) |
| `tests/test_unsigned_suffix_signed_params.py` | 15 | `misc.unsigned_suffix` signed-param exemption (new in v1.6.0) |
| `tests/test_pointer_prefix_fix.py` | 20 | `variable.pointer_prefix` auto-fix mode (new in v1.6.0) |
| `tests/test_case_style_config.py` | 27 | Case-style aliases and rejection of unknown names (new in v2.0.0, #422) |
| `tests/test_functions_case_removed.py` | 16 | `functions.case` removal warning (new in v2.0.0, #424) |
| `tests/test_exit_code_entry_points.py` | 8 | Exit code 2 for config / usage errors from both entry points (new in v2.0.0, #425) |
| `tests/test_output_dirs.py` | 11 | Missing output folders created (new in v2.0.0, #441) |
| `tests/test_partial_struct.py` | 89 | `misc.partial_struct_assignment` / `misc.partial_struct_initialiser` (new in v2.0.0, #456, #460 to #463) |
| `tests/test_collect_metrics.py` | 54 | Trend-analysis metrics scripts (new in v2.0.0, #388) |
| `tests/test_cli_requirements.py` | 22 | Unit tests for SWE1-015, SWE1-094, SWE1-096 (new in v2.0.0, #407, #413, #439) |
| **Total** | **1671** | |

### 5.5 Documentation

> **Baseline note (v2.0.0, 2026-11-20):** the document versions below are the v2.0.0 release baseline (CR #443).

| Document ID | Title | Version |
|---|---|---|
| CSC-SVD-001 | Software Version Description (this document) | 1.35 |
| CSC-SWE1-001 | Software Requirements Specification | 2.32 |
| CSC-SWE2-001 | Software Architecture Design | 1.36 |
| CSC-SWE3-001 | Software Detailed Design | 1.42 |
| CSC-SWE4-001 | Software Unit Verification Specification | 1.48 |
| CSC-SWE5-001 | Software Integration Test Specification | 1.37 |
| CSC-SWE6-001 | Software Qualification Test Specification | 1.40 |
| CSC-SYS2-001 | System Requirements Specification | 2.25 |
| CSC-SYS3-001 | System Architecture Design | 1.27 |
| CSC-SYS4-001 | System Integration Test Specification | 1.34 |
| CSC-SYS5-001 | System Verification Specification | 1.31 |
| CSC-MAN3-001 | Project Management Plan | 1.30 |
| CSC-MAN5-001 | Risk Management Plan | 1.25 |
| CSC-SUP1-001 | Quality Assurance Plan | 1.30 |
| CSC-SUP8-001 | Configuration Management Plan | 1.34 |
| CSC-SUP9-001 | Problem Resolution Plan | 1.24 |
| CSC-SUP10-001 | Change Request Plan | 1.26 |
| CSC-ACQ4-001 | Supplier Monitoring Plan | 1.24 |
| CSC-PA2-001 | Capability Level 2 Records | 1.45 |
| CSC-DEV-001 | AI Authorship Deviation Record | 1.22 |
| CSC-DEV-002 | Independent Review Deviation Record | 1.22 |

---

## 6. Change Summary (v1.3.0 → v2.0.0)

### 6.1 New Features

| ID | Description | Issue |
|---|---|---|
| F-006 | `macro.trailing_semicolon` — flags `#define` macros whose expansion ends with a semicolon, preventing double-semicolon and dangling-else bugs at the call site | [#228](https://github.com/dermot-murphy/CStyleCheck/issues/228) |
| F-007 | `macro.multistatement_wrapper` — enforces that function-like macros containing multiple statements are wrapped in `do { ... } while (0)` for safe use in `if`/`else` branches | [#229](https://github.com/dermot-murphy/CStyleCheck/issues/229) |
| F-008 | `misc.function_length` — configurable maximum function body line count; supports `count_comments: false` to exclude blank and comment-only lines | [#221](https://github.com/dermot-murphy/CStyleCheck/issues/221) |
| F-009 | `misc.function_doc_header` — requires a Doxygen-style `@brief`/`@param`/`@return` block comment before each non-static function definition (disabled by default) | [#222](https://github.com/dermot-murphy/CStyleCheck/issues/222) |
| F-010 | `misc.assert_density` — enforces a minimum number of `assert()` calls per qualifying function; supports per-function exemption via regex patterns (disabled by default) | [#225](https://github.com/dermot-murphy/CStyleCheck/issues/225) |
| F-011 | `misc.null_statement_comment` — requires a comment whenever a null statement (`while (x) ;`, standalone `;`) is used | [#227](https://github.com/dermot-murphy/CStyleCheck/issues/227) |
| F-012 | `misc.declaration_spacing` — enforces a blank line between variable declarations and the first executable statement in a function body (disabled by default) | [#224](https://github.com/dermot-murphy/CStyleCheck/issues/224) |
| F-013 | `misc.file_length` — configurable maximum total lines per source file; supports excluding blank and/or comment-only lines from the count | [#232](https://github.com/dermot-murphy/CStyleCheck/issues/232) |
| F-014 | `misc.reserved_header_name` — flags source files and `#include "..."` directives that use a name identical to a standard C or POSIX library header | [#230](https://github.com/dermot-murphy/CStyleCheck/issues/230) |
| F-015 | `naming.identifier_length` — uniform minimum/maximum identifier-length check across all identifier categories with per-name exemptions (disabled by default) | [#223](https://github.com/dermot-murphy/CStyleCheck/issues/223) |
| F-016 | `naming.no_single_char_identifiers` — flags single-character variable names outside a configurable exempt list (disabled by default) | [#231](https://github.com/dermot-murphy/CStyleCheck/issues/231) |
| F-017 | `misc.non_ascii_source` — flags characters outside the printable ASCII set (code points outside 0x20–0x7E plus TAB/LF/CR), implementing MISRA C:2012/2023 Rule 4.1. Optional `exempt_string_literals: true` exempts non-ASCII inside string literals | [#279](https://github.com/dermot-murphy/CStyleCheck/issues/279) |
| F-018 | Per-file breakdown in `--summary` output — the summary footer now includes "Files with errors / warnings / info / clean" counts, satisfying the invariant that all four buckets sum to files-checked | [#278](https://github.com/dermot-murphy/CStyleCheck/issues/278) |
| F-019 | `constant.case` typedef-alias exemption — object-like `#define`s whose name ends with the configured `typedefs.suffix.suffix` (e.g. `_t`) are now exempt from `constant.case` when `typedefs.suffix.enabled: true`, eliminating false positives on `#define api_nvm_error_t uint8_t` style type aliases | [#272](https://github.com/dermot-murphy/CStyleCheck/issues/272), [#244](https://github.com/dermot-murphy/CStyleCheck/issues/244) |

### 6.2 Bug Fixes

| ID | Description | Issue |
|---|---|---|
| B-001 | Parameter and pointer naming-prefix checks no longer require both prefixes simultaneously when only one is configured, fixing false positives on otherwise compliant declarations | [#245](https://github.com/dermot-murphy/CStyleCheck/issues/245), [#246](https://github.com/dermot-murphy/CStyleCheck/issues/246) |
| B-002 | Fixed a catastrophic-backtracking (ReDoS) regular expression in `misc.null_statement_comment` that could hang indefinitely on an unclosed `if`/`while`/`for` condition spanning a long line | [#248](https://github.com/dermot-murphy/CStyleCheck/issues/248), [#249](https://github.com/dermot-murphy/CStyleCheck/issues/249) |
| B-003 | Fixed broken GitHub Wiki links: malformed triple-hyphen slugs for headings containing backticks/parentheses, and a non-functional "Rules and Configuration Reference" link | [#251](https://github.com/dermot-murphy/CStyleCheck/issues/251) |

### 6.3 Documentation Updates

| ID | Description | Issue |
|---|---|---|
| D-006 | ASPICE audit CSC-AUD-006 corrective action: fixed pervasive stale test counts (1152/49 modules), a Document-ID collision (`CSC-STD-001`), systemic cross-reference version-citation drift across all 22 `docs/aspice/*.md` work products, three orphaned top-level docs, and `CHANGELOG.md` gaps | [#254](https://github.com/dermot-murphy/CStyleCheck/issues/254) |
| D-007 | Fixed Wiki sidebar/README links: malformed triple-hyphen slugs and the non-functional "Rules and Configuration Reference" link | [#251](https://github.com/dermot-murphy/CStyleCheck/issues/251) |
| D-008 | 102 new tests (1152 total) covering all 11 new rules, including edge cases for multi-line macros, nested braces, comment exclusion, and regex-based exemptions | — |

### 6.4 v1.5.0 New Features and Fixes (2026-06-26)

| ID | Description | Issue |
|---|---|---|
| F-017 | New rule `misc.non_ascii_source` — see §6.1 above | [#279](https://github.com/dermot-murphy/CStyleCheck/issues/279) |
| F-018 | Per-file breakdown in `--summary` output — see §6.1 above | [#278](https://github.com/dermot-murphy/CStyleCheck/issues/278) |
| F-019 | `constant.case` typedef-alias exemption — see §6.1 above | [#272](https://github.com/dermot-murphy/CStyleCheck/issues/272) |
| B-004 | `variable.parameter.p_prefix` false positive on call statements — `RE_FUNCTION_DECL`/`RE_FUNCTION_DEF` required only a zero-width-permitted separator between the return-type and name tokens, allowing regex backtracking to misparse a plain function-call statement (e.g. `foo (args) ;`) as a declaration/definition and check its call arguments as if they were parameters. Fixed by requiring a real separator (whitespace and/or pointer star) | [#273](https://github.com/dermot-murphy/CStyleCheck/issues/273) |
| D-009 | `docker_publish.yml` `github-release` job's checkout step was missing `token: secrets.GITHUB_TOKEN`, inconsistent with the `build-and-push` job | — |
| D-010 | 25 new tests (1182 total): 12 in `test_misra_rules.py` (NR-004), 6 in `test_defines.py` (typedef-alias), 7 in `test_print_summary.py` (per-file breakdown) | — |

### 6.5 v1.6.0 New Features and Fixes (2026-07-01 → 2026-07-06)

| ID | Description | Issue |
|---|---|---|
| F-020 | New rule `misc.constant_comparison` — flags `==`/`!=` comparisons where **both** sides are compile-time constants (literals, `true`/`false`/`NULL`, ALL_CAPS identifiers). Distinguishes from `misc.yoda_condition` (which fires when one side is a variable). Exempt contexts: `#define` RHS, `return` statements | [#339](https://github.com/dermot-murphy/CStyleCheck/issues/339) |
| F-021 | `--fix` auto-fix mode for `variable.pointer_prefix` — renames a non-prefixed pointer parameter throughout the function scope: signature, body, and `@param`/`\param` in the preceding Doxygen block. For `.c` files, also renames the corresponding parameter in the matching `.h` file declaration via `fix_pointer_prefix_in_header()`. Non-safe fix (only applied with `--fix`, not `--safe-only`) | [#341](https://github.com/dermot-murphy/CStyleCheck/issues/341) |
| F-022 | Startup banner — tool name, version, and copyright notice printed to `stderr` at startup; also written to log file via `tee.log_print()`. Does not appear on stdout/pipeline output | [#369](https://github.com/dermot-murphy/CStyleCheck/issues/369) |
| F-023 | Copyright notice in `--version` output — `(C) 2026 Dermot Murphy` appended after the version string | [#368](https://github.com/dermot-murphy/CStyleCheck/issues/368) |
| F-024 | Block-comment inline suppression — `/* cstylecheck: disable=rule.id */` now accepted as an alternative to `//` for all inline suppression directives | [#360](https://github.com/dermot-murphy/CStyleCheck/issues/360) |
| F-025 | `prerelease_check.sh` and `check_my_project.bat` helper scripts added to repository root for pre-release validation and project self-check | [#343](https://github.com/dermot-murphy/CStyleCheck/issues/343) |
| B-005 | `misc.unsigned_suffix` false positive on literals passed to signed-type parameters — when a function is declared or defined in the same translation unit with an `int8_t`, `int16_t`, `int32_t`, `int64_t`, `int`, `short`, `long`, or `char` typed parameter, integer literals at the matching argument position are exempt from the unsigned-suffix requirement. Cross-file cases still require `exempt_function_args` | [#340](https://github.com/dermot-murphy/CStyleCheck/issues/340) |
| B-006 | Function violations reported on wrong line — `RE_FUNCTION_DEF` starts with `(?:^|\n)`, causing `m.start()` to reference the `\n` ending the preceding line. Fixed with `fn_start` correction (`fn_start = m.start()+1 if clean[m.start()] == '\n' else m.start()`); all function-rule violations now reported on the function's own line | [#362](https://github.com/dermot-murphy/CStyleCheck/issues/362), [#363](https://github.com/dermot-murphy/CStyleCheck/issues/363) |
| B-007 | Function-pointer typedef raised spurious `variable.parameter.p_prefix` — `typedef void (*callback_fn_t)(int x)` was misparsed as a function declaration. Function-pointer typedef patterns now skipped by parameter-prefix check | [#359](https://github.com/dermot-murphy/CStyleCheck/issues/359), [#361](https://github.com/dermot-murphy/CStyleCheck/issues/361) |
| B-008 | `misc.yoda_condition` false positives — no longer fires on array-element LHS (`arr[i] == val`) or when both operands are constants (deferred to `misc.constant_comparison`) | [#354](https://github.com/dermot-murphy/CStyleCheck/issues/354) |
| B-009 | `constant.case` false positives on function-call-like or alias-style `#define`s (e.g. `#define api_error_t uint8_t`) | [#355](https://github.com/dermot-murphy/CStyleCheck/issues/355) |
| B-010 | Non-ASCII characters (em-dash, curly quotes) removed from all terminal, log, and verbose-progress output; all strings now 7-bit ASCII | [#363](https://github.com/dermot-murphy/CStyleCheck/issues/363), [#364](https://github.com/dermot-murphy/CStyleCheck/issues/364) |
| B-011 | File paths now use OS-native separator (`\` on Windows, `/` on POSIX) throughout verbose output and violation reports via `os.path.normpath()` in `emit()` | [#367](https://github.com/dermot-murphy/CStyleCheck/issues/367) |
| D-011 | 40 new tests (1223 from v1.5.0 baseline): 21 in `test_constant_comparison.py`, 9 in `test_unsigned_suffix_signed_params.py`, 10 in `test_pointer_prefix_fix.py` | — |
| D-012 | 56 additional tests (1279 total): +9 in `test_yoda_condition.py` (B-008), +9 in `test_inline_suppression.py` (F-024), +6 in `test_constant_comparison.py` (B-009 edge cases), +8 in `test_defines.py`, +4 in `test_parameter_prefix.py` (B-007), +10 in `test_pointer_prefix_fix.py`, +4 in `test_print_summary.py`, +6 in `test_unsigned_suffix_signed_params.py` | — |

### 6.6 v1.6.1 Bug Fix (2026-10-06)

| ID | Description | Issue |
|---|---|---|
| B-012 | Startup banner no longer written into a machine-readable `--log` file — v1.6.0 wrote the two-line banner to the `--log` file for every output format, so with `--output-format json` or `sarif` the file did not parse and the GitHub Action, which reads its results from that file, failed on every run with `could not read results JSON`. `main()` now writes the banner to the log via `tee.log_print()` only when `--output-format` is `text`; for `json`, `sarif` and `html` the log file holds only the report document. The banner is still written to `stderr` for every format (SWE1-094) | [#439](https://github.com/dermot-murphy/CStyleCheck/issues/439) |
| D-013 | 2 new tests (1281 total) in `test_cli.py` (`TestStartupBannerLogFile`): `test_text_log_file_has_banner` (text log starts with the banner) and `test_structured_log_file_has_no_banner` (json / sarif / html log equals the stdout document, has no banner, and JSON / SARIF parse; banner still on `stderr`) | [#439](https://github.com/dermot-murphy/CStyleCheck/issues/439) |

### 6.7 v2.0.0 Changes (2026-11-20)

Content of the `[2.0.0]` section of `CHANGELOG.md` (the `[Unreleased]` section before the release). Changes are recorded in detail in the CHANGELOG and in the CR / problem records (CSC-SUP10-001 §7, CSC-SUP9-001 §6.2); this table summarises them.

#### 6.7.1 Compatibility (breaking) changes

| ID | Description | Issue |
|---|---|---|
| C-001 | Unknown case-style values are rejected: a value that is not a canonical name (`lower_snake`, `upper_snake`, `camel`, `pascal`, `any`) or an accepted alias is a configuration error, exit 2. Presets and `--init` write canonical names only; aliases are normalised by `load_config()` | [#422](https://github.com/dermot-murphy/CStyleCheck/issues/422) |
| C-002 | Configuration and usage errors exit 2 (not 1) from the installed `cstylecheck` command as well as `python src/cstylecheck.py` (`config_error()`) | [#425](https://github.com/dermot-murphy/CStyleCheck/issues/425) |
| C-003 | The last member of a `typedef enum` is checked by `enum.member_case` / `enum.member_prefix` with or without a trailing comma; new findings are possible | [#423](https://github.com/dermot-murphy/CStyleCheck/issues/423) |
| C-004 | `functions.case` removed (it had no effect); a config that still sets it loads with a `WARNING` — use `functions.style` | [#424](https://github.com/dermot-murphy/CStyleCheck/issues/424) |
| C-005 | New-rule opt-in policy: all rules added since v1.6.1 ship `enabled: false` and are off when the key is absent; `misc.boolean_comparison` matches lowercase `true` / `false` only; `--preset misra` / `--preset barr-c` and `--init` enable the rules of the chosen standard | [#412](https://github.com/dermot-murphy/CStyleCheck/issues/412), [#418](https://github.com/dermot-murphy/CStyleCheck/issues/418), [#420](https://github.com/dermot-murphy/CStyleCheck/issues/420) |

#### 6.7.2 New features

| ID | Description | Issue |
|---|---|---|
| F-026 | 8 opt-in MISRA C / Barr-C rules: `misc.goto_usage`, `misc.assignment_in_condition`, `misc.multiple_statements_per_line`, `misc.void_pointer`, `misc.recursive_function`, `misc.sizeof_type`, `misc.boolean_comparison`, `misc.empty_else` | PR [#391](https://github.com/dermot-murphy/CStyleCheck/pull/391), PR [#392](https://github.com/dermot-murphy/CStyleCheck/pull/392) |
| F-027 | 2 opt-in rules for partially initialised local structs: `misc.partial_struct_assignment`, `misc.partial_struct_initialiser` (83 rule IDs) | [#456](https://github.com/dermot-murphy/CStyleCheck/issues/456) |
| F-028 | `misc.partial_struct_*`: struct definitions from files that are not checked (`definition_paths`, `--definitions GLOB`) | [#461](https://github.com/dermot-murphy/CStyleCheck/issues/461) |
| F-029 | `misc.partial_struct_*`: `report_unknown_types` (default `false`) | [#462](https://github.com/dermot-murphy/CStyleCheck/issues/462) |
| F-030 | Missing parent folders of `--log`, `--write-baseline` and `--init-output` files are created | [#441](https://github.com/dermot-murphy/CStyleCheck/issues/441) |
| F-031 | Presets and `--init` enable the matching opt-in rules | [#420](https://github.com/dermot-murphy/CStyleCheck/issues/420) |
| F-032 | Trend analysis: safety indicators and industry-standard C source metrics, new charts | [#388](https://github.com/dermot-murphy/CStyleCheck/issues/388) |
| F-033 | Merge-time ASPICE process controls: `scripts/aspice_check.py`, `aspice_consistency.yml`, PR template and issue forms | [#437](https://github.com/dermot-murphy/CStyleCheck/issues/437) |

#### 6.7.3 Bug fixes

| ID | Description | Issue |
|---|---|---|
| B-013 | `misc.sizeof_type` no longer reports an object that looks like a type (upper case or `_t`) | [#460](https://github.com/dermot-murphy/CStyleCheck/issues/460) |
| B-014 | `misc.partial_struct_*` count members inside `#if` blocks only when the condition is true | [#463](https://github.com/dermot-murphy/CStyleCheck/issues/463) |
| B-015 | `misc.constant_comparison` no longer reports `#if` / `#elif` conditions; `identifiers:` exclusions can suppress it | [#447](https://github.com/dermot-murphy/CStyleCheck/issues/447) |
| B-016 | Startup banner kept out of a json / sarif / html `--log` file (released in v1.6.1, §6.6; back-merged into `develop`) | [#439](https://github.com/dermot-murphy/CStyleCheck/issues/439) |
| B-017 | `misc.boolean_comparison` no longer cites MISRA C:2012 Rule 14.4 | [#410](https://github.com/dermot-murphy/CStyleCheck/issues/410) |
| B-018 | `misc.multiple_statements_per_line` no longer cites MISRA C:2012 Rule 15.5 | [#408](https://github.com/dermot-murphy/CStyleCheck/issues/408) |
| B-019 | Baseline matching ignores line numbers (`(file, rule, message)` multiset) | #394 |
| B-020 | Baseline paths are platform-independent (`/` separators) | #395 |
| B-021 | `barr-c` preset `typedefs.suffix` / `enums.type_suffix` written in the nested form (crash with the generated config) | [#420](https://github.com/dermot-murphy/CStyleCheck/issues/420) |
| B-022 | Trend-metrics accuracy (cyclomatic complexity, counters ignore comments and strings, function length, static variables) | [#388](https://github.com/dermot-murphy/CStyleCheck/issues/388) |
| B-023 | Startup-banner requirements SYS-F-046 / SWE1-094 aligned with the implementation (documentation only, CR-413) | [#413](https://github.com/dermot-murphy/CStyleCheck/issues/413) |

#### 6.7.4 CI, repository and process changes

| ID | Description | Issue |
|---|---|---|
| P-001 | No workflow pushes to `develop` or `main`; every workflow declares `permissions:`; *All Checks Passed* aggregate job; required status checks on `develop` | [#449](https://github.com/dermot-murphy/CStyleCheck/issues/449), [#453](https://github.com/dermot-murphy/CStyleCheck/issues/453) |
| P-002 | Dependabot targets `develop` (CI-configuration-only hotfix #399, recorded here per CSC-SUP8-001 §7.6) | PR [#399](https://github.com/dermot-murphy/CStyleCheck/pull/399), PR [#403](https://github.com/dermot-murphy/CStyleCheck/pull/403) |
| P-003 | GitHub Actions updated: `actions/checkout@v7`, `actions/setup-python@v7`, `actions/upload-artifact@v7`, `docker/login-action@v4.6.0` | #386, #387, #400 to #402, #404 |
| P-004 | Internal audits CSC-AUD-009 and CSC-AUD-010 and their corrective actions | [#405](https://github.com/dermot-murphy/CStyleCheck/issues/405), [#430](https://github.com/dermot-murphy/CStyleCheck/issues/430) |
| P-005 | ASPICE document-version resyncs | #416, #435 |
| P-006 | `examples/embedded_project` sample project | — |

#### 6.7.5 Tests

| ID | Description | Issue |
|---|---|---|
| D-014 | 390 new tests (1281 at v1.6.1 → 1671 at v2.0.0, 53 → 60 modules); new modules `test_case_style_config.py`, `test_functions_case_removed.py`, `test_exit_code_entry_points.py`, `test_output_dirs.py`, `test_partial_struct.py`, `test_collect_metrics.py`, `test_cli_requirements.py` (§5.4) | — |

---

## 7. Known Issues and Limitations

The following issues are open at the time of this release and deferred to a future version:

| Issue | Title | Priority |
|---|---|---|
| [#159](https://github.com/dermot-murphy/CStyleCheck/issues/159) | Add `--output-format=junit-xml` output option | Low |
| [#160](https://github.com/dermot-murphy/CStyleCheck/issues/160) | Pre-commit hook: warn gracefully when no C files are staged | Low |
| [#161](https://github.com/dermot-murphy/CStyleCheck/issues/161) | `misc.copyright_header` regex anchoring edge cases on Windows line endings | Low |

> No open issues map to known functional defects in the 83 rules. All issue numbers above are illustrative; see GitHub for the live issue tracker.

---

## 8. Release Verification

### 8.1 CI Status at Release

CI results on the release PR `release/2.0.0` → `main` (#465), commit `0c99dad`: `cstylecheck_tests.yml` run 44714166810, `cstylecheck_rules.yml` run 44714167028 and `aspice_consistency.yml` run 44714167031. mypy, ruff and the coverage gate are steps of the Unit Tests (Python 3.11) job.

| Check | Result |
|---|---|
| Unit Tests (Python 3.10) | ✅ Pass |
| Unit Tests (Python 3.11) | ✅ Pass |
| Unit Tests (Python 3.12) | ✅ Pass |
| mypy type check (Python 3.11) | ✅ Pass |
| ruff lint (Python 3.11) | ✅ Pass |
| Coverage gate ≥ 85% combined (Python 3.11) | ✅ Pass |
| Example C file action (CStyleCheck self-check) | ✅ Pass |
| Docker build (`docker_publish.yml`) | Not run on the PR. The workflow has no `pull_request` trigger; it runs on the merge to `main` and on the `v2.0.0` tag push. Its result is recorded after the tag (CR #443) |
| ASPICE work-product consistency (`aspice_consistency.yml`, #437) | ✅ Pass |

### 8.2 Qualification Test Status

All 1671 tests pass with no failures. Test counts per module are documented in §5.4.

### 8.3 Docker Build

The Docker image is built for `linux/amd64` and `linux/arm64` and published to Docker Hub and GHCR automatically on creation of the `v2.0.0` tag via `docker_publish.yml`.

### 8.4 GitHub Pages / Wiki

The GitHub Wiki is rebuilt automatically on any push to `main` that touches `README.md` or `docs/aspice/**` via `wiki_publish.yml`. GitHub Pages (gh-pages branch) hosts the naming-convention trend dashboard, updated on each main-branch push via `cstylecheck_rules.yml`.

---

## 9. Installation and Upgrade Notes

### 9.1 Upgrade from v1.6.x

v2.0.0 has breaking changes (§4.2, §6.7.1). Before upgrading a project:

1. Run `cstylecheck --update-config` (or compare with `src/rules.yml`) to add the new rule keys; they are added as `enabled: false`.
2. Replace any non-canonical case-style value (e.g. `PascalCase`, `camelCase`) if it is not an accepted alias; an unknown value now stops the run with exit 2 (#422).
3. Replace `functions.case` with `functions.style` (#424).
4. CI scripts that tested for exit code 1 on a configuration or usage error must test for 2 (#425).
5. Expect possible new `enum.member_case` / `enum.member_prefix` findings for last enum members written without a trailing comma (#423); a configuration generated by `--preset barr-c` or `--init` (camelCase / PascalCase answer) can also report naming findings that were skipped before (#422).

```bash
# pip / pipx
pip install --upgrade cstylecheck

# Docker
docker pull dermotmurphy/cstylecheck:2.0.0

# pre-commit (update rev in .pre-commit-config.yaml)
rev: v2.0.0

# GitHub Action
uses: dermot-murphy/CStyleCheck@v2.0.0
```

### 9.2 New Features — Optional Activation

The 10 rules added in v2.0.0 are disabled by default (`enabled: false`, and off when the key is absent):

- **MISRA C / Barr-C rules** — `misc.goto_usage`, `misc.assignment_in_condition`, `misc.multiple_statements_per_line`, `misc.void_pointer`, `misc.recursive_function`, `misc.sizeof_type`, `misc.boolean_comparison`, `misc.empty_else`. Enable per rule (`misc.<rule>.enabled: true`) or generate a config with `--preset misra` / `--preset barr-c` or `--init`.
- **Partially initialised local structs** — `misc.partial_struct_assignment`, `misc.partial_struct_initialiser`; optional `definition_paths` / `--definitions GLOB` (#461) and `report_unknown_types` (#462).

Missing output folders (#441) and line-independent baseline matching (#394, #395) need no configuration change.

### 9.3 Backward Compatibility

The `src/cstylecheck.py` entry point shim and all CLI flags of v1.6.x are retained; `--definitions` is new. The 73 rule IDs present in v1.6.x are all retained; 10 rule IDs were added (83 rule IDs total). The behaviour changes listed in §6.7.1 can change the findings or the exit code of an existing project. Baselines written by v1.6.x are still honoured (entries are matched without the line number). Users who import the checker programmatically via `import cstylecheck` continue to work, except that `matches_case()` raises `ValueError` for an unknown style and `load_baseline()` returns a `collections.Counter`.
---

## 10. Traceability

> **Baseline note (v2.0.0, 2026-11-20):** the document versions below are the v2.0.0 release baseline (CR #443).

| Work Product | Document | Version | Status |
|---|---|---|---|
| System Requirements | CSC-SYS2-001 | 2.25 | Released |
| System Architecture | CSC-SYS3-001 | 1.27 | Released |
| System Integration Tests | CSC-SYS4-001 | 1.34 | Released |
| System Verification | CSC-SYS5-001 | 1.31 | Released |
| Software Requirements | CSC-SWE1-001 | 2.32 | Released |
| Software Architecture | CSC-SWE2-001 | 1.36 | Released |
| Detailed Design | CSC-SWE3-001 | 1.42 | Released |
| Unit Verification | CSC-SWE4-001 | 1.48 | Released |
| Integration Tests | CSC-SWE5-001 | 1.37 | Released |
| Qualification Tests | CSC-SWE6-001 | 1.40 | Released |
| Source Code | `src/cstylecheck/` (package) | 2.0.0 | Released |
| Test Suite | `tests/` (1671 tests) | 2.0.0 | Released |
| CI Automation | `.github/workflows/` + `scripts/ci/` + `scripts/aspice_check.py` | 2.0.0 | Released |
| Docker Image | `Dockerfile/Dockerfile` | 2.0.0 | Released |
| Change Log | `CHANGELOG.md` | 2.0.0 | Released |

---

## 11. Review & Approval

| Role | Name | Signature / Electronic Approval | Date |
|---|---|---|---|
| Author | Claude | Approved | 2026-11-20 |
| Technical Reviewer | Dermot Murphy | By merge (CSC-DEV-002 §5.2) | On PR merge |
| Quality Assurance | Dermot Murphy | By merge (CSC-DEV-002 §5.2) | On PR merge |
| Approver | Dermot Murphy | By merge (CSC-DEV-002 §5.2) | On PR merge |

> Approval is given by the owner's merge of the pull request that introduces this revision; the merge commit is the approval record (CSC-DEV-002 §5.2).

> **Note:** This document is under configuration management (SUP.8). Post-approval changes require a change request (SUP.10) and a new document version.

---

*End of Software Version Description — CStyleCheck v2.0.0*
