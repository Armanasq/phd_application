# serdark/academic-jobs-scraper — deep static source audit

- Inspected: 2026-11-12; [pinned commit e221d512b0bc2061308fc1b618267d85370d0879](https://github.com/serdark/academic-jobs-scraper/commit/e221d512b0bc2061308fc1b618267d85370d0879).
- State: DEEP_REVIEW_DOCUMENTED (static source, workflow metadata, no browser/network execution here).
- Category: Turkish public academic **research-assistant hiring** notifier for visual communication design and gastronomy; not funded doctorate admissions.
- Verdict: limited adaptation of scheduled source monitoring and dedup; reject as a portable PhD vacancy or reliable alerting engine as-is.
- Complete tracked tree: three files — scraper.py, GitHub Actions schedule.yml, seen_jobs.json. No README, LICENSE, tests or pinned requirements.

## 1. Purpose, scope and recruitment unit

The [sole Python program](https://github.com/serdark/academic-jobs-scraper/blob/e221d512b0bc2061308fc1b618267d85370d0879/scraper.py) monitors Turkish governmental academic job advertisements at ilan.gov.tr. Its specialization is employment titles containing Turkish "araştırma görevlisi" (research assistant), limited to visual communication/graphic design or gastronomy and culinary-arts text matches. That is a specific academic staff recruitment category, not admission to a PhD program, verified stipend or international eligibility. Some research assistants may also be doctoral students; the relationship must not be assumed. The project is relevant to monitoring architecture more than to this program's priority-country funding shortlist.

## 2. Dataflow and architecture

The [scraper](https://github.com/serdark/academic-jobs-scraper/blob/e221d512b0bc2061308fc1b618267d85370d0879/scraper.py) opens four hard-coded recent listing pages (indices 0–3) in a headless Selenium Chrome driver, waits ten seconds per page, collects all anchor links with the ilan.gov.tr /ilan/ path, and discards URLs already in seen_jobs.json. Each unseen link is fetched with a three-second wait. The scraper Turkish-lowercases the whole page, checks for research-assistant terminology, then matches vocabulary lists for visual communication design or gastronomy. For positives it constructs a Telegram HTML alert containing a derived university name, broad field label and source link; for *all* inspected links, including nonmatches, it adds the URL to the seen list.

The [workflow](https://github.com/serdark/academic-jobs-scraper/blob/e221d512b0bc2061308fc1b618267d85370d0879/.github/workflows/schedule.yml) schedules frequent weekday and weekend runs, installs Selenium and requests unpinned, sets Telegram bot token/chat ID from GitHub Secrets, runs the script, stages seen_jobs.json, rebases on GitHub main and pushes a snapshot commit. Workflow concurrency is serialized by group scraper-group; repo writes are authorized via contents:write. No test step validates output correctness.

## 3. Data lineage, coverage and current snapshot

The [seen-jobs snapshot](https://github.com/serdark/academic-jobs-scraper/blob/e221d512b0bc2061308fc1b618267d85370d0879/seen_jobs.json) is a JSON array of **386 unique-looking stored URLs** at this revision (the count was determined by parsing all 386 array items; no live URLs were checked). These are **processed links**, not 386 successful notifications, doctoral offers, active jobs or applicant-eligible opportunities. No per-link scraped date, full employment requirements, alert status, failure reason, normalized posting ID, source snapshot hash, last_checked or expiry exists. The workflow's recent Action runs, including a Nov 11, 2026 run, concluded success; that shows the scheduled process executed without a reported CI failure, not that the crawler found valid open offers.

Only four pages are requested per run; there is no persisted page cursor, explicit source coverage counter or pagination termination condition. A broad site's new postings can escape this fixed window. The official Turkish government listing host is a strong initial source identity but its link text must still be checked against the exact employer announcement and specific position criteria.

## 4. Failure modes and alert reliability

- **False permanent deduplication:** links are appended to seen_history even if they do not meet the fields or if a Telegram send fails. The alert helper's [requests.post](https://github.com/serdark/academic-jobs-scraper/blob/e221d512b0bc2061308fc1b618267d85370d0879/scraper.py) does not check HTTP status, body, retry policy or timeout; an HTTP 400/429/5xx can be silently regarded as delivered. An exception in a processing iteration is swallowed and the item is not marked seen, leading to unbounded retry but no durable failure record.
- **Output injection:** untrusted page_title is concatenated into Telegram parse_mode HTML without escaping. The institution string could contain malformed markup or attacker-controlled HTML, causing rejected/misleading alert content. The URL comes from links collected under an ilan.gov.tr substring test rather than strict parsed host equality.
- **Silent scheduler failure:** the scraper main catches all exceptions without reporting failure, so GitHub Actions can show "success" even if no meaningful crawl occurred. Fixed 10s/3s sleeps and no navigation timeouts create unbounded end-to-end runtime under a large backlog.
- **Non-atomic persistence:** each run overwrites one JSON list without an atomic replace or per-item durable transaction. GitHub Action auto-commits state to main; rebase/push failure is not repaired by the script. No migration or data corruption recovery.
- **Filter scope error:** whole-body substring matches can select a job where "research assistant" and the design/gastronomy keywords refer to different positions on the same advertisement page; there is no table-row/job-level binding.
- **Policy/eligibility omission:** none of PhD registration, pay, funding, nationality, language, tuition or deadline is extracted or verified. The URL may continue being logged after the underlying posting closes.

## 5. Maintenance, security and checks

The repository was created September 2026; commits update the seen list through Nov 11. Issue/PR searches returned none. A Github Actions run succeeded on Nov 11 and earlier dates, but there is no separate automated testing beyond process execution. Secrets are referenced via workflow GitHub secrets and not embedded in the tracked Python file; no token value was accessed. A LICENSE file is absent at this snapshot, so reuse permissions are unspecified. Python 3.10 with Selenium and requests is set in the [workflow](https://github.com/serdark/academic-jobs-scraper/blob/e221d512b0bc2061308fc1b618267d85370d0879/.github/workflows/schedule.yml), not a version-locked packaging manifest.

## 6. Comparison and source-dependence

Relative to many academic job monitors, persistence of already-seen IDs and configured cron scheduling are operational assets. But the monotonic "seen" set conflates observed, filtered, delivered, and failed states. Compare this with a durable opportunity system: discovered URL -> fetched snapshot -> scoped job classification -> notification attempt with acknowledgment -> reviewed record -> explicit expiry. Re-running a source cannot be interpreted as confirming old vacancies remain active.

## 7. Transfer to PhD Atlas

Adapt the notion of a government source adapter, locale-aware Turkish case folding and scheduled bounded discovery. Replace its single seen set with typed stages and idempotency keys; enforce exact URL authority, conservative cross-page completeness, per-advertisement extraction and proof of successful messaging. Add critical dates and current applicant/funding gates. Never import seen_jobs.json as verified doctoral opportunities and do not send Telegram messages from research tests.

## 8. Evidence and execution boundary

Inspected all [source](https://github.com/serdark/academic-jobs-scraper/blob/e221d512b0bc2061308fc1b618267d85370d0879/scraper.py), [scheduled workflow](https://github.com/serdark/academic-jobs-scraper/blob/e221d512b0bc2061308fc1b618267d85370d0879/.github/workflows/schedule.yml), and [386-URL snapshot](https://github.com/serdark/academic-jobs-scraper/blob/e221d512b0bc2061308fc1b618267d85370d0879/seen_jobs.json); full tree, latest commit history, issue/PR listings and five upstream GitHub workflow run statuses. Did **not** execute Selenium, access Telegram, verify job pages or run an employment eligibility audit. Workflow success and static source behavior are reported separately. No secrets were extracted or exposed.
