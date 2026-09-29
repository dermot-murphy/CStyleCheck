"""
baseline.py — Baseline suppression for CStyleCheck.

Contains load_baseline, write_baseline, apply_baseline, _baseline_key and
_normalise_path.

Imports from: models.
"""
from __future__ import annotations

import posixpath
from collections import Counter
from pathlib import Path

from .models import Violation
from .utils import config_error


# ---------------------------------------------------------------------------
# Baseline suppression
# ---------------------------------------------------------------------------

def _normalise_path(path: str) -> str:
    """Return *path* with ``/`` separators and redundant ``./`` removed.

    Baseline files must be portable between Windows and Linux (issue #395):
    a path written on Windows as ``src\\mod.c`` and on Linux as
    ``src/mod.c`` must produce the same key.  Backslashes are converted on
    every platform so that baselines written by older Windows releases are
    still honoured on Linux.
    """
    posix = path.replace("\\", "/")
    return posixpath.normpath(posix) if posix else posix


def _baseline_key(v: Violation) -> str:
    """Stable string key identifying a violation for baseline matching.

    The line number is deliberately excluded (issue #394) so that an
    accepted violation stays suppressed when unrelated edits move it up or
    down the file.  Duplicates are handled by multiset counting in
    :func:`apply_baseline`.
    """
    return f"{_normalise_path(v.filepath)}:{v.rule}:{v.message}"


def load_baseline(path: str) -> Counter:
    """Load a baseline JSON file and return a multiset of violation keys.

    Each key is ``file:rule:message`` (see :func:`_baseline_key`); the count
    is the number of baseline entries with that key.  The ``line`` field is
    kept in the file for human review but is not used for matching.
    """
    import json
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        config_error(f"Cannot read baseline file '{path}': {e}")
    keys: Counter = Counter()
    for entry in data.get("violations", []):
        key = (f"{_normalise_path(str(entry.get('file', '')))}:"
               f"{entry.get('rule', '')}:{entry.get('message', '')}")
        keys[key] += 1
    return keys


def apply_baseline(violations: list, baseline: Counter) -> list:
    """Return the violations in *violations* not suppressed by *baseline*.

    Each baseline entry suppresses at most one violation with the same
    file, rule and message, so an extra copy of an accepted violation is
    still reported as new.  *baseline* is not modified.
    """
    remaining = Counter(baseline)
    kept: list = []
    for v in violations:
        key = _baseline_key(v)
        if remaining[key] > 0:
            remaining[key] -= 1
        else:
            kept.append(v)
    return kept


def write_baseline(violations: list, path: str) -> None:
    """Write *violations* as a JSON baseline file to *path*.

    File paths are written with ``/`` separators on every platform.
    """
    import json
    data = {
        "violations": [
            {
                "file":    _normalise_path(v.filepath),
                "line":    v.line,
                "rule":    v.rule,
                "message": v.message,
            }
            for v in violations
        ]
    }
    try:
        Path(path).write_text(json.dumps(data, indent=2), encoding="utf-8")
    except OSError as e:
        config_error(f"Cannot write baseline file '{path}': {e}")
