#!/usr/bin/env python3
import csv
import json
import pathlib
import re
import sqlite3
import sys
from urllib.parse import urlsplit

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
EXPECTED = {
    "opportunities.csv": {"id", "country", "institution", "title", "type", "deadline_local", "timezone", "status", "funding", "url", "verified_on", "funding_verification", "international_fee_status", "offer_before_2027"},
    "opportunity_assessments.csv": {"opportunity_id", "funding_gate", "verification_state", "target_portfolio", "official_source", "checked_on"},
    "application_readiness.csv": {"opportunity_id", "official_source_url", "funding_state", "readiness_state", "approval_status"},
    "repositories.csv": {"repository", "category", "inspection_level", "verdict", "url", "checked_on", "snapshot_sha", "review_path", "review_state", "deep_review_path"},
    "github_discovery_candidates.csv": {"repository", "discovery_queries", "screening_state", "review_record", "discovered_on"},
    "github_search_log.csv": {"date", "surface", "query", "page", "returned_count", "new_unique_records"},
    "exclusions.csv": {"repository", "code", "rationale", "evidence_url", "screened_on"},
    "discovery_query_matrix.csv": {"family", "channel", "example_query", "status"},
    "evidence.csv": {"claim_id", "claim", "source_url", "checked_on", "status"},
    "search_log.csv": {"date", "surface", "query_group", "status"},
}
STATES = {"UNTRIAGED", "SCREENED_INCLUDE", "SCREENED_EXCLUDE", "REVIEW_RECORDED"}
REVIEW_STATES = {"PRELIMINARY_FOCUSED", "DEEP_REVIEW_DOCUMENTED", "INDEPENDENTLY_VALIDATED"}
COUNTRIES = {"Canada", "United Kingdom", "Ireland", "Luxembourg", "Switzerland", "Norway", "New Zealand", "Australia"}
OPPORTUNITY_STATES = {"open_verified", "rolling", "upcoming_confirmed", "verification_needed", "closed", "expired"}
DEEP_SECTIONS = tuple(f"## {index}" for index in range(1, 9))

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

def assert_https(value, label):
    url = urlsplit(value)
    assert url.scheme == "https" and bool(url.netloc), f"{label}: expected https canonical URL"

def validate_repositories(tables):
    reviews = tables["repositories.csv"]
    candidates = tables["github_discovery_candidates.csv"]
    by_name = {r["repository"].casefold(): r for r in candidates}
    names = [r["repository"].casefold() for r in candidates]
    assert len(names) == len(set(names)), "duplicate discovery candidates"
    reviewed_names = [r["repository"].casefold() for r in reviews]
    assert len(reviewed_names) == len(set(reviewed_names)), "duplicate reviewed repositories"
    for r in candidates:
        assert r["screening_state"] in STATES, f"invalid screening state: {r['repository']}"
        if r["screening_state"] not in {"REVIEW_RECORDED"}:
            assert not r["review_record"], f"review path without review status: {r['repository']}"
    deep_count = 0
    for r in reviews:
        key = r["repository"].casefold()
        assert key in by_name, f"reviewed repo missing from candidate queue: {key}"
        assert_https(r["url"], key)
        assert r["url"].lower() == f"https://github.com/{key}", key
        assert re.fullmatch(r"[a-f0-9]{40}", r["snapshot_sha"]), f"bad SHA: {key}"
        assert r["review_state"] in REVIEW_STATES, key
        assert by_name[key]["screening_state"] == "REVIEW_RECORDED", key
        relative = r["review_path"]
        assert relative.startswith(("docs/github/reviews/", "research/repositories/reviews/")), key
        assert (ROOT / relative).is_file(), f"review note missing: {relative}"
        assert by_name[key]["review_record"] == relative, key
        if r["review_state"] in {"DEEP_REVIEW_DOCUMENTED", "INDEPENDENTLY_VALIDATED"}:
            path = r["deep_review_path"]
            assert path.startswith("research/repositories/reviews/"), f"deep review path missing: {key}"
            assert (ROOT / path).is_file(), f"deep review missing: {key}"
            content = (ROOT / path).read_text(encoding="utf-8")
            headings = re.findall(r"^## (\d+)\b", content, re.MULTILINE)
            assert all(str(n) in headings for n in range(1, 9)), f"deep review sections missing: {key}"
            assert "github.com/" in content, f"deep review lacks source URLs: {key}"
            deep_count += 1
        else:
            assert not r["deep_review_path"], f"preliminary review has deep-review path: {key}"
    for r in candidates:
        if r["screening_state"] == "REVIEW_RECORDED":
            assert r["repository"].casefold() in set(reviewed_names), f"recorded review absent from catalog: {r['repository']}"
    excluded = {r["repository"].casefold() for r in tables["exclusions.csv"]}
    assert len(excluded) == len(tables["exclusions.csv"]), "duplicate exclusions"
    assert excluded.isdisjoint(reviewed_names), "included and excluded repository overlap"
    for r in tables["exclusions.csv"]:
        assert r["repository"].casefold() in by_name, f"exclusion not in queue: {r['repository']}"
        assert by_name[r["repository"].casefold()]["screening_state"] == "SCREENED_EXCLUDE", r["repository"]
        assert r["code"] and r["rationale"], r["repository"]
        assert_https(r["evidence_url"], r["repository"])
    return deep_count

