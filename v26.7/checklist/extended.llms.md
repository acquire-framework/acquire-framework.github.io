**Version 26.7** — a fixed snapshot, built 2026-07-18 from commit `a11dbb0`. Thresholds and recipes change as evidence accumulates. [See the current version](https://acquire-framework.github.io/).

# Extended operational checklist

For building a study, not for reporting one.

> **NOTE:**
>
> **This is not the paper’s checklist.** The paper’s instrument is the ten-item [Minimum Reporting Checklist](../checklist/index.llms.md), which specifies what a study should *disclose* so a reader can assess it.
>
> This longer list is an operational companion covering what a team should *do*, stage by stage, so that the MRC can be answered honestly at the end. Most of these decisions never appear in a methods section. It is offered as practice, not as a reporting standard, and carries no claim to completeness.

Each item maps to the MRC item it ultimately serves, or to a taxonomy row it guards against.

**Version 26.7** · updated 2026-07-18 · 65 items

**Study types used for filtering:**

- `mobile-imu` — Inertial data collected via a mobile application
- `wearable-ble` — Data collected from a BLE wearable device
- `multi-device` — Two or more devices recording concurrently
- `longitudinal` — Collection spanning weeks or months

## Items by stage

### Design

8 items

|  | Statement | Applies to | Guards against |
|:---|:---|:---|:---|
| `DSGN-01` | The required sampling rate was derived from the phenomenon being measured, not inherited from a previous study or an SDK default. | `mobile-imu`, `wearable-ble` |  |
| `DSGN-02` | A minimum acceptable data yield per participant was stated in advance, together with the analysis consequence of falling below it. | `longitudinal` |  |
| `DSGN-03` | Explicit validity criteria were written down before collection began. | `mobile-imu`, `wearable-ble` |  |
| `DSGN-04` | The measurement range required by the most vigorous activity in the protocol was calculated rather than assumed. | `mobile-imu`, `wearable-ble` | [detail](../recipes/05-range-saturation.llms.md) |
| `DSGN-05` | Device and OS diversity in the intended population was enumerated, including the oldest hardware permitted. | `mobile-imu` |  |
| `DSGN-06` | Battery and storage budgets were computed for the intended duration and rate on the worst-case device. | `mobile-imu`, `longitudinal` |  |
| `DSGN-07` | Consent and ethics documentation covers telemetry and crash reporting, not only the primary sensor data. | `mobile-imu`, `wearable-ble` |  |
| `DSGN-08` | A data management plan exists naming where raw data lives, who can access it, and how long it is retained. | `mobile-imu`, `wearable-ble` |  |

### Instrument

15 items

|  | Statement | Applies to | Guards against |
|:---|:---|:---|:---|
| `INST-01` | Crash and error reporting is embedded in the acquisition application and verified to deliver from a real device. | `mobile-imu` |  |
| `INST-02` | Telemetry reports are scrubbed of participant identifiers and raw signal content, and the scrubbing is tested. | `mobile-imu` |  |
| `INST-03` | Where data residency or ethics approval requires it, a self-hosted telemetry backend is used. | `mobile-imu` |  |
| `INST-04` | Effective sampling rate was verified against nominal on every device model before deployment. | `mobile-imu`, `wearable-ble` | [detail](../recipes/03-doze-downsampling.llms.md) |
| `INST-05` | The application runs as a foreground service or declares appropriate background modes, verified on the oldest handset in the fleet. | `mobile-imu` | [detail](../recipes/03-doze-downsampling.llms.md) |
| `INST-06` | The nominal sampling rate is recorded in dataset metadata. | `mobile-imu`, `wearable-ble` | [detail](../recipes/03-doze-downsampling.llms.md) |
| `INST-07` | Both a monotonic timestamp and wall-clock time are recorded. | `mobile-imu`, `wearable-ble` | [detail](../recipes/01-clock-drift.llms.md) |
| `INST-08` | NTP corrections are logged as events so they can be undone. | `multi-device` | [detail](../recipes/01-clock-drift.llms.md) |
| `INST-09` | A deliberate synchronisation event is recorded at the start of each session. | `multi-device` | [detail](../recipes/01-clock-drift.llms.md) |
| `INST-10` | Units are recorded explicitly in dataset metadata. | `mobile-imu`, `wearable-ble` | [detail](../recipes/02-unit-scale-mismatch.llms.md) |
| `INST-11` | A static calibration recording was captured at enrolment for every device. | `mobile-imu`, `wearable-ble` | [detail](../recipes/02-unit-scale-mismatch.llms.md) |
| `INST-12` | Sensor range is configured for the most vigorous activity in the protocol, and the configured range is recorded. | `mobile-imu`, `wearable-ble` | [detail](../recipes/05-range-saturation.llms.md) |
| `INST-13` | Every upload attempt is logged with outcome, size, and device-side timestamp. | `mobile-imu`, `longitudinal` |  |
| `INST-14` | Application version and build are recorded with every recording. | `mobile-imu` |  |
| `INST-15` | Local buffering survives application restart and device reboot, verified by actually restarting and rebooting. | `mobile-imu`, `longitudinal` |  |

### Pilot

11 items

|  | Statement | Applies to | Guards against |
|:---|:---|:---|:---|
| `PLT-01` | At least one recording traversed the complete chain to analysis and was validated at the far end. | `mobile-imu`, `wearable-ble` |  |
| `PLT-02` | Automated diagnostics were run over pilot recordings and the results recorded. | `mobile-imu`, `wearable-ble` |  |
| `PLT-03` | The pilot ran on the oldest and cheapest device model permitted in the study. | `mobile-imu` |  |
| `PLT-04` | The pilot included at least one full overnight period. | `mobile-imu`, `longitudinal` | [detail](../recipes/03-doze-downsampling.llms.md) |
| `PLT-05` | Behaviour was verified with the device offline for a prolonged period and buffered data confirmed to arrive intact. | `mobile-imu`, `longitudinal` |  |
| `PLT-06` | Behaviour was verified across application restart and device reboot. | `mobile-imu` |  |
| `PLT-07` | Behaviour was verified under aggressive battery saving. | `mobile-imu` | [detail](../recipes/03-doze-downsampling.llms.md) |
| `PLT-08` | Behaviour was verified with storage nearly full. | `mobile-imu`, `longitudinal` |  |
| `PLT-09` | A static calibration recording confirmed resting magnitude of one g on every device model. | `mobile-imu`, `wearable-ble` | [detail](../recipes/02-unit-scale-mismatch.llms.md) |
| `PLT-10` | A vigorous-activity recording confirmed the configured range is not saturated. | `mobile-imu`, `wearable-ble` | [detail](../recipes/05-range-saturation.llms.md) |
| `PLT-11` | Monitoring and alerting were active during the pilot and at least one alert was deliberately triggered. | `mobile-imu`, `wearable-ble` |  |

### Deploy

7 items

|  | Statement | Applies to | Guards against |
|:---|:---|:---|:---|
| `DPLY-01` | Enrolment was staged, with a small first cohort validated before the remainder were enrolled. | `longitudinal` |  |
| `DPLY-02` | Each participant’s first 24 hours were validated before their data counted toward the study. | `longitudinal` |  |
| `DPLY-03` | The application version deployed to each participant is recorded, and changes during the study are logged. | `mobile-imu`, `longitudinal` |  |
| `DPLY-04` | A tested rollback path exists that does not lose buffered data. | `mobile-imu`, `longitudinal` |  |
| `DPLY-05` | Device model, OS version, and vendor are recorded per participant. | `mobile-imu` |  |
| `DPLY-06` | Participants have a documented route to report problems, and reports are logged alongside technical telemetry. | `longitudinal` |  |
| `DPLY-07` | Onboarding states explicitly what participants must not do, and compliance is verified rather than assumed. | `mobile-imu`, `longitudinal` |  |

### Monitor

8 items

|  | Statement | Applies to | Guards against |
|:---|:---|:---|:---|
| `MON-01` | Error and crash telemetry is deployed and confirmed to deliver from production devices. | `mobile-imu` |  |
| `MON-02` | Alerts route to a person on duty with a stated expected response time. | `longitudinal` |  |
| `MON-03` | Alerting was deliberately triggered at least once to confirm the whole path works. | `longitudinal` |  |
| `MON-04` | Effective sampling rate per device is computed on ingestion and alerted on when it deviates from nominal. | `mobile-imu`, `wearable-ble`, `longitudinal` | [detail](../recipes/03-doze-downsampling.llms.md) |
| `MON-05` | Signal variance is monitored with alerting on collapse to zero. | `mobile-imu`, `wearable-ble`, `longitudinal` | [detail](../recipes/04-stuck-sensor.llms.md) |
| `MON-06` | Data yield per participant per day is tracked against the minimum acceptable threshold. | `longitudinal` |  |
| `MON-07` | Diagnostics run automatically over incoming data rather than on request. | `longitudinal` |  |
| `MON-08` | Detection latency — the interval between a failure starting and someone knowing — is measured and reported. | `longitudinal` |  |

### Curate

8 items

|  | Statement | Applies to | Guards against |
|:---|:---|:---|:---|
| `CUR-01` | Raw data is stored immutably; processing produces new artifacts rather than overwriting originals. | `mobile-imu`, `wearable-ble` |  |
| `CUR-02` | Every processing step is recorded with the software version that performed it. | `mobile-imu`, `wearable-ble` |  |
| `CUR-03` | Data is versioned and any published analysis names the version it used. | `mobile-imu`, `wearable-ble` |  |
| `CUR-04` | Validation results are stored alongside the data. | `mobile-imu`, `wearable-ble` |  |
| `CUR-05` | Exclusions are recorded with reasons at the point of decision. | `mobile-imu`, `wearable-ble` |  |
| `CUR-06` | Device metadata travels with the data rather than living separately. | `mobile-imu`, `wearable-ble` |  |
| `CUR-07` | Backups exist and restoring from them has been tested. | `longitudinal` |  |
| `CUR-08` | Personal data handling matches what consent and ethics approval permit, including for telemetry. | `mobile-imu`, `wearable-ble` |  |

### Release

8 items

|  | Statement | Applies to | Guards against |
|:---|:---|:---|:---|
| `REL-01` | The dataset has a persistent identifier and a stated licence. | `mobile-imu`, `wearable-ble` |  |
| `REL-02` | Nominal sampling rate, units, sensor range, and device models are documented per recording. | `mobile-imu`, `wearable-ble` |  |
| `REL-03` | Validation results are published with the data, including failures. | `mobile-imu`, `wearable-ble` |  |
| `REL-04` | Exclusions and their reasons are reported in aggregate. | `mobile-imu`, `wearable-ble` |  |
| `REL-05` | Known limitations are stated, including failure modes that could not be checked. | `mobile-imu`, `wearable-ble` |  |
| `REL-06` | The completed ACQUIRE checklist is attached as supplementary material, with justifications for items marked not applicable. | `mobile-imu`, `wearable-ble` |  |
| `REL-07` | Code producing the released artifacts is archived at the same version as the data. | `mobile-imu`, `wearable-ble` |  |
| `REL-08` | A minimal worked example is included so a new user can reproduce one figure. | `mobile-imu`, `wearable-ble` |  |

## How this relates to the reporting checklist

The two instruments answer different questions and are used at different times.

|  | Minimum Reporting Checklist | Extended operational checklist |
|:---|:---|:---|
| **Question** | What must a reader be told? | What should a team do? |
| **Used** | When writing the methods section | Throughout the study |
| **Audience** | Authors, reviewers, curators | Engineers, PhD students, PIs |
| **Status** | The paper’s instrument, v26.7 | Practice, no standing as a standard |
| **Length** | 10 items | 65 items |

A study can complete the extended checklist and still report nothing; a study can report everything on the MRC without having done any of this. The intended relationship is that doing the first makes the second answerable with real numbers instead of silence.

## Source

[`checklist/acquire-checklist.yml`](https://github.com/acquire-framework/acquire-framework.github.io/blob/main/checklist/acquire-checklist.yml).

Items here are less settled than the MRC and were not derived by the procedure described in the paper. Disagreement is expected and welcome.

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
