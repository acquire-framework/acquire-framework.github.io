# Contributing to ACQUIRE

The contribution this catalogue most needs is **replication**: independent
confirmation that a failure mode is real and that its detector works on data
other than ours.

## What to contribute

**Replications** (most valuable). Run `acquire check` over one participant's
recording and report what you found — device model, OS version, effective rate,
and whether the failure appeared. An hour of work moves a recipe from `●●○○` to
`●●●○`.

**New failure modes.** Something that went wrong in your study that isn't in the
catalogue. Even without a detector, a well-described symptom and root cause is a
useful entry at `●○○○`.

**Format adapters.** A reader for a device or toolchain we don't yet support.
Usually an afternoon, and it makes the framework usable by everyone with that
hardware.

**Disagreement with the checklist.** Items you think are wrong, unmeasurable, or
missing. At v0.1 this is one group's opinion; it becomes a standard only through
public disagreement.

## Recipe format

Every recipe follows the same structure, in this order:

- **Symptom** — what you observe, written so someone can recognise their own data
- **Root cause** — the mechanism, distinguishing causes that share a signature
- **Detection** — runnable code, with the diagnostic's limits stated
- **Evidence** — how well the detector works, on what data, at what sensitivity
- **Mitigation** — numbered, actionable steps

The **Evidence** section is what separates a recipe from a blog post. Be specific
about what you observed and explicit about what you did not. An honest
`●○○○` entry is more useful than an overstated `●●●○` one.

## Evidence levels

| Badge | Level | Meaning |
|:--|:--|:--|
| `●○○○` | anecdotal | Observed, not systematically validated |
| `●●○○` | single site | One deployment; detector validated against ground truth |
| `●●●○` | replicated | Confirmed by an independent group |
| `●●●●` | multi-site | Confirmed across three or more independent groups |

## Code standards

- The core package must import with **only numpy, pandas, and scipy**. Anything
  else breaks the in-browser build; this is enforced by
  `tests/test_pyodide_constraint.py`.
- Every diagnostic needs a test that injects a fault of known magnitude and
  asserts detection. A diagnostic that silently fails to detect is worse than no
  diagnostic.
- Report sensitivity, don't assume it. Where a detector has a threshold, test
  across fault magnitudes and publish the table.
- State limits explicitly. If a check cannot detect something adjacent to what it
  measures, say so — in the code, in the recipe, and in `NOT_CHECKED` where
  appropriate.

## Credit

Contributors of accepted recipes, replications, and adapters are credited on the
release record, which carries a DOI and is citable.

**Contributing to the framework is distinct from co-authorship on associated
research papers.** Framework credit is real and appears in the archived release;
it does not automatically confer authorship on journal articles arising from the
maintainers' own studies. Where a contribution forms a substantive part of a
paper, authorship is discussed explicitly and in advance.

This is stated plainly to avoid mismatched expectations later, which is a common
and avoidable source of difficulty in community research projects.

## Editorial decisions

Structure, schema, checklist wording, and evidence-level assignments rest with
the maintainer. This is a deliberate choice: opinionated frameworks need a single
editorial voice to stay coherent, in the way reporting standards such as CONSORT
are maintained by named editors rather than by open vote.

Contributions that *add* — recipes, evidence, adapters, corrections — are very
welcome. Proposals to restructure are welcome as discussion issues before any
implementation work.

## How to submit

1. Open an issue describing what you intend to add
2. Fork, branch, and make the change
3. Run `pytest` and `quarto render` locally
4. Open a pull request referencing the issue

For replications, an issue alone is enough — no pull request needed. Report what
you ran and what you found, and it will be incorporated with credit.
