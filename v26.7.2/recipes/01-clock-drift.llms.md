**ACQUIRE 26.7.2** — a fixed snapshot of the specification, built 2026-07-19 from commit `32d64e8`. Thresholds and recipes change as evidence accumulates. [See the current version](https://acquire-framework.github.io/).

# Clock drift and reset across devices

Timestamps that cannot be trusted make every windowed analysis meaningless.

timing

multi-device

Device clocks drift, jump on NTP correction, and reset on reboot. Multi-device studies lose alignment silently.

●○○○ evidence: anecdotal

> **NOTE:**
>
> **Recipe TIME-03 · [Stage: instrument](../lifecycle/instrument.llms.md) · Last reviewed 2026-07-18**

## Symptom

Timestamps step backwards, jump forwards, or accumulate offset relative to a second device recording the same event. Where two streams should align, features appear shifted by seconds to minutes — enough to destroy any cross-device analysis without producing an obviously broken file.

## Root cause

Three distinct mechanisms, often conflated:

- **Reset.** The device reboots or the user changes timezone; a clock based on wall time jumps discontinuously.
- **Correction.** NTP synchronisation applies a step correction mid-recording.
- **Drift.** The oscillator runs fast or slow. Consumer hardware drifts on the order of seconds per day, and the rate varies with temperature.

Recording wall-clock time alone cannot distinguish these. Recording a monotonic clock alone cannot relate the data to anything external.

## Detection

Backward steps are detectable from a single recording and gate every other timing check, because windowing a non-monotonic series is meaningless.

Concretely: take the successive differences of the timestamp column and test whether any is zero or negative. A single backward step invalidates every windowed statistic computed downstream, so this test should gate the others rather than run alongside them.

## Evidence

**A limitation stated plainly:** modest drift is *not* detectable from a single recording. Nothing in the data distinguishes “the clock ran fast” from “sampling ran slow” — both stretch elapsed time identically. Detecting drift requires an external reference: a second device, an NTP query logged alongside the data, or a deliberate synchronisation event.

This is why clock agreement appears in the framework’s `NOT_CHECKED` list rather than as a check that quietly under-performs.

Only gross drift, large enough to breach the sampling-rate tolerance, surfaces indirectly through [TIME-01](../recipes/03-doze-downsampling.llms.md).

**This recipe needs work.** A validated cross-device drift detector — given two recordings with a shared event — would be a substantial contribution and is currently unimplemented.

## Mitigation

1.  **Record both clocks.** Log a monotonic timestamp *and* wall time for every sample or every batch. One is for ordering, the other for relating to the world.
2.  **Log NTP offset** whenever the device syncs, so corrections can be undone.
3.  **Design in a synchronisation event.** Ask participants to tap all devices together at the start of each session, or emit a shared marker. A known common event makes drift measurable after the fact.
4.  **Never merge streams on wall time alone** without first checking alignment.

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
