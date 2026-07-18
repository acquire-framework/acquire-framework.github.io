"""Shared plotting style for the website.

Not part of the distributed package: the figures on the site must match the
instrument visual system, but nothing in `acquire/` may depend on matplotlib
(it would break the Pyodide build).
"""

from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt

# Figures are rendered once at build time and cannot follow the reader's theme.
# They are therefore styled light and given an explicit light background, so
# they stay legible as a light card when the page is viewed in dark mode. Every
# ink colour below meets WCAG AA against this background.
BG = "#f6f5f3"
SURFACE = "#ffffff"
TEXT = "#1b1a19"
MUTED = "#55504b"
ACCENT = "#0b6e63"
PASS = "#1149a8"
FAIL = "#9a4409"
BORDER = "#c9c5bf"


def style() -> None:
    """Apply the ACQUIRE figure style. Call once per page."""
    mpl.rcParams.update(
        {
            "figure.facecolor": BG,
            "axes.facecolor": BG,
            "savefig.facecolor": BG,
            "axes.edgecolor": BORDER,
            "axes.labelcolor": MUTED,
            "axes.titlecolor": TEXT,
            "text.color": TEXT,
            "xtick.color": MUTED,
            "ytick.color": MUTED,
            "grid.color": BORDER,
            "grid.linewidth": 0.5,
            "axes.grid": True,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "font.family": "monospace",
            "font.size": 8,
            "axes.titlesize": 9,
            "axes.titleweight": "600",
            "figure.dpi": 130,
            "legend.frameon": False,
        }
    )


def rate_trace(ax, df, nominal_hz, window_s=30.0):
    """Plot effective sampling rate over time against the nominal rate.

    This is the site's signature figure: the fault is visible as a shelf, and
    the shelf is real data, not decoration.
    """
    from acquire.schema import seconds

    t = seconds(df)
    edges = list(range(0, int(t[-1]), int(window_s)))
    centres, rates = [], []
    for start in edges:
        n = ((t >= start) & (t < start + window_s)).sum()
        centres.append((start + window_s / 2) / 60.0)
        rates.append(n / window_s)

    ax.axhline(nominal_hz, color=MUTED, lw=0.8, ls="--", label=f"nominal {nominal_hz:g} Hz")
    ax.plot(centres, rates, color=ACCENT, lw=1.2, label="effective")
    ax.fill_between(
        centres,
        rates,
        nominal_hz,
        where=[r < nominal_hz * 0.95 for r in rates],
        color=FAIL,
        alpha=0.22,
        interpolate=True,
    )
    ax.set_xlabel("minutes into recording")
    ax.set_ylabel("Hz")
    ax.set_ylim(0, nominal_hz * 1.25)
    ax.legend(loc="lower left", fontsize=7)
    return ax


def new_axes(height=2.0):
    fig, ax = plt.subplots(figsize=(7.2, height))
    return fig, ax
