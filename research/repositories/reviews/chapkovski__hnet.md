# chapkovski/hnet — deep static review of an academic-job archive crawler

**Reviewed:** 2026-11-12; **upstream commit:** [ea29e333b291129ea63055fd9a39d5d57895373b](https://github.com/chapkovski/hnet/commit/ea29e333b291129ea63055fd9a39d5d57895373b).  
**Status:** DEEP_REVIEW_DOCUMENTED, static inspection only.  
**Disposition:** structural design reference for archive-first extraction; reject deployment as-is.

## 1. Purpose and supported source

A Django 3-era system collecting historical H-Net academic job advertisements by numerical identifier (`https://www.h-net.org/jobs/job_display.php?id=...`). The project stores raw HTML plus a normalized record with institution type, position, category, location, posting date, closing date, link and contact. It is primarily a historical humanities/academic jobs dataset, **not** a verified current fully funded PhD opportunity provider.

The repository has 36 tracked files and a 2021 last commit. The README directs users to an OSF data deposit, but that separate dataset was not re-fetched or validated.

## 2. Architecture and state model

The Django models separate `Raw` from `StructuredPost`. `Raw` holds external identifier, original URL, HTML body and timestamps. `StructuredPost` references the raw record one-to-one, with normalized metadata and many-to-many taxonomies (`Category`, `Position`). `UnfoundRecord` and `FailedRenderPost` capture source misses and parse failures.

The `collect` management command receives a start/end ID range, subtracts previously collected and not-found identifiers, then fetches remaining IDs concurrently using `requests_futures.FuturesSession`. The `process` command reads saved raw HTML and attempts structured extraction using BeautifulSoup, Pandas and Django ORM.

This raw-to-structured boundary and explicit unfound/render-failure persistence are transferable design patterns.

## 3. Ingestion completeness, correctness and deduplication

`collect` constructs **one future for every unprocessed ID in the supplied range**. No bounded queue, concurrency budget or per-host rate policy was found. Wide numeric ranges may trigger excessive parallel requests. Requests do not define explicit timeouts or retry policies.

The collector uses `Raw.objects.create(external_id=...)` after checking existing values, but `Raw.external_id` is not declared unique in the model. Two simultaneous collectors can race and create duplicates despite the pre-check. `UnfoundRecord.external_id` likewise lacks database uniqueness.

It assumes `page.url` ends in `?id=<digits>` and immediately calls `m.group` without guarding redirects or unexpected final URLs. HTTP 200 pages are classified by the presence of `p.error`; a redesigned error template or bot-block page can be stored as a valid advertisement.

A failed response aborts the run rather than preserving independent per-ID retry state. Historical missing IDs are never automatically reconsidered, even if the upstream archive later repairs a missing record.

## 4. Parser and date handling

`process` assumes two `table.table_border` elements and `div.nav_end > div.text`, then uses `pd.read_html` and positional field mapping. Missing/changed markup triggers exceptions handled by storing a `FailedRenderPost` record, which is better than silently presenting missing results as valid data.

However:
- `get_categories_from_table` can return `None`, and its result is iterated without a guard.
- `posting_date_obj` and `closing_date_obj` may be `None`, yet `.astimezone(pytz.utc)` is called unconditionally. Any record lacking one of these dates is rejected.
- Parsed dates are naive `datetime` objects; using `.astimezone` assigns an implicit host-local interpretation before UTC conversion, rather than an authoritative source timezone.
- The parser uses an outer exception handler, records the failure and continues, but no structured error type, severity or retry schedule is saved.
- Processed many-to-many relations are added without clearing previous values, so changed source categories can leave stale associations on reprocessing.

## 5. API and security boundary

`hnet/serializers.py` mounts `RawViewSet` and `PostViewSet` as DRF `ModelViewSet` routes. The root `urls.py` includes the router. Neither the viewsets nor `REST_FRAMEWORK` settings define authentication/permission classes requiring authorized access. In the inspected configuration, DRF's default is effectively permissive for these endpoints; exposure can allow external reading and modification of raw and processed records.

The source also commits a literal Django `SECRET_KEY` and configures `DEBUG=True`. These are development defaults, not acceptable hosted settings. This review intentionally does not reproduce the secret value. `ALLOWED_HOSTS=[]` may block requests in standard deployment but is not an authorization control; changing it without hardening the API would expose these endpoints.

An ingestion service should use a service-to-service credential, read-only external API, network isolation and non-public administrator routes.

## 6. Tests, operations and provenance

The file named `hnet/tests.py` is not an automated test suite: it executes database queries at import time and calls `sys.exit()`. This is unsafe for a test runner and does not establish reproducible coverage. No CI workflow or explicit license file appears in the tree. Upstream code is not executed.

Storing original HTML and source URL improves post-hoc traceability, but the data lacks content hashes, source checked timestamps per extraction, immutable revision history, effective cycle and claim-level evidence spans. It is not a live vacancy verification system.

## 7. Evidence and limitations

The source-level flaws above follow from the pinned collector, models, parser, settings and router. Runtime exploitability, upstream changes, H-Net access terms, actual data integrity and record counts were **not** independently tested. The archived OSF dataset was not downloaded.

Relevant source paths:
- [Collector](https://github.com/chapkovski/hnet/blob/ea29e333b291129ea63055fd9a39d5d57895373b/hnet/management/commands/collect.py)
- [Parser](https://github.com/chapkovski/hnet/blob/ea29e333b291129ea63055fd9a39d5d57895373b/hnet/management/commands/process.py)
- [Models](https://github.com/chapkovski/hnet/blob/ea29e333b291129ea63055fd9a39d5d57895373b/hnet/models.py)
- [Router and viewsets](https://github.com/chapkovski/hnet/blob/ea29e333b291129ea63055fd9a39d5d57895373b/hnet/serializers.py)
- [Django settings](https://github.com/chapkovski/hnet/blob/ea29e333b291129ea63055fd9a39d5d57895373b/hnetproj/settings.py)
- [Test module](https://github.com/chapkovski/hnet/blob/ea29e333b291129ea63055fd9a39d5d57895373b/hnet/tests.py)

## 8. Transfer decision for PhD Atlas

Reuse **the architecture, not the implementation**: immutable raw source observation, typed parse result, separate not-found and render-failure states, stable upstream ID, source-specific normalized taxonomy. Correct the missing DB uniqueness, add per-page budgets/timeouts, explicit source timezone, record-level failure queues, verified parser fixtures, read-only authenticated routes and data versioning.

Model H-Net academic jobs as **low-priority historical discovery leads**, not confirmed current PhD vacancies, funding or admissions eligibility.
