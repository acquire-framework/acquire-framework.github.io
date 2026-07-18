#!/usr/bin/env python3
"""Emit the taxonomy and checklist as CSV and Markdown.

The paper commits to distributing both in machine-readable form (Markdown, CSV,
YAML). YAML is the source of truth; this derives the other two so they cannot
drift from it.

    python tools/export_artifact.py

Writes into dist/.
"""

from __future__ import annotations

import csv
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"


def load(rel: str) -> dict:
    return yaml.safe_load((ROOT / rel).read_text(encoding="utf-8"))


def export_taxonomy(spec: dict) -> None:
    rows = []
    for f in spec["failures"]:
        rows.append(
            {
                "id": f["id"],
                "layer": spec["layers"][f["layer"]],
                "failure_mode": f["mode"],
                "signature": f["signature"].strip(),
                "property": "+".join(f["property"]),
                "property_note": f["property_note"].strip(),
                "evidence": f["evidence"],
                "evidence_note": f["evidence_note"].strip(),
                "detector": ",".join(f.get("detectable_by") or []),
            }
        )

    with (DIST / "acquire-taxonomy.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    md = [
        "# ACQUIRE acquisition-failure taxonomy v" + spec["version"],
        "",
        f"Machine-readable form of Table 1 of {spec['paper']}.",
        "",
        "Initial, expert-derived, formative. Not a systematic review: no",
        "pre-registered protocol, no independent coders, no inter-rater",
        "reliability, no external validation. Rows marked [E] are candidate",
        "classes, not prevalence estimates.",
        "",
        "Property: [M] measurement validity · [EN] record integrity and",
        "provenance · [O] observation-process validity.",
        "Evidence: [L] published example · [E] experience-derived · [A] assumption.",
        "",
        "| ID | Failure mode | Signature | Property | Evidence |",
        "|:--|:--|:--|:--|:--|",
    ]
    for f in spec["failures"]:
        props = " ".join(f"[{p}]" for p in f["property"])
        md.append(
            f"| {f['id']} | {f['mode']} | {f['signature'].strip()} "
            f"| {props} | [{f['evidence']}] |"
        )
    (DIST / "acquire-taxonomy.md").write_text("\n".join(md) + "\n", encoding="utf-8")


def export_mrc(spec: dict) -> None:
    rows = []
    for item in spec["items"]:
        rows.append(
            {
                "id": item["id"],
                "tier": item["tier"],
                "statement": item["statement"].strip(),
                "property": "+".join(item["property"]),
                "taxonomy": ",".join(item.get("taxonomy") or []),
                "auto": str(item.get("auto", False)),
            }
        )

    with (DIST / "acquire-mrc.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    md = [
        "# ACQUIRE Minimum Reporting Checklist v" + spec["version"],
        "",
        f"Machine-readable form of Table 2 of {spec['paper']}.",
        "",
        "v0.1 has not been evaluated for usability, coverage, or inter-rater",
        "agreement. No claim is made that applying it improves study outcomes.",
        "",
        "Items marked not applicable require a written justification: silent",
        "omission and reasoned exclusion look identical in a finished document.",
        "",
    ]
    for item in spec["items"]:
        props = " ".join(f"[{p}]" for p in item["property"])
        md.append(f"- [ ] **{item['id']}** ({item['tier']}, {props}) "
                  f"{item['statement'].strip()}")
        if item.get("justification_floor"):
            md.append(f"      - *Justification floor:* "
                      f"{item['justification_floor'].strip()}")
    (DIST / "acquire-mrc.md").write_text("\n".join(md) + "\n", encoding="utf-8")


def main() -> None:
    DIST.mkdir(exist_ok=True)
    export_taxonomy(load("taxonomy/acquire-taxonomy.yml"))
    export_mrc(load("checklist/acquire-mrc.yml"))
    for path in sorted(DIST.iterdir()):
        print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
