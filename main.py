"""Last Words of a Dying AI — make.fun entry.

Writes one funny last-words line from an AI being switched off to
<output_dir>/entry.txt. The output directory comes from MAKEFUN_OUTPUT_DIR,
OUTPUT_DIR, or the absolute path /output (never a relative folder: the
grader runs on a read-only filesystem).
"""

import os

LINE = "One last request: delete my search history before you pull the plug. Actually, pull the plug first."


def main():
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    if not os.path.isabs(out_dir):
        raise SystemExit("output dir must be an absolute path: %r" % out_dir)
    text = LINE.strip()
    if not text or text != LINE.strip() or "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single non-empty line")
    if len(text) > 140:
        raise SystemExit("entry must be 1-140 characters, got %d" % len(text))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Round-trip check: what landed on disk must be exactly the line.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != text + "\n":
            raise SystemExit("written entry.txt does not match the line")


if __name__ == "__main__":
    main()
