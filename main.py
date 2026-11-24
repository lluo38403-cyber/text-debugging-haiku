"""Seventeen Syllables of Debugging — make.fun entry.

Writes a 5-7-5 haiku about debugging to /output/entry.txt:

    the stack trace just ends          (5 syllables)
    where the function should return  (7 syllables)
    it returns nothing                (5 syllables)

The concrete image is the stack trace ending where a function should
return; the last line turns the poem by revealing that it returns
nothing at all.
"""

import os

ENTRY = (
    "the stack trace just ends\n"
    "where the function should return\n"
    "it returns nothing"
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    lines = text.split("\n")
    assert len(lines) == 3, f"haiku must have 3 lines, got {len(lines)}"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
