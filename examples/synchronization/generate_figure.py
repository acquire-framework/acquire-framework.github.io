#!/usr/bin/env python3
"""Cross-device clock drift under re-anchoring at BLE reconnection.

Reproduces Figure 2 of the accompanying paper and the offset series behind it,
so a reviewer can confirm that the plotted excursions follow from the stated
ppm values and re-anchor intervals.

All values are synthetic [A]. No participant or device data is used.

Model (Section 5 of the paper)
------------------------------
Two BLE devices timestamp on free-running real-time clocks with fractional
frequency offsets of +40 and -25 ppm relative to the phone. Each device's clock
error accumulates linearly since its last re-anchor and is reset to the residual
reconciliation error at every reconnection. Reconnections occur every 2-3.5 h.

The point of the figure is that completeness stays at 100% and every
conventional quality flag stays green while the inter-device offset grows past
any tolerance a latency measurand such as pulse-arrival time would demand.

Usage
-----
    python generate_figure.py

Outputs (written next to this script)
-------------------------------------
    fig-clock-drift.pdf / .png   the figure
    synthetic_offsets.csv        the offset series behind it

Requires only Python with NumPy, pandas and Matplotlib.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ── declared assumptions ────────────────────────────────────────────────────
# Every number the figure depends on is stated here rather than buried in the
# plotting code, so the assumptions can be audited and varied.

DURATION_H = 24.0          # length of the simulated recording
SAMPLE_S = 30.0            # offset evaluated every 30 s
PPM_A = +40.0              # device A fractional frequency offset [ppm]
PPM_B = -25.0              # device B fractional frequency offset [ppm]
REANCHOR_MIN_H = 2.0       # BLE reconnection interval, lower bound
REANCHOR_MAX_H = 3.5       # BLE reconnection interval, upper bound
RESIDUAL_MS = 10.0         # reconciliation residual retained at re-anchor [ms]
SEED = 20260718            # fixed so the artifact is bit-reproducible

# Tolerance band drawn for reference: a latency measurand such as PAT would
# require the inter-device offset to stay inside single-digit to low-tens of ms.
PAT_TOLERANCE_MS = 20.0

ACCENT = "#0b6e63"
FAIL = "#9a4409"
PASS = "#1149a8"
MUTED = "#55504b"
BORDER = "#c9c5bf"
BG = "#f6f5f3"


def reanchor_times(rng: np.random.Generator) -> np.ndarray:
    """Reconnection instants, drawn uniformly in [REANCHOR_MIN_H, REANCHOR_MAX_H]."""
    times, t = [], 0.0
    while True:
        t += rng.uniform(REANCHOR_MIN_H, REANCHOR_MAX_H) * 3600.0
        if t >= DURATION_H * 3600.0:
            break
        times.append(t)
    return np.asarray(times)


def clock_error(t: np.ndarray, ppm: float, anchors: np.ndarray,
                rng: np.random.Generator) -> np.ndarray:
    """Clock error in milliseconds, accumulating since the last re-anchor.

    At each re-anchor the error is reset to a residual drawn within
    +/- RESIDUAL_MS: reconciliation bounds the error but does not zero it.
    """
    error = np.empty_like(t)
    # Residual left behind by each reconciliation, including the initial one.
    residuals = rng.uniform(-RESIDUAL_MS, RESIDUAL_MS, size=len(anchors) + 1)
    edges = np.concatenate(([0.0], anchors, [t[-1] + 1.0]))

    for i in range(len(edges) - 1):
        seg = (t >= edges[i]) & (t < edges[i + 1])
        if not seg.any():
            continue
        elapsed = t[seg] - edges[i]
        # ppm is parts per million of elapsed time; x1000 converts s -> ms.
        error[seg] = residuals[i] + elapsed * ppm * 1e-6 * 1e3
    return error


def main() -> None:
    here = Path(__file__).resolve().parent
    rng = np.random.default_rng(SEED)

    t = np.arange(0.0, DURATION_H * 3600.0, SAMPLE_S)
    anchors = reanchor_times(rng)

    err_a = clock_error(t, PPM_A, anchors, rng)
    err_b = clock_error(t, PPM_B, anchors, rng)
    # The measurand of interest is the difference: common-mode error cancels.
    inter = err_a - err_b

    frame = pd.DataFrame(
        {
            "t_s": t,
            "t_h": t / 3600.0,
            "device_a_offset_ms": err_a,
            "device_b_offset_ms": err_b,
            "inter_device_offset_ms": inter,
            "completeness": 1.0,          # every sample present, by construction
            "quality_flag": "ok",         # every conventional flag green
        }
    )
    frame.to_csv(here / "synthetic_offsets.csv", index=False)

    # ── figure ──────────────────────────────────────────────────────────────
    plt.rcParams.update(
        {
            "figure.facecolor": BG, "axes.facecolor": BG, "savefig.facecolor": BG,
            "axes.edgecolor": BORDER, "axes.labelcolor": MUTED,
            "text.color": "#1b1a19", "xtick.color": MUTED, "ytick.color": MUTED,
            "grid.color": BORDER, "grid.linewidth": 0.5, "axes.grid": True,
            "axes.spines.top": False, "axes.spines.right": False,
            "font.family": "monospace", "font.size": 8, "legend.frameon": False,
        }
    )

    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(7.0, 4.4), sharex=True,
        gridspec_kw={"height_ratios": [1.0, 1.15]},
    )

    for a in anchors / 3600.0:
        ax1.axvline(a, color=BORDER, lw=0.7, zorder=0)
        ax2.axvline(a, color=BORDER, lw=0.7, zorder=0)

    ax1.plot(frame.t_h, err_a, color=PASS, lw=1.0, label=f"device A ({PPM_A:+.0f} ppm)")
    ax1.plot(frame.t_h, err_b, color=ACCENT, lw=1.0, label=f"device B ({PPM_B:+.0f} ppm)")
    ax1.axhline(0, color=MUTED, lw=0.7, ls="--")
    ax1.set_ylabel("offset vs phone [ms]")
    ax1.legend(loc="upper left", fontsize=7, ncol=2)
    ax1.set_title(
        "Clock drift between re-anchors — completeness 100%, all quality flags green",
        loc="left", fontsize=8.5, fontweight="bold",
    )

    ax2.plot(frame.t_h, inter, color=FAIL, lw=1.2, label="inter-device offset")
    ax2.axhspan(-PAT_TOLERANCE_MS, PAT_TOLERANCE_MS, color=PASS, alpha=0.10,
                label=f"±{PAT_TOLERANCE_MS:.0f} ms tolerance for a latency measurand")
    ax2.axhline(0, color=MUTED, lw=0.7, ls="--")
    ax2.set_ylabel("A − B [ms]")
    ax2.set_xlabel("hours into recording   (vertical lines: BLE reconnection / re-anchor)")
    ax2.legend(loc="upper left", fontsize=7)

    exceeded = float(np.mean(np.abs(inter) > PAT_TOLERANCE_MS))
    ax2.text(
        0.99, 0.06,
        f"|offset| > {PAT_TOLERANCE_MS:.0f} ms for {exceeded:.0%} of the recording;"
        f" peak {np.abs(inter).max():.0f} ms",
        transform=ax2.transAxes, ha="right", fontsize=7.5, color=FAIL,
    )

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(here / f"fig-clock-drift.{ext}", dpi=200, bbox_inches="tight")

    print(f"re-anchors:            {len(anchors)}")
    print(f"peak |inter-device|:   {np.abs(inter).max():.1f} ms")
    print(f"fraction beyond ±{PAT_TOLERANCE_MS:.0f} ms: {exceeded:.1%}")
    print(f"completeness:          {frame.completeness.mean():.0%}")
    print("wrote fig-clock-drift.pdf, fig-clock-drift.png, synthetic_offsets.csv")


if __name__ == "__main__":
    main()
