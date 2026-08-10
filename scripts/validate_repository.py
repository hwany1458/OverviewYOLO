#!/usr/bin/env python3
"""Validate the public OverviewYOLO metadata package.

This script validates structure and provenance rules. It does not verify that
external benchmark claims are scientifically correct or that URLs are online.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []

EXPECTED_CORE = {
    "YOLOv1",
    "YOLOv2",
    "YOLOv3",
    "YOLOv4",
    "YOLOv5",
    "YOLOv6",
    "YOLOv7",
    "YOLOv8",
    "YOLOv9",
    "YOLOv10",
    "YOLO11",
    "YOLOv12",
    "YOLOv13",
    "YOLO26",
}
EVIDENCE_LABELS = {"SR-P", "SR-R", "IR", "AR", "SYN"}
COMPARABILITY_LABELS = {"C", "P", "NC"}
EVIDENCE_LEVELS = {"A", "B", "C", "D"}


def error(message: str) -> None:
    ERRORS.append(message)


def warning(message: str) -> None:
    WARNINGS.append(message)


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.is_file():
        error(f"Missing CSV: {path.relative_to(ROOT)}")
        return [], []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            error(f"CSV has no header: {path.relative_to(ROOT)}")
            return [], []
        return reader.fieldnames, list(reader)


def require_columns(path: Path, header: list[str], required: set[str]) -> None:
    missing = sorted(required.difference(header))
    if missing:
        error(f"{path.relative_to(ROOT)} missing columns: {', '.join(missing)}")


def valid_http_url(value: str) -> bool:
    return value.startswith("https://") or value.startswith("http://")


def validate_core_versions() -> None:
    path = ROOT / "data" / "core_versions.csv"
    header, rows = read_csv(path)
    required = {
        "version",
        "official_name",
        "primary_source_type",
        "evidence_level",
        "primary_url",
        "official_code_url",
        "evidence_status",
    }
    require_columns(path, header, required)
    if not rows:
        return
    versions = {row.get("version", "") for row in rows}
    if versions != EXPECTED_CORE:
        error(
            "Core-version set mismatch; missing="
            f"{sorted(EXPECTED_CORE - versions)}, extra={sorted(versions - EXPECTED_CORE)}"
        )
    for line, row in enumerate(rows, start=2):
        if row.get("evidence_level") not in EVIDENCE_LEVELS:
            error(f"core_versions.csv:{line} invalid evidence_level")
        for field in ("primary_url", "official_code_url"):
            value = row.get(field, "")
            if value and not valid_http_url(value):
                error(f"core_versions.csv:{line} invalid URL in {field}: {value}")
        if row.get("version") in {"YOLOv5", "YOLOv8", "YOLO11"}:
            source_type = row.get("primary_source_type", "").lower()
            if "software" not in source_type:
                error(f"core_versions.csv:{line} software-only release mislabeled")


def validate_source_ledger() -> None:
    path = ROOT / "data" / "source_ledger.csv"
    header, rows = read_csv(path)
    required = {
        "source_id",
        "version",
        "source_type",
        "evidence_label",
        "evidence_level",
        "title",
        "primary_url",
        "accessed_on",
        "verification_status",
    }
    require_columns(path, header, required)
    seen: set[str] = set()
    for line, row in enumerate(rows, start=2):
        source_id = row.get("source_id", "")
        if not source_id:
            error(f"source_ledger.csv:{line} blank source_id")
        elif source_id in seen:
            error(f"source_ledger.csv:{line} duplicate source_id {source_id}")
        seen.add(source_id)
        if row.get("evidence_label") not in EVIDENCE_LABELS:
            error(f"source_ledger.csv:{line} invalid evidence_label")
        if row.get("evidence_level") not in EVIDENCE_LEVELS:
            error(f"source_ledger.csv:{line} invalid evidence_level")
        if not valid_http_url(row.get("primary_url", "")):
            error(f"source_ledger.csv:{line} invalid primary_url")
        if row.get("verification_status") not in {"verified", "pending", "retracted"}:
            error(f"source_ledger.csv:{line} invalid verification_status")


def validate_benchmark_rows() -> None:
    path = ROOT / "data" / "benchmark_results_template.csv"
    header, rows = read_csv(path)
    required = {
        "result_id",
        "model_version",
        "metric_name",
        "metric_value",
        "source_id",
        "evidence_label",
        "comparability_label",
        "delta_value",
        "run_manifest_path",
        "raw_output_path",
    }
    require_columns(path, header, required)
    seen: set[str] = set()
    for line, row in enumerate(rows, start=2):
        result_id = row.get("result_id", "")
        if not result_id:
            error(f"benchmark_results_template.csv:{line} blank result_id")
        elif result_id in seen:
            error(f"benchmark_results_template.csv:{line} duplicate result_id")
        seen.add(result_id)
        evidence = row.get("evidence_label", "")
        comparison = row.get("comparability_label", "")
        if evidence not in EVIDENCE_LABELS:
            error(f"benchmark_results_template.csv:{line} invalid evidence_label")
        if comparison not in COMPARABILITY_LABELS:
            error(f"benchmark_results_template.csv:{line} invalid comparability_label")
        if comparison in {"P", "NC"} and row.get("delta_value", "").strip():
            error(f"benchmark_results_template.csv:{line} delta forbidden for {comparison}")
        if evidence == "AR":
            if not row.get("run_manifest_path", "").strip():
                error(f"benchmark_results_template.csv:{line} AR row missing run_manifest_path")
            if not row.get("raw_output_path", "").strip():
                error(f"benchmark_results_template.csv:{line} AR row missing raw_output_path")


def validate_bibtex() -> None:
    path = ROOT / "references" / "yolo_core.bib"
    if not path.is_file():
        error("Missing references/yolo_core.bib")
        return
    text = path.read_text(encoding="utf-8")
    keys = re.findall(r"@[A-Za-z]+\s*\{\s*([^,\s]+)", text)
    duplicates = sorted({key for key in keys if keys.count(key) > 1})
    if duplicates:
        error(f"Duplicate BibTeX keys: {', '.join(duplicates)}")
    if "<verified" in text or "<real DOI" in text:
        error("Placeholder found in core BibTeX library")


def validate_local_markdown_links() -> None:
    pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for target in pattern.findall(text):
            target = target.split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                warning(f"Link leaves repository: {path.relative_to(ROOT)} -> {target}")
                continue
            if not resolved.exists():
                error(f"Broken local link: {path.relative_to(ROOT)} -> {target}")


def validate_required_files() -> None:
    required = [
        "README.md",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "LICENSE_GUIDANCE.md",
        "configs/benchmark_protocol.yaml",
        "data/run_manifest_template.csv",
        "docs/01_CORE_PAPERS.md",
        "docs/02_OFFICIAL_CODE_AND_MODELS.md",
        "docs/03_EXPERIMENTS_AND_BENCHMARKS.md",
        "docs/04_EVIDENCE_AND_COMPARABILITY.md",
        "docs/05_PUBLIC_RELEASE_CHECKLIST.md",
        "docs/06_MANUSCRIPT_TRACEABILITY.md",
        "docs/07_REPOSITORY_UPLOAD_GUIDE_KO.md",
        "experiments/README.md",
        "scripts/clone_official_sources.sh",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            error(f"Missing required file: {relative}")


def main() -> int:
    validate_required_files()
    validate_core_versions()
    validate_source_ledger()
    validate_benchmark_rows()
    validate_bibtex()
    validate_local_markdown_links()

    for message in WARNINGS:
        print(f"WARNING: {message}")
    for message in ERRORS:
        print(f"ERROR: {message}")

    if ERRORS:
        print(f"Validation failed with {len(ERRORS)} error(s) and {len(WARNINGS)} warning(s).")
        return 1
    print(f"Validation passed with {len(WARNINGS)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
