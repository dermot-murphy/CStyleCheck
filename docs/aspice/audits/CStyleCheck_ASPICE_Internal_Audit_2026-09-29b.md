# CStyleCheck ASPICE Internal Audit — CSC-AUD-010

| Field | Value |
|---|---|
| **Audit ID** | CSC-AUD-010 |
| **Date** | 2026-09-29 |
| **Branch** | `develop` (commit `2444036`; audited on `ccr-15d55b1c-l6c5rf`) |
| **Auditor** | AI-assisted internal audit (Claude, per CSC-DEV-001) |
| **Scope** | Full CL2 re-assessment of all 17 processes at `develop` `2444036`. Delta focus: the changes merged since the CSC-AUD-009 corrective actions (`3240651`): #407, #408, #410, #412, #413, #418, #420, #422, #423, #424, #425. **Exclusions (per Audit Owner):** document version numbers in ASPICE work products (version citations, version bumps) and CSC-SVD-001 are out of scope |
| **Overall Status** | **CL2 Achieved — 4F/13L/0P/0N** (was 3F/14L at CSC-AUD-009) |
| **Test count (actual)** | 1545 passed (+169 subtests) / 58 test modules (`python -m pytest -q`, Python 3.11, 2026-09-29) |
| **Static analysis** | `ruff check src tests` — all checks passed |
| **Rule count (actual)** | 81 (`src/rules.yml` and `tests/rules.yml` key sets identical) |
| **SW requirements** | 121 (113 in scope for SWQ) |
| **Findings** | 32 (8 High, 13 Medium, 11 Low) |
| **Issue** | #430 |

---

## 1. Purpose and Trigger

CSC-AUD-009 (earlier on 2026-09-29) rated the post-v1.6.0 baseline 3F/14L and closed its 28 findings in #405. Since then eleven changes have merged to `develop`, several of which alter user-visible behaviour:

| Change | Summary |
|---|---|
| #407 | Unit tests for SWE1-015, SWE1-094, SWE1-096 (`tests/test_cli_requirements.py`) |
| #408 | MISRA 15.5 citation removed from `misc.multiple_statements_per_line` message |
| #410 | MISRA 14.4 citation removed from `misc.boolean_comparison` |
| #412 | `misc.boolean_comparison` opt-in and lowercase-only |
| #413 | CR-413: startup-banner requirements aligned with code |
| #418 | CR-418: opt-in policy; 7 post-v1.6.0 MISRA/Barr-C rules disabled by default |
| #420 | Presets and `--init` enable the standard opt-in rules |
| #422 | Unknown case-style names rejected (exit 2); aliases normalised; canonical names in presets/wizard |
| #423 | Last enum member checked with or without trailing comma |
| #424 | `functions.case` removed; WARNING if a config still sets it |
| #425 | Config/usage errors exit 2 from the installed `cstylecheck` command (was 1) |

All GitHub issues are closed at the time of audit.

---

## 2. Method

Three independent read-only review passes were run against `2444036`, and every High finding was re-checked by the auditor against source and documents:

1. **Change traceability** — each change above traced through SYS2–SYS5, SWE1–SWE6, SUP9/SUP10, README, Rules-and-Configuration.md and CHANGELOG; contradiction sweeps (MISRA 14.4/15.5, "enabled by default", `functions.case`, exit code 1, non-canonical case names, enum trailing comma).
2. **Counts and traceability** — scripted checks of rule IDs, per-module test counts, bidirectional SYS2↔SWE1↔SWE3/SWE4/SWE6 traces, dangling IDs, and all `file.py:NNN` references in the SWE3 unit catalogue.
3. **Support, management and GP 2.1/2.2** — MAN3, MAN5, SUP1, SUP8, SUP9, SUP10, ACQ4, PA2, DEV-001/002; header dates, revision rows, approval tables, CI list vs `git ls-files`.

---

## 3. CL2 Coverage Summary — `develop` `2444036`

