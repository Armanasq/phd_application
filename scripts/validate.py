#!/usr/bin/env python3
import csv
import pathlib
import re
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
EXPECTED = {
    "opportunities.csv": {"id", "country", "institution", "title", "type", "deadline_local", "timezone", "status", "funding", "url", "verified_on"},
    "repositories.csv": {"repository", "category", "inspection_level", "verdict", "url", "checked_on", "snapshot_sha", "review_path"},
    "github_discovery_candidates.csv": {"repository", "discovery_queries", "screening_state", "review_record", "discovered_on"},
    "github_search_log.csv": {"date", "surface", "query", "page", "returned_count", "new_unique_records"},
    "evidence.csv": {"claim_id", "claim", "source_url", "checked_on", "status"},
    "search_log.csv": {"date", "surface", "query_group", "status"},
}
def validate_csv(name, columns):
    with (DATA / name).open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        missing = columns - set(reader.fieldnames or [])
        assert not missing, f"{name}: missing columns {sorted(missing)}"
        rows = list(reader)
        for number, row in enumerate(rows, 2):
            assert None not in row, f"{name}:{number}: extra columns"
            assert all(k is not None for k in row), f"{name}:{number}: missing value"
        return rows
def validate_repositories(tables):
    reviews = tables["repositories.csv"]
    discovered = tables["github_discovery_candidates.csv"]
    repo_names = [r["repository"].casefold() for r in reviews]
    candidate_names = [r["repository"].casefold() for r in discovered]
    assert len(repo_names) == len(set(repo_names)), "duplicate reviewed repository"
    assert len(candidate_names) == len(set(candidate_names)), "duplicate discovery candidate"
    candidates = {r["repository"].casefold(): r for r in discovered}
    for r in reviews:
        key = r["repository"].casefold()
        assert key in candidates, f"reviewed repo absent from discovery: {key}"
        assert r["url"].lower() == "https://github.com/" + key
        assert re.fullmatch("[0-9a-f]{40}", r["snapshot_sha"]), f"bad snapshot SHA: {key}"
        expected = "docs/github/reviews/" + key.replace("/", "--") + ".md"
        assert r["review_path"] == expected, f"review path mismatch: {key}"
        assert (ROOT / r["review_path"]).is_file(), f"missing review record: {key}"
        assert candidates[key]["screening_state"] == "REVIEW_RECORDED", key
        assert candidates[key]["review_record"] == expected, key
    for c in discovered:
        if c["screening_state"] == "REVIEW_RECORDED":
            assert c["repository"].casefold() in set(repo_names), c["repository"]
        else:
            assert c["screening_state"] == "UNTRIAGED", c["repository"]
            assert not c["review_record"], c["repository"]
    assert len(tables["github_search_log.csv"]) >= 1
def main():
    tables = {name: validate_csv(name, cols) for name, cols in EXPECTED.items()}
    opportunities = tables["opportunities.csv"]
    ids = [r["id"] for r in opportunities]
    assert len(ids) == len(set(ids)), "duplicate opportunity IDs"
    assert {r["country"] for r in opportunities} <= {"Canada", "United Kingdom", "Ireland", "Luxembourg", "Switzerland", "Norway", "New Zealand", "Australia"}
    assert all(r["url"].startswith("https://") and r["verified_on"] for r in opportunities)
    validate_repositories(tables)
    for slug in ["canada","united-kingdom","ireland","luxembourg","switzerland","norway","new-zealand","australia"]:
        assert (ROOT/"docs"/"countries"/f"{slug}.md").is_file(), slug
    with sqlite3.connect(":memory:") as db:
        db.executescript((ROOT / "sql" / "schema.sql").read_text(encoding="utf-8"))
        assert db.execute("PRAGMA foreign_key_check").fetchall() == []
    print(f"PASS: {len(opportunities)} opportunities; {len(tables['repositories.csv'])} reviews; {len(tables['github_discovery_candidates.csv'])} discovery candidates; 8 country dossiers")
if __name__ == "__main__":
    try:
        main()
    except (AssertionError, OSError, sqlite3.Error) as exc:
        sys.exit(f"FAIL: {exc}")
