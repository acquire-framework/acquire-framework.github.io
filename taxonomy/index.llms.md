# Acquisition-failure taxonomy

Table 1 of the paper, in machine-readable form.

Failure modes grouped by the acquisition-system layer in which they originate, each mapped to its observable signature in the resulting dataset and to the property it threatens.

> **IMPORTANT:**
>
> **This is an initial, expert-derived structure, not a systematic review.** There was no pre-registered protocol, database search strategy, or inclusion criteria; no independent coders, no inter-rater reliability assessment, no Delphi process, no external expert validation, and no user study.
>
> It is a formative artifact offered for community evaluation and extension. Rows marked `[E]` are candidate classes, **not prevalence estimates**.

## The three properties

A failure threatens one or more of three analytically distinct properties. Conflating them is the error the framework most wants to avoid.

| Tag | Property | Governs |
|:---|:---|:---|
| **\[M\]** | Measurement validity | The quantity indicated by the instrument — accuracy, calibration, traceability, synchronization uncertainty, drift |
| **\[EN\]** | Record integrity and provenance | Whether what the instrument indicated was faithfully retained |
| **\[O\]** | Observation-process validity | Which observations exist at all — adherence, permissions, attrition, selective observation |

The axes are jointly necessary. A faithfully retained record may still contain invalid measurements; valid measurements may still be selectively observed; and failure along one axis may mask or compound failure along another.

**\[O\] is not a metrological problem.** Non-random acquisition loss changes the observation process and may bias estimands, but that is a missing-data and study-design issue, distinct from measurement error in the samples that do exist. Forcing it into metrological language overclaims.

## Evidence labels

| Tag       | Meaning                                                       |
|:----------|:--------------------------------------------------------------|
| **\[L\]** | Anchored by an illustrative published example                 |
| **\[E\]** | Experience-derived candidate class, not a prevalence estimate |
| **\[A\]** | Illustrative assumption                                       |

## The taxonomy

### Device and OS layer

#### `ACQ-F01` — Background-execution kill (Doze, vendor optimizers)

signature

Non-random gaps; completeness far below 100%; worsens over weeks.

property threatened

**\[O\]** **\[EN\]** Observation depends on device state and may bias time-aggregated estimands. \[EN\] additionally if kills are unlogged.

evidence

**\[L\]** 84% of scheduled executions missing across four devices (Gonzalez-Perez et al. 2022); 54.2% geolocation loss in the 625-participant IAB-SMART study (Bähr et al. 2022); no GPS on 49% of observation days in a 2,394-person Beiwe cohort (Yi et al. 2024, a figure that aggregates technical loss with attrition and adherence).

### Connectivity, backend and integrity layer

#### `ACQ-F02` — Offline-first sync loss / token expiry / duplicate re-sync

signature

Missing or duplicated records; silent truncation.

property threatened

**\[EN\]** Integrity and idempotency of the record.

evidence

**\[L\]** Sync and export failures reported but unquantified (Slade et al. 2025); \[E\] checksums and deduplication rarely described in methods sections.

### Wearable and BLE layer

#### `ACQ-F03` — Clock drift / timestamp reconciliation

signature

Drifting session boundaries; misaligned modalities.

property threatened

**\[M\]** Instrumental drift; traceability to a common time reference at an uncertainty suited to the measurand.

evidence

**\[L\]** Tens of ppm, of order seconds per day (Tirado-Andrés et al. 2019); BLE application-layer synchronization error exceeding 25 ms in 28% of sessions, maximum 183 ms (Yan et al. 2017).

> **WARNING:**
>
> **Detection limit.** Modest drift is NOT detectable from a single recording: nothing distinguishes a fast clock from slow sampling. Detection requires an external reference — a second device, a logged NTP offset, or a deliberate synchronization event.

Worked example: [`examples/synchronization`](https://github.com/acquire-framework/acquire-framework.github.io/tree/main/examples/synchronization).

#### `ACQ-F04` — BLE disconnection / firmware-dependent buffering

signature

Physiological gaps indistinguishable from true signal absence.

property threatened

**\[EN\]** **\[O\]** Gap provenance unrecorded; observation selectively absent.

evidence

**\[E\]** No systematic reporting of field disconnection and packet-loss rates was identified.

### Participant layer

#### `ACQ-F05` — Participant non-adherence / disabled permissions

signature

Missing sessions, confounded with technical loss.

property threatened

**\[O\]** Operator and protocol effects; missing-not-at-random risk.

evidence

**\[L\]** Mean EMA compliance 79.2% across 477 articles, with 43% of studies below the conventional 80% threshold (Wrzus & Neubauer 2023); permission and authorization failures reported by Slade et al. 2025.

### Metadata, provenance and protocol layer

#### `ACQ-F06` — Mid-study protocol / firmware / configuration change

signature

Discontinuity not marked in the data.

property threatened

**\[M\]** **\[EN\]** Measurement performance may change; the change is not recorded and prior verification is not transferable across it.

evidence

**\[L\]** A January 2019 Google Play policy change cut call- and text-log collection mid-recruitment in RADAR-MDD (Matcham et al. 2022); \[E\] protocols frequently changed without being versioned.

#### `ACQ-F07` — Missing schema / software / firmware provenance

signature

Dataset not machine-interpretable or re-executable.

property threatened

**\[EN\]** Severs the provenance chain from a published number back to the act of measurement — the record-fidelity analogue of, but distinct from, metrological traceability.

evidence

**\[E\]** Compare datasheets for datasets (Gebru et al. 2021).

#### `ACQ-F08` — No accuracy or uncertainty statement

signature

Numbers reported without stated uncertainty.

property threatened

**\[M\]** Measurement uncertainty unstated (JCGM 2008, GUM).

evidence

**\[L\]** Under-reported for wearables with no standardized characterization protocol (Cosoli et al. 2024); over 70% of surveyed light-dosimetry studies reported no sensor calibration (Spitschan et al. 2022).

## Source

The machine-readable taxonomy is [`taxonomy/acquire-taxonomy.yml`](https://github.com/acquire-framework/acquire-framework.github.io/blob/main/taxonomy/acquire-taxonomy.yml).

Contribute a failure case — particularly one with a quantified field rate — via the [failure-case issue template](https://github.com/acquire-framework/acquire-framework.github.io/issues/new?template=failure-case.yml). Negative reports are also valuable.

## Citation

BibTeX citation:

``` quarto-appendix-bibtex
@inproceedings{daniol2026acquire,
  author = {Danioł, Mateusz and Sroka, Ryszard},
  publisher = {Association for Computing Machinery},
  title = {Reproducibility {Begins} at {Acquisition:} {The} {ACQUIRE}
    {Framework} for {Trustworthy} {In-the-Wild} {Sensing}},
  booktitle = {Companion of the 2026 ACM International Joint Conference
    on Pervasive and Ubiquitous Computing (UbiComp/ISWC ’26 Companion)},
  date = {2026},
  address = {Shanghai, China},
  url = {https://acquire-framework.github.io},
  langid = {en}
}
```

For attribution, please cite this work as:

Danioł, Mateusz, and Ryszard Sroka. 2026. “Reproducibility Begins at Acquisition: The ACQUIRE Framework for Trustworthy In-the-Wild Sensing.” *Companion of the 2026 ACM International Joint Conference on Pervasive and Ubiquitous Computing (UbiComp/ISWC ’26 Companion)* (Shanghai, China). <https://acquire-framework.github.io>.
