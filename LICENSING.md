# Licensing

ACQUIRE is licensed in three parts, because its three kinds of content are
meant to be reused in different ways.

| What | Licence | Where |
|:--|:--|:--|
| **Data** — the taxonomy and checklist as structured records | [CC0 1.0](LICENSES/CC0-1.0.txt) | `taxonomy/*.yml`, `checklist/*.yml`, `dist/*.csv`, `dist/*.md` |
| **Documentation** — prose, templates, forms | [CC BY 4.0](LICENSES/CC-BY-4.0.txt) | `checklist/*.qmd`, `templates/`, `recipes/`, `lifecycle/`, `taxonomy/*.qmd`, and all other prose |
| **Code** — tooling, scripts, examples | [MIT](LICENSES/MIT.txt) | `acquire/`, `tools/`, `tests/`, `examples/`, `acqsite.py` |

Copyright 2026 Mateusz Danioł, Ryszard Sroka.

## Why they differ

**The data is CC0 — public domain, no attribution required.** The taxonomy and
checklist are only useful as a shared vocabulary. If someone wants to embed the
failure classes in a validation tool, a journal submission system, or a
competing framework, attribution requirements are friction with no upside. A
reporting standard that is awkward to adopt does not become a standard.

We would like to be cited, and the [citation page](https://acquire-framework.github.io/cite.html)
says how. But that is a scholarly norm, not a licence condition, and the two
should not be confused.

**The documentation is CC BY 4.0.** The prose explains, argues, and interprets;
attribution is appropriate and does not impede reuse. Translate it, adapt it
for a course, or extract it into a lab handbook — keep the credit.

**The code is MIT.** Permissive, familiar, and compatible with essentially any
research or commercial pipeline the scripts might run inside.

## Practical consequences

- You may copy the taxonomy or checklist into your own tool, standard, or paper
  with no obligation at all.
- You may adapt the templates and prose provided you credit ACQUIRE.
- You may vendor any of the code under MIT terms.
- A completed checklist you fill in is **yours**, not a derivative work of
  ours. Attach it to a paper or dataset under whatever licence you like.

## Machine-readable

Files carry `SPDX-License-Identifier` headers where the format permits a
comment. Where it does not — CSV, for instance — the licence is the one listed
for its directory in the table above.

The full licence texts are in [`LICENSES/`](LICENSES/), named by SPDX
identifier, following the [REUSE](https://reuse.software/) convention.
