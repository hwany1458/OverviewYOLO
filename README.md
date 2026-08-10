# OverviewYOLO

## From YOLOv1 to YOLO26: evidence-tracked resources for a unified comparative review

OverviewYOLO is the companion repository for the manuscript **“From YOLOv1 to YOLO26: A Unified Comparative Review of the Evolution, Architecture, and Applications of YOLO-Based Object Detection Frameworks.”** It organizes the primary papers, official implementations, source-reported benchmarks, evaluation protocols, and provenance records used in the review.

Manuscript record: [public preprint](https://www.preprints.org/manuscript/202607.1076). The journal version is under revision; repository releases should identify which manuscript version they support.

The repository is designed for two audiences:

1. readers who need a concise, version-wise map of the YOLO lineage; and
2. reviewers and researchers who need to trace a quantitative statement back to its paper, repository, model, dataset, and evaluation conditions.

> **Important:** this is an evidence-tracked literature and reproducibility resource. Unless a result is explicitly labeled `AR` (author-reproduced), numerical values are **not** presented as hardware-normalized re-benchmarking.

## Scope and naming

The review covers fourteen major releases:

`YOLOv1`, `YOLOv2`, `YOLOv3`, `YOLOv4`, `YOLOv5`, `YOLOv6`, `YOLOv7`, `YOLOv8`, `YOLOv9`, `YOLOv10`, `YOLO11`, `YOLOv12`, `YOLOv13`, and `YOLO26`.

The phrase **“YOLOv1 to YOLO26”** denotes the lineage spanning these releases. It does **not** imply that YOLOv14 through YOLOv25 exist. We preserve the names used by their maintainers: community and academic releases commonly retain the `v` prefix, whereas Ultralytics uses the official names `YOLO11` and `YOLO26`.

YOLO26 requires a date distinction in bibliographic records: initial model/repository availability is associated with 2025, whereas the formal Ultralytics technical report is dated 2026. Repository records keep both dates visible rather than silently collapsing them.

## What the review contributes

The manuscript interprets YOLO development as a sequence of bottleneck–response transitions rather than a simple list of models. Its principal analytical contributions are:

- a longitudinal map from unified regression in YOLOv1 to hypergraph-enhanced correlation modeling in YOLOv13 and native end-to-end, NMS-free inference in YOLO26;
- a **Why–How–What–Where** framework linking the motivation for a transition, its implementation mechanism, its measured effect, and its deployment context;
- a causal evolution matrix across backbone, neck, head, loss, label assignment, training strategy, and inference pipeline;
- an evidence-aware synthesis of accuracy, latency, throughput, parameters, FLOPs, and deployment characteristics;
- a distinction between accuracy-driven complexification and deployment-driven simplification;
- application mapping across autonomous systems, surveillance, industry, medicine, agriculture, remote sensing, and edge/mobile vision; and
- explicit treatment of evidence maturity for recent releases, especially YOLOv13 and YOLO26.

## Four evolutionary eras

| Era | Models | Dominant transition | Typical deployment concern |
|---|---|---|---|
| Foundation, 2016–2018 | YOLOv1–v3 | Unified regression, anchor priors, multi-scale prediction | Establishing real-time one-stage detection |
| Optimization and productization, 2020–2023 | YOLOv4–v8 and major derivatives | CSP/PAN aggregation, training-time “freebies,” re-parameterization, decoupled and anchor-free heads | Scalable training, export, and industrial use |
| Attention and refinement, 2024–early 2025 | YOLOv9–v12 | PGI/GELAN, end-to-end assignment, efficient attention | Accuracy–latency refinement under modern runtimes |
| Bifurcation, 2025–2026 | YOLOv13 and YOLO26 | High-order correlation modeling versus deployment-oriented simplification | Complex-scene accuracy versus deterministic edge inference |

## Core lineage at a glance

| Version | Primary evidence | Key contribution | Official implementation |
|---|---|---|---|
| YOLOv1 | CVPR 2016 paper | Detection as single-network regression | [pjreddie/darknet](https://github.com/pjreddie/darknet) |
| YOLOv2 / YOLO9000 | CVPR 2017 paper | Anchor priors, dimension clustering, multi-scale training | [pjreddie/darknet](https://github.com/pjreddie/darknet) |
| YOLOv3 | Official technical report | Darknet-53 and three-scale prediction | [pjreddie/darknet](https://github.com/pjreddie/darknet) |
| YOLOv4 | Official preprint | CSPDarknet53, SPP/PAN, bag of freebies and specials | [AlexeyAB/darknet](https://github.com/AlexeyAB/darknet) |
| YOLOv5 | Official software release; no formal paper | PyTorch-native productization and broad export support | [ultralytics/yolov5](https://github.com/ultralytics/yolov5) |
| YOLOv6 | Official technical reports | EfficientRep, re-parameterization, industrial deployment | [meituan/YOLOv6](https://github.com/meituan/YOLOv6) |
| YOLOv7 | CVPR 2023 paper | E-ELAN and trainable bag-of-freebies | [WongKinYiu/yolov7](https://github.com/WongKinYiu/yolov7) |
| YOLOv8 | Official software/docs; no formal paper | Anchor-free split head and multi-task platform | [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) |
| YOLOv9 | Official preprint | Programmable Gradient Information and GELAN | [WongKinYiu/yolov9](https://github.com/WongKinYiu/yolov9) |
| YOLOv10 | NeurIPS 2024 paper | Consistent dual assignments and NMS-free inference | [THU-MIG/yolov10](https://github.com/THU-MIG/yolov10) |
| YOLO11 | Official software/docs; no formal paper | Refined backbone/neck and multi-task efficiency | [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) |
| YOLOv12 | NeurIPS 2025 paper | Attention-centric real-time detection | [sunsmarterjie/yolov12](https://github.com/sunsmarterjie/yolov12) |
| YOLOv13 | Official preprint | HyperACE and FullPAD high-order correlation modeling | [iMoonLab/yolov13](https://github.com/iMoonLab/yolov13) |
| YOLO26 | Official 2026 technical report | Dual-head end-to-end inference, DFL removal, MuSGD, Progressive Loss, and STAL | [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) |

Full bibliographic details and evidence notes are in [Core papers](docs/01_CORE_PAPERS.md). Official code, weights, framework constraints, and license observations are in [Official code and models](docs/02_OFFICIAL_CODE_AND_MODELS.md).

## Evidence labels

Every result should carry one of the following provenance labels:

| Label | Meaning | Allowed interpretation |
|---|---|---|
| `SR-P` | Source-reported in a primary paper or official technical report | Report exactly with the source protocol |
| `SR-R` | Source-reported in an official repository or release note | Report with repository version and access date |
| `IR` | Independently reproduced by a third party | Report with the independent study’s full protocol |
| `AR` | Reproduced by this project’s authors | Report with code, environment, weights, dataset manifest, and raw outputs |
| `SYN` | Qualitative cross-source synthesis | No invented precision; do not present as a controlled experiment |

Evidence labels are separate from comparability labels:

| Label | Comparability | Rule |
|---|---|---|
| `C` | Comparable | Dataset/split, task, input, precision, hardware/runtime, batch, and timing scope are aligned closely enough for a paired comparison |
| `P` | Partially comparable | Some conditions align, but at least one material condition differs; describe the difference and avoid a strong ranking claim |
| `NC` | Not directly comparable | Do not compute a delta, speedup, or Pareto dominance claim |

See [Evidence and comparability policy](docs/04_EVIDENCE_AND_COMPARABILITY.md) for the decision rules.

## Repository contents

```text
OverviewYOLO-public/
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE_GUIDANCE.md
├── configs/
│   └── benchmark_protocol.yaml
├── data/
│   ├── core_versions.csv
│   ├── source_ledger.csv
│   ├── benchmark_results_template.csv
│   └── run_manifest_template.csv
├── docs/
│   ├── 01_CORE_PAPERS.md
│   ├── 02_OFFICIAL_CODE_AND_MODELS.md
│   ├── 03_EXPERIMENTS_AND_BENCHMARKS.md
│   ├── 04_EVIDENCE_AND_COMPARABILITY.md
│   ├── 05_PUBLIC_RELEASE_CHECKLIST.md
│   ├── 06_MANUSCRIPT_TRACEABILITY.md
│   ├── 07_REPOSITORY_UPLOAD_GUIDE_KO.md
│   └── CITATION_SETUP.md
├── experiments/
│   └── README.md
├── references/
│   └── yolo_core.bib
└── scripts/
    ├── clone_official_sources.sh
    └── validate_repository.py
```

## Resource status

This table prevents a repository visitor from mistaking a planned artifact for an available one.

| Resource | Status in this package | Interpretation |
|---|---|---|
| Core paper catalog | Available | Curated links and evidence maturity |
| Official code/model catalog | Available | Links only; third-party code and weights are not redistributed |
| BibTeX library | Available | Core releases plus selected derivatives |
| Source ledger | Available | Seed records; must be extended at claim/table-cell level |
| Benchmark protocol | Available | Prospective protocol, not proof that runs were completed |
| Source-reported benchmark table | Schema available; values under audit | Publish only traceable rows |
| Author-reproduced benchmarks | Not yet released | Add only after raw outputs and run manifests exist |
| TIDE error analysis | Protocol specified; results not yet released | Do not publish synthetic error percentages |
| Figure-generation scripts | Not included in the initial package | Required before claiming public availability |
| Model weights and datasets | Not redistributed | Obtain from original providers under their terms |

## Quantitative-use rule

The review combines values reported under heterogeneous protocols. Hardware, software stack, batch size, precision, input resolution, post-processing, and dataset split may differ. Therefore:

- retain every material condition in the result record;
- never convert latency to FPS without labeling the derived value and preserving the original latency;
- do not compare `test-dev` with `val2017` as if they were the same split;
- do not compare TensorRT FP16 with PyTorch FP32 as a hardware-only difference;
- report one-to-one and one-to-many YOLO26 heads separately;
- do not treat YOLOv5 and YOLOv5u as the same architecture;
- do not treat current documentation values as immutable—record the access date and software version; and
- do not calculate a cross-model delta when comparability is `P` or `NC`.

## Reproducing or extending the benchmark

1. Read [Experiments and benchmarks](docs/03_EXPERIMENTS_AND_BENCHMARKS.md).
2. Create one isolated environment or container per upstream repository family.
3. Pin the upstream repository to a release tag or commit SHA.
4. Record dataset checksums, model-weight checksums, framework versions, CUDA/cuDNN/TensorRT versions, hardware, power mode, and timing scope.
5. Validate accuracy with the official dataset evaluator.
6. Measure preprocessing, model inference, and post-processing separately, then report end-to-end latency as an additional value.
7. Store one `run_manifest` and the raw evaluator output for every result row.
8. Run `python scripts/validate_repository.py` before opening a pull request or generating manuscript tables.

The helper `scripts/clone_official_sources.sh` clones official upstream repositories into an external directory. It does not vendor those repositories into OverviewYOLO and does not override their licenses.

## Error analysis

Error proportions must come from a controlled evaluation, not an approximate cross-source narrative. A valid error-analysis release must include:

- the exact dataset and annotation version;
- the exact prediction file for every model;
- model and weight identifiers;
- confidence, IoU, maximum-detection, and NMS/end-to-end settings;
- the evaluator and TIDE version;
- the denominator used for every percentage; and
- the script and raw outputs used to produce each table or figure.

Until these artifacts are public, claims about background false positives, localization errors, small-object misses, occlusion misses, or class confusion should remain qualitative.

## Datasets and evaluation tools

- [MS COCO](https://cocodataset.org/) and the official [COCO API](https://github.com/cocodataset/cocoapi)
- [PASCAL VOC](https://www.robots.ox.ac.uk/~vgg/projects/pascal/VOC/)
- [KITTI Vision Benchmark Suite](https://www.cvlibs.net/datasets/kitti/)
- [TIDE error analysis](https://github.com/dbolya/tide)

Dataset files are not included here. Their original licenses, access requirements, and terms remain in force.

## Selected derivatives

The main lineage is supplemented by influential branches that changed the design space without constituting consecutive canonical version numbers:

- [Scaled-YOLOv4](https://github.com/WongKinYiu/ScaledYOLOv4): compound scaling of CSP-based detectors;
- [YOLOR](https://github.com/WongKinYiu/yolor): unified explicit and implicit knowledge representations;
- [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX): anchor-free detection, decoupled head, and SimOTA;
- [PP-YOLO / PP-YOLOE](https://github.com/PaddlePaddle/PaddleDetection): industrial optimization in the Paddle ecosystem; and
- [YOLO-NAS in SuperGradients](https://github.com/Deci-AI/super-gradients): hardware-aware neural architecture search and quantization-oriented deployment.

Derivative-to-canonical relationships are described as analogous or influential design motifs unless a primary source explicitly establishes direct inheritance.

## Citation

The manuscript is under revision. Do not add a fictitious DOI or incomplete author list. Follow [Citation setup](docs/CITATION_SETUP.md) to create `CITATION.cff` after the final bibliographic record is available. The core model references can be imported from [references/yolo_core.bib](references/yolo_core.bib).

## Licensing and third-party material

OverviewYOLO contains original documentation, curation records, schemas, and validation utilities. Upstream implementations, model weights, datasets, and borrowed figures remain governed by their original licenses. This repository links to those materials rather than relicensing or redistributing them.

Before public release, select licenses for the original code and for documentation/data. See [License guidance](LICENSE_GUIDANCE.md). This document is not legal advice.

## Limitations

- The repository does not make heterogeneous source-reported benchmarks directly comparable.
- Recent releases may have limited independent replication and may change after repository or package updates.
- Official documentation pages are living sources; stable releases and commit hashes are preferable for archival claims.
- Maximum headline accuracy is not a sufficient deployment criterion. Target hardware, runtime, quantization toolchain, memory, energy, thermal behavior, and application distribution must be validated separately.
- A linked official repository is evidence that an implementation exists, not evidence that this project reproduced its reported results.

## Contributing

Contributions are welcome when they improve provenance, reproducibility, or correction of the scholarly record. Please read [CONTRIBUTING.md](CONTRIBUTING.md). New performance rows without a primary source or complete run manifest will not be merged.

## Contact

Questions about the manuscript or curated records should be directed to the corresponding author using the contact information in the submitted article. Please use GitHub Issues for verifiable errors in links, metadata, or evaluation records.
