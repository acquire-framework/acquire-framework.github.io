# ACQUIRE Minimum Reporting Checklist, specification 26.7.1

SPDX-License-Identifier: CC0-1.0 — public domain, no attribution
required. Citation is a scholarly norm here, not a licence condition.

Machine-readable form of Table 2 of Danioł & Sroka (2026), UbiComp/ISWC '26 Companion.

This specification has not been evaluated for usability, coverage, or
inter-rater agreement. No claim is made that applying it improves outcomes.

Items marked not applicable require a written justification: silent
omission and reasoned exclusion look identical in a finished document.

- [ ] **MRC-01** (core, [O]) Expected versus observed completeness, per modality, with the sampling and background-execution policy.
- [ ] **MRC-02** (core, [O]) Missingness statistics and their suspected attribution (technical / adherence / attrition), with the evidence used.
- [ ] **MRC-03** (core, [M] [EN]) Device models, OS versions, app and firmware versions, and every mid-study change.
- [ ] **MRC-04** (core, [M]) Timestamping source, synchronization policy, and residual clock uncertainty after reconciliation.
- [ ] **MRC-05** (conditional, [M]) An accuracy or uncertainty statement appropriate to each primary derived measurand, or a documented justification of why quantitative uncertainty could not be established and what validation evidence is provided instead.
      - *Justification floor:* A justification is acceptable only if it names the dominant uncertainty sources, states why each could not be quantified, and describes the validation evidence offered in place of a budget. "Uncertainty could not be established" alone does not satisfy this item.
- [ ] **MRC-06** (core, [EN]) Upload retry, deduplication, and integrity-verification logic (checksums, sequence numbers).
- [ ] **MRC-07** (core, [EN]) Context and system-health events recorded alongside the data: power state, connectivity, permissions; crashes and service kills.
- [ ] **MRC-08** (core, [EN]) Machine-readable schema and collection-software artifacts published alongside the data.
- [ ] **MRC-09** (core, [EN]) QC exclusion criteria and preprocessing provenance from raw log to released dataset.
- [ ] **MRC-10** (conditional, [M] [EN] [O]) Pre-deployment verification evidence: which failure modes of the taxonomy were tested, how, and with what observed behaviour.
