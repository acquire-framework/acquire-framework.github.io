# Minimum Reporting Checklist

Ten methods-section disclosures about the measuring system.

Clinical trials have CONSORT. Systematic reviews have PRISMA. Observational studies have STROBE. For in-the-wild sensing there is no agreed statement of what a study should have done and reported for its measurements to be assessable by a reader.

The MRC reports a **different object** than existing mHealth reporting standards. CONSORT-EHEALTH and mERA standardize the reporting of *interventions*, saying little about the acquisition system that produced the sensor data. ACQUIRE is complementary: it reports the **measuring system**.

> **IMPORTANT:**
>
> **v0.1 is one group’s opinion, not a community consensus.** The checklist has not been evaluated for usability, coverage, or inter-rater agreement, and no claim is made that applying it improves study outcomes.
>
> It becomes a standard only if other groups use it, disagree with it in public, and shape it. [Challenge an item →](https://github.com/acquire-framework/acquire-framework.github.io/issues/new?template=checklist-feedback.yml)

## Who it is for

**Authors**, who attach it to a methods section. **Reviewers**, who use it to request specific acquisition details rather than a vague “more detail on data quality” — see the [reviewer form](../templates/index.llms.md#reviewer-form). **Dataset curators**, who use the schema and provenance templates. And **students**, for whom acquisition discipline is most cheaply instilled during supervision.

## The checklist

|  | Disclose in the methods section | Property | Tier | Disclosure |
|:---|:---|:--:|:--:|:--:|
| `MRC-01` | Expected versus observed completeness, per modality, with the sampling and background-execution policy. | \[O\] | core | partly automatic |
| `MRC-02` | Missingness statistics and their suspected attribution (technical / adherence / attrition), with the evidence used. | \[O\] | core | partly automatic |
| `MRC-03` | Device models, OS versions, app and firmware versions, and every mid-study change. | \[M\] \[EN\] | core | partly automatic |
| `MRC-04` | Timestamping source, synchronization policy, and residual clock uncertainty after reconciliation. | \[M\] | core | partly automatic |
| `MRC-05` | An accuracy or uncertainty statement appropriate to each primary derived measurand, or a documented justification of why quantitative uncertainty could not be established and what validation evidence is provided instead. | \[M\] | conditional | author-disclosed |
| `MRC-06` | Upload retry, deduplication, and integrity-verification logic (checksums, sequence numbers). | \[EN\] | core | author-disclosed |
| `MRC-07` | Context and system-health events recorded alongside the data: power state, connectivity, permissions; crashes and service kills. | \[EN\] | core | author-disclosed |
| `MRC-08` | Machine-readable schema and collection-software artifacts published alongside the data. | \[EN\] | core | author-disclosed |
| `MRC-09` | QC exclusion criteria and preprocessing provenance from raw log to released dataset. | \[EN\] | core | partly automatic |
| `MRC-10` | Pre-deployment verification evidence: which failure modes of the taxonomy were tested, how, and with what observed behaviour. | \[M\] \[EN\] \[O\] | conditional | author-disclosed |

## Proportionality

Items marked **core** apply to any study using this framework. Items marked **conditional** should be judged against the intended measurand and the study’s risk, not applied uniformly.

The synchronization example makes the point concretely: tens of milliseconds of clock error are negligible for daily step counts and disqualifying for cross-modal latency estimation. **The same dataset can be fit for one purpose and unfit for another.** Acquisition requirements should be set and evaluated against what is being measured.

## Disclosure should be a by-product, not extra work

The reason most acquisition detail goes unreported is not that authors are careless — it is that disclosure is unpaid work with no reward, and often requires numbers nobody computed.

Six of the ten items can be populated wholly or partly from data and logs by the shipped diagnostics, so that reporting becomes a by-product of a validation you would want to run anyway:

``` bash
pip install acquire-framework
acquire check recordings/day01.csv --nominal 50
```

| Item | What the diagnostics supply | What you must still supply |
|:---|:---|:---|
| `MRC-01` | Observed completeness and effective rate are computed by `acquire check` (TIME-01, TIME-02). Expected completeness and the background-execution policy are author-supplied. | — |
| `MRC-02` | Gap counts, durations and their distribution over time are computed. Attribution is an author judgement and must be argued, not asserted — published completeness figures routinely conflate these three causes. | — |
| `MRC-03` | Populated automatically where the collection app records these per recording, as the provenance template specifies. | — |
| `MRC-04` | Monotonicity and regularity are checked automatically. The residual synchronization uncertainty must be estimated from the study’s own offset logs — see examples/synchronization for the model and a worked budget. | — |
| `MRC-09` | Diagnostic results and the thresholds that produced them are emitted by `acquire check` and can be attached verbatim as the QC record. | — |

The remaining four items — integrity logic, health-event recording, published schema and software, and pre-deployment verification — are properties of how the study was built. No tool can infer them, and the checklist’s role there is to make their absence visible rather than silent.

## A floor under item MRC-05

MRC-05 permits a documented justification in place of an uncertainty statement. Without a floor, that escape hatch would be taken universally and the item would carry no information. A justification is acceptable only if it:

1.  **Names the dominant uncertainty sources** that would appear in a budget
2.  **States why each could not be quantified**
3.  **Describes the validation evidence offered instead**

“Uncertainty could not be established” alone does not satisfy the item. The [uncertainty statement template](../templates/index.llms.md#uncertainty-statement) provides both the budget form and the justification form.

## Templates

| Template | Satisfies |
|:---|:---|
| [Sensor schema](../templates/index.llms.md#sensor-schema) | MRC-08 |
| [Quality flags](../templates/index.llms.md#quality-flags) | MRC-01, MRC-02, MRC-09 |
| [Uncertainty statement](../templates/index.llms.md#uncertainty-statement) | MRC-05 |
| [Dataset provenance](../templates/index.llms.md#dataset-provenance) | MRC-03, MRC-09 |
| [Reviewer form](../templates/index.llms.md#reviewer-form) | all |

## Going further

The MRC is the reporting minimum — what a reader needs to assess a study after the fact. The [extended operational checklist](../checklist/extended.llms.md) is a longer, stage-by-stage companion for people **building** a study, covering decisions that never appear in a methods section but determine whether the MRC can be answered honestly at all.

## Source

[`checklist/acquire-mrc.yml`](https://github.com/acquire-framework/acquire-framework.github.io/blob/main/checklist/acquire-mrc.yml) is the single source of truth: the site renders it, the exports derive from it, and each item names the taxonomy rows it comes from.

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
