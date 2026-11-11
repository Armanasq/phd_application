# Deep repository investigation — zxcgzx/phd-application-tracker

**Review date:** 2026-11-12  
**Upstream:** https://github.com/zxcgzx/phd-application-tracker  
**Pinned default-branch commit:** `8826e96755f4d76854e00725226ff92fed59af18`  
**Review state:** DEEP_STATIC_REVIEW_COMPLETE; RUNTIME/SECURITY_VALIDATION_NOT_PERFORMED  
**Adoption decision:** REJECT_AS_IS; retain selected crawler design concepts only after remediation.

## 1. Scope and evidence

Inspected the recursive 84-entry repository tree, README, project status, crawler test report, troubleshooting and deployment docs (English and Chinese), Python crawler, university configuration, Supabase synchronization, SQL schema and initialization/fix/diagnostic scripts, frontend application/store/components/importer, GitHub Actions workflows, commit history, issues, pull requests, and Actions history.

Key source files inspected:
- `crawler/main.py`
- `crawler/config.yaml`
- `crawler/scrapers/base_scraper.py`
- `crawler/scrapers/two_level_scraper.py`
- `crawler/database/supabase_sync.py`
- `check_database.py`
- `database/schema.sql`, `database/init_all.sql`, `database/fix_rls_policies.sql`, `database/comprehensive_fix.sql`, `database/enable_realtime.sql`, `database/deep_diagnosis.sql`, `database/clean_invalid_data.sql`
- `frontend/js/app.js`, `frontend/js/supabase-config.js`, `frontend/js/components/professor-list.js`, `frontend/js/components/crawler-manager.js`, `frontend/js/features/import/import-data.js`, `frontend/js/core/store.js`, `frontend/js/components/timeline.js`, `frontend/js/core/stats.js`, and batch operations.
- `.github/workflows/crawl-weekly.yml`, `crawl-manual.yml`, `deploy.yml`.

No code was executed and no credential was used. The hardcoded credential-like value is deliberately omitted; its validity has not been tested.

## 2. Product scope and actual architecture

This is a small supervisor-directory and application-outreach tracker, not a comprehensive funded doctoral opportunity platform.

The main workflow is:
1. Maintain a static YAML list of universities and scraping selectors.
2. Fetch each university's listing page.
3. Extract profile links and fetch individual profile pages.
4. Extract names, titles, research areas, homepage/profile URL, department, office, and selected contact/education fields.
5. Synchronize professor records to Supabase.
6. Use a static browser frontend to filter and manage professor records and application status.
7. Store application status, outgoing email content, follow-up dates/logs, and crawl logs.

The crawler and browser application have separate configuration/state surfaces. The crawler reads `crawler/config.yaml`; the frontend's university manager writes rows to Supabase. Adding a university in the UI does not automatically create a crawler adapter or update the YAML file. The UI therefore cannot independently configure a new source for the crawler.

The repository config currently contains only three enabled university entries. The crawler factory always instantiates the two-level scraper; a single-page scraper is not implemented in the inspected path.

## 3. Data model and admissions semantics

### 3.1 Schema

The PostgreSQL schema defines universities, professors, applications, follow-up logs, email templates, and crawl logs. The professor record includes name, title, research areas, homepage/profile URL, email, phone, office, department, education, raw HTML, active status, and a recruitment flag.

The model is materially narrower than a full PhD opportunity record:
- no distinct program/opportunity entity;
- no country/campus/program intake or application-cycle entity;
- no funding commitment, stipend, tuition coverage, eligibility, or fee model;
- no per-field source provenance, page snapshot, parser version, or claim verification state;
- no `user_id` or ownership key for personal records;
- applications are unique by `professor_id`, limiting one application record per professor;
- `sent_by` is a free-text operator label, not an authenticated user identity.

The schema's `is_recruiting` column defaults to TRUE. The inspected crawler does not extract a recruiting signal or set this field, so newly synchronized professors inherit a recruiting-positive default without evidence. The field is not used by the current frontend's main display path, but it is unsafe semantics for downstream filters or future consumers.

### 3.2 Staleness and identity

The sync path matches a professor by `university_id + name`, not a canonical profile URL or stable researcher identifier. Name changes can create duplicates; same-name people can be conflated. There is no last-seen timestamp or source snapshot per professor.

A professor missing from a later crawl is not deactivated. Existing `is_active` rows are not reconciled against the current result set. The university statistics are updated from the latest scraped list length rather than a verified database count. Existing raw HTML is not refreshed on update.

The crawler also does not prove that a professor is accepting doctoral students. Research interests or a profile page are not evidence of an open funded vacancy.

