#!/usr/bin/env python3
"""Validate a compact manuscript-support release without source images."""

from __future__ import annotations

import argparse
import gzip
import json
from pathlib import Path

import pandas as pd


def read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def is_gzip(path: Path) -> bool:
    with path.open("rb") as handle:
        return handle.read(2) == b"\x1f\x8b"


def validate_status(path: Path) -> list[str]:
    errors: list[str] = []
    status = read_json(path)
    for field in ("run_complete", "validation_passed"):
        if status.get(field) is not True:
            errors.append(f"{path}: {field} is not true")
    if status.get("clinical_validation_claim_authorized") is True:
        errors.append(f"{path}: unexpected clinical-validation authorization")
    return errors


def validate_table(path: Path) -> list[str]:
    errors: list[str] = []
    if path.name.endswith(".csv.gz") and not is_gzip(path):
        return [f"{path}: .csv.gz extension does not contain gzip bytes"]
    try:
        frame = pd.read_csv(path, low_memory=False)
    except Exception as exc:
        return [f"{path}: unreadable table: {exc}"]
    if frame.empty:
        errors.append(f"{path}: empty table")
    if frame.columns.duplicated().any():
        errors.append(f"{path}: duplicated column names")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []

    statuses = sorted(root.rglob("final_status.json"))
    if not statuses:
        errors.append("No final_status.json files were found.")
    for path in statuses:
        errors.extend(validate_status(path))

    tables = sorted({*root.rglob("*.csv"), *root.rglob("*.csv.gz")})
    for path in tables:
        errors.extend(validate_table(path))

    if errors:
        print("RELEASE VALIDATION FAILED")
        for error in errors:
            print(" -", error)
        return 1

    print("RELEASE VALIDATION PASSED")
    print(f"Validated {len(statuses)} status files and {len(tables)} tables.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

