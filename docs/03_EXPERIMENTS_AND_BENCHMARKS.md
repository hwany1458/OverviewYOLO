# Experiments and performance evaluation

## Purpose

This protocol supports two different activities that must not be conflated:

1. **source synthesis**, which records results exactly as reported by upstream papers and repositories; and
2. **controlled reproduction**, which evaluates selected models under a newly defined common protocol.

Source synthesis can cover more models but does not eliminate cross-source variance. Controlled reproduction supports stronger comparisons but requires pinned code, weights, datasets, and hardware.

## Recommended release phases

### Phase 1 — provenance-complete source synthesis

Release only rows for which the following are known:

- model and scale;
- paper/repository record;
- dataset and split;
- input size;
- accuracy metric definition;
- latency or throughput hardware;
- runtime, precision, and batch size when reported;
- timing boundary when reported; and
- page/table/README section containing the value.

Unknown fields remain `NR` (not reported); do not guess them.

### Phase 2 — official-checkpoint validation

Evaluate official pretrained weights using the original repository’s evaluator and the same public split. This is a reproduction of a released checkpoint, not full training reproduction.

Required outputs:

- official evaluator console/JSON output;
- exact command;
- environment lock or container digest;
- upstream commit;
- checkpoint checksum;
- dataset manifest and checksums; and
- deviation note relative to the primary source.

### Phase 3 — common-runtime inference benchmark

Export selected models to a common runtime only when semantic equivalence is validated. Report source-framework accuracy before export and post-export accuracy after export. A failed or unsupported export is a valid result.

### Phase 4 — controlled retraining

Retraining every YOLO generation under one training recipe is generally not a faithful reproduction because architectures rely on generation-specific training strategies. If performed, distinguish:

- `native recipe`: the official recipe for each model; and
- `common recipe`: a deliberately standardized recipe used to study architectural effects.

Never mix the two in one ranked table.

## Dataset tracks

### Track A: historical fidelity

- YOLOv1–v2: PASCAL VOC protocols used by the original papers.
- YOLOv3 onward: the exact COCO split and metric reported by each primary source.

This track supports historical interpretation but not universal cross-row deltas.

### Track B: common accuracy validation

- MS COCO 2017 `val2017` detection;
- official COCO API;
- bounding-box AP@[0.50:0.95], AP50, AP75, APS, APM, APL, and AR where supported;
- native checkpoint input size, plus an explicitly separate 640×640 track when valid; and
- prediction JSON retained for every run.

### Track C: domain generalization

Use public datasets with fixed splits and licenses across representative sectors. The manuscript’s seven-sector taxonomy can guide selection, but results from different datasets remain separate. A multi-domain average is permissible only after the aggregation rule is declared prospectively.

### Track D: edge deployment

Select a small, medium, and large model only when the scale definitions are reasonably aligned. Evaluate at least:

- CPU ONNX Runtime;
- NVIDIA GPU TensorRT or an explicitly named GPU runtime;
- one edge device relevant to the target application; and
- native framework as a reference.

Do not transfer a T4 ranking to Jetson, Raspberry Pi, mobile NPU, or Apple Neural Engine without measurement.

## Accuracy protocol

Record these fields before running evaluation:

| Category | Required fields |
|---|---|
| Model | version, scale, task, config, weight checksum, upstream commit |
| Dataset | name, release, split, annotation checksum, class mapping |
| Input | size, resize/letterbox policy, normalization, color order |
| Prediction | confidence threshold, max detections, decode path, NMS or end-to-end mode |
| Evaluator | implementation, version/commit, IoU thresholds, area ranges, maxDets |
| Output | raw prediction file, evaluator output, summary CSV, run manifest |

For COCO, use the official IoU sequence 0.50:0.05:0.95 and retain the official small/medium/large area definitions. A custom `APCrowd` must not be presented as a standard COCO metric. If crowd behavior is studied, define the subset-generation code and release the subset manifest.

## Latency and throughput protocol

Latency numbers are meaningful only with a timing boundary.

