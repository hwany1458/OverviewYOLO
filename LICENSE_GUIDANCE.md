# License guidance before public release

No license is granted merely by publishing a GitHub repository. Without an explicit license, visitors generally have no permission to reuse the project’s original code, data curation, or documentation.

## Recommended split

Because this repository contains different artifact types, consider a clearly documented split:

- **Original utility code:** MIT or BSD-3-Clause.
- **Original documentation, curated tables, and project-created figures:** CC BY 4.0.
- **Manuscript text:** follow the journal’s final publishing license and self-archiving policy.
- **Third-party implementations, model weights, datasets, and figures:** retain the original provider’s license; do not place them under the OverviewYOLO license.

If a single repository-level license is preferred, obtain institutional advice about whether the code and non-code materials should share one license.

## Required public-release actions

1. Add the selected license text or texts at the repository root.
2. Add a short licensing table to the README.
3. Mark every imported or adapted figure with its source and permission basis.
4. Do not upload upstream model weights or datasets merely because they are publicly downloadable.
5. Pin upstream code to a release or commit and record the license observed at that revision.
6. Preserve notices required by any code that is actually incorporated.
7. Review AGPL-3.0 and GPL-3.0 obligations before combining upstream code with project utilities.

## Upstream examples observed during curation

Licenses can change, so the pinned upstream revision is authoritative.

| Upstream | License observed in the current repository | Repository action |
|---|---|---|
| `pjreddie/darknet` | YOLO license stating Darknet is public domain | Link and record revision |
| `AlexeyAB/darknet` | Check the exact upstream revision and included notices | Do not assume compatibility |
| `ultralytics/yolov5` | AGPL-3.0 / separate enterprise option | Link rather than vendor |
| `ultralytics/ultralytics` | AGPL-3.0 / separate enterprise option | Link rather than vendor |
| `meituan/YOLOv6` | GPL-3.0 | Keep isolated unless obligations are met |
| `WongKinYiu/yolov7` | GPL-3.0 | Keep isolated unless obligations are met |
| `WongKinYiu/yolov9` | GPL-3.0 | Keep isolated unless obligations are met |
| `THU-MIG/yolov10` | AGPL-3.0 | Link rather than vendor |
| `sunsmarterjie/yolov12` | AGPL-3.0 | Link rather than vendor |
| `iMoonLab/yolov13` | AGPL-3.0 | Link rather than vendor |
| `Megvii-BaseDetection/YOLOX` | Apache-2.0 | Preserve license and notices if reused |

This file is a project-management checklist, not legal advice.
