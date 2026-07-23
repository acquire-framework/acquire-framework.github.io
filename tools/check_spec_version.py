#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Mateusz Danioł, Ryszard Sroka
"""Fail if normative content changed without a spec-version bump.

    python tools/check_spec_version.py <base-ref>

The framework's citable content and its presentation change at different rates.
This guard keeps that separation honest: if a taxonomy row or checklist item is
edited, the version a study cites must change too, otherwise two different sets
of requirements would be published under one number.

Comparison is **semantic, not textual**: each normative file is parsed and the
resulting structures compared. Fixing a typo in a comment, rewrapping a line, or
correcting a cross-reference in a header therefore does not demand a version
bump, because none of them changes a requirement. Changing the wording of an
item does, because the parser sees it.

Editing prose, styles, templates, examples or supporting code never trips this.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout.strip()


def parse_at(path: str, ref: str | None) -> object | None:
    """Parse *path* at *ref* (or the working tree if ref is None), verbatim."""
    try:
        text = (
            (ROOT / path).read_text(encoding="utf-8")
            if ref is None
            else git("show", f"{ref}:{path}")
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return yaml.safe_load(text)


# Top-level keys that carry provenance and versioning metadata rather than
# requirements. Correcting a citation, a date, or a DOI is editorial and must
# not demand a specification bump; only the requirement-bearing content does.
_METADATA_KEYS = frozenset(
    {"version", "spec_version", "updated", "revised", "released", "doi",
     "paper", "source"}
)


def requirements_at(path: str, ref: str | None) -> object | None:
    """The requirement-bearing content: metadata keys removed for comparison."""
    doc = parse_at(path, ref)
    if isinstance(doc, dict):
        return {k: v for k, v in doc.items() if k not in _METADATA_KEYS}
    return doc


def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else "origin/main"

    manifest = yaml.safe_load((ROOT / "spec" / "spec.yml").read_text(encoding="utf-8"))
    current = manifest["spec_version"]

    # spec.yml is where a bump is declared, so it is not itself evidence that
    # requirements changed.
    normative = [p for p in manifest["normative"] if p != "spec/spec.yml"]

    changed = []
    for path in normative:
        before, after = requirements_at(path, base), requirements_at(path, None)
        if before != after:
            changed.append(path)

    if not changed:
        print("no normative content changed (semantic comparison)")
        return 0

    # Version read verbatim, never metadata-stripped.
    previous = (parse_at("spec/spec.yml", base) or {}).get("spec_version")
    print(f"normative content changed: {', '.join(changed)}")
    print(f"spec_version {previous} -> {current}")

    if previous is not None and previous == current:
        print(
            "\nERROR: normative content changed but spec_version did not.\n"
            "Bump spec_version in spec/spec.yml and add a changelog entry, so a\n"
            "study citing the previous version is not silently reassessed against\n"
            "different requirements.\n\n"
            "If your change was editorial — a comment, a cross-reference, or\n"
            "formatting — this check would not have fired, so something in the\n"
            "parsed content did change. Compare with:\n"
            f"    git diff {base} -- {' '.join(changed)}",
            file=sys.stderr,
        )
        return 1

    print("spec_version bumped correctly")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
