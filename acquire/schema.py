# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Mateusz Danioł, Ryszard Sroka
"""The canonical ACQUIRE schema for tri-axial inertial data.

Defining this schema explicitly is a deliverable, not an inconvenience: a
framework arguing for standardisation must say what it standardises on. Format
adapters convert vendor exports into this shape; every diagnostic consumes it.

Minimal contract
----------------
timestamp : float seconds since recording start, or datetime64
ax, ay, az : linear acceleration in m/s^2

Optional
--------
device_id : str, identifies the recording device when several are pooled
"""

from __future__ import annotations

import numpy as np
import pandas as pd

TIME = "timestamp"
AXES = ("ax", "ay", "az")
DEVICE = "device_id"

REQUIRED = (TIME, *AXES)

#: Standard gravity, m/s^2. The reference value for the resting-magnitude check.
G = 9.80665


class SchemaError(ValueError):
    """Raised when a frame does not satisfy the canonical schema."""


def validate(df: pd.DataFrame) -> None:
    """Raise :class:`SchemaError` if *df* does not satisfy the schema.

    Error messages name what was expected and what was found — a validity tool
    that fails obscurely is self-defeating.
    """
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise SchemaError(
            f"missing required column(s): {', '.join(missing)}. "
            f"Found: {', '.join(map(str, df.columns))}. "
            f"Required: {', '.join(REQUIRED)}."
        )
    if len(df) < 2:
        raise SchemaError(f"need at least 2 samples to assess timing, got {len(df)}")

    for axis in AXES:
        if not np.issubdtype(df[axis].dtype, np.number):
            raise SchemaError(f"column '{axis}' must be numeric, got {df[axis].dtype}")


def seconds(df: pd.DataFrame) -> np.ndarray:
    """Return the timestamp column as float seconds since the first sample.

    Accepts either float seconds or datetime64, so adapters need not normalise
    time representation themselves.
    """
    t = df[TIME]
    if np.issubdtype(t.dtype, np.datetime64):
        t = (t - t.iloc[0]).dt.total_seconds()
        return t.to_numpy(dtype=float)
    arr = t.to_numpy(dtype=float)
    return arr - arr[0]


def magnitude(df: pd.DataFrame) -> np.ndarray:
    """Return the Euclidean norm of the three acceleration axes."""
    return np.sqrt(sum(df[axis].to_numpy(dtype=float) ** 2 for axis in AXES))
