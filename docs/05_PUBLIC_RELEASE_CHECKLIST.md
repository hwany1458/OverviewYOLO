# Public-release checklist

Use this checklist before changing the repository from private to public and again before manuscript resubmission.

## A. Repository identity

- [ ] Repository title and description match the manuscript.
- [ ] `YOLOv1 to YOLO26` naming note is visible near the top of the README.
- [ ] YOLO11 and YOLO26 official names are used consistently.
- [ ] YOLO26 model-availability year and 2026 formal-report year are distinguished.
- [ ] Topics, website/preprint link, and contact route are set.
- [ ] Default branch is identified and protected where appropriate.

## B. Claims promised by the Data Availability Statement

- [ ] Author-curated comparison tables are present and machine readable.
- [ ] Every quantitative row has source provenance.
- [ ] Figure-generation scripts are present for every project-created quantitative figure.
- [ ] Benchmark-harness materials are present or the statement is narrowed to what is actually available.
- [ ] Analysis scripts are present for every derived metric.
- [ ] A public visitor can access the repository without authentication.
- [ ] The manuscript access date is updated to the actual public-release date.

Do not retain a Data Availability claim for files that are only planned.

## C. Scientific validity

- [ ] Tables 5–10 from the manuscript have been audited at cell level.
- [ ] No synthetic or untraceable robustness percentages remain.
- [ ] No custom `APCrowd` is presented as a standard COCO metric.
- [ ] Quantization rows include calibration and runtime provenance.
- [ ] Cross-paper modules are not combined into a fictional cumulative ablation.
- [ ] Error percentages have prediction files, denominators, and analysis code.
- [ ] `P` and `NC` rows have no paired delta.
- [ ] YOLO26 one-to-one and one-to-many results are separated.
- [ ] YOLOv5 is distinguished from YOLOv5u.
- [ ] Source-reported and author-reproduced values are visually distinguishable.

## D. Reproducibility

- [ ] Every upstream repository is pinned to a tag or commit.
- [ ] Every model weight has a checksum.
- [ ] Dataset and annotation manifests include checksums and license/access notes.
- [ ] Environment files or container digests are available.
- [ ] Exact commands are stored.
- [ ] Raw evaluator and timing outputs are retained.
- [ ] Timing scope and synchronization are documented.
- [ ] Exported artifacts record exporter/runtime versions and validation deltas.
- [ ] Random seeds are recorded for training, sampling, and corruptions.
- [ ] Failed runs and deviations are documented rather than silently removed.

## E. Bibliography

- [ ] Every core version has a primary or official source.
- [ ] YOLOv5, YOLOv8, and YOLO11 are cited as software/docs, not fictitious formal papers.
- [ ] YOLOv7 points to the CVPR 2023 record.
- [ ] YOLOv10 points to NeurIPS 2024.
- [ ] YOLOv12 points to NeurIPS 2025.
- [ ] YOLOv13 is identified as a primary preprint unless publication status changes.
- [ ] YOLO26 points to the official 2026 report.
- [ ] Sapkota et al. `arXiv:2509.25164` has the corrected four-author record.
- [ ] All living web/repository sources have access dates and pinned versions where possible.

## F. Figures and tables

- [ ] Figure data files and generation scripts are present.
- [ ] Figures 2, 3, and 8 match the technical architecture and current manuscript captions.
- [ ] No unsupported YOLOv2 direct prediction branch remains.
- [ ] YOLOv7 feature-map sizes, head naming, and output tensor notation are correct.
- [ ] Figure captions distinguish adapted, reproduced, and author-created content.
- [ ] Table and figure source IDs resolve to `data/source_ledger.csv`.
- [ ] No chart states “identical stress tests” without a released common pipeline.
- [ ] All accessibility alt text is present in the manuscript and web materials.

## G. Licensing and privacy

- [ ] A repository license or license split has been selected.
- [ ] Third-party licenses are recorded at pinned revisions.
- [ ] No dataset, checkpoint, figure, or code has been redistributed without permission.
- [ ] No API keys, tokens, credentials, private URLs, reviewer identities, or hidden comments are committed.
- [ ] Git history has been scanned for secrets, not only the current tree.
- [ ] Large binaries are excluded or managed intentionally.
- [ ] Personal data in logs and absolute local paths have been removed.

## H. Citation and archival release

- [ ] `CITATION.cff` contains the final author list and identifiers.
- [ ] Manuscript/preprint DOI is added only when real.
- [ ] A versioned GitHub release is created.
- [ ] The release tag is referenced in the resubmitted manuscript.
- [ ] Zenodo archival integration is considered for a repository DOI.
- [ ] The archived release contains the same data and scripts used for submitted tables/figures.
- [ ] A changelog summarizes corrections made after peer review.

## I. Automated checks

- [ ] `python scripts/validate_repository.py` passes locally.
- [ ] GitHub Actions passes on the public branch.
- [ ] Every Markdown link has been checked or sampled manually.
- [ ] CSV files open with UTF-8 and consistent column counts.
- [ ] YAML parses successfully.
- [ ] BibTeX has no placeholder authors or duplicate keys.

## Final release gate

The repository is ready to support the manuscript only when a reviewer can select a table value and trace it through:

`manuscript cell → result record → source/run manifest → raw value → generation script`.

If that chain breaks, narrow the manuscript’s Data Availability Statement or complete the missing artifact before public release.
