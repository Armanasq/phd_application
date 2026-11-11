# Second-batch synthesis — audit-20261112-r47c6f-b

Date: 2026-11-12. Three source-level or entire-Markdown investigations, plus two **incomplete binary PDF archival triages**. No live scraping, database connection, Telegram send, source-site verification or application was executed.

| Repository | Evidence inspected | Proposed canonical state | Decision |
|---|---|---|---|
| serdark/academic-jobs-scraper | All 3 files, 386 URL entries parsed, scheduled workflow, recent Actions/PR/issues | REVIEW_RECORDED, deep static | Turkish research-assistant academic ads; design/gastronomy only; adapt source scheduling, not PhD evidence |
| realrezi/Medical-PhD-Scraper | All 9 files, MIT license, app/database/filter, regex edge case separately tested | REVIEW_RECORDED, deep static | Aggregator-keyword leads, not official funded medical PhD vacancies |
| nishanchettri/PhD-positions-electronic-engineering | Entire one-file 4-entry 2024 list, metadata and PR/issues | REVIEW_RECORDED, preliminary | Historic university lead only; funding unverified |
| neuronalX/phd-and-postdoc-positions | README, Git tree and binary PDF metadata only | SCREENED_INCLUDE pending PDF | Inria 2023 doctoral topic; PDF contents not read |
| renzoe/positions_internships_phd_postdoc | README, Git tree and 4 PDF metadata entries only | SCREENED_INCLUDE pending PDF | French 2023 doctoral / 2025 engineering archived ads; PDF contents not read |

## Engineering lessons

- **State model:** observed source URL is not an active offer, a successful notification or a verified funded doctoral appointment. Use separate discovered/fetched/scoped/verified/notified statuses with receipts and deadlines.
- **Source fidelity:** per-claim official URL, quoted span, snapshot hash, retrieved timestamp, effective cycle, applicant nationality and fees/funding status. The sampled records contain insufficient evidence to infer admissions.
- **Failure safety:** fail closed on upstream HTML changes, alert delivery failures, failed Postgres insertions and expired vacancies. A seen-list entry must not mean a Telegram alert succeeded.
- **Filtering:** typography-sensitive regex (Ph.D. false negative) and body-wide keywords introduce systematic false results. Test representative variants and record uncertainty.
- **Source independence:** 386 URLs marked seen are not 386 funded offers; four 2024 "Fully Funded" rows are source claims, not current awards; six binary PDFs are not reviewed until text/figures are extracted.

## Coordination and limits

All five identities were UNTRIAGED in the session's pinned main snapshot when claimed, and no other agent's canonical records were edited on the isolated branch. The two PDF-only archives remain **unfinished** and should not be upgraded to REVIEW_RECORDED without reading the underlying documents. Canonical updates must be based on latest main and honor more recent classifications by other agents.

No upstream runtime tests were executed, apart from a bounded independent Python regex check. Live employment/funding checks, accuracy benchmarks and the remaining repository corpus remain outstanding.