| Process | PA 1.1 Evidence | Verdict | Delta from CSC-AUD-009 | Driving findings |
|---|---|---|---|---|
| SYS.2 | 58 SYS REQ-IDs; §6 RTM does not match SWE1 parent columns | **L** | No change | F-004 |
| SYS.3 | SYS-F-046 absent from §9 trace | **L** | Downgraded (was F) | F-003 |
| SYS.4 | 17 SITC; counts current; no defects found | **F** | Upgraded (was L) | — |
| SYS.5 | 13 SYS-VTC; SYS-F-046 absent from §6; VTC-008 PASS record inconsistent with #425 | **L** | No change | F-003, F-006 |
| SWE.1 | 121 SW requirements; §5 RTM parent gaps; SWE1-095 contradicts code | **L** | No change | F-005, F-007 |
| SWE.2 | 12 components; #422/#424/#425 not in COMP-02/COMP-12/§8.2 | **L** | No change | F-009 |
| SWE.3 | 136 units, all with §5 spec; 126/126 line refs correct; UNIT-05 step 2 contradicts code | **L** | No change | F-008 |
| SWE.4 | 1545 tests; all 58 module counts match; all 121 SWE1 IDs traced in §7 | **F** | Upgraded (was L) | — |
| SWE.5 | 27 SIT; SIT-024 step 2 contradicts code; count note stale | **L** | No change | F-007, F-019 |
| SWE.6 | 12 SWQ; §6 matrix covers all 121 IDs; §3.3 criterion text stale | **F** | Upgraded (was L) | F-018 (Medium, non-blocking) |
| MAN.3 | Counts current; lifecycle text stale; no release-classification decision | **L** | No change | F-002, F-016 |
| MAN.5 | 8 risks; no compatibility risk; RR-003-005 unconfirmed | **L** | No change | F-012 |
| SUP.1 | GATE-02 misdefined; approvals pending; PRs merged without review evidence | **L** | No change | F-013, F-014 |
| SUP.8 | 60 CIs; §7.1 contradicts §7.6 and practice | **L** | No change | F-015 |
| SUP.9 | Problems fixed and closed, but mandatory SEV label absent | **L** | Downgraded (was F) | F-011 |
| SUP.10 | 5 behaviour-changing CRs unregistered; semver policy not applied | **L** | Downgraded (was F) | F-001, F-002, F-010 |
| ACQ.4 | SUP-07/08 match every `uses:` line and Dependabot | **F** | Upgraded (was L) | F-030 (Low) |

> **📋 Rating scale:** N = Not achieved (0–15%), P = Partially achieved (15–50%), L = Largely achieved (50–85%), F = Fully achieved (85–100%). All processes must achieve **L or F** at PA 2.1 and PA 2.2 for CL2 to be awarded.

---

## 4. Overall CL2 Verdict

**✅ ASPICE CL2 IS ACHIEVED at `develop` `2444036` — 4 F / 13 L / 0 P / 0 N.**

The CSC-AUD-009 corrective actions are effective. The engineering chain is now in good shape: rule and test counts agree everywhere, all 121 SW requirements are traced to unit tests, qualification tests and design units, and all SWE3 source line references are correct.

The main new weakness is **change control of behaviour-changing fixes (SUP.10, SUP.9)**. #412, #420, #422, #424 and #425 change defaults, config acceptance or exit codes, but were handled as ordinary bug fixes. Only CR-413 and CR-418 have CR records, no SEV classification was applied, and the planned "v1.7.0" contradicts the SUP10 semver rule for changed default behaviour. The other High findings are narrow trace or design-text defects: SYS-F-046 traced down, SYS2 ↔ SWE1 parent consistency, SWE1-095 copyright format, SWE3 UNIT-05 step 2, and the SYS-VTC-008 evidence.

**All High findings must be closed before the next release is tagged.** Otherwise SUP.10 and SYS.5 risk falling to P at the release audit.

---

## 5. Evidence Summary

| Evidence Type | Count / Detail |
|---|---|
| Rule IDs | 81 — matches README table (README:871–882), SYS2 SYS-F-011, SYS3, SYS5 VTC-003, SWE6 SWQ-003, MAN3, PA2, SWE1 |
| Unit tests | 1545 (+169 subtests) in 58 modules — SWE4 §6 matches `pytest --collect-only` for every module |
| New test modules | `test_case_style_config.py` 27, `test_cli_requirements.py` 21, `test_exit_code_entry_points.py` 8, `test_functions_case_removed.py` 16 — catalogued in SWE4 §5.17–§5.21; CIs via CI-017 glob |
| SW requirements | 121 (113 in scope for SWQ); present in SWE1 §5, SWE4 §7, SWE3 §8, SWE6 §6 and SWE2 |
| SYS requirements / STK | 58 / 7 |
| SW units | 136 (all with §5 spec); 126 `file.py:NNN` refs checked, 0 stale; 10 script units without line numbers |
| SIT / SITC / SYS-VTC / SWQ | 27 / 17 / 13 / 12 |
| UV IDs | 176 |
| Configuration items | 60 (SUP8), matches PA2 |
| Dangling IDs | 0 (outside revision-history rows) |
| Contradiction sweeps | Clean: no stale MISRA 14.4/15.5 citation; no "enabled by default" claim for the 8 opt-in rules; no `functions.case` as a config key; no exit-1-for-config-error text; no non-canonical case names in presets/docs; no enum trailing-comma limitation |
| Installed-command check | `cstylecheck --config /nonexist.yaml x.c` → exit 2 at `2444036` |

