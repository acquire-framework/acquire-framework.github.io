**ACQUIRE 26.7.1** — a fixed snapshot of the specification, built 2026-07-18 from commit `199e1e9`. Thresholds and recipes change as evidence accumulates. [See the current version](https://acquire-framework.github.io/).

# Release

Publishing a dataset whose validity a stranger can assess.

A released dataset is a claim about measurement. What makes it reusable is not its size but whether someone who was not there can determine what it measures and how well.

## Checklist

**REL-01** — The dataset has a persistent identifier (DOI) and a stated licence.

**REL-02** — Nominal sampling rate, units, sensor range, and device models are documented per recording.

**REL-03** — Validation results are published with the data, including failures, not only the recordings that passed.

**REL-04** — Exclusions and their reasons are reported in aggregate, so a reader can judge selection effects.

**REL-05** — Known limitations are stated explicitly, including failure modes that were detected and those that could not be checked.

**REL-06** — The completed ACQUIRE checklist is attached as supplementary material, with justifications for items marked not applicable.

**REL-07** — Code that produced the released artifacts is archived at the same version as the data.

**REL-08** — A minimal worked example is included, so a new user can load the data and reproduce one figure.

## Publishing failures is not a weakness

A dataset that reports “9% of recordings failed the sampling-rate check and were excluded, distribution of effective rates below” is more useful and more credible than one that reports nothing. The second dataset has the same problems; it simply declines to say so.

This is the point at which the framework’s argument becomes concrete: validity that was measured continuously can be reported honestly, and validity that was never measured cannot be reported at all.

## Back to the start

→ [Design](../lifecycle/design.llms.md): the next study starts by deciding what would count as invalid.

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
