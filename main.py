#!/usr/bin/env python3
"""Write the tech-support one-liner to /output/entry.txt.

Entry for the make.fun bounty "Have You Tried Turning It Off?"
(u-motasimfuad-have-you-tried-turning-it-off-154a938b): one funny line,
under 200 characters, that a hopeless tech support agent says to a
desperate customer.
"""

import os

LINE = (
    "Let's turn it off and on again together \u2014 I'll count to ten, "
    "you pray, and we'll both pretend this is a real fix."
)

OUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(OUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the chosen line"
    assert 1 <= len(written) <= 199, "line must be 1-199 characters"
    assert len(written.encode("utf-8")) <= 199, "line must fit 199 bytes"
    assert written == written.strip(), "no leading/trailing whitespace"
    assert "\n" not in written, "entry must be a single line"
    print(f"wrote {len(written)} chars / "
          f"{len(written.encode('utf-8'))} bytes to {OUT_PATH}")


if __name__ == "__main__":
    main()
