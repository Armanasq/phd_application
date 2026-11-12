# A-tavv/phd_position_tracker — deep static source audit

**Date:** 2026-11-12. **Upstream commit:** [633256b65fe945fb5fc7fefa747a78a573e418cf](https://github.com/A-tavv/phd_position_tracker/commit/633256b65fe945fb5fc7fefa747a78a573e418cf).  
**State:** DEEP_REVIEW_DOCUMENTED (source inspection, NOT runtime-tested). **Verdict:** adapt bounded monitoring design; reject notification delivery state.

## 1. Scope

Monitors Netherlands-oriented doctoral vacancies from AcademicTransfer and EURAXESS. Topic/doctoral-title classification is discovery, not official evidence of funding, eligible nationality, offer or admission.

## 2. Architecture

The main module runs two source adapters, collects per-source diagnostic counters, deduplicates title/employer/location combinations, checks a Redis seen-key store and sends Telegram messages. The scraper includes HTTP retries/backoff, a public-token AcademicTransfer JSON API adapter, EURAXESS listing/detail HTML parsing, country checks, page caps and source reports. Actions runs the CLI once using secrets.

## 3. Persistent notification correctness

The workflow calls Redis mark_if_new before Telegram send. Redis uses atomic SET NX with a default 30-day TTL, while TelegramNotifier.send_message catches transport/HTTP errors and returns no delivery receipt. The caller increments sent_jobs regardless. Failed messages are therefore counted as sent and suppressed for that TTL. Missing REDIS_URL makes dedup always return true, sending recurring duplicates; Redis errors can abort the workflow. Stable URL ID alone cannot represent edits or new recruiting cycles.

## 4. Discovery coverage and filtering

AcademicTransfer scans no more than 20 pages of 10 JSON records; EURAXESS scans up to 15 pages and may stop early on errors or empty results. Counters measure HTTP codes, retries, pages, matched jobs and off-country results, but none proves completeness. The relevance predicate requires PhD/doctoral/doctorate plus a technical topic keyword in the **title**, even when the description supplies relevant context. Exclusion keywords are searched against title and context. False negatives are plausible, but recall was not measured.

## 5. Evidence/eligibility quality

Results hold title, source, employer, URL, location and ID only. Deadline, source timezone, salary or stipend, coverage of international tuition, citizenship/visa rules, faculty availability and document evidence are absent. Country can fall back to listing text if a detailed source fetch fails. Dedup by exact title/employer/location can merge distinct vacancies or miss aliases.

## 6. HTTP, runtime and security

Requests follow redirects; the source does not revalidate final host and resolved IP against an origin allowlist. Source HTML can provide hrefs for detail fetches, creating a hosted-use SSRF boundary. Dependencies are unpinned. Cron '0 8 */4 * *' runs every fourth day-of-month rather than daily or a strict every-96-hours cadence; the local scheduler's 96-hour interval is not calendar-equivalent. No tests, source snapshots or delivery recovery are demonstrated.

## 7. Pinned references and limitations

[main.py](https://github.com/A-tavv/phd_position_tracker/blob/633256b65fe945fb5fc7fefa747a78a573e418cf/main.py), [scraper.py](https://github.com/A-tavv/phd_position_tracker/blob/633256b65fe945fb5fc7fefa747a78a573e418cf/scraper.py), [storage.py](https://github.com/A-tavv/phd_position_tracker/blob/633256b65fe945fb5fc7fefa747a78a573e418cf/storage.py), [notifier.py](https://github.com/A-tavv/phd_position_tracker/blob/633256b65fe945fb5fc7fefa747a78a573e418cf/notifier.py), [config.py](https://github.com/A-tavv/phd_position_tracker/blob/633256b65fe945fb5fc7fefa747a78a573e418cf/config.py), [workflow](https://github.com/A-tavv/phd_position_tracker/blob/633256b65fe945fb5fc7fefa747a78a573e418cf/.github/workflows/daily_check.yml). No scraper, Redis, Telegram, network or CI run was executed; results are source-level, not empirical performance.

## 8. Transfer

Keep bounded source adapters and operational telemetry. Replace mark-before-send with a receipt-backed durable outbox and retryable UNKNOWN_DELIVERY state, revision/cycle-aware keys, explicit fetch-completeness states and source/redirect allowlisting. Preserve official URLs and exact funding/deadline/eligibility evidence before recommending an opportunity.
