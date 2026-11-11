#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import time
from typing import Callable, Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MATRIX = ROOT / "data" / "discovery_query_matrix.csv"
DEFAULT_CANDIDATES = ROOT / "data" / "github_discovery_candidates.csv"
DEFAULT_LOG = ROOT / "data" / "discovery_log.jsonl"
COLUMNS = ("repository", "discovery_queries", "screening_state", "review_record", "discovered_on")


class DiscoveryFailure(RuntimeError):
    pass


def utc_date() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def parse_matrix(path: Path) -> list[str]:
    with path.open(encoding="utf-8", newline="") as handle:
        records = list(csv.DictReader(handle))
    queries = []
    for record in records:
        if record.get("channel") != "github_repo":
            continue
        value = (record.get("example_query") or "").strip()
        if value and value not in queries:
            queries.append(value)
    return queries


def read_candidates(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        if tuple(reader.fieldnames or ()) != COLUMNS:
            raise DiscoveryFailure("Candidate CSV schema mismatch")
        records = list(reader)
    output = {}
    for record in records:
        key = record["repository"].casefold()
        if key in output:
            raise DiscoveryFailure(f"Duplicate existing repository: {record['repository']}")
        output[key] = record
    return output


def merge_hits(records: dict[str, dict[str, str]], hits: list[dict[str, Any]], query: str, date: str) -> tuple[int, int]:
    new = 0
    duplicated = 0
    for hit in hits:
        name = hit.get("full_name")
        if not isinstance(name, str) or name.count("/") != 1 or not all(name.split("/")):
            continue
        key = name.casefold()
        if key in records:
            duplicated += 1
            current = records[key]
            found = current["discovery_queries"].split(" | ") if current["discovery_queries"] else []
            if query not in found:
                current["discovery_queries"] = " | ".join([*found, query])
        else:
            records[key] = {
                "repository": name,
                "discovery_queries": query,
                "screening_state": "UNTRIAGED",
                "review_record": "",
                "discovered_on": date,
            }
            new += 1
    return new, duplicated


def search_page(query: str, page: int, per_page: int) -> dict[str, Any]:
    encoded = urlencode({"q": query, "page": page, "per_page": per_page})
    url = "https://api.github.com/search/repositories?" + encoded
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "phd-application-research/1.0",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = "Bearer " + token
    for attempt in range(3):
        try:
            with urlopen(Request(url, headers=headers), timeout=20) as response:
                payload = json.load(response)
                if not isinstance(payload, dict):
                    raise DiscoveryFailure("Unexpected response envelope")
                return payload
        except HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 2:
                raise DiscoveryFailure(f"GitHub search HTTP {exc.code}") from None
            delay = min(8, 2 ** attempt)
            time.sleep(delay)
        except (URLError, TimeoutError) as exc:
            if attempt == 2:
                raise DiscoveryFailure(f"GitHub search transport failure: {type(exc).__name__}") from None
            time.sleep(min(8, 2 ** attempt))
    raise DiscoveryFailure("GitHub search did not return data")


def discover(queries: list[str], existing: dict[str, dict[str, str]], *, pages: int, per_page: int, fetcher: Callable[[str, int, int], dict[str, Any]] = search_page) -> tuple[dict[str, dict[str, str]], list[dict[str, Any]], bool]:
    date = utc_date()
    log = []
    incomplete = False
    for query in queries:
        for page in range(1, pages + 1):
            event: dict[str, Any] = {
                "date": date,
                "channel": "github_repo_rest",
                "query": query,
                "page": page,
                "requested_per_page": per_page,
                "status": "error",
            }
            try:
                result = fetcher(query, page, per_page)
                items = result.get("items")
                if not isinstance(items, list):
                    raise DiscoveryFailure("Missing repository items array")
                new, duplicated = merge_hits(existing, items, query, date)
                event.update({
                    "status": "ok",
                    "returned": len(items),
                    "new_unique": new,
                    "existing_duplicates": duplicated,
                    "api_total_count": result.get("total_count"),
                    "api_incomplete_results": bool(result.get("incomplete_results", False)),
                })
                if result.get("incomplete_results"):
                    incomplete = True
                log.append(event)
                if len(items) < per_page:
                    break
            except (DiscoveryFailure, ValueError, TypeError) as exc:
                event["error"] = str(exc)[:280]
                log.append(event)
                incomplete = True
                break
    return existing, log, incomplete


def write_candidates(path: Path, records: dict[str, dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    try:
        with temporary.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=COLUMNS, quoting=csv.QUOTE_ALL)
            writer.writeheader()
            writer.writerows(sorted(records.values(), key=lambda x: x["repository"].casefold()))
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def append_log(path: Path, events: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as stream:
        for event in events:
            stream.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--matrix", type=Path, default=DEFAULT_MATRIX)
    p.add_argument("--candidates", type=Path, default=DEFAULT_CANDIDATES)
    p.add_argument("--log", type=Path, default=DEFAULT_LOG)
    p.add_argument("--max-pages", type=int, default=2)
    p.add_argument("--per-page", type=int, default=50)
    p.add_argument("--query", action="append", default=[])
    p.add_argument("--write", action="store_true")
    a = p.parse_args()
    if not 1 <= a.max_pages <= 10 or not 1 <= a.per_page <= 100:
        p.error("max-pages must be 1..10 and per-page 1..100")
    queries = list(dict.fromkeys(a.query or parse_matrix(a.matrix)))
    if not queries:
        p.error("no queries discovered")
    existing = read_candidates(a.candidates)
    records, events, incomplete = discover(queries, existing, pages=a.max_pages, per_page=a.per_page)
    print(json.dumps({"queries": len(queries), "pages": len(events), "candidates": len(records), "new_unique": sum(x.get("new_unique", 0) for x in events), "incomplete": incomplete, "write": a.write}, sort_keys=True))
    if a.write:
        write_candidates(a.candidates, records)
        append_log(a.log, events)
    if incomplete:
        raise SystemExit("INCOMPLETE: errors/incomplete API results recorded; review log before using candidates")


if __name__ == "__main__":
    main()
