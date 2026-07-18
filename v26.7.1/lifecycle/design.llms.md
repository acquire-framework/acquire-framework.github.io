**ACQUIRE 26.7.1** — a fixed snapshot of the specification, built 2026-07-18 from commit `199e1e9`. Thresholds and recipes change as evidence accumulates. [See the current version](https://acquire-framework.github.io/).

# Design

Deciding what you are measuring, and what would count as invalid.

Most acquisition failures are made *possible* by decisions taken at design time. Deciding fidelity, defining validity, and writing down what would falsify your data are cheap here and expensive later.

## Checklist

**DSGN-01** — The required sampling rate is derived from the phenomenon being measured (via the Nyquist limit for the highest frequency of interest), not inherited from a previous study or an SDK default.

**DSGN-02** — The minimum acceptable data yield per participant is stated in advance, with the analysis consequence of falling below it.

**DSGN-03** — Explicit validity criteria are written down before collection begins: what observable property would make a recording unusable.

**DSGN-04** — The measurement range required by the most vigorous activity in the protocol has been calculated, not assumed.

**DSGN-05** — Device and OS diversity in the intended population is enumerated, including the oldest hardware that will be permitted.

**DSGN-06** — Battery and storage budgets are computed for the intended duration at the intended rate, on the worst-case device.

**DSGN-07** — The consent and ethics documentation covers telemetry and crash reporting, not only the primary sensor data.

**DSGN-08** — A data management plan exists that names where raw data lives, who can access it, and how long it is retained.

## The question worth asking early

*If this study produced entirely invalid data, how and when would I find out?*

If the honest answer is “during analysis”, the design is not yet finished. Every item in [monitor](../lifecycle/monitor.llms.md) exists to move that answer earlier.

## Next

→ [Instrument](../lifecycle/instrument.llms.md): build the app and its telemetry.

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
