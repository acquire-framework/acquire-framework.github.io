# Templates and forms

Fill-in artifacts for the disclosures the checklist asks for.

Each template corresponds to items of the [Minimum Reporting Checklist](../checklist/index.llms.md). They are shown in full below and can be downloaded directly.

| Template | Satisfies | Download |
|:---|:---|:---|
| [Sensor schema](#sensor-schema) | MRC-08 | [`sensor-schema.yml`](sensor-schema.yml) |
| [Quality flags](#quality-flags) | MRC-01, 02, 09 | [`quality-flags.yml`](quality-flags.yml) |
| [Uncertainty statement](#uncertainty-statement) | MRC-05 | [`uncertainty-statement.md`](uncertainty-statement.md) |
| [Dataset provenance](#dataset-provenance) | MRC-03, 09 | [`dataset-provenance.yml`](dataset-provenance.yml) |
| [Reviewer form](#reviewer-form) | all | [`reviewer-form.md`](reviewer-form.md) |

## Sensor schema

Publish one per sensor stream, alongside the data. Without it a dataset is not machine-interpretable: a reader cannot tell what was measured, in what units, at what nominal rate, or against what expectation — and so cannot check the data for the failures the taxonomy catalogues.

The nominal rate matters most. It cannot be inferred from the data, because inferring it would define away [ACQ-F01](../taxonomy/index.llms.md), the best-quantified failure in the taxonomy.

``` yaml
# SPDX-License-Identifier: CC-BY-4.0
# SPDX-FileCopyrightText: 2026 Mateusz Danioł, Ryszard Sroka
# ACQUIRE sensor schema template — satisfies MRC-08.
#
# Publish one of these per sensor stream, alongside the data. Without it a
# dataset is not machine-interpretable: a reader cannot tell what was measured,
# in what units, at what nominal rate, or against what expectation — and so
# cannot check the data for the failures this framework catalogues.
#
# Replace every <angle-bracketed> value. Fields marked REQUIRED are the minimum
# for the dataset to be assessable at all.

schema_version: "0.1.0"
stream_id: <e.g. wrist_accelerometer>          # REQUIRED, unique in the dataset

measurand:
  quantity: <e.g. proper acceleration>          # REQUIRED — what is measured
  derived: <true|false>                         # REQUIRED — raw or computed?
  derivation: <if derived, the procedure and its software version>

signal:
  channels: [<ax>, <ay>, <az>]                  # REQUIRED
  unit: <e.g. m/s^2>                            # REQUIRED — "accelerometer" is not a unit
  nominal_rate_hz: <e.g. 50>                    # REQUIRED — cannot be inferred from data;
                                                # inferring it would define away the most
                                                # common failure in the taxonomy
  range: <e.g. ±8 g>                            # REQUIRED — needed to identify saturation
  resolution: <e.g. 16 bit>
  axis_convention: <e.g. right-handed, +z out of screen>

time:
  timestamp_field: <e.g. timestamp>             # REQUIRED
  representation: <epoch_ms | iso8601 | seconds_since_start>   # REQUIRED
  source: <device_rtc | host_clock | monotonic + host reconciliation>  # REQUIRED
  timezone: <e.g. UTC>
  synchronization_policy: <e.g. reconciled to phone at each BLE reconnection>
  residual_uncertainty: <e.g. U = 46 ms (k=2), estimated from logged offsets>

instrument:
  device_model: <e.g. Polar H10>                # REQUIRED
  firmware_version: <REQUIRED, and every mid-study change>
  app_version: <REQUIRED, and every mid-study change>
  os_version: <e.g. Android 14>
  calibration:
    performed: <true|false>                     # REQUIRED
    procedure: <e.g. 60 s static recording, device level, at enrolment>
    reference: <reference instrument, or "none">
    date: <YYYY-MM-DD>

quality:
  flags_file: <path to quality-flags.yml>
  known_limitations: <state them; silence reads as "none known">

provenance:
  collection_software: <URL and commit hash>    # REQUIRED
  raw_record: <path or archive identifier for the append-only raw log>
  processing: <path to dataset-provenance.yml>
```

## Quality flags

A flag is only interpretable if the reader knows the threshold that produced it and what applied it. The `not_covered` section is the important one: a reader who sees only green flags will otherwise infer a validation that never ran.

``` yaml
# SPDX-License-Identifier: CC-BY-4.0
# SPDX-FileCopyrightText: 2026 Mateusz Danioł, Ryszard Sroka
# ACQUIRE quality-flag template — supports MRC-01, MRC-02, MRC-09.
#
# A quality flag records a judgement about a span of data. The point of writing
# them down in this form is that a flag is only interpretable if the reader
# knows the threshold that produced it and who or what applied it.
#
# The cautionary case from the paper: a conventional quality audit passes a
# dataset in which two device clocks have drifted hundreds of milliseconds
# apart. Completeness is 100%, no values are impossible, every flag is green —
# and any inter-modal measurand is invalid. Green flags are evidence about the
# checks that ran, never about the checks that did not.

schema_version: "0.1.0"
stream_id: <matches sensor-schema.yml>

# Every flag definition states its threshold and its provenance.
definitions:
  - flag: rate_deficit
    description: Effective sampling rate below nominal beyond tolerance
    threshold: <e.g. |1 - effective/nominal| > 0.05>
    applied_by: <e.g. acquire v26.7, check TIME-01>
    property: O

  - flag: gap
    description: Interruption in the stream longer than the stated limit
    threshold: <e.g. inter-sample interval > 1.0 s>
    applied_by: <e.g. acquire v26.7, check TIME-02>
    property: O

  - flag: clock_nonmonotonic
    description: Timestamps not strictly increasing
    threshold: any backward step
    applied_by: <e.g. acquire v26.7, check TIME-03>
    property: M

  - flag: unit_scale_suspect
    description: Resting magnitude departs from one standard gravity
    threshold: <e.g. |1 - observed/9.80665| > 0.02>
    applied_by: <e.g. acquire v26.7, check SIG-01>
    property: M

  - flag: sensor_stuck
    description: All channels bit-identical across consecutive samples
    threshold: <e.g. frozen run > 2 s>
    applied_by: <e.g. acquire v26.7, check SIG-02>
    property: M

  - flag: saturation
    description: Samples censored at the configured range
    threshold: <e.g. > 0.1% of samples at the rail>
    applied_by: <e.g. acquire v26.7, check SIG-03>
    property: M

# What these flags do NOT cover. State this explicitly: a reader who sees only
# green flags will otherwise infer a validation that was never performed.
not_covered:
  - Calibration against a reference instrument
  - Agreement between device clocks, or with wall time
  - Whether the participant wore or carried the device as instructed
  - Whether recorded activity matches any label or diary entry
  - <add every check your study did not run>

spans:
  - stream_id: <stream>
    participant: <pseudonymous id>
    start: <timestamp>
    end: <timestamp>
    flag: <flag name>
    value: <measured value that triggered it>
    action: <excluded | retained_with_caveat | corrected>
    note: <free text>
```

## Uncertainty statement

Part A is the quantitative budget. Part B is the justification route permitted by MRC-05, with the floor that keeps it from becoming a null answer: name the dominant sources, state why each could not be quantified, describe the validation evidence offered instead.

``` markdown
# Uncertainty statement template — satisfies MRC-05

One statement per primary derived measurand. If a measurand is reported in a
results section, it needs one of these or a justification meeting the floor in
Part B.

This is a *design-stage* budget unless you state otherwise. A budget evaluated
from declared assumptions is not an empirical uncertainty statement about a
deployed system, and conflating the two is itself a reporting failure.

---

## Part A — quantitative budget

**Measurand:** `<e.g. pulse-arrival time, from ECG–PPG latency>`

**Measurement model:** state the equation relating the measured value to the
true value and every error term. For a two-device latency measurand:
```

Δt_meas = Δt_true + δ_A − δ_B + δ_sync,rel + δ_host


    where `δ_A`, `δ_B` are clock errors accumulated since the last re-anchor,
    `δ_sync,rel` is the residual *relative* synchronization error after
    reconciliation (common-mode error has already cancelled here), and `δ_host` is
    host-side timestamping uncertainty not already contained in `δ_sync,rel`.

    **Budget:**

    | Component | Assumed or measured limit | Distribution | Divisor | u_i |
    |:--|--:|:-:|--:|--:|
    | `<δ_A drift, 30 ppm over 900 s>` | `<±27 ms>` | rectangular | √3 | `<15.6>` |
    | `<δ_B drift>` | `<±27 ms>` | rectangular | √3 | `<15.6>` |
    | `<δ_sync,rel residual>` | `<±10 ms>` | rectangular | √3 | `<5.8>` |
    | `<δ_host timestamping>` | `<±2 ms>` | rectangular | √3 | `<1.2>` |
    | **Combined u_c** | | | | `<22.8>` |
    | **Expanded U = k·u_c, k = 2** | | | | **`<45.6>`** |

    **Basis of each limit:** for every row, state whether it is measured from your
    own logs, taken from a datasheet, or assumed. Values inherited from a citation
    that measured something else are assumptions, not measurements — label them so.

    **Correlation assumptions:** state which components are treated as independent
    and why. Where independence is not defensible, estimate the covariances or work
    directly from empirical offset distributions.

    **Double-counting check:** if `δ_sync,rel` was estimated empirically from
    end-to-end offset logs, host-side effects already inside that estimate must not
    be added again as a separate `δ_host`.

    **Fitness for purpose:** `<U ≈ 46 ms is negligible for daily step counts and
    material for cross-modal latency estimation. The same dataset can be fit for one
    purpose and unfit for another; state which.>`

    ---

    ## Part B — justification, where a budget could not be established

    MRC-05 permits a documented justification instead of a budget. To carry
    information, that justification must contain all three of the following.
    "Uncertainty could not be established" alone does not satisfy the item.

    1. **Dominant uncertainty sources**, named. Which terms would appear in the
       budget if you could evaluate them?
    2. **Why each could not be quantified.** No reference instrument available? No
       access to firmware timing behaviour? Vendor does not disclose the sampling
       implementation?
    3. **What validation evidence is offered instead** — bench comparison,
       concurrent-device agreement, published device validation with a statement of
       whether its conditions match yours (bench repeatability evidence does not
       transfer to a multi-month multi-device field deployment).

    ---

    ## Reporting language

    Replace silence with a statement. Before:

    > "Signals from both devices were recorded continuously and timestamped."

    After:

    > "Device clocks were reconciled to the phone at each BLE reconnection; residual
    > cross-device synchronization uncertainty, estimated from logged offsets, was
    > U = `<X>` ms (k = 2); PAT is reported with this uncertainty, and windows
    > exceeding `<Z>` ms were excluded."

## Dataset provenance

Records the auditable lineage from a published number back to the act of measurement — the record-fidelity analogue of metrological traceability, and distinct from it.

Provenance reconstructed at the end of a study is a best-effort narrative; provenance recorded as data arrives is evidence.

``` yaml
# SPDX-License-Identifier: CC-BY-4.0
# SPDX-FileCopyrightText: 2026 Mateusz Danioł, Ryszard Sroka
# ACQUIRE dataset provenance template — satisfies MRC-03 and MRC-09.
#
# Records the auditable lineage from a published number back to the act of
# measurement. This is the record-fidelity analogue of metrological
# traceability, and distinct from it.
#
# Provenance reconstructed at the end of a study is a best-effort narrative.
# Provenance recorded as data arrives is evidence. The difference costs almost
# nothing during collection and cannot be recovered afterwards.

schema_version: "0.1.0"
dataset:
  name: <dataset name>
  version: <e.g. 1.0.0>                 # REQUIRED — analyses must cite a version
  doi: <DOI or archive URL>
  licence: <e.g. CC-BY-4.0>
  released: <YYYY-MM-DD>

# ── the instrument, and every change to it ────────────────────────────────────
# A mid-study change means prior verification does not transfer across it.
instrument_history:
  - from: <YYYY-MM-DD>
    to: <YYYY-MM-DD | ongoing>
    device_model: <e.g. Polar H10>
    firmware_version: <version>
    app_version: <version>
    os_versions: [<Android 13>, <Android 14>]
    change_reason: <initial deployment | firmware update | vendor policy change>
    verification_transferred: <true|false>
    note: >-
      <If false, say what was re-verified after the change and what was not.
      Externally imposed changes — an OS policy change mid-recruitment, for
      instance — belong here even though you did not initiate them.>

# ── the raw record ────────────────────────────────────────────────────────────
raw_record:
  append_only: <true|false>             # REQUIRED
  integrity: <e.g. SHA-256 payload checksums, sequence numbers, server dedup>
  location: <archive identifier>
  retained: <true|false>
  note: <if raw records were not retained, say so plainly and explain why>

# ── from raw to released ──────────────────────────────────────────────────────
# Every processed product derives from the raw record by re-executable steps.
processing:
  - step: <e.g. resample to 50 Hz>
    software: <package and version>
    code: <URL and commit hash>
    inputs: <path or identifier>
    outputs: <path or identifier>
    parameters: <the parameters actually used>

# ── quality control ───────────────────────────────────────────────────────────
quality_control:
  checks_applied: <name and version of the validation software used>
  report: <path to the emitted validation report>
  exclusion_criteria:
    - criterion: <e.g. effective rate below 95% of nominal>
      rationale: <why this threshold>
      excluded_n: <count>
  excluded_summary: >-
    <Report exclusions in aggregate so a reader can judge selection effects.
    A dataset reporting "9% of recordings failed the sampling-rate check and
    were excluded" is more useful and more credible than one reporting nothing.>

# ── observation process ───────────────────────────────────────────────────────
# Distinct from the two sections above: this is about which observations exist,
# not whether the ones that exist are valid or faithfully retained.
observation_process:
  expected_completeness: <what the protocol called for>
  observed_completeness: <what was obtained, per modality>
  attribution:
    technical: <estimate and the evidence used>
    adherence: <estimate and the evidence used>
    attrition: <estimate and the evidence used>
    note: >-
      <If these cannot be separated, say so. Most published completeness
      figures aggregate all three without stating it, which is precisely the
      failure this field records.>

# ── limits ────────────────────────────────────────────────────────────────────
known_limitations:
  - <state them; an empty list reads as "none known", which is rarely true>
not_checked:
  - <every validity property this dataset does not establish>
```

## Reviewer form

For reviewing a manuscript or dataset reporting in-the-wild sensor data. Its purpose is to let a reviewer request *specific* acquisition details instead of “more detail on data quality”, which authors cannot act on.

Note the proportionality rule and the instruction that absence of a disclosure is a finding rather than a failing — the form should not push authors toward false precision.

``` markdown
# ACQUIRE reviewer form v26.7

For reviewing a manuscript or dataset that reports in-the-wild sensor data.

Its purpose is to let a reviewer request **specific** acquisition details
instead of "more detail on data quality", which authors cannot act on.

**Proportionality.** Requirements should be set against the intended measurand
and the study's risk, not applied uniformly. Tens of milliseconds of clock error
are negligible for daily step counts and disqualifying for cross-modal latency.
Judge each item against what the paper claims to measure — do not demand a full
uncertainty budget from a step-count study.

**Absence of a disclosure is a finding, not a failing.** Many groups genuinely
cannot produce some of these. An honest "we did not measure this" is a better
outcome than a fabricated number, and reviewers should say so explicitly rather
than pushing authors toward false precision.

---

## A. Measurement validity [M]

| | Question | Reported? | Note |
|:--|:--|:-:|:--|
| A1 | Are device models, firmware, app and OS versions stated, including mid-study changes? | ☐ | |
| A2 | Is the timestamping source stated (device RTC / host / monotonic)? | ☐ | |
| A3 | Is the synchronization policy stated, and the residual uncertainty after reconciliation? | ☐ | |
| A4 | Is there an accuracy or uncertainty statement for each primary derived measurand, or a justification meeting the floor (sources named, reasons given, substitute evidence described)? | ☐ | |
| A5 | If device validation is cited, does it match the study's conditions? Bench repeatability evidence does not transfer to a multi-month, multi-device field deployment. | ☐ | |
| A6 | Was calibration performed, and is the procedure stated? | ☐ | |

## B. Record integrity and provenance [EN]

| | Question | Reported? | Note |
|:--|:--|:-:|:--|
| B1 | Is a machine-readable schema published with the data? | ☐ | |
| B2 | Is the collection software available, with version or commit? | ☐ | |
| B3 | Is upload retry, deduplication and integrity-verification logic described? | ☐ | |
| B4 | Are context and system-health events recorded alongside the data (power, connectivity, permissions, crashes, service kills)? | ☐ | |
| B5 | Is a raw record retained, and is preprocessing provenance from raw to released traceable? | ☐ | |
| B6 | Are QC exclusion criteria stated, with counts? | ☐ | |

## C. Observation-process validity [O]

| | Question | Reported? | Note |
|:--|:--|:-:|:--|
| C1 | Is expected versus observed completeness reported per modality? | ☐ | |
| C2 | Is the background-execution / sampling policy stated? | ☐ | |
| C3 | Is missingness attributed to technical loss, adherence, or attrition — with the evidence used, or an explicit statement that they cannot be separated? | ☐ | |
| C4 | Is the possibility of non-random loss addressed where the estimand is time-aggregated or population-level? | ☐ | |
| C5 | Were participants told which OS features must remain enabled, and is that reported as part of the method? | ☐ | |

## D. Verification

| | Question | Reported? | Note |
|:--|:--|:-:|:--|
| D1 | Is pre-deployment verification evidence given — which failure modes were tested, how, with what result? | ☐ | |
| D2 | Did the pilot cover realistic conditions (overnight idle, aggressive vendor optimizers, offline periods, reboot)? | ☐ | |

---

## Reviewer summary

**Most consequential omission, and why it matters for *this* study's claims:**

> `<one paragraph>`

**Requested disclosures**, in priority order — be specific enough that the
author knows exactly what to add:

1. `<e.g. "State the nominal sampling rate and the observed effective rate per
   device model. Without the nominal rate, silent downsampling is undetectable
   by any reader.">`
2.
3.

**Where absence is acceptable**, and should be stated rather than filled in:

> `<e.g. "A full uncertainty budget is disproportionate for this measurand; a
> statement that synchronization uncertainty was not characterised, with the
> reason, would suffice.">`

---

*ACQUIRE MRC v26.7. The checklist has not been evaluated for usability, coverage,
or inter-rater agreement; no claim is made that applying it improves study
outcomes. Feedback on the form itself is welcome as a repository issue.*
```

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