---

## 6. Findings and Actions Required

**Severity scale** (as in CSC-AUD-009): **High** means a traceability break, a work-product statement that contradicts the implementation, or missing mandatory content that affects a BP/GP rating. **Medium** means stale content or missing supporting content that does not break a trace. **Low** means editorial or record-keeping defects.

### 6.1 Findings

| ID | Severity | Work Product | Finding | Evidence | Required Correction |
|---|---|---|---|---|---|
| AUD10-F-001 | High | CSC-SUP10-001 | Five user-visible changes have no CR record, impact level or approval: #412 (rule made opt-in), #420 (presets/`--init` output changed), #422 (previously valid configs now rejected; barr-c typedef/enum case changed), #424 (`functions.case` removed), #425 (exit code 1→2). #412, #422 and #424 carry the `config-change` label, and all of them change SWE1 requirements, so §4.1/§5.3 treat them as CRs. #422 breaks backwards compatibility, which §4.2 classes as High impact (QA sign-off). | SUP10:172–176 (register lists only #413, #418); SUP10 §4.1, §4.2 (line 74), §5.3; SWE1-001/002/032/069/075/115 changed | Add CR-412, CR-420, CR-422, CR-424 and CR-425 to the §7 register, with §7.1 impact analyses and approval evidence |
| AUD10-F-002 | High | CSC-SUP10-001, CSC-MAN3-001 | The release classification contradicts the policy. SUP10 requires a Major release for "changed default behaviour, incompatible config format". #422 rejects configs that used to load and #425 changes exit codes, yet MAN3 plans "v1.7.0", and its scope does not mention these changes. | SUP10:144; MAN3:189 | Record a release-classification decision (Major, or a justified Minor with rationale) in MAN3 §8 and SUP10, and list the compatibility changes in the planned scope |
| AUD10-F-003 | High | CSC-SYS3-001, CSC-SYS5-001 | SYS-F-046 (startup banner, CR-413) has no downward trace: 0 matches in SYS3 or SYS5. | SYS2:209 defines it; SYS3 §9 rows end at SYS-F-045 (SYS3:252); SYS5 §6 rows end at SYS-F-045 (SYS5:461) | Add SYS-F-046 to SYS3 §9 (SS-01, `cli.main`) and to SYS5 §6 (SIT-024; UV-CLI-017..019) |
| AUD10-F-004 | High | CSC-SYS2-001 | The SYS2 §6 RTM does not match the SWE1 §4 parent columns. SWE1-001, 002, 006, 013, 014, 016, 075 and 076 are missing from their parents' rows. Row SYS-F-001..010 lists SWE1-002/013/014/015/016/069, which have other parents. The note at SYS2:243 ("each SWE1 listed cites the SYS in this row as its parent") is therefore false. | SYS2:225–230, 243; SWE1 §4 parent column | Rebuild §6 from the SWE1 parent columns (scripted), or correct the note |
| AUD10-F-005 | High | CSC-SWE1-001 | The §5 RTM parent column omits parents given in §4: SYS-F-039 (row 001–006), SYS-F-020/027 (011–016), SYS-F-011/012/024 (017–029), SYS-F-012 (030–034) and SYS-F-024 (035–039). | SWE1:320–325 | Add the missing parents |
| AUD10-F-006 | High | CSC-SYS5-001 | The SYS-VTC-008 "Invalid config → exit 2 PASS" record (commit 93178cd) is not credible for the installed command. At that commit `load_config()` used `sys.exit("Config file not found…")`, which exits 1 through the `cstylecheck` console script (the #425 root cause). The record was not re-executed or annotated after #425. | SYS5:293, 299; `git show 3240651:src/cstylecheck/config.py:254`; SWE6:311 | Re-execute VTC-008 at the current baseline and record the result. Annotate the 93178cd result as invalid for the console-script entry point, and cross-reference CR-425 |
| AUD10-F-007 | High | CSC-SWE1-001, CSC-SWE5-001, CSC-SWE4-001 | SWE1-095 requires the copyright line format `Copyright (C) YYYY Dermot Murphy`, but the code prints `(C) 2026 Dermot Murphy` (SYS-F-046 already uses this). SIT-024 step 2 expects the word "Copyright". SWE4 says the text "is verified by SIT-024", but no unit test asserts the `--version` copyright line. | SWE1:282; `src/cstylecheck/__init__.py:41`; `cli.py:392–393`; SWE5:647; SWE4:624 | Align SWE1-095 and SIT-024 step 2 with `(C) <year> <holder>`. Add a unit test for the `--version` copyright line, or cite UV-CLI-018 |
| AUD10-F-008 | High | CSC-SWE3-001 | UNIT-05 step 2 says a `None` or non-dict YAML result → `sys.exit(2)`. `load_config()` has no such check: it returns the value unchanged, and `validate_case_styles()` returns `[]` for a non-dict. UNIT-05 was revised by #422, #424 and #425 without correcting this. | SWE3:337; `config.py:340–341, 419–424` | Correct the design text, or implement the check under a CR |
| AUD10-F-009 | Medium | CSC-SWE2-001 | The architecture was not updated for #422, #424 or #425 (only "cross-reference resync" revision rows). COMP-02 omits case-style validation, `validate_case_styles()` and `deprecated_key_warnings()`. COMP-12 omits `normalize_case_style()` and `config_error()`, and its "Used by" omits COMP-01/02/06. §8.2 has no "unknown case style → exit 2" or "`functions.case` → WARNING" rows. COMP-09 does not say that presets and the wizard enable opt-in rules and write canonical case names (#420, #422). | SWE2:24–25, 142–143, 284–286, 312–313, 413–418 | Update COMP-02, COMP-09, COMP-12 and §8.2 |
| AUD10-F-010 | Medium | CSC-SUP10-001 | The CR-418 impact statement is superseded: it says configs written by `--init`/`--preset` get no findings from the opt-in rules, but #420 changed that. The register status for #413 and #418 still reads "Implemented on `claude/…`; closes on PR merge", although both are merged. | SUP10:175–176, 203; `wizard.py:22–53` | Update the CR-418 impact with a reference to CR-420. Set both statuses to Closed, citing the PR and commit |
| AUD10-F-011 | Medium | CSC-SUP9-001 | The problem records have no severity. SUP9 makes a SEV-n label mandatory, but #410, #412, #422, #423, #424 and #425 are labelled `bug` only. So the SEV-2 SLA for "wrong exit code" (#425) cannot be shown to be met. | SUP9:63, 100; GitHub issue labels | Apply SEV labels retroactively and record the SLA outcome, or amend the plan |
| AUD10-F-012 | Medium | CSC-MAN5-001 | The risk register has no risk for user-visible behaviour change on upgrade. The exposures are #422 (config rejection), #423 (new enum findings), #425 (exit code) and #420 (preset output). RR-003-005 (Risk Owner confirmation of the RISK-003/005 reviews) is still pending. Review frequencies conflict: RISK-005 is quarterly (201), monthly (282) and per milestone (293), and RISK-004 has no last-review record. | MAN5:159, 180, 201, 282, 293; `grep -c compatib` → RISK-002 only | Add a compatibility risk (treated through the CHANGELOG ⚠️ notes and the semver policy). Obtain the owner confirmation. Set one frequency per risk and record the RISK-004 review |
| AUD10-F-013 | Medium | CSC-SUP1-001 | GATE-02 names the workflow `rules.yml` checking "`cstylecheck.py`". The real workflow is `cstylecheck_rules.yml`, which checks `src/**` and `source/**/*.[ch]`. WP-01 still names `cstylecheck.py`. | SUP1:94, 109; `.github/workflows/cstylecheck_rules.yml` | Correct the workflow name and scope |
| AUD10-F-014 | Medium | CSC-SUP1-001, CSC-DEV-002-001, all plan/SYS/SWE WPs (GP 2.2.3) | There is no review or approval evidence. Approval tables are `*pending*` while the header Status says "Released". CSC-REVIEW-003 is unsigned. PRs #419, #426, #428 and #429 have zero GitHub reviews. DEV-002 §5.2 claims a PR "approval timestamp" as evidence. | SUP1:176–178; MAN5:303–305; Review_Record_v1.6:20, 92, 123; DEV002:108 | Sign CSC-REVIEW-003 and the approval tables, or set Status to Draft/In review. Amend DEV-002 §5.2 to state that the owner's merge is the approval record |
| AUD10-F-015 | Medium | CSC-SUP8-001 | The CM plan contradicts itself and actual practice. §7.1 says every merge to `main` is tagged, but §7.6 exempts CI-only hotfixes (#399 untagged). §7.1–7.3 allow only `feature/*` and `bugfix/*` into `develop`, but all recent PRs use `claude/<topic>-<id>` (the CLAUDE.md convention), which §7.6 excuses only for hotfixes. | SUP8:214, 215, 221–222, 263, 265 | Align §7.1 with §7.6, and allow `claude/<topic>-<id>` for feature and bugfix branches |
| AUD10-F-016 | Medium | CSC-MAN3-001 | Lifecycle text is stale: §4.3 says "single-file architecture" and "v1.0.0 development complete; documentation phase in progress", and PH-04 names `cstylecheck.py` v1.0.0. WBS-16 and WBS-17 both cover release. | MAN3:98–99, 124, 150–151 | Refresh §4.3, PH-04 and the WBS |
| AUD10-F-017 | Medium | CSC-PA2-001 | The §6 SWE.3 row says "135 units", while PA2:83 and SWE3 have 136 (UNIT-136 `config_error`, #425). The §5.4 change-note column cites "#405; #407" for every WP, although #412–#425 changed them. CI-017 pairs 1545 tests with `develop 296e91b`. | PA2:83, 205, 209–232, 244, 262 | Correct 135 → 136, update the change notes, and cite `2444036` |
| AUD10-F-018 | Medium | CSC-SWE6-001 | The §3.3 coverage criterion still reads "All SWE1-001 to SWE1-099 and SWE1-MISRA-004". It excludes SWE1-100/101, SWE1-109..116 and SWE1-MISRA-001..003, although the §6 matrix covers all of them. | SWE6:89, 449 | Restate as "all 113 in-scope requirements" and list them explicitly |
| AUD10-F-019 | Medium | CSC-SWE5-001 | The post-v1.6.0 test-count note stops at "#420 … 1481 tests". #422, #424, #425 and #423 are missing, although SYS4 and SYS5 include them. | SWE5:768; SYS4:529; SYS5:181 | Extend the note to 1545 |
| AUD10-F-020 | Medium | README.md | The test tree is out of date: `test_enums.py` shows 11 tests (actual 24), and `test_cli_requirements.py` (21) and `test_exit_code_entry_points.py` (8) are not listed. | README:76–126, 91 | Update the count and add the two modules |
| AUD10-F-021 | Medium | CSC-AUD-009 residuals | RR-003-004 (post-v1.6.0 CI-matrix results not recorded) and RR-003-005 remain open with no tracking issue, now that every GitHub issue is closed. | CSC-AUD-009 §6.2 closure note; Review_Record_v1.6:92 | Open tracking issues, or close them with evidence |
| AUD10-F-022 | Low | CSC-SWE2-001, CSC-SYS2-001, CSC-STD-001 | Only `misc.boolean_comparison` is marked opt-in; the other 7 post-v1.6.0 rules are not. | SWE2:228–235; SYS2:139; STD-001:306–313 | Mark all 8 rules as opt-in |
| AUD10-F-023 | Low | Rules-and-Configuration.md | The `variables` `case` value list omits `lower`, `upper` and `any`, which the code and the Case-style values section support. | R&C:225; `utils.py:59–67` | Complete the list, or link to the Case-style values section |
| AUD10-F-024 | Low | CSC-SWE3-001 | UNIT-98 step 4 says an existing file with `overwrite=False` → return 1. The code asks "Overwrite?" first and returns 1 only on "no". | SWE3:903; `wizard.py:214–222` | Correct step 4 |
| AUD10-F-025 | Low | CSC-SWE1-001 | The RTM row for SWE1-040..042 does not cite `test_case_style_config.py` (UV-CASE-005), which SWE4 §7 traces. | SWE1 RTM; SWE4:580 | Add the citation |
| AUD10-F-026 | Low | CSC-SWE3-001 | SWE3:71 says "the old monolithic `src/cstylecheck.py` no longer exists", but the file is a 28-line wrapper (SWE3:1528; SUP8 CI-001). "## 4.1 Package Structure" is at the wrong heading level. | SWE3:71, 214, 1528; SUP8:133 | Reword line 71 and use `###` for §4.1 |
| AUD10-F-027 | Low | CSC-SWE4-001, CSC-SWE3-001 | SWE4 §6 names `validate_case_styles`, `normalize_case_style` and `deprecated_key_warnings`, which are not catalogued units. `_enum_members` (#423) is not catalogued either. | SWE4:522–523; SWE3:338–339, 1504; `checker.py:175` | Catalogue them as sub-units, or add a note naming them as helpers of UNIT-05, UNIT-43 and UNIT-27 |
| AUD10-F-028 | Low | CSC-SYS5-001, CSC-SWE6-001 | The overall verdicts are stated at old baselines (SYS5: v1.4.1 with 1157 tests; SWE6: v1.6.0 with 1279) without saying so. | SYS5:410; SWE6:478 | State the baseline each verdict applies to, or add the `develop` run |
| AUD10-F-029 | Low | CSC-SUP8-001 | `logo/cstylecheck.jpg` and `docs/templates/ASPICE_CL2_Test_Case_Template_1.md` are tracked but belong to no CI. | `git ls-files`; SUP8 §6.1 | Add them to a CI, or state that they are excluded |
| AUD10-F-030 | Low | CSC-ACQ4-001 | The CI tool suppliers (pytest, pytest-cov, ruff, mypy, codespell) are not in the supplier list. | ACQ4:70–77; `requirements.txt`; `cstylecheck_tests.yml:139` | Add them as SUP-09, or state that they are out of scope |
| AUD10-F-031 | Low | CSC-MAN5-001 | Each risk's Status field reads "Released", while the summary table says Active/Accepted. | MAN5:181, 273–280 | Use Active/Accepted in the risk fields |
| AUD10-F-032 | Low | CHANGELOG.md; GP 2.2 | [Unreleased] has no "Breaking / Compatibility" heading grouping #422, #423 and #425 (the ⚠️ notes are scattered). The plan documents carry about 8 "resync-only" revision rows each on a single day (e.g. SUP1:23–30), which makes the change history hard to review. | CHANGELOG.md [Unreleased]; SUP1:23–30 | Add a Compatibility heading. Batch cross-reference resyncs into one revision per release |

### 6.2 Actions

| Action | Finding(s) | Owner | Status |
|---|---|---|---|
| Register CR-412/420/422/424/425 with impact analysis and approval; update CR-418 impact and close CR-413/418; record the release-classification decision | F-001, F-002, F-010 | Dermot Murphy (approval) / Claude | Closed in #430. Approval recorded as owner merge of each PR (DEV-002 §5.2); QA sign-off of CR-422/CR-425 given by the owner's merge of PR #426 / #428 (approval-by-merge policy, 2026-09-29) |
| Apply SEV labels to #410–#425 and record SLA outcomes (or amend SUP9) | F-011 | Dermot Murphy | Closed in #430. SEV labels applied on GitHub 2026-09-29 (#422, #423 SEV-1; #412, #425 SEV-2; #408, #410, #413, #424 SEV-3); SUP9 §6.2 register added |
| Repair the SYS2 ↔ SWE1 ↔ SYS3/SYS5 traces (SYS-F-046, §6 RTM rebuild, SWE1 §5 parents) | F-003, F-004, F-005, F-025 | Claude | Closed in #430 |
| Re-execute SYS-VTC-008 and annotate the 93178cd record | F-006 | Claude | Closed in #430 |
| Align SWE1-095 / SIT-024 with the copyright format and add a unit test | F-007 | Claude | Closed in #430 |
| Correct the SWE3 UNIT-05, UNIT-98 and §4 text; update SWE2 COMP-02/09/12 and §8.2 | F-008, F-009, F-022, F-024, F-026, F-027 | Claude | Closed in #430 |
| Update MAN3, MAN5, SUP1, SUP8 and DEV-002; sign CSC-REVIEW-003 and the approval tables | F-012 … F-016, F-031 | Dermot Murphy / Claude | Closed in #430. Signatures replaced by policy: CSC-REVIEW-003 and the approval tables are authorised by the owner's merge of PR #431 (CSC-DEV-002 §5.2) |
| Stale counts and text: PA2, SWE5, SWE6, README, R&C, SYS5/SWE6 verdict baselines | F-017 … F-020, F-023, F-028 | Claude | Closed in #430 |
| CM/ACQ housekeeping and CHANGELOG Compatibility heading | F-029, F-030, F-032 | Claude | Closed in #430 |
| Track or close the CSC-AUD-009 residuals RR-003-004/005 | F-021 | Dermot Murphy | Closed in #430. RR-003-004: GitHub Actions run 36612676061 on commit `6bdc592` (PR #431): Unit Tests Python 3.10, 3.11, 3.12 all success, 2026-09-29. RR-003-005: Risk Owner confirmation given by the owner's merge of PR #431 |

**Owner decisions (2026-09-29):** the next release is **v2.0.0 (Major)** per SUP10. SWE1-095 / SIT-024 follow the implemented `(C) <year> <holder>` format (no output change). SWE3 UNIT-05 step 2 is corrected to the implementation (no code change). SEV labels are applied retroactively. **Approval by merge:** *"Rather than signing to authorise, merging by me is taken as authorisation."* The owner's merge of the PR that introduces a work-product revision is its approval; no separate signature is required (CSC-DEV-002 §5.2).

**Closure note (2026-09-29):** All 32 findings were corrected under #430 on branch `ccr-15d55b1c-l6c5rf` in commits `71d9505` (SWE2–SWE4, UV-CLI-018 copyright assertion, README, Rules-and-Configuration.md, CHANGELOG), `158c381` (SYS2/3/5, SWE1/5/6, STD-001; SYS-VTC-008 re-executed with the installed command, 9/9 PASS) and `924fc2c` (SUP1/8/9/10, MAN3/5, ACQ4, PA2, DEV-002). After the corrections: `python -m pytest -q` 1545 passed; `ruff check src tests` clean; `codespell` clean. No product code or package version was changed.

Items still open after closure (owner actions, tracked in #430):
- ~~Signing CSC-REVIEW-003 and the work-product approval tables; QA sign-off of the High-impact CRs CR-422 and CR-425.~~ Resolved by policy (2026-09-29, CSC-DEV-002 §5.2): authorisation is the owner's merge of PR #431 (CSC-REVIEW-003, approval tables) and of PR #426 / #428 (CR-422 / CR-425 QA sign-off).
- ~~RR-003-004 (CI-matrix results) and RR-003-005 (Risk Owner confirmation).~~ RR-003-004 closed: GitHub Actions run 36612676061 on commit `6bdc592` (PR #431): Unit Tests Python 3.10, 3.11, 3.12 all success, 2026-09-29. RR-003-005 closed on the owner's merge of PR #431.
- Document-version citations (e.g. the PA2 §5.4 Version column) were out of scope and are updated at the next batched resync.

The §3 ratings (4 F / 13 L) remain the audit ratings and are re-assessed at the v2.0.0 release audit.

---

## 7. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Auditor | Claude (AI-assisted) | 2026-09-29 | *per CSC-DEV-001* |
| Audit Owner / Reviewer | Dermot Murphy | Merge date of the introducing PR | *Authorised by owner merge of the PR that added this record (CSC-DEV-002 §5.2)* |

> **Note:** This audit was conducted by an AI tool (Claude) acting in the auditor role as documented in CSC-DEV-001. The solo-developer independent-review constraint is formally acknowledged in CSC-DEV-002. The Audit Owner's merge of the PR that added this record constitutes the required management review approval; no signature is required and the merge commit is the approval record (approval-by-merge policy of 2026-09-29, CSC-DEV-002 §5.2).

---

*Document: CSC-AUD-010 · Version 1.2 · 2026-09-29 (§6.2 closure recorded, #430; v1.2: Approval-by-merge policy (CSC-DEV-002 §5.2), #430 — signatures replaced by owner merge, RR-003-004/005 closed)*
*Location: `docs/aspice/audits/CStyleCheck_ASPICE_Internal_Audit_2026-09-29b.md`*
