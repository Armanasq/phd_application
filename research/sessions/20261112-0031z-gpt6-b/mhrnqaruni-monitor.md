# Deep static repository audit — Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor

**Reviewed:** 2026-11-12  
**Upstream:** https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor  
**Pinned main commit:** [`b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/commit/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9)  
**Git tree SHA:** `48b24fb9ab305d7ad06c7ce57f29551af289fcbe`  
**Scope:** DEEP_STATIC_REVIEW_COMPLETE for skill contract, state engine, critical gates, tests and CI; LIVE_SEARCH/EXECUTION_NOT_PERFORMED.  
**Decision:** ADAPT_DETERMINISTIC_GATE_AND_AUDIT_DESIGN; DO_NOT_TREAT_PACKET_EVIDENCE_AS_INDEPENDENTLY_VERIFIED.

## 1. Purpose, scope, and repository inventory

A portable Codex skill for daily discovery of genuinely funded doctoral vacancies, scored against a user-confirmed private CV/profile. It is a **workflow description plus a local state-management engine**, not a bundled autonomous web crawler or a guarantee that sources are independently checked.

The repository contains 26 recursive tree entries (18 blobs), including:
- [`SKILL.md`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/SKILL.md) and agent metadata;
- reference policies for applicant intake, coverage/source selection, reviewer scoring, state, scheduling, security and data contracts;
- [`phd_tracker.py`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py), a ~2,934-line Python standard-library SQLite state engine;
- [`tests/test_phd_tracker.py`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/tests/test_phd_tracker.py) and [`tests/test_skill_structure.py`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/tests/test_skill_structure.py);
- GitHub Actions [`validate.yml`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/.github/workflows/validate.yml) for Python 3.11 on Ubuntu and Windows.

Latest main commit is 2026-08-13. GitHub returned no issues or pull requests. The latest source-pinned `Validate skill` Actions run [31703647407](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/actions/runs/31703647407) finished successfully. This is evidence of a passing *source/unit* gate at that commit, not proof that any external vacancy has been independently verified.

## 2. Workflow and data ownership

The skill requires a user-confirmed profile extracted from a private CV, a configured country list, local IANA timezone, funding policy and source registry, and a manually reviewed baseline before permitting a recurring schedule.

A daily run follows:
1. Validate configuration, confirmed profile, local DB and CV inventory hash.
2. Acquire a single-run lock, make SQLite backup, register the run and its scope.
3. Retrieve due candidates, query configured country/source groups through the **executing agent's** web capabilities (not the Python script).
4. Normalize candidate fields, direct sources and review packet.
5. Apply deterministic eligibility, deadline, funding and country gates.
6. Compute candidate/CV/profile/config-bound review subject hash.
7. Obtain another verifier agent when available, otherwise perform a separately identified self-review.
8. Upsert evidence, decision, state history and aliases to SQLite.
9. Record complete, partial or failed coverage by country and required source URL.
10. Regenerate a cumulative spreadsheet-safe CSV, daily report and machine-readable log.

No automatic application submission, faculty email, personal-document upload or account registration is part of the authorized workflow.

## 3. Typed facts and deterministic gate semantics

[`phd_tracker.py`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py) defines explicit enums for:
- doctoral identity (`CONFIRMED`, `NOT_DOCTORAL`, `UNKNOWN`, `CONFLICT`);
- deadline precision (`DATE`, `DATETIME`, `ROLLING`, `UNKNOWN`) and lifecycle;
- funding route (`SALARY`, `PROJECT_ATTACHED`, `GUARANTEED_PROGRAM`, `AUTOMATIC_CONSIDERATION`, `SEPARATE_APPLICATION`, `COMPETITIVE`, `SELF_FUNDED`, `UNKNOWN`);
- funding verification and personal eligibility;
- tuition, stipend and international-fee coverage (`FULL`, `PARTIAL`, `NONE`, `NOT_APPLICABLE`, `UNKNOWN`);
- evidence fact types and authority levels;
- review modes and verdicts.

Its `derive_decision` enforces:
- in-scope host country, confirmed doctoral status, official posting and application URL;
- open/rolling deadline and the earliest of programme/funding deadlines;
- dated evidence for required claim types;
- accepted funding route, tuition/stipend/international fee coverage and optionally a configured amount/currency/period;
- confirmed eligibility and minimum application lead time;
- separate funding and doctoral deadlines where separate scholarship application is required;
- verification-confidence minimum and a fit score threshold at least 80;
- a PASS review with relevant explanation and recorded primary risk.

Unknown/conflicting load-bearing facts are held. Explicit authoritative disqualifiers cause rejection. A candidate scoring below 80 is retained internally, not published. The default confidence floor is 85/100; configuration validation allows 0–100, so a user may lower it to 0. This is a configurable gate, not universally enforced “independent 85% certainty”.

The fit rubric is exactly **35 topic + 25 methods + 20 research experience + 15 academic preparation + 5 preferences = 100 points**. Component fields must be numerical within their maxima and have explanation strings. This score is a subjective fit score, **not** admission or funding probability and not calibrated to historical outcomes.

## 4. Strong identity, persistence and recovery patterns

### 4.1 Multi-signal deduplication

A strong identity is established with existing `record_id`, official requisition ID scoped to an authority key, exact normalized URL, or known URL alias. A separate fingerprint uses normalized university, title/topic, department, place, supervisor and application cycle to **flag potential duplicates**; it does not silently merge them.

Explicit `record_id` updates require `expected_prior_content_hash`, preventing a stale caller from replacing newer content. Updates cannot silently change the canonical institution/country or remove an established official ID. Ambiguous fingerprints require a recorded `DISTINCT` review before opening a separate record.

Caveat: a caller-provided `authority_key` may override the derived authority identity. Official-ID identity is only as reliable as the provenance of the upstream institution/host mapping; the Python engine cannot certify that input on its own.

### 4.2 Evidence, state and review history

The engine has an SQLite schema version 3, with `runs`, `opportunities`, `aliases`, `evaluations`, `run_events` and `metadata` tables. Each evaluation and decision is appended, preserving the chronological rationale and hash.

First-seen, last-seen, last-verified, last-changed and first-published timestamps are distinct. A completed profile/CV change forces re-evaluation of relevant candidates and new confirmation. Past published results remain in the cumulative export even after expiry, scope exit or loss of fit, with current status updated.

### 4.3 Run isolation and atomicity

- `acquire_run_lock` uses exclusive `os.open(O_CREAT|O_EXCL)` and rejects an active lock; stale-lock recovery archives prior state.
- `run-start` creates a `sqlite3.Connection.backup()` snapshot before updates.
- Every live command checks immutable `config_hash`, `profile_hash`, and `cv_hash` against the recorded run snapshot.
- SQLite writes are committed transactionally; exporting/reports uses temporary files and atomic replacement.
- The script refuses unknown newer schema versions and includes migration paths from versions 1 and 2 to 3.
- A locked Excel CSV does not replace canonical SQLite with an older version; the export failure is visible.
- Source failures lower coverage but **must not be interpreted as proof that an opportunity closed**.

### 4.4 Safe presentation and recurrence

The report renderer escapes untrusted Markdown/HTML-like content. CSV export is UTF-8 with BOM and neutralizes leading `=`, `+`, `-`, `@` and whitespace-prefixed spreadsheet formula payloads. The scheduled workflow is intentionally local and must use one persistent workspace owner, after user review of a manual baseline.

## 5. Central evidence weakness: metadata checks are not source verification

[`validate_evidence`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L1666-L1695) verifies **structure**, timestamps, declared authority enums, nonempty summaries and URL syntax. It **does not fetch the claimed webpage**, establish the site belongs to the institution, compare supporting quotes to source text, or prove the claimed information is from the correct cycle.

[`authoritative_fact_present`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L1943-L1950) accepts any packet evidence item whose caller-supplied `fact` and `authority` match configured strings (`PRIMARY` or `AUTHORIZED_ATS`). Thus deterministic policy gates can be satisfied by an incorrectly classified source, absent real external verification by the agent.

The source policy *instructs* the executing agent to verify official postings and source hierarchy; this is a sound operational intention but **not an implementation-enforced proof**. A passing SQLite decision demonstrates only that the **submitted packet** satisfied deterministic conditions.

**Required strengthening:** server-fetched, tamper-evident source snapshots with normalized institution-domain registry, actual source URI/redirect/DNS verification, field-level quote or extraction spans, correct vacancy/cycle identifiers and distinct verified-at times. Institution-authorized ATS provenance must be established by an official employer link, not an arbitrary boolean or enum.

## 6. Second review is hash-bound but need not be independent

[`candidate_review_subject_hash`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L1695-L1716) hashes the normalized candidate packet and CV/profile/configuration context. [`validate_review`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L1716-L1760) enforces a matching 64-character hash, recent timestamp, nonempty reviewer ID, `PASS/HOLD/FAIL` and one of `INDEPENDENT_AGENT` or `SELF_SECOND_PASS`.

Crucially, the persisted review mode can be **`SELF_SECOND_PASS`** and `derive_decision` accepts `PASS` in this mode. Nothing independently proves the reviewer identity or checks that a separate agent reviewed it. The [skill instructions](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/SKILL.md#L63-L66) explicitly permit self-review when another agent is unavailable, despite the opening claim “publish only ... independent verification”.

Therefore:
- hash binding **prevents accidental replay of a past review across changed packets**;
- it **does not authenticate** reviewer independence, source truth, or actual review quality;
- “independently reviewed matches only” in README/skill introduction is stronger than what code enforces.

A defensible system must distinguish `SELF_REVIEWED` from `INDEPENDENT_AGENT_REVIEWED`; if true independence is a publication requirement, publication must reject self mode or require a separate evidence attestations/actor identity.

## 7. Operational limitations and edge cases

1. **HTTP allowed:** `normalize_url` accepts `http:` as well as `https:` for all recorded links. This is permissive for source identities; the script does not fetch URLs itself. Require HTTPS and verified official host for publication-critical claims.
2. **Authority values supplied by agent:** the script validates enum membership, not domain provenance; a configured source registry records exact URL matching but a caller can still falsely claim that a URL was checked.
3. **Coverage assertions are packet-derived:** `normalize_coverage` downgrades a COMPLETE claim if no source, failed source, or missing required source URL. However, success/status/timestamp are caller-supplied; it does not itself execute the source search. COMPLETE denotes consistency with the **declared** sweep, not an independent internet crawl.
4. **Time semantics:** date-only deadlines are treated as inclusive local calendar days; offset-bearing datetimes are absolute; an `OPEN_UNTIL_FILLED` status conflicts with fixed closing components. This is better than arbitrarily converting date-only records to UTC, but default timezone may differ from the employer's local timezone if not explicitly supplied.
5. **No guarantee of recruitment truth:** verified funding and applicant eligibility are determined by the external agent's interpretation of official policy and user-confirmed profile. There is no live official job validation in the state engine.
6. **Single local writer:** lock/backup design is appropriate for one machine; no distributed coordination or multi-device synchronization. The skill explicitly warns against concurrent writers to cloud-synced SQLite.
7. **Review and score confidences are not calibrated:** a 0–100 model/human input is not an empirically validated chance of funding or admission.
8. **External scheduling prerequisites:** source workflows require desktop task support, computer availability and workspace access. A saved prompt does not, by itself, guarantee the scheduled task exists or ran.
9. **Tests:** unit tests include threshold, funding unknown, source coverage, URL identity, change detection, profile/CV hash drift, expired deadlines, formula injection, review replay, locks and schema upgrades. The passing CI covers syntax/unit behavior on Python 3.11 Windows and Ubuntu; no live 2026/27 vacancy acceptance dataset was observed.

## 8. Engineering transfer to `phd_application`

**Adopt or adapt:**
1. Hard-gate semantic states separating confirmed funding, competitive consideration, eligibility, deadline and country from fit ranking.
2. Two distinct date sources (programme and separate funding), local timezone and effective earliest deadline.
3. Immutable first-seen/first-published timestamps and append-only evaluations even when a candidate later expires or becomes out of scope.
4. Multi-signal identity: official requisition scoped to employer, normalized URL aliases and ambiguous fingerprint review.
5. Content-hash optimistic concurrency and CV/profile/config-snapshot drift detection.
6. Country/source coverage completeness distinct from “no matches” and failure.
7. CSV formula neutralization and controlled local data ownership.
8. Baseline approval before recurring monitoring and no automatic submissions.

**Do not copy unchanged:**
1. Self-reported `PRIMARY`/ATS authority as source authentication.
2. Accepting `SELF_SECOND_PASS` while reporting “independently reviewed only”.
3. Source-coverage status as proof of external site traversal.
4. Uncalibrated match/confidence scores as probability or verification proof.
5. Arbitrary HTTP links as authoritative employer sources.

### Cross-repository synthesis

Compared with the command center and PhD Atlas:
- this monitor has the strongest **deterministic eligibility/funding/date + review-hash + candidate state machine** among these specific examined workflows;
- the command center has clearer **personal application document storage and forward-only Alembic migration protections**;
- PhD Atlas has more developed **server-side official-page crawling, DNS/host controls and agent authorization**, although its own lexical claim verification is not full entailment.

The research platform should combine the strengths: actual captured source evidence `→` field-scoped independent factual verification `→` deterministic hard gates `→` fit assessment `→` explicit user action. The state engine alone cannot certify upstream facts.

**Final status:** DEEP_STATIC_REVIEW_COMPLETE for enumerated source paths; NO_LIVE_SEARCH, NO_LOCAL_TEST_EXECUTION, NO_PERSONAL_CV_PROCESSING, NO_INDEPENDENT_SOURCE_VERIFICATION. No current funded position or admission result was established by reviewing this repository.