def validate_opportunities(tables):
    rows = tables["opportunities.csv"]
    ids = [r["id"] for r in rows]
    assert len(ids) == len(set(ids)), "duplicate opportunity IDs"
    checked = tables["opportunity_assessments.csv"]
    assess_ids = [r["opportunity_id"] for r in checked]
    assert len(assess_ids) == len(set(assess_ids)), "duplicate opportunity assessments"
    assert set(ids) == set(assess_ids), "missing/detached opportunity assessment"
    ready = tables["application_readiness.csv"]
    ready_ids = [r["opportunity_id"] for r in ready]
    assert len(ready_ids) == len(set(ready_ids)), "duplicate readiness records"
    assert set(ready_ids) <= set(ids), "readiness references untracked opportunity"
    for record in ready:
        assert record["approval_status"] == "NOT_AUTHORIZED", "public readiness cannot record authorization"
        assert record["readiness_state"] not in {"SUBMITTED","SENT","ACCEPTED"}, "unproven external action"
        assert_https(record["official_source_url"], record["opportunity_id"])
    for r in rows:
        assert r["country"] in COUNTRIES, r["id"]
        assert r["status"] in OPPORTUNITY_STATES, r["id"]
        assert r["funding_verification"], r["id"]
        assert r["offer_before_2027"], r["id"]
        assert r["verified_on"], r["id"]
        assert_https(r["url"], r["id"])
        if r["id"] in {"usn-ai", "usn-systems", "eth-3d", "lux-sparc-radar"}:
            assert r["status"] == "verification_needed", "ambiguous jobs falsely verified open"
        if r["id"] == "oxford-cs":
            assert r["funding_verification"] == "COMPETITIVE_UNAWARDED", "Oxford scholarship cannot be guaranteed"
        if r["id"] == "reading-robotics-2027":
            assert "HOME_FEE" in r["funding_verification"], "Home-only eligibility gate missing"

def validate_jsonl(path, required):
    rows = []
    with (DATA / path).open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            item = json.loads(line)
            missing = set(required) - set(item)
            assert not missing, f"{path}:{line_number}: missing {missing}"
            rows.append(item)
    keys = [r[required[0]] for r in rows]
    assert len(keys) == len(set(keys)), f"{path}: duplicate ID"
    return rows

def main():
    tables = {name: validate_csv(name, cols) for name, cols in EXPECTED.items()}
    deep_count = validate_repositories(tables)
    validate_opportunities(tables)
    for slug in ["canada","united-kingdom","ireland","luxembourg","switzerland","norway","new-zealand","australia"]:
        path = ROOT/"docs"/"countries"/f"{slug}.md"
        assert path.is_file() and "http" in path.read_text(encoding="utf-8"), slug
    claims = validate_jsonl("claim_register.jsonl", ("id", "subject", "value", "source_url", "status", "checked_on"))
    ledger = validate_jsonl("sources.jsonl", ("source_id","canonical_url","claim_ids","claim_statuses","first_checked","last_checked","independent_recheck"))
    claim_ids = {r["id"] for r in claims}
    assert {url for row in ledger for url in [row["canonical_url"]]} == {r["source_url"] for r in claims}, "source ledger differs from claims"
    for source in ledger:
        assert set(source["claim_ids"]) <= claim_ids, source["source_id"]
        assert source["independent_recheck"] == "NOT_PERFORMED", "source ledger should not claim independent verification"
    experiences = validate_jsonl("applicant_experiences.jsonl", ("case_id", "date", "source", "finding", "confidence"))
    with sqlite3.connect(":memory:") as db:
        db.executescript((ROOT / "sql" / "schema.sql").read_text(encoding="utf-8"))
        for migration in sorted((ROOT / "sql" / "migrations").glob("*.sql")):
            db.executescript(migration.read_text(encoding="utf-8"))
        assert db.execute("PRAGMA foreign_key_check").fetchall() == []
    print(f"PASS: {len(tables['repositories.csv'])} reviewed repos ({deep_count} full-structured static reviews), {len(tables['github_discovery_candidates.csv'])} candidates, {len(tables['opportunities.csv'])} leads, {len(claims)} claim records, {len(experiences)} applicant cases; 8 country dossiers")

if __name__ == "__main__":
    try:
        main()
    except (AssertionError, OSError, sqlite3.Error, json.JSONDecodeError, ValueError, KeyError) as exc:
        sys.exit(f"FAIL: {exc}")
