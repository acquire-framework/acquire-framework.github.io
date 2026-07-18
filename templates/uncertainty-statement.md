# Uncertainty statement template — satisfies MRC-05

One statement per primary derived measurand. If a measurand is reported in a
results section, it needs one of these or a justification meeting the floor in
Part B.

This is a *design-stage* budget unless you state otherwise. A budget evaluated
from declared assumptions is not an empirical uncertainty statement about a
deployed system, and conflating the two is itself a reporting failure.

---

## Part A — quantitative budget

**Measurand:** `<e.g. pulse-arrival time, from ECG–PPG latency>`

**Measurement model:** state the equation relating the measured value to the
true value and every error term. For a two-device latency measurand:

```
Δt_meas = Δt_true + δ_A − δ_B + δ_sync,rel + δ_host
```

where `δ_A`, `δ_B` are clock errors accumulated since the last re-anchor,
`δ_sync,rel` is the residual *relative* synchronization error after
reconciliation (common-mode error has already cancelled here), and `δ_host` is
host-side timestamping uncertainty not already contained in `δ_sync,rel`.

**Budget:**

| Component | Assumed or measured limit | Distribution | Divisor | u_i |
|:--|--:|:-:|--:|--:|
| `<δ_A drift, 30 ppm over 900 s>` | `<±27 ms>` | rectangular | √3 | `<15.6>` |
| `<δ_B drift>` | `<±27 ms>` | rectangular | √3 | `<15.6>` |
| `<δ_sync,rel residual>` | `<±10 ms>` | rectangular | √3 | `<5.8>` |
| `<δ_host timestamping>` | `<±2 ms>` | rectangular | √3 | `<1.2>` |
| **Combined u_c** | | | | `<22.8>` |
| **Expanded U = k·u_c, k = 2** | | | | **`<45.6>`** |

**Basis of each limit:** for every row, state whether it is measured from your
own logs, taken from a datasheet, or assumed. Values inherited from a citation
that measured something else are assumptions, not measurements — label them so.

**Correlation assumptions:** state which components are treated as independent
and why. Where independence is not defensible, estimate the covariances or work
directly from empirical offset distributions.

**Double-counting check:** if `δ_sync,rel` was estimated empirically from
end-to-end offset logs, host-side effects already inside that estimate must not
be added again as a separate `δ_host`.

**Fitness for purpose:** `<U ≈ 46 ms is negligible for daily step counts and
material for cross-modal latency estimation. The same dataset can be fit for one
purpose and unfit for another; state which.>`

---

## Part B — justification, where a budget could not be established

MRC-05 permits a documented justification instead of a budget. To carry
information, that justification must contain all three of the following.
"Uncertainty could not be established" alone does not satisfy the item.

1. **Dominant uncertainty sources**, named. Which terms would appear in the
   budget if you could evaluate them?
2. **Why each could not be quantified.** No reference instrument available? No
   access to firmware timing behaviour? Vendor does not disclose the sampling
   implementation?
3. **What validation evidence is offered instead** — bench comparison,
   concurrent-device agreement, published device validation with a statement of
   whether its conditions match yours (bench repeatability evidence does not
   transfer to a multi-month multi-device field deployment).

---

## Reporting language

Replace silence with a statement. Before:

> "Signals from both devices were recorded continuously and timestamped."

After:

> "Device clocks were reconciled to the phone at each BLE reconnection; residual
> cross-device synchronization uncertainty, estimated from logged offsets, was
> U = `<X>` ms (k = 2); PAT is reported with this uncertainty, and windows
> exceeding `<Z>` ms were excluded."
