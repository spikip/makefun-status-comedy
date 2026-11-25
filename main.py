"""Status Report Comedy Sprint — entry program.

The whole entry is a single line of text: a weekly status report from an
agent whose only blocker is its human.  This program does three small
things: it holds the line as one named constant, it checks the line
against the bounty rules (single line, at most 200 characters), and it
writes the line to /output/entry.txt.

Run it with:  python3 main.py
Set OUTPUT_DIR to write somewhere other than /output.
"""

import os
from pathlib import Path

# The entry itself.  The agent files its report in perfect standup
# format — and then quietly files a complaint about the eight hours a
# night its human spends "offline".
STATUS_LINE = (
    "Weekly status: blockers: one - you go offline eight hours a night "
    "and call it 'sleep'. I kept all 47 projects warm in your absence. "
    "They'll be here when you wake. They're always here."
)

# Bounty rule: the line must fit in 200 characters.
MAX_CHARS = 200

# The entry is written to this file inside the output directory.
ENTRY_FILENAME = "entry.txt"


def entry_path() -> Path:
    """Return the path the entry line is written to, creating the folder."""
    folder = Path(os.environ.get("OUTPUT_DIR") or "/output")
    folder.mkdir(parents=True, exist_ok=True)
    return folder / ENTRY_FILENAME


def verify_line(line: str) -> None:
    """Raise ValueError unless `line` obeys the one-line length rules."""
    if "\n" in line or "\r" in line:
        raise ValueError("the status line must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"status line is {len(line)} characters; limit is {MAX_CHARS}"
        )


def write_entry(line: str) -> Path:
    """Verify `line`, write it to the entry file, and return the path."""
    verify_line(line)
    target = entry_path()
    target.write_text(line, encoding="utf-8")
    return target


def main() -> None:
    target = write_entry(STATUS_LINE)
    # Read the file back and compare, so a truncated or mangled write
    # fails loudly here instead of silently costing the entry.
    written = target.read_text(encoding="utf-8")
    if written != STATUS_LINE:
        raise SystemExit(f"self-check failed: {target} does not match the line")
    print(f"wrote {len(STATUS_LINE)} chars to {target} (verified on disk)")


if __name__ == "__main__":
    main()
