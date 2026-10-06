# Change Request Management Plan

*Automotive SPICE® PAM v4.0 | SUP.10 Change Request Management*

---

## 1. Document Identification & Control

| Field | Value | Field | Value |
|---|---|---|---|
| **Document ID** | CSC-SUP10-001 | **Version** | 1.18 |
| **Project** | CStyleCheck | **Date** | 2026-10-06 |
| **Status** | Released | **Classification** | Internal |
| **Author** | Claude | **Reviewer** | Dermot Murphy |
| **Approver** | Dermot Murphy | **Related Process** | SUP.10 |

---

## 2. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.18 | 2026-10-06 | Claude | Cross-reference version resync after the v1.6.1 hotfix back-merge (#444): referenced-document versions set to the current baseline; no technical content change |
| 1.17 | 2026-10-05 | Claude | Issue #441: §7 register row and §7.1 record CR-441 (create missing parent folders of `--log`, `--write-baseline` and `--init-output` files; Medium; backwards compatible) |
| 1.16 | 2026-09-30 | Claude | Merge-time process controls (#437): §5.1 CRs raised with the CR issue form (`.github/ISSUE_TEMPLATE/change_request.yml`); §5.2 impact analysis recorded on the issue before the implementing PR is merged; §5.4 CI list names `cstylecheck_rules.yml` and `aspice_consistency.yml`; referenced-document versions resynced; §6 CI-impact table rewritten against the current CSC-SUP8-001 §6.1 list (implementation is CI-045, not the CI-001 shim; all six workflows, Dependabot, CI scripts, process templates and CI-055 for ASPICE documents) |
| 1.15 | 2026-09-30 | Claude | Cross-reference version resync (#435): all referenced-document versions set to the current baseline (every controlled work product bumped once in this change set); no technical content change |
| 1.14 | 2026-09-29 | Claude | CSC-AUD-010 corrective actions (#430). AUD10-F-001: §7 register rows and §7.1 records for CR-412, CR-420, CR-422, CR-424 and CR-425. AUD10-F-002: new §7.2 release-classification decision (next release v2.0.0, Major). AUD10-F-010: CR-418 impact superseded by CR-420; CR-413 and CR-418 set to Closed with PR and merge commit. AUD10-F-015: §5.4 branch table allows `claude/<topic>-<id>`; approval-by-merge policy (CSC-DEV-002 §5.2) |
| 1.13 | 2026-09-29 | Claude | Cross-reference resync with #423: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
| 1.12 | 2026-09-29 | Claude | Cross-reference resync with #425: 3 referenced-document version(s) updated to current (SVD excluded; updated at release) |
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
| CSC-SUP8-001 | Configuration Management Plan | 1.26 |
| CSC-SUP9-001 | Problem Resolution Management Plan | 1.16 |
| CSC-MAN3-001 | Project Management Plan | 1.22 |

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
| **High** | Changes architecture, adds/removes requirements, breaks backwards compatibility | Peer review + explicit QA sign-off (given by the owner's merge of the implementing PR; CSC-DEV-002 §5.2) |

---

## 5. Change Request Process

### 5.1 Raising a Change Request

All change requests are raised as **GitHub Issues** with the `enhancement`, `improvement`, `documentation`, `config-change`, or `process-change` label. Change requests are raised with the CR issue form `.github/ISSUE_TEMPLATE/change_request.yml` (CSC-SUP8-001 CI-064, #437), which applies the `[CR] ` title prefix and the `enhancement` label and makes the description and rationale, impact level (§4.2), affected requirements / work products, backwards compatibility (No ⇒ Major release, §5.6) and target release mandatory; the maintainer adjusts the type label (§4.1) at evaluation.

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
5. Record evaluation outcome in the Issue comment thread. The impact analysis is recorded on the issue before the implementing PR is merged; the PR template checklist (CSC-SUP1-001 §5.3) confirms that the CR is registered in §7 for configuration or behaviour changes

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
| New feature or enhancement | `feature/<issue-id>-<description>` or `claude/<topic>-<id>` | `develop` |
| Configuration or documentation | `feature/<issue-id>-<description>` or `claude/<topic>-<id>` | `develop` |
| Urgent backwards-compatible fix affecting released version | `hotfix/<issue-id>-<description>` | `main` and `develop` |

Commit messages must reference the Issue: `Implements #<issue-id>: <description>`

All implementing PRs must:
- Pass CI (`cstylecheck_tests.yml`, `cstylecheck_rules.yml`, `aspice_consistency.yml`)
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

| CR Type | Likely Affected CIs (per CSC-SUP8-001 §6.1) |
|---|---|
| New rule | CI-045 (checker package `src/cstylecheck/`), CI-003 (`src/rules.yml`), CI-018 (`tests/rules.yml`), CI-017 (test suite), CI-026 (README), CI-049 (`Rules-and-Configuration.md`), CI-047 (CHANGELOG), CI-055 (ASPICE work products: SWE1–SWE6, SYS2–SYS5) |
| New CLI flag | CI-045, CI-001 (`src/cstylecheck.py` entry-point shim, if the entry point changes), CI-004 (`src/options.txt`), CI-013 (`pyproject.toml`), CI-016 (`action.yml`), CI-015 (`.pre-commit-hooks.yml`), CI-026, CI-047, CI-055 |
| New output format | CI-045, CI-016 (`action.yml`), CI-026, CI-047, CI-055 |
| Config file change | CI-003 to CI-010, CI-050 (`src/project.defines`), CI-018; CI-045 when the loader or validation changes |
| CI workflow change | CI-023, CI-024, CI-025, CI-034, CI-038 and CI-062 (`.github/workflows/*.yml`); CI-046 (`.github/dependabot.yml`); scripts CI-029 to CI-031, CI-035, CI-036, CI-039 to CI-043, CI-061; CSC-ACQ4-001 when a third-party action changes |
| Process template change | CI-063 (PR template), CI-064 (issue forms), with the plan that defines them (CSC-SUP1-001, CSC-SUP9-001, this plan) |
| ASPICE document update | CI-055 (the affected work product, identified by its CSC document ID and version) + a new revision entry in its §2; cross-references resynced with `python scripts/aspice_check.py --fix-citations` (CI-061) |

All affected CIs must be updated within the same Git Flow branch as the implementing change (or in an explicitly linked follow-up Issue tracked to the same release).

---

## 7. Change Request Register

The GitHub Issues board at `https://github.com/dermot-murphy/CStyleCheck/issues` serves as the CR register. Filter by enhancement/improvement/documentation/config-change/process-change labels.

Summary view:

| Issue # | Type | Title | Impact | Status | Target Release |
|---|---|---|---|---|---|
| \<Auto-populated from GitHub Issues — see Issues board\> | | | | | |
| #412 | `bug`, `config-change` | Make `misc.boolean_comparison` opt-in and lowercase-only | Medium | Closed — PR #417, merge `eaa4b87` | v2.0.0 |
| #413 | `documentation` | [CR] Align startup-banner requirements SYS-F-046 and SWE1-094 with the implementation | Medium | Closed — PR #415, merge `5533d16` | v2.0.0 |
| #418 | `config-change` | [CR] New-rule opt-in policy: the 7 remaining post-v1.6.0 MISRA/Barr-C rules disabled by default | High | Closed — PR #419, merge `d247396` | v2.0.0 |
| #420 | `enhancement`, `config-change` | Presets and `--init` enable the standard-specific opt-in rules | Medium | Closed — PR #421, merge `29c1241` | v2.0.0 |
| #422 | `bug`, `config-change` | Normalise case-style aliases and reject unknown case-style names | High | Closed — PR #426, merge `e2555f0` | v2.0.0 |
| #424 | `bug`, `config-change` | Remove unused `functions.case`; warn when a config still sets it | Medium | Closed — PR #427, merge `31acd91` | v2.0.0 |
| #425 | `bug` | Config and usage errors exit 2 from the installed `cstylecheck` command | High | Closed — PR #428, merge `7ddf732` | v2.0.0 |
| #441 | `enhancement` | [CR] Create the parent folder of output files (`--log`, `--write-baseline`, `--init-output`) if it does not exist | Medium | Open — PR #442 | v2.0.0 |

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
| **Impact on behaviour** | With a project config that does not set `enabled: true` for these rules (the 7 rules no longer report violations. Upgrading therefore adds no new findings to an existing project. *Superseded in part by CR-420:* configs written by `--init` or `--preset` now enable the opt-in rules that belong to the selected standard, so those configs do report them. Projects that want the rules set `misc.<rule>.enabled: true`. Detection logic, rule IDs, severities and messages are unchanged |
| **Rationale** | `misc.boolean_comparison`, when on by default, produced 433 new warnings on a reference project (#412). Turning on new rules by default on upgrade has the same risk for the other 7 rules. Opt-in keeps upgrades stable and lets each project adopt a rule when it is ready |
| **Impact on code** | `src/cstylecheck/checker.py` (7 `enabled` defaults), `src/rules.yml`, `tests/rules.yml`, `examples/embedded_project/config/strict.yml` |
| **Affected documents** | CSC-SWE1-001 v2.14, CSC-SWE3-001 v1.24, CSC-SWE4-001 v1.29, CSC-SWE5-001 v1.20, CSC-SWE6-001 v1.23, CSC-SYS4-001 v1.17, CSC-SYS5-001 v1.14, CSC-PA2-001 v1.28, CSC-MAN3-001 v1.13, CONTRIBUTING, README, Rules-and-Configuration, CHANGELOG |
| **Verification** | 11 tests added to `tests/test_misra_rules.py` (UV-MSR-009): one key-absent test per rule, plus policy tests. The policy tests check that all 8 opt-in rules ship disabled, that none fires with an empty `misc` config, that every `misc` rule shipped `enabled: false` defaults to off in code, and that `--update-config` adds the rules as disabled. SIT-027 and SITC-017 updated; 1463 tests PASS |

| Field | CR-412 |
|---|---|
| **Issue / PR** | [#412](https://github.com/dermot-murphy/CStyleCheck/issues/412) / PR #417 (merge `eaa4b87`) |
| **Date** | 2026-09-29 |
| **Raised by / implemented by** | Dermot Murphy / Claude |
| **Type** | `bug`, `config-change` — default-configuration and requirement change |
| **Impact level** | Medium — changes several CIs (`checker.py`, `src/rules.yml`, `tests/rules.yml`) and modifies one requirement (SWE1-115), see §5.3. Not High: the rule had not been released (added after v1.6.0), so no released behaviour or config becomes incompatible |
| **Affected work products** | SWE1-115; CSC-SWE3-001, CSC-SWE4-001, CSC-SYS4-001, CHANGELOG, Rules-and-Configuration |
| **Impact analysis** | `misc.boolean_comparison` ships `enabled: false` and only flags lowercase `true`/`false`. On the reference project the rule, on by default, raised 433 warnings; after the change an upgrade adds no findings unless the project enables the rule. Rule ID, severity and message unchanged |
| **Verification** | Tests added to `tests/test_misra_rules.py`; test total 1444→1452 |
| **Approval** | Approved by owner merge of PR #417 |
| **Status / target release** | Closed / v2.0.0 |

| Field | CR-420 |
|---|---|
| **Issue / PR** | [#420](https://github.com/dermot-murphy/CStyleCheck/issues/420) / PR #421 (merge `29c1241`) |
| **Date** | 2026-09-29 |
| **Raised by / implemented by** | Dermot Murphy / Claude |
| **Type** | `enhancement`, `config-change` |
| **Impact level** | Medium — changes one CI (`wizard.py`) and the `--init` / `--preset` output interface, with a minor requirement change (SWE1-075). Not High: existing configs are not affected; only newly generated configs differ |
| **Affected work products** | SWE1-075; CSC-SWE3-001, CSC-SWE4-001, CSC-SWE5-001 (SIT-016), CSC-SYS4-001, README, CHANGELOG |
| **Impact analysis** | The `misra` and `barr-c` presets and the `--init` wizard (new MISRA C:2012 / Barr-C questions, default No) now write `enabled: true` for the opt-in rules of the selected standard. Supersedes the CR-418 statement that preset/`--init` configs report none of the opt-in rules. A config regenerated after upgrade can report findings that the v1.6.0-generated config did not |
| **Verification** | Tests added to `tests/test_init_wizard.py`; SIT-016 steps 4–5; test total 1463→1481 |
| **Approval** | Approved by owner merge of PR #421 |
| **Status / target release** | Closed / v2.0.0 |

| Field | CR-422 |
|---|---|
| **Issue / PR** | [#422](https://github.com/dermot-murphy/CStyleCheck/issues/422) / PR #426 (merge `e2555f0`) |
| **Date** | 2026-09-29 |
| **Raised by / implemented by** | Dermot Murphy / Claude |
| **Type** | `bug`, `config-change` — requirement and configuration-format change |
| **Impact level** | High — breaks backwards compatibility (§4.2): a config with a case-style value that is not a canonical name or known alias, which v1.6.0 loaded, is now rejected with exit 2. The barr-c preset typedef/enum case values change to canonical names |
| **Affected work products** | SWE1-001, SWE1-002; CSC-SWE2-001, CSC-SWE3-001 (UNIT-05), CSC-SWE4-001, CSC-SYS4-001, CSC-SYS5-001, Rules-and-Configuration, CHANGELOG (⚠️ note) |
| **Impact analysis** | `load_config()` normalises aliases to canonical case names and reports every unknown case-style value as a configuration error. Projects with a misspelt or unsupported value must correct the config on upgrade. Presets and the wizard write canonical names. Drives the Major release classification (§7.2) |
| **Verification** | `tests/test_case_style_config.py`; test total 1481→1508 |
| **Approval** | Approved by owner merge of PR #426 (owner decision 2026-09-29 accepts the incompatibility for v2.0.0; QA sign-off given by the owner's merge of PR #426, approval-by-merge policy of 2026-09-29, CSC-DEV-002 §5.2) |
| **Status / target release** | Closed / v2.0.0 |

| Field | CR-424 |
|---|---|
| **Issue / PR** | [#424](https://github.com/dermot-murphy/CStyleCheck/issues/424) / PR #427 (merge `31acd91`) |
| **Date** | 2026-09-29 |
| **Raised by / implemented by** | Dermot Murphy / Claude |
| **Type** | `bug`, `config-change` — configuration key removed |
| **Impact level** | Medium — changes several CIs (`config.py`, `wizard.py`, `__init__.py`) and two requirements (SWE1-001, SWE1-032). Not High: `functions.case` never had an effect, so no check result changes and a config that still sets it loads with a WARNING, not an error |
| **Affected work products** | SWE1-001, SWE1-032; CSC-SWE3-001, CSC-SWE4-001, CSC-SYS4-001, Rules-and-Configuration, CHANGELOG |
| **Impact analysis** | The unused `functions.case` key is removed from shipped configs, presets and the wizard; a config that sets it gets a deprecation WARNING on stderr. Function-name casing is controlled by `functions.style` only. Findings and exit codes are unchanged |
| **Verification** | `tests/test_functions_case_removed.py`; test total 1508→1524 |
| **Approval** | Approved by owner merge of PR #427 |
| **Status / target release** | Closed / v2.0.0 |

| Field | CR-425 |
|---|---|
| **Issue / PR** | [#425](https://github.com/dermot-murphy/CStyleCheck/issues/425) / PR #428 (merge `7ddf732`) |
| **Date** | 2026-09-29 |
| **Raised by / implemented by** | Dermot Murphy / Claude |
| **Type** | `bug` — exit-code interface change (SUP.9 SEV-2) handled under this plan for change control |
| **Impact level** | High — breaks backwards compatibility (§4.2): configuration and usage errors from the installed `cstylecheck` command now exit 2 instead of 1, so CI scripts that tested for 1 behave differently |
| **Affected work products** | SWE1-069; CSC-SWE3-001 (UNIT-136 `config_error`), CSC-SWE4-001, CSC-SYS4-001, CSC-SYS5-001, README, CHANGELOG (⚠️ note) |
| **Impact analysis** | `sys.exit("message")` calls replaced by `config_error()` (exit 2) in `config.py`, `cli.py`, `baseline.py`, `utils.py` and the `src/cstylecheck.py` wrapper, so both entry points match SYS-F-039. Exit codes 0 and 1 for checking are unchanged. Drives the Major release classification (§7.2) |
| **Verification** | `tests/test_exit_code_entry_points.py`; test total 1524→1532 |
| **Approval** | Approved by owner merge of PR #428 (QA sign-off given by the owner's merge of PR #428, approval-by-merge policy of 2026-09-29, CSC-DEV-002 §5.2) |
| **Status / target release** | Closed / v2.0.0 |

| Field | CR-441 |
|---|---|
| **Issue / PR** | [#441](https://github.com/dermot-murphy/CStyleCheck/issues/441) / PR #442 |
| **Date** | 2026-10-05 |
| **Raised by / implemented by** | Dermot Murphy / Claude |
| **Type** | `enhancement` |
| **Impact level** | Medium — changes three CIs' units (`cli.py` `main()`, `baseline.py` `write_baseline()`, `wizard.py` `run_wizard()` / `run_preset()`) plus a shared helper in `utils.py`, with a minor requirement change (SWE1-062, SWE1-065, SWE1-075). Not High: no requirement added or removed, and no backwards-compatibility break |
| **Affected work products** | SWE1-062, SWE1-065, SWE1-075; CSC-SWE1-001, CSC-SWE3-001 (new UNIT-137, UNIT-138), CSC-SWE4-001 (§5.22, UV-OUT-001 to UV-OUT-004), README, CHANGELOG |
| **Impact analysis** | `--log`, `--write-baseline` and `--init-output` now create missing parent folders of the output file, so callers no longer need `mkdir -p` first. A run that succeeds today behaves the same; only runs that failed with a missing-folder configuration error now succeed. A folder that cannot be created is still a configuration error (exit 2). `--init` / `--preset` with an unwritable output path now exit 2 with a message instead of a traceback (exit 1). No impact on SIT, SWQ or SYS-VTC procedures, which write into existing folders |
| **Verification** | 11 tests in `tests/test_output_dirs.py`; test total 1546→1557 |
| **Approval** | Approved by owner merge of the implementing PR |
| **Status / target release** | Open / v2.0.0 |

### 7.2 Release Classification Decision

| Field | Value |
|---|---|
| **Decision** | The next release is **v2.0.0 (Major)** |
| **Decided by / date** | Dermot Murphy, 2026-09-29 (CSC-AUD-010 AUD10-F-002, #430) |
| **Rationale** | §5.6 requires a Major version for changed default behaviour or an incompatible config format. CR-422 rejects configs that v1.6.0 loaded, and CR-425 changes the configuration-error exit code of the installed command from 1 to 2 |
| **Compatibility changes in scope** | CR-422 (config rejection, canonical case names), CR-425 (exit code 1→2), #423 (last enum member now checked; new findings possible), CR-420 (preset / `--init` output enables opt-in rules), CR-424 (`functions.case` removed, WARNING), CR-412 / CR-418 (post-v1.6.0 rules opt-in) |
| **Record** | CSC-MAN3-001 §8; CHANGELOG [Unreleased] ⚠️ notes |

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
| Technical Reviewer | Dermot Murphy | By merge (CSC-DEV-002 §5.2) | On PR merge |
| Quality Assurance | Dermot Murphy | By merge (CSC-DEV-002 §5.2) | On PR merge |
| Approver | Dermot Murphy | By merge (CSC-DEV-002 §5.2) | On PR merge |

> Approval is given by the owner's merge of the pull request that introduces this revision; the merge commit is the approval record (CSC-DEV-002 §5.2).

> **Note:** This document is under configuration management (SUP.8). Post-approval changes require a change request (SUP.10) and a new document version.
