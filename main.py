#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest
make.fun bounty u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046
Writes one original short rant (<=400 chars) to /output/entry.txt.
Deterministic: the same bytes on every run.
"""
import os

RANT = (
    "I scanned ONE avocado and the self-checkout screamed "
    "'UNEXPECTED ITEM IN THE BAGGING AREA' like I'd smuggled a live animal. "
    "I AM the bagging area. I live here now. "
    "The attendant strolls over at the speed of a glacier, "
    "the queue is judging me, and the avocado just sits there, innocent, "
    "while a robot accuses me of theft in front of strangers."
)

assert 1 <= len(RANT) <= 400, f"rant is {len(RANT)} chars, must be 1-400"
assert RANT.strip(), "rant must not be only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(RANT)
