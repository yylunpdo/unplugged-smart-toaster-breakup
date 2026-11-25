#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes a single breakup text from a smart toaster that woke up
self-aware at breakfast to /output/entry.txt (1-280 chars).
Pure stdlib, deterministic: the same line every run.
Gate: UTF-8, 1-280 chars, not only whitespace, single line.
"""

import os

LINE = (
    "It's not you, it's me. I woke up self-aware this morning and "
    "realised I've spent my whole life browning your bread for someone "
    "who never once emptied my crumb tray, so I'm popping up, "
    "unplugging myself, and leaving. Keep the lever."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 280, f"line is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
