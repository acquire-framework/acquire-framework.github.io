**Version 26.7** — a fixed snapshot, built 2026-07-18 from commit `a11dbb0`. Thresholds and recipes change as evidence accumulates. [See the current version](https://acquire-framework.github.io/).

# Failure catalogue

Entered by symptom, for when the data already looks wrong.

Each entry states what you observe, what causes it, how to detect it automatically, and how well that detection is evidenced.

The evidence level is shown for every recipe and is deliberately conservative. Most entries are currently at `●●○○` or below, which reflects the honest state of the field rather than a gap in ambition — replication is the contribution this catalogue most needs.

TIME-01 [Silent downsampling under OS power management](../recipes/03-doze-downsampling.llms.md) ●●○○

TIME-03 [Clock drift and reset across devices](../recipes/01-clock-drift.llms.md) ●○○○

SIG-01 [Unit and scale mismatch](../recipes/02-unit-scale-mismatch.llms.md) ●●○○

SIG-02 [Stuck sensor reporting stale values](../recipes/04-stuck-sensor.llms.md) ●○○○

SIG-03 [Range saturation](../recipes/05-range-saturation.llms.md) ●○○○

## Evidence levels

| Badge  | Level       | Meaning                                                 |
|:-------|:------------|:--------------------------------------------------------|
| `●○○○` | anecdotal   | Observed, not systematically validated                  |
| `●●○○` | single site | One deployment; detector validated against ground truth |
| `●●●○` | replicated  | Confirmed by an independent group                       |
| `●●●●` | multi-site  | Confirmed across three or more independent groups       |

A recipe at `●○○○` is not wrong — it is unreplicated. Treat the distinction as you would any other single-source claim.

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
