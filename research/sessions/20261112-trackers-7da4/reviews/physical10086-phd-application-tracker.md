# physical10086/phd-application-tracker — static collector, status and privacy audit

**Upstream:** https://github.com/physical10086/phd-application-tracker
**Pinned revision:** [60e477d6a3671b2ebb7a1c7ff958464f544e7cbb](https://github.com/physical10086/phd-application-tracker/commit/60e477d6a3671b2ebb7a1c7ff958464f544e7cbb)
**Review date:** 2026-11-12
**Classification:** DEEP_STATIC_SOURCE_REVIEW. No live scraper, HTTP requests, GitHub Actions job, Selenium/browser or private applicant data read beyond the publicly committed source needed to audit its schema.
**Scope:** Complete 19-entry Git tree / 16 blob files, full collector module, static UI, source/profile config, data schema and record-count statistics, history, README and file-level test/workflow presence.
**License:** No license file found in pinned tree.

## 1. What the repository actually implements

Static HTML/JS tracker for European AMO, Rydberg arrays and neutral-atom quantum PhD opportunities, with optional Python collector using requests and BeautifulSoup. The source contains a serverless browser UI that overlays localStorage statuses and profile information on committed data/opportunities.js seed records. Python discovery queries optional Serper first and Bing RSS otherwise; it visits discovered links, extracts text/deadline/topic by regular expressions, produces bounded candidate records, refreshes previously stored URLs, and serializes JSON plus browser-facing JavaScript. The source includes 20 committed seed opportunities and two dated search-log records; 2 seed application stages are "submitted", 13 are "contacted", and 5 "interested". These are *author-committed applicant assertions*, **not proof of applications or third-party outcomes**.

The README describes a GitHub Actions daily 00:25 UTC scheduled workflow, while the complete pinned tree has **no .github/workflows directory or workflow YAML**. Thus daily scheduled execution is not implemented in this repository snapshot. Individual scripts may still be run manually or by some out-of-repo automation, but no evidence of that is established. No automated tests were present.

**Primary sources:** [update script](https://github.com/physical10086/phd-application-tracker/blob/60e477d6a3671b2ebb7a1c7ff958464f544e7cbb/scripts/update_opportunities.py), [README](https://github.com/physical10086/phd-application-tracker/blob/60e477d6a3671b2ebb7a1c7ff958464f544e7cbb/README.md), [static UI](https://github.com/physical10086/phd-application-tracker/blob/60e477d6a3671b2ebb7a1c7ff958464f544e7cbb/app.js).

## 2. P0/P1 — source verification is not verified job eligibility or availability

The collector's fetch() returns ok=True after a successful HTTP response, even for non-HTML content, and candidate_from_page() sets source_verified=True for accepted candidates. The acceptance predicate is **generic page text containing any PhD term plus two broad research keywords**, not a particular job ad, university posting, hiring contact, funding amount or application opening. Its open_state is set to "open" when the page text contains broad phrases like "apply" or "applications"; a general lab website, aggregate portal, instructions page or unrelated job list may satisfy this predicate. The inferred university is always set to "source not specified" in the auto-generated record, and location matching comes from a small city token list rather than proof of institution.

This is **URL accessibility and topical matching**, not verification of a funded doctoral position. The final source links require independent official employer inspection. Preserve separate fields for HTTP accessibility, official-source authenticity, position type, actual hiring status, eligibility, funding, and deadline with evidence spans.

The score() method clamps simple keyword bonuses into **50–99**, and the UI calcScore() uses a different formula. Neither is an applicant admission probability; the README correctly calls matching a heuristic.

## 3. P1 — unstable opportunity identity and false deduplication

canonical(url) discards every query and fragment and lowercases the hostname. Distinct postings differentiated by query parameters may collapse; the title-only global existing_titles dedup key can also conflate distinct vacancies using the same generic title. Conversely make_id(url,title) incorporates title, so minor revisions to a posting title can create an additional identity for the same real opportunity if title-only dedup does not catch it. The 12-hex-digit truncated SHA-1 ID is deterministic but not a substitute for source-defined vacancy IDs and content/version provenance.

**Repair:** canonicalize only known non-semantic query parameters, preserve source-specific job IDs, match by institution+source job ID+cycle and verify duplicate conflicts rather than silently discarding.

## 4. P1 — status refresh can become stale or lose context

- refresh_existing() marks open_state closed if *any* page text contains "applications closed", "position filled" or "vacancy closed"; it does not require that text to describe this position.
- It never positively reopens a previously closed row after a new employer update. Deadlines are only populated if missing and not updated when the page later changes them; last_checked is refreshed on successful HTTP responses nonetheless.
- It declares a URL invalid after two consecutive 404/410 responses, a useful tolerance for transient failures, but other HTTP failure modes return unknown without a source-success timestamp/cause update.
- The collector does not capture snapshot hashes, a raw evidence span attached to each structured field, source authority classification, deadline timezone or meaningful next recheck time.
- fetch() follows redirects automatically from search-discovered URLs without an explicit host/IP allowlist or internal-address check. Running it in an environment with network access/credentials deserves SSRF and egress threat-model review; this was **not tested as an exploit**.

**Repair:** bounded HTTP trust policy, per-field claim status, old/new deadline conflict record, source-domain allowlist, official-origin provenance, and timestamped transitions for verified open/closed/unknown.

## 5. P1 — imported backups lose part of their state on later edits

In app.js, loadLocalState() can restore a backup using saved.override containing complete opportunity objects. importBackup() explicitly stores override:opportunities then reloads. But the next status edit calls saveState(), which **replaces** localStorage with an object containing, for seed IDs, only application_status, status_note and match_score. Any other properties imported for those seed identities (corrected deadline, funding description, URL, etc.) are not persisted; after a subsequent reload the original seed data reappears. This is a deterministic source-level state-loss path, not a tested browser reproduction.

**Repair:** versioned backup schema with three-way source refresh merge, immutable seed/source fields and explicit user-edit fields; round-trip/import/edit/reload tests with conflicting updates.

## 6. Privacy and provenance boundary

The README says applicant progress and personal background are saved in browser localStorage, which is true for *future local edits*. However the tracked repository also publicly commits its sample applicant's research background plus seed application statuses and notes. Thus public repository access is not a privacy-preserving local-only workflow for those seeded facts. Do not replicate, expose or reuse another applicant's profile or contacts as real strategy evidence; when adapting, keep all applicant identity/application outcomes encrypted or access-controlled outside a public repo. The report intentionally omits names, contact identifiers and personal narrative contents.

The UI escapes interpolated text via esc(), improving template safety, but its source URL is escaped as HTML attributes and **not constrained to an HTTP(S) scheme** before assignment into a clickable link; imported backups allow arbitrary links. Enforce URL schemes and safe rendering at the sink.

## 7. Transfer and acceptance tests

**Transferable:** explicit unknown-field sentinel, source_link + last_checked fields, separated browser status overlay, restore/export mechanism, bounded candidate limit, two-failure URL hysteresis and visibly heuristic ranking.

**Do not transfer:** scheduled monitoring without a workflow, HTTP-success-as-job-verification, page-wide closure/open heuristics, unversioned URL/title-only identity, silent stale deadline reuse, client-import state overwrite, or public seed application history.

**Tests to add:** scheduled workflow presence and dry-run logs; safe HTTP/redirect policy; false-positive landing-page fixture; two different job IDs on one host with different query params; same title at two universities; delayed deadline extension/position reopening; URL 404 vs 403/429; import → edit → reload state preservation; unknown deadline never inferred open; private details never committed.

**Validation limits:** Static inspection of all repository source and data structure at pinned commit; no external job-site availability, official vacancy checks, Actions CI, test execution, browser runtime, actual network results or personal applicant outreach were performed.
