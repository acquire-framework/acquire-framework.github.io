# Stuck sensor reporting stale values

The most dangerous failure in the catalogue: the stream looks perfectly healthy.

hardware

monitoring

A sensor stops updating but continues emitting its last value. Data arrives on schedule, so arrival-based monitoring reports success.

●○○○ evidence: anecdotal

> **NOTE:**
>
> **Recipe SIG-02 · [Stage: monitor](../lifecycle/monitor.llms.md) · Last reviewed 2026-07-18**

## Symptom

Sample count is correct, timing is correct, files arrive on schedule — and the values do not change. Plotted at study scale the signal is a flat line; plotted at the scale most dashboards use, it is indistinguishable from a participant sitting still.

## Root cause

A driver or firmware fault leaves the sensor’s output register holding its last value while the delivery pipeline continues to run. Reported causes include firmware faults after a suspend/resume cycle, I²C bus errors that are retried silently, and BLE characteristic caching on the host.

This is the most dangerous entry in the catalogue precisely because it defeats the monitoring most studies actually deploy. “Is data arriving?” answers yes. “Is the data changing?” is the question that had to be asked.

## Detection

Genuine stillness still produces sensor noise. **Exactly repeated values across all three axes are therefore a hardware fault, not a quiet participant** — a distinction that makes this detectable with no thresholds to tune.

Concretely: test successive samples for bit-identical values across all three axes, and report the longest such run. The only parameter is how long a frozen run must be before it counts as a fault — longer than any plausible period of stillness, so minutes rather than seconds.

## Evidence

The test is exact rather than statistical, which is unusual in this catalogue: bit-identical repetition either occurred or it did not.

**No field observation yet.** This recipe is included because the failure is well attested in hardware literature and because the test is trivially verifiable, not because it has been observed in a deployment by the authors.

**This recipe is unevidenced in the field.** If you have encountered a stuck sensor in a real deployment — device model, firmware version, and what triggered recovery — that report would move it to `●●○○` and is genuinely valuable.

## Mitigation

1.  **Monitor signal variance, not just data arrival.** This is the single change that catches it, and most telemetry setups do not do it. See [monitor](../lifecycle/monitor.llms.md).
2.  **Alert on zero variance over a window longer than plausible stillness** — minutes, not seconds.
3.  **Implement a watchdog that re-initialises the sensor** when variance collapses, and log every re-initialisation as an event.
4.  **Treat a recovered stuck period as missing data, not as valid rest.** It is censored, not observed.

## Citation

BibTeX citation:

``` quarto-appendix-bibtex
@software{acquire_2026,
  author = {Danioł, Mateusz and Sroka, Ryszard},
  title = {ACQUIRE: {Acquisition} {Criteria} for {Quality,}
    {Uncertainty,} {Integrity,} {Reproducibility,} and {Evidence}},
  version = {26.7.2},
  date = {2026},
  url = {https://acquire-framework.github.io},
  langid = {en}
}
```

For attribution, please cite this work as:

Danioł, Mateusz, and Ryszard Sroka. 2026. *ACQUIRE: Acquisition Criteria for Quality, Uncertainty, Integrity, Reproducibility, and Evidence*. V. 26.7.2. Released. <https://acquire-framework.github.io>.
