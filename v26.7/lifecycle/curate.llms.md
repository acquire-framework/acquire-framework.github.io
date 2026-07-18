**Version 26.7** — a fixed snapshot, built 2026-07-18 from commit `a11dbb0`. Thresholds and recipes change as evidence accumulates. [See the current version](https://acquire-framework.github.io/).

# Curate

Recording provenance as it happens, not reconstructing it afterwards.

Provenance reconstructed at the end of a study is a best-effort narrative. Provenance recorded as data arrives is evidence. The difference costs almost nothing during collection and cannot be recovered later.

## Checklist

**CUR-01** — Raw data is stored immutably. Processing produces new artifacts; it never overwrites the original.

**CUR-02** — Every processing step is recorded with the software version that performed it.

**CUR-03** — Data is versioned, and any published analysis names the version it used.

**CUR-04** — Validation results are stored *alongside* the data, so a future user sees what was checked and what was found.

**CUR-05** — Exclusions are recorded with reasons at the point of decision, not summarised afterwards.

**CUR-06** — Device metadata (model, OS, app version, configured range, nominal rate, units) travels with the data rather than living in a separate spreadsheet.

**CUR-07** — Backups exist, and restoring from them has actually been tested.

**CUR-08** — Personal data handling matches what consent and ethics approval permit, including for telemetry.

## The failure this prevents

The commonest irrecoverable curation failure is not data loss — it is data whose validity can no longer be assessed. A recording with no nominal rate recorded cannot be checked for downsampling by anyone, ever. The metadata is what makes the data assessable, and it is only free to capture at the moment of collection.

## Next

→ [Release](../lifecycle/release.llms.md): publish something another group can actually use.

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
