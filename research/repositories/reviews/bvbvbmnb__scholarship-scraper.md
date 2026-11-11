# bvbvbmnb/scholarship-scraper — deep static source review

**Review date:** 2026-11-12  
**Pinned commit:** [5338303f943b67decef6678b23f0d17ed5536bf3](https://github.com/bvbvbmnb/scholarship-scraper/commit/5338303f943b67decef6678b23f0d17ed5536bf3)  
**Classification:** DEEP_REVIEW_DOCUMENTED (static source and workflow audit, runtime NOT_RUN).  
**Disposition:** adapt monitoring workflow concepts only; do not trust extracted eligibility/deadlines without official evidence.  
**Scope:** complete five-file tree, full `main.py`, GitHub Actions workflow, dependencies, state-file format, commit history, issue/PR history; current Telegram pages, Google search responses and delivery were not exercised.

## 1. Product and source scope

A small scheduled scholarship lead-monitoring bot. It reads public `t.me/s/` preview pages from an enumerated set of Telegram channels, extracts HTML text, asks Google's Gemini model (configured with a search tool) to produce an English scholarship summary/card, and sends the draft card to an administrator's Telegram chat for manual forwarding. The monitored messages may describe bachelor's, master's, PhD or fellowship opportunities; there is no verified doctoral-only source filter.

## 2. Runtime architecture and control plane

GitHub Actions runs `main.py` on a five-minute cron and offers manual dispatch. Workflow-level concurrency prevents overlapping scheduled jobs in one concurrency group. It installs Python 3.13 and three unpinned packages: `python-dotenv`, `requests`, `google-genai`. Four required credentials/settings are injected through GitHub secrets. The script creates a Google GenAI client and `requests.Session`, iterates channels, constructs candidate cards and writes a JSON fingerprint register (`processed_posts.json`). The workflow commits that register back to its own default branch after runs.

The code defines `DESTINATION_CHANNEL` but does not use it to send; it sends approval cards to `ADMIN_USER_ID`. The project therefore implements *operator-assisted drafting*, not automated publication to a target channel.

## 3. Discovery completeness defects

- Each monitored channel is reduced to `latest_raw_msg = msg_blocks[-1]`. Other messages posted between scheduled runs are not processed; the result is a sample of one message per channel, not complete Telegram monitoring.
- HTML is split using a regular expression matching message-text `div` blocks. Nested HTML and layout changes can truncate content or miss messages entirely. Markdown/HTML entity normalization and stable Telegram message IDs are not preserved.
- The monitor has no cursor by channel and no pagination checkpoint. Reaching only a preview window loses messages outside the page; full history or reliable incremental completeness is not established.
- A SHA-256 fingerprint is computed over plain stripped text, not a stable `(channel, message_id)` identity. Two different posts with identical text collide, and edits generate new pseudo-identity without explicit revision handling.

## 4. State and exactly-once delivery defects

The job adds a post hash to `processed_posts` **before** calling Gemini and before sending the admin message. Model error, parse error or delivery failure may therefore permanently suppress the lead after the state file is saved.

`send_telegram_message()` ignores HTTP status and response body; it catches transport exceptions and returns no success indicator. On a Telegram 429, 4xx or 5xx response, the caller still treats the hash as processed. An exception is logged but does not unmark the hash. A crash before the final state save has the opposite effect: delivery may already have occurred, followed by repeat delivery on restart.

The state retention path `list(processed)[-3000:]` does not preserve chronological recency. A Python `set` has no insertion-time ordering contract, so the advertised “most recent” cap is not implemented. Old posts may reappear after arbitrary eviction.

**Required state machine:** `DISCOVERED -> FETCHED -> EXTRACTED -> PENDING_REVIEW -> DELIVERED/ACKNOWLEDGED` with durable job IDs, retry count, idempotency key, delivery receipt/HTTP response and backoff. Retain timestamped identifiers rather than trimming a set.

## 5. LLM inference and evidence quality

The system prompt asks Gemini to use Google Search to verify IELTS and application-fee requirements and to omit expired/not-yet-open calls. This instruction is not backed by a stored source citation, retrieval artifact, evidence span, verifier output, or independent official-source confirmation. The model-generated card is treated as a printable paragraph, not a structured, validated claim set.

The prompt contains a fixed “current year is 2026.” It will become stale next year even if the scheduler continues. Deadline timezone, admission cycle, nationality requirements, fee waivers and full funding components are not represented. The code uses the string test `"SKIP:" in generated_card`; malformed or model-noncompliant output can be sent as though verified.

Telegram posts are untrusted user-generated content. They can include inaccurate offers, fake official links or prompt-injection instructions. Google search availability does not independently prove eligibility or authorization to apply.

## 6. Security, operations and privacy

Secrets are provided via GitHub Actions secrets rather than committed literal tokens. However, dependency versions are unpinned and there is no visible test suite. A proxy URL can be configured; the code logs its host string after splitting on `@`, so logging should avoid userinfo and sensitive query components altogether.

The workflow commits mutable state every run and could race with concurrent independent pushes to the default branch despite the workflow concurrency group (which protects only its own runs). A push conflict leaves the processed-state file uncommitted in that run. Storage as a growing Git-tracked JSON file is operationally brittle; use a protected database or Actions artifact store with atomic updates and bounded retention.

An operator review is conceptually useful: this design deliberately sends a draft to an admin rather than sending directly to applicants or submitting applications. Human approval must still see original source, verifier evidence, and current official application details.

## 7. Tests, history and verification boundaries

The pinned project has five tracked files, many automated state-update commits, no README or license file, and no recorded unit-test or CI test job in the inspected tree. The scheduled Actions workflow is evidence of a configured schedule, not evidence that current Telegram sources or Gemini calls succeed. The stored hash corpus is not independently verified content. This audit did not execute the script, access a bot token, send a message or validate a vacancy.

## 8. PhD Atlas transfer decision

Adopt separate discovery and human-approval stages and scheduled source monitoring. Reject the implementation's one-message-per-channel assumption, fragile HTML regex, processed-before-delivered state transition and unverified generative “verified” fields. Add per-source cursor, stable upstream message ID, authority class, exact official URL, cycle/deadline/funding claim evidence, schema validation, delivery outbox, idempotent retries, and explicit source failure states.

**Adoption priority:** P2, only after safer design. Telegram should remain a low-trust lead source.

### Pinned code evidence

- [Core monitor](https://github.com/bvbvbmnb/scholarship-scraper/blob/5338303f943b67decef6678b23f0d17ed5536bf3/main.py)
- [Scheduled workflow](https://github.com/bvbvbmnb/scholarship-scraper/blob/5338303f943b67decef6678b23f0d17ed5536bf3/.github/workflows/scraper.yml)
- [Dependencies](https://github.com/bvbvbmnb/scholarship-scraper/blob/5338303f943b67decef6678b23f0d17ed5536bf3/requirements.txt)
- [Persistent hash state](https://github.com/bvbvbmnb/scholarship-scraper/blob/5338303f943b67decef6678b23f0d17ed5536bf3/processed_posts.json)
