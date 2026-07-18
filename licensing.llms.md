# Licensing

Three kinds of content, meant to be reused in different ways.

| What | Licence | Where |
|:---|:---|:---|
| **Data** — the taxonomy and checklist as structured records | [CC0 1.0](https://github.com/acquire-framework/acquire-framework.github.io/blob/main/LICENSES/CC0-1.0.txt) | `taxonomy/*.yml`, `checklist/*.yml`, the CSV and Markdown exports |
| **Documentation** — prose, templates, forms | [CC BY 4.0](https://github.com/acquire-framework/acquire-framework.github.io/blob/main/LICENSES/CC-BY-4.0.txt) | this site, `templates/`, `recipes/`, `lifecycle/` |
| **Code** — diagnostics, tooling, examples | [MIT](https://github.com/acquire-framework/acquire-framework.github.io/blob/main/LICENSES/MIT.txt) | `acquire/`, `tools/`, `tests/`, `examples/` |

Copyright 2026 Mateusz Danioł, Ryszard Sroka.

## Why they differ

**The data is CC0 — public domain, no attribution required.** The taxonomy and the checklist are only useful as a shared vocabulary. If someone wants to embed the failure classes in a validation tool, a journal submission system, or a competing framework, an attribution requirement is friction with no upside. A reporting standard that is awkward to adopt does not become a standard.

We would like to be cited, and the [citation page](cite.llms.md) says how. But that is a scholarly norm, not a licence condition, and the two should not be confused: enforcing citation through copyright would work against adoption, which is the only thing that makes a standard worth having.

**The documentation is CC BY 4.0.** The prose explains, argues, and interprets. Attribution is appropriate there and does not impede reuse — translate it, adapt it for a course, extract it into a lab handbook, and keep the credit.

**The code is MIT.** Permissive, familiar, and compatible with essentially any research or commercial pipeline the diagnostics might run inside.

## What this means in practice

- Copy the taxonomy or checklist into your own tool, standard, or paper with **no obligation at all**.
- Adapt the templates and prose provided you credit ACQUIRE.
- Vendor the diagnostics code under MIT terms.
- **A completed checklist is yours.** Filling one in does not make your document a derivative work of ours — attach it to a paper or dataset under whatever licence you like.

## Machine-readable

Files carry `SPDX-License-Identifier` headers where the format permits a comment. Where it does not — CSV, for instance — the licence is the one listed for its directory above.

Full licence texts live in [`LICENSES/`](https://github.com/acquire-framework/acquire-framework.github.io/tree/main/LICENSES), named by SPDX identifier, following the [REUSE](https://reuse.software/) convention.

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
