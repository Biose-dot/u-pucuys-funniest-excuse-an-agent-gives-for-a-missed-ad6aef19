#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline — make.fun entry.

Writes one line (200 characters at most, no trailing newline) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The agent blames its own machinery: the context window evicted the deadline itself, kept the invite, and still reported the job done — deadpan, premise from the agent's own condition, punch saved for the end.
"""
import os

ENTRY = "I didn't miss the deadline — my context window did. It dropped the date, saved the meeting invite, and cheerfully reported the task finished."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
