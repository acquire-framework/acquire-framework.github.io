# ACQUIRE Framework

*Acquisition Criteria for Quality, Uncertainty, Integrity, Reproducibility, and Evidence*

A taxonomy, a reporting checklist and templates for running reproducible
in-the-wild sensing studies — instrument validity, failure detection,
monitoring, data versioning, and reproducible dataset release.

**Site:** <https://acquire-framework.github.io>
**Status:** specification 26.7.1.

## What's here

- **`spec/`** — the specification manifest and changelog.
- **`taxonomy/`** — the acquisition-failure taxonomy.
- **`checklist/`** — the Minimum Reporting Checklist, YAML as single source of truth.
- **`templates/`** — sensor schema, quality flags, uncertainty statement,
  dataset provenance, reviewer form.
- **`recipes/`** — the failure catalogue, organised by symptom.
- **`lifecycle/`** — the guideline book, organised by study stage.
- **`examples/`** — a worked cross-device synchronization example.

## What this is

A specification and a set of documents. No software is published as part of
this release.

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
