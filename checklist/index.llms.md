# Minimum Reporting Checklist

Ten methods-section disclosures about the measuring system.

Clinical trials have CONSORT. Systematic reviews have PRISMA. Observational studies have STROBE. For in-the-wild sensing there is no agreed statement of what a study should have done and reported for its measurements to be assessable by a reader.

The MRC reports a **different object** than existing mHealth reporting standards. CONSORT-EHEALTH and mERA standardize the reporting of *interventions*, saying little about the acquisition system that produced the sensor data. ACQUIRE is complementary: it reports the **measuring system**.

> **IMPORTANT:**
>
> **v26.7 is one group’s opinion, not a community consensus.** The checklist has not been evaluated for usability, coverage, or inter-rater agreement, and no claim is made that applying it improves study outcomes.
>
> It becomes a standard only if other groups use it, disagree with it in public, and shape it. [Challenge an item →](https://github.com/acquire-framework/acquire-framework.github.io/issues/new?template=checklist-feedback.yml)

## Who it is for

**Authors**, who attach it to a methods section. **Reviewers**, who use it to request specific acquisition details rather than a vague “more detail on data quality” — see the [reviewer form](../templates/index.llms.md#reviewer-form). **Dataset curators**, who use the schema and provenance templates. And **students**, for whom acquisition discipline is most cheaply instilled during supervision.

## The checklist

|  | Disclose in the methods section | Property | Tier |
|:---|:---|:--:|:--:|
| `MRC-01` | Expected versus observed completeness and wear time, per modality, with the sampling policy, background-execution policy, and valid-observation criteria. | \[O\] | core |
| `MRC-02` | Missingness statistics, temporal patterns, and suspected attribution to technical loss, non-wear, adherence or attrition, with the evidence used for that attribution. | \[O\] | core |
| `MRC-03` | Device models, OS versions, app and firmware versions, and every mid-study change. | \[M\] \[EN\] | core |
| `MRC-04` | Timestamping source, synchronization policy, and residual clock uncertainty after reconciliation. | \[M\] | core |
| `MRC-05` | An accuracy or uncertainty statement appropriate to each primary derived measurand, or a documented justification of why quantitative uncertainty could not be established and what validation evidence is provided instead. | \[M\] | conditional |
| `MRC-06` | Upload retry, deduplication, and integrity-verification logic (checksums, sequence numbers). | \[EN\] | core |
| `MRC-07` | Context and system-health events recorded alongside the data: power state, connectivity, permissions; crashes and service kills. | \[EN\] | core |
| `MRC-08` | Machine-readable schema, timestamp semantics, quality-flag definitions, and available collection-software artifacts published alongside the data, or an availability statement documenting proprietary, ethical or licensing restrictions and the versioned information supplied instead. | \[EN\] | core |
| `MRC-09` | QC exclusion criteria, wear-time rules and valid-day thresholds where applicable, and preprocessing provenance from raw log to released dataset. | \[EN\] | core |
| `MRC-10` | Pre-deployment verification evidence: which failure modes of the taxonomy were tested, how, and with what observed behaviour. | \[M\] \[EN\] \[O\] | conditional |

## Proportionality

Items marked **core** apply to any study using this framework. Items marked **conditional** should be judged against the intended measurand and the study’s risk, not applied uniformly.

The synchronization example makes the point concretely: tens of milliseconds of clock error are negligible for daily step counts and disqualifying for cross-modal latency estimation. **The same dataset can be fit for one purpose and unfit for another.** Acquisition requirements should be set and evaluated against what is being measured.

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
