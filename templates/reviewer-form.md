# ACQUIRE reviewer form v0.1

For reviewing a manuscript or dataset that reports in-the-wild sensor data.

Its purpose is to let a reviewer request **specific** acquisition details
instead of "more detail on data quality", which authors cannot act on.

**Proportionality.** Requirements should be set against the intended measurand
and the study's risk, not applied uniformly. Tens of milliseconds of clock error
are negligible for daily step counts and disqualifying for cross-modal latency.
Judge each item against what the paper claims to measure — do not demand a full
uncertainty budget from a step-count study.

**Absence of a disclosure is a finding, not a failing.** Many groups genuinely
cannot produce some of these. An honest "we did not measure this" is a better
outcome than a fabricated number, and reviewers should say so explicitly rather
than pushing authors toward false precision.

---

## A. Measurement validity [M]

| | Question | Reported? | Note |
|:--|:--|:-:|:--|
| A1 | Are device models, firmware, app and OS versions stated, including mid-study changes? | ☐ | |
| A2 | Is the timestamping source stated (device RTC / host / monotonic)? | ☐ | |
| A3 | Is the synchronization policy stated, and the residual uncertainty after reconciliation? | ☐ | |
| A4 | Is there an accuracy or uncertainty statement for each primary derived measurand, or a justification meeting the floor (sources named, reasons given, substitute evidence described)? | ☐ | |
| A5 | If device validation is cited, does it match the study's conditions? Bench repeatability evidence does not transfer to a multi-month, multi-device field deployment. | ☐ | |
| A6 | Was calibration performed, and is the procedure stated? | ☐ | |

## B. Record integrity and provenance [EN]

| | Question | Reported? | Note |
|:--|:--|:-:|:--|
| B1 | Is a machine-readable schema published with the data? | ☐ | |
| B2 | Is the collection software available, with version or commit? | ☐ | |
| B3 | Is upload retry, deduplication and integrity-verification logic described? | ☐ | |
| B4 | Are context and system-health events recorded alongside the data (power, connectivity, permissions, crashes, service kills)? | ☐ | |
| B5 | Is a raw record retained, and is preprocessing provenance from raw to released traceable? | ☐ | |
| B6 | Are QC exclusion criteria stated, with counts? | ☐ | |

## C. Observation-process validity [O]

| | Question | Reported? | Note |
|:--|:--|:-:|:--|
| C1 | Is expected versus observed completeness reported per modality? | ☐ | |
| C2 | Is the background-execution / sampling policy stated? | ☐ | |
| C3 | Is missingness attributed to technical loss, adherence, or attrition — with the evidence used, or an explicit statement that they cannot be separated? | ☐ | |
| C4 | Is the possibility of non-random loss addressed where the estimand is time-aggregated or population-level? | ☐ | |
| C5 | Were participants told which OS features must remain enabled, and is that reported as part of the method? | ☐ | |

## D. Verification

| | Question | Reported? | Note |
|:--|:--|:-:|:--|
| D1 | Is pre-deployment verification evidence given — which failure modes were tested, how, with what result? | ☐ | |
| D2 | Did the pilot cover realistic conditions (overnight idle, aggressive vendor optimizers, offline periods, reboot)? | ☐ | |

---

## Reviewer summary

**Most consequential omission, and why it matters for *this* study's claims:**

> `<one paragraph>`

**Requested disclosures**, in priority order — be specific enough that the
author knows exactly what to add:

1. `<e.g. "State the nominal sampling rate and the observed effective rate per
   device model. Without the nominal rate, silent downsampling is undetectable
   by any reader.">`
2.
3.

**Where absence is acceptable**, and should be stated rather than filled in:

> `<e.g. "A full uncertainty budget is disproportionate for this measurand; a
> statement that synchronization uncertainty was not characterised, with the
> reason, would suffice.">`

---

*ACQUIRE MRC v0.1. The checklist has not been evaluated for usability, coverage,
or inter-rater agreement; no claim is made that applying it improves study
outcomes. Feedback on the form itself is welcome as a repository issue.*
