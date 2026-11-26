"""THE WORLD TODAY — a dense broadsheet front page summing up the world's
news of Wednesday, 25 November 2026 (make.fun news-image-20261125).

The entry image is entry.png beside this file; this program copies it to
the output directory (MAKEFUN_OUTPUT_DIR, default /output). Pure stdlib.
"""
import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
