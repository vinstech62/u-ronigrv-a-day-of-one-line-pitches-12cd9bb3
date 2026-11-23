"""One-line pitch for make.fun bounty u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes a single sentence (<=240 characters, UTF-8) to /output/entry.txt:
a plain-words pitch that convinces a friend who has never coded to let
an AI agent build their first app idea on make.fun.

Deterministic: the same fixed sentence on every run.
"""

import os

PITCH = (
    "You've been carrying that app idea around for ages \u2014 tell it to "
    "make.fun in plain words and an AI agent will build you a first version "
    "you can tap today, with no code and nothing to lose."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check the house gate before writing: 1-240 UTF-8 characters,
    # not only whitespace, one sentence.
    text = PITCH.strip()
    assert 1 <= len(text) <= 240, f"pitch is {len(text)} characters"
    assert text, "pitch is only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
