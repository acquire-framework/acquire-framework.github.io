# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Mateusz Danioł, Ryszard Sroka
"""ACQUIRE — diagnostics for reproducible in-the-wild sensing studies.

    >>> import acquire
    >>> df = acquire.synth.faulty()
    >>> report = acquire.check(df, nominal_hz=50)
    >>> print(report)
"""

from __future__ import annotations

import pandas as pd

from . import checks, schema, synth
from .report import CheckResult, Report
from .schema import SchemaError

#: Package version. The patch component moves independently of the spec:
#: 26.7.N implements ACQUIRE spec 26.7, and N increments for code fixes
#: that change no requirement.
__version__ = "26.7.2"

#: The version of the normative framework content this package implements.
#: Reports stamp it, so a quality-control record stays interpretable.
SPEC_VERSION = "26.7.2"

__all__ = [
    "CheckResult",
    "Report",
    "SchemaError",
    "SPEC_VERSION",
    "__version__",
    "check",
    "checks",
    "schema",
    "synth",
]

#: Stated in every passing report. Naming the limits of a diagnostic is part of
#: the diagnostic: a green result that stays silent about its scope invites
#: exactly the false confidence this framework exists to prevent.
NOT_CHECKED = (
    "Whether the sensor was calibrated against a reference instrument",
    "Whether device clocks agree with each other or with wall time",
    "Whether the participant wore or carried the device as instructed",
    "Whether the recorded activity matches any label or diary entry",
    "Anything about signal streams other than tri-axial acceleration",
)


def check(
    df: pd.DataFrame,
    nominal_hz: float,
    *,
    max_gap_s: float = 1.0,
    rate_tolerance: float = 0.05,
) -> Report:
    """Run the full v0.1 diagnostic suite against a recording.

    Parameters
    ----------
    df
        A frame satisfying the canonical schema (see :mod:`acquire.schema`).
    nominal_hz
        The sampling rate the application *requested*. This cannot be inferred
        from the data — inferring it would define away the most common failure
        in the catalogue — so it must be supplied.
    """
    schema.validate(df)

    report = Report(
        not_checked=list(NOT_CHECKED),
        spec_version=SPEC_VERSION,
        package_version=__version__,
    )

    # Monotonicity gates everything else: windowing a non-monotonic series is
    # meaningless, so it is evaluated first and reported first.
    monotonic = checks.check_monotonic(df)
    report.add(monotonic)

    if monotonic.passed:
        report.add(checks.check_rate(df, nominal_hz, tolerance=rate_tolerance))
        report.add(checks.check_gaps(df, max_gap_s=max_gap_s))
        report.add(checks.check_regularity(df))

    report.add(checks.check_resting_magnitude(df))
    report.add(checks.check_stuck(df))
    report.add(checks.check_clipping(df))

    return report
