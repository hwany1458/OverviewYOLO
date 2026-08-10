# Citation setup

The manuscript is under revision, so the repository should not publish an invented DOI or incomplete author record.

## Before acceptance or final preprint DOI

Keep the README’s citation section descriptive and cite the core models through `references/yolo_core.bib`. If a public preprint has a stable DOI and the authors approve it as the preferred citation, use that record.

## After the final bibliographic record exists

Create a root-level `CITATION.cff` with verified values:

```yaml
cff-version: 1.2.0
message: "If you use this repository, please cite the companion review."
title: "OverviewYOLO: Companion Resources for From YOLOv1 to YOLO26"
type: dataset
authors:
  - family-names: "<verified family name>"
    given-names: "<verified given names>"
    orcid: "https://orcid.org/<verified ORCID>"
  - family-names: "<verified family name>"
    given-names: "<verified given names>"
version: "1.0.0"
date-released: "YYYY-MM-DD"
repository-code: "https://github.com/hwany1458/OverviewYOLO"
doi: "<real DOI only>"
preferred-citation:
  type: article
  title: "From YOLOv1 to YOLO26: A Unified Comparative Review of the Evolution, Architecture, and Applications of YOLO-Based Object Detection Frameworks"
  authors:
    - family-names: "<verified family name>"
      given-names: "<verified given names>"
    - family-names: "<verified family name>"
      given-names: "<verified given names>"
  journal: "<journal>"
  year: <year>
  doi: "<article DOI>"
```

## Recommended archival sequence

1. Complete the data/source audit.
2. Tag the exact repository state used for resubmission.
3. Create a GitHub release.
4. Archive that release with Zenodo if desired.
5. Add the repository DOI to `CITATION.cff`.
6. Keep the article DOI and repository DOI as separate identifiers with separate citations.
