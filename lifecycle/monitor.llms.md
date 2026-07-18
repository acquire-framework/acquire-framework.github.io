# Monitor

Not ‘is data arriving?’ but ‘is the arriving data valid?’

This is the stage that separates studies which recover from failure from studies which discover it too late. Almost every deployed monitoring setup answers the wrong question.

## Two questions, only one of which is usually asked

**“Is data arriving?”** — answered by uptime checks, file counts, and crash reporting. Necessary, and satisfied by every failure in this catalogue except an outright crash. A throttled stream arrives. A stuck sensor arrives. Data in the wrong units arrives.

**“Is the arriving data valid?”** — answered by running diagnostics over incoming data continuously. This is the question that catches silent failure.

## Checklist

### Infrastructure

**MON-01** — Error and crash telemetry is deployed and confirmed to deliver from production devices (Sentry, GlitchTip, or equivalent).

**MON-02** — Alerts route to a person who is on duty, with a stated expectation of response time. An alert into an unwatched channel is not monitoring.

**MON-03** — Alerting has been deliberately triggered at least once to confirm the whole path works end to end.

### Validity monitoring

**MON-04** — Effective sampling rate per device is computed on ingestion and alerted on when it deviates from nominal. → [Silent downsampling](../recipes/03-doze-downsampling.llms.md)

**MON-05** — Signal variance is monitored, with alerting on collapse to zero over a window longer than plausible stillness. → [Stuck sensor](../recipes/04-stuck-sensor.llms.md)

**MON-06** — Data yield per participant per day is tracked against the minimum acceptable threshold defined at [design](../lifecycle/design.llms.md) time.

**MON-07** — Validity checks run automatically over incoming data, not on request — in the ingestion pipeline rather than by hand.

**MON-08** — Detection latency is measured — how long between a failure starting and someone knowing — and reported.

## Measuring detection latency

Detection latency is worth measuring explicitly, because it is the quantity that determines how much data a failure costs. A study that detects throttling within a day loses a day; one that detects it at analysis loses everything.

## Next

→ [Curate](../lifecycle/curate.llms.md): version and document data as it accumulates.

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
