"""Entrypoint: render The World Today front page for 24 November 2026.

Grader runs: python3 -P -s /bot/main.py
-P -s means the script directory is NOT on sys.path, so insert it first.
Writes /output/entry.png and, when run locally, entry.png beside main.py.
Deterministic: no timestamps, no randomness, fixed layout and fonts.
"""
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from draw import render


def main():
    img = render(BASE_DIR)
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        img.save(os.path.join(out_dir, "entry.png"), format="PNG")
    except OSError:
        pass
    # Local copy next to main.py (grader run: /bot is read-only, so skip on failure)
    try:
        img.save(os.path.join(BASE_DIR, "entry.png"), format="PNG")
    except OSError:
        pass


if __name__ == "__main__":
    main()