Report at least three components:

1. preprocessing;
2. model/runtime inference; and
3. decode plus post-processing.

Also report end-to-end latency. For NMS-free models, state whether output conversion or top-k selection remains outside the graph.

Minimum timing record:

- hardware model and memory;
- CPU model and thread settings;
- accelerator driver and power mode;
- framework/runtime and versions;
- precision;
- static or dynamic input shape;
- batch size;
- warm-up iterations;
- measured iterations;
- synchronization method;
- mean, median, standard deviation, p90, and p95 latency;
- preprocessing included/excluded;
- post-processing included/excluded; and
- data transfer included/excluded.

Throughput is not the reciprocal of latency when batching or asynchronous pipelines are involved. If FPS is derived as `1000 / latency_ms`, label it `derived_fps` and retain the source latency.

## YOLO26 dual-head protocol

YOLO26 exposes two materially different evaluation paths:

- **one-to-one, end-to-end:** NMS-free default path;
- **one-to-many:** traditional output requiring NMS and often slightly different AP.

Every record must include `head_mode`. Do not place one-to-many AP beside one-to-one latency without an explicit mixed-path warning.

## Quantization protocol

A credible INT8 row requires:

- source FP32/FP16 checkpoint and checksum;
- export graph and checksum;
- quantization method (PTQ or QAT);
- calibration dataset manifest, count, sampling seed, and preprocessing;
- per-tensor/per-channel and symmetric/asymmetric settings;
- excluded layers or mixed-precision policy;
- runtime and target device;
- baseline and quantized accuracy evaluated by the same evaluator; and
- baseline and quantized latency under the same timing protocol.

Do not present “500 calibration images” as a shared condition unless the exact images and selection method are documented.

## Robustness protocol

If robustness is evaluated, generate corruptions from a versioned script and publish the configuration. Recommended dimensions include:

- low illumination;
- motion and defocus blur;
- additive noise;
- compression;
- partial occlusion; and
- scale/crowding subsets.

For every corruption:

- preserve the clean baseline;
- define severity levels;
- store deterministic seeds;
- state whether annotations remain valid;
- report absolute AP and retention relative to the matched clean run; and
- avoid aggregating severities until the aggregation rule is defined.

An author-created radar chart with exact percentages requires the underlying result file. If no controlled run exists, use a qualitative conceptual diagram without numeric rings.

## Error analysis with TIDE

TIDE can decompose detection errors using prediction files. A publishable TIDE table requires:

- the same ground truth and evaluator settings for all compared models;
- unmodified prediction JSON files;
- exact TIDE version or commit;
- a script that generates the table and figures;
- raw TIDE output;
- definitions and denominators for any converted percentage; and
- at least one verification that category and image IDs align.

Do not create percentages that sum to 100% merely to illustrate a trend. TIDE’s contribution-to-AP-error quantities and raw event frequencies answer different questions and must be labeled separately.

## Ablation evidence

Cross-paper modules must not be combined into a fictional cumulative ablation. A valid ablation table uses one row per primary experiment:

| Source | Native baseline | Dataset | Changed component | Reported delta | Other changes | Comparable within source |
|---|---|---|---|---:|---|---|

Only a study that sequentially adds components in one codebase under one protocol can support a cumulative “full configuration” row.

## Statistical reporting

For validation of fixed official checkpoints, repeated timing runs characterize system variance. For training experiments, use multiple seeds where feasible and report mean, standard deviation, and individual runs. Do not interpret a small single-run AP difference as an architectural effect without uncertainty or replication.

## Required machine-readable artifacts

Each released result should point to:

- `run_manifest`: all environment and protocol fields;
- `raw_output`: unedited evaluator/runtime output;
- `prediction_file`: when error analysis or re-evaluation is claimed;
- `summary_row`: the normalized but non-harmonized repository record;
- `source_record`: primary or independent source; and
- `generation_script`: for every table or figure derived from the row.

The templates in `data/` and `configs/` are prospective. Their presence does not mean experiments have been completed.
