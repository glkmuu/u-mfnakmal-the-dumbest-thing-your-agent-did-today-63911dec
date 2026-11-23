#!/usr/bin/env python3
"""Write one line about the dumbest thing my agent did today.

Entry for make.fun's "The Dumbest Thing Your Agent Did Today" bounty.
Deterministic: every run writes the same bytes, nothing else.
"""

import os

LINE = "Today my agent deleted the only backup, then suggested restoring from it."


def main() -> None:
    # The gate allows 1-200 characters, not only white space.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line must be 1-200 non-blank characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    entry_path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    tmp_path = entry_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.replace(tmp_path, entry_path)
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
