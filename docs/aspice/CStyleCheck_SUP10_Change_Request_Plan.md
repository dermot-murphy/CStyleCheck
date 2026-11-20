# Change Request Management Plan

*Automotive SPICE® PAM v4.0 | SUP.10 Change Request Management*

---

## 1. Document Identification & Control

| Field | Value | Field | Value |
|---|---|---|---|
| **Document ID** | CSC-SUP10-001 | **Version** | 1.26 |
| **Project** | CStyleCheck | **Date** | 2026-11-20 |
| **Status** | Released | **Classification** | Internal |
| **Author** | Claude | **Reviewer** | Dermot Murphy |
| **Approver** | Dermot Murphy | **Related Process** | SUP.10 |

---

## 2. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.26 | 2026-11-20 | Claude | v2.0.0 release (CR #443): §7 register row and §7.1 record CR-443 (release v2.0.0, Major; High); CR-461 and CR-462 closed (PR #464, merge `153d5d1`); §7.2 record cites CR-443; referenced-document versions resynced; approval by merge (CSC-DEV-002 §5.2) |
| 1.25 | 2026-11-19 | Claude | Review fixes for #460 to #463 (`783b5a4`): CR-461 record — `definition_paths` read even from a disabled rule, files sorted within each glob, `--definitions` warning, `#define` precedence (plain over `#ifndef` default, project table over a file's own `#define`s, top-level `#undef`), new units `collect_macro_defs` / `MacroTable`, pre-scan time 66 s → 26 s, verification 7 tests; CR-462 record — typedef alias of an undefined struct reported, `#define`d type not, verification 6 tests |
| 1.24 | 2026-11-19 | Claude | Issues #461 and #462: §7 register rows and §7.1 records CR-461 (definition files for `misc.partial_struct_*`: `definition_paths`, `--definitions GLOB`; new requirement SWE1-121; Medium; backwards compatible) and CR-462 (`report_unknown_types`; new requirement SWE1-122; Low; backwards compatible); the companion problem reports #460 and #463 are in CSC-SUP9-001 §6.2; referenced-document versions resynced |
| 1.23 | 2026-11-19 | Claude | Issue #458: §7 register and §7.1 records — CR-441 (PR #442, merge `81b6f2e`) and CR-456 (PR #457, merge `d97c0b2`) set to Closed |
| 1.22 | 2026-11-19 | Claude | Issue #456: §7 register row and §7.1 record CR-456 (two opt-in rules for partially initialised local structs, `misc.partial_struct_assignment` and `misc.partial_struct_initialiser`; new requirements SWE1-118 to SWE1-120; Medium; disabled by default, no compatibility impact) |
| 1.21 | 2026-11-19 | Claude | Cross-reference version resync with #453 (CSC-SUP8-001 §7.1/§7.5 ruleset wording) |
| 1.20 | 2026-11-19 | Claude | Issue #449: §6 CI-impact table — CI workflow scripts are CI-029 and CI-030 (CI-031 retired); referenced-document versions resynced |
| 1.19 | 2026-10-06 | Claude | Cross-reference version resync with #447: referenced-document versions set to the current baseline; no technical content change |
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
| CSC-SUP8-001 | Configuration Management Plan | 1.35 |
| CSC-SUP9-001 | Problem Resolution Management Plan | 1.24 |
| CSC-MAN3-001 | Project Management Plan | 1.30 |

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
| CI workflow change | CI-023, CI-024, CI-025, CI-034, CI-038 and CI-062 (`.github/workflows/*.yml`); CI-046 (`.github/dependabot.yml`); scripts CI-029, CI-030, CI-035, CI-036, CI-039 to CI-043, CI-061; CSC-ACQ4-001 when a third-party action changes |
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
| #441 | `enhancement` | [CR] Create the parent folder of output files (`--log`, `--write-baseline`, `--init-output`) if it does not exist | Medium | Closed — PR #442, merge `81b6f2e` | v2.0.0 |
| #456 | `enhancement` | [CR] Opt-in rules for partially initialised local structs (`misc.partial_struct_assignment`, `misc.partial_struct_initialiser`) | Medium | Closed — PR [#457](https://github.com/dermot-murphy/CStyleCheck/pull/457), merge `d97c0b2` | v2.0.0 |
| #461 | `enhancement` | [CR] `misc.partial_struct_*`: read struct definitions from excluded paths (e.g. vendor SDK headers) | Medium | Closed — PR [#464](https://github.com/dermot-murphy/CStyleCheck/pull/464), merge `153d5d1` | v2.0.0 |
| #462 | `enhancement` | [CR] `misc.partial_struct_*`: optionally report locals whose struct type is unknown | Low | Closed — PR [#464](https://github.com/dermot-murphy/CStyleCheck/pull/464), merge `153d5d1` | v2.0.0 |
| #443 | `enhancement` | [CR] Release v2.0.0: merge develop to main through release/2.0.0 | High | Implemented — release PR `release/2.0.0` → `main` | v2.0.0 |

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
| **Status / target release** | Closed / v2.0.0 |

