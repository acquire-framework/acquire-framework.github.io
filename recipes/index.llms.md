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
