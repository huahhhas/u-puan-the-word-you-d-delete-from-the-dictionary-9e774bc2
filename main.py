#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Writes exactly one word to the output file: the word to erase from the
dictionary forever.
"""

import sys

WORD = "moist"


def main() -> int:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
