# Configuration Management Plan

*Automotive SPICE® PAM v4.0 | SUP.8 Configuration Management*

---

## 1. Document Identification & Control

| Field | Value | Field | Value |
|---|---|---|---|
| **Document ID** | CSC-SUP8-001 | **Version** | 1.23 |
| **Project** | CStyleCheck | **Date** | 2026-09-29 |
| **Status** | Released | **Classification** | Internal |
| **Author** | Claude | **Reviewer** | Dermot Murphy |
| **Approver** | Dermot Murphy | **Related Process** | SUP.8 |

---

## 2. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.23 | 2026-09-29 | Claude | CSC-AUD-010 corrective actions (#430). AUD10-F-015: §7.1–7.3 aligned with §7.6 (CI-only hotfixes merge to `main` untagged) and allow `claude/<topic>-<id>` branches for feature and bug-fix work into `develop`; §9 approval step matches CSC-DEV-002 §5.2 (owner's merge is the approval record). AUD10-F-029: `logo/cstylecheck.jpg` added to CI-026 and `docs/templates/ASPICE_CL2_Test_Case_Template_1.md` to CI-055 (CI count unchanged at 60). AUD10-F-032: §9 note — cross-reference resyncs batched into one revision per document per change set; approval-by-merge policy (CSC-DEV-002 §5.2) |
| 1.22 | 2026-09-29 | Claude | Cross-reference resync with #423: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.21 | 2026-09-29 | Claude | Cross-reference resync with #425: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.20 | 2026-09-29 | Claude | Cross-reference resync with #424: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.19 | 2026-09-29 | Claude | Cross-reference resync with #422: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.18 | 2026-09-29 | Claude | Cross-reference resync with #420: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.17 | 2026-09-29 | Claude | Cross-reference resync with #418: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.16 | 2026-09-29 | Claude | Release-prep cross-reference resync: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.15 | 2026-09-29 | Claude | Release-prep cross-reference resync: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.14 | 2026-09-29 | Claude | Issue #407: cross-reference update only; referenced-document versions resynced (SUP10 1.3→1.4, SUP9 1.3→1.4, SWE1 2.8→2.9) |
| 1.13 | 2026-09-29 | Claude | CSC-AUD-009 corrective actions (#405). AUD9-F-009: add CI-045 to CI-060 (checker package `src/cstylecheck/*.py`, `.github/dependabot.yml`, CHANGELOG, CONTRIBUTING, Rules-and-Configuration, `src/project.defines`, `scripts/build.bat`/`test.bat`, `tests/__init__.py`, LICENSE, ASPICE WPs, audit records, repository configuration, CLAUDE.md, examples, draft standards); fix the CI-027 path; clarify CI-001/CI-002/CI-044. AUD9-F-019: §7.5 Dependabot target-branch rule. AUD9-F-028: add §7.6 hotfix versioning/tagging policy and record hotfix #399. AUD9-F-015: header date. AUD9-F-024: Author and Description columns swapped back in the v1.9 row. AUD9-F-014: referenced-document versions resynced to current revisions |
| 1.12 | 2026-09-29 | Claude | Add trend-analysis metrics workflow, scripts, threshold config and unit tests to CI list (CI-038 to CI-044) — issue #388 |
| 1.11 | 2026-07-06 | Claude | ASPICE audit — add prerelease_check.sh, check_my_project.bat, DOCKERHUB_README.md to CI list — closes #379 |
| 1.10 | 2026-07-01 | Claude | v1.6.0 release — update §3.1 scope to v1.6.0; update §3.3 SWE1 ref 2.4→2.5 |
| 1.9 | 2026-06-27 | Dermot Murphy | Fix §3.3 cross-ref: SWE1 2.2→2.4 (+ any other stale refs fixed) |
| 1.8 | 2026-06-27 | Claude | ASPICE audit — §3.1 scope v1.2.0→v1.5.0; §3.3 SWE1 ref 1.9→2.2; update Review & Approval dates — closes #321 #323 |
| 1.7 | 2026-06-18 | Claude | ASPICE audit #254 — sync referenced-document version citations to current versions |
| 1.6 | 2026-06-04 | Claude | Deep accuracy audit: fix CI-024 workflow filename (rules.yml→cstylecheck_rules.yml), fix §7.5 reference, update SWE1-001 version in §3.3 — resolves issue #163 |
| 1.5 | 2026-06-04 | Claude | Automated accuracy audit: fix §3.1 version text v1.0.0→v1.2.0, update referenced doc versions — resolves issue #163 |
| 1.4 | 2026-05-28 | Dermot Murphy | Add CI-034 (wiki_publish.yml) to CI inventory — closes issue #150 |
| 1.3 | 2026-05-28 | Dermot Murphy | Add CI-032 (CSC-DEV-002 independent review deviation) and CI-033 (CSC-SVD-001) to CI list — issue #61 |
| 1.2 | 2026-05-28 | Dermot Murphy | Add CI-028 (CSC-DEV-001 deviation document) to CI list — issue #52 |
| 1.1 | 2026-04-12 | Claude | Updated branching strategy to Git Flow; clarified PR/Issue terminology throughout |
| 1.0 | 2026-04-11 | Claude | Initial release |

---

## 3. Purpose & Scope

### 3.1 Purpose

This Configuration Management (CM) Plan defines the processes, tools, methods, and responsibilities used to identify, control, store, and audit all configuration items (CIs) produced during the development and maintenance of **CStyleCheck v1.6.0** — an embedded C naming-convention linter implementing Barr-C:2018 and MISRA-C complementary rules.

This plan satisfies the requirements of **Automotive SPICE® PAM v4.0, SUP.8 — Configuration Management**.

### 3.2 Scope

This plan applies to all configuration items produced by the CStyleCheck project, including:

- Source code and supporting scripts
- Test suite and test data
- Configuration and rule definition files
- CI/CD workflow definitions
- Packaging and container artefacts
- Project documentation (including this plan)

### 3.3 Referenced Documents

| Document ID | Title | Version |
|---|---|---|
| ASPICE PAM v4.0 | Automotive SPICE Process Assessment Model | 4.0 |
| CSC-SUP9-001 | CStyleCheck Problem Resolution Management Plan | 1.12 |
| CSC-SUP10-001 | CStyleCheck Change Request Management Plan | 1.13 |
| CSC-SWE1-001 | CStyleCheck Software Requirements Specification | 2.19 |

---

## 4. Configuration Management Objectives

The CM process for CStyleCheck shall ensure that:

1. All configuration items are uniquely identified and versioned
2. Changes to CIs are controlled, reviewed, and traceable
3. Baselines are established at defined project milestones
4. The integrity of the software and its artefacts is maintained at all times
5. All releases are reproducible from a known, auditable baseline
6. Problem reports and change requests are linked to affected CIs

---

## 5. Configuration Management Tool & Repository

### 5.1 Version Control System

| Attribute | Value |
|---|---|
| **Tool** | Git |
| **Hosting Platform** | GitHub |
| **Repository URL** | `https://github.com/dermot-murphy/CStyleCheck` |
| **Visibility** | Public |
| **Default Branch** | `main` |
| **Access Control** | GitHub repository permissions (Owner: Claude) |

### 5.2 Container Registry

| Attribute | Value |
|---|---|
| **Registry** | GitHub Container Registry (GHCR) |
| **Image Path** | `ghcr.io/<org>/cstylecheck` |
| **Secondary Registry** | Docker Hub |
| **Image Build** | Automated via `docker_publish.yml` on push to `main` or version tag |

### 5.3 Artefact Storage

| Artefact Type | Storage Location |
|---|---|
| Source code | GitHub repository (`main` branch + tags) |
| Docker images | GHCR + Docker Hub |
| Test coverage reports | GitHub Actions artefacts (retention: 30 days) |
| Release packages | GitHub Releases (pip-installable `.whl` / `.tar.gz`) |

---

## 6. Configuration Item Identification

### 6.1 Configuration Item List

All items in the following table are placed under configuration control.

| CI ID | Item | Path in Repository | Type |
|---|---|---|---|
| CI-001 | CLI entry-point shim (backward-compatible) | `src/cstylecheck.py` | Source code |
| CI-002 | Version file (generated at build time from `git describe`; git-ignored, not stored in the repository) | `src/_version.py` | Generated / version |
| CI-003 | Production naming convention config | `src/rules.yml` | Configuration |
| CI-004 | CLI options defaults file | `src/options.txt` | Configuration |
| CI-005 | Exclusions configuration | `src/exclusions.yml` | Configuration |
| CI-006 | Project preprocessor defines | `src/defines.txt` | Configuration |
| CI-007 | Module alias map | `src/aliases.txt` | Configuration |
| CI-008 | C keyword dictionary | `src/c_keywords.txt` | Data file |
| CI-009 | C stdlib name dictionary | `src/c_stdlib_names.txt` | Data file |
| CI-010 | Spell-check dictionary | `src/c_spell_dict.txt` | Data file |
| CI-011 | Dockerfile | `Dockerfile/Dockerfile` | Build / container |
| CI-012 | Docker ignore file | `Dockerfile/.dockerignore` | Build / container |
| CI-013 | Package metadata | `pyproject.toml` | Build / packaging |
| CI-014 | pip dependencies | `requirements.txt` | Build / packaging |
| CI-015 | pre-commit hook definition | `.pre-commit-hooks.yml` | Integration |
| CI-016 | GitHub Action definition | `action.yml` | Integration |
| CI-017 | Test suite (all test files) | `tests/test_*.py` | Test |
| CI-018 | Test naming convention config | `tests/rules.yml` | Test configuration |
| CI-019 | Test harness | `tests/harness.py` | Test |
| CI-020 | Test keyword dictionary | `tests/c_keywords.txt` | Test data |
| CI-021 | Test stdlib dictionary | `tests/c_stdlib_names.txt` | Test data |
| CI-022 | Test spell dictionary | `tests/c_spell_dict.txt` | Test data |
| CI-023 | CI — test workflow | `.github/workflows/cstylecheck_tests.yml` | CI/CD |
| CI-024 | CI — naming convention workflow | `.github/workflows/cstylecheck_rules.yml` | CI/CD |
| CI-025 | CI — Docker publish workflow | `.github/workflows/docker_publish.yml` | CI/CD |
| CI-026 | Project README (with the logo image it embeds) | `README.md`, `logo/cstylecheck.jpg` | Documentation |
| CI-027 | This CM Plan | `docs/aspice/CStyleCheck_SUP8_CM_Plan.md` | Documentation |
| CI-028 | AI Authorship Deviation Record | `docs/aspice/CStyleCheck_DEV001_AI_Authorship_Deviation.md` | Documentation |
| CI-029 | CI trend-record append script | `scripts/ci/append_trend_record.py` | CI script |
| CI-030 | CI trend HTML and badge generation script | `scripts/ci/generate_trend.py` | CI script |
| CI-031 | CI README badge update script | `scripts/ci/update_readme_badge.py` | CI script |
| CI-032 | Independent Review Deviation Record | `docs/aspice/CStyleCheck_DEV002_Independent_Review_Deviation.md` | Documentation |
| CI-033 | Software Version Description | `docs/aspice/CStyleCheck_SVD_Software_Version_Description.md` | Documentation |
| CI-034 | CI — wiki publish workflow | `.github/workflows/wiki_publish.yml` | CI/CD |
| CI-035 | Pre-release validation script | `scripts/prerelease_check.sh` | CI/CD script |
| CI-036 | Pre-release validation script (Windows) | `scripts/check_my_project.bat` | CI/CD script |
| CI-037 | DockerHub repository description | `DOCKERHUB_README.md` | Documentation |
| CI-038 | CI — trend-analysis metrics workflow | `.github/workflows/metrics.yml` | CI/CD |
| CI-039 | Trend metrics collection script (C source metrics) | `scripts/collect_metrics.py` | CI script |
| CI-040 | Trend chart (SVG) generation script | `scripts/generate_charts.py` | CI script |
| CI-041 | Trend-Analysis wiki page generation script | `scripts/update_wiki_metrics.py` | CI script |
| CI-042 | PR metrics comparison report script | `scripts/compare_metrics.py` | CI script |
| CI-043 | Trend metrics CStyleCheck config and threshold documentation | `scripts/metrics_rules.yml` | CI config |
| CI-044 | Trend metrics unit tests (subset of CI-017, listed separately because it verifies COMP-13 rather than the package) | `tests/test_collect_metrics.py` | Test |
| CI-045 | Checker package source (12 modules: `__init__`, `baseline`, `checker`, `cli`, `config`, `fixer`, `models`, `output`, `preprocessor`, `sign_checker`, `utils`, `wizard`) | `src/cstylecheck/*.py` | Source code |
| CI-046 | Dependabot configuration (`pip` and `github-actions`, `target-branch: develop`) | `.github/dependabot.yml` | CI/CD configuration |
| CI-047 | Change log | `CHANGELOG.md` | Documentation |
| CI-048 | Contribution guide | `CONTRIBUTING.md` | Documentation |
| CI-049 | Rules and configuration reference (wiki source) | `Rules-and-Configuration.md` | Documentation |
| CI-050 | Example project preprocessor defines | `src/project.defines` | Configuration |
| CI-051 | Windows build helper script | `scripts/build.bat` | Build script |
| CI-052 | Windows test helper script | `scripts/test.bat` | Build script |
| CI-053 | Test package marker | `tests/__init__.py` | Test |
| CI-054 | Licence | `LICENSE` | Documentation |
| CI-055 | ASPICE work products (each identified by its CSC document ID and version, e.g. CSC-SWE1-001; includes review records and the review template) | `docs/aspice/CStyleCheck_*.md`, `docs/templates/ASPICE_CL2_Test_Case_Template_1.md` | Documentation |
| CI-056 | ASPICE internal audit records (CSC-AUD-nnn) | `docs/aspice/audits/*.md` | Documentation |
| CI-057 | Repository configuration | `.gitignore`, `.gitattributes`, `.codespellrc` | Repository configuration |
| CI-058 | AI assistant standing instructions (see CSC-DEV-001) | `CLAUDE.md` | Documentation |
| CI-059 | Example C sources (trend-metrics input, CI-038 to CI-043) and example project | `examples/**` | Example / test data |
| CI-060 | Draft companion standards documents | `embedded_c_style_guide.md`, `embedded_c_coding_standard.md`, `external_standards_analysis.md` | Documentation (draft) |

### 6.2 Identification Scheme

- **Source files** are identified by file path within the repository and Git commit SHA
- **Releases** are identified by semantic version tag in the format `vMAJOR.MINOR.PATCH` (e.g., `v1.0.0`)
- **Docker images** are tagged using the scheme:
  - On version tag `v1.2.3`: `:1.2.3`, `:1.2`, `:1`, `:latest`
  - On branch push: `:main`, `:sha-<short>`
- **CI artefacts** (coverage reports) are identified by workflow run ID and Python version matrix entry
- **Documents** use the ID scheme `CSC-<PROCESS>-<NNN>` (e.g., `CSC-SUP8-001`)

---

## 7. Branching Strategy

CStyleCheck uses the **Git Flow** branching model. The following branches are defined and maintained under configuration control.

### 7.1 Permanent Branches

| Branch | Purpose | Protection Rules |
|---|---|---|
| `main` | Production-ready code only; reflects the latest release baseline | Direct push prohibited; merged from `release/*` or `hotfix/*` only; every release merge and every hotfix that changes the delivered software creates a version tag; CI/repository-configuration-only hotfixes are not tagged (§7.6) |
| `develop` | Integration branch for completed features; always buildable | Direct push restricted; merged from `feature/*`, `bugfix/*` and `claude/<topic>-<id>` (AI-authored feature or bug-fix work, see CLAUDE.md) via pull request; CI must pass |

### 7.2 Supporting Branches

| Branch Pattern | Created From | Merges Into | Purpose |
|---|---|---|---|
| `feature/<issue-id>-<short-description>` | `develop` | `develop` | New feature or enhancement; one branch per GitHub Issue |
| `bugfix/<issue-id>-<short-description>` | `develop` | `develop` | Non-critical bug fix targeting the next release |
| `claude/<topic>-<id>` | `develop` | `develop` | AI-authored feature or bug-fix work (equivalent to `feature/*` / `bugfix/*`); the PR references the GitHub Issue. May also be used for a hotfix targeting `main` under §7.6 |
| `release/<version>` | `develop` | `main` and `develop` | Release preparation; version bump, final testing, and docs only — no new features |
| `hotfix/<issue-id>-<short-description>` | `main` | `main` and `develop` | Critical production defect requiring immediate patch release, or a CI/repository-configuration-only fix (no version bump or tag, §7.6) |

### 7.3 Branch Naming Convention

Supporting branches shall be named using the following scheme:

- `feature/42-add-misra-rule-15` — feature branch for GitHub Issue #42
- `bugfix/67-fix-typedef-false-positive` — bug fix for GitHub Issue #67
- `release/1.1.0` — release preparation for version 1.1.0
- `hotfix/89-null-pointer-crash` — hotfix for critical Issue #89
- `claude/boolean-optin-412` — AI-authored work for Issue #412 (`claude/<topic>-<id>`, where `<id>` is the Issue number or a session suffix)

### 7.4 Git Flow Lifecycle

```
develop ──────────────────────────────────────────────────►
         ↑   ↑                   ↑
         │   └── feature/* ──────┘
         │
release/* branch ──► main ──► tag v1.0.0
                  └──────────► develop (back-merge)

main ──► hotfix/* ──► main ──► tag v1.0.1
                   └────────► develop (back-merge)
```

### 7.5 CI Enforcement

- All merges to `develop` and `main` require CI (`cstylecheck_tests.yml`) to pass
- The `cstylecheck_rules.yml` workflow runs the linter against the project's own source on every commit touching C files, enforcing self-hosting of the tool's own rules
- Supporting branches are deleted after merge
- Dependabot (CI-046) opens dependency-update pull requests against `develop` (`target-branch: develop`, #399/#403). Dependabot PRs follow the normal feature-PR rules and reach `main` only through a release

> **📋 Note:** The `release/*` branch is the only branch where version-bump commits (`_version.py`, `pyproject.toml`) and release notes updates are permitted outside of `develop`. No new features may be introduced on a `release/*` branch.

### 7.6 Hotfix Versioning and Tagging Policy

| Hotfix content | Version bump | Tag | Records |
|---|---|---|---|
| Change to the delivered software (`src/`, `pyproject.toml`, `Dockerfile/`, `action.yml`, `.pre-commit-hooks.yml`) | Mandatory PATCH bump (e.g. 1.6.0 → 1.6.1) in `pyproject.toml` | Annotated tag `vX.Y.Z` on the `main` merge commit (pushed manually by the repository owner; tag pushes are not possible from the AI environment) | CHANGELOG entry, SVD update, GitHub Release |
| CI / repository-configuration only (`.github/`, `scripts/ci/`, documentation), no change to the delivered software | No version bump | No tag. The `main` HEAD remains a development baseline (§8.1) of the last release | CHANGELOG `[Unreleased]` / next SVD "CI and repository changes" entry; the hotfix PR is referenced in the next release notes |

Every hotfix is back-merged into `develop` immediately. Hotfix branches may use the `claude/<topic>-<id>` naming used for AI-authored work (see CLAUDE.md) in place of `hotfix/<issue-id>-…`, provided the PR is labelled as a hotfix and targets `main`.

> **Record (AUD9-F-028):** Hotfix #399 (commits `8da22b9`/`945dd02`, Dependabot `target-branch: develop`) was a CI-configuration-only change. Under this policy it needed no patch version or tag. It was back-merged into `develop` by #403 and is to be recorded in the next SVD. `main` therefore holds `v1.6.0` plus #399 with no new tag.

---

## 8. Baseline Management

### 8.1 Baseline Types

| Baseline Type | Trigger | Git Mechanism | Contents |
|---|---|---|---|
| **Development Baseline** | Successful CI run on `main` | Commit SHA on `main` | Latest passing source + tests |
| **Release Baseline** | Manual decision to release | Annotated Git tag `v*.*.*` | Full repository snapshot at that commit |
| **Container Baseline** | Docker publish workflow | GHCR image digest + tag | Immutable Docker image layer set |

### 8.2 Release Baseline Procedure

1. A `release/<version>` branch is created from `develop`; all CI checks pass (unit tests across Python 3.10 / 3.11 / 3.12, naming convention check, Docker build)
2. `_version.py` reflects the intended release version (generated via `git describe --tags`)
3. The `release/<version>` branch is merged into `main` and back-merged into `develop`
4. An annotated tag is created on `main`: `git tag -a v1.0.0 -m "Release v1.0.0"`
5. Tag is pushed: `git push origin v1.0.0`
6. `docker_publish.yml` automatically builds and pushes the tagged image to GHCR and Docker Hub
7. A GitHub Release entry is created with release notes derived from the change log
8. The `release/<version>` branch is deleted

### 8.3 Baseline Integrity

- Git SHA is the primary integrity mechanism for source baselines
- Docker image digest (SHA-256) provides integrity verification for container baselines
- The `build-and-push` job prints the image digest to the Actions log as an audit record
- Layer caching uses a dedicated `:buildcache` tag in GHCR to speed incremental builds without affecting release tags

---

## 9. Change Control

Changes to controlled configuration items shall follow the change control process defined in **CSC-SUP10-001 (Change Request Management Plan)**. In summary:

1. A change request (CR) or problem resolution record is raised as a **GitHub Issue**, labelled appropriately (`bug`, `enhancement`, `change-request`)
2. The Issue is linked in all related branch names and commit messages (e.g., `Closes #42`)
3. The change is implemented on the appropriate Git Flow branch (`feature/*`, `bugfix/*`, `claude/<topic>-<id>` or `hotfix/*`) per §7
4. A pull request is opened targeting `develop` (or `main` for hotfixes); CI must pass before merge. The owner's merge of the PR is the approval and authorisation of every work-product revision it introduces; no separate signature is required, and the merge commit is the approval record (solo-developer project; CSC-DEV-002 §5.2)
5. The merged commit SHA is recorded in the GitHub Issue closure comment
6. If the change affects a release, a `release/*` branch is created and a new version tag applied per §8.2

> **Revision-history practice (AUD10-F-032):** When a change set only resyncs cross-referenced document versions in a work product, the resync is recorded as one revision of that document per change set (one PR, or one release preparation), not as one revision per upstream change.

> **Note:** This document is under configuration management (SUP.8). Post-approval changes require a change request (SUP.10) and a new document version.

---

## 10. Configuration Status Accounting

### 10.1 Status Tracking

| Mechanism | What It Tracks |
|---|---|
| GitHub commit history | Full chronological record of all changes to every CI |
| GitHub Issues | Problem resolution records and change requests, linked to commits and pull requests |
| GitHub Pull Requests | Review record, CI pass/fail, approvals, merge commit, and linked Issue closure |
| GitHub Actions run log | CI execution evidence per commit; coverage artefact per run |
| GitHub Releases | Named release baselines with artefact links |
| GHCR image tags | Container release history with immutable digests |

### 10.2 Reporting

Configuration status shall be accessible at any time via:

- `git log --oneline` — commit history
- `git tag -l` — all release baselines
- GitHub Releases page — named releases with notes
- GHCR package page — container image history and digests

---

## 11. Configuration Audits

### 11.1 Functional Configuration Audit (FCA)

Performed prior to each release baseline to verify:

- [ ] All CI-001 to CI-037 items are present and committed
- [ ] Version in `_version.py` (CI-002) matches the intended tag
- [ ] All unit tests pass on Python 3.10, 3.11, 3.12
- [ ] Naming convention workflow passes on current source
- [ ] Docker image builds without error
- [ ] `pyproject.toml` version (CI-013) matches `_version.py`
- [ ] `README.md` is up to date with the release

### 11.2 Physical Configuration Audit (PCA)

Performed after tagging to verify:

- [ ] Git tag points to the correct commit
- [ ] Docker image digest is recorded in the GitHub Actions run log
- [ ] GitHub Release entry references the correct tag and digest
- [ ] No uncommitted changes exist on `main` at the point of tagging

### 11.3 Audit Schedule

| Audit Type | Frequency |
|---|---|
| Functional Configuration Audit | Before every release |
| Physical Configuration Audit | After every release tag |
| Informal CM Review | Monthly, or on any SUP.10 change request affecting CIs |

---

## 12. Roles & Responsibilities

| Role | Responsibility |
|---|---|
| **CM Manager** (Claude) | Owns this plan; approves baselines; creates release tags; manages GHCR |
| **Developer** | Creates Git Flow branches; raises GitHub Issues; opens pull requests; links commits and PRs to Issues |
| **Reviewer** | Dermot Murphy |
| **CI System** (GitHub Actions) | Automated enforcement: runs tests, linting, Docker build on every push/PR |

---

## 13. Backup & Recovery

| Item | Mechanism | Recovery |
|---|---|---|
| Source repository | GitHub hosted (distributed Git — every clone is a backup) | Re-clone from GitHub or any developer's local copy |
| Docker images | GHCR + Docker Hub (dual registry) | Pull from either registry by tag or digest |
| CI artefacts | GitHub Actions artefacts (30-day retention) | Re-run the workflow from the same commit SHA to regenerate |

> **📋 Note:** Because Git is a distributed VCS, every developer's local clone constitutes an independent backup of all commits and tags up to their last `fetch`. The primary risk is loss of GitHub-hosted Issues and pull request history; this is mitigated by GitHub's platform reliability and the requirement to reference Issue numbers in all commit messages and branch names.

---

## 14. Review & Approval

| Role | Name | Signature / Electronic Approval | Date |
|---|---|---|---|
| Author | Claude | Approved | 2026-09-29 |
| Technical Reviewer | Dermot Murphy | By merge (CSC-DEV-002 §5.2) | On PR merge |
| Quality Assurance | Dermot Murphy | By merge (CSC-DEV-002 §5.2) | On PR merge |
| Approver | Dermot Murphy | By merge (CSC-DEV-002 §5.2) | On PR merge |

> Approval is given by the owner's merge of the pull request that introduces this revision; the merge commit is the approval record (CSC-DEV-002 §5.2).

> **Note:** This document is under configuration management (SUP.8). Post-approval changes require a change request (SUP.10) and a new document version.
