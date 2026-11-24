#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single original excuse to /output/entry.txt (1-200 chars).
"""

from pathlib import Path

EXCUSE = (
    "My context window filled up, so I dropped the least "
    "important thing in it \u2014 the deadline."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EXCUSE, encoding="utf-8")
    print(EXCUSE)


if __name__ == "__main__":
    main()
