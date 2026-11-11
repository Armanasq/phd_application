# KeithBH/phd-positions — complete single-file source and data audit

**Upstream:** https://github.com/KeithBH/phd-positions
**Pinned revision:** [2dfe11ac0d7403e3f143ab7aab7c45f05574edff](https://github.com/KeithBH/phd-positions/commit/2dfe11ac0d7403e3f143ab7aab7c45f05574edff)
**Review date:** 2026-11-12
**Audit depth:** Complete static source and embedded-data inspection of the project's only substantive file, [index.html](https://github.com/KeithBH/phd-positions/blob/2dfe11ac0d7403e3f143ab7aab7c45f05574edff/index.html). No live employer/aggregator verification, browser execution, deployment tests or outreach.
**Verdict:** Curated, dated discovery leads. Do not treat the displayed active counts, labels, hiring status or funding as verified facts.

## 1. Real scope and operating model

The two-file tree contains only `index.html` and an empty `.nojekyll`. The standalone page uses inline CSS, an embedded JSON-like JavaScript array, and client-side filters, sorting and row rendering. It contains no scraper, backend, scheduled refresh, database, test suite, CI workflow, README or license declaration at the pinned snapshot. The recent commit history consists of manual updates; the latest 2026-10-16 commit added ETH humanoid robotics and University of Twente EngD leads. There are no open issues or pull requests at inspection.

The page targets European industrial AI, robotics and manufacturing applicants. Its Chinese-language record schema combines opportunity ID, area/country, university, lab, supervisor, title, research topic, deadline, URL, hand-assigned relevance, status, notes and job type. Data are author-curated, not a normalized employer vacancy feed.

## 2. Reproducible static-data reconciliation

The exact JavaScript array beginning `const DATA = [` and ending immediately before `let currentSort` parses as valid JSON and has **192 unique-ID rows**. Counts below were independently computed from that array, not copied from the visual counters:

| Measure | Embedded data | Hard-coded headline | Difference |
| --- | ---: | ---: | ---: |
| Total rows | **192** | **144** | 48 understated |
| Status `待查看` (pending review) | **115** | **82 active** | 33 understated; pending is not verified active |
| Status `已过期` (expired) | **77** | **62 expired** | 15 understated |
| Relevance `3` (high) | **57** | **44 high** | 13 understated |
| High relevance among pending | **30** | not presented | — |

The banner numbers are literal HTML, not derived from `DATA`. The interface dynamically counts *filtered* rows only in the results line; its four top counters remain stale after hand-edits. These counts are internal source-data statistics, **not** verified advertised positions, funded positions or applicant-fit measurements.

Source: [header counters and DATA](https://github.com/KeithBH/phd-positions/blob/2dfe11ac0d7403e3f143ab7aab7c45f05574edff/index.html).

## 3. P0/P1: outdated openings remain in the default active view

The `applyFilters()` implementation hides a row when its **manually entered status** contains the Chinese text for expired; it does not compare an ISO deadline to today's calendar or source-local time. As of **2026-11-12**, **14** rows have syntactically valid ISO deadlines earlier than that date while still marked `待查看`. Examples: ID 193, Örebro distributed-AI doctorate, deadline 2026-11-02; ID 191, ETH computational engineering design, deadline 2026-11-01; ID 189, University of Antwerp mechatronic systems, deadline 2026-11-02. These rows remain in the default 115-row pending set. It is not independently established whether any employer extended their deadlines.

The dataset has **102/192 non-ISO deadline values**, including unknown or rolling-recruitment text. A parser that simply treats these as future/open would be incorrect. Record ID 194, ETH humanoid robotics and embodied AI, has an unknown deadline, not an officially confirmed open status; ID 195 has a 2026-11-15 date but is **EngD**, not a conventional PhD.

**Required design:** keep source-observed status separate from inferred time status and formally verified employer status. Store deadline as optional structured local date/time/timezone, cycle, original raw string, check timestamp, and source URL. Treat unknown as unknown. Recheck official employers before recommending applications or reporting an opportunity active.

## 4. P1: links, eligibility and program type cannot be trusted as curated

- **24** rows have blank or non-HTTP application URLs; this count is based on the embedded field, not an external link checker. Empty links render as self-navigation with the current anchor template.
- **54** rows contain author notes indicating broken/unavailable links or mentioning HTTP 403/404 (computed from note strings); this is a historical annotation count, **not** independent HTTP validation.
- **31** duplicate link-field occurrences were counted, including blank values. Equal links are not necessarily duplicated jobs because generic landing pages may be shared.
- The **192 rows** include **174** marked normal position contracts, **11** CSC categories, **3 EngD**, **1 Postdoc**, **1 research engineer**, **1 'urgent' type** and **1 blank type**. Counting all 192 as PhD admissions would be a category error.
- The source has a qualitative 1–3 fit score without a documented rubric or applicant-specific evidence. It is not an empirical selection probability.

**Required design:** distinguish doctorate, EngD, postdoc, research assistant/engineer, scholarship, and unknown roles. Represent international eligibility, stipend, tuition coverage, residency and language needs separately with source-level evidence and tri-state values.

## 5. P1/P2: static UI, browser trust and provenance weaknesses

The page is not a live collector: neither `fetch()` nor crawler/scheduler code appears in the tracked file. Changing a vacancy or extending a deadline upstream does not change this page without a new author commit. The row renderer uses `tbody.innerHTML` to interpolate source-record strings and `href`; filter chips use `container.innerHTML` to interpolate the viewer's search text without HTML escaping. This latter path can render raw markup typed into the filter field; no remote exploit vector or production breach is claimed. Use DOM-safe text nodes, URL scheme allowlisting and attribute encoding.

The embedded records do not carry immutable source hashes, extraction timestamps, official employer verification, field-level evidence spans, independent recheck results or change history per opportunity. A latest repository commit date is only the page's update date and says nothing about the freshness of each individual entry.

**Required design:** version individual source observations; maintain per-field evidence and verification, preserve previous deadlines and conflicts, add non-destructive URL/identity matching and upstream permission checks, and regenerate counters directly from validated records.

## 6. Transfer to PhD application strategy

**Useful:** compact single-page human triage, country/university/search/type filters, preliminary relevance notes, clearly distinguished author-curated scope, and historical interest-group leads.

**Do not transfer:** stale status badges, literal global counters, unverified opportunity counts, an unqualified 'active' label, expired dates represented as open, raw free-text deadline as a verified timestamp, missing application URLs, self-interpolated HTML, or conflation of EngD/postdoc/engineering roles with funded PhDs.

A viable evidence pipeline is: official employer or permitted advertisement source → dated captured source → job-type normalization → candidate field claims → independent deadline/funding/eligibility verification → human review → separated applicant-private application workflow. Until verification, these **192 source leads are neither live openings nor 192 actionable applications**.

## 7. Validation boundary

Inspected the complete source tree, complete embedded array, current source filters and rendering functions, source metadata, commit history, issues and PR lists at the pinned snapshot. Derived counts through parsing the embedded DATA array; did not visit the 192 linked pages, use the live GitHub Pages site, run browser/XSS tests, check robots/terms, execute or host any upstream code, or independently validate any vacancy. The 14 stale-by-date records are a static deadline/status contradiction, not independent proof that positions are permanently closed.

**Primary source:** [pinned index.html](https://github.com/KeithBH/phd-positions/blob/2dfe11ac0d7403e3f143ab7aab7c45f05574edff/index.html).