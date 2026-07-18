# ACQUIRE Framework

*Acquisition Criteria for Quality, Uncertainty, Integrity, Reproducibility, and Evidence*

Recipes, guidelines, and diagnostics for running reproducible in-the-wild sensing
studies — instrument validity, failure detection, monitoring, data versioning, and
reproducible dataset release.

**Site:** <https://acquire-framework.github.io>
**Status:** v0.1.0 — first public release.

## What's here

- **`acquire/`** — the diagnostics package. Seven checks across timing and signal
  validity, a canonical schema, and a synthetic generator with injectable faults.
- **`lifecycle/`** — the guideline book, organised by study stage.
- **`recipes/`** — the failure catalogue, organised by symptom.
- **`checklist/`** — the reporting checklist, YAML as single source of truth.

## Quick start

```bash
pip install acquire-framework
acquire check recordings/day01.csv --nominal 50
```

Exits non-zero on failure, so it can gate a pipeline.

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
