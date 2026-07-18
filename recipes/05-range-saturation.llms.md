# Range saturation

Censored samples that no downstream filtering can recover.

configuration

hardware

The configured measurement range is too narrow for the activity being measured, so peaks are clipped at the rail.

●○○○ evidence: anecdotal

> **NOTE:**
>
> **Recipe SIG-03 · [Stage: pilot](../lifecycle/pilot.llms.md) · Last reviewed 2026-07-18**

## Symptom

The signal has flat tops. Peak magnitudes cluster at a suspiciously round value — 2 g, 4 g, 8 g — and impact-related features are compressed or absent. Activity recognition performs adequately on sedentary classes and poorly on vigorous ones.

## Root cause

The accelerometer range was left at a default too narrow for the study population or activity. A ±2 g range is comfortable for posture and gait but is exceeded routinely by running, stair descent, and any impact.

The samples are not noisy, they are **censored**: the true value was outside the representable range and no information about it was recorded. No filtering, interpolation, or model capacity recovers it.

## Detection

Concretely: find the maximum absolute value per axis and count how many samples sit within a small fraction of it. A healthy recording touches its peak once; a saturated one returns to it repeatedly, because the rail is a value the signal cannot exceed rather than one it happens to reach.

## Evidence

**No field observation yet.** A threshold of 0.1% of samples at the rail is a defensible starting point rather than an empirically derived one, and would benefit from calibration against real recordings across activity types.

**The threshold needs empirical grounding.** Recordings from vigorous activity with a known-adequate range would let this be set from data rather than judgement.

## Mitigation

1.  **Set the range from the most vigorous activity in your protocol**, not the typical one. The cost of a wider range is quantisation resolution, which is almost always the better trade.
2.  **Verify during pilot** with your most active participant, not in the lab. See [pilot](../lifecycle/pilot.llms.md).
3.  **Record the configured range in dataset metadata.** Without it, a future user cannot tell censored samples from real peaks.
4.  **Treat clipped samples as missing in analysis**, and report what fraction were clipped.

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
