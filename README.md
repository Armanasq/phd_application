# PhD Admissions Intelligence & Execution

**Research baseline:** 2026-11-11 · **Program status:** ongoing, source-backed but incomplete.

Local-first research system for doctoral admissions in Canada, United Kingdom, Ireland, Luxembourg, Switzerland, Norway, New Zealand, and Australia. Scientific emphasis: robotics, AI, deep learning, SLAM, navigation, sensor fusion and autonomous systems.

## Entry points
- [Executive admissions strategy](docs/strategy/executive-2026-2027.md)
- [Eight preliminary country dossiers](docs/countries/README.md)
- [Funded opportunity leads](data/opportunities.csv)
- [GitHub research index and ranked findings](docs/github/README.md)
- [Thirty repository assessments](docs/github/reviews/)
- [Reviewed repository register](data/repositories.csv): 30 rows, commit-pinned, each linked to an individual assessment.
- [Broad GitHub discovery queue](data/github_discovery_candidates.csv): 392 distinct discovery records, **362 untriaged**. Not a claim of 392 audits.
- [GitHub search log](data/github_search_log.csv): 12 query groups, first returned page per query; no global exhaustiveness established.
- [Key engineering lessons](docs/github/engineering-lessons.md) and [source-based risk register](docs/github/failure-register.md)
- [Research protocol](docs/methodology/research-protocol.md) and [research log](docs/methodology/research-log.md)
- [Relational data architecture](docs/architecture/data-model.md) and [application operations](docs/operations/application-playbook.md)
- [Public redacted candidate baseline](docs/candidate/profile.md)

## Current discovery counts
- 8 preliminary country dossiers
- 7 first-pass funded/program/position leads; financial terms and actual eligibility may remain unverified
- 30 individually documented **focused** GitHub reviews; depth varies by repository and is explicit in each report
- 392 unique initial repository search candidates, including noise; 362 still untriaged
- 12 logged broad keyword search queries (only page one requested)
- 0 applications submitted, supervisors contacted or offers received by this workspace

No repository or historical link is accepted as proof of a current funded vacancy. The initial catalog includes important findings about embedded credentials, misleading funding extraction, outdated scholarship rows, link freshness and dataset deprecation. Read [failure register](docs/github/failure-register.md) before considering external code reuse.

## Structure

```text
docs/
  countries/       separate, evidence-aware national dossiers
  strategy/        immediate and 2027 application portfolios
  candidate/       redacted candidate and evidence gaps
  architecture/    data entities and proof requirements
  methodology/     source protocol and chronological research log
  operations/      application and authorization states
  github/          review index, engineering lessons, failure register
    reviews/       30 source-pinned individual repository assessments
data/
  opportunities.csv
  evidence.csv
  repositories.csv
  github_discovery_candidates.csv
  github_search_log.csv
sql/               SQLite schema
scripts/           stdlib-only dataset validation and bootstrap
tests/             catalog and safety regression tests
.github/workflows/ validation
```

## Evidence and privacy
An advertised doctoral employment vacancy is not the same as generic program admission, and scholarship eligibility is not an award. Keep application deadline, decision date, enrollment date and funding start distinct. Record unknown applicant credentials and funding terms as unknown.

**This repository is public.** Keep passports, transcripts, residence records, private email, referees' contact details, API keys and all applicant-private drafts out of git. Never copy credentials found in third-party code. Search and AI-generated text are untrusted discovery aids. Every high-stakes assertion needs current, official, claim-specific evidence.

## Local quality gate

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/bootstrap.py --db .local/phd_intelligence.sqlite
```

GitHub Actions is configured to run validation and tests; do not infer a green build unless an actual run confirms it.

## Operating boundary
Research review and preparation can proceed without outreach. Supervisor emails, applications, commitments, external accounts and any acceptance action require explicit authorization.
