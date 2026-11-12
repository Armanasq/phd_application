# Rehmanjeff/scrape-phd-positions — deep static Scrapy audit

**Pinned revision:** `b086e5cf78ec75d8fdfee8795488fa319747568e` ([Git tree](https://api.github.com/repos/Rehmanjeff/scrape-phd-positions/git/trees/b086e5cf78ec75d8fdfee8795488fa319747568e)); **inspected:** 2026-11-12. **Execution:** NOT_TESTED. Public plaintext connection credential is present upstream; no secret value copied.

## 1. Purpose and boundaries

Small historical Scrapy project fetching scholarshipdb.net IoT-related PhD ads, not a verified current official university job or application service.

## 2. Inventory and architecture

The pinned tree has 30 entries: Scrapy spider, items, settings, no-op pipeline, database helper, HTML cache and JSON dump, generated Python bytecode. No root README was found. Source modules inventoried and `phdPositions/spiders/phdPosition_spider.py`, `settings.py`, `pipelines.py` inspected; database helper was checked for its connection-side-effect semantics without reproducing credential values.

## 3. Parser and retrieval dataflow

`start_requests()` embeds a historical scholarshipdb.net search URL at page 3, then `parse()` iterates `.position-details`, extracts program title, university, country, summary and an apply link, following detail and next-page anchors. It does not extract a typed deadline, degree/financial offer, verified host provenance or applicant eligibility.

## 4. Confirmed implementation defects

The spider imports `dbModule` at module import and that helper constructs a PostgreSQL connection with inline authentication. It accesses `detail.css('div::text')[1]` without checking length, risking IndexError. The heading and apply link are taken from full-response selectors rather than the current card, creating cross-post association risks. The `PhdpositionsPipeline.process_item` method only returns its input without validating/upserting, so the apparent DB flow is not a implemented transaction. Source: [spider](https://github.com/Rehmanjeff/scrape-phd-positions/blob/b086e5cf78ec75d8fdfee8795488fa319747568e/phdPositions/spiders/phdPosition_spider.py) and [pipeline](https://github.com/Rehmanjeff/scrape-phd-positions/blob/b086e5cf78ec75d8fdfee8795488fa319747568e/phdPositions/pipelines.py).

## 5. Security and privacy

A hardcoded database password in repository source is a credential-leak risk: revoke/rotate if active, and remove from history. The crawler has no per-source rate-limit/terms policy, bounded source completeness, multi-tenant privacy model or safe deployment authentication. Do not run its connector or sample data unchanged.

## 6. Transfer to global PhD Atlas

A source-specific adapter can preserve university/job ID, fetched time, exact original vacancy URL, full institutional evidence and open-status verification. This project provides only a small historical parsing example. Compare with source-driven collectors with stronger type/provenance gates; never infer full funding from a third-party search result.

## 7. Verdict

**REJECT_AS_PRODUCTION_SOURCE, priority P0.** Static deep inspection of core source modules completed; no evidence of a valid current funded vacancy, acceptance or compliant crawl.

## 8. Testing and validation gaps

Required tests: malformed/empty HTML card, per-card field association, pagination/duplicate identity, HTTP failure handling, credential checks, university-host verification and privacy-safe persistence. No Scrapy execution, actual database connection, exploit, source-terms check or official program verification performed.
