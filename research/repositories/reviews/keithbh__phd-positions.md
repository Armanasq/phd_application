# Deep static audit — KeithBH/phd-positions

**Inspected:** 2026-11-12. **Pinned upstream commit:** [`2dfe11ac0d7403e3f143ab7aab7c45f05574edff`](https://github.com/KeithBH/phd-positions/commit/2dfe11ac0d7403e3f143ab7aab7c45f05574edff). **Scope:** complete static source and embedded-array inspection; no live vacancy checks. **Decision:** historic discovery inputs only, not a current funded-vacancy index.

## 1. Repo, version, tree and scope

The tree consists of a standalone `index.html` plus an empty `.nojekyll`. The page is a browser-side, Chinese-language, author-maintained catalogue of European AI, robotics and industrial/manufacturing research positions. It contains inline CSS, a JavaScript `DATA` array, status and relevance filters, sorting and DOM rendering. No backend, search provider API, scheduled crawl, CI tests, update feed, professional licence declaration or independently generated current-job evidence appears in the two-file tree. Commit history shows manual curation with most recent inspected change on 16 October 2026.

Primary evidence: [full pinned index.html](https://github.com/KeithBH/phd-positions/blob/2dfe11ac0d7403e3f143ab7aab7c45f05574edff/index.html). Original full technical report: [session audit](../../sessions/20261112-phdbench-keith-4e23/reviews/keithbh-phd-positions.md).

## 2. Actual source schema and implementation

The complete embedded `const DATA = [...]` was independently parsed as valid JSON from the pinned file. It contains **192 records with 192 distinct IDs**, with fields for institution, country, location/area, group, supervisor, title, research direction, deadline, link, qualitative fit, manually assigned status, free-text notes and role type. The browser filters and sorts these local records and displays them in a table; it does not fetch official employer vacancy content.

Records are not normalized across publication, applicant fit, funding, nationality, visa, tuition, source or cycle. A local row ID and string search relevance are not employer vacancy identity or admission probability.

## 3. Reproducible count and status contradictions

The parsed source has **115** records with the status `待查看` (pending review) and **77** marked `已过期` (expired). The top-of-page manually typed counters claim 144 total, 82 active, 62 expired and 44 high-relevance; these are not derived from the array and cannot be used as trustworthy metrics.

| Field | Verified static source value |
|---|---:|
| Embedded records | 192 |
| Unique record IDs | 192 |
| Pending-review records (not verified open) | 115 |
| Manually expired records | 77 |
| ISO-shaped deadline strings | 90 |
| Other deadlines (unknown, rolling or text) | 102 |
| Pending-review records with ISO dates before 2026-11-12 | **14** |
| Blank or non-HTTP link fields | **24** |
| Duplicate link-field occurrences including blank values | **31** |
| Notes mentioning invalid/broken links or 403/404 using documented match rules | **54** |

These counts were independently reproduced by parsing the pinned array and checking string values; they are *internal dataset statistics*, not active-position or funding counts. Recheck manually if upstream commits change the array.

## 4. Deadline freshness and false-open risks

The page default filter uses the manual source status rather than comparing an official deadline against the present date. As of **12 November 2026**, **14** entries marked pending have ISO deadlines before that date (e.g., source IDs 193, 191 and 189). It is unknown whether any employers extended or reopened those vacancies. No publication date, source content hash, last checked time or historical correction event is recorded per source claim.

Of 192 records, **102 deadlines are not strict YYYY-MM-DD dates**; some represent rolling windows or unknown. This is not evidence of future openness. Funding, offer timing, eligibility and timezone are not represented in separately verified fields. Correct design retains original deadline text and status, parsed date/time/timezone if supported, employer-verified current state and conflict history separately.

## 5. Type confusion, links and provenance gaps

The source assigns **174** normal employment-type roles, **11** CSC entries, **3 EngD**, **1 postdoctoral role**, **1 research engineer**, **1 urgent type** and **1 empty type**. A CSC category is not automatically unrestricted funding; an EngD is not interchangeable with a research doctorate. Blank/non-HTTP application links appear in 24 records, and 31 duplicate link-field occurrences include blank/generic links. Neither row-title similarity nor equal general university pages necessarily means two records describe the same vacancy.

A 1–3 manual fit score is an author judgement, not a candidate-conditioned ranking model or selection probability. There are no per-field official source snapshots and no employer-verified eligibility/funding/tuition components.

## 6. Frontend rendering and verification boundaries

The rendering code uses `innerHTML` for row templates and filter controls, incorporating source strings and some displayed search state. The original audit identified unescaped input-to-markup paths. These are relevant DOM-safety concerns but no browser execution, XSS payload, or deployed exploit was tested. No runtime build/test harness or link status crawler exists in this source snapshot. A page timestamp or repository commit does not establish current vacancy status.

A safe downstream pipeline should text-escape content, validate link schemes, derive counters from typed records, deduplicate official vacancy IDs, and refuse to output a verified-open status without a recent primary employer source. Respect source access terms and international eligibility distinctions before crawling linked sites.

## 7. Interconnection with applicant tools and domain modelling

This source is useful as a compact **human triage UX** and seed list of historic institutions and robotics/industrial-AI supervisors. It is not a structured job feed. Compare [PhDBench's candidate-workflow findings](nikhil-rao20__phdbench.md): source-side pending cannot mean open; client-side submitted counts cannot mean actual submitted. Both errors arise from treating a manually assigned or inferred label as external evidence.

The system should store `source_observation` (title, raw date/status, link, observed_at, hash), `normalized_opportunity` (employer, canonical ID, type, separate funded/fee/visa terms), `independent_verification` (official policy/vacancy source, checked time, claim-level support) and **private applicant action** (approval, send, receipt, feedback) as distinct entities.

## 8. Decision, evidence and outstanding validation

**DEEP_REVIEW_DOCUMENTED** of this complete two-file static repo and its 192 inlined rows; **LIVE_VACANCIES_UNVERIFIED**, **NO_BROWSER_TEST**, **NO_RUNTIME_TEST**, **NO_EMPLOYER_RECHECK**. Do not represent the 115 pending, 192 total or 30 high-fit pending as genuine active fully funded PhD vacancies. The data's academic-interest value is historical; actionable application decisions need source-specific employer confirmation, local date/time context, applicant funding eligibility and an authenticated portal route.

Source: [pinned source file](https://github.com/KeithBH/phd-positions/blob/2dfe11ac0d7403e3f143ab7aab7c45f05574edff/index.html). The independently reproduced 192/115/77/14/102/24/31/54 counts strengthen the static audit but do not substitute for linked employer checks.
