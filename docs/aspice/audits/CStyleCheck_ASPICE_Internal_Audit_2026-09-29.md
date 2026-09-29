# CStyleCheck ASPICE Internal Audit — CSC-AUD-009

| Field | Value |
|---|---|
| **Audit ID** | CSC-AUD-009 |
| **Date** | 2026-09-29 |
| **Branch** | `develop` (post-v1.6.0, commit `296e91b`; audited on `claude/aspice-audit-2026-09-29`) |
| **Auditor** | AI-assisted internal audit (Claude, per CSC-DEV-001) |
| **Scope** | Full CL2 re-assessment of all 17 processes at the post-v1.6.0 `develop` baseline; verification that PRs #391, #392, #397, #398, #399/#403 and the Dependabot GitHub Actions bumps (#400–#402, #404) are reflected in all affected work products (26 files in `docs/aspice/`, README, CHANGELOG, CONTRIBUTING, `pyproject.toml`, `src/`, `tests/`, `scripts/`, `.github/`) |
| **Overall Status** | **CL2 Achieved — 3F/14L/0P/0N** (down from 17F at CSC-AUD-008) |
| **Test count (actual)** | 1422 / 54 test modules (`python -m pytest --collect-only -q`; 1422 passed, 2026-09-29) |
| **Rule count (actual)** | 81 (73 at v1.6.0 + 8 added by #391/#392) |
| **SW requirements** | 112 (SWE1-001 through SWE1-108 + SWE1-MISRA-001 through SWE1-MISRA-004) |
| **SIT test cases** | 26 (SIT-001 through SIT-026) |
| **Findings** | 28 (9 High, 14 Medium, 5 Low) |
| **Issue** | #405 |

---

## 1. Purpose and Trigger

This audit establishes the CL2 capability record for the **post-v1.6.0 `develop` baseline** ahead of the next release. The trigger is a series of feature, fix and CI merges to `develop` since v1.6.0 (2026-07-06), plus a hotfix to `main`:

- **PR #391** — `misc.goto_usage` (MISRA 15.1) and `misc.assignment_in_condition` (MISRA 13.4)
- **PR #392** — six MISRA/Barr-C rules (`misc.multiple_statements_per_line`, `misc.void_pointer`, `misc.recursive_function`, `misc.sizeof_type`, `misc.boolean_comparison`, `misc.empty_else`) and six trend "safety" metrics (`assert_count`, `assert_density`, `goto_count`, `void_ptr_count`, `cast_count`, `macro_count`)
- **PR #397** — baseline matching without line numbers and path normalisation (#394, #395); SWE1-100/101, UNIT-119/120, UV-CLI-011..013
- **PR #398** — trend-analysis C source metrics (#388); SWE1-102..108, UNIT-121..127, UV-MET-001..010, SUP8 CI-038..044
- **PR #399 (hotfix to `main`) / #403 (back-merge)** — Dependabot `target-branch: develop`
- **Dependabot** — `actions/setup-python@v7`, `actions/checkout@v7`, `actions/upload-artifact@v7`, `docker/login-action@v4.6.0`

The previous audit (CSC-AUD-008, v1.5.1, 2026-06-28) rated all 17 processes F. No audit record was produced for the v1.6.0 release (see AUD9-F-021).

---

## 2. Baseline Changes Since CSC-AUD-008 (v1.5.1 → develop post-v1.6.0)

| Work Product | v1.5.1 Version | Current Version | Key Changes |
|---|---|---|---|
| CSC-SWE1-001 | 2.4 | 2.7 | SWE1-091..099 (v1.6.0); SWE1-065..067 revised and SWE1-100/101 (#397); §4.18 SWE1-102..108 (#398). **No requirements for the 8 rules from #391/#392** |
| CSC-SWE2-001 | 1.11 | 1.12 | COMP-06 functions, baseline key and SWA-IF-08 edited by #397 **without a version bump or revision entry** |
| CSC-SWE3-001 | 1.15 | 1.17 | UNIT-119/120 (#397), UNIT-121..127 (#398). **No units for the 8 new checker methods** |
| CSC-SWE4-001 | 1.17 | 1.21 | UV-CLI-011..013 (#397), §5.16 UV-MET-001..010 (#398); total 1346. **76 tests from #391/#392 not catalogued** |
| CSC-SWE5-001 | 1.11 | 1.14 | SIT-021..026 (v1.6.0) |
| CSC-SWE6-001 | 1.13 | 1.16 | SWQ-003 73 rule IDs (v1.6.0) |
| CSC-SYS2-001 | 2.1 | 2.2 | SYS-F-011 73 rule IDs; SYS-F-046 added (v1.6.0) |
| CSC-SYS3-001 | 1.5 | 1.6 | Scope v1.6.0; 73 rule IDs |
| CSC-SYS4-001 | 1.9 | 1.11 | SITC-016 (v1.6.0) |
| CSC-SYS5-001 | 1.7 | 1.8 | SYS-VTC-003 73 rule IDs |
| CSC-SUP1-001 | 1.8 | 1.9 | v1.6.0 cross-ref updates |
| CSC-SUP8-001 | 1.9 | 1.12 | CI-035..037 (v1.6.0); CI-038..044 (#398) |
| CSC-SVD-001 | 1.20 | 1.23 | v1.6.0 release content (73 rules, 1279 tests) |
| CSC-MAN3-001 | 1.6 | 1.7 | v1.6.0 test count |
| CSC-PA2-001 | 1.19 | 1.22 | v1.6.0 counts and §5.4 versions |

Documents unchanged since v1.5.1: CSC-MAN5-001 (v1.4), CSC-SUP9-001 (v1.2), CSC-SUP10-001 (v1.2), CSC-ACQ4-001 (v1.3), CSC-DEV-001 (v1.2), CSC-DEV-002 (v1.1), CSC-STD-001 (v1.2).

Not reflected in any work product: PR #391, PR #392 (rules and safety metrics), PR #399/#403 (Dependabot target branch), and the Dependabot Actions bumps (#400–#402, #404).

---

## 3. CL2 Coverage Summary — develop post-v1.6.0 Baseline

| Process | PA 1.1 Evidence | PA 2.1 | PA 2.2 | Verdict | Delta from v1.5.1 |
|---|---|---|---|---|---|
| SYS.2 | 58 SYS REQ-IDs; SYS-F-011 still states 73 rule IDs; SYS-F-046 traced to the wrong SWE1 ID; RTM omits SWE1-091..101 | §4.1 objectives | CSC-SYS2-001 v2.2; §3.3 refs stale | **L** | Downgraded (was F; AUD9-F-005, F-008) |
| SYS.3 | Architecture unchanged; §9 still states 73 rule IDs | §4.1; §4.3 | CSC-SYS3-001 v1.6; refs stale | **F** | No change |
| SYS.4 | 16 SITC; no coverage of the 8 new rules | §4.1 | CSC-SYS4-001 v1.11 | **L** | Downgraded (was F; AUD9-F-005) |
| SYS.5 | 13 SYS-VTC; SYS-VTC-003 covers 73 of 81 rule IDs | §4.1 | CSC-SYS5-001 v1.8 | **L** | Downgraded (was F; AUD9-F-005) |
| SWE.1 | 112 SW requirements; 8 implemented rules have no requirement; SWE1-102..108 have no parent | §4.1; §4.2 | CSC-SWE1-001 v2.7; header date stale | **L** | Downgraded (was F; AUD9-F-001, F-011) |
| SWE.2 | 12 components; COMP-05f and §8.1 omit the 8 new checks; no element for the `scripts/` metrics units | §4.1 | CSC-SWE2-001 v1.12 edited without revision | **L** | Downgraded (was F; AUD9-F-002, F-015) |
| SWE.3 | 127 units catalogued; 8 checker methods not designed; 43 stale line refs; 35 units without §5 spec; §6.3 baseline format wrong | §4.1 | CSC-SWE3-001 v1.17 | **L** | Downgraded (was F; AUD9-F-002, F-007, F-012, F-013) |
| SWE.4 | 1422 tests PASS; catalogue shows 1346; 29 SW requirements without a §7 trace | §4.1; coverage targets | CSC-SWE4-001 v1.21 | **L** | Downgraded (was F; AUD9-F-003, F-004) |
| SWE.5 | 26 SIT; none for the 8 new rules; SWA-IF-09 / SIT-012 describe the old baseline model | §4.1 | CSC-SWE5-001 v1.14 | **L** | Downgraded (was F; AUD9-F-005, F-006) |
| SWE.6 | 12 SWQ; SWQ-003 covers 73 of 81; SWQ-007 step 4 contradicts SWE1-100 | §4.1; release gate | CSC-SWE6-001 v1.16 | **L** | Downgraded (was F; AUD9-F-005, F-006) |
| MAN.3 | Scope, WBS and schedule stale (53 rules, 10 modules, 3 workflows; schedule ends at v1.1.0) | §4.1; §4.3 | CSC-MAN3-001 v1.7 | **L** | Downgraded (was F; AUD9-F-020) |
| MAN.5 | 8 risks; RISK-003/RISK-005 review dates (2026-08-28) overdue | §4.1; risk monitoring | CSC-MAN5-001 v1.4 | **L** | Downgraded (was F; AUD9-F-019) |
| SUP.1 | Per-release peer-review record missing for v1.5.0, v1.5.1 and v1.6.0 | §4.1; CI evidence | CSC-SUP1-001 v1.9 | **L** | Downgraded (was F; AUD9-F-022) |
| SUP.8 | 44 CIs; implementation package `src/cstylecheck/` and `.github/dependabot.yml` not CIs | §4.1; CM monitoring | CSC-SUP8-001 v1.12; header date stale | **L** | Downgraded (was F; AUD9-F-009) |
| SUP.9 | Problem process with SLAs and register | §4.1; Issue metrics | CSC-SUP9-001 v1.2 | **F** | No change |
| SUP.10 | CR process with impact levels and approval | §4.1; CR metrics | CSC-SUP10-001 v1.2 | **F** | No change |
| ACQ.4 | 6 suppliers; pinned GitHub Actions list stale (v6 vs v7); 6 third-party actions unregistered | §4.1; monitoring schedule | CSC-ACQ4-001 v1.3 | **L** | Downgraded (was F; AUD9-F-018) |

> **📋 Rating scale:** N = Not achieved (0–15%), P = Partially achieved (15–50%), L = Largely achieved (50–85%), F = Fully achieved (85–100%). All processes must achieve **L or F** at PA 2.1 and PA 2.2 for CL2 to be awarded.

---

## 4. Overall CL2 Verdict

**✅ ASPICE CL2 IS ACHIEVED on the post-v1.6.0 `develop` baseline**, but with a significant regression: **3 F, 14 L, 0 P/N** (was 17 F at CSC-AUD-008).

The main cause is that PRs #391 and #392 added **8 rule IDs (73 → 81), 76 unit tests and 6 trend metrics** to `develop` without any change to the ASPICE work products, README, Rules-and-Configuration.md or CHANGELOG. PRs #397 and #398 were documented in SWE.1–SWE.4 and SUP.8, but those updates did not reach SYS.2, SWE.2 (no revision), SWE.5, SWE.6, MAN.3 or CSC-PA2-001. The audit also found several traceability and CM defects that CSC-AUD-008 did not detect: the unregistered implementation package, SYS-F-046 traced to the wrong SWE1 ID, 43 stale source line references in SWE3, and 29 SW requirements with no SWE4 §7 trace.

All High findings must be closed before the next release is tagged. Otherwise, SWE.1, SWE.4, SWE.5 and SWE.6 risk dropping to P at the release audit.

---

## 5. Evidence Summary

| Evidence Type | Count / Detail | CI Reference |
|---|---|---|
| Software requirements | 112 (SWE1-001..108 + SWE1-MISRA-001..004); 147 SWE1 table rows (`grep -cE "^\| SWE1-"`) | CSC-SWE1-001 §4 |
| Unit test cases | 1422 across 54 modules (all PASS, 2026-09-29, Python 3.11 local run) | CSC-SWE4-001; CI-017 |
| `test_misra_rules.py` | 140 tests (documented 64); new classes: AssignmentInCondition 16, GotoUsage 10, BooleanComparison 10, EmptyElse 9, MultipleStatementsPerLine 8, VoidPointer 8, RecursiveFunction 8, SizeofType 7 = 76 | CSC-SWE4-001 §5.14 |
| `test_improvements.py` | 80 (SWE4 80 ✔; README 67 ✘) | CSC-SWE4-001 §6 |
| `test_collect_metrics.py` | 54 (10 classes; matches UV-MET-001..010 counts exactly) | CI-044 |
| Rules (lint checks) | 81 (8 new `misc.*` keys in `src/rules.yml:775–859`; checks called at `checker.py:354–361`) | CI-003 |
| SW units | 127 catalogued (UNIT-01..127, no gaps); 92 with §5 detailed spec | CSC-SWE3-001 |
| SIT / SITC / SYS-VTC / SWQ | 26 / 16 / 13 / 12 | CSC-SWE5/SYS4/SYS5/SWE6 |
| Configuration items | 44 listed (CI-001..044) | CSC-SUP8-001 §6.1 |
| Stale reference-version citations | 68 rows in 21 documents | §3.1-style tables |
| GitHub Actions in workflows | `checkout@v7`, `setup-python@v7`, `upload-artifact@v7`, `docker/login-action@v4.6.0`, `docker/setup-qemu-action@v4`, `docker/setup-buildx-action@v4`, `docker/metadata-action@v6`, `docker/build-push-action@v7`, `peter-evans/dockerhub-description@v5`, `tj-actions/changed-files@9426d40…` (v47.0.6) | `.github/workflows/*.yml` |
| Dependabot | `target-branch: "develop"` for `pip` and `github-actions` (`.github/dependabot.yml:5,13`) | not a CI |

---

## 6. Findings and Actions Required

**Severity scale** (as in CSC-AUD-005/007): **High** means a traceability break, a work-product statement that contradicts the implementation, or a missing mandatory work-product content that affects a BP/GP rating. **Medium** means stale counts, versions or references, or a missing supporting content that does not break a trace. **Low** means editorial or record-keeping defects.

### 6.1 Findings

| ID | Severity | Work Product | Finding | Evidence | Required Correction |
|---|---|---|---|---|---|
| AUD9-F-001 | High | CSC-SWE1-001 | The 8 rules added by #391/#392 have no SW requirement, no RTM row and no Appendix A entry. Appendix A.2/A.3 still delegate MISRA 11.5, 13.4, 15.1, 15.7 and 17.2 wholly to cppcheck. | `grep -c` = 0 for all 8 rule IDs in SWE1; `src/rules.yml:775–859`; `checker.py:2425–2728` (8 `_check_*` methods), called at `checker.py:354–361`; SWE1 Appendix A.1 (lines 372–402), A.2 rows "Rules 11.1–11.9 … 17.1–17.8" | Add SWE1-109..116 (parent SYS-F-020) in §4.9, add §5 RTM rows, add Appendix A.1 rows (MISRA/Barr-C refs), and amend A.2/A.3 to show partial CStyleCheck coverage |
| AUD9-F-002 | High | CSC-SWE2-001, CSC-SWE3-001 | The 8 new checker methods have no architectural or detailed design. There is no UNIT entry, no §5 spec and no §8 RTM row. The SWE2 COMP-05f list and the §8.1 `run_all()` sequence end at `_check_non_ascii_source()`. | SWE3: 0 matches for `_check_goto_usage`, `_check_assignment_in_condition`, `_check_multiple_statements_per_line`, `_check_void_pointer`, `_check_recursive_function`, `_check_sizeof_type`, `_check_boolean_comparison`, `_check_empty_else`; SWE2:342 (last sequence entry); SWE2 §10 RTM ends at SWE1-099 (line 420) | Add UNIT-128..135 with `checker.py` line refs, §5 algorithm specs and §8 RTM rows. Add the methods to SWE2 COMP-05f, §8.1 and §10 |
| AUD9-F-003 | High | CSC-SWE4-001 | The unit-test catalogue does not include the 76 tests added by #391/#392. The documented total is 1346, but 1422 tests exist. | SWE4:353 heading "(64 tests)", SWE4:430 `test_misra_rules.py` 64 (actual 140), SWE4:462 total 1346 (actual 1422), SWE4:89 "all 1279 tests"; SWE6:490 "64 test cases" | Add §5.14 TC rows for the 8 new classes and set `test_misra_rules.py` to 140 and the total to 1422 (54 modules). Fix SWE4:89 and SWE6:490. Add §7 rows for SWE1-109..116 |
| AUD9-F-004 | High | CSC-SWE4-001 | 29 SW requirements have no entry in the §7 SW-requirement → test-case trace. | §7 omits SWE1-001..006, 011..016, 057..064, 094..099 and SWE1-MISRA-001..003 (the MISRA IDs appear only in §5.14 prose, line 356) | Add §7 rows mapping each requirement to existing UV-/test IDs (`test_cli.py`, `test_dictionaries.py`, `test_misc.py`, `test_print_summary.py`, `test_functions.py`, `test_variables.py`, `test_misra_rules.py`) |
| AUD9-F-005 | High | CSC-SYS2-001, CSC-SYS3-001, CSC-SYS4-001, CSC-SYS5-001, CSC-SWE5-001, CSC-SWE6-001 | The 8 new rules have no system requirement text and no integration, system-integration, system-verification or qualification coverage. All of these documents still state 73 rule IDs (the AUD7-F-001 pattern). | SYS2:119 SYS-F-011 "73 rule IDs", SYS2:128 SYS-F-020 list lacks the 8 rules; SYS3:226; SYS5:145, 383, 413; SWE6:141, 369; 0 matches for the 8 rule IDs in SWE5/SYS4/SYS5/SWE6 | SYS-F-011 → 81 rule IDs and extend SYS-F-020. Add SIT-027 (SWE5), extend or add a SITC (SYS4), and extend SYS-VTC-003 and SWQ-003 to 81 rule IDs, covering SWE1-109..116. Update SYS3 §9 |
| AUD9-F-006 | High | CSC-SWE6-001, CSC-SWE5-001, CSC-SYS2-001 | The verification specs contradict the #397 baseline design. SWQ-007 step 4 expects a moved violation **not** to be suppressed ("line number in key"). SWA-IF-09 still says `frozenset`. SIT-012 expects a JSON array with a `filepath` field. The SYS2 RTM maps baseline suppression only to SWE1-065..067. | SWE6:257; SWE6:249, 373, 400 (trace SWE1-065..067 only); SWE5:94, 353; SYS2:217; contradicts SWE1-100 (SWE1:219) and `test_moved_violation_still_suppressed` | Rewrite SWQ-007 step 4 (moved violation stays suppressed) and add steps for the extra-copy and Windows-path cases. Trace SWQ-007, SIT-012 and the SYS2 RTM to SWE1-100/101. SWA-IF-09 → `collections.Counter` multiset; SIT-012 step 4 → `{"violations":[{file,line,rule,message}]}` |
| AUD9-F-007 | High | CSC-SWE3-001, CSC-SWE1-001, CSC-SWE2-001 | The baseline data design does not match the implementation. SWE3 §6.3 shows a top-level JSON array with a `filepath` key, and SWE1-065 says "JSON array". The code writes an object `{"violations": [...]}` with a `file` key. | SWE3:1272–1283; SWE1:216; `baseline.py:91–100` (write), `baseline.py:60–62` (load reads `data["violations"]`, `entry["file"]`) | Correct §6.3 to the actual schema and state that `line` is informational only (SWE1-100). Reword SWE1-065 ("JSON object with a `violations` array") |
| AUD9-F-008 | High | CSC-SYS2-001, CSC-SWE1-001 | SYS.2 ↔ SWE.1 traceability is not bidirectional. The SYS2 RTM traces SYS-F-046 (startup banner) to SWE1-091 (`misc.constant_comparison`), while the banner requirement SWE1-094 names SYS-F-032 as its parent. The SYS2 RTM omits SWE1-091..101. 23 SYS REQ-IDs are never cited as a parent by any SWE1 requirement. | SYS2:230; SWE1 §4.17 SWE1-094 parent SYS-F-032; SYS2 §6 rows end at SWE1-090; uncited: SYS-F-001, 003, 025, 026, 036, 038, 040, 041..046, SYS-NF-002..007, 009..012 | Correct SYS-F-046 → SWE1-094 and set SWE1-094's parent to SYS-F-046. Add SWE1-091..101 (and SWE1-109..116) to the SYS2 RTM. Align the SWE1 parent column with the SYS2 RTM for SYS-F-041..045 (SWE1-072..077) and the other uncited IDs, or record the rationale |
| AUD9-F-009 | High | CSC-SUP8-001 | The CI list omits the implementation itself. CI-001 is only the thin shim `src/cstylecheck.py`; the 12-module package `src/cstylecheck/` (7123 lines) is not a CI. Also missing: `.github/dependabot.yml`, `CHANGELOG.md`, `CONTRIBUTING.md`, `Rules-and-Configuration.md`, `src/project.defines`, `scripts/build.bat`, `scripts/test.bat`, `tests/__init__.py`, `LICENSE`, and all ASPICE WPs except DEV-001/002/SVD. CI-027 is only "This CM Plan", yet CSC-PA2-001 §5.3 maps every WP to CI-027. CI-044 duplicates CI-017. | SUP8:123–166; `git ls-files`; PA2:143, 147 | Add CIs for `src/cstylecheck/*.py`, `.github/dependabot.yml`, the listed docs and scripts, and each `docs/aspice/*.md` / audit record (or a `docs/aspice/**` CI). Fix the CI-027 path. Mark CI-044 as a subset of CI-017 |
| AUD9-F-010 | Medium | CSC-SWE1-001, CSC-SWE3-001, CSC-SWE4-001, CHANGELOG, README | The 6 trend "safety" metrics from #392 (`assert_count`, `assert_density`, `goto_count`, `void_ptr_count`, `cast_count`, `macro_count`) and the `safety_indicators` / `macro_metrics` charts are not specified or documented. SWE1-108 lists 7 charts; 9 exist. | `scripts/collect_metrics.py:845–897, 959–963, 1072–1074`; `generate_charts.py` (`safety_indicators`, `macro_metrics`); `update_wiki_metrics.py`; 0 matches for `goto_count` etc. in docs, CHANGELOG and README; only tested at `test_collect_metrics.py:389–391` | Add a requirement (e.g. SWE1-117) or extend SWE1-104/108. Extend the UNIT-125/127 specs and map to UV-MET-008. Add them to CHANGELOG [Unreleased] and the README trend-analysis paragraph |
| AUD9-F-011 | Medium | CSC-SWE1-001, CSC-SWE2-001, CSC-MAN3-001, CSC-PA2-001 | The upward trace is dangling. SWE1-102..108 cite "MAN.3 / GP 2.1.4" as parent, but MAN3 has no trend or metrics content. SWE3 assigns UNIT-121..127 to a component "CI script (metrics)" that does not exist in SWE2. The SWE1 §5 RTM row "SWE1-065 to SWE1-067" does not include SWE1-100/101. PA2 claims "100% traceable to SYS.2". | SWE1:270–280, 314; MAN3 `grep -ci "trend\|metrics"` = 0; SWE2 `grep -c "collect_metrics\|CI script"` = 0; PA2:70 | Add a MAN3 §-entry for trend-analysis monitoring (metrics.yml, charts, wiki) and cite it as parent. Add an SWE2 component for `scripts/` metrics or state the scope exclusion. Add SWE1-100/101 to the §5 RTM. Qualify the PA2 statement |
| AUD9-F-012 | Medium | CSC-SWE3-001 | 43 of 114 `file:line` source references in the §4 unit catalogue are stale. All 43 were already stale at v1.6.0 (checked against `origin/main`), so they were missed by CSC-AUD-008 and the v1.6.0 audit. | e.g. UNIT-24 `checker.py:870` → 969; UNIT-32 `checker.py:2047` → 2755; UNIT-40 `output.py:125` → 269; UNIT-17 `preprocessor.py:113` → 202; UNIT-46 `cli.py:319` → 367 (full list reproducible via AST scan) | Regenerate all line numbers from the current source (baseline.py refs UNIT-35/36/37/119/120 are correct). Consider a CI check |
| AUD9-F-013 | Medium | CSC-SWE3-001, CSC-PA2-001 | 35 catalogued units have no §5 detailed-design section, although PA2 claims "118 units with algorithmic specs". | Missing `### UNIT-nn` for 06–09, 11–13, 15, 17, 18, 20, 24, 26–30, 32, 33, 35, 36, 40–49, 91–94 (127 catalogued, 92 specified); PA2:248 | Add §5 specs (or explicit "trivial accessor — no algorithm" entries) and correct the PA2 wording and count |
| AUD9-F-014 | Medium | All 21 controlled WPs | 68 referenced-document version citations are stale. 16 of them are caused by the post-v1.6.0 bumps (SWE1 2.7, SWE3 1.17, SWE4 1.21, SUP8 1.12). | e.g. SWE2:49 SWE1 2.6→2.7; SWE5:54 SWE1 2.5→2.7; SUP8:65 SWE1 2.5→2.7; MAN3:54 SYS2 1.6→2.2; SYS5:49 SYS4 1.4→1.11; DEV001:135 PA2 1.9→1.22; STD-001:44–46; PA2:202–219 (full list in audit working notes: 68 rows / 21 docs) | Resync every §3.1/§3.2/§3.3 table to the latest versions after the corrections for this audit are applied. SVD §3/§10 citations stay release-baselined and are updated at the next release |
| AUD9-F-015 | Medium | CSC-SWE1-001, CSC-SWE2-001, CSC-SWE3-001, CSC-SWE4-001, CSC-SUP8-001 | GP 2.2 work-product control problems. Header dates were not updated with the 2026-09-29 revisions. SWE2 content was changed by #397 with no version bump or revision entry. Approval tables predate the current versions. | Header Date vs latest revision: SWE1 2026-07-01/2026-09-29, SWE3, SWE4 and SUP8 2026-07-06/2026-09-29; SWE2 v1.12 diff (COMP-06, SWA-IF-08, baseline key) vs `origin/main`; approvals SWE2/3/4 2026-06-27 | Set header dates to the revision dates. Issue SWE2 v1.13 with a revision entry for #397. Refresh the approval tables per SUP1 |
| AUD9-F-016 | Medium | README.md, Rules-and-Configuration.md | User documentation does not cover the 8 new rules, and the totals are stale. | README:11, 20, 50, 60 "73"; README:806 "Rule IDs (73 total)" table lacks the 8 IDs; README:101 `test_improvements.py` 67 (80), README:105 `test_misra_rules.py` 64 (140), README:140 "(1279 tests)" (1422); Rules-and-Configuration.md: 0 matches for all 8 rule IDs | Set the totals to 81 rule IDs and 1422 tests. Add the 8 IDs to the README Rule IDs table. Add a section per rule (YAML plus annotated C example) to Rules-and-Configuration.md |
| AUD9-F-017 | Medium | CHANGELOG.md | [Unreleased] records #388, #394 and #395 but has no entry for the 8 rules (#391, #392) or the 6 safety metrics. The issue is the missing content, not the unreleased status. | CHANGELOG.md:10–55; `git log` 2edf05d (#391), e1a22aa (#392) | Add "Added" entries for the 8 rules (with MISRA/Barr-C refs and severities) and the safety metrics |
| AUD9-F-018 | Medium | CSC-ACQ4-001 | The GitHub Actions supplier record is stale. The pinned list shows `@v6` for checkout, setup-python and upload-artifact (actual `@v7`). Docker actions (`login-action@v4.6.0`, `setup-qemu`/`setup-buildx@v4`, `metadata@v6`, `build-push@v7`), `peter-evans/dockerhub-description@v5` and the third-party `tj-actions/changed-files` (SHA-pinned v47.0.6) are not registered. The record says "three CI workflows" (5 exist) and names `rules.yml` instead of `cstylecheck_rules.yml`. Dependabot is not recorded as the monitoring mechanism. | ACQ4:87, 94–96, 99; `.github/workflows/*.yml` `uses:` lines (e.g. `docker_publish.yml:88,96`, `cstylecheck_rules.yml:80`) | Update §5.2 pinned list, add the third-party action suppliers (with the SHA-pinning policy for `tj-actions`), set the workflow count to 5, and reference Dependabot (`target-branch: develop`) |
| AUD9-F-019 | Medium | CSC-MAN5-001 | Risk monitoring is overdue. RISK-003 and RISK-005 review dates of 2026-08-28 have passed with no review recorded. The RISK-003 treatment does not record `target-branch: develop` or the #399 correction, which fixed Dependabot PRs opening against `main`. | MAN5:149, 191; `.github/dependabot.yml:5,13`; commit 945dd02 on `main` | Record the reviews, set new review dates, and add the target-branch policy and the #399/#403 history to RISK-003. Issue MAN5 v1.5 |
| AUD9-F-020 | Medium | CSC-MAN3-001 | The project plan is stale. §3 states "10 sub-modules implementing 53 rule IDs" (actual 12 / 81), "1279 pytest tests across 53 test modules" (1422 / 54) and "3 workflows" (5). The §8 schedule ends at the v1.1.0 milestones, with no v1.2–v1.6 or next-release milestones. | MAN3:66, 67, 73, 129, 132, 158–169 | Update the scope, WBS-07/WBS-10 and the §8 schedule (actuals for v1.2.0–v1.6.0 and a planned next release) |
| AUD9-F-021 | Medium | CSC-PA2-001 | The capability records are stale and there is no audit record for v1.6.0. PA2 states 99 SW requirements (112), 90 / 118 units (127), 24 SIT (26), 37 CIs (44), 1279 tests and 73 rules. The §5.4 versions are stale. §6 ratings still cite CSC-AUD-008 (v1.5.1), although revisions 1.21/1.22 describe a "v1.6.0 ASPICE audit" for which no CSC-AUD record exists. | PA2:70, 72, 74, 79, 202–219, 246–251, 264, 266 | Update PA2 to v1.23 with the CSC-AUD-009 ratings and counts, add CSC-AUD-009 to §5.4, and record the v1.6.0 audit gap |
| AUD9-F-022 | Medium | CSC-SUP1-001 | The SUP1 §5.4 release gate "peer-review record produced" was not met for v1.5.0, v1.5.1 or v1.6.0. Only Review_Record_v1.2 and v1.4 exist. | SUP1:116; `docs/aspice/` listing | Produce CSC-REVIEW-003 for v1.6.0 (or a retrospective record for v1.5.x–v1.6.0) and add it to PA2 §5.4. Enforce the gate at the next release |
| AUD9-F-023 | Medium | CSC-STD-001 | The standards comparison lists `goto` (MISRA 15.1) and recursion (MISRA 17.2) as not implemented (🔵), but `misc.goto_usage` and `misc.recursive_function` now exist. The other new rules are not reflected. | STD-001:110, 193, 343, 345; §3 cites SWE1 1.9, SWE2 1.8, SWE3 1.10 (lines 44–46) | Update the comparison rows for the 8 new rules and the references. Issue STD-001 v1.3 |
| AUD9-F-024 | Low | 11 WPs (SUP1, SUP8, SVD, SWE1–SWE6, SYS2, SYS4) | 19 revision-history rows have the Author and Description columns swapped (description in the Author column, "Dermot Murphy" in the Description column). | SUP1:24; SUP8:26; SVD:26–28; SWE1:28–29; SWE2:24–25; SWE3:25–26; SWE4:29–30; SWE5:26–27; SWE6:28–29; SYS2:24; SYS4:25 | Swap the columns in these rows |
| AUD9-F-025 | Low | CSC-SWE1-001 | Section order is broken: §4.16, §4.17 and §4.18 appear before §4.15 "Verification Criteria". | SWE1:230, 257, 268, 282 | Renumber §4.15 → §4.19 (or move it after §4.18) and fix internal references |
| AUD9-F-026 | Low | CSC-SWE5-001, CSC-SYS4-001, CSC-SYS5-001 | CM baseline identifiers are stale or refer to pre-merge states. | SWE5:67 "v1.6.0 (pending merge of claude/embedded-c-style-standards-pgqhdc…)"; SYS4:73 "93178cd (… 2026-05-28)"; SYS5:66 "v1.2.0 release tag" | Set the CM baseline to the release tag or commit that the verification ran against |
| AUD9-F-027 | Low | `src/rules.yml`, `tests/rules.yml`, `src/cstylecheck/checker.py` | `misc.multiple_statements_per_line` cites MISRA C:2012 Rule 15.5, which is "single point of exit" and does not relate to multiple statements per line. | `src/rules.yml:792` "Barr-C §3.2 / MISRA C:2012 Rule 15.5"; `checker.py:356` "# Barr-C §3.2 / MISRA 15.5"; same block in `tests/rules.yml` | Remove the MISRA 15.5 citation (keep the Barr-C reference) in both rules.yml files and the checker comment. Use the corrected mapping in SWE1 Appendix A |
| AUD9-F-028 | Low | CSC-SUP8-001, CSC-SVD-001 | Hotfix #399 (Dependabot `target-branch`) was merged to `main` (945dd02) without a patch version, tag or SVD/CHANGELOG record. SUP8 §5 defines hotfixes as patch releases, so `main` now differs from tag v1.6.0 with no recorded baseline. | `git log origin/main`: 945dd02, 8da22b9 after a6102d6 (v1.6.0); SUP8:198 | Record in SUP8 that CI-configuration-only hotfixes are permitted without a patch release (or tag v1.6.1), and log the #399 change in the next SVD |

### 6.2 Actions

| Action | Finding(s) | Owner | Status |
|---|---|---|---|
| Add SWE1-109..116, UNIT-128..135, SWE4 TC rows, SWE2 COMP-05f/§8.1/§10 entries for the 8 new rules | AUD9-F-001, F-002, F-003 | Claude | Closed in #405 (`6ece0e7`) |
| Add SIT/SITC/SYS-VTC/SWQ coverage and SYS-F-011/020 updates to 81 rule IDs | AUD9-F-005 | Claude | Closed in #405 (`6ece0e7`) |
| Align the baseline verification and design with #397 (SWQ-007, SIT-012, SWA-IF-09, SWE3 §6.3, SWE1-065) | AUD9-F-006, F-007 | Claude | Closed in #405 (`6ece0e7`) |
| Repair SYS2↔SWE1 and SWE1→SWE4 traceability | AUD9-F-004, F-008, F-011 | Claude | Closed in #405 (`6ece0e7`, `7ca8e40`). SWE1-015, SWE1-094 and SWE1-096 were traced to integration or inspection evidence, with dedicated unit tests tracked as RR-003-001. **AUD9-F-004 fully closed via #407** (2026-09-29): UV-CLI-014 to UV-CLI-022 in `tests/test_cli_requirements.py` (16 tests; suite 1423→1439), CSC-SWE4-001 v1.24 §7 cites them; RR-003-001 closed. The tests found that the SWE1-094 `--quiet` clause and one-line banner are not implemented — recorded in CSC-SWE4-001 §7 for a change request |
| Extend the SUP8 CI list (package, dependabot.yml, docs, scripts) | AUD9-F-009 | Claude | Closed in #405 (`7ca8e40`) |
| Specify and document the trend safety metrics | AUD9-F-010 | Claude | Closed in #405 (`6ece0e7`, `bb0324c`) |
| Regenerate SWE3 line refs and add missing §5 unit specs | AUD9-F-012, F-013 | Claude | Closed in #405 (`6ece0e7`) |
| Update README, Rules-and-Configuration.md and CHANGELOG for the 8 rules and totals | AUD9-F-016, F-017 | Claude | Closed in #405 (`bb0324c`) |
| Update ACQ4, MAN5, MAN3 and STD-001 | AUD9-F-018, F-019, F-020, F-023 | Claude / Dermot Murphy | Closed in #405 (`7ca8e40`). Risk Owner confirmation of the RISK-003/005 reviews is pending (RR-003-005) |
| Update PA2 to v1.23 with CSC-AUD-009 ratings, and add CSC-REVIEW-003 | AUD9-F-021, F-022 | Claude / Dermot Murphy | Closed in #405 (`7ca8e40`). CSC-REVIEW-003 is a self-review under CSC-DEV-002 and is pending the Review Owner's signature |
| Final cross-reference resync, header dates and revision-table fixes (after all other corrections) | AUD9-F-014, F-015, F-024, F-025, F-026 | Claude | Closed in #405 (`6ece0e7`, `7ca8e40`, `3240651`). CSC-SVD-001 intentionally unchanged (release-baselined); its stale citations and swapped revision rows are updated at the next release (RR-003-002) |
| Correct the MISRA 15.5 citation; record the hotfix policy | AUD9-F-027, F-028 | Claude | Closed in #405 (`9d15f96`, `7ca8e40`). The runtime message of `misc.multiple_statements_per_line` still cites Rule 15.5; changing it changes output and is left for a code PR (RR-003-003). No tag or version change. **Residual closed in #408:** message now cites Barr-C §3.2 only; unit test added |


**Closure note (2026-09-29):** All 28 findings were corrected under #405 on branch `claude/aspice-audit-2026-09-29` in commits `6ece0e7` (SWE/SYS work products), `7ca8e40` (support and management work products, CSC-REVIEW-003), `bb0324c` (README, Rules-and-Configuration.md, CHANGELOG), `9d15f96` (comment-only MISRA citation fix) and `3240651` (cross-reference resync, done last).

After the corrections the suite passes (`python -m pytest -q`: 1422 passed) and `ruff check src tests` is clean. No code behaviour, package version or tag was changed.

Items still open after closure:
- ~~3 SW requirements have no dedicated unit test (RR-003-001).~~ Closed by #407 (UV-CLI-014 to UV-CLI-022).
- CSC-SVD-001 is unchanged until the next release (RR-003-002).
- ~~The runtime message text still cites Rule 15.5 (RR-003-003).~~ Closed in #408.
- Post-v1.6.0 test results have not yet been recorded from the CI matrix (RR-003-004).
- The Risk Owner and Review Owner have not yet confirmed or signed (RR-003-005, §7).

The §3 ratings (3 F / 14 L) remain the audit ratings. They are re-assessed at the next release audit, which must confirm the corrections.
---

## 7. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Auditor | Claude (AI-assisted) | 2026-09-29 | *per CSC-DEV-001* |
| Audit Owner / Reviewer | Dermot Murphy | — | *pending manual review* |

> **Note:** This audit was conducted by an AI tool (Claude) acting in the auditor role as documented in CSC-DEV-001. The solo-developer independent-review constraint is formally acknowledged in CSC-DEV-002. The Audit Owner signature above constitutes the required management review approval for this ASPICE-internal document.

---

*Document: CSC-AUD-009 · Version 1.1 · 2026-09-29 (§6.2 closure recorded 2026-09-29, #405; v1.1: AUD9-F-027 residual closed, #408; AUD9-F-004 fully closed and RR-003-001 closed, #407)*
*Location: `docs/aspice/audits/CStyleCheck_ASPICE_Internal_Audit_2026-09-29.md`*
