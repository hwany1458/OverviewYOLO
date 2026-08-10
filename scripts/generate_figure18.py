#!/usr/bin/env python3
"""Generate the source-separated accuracy-latency comparison (Figure 18 replacement)."""

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


def plot_family(
    ax: plt.Axes,
    family_rows: list[dict[str, str]],
    connect: bool,
    annotate: bool,
) -> None:
    family = family_rows[0]["family"]
    color = FAMILY_COLORS.get(family, "#333333")
    ordered = sorted(family_rows, key=lambda row: float(row["latency_ms"]))
    if connect:
        ax.plot(
            [float(row["latency_ms"]) for row in ordered],
            [float(row["ap50_95"]) for row in ordered],
            color=color,
            linewidth=1.0,
            alpha=0.75,
            zorder=1,
        )
    for row in ordered:
        x_value = float(row["latency_ms"])
        y_value = float(row["ap50_95"])
        ax.scatter(
            x_value,
            y_value,
            s=48,
            marker=SCALE_MARKERS.get(row["scale"], "o"),
            color=color,
            edgecolor="white",
            linewidth=0.7,
            zorder=3,
            label=family if row is ordered[0] else None,
        )
        if annotate:
            ax.annotate(
                row["model"],
                (x_value, y_value),
                xytext=(3, 3),
                textcoords="offset points",
                fontsize=6.2,
                color="#222222",
            )


def main() -> None:
    configure_style()
    rows = load_audited_rows("plot_figure18")
    group_a = group_rows(rows, GROUP_A)
    group_b = group_rows(rows, GROUP_B)

    fig, axes = plt.subplots(1, 2, figsize=(12.2, 5.2), constrained_layout=True)

    for family in sorted({row["family"] for row in group_a}):
        plot_family(
            axes[0],
            [row for row in group_a if row["family"] == family],
            connect=True,
            annotate=family == "YOLOv13",
        )
    frontier = pareto_frontier(group_a, "latency_ms", "ap50_95")
    if frontier:
        axes[0].plot(
            [point[0] for point in frontier],
            [point[1] for point in frontier],
            color="#111111",
            linestyle="--",
            linewidth=1.2,
            label="Within-table Pareto frontier",
            zorder=2,
        )
    axes[0].set_title("A. YOLOv13 Table I comparison group\nT4, TensorRT FP16, 640 px")
    axes[0].set_xlabel("Source-reported latency (ms)")
    axes[0].set_ylabel(r"COCO val2017 AP$_{50:95}$ (%)")
    axes[0].legend(fontsize=6.5, ncol=2, frameon=True)

    for family in sorted({row["family"] for row in group_b}):
        plot_family(
            axes[1],
            [row for row in group_b if row["family"] == family],
            connect=True,
            annotate=True,
        )
    axes[1].set_title("B. Ultralytics documentation group\nT4 TensorRT10, accessed 2026-08-11")
    axes[1].set_xlabel("Source-reported latency (ms)")
    axes[1].set_ylabel(r"COCO val2017 AP$_{50:95}$ (%)")
    axes[1].legend(fontsize=7, frameon=True)
    axes[1].text(
        0.02,
        0.98,
        "YOLO26 uses e2e AP to match the default e2e latency.\n"
        "YOLO11 is NMS-based; cross-family comparability is partial (P).",
        transform=axes[1].transAxes,
        va="top",
        fontsize=6.7,
        color="#444444",
        bbox={"facecolor": "white", "edgecolor": "#CCCCCC", "alpha": 0.9, "pad": 3},
    )

    fig.suptitle(
        "Accuracy-Latency Trade-offs with Protocol Groups Kept Separate",
        fontsize=13,
        fontweight="bold",
    )
    fig.text(
        0.5,
        -0.015,
        "Source-reported/independently reproduced values; not an author-run, globally normalized benchmark. "
        "Sources: YOLOv13 Table I and Ultralytics model documentation.",
        ha="center",
        fontsize=7,
        color="#444444",
    )
    save_figure(fig, "figure18_accuracy_latency_source_separated")
    plt.close(fig)


if __name__ == "__main__":
    main()
