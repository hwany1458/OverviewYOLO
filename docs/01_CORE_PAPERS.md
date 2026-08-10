# Core papers and bibliographic evidence

This catalog distinguishes peer-reviewed papers, official technical reports/preprints, and software releases. A software-only release must not be described as a peer-reviewed model paper.

## Evidence maturity scale

| Level | Definition |
|---|---|
| `A` | Peer-reviewed primary paper plus an author-linked official implementation |
| `B` | Author-issued primary preprint or technical report plus an official implementation |
| `C` | Official software release and maintainers’ documentation, but no formal primary model paper |
| `D` | Secondary analysis or independent evaluation; useful for validation, not a replacement for primary evidence |

## Fourteen core releases

| Version | Representative primary record | Publication status | Evidence | Code |
|---|---|---|---|---|
| YOLOv1 | Redmon et al., [“You Only Look Once: Unified, Real-Time Object Detection”](https://arxiv.org/abs/1506.02640), CVPR 2016 | Peer reviewed | `A` | [Darknet](https://github.com/pjreddie/darknet) |
| YOLOv2 / YOLO9000 | Redmon and Farhadi, [“YOLO9000: Better, Faster, Stronger”](https://arxiv.org/abs/1612.08242), CVPR 2017 | Peer reviewed | `A` | [Darknet](https://github.com/pjreddie/darknet) |
| YOLOv3 | Redmon and Farhadi, [“YOLOv3: An Incremental Improvement”](https://arxiv.org/abs/1804.02767), 2018 | Technical report | `B` | [Darknet](https://github.com/pjreddie/darknet) |
| YOLOv4 | Bochkovskiy, Wang, and Liao, [“YOLOv4: Optimal Speed and Accuracy of Object Detection”](https://arxiv.org/abs/2004.10934), 2020 | Primary preprint | `B` | [AlexeyAB/darknet](https://github.com/AlexeyAB/darknet) |
| YOLOv5 | Jocher, [Ultralytics YOLOv5 software](https://github.com/ultralytics/yolov5), initial release 2020; [Zenodo DOI](https://doi.org/10.5281/zenodo.3908559) | No formal model paper | `C` | [ultralytics/yolov5](https://github.com/ultralytics/yolov5) |
| YOLOv6 | Li et al., [“YOLOv6: A Single-Stage Object Detection Framework for Industrial Applications”](https://arxiv.org/abs/2209.02976), 2022; Li et al., [“YOLOv6 v3.0: A Full-Scale Reloading”](https://arxiv.org/abs/2301.05586), 2023 | Technical reports | `B` | [meituan/YOLOv6](https://github.com/meituan/YOLOv6) |
| YOLOv7 | Wang, Bochkovskiy, and Liao, [“YOLOv7: Trainable Bag-of-Freebies Sets New State-of-the-Art for Real-Time Object Detectors”](https://openaccess.thecvf.com/content/CVPR2023/html/Wang_YOLOv7_Trainable_Bag-of-Freebies_Sets_New_State-of-the-Art_for_Real-Time_Object_Detectors_CVPR_2023_paper.html), CVPR 2023 | Peer reviewed | `A` | [WongKinYiu/yolov7](https://github.com/WongKinYiu/yolov7) |
| YOLOv8 | Jocher, Chaurasia, and Qiu, [Ultralytics YOLOv8 software and documentation](https://docs.ultralytics.com/models/yolov8/), release 2023 | No formal model paper | `C` | [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) |
| YOLOv9 | Wang, Yeh, and Liao, [“YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information”](https://arxiv.org/abs/2402.13616), 2024 | Primary preprint | `B` | [WongKinYiu/yolov9](https://github.com/WongKinYiu/yolov9) |
| YOLOv10 | Wang et al., [“YOLOv10: Real-Time End-to-End Object Detection”](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c34ddd05eb089991f06f3c5dc36836e0-Abstract-Conference.html), NeurIPS 2024 | Peer reviewed | `A` | [THU-MIG/yolov10](https://github.com/THU-MIG/yolov10) |
| YOLO11 | Jocher and Qiu, [Ultralytics YOLO11 software and documentation](https://docs.ultralytics.com/models/yolo11/), release 2024 | No formal model paper | `C` | [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) |
| YOLOv12 | Tian, Ye, and Doermann, [“YOLOv12: Attention-Centric Real-Time Object Detectors”](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7103444259031cc58051f8c9a4868533-Abstract-Conference.html), NeurIPS 2025 | Peer reviewed | `A` | [sunsmarterjie/yolov12](https://github.com/sunsmarterjie/yolov12) |
| YOLOv13 | Lei et al., [“YOLOv13: Real-Time Object Detection with Hypergraph-Enhanced Adaptive Visual Perception”](https://arxiv.org/abs/2506.17733), 2025 | Primary preprint | `B` | [iMoonLab/yolov13](https://github.com/iMoonLab/yolov13) |
| YOLO26 | Jocher et al., [“Ultralytics YOLO26: Unified Real-Time End-to-End Vision Models”](https://arxiv.org/abs/2606.03748), 2026 | Official technical report/preprint | `B` | [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) |

## Version-specific reading notes

### YOLOv1

Use the CVPR paper for the unified regression formulation, 7×7 grid, two boxes per cell, loss, and PASCAL VOC results. When redrawing the architecture, verify all 24 convolutional layers and the two fully connected layers against the paper rather than a simplified secondary diagram.

### YOLOv2 / YOLO9000

The paper contains two related contributions: the improved YOLOv2 detector and YOLO9000 joint detection/classification training. For architecture figures, the final detection head follows the concatenated passthrough and main features; do not add an unsupported second direct prediction branch.

### YOLOv3

The technical report is the primary source for Darknet-53, three prediction scales, independent logistic classifiers, and objectness prediction. Preserve the paper’s exact input size, dataset split, metric, and hardware when recording performance.

### YOLOv4

The primary record separates bag-of-freebies from bag-of-specials and reports results across multiple GPU generations. Do not compare a V100 speed with another model’s T4 or A100 speed without an `NC` or `P` label.

### YOLOv5

Ultralytics states that it did not publish a formal YOLOv5 research paper. Cite the versioned software record and repository. Distinguish original anchor-based YOLOv5 checkpoints from later YOLOv5u models using the anchor-free Ultralytics head; they are not interchangeable.

### YOLOv6

The 2022 report documents the industrial framework; the v3.0 report documents the later full-scale release. A record must identify the YOLOv6 generation and scale rather than writing only `YOLOv6`.

### YOLOv7

The CVPR paper is the stable bibliographic source. Training-time auxiliary heads and re-parameterized inference structures must be separated in parameter/FLOP records.

### YOLOv8

Ultralytics states that there is no formal model paper. Use versioned software/documentation and do not substitute a third-party architectural review as the primary citation. Documentation is a living source, so retain access date and package/repository revision.

### YOLOv9

The primary preprint introduces Programmable Gradient Information (PGI) and GELAN. Training graphs with auxiliary/reversible branches can have different parameter counts from converted inference models; record which artifact was evaluated.

### YOLOv10

Use the NeurIPS 2024 paper for consistent dual assignments and end-to-end, NMS-free inference. Timing boundaries must specify whether post-processing is excluded because the model is end-to-end.

### YOLO11

Ultralytics states that there is no formal model paper. Cite the official software/docs. Keep the official name `YOLO11`, not `YOLOv11`, in the project’s core lineage fields.

### YOLOv12

The peer-reviewed NeurIPS 2025 paper supersedes a preprint-only description for publication-status fields. Record the repository implementation and the exact release because values changed between early and conference materials.

### YOLOv13

The current primary evidence is the authors’ preprint and official code. The central mechanisms are Hypergraph-based Adaptive Correlation Enhancement (HyperACE), Full-Pipeline Aggregation-and-Distribution (FullPAD), and depthwise-separable lightweight blocks. Treat source-reported COCO gains as preliminary until independently reproduced across broader tasks and hardware.

### YOLO26

The official 2026 report documents a dual-head architecture, native one-to-one end-to-end inference, an optional one-to-many path, DFL-free regression, MuSGD, Progressive Loss, and Small-Target-Aware Label Assignment (STAL). Record one-to-one and one-to-many accuracy separately. The model name is not a sequential assertion that versions 14–25 exist.

## Influential derivatives

| Model | Representative record | Contribution | Evidence role |
|---|---|---|---|
| Scaled-YOLOv4 | Wang, Bochkovskiy, and Liao, [“Scaled-YOLOv4: Scaling Cross Stage Partial Network”](https://arxiv.org/abs/2011.08036), CVPR 2021 | Model scaling across resource envelopes | Primary derivative |
| YOLOR | Wang, Yeh, and Liao, [“You Only Learn One Representation”](https://arxiv.org/abs/2105.04206) | Explicit and implicit knowledge in a unified representation | Primary derivative |
| YOLOX | Ge et al., [“YOLOX: Exceeding YOLO Series in 2021”](https://arxiv.org/abs/2107.08430) | Anchor-free design, decoupled head, SimOTA | Primary derivative |
| PP-YOLO | Long et al., [“PP-YOLO: An Effective and Efficient Implementation of Object Detector”](https://arxiv.org/abs/2007.12099) | Industrial engineering in PaddlePaddle | Primary derivative |
| PP-YOLOv2 | Huang et al., [“PP-YOLOv2: A Practical Object Detector”](https://arxiv.org/abs/2104.10419) | Practical refinement of PP-YOLO | Primary derivative |
| PP-YOLOE | Xu et al., [“PP-YOLOE: An Evolved Version of YOLO”](https://arxiv.org/abs/2203.16250) | Anchor-free task alignment and deployment | Primary derivative |
| YOLO-NAS | [SuperGradients model implementation](https://github.com/Deci-AI/super-gradients) | Hardware-aware NAS and quantization-oriented design | Official software/model release; architectural search details are not fully disclosed in a conventional primary paper |

Do not state that a derivative innovation was “absorbed by” a later canonical release unless a primary source explicitly documents that lineage. Safer phrasing is `an analogous motif appears in later releases`.

## Independent-evaluation watchlist

These records are useful counterweights to official headline claims, but their task-specific results should not be generalized beyond their protocols.

| Scope | Study | What it contributes |
|---|---|---|
| YOLOv8–YOLOv13 | [“Benchmarking YOLOv8 to YOLOv13 for Robust Hand Gesture Recognition in Human–Robot Interaction”](https://www.nature.com/articles/s41598-025-23925-9), Scientific Reports, 2025 | Same task/training context across recent nano models; newer was not universally best |
| YOLOv5–YOLO11 | Jiang and Zhong, [“ODVerse33: Is the New YOLO Version Always Better?”](https://arxiv.org/abs/2502.14314), 2025 | Multi-domain benchmark across 33 datasets; indirect context for recent-release caution |
| YOLOv8/11/26 | Baral and Zhou, [“AutoFormBench”](https://arxiv.org/abs/2603.29832), 2026 | Form-element detection where YOLO11 outperformed evaluated YOLO26 variants |
| YOLOv5u/v8/11/26 | Ranjan et al., [aquaculture edge benchmark](https://arxiv.org/abs/2607.09835), 2026 | Accuracy, data efficiency, A100, and Raspberry Pi 5 behavior; emphasizes hardware- and data-dependent model selection |
| YOLO26 architecture | Sapkota et al., [“YOLO26: Key Architectural Enhancements and Performance Benchmarking for Real-Time Object Detection”](https://arxiv.org/abs/2509.25164) | Early deployment-focused secondary report; cite the corrected four-author record |

## Bibliographic rules

1. Prefer the peer-reviewed record when one exists, while preserving the arXiv link if it provides an open manuscript.
2. Use a software citation for YOLOv5, YOLOv8, and YOLO11; do not invent a journal or conference paper.
3. For living repositories, include the version/tag or commit and access date.
4. Do not use a survey as the only source for a core architectural claim when the primary paper or official repository is available.
5. Separate publication year, model release year, and documentation year when they differ.
6. Verify the complete author list against the current primary record before manuscript submission.
