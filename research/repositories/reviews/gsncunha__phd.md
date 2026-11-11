# GSNCunha/PHD — deep static repository review

**Reviewed:** 2026-11-12. **Pinned upstream:** [522edd796d4a51a722e2313b811c9ab05aabe3b2](https://github.com/GSNCunha/PHD/commit/522edd796d4a51a722e2313b811c9ab05aabe3b2).  
**Review state:** DEEP_REVIEW_DOCUMENTED; source audit, no live monitoring executed.  
**Verdict:** reference monitored-source grouping and no-send-on-failure handling; reject inference-only verification.

## 1. Purpose

A scheduled robotics/SLAM-focused PhD opportunity agent covering Alpine universities and selected European portals. It searches Serper/Google across enumerated university domains, reads two AcademicPositions RSS feeds, asks Gemini to assess the candidate fit and funding status, then alerts a user through Telegram. Research terms include autonomous navigation, robotics, ROS 2, SLAM, control and AI. This is a **lead monitor**, not a verified funded-position registry.

## 2. Architecture

The single `agente.py` module defines source domain registries, research profile, Serper search queries with `site:` filters and 60-day restriction, RSS parsing, Gemini JSON-format prompt, Telegram sender, and JSON link-history file. GitHub Actions schedules a daily Python 3.10 job and commits updated `seen_jobs.json` to the default branch. Secrets provide Gemini, Serper and Telegram credentials. The source contains five files and no independent test suite.

## 3. Retrieval and source coverage

Queries are batched in groups of ten hostnames and return up to ten Serper hits per query. Domain grouping does not imply exhaustive crawling, current publication or true host provenance; search snippets can include person profiles, archived jobs, curricula, events and irrelevant matches. Two RSS feeds are capped at ten entries each. No explicit coverage marker, source-page evidence, pagination cursor or official-call snapshot is retained. Search metadata alone cannot establish current doctoral position availability.

## 4. Model evaluation and false positives

Gemini receives the search result title/snippet and link, **not fetched official vacancy-page body**. The prompt requests `is_open_position`, `funded`, `deadline`, `score_match`, `recommend`, country and rationale. Returned JSON is extracted via a broad regular expression and is not schema-validated or independently checked.

Most importantly, `process_jobs` sends a Telegram alert if `recommend or is_alpine_source`. Any result originating from `"Alpine Domains"` bypasses the model's `recommend` gate even when `is_open_position` is false, the position is expired, or funding is negative. The output may label such a hit a target-university alert. This is an observed logic branch, not a measured false-positive rate.

## 5. Idempotency and delivery

Links are deduplicated with an append-only JSON set. The sender checks HTTP status 200 and returns a boolean. Successfully delivered recommendations are marked seen; failed deliveries are not marked, enabling retry. This is a stronger policy than “processed before delivered.”

However, model-rejected leads are also placed in the seen set forever, so later-valid opportunities sharing the URL or a revised listing cannot re-enter assessment. Empty/unexpected history content, URL redirects, new funding cycles and source edits have no version-aware observation. A send-accepted/commit-failed crash can still duplicate an alert. There is no transactional notification outbox.

## 6. Operational and security risks

Gemini quota retries are partly bounded, and each run evaluates only 20 unseen links. A popular irrelevant domain can exhaust that budget. A fixed four-second delay adds cost/latency. JSON output lacks strict validation; program behavior can raise errors for malformed nonnumeric scores. Secrets are external, but `seen_jobs.json` is committed back to the repository by CI, creating race/conflict risk with parallel maintainer pushes.

The static code mentions a `gemini-3.6-flash` model identifier; this review does not establish current availability, pricing or compatibility. No email or university application action is performed.

## 7. Evidence boundaries

Inspected `agente.py`, Actions workflow, requirements and state file. No real RSS fetch, Serper request, Gemini request, Telegram send or model quality experiment was performed. Presence of a link in `seen_jobs.json` is not proof that it was an open PhD position or passed official-source verification. The job file contains heterogeneous links including staff profiles and university announcements, supporting the need for stringent classification but not proving specific exposure.

Pinned evidence: [monitor](https://github.com/GSNCunha/PHD/blob/522edd796d4a51a722e2313b811c9ab05aabe3b2/agente.py), [workflow](https://github.com/GSNCunha/PHD/blob/522edd796d4a51a722e2313b811c9ab05aabe3b2/.github/workflows/agente.yml), [dependencies](https://github.com/GSNCunha/PHD/blob/522edd796d4a51a722e2313b811c9ab05aabe3b2/requirements.txt).

## 8. Transfer decision

Use a bounded multi-source discovery scheduler with separate source classes, but enforce `is_official_current_call AND funded_for_applicant AND deadline_open` for the verified-opportunity state. Preserve `UNKNOWN` where source lacks evidence. Treat university-domain matches as priority for *manual review*, not automatic recommended openings. Store exact source snapshots, checked time, claim-level evidence, source URL/cycle and update-aware deduplication. Send only after validation and maintain receipt-backed notification history.
