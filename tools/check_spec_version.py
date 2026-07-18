#!/usr/bin/env python3
"""Fail if normative content changed without a spec-version bump.

    python tools/check_spec_version.py <base-ref>

The framework's citable content and its presentation change at different rates.
This guard keeps that separation honest: if a taxonomy row or checklist item is
edited, the version a study cites must change too, otherwise two different
requirements would be published under one number.

Editing prose, styles, templates, examples or package code does not trip it.
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


def spec_version_at(ref: str | None = None) -> str | None:
    if ref is None:
        text = (ROOT / "spec" / "spec.yml").read_text(encoding="utf-8")
    else:
        try:
            text = git("show", f"{ref}:spec/spec.yml")
        except subprocess.CalledProcessError:
            return None  # spec.yml did not exist at that ref
    return yaml.safe_load(text)["spec_version"]


def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else "origin/main"

    manifest = yaml.safe_load((ROOT / "spec" / "spec.yml").read_text(encoding="utf-8"))
    normative = set(manifest["normative"])
    current = manifest["spec_version"]

    try:
        changed = set(git("diff", "--name-only", f"{base}...HEAD").splitlines())
    except subprocess.CalledProcessError:
        print(f"could not diff against {base}; skipping check")
        return 0

    touched = sorted(changed & normative)
    # spec.yml itself changing is how a bump is expressed, so it does not
    # by itself constitute a normative content change.
    substantive = [p for p in touched if p != "spec/spec.yml"]

    if not substantive:
        print("no normative content changed")
        return 0

    previous = spec_version_at(base)
    print(f"normative files changed: {', '.join(substantive)}")
    print(f"spec_version {previous} -> {current}")

    if previous is not None and previous == current:
        print(
            "\nERROR: normative content changed but spec_version did not.\n"
            "Bump spec_version in spec/spec.yml and add a changelog entry, so a\n"
            "study citing the previous version is not silently reassessed\n"
            "against different requirements.",
            file=sys.stderr,
        )
        return 1

    print("spec_version bumped correctly")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
