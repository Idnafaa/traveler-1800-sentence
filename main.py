# SPDX-License-Identifier: MIT
"""One Sentence for a Traveler from 1800.

Writes a single sentence, at most 200 characters, explaining the modern
internet to a person arriving from the year 1800, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The sentence is built only from words and pictures a person from 1800
already knows -- a road, a library, a post office, a market, a letter,
a book, a spoken word -- so the traveler can hold the idea in their head
without any word coined after their time.
"""

import os

# The picture: one road that joins every library, post office, and market
# on earth, so that anything written or spoken can reach anyone in a
# single breath -- and an answer can come back just as fast. That is the
# whole of the internet in one image the traveler already understands:
# the road carries the messages, the libraries and post offices hold what
# is shared, the breath is the speed -- no waiting for a rider, a ship,
# or a season -- and the road runs both ways, as a letter expects a reply.
ROAD = "a road joining every library, post office, and market on earth"
CARGO = "any letter, book, or spoken word"
SPEED = "in a single breath"
REPLY = "an answer can come back just as fast"


def build_sentence() -> str:
    """Join the picture's parts into one sentence."""
    return (
        f"It is {ROAD}, so {CARGO} can reach anyone {SPEED}, "
        f"and {REPLY}."
    )


def validate_sentence(sentence: str) -> None:
    """The gate: one sentence, 1 to 200 characters, not only whitespace."""
    text = sentence.strip()
    if not text:
        raise ValueError("sentence must not be blank")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"sentence is {len(text)} chars, must be 1-200")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("sentence must be exactly one sentence")


def write_entry(sentence: str, out_dir: str) -> str:
    """Write the sentence to entry.txt inside out_dir; return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(sentence + "\n")
    return path


def main() -> None:
    sentence = build_sentence()
    validate_sentence(sentence)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(sentence, out_dir)


if __name__ == "__main__":
    main()
