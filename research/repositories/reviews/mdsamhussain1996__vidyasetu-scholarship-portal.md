# mdsamhussain1996/vidyasetu-scholarship-portal — source-level repository investigation

**Date:** 2026-11-11  
**Pinned upstream commit:** [`fc11048d6488c86d9da373795d857f2019f88204`](https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal/commit/fc11048d6488c86d9da373795d857f2019f88204)  
**Review state:** PRELIMINARY_FOCUSED. Substantive static inspection, not full-file exhaustive review or independent runtime validation.  
**Applicability:** scholarship_evidence_and_review_pipeline  
**Primary risk:** substring_official_domain_and_premature_auto_verification  
**Reuse decision:** original methods only; no unreviewed code adoption

## 1. Purpose and scope

An India-focused multi-class opportunity portal with government, university, internships, fellowships, project positions and international route references. The interesting research object is its source-change/update process: recurring funding schemes need a different temporal state model from one-off doctoral job postings, and new LLM-extracted leads need human review before becoming a public fact.

## 2. Architecture and actual components

`config/sources.yaml` enumerates watched official pages; `scripts/discover.py` fetches source HTML, caches its hash, asks an LLM to extract a constrained JSON schema, deduplicates by provider and title, sends new records to `pending.json`, updates existing entries, rolls annual deadlines, and produces audit metadata. `data/schema.json` contains separate `firstSeen`, `lastVerified`, `verifiedBy`, `confidence`, and `dateConfidence` (`confirmed|expected|unknown`). Tests cover rollover, title dedup, scam warnings and broad link heuristics. GitHub Actions schedules daily discovery and a PR for pending items.

## 3. Task-to-data flow and dependencies

Temporal dependency: source snapshot -> proposed facts with quoted text -> canonicalized provider identity -> staging queue or updated existing record -> annual-cycle maintenance. For recurring schemes, when a cycle deadline passes, the algorithm clears exact open/end dates, sets `dateConfidence=expected` and `status=upcoming` but intentionally does not reset `lastVerified`; this prevents a historical confirmed date from appearing current. A weekly link check is separate from date facts. Each opportunity can require multiple application steps/documents, making it useful for process decomposition.

## 4. Methods and source-level evidence

Important verified code-path bugs: `is_official_link` uses trusted-domain *substring* membership against the entire lowercased URL instead of validating exact DNS hostname boundaries. The provider fallback compares host containment in either direction. Both can misclassify lookalikes. `run_discovery` sets a new watched-page content hash *before* confirming extraction success; failed/quota-exhausted extraction may not retry unchanged pages. New `cand` confidence becomes `0.9` merely because an `evidence` string exists. For duplicate entries, `if cand.get('evidence')` updates source, lastVerified and confirmed date without excluding failed domain/scam review flags.

## 5. Implementation and operational reconstruction

Do not reuse auto-verified status semantics as they stand. Require URL parsing with IDNA/canonical hostname and registrable-domain allowlist, redirects rechecked; quote-to-source substring/span validation; a per-claim source revision hash and cycle; transactional watch hash advancement only after successful ingestion; idempotent pending items; and human review gating for conflicting/updated published dates. Test a source update containing a forged quoted date, misleading host, and two distinct similarly titled awards.

## 6. Failure modes and validation gaps

Limitations: a valid webpage and exact quote still do not establish funder legitimacy or applicant eligibility. Some database attributes require non-negative funding amount even if the award does not state one; such schema decisions can force placeholders. The auto-update workflow writes existing data to main separately from pending PRs. `tests/test_portal.py` checks expected examples but not malicious host aliases, extraction failures, or verified-date corruption. No upstream workflow executions or model accuracy tests were run here.

## 7. Transfer to PhD Atlas and admissions workflow

Adopt source hashing, annual-cycle rollback, pending-review PRs and separate verification timestamps, but design a strict review escalation ladder: `discovered -> fetched -> field_extracted -> official_source_attested -> policy_scoped -> independently_verified -> eligible -> actionable`. Referee/documents remain separate application entities. Treat every future annual deadline as Unknown/Expected until specific official 2027 conditions are retrieved.

## 8. Provenance and outstanding verification

Inspected schema, discovery engine, validation module, source/query settings, unit tests and scheduled workflow at pinned revision. Static source-level conclusions are grounded in linked files, not an assertion that the internet archive, full corpus, scheduled cron or downstream PR actually succeeded. External verification and test execution remain outstanding.

## Pinned source files inspected

- [`data/schema.json`](https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal/blob/fc11048d6488c86d9da373795d857f2019f88204/data/schema.json)
- [`scripts/discover.py`](https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal/blob/fc11048d6488c86d9da373795d857f2019f88204/scripts/discover.py)
- [`scripts/validate.py`](https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal/blob/fc11048d6488c86d9da373795d857f2019f88204/scripts/validate.py)
- [`tests/test_portal.py`](https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal/blob/fc11048d6488c86d9da373795d857f2019f88204/tests/test_portal.py)
- [`.github/workflows/daily-update.yml`](https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal/blob/fc11048d6488c86d9da373795d857f2019f88204/.github/workflows/daily-update.yml)
- [`config/search_queries.yaml`](https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal/blob/fc11048d6488c86d9da373795d857f2019f88204/config/search_queries.yaml)
- [`config/sources.yaml`](https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal/blob/fc11048d6488c86d9da373795d857f2019f88204/config/sources.yaml)

## Validation protocol not yet completed

1. Inspect remaining implementation paths, licenses, issues, history and source links, then record coverage independently.
2. Run tests with pinned toolchain in a sandbox; capture commands, fixtures, exit codes and outputs.
3. Verify each admissions, fee, funding and applicant eligibility claim against authoritative live sources for the correct cycle.
4. Record conflicting claims, reviewer authorization and revisions; never infer an application was sent or an offer obtained.
