#!/usr/bin/env python3
import csv
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
EXPECTED = {
    "opportunities.csv": {"id", "country", "institution", "title", "type", "deadline_local", "timezone", "status", "funding", "url", "verified_on"},
    "repositories.csv": {"repository", "category", "inspection_level", "verdict", "url", "checked_on"},
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
def main():
    tables = {name: validate_csv(name, cols) for name, cols in EXPECTED.items()}
    opportunities = tables["opportunities.csv"]
    ids = [r["id"] for r in opportunities]
    assert len(ids) == len(set(ids)), "duplicate opportunity IDs"
    assert {r["country"] for r in opportunities} <= {"Canada", "United Kingdom", "Ireland", "Luxembourg", "Switzerland", "Norway", "New Zealand", "Australia"}
    assert all(r["url"].startswith("https://") and r["verified_on"] for r in opportunities)
    assert len({r["repository"] for r in tables["repositories.csv"]}) == len(tables["repositories.csv"])
    for slug in ["canada","united-kingdom","ireland","luxembourg","switzerland","norway","new-zealand","australia"]:
        assert (ROOT/"docs"/"countries"/f"{slug}.md").is_file(), slug
    with sqlite3.connect(":memory:") as db:
        db.executescript((ROOT / "sql" / "schema.sql").read_text(encoding="utf-8"))
        assert db.execute("PRAGMA foreign_key_check").fetchall() == []
    print(f"PASS: {len(opportunities)} opportunities, {len(tables['repositories.csv'])} repositories, 8 dossiers, SQL schema")
if __name__ == "__main__":
    try:
        main()
    except (AssertionError, OSError, sqlite3.Error) as exc:
        sys.exit(f"FAIL: {exc}")
