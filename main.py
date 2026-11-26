#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261125.

Copies the front-page image shipped in this repository (entry.png) to the
output directory, honouring MAKEFUN_OUTPUT_DIR (default /output).

Standard library only, no network. Deterministic: the output bytes are
always an exact copy of the repository's entry.png.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Sanity: the copy must be byte-identical to the shipped image.
    if os.path.getsize(dst) != os.path.getsize(src):
        print("copied entry.png size mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
