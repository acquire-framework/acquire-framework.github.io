# Check your data

The diagnostics, run against your own recordings.

## In your pipeline

This is the intended production path. The package runs where your data already is — in your ingestion pipeline, your analysis notebook, or CI — with no conversion step and no upload:

``` bash
git clone https://github.com/acquire-framework/acquire-framework.github.io
cd acquire-framework.github.io
uv sync --extra dev
uv run acquire check recordings/day01.csv --nominal 50
```

> **NOTE:**
>
> **Not yet on a package index.** The diagnostics run from a clone of the repository. A published package will follow once the API has settled; until then, pin the commit you ran so your quality-control record stays meaningful.

It exits non-zero when a check fails, so it can gate a pipeline directly. In Python:

``` python
import acquire, pandas as pd

df = pd.read_csv("recordings/day01.csv")
report = acquire.check(df, nominal_hz=50)

for result in report.failures:
    print(result)
```

The frame needs four columns — `timestamp`, `ax`, `ay`, `az` — in the [canonical schema](https://github.com/acquire-framework/acquire-framework.github.io/blob/main/acquire/schema.py). Timestamps may be float seconds or datetimes.

## In your browser

> **NOTE:**
>
> **Planned for v0.2.** The same package will run directly in this page via Pyodide — Python compiled to WebAssembly, executing in your tab.
>
> **Your data will never leave your device.** There is no upload, no server, and no request: the computation happens locally, and you can confirm that in your browser’s network tab. For studies operating under ethics approval, consent constraints, or GDPR, that distinction is the difference between a tool you can try and one you cannot.

The browser version is deliberately scoped as a *demonstration* — a way to see what the checks do and what a failure looks like, using example data with deliberately injected faults. Format fragmentation makes “upload your study data” a poor first experience: everyone’s export differs, and a tool that demands conversion before delivering value does not get used.

## Why the nominal rate must be supplied

Every diagnostic takes the sampling rate your application *requested*. It is not inferred from the data, and this is deliberate: inferring it would define away the most common failure in the catalogue. If the tool guessed 43 Hz because that is what it observed, it could never tell you the app asked for 50.

This is the general principle behind the framework. A measurement is only assessable against a stated expectation — which is why so many items in the [checklist](../checklist/index.llms.md) are about recording what you intended, not just what you got.

## What the checks do not cover

Stated on every passing report, and worth repeating here:

- Whether the sensor was calibrated against a reference instrument
- Whether device clocks agree with each other or with wall time
- Whether the participant wore or carried the device as instructed
- Whether the recorded activity matches any label or diary entry
- Anything about signal streams other than tri-axial acceleration

A passing report means the checks that ran found nothing. It is not a certificate of validity, and a framework that let you read it as one would be reproducing the problem it exists to solve.

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
