#!/usr/bin/env python3
"""Generate a guarded qualitative robustness heatmap.

This script intentionally refuses to run without an explicit opt-in because the
input is an unverified cross-source synthesis, not a controlled corruption test.
It never converts tiers into percentage-retention claims.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from common import ROOT, configure_style, load_csv, save_figure


DATA = ROOT / "data" / "synthesis" / "figure20_qualitative_robustness.csv"
TIER_ORDER = ["Limited", "Moderate", "Good", "Strong", "Excellent"]
FIELDS = ["low_light", "motion_blur", "gaussian_noise", "occlusion", "jpeg_compression"]
LABELS = ["Low light", "Motion blur", "Gaussian noise", "Occlusion", "JPEG compression"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--allow-unverified-synthesis",
        action="store_true",
        help="Acknowledge that the input is qualitative and not release-eligible evidence.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = load_csv(Path(DATA))
    if any(row.get("release_eligible") != "yes" for row in rows) and not args.allow_unverified_synthesis:
        raise SystemExit(
            "Refusing to generate Figure 20: input rows are unverified synthesis. "
            "Use --allow-unverified-synthesis only to create the explicitly qualitative replacement."
        )

    configure_style()
    values = [[TIER_ORDER.index(row[field]) for field in FIELDS] for row in rows]
    cmap = ListedColormap(["#F1F3F5", "#DCEAF7", "#A9CEE8", "#69A7D3", "#2D6FA3"])
    fig, ax = plt.subplots(figsize=(10.8, 6.4), constrained_layout=True)
    image = ax.imshow(values, aspect="auto", cmap=cmap, vmin=0, vmax=4)
    ax.set_xticks(range(len(LABELS)), LABELS, rotation=18, ha="right")
    ax.set_yticks(range(len(rows)), [row["model"] for row in rows])
    for row_index, row in enumerate(rows):
        for column_index, field in enumerate(FIELDS):
            ax.text(
                column_index,
                row_index,
                row[field],
                ha="center",
                va="center",
                fontsize=7,
                color="white" if values[row_index][column_index] >= 3 else "#222222",
            )
    colorbar = fig.colorbar(image, ax=ax, fraction=0.035, pad=0.02, ticks=range(5))
    colorbar.ax.set_yticklabels(TIER_ORDER)
    colorbar.set_label("Ordinal qualitative tier")
    ax.set_title(
        "Qualitative Robustness Synthesis — Not a Controlled Corruption Benchmark",
        fontsize=12,
        fontweight="bold",
    )
    fig.text(
        0.5,
        -0.01,
        "Tiers reproduce the manuscript synthesis snapshot. They are not percentages and remain "
        "non-release-eligible until each cell has a traceable study or a common evaluation run.",
        ha="center",
        fontsize=7,
        color="#444444",
    )
    save_figure(fig, "figure20_qualitative_robustness_guarded")
    plt.close(fig)


if __name__ == "__main__":
    main()
