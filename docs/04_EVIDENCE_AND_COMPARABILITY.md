# Evidence, comparability, and claim policy

## Objective

The repository must make it possible to answer two questions for every statement:

1. **Where did the claim or value come from?**
2. **What comparisons does the available evidence legitimately support?**

## Source hierarchy

Use sources in this order for core model claims:

1. peer-reviewed primary paper;
2. author-issued primary preprint or technical report;
3. official repository, versioned release, model card, and documentation;
4. peer-reviewed independent reproduction or benchmark;
5. independent preprint with a complete public protocol;
6. high-quality survey for context only; and
7. blog/tutorial only for non-scholarly operational guidance.

A lower-ranked source may be essential when a higher-ranked source does not report a field, but it cannot silently replace the higher-ranked source’s protocol.

## Evidence labels

### `SR-P` — source-reported primary

The value appears in a primary paper or official technical report. Store the exact table/figure/page and original unit.

### `SR-R` — source-reported repository

The value appears in an official repository, release, model card, or documentation. Store the tag/commit/package version and access date because the page may change.

### `IR` — independent reproduction

The value comes from a separate study that trained or evaluated the model. Store its task, dataset, protocol, and code availability. An `IR` result is not automatically a reproduction of the primary COCO claim.

### `AR` — author-reproduced

The OverviewYOLO authors executed the run. A valid `AR` row requires an upstream pin, environment, dataset/weight checksums, exact command, raw output, and run manifest.

### `SYN` — synthesis

The statement is an author interpretation across sources. It must use qualitative or bounded wording. `SYN` cannot manufacture numerical precision absent from the underlying sources.

## Comparability decision

Evaluate the following fields:

- task;
- dataset release and split;
- metric definition;
- model scale/capacity;
- input size and preprocessing;
- checkpoint training data/recipe;
- precision;
- runtime/export;
- hardware;
- batch size;
- timing boundary;
- post-processing/head mode; and
- software version.

### `C` — comparable

All fields material to the specific claim are aligned. Example: two models evaluated by the same script on COCO val2017, 640×640, batch 1, TensorRT 10 FP16, same T4, same timing boundary, and matched post-processing scope.

### `P` — partially comparable

The records share some major conditions, but at least one material field differs or is unknown. Example: same dataset and input but different GPU/runtime. Absolute values may be shown side by side if the difference is visible; a strong speedup or paired delta is not justified.

### `NC` — not directly comparable

The records differ on dataset/split, input resolution, metric, task, model path, or multiple major runtime conditions. Show the values only as historical source records. Leave paired delta blank.

## Delta rules

A numerical delta, ratio, speedup, or Pareto dominance claim requires `C`. For `P` or `NC`:

- `delta_value` must be empty;
- `delta_reason` must explain why no delta is computed; and
- narrative wording must avoid `outperforms`, `improves by`, or `faster than` unless the cited source itself made a within-protocol comparison.

## Derived values

Derived values are allowed only when:

- the formula is explicit;
- the original value is retained;
- the result is labeled `derived`;
- significant figures do not exceed the source; and
- the derivation does not create false comparability.

For example, `1000 / 1.7 ms = 588 FPS` is a reciprocal-latency value, not a measured asynchronous throughput result.

## Claim language

| Evidence situation | Preferred wording |
|---|---|
| Primary result only | “The primary release reports …” |
| Official repository value | “The official repository reports … as of [date/version].” |
| Independent task-specific result | “In [task/dataset], the independent evaluation found …” |
| Cross-source pattern | “Across the reviewed sources, a recurring qualitative pattern is …” |
| Author interpretation | “We interpret this transition as …” |
| Non-comparable values | “The absolute values are shown for context but are not directly comparable.” |

Avoid universal deployment prescriptions. Use `candidate for evaluation` instead of `recommended model` until target-hardware and target-data validation exists.

## Recent-model maturity

| Model | Current primary evidence | Independent evidence | Recommended maturity wording |
|---|---|---|---|
| YOLOv13 | 2025 primary preprint and author code | Emerging task-specific peer-reviewed evaluation | `Preliminary with emerging independent evidence` |
| YOLO26 | 2026 official technical report, official code/docs; initial model availability predates the report | Several early task- and device-specific studies | `Preliminary with emerging independent evidence` |

Do not label either model `mature` solely because official weights and documentation are available.

## Architecture lineage

Similarity is not proof of inheritance. Use one of these relationship labels:

- `explicitly inherited`: stated by a primary source;
- `author-acknowledged influence`: source acknowledges the earlier work;
- `architecturally analogous`: similar design motif without a documented inheritance path; or
- `independent/convergent`: similar objective reached through different design choices.

## Source-ledger granularity

A paper-level bibliography is not enough for a quantitative review. The source ledger should eventually contain one record per manuscript claim or table-cell group. Each record should include:

- manuscript location;
- claim/value;
- source ID;
- source location;
- evidence label;
- comparability label;
- transformation/derivation;
- verification status; and
- reviewer-relevant notes.

## Prohibited practices

- Filling missing benchmark cells with approximate values inferred from charts unless digitization is declared and uncertainty is reported.
- Creating error rates that lack prediction files and a denominator.
- Combining ablations from different papers into one sequential experiment.
- Describing all latency as GPU latency without the exact GPU/runtime.
- Hiding input-resolution differences.
- Treating current branch results as identical to an older paper release.
- Using a review article as evidence that official source code reproduced a result.
- Reporting a private or incomplete repository as publicly available.
