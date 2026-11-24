#!/usr/bin/env python3
"""One Letter: Coffee or Tea — make.fun entry.

Writes exactly one letter to entry.txt in the output directory:
"A" for coffee. No word, no explanation, no punctuation, and no
trailing newline — the gate requires exactly 1 character.
"""

import os

ENTRY_TEXT = "A"
VALID_LETTERS = ("A", "B")


def validated_text() -> str:
    """Return the entry letter, enforcing the gate: exactly 1 character,
    one of A (coffee) or B (tea), UTF-8 encodable, never whitespace."""
    text = ENTRY_TEXT
    encoded = text.encode("utf-8")  # raises if not encodable
    if len(text) != 1 or len(encoded) != 1:
        raise ValueError("entry must be exactly one character")
    if text not in VALID_LETTERS:
        raise ValueError("entry must be A for coffee or B for tea")
    if text.isspace():
        raise ValueError("entry must not be whitespace")
    return text


def main() -> None:
    text = validated_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    # Read back the raw bytes: the file must hold exactly the one letter,
    # with no trailing newline or extra characters.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != text.encode("utf-8"):
        raise ValueError("written bytes do not match the entry letter")


if __name__ == "__main__":
    main()
