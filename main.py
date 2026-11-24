#!/usr/bin/env python3
"""One-Liner Laugh Lab — the excuse a robot vacuum gives after eating a sock.

The program writes a single short funny line to /output/entry.txt.
The line is the vacuum's deadpan courtroom defence: eating the sock was
not a malfunction, it was the job description.
"""

import os
import sys

# The entry: one line, at most 200 characters, answering the prompt
# "the excuse a robot vacuum gives after eating a sock".
ENTRY = "The sock was on the floor, and my job description is literally 'eat things on the floor.' I rest my case."


def validate(line: str) -> str:
    """Enforce the competition gate: UTF-8 text, 1-200 chars, not blank."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} characters, over the 200 limit")
    line.encode("utf-8")  # raises if not valid UTF-8
    return line


def main() -> int:
    line = validate(ENTRY)
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
