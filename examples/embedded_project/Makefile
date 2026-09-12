# =============================================================================
# Makefile — CStyleCheck convenience targets for embedded_project example
# =============================================================================
# Usage:
#   make              — run CI gate scan (fails on errors)
#   make strict       — run full Barr-C strict scan (always exits 0)
#   make dev          — run development profile scan (always exits 0)
#   make all          — run all three profiles and save reports
#   make clean        — remove generated reports
# =============================================================================

PYTHON    ?= python3
CHECKER   ?= $(PYTHON) ../../src/cstylecheck.py

SRC_FILES := $(wildcard src/*.c) $(wildcard include/*.h)
REPORTS   := reports

.PHONY: all check strict dev clean

# Default: CI gate — mirrors what runs in the pull-request workflow.
check:
	@mkdir -p $(REPORTS)
	$(CHECKER) \
	    --config config/ci.yml \
	    --output-format json \
	    $(SRC_FILES) | tee $(REPORTS)/ci_report.json

# Full Barr-C strict scan — informational, never fails the build.
strict:
	@mkdir -p $(REPORTS)
	$(CHECKER) \
	    --config config/strict.yml \
	    --exit-zero \
	    --output-format json \
	    $(SRC_FILES) | tee $(REPORTS)/strict_report.json

# Development profile — low-noise, suited to IDE integration.
dev:
	@mkdir -p $(REPORTS)
	$(CHECKER) \
	    --config config/development.yml \
	    --exit-zero \
	    --output-format json \
	    $(SRC_FILES) | tee $(REPORTS)/development_report.json

# Run all three profiles and save reports.
all: check strict dev

clean:
	rm -f $(REPORTS)/*.json
