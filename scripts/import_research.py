#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from hashlib import sha256
import json
from pathlib import Path
import sqlite3
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
COUNTRIES = {
    "Canada": "ca",
    "United Kingdom": "gb",
    "Ireland": "ie",
    "Luxembourg": "lu",
    "Switzerland": "ch",
    "Norway": "no",
    "New Zealand": "nz",
    "Australia": "au",
}
STATUS_DB = {"open_verified", "rolling", "upcoming_confirmed", "verification_needed", "closed"}


class ImportErrorData(ValueError):
    pass


def stable_id(prefix: str, value: str) -> str:
    return prefix + sha256(value.encode("utf-8")).hexdigest()[:24]


def read_csv(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def read_jsonl(name: str) -> list[dict]:
    with (DATA / name).open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream if line.strip()]


def valid_url(url: str) -> str:
    parsed = urlsplit(url)
    if parsed.scheme != "https" or not parsed.hostname:
        raise ImportErrorData(f"Source URL not canonical HTTPS: {url[:100]}")
    return url


def prepare(db: sqlite3.Connection) -> None:
    db.execute("PRAGMA foreign_keys = ON")
    db.executescript((ROOT / "sql" / "schema.sql").read_text(encoding="utf-8"))
    for path in sorted((ROOT / "sql" / "migrations").glob("*.sql")):
        db.executescript(path.read_text(encoding="utf-8"))


def source(db: sqlite3.Connection, url: str, source_type: str, checked_on: str) -> str:
    valid_url(url)
    sid = stable_id("src:", url)
    db.execute(
        "INSERT INTO sources(id,canonical_url,source_type,checked_on,review_status) VALUES(?,?,?,?,?) "
        "ON CONFLICT(canonical_url) DO UPDATE SET checked_on=excluded.checked_on",
        (sid, url, source_type or "UNKNOWN", checked_on, "SOURCE_RECORDED_NOT_INDEPENDENTLY_RECHECKED"),
    )
    return sid


def repo_node(db: sqlite3.Connection, full_name: str, state: str, category: str = "") -> str:
    if full_name.count("/") != 1 or not all(full_name.split("/")):
        raise ImportErrorData(f"Invalid repository identity: {full_name!r}")
    key = full_name.casefold()
    owner, name = full_name.split("/", 1)
    db.execute(
        "INSERT INTO research_repositories(repository_key,canonical_url,owner,name,category,current_screening_state) "
        "VALUES(?,?,?,?,?,?) ON CONFLICT(repository_key) DO UPDATE SET "
        "category=COALESCE(NULLIF(excluded.category,''),research_repositories.category),"
        "current_screening_state=excluded.current_screening_state",
        (key, f"https://github.com/{full_name}", owner, name, category or None, state),
    )
    return key


