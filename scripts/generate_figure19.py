#!/usr/bin/env python3
"""Generate the source-separated FLOPs-accuracy comparison (Figure 19 replacement)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from common import (
    FAMILY_COLORS,
    SCALE_MARKERS,
    configure_style,
    group_rows,
    load_audited_rows,
    pareto_frontier,
    save_figure,
)


GROUP_A = "Y13_TABLE_I_T4_TRT_FP16"
GROUP_B = "ULTRA_DOCS_2026_08_11_T4_TRT10"


def plot_group(ax: plt.Axes, rows: list[dict[str, str]], allow_frontier: bool) -> None:
    for family in sorted({row["family"] for row in rows}):
        family_rows = sorted(
            [row for row in rows if row["family"] == family],
            key=lambda row: float(row["flops_g"]),
        )
        color = FAMILY_COLORS.get(family, "#333333")
        ax.plot(
            [float(row["flops_g"]) for row in family_rows],
            [float(row["ap50_95"]) for row in family_rows],
            color=color,
            linewidth=0.9,
            alpha=0.7,
        )
        for index, row in enumerate(family_rows):
            params = float(row["params_m"])
            ax.scatter(
                float(row["flops_g"]),
                float(row["ap50_95"]),
                s=30 + 1.4 * params,
                marker=SCALE_MARKERS.get(row["scale"], "o"),
                color=color,
                edgecolor="white",
                linewidth=0.7,
                zorder=3,
                label=family if index == 0 else None,
            )
            if family in {"YOLOv13", "YOLO26"}:
                ax.annotate(
                    row["model"],
                    (float(row["flops_g"]), float(row["ap50_95"])),
                    xytext=(3, 3),
                    textcoords="offset points",
                    fontsize=6.1,
                )
    if allow_frontier:
        frontier = pareto_frontier(rows, "flops_g", "ap50_95")
        if frontier:
            ax.plot(
                [point[0] for point in frontier],
                [point[1] for point in frontier],
                color="#111111",
                linestyle="--",
                linewidth=1.2,
                label="Within-table Pareto frontier",
            )
    ax.set_xscale("log")
    ax.set_xlabel("Source-reported FLOPs (G), logarithmic scale")
    ax.set_ylabel(r"COCO val2017 AP$_{50:95}$ (%)")
    ax.legend(fontsize=6.5, ncol=2, frameon=True)


def main() -> None:
    configure_style()
    rows = load_audited_rows("plot_figure19")
    group_a = group_rows(rows, GROUP_A)
    group_b = group_rows(rows, GROUP_B)

    fig, axes = plt.subplots(1, 2, figsize=(12.2, 5.2), constrained_layout=True)
    plot_group(axes[0], group_a, allow_frontier=True)
    axes[0].set_title("A. YOLOv13 Table I comparison group")
    plot_group(axes[1], group_b, allow_frontier=False)
    axes[1].set_title("B. Ultralytics documentation group (2026-08-11)")
    axes[1].text(
        0.02,
        0.98,
        "Marker area scales with parameter count.\n"
        "YOLO26 AP is the e2e value paired with its fused e2e model.",
        transform=axes[1].transAxes,
        va="top",
        fontsize=6.7,
        bbox={"facecolor": "white", "edgecolor": "#CCCCCC", "alpha": 0.9, "pad": 3},
    )
    fig.suptitle(
        "FLOPs-Accuracy Relations with Evidence Sources Kept Separate",
        fontsize=13,
        fontweight="bold",
    )
    fig.text(
        0.5,
        -0.015,
        "No global efficiency frontier is inferred across protocol groups. "
        "Values retain their original source and access-date metadata.",
        ha="center",
        fontsize=7,
        color="#444444",
    )
    save_figure(fig, "figure19_flops_accuracy_source_separated")
    plt.close(fig)


if __name__ == "__main__":
    main()
