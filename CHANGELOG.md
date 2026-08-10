# Changelog

All material corrections should be recorded here in addition to Git history, especially corrections that affect a manuscript table, figure, or conclusion.

## Unreleased

### Required before manuscript resubmission

- Populate the claim-level source ledger.
- Replace or remove untraceable robustness, quantization, ablation, scale/crowding, and error-analysis values.
- Add deterministic figure/table generation scripts.
- Add author-reproduced run manifests and raw outputs only after execution.
- Pin every upstream source to a tag or commit.
- Select repository licenses.
- Create the final `CITATION.cff` after verifying the complete author and DOI records.

## 0.1.0 — 2026-08-11

### Added

- Detailed public-facing README and lineage summary.
- Curated core-paper and official-code catalogs.
- Evidence-maturity and comparability policies.
- Prospective accuracy, latency, quantization, robustness, and TIDE protocols.
- Core-version and source-ledger CSV files.
- Benchmark-result and run-manifest schemas.
- Core BibTeX library.
- Official-source cloning helper.
- Metadata and local-link validator with GitHub Actions workflow.
- Public-release, licensing, citation, and manuscript-traceability guidance.

### Scientific safeguards

- Explicitly distinguished source-reported, independent, and author-reproduced evidence.
- Prohibited paired deltas for partially or non-comparable records.
- Distinguished YOLOv5 from YOLOv5u.
- Distinguished YOLO26 one-to-one and one-to-many evaluation paths.
- Marked numeric robustness and error-analysis outputs as unavailable until controlled runs and raw artifacts are released.
