# Research log
## 2026-11-11 — Phase 1 baseline
Initialized research workspace, country dossiers and first official-source opportunity leads. Time-critical ETH/EPFL/Oxford sources were considered. See executive strategy and opportunity inventory. Application actions remain unperformed.

## 2026-11-11 — GitHub discovery and focused audit pass
- Repeated 12 GitHub repository search query families (English plus Chinese; first page only, max 35 per query).
- Deduplicated search hits and included qualified repositories identified independently. The resulting discovery CSV contains **392** distinct candidate names; **30** were source-reviewed, **362** remain UNTRIAGED. Irrelevant names may remain in the raw candidate set.
- For each of the 30 selected repositories, captured HEAD snapshot SHA, reviewed README and relevant code/docs when possible, and wrote a per-repository file. Review depth explicitly varies; no source is represented as fully audited.
- Compared scraper/monitoring tools, prompt-driven workflows, application data models, statement examples, country/field advice and scholarship directories.
- Identified two published credential-like exposures, placeholder structured extraction, factually incorrect geographic scholarship rows, deprecated recruitment data, and TLS/schema hardening gaps. Did not attempt to authenticate with any third-party credential or execute third-party scrapers.
- Persisted a current reviewed register, discovery backlog, full query log and engineering adoption design.

## Explicit remaining gaps
- GitHub code search, issues/discussions chains for all qualified resources, alternative-language search coverage, pagination beyond first results, full linked-resource audits, and measurable discovery saturation.
- Missing PDF content review for some historical statement/experience resources; incomplete portions of exceptionally large READMEs.
- No execution of remote code, benchmarked scraper recall or verified current vacancy output from third-party tools.
- Eight country dossiers still need project-level vacancy search, supervisor publication matching, individual eligibility and funding confirmation.
- No applications submitted, emails sent, supervisors contacted, offers issued or accepted.

## Next prioritized pass
1. Finish actual deadline-sensitive application requirements and candidate document gates.
2. Deep-audit top two tooling comparators using sandboxed execution and a fixed validation fixture if useful; no running credential-bearing projects.
3. Expand code search and next GitHub result pages; compute marginal yield of newly qualified repositories.
4. Follow one-hop external original sources from curation hubs and deduplicate across them.
5. Extend official Canada/Australia/New Zealand/Ireland/Luxembourg/Norway job searches with evidence and 2027 round dates.

## 2026-11-11 — Corrective systematic mapping and admissions execution pass
This log extends—not replaces—the original **392-result/30-note baseline**, which remains a historical measurement of the earlier, weaker research pass. At that historical 2026-11-11 checkpoint, the corpus had **404 raw unique candidate identities**, **35** individually inspected sources, **8** structured eight-section static deep reviews, **27** preliminary notes, **9** explicit exclusions, **7** screened included yet awaiting review and **353** untriaged. Search remains unfinished.

- Added `METHODOLOGY.md`, `SOURCE_POLICY.md`, research-status and coverage audit, explicit screening statuses and recorded GitHub code searches/second multilingual repository queries.
- Deep-reviewed eight source-pinned materials, including actual code/data/issue evidence for PhD-Seeker, SihengTao planner, BaseLayerAI monitor, eparrainage feed, ProReach CRM, erikpsw outreach pipeline, Wenzi fit rubric, and BrainPhD-CN firsthand guide. Rejected source-level unsafe `eval` and disabled TLS, and flagged historical advice to misrepresent an address.
- Expanded all eight independent country dossiers and differentiated salaried employee doctoral posts, competitive international scholarships, fee/tuition gaps and national institution-only grant routes.
- Recorded 20 program/project/rolling/competitive funding leads, 26 source-linked individual claims, 21 unique canonical sources, 5 cross-repository source dependence relations, 6 classified firsthand cases and 3 recent-method lab fit dossiers. No entry equates program admission with an actual funding award.
- Corrected ETH RobotX: final decisions by Feb 15 next year, so Nov 2026 application is **not** a demonstrated December 2026 offer. Identified UZH RPG continued screening as **capacity/form verification needed**, while Luxembourg CVI2 has salary amount but external application portal not confirmed.
- Identified the applicant's one peer-reviewed 2023 `Measurement` DOI from the publisher, but the Monash top-ranked venue requirement remains unresolved. No transcripts, identity records, scores or applicant-private data published.
- Built stdlib search/duplicate/source-check utilities, generated indexes, source ledger, add-on SQLite migration and proof-backed application events; GitHub CI checks structural consistency only. Independent semantic source verification and third-party source-code execution remain NOT PERFORMED.

