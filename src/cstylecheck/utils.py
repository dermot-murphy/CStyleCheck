"""
utils.py — Naming/case helpers and shared utility functions for CStyleCheck.

Contains _CASE_PATTERNS, _CASE_ALIASES, normalize_case_style,
matches_case, matches_case_abbrev, to_case, module_name, is_exempt,
_cfg, _strip_module_prefix, and _github_annotation_category.

No internal dependencies (stdlib only).
"""
from __future__ import annotations

import re
from pathlib import Path

from .models import _MISRA_ANNOTATION_RULES, _NAMING_ANNOTATION_PREFIXES


# ---------------------------------------------------------------------------
# GitHub annotation category helper
# ---------------------------------------------------------------------------

def _github_annotation_category(rule: str) -> str:
    """Return the GitHub Actions annotation title category for *rule*."""
    if rule in _MISRA_ANNOTATION_RULES:
        return "MISRA"
    if rule == "sign_compatibility":
        return "SignCompat"
    if rule == "spell_check":
        return "SpellCheck"
    if rule.split(".", 1)[0] in _NAMING_ANNOTATION_PREFIXES:
        return "NamingConvention"
    return "Misc"


# ---------------------------------------------------------------------------
# Case patterns
# ---------------------------------------------------------------------------

_CASE_PATTERNS = {
    "lower_snake": re.compile(r"^[a-z][a-z0-9_]*$"),
    "upper_snake": re.compile(r"^[A-Z][A-Z0-9_]*$"),
    "camel":       re.compile(r"^[a-z][a-zA-Z0-9]*$"),
    "pascal":      re.compile(r"^[A-Z][a-zA-Z0-9]*$"),
    "lower":       re.compile(r"^[a-z][a-z0-9]*$"),    # no underscores
    "upper":       re.compile(r"^[A-Z][A-Z0-9]*$"),    # no underscores
    "any":         re.compile(r"^.*$", re.DOTALL),     # explicit opt-out
}

# Accepted spellings of the canonical case-style names (#422).  Keys are
# lower-cased; lookup is case-insensitive.  "lower" / "upper" are NOT
# aliases: they are distinct canonical styles (no underscores allowed).
_CASE_ALIASES = {
    "pascalcase":           "pascal",
    "pascal_case":          "pascal",
    "camelcase":            "camel",
    "camel_case":           "camel",
    "upper_snake_case":     "upper_snake",
    "screaming_snake":      "upper_snake",
    "screaming_snake_case": "upper_snake",
    "snake_case":           "lower_snake",
    "lower_snake_case":     "lower_snake",
    "snake":                "lower_snake",
}


def normalize_case_style(style):
    """
    Return the canonical ``_CASE_PATTERNS`` name for *style* (#422).

    Matching is case-insensitive and accepts the aliases in
    ``_CASE_ALIASES`` (e.g. ``PascalCase`` -> ``pascal``, ``UPPER_SNAKE``
    -> ``upper_snake``).  A value that is not a canonical name or alias is
    returned unchanged so the caller can report it; non-strings are returned
    unchanged too.
    """
    if not isinstance(style, str):
        return style
    key = style.strip().lower()
    if key in _CASE_PATTERNS:
        return key
    return _CASE_ALIASES.get(key, style)


def matches_case(name: str, style: str) -> bool:
    """
    True if *name* matches case *style* (canonical name or alias).

    An unknown style raises ``ValueError`` rather than silently passing
    (#422); configs loaded through ``load_config`` are validated up front
    so the CLI reports this as a config error (exit 2) instead.
    """
    pat = _CASE_PATTERNS.get(normalize_case_style(style))
    if pat is None:
        raise ValueError(
            f"Unknown case style {style!r}; allowed: "
            f"{', '.join(_CASE_PATTERNS)}")
    return pat.match(name) is not None


def matches_case_abbrev(name: str, style: str, abbrevs: set) -> bool:
    """
    Like matches_case() but for lower_snake / lower styles, each
    underscore-delimited segment is also accepted if it appears (in any
    case) in *abbrevs* (the set of allowed uppercase abbreviations).

    Example:  read_FIFO_registers  passes lower_snake when FIFO is in abbrevs.
    For all other styles the function behaves identically to matches_case().
    """
    style = normalize_case_style(style)
    if style not in ("lower_snake", "lower") or not abbrevs:
        return matches_case(name, style)
    segments = name.split("_")
    for seg in segments:
        if not seg:
            continue
        if seg.upper() in abbrevs:
            continue   # allowed abbreviation — any capitalisation
        if not re.match(r"^[a-z0-9]+$", seg):
            return False
    return True


def to_case(name: str, style: str) -> str:
    """Convert *name* to *style* — used to derive enum member prefixes."""
    style = normalize_case_style(style)
    if style in ("upper_snake", "upper"):
        return name.upper()
    if style in ("lower_snake", "lower", "camel"):
        return name.lower()
    return name    # pascal / as_is — unchanged


def module_name(filepath: str) -> str:
    return Path(filepath).stem.lower()


def is_exempt(name: str, patterns: list) -> bool:
    for p in patterns:
        try:
            if re.match(p, name):
                return True
        except re.error:
            pass
    return False


def _cfg(cfg: dict, *keys, default=None):
    node = cfg
    for k in keys:
        if not isinstance(node, dict):
            return default
        node = node.get(k, default)
        if node is None:
            return default
    return node


# ---------------------------------------------------------------------------
# Module-prefix stripping helper (used in variable checks)
# ---------------------------------------------------------------------------

def _strip_module_prefix(name: str, prefix: str) -> str:
    """Return *name* with the module prefix removed (case-insensitive)."""
    if name.lower().startswith(prefix.lower()):
        return name[len(prefix):]
    return name
