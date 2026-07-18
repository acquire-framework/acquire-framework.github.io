"""Timing diagnostics: sampling rate, gaps, monotonicity, drift.

Timing faults are the archetypal in-the-wild failure — they are invisible in
summary statistics, survive every plausible sanity check on the values
themselves, and silently bias any frequency-domain feature computed downstream.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from ..report import CheckResult
from ..schema import TIME, seconds


def check_rate(
    df: pd.DataFrame, nominal_hz: float, tolerance: float = 0.05
) -> CheckResult:
    """Compare the effective sampling rate against the rate the app requested.

    The effective rate is samples-per-elapsed-second over the whole recording,
    which is the quantity that actually matters for analysis. Nominal rate is
    what the application asked the OS for; the two diverge silently whenever
    power management intervenes.
    """
    t = seconds(df)
    elapsed = t[-1] - t[0]
    effective = (len(df) - 1) / elapsed if elapsed > 0 else float("nan")
    ratio = effective / nominal_hz
    passed = abs(1 - ratio) <= tolerance

    return CheckResult(
        id="TIME-01",
        title="Effective vs nominal sampling rate",
        passed=passed,
        value=f"{effective:.2f} Hz ({ratio:.0%} of nominal)",
        expected=f"{nominal_hz:.2f} Hz ±{tolerance:.0%}",
        detail=(
            f"{len(df)} samples over {elapsed:.1f} s. "
            "A deficit concentrated in time indicates throttling; a uniform "
            "deficit indicates the requested rate was never honoured."
        ),
        recipe="recipes/03-doze-downsampling.html",
    )


def check_gaps(df: pd.DataFrame, max_gap_s: float = 1.0) -> CheckResult:
    """Count interruptions longer than *max_gap_s*.

    Reported separately from sampling rate because the two have different
    causes: a gap is the stream stopping, a rate deficit is the stream
    thinning. Averaging them together hides both.
    """
    t = seconds(df)
    intervals = np.diff(t)
    gaps = intervals[intervals > max_gap_s]
    total = float(gaps.sum())
    passed = len(gaps) == 0

    if len(gaps):
        worst = f", longest {gaps.max():.1f} s"
    else:
        worst = ""

    return CheckResult(
        id="TIME-02",
        title="Stream continuity",
        passed=passed,
        value=f"{len(gaps)} gaps, {total:.1f} s lost{worst}",
        expected=f"no interval > {max_gap_s:.1f} s",
        detail=(
            "Gaps clustering overnight or during device idle periods point to "
            "OS power management rather than hardware or connectivity."
        ),
        recipe="recipes/03-doze-downsampling.html",
    )


def check_monotonic(df: pd.DataFrame) -> CheckResult:
    """Verify timestamps strictly increase.

    Non-monotonic timestamps mean the clock was reset or two sources were merged
    incorrectly. Any windowing performed on such a series is meaningless, so this
    check gates the others.
    """
    t = df[TIME].to_numpy()
    if np.issubdtype(t.dtype, np.datetime64):
        t = t.astype("datetime64[ns]").astype(np.int64)
    else:
        t = t.astype(float)

    violations = int((np.diff(t) <= 0).sum())

    return CheckResult(
        id="TIME-03",
        title="Timestamp monotonicity",
        passed=violations == 0,
        value=f"{violations} non-increasing steps",
        expected="0",
        detail=(
            "Backward steps usually indicate a clock reset (NTP correction, "
            "timezone change, or device reboot) mid-recording."
        ),
        recipe="recipes/01-clock-drift.html",
    )


def check_regularity(df: pd.DataFrame, tolerance: float = 0.25) -> CheckResult:
    """Assess how *evenly* samples are spaced, independent of their average rate.

    A recording can hit its nominal rate on average while delivering samples in
    irregular bursts — common when a sensor is batched in hardware FIFO and
    flushed opportunistically. Bursty delivery breaks any analysis assuming
    uniform sampling, so it is measured separately.
    """
    t = seconds(df)
    intervals = np.diff(t)
    median = float(np.median(intervals))

    # Upper-tail dispersion rather than median absolute deviation. MAD collapses
    # to zero whenever more than half the intervals are identical — which is the
    # normal case for a stream that is mostly regular with occasional dropouts,
    # exactly the condition this check must not miss.
    upper = float(np.quantile(intervals, 0.9))
    jitter = (upper - median) / median if median > 0 else float("nan")

    return CheckResult(
        id="TIME-04",
        title="Sampling regularity",
        passed=jitter <= tolerance,
        value=f"jitter {jitter:.1%} above median interval (p90)",
        expected=f"≤ {tolerance:.0%}",
        detail=(
            f"Median interval {median * 1000:.1f} ms. High jitter with a correct "
            "mean rate indicates hardware FIFO batching rather than sample loss."
        ),
        recipe="recipes/03-doze-downsampling.html",
    )
