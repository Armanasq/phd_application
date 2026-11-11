#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def generate(source_file: Path) -> str:
    claims = [json.loads(line) for line in source_file.read_text(encoding="utf-8").splitlines() if line.strip()]
    by_url = {}
    for claim in claims:
        by_url.setdefault(claim["source_url"], []).append(claim)
    out = []
    for url in sorted(by_url):
        items = by_url[url]
        dates = sorted(row["checked_on"] for row in items)
        record = {
            "source_id": "source:" + url,
            "canonical_url": url,
            "source_types": sorted({row["source_type"] for row in items}),
            "claim_ids": sorted(row["id"] for row in items),
            "claim_statuses": sorted({row["status"] for row in items}),
            "first_checked": dates[0],
            "last_checked": dates[-1],
            "independent_recheck": "NOT_PERFORMED",
        }
        out.append(json.dumps(record, ensure_ascii=False, separators=(",", ":")))
    return "\n".join(out) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=ROOT/"data"/"claim_register.jsonl")
    parser.add_argument("--output", type=Path, default=ROOT/"data"/"sources.jsonl")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = generate(args.input)
    if args.check:
        if args.output.read_text(encoding="utf-8") != data:
            raise SystemExit("FAIL: source ledger is stale relative to claim register")
        print("PASS: source ledger generated from claim register")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data, encoding="utf-8")
        print(args.output)


if __name__ == "__main__":
    main()
