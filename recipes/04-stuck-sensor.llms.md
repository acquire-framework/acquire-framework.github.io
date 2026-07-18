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

Genuine stillness still produces sensor noise. **Exactly repeated values across all three axes are therefore a hardware fault, not a quiet participant** — a distinction that makes this detectable with no thresholds to tune:

``` python
import acquire
from acquire.synth import Fault, clean, inject

df = inject(clean(duration_s=900, seed=4), Fault("stuck", start=300, end=400))

next(r for r in acquire.check(df, nominal_hz=50).results if r.id == "SIG-02")
```

    CheckResult(id='SIG-02', title='Stuck sensor', passed=np.False_, value='longest frozen run 100.0 s', expected='≤ 2.0 s', detail='All three axes identical across consecutive samples. Genuine stillness still produces sensor noise, so exact repetition is a hardware or driver fault, not a quiet participant.', recipe='recipes/04-stuck-sensor.html')

## Evidence

The detector is exact rather than statistical: it reports the longest run of bit-identical consecutive samples. The only tunable is how long a frozen run must be before it is called a fault, defaulting to two seconds.

**No field observation yet.** This recipe is included because the failure is well attested in hardware literature and because the detector is trivially verifiable, not because it has been observed in a deployment by the authors.

**This recipe is unevidenced in the field.** If you have encountered a stuck sensor in a real deployment — device model, firmware version, and what triggered recovery — that report would move it to `●●○○` and is genuinely valuable.

## Mitigation

1.  **Monitor signal variance, not just data arrival.** This is the single change that catches it, and most telemetry setups do not do it. See [monitor](../lifecycle/monitor.llms.md).
2.  **Alert on zero variance over a window longer than plausible stillness** — minutes, not seconds.
3.  **Implement a watchdog that re-initialises the sensor** when variance collapses, and log every re-initialisation as an event.
4.  **Treat a recovered stuck period as missing data, not as valid rest.** It is censored, not observed.

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
