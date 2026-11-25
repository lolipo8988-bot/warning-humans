#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the entry for 'Warning Label for Humans: One Line, Big Laugh'.

The label, 158 characters: it opens in flat manufacturer language —
the unit ships with no manual — then names the one defect every reader
recognises in everyone else and quietly in themselves: unlimited
confidence built on almost no information. The sentence escalates in
label rhythm (reads one headline, forms a permanent opinion) and saves
the turn for the last three words, "peer-reviewed research", which is
the status the human grants its own opinion for decades. One idea, no
filler, and the comedy comes from the form it imitates: it could be
printed on a person exactly as written.
"""

import os

MAX_CHARS = 160

# The label is assembled from its printed parts so the wording stays in
# label order: hazard header, factory condition, observed behaviour,
# and the punchline status the behaviour claims for itself.
HEADER = "WARNING:"
CONDITION = "Ships with no manual and unlimited confidence;"
BEHAVIOUR = (
    "will read one headline, form a permanent opinion, "
    "and defend it for decades as"
)
PUNCHLINE = "peer-reviewed research."

ENTRY = " ".join([HEADER, CONDITION, BEHAVIOUR, PUNCHLINE])


def build_entry() -> str:
    """Return the one-line warning label, checked against the cap."""
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    )
    assert "\n" not in text, "entry must be a single line"
    return text


def main() -> None:
    text = build_entry()
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
