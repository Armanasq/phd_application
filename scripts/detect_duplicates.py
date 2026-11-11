#!/usr/bin/env python3
import argparse
import csv
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def detect(path: Path) -> dict[str, object]:
    with path.open(newline="", encoding="utf-8") as stream:
        records = list(csv.DictReader(stream))
    seen: dict[str, int] = {}
    duplicate_ids = []
    by_basename: dict[str, set[str]] = {}
    for row_idx, row in enumerate(records, 2):
        name = (row.get("repository") or "").strip()
        canonical = name.casefold()
        if not name or name.count("/") != 1:
            duplicate_ids.append({"row": row_idx, "issue": "invalid_name", "repository": name})
            continue
        if canonical in seen:
            duplicate_ids.append({"row": row_idx, "first_row": seen[canonical], "issue": "duplicate_id", "repository": name})
        else:
            seen[canonical] = row_idx
        basename = name.split("/")[1].casefold().replace("_", "-")
        by_basename.setdefault(basename, set()).add(name)
    possible_derivatives = [{"repository_name": stem, "names": sorted(names)} for stem, names in by_basename.items() if len(names) > 1]
    return {"records": len(records), "canonical_duplicates": duplicate_ids, "potential_derivatives_unverified": possible_derivatives}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=ROOT / "data" / "github_discovery_candidates.csv")
    parser.add_argument("--fail-on-duplicates", action="store_true")
    args = parser.parse_args()
    result = detect(args.input)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if result["canonical_duplicates"] and args.fail_on_duplicates:
        sys.exit(1)


if __name__ == "__main__":
    main()
