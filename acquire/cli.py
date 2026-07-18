"""Command-line interface: ``acquire check <path> --nominal 50``.

Designed to run in CI against incoming study data, which is the intended
production use. The browser widget on the website is a demonstration of these
same checks, not a replacement for them.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

from . import __version__, check
from .schema import SchemaError


def _read(path: Path) -> pd.DataFrame:
    if path.suffix.lower() in {".parquet", ".pq"}:
        return pd.read_parquet(path)
    return pd.read_csv(path)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="acquire",
        description="Diagnostics for reproducible in-the-wild sensing studies.",
    )
    parser.add_argument("--version", action="version", version=f"acquire {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("check", help="run diagnostics against a recording")
    run.add_argument("path", type=Path, help="CSV or Parquet file")
    run.add_argument(
        "--nominal",
        type=float,
        required=True,
        metavar="HZ",
        help="sampling rate the application requested (cannot be inferred)",
    )
    run.add_argument("--max-gap", type=float, default=1.0, metavar="S")

    args = parser.parse_args(argv)

    try:
        df = _read(args.path)
    except FileNotFoundError:
        print(f"error: no such file: {args.path}", file=sys.stderr)
        return 2
    except Exception as exc:  # noqa: BLE001 - surface the reader's own message
        print(f"error: could not read {args.path}: {exc}", file=sys.stderr)
        return 2

    try:
        report = check(df, nominal_hz=args.nominal, max_gap_s=args.max_gap)
    except SchemaError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    print(report)
    # Non-zero exit on failure so this can gate a CI pipeline.
    return 0 if report.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
