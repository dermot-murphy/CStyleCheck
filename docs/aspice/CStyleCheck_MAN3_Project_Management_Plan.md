# Project Management Plan

*Automotive SPICE® PAM v4.0 | MAN.3 Project Management*

---

## 1. Document Identification & Control

| Field | Value | Field | Value |
|---|---|---|---|
| **Document ID** | CSC-MAN3-001 | **Version** | 1.22 |
| **Project** | CStyleCheck | **Date** | 2026-10-06 |
| **Status** | Released | **Classification** | Internal |
| **Author** | Claude | **Reviewer** | Dermot Murphy |
| **Approver** | Dermot Murphy | **Related Process** | MAN.3 |

---

## 2. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.22 | 2026-10-06 | Claude | Cross-reference version resync after the v1.6.1 hotfix back-merge (#444): referenced-document versions set to the current baseline; no technical content change |
| 1.21 | 2026-09-30 | Claude | Merge-time process controls (#437): §4.1 scope lists 6 CI workflows (adds `aspice_consistency.yml`); §10.1 work-product consistency monitoring row; §10.2 corrective action for a consistency-check failure; referenced-document versions resynced |
| 1.20 | 2026-09-30 | Claude | Cross-reference version resync (#435): all referenced-document versions set to the current baseline (every controlled work product bumped once in this change set); no technical content change |
| 1.19 | 2026-09-29 | Claude | CSC-AUD-010 corrective actions (#430). AUD10-F-002: §8 release-classification decision — next release v2.0.0 (Major) replaces the planned v1.7.0, with the compatibility changes in scope listed. AUD10-F-016: §4.3 lifecycle text refreshed (package architecture, 12 modules; post-v1.6.0 development toward v2.0.0); PH-04 names the `src/cstylecheck/` package; WBS-16/WBS-17 overlap removed; approval-by-merge policy (CSC-DEV-002 §5.2) |
| 1.18 | 2026-09-29 | Claude | #423: test total 1532→1545 (last enum member tests); referenced-document versions resynced (5) |
| 1.17 | 2026-09-29 | Claude | #425: test total 1524→1532, 57→58 test modules (config-error exit-code tests for both entry points); referenced-document versions resynced (5) |
| 1.16 | 2026-09-29 | Claude | #424: test total 1508→1524, 56→57 test modules (`functions.case` removal tests); referenced-document versions resynced (5) |
| 1.15 | 2026-09-29 | Claude | #422: test total 1481→1508, 55→56 test modules (case-style config validation tests); referenced-document versions resynced (5) |
| 1.14 | 2026-09-29 | Claude | #420: test total 1463→1481; referenced-document versions resynced (5) |
| 1.13 | 2026-09-29 | Claude | #418 (CR-418): test total 1452→1463; referenced-document versions resynced (5) |
| 1.12 | 2026-09-29 | Claude | #412: test total 1444→1452; referenced-document versions resynced (5) |
| 1.11 | 2026-09-29 | Claude | Release-prep cross-reference resync: 5 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.10 | 2026-09-29 | Claude | #413: test total 1439→1444 |
| 1.9 | 2026-09-29 | Claude | Issue #407: §4.1 scope, WBS-07 and WBS-10 → 1439 tests / 55 modules (CSC-SWE4-001 v1.24); referenced-document versions resynced (MAN5 1.5→1.6, SUP1 1.10→1.11, SUP8 1.13→1.14, SWE1 2.8→2.9, SYS2 2.3→2.4) |
| 1.8 | 2026-09-29 | Claude | CSC-AUD-009 corrective actions (#405). AUD9-F-020: §3.1 version 1.2.0→1.6.0; §4.1 scope (12 modules, 81 rules, 1422 tests / 54 modules, 5 workflows, Dependabot); WBS-07/10 to 16 statuses; §8 schedule adds actuals for v1.2.0 to v1.6.0, CSC-AUD-009 and the planned v1.7.0. AUD9-F-011: add §10.3 Trend-Analysis Metrics Monitoring (parent of SWE1-102 to SWE1-108 and SWE1-117) and a §10.1 row; `rules.yml` → `cstylecheck_rules.yml`. AUD9-F-014: referenced-document versions resynced to current revisions |
| 1.7 | 2026-07-06 | Claude | ASPICE audit — update WBS-07 and WBS-10 stale test counts — closes #379 |
| 1.6 | 2026-06-18 | Claude | ASPICE audit #254 — sync referenced-document version citations to current versions |
| 1.5 | 2026-06-04 | Claude | Deep accuracy audit: fix §3 Purpose version text v1.0.0→v1.2.0, update SWE1-001 version in §3.2 (1.3→1.5) — resolves issue #163 |
| 1.4 | 2026-06-04 | Claude | Automated accuracy audit: fix §3.1 version, §4.1 rule count 48→53 and package reference, update test count and module count, update referenced doc versions, update WBS-10 status — resolves issue #163 |
| 1.3 | 2026-05-28 | Dermot Murphy | §6 WBS-10 to WBS-16: update status with concrete facts (839 tests, release dates, blocked items) — closes issue #154 |
| 1.2 | 2026-05-28 | Dermot Murphy | Resolve \<TBD\> milestone dates for v1.0.0; add v1.1.0 milestone row — closes issue #53 |
| 1.1 | 2026-05-28 | Claude | Reviewed and updated for v1.1.0 release; revision history maintained per ASPICE GP 2.2.4 |
| 1.0 | 2026-04-12 | Claude | Initial release |

---

## 3. Purpose & Scope

This Project Management Plan (PMP) defines the project scope, lifecycle, work breakdown, resources, schedule, interfaces, and monitoring approach for **CStyleCheck v1.2.0**. It satisfies **Automotive SPICE® PAM v4.0, MAN.3 — Project Management**.

### 3.1 Project Overview

| Attribute | Value |
|---|---|
| **Product** | CStyleCheck — Embedded C naming-convention linter |
| **Version** | 1.6.0 (released 2026-07-06); `develop` post-v1.6.0 |
| **Repository** | `https://github.com/dermot-murphy/CStyleCheck` |
| **Language** | Python 3.10–3.12 |
| **Deployment** | CLI, pip/pipx, Docker (GHCR + Docker Hub), GitHub Action, pre-commit |
| **Standards** | Barr-C:2018, MISRA-C complementary, Automotive SPICE® PAM v4.0 |
| **Licence** | MIT |

### 3.2 Referenced Documents

| Document ID | Title | Version |
|---|---|---|
| CSC-SYS2-001 | System Requirements Specification | 2.18 |
| CSC-SWE1-001 | Software Requirements Specification | 2.25 |
| CSC-SUP8-001 | Configuration Management Plan | 1.26 |
| CSC-MAN5-001 | Risk Management Plan | 1.18 |
| CSC-SUP1-001 | Quality Assurance Plan | 1.23 |

---

## 4. Project Scope and Objectives

### 4.1 In Scope

- Design, implementation, and testing of `src/cstylecheck/` package (12 sub-modules) implementing 81 rule IDs (73 at v1.6.0; 8 added on `develop` by #391/#392)
- Test suite (1545 pytest tests across 58 test modules on `develop`, 2026-09-29, after #408, #407, #413, #412, #418, #420, #422, #424, #425 and #423; 1279 at v1.6.0)
- Docker image build and multi-platform publication to GHCR and Docker Hub
- GitHub Action integration (`action.yml`)
- pre-commit hook integration (`.pre-commit-hooks.yml`)
- pip/pipx packaging (`pyproject.toml`)
- Full ASPICE CL2 documentation set (SYS.2–SYS.5, SWE.1–SWE.6, MAN.3, MAN.5, SUP.1, SUP.8–SUP.10, ACQ.4, PA 2.1, PA 2.2)
- CI/CD automation via GitHub Actions (6 workflows: `cstylecheck_tests.yml`, `cstylecheck_rules.yml`, `docker_publish.yml`, `wiki_publish.yml`, `metrics.yml`, `aspice_consistency.yml`) and Dependabot dependency updates (`target-branch: develop`)
- Trend-analysis metrics for process monitoring (`scripts/collect_metrics.py` et al., see §10.3)

### 4.2 Out of Scope

- GUI or IDE plugin
- C++ language support beyond C/C++ keyword detection
- Hardware engineering or mechanical engineering processes
- Machine learning engineering processes

### 4.3 Feasibility Assessment

| Constraint | Assessment |
|---|---|
| **Technical** | Python-only implementation; package architecture (`src/cstylecheck/`, 12 modules, plus the `src/cstylecheck.py` wrapper); no exotic dependencies. Technically feasible with one engineer |
| **Schedule** | v1.6.0 released 2026-07-06; current phase is post-v1.6.0 development on `develop` toward v2.0.0 (see §8) |
| **Resources** | Solo developer; GitHub Actions for CI/CD (zero compute cost for public repo) |
| **Standards compliance** | ASPICE CL2 documentation producible; naming convention self-check demonstrable |

---

## 5. Project Lifecycle

CStyleCheck follows a **Git Flow** based lifecycle aligned with the V-model:

```
Requirements  →  Architecture  →  Detailed Design  →  Implementation
    (SYS.2/SWE.1)   (SYS.3/SWE.2)     (SWE.3)            (SWE.3 BP8)
         ↑                                                       ↓
  System Verification  ←  SW Qualification  ←  SW Integration  ←  Unit Verification
      (SYS.5)               (SWE.6)              (SWE.5)           (SWE.4)
```

### 5.1 Project Phases

| Phase ID | Phase Name | Deliverables | Entry Criteria | Exit Criteria |
|---|---|---|---|---|
| PH-01 | Requirements | SYS.2, SWE.1 | Project initiated | Requirements reviewed and approved |
| PH-02 | Architecture | SYS.3, SWE.2 | Requirements approved | Architecture reviewed and approved |
| PH-03 | Detailed Design | SWE.3 | Architecture approved | Design reviewed and approved |
| PH-04 | Implementation | `src/cstylecheck/` package (per release), test suite | Design approved | All unit tests pass (SWE.4) |
| PH-05 | Integration & Verification | SWE.5, SWE.6, SYS.4, SYS.5 | Unit tests pass | All qualification tests pass |
| PH-06 | Release | v1.0.0 tag, GHCR image, GitHub Release | All tests pass; docs approved | Release baseline created (SPL.2) |
| PH-07 | Documentation | Full ASPICE CL2 doc set | Release complete | All documents approved |

---

## 6. Work Breakdown Structure

| WBS-ID | Work Package | Estimated Effort | Responsible | Status |
|---|---|---|---|---|
| WBS-01 | System requirements (SYS.2) | 4h | Claude | Complete |
| WBS-02 | System architecture (SYS.3) | 4h | Claude | Complete |
| WBS-03 | Software requirements (SWE.1) | 8h | Claude | Complete |
| WBS-04 | Software architecture (SWE.2) | 6h | Claude | Complete |
| WBS-05 | Detailed design (SWE.3) | 8h | Claude | Complete |
| WBS-06 | Core linter implementation | 80h | Claude | Complete |
| WBS-07 | Test suite (1545 tests on `develop`) | 40h | Claude | Complete (ongoing per feature) |
| WBS-08 | Docker packaging and CI | 8h | Claude | Complete |
| WBS-09 | GitHub Action and pre-commit | 6h | Claude | Complete |
| WBS-10 | Unit verification (SWE.4) | 4h | Claude | Complete — 1545 tests across 58 modules; SWE4 catalogue updated (CSC-SWE4-001 v1.24, #405, #408, #407) |
| WBS-11 | Integration testing (SWE.5) | 4h | Claude | Complete — #152 closed 2026-05-28; SIT-001 to SIT-027 recorded |
| WBS-12 | Qualification testing (SWE.6) | 4h | Claude | Complete — SWQ-001 to SWQ-012 recorded (v1.6.0); post-v1.6.0 extensions recorded 2026-09-29 |
| WBS-13 | System integration testing (SYS.4) | 4h | Claude | Complete — SITC-001 to SITC-017 recorded |
| WBS-14 | System verification (SYS.5) | 4h | Claude | Complete — SYS-VTC-001 to SYS-VTC-013 recorded |
| WBS-15 | Documentation finalisation | 4h | Claude | Ongoing per release — CSC-AUD-009 corrective actions (#405) applied 2026-09-29 |
| WBS-16 | Release (tag, GitHub Release, container images) — per release | 2h | Claude | Releases v1.0.0 to v1.6.0 complete (see §8); next release v2.0.0 (Major) planned |
| WBS-17 | *Merged into WBS-16 (was: v1.0.0 release, complete 2026-04-12)* | — | — | Withdrawn 2026-09-29 (CSC-AUD-010 AUD10-F-016) |

---

## 7. Resource Plan

| Resource | Type | Allocation |
|---|---|---|
| Claude | Engineer (sole developer) | 100% |
| GitHub Actions | CI/CD infrastructure | On-demand; zero cost (public repo) |
| GHCR | Container registry | Free tier |
| Docker Hub | Container registry | Free tier |
| GitHub Issues | Change/problem tracking | Included in GitHub |
| `pytest` / `pytest-cov` | Test tooling | Open source |

---

## 8. Project Schedule

| Milestone | Target Date | Status | Actual Date |
|---|---|---|---|
| Core linter v1.0.0 implementation complete | 2026-04-11 | ✅ Complete | 2026-04-11 |
| Test suite ≥500 tests all passing | 2026-04-11 | ✅ Complete | 2026-04-11 |
| Docker image published to GHCR | 2026-04-11 | ✅ Complete | 2026-04-11 |
| SYS.2–SYS.5 documentation complete | 2026-04-12 | ✅ Complete | 2026-04-12 |
| SWE.1–SWE.6 documentation complete | 2026-04-12 | ✅ Complete | 2026-04-12 |
| Remaining ASPICE CL2 documents complete | 2026-04-12 | ✅ Complete | 2026-04-15 |
| All documents reviewed and approved (v1.0.0) | 2026-04-15 | ✅ Complete | 2026-04-15 |
| v1.0.0 release baseline created | 2026-04-15 | ✅ Complete | 2026-04-15 |
| All documents reviewed and approved (v1.1.0) | 2026-05-28 | ✅ Complete | 2026-05-28 |
| v1.1.0 release baseline created | 2026-06-30 | ✅ Complete | 2026-05-28 |
| v1.2.0 / v1.2.1 release baselines | 2026-05-29 | ✅ Complete | 2026-05-29 |
| v1.3.0 release baseline | 2026-06-05 | ✅ Complete | 2026-06-05 |
| v1.4.0 / v1.4.1 release baselines (CSC-AUD-007) | 2026-06-18 | ✅ Complete | 2026-06-18 |
| v1.5.0 release baseline | 2026-06-26 | ✅ Complete | 2026-06-26 |
| v1.5.1 release baseline (CSC-AUD-008) | 2026-06-28 | ✅ Complete | 2026-06-28 |
| v1.6.0 release baseline | 2026-07-06 | ✅ Complete | 2026-07-06 |
| Internal audit CSC-AUD-009 and corrective actions (#405) | 2026-09-29 | ✅ Complete | 2026-09-29 |
| v2.0.0 release (Major) — 8 opt-in MISRA/Barr-C rules, baseline matching, trend metrics; compatibility changes: config with unknown case-style names rejected (#422), config/usage-error exit code 1→2 for the installed command (#425), last enum member now checked (#423), presets/`--init` enable opt-in rules (#420), `functions.case` removed with WARNING (#424); release audit and CSC-REVIEW record | 2026-Q4 | ⏳ Planned | — |

**Release-classification decision (2026-09-29, Dermot Murphy):** the next release is **v2.0.0 (Major)**, not v1.7.0. Rationale: CSC-SUP10-001 §5.6 requires a Major version for changed default behaviour or an incompatible config format; CR-422 rejects configs that v1.6.0 loaded and CR-425 changes the config-error exit code of the installed command from 1 to 2. Recorded in CSC-SUP10-001 §7.2 (CSC-AUD-010 AUD10-F-002, #430).

---

## 9. Project Interfaces

| Interface | Counterpart | Type | Communication Method | Frequency |
|---|---|---|---|---|
| INT-01 | End users (embedded C developers) | External | GitHub README, GitHub Releases, Docker Hub | On release |
| INT-02 | CI/CD system (GitHub Actions) | Internal tool | `push` / `pull_request` event triggers | Per commit/PR |
| INT-03 | Container registries (GHCR, Docker Hub) | External service | Automated push via `docker_publish.yml` | On release tag |
| INT-04 | pre-commit framework | External tool | `.pre-commit-hooks.yml` | On user install |
| INT-05 | GitHub Marketplace | External platform | `action.yml` + release tag | On publish |
| INT-06 | Assessor / auditor | External | ASPICE documentation set | On assessment |

---

## 10. Progress Monitoring and Reporting

### 10.1 Monitoring Approach

| Activity | Method | Frequency |
|---|---|---|
| Build and test status | GitHub Actions CI badge on README | Continuous (per commit) |
| Test pass rate | `cstylecheck_tests.yml` — pytest result matrix | Per commit to `develop`/`main` |
| Naming convention compliance | `cstylecheck_rules.yml` CI job | Per commit touching C sources |
| Code coverage | `pytest-cov` — `coverage.xml` artefact | Per CI run on Python 3.11 |
| Open Issues (bugs/changes) | GitHub Issues board | Reviewed weekly |
| WBS progress | Manual update to this document | Per milestone |
| Risk status | Risk register (CSC-MAN5-001) | Monthly or on new risk identified |
| Code-quality trends | Trend-analysis metrics (§10.3) | Per PR merge to `main` / `develop` |
| Work-product consistency | `aspice_consistency.yml` — `python scripts/aspice_check.py` (CSC-SUP1-001 GATE-04, #437) | Every PR; push to `develop` / `main` |

### 10.2 Corrective Action Triggers

| Trigger | Action |
|---|---|
| CI test failure on `develop` or `main` | Raise GitHub Issue; fix on `bugfix/` branch before next merge |
| Coverage drop below target threshold | Raise Issue; add missing tests before next release |
| Naming convention CI failure on own source | Raise Issue; fix in same commit; never merge failing source |
| ASPICE consistency check failure on a PR | Fix the work products in the same PR (`python scripts/aspice_check.py --fix-citations` for citations) before merge |
| Milestone slipped by >1 week | Update schedule; assess risk impact; update CSC-MAN5-001 |
| New risk identified | Add to risk register (CSC-MAN5-001); assign treatment |

### 10.3 Trend-Analysis Metrics Monitoring

The project monitors code-quality trends as a GP 2.1.4 (monitor process performance) activity. `.github/workflows/metrics.yml` runs `scripts/collect_metrics.py` after each merge to `main` and `develop` and on pull requests. It collects violation counts, file statistics, LOC composition, cyclomatic complexity, function size, doxygen coverage, coupling, safety indicators and violation quality for `examples/`. `scripts/generate_charts.py` renders SVG trend charts, `scripts/update_wiki_metrics.py` publishes the Trend-Analysis wiki page, and `scripts/compare_metrics.py` attaches a comparison report to each PR. Thresholds (function > 60 lines, > 5 parameters, V(G) > 10) are defined in `scripts/collect_metrics.py` and documented in `scripts/metrics_rules.yml`.

| Metric trend | Review trigger |
|---|---|
| Violations or defect density rising on `develop` for 3 consecutive merges | Raise a GitHub Issue; assess in weekly review |
| `cc_over_threshold`, `func_over_length` or `func_over_params` > 0 on `develop` | Raise a GitHub Issue to refactor the example sources |
| Safety indicators (`goto_count`, `void_ptr_count`, `cast_count`) increasing | Review the change for the MISRA/Barr-C rule concerned |

These tooling requirements are specified in CSC-SWE1-001 §4.17 (SWE1-102 to SWE1-108, SWE1-117) and have no SYS.2 parent. This section is their planning source.

---

## 11. Review & Approval

| Role | Name | Signature / Electronic Approval | Date |
|---|---|---|---|
| Author | Claude | Approved | 2026-09-29 |
| Technical Reviewer | Dermot Murphy | By merge (CSC-DEV-002 §5.2) | On PR merge |
| Quality Assurance | Dermot Murphy | By merge (CSC-DEV-002 §5.2) | On PR merge |
| Approver | Dermot Murphy | By merge (CSC-DEV-002 §5.2) | On PR merge |

> Approval is given by the owner's merge of the pull request that introduces this revision; the merge commit is the approval record (CSC-DEV-002 §5.2).

> **Note:** This document is under configuration management (SUP.8). Post-approval changes require a change request (SUP.10) and a new document version.