def import_records(db: sqlite3.Connection) -> dict[str, int]:
    counts: dict[str, int] = {}
    candidates = read_csv("github_discovery_candidates.csv")
    reviews = read_csv("repositories.csv")
    relations = read_csv("repository_relations.csv")
    claims = read_jsonl("claim_register.jsonl")
    opportunities = read_csv("opportunities.csv")
    assessments = {row["opportunity_id"]: row for row in read_csv("opportunity_assessments.csv")}
    experiences = read_jsonl("applicant_experiences.jsonl")
    for country, code in COUNTRIES.items():
        db.execute("INSERT INTO countries(id,name) VALUES(?,?) ON CONFLICT(id) DO UPDATE SET name=excluded.name", (code, country))
    counts["countries"] = len(COUNTRIES)

    for row in candidates:
        repo_node(db, row["repository"], row["screening_state"])
    counts["candidate_repositories"] = len(candidates)
    for row in reviews:
        key = repo_node(db, row["repository"], "REVIEW_RECORDED", row["category"])
        review_path = row["deep_review_path"] or row["review_path"]
        aid = stable_id("audit:", f"{key}\x00{row['snapshot_sha']}\x00{row['checked_on']}")
        db.execute(
            "INSERT INTO repository_audits(id,repository_key,snapshot_sha,checked_on,review_state,review_path,empirical_execution) "
            "VALUES(?,?,?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET "
            "review_state=excluded.review_state,review_path=excluded.review_path",
            (aid, key, row["snapshot_sha"], row["checked_on"], row["review_state"], review_path, "NOT_TESTED"),
        )
    counts["repo_audits"] = len(reviews)

    extra = set()
    relation_types = {"DERIVED_FROM": "DERIVED_FROM", "SHARES_DATA_ORIGIN": "REUSES_DATA", "SHARES_ORIGINAL_ADMISSIONS_GUIDES": "SHARES_SOURCE"}
    for row in relations:
        src, dest = row["source_repo"], row["destination_repo"]
        for name in (src, dest):
            key = name.casefold()
            if not any(candidate["repository"].casefold() == key for candidate in candidates):
                repo_node(db, name, "UNTRIAGED")
                extra.add(key)
        relation = relation_types.get(row["relation"])
        if not relation:
            raise ImportErrorData(f"Unrecognized repo relation: {row['relation']}")
        db.execute(
            "INSERT INTO repository_relations(source_repo_key,destination_repo_key,relation_type,evidence_url,checked_on) "
            "VALUES(?,?,?,?,?) ON CONFLICT(source_repo_key,destination_repo_key,relation_type) DO UPDATE SET "
            "evidence_url=excluded.evidence_url,checked_on=excluded.checked_on",
            (src.casefold(), dest.casefold(), relation, valid_url(row["source_evidence_url"]), row["checked_on"]),
        )
    counts["repo_relations"] = len(relations)
    counts["relation_only_reference_nodes"] = len(extra)

    for row in claims:
        sid = source(db, row["source_url"], row["source_type"], row["checked_on"])
        db.execute(
            "INSERT INTO claim_register(id,subject,predicate,value_text,status,checked_on,decision_effect,uncertainty) "
            "VALUES(?,?,?,?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET "
            "subject=excluded.subject,value_text=excluded.value_text,status=excluded.status,"
            "checked_on=excluded.checked_on,decision_effect=excluded.decision_effect",
            (row["id"], row["subject"], None, str(row["value"]), row["status"], row["checked_on"], row.get("consequence"), "NO_INDEPENDENT_SEMANTIC_RECHECK"),
        )
        db.execute(
            "INSERT INTO claim_sources(claim_id,source_id,source_role,retrieval_status) VALUES(?,?,?,?) "
            "ON CONFLICT(claim_id,source_id) DO UPDATE SET source_role=excluded.source_role",
            (row["id"], sid, "SUPPORTS", "CLAIM_SOURCE_RECORDED"),
        )
    counts["claims"] = len(claims)

    if set(row["id"] for row in opportunities) != set(assessments):
        raise ImportErrorData("Missing, extra or duplicate opportunity assessments")
    for row in opportunities:
        country = COUNTRIES.get(row["country"])
        if not country:
            raise ImportErrorData(f"Unknown country: {row['country']}")
        institution_id = stable_id("inst:", country + "\x00" + row["institution"].strip().casefold())
        db.execute(
            "INSERT INTO institutions(id,country_id,name) VALUES(?,?,?) ON CONFLICT(id) DO UPDATE SET name=excluded.name",
            (institution_id, country, row["institution"]),
        )
        sid = source(db, row["url"], "OPPORTUNITY_OR_PROGRAM", row["verified_on"])
        status = row["status"]
        if status == "expired":
            status = "closed"
        if status not in STATUS_DB:
            raise ImportErrorData(f"Unknown opportunity status for {row['id']}: {status}")
        db.execute(
            "INSERT INTO opportunities(id,institution_id,source_id,title,kind,deadline_local,deadline_timezone,start_date,decision_date,tuition_coverage,status) "
            "VALUES(?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET "
            "source_id=excluded.source_id,title=excluded.title,kind=excluded.kind,"
            "deadline_local=excluded.deadline_local,deadline_timezone=excluded.deadline_timezone,"
            "start_date=excluded.start_date,decision_date=excluded.decision_date,"
            "tuition_coverage=excluded.tuition_coverage,status=excluded.status",
            (row["id"], institution_id, sid, row["title"], row["type"], row.get("deadline_local") or None,
             row.get("timezone") or None, row.get("start_date") or None, row.get("decision_date") or None,
             row.get("international_fee_status") or None, status),
        )
        assessment = assessments[row["id"]]
        db.execute(
            "INSERT INTO opportunity_verification(opportunity_id,verified_on,application_channel_status,"
            "individual_funding_status,international_tuition_status,offer_date_evidence,salary_or_stipend_terms,"
            "employer_status_discrepancy,action_blockers,source_id) "
            "VALUES(?,?,?,?,?,?,?,?,?,?) ON CONFLICT(opportunity_id) DO UPDATE SET "
            "verified_on=excluded.verified_on,application_channel_status=excluded.application_channel_status,"
            "individual_funding_status=excluded.individual_funding_status,"
            "international_tuition_status=excluded.international_tuition_status,"
            "offer_date_evidence=excluded.offer_date_evidence,salary_or_stipend_terms=excluded.salary_or_stipend_terms,"
            "employer_status_discrepancy=excluded.employer_status_discrepancy,"
            "action_blockers=excluded.action_blockers,source_id=excluded.source_id",
            (row["id"], row["verified_on"], row["status"], row["funding_verification"], row["international_fee_status"],
             row["offer_before_2027"], row["funding"], row.get("status_discrepancy"),
             assessment.get("risk"), sid),
        )
    counts["opportunities"] = len(opportunities)

    for row in experiences:
        geographic = row.get("geography", "").casefold()
        country = "gb" if ("united kingdom" in geographic or "uk" in geographic) else "no" if "norway" in geographic else None
        db.execute(
            "INSERT INTO applicant_experience_cases(id,source_url,posted_on,country_id,observed_process,evidence_class,survivorship_risk,external_recheck) "
            "VALUES(?,?,?,?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET "
            "source_url=excluded.source_url,posted_on=excluded.posted_on,country_id=excluded.country_id,"
            "observed_process=excluded.observed_process,evidence_class=excluded.evidence_class,"
            "survivorship_risk=excluded.survivorship_risk",
            (row["case_id"], valid_url(row["source"]), row["date"], country, row["finding"],
             row["confidence"], row.get("bias"), "NOT_INDEPENDENTLY_VERIFIED"),
        )
    counts["applicant_cases"] = len(experiences)

    publication_claim = next((x for x in claims if x["id"] == "CV001"), None)
    if publication_claim:
        sid = source(db, publication_claim["source_url"], publication_claim["source_type"], publication_claim["checked_on"])
        db.execute(
            "INSERT INTO research_publications(id,title,year,doi,publication_state,source_id) VALUES(?,?,?,?,?,?) "
            "ON CONFLICT(id) DO UPDATE SET source_id=excluded.source_id",
            ("pub:measurement-2023-113105",
             "Generalizable end-to-end deep learning frameworks for real-time attitude estimation using 6DoF inertial measurement units",
             2023, "10.1016/j.measurement.2023.113105", "PEER_REVIEWED", sid),
        )
        counts["verified_publication_records"] = 1
    return counts


def run(db: sqlite3.Connection) -> dict[str, int]:
    prepare(db)
    with db:
        stats = import_records(db)
        if db.execute("PRAGMA foreign_key_check").fetchall():
            raise ImportErrorData("Foreign key verification failure")
        if db.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            raise ImportErrorData("SQLite integrity verification failure")
    return stats


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, default=ROOT/".local"/"phd_intelligence.sqlite")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.dry_run:
        with sqlite3.connect(":memory:") as db:
            counts = run(db)
    else:
        args.db.parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(args.db) as db:
            counts = run(db)
    print(json.dumps({"success": True, "dry_run": args.dry_run, "counts": counts}, sort_keys=True))


if __name__ == "__main__":
    main()
