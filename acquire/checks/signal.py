"""Signal-value diagnostics: units, stuck sensors, saturation.

These checks exploit the one piece of ground truth available in every inertial
recording without any labelling effort: a device at rest measures exactly one g.
That makes unit and scale errors detectable from the data alone, which is the
metrological core of the framework.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from ..report import CheckResult
from ..schema import AXES, G, magnitude, seconds


def _resting_mask(df: pd.DataFrame, quantile: float = 0.2) -> np.ndarray:
    """Identify the quietest samples, which are assumed to be at rest.

    Uses a rolling standard deviation of the magnitude over roughly one second
    and takes the lowest *quantile*. Deliberately assumption-light: it does not
    require the device to be still for any particular duration, only that the
    recording contains some quiet time.
    """
    t = seconds(df)
    elapsed = t[-1] - t[0]
    rate = (len(df) - 1) / elapsed if elapsed > 0 else 1.0
    window = max(3, int(round(rate)))

    mag = pd.Series(magnitude(df))
    rolling = mag.rolling(window, center=True, min_periods=3).std()
    threshold = rolling.quantile(quantile)
    return (rolling <= threshold).to_numpy(dtype=bool)


def check_resting_magnitude(df: pd.DataFrame, tolerance: float = 0.02) -> CheckResult:
    """Verify that the device at rest measures one g.

    This is the framework's showcase diagnostic because the expected value is
    a physical constant, not a convention: any deviation is a real measurement
    error. A ratio near 1/9.81 means the data is in g rather than m/s²; a ratio
    that is neither 1 nor a familiar unit conversion points at miscalibration.
    """
    mask = _resting_mask(df)
    n_rest = int(mask.sum())
    if n_rest < 10:
        return CheckResult(
            id="SIG-01",
            title="Resting magnitude",
            passed=False,
            value="insufficient quiet samples",
            expected=f"{G:.3f} m/s² ±{tolerance:.0%}",
            detail=(
                "Fewer than 10 low-motion samples found, so the reference cannot "
                "be established. This is itself suspicious for an in-the-wild "
                "recording, which should contain substantial idle time."
            ),
            recipe="recipes/02-unit-scale-mismatch.html",
        )

    observed = float(np.mean(magnitude(df)[mask]))
    ratio = observed / G
    passed = abs(1 - ratio) <= tolerance

    hint = ""
    if not passed:
        if abs(ratio - 1 / G) < 0.05:
            hint = " Consistent with data recorded in g rather than m/s²."
        elif abs(ratio - G) < 0.5:
            hint = " Consistent with a gravity conversion applied twice."

    return CheckResult(
        id="SIG-01",
        title="Resting magnitude",
        passed=passed,
        value=f"{observed:.3f} m/s² ({ratio:.3f} g)",
        expected=f"{G:.3f} m/s² ±{tolerance:.0%}",
        detail=f"Estimated from {n_rest} low-motion samples.{hint}",
        recipe="recipes/02-unit-scale-mismatch.html",
    )


def check_stuck(df: pd.DataFrame, max_run_s: float = 2.0) -> CheckResult:
    """Detect a sensor that stopped updating while continuing to report.

    A dead sensor that still emits its last value is the most dangerous failure
    in the catalogue: the stream looks healthy to any monitoring that only
    checks whether data is arriving.
    """
    t = seconds(df)
    elapsed = t[-1] - t[0]
    rate = (len(df) - 1) / elapsed if elapsed > 0 else 1.0

    identical = np.ones(len(df) - 1, dtype=bool)
    for axis in AXES:
        vals = df[axis].to_numpy(dtype=float)
        identical &= np.diff(vals) == 0

    longest = 0
    current = 0
    for flag in identical:
        current = current + 1 if flag else 0
        longest = max(longest, current)

    longest_s = longest / rate if rate > 0 else 0.0

    return CheckResult(
        id="SIG-02",
        title="Stuck sensor",
        passed=longest_s <= max_run_s,
        value=f"longest frozen run {longest_s:.1f} s",
        expected=f"≤ {max_run_s:.1f} s",
        detail=(
            "All three axes identical across consecutive samples. Genuine "
            "stillness still produces sensor noise, so exact repetition is a "
            "hardware or driver fault, not a quiet participant."
        ),
        recipe="recipes/04-stuck-sensor.html",
    )


def check_clipping(df: pd.DataFrame, max_fraction: float = 0.001) -> CheckResult:
    """Detect saturation against the configured measurement range.

    Clipping means the range was set too narrow for the activity being measured.
    The samples are not merely noisy, they are censored, and no downstream
    filtering recovers them.
    """
    total = 0
    n = len(df)
    rail = 0.0
    for axis in AXES:
        vals = np.abs(df[axis].to_numpy(dtype=float))
        peak = float(vals.max())
        rail = max(rail, peak)
        # Samples sitting within 0.1% of the observed peak are treated as railed.
        total += int((vals >= peak * 0.999).sum())

    fraction = total / (n * len(AXES))

    return CheckResult(
        id="SIG-03",
        title="Saturation",
        passed=fraction <= max_fraction,
        value=f"{fraction:.3%} of samples at rail (±{rail:.1f} m/s²)",
        expected=f"≤ {max_fraction:.1%}",
        detail=(
            "Repeated samples at the extreme of the observed range indicate the "
            "sensor range was configured too narrow for the measured activity."
        ),
        recipe="recipes/05-range-saturation.html",
    )
