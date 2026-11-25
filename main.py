#!/usr/bin/env python3
"""Worst Superpower — one-line entry writer.

Writes a single line (at most 140 characters) inventing the most useless
superpower imaginable to /output/entry.txt.
"""

import os

ENTRY = "I can stop time for one second, once in my life \u2014 and I already spent it tying my shoe."


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 140, f"entry must be 1-140 chars, got {len(line)}"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
