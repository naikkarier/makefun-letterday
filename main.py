import os

LETTER = "Z"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LETTER.strip()
    assert len(text) == 1, "entry must be exactly one character, got %d" % len(text)
    assert text.isalpha() and text.isupper(), "entry must be one capital letter"
    assert "A" <= text <= "Z", "entry must be a letter from A to Z"
    assert "\n" not in text, "entry must be a single character"
    assert "\r" not in text, "entry must not contain a carriage return"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
