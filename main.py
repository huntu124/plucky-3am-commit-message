"""One-line entry for The 3 AM Commit Message: writes the line the judge reads to /output/entry.txt."""

import os

LINE = (
    "fix: stop the button from running away from the cursor (it was shy) (it is not fixed) (we ship at 9)"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
