# Relational evidence and application architecture (2026-11-11)

## Storage boundaries
- **Version-controlled public:** source metadata, formal method, redacted original research, canonical URLs, public GitHub snapshots, verified opportunity descriptions, non-sensitive record IDs.
- **Private local database:** applicant documents, grades, nationality, contact information, correspondence, authentication and action receipts. The public repository has *no* real applicant accounts or secrets.
- **Untrusted input:** scraped web/admissions text and LLM suggestions remain tentative until recorded claim-level verification. Never send external email just because a model drafted one.

## Schema and migrations
The original tables in [schema.sql](../../sql/schema.sql) remain supported. [001_research_evidence.sql](../../sql/migrations/001_research_evidence.sql) adds:
```text
research_repositories 1---N repository_audits 1---N repository_findings
research_repositories N---N research_repositories (repository_relations)
sources N---N claim_register (claim_sources)
supervisors N---N research_publications (supervisor_publications)
opportunities 1---1 opportunity_verification
applications 1---N communication_actions
countries 1---N applicant_experience_cases
recorded_discovery_searches
```
SQLite migrations are additive with `CREATE TABLE IF NOT EXISTS` and retain previous production content; bootstrap applies sorted migrations. Runtime supports SQLite's foreign-key and CHECK constraints. Application status `ACCEPTED` is blocked without an evidence-backed `ACCEPTANCE_RECEIPT` event. Sending correspondence requires authorization metadata and delivery proof. These are **data integrity guards**, not a complete authorization service; an app must still cryptographically authenticate the user, store permission scope, and validate transitions.

## Evidence modeling
A repository review is identified by canonical repository key, snapshot revision, check date, document path and observed execution level. Claim rows link *multiple* original sources; each edge records support, contradiction or discovery-only. A claim is only corroborated if independent sources genuinely support it; two mirrors of the same original are dependent evidence.

## Opportunity classification
An `open_verified` status means the specific application portal is open **according to its source at check time**. It does **not** imply the individual has the funded award, meets requirements or will receive an offer. A separate opportunity verification records funding security, international fee exposure, offer-date evidence and live-state conflict. ETH RobotX has an official Nov27 deadline but February2027 final decision schedule; UZH RPG Oct27 cutoff has possible continued screening, so portal capacity remains blocked.

## Implementation posture
Migration 001 is new and import/export scripts are incremental. CSVs remain reviewed source inventories, not a synchronized materialized database. No auto-enrollment of applicants or posting personal credentials. Transactionally import through a future explicit ETL that retains original evidence snapshots and import reports.

## Reproducibility
```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/bootstrap.py --db .local/phd_intelligence.sqlite
python3 scripts/validate_sources.py
```
`PRAGMA foreign_key_check` and migration idempotence are covered by tests. A passing SQLite migration does not establish factual correctness of university rules.
