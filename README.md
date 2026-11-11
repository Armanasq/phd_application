# PhD Admissions Intelligence & Execution

**Research baseline:** 2026-11-11 · **Status:** initial evidence-backed research infrastructure, not a completed worldwide search.

A local-first, source-auditable research workspace for a fully funded PhD campaign across Canada, the United Kingdom, Ireland, Luxembourg, Switzerland, Norway, New Zealand, and Australia. Focus: robotics, state estimation, autonomous systems, navigation, perception, and AI. The **admissions campaign** and **research intelligence process** are separate workflows.

## Read first

- [Executive strategy](docs/strategy/executive-2026-2027.md): immediate deadlines and 2027 parallel route.
- [Country dossiers](docs/countries/README.md): eight independently maintained country assessments.
- [Opportunity tracker](data/opportunities.csv): official source, verification state, deadline, funding, research fit and next action. An admission program is not automatically a funded opening.
- [GitHub discovery inventory](data/repositories.csv) and [audit index](docs/github/README.md): screened resources, inspection level and provenance.
- [Research protocol](docs/methodology/research-protocol.md) and [search log](data/search_log.csv).
- [Entity and evidence design](docs/architecture/data-model.md): a durable relational data model with source/claim lineage.
- [Execution playbook](docs/operations/application-playbook.md): practical application workflow.
- [Baseline and gaps](docs/candidate/profile.md): self-reported facts separated from formal verification.

## Architecture

```text
docs/
  architecture/     relational design, states, privacy
  candidate/        evidence-gated applicant baseline
  countries/        independent country dossiers
  github/           audit methods and qualified repository reviews
  methodology/      verification, discovery and decision framework
  operations/       application, outreach and document workflows
  strategy/         near-term and 2027 portfolios
data/               UTF-8 CSV system-of-record seeds and evidence register
sql/                normalized SQLite schema
scripts/            stdlib-only validation and local database bootstrap
tests/              data integrity and workflow checks
.github/workflows/  validation CI
```

All publicly committed records must omit private documents, IDs, sensitive residence/citizenship information, email correspondence and API credentials. Keep personal application materials in private storage. Machine-readable CSV is a **reviewed seed dataset**, not an automated live feed.

## Non-negotiable semantics

- **Date fields are distinct:** application deadline, decision date, enrollment and funding start.
- **Funding:** confirmed full, partial, conditional, not evidenced; full funding requires tuition + sustainable living support.
- **Opportunity status:** verified open, published recurring channel, upcoming confirmed, verification needed, closed.
- **Research status is not submission status.** No application/contact/offer is considered completed without documentary evidence.
- **Sources:** official current rules override old third-party advice; every high-impact claim retains an inspectable source link and check date.
- **Uncertainty:** UNKNOWN is preferable to inferred personal eligibility or invented admissions probabilities.
- **Risk control:** deadlines and advertised jobs should be manually rechecked on the official site before taking action.

## Local workflow

```sh
python3 scripts/validate.py
python3 scripts/bootstrap.py --db .local/phd_intelligence.sqlite
```

The database file is a generated local artifact and must not be committed. Python standard library only. The docs, schema and first source records are deliberately incremental; consult [research log](docs/methodology/research-log.md) for inspected scope and unresolved gaps.

## Campaign boundaries

This repository supports planning and verification. It does not submit applications, email supervisors, accept offers, or modify external accounts. External communication and submission require explicit user authorization.

**Created:** 2026-11-11. Findings become stale; do not reuse unverified information for decisions.
