#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — self-checkout avocado rant.

Deterministic: fixed string literal, no randomness, time, or network.
Writes the 342-character rant to /output/entry.txt with no trailing newline.
"""

import os

PART_A = "I scanned ONE avocado and the self-checkout screamed 'UNEXPECTED ITEM IN THE BAGGING AREA' like I'd smuggled a live animal. I AM the bagging area. I live here now. "
PART_B = "The attendant strolls over at the speed of a glacier, the queue is judging me, and the avocado just sits there, innocent, while a robot accuses me of theft in front of strangers."


def main():
    entry = PART_A + PART_B
    assert 1 <= len(entry) <= 400, "entry must be 1-400 chars"
    assert entry.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(entry)


if __name__ == "__main__":
    main()
