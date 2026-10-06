# Supplier Monitoring Plan

*Automotive SPICE® PAM v4.0 | ACQ.4 Supplier Monitoring*

---

## 1. Document Identification & Control

| Field | Value | Field | Value |
|---|---|---|---|
| **Document ID** | CSC-ACQ4-001 | **Version** | 1.17 |
| **Project** | CStyleCheck | **Date** | 2026-10-06 |
| **Status** | Released | **Classification** | Internal |
| **Author** | Claude | **Reviewer** | Dermot Murphy |
| **Approver** | Dermot Murphy | **Related Process** | ACQ.4 |

---

## 2. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.17 | 2026-10-06 | Claude | Cross-reference version resync after the v1.6.1 hotfix back-merge (#444): referenced-document versions set to the current baseline; no technical content change |
| 1.16 | 2026-09-30 | Claude | Merge-time process controls (#437): §5.2 CI workflow availability monitors `aspice_consistency.yml`; acceptance criterion counts six CI workflows; referenced-document versions resynced |
| 1.15 | 2026-09-30 | Claude | Cross-reference version resync (#435): all referenced-document versions set to the current baseline (every controlled work product bumped once in this change set); no technical content change |
| 1.14 | 2026-09-29 | Claude | CSC-AUD-010 corrective actions (#430). AUD10-F-030: SUP-09 (Python development and CI tool maintainers: pytest, pytest-cov, ruff, mypy with types-PyYAML, codespell) added to §4 with monitoring approach in new §5.8 and interface ACQ-IF-07 in §6; approval-by-merge policy (CSC-DEV-002 §5.2) |
| 1.13 | 2026-09-29 | Claude | Cross-reference resync with #423: 4 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.12 | 2026-09-29 | Claude | Cross-reference resync with #425: 4 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.11 | 2026-09-29 | Claude | Cross-reference resync with #424: 4 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.10 | 2026-09-29 | Claude | Cross-reference resync with #422: 4 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.9 | 2026-09-29 | Claude | Cross-reference resync with #420: 4 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.8 | 2026-09-29 | Claude | Cross-reference resync with #418: 4 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.7 | 2026-09-29 | Claude | Release-prep cross-reference resync: 4 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.6 | 2026-09-29 | Claude | Release-prep cross-reference resync: 4 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.5 | 2026-09-29 | Claude | Issue #407: cross-reference update only; referenced-document versions resynced (MAN3 1.8→1.9, MAN5 1.5→1.6, SUP8 1.13→1.14, SUP9 1.3→1.4) |
| 1.4 | 2026-09-29 | Claude | CSC-AUD-009 corrective actions (#405). AUD9-F-018: §5.2 Actions versions @v6→@v7 with the Docker and third-party actions; workflow list 3→5 (`rules.yml` → `cstylecheck_rules.yml`, add `wiki_publish.yml`, `metrics.yml`); Dependabot (`target-branch: develop`) monitoring row; add SUP-07 (Docker, Inc. actions) and SUP-08 (tj-actions, peter-evans) and §5.7 monitoring; SHA-pinning policy. AUD9-F-014: referenced-document versions resynced to current revisions |
| 1.3 | 2026-06-26 | Claude | Add SUP-06 Anthropic/Claude AI tool supplier entry (§3, §4, §5.6, §6); update CSC-MAN5-001 ref to 1.4; advance ACQ.4 to Full — closes issue #269 |
| 1.2 | 2026-06-18 | Claude | ASPICE audit #254 — sync referenced-document version citations to current versions |
| 1.1 | 2026-05-28 | Claude | Reviewed and updated for v1.1.0 release; revision history maintained per ASPICE GP 2.2.4 |
| 1.0 | 2026-04-12 | Claude | Initial release |

---

## 3. Purpose & Scope

This Supplier Monitoring Plan defines how CStyleCheck monitors and manages its external suppliers of components, tools, and services. It satisfies **Automotive SPICE® PAM v4.0, ACQ.4 — Supplier Monitoring**.

CStyleCheck is a Python-only tool with minimal external dependencies. Its suppliers are limited to:

1. **PyPI / PyYAML** — the single runtime dependency
2. **GitHub** — version control, CI/CD, container registry, and release infrastructure
3. **Docker Hub** — secondary container registry
4. **Python Software Foundation** — Python interpreter (runtime platform)
5. **Base Docker image provider** — `python:slim` official images from Docker Hub
6. **Anthropic, PBC** — Claude AI assistant (AI-assisted code authoring, document generation, and ASPICE compliance analysis; see CSC-DEV-001)

There are no contracted Tier-1 software suppliers or subcontractors.

### 3.1 Referenced Documents

| Document ID | Title | Version |
|---|---|---|
| CSC-MAN3-001 | Project Management Plan | 1.22 |
| CSC-MAN5-001 | Risk Management Plan | 1.18 |
| CSC-SUP8-001 | Configuration Management Plan | 1.26 |
| CSC-SUP9-001 | Problem Resolution Management Plan | 1.16 |

---

## 4. Supplier Register

| SUP-ID | Supplier | Component / Service | Dependency Type | Version Constraint | Risk Reference |
|---|---|---|---|---|---|
| SUP-01 | Python Packaging Authority (PyPI) | PyYAML library | Runtime dependency | `pyyaml>=6.0,<7.0` | RISK-003 |
| SUP-02 | GitHub, Inc. | Source control, CI/CD (Actions), GHCR, Releases, Issues | Platform / Infrastructure | N/A (SaaS) | RISK-004 |
| SUP-03 | Docker, Inc. | Docker Hub (secondary registry); base image hosting | Platform / Infrastructure | N/A (SaaS) | RISK-004 |
| SUP-04 | Python Software Foundation | CPython interpreter | Runtime platform | 3.10, 3.11, 3.12 | RISK-002 |
| SUP-05 | Docker, Inc. | `python:3.12-slim` base image | Container base | Pinned via `ARG PYTHON_VERSION=3.12` | RISK-008 |
| SUP-06 | Anthropic, PBC | Claude AI assistant (code generation, document authoring, test generation, ASPICE compliance analysis) | AI/SaaS tool | N/A (SaaS; prompt-based; see CSC-DEV-001) | RISK-005 |
| SUP-07 | Docker, Inc. (GitHub Actions publisher) | `docker/login-action`, `docker/setup-qemu-action`, `docker/setup-buildx-action`, `docker/metadata-action`, `docker/build-push-action` (used in `docker_publish.yml`) | CI/CD action | Major-version tags (`@v4.6.0`, `@v4`, `@v4`, `@v6`, `@v7`); updated by Dependabot | RISK-004, RISK-008 |
| SUP-08 | Third-party GitHub Action publishers (`tj-actions`, `peter-evans`) | `tj-actions/changed-files` (`cstylecheck_rules.yml`), `peter-evans/dockerhub-description` (`docker_publish.yml`) | CI/CD action | `tj-actions/changed-files` pinned to full commit SHA `9426d40962ed5378910ee2e21d5f8c6fcbf2dd96` (v47.0.6); `peter-evans/dockerhub-description@v5` | RISK-008 |
| SUP-09 | Open-source maintainers via PyPI (pytest, pytest-cov, ruff, mypy, types-PyYAML, codespell) | Development and CI tools: test runner and coverage gate, lint, static type check, spell check (`cstylecheck_tests.yml`) | Development / CI tool (not shipped to users) | `requirements.txt`: `pytest>=7.4,<9.0`, `pytest-cov>=4.1,<6.0`, `mypy>=1.0`, `types-PyYAML>=6.0`, `ruff>=0.1`, `codespell>=2.2` (the Spell check step also installs `codespell` unpinned) | RISK-001, RISK-002 |

---

## 5. Supplier Monitoring Activities

### 5.1 PyYAML (SUP-01)

| Activity | Method | Frequency | Owner | Evidence |
|---|---|---|---|---|
| Security advisory monitoring | Check PyPI security advisories and GitHub advisory database for `pyyaml` | Monthly | Claude | Advisory review note in GitHub Issue (if action needed) |
| Version range review | Assess whether `pyyaml>=6.0,<7.0` remains appropriate; evaluate new major versions | Per PyYAML major release | Claude | `pyproject.toml` version constraint update CR if required |
| Availability check | Verify `pip install` succeeds in CI | Per CI run | GitHub Actions | `cstylecheck_tests.yml` — install step |

**Acceptance criteria for PyYAML:**
- `pip install pyyaml>=6.0,<7.0` succeeds without error in all CI environments
- No open critical CVEs against the installed version range
- `yaml.safe_load()` used exclusively (never `yaml.load()`)

### 5.2 GitHub (SUP-02)

| Activity | Method | Frequency | Owner | Evidence |
|---|---|---|---|---|
| CI workflow availability | Monitor `cstylecheck_tests.yml`, `cstylecheck_rules.yml`, `docker_publish.yml`, `wiki_publish.yml`, `metrics.yml` and `aspice_consistency.yml` job completion | Per commit | GitHub Actions status | CI badge on README; Actions run log |
| Action version updates | Dependabot `github-actions` ecosystem (`.github/dependabot.yml`, weekly, `target-branch: develop`) raises update PRs; each PR is reviewed and must pass CI before merge | Weekly | Dependabot / Dermot Murphy | Dependabot PRs (e.g. #400–#402, #404) |
| GHCR availability | Verify Docker images pullable after each push | Per `docker_publish.yml` run | GitHub Actions | `docker manifest inspect` in publish job |
| Actions runner version changes | Monitor GitHub changelog for breaking changes to `ubuntu-latest` runner | Monthly | Claude | GitHub blog / changelog review |
| API deprecation notices | Monitor GitHub Actions deprecation notices (e.g., deprecated action versions) | Monthly | Claude | GitHub announcement emails |

**Actions versions in use (`develop`, 2026-09-29):**
- `actions/checkout@v7` (#402)
- `actions/setup-python@v7` (#386, #404)
- `actions/upload-artifact@v7` (#400)
- `docker/login-action@v4.6.0` (#387, #401), `docker/setup-qemu-action@v4`, `docker/setup-buildx-action@v4`, `docker/metadata-action@v6`, `docker/build-push-action@v7` (SUP-07)
- `peter-evans/dockerhub-description@v5` and `tj-actions/changed-files@9426d40962ed5378910ee2e21d5f8c6fcbf2dd96` (v47.0.6) (SUP-08)

**Pinning policy:** first-party (`actions/*`) and Docker, Inc. actions are pinned to major-version tags and updated by Dependabot. Third-party actions whose publisher has had a supply-chain compromise (`tj-actions/changed-files`, March 2025) are pinned to a full commit SHA, with the version in a trailing comment.

**Acceptance criteria for GitHub:**
- All six CI workflows complete successfully when triggered on `develop`/`main`
- GHCR image available and pullable within 30 minutes of `docker_publish.yml` completion

### 5.3 Docker Hub (SUP-03)

| Activity | Method | Frequency | Owner | Evidence |
|---|---|---|---|---|
| Push availability | `docker_publish.yml` pushes to Docker Hub on release tags | Per release | GitHub Actions | `docker_publish.yml` job log |
| Image pullability | Verify published image pullable via `docker pull` | Post-release | Claude | Manual verification; GitHub Release checklist |

**Acceptance criteria for Docker Hub:**
- Image push succeeds without error in `docker_publish.yml`
- Published image responds correctly to `docker run cstylecheck:latest --help`

### 5.4 Python Software Foundation (SUP-04)

| Activity | Method | Frequency | Owner | Evidence |
|---|---|---|---|---|
| Version support monitoring | Track CPython release schedule for EOL of 3.10, 3.11, 3.12 | Annually | Claude | Python EOL schedule (`devguide.python.org`) |
| New minor version evaluation | Evaluate adding new Python minor version to CI matrix | Per new Python minor release | Claude | CR raised if new version added to matrix |
| Compatibility testing | `cstylecheck_tests.yml` matrix tests all supported versions | Per commit | GitHub Actions | CI matrix result |

**Current Python version policy:** Support the three most recent minor releases. When Python 3.13 is added, Python 3.10 is dropped (raise CR).

**Acceptance criteria for CPython:**
- All tests pass on all three supported versions per CI matrix
- `pyproject.toml` `requires-python` constraint updated to reflect dropped versions

### 5.5 Base Docker Image (SUP-05)

| Activity | Method | Frequency | Owner | Evidence |
|---|---|---|---|---|
| Base image security scan | Review Docker Scout / Docker Hub security advisories for `python:3.12-slim` | Monthly | Claude | Advisory review note |
| Image digest verification | Docker digest recorded in `docker_publish.yml` build log | Per build | GitHub Actions | Actions run log |
| Base image update | Bump `ARG PYTHON_VERSION` or rebuild to get updated OS packages | Per security advisory | Claude | CR raised; new Docker image pushed |

**Acceptance criteria for base image:**
- No critical CVEs unpatched in the deployed `python:3.12-slim` layer
- Image digest recorded in GitHub Actions log for each production build

### 5.6 Anthropic / Claude AI Assistant (SUP-06)

| Activity | Method | Frequency | Owner | Evidence |
|---|---|---|---|---|
| Output review | All AI-generated code, tests, and documents reviewed and approved by Dermot Murphy before commit | Per usage | Dermot Murphy | GitHub PR approval record; Reviewer/Approver fields in each ASPICE document |
| Model version change assessment | Monitor Anthropic release notes for capability or behaviour changes affecting output quality | Per Claude model release | Dermot Murphy | GitHub Issue raised if prompt compatibility or output quality degrades |
| Reproducibility verification | Verify that key ASPICE documents and code can be regenerated from existing context when required | Per release | Dermot Murphy | Internal note in pre-release checklist (CSC-SUP1-001 §5.4) |
| AI authorship deviation compliance | Confirm CSC-DEV-001 deviation record remains current and approved | Per document revision | Dermot Murphy | CSC-DEV-001 revision history |

**Acceptance criteria for Anthropic/Claude:**
- All AI-generated content reviewed and approved by Dermot Murphy before merge (enforced via PR review gate)
- No unreviewed AI-generated outputs committed to the repository
- CSC-DEV-001 AI Authorship Deviation Record remains current and approved

### 5.7 GitHub Action Publishers (SUP-07, SUP-08)

| Activity | Method | Frequency | Owner | Evidence |
|---|---|---|---|---|
| Version updates | Dependabot `github-actions` PRs against `develop`; review release notes before merge | Weekly | Dermot Murphy | Dependabot PRs |
| Supply-chain advisories | Check GitHub Security Advisories for each action in use; for SHA-pinned actions, re-verify the SHA against the upstream tag before bumping | Monthly | Claude | Advisory review note in the GitHub Issue |
| Permissions review | Confirm each workflow's `permissions:` block grants only what the action needs | Per workflow change | Claude | PR review |

**Acceptance criteria:** every action in `.github/workflows/*.yml` appears in the §5.2 list with its current version, and third-party actions are SHA-pinned or on a Dependabot-tracked tag.

### 5.8 Development and CI Tools (SUP-09)

| Activity | Method | Frequency | Owner | Evidence |
|---|---|---|---|---|
| Version updates | Dependabot `pip` ecosystem (`.github/dependabot.yml`, directory `/`, weekly, `target-branch: develop`) raises update PRs for `requirements.txt`; each PR must pass CI before merge | Weekly | Dependabot / Dermot Murphy | Dependabot PRs |
| Tool availability and behaviour | `pip install -r requirements.txt` and the pytest (coverage gate `--cov-fail-under=85`), mypy, ruff and codespell steps must succeed in `cstylecheck_tests.yml`; a failure caused by a new tool release (new lint rule, new spelling, changed coverage measurement) is raised as a SUP.9 Issue | Per CI run | GitHub Actions / Claude | `cstylecheck_tests.yml` run log |
| Configuration review | Keep `[tool.pytest.ini_options]` and `[tool.ruff.lint]` in `pyproject.toml` and `.codespellrc` consistent with the installed tool versions | Per tool major release | Claude | PR that changes the configuration |
| Security advisories | Check the GitHub advisory database for the tools; they run only in CI and developer environments and are not part of the delivered package or Docker image | Quarterly | Claude | Advisory review note in the GitHub Issue (if action needed) |

**Acceptance criteria:** all tool steps in `cstylecheck_tests.yml` pass on `develop` and `main`; version constraints in `requirements.txt` are current or a Dependabot PR is open for them.

---

## 6. Supplier Interface Summary

| Interface | From | To | Data Exchanged | Protocol |
|---|---|---|---|---|
| ACQ-IF-01 | `cstylecheck.py` | PyYAML (SUP-01) | YAML config file content | Python `import yaml; yaml.safe_load()` |
| ACQ-IF-02 | `cstylecheck_tests.yml` | GitHub Actions (SUP-02) | Source code; test results; coverage report | GitHub Actions event-driven |
| ACQ-IF-03 | `docker_publish.yml` | GHCR (SUP-02) | Docker image layers | Docker push; OCI registry API |
| ACQ-IF-04 | `docker_publish.yml` | Docker Hub (SUP-03) | Docker image layers | Docker push; Docker Registry API |
| ACQ-IF-05 | Dockerfile | `python:3.12-slim` (SUP-05) | Base OS + Python runtime | Docker `FROM` directive |
| ACQ-IF-06 | Development workflow | Anthropic/Claude (SUP-06) | Prompts; generated code; document content | Claude Code CLI / Anthropic API |
| ACQ-IF-07 | `cstylecheck_tests.yml`, developer environment | pytest, pytest-cov, ruff, mypy, codespell (SUP-09) | Source code, tests and docs in; test, coverage, lint, type and spelling results out | `pip install -r requirements.txt`; command-line invocation |

---

## 7. Non-Conformance Handling

If a supplier fails to meet acceptance criteria:

| Scenario | Response |
|---|---|
| PyYAML critical CVE | Raise RISK-003 impact; evaluate upgrade or workaround; raise CR; release patch |
| GitHub Actions outage | Monitor GitHub status page; retry CI when service restored; no code change required |
| GHCR push failure | Retry via `workflow_dispatch`; users fall back to Docker Hub image |
| Python version incompatibility | Raise Issue; fix in `bugfix/` branch; update CI matrix |
| Base image CVE | Rebuild Docker image with updated base; create patch release |

All non-conformances are recorded as GitHub Issues (label: `supplier-issue`) and tracked to closure.

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
