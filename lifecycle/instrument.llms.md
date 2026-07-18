# Instrument

Building the acquisition app and the telemetry that tells you it is working.

This is where most preventable failures are introduced, and where almost all of them can be made detectable. The guiding principle: **assume every component will fail silently, and instrument accordingly.**

## Checklist

### Error and crash reporting

**INST-01** — Crash and error reporting is embedded in the acquisition app (Sentry, GlitchTip, or equivalent) and verified to deliver from a real device, not only from the emulator.

**INST-02** — Reports are scrubbed of participant identifiers and raw signal content before transmission, and this scrubbing is tested.

**INST-03** — A self-hosted option is used where ethics approval or data residency requires it. GlitchTip is API-compatible with Sentry clients and can be self-hosted, which usually resolves this constraint without changing application code.

### Sampling integrity

**INST-04** — Effective sampling rate is verified against nominal on every device model before deployment. → [Silent downsampling](../recipes/03-doze-downsampling.llms.md)

**INST-05** — The app runs as a foreground service (Android) or declares the appropriate background modes (iOS), and this is verified on the oldest and cheapest handset in the fleet, where vendor power management is most aggressive.

**INST-06** — The nominal sampling rate is recorded in dataset metadata. Without it, downsampling is undetectable after the fact.

### Time

**INST-07** — Both a monotonic timestamp and wall-clock time are recorded. One is for ordering, the other for relating data to the world. → [Clock drift](../recipes/01-clock-drift.llms.md)

**INST-08** — NTP corrections are logged as events so they can be undone.

**INST-09** — Multi-device studies include a deliberate synchronisation event (a shared tap, marker, or signal) at each session start.

### Units and calibration

**INST-10** — Units are recorded explicitly in metadata. “Accelerometer” is not a unit. → [Unit and scale mismatch](../recipes/02-unit-scale-mismatch.llms.md)

**INST-11** — A static calibration recording (device level and still for ~60 s) is captured at enrolment for every device.

**INST-12** — Sensor range is configured for the most vigorous activity in the protocol, and the configured range is recorded. → [Range saturation](../recipes/05-range-saturation.llms.md)

### Request and transfer logging

**INST-13** — Every upload attempt is logged with outcome, size, and device-side timestamp, so gaps can later be attributed to collection versus transfer.

**INST-14** — The app records its own version and build with every recording, so behaviour changes can be attributed to releases.

**INST-15** — Local buffering survives app restart and device reboot, and this has been tested by actually restarting and rebooting.

## Why telemetry is not enough

Crash reporting tells you when the app *stopped*. It cannot tell you when the app kept running and collected invalid data — which is the failure mode that costs studies most. Telemetry is necessary and insufficient; pair it with the validity monitoring described in [monitor](../lifecycle/monitor.llms.md).

## Next

→ [Pilot](../lifecycle/pilot.llms.md): smoke-test the whole chain before anything scales.

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
