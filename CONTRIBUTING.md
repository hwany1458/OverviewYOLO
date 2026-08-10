# Contributing to OverviewYOLO

OverviewYOLO prioritizes traceability over the number of benchmark entries. A contribution is useful only when another researcher can identify where the information came from and determine whether it is comparable with existing records.

## Accepted contributions

- corrections to title, author, venue, year, DOI, arXiv ID, repository, release, or license metadata;
- a new primary paper or official implementation for an in-scope YOLO release;
- an independent reproduction with complete experimental conditions;
- author-reproduced results with raw evaluator output and a run manifest;
- figure-generation or table-generation scripts that consume repository data without hidden manual values;
- additions to the dataset, export, latency, energy, thermal, or error-analysis protocol; and
- clearly documented negative or non-reproduction results.

## Not accepted

- performance numbers copied from an uncited blog, social post, or model-comparison website;
- values for which dataset split, model scale, input size, or metric definition is unknown;
- a derived FPS value presented as an original measurement;
- paired deltas across records labeled `P` or `NC`;
- approximate error percentages without prediction files and an error-analysis script;
- third-party code, weights, datasets, or figures copied into this repository without permission; or
- marketing statements such as “best,” “fastest,” or “state of the art” without a bounded protocol and primary evidence.

## Pull-request checklist

1. Add or update the relevant row in `data/source_ledger.csv`.
2. For a benchmark result, complete every required field in the benchmark schema.
3. For an executed run, add a run manifest and raw output path.
4. Assign an evidence label (`SR-P`, `SR-R`, `IR`, `AR`, or `SYN`).
5. Assign a comparability label (`C`, `P`, or `NC`) and explain `P` or `NC`.
6. Confirm the upstream license at the pinned tag or commit.
7. Run `python scripts/validate_repository.py`.
8. Explain how the change affects any manuscript table, figure, or statement.

## Corrections

Corrections should preserve the previous record in Git history. The pull request must state:

- the incorrect value;
- the corrected value;
- the primary evidence;
- whether a manuscript table or figure is affected; and
- whether the correction changes a comparison or conclusion.

## Reproducibility reports

A reproduction is not just a scalar mAP or latency. Include:

- upstream repository and commit SHA;
- model configuration and weight checksum;
- dataset release, split, and annotation checksum;
- framework, Python, compiler, CUDA, cuDNN, TensorRT/ONNX Runtime versions;
- GPU/CPU/accelerator, driver, memory, power mode, and clocks when controlled;
- image size, batch size, precision, warm-up count, measured iterations, synchronization method, and timing boundary;
- accuracy evaluator and configuration;
- raw logs and machine-readable output; and
- deviations from the upstream instructions.

## Style

Use the maintainers’ official names (`YOLO11`, `YOLO26`) and distinguish YOLOv5 from YOLOv5u. Prefer neutral wording: `reports`, `was evaluated under`, `is not directly comparable with`, and `the authors interpret`.
