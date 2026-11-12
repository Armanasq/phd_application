# physical10086/phd-application-tracker — deep static vacancy monitor and privacy audit

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/physical10086/phd-application-tracker | **Pinned revision:** [`60e477d6a3671b2ebb7a1c7ff958464f544e7cbb`](https://github.com/physical10086/phd-application-tracker/commit/60e477d6a3671b2ebb7a1c7ff958464f544e7cbb) | **State:** DEEP_REVIEW_DOCUMENTED (static code review) | **Decision:** adapt separation of source verification and private annotations; reject present “verified/open” inference and public applicant record sharing.

## 1. Product scope and source

A Chinese-language, static HTML/JavaScript PhD application tracker focused on neutral-atom/experimental AMO/quantum-hardware positions across European labs. It includes a Python daily discovery script, configurable search queries, a JSON/JavaScript opportunity seed file, a search history, localStorage-based personal annotations and a GitHub Actions workflow. The pinned default-branch tree has 19 entries, last observed update 2026-09-22. The README describes both manual records and automated Bing RSS/optional Serper discovery.

This is principally one applicant's workflow, not a representative international doctoral vacancy census, funded-offer validator, or institution-operated admissions portal.

## 2. Discovery, extraction and persistence

`scripts/update_opportunities.py` reads config and current opportunities, rechecks each existing URL, runs a fixed high-priority query plus selected `site:` searches, retrieves result pages with Requests/BeautifulSoup, checks for broad doctoral terms and topic keyword hits, extracts nearby page sentences and deadlines with regular expressions, assigns a heuristic keyword score and appends new records. It writes `opportunities.json`, a corresponding JS seed, and a JSON/JS search log. Search providers and original URLs are recorded, with missing text marked by the Chinese equivalent of “not specified by source”.

`app.js` renders seeds as cards, filters and application-state dashboards; localStorage stores user profile and state overrides. It escapes text and HTML attributes before interpolation into its main templated cards, a positive practice relative to raw unescaped markup.

## 3. Source truth and false verification semantics

The crawler sets `source_verified=True` whenever a URL returns HTTP success, regardless of whether the page actually contains a current official PhD vacancy, salary amount or institution-issued confirmation. Its `candidate_from_page()` can label an opportunity `OPEN` based on broad words such as “apply” or “applications” anywhere in a topical page, even without a dated active vacancy. The title, institution and PI may remain unknown. This is URL accessibility plus keyword relevance, **not opportunity verification**.

Existing records reset `source_verified=True` on HTTP 200 and can retain prior `open_state` unless a narrow “closed/filled” phrase is found. A changed page, archived listing or source redirect can therefore remain “open” without official evidence. The README's two consecutive 404/410 invalid-link rule is useful for availability stability, but HTTP 200 is not a positive recruitment signal.

## 4. Deduplication, chronology and reconciliation

`make_id()` hashes canonical URL plus lowercased title, while `canonical()` strips all query parameters and fragments. Applications or different intake cycles sharing a landing URL can collapse, and updated titles can split one source into multiple IDs. Deduplication also checks a normalized title prefix, so semantically distinct vacancies with similar titles may be dropped.

`refresh_existing()` mutates items in place; search failures do not record a run completeness state or identify whether an old open claim remains stale. The writer directly replaces multiple JSON/JS files rather than using a locked transaction or atomic swap, so failure or concurrent scheduled runs can leave mismatched versions. No unit test fixtures were found for source changes, redirects, duplicate cycles, empty results or date parsing.

## 5. Candidate privacy and submission evidence

The repository's committed seed opportunity data includes **personal applicant-status notes** stating that emails have been sent or portal applications submitted. These are source statements about the original owner's activity, **not validated receipts**, nor facts about the user of the present PhD workspace. Such histories should not be duplicated in public research records or used as templates for applicants.

The web frontend places local edits in localStorage but the JSON/JS seed may still contain identifying correspondence details. A public GitHub Pages repository is not private applicant-data storage. Keep correspondence, referrer contacts, grades, transcripts, sent-mail evidence and submission receipts in private, authorized storage.

## 6. Funding and scientific-fit scoring

The keyword-based “match score” favors Rydberg, neutral atoms, optical tweezers, quantum computing, AMO hardware and profile keywords, and is explicitly described by the README as a **ranking heuristic, not admission probability**. The code caps it at 99, but high scores cannot prove an open funded job, eligibility, laboratory funding, language standards, or the presence of a faculty slot. Existing seed records distinguish opportunities and informal group inquiries to some degree, but they should never be promoted without current official offer evidence.

Potential contact routes, lab project pages and named supervisors can be useful research-fit leads without being active vacancies; group research descriptions do not establish a funded contract.

## 7. Transfer requirements and adoption decision

Retain: source URL and timestamp, missing-field preservation, scored research relevance separate from acceptance odds, local annotation preservation, source-check failure counters, search logs, and a human-readable application state pipeline.

Required redesign:
1. Distinguish `URL_REACHABLE`, `SOURCE_PARSED`, `OFFICIAL_ACTIVE_VACANCY_VERIFIED`, `OFFICIAL_CLOSED`, `UNKNOWN` and `STALE`.
2. Track official vacancy ID, institution/cycle, application deadline timezone and funding components.
3. Keep personal application events private and permit “submitted” only after an actual receipt/authorized action.
4. Enforce safe URL/redirect/DNS/IP fetch policy, resource limits, host rate limits, and source terms.
5. Use atomic writes, freshness/read completeness records and scheduled-run fencing.
6. Test ambiguous dates, false positives, reopened jobs, shared landing URLs and partial search/provider failure.

## 8. Pinned evidence and limitations

- [README and declared source policy](https://github.com/physical10086/phd-application-tracker/blob/60e477d6a3671b2ebb7a1c7ff958464f544e7cbb/README.md)
- [Crawler and source verification](https://github.com/physical10086/phd-application-tracker/blob/60e477d6a3671b2ebb7a1c7ff958464f544e7cbb/scripts/update_opportunities.py)
- [Browser local state and escaping](https://github.com/physical10086/phd-application-tracker/blob/60e477d6a3671b2ebb7a1c7ff958464f544e7cbb/app.js)
- [Search configuration](https://github.com/physical10086/phd-application-tracker/blob/60e477d6a3671b2ebb7a1c7ff958464f544e7cbb/config/sources.json)
- [Search profile](https://github.com/physical10086/phd-application-tracker/blob/60e477d6a3671b2ebb7a1c7ff958464f544e7cbb/config/search_profile.json)
- [Seed structure](https://github.com/physical10086/phd-application-tracker/blob/60e477d6a3671b2ebb7a1c7ff958464f544e7cbb/data/opportunities.json)
- [Search log](https://github.com/physical10086/phd-application-tracker/blob/60e477d6a3671b2ebb7a1c7ff958464f544e7cbb/data/search_log.json)

**DEEP_REVIEW_DOCUMENTED — static source only.** Crawler, model, browser and primary seed/source structure inspected. No upstream automation, actual applicant account, email/portal action, third-party research webpage, funding claim, live vacancy or runtime test was independently verified. This review does not reproduce personal notes or contact information.
