# Worked example: cross-device synchronization

Reproduces Figure 2 of the accompanying paper and the offset series behind it.

```bash
python generate_figure.py
```

Requires only Python with NumPy, pandas and Matplotlib.

## Outputs

| File | Contents |
|:--|:--|
| `fig-clock-drift.pdf` / `.png` | The figure |
| `synthetic_offsets.csv` | The per-sample offset series behind it |

All values are synthetic **[A]**. No participant or device data is used.

## What it shows

Two BLE devices timestamp on free-running real-time clocks at **+40 ppm** and
**−25 ppm** relative to the phone, reconciled only at reconnection (every
2–3.5 h). Running it produces:

```
re-anchors:            8
peak |inter-device|:   786.6 ms
fraction beyond ±20 ms: 96.1%
completeness:          100%
```

Completeness is 100%, no values are impossible, and every conventional quality
flag stays green — while the inter-device offset spends 96% of the recording
outside any tolerance a latency measurand such as pulse-arrival time would
demand, peaking near 0.8 s.

This is the point of separating the axes. A **record-integrity** audit and a
conventional **data-quality** audit both pass this dataset. A **measurement
validity** audit does not. The data-quality reflex — impute or drop bad windows
— has nothing to act on, because no window looks bad.

The magnitude follows directly from the stated assumptions: a 65 ppm relative
offset accumulating over a 3.5 h re-anchor gap gives 65 × 10⁻⁶ × 12600 s ≈
819 ms, which is what the simulation produces.

## Auditing the assumptions

Every value the figure depends on is a module-level constant at the top of
`generate_figure.py` — drift rates, re-anchor bounds, reconciliation residual,
duration, and the random seed. Change one and re-run to see its effect. The
seed is fixed so the artifact is bit-reproducible.

## The response

Not to clean the data afterwards, but to instrument acquisition: log the
device-versus-phone offset at every reconnection, estimate drift, re-anchor more
often, and report the residual. The budget in Table 3 of the paper is dominated
by free-running drift between re-anchors, so the effective intervention is
immediate — shorten the interval, or log the offset and correct for it.

See [`templates/uncertainty-statement.md`](../../templates/uncertainty-statement.md)
for the reporting form, and note that a deployed study should establish the
residual synchronization term from its own offset logs rather than assuming the
±10 ms design target used here.
