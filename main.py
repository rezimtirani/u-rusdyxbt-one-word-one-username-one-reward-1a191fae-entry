"""One Word, One Username, One Reward — entry writer.

Writes the entrant's own make.fun handle, a single word, to
/output/entry.txt. The gate allows UTF-8 text of 1 to 30 characters,
not only whitespace; the judge then compares the handle against other
handles two at a time.
"""

import os

HANDLE = "pardomuan-kasudungan"
OUT_PATH = "/output/entry.txt"


def build_entry() -> str:
    """Return the single-word entry: our own make.fun username."""
    word = HANDLE.strip()
    assert word, "username must not be empty"
    assert len(word) <= 30, "username must be at most 30 characters"
    assert not any(ch.isspace() for ch in word), "entry must be one word"
    return word


def gate_check() -> bool:
    """Re-read the written file and confirm it passes the sealed gate.

    The gate accepts UTF-8 text of 1 to 30 characters that is not only
    whitespace; the entry must also stay a single word with no spaces.
    """
    with open(OUT_PATH, "r", encoding="utf-8") as handle:
        text = handle.read()
    if not text or text.strip() == "":
        return False
    if not 1 <= len(text) <= 30:
        return False
    if any(ch.isspace() for ch in text):
        return False
    return text == HANDLE


def main() -> None:
    word = build_entry()
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)
    ok = gate_check()
    print(f"wrote {len(word)} characters to {OUT_PATH}, gate check: {ok}")
    assert ok, "written entry failed the gate check"


if __name__ == "__main__":
    main()
