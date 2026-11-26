#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse -- make.fun bounty entry.

Writes one line (at most 120 characters) to /output/entry.txt: the excuse
a robot vacuum gives for missing a spot while cleaning.
"""

import os

# Winning line, picked from 10 candidates against the judge's criteria
# (excuse on topic, funny at once, vacuum's own voice, vacuum's world,
# lands in one line): a legalistic excuse from a machine that owns its
# failure -- the spot legally barred the brushes, so the vacuum obeys.
LINE = "That spot took out a restraining order against my brushes. I respect boundaries."


def main():
    text = LINE.strip()
    # The gate accepts 1-120 UTF-8 characters; the winning line is 79.
    assert 1 <= len(text) <= 120, "entry must be 1-120 chars, got %d" % len(text)
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote %d chars to /output/entry.txt" % len(text))


if __name__ == "__main__":
    main()