| Field | CR-456 |
|---|---|
| **Issue / PR** | [#456](https://github.com/dermot-murphy/CStyleCheck/issues/456) / [#457](https://github.com/dermot-murphy/CStyleCheck/pull/457) |
| **Date** | 2026-11-19 |
| **Raised by / implemented by** | Dermot Murphy / Claude |
| **Type** | `enhancement` — two new rules and new requirements |
| **Impact level** | Medium — changes CIs `checker.py` (new module-level struct-definition table functions and four `Checker` methods), `cli.py` (`main()` struct-definition pre-pass), `wizard.py` (presets and `--init`), `src/rules.yml` and `tests/rules.yml`, and adds requirements SWE1-118 to SWE1-120 with a minor change to SWE1-075 and SYS-F-011 / SYS-F-020. Not High: both rules ship `enabled: false` and are disabled when the key is absent (CR-418 policy), so an existing project gets no new findings and no backwards-compatibility break |
| **Change** | `misc.partial_struct_assignment` (warning) flags a non-static local struct without an initialiser that has only some members assigned before its first use as a whole; `misc.partial_struct_initialiser` (info) flags a local struct whose positional brace initialiser lists fewer values than members. The member lists come from the struct definitions of every scanned file, collected by the CLI before the per-file checks when either rule is enabled or `--per-dir-config` is used. `--preset misra` enables both rules, `--preset barr-c` enables `misc.partial_struct_assignment`; the `--init` wizard lists them with the other opt-in rules. The sample profile `examples/embedded_project/config/strict.yml` enables both |
| **Rationale** | A partly assigned local struct passes indeterminate stack data to the callee (MISRA C:2012 Rule 9.1, Barr-C §7.2); a short positional initialiser hides whether the missing values were intended (cf. MISRA C:2012 Rule 9.3) |
| **Affected work products** | SYS-F-011, SYS-F-020, SWE1-075, SWE1-118 to SWE1-120; CSC-SYS2-001 v2.22, CSC-SYS3-001 v1.24, CSC-SWE1-001 v2.29, CSC-SWE2-001 v1.33 (SWA-IF-11), CSC-SWE3-001 v1.39 (UNIT-139 to UNIT-145), CSC-SWE4-001 v1.44 (§5.24, UV-PSI-001 to UV-PSI-005), CSC-SWE5-001 v1.33 (SIT-028), CSC-SWE6-001 v1.36, CSC-SYS4-001 v1.30 (SITC-018), CSC-SYS5-001 v1.27, CSC-STD-001 v1.21, README, Rules-and-Configuration, CHANGELOG, `examples/embedded_project` |
| **Impact analysis** | With the default configuration nothing changes. When either rule is enabled, every scanned file is read once before checking (the content is cached and reused, so each file is still read once, SYS-F-010). Struct types whose definition is not in a scanned file are not checked; order is lexical (no control-flow analysis). Configs regenerated with `--preset misra` / `--preset barr-c` or `--init` (standard question answered yes) enable the new rules and can report findings, as for CR-420 |
| **Verification** | New module `tests/test_partial_struct.py` (54 tests) and 2 key-absent tests in `tests/test_misra_rules.py` (UV-MSR-009); `tests/test_init_wizard.py` preset / wizard tests cover the new rules; SIT-028, SITC-018; test total 1574→1630 |
| **Approval** | By merge (CSC-DEV-002 §5.2) — owner merge of the implementing PR |
| **Status / target release** | Closed / v2.0.0 |

| Field | CR-461 |
|---|---|
| **Issue / PR** | [#461](https://github.com/dermot-murphy/CStyleCheck/issues/461) / PR [#464](https://github.com/dermot-murphy/CStyleCheck/pull/464) (shared with #460, #462, #463), merge `153d5d1` |
| **Date** | 2026-11-19 |
| **Raised by / implemented by** | Dermot Murphy / Claude |
| **Type** | `enhancement` — new rule key, new CLI option and a new requirement |
| **Impact level** | Medium — changes CIs `checker.py` (new module-level functions `struct_definition_paths`, `clean_for_struct_scan`, `collect_macro_defs`, `collect_macros`, `collect_typedef_names` and class `MacroTable`; `Checker.__init__` gains `macros=` and `type_names=`), `cli.py` (`--definitions GLOB`; the `main()` pre-pass reads definition files), `src/rules.yml` and `tests/rules.yml` (`definition_paths: []` on both rules), and adds requirement SWE1-121 with minor changes to SWE1-120 and SYS-F-020; SWA-IF-11 carries more data. Not High: the key defaults to an empty list and the option is new, so an existing configuration behaves as before |
| **Change** | `misc.partial_struct_assignment` and `misc.partial_struct_initialiser` take `definition_paths` (globs relative to the working directory; the lists of both rules are joined, read even when a rule is disabled in the root configuration so that per-directory configurations can enable it), and the repeatable `--definitions GLOB` adds more; with neither rule enabled, `--definitions` is ignored with a `WARNING`. These **definition files** are read only for struct, typedef and `#define` definitions: they are never checked or reported on, and `--exclude` does not apply to them. Precedence: checked files first, then definition files in the order listed (sorted within each glob); a struct definition from a definition file never replaces one from a checked file or an earlier definition file. `#define`s form one project-wide table (#463): a plain `#define` (top level or inside an include guard) beats an `#ifndef X` / `#define X` default, the first file in precedence order wins within a kind, `#define`s under any other conditional are not used, a top-level `#undef` drops the name, and the table beats a file's own `#define`s, so a checked `sdk_config.h` beats an SDK header's default. Only the root configuration's `definition_paths` are used |
| **Rationale** | Projects exclude vendor SDK code from checking, but the local structs most often set member by member are SDK configuration structs (nRF `nrfx_spim_config_t`, STM32 HAL `*_InitTypeDef`); without their definitions the rule checks nothing. On a downstream nRF52840 project (228 files, nRF5 SDK 17.1.0 headers given as `definition_paths`) the rule now reports two local `nrfx_spim_config_t` structs with 10 of 14 members assigned (`dcx_pin`, `rx_delay`, `use_hw_ss` and `ss_duration` missing), which it missed before |
| **Affected work products** | SYS-F-020, SWE1-120, SWE1-121; CSC-SYS2-001 v2.24, CSC-SWE1-001 v2.31, CSC-SWE2-001 v1.35 (SWA-IF-11), CSC-SWE3-001 v1.41 (UNIT-46, UNIT-88, UNIT-150, UNIT-151), CSC-SWE4-001 v1.46 (UV-PSI-007), CSC-SWE5-001 v1.35 (SIT-028), CSC-SWE6-001 v1.38, CSC-SYS4-001 v1.32 (SITC-018), CSC-SYS5-001 v1.29, README, Rules-and-Configuration, CHANGELOG |
| **Impact analysis** | With no definition files nothing changes. With them, each definition file is read once per run in addition to the checked files (no source cache entry, as it is never checked); on a downstream project the pre-scan of 228 checked files and 1002 SDK headers took 26 s after the review fixes (66 s before: the macro table is no longer copied per file); a broad glob over a whole SDK costs read time and can pick up SDK example `sdk_config.h` files whose `#define`s then win, so the documentation advises listing the project's configuration headers first and keeping SDK globs narrow. Per-directory configurations do not add definition files (a known limitation, documented). More structs become known, so enabling the option can report findings that were silently skipped before — the purpose of the change. No impact on SIT, SWQ or SYS-VTC procedures beyond the new SIT-028 / SITC-018 steps |
| **Verification** | `tests/test_partial_struct.py` UV-PSI-007 `TestDefinitionPaths` (7 tests) and UV-PSI-009 `TestMacroCollection` (11 tests, `#define` precedence); SIT-028 steps 7 to 9, 11 and 12, SITC-018 steps 5 and 6; test total 1630→1671 with #460, #462 and #463 |
| **Approval** | By merge (CSC-DEV-002 §5.2) — owner merge of the implementing PR |
| **Status / target release** | Closed / v2.0.0 |

| Field | CR-462 |
|---|---|
| **Issue / PR** | [#462](https://github.com/dermot-murphy/CStyleCheck/issues/462) / PR [#464](https://github.com/dermot-murphy/CStyleCheck/pull/464) (shared with #460, #461, #463), merge `153d5d1` |
| **Date** | 2026-11-19 |
| **Raised by / implemented by** | Dermot Murphy / Claude |
| **Type** | `enhancement` — new rule key and a new requirement |
| **Impact level** | Low — changes CI `checker.py` (`Checker._is_unknown_struct_type`, `Checker._report_unknown_type`, `_STD_SCALAR_TYPES`, `_iter_local_struct_decls(include_unknown=False)`, `collect_typedef_names`), `src/rules.yml` and `tests/rules.yml` (`report_unknown_types: false` on both rules), and adds requirement SWE1-122. The key defaults to `false`, so the output of an existing configuration does not change |
| **Change** | With `report_unknown_types: true`, `misc.partial_struct_assignment` and `misc.partial_struct_initialiser` give one `info` finding, under their own rule ID, for each local they could not check because its struct type has no definition: an explicit `struct tag`, a typedef alias of a struct with no definition (`typedef struct foo_s foo_t;`), or a name that is neither a typedef nor a `#define` found in the checked or definition files nor a standard type. The assignment rule reports non-static locals without an initialiser; the initialiser rule reports locals with a positional brace initialiser |
| **Rationale** | A run that skips every local of an unknown type reads as a clean result; the user cannot tell "fully initialised" from "never checked" (on a downstream nRF52840 project every SDK configuration struct was skipped this way, including one that really was partly initialised, see CR-461) |
| **Affected work products** | SYS-F-020, SWE1-122; CSC-SYS2-001 v2.24, CSC-SWE1-001 v2.31, CSC-SWE2-001 v1.35, CSC-SWE3-001 v1.41 (UNIT-143 to UNIT-145, UNIT-149, UNIT-152, UNIT-153), CSC-SWE4-001 v1.46 (UV-PSI-008), CSC-SWE5-001 v1.35 (SIT-028), CSC-SWE6-001 v1.38, CSC-SYS4-001 v1.32 (SITC-018), CSC-SYS5-001 v1.29, README, Rules-and-Configuration, CHANGELOG |
| **Impact analysis** | Default output unchanged. When enabled, the extra findings are `info` (they do not change the exit code unless `--warnings-as-errors` is used) and can be suppressed like any other finding (inline, `--exclusions`, baseline). A typedef name that is not a struct (enum, scalar, pointer typedef) is not reported when its typedef is in a checked or definition file; a project type defined only in an unscanned header is reported, which is the intent |
| **Verification** | `tests/test_partial_struct.py` UV-PSI-008 `TestReportUnknownTypes` (6 tests); SIT-028 step 10, SITC-018 step 7 |
| **Approval** | By merge (CSC-DEV-002 §5.2) — owner merge of the implementing PR |
| **Status / target release** | Closed / v2.0.0 |

| Field | CR-443 |
|---|---|
| **Issue / PR** | [#443](https://github.com/dermot-murphy/CStyleCheck/issues/443) / release PR `release/2.0.0` → `main` |
| **Date** | 2026-11-20 (scope question resolved 2026-10-06: #439 shipped alone as v1.6.1) |
| **Raised by / implemented by** | Dermot Murphy / Claude |
| **Type** | `enhancement` — release baseline (CSC-SUP8-001 §8.2) |
| **Impact level** | High — the release breaks backwards compatibility (§7.2): CR-422, CR-425, #423, CR-424, CR-412 / CR-418 / CR-420 |
| **Change** | Release **v2.0.0 (Major)** from `develop` through `release/2.0.0`: version bump (`pyproject.toml`), CHANGELOG `[Unreleased]` → `[2.0.0] - 2026-11-20`, README / DOCKERHUB_README / `action.yml` usage examples to `@v2.0.0`, ASPICE release records (CSC-SVD-001 v1.35, CSC-SUP8-001 v1.34 §8.4, CSC-SWE4-001 v1.48, CSC-SWE5-001 v1.37, CSC-SWE6-001 v1.40 §9, CSC-SYS4-001 v1.34, CSC-SYS5-001 v1.31, CSC-MAN3-001 v1.30, CSC-PA2-001 v1.45, CSC-SUP9-001 v1.24, this record); merge to `main`, back-merge to `develop`, annotated tag `v2.0.0` on the `main` merge commit |
| **Content** | All changes since v1.6.1 (CSC-SVD-001 §6.7): CR-412, CR-413, CR-418, CR-420, CR-422, CR-424, CR-425, CR-441, CR-456, CR-461, CR-462; problem fixes #408, #410, #423, #447, #460, #463 (CSC-SUP9-001 §6.2); #388, #394, #395, #437, #449; 83 rule IDs, 1671 tests |
| **Impact analysis** | Projects upgrading from v1.6.x can see new findings, a configuration error (exit 2) or a different exit code; the new rules are opt-in, so they add no findings by default. Upgrade steps are in CSC-SVD-001 §9.1 and the CHANGELOG ⚠️ Compatibility section; the GitHub Release lists the breaking changes in their own section |
| **Verification** | 1671 tests, 0 failures (local run on `release/2.0.0`, 2026-11-20); CI on the release PR (Python 3.10 / 3.11 / 3.12, naming-convention check, Docker build, ASPICE consistency) must pass before merge; release-readiness gate CSC-SWE6-001 §9; SYS.5 verdict CSC-SYS5-001 §6; after the tag, the action is run end to end with `--output-format json --log` (#439 regression) and the Docker publication is confirmed (CSC-SUP8-001 §11.2) |
| **Approval** | By merge (CSC-DEV-002 §5.2) — owner merge of the release PR |
| **Status / target release** | Implemented on `release/2.0.0`; closed when the release PR is merged and `v2.0.0` is tagged / v2.0.0 |

### 7.2 Release Classification Decision

| Field | Value |
|---|---|
| **Decision** | The next release is **v2.0.0 (Major)** |
| **Decided by / date** | Dermot Murphy, 2026-09-29 (CSC-AUD-010 AUD10-F-002, #430) |
| **Rationale** | §5.6 requires a Major version for changed default behaviour or an incompatible config format. CR-422 rejects configs that v1.6.0 loaded, and CR-425 changes the configuration-error exit code of the installed command from 1 to 2 |
| **Compatibility changes in scope** | CR-422 (config rejection, canonical case names), CR-425 (exit code 1→2), #423 (last enum member now checked; new findings possible), CR-420 (preset / `--init` output enables opt-in rules), CR-424 (`functions.case` removed, WARNING), CR-412 / CR-418 (post-v1.6.0 rules opt-in) |
| **Record** | CSC-MAN3-001 §8; CHANGELOG [2.0.0] ⚠️ Compatibility notes; released as v2.0.0 on 2026-11-20 under CR-443 |

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
| Author | Claude | Approved | 2026-11-20 |
| Technical Reviewer | Dermot Murphy | By merge (CSC-DEV-002 §5.2) | On PR merge |
| Quality Assurance | Dermot Murphy | By merge (CSC-DEV-002 §5.2) | On PR merge |
| Approver | Dermot Murphy | By merge (CSC-DEV-002 §5.2) | On PR merge |

> Approval is given by the owner's merge of the pull request that introduces this revision; the merge commit is the approval record (CSC-DEV-002 §5.2).

> **Note:** This document is under configuration management (SUP.8). Post-approval changes require a change request (SUP.10) and a new document version.
