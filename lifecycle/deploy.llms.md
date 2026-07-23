# Deploy

Starting collection without betting the study on an untested rollout.

Deployment is where a single mistake multiplies by your participant count. The goal is to make a bad rollout detectable in days rather than at analysis.

## Checklist

**DPLY-01** — Enrolment is staged: a small first cohort is validated before the remainder are enrolled.

**DPLY-02** — Each participant’s first 24 hours are validated individually before their data is counted toward the study.

**DPLY-03** — The app version deployed to each participant is recorded, and changes to it during the study are logged as events.

**DPLY-04** — A rollback path exists and has been tested: a bad release can be reverted without losing buffered data.

**DPLY-05** — Device model, OS version, and vendor are recorded per participant, so failures can be attributed to hardware populations.

**DPLY-06** — Participants have a documented route to report problems, and those reports are logged alongside the technical telemetry.

**DPLY-07** — Onboarding instructions state explicitly what participants must not do (force-stop the app, disable background activity, revoke permissions), and this is verified rather than assumed.

## Staged enrolment is the cheapest insurance

The difference between discovering a fatal configuration error at participant 5 and at participant 200 is the entire study. Staging costs a few days.

## Next

→ [Monitor](../lifecycle/monitor.llms.md): detect failure while it is still cheap.

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
