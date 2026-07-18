# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Mateusz Danioł, Ryszard Sroka
"""Synthetic tri-axial data with deliberately injected faults.

Demonstrating that a detector catches a fault you *planted* is a stronger claim
than showing it on data that happened to be broken: the ground truth is known,
so detection rate can be measured rather than asserted.

Every fault here corresponds to a recipe in the catalogue.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from .schema import AXES, G, TIME


@dataclass
class Fault:
    """A fault to inject.

    kind
        ``throttle``  keep only a fraction of samples (OS power management)
        ``gap``       remove a span entirely (app killed, BLE dropout)
        ``drift``     accumulate timestamp error (clock desync)
        ``stuck``     freeze values (dead sensor still reporting)
        ``clip``      saturate to a rail (range misconfigured)
        ``scale``     multiply values (units recorded in g, not m/s^2)
    start, end
        Bounds in seconds. ``end=None`` runs to the end of the recording.
    factor
        Interpretation depends on ``kind``; see :func:`inject`.
    """

    kind: str
    start: float = 0.0
    end: float | None = None
    factor: float = 0.5


def clean(
    duration_s: float = 3600.0,
    rate_hz: float = 50.0,
    seed: int = 0,
    resting_fraction: float = 0.4,
) -> pd.DataFrame:
    """Generate a fault-free recording.

    The signal is a resting device (gravity on z, small sensor noise) punctuated
    by bouts of movement, which is what an overnight in-the-wild recording looks
    like and what the resting-magnitude check depends on.
    """
    rng = np.random.default_rng(seed)
    n = int(duration_s * rate_hz)
    t = np.arange(n) / rate_hz

    # Movement envelope: quiet for `resting_fraction` of the time.
    envelope = np.zeros(n)
    n_bouts = max(1, int(duration_s / 300))
    for _ in range(n_bouts):
        centre = rng.uniform(0, duration_s)
        width = rng.uniform(20, 90)
        envelope += np.exp(-0.5 * ((t - centre) / width) ** 2)
    envelope *= (1.0 - resting_fraction) * 6.0

    walk = 2.0 * np.pi * 1.9 * t  # ~1.9 Hz, human gait
    ax = envelope * 0.6 * np.sin(walk) + rng.normal(0, 0.04, n)
    ay = envelope * 0.4 * np.cos(walk * 0.5) + rng.normal(0, 0.04, n)
    az = G + envelope * 0.8 * np.sin(walk + 0.7) + rng.normal(0, 0.04, n)

    return pd.DataFrame({TIME: t, "ax": ax, "ay": ay, "az": az})


def inject(df: pd.DataFrame, fault: Fault, seed: int = 0) -> pd.DataFrame:
    """Return a copy of *df* with *fault* applied."""
    rng = np.random.default_rng(seed)
    out = df.copy().reset_index(drop=True)
    t = out[TIME].to_numpy(dtype=float)
    end = float(t[-1]) if fault.end is None else fault.end
    window = (t >= fault.start) & (t <= end)

    if fault.kind == "throttle":
        # Keep `factor` of the samples in the window: effective rate drops while
        # the nominal rate the app requested stays unchanged.
        idx = np.where(window)[0]
        drop = rng.choice(idx, size=int(len(idx) * (1 - fault.factor)), replace=False)
        out = out.drop(index=drop).reset_index(drop=True)

    elif fault.kind == "gap":
        out = out.loc[~window].reset_index(drop=True)

    elif fault.kind == "drift":
        # factor = seconds of error accumulated per hour.
        elapsed = np.clip(t - fault.start, 0, None)
        out[TIME] = t + elapsed * (fault.factor / 3600.0)

    elif fault.kind == "stuck":
        first = int(np.argmax(window))
        for axis in AXES:
            out.loc[window, axis] = out[axis].iloc[first]

    elif fault.kind == "clip":
        for axis in AXES:
            vals = out[axis].to_numpy(dtype=float, copy=True)
            vals[window] = np.clip(vals[window], -fault.factor, fault.factor)
            out[axis] = vals

    elif fault.kind == "scale":
        for axis in AXES:
            vals = out[axis].to_numpy(dtype=float, copy=True)
            vals[window] = vals[window] * fault.factor
            out[axis] = vals

    else:
        raise ValueError(f"unknown fault kind: {fault.kind!r}")

    return out


def faulty(
    duration_s: float = 3600.0,
    rate_hz: float = 50.0,
    seed: int = 0,
    faults: list[Fault] | None = None,
) -> pd.DataFrame:
    """Generate a recording with a default, realistic set of injected faults.

    The defaults reproduce the canonical overnight failure: the device is idle,
    the OS throttles sensor delivery, and the app is briefly killed.
    """
    if faults is None:
        faults = [
            Fault("throttle", start=duration_s * 0.5, factor=0.55),
            Fault("gap", start=duration_s * 0.72, end=duration_s * 0.72 + 45),
        ]
    df = clean(duration_s=duration_s, rate_hz=rate_hz, seed=seed)
    for i, fault in enumerate(faults):
        df = inject(df, fault, seed=seed + i + 1)
    return df
