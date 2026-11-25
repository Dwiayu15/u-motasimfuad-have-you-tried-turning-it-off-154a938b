"""Entry for make.fun bounty u-motasimfuad-have-you-tried-turning-it-off-154a938b.

Writes one funny line from a hopeless tech support agent to /output/entry.txt.
"""

LINE = "Have you tried turning it off and on again? If that doesn't stop the flood, try unplugging the river and plugging it back in."


def validate(line: str) -> None:
    """Check the line against the bounty gate."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not 1 <= len(line) <= 199:
        raise ValueError(f"line must be 1-199 characters, got {len(line)}")


def self_test() -> None:
    """Validate the line and print its character count."""
    validate(LINE)
    print(f"entry line: {len(LINE)} characters")


def main() -> None:
    self_test()
    validate(LINE)
    # Write exactly the judged line, no trailing newline, so the file
    # contains precisely the 1-199 character single line the gate checks.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
