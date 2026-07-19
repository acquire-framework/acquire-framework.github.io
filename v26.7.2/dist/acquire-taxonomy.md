# ACQUIRE acquisition-failure taxonomy, specification 26.7.2

SPDX-License-Identifier: CC0-1.0 — public domain, no attribution
required. Citation is a scholarly norm here, not a licence condition.

Machine-readable form of Table 1 of Danioł & Sroka (2026), UbiComp/ISWC '26 Companion.

Initial, expert-derived, formative. Not a systematic review: no
pre-registered protocol, no independent coders, no inter-rater
reliability, no external validation. Rows marked [E] are candidate
classes, not prevalence estimates.

Property: [M] measurement validity · [EN] record integrity and
provenance · [O] observation-process validity.
Evidence: [L] published example · [E] experience-derived · [A] assumption.

| ID | Failure mode | Signature | Property | Evidence |
|:--|:--|:--|:--|:--|
| ACQ-F01 | Background-execution kill (Doze, vendor optimizers) | Non-random gaps; completeness far below 100%; worsens over weeks. | [O] [EN] | [L] |
| ACQ-F02 | Offline-first sync loss / token expiry / duplicate re-sync | Missing or duplicated records; silent truncation. | [EN] | [L] |
| ACQ-F03 | Clock drift / timestamp reconciliation | Drifting session boundaries; misaligned modalities. | [M] | [L] |
| ACQ-F04 | BLE disconnection / firmware-dependent buffering | Physiological gaps indistinguishable from true signal absence. | [EN] [O] | [E] |
| ACQ-F05 | Participant non-adherence / disabled permissions | Missing sessions, confounded with technical loss. | [O] | [L] |
| ACQ-F06 | Mid-study protocol / firmware / configuration change | Discontinuity not marked in the data. | [M] [EN] | [L] |
| ACQ-F07 | Missing schema / software / firmware provenance | Dataset not machine-interpretable or re-executable. | [EN] | [E] |
| ACQ-F08 | No accuracy or uncertainty statement | Numbers reported without stated uncertainty. | [M] | [L] |
