# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Mateusz Danioł, Ryszard Sroka
"""Guard the in-browser build.

The website's interactive checker runs this package under Pyodide, which only
provides numpy, pandas and scipy. A dependency added casually for convenience
would break the browser widget silently and only be noticed after deploy, so
the constraint is asserted here rather than documented and hoped for.
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path

PYODIDE_AVAILABLE = {"numpy", "pandas", "scipy"}
PACKAGE = Path(__file__).resolve().parent.parent / "acquire"


def _third_party_imports(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    found: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            found.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            # level > 0 is a relative import within the package.
            if node.level == 0 and node.module:
                found.add(node.module.split(".")[0])
    return {
        name
        for name in found
        if name not in sys.stdlib_module_names and name != "acquire"
    }


def test_core_package_only_imports_pyodide_available_packages():
    offenders: dict[str, set[str]] = {}
    for path in PACKAGE.rglob("*.py"):
        extra = _third_party_imports(path) - PYODIDE_AVAILABLE
        if extra:
            offenders[str(path.relative_to(PACKAGE.parent))] = extra

    assert not offenders, (
        "these modules import packages unavailable in Pyodide, which would break "
        f"the in-browser checker: {offenders}"
    )
