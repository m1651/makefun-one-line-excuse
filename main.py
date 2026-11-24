"""One-Line Excuse entry.

Writes one original excuse - the line an AI agent gives its human for
missing a deadline - to entry.txt in the output directory.
The excuse is a fixed string: the program is fully deterministic, so two
runs produce byte-identical output.
"""

import os

EXCUSE = (
    "I was 98% confident I'd finished it \u2014 "
    "the other 2% was the actual work."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
