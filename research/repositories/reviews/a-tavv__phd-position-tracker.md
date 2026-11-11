# A-tavv/phd_position_tracker — focused source review

- **Review date:** 2026-11-11
- **Pinned upstream commit:** [633256b65fe945fb5fc7fefa747a78a573e418cf](https://github.com/A-tavv/phd_position_tracker/commit/633256b65fe945fb5fc7fefa747a78a573e418cf); latest commit observed 2026-04-15.
- **Category:** Netherlands-focused PhD vacancy scraper and Telegram notifier.
- **Review state:** PRELIMINARY_FOCUSED. Static inspection of scraper, orchestration, Redis deduplication, notifier and GitHub Actions; no upstream execution.
- **License:** no explicit license metadata or license file confirmed in this pass.

## 1. Problem and intended user

Monitors AcademicTransfer and EURAXESS for Netherlands-based doctoral vacancies, applies keyword/exclusion filters, deduplicates the combined results and sends Telegram notifications. This is a country-specific alert bot, not a global admissions or funding database.

## 2. Architecture and data flow

Two source adapters collect search results and detail-page metadata. `main.py` normalizes the combined job list, deduplicates within a run by title/employer/location, checks a Redis seen-ID store, then sends Telegram messages. The GitHub Actions workflow invokes a one-shot run. Configuration sets a 96-hour interval, request timeouts, delays, retry/backoff, page caps and Netherlands-specific source URLs.

Relevant files: [scraper.py](https://github.com/A-tavv/phd_position_tracker/blob/633256b65fe945fb5fc7fefa747a78a573e418cf/scraper.py), [main.py](https://github.com/A-tavv/phd_position_tracker/blob/633256b65fe945fb5fc7fefa747a78a573e418cf/main.py), [storage.py](https://github.com/A-tavv/phd_position_tracker/blob/633256b65fe945fb5fc7fefa747a78a573e418cf/storage.py), [notifier.py](https://github.com/A-tavv/phd_position_tracker/blob/633256b65fe945fb5fc7fefa747a78a573e418cf/notifier.py), [workflow](https://github.com/A-tavv/phd_position_tracker/blob/633256b65fe945fb5fc7fefa747a78a573e418cf/.github/workflows/daily_check.yml).

## 3. Useful implementation ideas

- Separate source adapters rather than one generic scraper.
- Detail-page enrichment after search-result discovery.
- Bounded pagination, request timeouts, retries and backoff.
- Per-source operational reports include page counts, HTTP statuses, retries, off-country results and stop reasons.
- Redis `SET NX EX` provides an atomic, expiring seen-job key when configured.

## 4. Correctness and delivery findings

The most important defect is the order of operations: `mark_if_new` persists the job ID **before** Telegram delivery. `send_message` logs failures but returns no success result; the caller increments its sent counter regardless. A failed delivery is therefore counted as sent and suppressed for the 30-day TTL, with no retry queue. When Redis is not configured, `mark_if_new` returns true for every job, so cross-run deduplication is disabled and old vacancies can be resent on every scan.

Cross-source deduplication uses exact normalized title, employer and location; it can miss near-duplicates or collapse distinct positions sharing those fields. The 30-day TTL can also allow a still-open vacancy to reappear after expiry. The workflow comment describes a daily check, but the cron expression is `0 8 */4 * *`; the job is not daily. The code configuration separately states a 96-hour interval.

The filter is intentionally Netherlands-specific and excludes several role terms, including research-assistant roles. This can reduce recall for doctoral posts whose title uses local employment terminology. The project should expose false-negative review samples rather than treating keyword filtering as exhaustive.

## 5. Funding and eligibility limitations

The monitor does not establish whether a role covers international tuition, whether the applicant's nationality/residence status is eligible, or whether the stated salary is a guaranteed doctoral employment contract. A Netherlands location and a PhD-like title are not equivalent to a fully funded offer.

## 6. Testing and operational maturity

No live scraper execution, Telegram delivery test, Redis outage test or failure-recovery test was run. The current configuration is narrow and requires source-specific maintenance as portal markup changes.

## 7. Adoption judgment

**ADAPT THE ADAPTER/OBSERVABILITY PATTERN; REWRITE DELIVERY STATE.** Useful for source adapters, retry telemetry and bounded scraping. Replace mark-before-send with a durable outbox: discovered → validated → queued → delivered/failed, with idempotency keys and retry policy. Preserve the original employer URL and independent funding/eligibility verification.

## 8. Unresolved work

Test each source against archived fixtures; measure recall and precision; add canonical URL/title matching; implement delivery acknowledgements and retryable outbox; add Redis-disabled persistent fallback; validate country and international-fee status; review robots/terms and rate limits.