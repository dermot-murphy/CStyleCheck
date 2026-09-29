# Change Request Management Plan

*Automotive SPICE® PAM v4.0 | SUP.10 Change Request Management*

---

## 1. Document Identification & Control

| Field | Value | Field | Value |
|---|---|---|---|
| **Document ID** | CSC-SUP10-001 | **Version** | 1.12 |
| **Project** | CStyleCheck | **Date** | 2026-09-29 |
| **Status** | Released | **Classification** | Internal |
| **Author** | Claude | **Reviewer** | Dermot Murphy |
| **Approver** | Dermot Murphy | **Related Process** | SUP.10 |

---

## 2. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.12 | 2026-09-29 | Claude | Cross-reference resync with #423: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.11 | 2026-09-29 | Claude | Cross-reference resync with #424: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.10 | 2026-09-29 | Claude | Cross-reference resync with #422: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.9 | 2026-09-29 | Claude | Cross-reference resync with #420: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.8 | 2026-09-29 | Claude | Issue #418: §7 register row and new §7.1 record for CR-418 (new-rule opt-in policy; the 7 remaining post-v1.6.0 MISRA/Barr-C rules disabled by default, also when the key is absent; requirements change SWE1-109 to SWE1-114 and SWE1-116; impact on behaviour); referenced-document versions resynced (3) |
| 1.7 | 2026-09-29 | Claude | Release-prep cross-reference resync: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.6 | 2026-09-29 | Claude | Release-prep cross-reference resync: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.5 | 2026-09-29 | Claude | Issue #413: §7 register row and new §7.1 record for CR-413 (SYS-F-046 / SWE1-094 startup-banner requirements aligned with the implementation; no code impact) |
| 1.4 | 2026-09-29 | Claude | Issue #407: cross-reference update only; referenced-document versions resynced (MAN3 1.8→1.9, SUP8 1.13→1.14, SUP9 1.3→1.4) |
| 1.3 | 2026-09-29 | Claude | CSC-AUD-009 corrective actions (#405). AUD9-F-014: referenced-document versions resynced to current revisions |
| 1.2 | 2026-06-18 | Claude | ASPICE audit #254 — sync referenced-document version citations to current versions |
| 1.1 | 2026-05-28 | Claude | Reviewed and updated for v1.1.0 release; revision history maintained per ASPICE GP 2.2.4 |
| 1.0 | 2026-04-12 | Claude | Initial release |

---

## 3. Purpose & Scope

This Change Request Management Plan defines the process for requesting, evaluating, approving, implementing, and verifying changes to any controlled configuration item of **CStyleCheck v1.0.0**. It satisfies **Automotive SPICE® PAM v4.0, SUP.10 — Change Request Management**.

A **change request (CR)** covers any planned modification to a baselined work product that is not a defect fix — including new features, new rules, configuration changes, documentation updates, and process improvements. Defect fixes are handled under SUP.9 but also follow this plan for their change-control steps once the fix has been accepted.

### 3.1 Referenced Documents

| Document ID | Title | Version |
|---|---|---|
| CSC-SUP8-001 | Configuration Management Plan | 1.21 |
| CSC-SUP9-001 | Problem Resolution Management Plan | 1.11 |
| CSC-MAN3-001 | Project Management Plan | 1.17 |

---

## 4. Change Request Classification

### 4.1 Change Types

| Type | Label | Description |
|---|---|---|
| **Enhancement** | `enhancement` | New rule, new output format, new CLI flag, new integration |
| **Improvement** | `improvement` | Optimisation, UX improvement, performance improvement |
| **Documentation** | `documentation` | Update to ASPICE documents, README, or in-code documentation |
| **Configuration** | `config-change` | Update to `rules.yml`, `exclusions.yml`, or dictionary files |
| **Process** | `process-change` | Update to CI workflows, Git Flow procedure, or QA activities |

### 4.2 Impact Levels

| Impact | Criteria | Approval Required |
|---|---|---|
| **Low** | Changes a single CI; no interface impact; no requirement change | Author self-review |
| **Medium** | Changes multiple CIs; impacts one interface; minor requirement change | Peer review (1 approver) |
| **High** | Changes architecture, adds/removes requirements, breaks backwards compatibility | Peer review + explicit QA sign-off |

---

## 5. Change Request Process

### 5.1 Raising a Change Request

All change requests are raised as **GitHub Issues** with the `enhancement`, `improvement`, `documentation`, `config-change`, or `process-change` label.

Minimum required fields when raising a CR Issue:

| Field | Required Content |
|---|---|
| **Title** | `[CR] <brief description of change>` |
| **Type label** | One of the type labels from §4.1 |
| **Impact level** | Low / Medium / High |
| **Motivation** | Why the change is needed; which stakeholder need or deficiency it addresses |
| **Description** | What specifically will change; which CIs (from CSC-SUP8-001 §6.1) are affected |
| **Affected documents** | Which ASPICE work products require updating |
| **Proposed target release** | Which version the change is planned for |

### 5.2 Change Evaluation

1. Issue assigned to Claude for evaluation
2. Assess: technical feasibility, effort estimate, impact on existing requirements, impact on test suite, version number implications (patch/minor/major)
3. Check for conflicts with open Issues or other planned changes
4. Evaluate impact on ASPICE documents — identify which WPs need revision
5. Record evaluation outcome in the Issue comment thread

### 5.3 Change Approval

| Impact Level | Approval Mechanism |
|---|---|
| Low | Author marks Issue as approved in comment; proceeds to implementation |
| Medium | At least one peer review approval on the implementing pull request |
| High | Explicit approval comment from QA role in the Issue thread before implementation begins |

Changes that modify requirements (CSC-SWE1-001 or CSC-SYS2-001) always require Medium or High approval regardless of other impact assessment.

### 5.4 Implementation

Accepted changes are implemented following the Git Flow process defined in CSC-SUP8-001 §7:

| Change Type | Branch | Target |
|---|---|---|
| New feature or enhancement | `feature/<issue-id>-<description>` | `develop` |
| Configuration or documentation | `feature/<issue-id>-<description>` | `develop` |
| Urgent backwards-compatible fix affecting released version | `hotfix/<issue-id>-<description>` | `main` and `develop` |

Commit messages must reference the Issue: `Implements #<issue-id>: <description>`

All implementing PRs must:
- Pass CI (`cstylecheck_tests.yml`, `rules.yml`)
- Include or update affected ASPICE documents in the same branch or a linked follow-up Issue
- Update traceability tables if requirements are added or modified

### 5.5 Verification

1. CI must pass on the implementing branch
2. If the CR adds a new rule: at least one test case must be added to the test suite demonstrating the rule fires on invalid input and passes on valid input
3. If the CR changes a requirement: the corresponding SWE.4/SWE.6 test case must be updated
4. Pull request reviewer confirms all affected documents have been updated before approving

### 5.6 Closure

- Issue is closed when the implementing PR is merged
- If the CR affects a released version: version number is incremented per semantic versioning
  - Patch (`1.0.x`): backwards-compatible bug fixes
  - Minor (`1.x.0`): new rules, new CLI flags, new output formats (backwards compatible)
  - Major (`x.0.0`): breaking changes (removed flags, changed default behaviour, incompatible config format)
- Release notes for the target release must reference the CR Issue number

---

## 6. Impact on Configuration Items

When a CR is approved, the following CIs may require update:

| CR Type | Likely Affected CIs |
|---|---|
| New rule | CI-001 (`cstylecheck.py`), CI-003 (`rules.yml`), CI-017 (test suite), CI-026 (README) |
| New CLI flag | CI-001, CI-013 (`pyproject.toml`), CI-016 (`action.yml`), CI-026 (README) |
| New output format | CI-001, CI-016 (`action.yml`), CI-026 (README) |
| Config file change | CI-003 or CI-005 to CI-010 |
| CI workflow change | CI-023 to CI-025 |
| ASPICE document update | Affected document CI (e.g., CI-027) + new version entry in §2 |

All affected CIs must be updated within the same Git Flow branch as the implementing change (or in an explicitly linked follow-up Issue tracked to the same release).

---

## 7. Change Request Register

The GitHub Issues board at `https://github.com/dermot-murphy/CStyleCheck/issues` serves as the CR register. Filter by enhancement/improvement/documentation/config-change/process-change labels.

Summary view:

| Issue # | Type | Title | Impact | Status | Target Release |
|---|---|---|---|---|---|
| \<Auto-populated from GitHub Issues — see Issues board\> | | | | | |
| #413 | `documentation` | [CR] Align startup-banner requirements SYS-F-046 and SWE1-094 with the implementation | Medium | Implemented on `claude/banner-reqs-413`; closes on PR merge | Next release after v1.6.0 |
| #418 | `config-change` | [CR] New-rule opt-in policy: the 7 remaining post-v1.6.0 MISRA/Barr-C rules disabled by default | High | Implemented on `claude/optin-policy-418`; closes on PR merge | Next release after v1.6.0 |

### 7.1 Change Request Records

| Field | CR-413 |
|---|---|
| **Issue** | [#413](https://github.com/dermot-murphy/CStyleCheck/issues/413) |
| **Date** | 2026-09-29 |
| **Raised by / implemented by** | Dermot Murphy (option 1 selected) / Claude |
| **Type** | `documentation` — requirement change to align with the implementation |
| **Impact level** | Medium (modifies CSC-SYS2-001 and CSC-SWE1-001, see §5.3) |
| **Change** | SYS-F-046 and SWE1-094 rewritten to the behaviour of `main()` in `cli.py`: two lines on stderr (`CStyleCheck <version>`, `(C) 2026 Dermot Murphy`) before checking, also written to `--log`, written even when stdout is piped, no suppression option, never on stdout. SWE1-015 records the `--fix` header re-read exception. IDs and the SYS-F-046 → SWE1-094 trace are unchanged |
| **Rationale** | The banner was specified three different ways (SYS-F-046: date-time, file count, suppressed when stdout is not a TTY; SWE1-094: one line, suppressed by `--quiet`; code: two lines, always). The v1.6.0 behaviour is released and documented (CHANGELOG, README) and keeps stdout clean for piped JSON/SARIF output, so the requirements were changed rather than the code |
| **Impact on code** | None — no change to `src/` |
| **Affected documents** | CSC-SYS2-001 v2.5, CSC-SWE1-001 v2.10, CSC-SWE2-001 v1.15, CSC-SWE3-001 v1.20, CSC-SWE4-001 v1.25, CSC-SWE5-001 v1.17, CSC-SWE6-001 v1.19, README, CHANGELOG |
| **Verification** | 5 unit tests added to `tests/test_cli_requirements.py` (UV-CLI-017 to UV-CLI-019 now verify SWE1-094 in full); 1444 tests PASS |

| Field | CR-418 |
|---|---|
| **Issue** | [#418](https://github.com/dermot-murphy/CStyleCheck/issues/418) |
| **Date** | 2026-09-29 |
| **Raised by / implemented by** | Dermot Murphy (option 1 selected: all new rules are opt-in) / Claude |
| **Type** | `config-change` — requirement change and default-configuration change |
| **Impact level** | High (changes the default behaviour of 7 rules on `develop` (not yet released) and modifies CSC-SWE1-001, see §4.2 and §5.3) |
| **Change** | `misc.goto_usage`, `misc.assignment_in_condition`, `misc.multiple_statements_per_line`, `misc.void_pointer`, `misc.recursive_function`, `misc.sizeof_type` and `misc.empty_else` ship `enabled: false` in `src/rules.yml` and `tests/rules.yml`, and each `_check_*` method reads `cfg.get("enabled", False)`. `misc.boolean_comparison` was already opt-in (#412). `--update-config` adds the keys as `enabled: false`. The sample profile `examples/embedded_project/config/strict.yml` enables all 8 at their default severities |
| **Policy** | New rules ship `enabled: false` and default to disabled when the key is absent; they may be enabled in presets. Recorded in `CONTRIBUTING.md` (New Rule Policy) and enforced by the UV-MSR-009 policy tests |
| **Requirements change** | SWE1-109 to SWE1-114 and SWE1-116 each gain "The rule shall be disabled by default, including when the configuration key is absent (opt-in, #418)"; RTM rows marked opt-in. SYS-F-020 is unchanged (it states what can be enforced, not the defaults). IDs and traces are unchanged |
| **Impact on behaviour** | With a project config that does not set `enabled: true` for these rules (including configs written by `--init` or `--preset`, which do not list them), the 7 rules no longer report violations. Upgrading therefore adds no new findings to an existing project. Projects that want the rules set `misc.<rule>.enabled: true`. Detection logic, rule IDs, severities and messages are unchanged |
| **Rationale** | `misc.boolean_comparison`, when on by default, produced 433 new warnings on a reference project (#412). Turning on new rules by default on upgrade has the same risk for the other 7 rules. Opt-in keeps upgrades stable and lets each project adopt a rule when it is ready |
| **Impact on code** | `src/cstylecheck/checker.py` (7 `enabled` defaults), `src/rules.yml`, `tests/rules.yml`, `examples/embedded_project/config/strict.yml` |
| **Affected documents** | CSC-SWE1-001 v2.14, CSC-SWE3-001 v1.24, CSC-SWE4-001 v1.29, CSC-SWE5-001 v1.20, CSC-SWE6-001 v1.23, CSC-SYS4-001 v1.17, CSC-SYS5-001 v1.14, CSC-PA2-001 v1.28, CSC-MAN3-001 v1.13, CONTRIBUTING, README, Rules-and-Configuration, CHANGELOG |
| **Verification** | 11 tests added to `tests/test_misra_rules.py` (UV-MSR-009): one key-absent test per rule, plus policy tests. The policy tests check that all 8 opt-in rules ship disabled, that none fires with an empty `misc` config, that every `misc` rule shipped `enabled: false` defaults to off in code, and that `--update-config` adds the rules as disabled. SIT-027 and SITC-017 updated; 1463 tests PASS |

---

## 8. Metrics

| Metric | Measurement | Frequency |
|---|---|---|
| Open CRs | GitHub Issues count by CR-type labels | Weekly |
| CRs accepted per release | Count of closed CR Issues per release tag | Per release |
| Mean CR cycle time | Days from Issue open to PR merge | Per release |
| CRs that required document updates | Count of CRs with ASPICE document changes | Per release |

---

## 9. Review & Approval

| Role | Name | Signature / Electronic Approval | Date |
|---|---|---|---|
| Author | Claude | Approved | 2026-09-29 |
| Technical Reviewer | Dermot Murphy | — | *pending* |
| Quality Assurance | Dermot Murphy | — | *pending* |
| Approver | Dermot Murphy | — | *pending* |

> **Note:** This document is under configuration management (SUP.8). Post-approval changes require a change request (SUP.10) and a new document version.
