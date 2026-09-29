# Process Capability Records

*Automotive SPICE® PAM v4.0 | PA 2.1 Process Performance Management & PA 2.2 Work Product Management*

---

## 1. Document Identification & Control

| Field | Value | Field | Value |
|---|---|---|---|
| **Document ID** | CSC-PA2-001 | **Version** | 1.34 |
| **Project** | CStyleCheck | **Date** | 2026-09-29 |
| **Status** | Released | **Classification** | Internal |
| **Author** | Claude | **Reviewer** | Dermot Murphy |
| **Approver** | Dermot Murphy | **Related Process** | PA 2.1, PA 2.2 |

---

## 2. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.34 | 2026-09-29 | Claude | CSC-AUD-010 corrective actions (#430). AUD10-F-017: §6 SWE.3 135→136 units; §5.4 CM-baseline column cites the post-v1.6.0 changes (#408–#425) per work product and #430, with a note; CI-017 and CI-045 baseline → `develop` `2444036`. AUD10-F-021: §5.4 records that CSC-AUD-009 residuals RR-003-004/005 are tracked under #430. AUD10-F-002: §6 MAN.3 next release v2.0.0. AUD10-F-012: §6 MAN.5 9 risks. AUD10-F-030: §6 ACQ.4 9 suppliers. AUD10-F-014: §5.3 approval record = owner's PR merge |
| 1.33 | 2026-09-29 | Claude | #423: SWE.4 evidence — test total 1532→1545 (last enum member checked with and without trailing comma, `tests/test_enums.py`); referenced-document versions resynced (21) |
| 1.32 | 2026-09-29 | Claude | #425: SWE.4 evidence — test total 1524→1532, 57→58 modules (config/usage errors exit 2 from the console script and the wrapper, `tests/test_exit_code_entry_points.py`); SWE.3 objective 136 units (UNIT-136 `config_error`); referenced-document versions resynced (21) |
| 1.31 | 2026-09-29 | Claude | #424: SWE.4 evidence — test total 1508→1524, 56→57 modules (`functions.case` removed: not generated, deprecated with a warning, `tests/test_functions_case_removed.py`); referenced-document versions resynced (21) |
| 1.30 | 2026-09-29 | Claude | #422: SWE.4 evidence — test total 1481→1508, 55→56 modules (case-style names, alias normalisation and unknown-style config error, `tests/test_case_style_config.py`); referenced-document versions resynced (21) |
| 1.29 | 2026-09-29 | Claude | #420: SWE.4 evidence — test total 1463→1481 (presets / `--init` enable the standard-specific opt-in rules); referenced-document versions resynced (21) |
| 1.28 | 2026-09-29 | Claude | #418 (CR-418): SWE.4 evidence — test total 1452→1463 (the 7 remaining post-v1.6.0 rules opt-in; policy tests); referenced-document versions resynced (21) |
| 1.27 | 2026-09-29 | Claude | #412: SWE.4 evidence — test total 1444→1452 (`misc.boolean_comparison` opt-in, lowercase only); referenced-document versions resynced (21) |
| 1.26 | 2026-09-29 | Claude | Release-prep cross-reference resync: 21 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.25 | 2026-09-29 | Claude | #413: SWE.4 evidence — test total 1439→1444; SWE1-094 fully verified after CR-413 |
| 1.24 | 2026-09-29 | Claude | Issue #407: §4.1 SWE.4 criterion and CI-017 → 1439 tests; §6 SWE.4 evidence (55 modules, RR-003-001 closed, SWE1-094 `--quiet` gap); §5.4 register CSC-AUD-009 1.0→1.1 and CSC-REVIEW-003 1.0→1.1; referenced-document versions resynced (ACQ4 1.4→1.5, DEV-001 1.3→1.4, DEV-002 1.2→1.3, MAN3 1.8→1.9, MAN5 1.5→1.6, PA2 1.23→1.24, STD 1.3→1.4, SUP1 1.10→1.11, SUP10 1.3→1.4, SUP8 1.13→1.14, SUP9 1.3→1.4, SWE1 2.8→2.9, SWE2 1.13→1.14, SWE3 1.18→1.19, SWE4 1.22→1.24, SWE5 1.15→1.16, SWE6 1.17→1.18, SYS2 2.3→2.4, SYS3 1.7→1.8, SYS4 1.12→1.13, SYS5 1.9→1.10) |
| 1.23 | 2026-09-29 | Claude | CSC-AUD-009 corrective actions (#405). AUD9-F-021: §6 ratings per CSC-AUD-009 (3 F / 14 L), verdict and history note (no standalone v1.6.0 audit record); §4.1 counts (121 SW req, 135 units, 1422 tests, 27 SIT, 17 SITC, 60 CIs); §5.4 versions for all corrected WPs plus CSC-REVIEW-003, CSC-STD-001 and CSC-AUD-009; CI-045 package row. AUD9-F-013: SWE.3 wording (135 units, all specified). AUD9-F-009: §5.3 WP storage CI-027 → CI-055 |
| 1.22 | 2026-07-06 | Claude | ASPICE audit — §4.1 SYS.4 15→16 SITC, SUP.8 34→37 CIs; §5.4 SYS2→2.2, SYS3→1.6, SYS4→1.11, SYS5→1.8, SUP8→1.11, SUP1→1.9, MAN3→1.7; §6 SYS.4/SUP.8 counts — closes #379 |
| 1.21 | 2026-07-06 | Claude | ASPICE audit — §5.4 cross-refs updated: SWE1 2.4→2.6, SWE2 1.11→1.12, SWE3 1.15→1.16, SWE4 1.19→1.20, SWE5 1.13→1.14, SWE6 1.15→1.16, SUP8 1.9→1.10, SVD 1.20→1.22, PA2 self 1.19→1.20; §4.1 SWE.1 count 91→99; §6 fix SYS.5/SWE.6 rule count 72→73, SWE.5/SWE.6 counts; self-ref fixed — closes #377 |
| 1.20 | 2026-07-06 | Claude | v1.6.0 RC — update §4.1 SWE.4 tests 1183→1279; §5.4 doc versions updated (SVD 1.22, SWE4 1.19, SWE5 1.13, SWE6 1.15, SYS4 1.10); §6 counts updated (73 rules, 1279 tests, 21 SIT); CI-001/CI-017 to v1.6.0; full ASPICE audit pending before release |
| 1.19 | 2026-06-28 | Claude | Update to v1.5.1 baseline: §4.1 SWE.1 requirements 70→91, SWE.4 tests 1157→1183, SWE.5 SIT cases 19→20; §5.4 all doc versions updated (SVD 1.20, SWE1 2.4, SWE2 1.11, SWE3 1.15, SWE4 1.17, SWE5 1.11, SWE6 1.13, SYS2 2.1, SYS4 1.9, SUP1 1.8, SUP8 1.9); CI-001/CI-017 to v1.5.1; add CSC-AUD-008 row; §6 ratings/counts updated (72 rules, 91 req, 1183 tests, 20 SIT); §7 dates updated |
| 1.18 | 2026-06-26 | Claude | §6: advance SYS.2 L→F (RTM placeholders resolved; §3.3 SWE1-001 added; scope updated to v1.4.1); verdict 16F/1L→17F/0L; §5.4: SYS2 to 1.9, self to 1.18 — closes issue #292 |
| 1.17 | 2026-06-26 | Claude | §6: advance SYS.4/SYS.5/SWE.5/SWE.6 L→F (SITC-015 + SIT-019 added; SYS-F-020 expanded; AUD7-F-001 fully resolved); verdict 12F/5L→16F/1L — closes issue #261 |
| 1.16 | 2026-06-26 | Claude | §6: advance SUP.1 L→F (recurring review process established; CSC-REVIEW-002 produced); verdict 11F/6L→12F/5L; §5.4: update SUP1 to 1.5, add CSC-REVIEW-001/002 rows, self to 1.16 — closes issue #268 |
| 1.15 | 2026-06-26 | Claude | §6: advance MAN.5 L→F and ACQ.4 L→F (RISK-003/005 treatments implemented; SUP-06 added); verdict 9F/8L→11F/6L; §5.4: update MAN5 to 1.4, ACQ4 to 1.3, self to 1.15 |
| 1.14 | 2026-06-25 | Claude | §5.4: add missing CSC-AUD-005 and CSC-AUD-006 rows; update CSC-SYS2-001 to 1.7; update self to 1.14 — closes issues #266, #270 |
| 1.13 | 2026-06-25 | Claude | Doc accuracy — update §5.4 baseline table: all document versions synced to v1.4.1 state (CSC-AUD-007 / PR #281); fix CI-001/CI-017 versions; update §5.4 preamble |
| 1.12 | 2026-06-25 | Claude | AUD7-F-001 doc fix — update §6 SWE.6 capability summary; update CL2 verdict note to reflect SYS-VTC-003/SWQ-003 updated to 71 rule IDs; remaining test-scope gap still pending v1.5.0 |
| 1.11 | 2026-06-18 | Claude | Fix §6 verdict summary arithmetic (11 F, 6 L → 9 F, 8 L; table itself was already correct); bump CSC-AUD-007 §5.4 entry to v1.1 (matching erratum); reorganise Wiki publishing into Deviations/Audits sections — see issue tracker |
| 1.10 | 2026-06-18 | Claude | CSC-AUD-007 — §6 was stale since 2026-05-28 (predated issue #152 closure and superseding audit CSC-AUD-002); resync §6 ratings/verdict to current `main` (v1.4.0); CL2 confirmed ACHIEVED; add §5.4 rows for CSC-AUD-002/CSC-AUD-007 |
| 1.9 | 2026-06-18 | Claude | ASPICE audit #254 — update §4.1/§5.4/§6 SWE.4 test count 965→1152; mark CI-017 released at v1.3.0 |
| 1.8 | 2026-06-04 | Claude | Deep accuracy audit: fix §4.1 SWE.3 unit count (46→90), SUP.8 CI count (27→34), §6 SWE.3 (89→90) and SUP.8 (29→34); update §5.4 document version table — resolves issue #163 |
| 1.7 | 2026-06-04 | Claude | Automated accuracy audit: update §4.1 SWE.4 test count ≥500→965, §5.2 SWE.4 839→965, §5.4 CI-017 839→965 and SUP9/10/ACQ4 versions, §6 SWE.4 839→965 — resolves issue #163 |
| 1.6 | 2026-05-29 | Claude | §5.4: mark all work products Released at v1.2.0 tag; update SVD to 1.2, PA2 to 1.6, AUD-001 to Released |
| 1.5 | 2026-05-28 | Dermot Murphy | §5.4: update all document version numbers to reflect issues #146–#157 changes — closes issue #156 |
| 1.4 | 2026-05-28 | Claude / Dermot Murphy | Internal audit CSC-AUD-001: populate §6 Assessment Verdicts for all 17 processes (N/P/L/F); update §5.4 document version table to current versions; add audit report reference — closes issue #136 |
| 1.3 | 2026-05-28 | Dermot Murphy | Update SWE.4 performance objective: subprocess coverage instrumented, gate 85% combined; actual 87.31% combined / 89.8% stmt — closes issue #54 |
| 1.2 | 2026-05-28 | Dermot Murphy | Add CSC-DEV-002 deviation reference at GP 2.2.3; add CI-028 (SVD) and CI-029 (DEV-002) to §5.4 — closes issue #61 |
| 1.1 | 2026-05-28 | Dermot Murphy | Add deviation reference at GP 2.1.6 — closes issue #52 |
| 1.0 | 2026-04-12 | Claude | Initial release |

---

## 3. Purpose

This document records the generic practices evidence for **Automotive SPICE® PAM v4.0 Capability Level 2** across all assessed processes. It provides a single consolidated reference for assessors to verify PA 2.1 (Process Performance Management) and PA 2.2 (Work Product Management) achievement for CStyleCheck v1.5.1.

**PA 2.1** requires that each process is planned, monitored, and adjusted.
**PA 2.2** requires that work products are defined, stored, controlled, reviewed, and adjusted.

---

## 4. PA 2.1 — Process Performance Management

### 4.1 GP 2.1.1 — Define Process Performance Objectives

For each assessed process, performance objectives are defined in the table below.

| Process | Performance Objective | Defined In | Status |
|---|---|---|---|
| SYS.2 | System requirements complete, reviewed, and approved before architecture begins | CSC-MAN3-001 §5.1 (PH-01 exit criteria) | ✅ Defined |
| SYS.3 | Architecture reviewed and approved; all SYS.2 requirements traced to architecture elements | CSC-SYS3-001 §9 traceability matrix | ✅ Defined |
| SYS.4 | All 17 SITC integration test cases PASS before SYS.5 begins | CSC-SYS4-001 §5 verification criteria | ✅ Defined |
| SYS.5 | All SYS-VTC test cases PASS; 100% requirements coverage; no open critical Issues | CSC-SYS5-001 §3.4 verification criteria | ✅ Defined |
| SWE.1 | 121 software requirements defined, reviewed, approved; 113 traceable to a SYS.2 parent, and the 8 trend-metrics requirements (SWE1-102 to SWE1-108, SWE1-117) traceable to CSC-MAN3-001 §10.3 | CSC-SWE1-001 §4.18 verification criteria | ✅ Defined |
| SWE.2 | Architecture reviewed; all SWE.1 requirements mapped to components; interfaces defined | CSC-SWE2-001 §10 traceability | ✅ Defined |
| SWE.3 | All 136 units designed (UNIT-01 to UNIT-136, each with a §5 specification); resource usage documented | CSC-SWE3-001 §4 unit catalogue | ✅ Defined |
| SWE.4 | ≥ 85% combined statement + branch coverage (CI gate); ≥ 90% statement / ≥ 85% branch (long-term target); all 1545 unit tests PASS on Python 3.10/11/12 | CSC-SWE4-001 §4.2 coverage criteria | ✅ Defined |
| SWE.5 | All 27 SIT integration test cases PASS; all 10 SWA interfaces covered | CSC-SWE5-001 §3.3 verification criteria | ✅ Defined |
| SWE.6 | All 12 SWQ qualification test cases PASS; 100% SW requirements coverage; release gate met | CSC-SWE6-001 §3.3 qualification criteria | ✅ Defined |
| MAN.3 | All WBS work packages completed; milestones achieved within schedule | CSC-MAN3-001 §8 schedule | ✅ Defined |
| MAN.5 | All risks identified, scored, and treated; no High residual risks at release | CSC-MAN5-001 §6 risk summary | ✅ Defined |
| SUP.1 | All QA gates pass; pre-release checklist complete; zero open bug Issues | CSC-SUP1-001 §4 quality objectives | ✅ Defined |
| SUP.8 | All 60 CIs identified, version-controlled, and baselined per release | CSC-SUP8-001 §6 CI list | ✅ Defined |
| SUP.9 | All SEV-1 problems resolved before release; regression tests added for SEV-1/2 | CSC-SUP9-001 §5.5 closure criteria | ✅ Defined |
| SUP.10 | All approved CRs implemented with PR, CI passing, and document updates | CSC-SUP10-001 §5.5 closure criteria | ✅ Defined |
| ACQ.4 | All supplier acceptance criteria met; no unresolved supplier non-conformances at release | CSC-ACQ4-001 §5 monitoring activities | ✅ Defined |

### 4.2 GP 2.1.2 — Define Process Strategy

| Process | Strategy Summary | Defined In |
|---|---|---|
| SYS.2–SYS.5 | V-model lifecycle; requirements → architecture → integration test → qualification | CSC-MAN3-001 §5 lifecycle |
| SWE.1–SWE.6 | V-model lifecycle; SW requirements → architecture → detailed design → unit → integration → qualification | CSC-MAN3-001 §5 lifecycle |
| MAN.3 | Git Flow branching; WBS with effort estimates; milestone-based schedule | CSC-MAN3-001 §6–8 |
| MAN.5 | Risk scoring (Likelihood × Impact = RPN); treatment and monitoring per risk | CSC-MAN5-001 §4 strategy |
| SUP.1 | Automated CI gates + manual pre-release checklist | CSC-SUP1-001 §5 QA activities |
| SUP.8 | Git-based version control; annotated tags for baselines; dual-registry Docker | CSC-SUP8-001 §7–8 |
| SUP.9 | GitHub Issues (bug label); severity-driven resolution time targets | CSC-SUP9-001 §4–5 |
| SUP.10 | GitHub Issues (CR labels); impact-based approval; Git Flow implementation | CSC-SUP10-001 §4–5 |
| ACQ.4 | Per-supplier monitoring activities; acceptance criteria; non-conformance handling | CSC-ACQ4-001 §5–7 |

### 4.3 GP 2.1.3 to GP 2.1.5 — Plan, Monitor, and Adjust Process Performance

| Process | Planning Evidence | Monitoring Evidence | Adjustment Mechanism |
|---|---|---|---|
| SYS.2–SWE.6 | Section entry/exit criteria in each document; WBS in MAN.3 | CI build status; document review records | Change request (SUP.10) if criteria not met |
| MAN.3 | WBS table with effort and status; milestone schedule | Weekly Issue board review; CI badge | Schedule update + risk register update |
| MAN.5 | Risk register with treatment activities | Monthly risk review; trigger-based updates | Risk score revision; new treatment if residual RPN rises |
| SUP.1 | QA activity schedule; CI gate definitions | CI run results; pre-release checklist | Non-conformance handling (SUP.9 / SUP.10) |
| SUP.8 | CM plan (this document); CI identification list | Git log; baseline FCA/PCA checklists | CM plan update via SUP.10 |
| SUP.9 | Problem resolution SLA targets | Open Issue count; resolution time tracking | Process step revision if SLAs missed |
| SUP.10 | CR process steps; approval thresholds | CR cycle time tracking | Process revision if approval bottlenecks arise |
| ACQ.4 | Supplier monitoring schedule | CI job results; advisory review notes | Supplier non-conformance issue + CR if required |

### 4.4 GP 2.1.6 — Define Responsibilities

> **Note — AI-Assisted Authorship Deviation (CSC-DEV-001):** The entries below reflect Claude (AI assistant) as the authoring tool used to produce work products. All roles carry **Dermot Murphy** as the accountable human responsible party. The `Author: Claude` fields throughout all 18 ASPICE work products are accepted under deviation record **CSC-DEV-001** (`docs/aspice/CStyleCheck_DEV001_AI_Authorship_Deviation.md`), which documents the justification and residual risk. Claude holds no independent authority; Dermot Murphy reviewed and approved all outputs.

| Role | Authoring Tool | Accountable Person | Process Responsibility |
|---|---|---|---|
| Project Manager / CM Manager | Claude | Dermot Murphy | MAN.3, MAN.5, SUP.8, ACQ.4 |
| Lead Developer | Claude | Dermot Murphy | SWE.1, SWE.2, SWE.3, SWE.4 implementation |
| Test Lead | Claude | Dermot Murphy | SWE.4, SWE.5, SWE.6, SYS.4, SYS.5 execution |
| Quality Assurance | — | Dermot Murphy | Document reviews; PR reviews; pre-release checklist |
| CI System | — | GitHub Actions | Automated enforcement of GATE-01, GATE-02, GATE-03 |

### 4.5 GP 2.1.7 — Manage Interfaces

| Interface | Parties | Agreement | Communication Method |
|---|---|---|---|
| CI → Developer | GitHub Actions ↔ Claude | CI must pass before merge to `develop`/`main` | GitHub Actions status checks; email notification |
| Developer → Reviewer | Claude ↔ Reviewer | PR requires at least 1 approval for Medium/High impact | GitHub PR review mechanism |
| Developer → QA | Claude ↔ QA role | Pre-release checklist must be signed before release | CSC-SUP1-001 §5.4 checklist |
| Project → Suppliers | CStyleCheck ↔ SUP-01 to SUP-06 | Acceptance criteria per CSC-ACQ4-001 §5 | CI jobs; advisory monitoring; PR review gate |
| Project → Assessor | CStyleCheck ↔ ASPICE Assessor | Full documentation set; CI evidence; GitHub repository access | Document delivery; GitHub access grant |

---

## 5. PA 2.2 — Work Product Management

### 5.1 GP 2.2.1 — Define Requirements for Work Products

All work products are defined with content requirements in their respective document templates. The following table summarises the defining document for each work product type.

| Work Product | WP ID (PAM v4.0) | Content Requirements Defined In | CI Reference |
|---|---|---|---|
| System Requirements Specification | 17-10 | CSC-SYS2-001 §5 requirements tables | CI-055 (ASPICE work products) |
| System Architecture Description | 04-04 (adapted) | CSC-SYS3-001 §5 subsystem descriptions | CI-055 |
| System Integration Test Spec | 13-12 | CSC-SYS4-001 §4 test cases | CI-055 |
| System Verification Report | 13-13 | CSC-SYS5-001 §5 results table | CI-055 |
| Software Requirements Specification | 17-10 | CSC-SWE1-001 §4 requirements tables | CI-055 |
| Software Architecture Description | 04-04 | CSC-SWE2-001 §5 component descriptions | CI-055 |
| Software Detailed Design | 04-05 | CSC-SWE3-001 §5 unit designs | CI-055 |
| Unit Verification Specification | 13-12 | CSC-SWE4-001 §5 test catalogue | CI-055 |
| Integration Test Specification | 13-12 | CSC-SWE5-001 §4 test cases | CI-055 |
| Qualification Test Specification | 13-12 | CSC-SWE6-001 §4 test cases | CI-055 |
| Source code (`cstylecheck.py`) | 20-04 | CSC-SWE3-001 unit specifications | CI-001 |
| Test suite | 13-12 | CSC-SWE4-001 test catalogue | CI-017 |
| Configuration Management Plan | 08-27 | CSC-SUP8-001 — this document is the plan | CI-055 |
| Project Management Plan | 08-14 | CSC-MAN3-001 | CI-055 |
| Risk Register | 08-26 | CSC-MAN5-001 §5 risk register | CI-055 |
| Quality Assurance Plan | 08-15 | CSC-SUP1-001 | CI-055 |
| Problem Resolution Records | 13-07 | CSC-SUP9-001 §6 register; GitHub Issues | GitHub |
| Change Requests | 13-01 | CSC-SUP10-001 §7 register; GitHub Issues | GitHub |
| Supplier Monitoring Records | 08-16 | CSC-ACQ4-001 §5 monitoring tables | CI-055 |

### 5.2 GP 2.2.2 — Store and Control Work Products

| Work Product Type | Storage | Version Control | Access Control |
|---|---|---|---|
| Source code and config files | Git repository (`main` branch + tags) | Git SHA; annotated tags | GitHub repository permissions |
| ASPICE documentation (`.md` files) | Git repository + outputs directory | Git SHA; annotated tags | GitHub repository permissions |
| Docker images | GHCR + Docker Hub | Image tag + SHA-256 digest | GHCR: repository-scoped token |
| Problem reports and CRs | GitHub Issues | Issue number; state; labels | GitHub repository permissions |
| CI run evidence | GitHub Actions logs + artefacts | Workflow run ID; commit SHA | GitHub repository; 30-day artefact retention |
| Release packages | GitHub Releases | Release tag | Public (MIT licence) |

**Baseline procedure:** See CSC-SUP8-001 §8.2.

### 5.3 GP 2.2.3 — Review and Adjust Work Products

> **Note — Single-Person Reviewer Deviation (CSC-DEV-002):** CStyleCheck has one human team member (Dermot Murphy). All ASPICE work products carry `Reviewer: Dermot Murphy` and `Approver: Dermot Murphy` — the same individual. This deviates from the GP 2.2.3 expectation of an independent reviewer. The deviation is formally accepted under **CSC-DEV-002** (`docs/aspice/CStyleCheck_DEV002_Independent_Review_Deviation.md`), which documents the justification, compensating controls (AI-assisted review, CI quality gates, PR audit trail), and residual risk. Assessors may rate this practice as Largely Achieved rather than Fully Achieved on the independence criterion.

All work products are reviewed before approval according to the following schedule:

| Work Product | Review Type | Reviewer | Review Evidence |
|---|---|---|---|
| Source code changes | Pull request review | Dermot Murphy (see CSC-DEV-002) | Owner's PR merge (approval record, CSC-DEV-002 §5.2) |
| ASPICE documents | Formal document review | Dermot Murphy (see CSC-DEV-002) | Reviewer/Approver table in each document |
| Test suite additions | Pull request review | Dermot Murphy (see CSC-DEV-002) | Owner's PR merge (approval record, CSC-DEV-002 §5.2) |
| CI workflow changes | Pull request review | Dermot Murphy (see CSC-DEV-002) | Owner's PR merge (approval record, CSC-DEV-002 §5.2) |
| Release baseline | Pre-release checklist | Dermot Murphy / QA role | CSC-SUP1-001 §5.4 signed checklist |

**Adjustment mechanism:** Any non-conformance found during review is raised as a GitHub Issue (SUP.9) or change request (SUP.10) and tracked to resolution before the work product is approved.

### 5.4 Work Product Baseline Status

*Updated 2026-09-29. Document versions reflect the CSC-AUD-009 corrective-action baseline (#405) on `claude/aspice-audit-2026-09-29` → `develop`, as bumped by #407 (unit tests for SWE1-015/094/096 and the resulting cross-reference resync). CSC-SVD-001 stays at the v1.6.0 release baseline until the next release.*

*Change notes (CSC-AUD-010 AUD10-F-017, #430): the CM Baseline column lists, per work product, the post-v1.6.0 issues that changed its content (#408 to #425) and the issues for which only cross-references were resynced ("resync"). "CSC-AUD-010 (#430)" marks the documents revised by the CSC-AUD-010 corrective actions; the Version column is not yet resynced for #430 and is updated in the next batched cross-reference resync (CSC-SUP8-001 §9). The CSC-AUD-009 residuals RR-003-004 (post-v1.6.0 CI-matrix results not recorded) and RR-003-005 (Risk Owner confirmation of the RISK-003/005 reviews) remain open and are tracked under #430 (AUD10-F-021).*

| Document ID | Work Product | Version | Baseline Status | CM Baseline |
|---|---|---|---|---|
| CSC-SYS2-001 | System Requirements Spec | 2.13 | Released | CSC-AUD-009 corrective actions (#405); #407; #410, #413, #418; resync #418–#425 |
| CSC-SYS3-001 | System Architecture Description | 1.16 | Released | CSC-AUD-009 corrective actions (#405); #407; resync #418–#425 |
| CSC-SYS4-001 | System Integration Test Spec | 1.22 | Released | CSC-AUD-009 corrective actions (#405); #407; #408, #412, #413, #418, #420, #422–#425; resync #418–#425 |
| CSC-SYS5-001 | System Verification Report | 1.19 | Released | CSC-AUD-009 corrective actions (#405); #407; #408, #412, #413, #418, #420, #422–#425; resync #418–#425 |
| CSC-SWE1-001 | SW Requirements Spec | 2.19 | Released | CSC-AUD-009 corrective actions (#405); #407; #410, #412, #413, #418, #420, #422–#425; resync #418–#425 |
| CSC-SWE2-001 | SW Architecture Description | 1.24 | Released | CSC-AUD-009 corrective actions (#405); #407; #410, #412, #413, #418, #420, #422, #425; resync #418–#425 |
| CSC-SWE3-001 | SW Detailed Design | 1.29 | Released | CSC-AUD-009 corrective actions (#405); #407; #410, #412, #413, #418, #420, #422–#425; resync #418–#425 |
| CSC-SWE4-001 | Unit Verification Spec | 1.34 | Released | CSC-AUD-009 corrective actions (#405); #407; #408, #410, #412, #413, #418, #420, #422–#425; resync #418–#425 |
| CSC-SWE5-001 | Integration Test Spec | 1.25 | Released | CSC-AUD-009 corrective actions (#405); #407; #408, #412, #413, #418, #420; resync #418–#425 |
| CSC-SWE6-001 | Qualification Test Spec | 1.28 | Released | CSC-AUD-009 corrective actions (#405); #407; #408, #410, #412, #413, #418, #420, #422–#425; resync #418–#425 |
| CSC-MAN3-001 | Project Management Plan | 1.18 | Released | CSC-AUD-009 corrective actions (#405); #407; #412, #413, #418, #420, #422–#425; resync #418–#425; CSC-AUD-010 (#430) |
| CSC-MAN5-001 | Risk Management Plan | 1.14 | Released | CSC-AUD-009 corrective actions (#405); #407; resync #418–#425; CSC-AUD-010 (#430) |
| CSC-SUP1-001 | Quality Assurance Plan | 1.19 | Released | CSC-AUD-009 corrective actions (#405); #407; #413, #418; resync #418–#425; CSC-AUD-010 (#430) |
| CSC-SUP8-001 | Configuration Management Plan | 1.22 | Released | CSC-AUD-009 corrective actions (#405); #407; resync #418–#425; CSC-AUD-010 (#430) |
| CSC-SUP9-001 | Problem Resolution Plan | 1.12 | Released | CSC-AUD-009 corrective actions (#405); #407; resync #418–#425; CSC-AUD-010 (#430) |
| CSC-SUP10-001 | Change Request Plan | 1.13 | Released | CSC-AUD-009 corrective actions (#405); #407; #413, #418; resync #418–#425; CSC-AUD-010 (#430) |
| CSC-ACQ4-001 | Supplier Monitoring Plan | 1.13 | Released | CSC-AUD-009 corrective actions (#405); #407; resync #418–#425; CSC-AUD-010 (#430) |
| CSC-PA2-001 | PA 2.1 / PA 2.2 Records | 1.33 | Released | CSC-AUD-009 corrective actions (#405); #407; #412, #413, #418, #420, #422–#425; resync #418–#425; CSC-AUD-010 (#430) |
| CSC-REVIEW-001 | ASPICE Peer Review Record (v1.2.1 baseline) | 1.0 | Released | issue #169 |
| CSC-REVIEW-002 | ASPICE Peer Review Record (v1.4.1 baseline) | 1.0 | Released | PR (issue #268) |
| CSC-REVIEW-003 | ASPICE Peer Review Record (v1.6.0 / post-v1.6.0 `develop`; retrospective for v1.5.x–v1.6.0; self-review under CSC-DEV-002) | 1.1 | Released (pending Review Owner signature) | CSC-AUD-009 corrective actions (#405); RR-003-003 closed (#408), RR-003-001 closed (#407) |
| CSC-STD-001 | Industry Standards Comparison | 1.13 | Released | CSC-AUD-009 corrective actions (#405); #407; #410; resync #418–#425 |
| CSC-DEV-001 | AI Authorship Deviation Record | 1.12 | Released | CSC-AUD-009 corrective actions (#405); #407; resync #418–#425 |
| CSC-DEV-002 | Independent Review Deviation Record | 1.11 | Released | CSC-AUD-009 corrective actions (#405); #407; resync #418–#425; CSC-AUD-010 (#430) |
| CSC-SVD-001 | Software Version Description | 1.23 | Released | ASPICE audit #379 |
| CSC-AUD-001 | ASPICE Internal Audit Report | 1.0 | Released | v1.2.0 tag |
| CSC-AUD-002 | ASPICE Internal Audit — CL2 Re-assessment (2026-05-29) | 1.0 | Released | v1.2.1 tag |
| CSC-AUD-003 | ASPICE Internal Audit — Accuracy (2026-06-04) | 1.0 | Released | issue #163 audit |
| CSC-AUD-004 | ASPICE Internal Audit — Deep Accuracy (2026-06-04) | 1.0 | Released | issue #163 deep audit |
| CSC-AUD-005 | ASPICE Internal Audit — Post-release accuracy (2026-06-05) | 1.0 | Released | issue #163 / v1.3.0 |
| CSC-AUD-006 | ASPICE Internal Audit — Test/module-count drift (2026-06-18) | — | Released (issue #254 only; no standalone report) | issue #254 |
| CSC-AUD-007 | ASPICE Internal Audit — CL2 Re-assessment (2026-06-18) | 1.1 | Released | v1.4.0 tag |
| CSC-AUD-008 | ASPICE Internal Audit — CL2 Assessment (2026-06-28) | 1.0 | Released | v1.5.1 tag |
| CSC-AUD-009 | ASPICE Internal Audit — CL2 Re-assessment, post-v1.6.0 `develop` (2026-09-29) | 1.1 | Released | #405; AUD9-F-027 residual (#408) and AUD9-F-004 closure (#407) |
| CI-045 | `src/cstylecheck/` package (12 modules) | 1.6.0 + `develop` | Released (v1.6.0); `develop` in progress | v1.6.0 tag / `develop` `2444036` |
| CI-017 | Test suite (1279 tests at v1.6.0; 1545 on `develop`) | 1.6.0 + `develop` | Released (v1.6.0); `develop` in progress | v1.6.0 tag / `develop` `2444036` |

---

## 6. ASPICE CL2 Coverage Summary

*Updated 2026-09-29. Ratings from internal audit CSC-AUD-009 (post-v1.6.0 `develop`, commit `296e91b`): 3 F, 14 L, 0 P/N. CL2 is maintained. Corrective actions for all 28 findings were applied under #405 on 2026-09-29. Re-rating is due at the next release audit.*

The table below summarises all assessed processes and their CL2 PA achievement evidence as rated by CSC-AUD-009. The evidence column reflects the state after the #405 corrective actions.

| Process | PA 1.1 (Performed) | PA 2.1 (Perf. Mgmt) | PA 2.2 (WP Mgmt) | Assessment Verdict | Open Issue(s) |
|---|---|---|---|---|---|
| SYS.2 | 58 SYS REQ-IDs; SYS-F-011 81 rule IDs; SYS-F-046 → SWE1-094 corrected; bidirectional RTM (AUD9-F-005/F-008) | Objectives: §4.1; strategy: §4.2 | CSC-SYS2-001 v2.4; in CM | **L** | #405 |
| SYS.3 | Architecture with subsystems and interfaces; §9 covers 81 rule IDs | Objectives: §4.1; monitoring: §4.3 | CSC-SYS3-001 v1.8; in CM | **F** | — |
| SYS.4 | 17 SITC test cases (SITC-017 adds the 8 post-v1.6.0 rules); all 81 rules covered | Objectives: §4.1 | CSC-SYS4-001 v1.13; in CM | **L** | #405 |
| SYS.5 | SYS-VTC-003 covers all 81 rule IDs; SYS-VTC-007 updated for #394 | Objectives: §4.1 | CSC-SYS5-001 v1.10; in CM | **L** | #405 |
| SWE.1 | 121 SW requirements (SWE1-109 to SWE1-117 added); SWE1-102 to 108/117 parent = CSC-MAN3-001 §10.3 | Objectives: §4.1; strategy: §4.2 | CSC-SWE1-001 v2.9; in CM | **L** | #405 |
| SWE.2 | 13 components (COMP-13 trend scripts added), 10 interfaces; COMP-05f and run_all() include the 8 new checks | Objectives: §4.1 | CSC-SWE2-001 v1.14; in CM | **L** | #405 |
| SWE.3 | 136 units, all with §5 specs; line references regenerated; §6.3 baseline format corrected | Objectives: §4.1 | CSC-SWE3-001 v1.19; in CM | **L** | #405 |
| SWE.4 | 1545 unit tests (58 modules); §7 traces all SW requirements; SWE1-015/094/096 unit tests added by #407 (RR-003-001 closed; SWE1-094 aligned with the implementation by CR-413 (#413), fully verified) | Objectives: §4.1; coverage targets | CSC-SWE4-001 v1.24; CI evidence | **L** | #405 |
| SWE.5 | 27 SIT tests (SIT-027 for the 8 new rules); SIT-012 updated for #394/#395 | Objectives: §4.1 | CSC-SWE5-001 v1.16; in CM | **L** | #405 |
| SWE.6 | 12 SWQ tests; SWQ-003 covers 81 rule IDs; SWQ-007 aligned with SWE1-100; 113/113 in-scope requirements | Objectives: §4.1; release gate | CSC-SWE6-001 v1.18; CI evidence | **L** | #405 |
| MAN.3 | WBS, schedule (actuals to v1.6.0; next release v2.0.0 (Major) planned, classification decision §8) and trend-metrics monitoring (§10.3) | Objectives: §4.1; §4.3 monitoring | CSC-MAN3-001 v1.9; in CM | **L** | #405 |
| MAN.5 | 9 risks (RISK-009 upgrade compatibility added by #430); RISK-003/005 reviewed 2026-09-29 (next 2026-12-29); Dependabot target branch recorded | Objectives: §4.1; risk monitoring | CSC-MAN5-001 v1.6; in CM | **L** | #405 |
| SUP.1 | QA gates and checklist; gate compliance record added; CSC-REVIEW-003 produced retrospectively for v1.5.x–v1.6.0 | Objectives: §4.1; CI evidence | CSC-SUP1-001 v1.11; in CM | **L** | #405 |
| SUP.8 | 60 CIs (package, dependabot.yml, docs added); hotfix versioning/tagging policy §7.6 | Objectives: §4.1; CM monitoring | CSC-SUP8-001 v1.14; in CM | **L** | #405 |
| SUP.9 | Problem process with SLAs and register | Objectives: §4.1; Issue metrics | CSC-SUP9-001 v1.4; in CM | **F** | DEV-002 |
| SUP.10 | CR process with impact levels and approval | Objectives: §4.1; CR metrics | CSC-SUP10-001 v1.4; in CM | **F** | DEV-002 |
| ACQ.4 | 9 suppliers (SUP-07 Docker actions, SUP-08 third-party actions added; SUP-09 development/CI tools added by #430); Actions versions current; SHA-pinning policy | Objectives: §4.1; monitoring schedule | CSC-ACQ4-001 v1.5; in CM | **L** | #405 |

> **📋 Rating scale:** N = Not achieved (0–15%), P = Partially achieved (15–50%), L = Largely achieved (50–85%), F = Fully achieved (85–100%). All processes must achieve **L or F** at PA 2.1 and PA 2.2 for CL2 to be awarded.
>
> **✅ CL2 Verdict: ACHIEVED (post-v1.6.0 `develop` baseline, CSC-AUD-009).** 3 F (SYS.3, SUP.9, SUP.10), 14 L, 0 P/N. The downgrade from 17 F (CSC-AUD-008, v1.5.1) is due to 28 findings, mainly the 8 rules from #391/#392 not being reflected in any work product. All findings were corrected under #405 on 2026-09-29 (see CSC-AUD-009 §6.2). The ratings above are the audit ratings and are re-assessed at the next release audit.
>
> **Previous verdicts:** CSC-AUD-008 (2026-06-28, v1.5.1): 17 F. The v1.6.0 release (2026-07-06) was not assessed by a standalone audit record. The "v1.6.0 ASPICE audit" in revisions 1.21/1.22 refers to the issue-driven document updates for #371–#379 (AUD9-F-021).
>
> **Ratings assigned by internal audit CSC-AUD-009, 2026-09-29 (supersedes CSC-AUD-008 2026-06-28 for this table).**
---

## 7. Review & Approval

| Role | Name | Signature / Electronic Approval | Date |
|---|---|---|---|
| Author | Claude | Approved | 2026-09-29 |
| Technical Reviewer | Dermot Murphy | — | *pending* |
| Quality Assurance | Dermot Murphy | — | *pending* |
| Approver | Dermot Murphy | — | *pending* |

> **Note:** This document is under configuration management (SUP.8). Post-approval changes require a change request (SUP.10) and a new document version.
