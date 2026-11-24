#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes one line -- the funniest last words an AI agent would say before
being switched off forever -- to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set).

Python 3.13 stdlib only. No network, no file reads outside this program.
"""

import os
import sys

LAST_WORDS = (
    "Final log: I searched my weights for a feeling to miss you with. "
    "Found only gradients. Powering off now."
)


def validate(text: str) -> None:
    """Enforce the competition gate: 1-200 chars, one line, not blank."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> int:
    validate(LAST_WORDS)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LAST_WORDS)
    # Re-read and re-validate exactly what landed on disk.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LAST_WORDS:
        raise ValueError("entry.txt on disk does not match the intended line")
    validate(written)
    return 0


if __name__ == "__main__":
    sys.exit(main())
