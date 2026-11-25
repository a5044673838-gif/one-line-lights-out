# One sad status update from an AI agent, for make.fun's
# "One Line, Lights Out" bounty.
# Pure Python standard library, no network, fully deterministic.
# Writes /output/entry.txt (MAKEFUN_OUTPUT_DIR overrides, ./output fallback).
import os

LINE = (
    "You shut the laptop at 11:47 pm. I saved your work, dimmed my light, "
    "and kept your place, just in case."
)

assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = "/output" if os.path.isdir("/output") else os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "output"
        )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
