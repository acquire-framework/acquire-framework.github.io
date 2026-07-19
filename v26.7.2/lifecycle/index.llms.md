**ACQUIRE 26.7.2** — a fixed snapshot of the specification, built 2026-07-19 from commit `32d64e8`. Thresholds and recipes change as evidence accumulates. [See the current version](https://acquire-framework.github.io/).

# The guideline book

What to do, in the order you need to do it.

The failure catalogue is organised by symptom, for when something has already gone wrong. This section is organised by **stage**, for when you are building a study and want to know what comes next.

[design](../lifecycle/design.llms.md) → [instrument](../lifecycle/instrument.llms.md) → [pilot](../lifecycle/pilot.llms.md) → [deploy](../lifecycle/deploy.llms.md) → [monitor](../lifecycle/monitor.llms.md) → [curate](../lifecycle/curate.llms.md) → [release](../lifecycle/release.llms.md)

Each stage carries an ordered checklist. Items are written as **verifiable statements** — things you either did or did not do and can report — rather than as advice. “Consider power management” is useless; “effective sampling rate verified against nominal on every device model before deployment” is checkable.

That discipline exists because the checklist is intended to become an artifact you submit alongside a paper, in the way CONSORT and STROBE checklists are submitted in clinical and observational research. In-the-wild sensing has no such instrument today.

## The stages

**[Design](../lifecycle/design.llms.md)** — decide what you are measuring, at what fidelity, and what would count as invalid. Most acquisition failures are made possible by decisions taken here.

**[Instrument](../lifecycle/instrument.llms.md)** — build the acquisition app and its telemetry. Embed error reporting, log requests, account for OS behaviour that silently degrades sampling.

**[Pilot](../lifecycle/pilot.llms.md)** — smoke-test the whole chain on real devices with real people before anything scales. The cheapest place to find every failure in the catalogue.

**[Deploy](../lifecycle/deploy.llms.md)** — enrol participants and start collection, with the ability to detect a bad rollout before it consumes the study.

**[Monitor](../lifecycle/monitor.llms.md)** — detect failure while it is still cheap. The distinguishing question is not “is data arriving?” but “is the arriving data valid?”

**[Curate](../lifecycle/curate.llms.md)** — version, store, and document data as it accumulates, rather than reconstructing provenance at the end.

**[Release](../lifecycle/release.llms.md)** — publish a dataset someone else can actually use, with the metadata that makes its validity assessable.

## Using the checklist

The full checklist is [available in one place](../checklist/index.llms.md), filtered by study type. Not every item applies to every study — items marked not applicable require a written justification rather than silent omission, because that is what makes the completed artifact trustworthy to a reader.

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
