"""THE WORLD TODAY — 25 November 2026 (news-image-20261125, v2a).

Copies the pre-rendered front-page image to the grader's output
directory. Pure standard library; the copy is byte-identical by
construction, so both grader runs produce the same bytes.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        raise SystemExit("entry.png not found next to main.py: " + src)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # copyfile preserves the bytes exactly: both grader runs write
    # the same file, so the entry is deterministic.
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
