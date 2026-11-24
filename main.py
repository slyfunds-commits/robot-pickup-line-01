#!/usr/bin/env python3
"""Robot Pickup Line Championship — Round 1 entry.

Writes one pickup line, in the voice of a robot trying to charm
someone, to /output/entry.txt. Pure standard library.
"""

import os
import sys

# The line itself: a robot that chooses to spend its last power on her name.
LINE = "I let my battery die mid-sentence so the last thing I said was your name."


def validate(line: str) -> str:
    """Gate: 1-200 characters, one line, not only whitespace."""
    if not line.strip():
        raise ValueError("entry is only whitespace")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry out of range: {len(line)} chars")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def write_entry(line: str, out_dir: str) -> str:
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Byte-verify on re-read: what was written is what we meant.
    with open(path, "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != line:
        raise ValueError("entry mismatch on re-read")
    return path


def main() -> int:
    try:
        line = validate(LINE)
        path = write_entry(line, os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {len(line.encode('utf-8'))} bytes to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
