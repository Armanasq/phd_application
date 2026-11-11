# putrosm/scholarship-ummanitarian — deep static repository review

**Reviewed:** 2026-11-12. **Pinned upstream:** [043f0d8681d394c8306a1a7d6530558ded87caae](https://github.com/putrosm/scholarship-ummanitarian/commit/043f0d8681d394c8306a1a7d6530558ded87caae).  
**State:** DEEP_REVIEW_DOCUMENTED — source/workflow review; no GitHub Actions, DeepSeek, Telegram or Cloudflare execution.  
**Verdict:** do not adopt as a verified funded-PhD feed; useful example of evolving human-approval vs automation tradeoff.

## 1. Intended domain

An Indonesian-language niche PhD scholarship catalogue focusing on humanitarian studies, conflict health, IHL, global health and disaster management. Its stack comprises a static Cloudflare Pages frontend, GitHub Actions schedules, Python source crawler, DeepSeek text generation, Telegram messaging/approval scripts and Git-tracked JSON state. The README and earlier `AGENTS.md` describe human approval before publication; a newer handover describes a migration to direct automatic publication.

## 2. Actual deployed-path source logic

The inspected `weekly-source.yml` calls `scripts/source.py`, stages **only** `data/scholarships.json`, commits changes, and deploys to Cloudflare Pages. It does **not** call `notify_telegram.py`, `poll_approve.py` or load pending approvals. The source script sets every new record's `review_status` directly to `approved`. The GitHub workflow implementation therefore supports **direct auto-publication**, consistent with the later handover but contradictory to the older `AGENTS.md` approval flow. Both `daily-poll.yml` and its cron remain in the tracked tree; the handover claims daily polling is disabled, but workflow-file presence alone cannot establish GitHub's enabled/disabled workflow state. That operational status was not verified.

## 3. Source discovery and “knowledge fallback”

`SOURCES` includes official funder/university pages and aggregators; some university entries are intentionally `fetch=False`. For fetchable pages the script requests HTML and strips navigation/styles, then sends up to 5,000 characters of page content to DeepSeek. If a page fails or yields under 200 characters, the script calls `extract_from_knowledge(source_name)` instead, prompting the model to **list 3–6 scholarships it believes exist** using model knowledge. There is no official-source retrieval or independently verifiable evidence in that fallback.

Any such generated award can be written with a program title, funding type, country, official link guessed by the model, and `review_status="approved"`. This is a strong epistemic failure: model familiarity and generated URLs are not proof of current awards or international PhD eligibility.

## 4. Verification and temporal semantics

The fetch helper returns stripped HTML without checking `response.raise_for_status()` or validating an official domain after redirect. HTTP error or CAPTCHA content can enter the extraction path. The model's JSON output is only required to be a top-level list; no Pydantic/schema validation, official URL check, evidence quote, award-year confirmation, current-cycle validity or applicant-specific nationality restriction is enforced before auto-publication. The handover claims a set of HTTP-200-checked links, but no such verification contract was demonstrated in the current source path.

`compute_status` parses date-only strings with server-local `datetime.now()`, interpreting missing/unparsable deadlines as `Unknown` and still allowing them to publish. A date-only deadline at midnight can be marked expired early relative to a source's local closing time. A null deadline is **not** evidence of an open call.

## 5. Identity and duplicates

Opportunity IDs are the first 12 hex digits of MD5 on normalized title and university. This gives deterministic identities, but reissues with identical names in a new cycle are suppressed indefinitely via `existing_ids`; edits to funding/deadline cannot update an old record. The script appends new entries and rewrites `scholarships.json` directly without atomic replace, schema migration, revision snapshot or reconciliation when an award expires.

The additional `key_figures` list is generated from model knowledge of researchers at a university, without fetching each faculty's profile URL or confirming current recruitment. It is not a verified supervisor directory.

## 6. Human approval and message durability

Legacy scripts implement Telegram approve/reject callbacks and an update-ID cursor; however the current weekly path bypasses those scripts. Even the legacy `notify_telegram.py` marks messages as sent after calling `requests.post` **without checking its status or body**, so Telegram API errors could permanently suppress an unreviewed item. `poll_approve.py` writes three JSON files directly and separately, without a transaction or atomic checkpoint, allowing partial state after process interruption.

The direct publication choice reduces reviewer friction but removes the last independent correctness gate from low-trust AI extraction.

## 7. Licensing, security, operations and evidence boundary

The project uses repository secrets for DeepSeek, Telegram and Cloudflare credentials; no secret value is quoted here. Both workflows can commit state and push to `main` and may collide with simultaneous maintainers; the static code does not establish a concurrency lock across workflows. Documentation includes operator configuration and detailed internal steps which should be reviewed for privacy if republished. This audit inspected all relevant code, workflows, README, `AGENTS.md`, handover and source tree, but did not call any API, download the live catalogue, verify funding notices or test deployment. No external application was submitted.

Pinned evidence: [weekly workflow](https://github.com/putrosm/scholarship-ummanitarian/blob/043f0d8681d394c8306a1a7d6530558ded87caae/.github/workflows/weekly-source.yml), [source job](https://github.com/putrosm/scholarship-ummanitarian/blob/043f0d8681d394c8306a1a7d6530558ded87caae/scripts/source.py), [legacy notify](https://github.com/putrosm/scholarship-ummanitarian/blob/043f0d8681d394c8306a1a7d6530558ded87caae/scripts/notify_telegram.py), [approval poll](https://github.com/putrosm/scholarship-ummanitarian/blob/043f0d8681d394c8306a1a7d6530558ded87caae/scripts/poll_approve.py), [handover](https://github.com/putrosm/scholarship-ummanitarian/blob/043f0d8681d394c8306a1a7d6530558ded87caae/HANDOVER.md), [AGENTS.md](https://github.com/putrosm/scholarship-ummanitarian/blob/043f0d8681d394c8306a1a7d6530558ded87caae/AGENTS.md).

## 8. PhD Atlas transfer decision

Use source-specific scheduled collection and a human-verification decision trail, but prohibit model-knowledge fallback records from entering a **verified opportunity** register. Preserve official source URL, exact evidence excerpt, date checked, award cycle, funder, degree/applicant class, funding components, and supervisor identity separately. Gate publication on source integrity and human review, add idempotent notification outbox, incremental source history, strict schema checks and atomic storage/merge. Treat no-deadline as Unknown rather than open.
