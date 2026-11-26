import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    # Deterministic: byte-identical copy of the entry image, every run.
    os.makedirs(OUT, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(OUT, "entry.png"))


if __name__ == "__main__":
    main()
