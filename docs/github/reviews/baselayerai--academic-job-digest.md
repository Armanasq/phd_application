# BaseLayerAI/academic-job-digest

- **Assessment date:** 2026-11-11
- **Canonical repository:** https://github.com/BaseLayerAI/academic-job-digest
- **Inspected snapshot:** fec14470cf708784698865cbbfc48ec41d44c3a1
- **Category:** JOB_MONITORING_PIPELINE
- **Review depth:** focused repository inspection (not a complete source audit)
- **Inspected material:** README.md; src/db.ts; src/pi.ts; tree
- **Verdict:** ADAPT_CONCEPTS

## Distinct practical value
Operational ingestion architecture: career-site adapters -> filtering -> Postgres upsert/dedup -> PI enrichment with LLM/search -> ranking -> scheduled digest; local candidate profile is excluded from source control.

## Verified limitations and risks
Targets six US biomedical institutions, not all eight target countries; email is an actual downstream action. Postgres configuration includes TLS rejectUnauthorized=false for some connection strings and interpolates a configurable schema identifier into SQL. These designs require security review before reuse. README says unresolved PI causes position suppression, which can omit otherwise valid jobs.

## Candidate-specific action
Adapt pipeline architecture, but keep unresolved PI jobs visible, separate candidate fit from source truth, validate identifiers/TLS and avoid automatic sending.

## Not inspected or demonstrated
No execution, complete threat model, test suite run or source-site behavior validation.

**Source rule:** External funding, admissions and visa claims cited by the repository require fresh verification at original official sources. No tool was installed, code executed or external action authorized merely by this review.
