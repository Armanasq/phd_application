# Sekilloda/FindMeAPhD — eight-section static source review

**Upstream revision:** `878ef253e41637c8436ae4c63aa4eabfba25ab4a`; **inspected:** 2026-11-12; **review:** DEEP_REVIEW_DOCUMENTED; **runtime validation:** NOT_PERFORMED; **source action:** READ_ONLY.

## 1. Scope and domain fit

Hypatia is an AI/multi-agent macOS monitor for theoretical/quantum physics doctoral posts. It claims integration with InspireHEP, Quantiki, CERN SmartRecruiters, DESY and Nordic universities via Varbi, local/cloud LLM scoring, calendar deadlines, dossier drafts and email alert persistence. Physics-specific source selection and fit weights limit direct transfer to robotics, SLAM and AI research. README promises autonomous headless runs but is not proof those feeds are live now.

## 2. Source modules and workflow

40 tracked entries: core/fetchers.py has adapters for INSPIRE-HEP, Quantiki, CERN, DESY, Scandinavian Varbi and AcademicPositions; core/workflow.py uses a LangGraph state with sites/search/grading/ranking agents; core/models.py uses Pydantic offering/preferences; core/deduplicator.py normalizes URLs, institutions, titles and some application URLs; core/calendar_sync.py uses Google Calendar OAuth and extendedProperties; core/mailer.py sends Gmail API/SMTP/Apple Mail and uses a persistent JSON outbox. Tests exist for outbox, calendar and dedup. Code and files were statically inspected, not executed.

## 3. Critical deduplication defect

DuplicateDetector.find_duplicate returns True when cand_title_norm == exist_title_norm **before checking institution, city or deadline**. A near-identical title (ratio>=0.93) is also accepted unconditionally even when institutions differ. 'PhD in Machine Learning' at two universities can therefore collapse into one vacancy. Less-strict matching otherwise combines Jaccard/SequenceMatcher with institution or deadline. Correct identity should prefer official requisition ID or canonical application URL, and fuzzy pairs require same employer/location/cycle plus human review if ambiguous. This is a code-path defect, not a reproduced live-data incident.

## 4. Notification, outbox and delivery semantics

Mailer.send_phd_alert tries immediate dispatch via Gmail API, Gmail SMTP, custom SMTP or optionally Apple Mail, else writes a JSON queue. flush_outbox reads each pending file, retries dispatch and writes to sent/ before deleting the queue entry. It does not atomically claim a record before dispatch, use a delivery idempotency key, or transactionally couple send and archive; concurrent runners or a crash between SMTP success and queue deletion may cause duplicate alerts. Date-only urgency uses date.today()/dateutil.parse without source timezone. Unit tests assert basic queue counts, not distributed exactly-once delivery.

## 5. Calendar and source-trust limitations

CalendarSync parses various text dates and uses a stable extendedProperties offering ID for deduping existing events. The event may still reflect an incorrect scraped deadline, missing timezone, or a falsely deduplicated offering. Some HTML adapters use fixed selectors and keyword-based job-role filters; a physics vacancy is not confirmed simply by matching 'PhD'. Pydantic Offering schema has optional scoring fields and no mandatory official funding-evidence or international-fee coverage. Credit LLM grading only as heuristic fit until evidence gates pass.

## 6. Privacy and security considerations

Mailer reads OAuth token files/environment secrets, caches full alert bodies in JSON outbox, and includes fallback default sender/recipient addresses in public source. Do not reproduce those addresses in a copied system. Calendar events may disclose study intentions and source/score details to connected account devices. Email alerts are different from supervisor outreach; this repository mainly sends notifications to the applicant. Do not grant calendar/email permissions in the absence of explicit user approval.

## 7. Comparative lessons and testing

Compared with source-only PhD-Seeker, Hypatia offers richer source-specific extraction and durable notification workflow; compared with Mhrnqaruni's tracker, it has weaker explicit claim-level funding/eligibility gates. Favor Hypatia's adapter decomposition, persisted queue, calendar upsert and source-specific fit templates, but add hard evidence checks, source coverage classification, true cross-source identity and atomic outbox semantics. Test suites and README pass claims not empirically executed by this audit.

## 8. Verdict and pinned sources

DEEP_REVIEW_DOCUMENTED (static source inspection, no live feed or integration run). Source files: [README](https://github.com/Sekilloda/FindMeAPhD/blob/878ef253e41637c8436ae4c63aa4eabfba25ab4a/README.md), [deduplicator](https://github.com/Sekilloda/FindMeAPhD/blob/878ef253e41637c8436ae4c63aa4eabfba25ab4a/core/deduplicator.py), [fetchers](https://github.com/Sekilloda/FindMeAPhD/blob/878ef253e41637c8436ae4c63aa4eabfba25ab4a/core/fetchers.py), [outbox](https://github.com/Sekilloda/FindMeAPhD/blob/878ef253e41637c8436ae4c63aa4eabfba25ab4a/core/mailer.py), [calendar](https://github.com/Sekilloda/FindMeAPhD/blob/878ef253e41637c8436ae4c63aa4eabfba25ab4a/core/calendar_sync.py), [outbox tests](https://github.com/Sekilloda/FindMeAPhD/blob/878ef253e41637c8436ae4c63aa4eabfba25ab4a/tests/test_outbox_queue.py).
