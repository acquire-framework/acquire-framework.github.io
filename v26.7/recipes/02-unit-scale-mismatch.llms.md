**Version 26.7** — a fixed snapshot, built 2026-07-18 from commit `a11dbb0`. Thresholds and recipes change as evidence accumulates. [See the current version](https://acquire-framework.github.io/).

# Unit and scale mismatch

The one failure with an unambiguous physical ground truth.

units

calibration

metrology

Data recorded in g rather than m/s², or with a scale factor applied twice. Detectable from the data alone, because a device at rest measures exactly one g.

●●○○ evidence: single deployment

> **NOTE:**
>
> **Recipe SIG-01 · [Stage: instrument](../lifecycle/instrument.llms.md) · Last reviewed 2026-07-18**

## Symptom

Values are self-consistent and plausible-looking but wrong by a constant factor. Models trained on the data work; models transferred to or from another dataset fail. Thresholds tuned elsewhere behave nonsensically.

Because the data looks fine in isolation, this failure typically surfaces only when someone attempts reuse — which is precisely the reproducibility failure the framework exists to prevent.

## Root cause

- The SDK reports g; the pipeline assumes m/s² (or the reverse)
- A gravity conversion is applied twice, once in the app and once in analysis
- A vendor scale factor is applied to already-scaled values
- Axis convention differs between device and specification, changing sign but not magnitude

## Detection

This is the framework’s showcase diagnostic, because the reference value is a **physical constant rather than a convention**: a device at rest measures one standard gravity, 9.80665 m/s². Any deviation is a real measurement error, and no labelling effort is required to establish the ground truth.

``` python
import acquire
from acquire.synth import Fault, clean, inject
from acquire.schema import G

df = inject(clean(duration_s=900, seed=9), Fault("scale", factor=1 / G))  # data in g

next(r for r in acquire.check(df, nominal_hz=50).results if r.id == "SIG-01")
```

    CheckResult(id='SIG-01', title='Resting magnitude', passed=False, value='1.000 m/s² (0.102 g)', expected='9.807 m/s² ±2%', detail='Estimated from 9000 low-motion samples. Consistent with data recorded in g rather than m/s².', recipe='recipes/02-unit-scale-mismatch.html')

The detector identifies low-motion samples by rolling standard deviation and compares their mean magnitude against g. It deliberately assumes only that the recording contains *some* quiet time — true of any in-the-wild recording, and false only for continuously agitated sensors.

## Evidence

|     | condition             | observed              | detected |
|-----|-----------------------|-----------------------|----------|
| 0   | correct (m/s²)        | 9.806 m/s² (1.000 g)  | no       |
| 1   | recorded in g         | 1.000 m/s² (0.102 g)  | yes      |
| 2   | gravity applied twice | 96.169 m/s² (9.806 g) | yes      |
| 3   | 2% miscalibration     | 10.003 m/s² (1.020 g) | no       |
| 4   | 5% miscalibration     | 10.297 m/s² (1.050 g) | yes      |

The 2% tolerance is the deliberate boundary between calibration error worth flagging and ordinary sensor accuracy. Consumer MEMS accelerometers are commonly specified at 1–3% of full scale, so a tighter tolerance would generate false positives on correctly configured hardware.

**Field observation:** one deployment; two device models shipped values in g despite the SDK documenting m/s². No independent replication yet.

## Mitigation

1.  **Assert units at ingestion.** Run this check on the first hour of every new device model before the study opens, not after it closes.
2.  **Record units explicitly in metadata.** “Accelerometer” is not a unit.
3.  **Perform a static calibration recording.** Place the device on a level surface for sixty seconds at enrolment. It costs nothing and gives every subsequent analysis a reference point.
4.  **Never apply a scale factor without checking whether it was already applied.**

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
