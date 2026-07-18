# ACQUIRE Framework

*Acquisition Criteria for Quality, Uncertainty, Integrity, Reproducibility, and Evidence*

Recipes, guidelines, and diagnostics for running reproducible in-the-wild sensing
studies — instrument validity, failure detection, monitoring, data versioning, and
reproducible dataset release.

**Site:** <https://acquire-framework.github.io>
**Status:** specification 26.7.1.

## What's here

- **`spec/`** — the specification manifest and changelog.
- **`lifecycle/`** — the guideline book, organised by study stage.
- **`recipes/`** — the failure catalogue, organised by symptom.
- **`checklist/`** — the reporting checklist, YAML as single source of truth.

## What this is

A specification and a set of documents. No diagnostic software is published;
tooling is on the roadmap and deliberately not announced.

## Development

```bash
uv sync --extra dev --extra docs
uv run pytest
QUARTO_PYTHON=.venv/bin/python uv run quarto preview
```

## Contributing

Replication is the contribution the catalogue most needs — see
[CONTRIBUTING.md](CONTRIBUTING.md). Contributors are credited on the citable
release record.

## Citing

See [CITATION.cff](CITATION.cff) or the [cite page](https://acquire-framework.github.io/cite.html).