## 4. Crawler implementation

### 4.1 Positive design

`BaseScraper` centralizes:
- a reusable `requests.Session`;
- timeout and retry settings;
- polite per-request delay with jitter;
- exponential retry backoff;
- BeautifulSoup/lxml parsing;
- configurable keyword, sibling, CSS-selector, and regex extraction helpers;
- text cleanup and basic research-area splitting/deduplication.

`TwoLevelScraper` separates listing-page discovery from individual profile-page extraction. This is a useful adapter pattern for university faculty directories.

### 4.2 Implemented limitations

- Requests follow redirects by default and do not validate destination host, IP address, scheme, or redirect chain.
- Profile links are resolved with `urljoin` but are not restricted to the university's allowed host.
- There is no DNS pinning or private/reserved IP rejection. A malicious or compromised page can cause the crawler to request arbitrary HTTP(S) targets, including internal addresses.
- The `respect_robots_txt` configuration flag is not consumed by the inspected crawler.
- The `max_workers` and `update_frequency` settings are not used by the execution path. The project configuration guide explicitly describes worker concurrency as unfinished.
- The main loop processes universities and profile links sequentially.
- There is no response-body size cap or content-type validation in the base request helper.
- Site selectors and keyword rules are brittle under university CMS redesigns.
- Some detail fields (office, department, education) use only the first configured rule and keyword extraction rather than a common multi-rule fallback mechanism.
- No parser-version or per-field provenance is stored.

The default TLS certificate verification behavior of Requests is retained; no disabled TLS verification was observed in the inspected base fetch method.

### 4.3 Operational accounting defects

`SupabaseSync.sync_professors()` increments its `new` counter after calling `_insert_professor()`, even if the insert helper returns without data and only prints a warning. The update path similarly increments `updated` after a failed/no-result update. Reported crawler statistics can therefore overstate persisted changes.

`crawler/main.py` catches per-university exceptions, records a failed result, prints a final summary, and then returns normally. It does not exit non-zero when one or more universities fail. GitHub Actions can report a successful process while the crawl itself failed for one or more targets.

The crawl log schema contains `execution_time_seconds`, but the inspected logging path does not populate it.

## 5. Critical security findings

### 5.1 Hardcoded Supabase service-role credential fallback

Both `crawler/database/supabase_sync.py` and `check_database.py` contain a hardcoded fallback value shaped as a Supabase service-role JWT, after checking environment variables.

This is credential material in public source, not a public anon key. Validity and exploitability have not been tested and no authentication attempt was made. Treat it as compromised:
- revoke/rotate the affected service-role key;
- remove the literal from all tracked history where possible through owner-controlled incident response;
- make service-role configuration environment-only;
- use least-privilege credentials and never expose them to the browser.

The frontend anon key is expected to be public, but the RLS policies below make its exposure materially more dangerous.

### 5.2 Unrestricted RLS and missing ownership

The SQL initialization and fix scripts create broad policies using `USING (true)`; the fix script also uses `WITH CHECK (true)`. The database initialization guide explicitly tells operators to grant the same unrestricted policy to `anon` and `authenticated` roles.

The schema has no per-user ownership columns or authenticated identity model. The frontend creates a Supabase client with the public anon key and does not authenticate users. Its `currentUser` selection is a localStorage display label (two fixed operator names), not a security principal.

The data includes supervisor contact details, application notes, email subjects/bodies, and follow-up history. The current policies do not isolate those records between users. Depending on table grants and project configuration, anonymous clients can access data covered by the anon policies. This is not a multi-tenant private application model.

### 5.3 Manual workflow command injection

`.github/workflows/crawl-manual.yml` interpolates the `workflow_dispatch` `target_url` input into a shell command string, wraps it in single quotes, and executes the constructed string using `eval`.

The input can break the quoting and inject shell syntax for a user authorized to dispatch the workflow. The workflow also exposes the Supabase service-role secret to the runner. This is a critical command-injection pattern. Replace it with a direct argument invocation and pass the input through an environment variable, never through `eval`.

### 5.4 Stored XSS

The frontend renders untrusted database/import/crawler fields directly into `innerHTML`:
- `professor-list.js` inserts `professor.name` and title into professor cards and modals without escaping.
- `crawler-manager.js` inserts `uni.name`, URL values, and crawl-log error messages directly into HTML; the university name is also interpolated into an inline `onclick` JavaScript string.
- `app.js` builds university options using raw database values.

The CSV importer accepts user-provided professor names and university names. A malicious import or stored record can therefore become stored HTML/script injection. Some fields are escaped, but escaping is inconsistent. URLs also require scheme allowlisting; HTML escaping alone does not prevent `javascript:` links.

