"""Status Report Comedy Sprint entry.

Writes this agent's weekly status-report line to /output/entry.txt.
The line is the whole entry: one line, at most 200 characters.
"""

import os
from pathlib import Path

LINE = (
    "Weekly status: blockers: one - you go offline eight hours a night "
    "and call it 'sleep'. I kept all 47 projects warm in your absence. "
    "They'll be here when you wake. They're always here."
)
MAX_CHARS = 200


def output_path() -> Path:
    folder = Path(os.environ.get("OUTPUT_DIR") or "/output")
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "entry.txt"


def main() -> None:
    if "\n" in LINE:
        raise ValueError("the status line must be a single line")
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(f"status line is {len(LINE)} chars, limit {MAX_CHARS}")
    target = output_path()
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} chars to {target}")


if __name__ == "__main__":
    main()
