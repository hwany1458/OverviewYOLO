# Experiment workspace contract

This directory should contain only OverviewYOLO-authored run metadata, summaries, and scripts. Upstream repositories, datasets, and model weights belong outside the repository and are excluded by `.gitignore`.

## Proposed layout after experiments are executed

```text
experiments/
├── manifests/
│   └── <run_id>.yaml
├── raw/
│   └── <run_id>/
│       ├── command.txt
│       ├── environment.txt
│       ├── evaluator.json
│       └── timing.json
├── predictions/
│   └── <run_id>.json
├── summaries/
│   └── benchmark_results.csv
└── scripts/
    ├── evaluate_accuracy.py
    ├── benchmark_latency.py
    ├── run_tide.py
    └── generate_tables_figures.py
```

## Status rule

Do not add an empty directory and describe an experiment as available. A model is `AR` only when its run manifest and raw output are committed or archived at a stable linked location.

## Minimal run workflow

1. Clone and pin the upstream repository outside this repository.
2. Create the isolated environment.
3. Verify dataset and weight checksums.
4. Copy and complete a run-manifest template.
5. Save the exact command before execution.
6. Retain the unedited evaluator output.
7. Normalize the result into the benchmark-results schema.
8. Assign evidence and comparability labels.
9. Generate tables/figures only from normalized records.
10. Run the repository validator.

## Naming

Use stable identifiers:

```text
<evidence>-<model>-<scale>-<dataset>-<split>-<metric/runtime>-<sequence>
```

Examples:

```text
AR-yolov8-n-coco-val2017-ap5095-001
AR-yolo11-n-coco-val2017-t4trt10fp16-latency-001
AR-yolo26-n-coco-val2017-e2e-tide-001
```

## Required separation

- reported values versus executed values;
- native checkpoint versus exported model;
- training graph versus deploy/fused graph;
- accuracy evaluation versus speed benchmark;
- one-to-one versus one-to-many YOLO26 head;
- clean versus corrupted dataset; and
- native model recipe versus a common experimental recipe.