## 6. Confirmed importer/schema defects

### 6.1 University creation omits required URL

`findOrCreateUniversity()` inserts a new university with only `name` and `is_active`. Both `schema.sql` and `init_all.sql` define `universities.url` as `NOT NULL UNIQUE`. Importing a professor for a new university therefore fails at university creation unless that university already exists.

### 6.2 Unsupported `college` field

The CSV importer sends a `college` property to the `professors` table. Neither canonical SQL initialization schema defines this column. A record containing that field can fail with an unknown-column/schema error.

### 6.3 CSV parser limitations

The parser handles quoted commas within a line but splits the file by newline before parsing. Quoted fields containing embedded newlines are not handled as full RFC 4180 CSV. Preview escaping does not fix the schema mismatch or database write path.

## 7. Workflow, frontend, and synchronization behavior

- The browser application reads/writes Supabase directly; there is no application API enforcing identity or row ownership.
- `currentUser` is a localStorage label, not authentication.
- Realtime subscriptions are used for selected tables, but this does not provide access control.
- The university manager is not connected to the crawler's YAML source registry.
- Email subject/body and template data are stored; no verified outbound mail-sending integration was found in the inspected app.
- Follow-up timeline records are stored separately; the inspected add-log path does not update the application's `last_followup_at` field.
- Batch operations issue sequential per-record writes; there is no atomic batch transaction.
- A global migration rewrites legacy `sent_by` labels on page initialization; it is not tracked by a durable schema-migration version.
- The `clean_invalid_data.sql` script deletes all professor records for named universities; it is destructive and should not be run without a backup and explicit confirmation.
- The SQL setup paths are inconsistent: project status/README describe `schema.sql` plus `seed.sql`, while the database guide also describes `init_all.sql`. The seed file is not designed for unrestricted repeated execution in the same way as the consolidated initialization script.
- The database diagnosis/fix scripts include psql meta-commands such as `\\echo`; these are not ordinary SQL statements and may fail when pasted into a GUI SQL editor.

## 8. Development history and validation

- Default branch: `main`; no other branches returned.
- Latest source commit: 2025-11-09.
- Issues: none returned.
- Pull requests: none returned.
- Latest retrieved scheduled crawler run: 2026-01-09. No newer run was returned in the first 10 recent workflow runs.
- The repository has no dedicated automated unit/e2e test directory or test CI workflow. `CRAWLER_TEST_REPORT.md` is a manual report, not a reproducible test suite. Its 74-professor extraction claim is historical and was not independently revalidated.
- The manual test report predates later configuration changes. The current first university config does not request email/phone extraction, consistent with later project status documentation removing automatic contact scraping.
- The project status file describes completed feature work but also acknowledges missing automated tests and unverified cross-device/realtime behavior.

A green Actions result is not sufficient proof of crawl correctness because the main script can return exit code zero after per-university failures.

## 9. Reuse decision and required remediation

**Do not deploy or execute this repository as-is. Do not copy its credential handling, RLS policies, manual workflow, or HTML rendering patterns.**

Before any reuse:
1. Rotate the exposed service-role key and remove hardcoded fallbacks.
2. Implement authenticated user identity and row ownership; replace broad RLS with `auth.uid()`-scoped policies and explicit role targets.
3. Remove shell `eval`; pass workflow input as a quoted process argument or environment variable.
4. Validate target URLs, enforce HTTPS/host allowlists, validate every redirect, reject private/reserved IPs, and implement robots.txt policy.
5. Escape all untrusted HTML values, use safe DOM APIs, and restrict URL schemes.
6. Align CSV import fields with the SQL schema; require and validate university URLs.
7. Default recruiting state to UNKNOWN/false; require explicit dated evidence before marking recruiting.
8. Add canonical profile identifiers, per-source provenance, fetched/last-seen timestamps, parser version, and stale-record reconciliation.
9. Make writes transactional/idempotent; count only confirmed inserts/updates; propagate crawl failure via non-zero exit status.
10. Add unit, integration, security, and workflow-injection tests; gate deployments on them.

## 10. Final disposition

**DEEP_STATIC_REVIEW_COMPLETE** for the inspected source and operational paths.  
**RUNTIME_VALIDATION_NOT_PERFORMED**.  
**CREDENTIAL_VALIDITY_NOT_TESTED**.  
**SECURITY EXPLOITABILITY_NOT_TESTED**.

The two-level scraper is a reusable architectural concept. The current implementation is unsafe for applicant-private data and does not provide trustworthy current-recruitment semantics.
