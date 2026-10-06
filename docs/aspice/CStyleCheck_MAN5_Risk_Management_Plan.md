# Risk Management Plan

*Automotive SPICE® PAM v4.0 | MAN.5 Risk Management*

---

## 1. Document Identification & Control

| Field | Value | Field | Value |
|---|---|---|---|
| **Document ID** | CSC-MAN5-001 | **Version** | 1.19 |
| **Project** | CStyleCheck | **Date** | 2026-10-06 |
| **Status** | Released | **Classification** | Internal |
| **Author** | Claude | **Reviewer** | Dermot Murphy |
| **Approver** | Dermot Murphy | **Related Process** | MAN.5 |

---

## 2. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.19 | 2026-10-06 | Claude | Cross-reference version resync with #447: referenced-document versions set to the current baseline; no technical content change |
| 1.18 | 2026-10-06 | Claude | Cross-reference version resync after the v1.6.1 hotfix back-merge (#444): referenced-document versions set to the current baseline; no technical content change |
| 1.17 | 2026-09-30 | Claude | Cross-reference version resync (#437): referenced-document versions set to the current baseline after the merge-time process-control changes; no technical content change |
| 1.16 | 2026-09-30 | Claude | Cross-reference version resync (#435): all referenced-document versions set to the current baseline (every controlled work product bumped once in this change set); no technical content change |
| 1.15 | 2026-09-29 | Claude | CSC-AUD-010 corrective actions (#430). AUD10-F-012: new RISK-009 (user-visible behaviour change on upgrade); one review frequency per risk (RISK-005 quarterly in §5, §6 note and §7; RISK-004 review recorded 2026-09-29); RR-003-005 owner confirmation of RISK-003/005 remains pending, tracked in #430. AUD10-F-021: CSC-AUD-009 residuals RR-003-004/005 tracking recorded in §6. AUD10-F-031: risk Status fields set to Active/Accepted to match §6; approval-by-merge policy (CSC-DEV-002 §5.2); RR-003-004/005 closed |
| 1.14 | 2026-09-29 | Claude | Cross-reference resync with #423: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.13 | 2026-09-29 | Claude | Cross-reference resync with #425: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.12 | 2026-09-29 | Claude | Cross-reference resync with #424: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.11 | 2026-09-29 | Claude | Cross-reference resync with #422: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.10 | 2026-09-29 | Claude | Cross-reference resync with #420: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.9 | 2026-09-29 | Claude | Cross-reference resync with #418: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.8 | 2026-09-29 | Claude | Release-prep cross-reference resync: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.7 | 2026-09-29 | Claude | Release-prep cross-reference resync: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.6 | 2026-09-29 | Claude | Issue #407: cross-reference update only; referenced-document versions resynced (MAN3 1.8→1.9, SUP10 1.3→1.4, SUP8 1.13→1.14) |
| 1.5 | 2026-09-29 | Claude | CSC-AUD-009 corrective actions (#405). AUD9-F-019: record the overdue RISK-003 and RISK-005 reviews (2026-09-29) and set the next review to 2026-12-29; RISK-003 treatment records Dependabot `target-branch: develop`, hotfix #399 / back-merge #403 and the Actions updates #400 to #402 and #404. AUD9-F-014: referenced-document versions resynced to current revisions |
| 1.4 | 2026-06-26 | Claude | Implement RISK-003 and RISK-005 treatments: add `.github/dependabot.yml` (Dependabot for PyPI and GitHub Actions); add `CONTRIBUTING.md` (community onboarding); update §3 scope to v1.4.1 |
| 1.3 | 2026-06-18 | Claude | ASPICE audit #254 — sync referenced-document version citations to current versions |
| 1.2 | 2026-05-28 | Dermot Murphy | RISK-003: add Dependabot; update owner and review date. RISK-005: add CONTRIBUTING.md and AI-reproducibility mitigations; update owner and review date — closes issue #155 |
| 1.1 | 2026-05-28 | Claude | Reviewed and updated for v1.1.0 release; revision history maintained per ASPICE GP 2.2.4 |
| 1.0 | 2026-04-12 | Claude | Initial release |

---

## 3. Purpose & Scope

This Risk Management Plan defines the risk identification, analysis, treatment, and monitoring approach for **CStyleCheck v1.4.1**. It satisfies **Automotive SPICE® PAM v4.0, MAN.5 — Risk Management**.

### 3.1 Referenced Documents

| Document ID | Title | Version |
|---|---|---|
| CSC-MAN3-001 | Project Management Plan | 1.23 |
| CSC-SUP8-001 | Configuration Management Plan | 1.27 |
| CSC-SUP10-001 | Change Request Management Plan | 1.19 |

---

## 4. Risk Management Strategy

### 4.1 Risk Scoring

**Likelihood:**

| Score | Label | Description |
|---|---|---|
| 1 | Rare | < 10% probability in project lifetime |
| 2 | Unlikely | 10–30% probability |
| 3 | Possible | 30–60% probability |
| 4 | Likely | 60–85% probability |
| 5 | Almost Certain | > 85% probability |

**Impact:**

| Score | Label | Description |
|---|---|---|
| 1 | Negligible | No effect on schedule, quality, or users |
| 2 | Minor | < 1 week delay; minor quality reduction |
| 3 | Moderate | 1–4 week delay; notable quality reduction |
| 4 | Major | >1 month delay or significant user impact |
| 5 | Critical | Project failure or safety/compliance breach |

**Risk Priority Number (RPN):** `Likelihood × Impact`

| RPN Range | Rating | Action Required |
|---|---|---|
| 1–4 | Low | Monitor; no immediate action |
| 5–9 | Medium | Treatment plan required |
| 10–16 | High | Immediate treatment; escalate |
| 17–25 | Critical | Stop work; escalate immediately |

### 4.2 Risk Treatment Options

| Option | Description |
|---|---|
| **Avoid** | Eliminate the source of risk |
| **Mitigate** | Reduce likelihood or impact |
| **Transfer** | Assign risk to another party |
| **Accept** | Accept risk with monitoring |

---

## 5. Risk Register

### RISK-001 — Regex False Positives / False Negatives

| Field | Value |
|---|---|
| **Risk ID** | RISK-001 |
| **Source** | Technical — regex-based parsing without full C parser |
| **Undesirable Event** | Linter incorrectly flags valid code (false positive) or misses violations (false negative) |
| **Likelihood** | 3 (Possible) |
| **Impact** | 3 (Moderate) — user trust erosion; adoption blocked |
| **RPN** | 9 (Medium) |
| **Treatment Option** | Mitigate |
| **Treatment Activities** | Comprehensive test suite (500+ tests); `test_improvements.py` regression suite for each bug fixed; `rules.yml` self-hosting verification; baseline suppression feature for legacy adoption |
| **Residual Likelihood** | 2 |
| **Residual Impact** | 2 |
| **Residual RPN** | 4 (Low) |
| **Owner** | Claude |
| **Review Date** | Per release |
| **Status** | Active |

---

### RISK-002 — Python Version Incompatibility

| Field | Value |
|---|---|
| **Risk ID** | RISK-002 |
| **Source** | Technical — language version differences |
| **Undesirable Event** | Tool fails on a supported Python version (3.10, 3.11, or 3.12) due to syntax or stdlib changes |
| **Likelihood** | 2 (Unlikely) |
| **Impact** | 3 (Moderate) — users on affected version blocked |
| **RPN** | 6 (Medium) |
| **Treatment Option** | Mitigate |
| **Treatment Activities** | `cstylecheck_tests.yml` matrix tests all three versions on every commit; `pyproject.toml` specifies `requires-python = ">=3.10"` |
| **Residual Likelihood** | 1 |
| **Residual Impact** | 2 |
| **Residual RPN** | 2 (Low) |
| **Owner** | Claude |
| **Review Date** | Per Python minor release |
| **Status** | Active |

---

### RISK-003 — PyYAML Security Vulnerability

| Field | Value |
|---|---|
| **Risk ID** | RISK-003 |
| **Source** | External dependency — PyYAML |
| **Undesirable Event** | A CVE is published against PyYAML affecting the `6.x` range; users exposed via `pip install` |
| **Likelihood** | 2 (Unlikely) |
| **Impact** | 3 (Moderate) — security advisory required; patched release needed |
| **RPN** | 6 (Medium) |
| **Treatment Option** | Mitigate |
| **Treatment Activities** | Pin `pyyaml>=6.0,<7.0` in `pyproject.toml` (already in place); use `yaml.safe_load()` (never `yaml.load()`); enable GitHub Dependabot for `pyproject.toml` to receive automated CVE alerts; monitor PyPI security advisories; **Implemented (2026-06-26):** `.github/dependabot.yml` committed — weekly automated scan for PyPI (`pyproject.toml`) and GitHub Actions dependencies; alerts delivered as automated PRs. **Update (2026-09-29, #399/#403):** `target-branch: develop` added for both ecosystems so Dependabot PRs follow Gitflow (CSC-SUP8-001 §7.5). Before this change, Dependabot PRs opened against `main`; the configuration was corrected by hotfix #399 on `main` and back-merged by #403. Dependabot has since delivered the GitHub Actions updates `actions/checkout@v7`, `actions/setup-python@v7`, `actions/upload-artifact@v7` and `docker/login-action@v4.6.0` (#400–#402, #404); supplier record in CSC-ACQ4-001 §5.2 |
| **Residual Likelihood** | 2 |
| **Residual Impact** | 2 |
| **Residual RPN** | 4 (Low) |
| **Owner** | Dermot Murphy |
| **Review Date** | 2026-12-29 (next quarterly review). Reviewed 2026-09-29 during CSC-AUD-009 (#405): no Dependabot PR or alert for PyYAML in the repository history; Dependabot active on `develop`; ratings unchanged. Owner confirmation given by the owner's merge of PR #431 (approval-by-merge policy of 2026-09-29, CSC-DEV-002 §5.2; CSC-AUD-009 residual RR-003-005 closed) |
| **Status** | Active |

---

### RISK-004 — GitHub Platform Dependency

| Field | Value |
|---|---|
| **Risk ID** | RISK-004 |
| **Source** | External — GitHub hosted infrastructure |
| **Undesirable Event** | GitHub Actions, GHCR, or GitHub Releases become unavailable or change pricing/API, breaking CI/CD pipeline |
| **Likelihood** | 1 (Rare) |
| **Impact** | 4 (Major) — CI, Docker builds, and release process disrupted |
| **RPN** | 4 (Low) |
| **Treatment Option** | Accept + Mitigate |
| **Treatment Activities** | Distributed Git (every developer clone is a source backup); Docker Hub as secondary registry; `docker_publish.yml` pushes to both registries simultaneously |
| **Residual Likelihood** | 1 |
| **Residual Impact** | 3 |
| **Residual RPN** | 3 (Low) |
| **Owner** | Claude |
| **Review Date** | Quarterly — next 2026-12-29. Last reviewed 2026-09-29 (CSC-AUD-010, #430): GitHub Actions CI, GHCR and Docker Hub publication operating; no GitHub pricing or API change affecting the project; ratings unchanged |
| **Status** | Accepted |

---

### RISK-005 — Single Developer Resource Risk

| Field | Value |
|---|---|
| **Risk ID** | RISK-005 |
| **Source** | Resource — sole developer project |
| **Undesirable Event** | Developer unavailability delays release, bug fixing, or ASPICE assessment response |
| **Likelihood** | 2 (Unlikely) |
| **Impact** | 4 (Major) — schedule slip; open Issues unaddressed |
| **RPN** | 8 (Medium) |
| **Treatment Option** | Mitigate |
| **Treatment Activities** | Maintain detailed ASPICE documentation set as living knowledge base; all logic AI-assisted (reproducible from prompts and ASPICE docs); publish `CONTRIBUTING.md` to enable community onboarding; MIT licence enables community contributions; all work tracked via GitHub Issues for continuity; **Implemented (2026-06-26):** `CONTRIBUTING.md` committed — covers reporting issues, PR workflow, code style, AI assistance policy, and licence |
| **Residual Likelihood** | 2 |
| **Residual Impact** | 3 |
| **Residual RPN** | 6 (Medium) |
| **Owner** | Dermot Murphy |
| **Review Date** | 2026-12-29 (next quarterly review). Reviewed 2026-09-29 during CSC-AUD-009 (#405): still a single human contributor; mitigations in place; ratings unchanged. Owner confirmation given by the owner's merge of PR #431 (approval-by-merge policy of 2026-09-29, CSC-DEV-002 §5.2; CSC-AUD-009 residual RR-003-005 closed) |
| **Status** | Active |

---

### RISK-006 — Barr-C Standard Interpretation Divergence

| Field | Value |
|---|---|
| **Risk ID** | RISK-006 |
| **Source** | Technical — normative standard interpretation |
| **Undesirable Event** | CStyleCheck's interpretation of a Barr-C or MISRA-C rule differs from user expectation, causing adoption friction |
| **Likelihood** | 3 (Possible) |
| **Impact** | 2 (Minor) — user confusion; support burden |
| **RPN** | 6 (Medium) |
| **Treatment Option** | Mitigate |
| **Treatment Activities** | Each rule documented in README with rationale and Barr-C section reference; all rules configurable (enable/disable/severity); `exclusions.yml` allows per-file suppression |
| **Residual Likelihood** | 2 |
| **Residual Impact** | 1 |
| **Residual RPN** | 2 (Low) |
| **Owner** | Claude |
| **Review Date** | Per major release |
| **Status** | Active |

---

### RISK-007 — ASPICE Assessment Non-Compliance

| Field | Value |
|---|---|
| **Risk ID** | RISK-007 |
| **Source** | Process — ASPICE CL2 documentation gaps |
| **Undesirable Event** | ASPICE assessor identifies missing or insufficient work products, resulting in CL2 not achieved |
| **Likelihood** | 2 (Unlikely) |
| **Impact** | 4 (Major) — CL2 not achieved; re-assessment required |
| **RPN** | 8 (Medium) |
| **Treatment Option** | Mitigate |
| **Treatment Activities** | Full CL2 documentation set produced (SYS.2–5, SWE.1–6, MAN.3, MAN.5, SUP.1, SUP.8–10, ACQ.4, PA 2.1, PA 2.2); internal pre-assessment using ASPICE compliance matrices in each document; bidirectional traceability maintained |
| **Residual Likelihood** | 1 |
| **Residual Impact** | 3 |
| **Residual RPN** | 3 (Low) |
| **Owner** | Claude |
| **Review Date** | Pre-assessment |
| **Status** | Active |

---

### RISK-008 — Docker Image Supply Chain Attack

| Field | Value |
|---|---|
| **Risk ID** | RISK-008 |
| **Source** | Security — container supply chain |
| **Undesirable Event** | Base Python image or dependencies compromised; malicious image published to GHCR |
| **Likelihood** | 1 (Rare) |
| **Impact** | 4 (Major) — users of Docker image impacted |
| **RPN** | 4 (Low) |
| **Treatment Option** | Mitigate |
| **Treatment Activities** | Pin base image to specific Python version (`ARG PYTHON_VERSION=3.12`); use official `python:slim` images; image digest recorded in Actions log per build; dual-registry publication makes single-registry compromise detectable |
| **Residual Likelihood** | 1 |
| **Residual Impact** | 3 |
| **Residual RPN** | 3 (Low) |
| **Owner** | Claude |
| **Review Date** | Per Docker build |
| **Status** | Active |

---

### RISK-009 — User-Visible Behaviour Change on Upgrade

| Field | Value |
|---|---|
| **Risk ID** | RISK-009 |
| **Source** | Technical / change management — changes to defaults, config validation, exit codes and generated configs |
| **Undesirable Event** | A user upgrades and the tool behaves differently without warning: a config that loaded before is rejected (#422), new findings appear (#423 last enum member checked), a CI script's exit-code check changes (#425, 1→2), or a regenerated preset / `--init` config enables more rules (#420) |
| **Likelihood** | 3 (Possible) |
| **Impact** | 3 (Moderate) — CI pipelines fail or change result on upgrade; user trust erosion |
| **RPN** | 9 (Medium) |
| **Treatment Option** | Mitigate |
| **Treatment Activities** | CHANGELOG ⚠️ notes and a Compatibility section for every user-visible change; SUP10 semantic-versioning policy (CSC-SUP10-001 §5.6) applied — next release classified v2.0.0 (Major), decision in CSC-SUP10-001 §7.2 and CSC-MAN3-001 §8; CR impact analysis per CSC-SUP10-001 §4.2 records backwards-incompatible changes as High impact (CR-412, CR-418, CR-420, CR-422, CR-424, CR-425); new-rule opt-in policy (CR-418) so upgrades add no findings from new rules; deprecated keys warn rather than fail (`functions.case`, CR-424) |
| **Residual Likelihood** | 2 |
| **Residual Impact** | 2 |
| **Residual RPN** | 4 (Low) |
| **Owner** | Dermot Murphy |
| **Review Date** | Per release — before each release tag, confirm the CHANGELOG Compatibility section and the version classification |
| **Status** | Active |

---

## 6. Risk Summary

| Risk ID | Title | RPN (Initial) | RPN (Residual) | Rating | Status |
|---|---|---|---|---|---|
| RISK-001 | Regex false positives/negatives | 9 | 4 | Low | Active |
| RISK-002 | Python version incompatibility | 6 | 2 | Low | Active |
| RISK-003 | PyYAML security vulnerability | 6 | 4 | Low | Active |
| RISK-004 | GitHub platform dependency | 4 | 3 | Low | Accepted |
| RISK-005 | Single developer resource | 8 | 6 | Medium | Active |
| RISK-006 | Barr-C interpretation divergence | 6 | 2 | Low | Active |
| RISK-007 | ASPICE assessment non-compliance | 8 | 3 | Low | Active |
| RISK-008 | Docker supply chain attack | 4 | 3 | Low | Active |
| RISK-009 | User-visible behaviour change on upgrade | 9 | 4 | Low | Active |

> **📋 Note:** No risks currently exceed the High threshold (RPN ≥ 10) after treatment. RISK-005 (single developer) remains Medium residual and is reviewed quarterly (next 2026-12-29).

> **Closed residuals (CSC-AUD-009, tracked under #430, CSC-AUD-010 AUD10-F-021):** RR-003-004 closed — post-v1.6.0 CI matrix recorded: GitHub Actions run 36612676061 on commit `6bdc592` (PR #431), Unit Tests Python 3.10, 3.11, 3.12 all success, 2026-09-29. RR-003-005 closed — Risk Owner confirmation of the RISK-003 and RISK-005 reviews given by the owner's merge of PR #431 (approval-by-merge policy of 2026-09-29, CSC-DEV-002 §5.2).

---

## 7. Risk Monitoring Schedule

| Activity | Frequency | Owner |
|---|---|---|
| Review open GitHub Issues for new risk indicators | Weekly | Claude |
| Check PyYAML CVE advisories | Monthly | Claude |
| Update risk register residual scores | Per milestone | Claude |
| Review RISK-005 (resource) | Quarterly | Dermot Murphy |
| Pre-assessment risk review | Before ASPICE assessment | Claude |

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
