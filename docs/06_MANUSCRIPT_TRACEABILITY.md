# Manuscript-to-repository traceability

## Goal

This file defines the evidence chain expected for the revised manuscript. It does not assert that every current manuscript table has already passed the audit.

## Traceability map

| Manuscript component | Repository source of truth | Required generator/evidence | Current package status |
|---|---|---|---|
| Scope and fourteen-version lineage | `data/core_versions.csv` | README/version catalog | Available |
| Core roadmap and era classification | `data/core_versions.csv` plus primary papers | Timeline generation script | Data available; script still needed for the manuscript figure |
| Representative papers | `docs/01_CORE_PAPERS.md`, `references/yolo_core.bib` | Bibliographic audit | Available |
| Official implementations and weights | `docs/02_OFFICIAL_CODE_AND_MODELS.md`, `data/source_ledger.csv` | Link/revision/license audit | Seed catalog available |
| Causal Evolution Matrix | Claim-level source ledger | Matrix-generation script | Must be added at claim level |
| Cross-version quantitative table | `data/benchmark_results_*.csv` | Table-generation script | Schema only; manuscript values require audit |
| Derived-model comparison (Supplementary) | Result records plus comparability labels | Script that leaves `P`/`NC` deltas blank | Schema/policy available; populated audited table still needed |
| Accuracy–latency/FLOPs figures | Audited result records | Deterministic plotting script | Not included in initial package |
| Robustness figure/table | Controlled corruption-run records | Corruption and plotting scripts plus raw results | Not released; numeric claims should not be public yet |
| Scale/crowding table | Official COCO metrics or released custom subset | Evaluator/subset script | Existing manuscript values require audit |
| Quantization table | FP baseline and INT8 paired run manifests | Export/calibration/evaluation scripts | Existing manuscript values require audit |
| Ablation table | One native ablation source per row | Source extraction script or author run | Existing cumulative cross-paper construction must be replaced |
| Error-type table | Prediction JSON plus TIDE run | TIDE script and raw output | Not released; approximate percentages must not be used |
| Figure 2 (YOLOv1) | Original paper/cfg and project figure source | Editable source and render script | Figure exists in manuscript; technical layer count must be rechecked |
| Figure 3 (YOLOv2) | Original paper/cfg and project figure source | Editable source and render script | Figure exists; unsupported direct head must be removed if still present |
| Figure 8 (YOLOv7) | CVPR paper and official cfg | Editable source and render script | Figure exists; tensor sizes/head labels must be rechecked |

## Result-record key

Each quantitative manuscript cell should cite or internally map to a stable `result_id`, for example:

```text
SRP-yolov13-n-coco-val2017-ap5095-001
SRR-yolo26-n-coco-val2017-t4trt10fp16-latency-001
AR-yolov8-n-coco-val2017-onnx-cpu-latency-001
```

Recommended structure:

`<evidence>-<model>-<scale>-<dataset>-<split>-<runtime/metric>-<sequence>`

The identifier must remain stable when wording changes. If the underlying value is corrected, keep the ID and document the correction in Git history/changelog; if the protocol changes, create a new ID.

## Source-record fields for manuscript claims

Add these columns when the seed source ledger is expanded to cell-level provenance:

- `manuscript_section`
- `manuscript_table_figure`
- `manuscript_claim`
- `result_id`
- `source_id`
- `source_location`
- `original_value`
- `original_unit`
- `transformation`
- `display_value`
- `evidence_label`
- `comparability_label`
- `verification_status`
- `verified_by`
- `verified_on`

## Data Availability alignment

The current manuscript statement promises author-curated tables, figure-generation scripts, and benchmark-harness materials. Before resubmission, either:

1. publish those artifacts and point to a versioned release; or
2. narrow the statement to the resources actually available.

A defensible interim statement would be:

> This review did not generate a new experimental dataset. The repository provides the curated bibliography, official-source registry, provenance schema, and prospective benchmark protocol used to organize the review. Source-reported values remain attributable to the cited primary papers and official repositories. Author-reproduced benchmark outputs and figure-generation materials are identified individually when available. Third-party datasets, weights, and implementations remain subject to their original licenses and access policies.

Use the stronger original statement only after the promised scripts and result records are public.

## Reviewer-response use

For every reviewer comment involving a value, figure, or comparison, the response letter should identify:

- the manuscript location;
- the repository file and record ID;
- the evidence and comparability labels;
- whether the value is source-reported or reproduced;
- the correction or new analysis; and
- the versioned repository release used for resubmission.