### Completion blockers
No credible search saturation, 353 unscreened candidates, 27 non-deep preliminary reviews, 7 included-for-review records, no representative applicant experience population, incomplete supervisor funding and visa checks, incomplete institutional eligibility. No emails/applications/acceptances undertaken.


## 2026-11-11 — Continued repository screening and focused source review
- Reconciled the live CSV candidate register before screening: 404 canonical candidate identities, 43 previously reviewed, 9 excluded, 6 screened-in awaiting investigation and 346 untriaged.
- Individually inspected four screened-in candidates (Twinly architecture documents, PhD Radar, Doctoral-Supervisor-Skill and CS-PhD-Application-Tips) and six additional untriaged candidates (0612Leo daily tracker, A-tavv Netherlands monitor, abono200 admissions platform, AdewuyiDaniels notebook, D2Simon PhDHub and DataBizex Excel tracker).
- Added ten commit-pinned preliminary reviews. The register now contains **53 reviewed**, **9 excluded**, **2 screened-in awaiting first review**, and **340 untriaged**. Of the 53 reviewed records, **8** have the structured eight-part static deep review and **45** remain preliminary.
- Important implementation findings: notification outbox ordering in A-tavv; import-triggered XSS in the local daily journal; hard-coded analytics and unauthenticated writes in PhD Radar; uncalibrated admission/funding probabilities in static dossiers; unpinned fuzzy scholarship data; PhDHub's network exposure, plaintext secrets, user-controlled URL fetching and untrusted email-to-LLM flow; and fixed Excel ranges plus a funding/urgency composite-score defect.
- Captured positive patterns separately: explicit memory write gates, source-specific scraping with bounded retries/telemetry, local-first export and supervisor/application workflow decomposition.
- All ten reviews remain **PRELIMINARY_FOCUSED**. No third-party project was executed; no runtime, test-suite, security or admissions-policy validation is claimed.


## 2026-11-12 — PR integration and register reconciliation
- Merged PR #6 (`fcbbb597b58f55b84fd517327dd341b3954e544f`) into `main` using squash merge. It contributes ten session-specific repository investigations and a cross-repository synthesis under `research/sessions/2cabbe82/`; no canonical inventory or review index was changed by that PR.
- Recomputed the canonical register directly from `data/github_discovery_candidates.csv`, `data/repositories.csv`, and `data/exclusions.csv`: **404** unique candidates = **63** review records + **330** untriaged + **2** screened-in pending review + **9** exclusions. The 63 review records comprise **8** deep static reviews and **55** preliminary reviews.
- Corrected stale totals in `README.md`, `RESEARCH_STATUS.md`, `docs/github/README.md`, and `quality/coverage-report.md`. Historical counts in earlier log entries remain as dated checkpoints, not current state.
- Four other published research branches remain active and isolated. Their work is not merged or modified while their manifests report incomplete investigations.
- Runtime validation of third-party repositories remains unperformed; the execution container still cannot resolve `github.com`. No saturation claim is made.

## 2026-11-12 — Three further candidate screens and source-level implementation review
- Inspected aluminium5/ScholarshipScraper at 36a8f80a95e336a13114c8c23d8df698e0d96c10. Registered a preliminary review of its Indian scholarship ingestion, app tracker, backend models, authorization paths, tests and data-quality limits. Upstream tests/runtime not executed.
- Inspected agandony/sop-cs-kirimkirim at 186e1e904c491c354acce249fd4e129a47138c32: SOP refers to customer-service operations for a florist, not graduate statements of purpose. Excluded with source evidence.
- Inspected adamrpah/CSSMA at 8f5b8d14f93716fe2f59c6498c3a30e2b71eb734: computational social science teaching materials, not admissions. Excluded with source evidence.
- Recomputed canonical register: 404 raw identities = 64 reviewed (8 deep static, 56 preliminary) + 327 untriaged + 2 screened-in + 11 excluded. Other merged session investigations remain supplemental until separately reconciled.
- Identified a potential source deactivation defect in ScholarTrack: a non-empty scrape with all records rejected for missing deep links can clear previously active rows for that source. Static reasoning only; no runtime repro.

