#!/usr/bin/env python3
"""One Star for Monday — a one-star review of Monday as a restaurant.

The program writes a single original line of plain text to
/output/entry.txt: a diner's complaint about Monday, treated as a
restaurant. The line is a fixed string held in this file; the program
validates it against the competition gate (1-180 characters, at most
25 words, one line, not only whitespace) before writing it out.
"""

import os
import sys

# The review: a diner who was seated at Friday's sticky table, fed the
# weekend as leftovers, and billed before ordering. Table, dish and bill
# all go wrong, and the joke only works for Monday.
REVIEW = (
    "One star. Monday seated me at Friday's sticky table, "
    "served the weekend as leftovers, "
    "and billed me before I'd even ordered."
)


def main() -> int:
    line = REVIEW.strip()
    words = line.split()
    if not line or len(line) > 180:
        print("review fails the 1-180 character gate", file=sys.stderr)
        return 1
    if len(words) > 25:
        print("review exceeds 25 words", file=sys.stderr)
        return 1
    if "\n" in line:
        print("review must be a single line", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(line)
    # Read back what was written and confirm it is byte-identical to the
    # validated line, so a silent write failure can never pass as success.
    with open(out_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != line:
        print("written entry does not match the review", file=sys.stderr)
        return 1
    print(
        "wrote %d characters, %d words to %s" % (len(line), len(words), out_path)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
