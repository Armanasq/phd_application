#!/usr/bin/env python3
import argparse
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "repositories.csv"
INDEX = ROOT / "research" / "repositories" / "index.md"

def generate():
    with CATALOG.open(newline="", encoding="utf-8") as stream:
        rows = sorted(csv.DictReader(stream), key=lambda row: row["repository"].casefold())
    lines = [
        "# Global GitHub research corpus — review state index",
        "",
        "Source: `data/repositories.csv`. Generated deterministically; do not edit directly.",
        "",
        f"**Rows:** {len(rows)}. Only entries explicitly labeled `DEEP_REVIEW_DOCUMENTED` have the structured eight-part analysis. Other rows are bounded preliminary notes, not final exhaustive reviews.",
        "",
        "| Repository | Category | Review state | Evidence record |",
        "|---|---|---|---|",
    ]
    for row in rows:
        target = row["deep_review_path"] or row["review_path"]
        lines.append(f"| [{row['repository']}]({row['url']}) | {row['category']} | {row['review_state']} | [Review](../../{target}) |")
    return "\n".join(lines) + "\n"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    output = generate()
    if args.check:
        assert INDEX.read_text(encoding="utf-8") == output, f"{INDEX}: index is stale"
        print("PASS: generated repository index matches catalog")
    else:
        INDEX.parent.mkdir(parents=True, exist_ok=True)
        INDEX.write_text(output, encoding="utf-8")
        print(str(INDEX))

if __name__ == "__main__":
    main()
