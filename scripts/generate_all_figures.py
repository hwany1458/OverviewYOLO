#!/usr/bin/env python3
"""Generate release-eligible quantitative figures and optional qualitative snapshot."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIGURE_SCRIPTS = ROOT / "scripts" / "figures"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--include-qualitative-figure20",
        action="store_true",
        help="Generate the guarded, explicitly qualitative Figure 20 snapshot.",
    )
    args = parser.parse_args()
    scripts = ["generate_figure18.py", "generate_figure19.py"]
    for name in scripts:
        subprocess.run([sys.executable, str(FIGURE_SCRIPTS / name)], check=True)
    if args.include_qualitative_figure20:
        subprocess.run(
            [
                sys.executable,
                str(FIGURE_SCRIPTS / "generate_figure20.py"),
                "--allow-unverified-synthesis",
            ],
            check=True,
        )
    print("Figure generation completed.")


if __name__ == "__main__":
    main()
