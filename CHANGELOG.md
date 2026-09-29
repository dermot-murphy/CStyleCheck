# Changelog

All notable changes to CStyleCheck are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/).

---

## [Unreleased]

### Added

- **8 new MISRA C / Barr-C rules** (81 rule IDs in total), all **disabled by default** (opt-in; `enabled: false` in `src/rules.yml`, and off when the
  key is absent — #412, #418):
  - `misc.goto_usage` (error, disabled by default) — every `goto` (MISRA C:2012 Rule 15.1)
    ([#391](https://github.com/dermot-murphy/CStyleCheck/pull/391)).
  - `misc.assignment_in_condition` (warning, disabled by default) — `=` inside an `if`/`while` condition or a
    `for` condition clause (MISRA C:2012 Rule 13.4)
    ([#391](https://github.com/dermot-murphy/CStyleCheck/pull/391)).
  - `misc.multiple_statements_per_line` (warning, disabled by default) — more than one statement on a line;
    `for` headers exempt (Barr-C §3.2).
  - `misc.void_pointer` (warning, disabled by default) — `void *` usage (MISRA C:2012 Rule 11.5).
  - `misc.recursive_function` (error, disabled by default) — direct recursion (MISRA C:2012 Rule 17.2).
  - `misc.sizeof_type` (info, disabled by default) — `sizeof` applied to a type name instead of an object
    (Barr-C §5.7).
  - `misc.boolean_comparison` (warning, disabled by default) — `==`/`!=` against the
    lowercase `true`/`false` literals (style rule).
  - `misc.empty_else` (warning, disabled by default) — empty `else { }` block; a block containing a comment
    is accepted (Barr-C §8.3).

  The last six were added in [#392](https://github.com/dermot-murphy/CStyleCheck/pull/392).
  Projects upgrading with an existing `rules.yml` can add the new keys with
  `--update-config` (they are added as `enabled: false`). 76 new tests in `tests/test_misra_rules.py`.
- **Trend analysis — safety indicators** — `scripts/collect_metrics.py` records
  `assert_count`, `assert_density` (per KLOC SLOC), `goto_count`, `void_ptr_count`,
  `cast_count` (C-style casts) and `macro_count` (excluding include guards), counted on
  comment- and string-stripped text. `scripts/generate_charts.py` adds the
  `safety_indicators` and `macro_metrics` charts, and `scripts/update_wiki_metrics.py`
  adds snapshot rows for them
  ([#392](https://github.com/dermot-murphy/CStyleCheck/pull/392)).
- **Trend analysis — industry-standard C source code metrics** — `scripts/collect_metrics.py`
  now uses a comment/string-aware lexer (`strip_comments_and_strings()`, `classify_lines()`,
  `extract_functions()`, `count_file_scope_variables()`) so keywords, braces and calls inside
  comments or strings are never counted. New per-commit data-point fields (existing fields
  are unchanged; older data points without them still chart):
  `c_file_count`, `h_file_count`, `cc_bucket_1_5`, `cc_bucket_6_10`, `cc_bucket_11_15`,
  `cc_bucket_16_plus`, `dox_coverage_pct`, `global_vars`, `fanout_avg`,
  `recursive_func_count`, `violations_by_category`, `files_zero_violations`, `top_rules`.
  New charts in `scripts/generate_charts.py`: `cc_distribution` (stacked),
  `function_size`, `violations_by_category` (stacked), `documentation_coverage`,
  `coupling`; `loc_breakdown` is now a stacked-area LOC composition chart and
  `defect_density` plots defect density alone. `scripts/update_wiki_metrics.py` adds
  snapshot rows for the new metrics plus violations-by-category and top-5-rules tables;
  `scripts/compare_metrics.py` compares the new scalar metrics. Thresholds are documented
  in `scripts/metrics_rules.yml`
  (issue [#388](https://github.com/dermot-murphy/CStyleCheck/issues/388)).

### Changed

- **Presets enable the matching opt-in rules (#420)** — `--preset misra` now enables
  `misc.goto_usage` (MISRA C:2012 Rule 15.1), `misc.assignment_in_condition` (13.4),
  `misc.void_pointer` (11.5), `misc.recursive_function` (17.2) and `misc.empty_else`
  (related to 15.7); `--preset barr-c` enables `misc.multiple_statements_per_line` (§3.2),
  `misc.sizeof_type` (§5.7) and `misc.empty_else` (§8.3). `minimal` is unchanged and
  `misc.boolean_comparison` is in no preset. Severities are the shipped defaults. The
  `--init` wizard asks two new yes/no questions last (enable the MISRA C:2012 rules; enable
  the Barr-C rules), both defaulting to No; the generated config lists all seven rules with
  `enabled: true` only for the standard(s) answered yes. The `barr-c` preset's
  `typedefs.suffix` and `enums.type_suffix` are now written in the nested
  `{enabled, suffix}` form; the previous bare strings made the checker crash when the
  generated config was used. 18 new tests in `tests/test_init_wizard.py`; total 1463→1481
  (issue [#420](https://github.com/dermot-murphy/CStyleCheck/issues/420)).
- **New rules are opt-in (#418)** — `misc.goto_usage`, `misc.assignment_in_condition`,
  `misc.multiple_statements_per_line`, `misc.void_pointer`, `misc.recursive_function`,
  `misc.sizeof_type` and `misc.empty_else` now ship `enabled: false` in `src/rules.yml` and
  are disabled when their key is absent from a project config (the checker reads
  `cfg.get("enabled", False)`), as `misc.boolean_comparison` already was (#412). Upgrading
  therefore adds no new findings to an existing project. `--update-config` adds the keys as
  `enabled: false`. To use a rule, set `misc.<rule>.enabled: true`. The sample profile
  `examples/embedded_project/config/strict.yml` enables all 8. **Policy** (recorded in
  `CONTRIBUTING.md` and as CR-418 in SUP10): new rules ship `enabled: false` and default to
  disabled when the key is absent; they may be enabled in presets. 11 new tests in
  `tests/test_misra_rules.py`, including policy tests that fail if a rule shipped
  `enabled: false` defaults to on in code; total 1452→1463
  (issue [#418](https://github.com/dermot-murphy/CStyleCheck/issues/418)).
- **`misc.boolean_comparison` is opt-in and matches lowercase `true`/`false` only (#412)** —
  the rule is now disabled by default, including when the key is missing from a project
  config (`enabled: false` in `src/rules.yml`; the checker defaults to disabled). Enabled by
  default it produced 433 new warnings on a reference project. It also no longer matches
  `TRUE`/`FALSE` macros: comparing an integer flag against `TRUE` is not redundant
  (`if (flag)` and `if (TRUE == flag)` differ when `flag == 2`), so the suggested rewrite
  changed behaviour. Only the `<stdbool.h>` literals `true`/`false` are flagged. To keep the
  rule, set `misc.boolean_comparison.enabled: true`. 8 new tests in
  `tests/test_misra_rules.py` and one changed (`TRUE` no longer flagged); total 1444→1452
  (issue [#412](https://github.com/dermot-murphy/CStyleCheck/issues/412)).
- **Dependabot targets `develop`** — `.github/dependabot.yml` sets `target-branch: develop`
  for the `pip` and `github-actions` ecosystems (hotfix
  [#399](https://github.com/dermot-murphy/CStyleCheck/pull/399), back-merged in
  [#403](https://github.com/dermot-murphy/CStyleCheck/pull/403)). GitHub Actions updated:
  `actions/checkout@v7`, `actions/setup-python@v7`, `actions/upload-artifact@v7`,
  `docker/login-action@v4.6.0` (#386, #387, #400–#402, #404).
- **Trend metrics accuracy** — cyclomatic complexity no longer counts `do` separately from
  its `while`; `assert`/`goto`/`void *`/cast/macro counters ignore comments and strings;
  `func_over_params` threshold is now > 5 parameters (was > 6); function length is measured
  from the function-name line to the closing brace; static-variable counting handles
  multi-line and multi-declarator definitions. Expect a one-off step in these series
  (issue [#388](https://github.com/dermot-murphy/CStyleCheck/issues/388)).
- **Startup-banner requirements match the tool (documentation only)** — SYS-F-046 and SWE1-094
  now specify the existing behaviour: two lines on `stderr` (`CStyleCheck <version>`,
  `(C) 2026 Dermot Murphy`), also written to `--log`, emitted even when output is piped, not
  suppressible, never on `stdout`. The `--quiet`, date-time, file-count and non-TTY clauses are
  removed. SWE1-015 records the `--fix` header re-read exception. Change request CR-413; no
  code change; 5 new tests in `tests/test_cli_requirements.py` (total 1439→1444)
  (issue [#413](https://github.com/dermot-murphy/CStyleCheck/issues/413)).

### Removed

- **`functions.case` setting (#424)** — the `misra`, `barr-c` and `minimal` presets and
  the `--init` wizard wrote `functions.case`, and #422 validated it as a case-style key,
  but the checker never read it, so it had no effect. Function-name casing is set by
  `functions.style` (`object_verb`, `verb_object`, `lower_snake`, `any`). The key is no
  longer written by the presets or the wizard, and is removed from the
  `examples/embedded_project/config/*.yml` files, `scripts/metrics_rules.yml` and
  `Rules-and-Configuration.md`. `validate_case_styles()` no longer lists it as a
  case-style key (14 keys). A config (root or per-directory `.cstylecheck.yml`) that
  still contains `functions.case` loads normally with the same exit code, and prints one
  `WARNING` on `stderr` per config file saying the key is not used and to use
  `functions.style` instead. New helper `deprecated_key_warnings()`. 16 new tests in
  `tests/test_functions_case_removed.py`; total 1508→1524
  (issue [#424](https://github.com/dermot-murphy/CStyleCheck/issues/424)).

### Fixed

- **Unknown case-style names no longer pass silently (#422)** — `matches_case()`
  returned True for any style name it did not know, and the `barr-c` preset wrote
  `PascalCase` / `UPPER_SNAKE` while the `--init` wizard wrote `camelCase` /
  `PascalCase`, so naming checks configured that way never reported anything. The
  presets and the wizard now write only canonical names (`lower_snake`,
  `upper_snake`, `camel`, `pascal`); the wizard still shows the friendly labels, in
  the same order. The `barr-c` preset's `typedefs.case` and `enums.type_case` are now
  `lower_snake` (Barr-C §5.1.a): `pascal` cannot be satisfied together with the `_t`
  suffix. `load_config()` (and each per-directory `.cstylecheck.yml`) converts
  aliases such as `PascalCase`, `camelCase`, `UPPER_SNAKE`, `SCREAMING_SNAKE_CASE`
  and `snake_case` to the canonical name, ignoring letter case. `any` is accepted
  as an explicit "no case check" value. New helpers `normalize_case_style()` and
  `validate_case_styles()`; `matches_case()` raises `ValueError` for an unknown style.
  Valid names and aliases are listed in `Rules-and-Configuration.md`. 27 new tests in
  `tests/test_case_style_config.py`; total 1481→1508
  (issue [#422](https://github.com/dermot-murphy/CStyleCheck/issues/422)).

  > ⚠️ **Behaviour change:** projects that use a config generated by `--preset barr-c`
  > or the `--init` wizard (camelCase / PascalCase answer) will now get naming findings
  > (`typedef.case`, `enum.type_case`, `enum.member_case`, `variable.*.case`) that were
  > silently skipped before. An unknown case name in any case-style key (or in
  > `functions.style`, `file_prefix.case` or `misc.eof_comment.filename_case`) now stops
  > the run before any file is checked, with exit code `2` and a message naming the key
  > and the allowed values.
- **`misc.boolean_comparison` message citation (#410)** — the rule no longer cites
  MISRA C:2012 Rule 14.4. Rule 14.4 requires controlling expressions to be essentially
  Boolean, and `if (flag == true)` is compliant with it, so the citation overstated MISRA
  coverage. The rule is now a style rule; its message ends with
  "(redundant comparison with a Boolean literal)" instead of "(MISRA C:2012 Rule 14.4)".
  The `misc.yoda_condition` "Rule 14.4 (informative)" citation in the ASPICE documents
  was also removed as unrelated. Tools that match on the exact message text need updating.
- **`misc.multiple_statements_per_line` message citation (#408)** — the violation message
  no longer cites MISRA C:2012 Rule 15.5 (single point of exit), which is unrelated; it now
  cites Barr-C §3.2 only. Tools that match on the exact message text need updating.
- **Baseline matching ignores line numbers (#394)** — `--baseline-file` now matches
  on `(file, rule, message)` as a multiset instead of `file:line:rule:message`.
  Accepted violations stay suppressed when unrelated edits move them up or down the
  file. Each baseline entry suppresses at most one violation, so an extra copy of an
  accepted violation is still reported as new. The `line` field is still written for
  review. New helper `apply_baseline()`; `load_baseline()` now returns a
  `collections.Counter` instead of a `frozenset`.
- **Baseline paths are platform-independent (#395)** — baseline file paths are
  normalised to `/` separators (and `./` removed) when written, loaded and matched,
  so baselines written on Windows and Linux are interchangeable. Existing baselines
  containing backslashes are still honoured. New helper `_normalise_path()`.

### Tests

- **Unit tests for SWE1-015, SWE1-094 and SWE1-096 (#407)** — new module
  `tests/test_cli_requirements.py` (16 tests, UV-CLI-014 to UV-CLI-022) asserts that
  each source file is read from disk exactly once per run and shared by `Checker` and
  `SignChecker` (including a cross-file sign check), that the startup banner (tool name,
  version, copyright) goes to `stderr` and never to `stdout`, and that violation paths use
  the OS-native separator (both `\` and `/` behaviour, via `ntpath`/`posixpath`).
  Closes RR-003-001 (CSC-REVIEW-003) and AUD9-F-004 (CSC-AUD-009). Test total 1423→1439
  (issue [#407](https://github.com/dermot-murphy/CStyleCheck/issues/407)).

---

## [1.6.0] — 2026-07-06

### Added

- **`misc.constant_comparison` rule** — flags `==`/`!=` comparisons where **both** operands
  are compile-time constants (literals, `true`/`false`/`NULL`, ALL_CAPS identifiers).
  Distinguishes from `misc.yoda_condition` (which fires when one side is a variable).
  Exempt contexts: `#define` RHS, `return` statements
  (issue [#339](https://github.com/dermot-murphy/CStyleCheck/issues/339)).
- **`--fix` auto-fix support for `variable.pointer_prefix`** — renames a non-prefixed
  pointer parameter throughout the function scope (signature, body, and Doxygen
  `@param` block). For `.c` files also patches the matching `.h` declaration via
  `fix_pointer_prefix_in_header()`. Classified as a non-safe fix; only applied with
  `--fix`, not `--safe-only`
  (issue [#341](https://github.com/dermot-murphy/CStyleCheck/issues/341)).
- **Startup banner** — tool name, version, and copyright notice printed to `stderr`
  whenever CStyleCheck starts, regardless of other flags; also written to the log
  file when `--log` is used. Does not appear in stdout/pipeline output
  (issue [#369](https://github.com/dermot-murphy/CStyleCheck/issues/369)).
- **Copyright notice** — `(C) 2026 Dermot Murphy` appended after the version string in
  `--version` output and in the log file header
  (issue [#368](https://github.com/dermot-murphy/CStyleCheck/issues/368)).
- **`prerelease_check.sh` and `check_my_project.bat`** — helper scripts for running a
  pre-release validation sweep and a project self-check on Windows/Linux
  (issue [#343](https://github.com/dermot-murphy/CStyleCheck/issues/343)).
- **Block-comment inline suppression syntax** — `/* cstylecheck: disable=rule.id */`
  now accepted as an alternative to the `//` line-comment form for all inline
  suppression directives (`disable=`, `disable-next-line=`, `enable=`)
  (issue [#360](https://github.com/dermot-murphy/CStyleCheck/issues/360)).

### Changed

- **`--summary` output restructured** — `Files:` section now appears before `Results:`;
  header line shows tool version and run timestamp (`Run at: YYYY-MM-DD HH:MM:SS`);
  `Results:` separator line width now tracks the digit count of the largest count;
  section labels renamed from `Errors & Warnings:` to `Results:`
  (issues [#352](https://github.com/dermot-murphy/CStyleCheck/issues/352),
  [#365](https://github.com/dermot-murphy/CStyleCheck/issues/365),
  [#366](https://github.com/dermot-murphy/CStyleCheck/issues/366)).
- **Verbose progress output** — progress line now uses the terminal width to prevent
  violation lines from being overwritten
  (issue [#357](https://github.com/dermot-murphy/CStyleCheck/issues/357)).

### Fixed

- **`misc.unsigned_suffix` false positive on signed-parameter arguments** — integer
  literals passed at a call site to a function parameter declared as `int8_t`,
  `int16_t`, `int32_t`, `int64_t`, `int`, `short`, `long`, or `char` are now exempt
  from the unsigned-suffix requirement when the function is declared/defined in the
  same translation unit
  (issue [#340](https://github.com/dermot-murphy/CStyleCheck/issues/340)).
- **Function violations reported on wrong line** — `RE_FUNCTION_DEF` starts with
  `(?:^|\n)`, causing `m.start()` to point to the `\n` ending the preceding line.
  Fixed with `fn_start` correction so all function-rule violations are reported on
  the function's own line
  (issue [#362](https://github.com/dermot-murphy/CStyleCheck/issues/362)).
- **`function.prefix` not suppressed by inline block directive** — the line-offset
  bug above also caused `// cstylecheck: disable=function.prefix` blocks to miss the
  function declaration line; now resolved by the same `fn_start` correction
  (issue [#362](https://github.com/dermot-murphy/CStyleCheck/issues/362)).
- **Function-pointer `typedef` false positive** — `typedef void (*callback_fn_t)(int x)`
  was parsed as a function declaration, raising a spurious `variable.parameter.p_prefix`
  violation on parameter `x`. Function-pointer typedef patterns are now recognised and
  skipped by the parameter-prefix check
  (issues [#359](https://github.com/dermot-murphy/CStyleCheck/issues/359),
  [#361](https://github.com/dermot-murphy/CStyleCheck/issues/361)).
- **`misc.yoda_condition` false positives** — no longer fires when the LHS is an
  array-element expression (`arr[i] == val`) or when both operands are constants
  (the latter case is now handled by `misc.constant_comparison`)
  (issue [#354](https://github.com/dermot-murphy/CStyleCheck/issues/354)).
- **`constant.case` false positives on function/alias `#define`s** — names that
  resemble function calls or typedef-style aliases (e.g.
  `#define api_error_t uint8_t`) are now exempt from `constant.case`
  (issue [#355](https://github.com/dermot-murphy/CStyleCheck/issues/355)).
- **Non-ASCII characters in output** — em-dash and curly quotes removed from all
  terminal, log, and verbose-progress output; all strings are now 7-bit ASCII
  (issues [#363](https://github.com/dermot-murphy/CStyleCheck/issues/363),
  [#364](https://github.com/dermot-murphy/CStyleCheck/issues/364)).
- **Mixed path separators in verbose output** — file paths now use the OS-native
  separator (backslash on Windows, forward slash on POSIX) consistently throughout
  verbose progress and violation reports
  (issue [#367](https://github.com/dermot-murphy/CStyleCheck/issues/367)).

---

## [1.5.1] — 2026-06-28

### Added

- **`DOCKERHUB_README.md`** — dedicated Docker Hub README automatically pushed by
  `docker_publish.yml` to keep the Docker Hub listing in sync with the GitHub README
  (issue [#300](https://github.com/dermot-murphy/CStyleCheck/issues/300)).

### Fixed

- **Docker `ARG GITHUB_REPOSITORY` placement** — `ARG` declaration moved after the
  `FROM` line to satisfy Docker BuildKit's scope rules; previously caused a build
  warning on multi-stage builds
  (issue [#300](https://github.com/dermot-murphy/CStyleCheck/issues/300)).
- **ASPICE document cross-reference drift** — stale version citations corrected in
  all 22 work products following the v1.5.0 release: SYS2 §3.3, SUP1 §3.1, and
  cascading SVD cross-refs updated to reflect the post-audit baseline
  (issues [#302](https://github.com/dermot-murphy/CStyleCheck/issues/302)–[#312](https://github.com/dermot-murphy/CStyleCheck/issues/312),
  [#315](https://github.com/dermot-murphy/CStyleCheck/issues/315)–[#335](https://github.com/dermot-murphy/CStyleCheck/issues/335)).

---

## [1.5.0] — 2026-06-26

### Added

- **`misc.non_ascii_source` rule** — flags characters outside the printable ASCII set
  (code points outside 0x20–0x7E, plus TAB/LF/CR), implementing MISRA C:2012/2023 Rule 4.1.
  Optional `exempt_string_literals: true` suppresses violations inside double-quoted string
  literals (issue [#279](https://github.com/dermot-murphy/CStyleCheck/issues/279)).
- **Per-file breakdown in `--summary` output** — the summary block now includes
  "Files with errors / warnings / info / clean" counts. Invariant: all four buckets
  sum to the total files-checked count
  (issue [#278](https://github.com/dermot-murphy/CStyleCheck/issues/278)).

### Changed

- **`constant.case` typedef-alias exemption** — object-like `#define` names ending with
  the configured `typedefs.suffix.suffix` (e.g. `_t`) are now exempt from `constant.case`
  when `typedefs.suffix.enabled: true`. This eliminates the false positive on
  `#define api_nvm_error_t uint8_t`-style type aliases
  (issues [#272](https://github.com/dermot-murphy/CStyleCheck/issues/272),
  [#244](https://github.com/dermot-murphy/CStyleCheck/issues/244)).

### Fixed

- **`variable.parameter.p_prefix` false positive on call statements** —
  `RE_FUNCTION_DECL`/`RE_FUNCTION_DEF` now require a real (non-zero-width) separator
  between the return-type token and the function-name token, preventing regex
  backtracking from misparsing a plain call statement as a declaration/definition
  (issue [#273](https://github.com/dermot-murphy/CStyleCheck/issues/273)).

---

## [1.4.1] — 2026-06-18

### Fixed

- **`variable.parameter.p_prefix` false positive on call statements** —
  `RE_FUNCTION_DECL`/`RE_FUNCTION_DEF` allowed a zero-width separator between
  the captured return-type token and the function-name token. Regex
  backtracking on a plain call statement (e.g. `foo (args) ;`, a single
  identifier with no real type/name split) could split that identifier into a
  fake type + fake name, making the call match as if it were a declaration or
  definition. The call's arguments were then parsed as parameters, producing
  nonsensical `variable.parameter.p_prefix` violations (e.g. flagging `t` from
  a `(uint16_t)` cast, or substrings of `interval`/`timeout`). Fixed by
  requiring a real (non-zero-width) separator — whitespace and/or a pointer
  star — between the return type and the name
  (issue [#273](https://github.com/dermot-murphy/CStyleCheck/issues/273)).
- **`docker_publish.yml` `github-release` job** — checkout step was missing
  the explicit `token: secrets.GITHUB_TOKEN`, inconsistent with the
  `build-and-push` job's checkout step.

---

## [1.4.0] — 2026-06-18

### Added

- **`macro.trailing_semicolon` rule** — detects `#define` macros whose expansion ends
  with a semicolon, preventing double-semicolon and dangling-else bugs at the call site
  (issue [#228](https://github.com/dermot-murphy/CStyleCheck/issues/228)).
- **`macro.multistatement_wrapper` rule** — enforces that function-like macros containing
  multiple statements are wrapped in `do { ... } while (0)` for safe use in `if`/`else`
  branches
  (issue [#229](https://github.com/dermot-murphy/CStyleCheck/issues/229)).
- **`misc.function_length` rule** — configurable maximum function body line count;
  supports `count_comments: false` to exclude blank and comment-only lines from the count
  (issue [#221](https://github.com/dermot-murphy/CStyleCheck/issues/221)).
- **`misc.function_doc_header` rule** — requires a Doxygen-style `@brief`/`@param`/`@return`
  block comment before each non-static function definition (disabled by default)
  (issue [#222](https://github.com/dermot-murphy/CStyleCheck/issues/222)).
- **`misc.assert_density` rule** — enforces a minimum number of `assert()` calls per
  qualifying function; supports per-function exemption via regex patterns (disabled by default)
  (issue [#225](https://github.com/dermot-murphy/CStyleCheck/issues/225)).
- **`misc.null_statement_comment` rule** — requires a comment whenever a null statement
  (`while (x) ;`, standalone `;`) is used, preventing accidental empty loop bodies
  (issue [#227](https://github.com/dermot-murphy/CStyleCheck/issues/227)).
- **`misc.declaration_spacing` rule** — enforces a blank line between variable declarations
  and the first executable statement in a function body (disabled by default)
  (issue [#224](https://github.com/dermot-murphy/CStyleCheck/issues/224)).
- **`misc.file_length` rule** — configurable maximum total lines per source file; supports
  excluding blank and/or comment-only lines from the count
  (issue [#232](https://github.com/dermot-murphy/CStyleCheck/issues/232)).
- **`misc.reserved_header_name` rule** — flags source files and `#include "..."` directives
  that use a name identical to a standard C or POSIX library header, preventing shadowing
  (issue [#230](https://github.com/dermot-murphy/CStyleCheck/issues/230)).
- **`naming.identifier_length` rule** — uniform minimum/maximum identifier-length check
  across all identifier categories with per-name exemptions (disabled by default)
  (issue [#223](https://github.com/dermot-murphy/CStyleCheck/issues/223)).
- **`naming.no_single_char_identifiers` rule** — flags single-character variable names
  outside a configurable exempt list (e.g. `i`, `j`, `k`) (disabled by default)
  (issue [#231](https://github.com/dermot-murphy/CStyleCheck/issues/231)).
- **102 new tests** (1152 total) covering all 11 new rules, including edge cases for
  multi-line macros, nested braces, comment exclusion, and regex-based exemptions.
- Draft companion documents `embedded_c_style_guide.md`, `embedded_c_coding_standard.md`,
  and `external_standards_analysis.md` — pending rule population, linked from the README.

### Fixed

- Parameter and pointer naming-prefix checks no longer require both prefixes
  simultaneously when only one is configured, fixing false positives on otherwise
  compliant declarations
  (issues [#245](https://github.com/dermot-murphy/CStyleCheck/issues/245),
  [#246](https://github.com/dermot-murphy/CStyleCheck/issues/246)).
- Fixed a catastrophic-backtracking (ReDoS) regular expression in
  `misc.null_statement_comment` that could hang indefinitely on an unclosed
  `if`/`while`/`for` condition spanning a long line
  (issues [#248](https://github.com/dermot-murphy/CStyleCheck/issues/248),
  [#249](https://github.com/dermot-murphy/CStyleCheck/issues/249)).
- Fixed broken GitHub Wiki links: malformed triple-hyphen slugs for headings containing
  backticks/parentheses, and a non-functional "Rules and Configuration Reference" link
  that previously prompted "Create a new page" instead of opening the Rules page
  (issue [#251](https://github.com/dermot-murphy/CStyleCheck/issues/251)).

---

## [1.3.0] — 2026-06-05

### Added

- **Inline suppression comments** (`preprocessor.parse_inline_suppressions`) — suppress
  violations on a per-line, next-line, or block basis using structured `// cstylecheck:
  disable=rule.id` comments in C source.  Multiple rules can be comma-separated;
  directives are case-insensitive
  (issue [#188](https://github.com/dermot-murphy/CStyleCheck/issues/188)).
- **`--fix` auto-fix mode** (`fixer.py`) — apply safe mechanical fixes in-place.
  Currently fixes `misc.unsigned_suffix` (`42u` → `42U`) and `misc.lowercase_l_suffix`
  (`100l` → `100L`).  Use `--dry-run` to preview a unified diff without writing, and
  `--safe-only` to restrict to zero-risk fixes (all current fixes qualify)
  (issue [#189](https://github.com/dermot-murphy/CStyleCheck/issues/189)).
- **`--init` config wizard and `--preset`** (`wizard.py`) — `--init` launches an
  interactive Q&A wizard that writes `.cstylecheck.yml`; `--preset barr-c|minimal|misra`
  writes a pre-built config without the wizard.  `--init-output FILE` sets a custom
  output path; `--overwrite` allows overwriting an existing file
  (issue [#190](https://github.com/dermot-murphy/CStyleCheck/issues/190)).
- **Per-directory config** (`config.py resolve_per_dir_config`) — `--per-dir-config`
  flag enables upward directory-walk from each source file, deep-merging any
  `.cstylecheck.yml` found along the path on top of the root config.  The nearest config
  wins; `root: true` in any `.cstylecheck.yml` stops the upward search.  Results are
  cached per directory
  (issue [#193](https://github.com/dermot-murphy/CStyleCheck/issues/193)).
- **HTML report** (`output.py _violations_to_html`) — `--output-format html` produces a
  self-contained HTML report with inline CSS, summary cards (errors / warnings / info /
  total / files), and per-file violation tables.  Written to `--log FILE` if provided,
  else stdout
  (issue [#192](https://github.com/dermot-murphy/CStyleCheck/issues/192)).

---


## [1.2.1] — 2026-05-29

### Fixed

- **Docker image broken in v1.2.0** — `Dockerfile` was missing `COPY src/cstylecheck/ ./cstylecheck/`.
  The shim `cstylecheck.py` does `from cstylecheck.cli import main` which requires the package
  directory to be present alongside the shim inside `/app/`. Without it, Python resolved
  `cstylecheck` to the shim file itself, producing
  `ModuleNotFoundError: No module named 'cstylecheck.cli'; 'cstylecheck' is not a package`.

---

## [1.2.0] — 2026-05-29

### Added

- **`misc.comment_ratio` rule** — configurable minimum comment-density gate; fails when the
  ratio of comment lines to total lines in a file falls below the configured threshold
  (issue [#68](https://github.com/dermot-murphy/CStyleCheck/issues/68)).
- **`misc.whitespace_ratio` rule** — configurable blank-line density gate; fails when the
  ratio of blank lines to total lines exceeds the configured ceiling, catching overly sparse or
  padded source files
  (issue [#145](https://github.com/dermot-murphy/CStyleCheck/issues/145)).
- **`misc.declared_not_defined` cross-file rule** — detects functions declared in a `.h` file
  but never defined in any paired `.c` file in the same invocation, surfacing missing
  implementation stubs early
  (issue [#114](https://github.com/dermot-murphy/CStyleCheck/issues/114)).
- **Package refactor** — `cstylecheck.py` monolith split into a proper Python package
  (`src/cstylecheck/`) comprising 10 sub-modules (`checker.py`, `cli.py`, `config.py`,
  `models.py`, `preprocessor.py`, `utils.py`, `sign_checker.py`, `baseline.py`, `output.py`,
  `__init__.py`). The thin shim `src/cstylecheck.py` retains CLI backward compatibility
  (issue [#65](https://github.com/dermot-murphy/CStyleCheck/issues/65)).
- **CSC-DEV-002 Independent Review Deviation Record** added to ASPICE documentation, formally
  acknowledging the solo-developer peer-review constraint
  (issue [#61](https://github.com/dermot-murphy/CStyleCheck/issues/61)).
- **ASPICE internal audit (CSC-AUD-001)** completed; 58 defects in 14 work products resolved
  (issues [#143](https://github.com/dermot-murphy/CStyleCheck/issues/143),
  [#146](https://github.com/dermot-murphy/CStyleCheck/issues/146)–[#157](https://github.com/dermot-murphy/CStyleCheck/issues/157)).

### Changed

- **Test suite expanded to 839 tests** across 30 test modules — 290 tests added since v1.1.0
  covering the 3 new rules, package refactor, and additional edge cases.
- **Coverage gate raised to 85% combined** (statement + branch) via subprocess coverage for the
  CLI entry point; `--cov-fail-under=85` enforced in CI
  (issue [#54](https://github.com/dermot-murphy/CStyleCheck/issues/54)).
- **ASPICE documentation** — all 17 work products updated with v1.2.x revision history entries.
  ASPICE SWE3 Detailed Design updated to reflect the new 10-module package architecture.

### Fixed

- **CI path trigger** for `cstylecheck_tests.yml` corrected to include `src/cstylecheck/**`
  after the package refactor (was triggering only on `src/cstylecheck.py`).

---

## [1.1.0] — 2026-05-28

### Added

- **MISRA C:2012/2023 coverage matrix** added to `Rules-and-Configuration.md`, mapping each
  CStyleCheck rule ID to the MISRA C:2012 and MISRA C:2023 rules it implements or supports
  (issues [#64](https://github.com/dermot-murphy/CStyleCheck/issues/64)).
- **mypy static type-checking gate** added to the CI test workflow
  (`cstylecheck_tests.yml`): runs `mypy src/cstylecheck.py --ignore-missing-imports
  --implicit-optional` on Python 3.11 and fails the build on type errors
  (issue [#66](https://github.com/dermot-murphy/CStyleCheck/issues/66)).
- **ruff lint gate** added to the CI test workflow: runs `ruff check src/ tests/` on
  Python 3.11 and fails the build on lint violations; ruff config added to `pyproject.toml`
  (issue [#66](https://github.com/dermot-murphy/CStyleCheck/issues/66)).
- **CSC-DEV-001 AI Authorship Deviation Record** (`docs/aspice/CStyleCheck_DEV001_AI_Authorship_Deviation.md`)
  documents the approved deviation for AI-assisted content generation across all ASPICE work
  products (issue [#52](https://github.com/dermot-murphy/CStyleCheck/issues/52)).
- **Badge-path regression tests** (`tests/test_workflow_config.py`) prevent future drift in
  the shields.io badge endpoint path (issue [#42](https://github.com/dermot-murphy/CStyleCheck/issues/42)).

### Changed

- **CI scripts extracted from workflow YAML**: inline Python blocks in
  `cstylecheck_rules.yml` moved to dedicated scripts in `scripts/ci/`:
  `append_trend_record.py`, `generate_trend.py`, `update_readme_badge.py`.
  Improves readability and testability (issue [#63](https://github.com/dermot-murphy/CStyleCheck/issues/63)).
- **Shields.io badge endpoint** now uses `raw.githubusercontent.com` (gh-pages branch) as
  the endpoint URL instead of the GitHub Pages CDN — fixes intermittent badge staleness.
- **ASPICE work products** updated with v1.1 revision history entries in all 17 documents
  (issue [#62](https://github.com/dermot-murphy/CStyleCheck/issues/62)).

### Fixed

- **`--spell-words` with disabled spell check** now emits a clear warning instead of
  silently ignoring the flag (issue [#90](https://github.com/dermot-murphy/CStyleCheck/issues/90)).
- **`tj-actions/changed-files`** pinned to full commit SHA (SHA-pinned to v44) to prevent
  supply-chain risk from mutable tag references
  (issue [#59](https://github.com/dermot-murphy/CStyleCheck/issues/59)).
- **`moby/buildkit`** Docker build driver pinned to `v0.19.0` for reproducible multi-platform
  builds (issue [#60](https://github.com/dermot-murphy/CStyleCheck/issues/60)).
- **Global mutation of `C_KEYWORDS`/`C_STDLIB_NAMES`** in `main()` eliminated; lists are now
  copied before modification, preventing cross-invocation contamination when the checker is
  imported (issue [#79](https://github.com/dermot-murphy/CStyleCheck/issues/79)).
- **GitHub Actions annotation titles** now reflect the rule type (Error/Warning/Info) rather
  than always showing "error" (issue [#77](https://github.com/dermot-murphy/CStyleCheck/issues/77)).
- **`lower` and `upper` case pattern matchers** corrected to reject identifiers containing
  underscores where the rule requires purely lower-case or upper-case letters
  (issue [#74](https://github.com/dermot-murphy/CStyleCheck/issues/74)).
- **CRLF line endings** normalised once in `Checker.__init__()` rather than on every
  individual check, fixing false positives on Windows-formatted files
  (issue [#73](https://github.com/dermot-murphy/CStyleCheck/issues/73)).
- **Single-quoted char literals** (e.g. `'\n'`, `'a'`) now stripped in `strip_strings()`,
  preventing false positives from character constants
  (issue [#72](https://github.com/dermot-murphy/CStyleCheck/issues/72)).
- **Digit segments in `lower_snake` variable names** now accepted (e.g. `buf16`, `i2c_bus`)
  (issue [#70](https://github.com/dermot-murphy/CStyleCheck/issues/70)).
- **Bidirectional alias map** built correctly so that either column order in `aliases.txt`
  is accepted (issue [#57](https://github.com/dermot-murphy/CStyleCheck/issues/57)).
- **`datetime.utcnow()`** replaced with timezone-aware `datetime.now(timezone.utc)` in
  trend-record script, eliminating Python 3.12 deprecation warning
  (issue [#56](https://github.com/dermot-murphy/CStyleCheck/issues/56)).
- **CI concurrency group** added to `cstylecheck_rules.yml` to serialise runs on the same
  branch and prevent parallel pushes racing to append trend records
  (issue [#55](https://github.com/dermot-murphy/CStyleCheck/issues/55)).
- **Exit code 2** (configuration error) now correctly terminates CI with an informative
  error annotation rather than silently passing
  (issue [#50](https://github.com/dermot-murphy/CStyleCheck/issues/50)).
- **Explicit `token:` parameter** added to all bare `actions/checkout` steps to prevent
  intermittent authentication failures on self-hosted runners
  (issue [#51](https://github.com/dermot-murphy/CStyleCheck/issues/51)).
- **Dead `_vb_prev_dir` assignments** removed from `main()` (dead code cleanup)
  (issue [#76](https://github.com/dermot-murphy/CStyleCheck/issues/76)).
- **Redundant local `re` import** removed from `_v()` (code hygiene)
  (issue [#75](https://github.com/dermot-murphy/CStyleCheck/issues/75)).
- **Unused `OrderedDict` import** removed from `_violations_to_sarif()`; spurious `f`-prefix
  strings and unused local variables cleaned up to pass ruff `F401`/`F541`/`F841` checks
  (issue [#66](https://github.com/dermot-murphy/CStyleCheck/issues/66)).

### Documentation

- `docs/aliases.txt` clarified to explain bidirectionality and document commented-out examples
  (issue [#71](https://github.com/dermot-murphy/CStyleCheck/issues/71)).
- `docs/aspice/CStyleCheck_SWE3_Detailed_Design.md` section headers renumbered to match
  `run_all()` execution order (issue [#78](https://github.com/dermot-murphy/CStyleCheck/issues/78)).

---

## [1.0.2] — 2026-05-12

Internal maintenance release (tag only, no GitHub Release page).

### Fixed

- Version badge references updated in README.
- `docker_publish.yml` path trigger corrected to `src/rules.yml`.

---

## [1.0.0] — 2026-04-15

Initial public release.

### Added

- **50 rule IDs** implementing Barr-C:2018 and MISRA-C complementary naming conventions.
- GitHub Actions CI workflow (`cstylecheck_rules.yml`) with trend graph and shields.io badge.
- Docker image published to GHCR and Docker Hub (`cstylecheck`).
- ASPICE CL2 work-product documentation suite (SYS, SWE, MAN, SUP, ACQ processes).
- pre-commit hook support.
- Baseline suppression file (`--exclusions`).
- Structured SARIF / JSON output.
- `--spell-check` integration with custom dictionary.
- `--copyright` file enforcement (`misc.copyright_header`).
- `--eof-comment` mandatory EOF marker (`misc.eof_comment`).

---

[Unreleased]: https://github.com/dermot-murphy/CStyleCheck/compare/v1.6.0...HEAD
[1.6.0]: https://github.com/dermot-murphy/CStyleCheck/compare/v1.5.1...v1.6.0
[1.5.1]: https://github.com/dermot-murphy/CStyleCheck/compare/v1.5.0...v1.5.1
[1.5.0]: https://github.com/dermot-murphy/CStyleCheck/compare/v1.4.1...v1.5.0
[1.4.1]: https://github.com/dermot-murphy/CStyleCheck/compare/v1.4.0...v1.4.1
[1.4.0]: https://github.com/dermot-murphy/CStyleCheck/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/dermot-murphy/CStyleCheck/compare/v1.2.1...v1.3.0
[1.2.1]: https://github.com/dermot-murphy/CStyleCheck/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/dermot-murphy/CStyleCheck/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/dermot-murphy/CStyleCheck/compare/V1.0.0...v1.1.0
[1.0.2]: https://github.com/dermot-murphy/CStyleCheck/compare/V1.0.0...V1.0.2
[1.0.0]: https://github.com/dermot-murphy/CStyleCheck/releases/tag/V1.0.0
