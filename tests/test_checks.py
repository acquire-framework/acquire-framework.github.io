"""Each diagnostic is tested against a fault whose ground truth is known.

This is the layer that matters most: a diagnostic which silently fails to
detect is worse than no diagnostic at all, because it converts an unknown
problem into a false assurance.
"""

from __future__ import annotations

import pytest

import acquire
from acquire.synth import Fault, clean, inject


@pytest.fixture(scope="module")
def good():
    return clean(duration_s=1200, rate_hz=50, seed=7)


def test_clean_data_passes_every_check(good):
    report = acquire.check(good, nominal_hz=50)
    assert report.passed, f"false positives on clean data:\n{report}"


def test_clean_report_declares_its_own_scope(good):
    report = acquire.check(good, nominal_hz=50)
    assert report.not_checked, "a passing report must state what it did not check"


def _result(report, check_id):
    return next(r for r in report.results if r.id == check_id)


def test_detects_throttling(good):
    df = inject(good, Fault("throttle", start=600, factor=0.5))
    assert not _result(acquire.check(df, nominal_hz=50), "TIME-01").passed


def test_detects_gap(good):
    df = inject(good, Fault("gap", start=600, end=640))
    assert not _result(acquire.check(df, nominal_hz=50), "TIME-02").passed


def test_gross_clock_drift_surfaces_as_a_rate_error(good):
    # 600 s/hour (17%) distorts elapsed time enough to breach the rate tolerance.
    df = inject(good, Fault("drift", start=0, factor=600))
    assert not _result(acquire.check(df, nominal_hz=50), "TIME-01").passed


def test_modest_clock_drift_is_NOT_detectable_without_a_reference(good):
    """Documents a real limit of the method rather than papering over it.

    Nothing in a single recording distinguishes "the clock drifted" from
    "sampling ran slightly slow": both stretch elapsed time identically.
    Detecting modest drift requires an external reference — a second device,
    NTP, or wall time — which is why this appears in ``NOT_CHECKED`` rather
    than as a check that quietly under-performs.
    """
    df = inject(good, Fault("drift", start=0, factor=120))  # 3.3% distortion
    report = acquire.check(df, nominal_hz=50)
    assert _result(report, "TIME-01").passed
    assert any("clocks agree" in item for item in report.not_checked)


def test_detects_stuck_sensor(good):
    df = inject(good, Fault("stuck", start=600, end=640))
    assert not _result(acquire.check(df, nominal_hz=50), "SIG-02").passed


def test_detects_clipping(good):
    df = inject(good, Fault("clip", start=0, factor=5.0))
    assert not _result(acquire.check(df, nominal_hz=50), "SIG-03").passed


def test_detects_units_recorded_in_g(good):
    """Data in g rather than m/s² is the archetypal silent scale error."""
    df = inject(good, Fault("scale", start=0, factor=1 / 9.80665))
    result = _result(acquire.check(df, nominal_hz=50), "SIG-01")
    assert not result.passed
    assert "in g rather than" in result.detail


def test_irregular_delivery_is_flagged_despite_correct_median(good):
    """Guards the MAD degeneracy: mostly-regular streams with dropouts."""
    df = inject(good, Fault("throttle", start=0, factor=0.6))
    assert not _result(acquire.check(df, nominal_hz=50), "TIME-04").passed


@pytest.mark.parametrize("magnitude", [0.30, 0.45, 0.60, 0.75])
def test_throttle_detection_rate_against_fault_magnitude(good, magnitude):
    """Sensitivity is measured, not assumed — this table is the EVIDENCE block."""
    df = inject(good, Fault("throttle", start=0, factor=magnitude))
    result = _result(acquire.check(df, nominal_hz=50), "TIME-01")
    # A uniform deficit of 25% or more must always be caught.
    assert not result.passed


def test_schema_error_names_the_missing_column(good):
    with pytest.raises(acquire.SchemaError, match="ax"):
        acquire.check(good.drop(columns=["ax"]), nominal_hz=50)


def test_nonmonotonic_time_gates_the_timing_checks(good):
    df = good.copy()
    df.loc[100, "timestamp"] = df.loc[50, "timestamp"]
    report = acquire.check(df, nominal_hz=50)
    assert not _result(report, "TIME-03").passed
    # Rate and continuity are meaningless on a broken clock, so they are skipped.
    assert all(r.id != "TIME-01" for r in report.results)
