# Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor — eight-section static source review

**Upstream revision:** `b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9`; **inspected:** 2026-11-12; **review:** DEEP_REVIEW_DOCUMENTED; **runtime validation:** NOT_PERFORMED; **source action:** READ_ONLY.

## 1. Research objective and candidacy scope

This Python/Codex package targets funded doctoral opportunity discovery against a user-confirmed applicant profile. Unlike general scholarship aggregators, it explicitly separates doctoral identity, official application route, applicable deadlines, stipend/tuition terms, eligibility gates, country scope and academic match. It forbids interpreting its scoring percentage as admission probability. The README's scheduling and live-source claims describe a prescribed workflow, not an empirical result from this audit.

## 2. Pinned source architecture

The 26-entry tree contains a public agent specification, security/verification/data-contract reference files, one standard-library Python tracker (~129 kB), unittest files and a GitHub validation workflow. The tracker implements CLI init, validate, run-start, due, lookup, touch, review-subject, candidate-upsert, run-finish/abort, export and stats. A private workspace holds the CV, confirmed profile, SQLite DB, snapshot-backed output, logs and backups. Config-driven country source lists can express full, partial and failed coverage.

## 3. Data model, migrations and transactional behavior

The code uses SQLite PRAGMA user_version with explicit upgrades from v1→v2→v3, separate run/evaluation/opportunity tables, identity/alias keys, first-seen timestamps, input hashes, update-content optimistic concurrency and an append-only evaluation history. run-start uses an exclusive O_CREAT|O_EXCL lock and a database backup; stale locks are archived, and concurrent active runs rejected. The tracker enforces unchanged CV/profile/config hashes through a run. It uses an atomic filesystem replacement for exported CSV/JSON and a transaction to finalize a run. These mechanisms are source-inspected, not stress-tested.

## 4. Verification gating and temporal precision

Verification-and-scoring.md names mandatory official facts (OFFICIAL_POSTING, DEADLINE, FUNDING, ELIGIBILITY, APPLICATION), explicitly holds unknown/conflicted values, separates funding models and component deadlines, and defines earliest mandatory date. The implementation parses date-only and offset-bearing timestamps, respects configured IANA zones for date-only expiry, rejects older-than-limit evidence timestamps and binds critical review to a SHA-256 digest of candidate evidence and run context. A score threshold only applies after material gates pass.

## 5. Correctness and provenance risks

A self-reported packet can label an arbitrary URL/summary as authority=PRIMARY and provide its own checked_at timestamp; validate_evidence checks structure, temporal age, URL syntax and authority enum, not independently whether that webpage actually asserts the claim. The source can help a supervised verification workflow enforce evidence shape, but it is not an autonomous guarantee of official facts. normalize_url accepts http as well as https (perhaps necessary for metadata, but not sufficient transport provenance). A reviewer_id and content hash are review-traceability fields, not proof an independent human checked the page. Reviewer independence is a process requirement external to the code.

## 6. Tests, execution and security

tests/test_phd_tracker.py uses isolated temporary workspaces with fake official.example sources and exercises init/config/profile, source-status coverage, decision gates, state transitions and backup behavior. Test content and workflow were inspected, but NO tests, actual site fetches, scheduler, applicant eligibility check or system integration run occurred here. Security policy avoids public CV storage, account creation, CAPTCHA bypass, unsolicited email and unapproved application submissions. It treats third-party vacancy pages as untrusted prompt input.

## 7. Interconnections and applicability

Strongest reference so far for source-aware memory and repeatable funding screening; complements source-specific scrapers (ScholarTrack, Hypatia) and local application case management (Application Atlas). Particularly relevant to current internal issue #5 (SQLite versioning, row integrity, snapshot provenance) and issue #4 (separate public research data from private applicant evidence). Keep official vacancy evidence distinct from manually supplied matching scores, generated research narratives and any user-entered contact status.

## 8. Adoption verdict and evidence

DEEP_REVIEW_DOCUMENTED (static source-level, NOT runtime validated). Adopt conceptual hard gates, explicit unknowns, source coverage, immutable run snapshots, typed deadline zones, crash-safe exports and reviewer hash binding. For deployment require official-host provenance checks or human-reviewed primary citations, adversarial fixtures and isolated dry-runs before scheduled sweeps. [README](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/README.md); [tracker source](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py); [verification contract](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/references/verification-and-scoring.md); [security policy](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/references/security-and-failure-policy.md); [tests](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/tests/test_phd_tracker.py).
