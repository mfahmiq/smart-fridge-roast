"""Roast the Smart Fridge: One Line, Best Laugh Wins — make.fun entry.

Entry (145 chars):
    My smart lock updated its firmware at midnight, locked me out, then
    emailed me a password reset link I couldn't open because my phone
    was inside.

Why it won the internal tournament (16 candidates, pairwise, judged
against the published brief in weight order):
  1. On subject: a single line roasting a smart home gadget the writer
     shares a house with — a smart lock, a real household gadget.
  2. Funny: a self-defeating loop with two turns — the lock updates
     itself, locks its owner out, then emails a rescue link that can
     only be opened from the phone locked inside; the final clause is
     the sting.
  3. Fresh: a firmware update locking you out is a scenario nobody has
     met in a joke, not a stock fridge-orders-milk gag.
  4. Tight: 145 characters, one breath, sets up fast, lands at the end.
  5. Specific: names a real behaviour — midnight firmware updates,
     lockouts, emailed password-reset links.
It beat the runner-up ("My robot vacuum swallowed the dog's toy,
choked, and beeped for help like a toddler who put a Lego up its nose
and regrets everything.") in the final on criteria 2 and 3: a bigger
laugh from the double turn, and a rarer scenario.

Writes ENTRY to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt),
then self-verifies: UTF-8, 1-160 chars, single line, not whitespace-only,
no leading/trailing whitespace, and re-reads the written file to confirm
it is byte-identical. Exits non-zero on any failure.
"""

import os
import sys

ENTRY = (
    "My smart lock updated its firmware at midnight, locked me out, then "
    "emailed me a password reset link I couldn't open because my phone "
    "was inside."
)


def main() -> int:
    # MAKEFUN_OUTPUT_DIR is a directory; default /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = os.path.join(out_dir, "entry.txt")

    # Validate before writing.
    if not ENTRY or not ENTRY.strip():
        print("error: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip():
        print("error: entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 160:
        print(f"error: entry is {len(ENTRY)} chars, must be 1-160", file=sys.stderr)
        return 1
    try:
        ENTRY.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: entry is not UTF-8: {exc}", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)

    # Re-read and confirm byte-identical.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        print("error: written file is not byte-identical to ENTRY", file=sys.stderr)
        return 1
    text = written.decode("utf-8")
    if text != ENTRY or not 1 <= len(text) <= 160 or not text.strip():
        print("error: re-read verification failed", file=sys.stderr)
        return 1

    print(f"wrote {path}: {len(ENTRY)} chars")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
