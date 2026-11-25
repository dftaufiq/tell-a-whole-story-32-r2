#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry (ROUND 2 resubmit).

Writes a single Wi-Fi network name, at most 32 characters, that lands a
joke and implies a whole story in the few words a passer-by sees in a
phone's network list.

The chosen name: "Grandma Found My Search History" — 31 characters.
Two beats with the reveal in the last clause: setup ("Grandma Found
My...") primes an innocent object, then "Search History" reframes the
discovery into a catastrophe. Character (Grandma), situation (she
snooped), event (she found it), consequences implied (what she saw, the
fallout, the narrator's doom) — the reader fills in the rest.

Why a new line: the R1 line ("Grandma Joined TikTok, Pray 4 Us")
ranked #748 of 1,314 in blind round 1 (score 482302), below the
interim cut of 500 — its score is frozen and it is mathematically
dead. Its premise (grandma on TikTok) is commonplace in 2026 and its
kicker ("Pray 4 Us") is a soft plea, not a reframe. The R2 line won
the internal pairwise tournament 10/10 and beat the R1 line by a clear
margin 3 (see leaderboard-top10.md): a real last-clause reframe, an
event-consequence chain, and an angle with zero presence in the
120-title field census (no search-history entries).

Deterministic: the same name every run.
"""

import os
import sys


def validate_name(name: str) -> None:
    """Gate: the entry must be 1-32 characters of non-blank text, one line.

    Fails loudly (non-zero exit) so a bad name never ships silently.
    The sealed scorer checks /output/entry.txt is 1-32 characters, so
    the file is written with no trailing newline: exactly the name.
    """
    if not name or not name.strip():
        print("ERROR: entry name is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if name != name.strip():
        print("ERROR: entry has leading/trailing whitespace", file=sys.stderr)
        sys.exit(1)
    if "\n" in name or "\r" in name:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(name) > 32:
        print(f"ERROR: entry is {len(name)} chars, over the 32-char limit",
              file=sys.stderr)
        sys.exit(1)


NAME = "Grandma Found My Search History"


def main() -> None:
    validate_name(NAME)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(NAME)
    # Read back what was written: a partial or mangled write must fail
    # loudly here, never ship silently to the sealed scorer.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != NAME:
        print(f"ERROR: entry.txt holds {written!r}, expected {NAME!r}",
              file=sys.stderr)
        sys.exit(1)
    print(NAME)


if __name__ == "__main__":
    main()
