# Manuscript corrections required for repository alignment

## Why this file exists

The repository now supports an audited subset of Table 4 and replacement Figures 18–19. The submitted manuscript contains additional values that do not yet have the same provenance chain. This file prevents the public repository from being used to overstate what has been validated.

## Table 4

Do not retain a caption asserting that nearly all listed variants were measured on T4/TensorRT FP16 unless every row is mapped to a source that actually used that protocol. The submitted snapshot is preserved in `data/manuscript_snapshot/table4_submitted_snapshot.csv`; it contains unaudited rows and must not be treated as source data.

Use `tables/generated/table4_audited.md` as the defensible replacement subset. If additional families are retained, add each numerical field to `data/audited/table4_accuracy_speed_size.csv` with its primary source location and protocol group before regenerating the claim map and table.

## Figure 18 replacement caption

> **Figure 18. Source-separated accuracy–latency relations for selected YOLO families.** Panel A reproduces the comparison group reported in Table I of the YOLOv13 primary paper, which evaluates the listed models on MS COCO val2017 at 640 × 640 using a Tesla T4 GPU and TensorRT FP16. Panel B reports current Ultralytics YOLO11 and YOLO26 documentation values (accessed 11 August 2026) as a separate evidence group. For YOLO26, end-to-end AP is paired with the default end-to-end latency. The dashed Pareto frontier is computed only within Panel A; no cross-panel dominance claim is made.

Remove the current statement that a single frontier demonstrates a 15–20% efficiency improvement unless that percentage is derived by a released method and recorded in the claim map.

## Figure 19 replacement caption

> **Figure 19. Source-separated FLOPs–accuracy relations for the audited comparison records.** Marker area represents parameter count. Panel A uses the YOLOv13 Table I comparison group, whereas Panel B uses current Ultralytics documentation values accessed on 11 August 2026. Source groups are kept separate because their evidence provenance and head semantics differ. No global efficiency frontier is inferred across groups.

Remove the YOLO-NAS highlighted region and any percentage reduction claim until each YOLO-NAS value has an official source locator and the baseline comparison receives a `C`, `P`, or `NC` decision.

## Figure 20

The original percentage-retention radar cannot be supported by the current repository because there are no released corruption images, prediction files, evaluator output, or common protocol. Either remove it or replace it with the guarded qualitative heatmap using this caption:

> **Figure 20. Qualitative synthesis of reported robustness tendencies across selected YOLO families.** Cells show ordinal categories retained from the literature-synthesis snapshot and do not represent percentages or results from a common corruption benchmark. Because the underlying studies use heterogeneous protocols, the figure is interpretive and is not used for paired performance ranking.

Even this qualitative replacement should be removed if individual cells cannot be mapped to specific studies before resubmission.

## Tables 5–10

The current status matrix is in `data/audit/manuscript_artifact_status.csv`. In brief:

- Table 5 is qualitative but lacks cell-level source mapping.
- Table 6 contains a non-standard `APCrowd` metric without released evaluation code.
- Table 7 lacks paired INT8 calibration/run manifests.
- Table 8 uses approximate heterogeneous values.
- Table 9 is not a valid single-codebase cumulative ablation.
- Table 10 lacks prediction files, denominators, and TIDE outputs.

The presence of repository placeholders or snapshots does not make these tables publishable.

## Repository-aligned Data Availability Statement

> This review did not generate a new experimental dataset. The versioned companion repository provides the curated source registry, an audited subset of the source-reported comparison data with cell-level provenance, deterministic table and figure-generation scripts for the revised quantitative Figures 18 and 19, generated PNG/PDF artifacts, and prospective benchmark schemas. Numerical records retain their original dataset, evaluation, hardware, runtime, evidence, and comparability metadata. The repository does not redistribute third-party datasets, model weights, or upstream implementations. Author-reproduced benchmarks, controlled robustness results, quantization experiments, and TIDE error-analysis outputs are identified as unavailable unless accompanied by run manifests and raw outputs.

Use this statement only after creating a public, versioned release containing the same files used for the submitted revision.
