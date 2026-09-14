# Embedded Project Example

A minimal embedded C project demonstrating CStyleCheck integration.
The project implements a cooperative task scheduler and an LED control module
that could run on any microcontroller with a GPIO peripheral and a millisecond
tick counter.

## Project structure

```
embedded_project/
├── include/
│   ├── project_config.h      # System-wide constants and includes
│   ├── led_control.h         # LED control module public API
│   └── task_scheduler.h      # Cooperative task scheduler public API
├── src/
│   ├── led_control.c         # LED control implementation
│   ├── task_scheduler.c      # Round-robin scheduler implementation
│   └── main.c                # Application entry point
├── config/
│   ├── ci.yml                # CI gate profile (errors only block the build)
│   ├── strict.yml            # Barr-C / MISRA-aligned full profile
│   └── development.yml       # Low-noise IDE profile
├── workflow/
│   └── cstylecheck.yml       # Drop-in GitHub Actions workflow for your project
├── reports/                  # Sample CStyleCheck JSON reports
│   ├── ci_report.json
│   ├── strict_report.json
│   └── development_report.json
├── charts/                   # Sample trend SVG charts
│   ├── main_errors_warnings.svg
│   ├── main_loc_breakdown.svg
│   ├── main_cyclomatic_complexity.svg
│   ├── main_defect_density.svg
│   └── main_func_metrics.svg
└── Makefile                  # Convenience targets for local development
```

## Running checks locally

From this directory (`examples/embedded_project/`):

```bash
# CI gate — mirrors what runs in pull-request CI (fails on errors)
make check

# Full Barr-C strict profile — informational, never fails the build
make strict

# Low-noise development profile — suited for IDE integration
make dev

# Run all three and save reports to reports/
make all

# Clean generated reports
make clean
```

### Running without Make

```bash
python3 ../../src/cstylecheck.py \
    --config config/ci.yml \
    src/led_control.c src/task_scheduler.c src/main.c \
    include/led_control.h include/task_scheduler.h include/project_config.h
```

Add `--output-format json` to get machine-readable output.
Add `--exit-zero` to prevent a non-zero exit code on violations (e.g. strict/dev profiles).

## Config profiles

| Profile | Purpose | Exits non-zero on |
|---------|---------|-------------------|
| `config/ci.yml` | Pull-request gate | Errors only (non-ASCII, bad include guards, indentation, octal, trigraphs) |
| `config/strict.yml` | Full Barr-C / MISRA review | All violations (informational in CI — use `--exit-zero`) |
| `config/development.yml` | IDE / daily dev use | Errors only (same set as CI) |

### Key rules enforced by each profile

**ci.yml** (hard errors — blocks CI):
- `misc.non_ascii_source` — no non-ASCII characters in source files
- `misc.include_guards` — every header must have a proper include guard
- `misc.indentation` — 4-space indentation required
- `misc.octal_constant` — no octal literals
- `misc.trigraph` — no C trigraph sequences
- `misc.lowercase_l_suffix` — use `1UL` not `1ul`

**strict.yml** (additional warnings on top of ci):
- `variables.global.g_prefix` — global variables must start with `g_`
- `variables.parameter.p_prefix` — pointer parameters must start with `p_`
- `misc.line_length` max 80 characters
- `functions.max_lines` max 50 lines
- `misc.copyright_header` — copyright comment required in every file

**development.yml** (info only):
- All violations demoted to `info` severity
- Line length limit raised to 100 characters
- Function length limit raised to 100 lines
- No naming-prefix requirements
- No copyright requirement

## Using the workflow in your own project

1. Copy `workflow/cstylecheck.yml` to `.github/workflows/cstylecheck.yml` in your repository.
2. Copy the `config/` directory to your project root (or adjust the `--config` paths in the workflow).
3. Update `SRC_GLOB` and `INCLUDE_GLOB` in the workflow to match your source tree.
4. Push — the check runs automatically on every PR and push to `main`/`develop`.

The workflow runs two jobs:
- **CI gate scan** — fails the check on errors; report uploaded as `cstylecheck-ci-report`.
- **Strict Barr-C scan** — always exits 0 (informational); report uploaded as `cstylecheck-strict-report`.

## Sample reports

The `reports/` directory contains pre-generated JSON reports for the source files
in this example, produced with each of the three config profiles:

| Report | Errors | Warnings | Info | Total |
|--------|--------|----------|------|-------|
| `ci_report.json` | 0 | 0 | 3 | 3 |
| `strict_report.json` | 0 | 36 | 0 | 36 |
| `development_report.json` | 0 | 0 | 3 | 3 |

The 3 info violations in the CI/development reports are `misc.comment_ratio` and
`enums.type_case` observations that are below the configured thresholds — they are
reported for visibility but do not affect the build outcome.

The 36 warnings in the strict report come primarily from naming-prefix rules
(`g_` for globals, `p_` for pointer parameters) and the stricter 80-character
line length limit — rules appropriate for safety-critical codebases
(IEC 61508-3, ISO 26262-6, MISRA C:2012) but relaxed in CI to reduce noise.

## Sample charts

The `charts/` directory contains SVG trend charts generated from simulated
4-commit history showing the project being brought into compliance over time:

| Chart | What it shows |
|-------|--------------|
| `main_errors_warnings.svg` | Errors, warnings, and info counts per commit |
| `main_loc_breakdown.svg` | Physical lines, SLOC, comment lines, blank lines |
| `main_cyclomatic_complexity.svg` | Max / average McCabe complexity and functions over threshold |
| `main_defect_density.svg` | Violations per KLOC (ASPICE SWE.4 maturity indicator) |
| `main_func_metrics.svg` | Max / average function length and parameter count |

In a real project, these charts are generated automatically on each push to
`main` or `develop` by the CStyleCheck metrics workflow and published to the
`gh-pages` branch.
