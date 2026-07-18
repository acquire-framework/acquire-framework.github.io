**ACQUIRE 26.7.1** — a fixed snapshot of the specification, built 2026-07-18 from commit `199e1e9`. Thresholds and recipes change as evidence accumulates. [See the current version](https://acquire-framework.github.io/).

# Pilot

Smoke-test the whole chain before anything scales.

The pilot is the cheapest place to find every failure in the catalogue. Its purpose is not to check whether the app runs — it is to check whether the data the app produces is *valid*, end to end, on real hardware carried by real people.

## Checklist

### End-to-end

**PLT-01** — At least one recording has traversed the complete chain — device, upload, storage, and analysis pipeline — and been validated at the far end, not merely observed to arrive.

**PLT-02** — Validation checks have been run over pilot recordings and the results recorded.

**PLT-03** — The pilot ran on the oldest and cheapest device model permitted in the study, not only on the developer’s handset.

**PLT-04** — The pilot included at least one full overnight period, where OS power management engages. → [Silent downsampling](../recipes/03-doze-downsampling.llms.md)

### Adversarial conditions

**PLT-05** — Behaviour has been verified with the device offline for a prolonged period, and buffered data confirmed to arrive intact afterwards.

**PLT-06** — Behaviour has been verified across an app restart and a device reboot.

**PLT-07** — Behaviour has been verified with the battery low enough to trigger aggressive power saving.

**PLT-08** — Behaviour has been verified when storage is nearly full.

### Validity

**PLT-09** — A static calibration recording confirms resting magnitude is one g on every device model. → [Unit and scale mismatch](../recipes/02-unit-scale-mismatch.llms.md)

**PLT-10** — A vigorous-activity recording confirms the configured range is not saturated. → [Range saturation](../recipes/05-range-saturation.llms.md)

**PLT-11** — Monitoring and alerting were active during the pilot, and at least one alert was deliberately triggered to confirm it fires and reaches someone.

## The test most studies skip

Deliberately break something — unplug the network, force-stop the app, fill the storage — and confirm your monitoring notices. Monitoring that has never fired is not monitoring; it is a configuration you hope is correct.

## Next

→ [Deploy](../lifecycle/deploy.llms.md): enrol participants and start collection.

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
