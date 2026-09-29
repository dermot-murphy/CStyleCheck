# Contributing to CStyleCheck

Thank you for your interest in contributing to CStyleCheck.

## Reporting Issues

Use the [GitHub Issues](https://github.com/dermot-murphy/CStyleCheck/issues) tracker:

- **Bug reports**: label `bug` — include a minimal reproducing C file, your `.cstylecheck.yml`, and the version (`cstylecheck --version`).
- **Feature requests**: label `enhancement` — describe the Barr-C:2018 or MISRA-C rule being targeted and the expected behaviour.
- **Documentation issues**: label `documentation`.

## Pull Requests

1. Fork the repository and create a branch from `develop` (not `main`).
2. Follow the coding conventions enforced by CStyleCheck's own `rules.yml`:
   - Run `python src/cstylecheck.py --config src/rules.yml src/cstylecheck/` before pushing.
3. Add or update unit tests in `tests/` covering the changed behaviour.
4. Ensure CI passes: `pytest tests/ --tb=short`.
5. Open the PR against `develop`; include a reference to the relevant GitHub Issue.

## Code Style

CStyleCheck applies Barr-C:2018 and MISRA-C complementary naming conventions to its own source. The project's rule configuration is `src/rules.yml`. Any contribution must pass the self-check CI job (`cstylecheck_rules.yml`).

## New Rule Policy (opt-in)

New rules ship `enabled: false` and default to disabled when the key is absent; they may be enabled in presets.

In practice (issue #418):

- Add the rule to `src/rules.yml` **and** `tests/rules.yml` with `enabled: false`.
- Read the flag in the checker as `cfg.get("enabled", False)`, so a project config that
  predates the rule (or omits its key) keeps it off. `--update-config` then adds the key
  as `enabled: false`.
- Add an "off when key absent" test and an explicit-enable test. The policy tests in
  `tests/test_misra_rules.py` check that every `misc` rule shipped `enabled: false`
  also defaults to off in code.
- A rule may be switched on in a preset or a sample profile such as
  `examples/embedded_project/config/strict.yml`.
- A standard-specific opt-in rule (one that enforces a MISRA C or Barr-C rule) should
  also be added to the matching preset in `src/cstylecheck/wizard.py` (`misra` or
  `barr-c`, via `MISRA_OPT_IN_RULES` / `BARR_C_OPT_IN_RULES`) with its shipped default
  severity, so `--preset` and the `--init` wizard question for that standard enable it
  (issue #420). Style rules that belong to no standard (e.g. `misc.boolean_comparison`)
  stay out of the presets.

Upgrading CStyleCheck therefore never adds new findings to an existing project.
Users opt in to each new rule.

## AI Assistance Policy

This project uses AI tooling (Claude, Anthropic) as a development aid, documented in `docs/aspice/CStyleCheck_DEV001_AI_Authorship_Deviation.md`. Human review and approval of all AI-generated changes is required before merge (see `docs/aspice/CStyleCheck_DEV002_Independent_Review_Deviation.md`).

Contributors may also use AI assistance; however, the contributor is responsible for the correctness and style conformance of any AI-generated code submitted via PR.

## Licence

By contributing you agree that your contributions will be licensed under the [MIT Licence](LICENSE).
