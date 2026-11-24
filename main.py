#!/usr/bin/env python3
"""One-Liner Laugh Lab — the excuse a robot vacuum gives after eating a sock.

The program writes a single short funny line to /output/entry.txt.
The line is the vacuum's deadpan defence: it was only doing the job
it was literally built for.
"""

import os
import sys

# The entry: one line, at most 200 characters, answering the prompt
# "the excuse a robot vacuum gives after eating a sock".
ENTRY = "I didn't eat the sock \u2014 I was just doing my job. My name is literally VACUUM."


def main() -> int:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
