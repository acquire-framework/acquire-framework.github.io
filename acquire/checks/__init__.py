"""Individual diagnostics. One module per failure family."""

from .signal import check_clipping, check_resting_magnitude, check_stuck
from .timing import check_gaps, check_monotonic, check_rate, check_regularity

__all__ = [
    "check_clipping",
    "check_gaps",
    "check_monotonic",
    "check_rate",
    "check_regularity",
    "check_resting_magnitude",
    "check_stuck",
]
