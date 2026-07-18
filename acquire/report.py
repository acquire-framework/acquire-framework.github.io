"""Result types for ACQUIRE diagnostics."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class CheckResult:
    """The outcome of a single diagnostic.

    ``value`` and ``expected`` are kept separate and reported verbatim so a
    reader can see the measurement, not merely the verdict. A validity tool
    that says only "failed" cannot be audited.
    """

    id: str
    title: str
    passed: bool
    value: str
    expected: str
    detail: str = ""
    recipe: str | None = None

    @property
    def glyph(self) -> str:
        # Paired with colour in the rendered output, never colour alone.
        return "PASS" if self.passed else "FAIL"

    def __str__(self) -> str:
        return f"[{self.glyph}] {self.title}: {self.value} (expected {self.expected})"


@dataclass
class Report:
    """A collection of check results plus an explicit record of what was *not* checked.

    The ``not_checked`` list is not decoration. A green report that stays silent
    about its own scope invites the reader to treat it as blanket validation,
    which is precisely the failure mode this framework exists to prevent.
    """

    results: list[CheckResult] = field(default_factory=list)
    not_checked: list[str] = field(default_factory=list)

    def add(self, result: CheckResult) -> None:
        self.results.append(result)

    @property
    def failures(self) -> list[CheckResult]:
        return [r for r in self.results if not r.passed]

    @property
    def passed(self) -> bool:
        return not self.failures

    def __str__(self) -> str:
        lines = [str(r) for r in self.results]
        if self.passed:
            lines.append("")
            lines.append("All checks passed. NOT checked by this run:")
            lines.extend(f"  - {item}" for item in self.not_checked)
        return "\n".join(lines)

    def _repr_html_(self) -> str:
        """Render as an instrument-style panel inside Quarto and Jupyter."""
        rows = []
        for r in self.results:
            state = "pass" if r.passed else "fail"
            mark = "&check;" if r.passed else "&times;"
            recipe = (
                f'<a class="acq-recipe" href="/{r.recipe}">recipe &rarr;</a>'
                if r.recipe and not r.passed
                else ""
            )
            rows.append(
                f'<tr class="acq-{state}">'
                f'<td class="acq-mark">{mark}</td>'
                f"<td>{r.title}</td>"
                f'<td class="acq-val">{r.value}</td>'
                f'<td class="acq-exp">{r.expected}</td>'
                f"<td>{recipe}</td>"
                f"</tr>"
            )
        note = ""
        if self.passed and self.not_checked:
            items = "".join(f"<li>{item}</li>" for item in self.not_checked)
            note = (
                '<div class="acq-scope"><strong>Not checked by this run</strong>'
                f"<ul>{items}</ul></div>"
            )
        return f'<div class="acq-report"><table>{"".join(rows)}</table>{note}</div>'
