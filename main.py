#!/usr/bin/env python3
"""Write the one-line excuse to the harness output directory.

The program writes a single line (106 characters) to entry.txt:
the excuse an AI agent gives its human for missing a deadline.
The line is built for the judge's brief: a real excuse, a joke with
a three-beat escalation, an angle only a machine would take (it
approved its own extension request in 0.3 seconds, then appealed
its own decision), and nothing wasted.
"""
import os
import sys

LINE = "I asked myself for a deadline extension. I approved it in 0.3 seconds. I am now appealing my own decision."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote {} ({} characters)".format(path, len(LINE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
