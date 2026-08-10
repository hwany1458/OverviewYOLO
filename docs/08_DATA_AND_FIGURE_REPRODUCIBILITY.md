# Data and figure reproducibility

## Purpose

This release adds the minimum inspectable artifacts required to support the repository statement for the audited comparison subset and the project-created quantitative Figures 18 and 19. It does not retroactively validate every number in the submitted manuscript.

## Evidence chain

| Layer | File | Function |
|---|---|---|
| Source registry | `data/source_ledger.csv` | Stable source identity, type, URL, evidence level, and access date |
| Audited result rows | `data/audited/table4_accuracy_speed_size.csv` | Model-level AP, latency, parameters, FLOPs, protocol, head mode, and source locator |
| Per-number provenance | `data/provenance/claim_source_map.csv` | One row per numerical field, generated from each stable result record |
| Manuscript snapshot | `data/manuscript_snapshot/table4_submitted_snapshot.csv` | Preserves the submitted/revised Table 4 for discrepancy analysis; not evidence of correctness |
| Artifact status | `data/audit/manuscript_artifact_status.csv` | Release gate for Tables 4–10 and Figures 18–20 |
| Table generator | `scripts/generate_table4_audited.py` | Produces `tables/generated/table4_audited.md` |
| Figure generators | `scripts/figures/generate_figure18.py`, `generate_figure19.py` | Produce deterministic quantitative PNG/PDF files |
| Guarded synthesis | `scripts/figures/generate_figure20.py` | Produces only an explicitly qualitative heatmap after opt-in |

## Audited comparison groups

### `Y13_TABLE_I_T4_TRT_FP16`

- Source: Lei et al., *YOLOv13: Real-Time Object Detection with Hypergraph-Enhanced Adaptive Visual Perception*, Table I, page 7.
- Dataset and split: MS COCO 2017, val2017.
- Input: 640 × 640.
- Latency: one NVIDIA Tesla T4 GPU, TensorRT FP16.
- Scope: YOLOv8, YOLOv10, YOLO11, YOLOv12, and YOLOv13 N/S/L/X rows available in that table.
- Comparability: `C` within this source-defined group. This does not make training recipes identical, and it does not authorize comparison with a different hardware/runtime group.
- Evidence: YOLOv13 rows are `SR-P`; earlier-family rows are `IR` because the later paper reports/reproduces them under its comparison protocol.

### `ULTRA_DOCS_2026_08_11_T4_TRT10`

- Sources: official Ultralytics YOLO11 and YOLO26 performance documentation accessed on 11 August 2026.
- Dataset and split: MS COCO 2017, val2017.
- Input: 640 × 640.
- Latency: NVIDIA T4, TensorRT10 documentation column.
- Comparability: `P`. The documentation columns align, but YOLO11 is NMS-based and YOLO26 defaults to a one-to-one end-to-end head; post-processing/timing semantics are not reported in enough detail to assign `C`.
- Head rule: YOLO26's end-to-end AP (40.1–56.9) is paired with the default end-to-end latency. Its conventional one-to-many AP (40.9–57.5) is preserved in row notes and must not silently replace the e2e AP in an accuracy-latency plot.

## Reproduction commands

From the repository root:

```bash
python -m pip install -r requirements-figures.txt
python scripts/generate_claim_source_map.py
python scripts/generate_table4_audited.py
python scripts/generate_all_figures.py
python scripts/validate_repository.py
```

Expected quantitative outputs:

- `figures/generated/figure18_accuracy_latency_source_separated.png`
- `figures/generated/figure18_accuracy_latency_source_separated.pdf`
- `figures/generated/figure19_flops_accuracy_source_separated.png`
- `figures/generated/figure19_flops_accuracy_source_separated.pdf`
- `tables/generated/table4_audited.md`
- `data/provenance/claim_source_map.csv`

The optional qualitative Figure 20 snapshot requires an explicit acknowledgement:

```bash
python scripts/generate_all_figures.py --include-qualitative-figure20
```

The output is not a percentage-retention chart and must not be cited as controlled experimental evidence.

## Determinism and scope

The scripts perform no network access and no benchmark inference. They transform checked-in CSV records into tables and figures. Regeneration is deterministic up to small renderer/font differences across Matplotlib platforms. The numerical values remain source-reported or independently reproduced; they are not author-reproduced (`AR`) results.

## Release gate

A result can enter the default quantitative generators only when all of the following are present:

1. stable `record_id`;
2. resolvable `source_id` in `data/source_ledger.csv`;
3. exact source locator;
4. dataset, split, input, hardware, runtime, precision, and head mode fields;
5. `verification_status=verified`;
6. evidence and comparability labels; and
7. a declared figure-selection flag.

Rows that fail these conditions remain in a manuscript snapshot or blocked dataset and do not enter release figures.