## 2026-11-12 — Five additional verified exclusions
- Screened allen9408/Web-Application at dbcb6e2921ffcc5c1cdb87b8330d0f8c6a218691: 2017 software-engineering coursework, Bayesian fitting and stock exercises; not admissions.
- Screened alparslancay/New-Graduated-Recruitment-Application at 52307e289980e34b581d1e7ecc3a8830beed04c0: student-to-company recruitment via C#/MSSQL; not doctoral funding.
- Screened AHS-CS2/ahs-cs3-classroom-cs_sop_demo-CS_SOP_demo at 6dd9ad9f9a696f985b0c83877941712d3ad937f4: empty README and Java calculator classroom test; SOP keyword collision.
- Screened Anubhav-01-lang/software-review-dashboard at 090f0d192d5ccee1a60e67f359312153aa159ebf: software product reviews NLP, not academic admissions review.
- Screened ankurhcu/6S191_MIT_DeepLearning at 2c4966842d8efceeab2916b49d57e8177f6fb2c3: MIT deep learning coursework, not doctoral application guidance.
- Canonical counts after this transaction: **404** discovered = **67** reviewed (9 deep static, 58 preliminary) + **18** exclusions + **319** untriaged + **0** screened included.
- Each exclusion has a pinned primary-source URL and its precise scope verdict in `data/exclusions.csv`. No upstream code executed; exclusions are screening decisions, not software-quality audits.

## 2026-11-12 — Four deep static source investigations: outreach integrity, storage, privacy
- Usaid786467/Global-PhD-Scholarship-Finder-Application-Automator: verified fake faculty-name/email/publication/h-index generation in the advertised professor scraper, connected to user-visible discovery and outbound email queues. Reject fabricated contact records; mock data cannot be admissions evidence.
- WagnerJon/application-atlas: verified UUID-based event history, versioned/validated backups, atomic restore, previous-data preservation, bounded attachments and CSV formula-injection mitigation in source. Local state is not official admissions confirmation.
- Tyin-nn/phd-application-manager: verified non-destructive localStorage schema migration, material/recommender tracking, browser-local backup, but deficient typed import validation and unverified cycle-specific dates.
- rjalfa/PhDAdmission: identified applicant-like directory structure with 1,600 files across 800 per-applicant-like folders; inspected only non-personal code paths. UserController logs all posted parameter values and a fixed administrator email appears in AuthenticationFilter. No applicant content accessed or reproduced.
- All four are eight-section static reviews with pinned upstream SHAs, explicit source limits, non-execution of tests, risk codes and transfer decisions.
- Canonical split: **404 = 79 reviewed (16 deep static and 63 preliminary) + 19 excluded + 306 untriaged + 0 screened included**. Canonical index regenerated.

## 2026-11-12 — Four additional preliminary investigations and one exclusion
- stevanoryan/scholarship-atlas: reviewed full static scholarship dataset design and source/reference/expected-date distinction. 172 entries reported by author; no independent live official validation; browser status cannot prove current opening.
- zarif98sjs/how-not-to-do-phd-application: analyzed author-declared US CS Fall-2024 process lessons and anecdote limitations.
- zll-hust/Business2CEEPhD: analyzed historical management/operations research to CEE interdisciplinary PhD transition and adviser/committee funding distinction.
- ShahriarAbir86/higher-study-analysis-skill: inspected README and packaged artifact inventory; a 'fully verified' generated guide is a claim, not independently sourced evidence.
- Excluded wonyly13/phd-application-prep because its single README promises nonexistent directories and an undated template placeholder rather than usable data.
- Canonical 404 = **83 reviewed (16 deep static, 67 preliminary), 20 excluded, 301 untriaged, 0 screened included**.

## 2026-11-12 — Seven source-pinned repository investigations
- Deep static: Mhrnqaruni's monitor (SQLite migrations, SHA-bound critic review, coverage and fail-closed gates, but source-claimed 'PRIMARY' not externally authenticated), ratulsaha2021 scholarship-agent (explicit send confirmation, but failed/invalid LLM fact checks return empty problems; potentially plaintext SMTP credentials), Sekilloda Hypatia (multiple physics job sources, fuzzy source collisions, non-transactional email outbox).
- Preliminary: seanxuu/PhD-Seeker is a variant of Aghababaei upstream with several changed code blobs, one scraper path TLS verify=False; Rehmanjeff Scrapy project contains a plainly committed database password in source (secret itself not copied); RZFan NLP PhD list has undated faculty and English/GRE conditions; ZhenbangYou Chinese CS admissions narrative contains historical process advice and institution/cycle-specific claims.
- All seven upstream revisions pinned, risks documented, third-party runtime and official opportunity verification **NOT PERFORMED**; no mail, calendar, applicant data or unsafe external scripts executed.
- Canonical split: **404 = 95 reviewed (23 deep static, 72 preliminary) + 22 excluded + 287 untriaged + 0 screened included**.
