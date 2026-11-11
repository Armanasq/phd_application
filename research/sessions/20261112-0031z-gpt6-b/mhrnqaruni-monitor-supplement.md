# Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor — independent static supplement

**Reviewed:** 2026-11-12  
**Upstream:** https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor  
**Pinned source:** `b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9` (Git tree `48b24fb9ab305d7ad06c7ce57f29551af289fcbe`)  
**Canonical review:** [`research/repositories/reviews/mhrnqaruni__ai-agent-skill-phd-scholarship-monitor.md`](../../../repositories/reviews/mhrnqaruni__ai-agent-skill-phd-scholarship-monitor.md) — already merged by another agent as `DEEP_REVIEW_DOCUMENTED`.  
**Status:** SUPPLEMENTAL_STATIC_FINDINGS; the canonical report remains the primary review; no runtime or vacancy verification.

## 1. Scope of independent additional inspection

Examined the 2,934-line [Python state engine](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py), complete skill workflow, source/verification/scoring/recurrence/security policies, the 848-line [unit-test file](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/tests/test_phd_tracker.py), and the Ubuntu/Windows [CI workflow](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/.github/workflows/validate.yml). The published CI [run 31703647407](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/actions/runs/31703647407) passed at the pinned commit; no local execution was performed.

## 2. Reviewer independence versus review-hash correctness

[`candidate_review_subject_hash`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L1695-L1716) binds the candidate/evidence packet to config, CV and profile hashes. [`validate_review`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L1716-L1760) requires a matching digest, review timestamp, verdict, reviewer ID and a mode of either `INDEPENDENT_AGENT` or `SELF_SECOND_PASS`. [`derive_decision`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L1950-L2108) requires `PASS` but does **not** require independent mode.

The [skill itself](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/SKILL.md#L63-L65) explicitly permits self-review if a separate verifier is unavailable, while its introductory publication claim refers to independent verification. A self-review can therefore publish. A hash prevents reuse of the wrong packet; it cannot prove verifier independence, reviewer honesty or actual page contents.

**Transfer:** store reviewer type distinctly (`SELF_REVIEWED` vs `INDEPENDENT`), authenticate distinct actor identity when required, and require actual source-bound attestations rather than accepting caller-provided reviewer labels as proof.

## 3. Source evidence/officialness and coverage are caller assertions

[`validate_evidence`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L1666-L1695) checks nonempty summary, URL, timestamp, fact and declared authority enum; it does not fetch the official webpage or prove the page supports the stated funding/deadline/eligibility fact. [`authoritative_fact_present`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L1943-L1950) trusts the declared `PRIMARY`/`AUTHORIZED_ATS` value. [`normalize_coverage`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L2361-L2474) downgrades country completeness for missing or unsuccessful required-source URLs but accepts the submitted statuses/timestamps rather than performing a crawl.

The source-research discipline lives in the *executing agent*, outside this state manager. Passing gates certifies packet **internal consistency**, not actual current vacancies. A reliable source verification layer needs officially established institution host mappings, fetched page snapshots, redirect chains, field-level evidence spans and cycle/date scope.

## 4. Configurable thresholds and date treatment

The default config sets fit score threshold 80 and verification-confidence floor 85. [`validate_config`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L481-L615) enforces fit threshold 80–100 but permits a confidence floor of 0–100. Describing all published results as “85+ confidence” would be incorrect for modified configurations; in any case these values are **not empirical acceptance probabilities**.

[`deadline_expired`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L309-L331) treats a date-only deadline as valid through its local calendar date in the configured timezone, while offset-bearing datetime deadlines use exact instants. [`earliest_deadline`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L338-L345) compares separate mandatory programme/funding deadlines. The distinction is good; the configured timezone still needs alignment with the institution's published deadline zone.

## 5. Identity and concurrent state

[`find_identity_signals`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L1422-L1460) looks for official ID+authority, canonical URL, aliases and strong record ID. Fingerprints flag a candidate duplicate but do not automatically merge. [`validate_existing_record_update`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L1461-L1507) requires an expected prior content hash for explicit updates and preserves core university/country/official-ID identity.

The [run lock](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L1033-L1081) uses exclusive file creation and a stale lock archive; [run-start](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L1200-L1312) backs up SQLite, snapshots CV/config/profile hashes and prevents mixed-run inputs. [`candidate-upsert`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L2108-L2353) commits records, aliases, evaluations and audit events transactionally. These are strong local-first state-control patterns, but not distributed multi-writer coordination.

## 6. Output and data safety

CSV export uses UTF-8 BOM, temporary-file replacement and [formula-prefix neutralization](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L353-L368) to mitigate spreadsheet injection; `ever_published` preserves prior qualified rows after the position's status changes. The skill keeps CVs outside the public repo, avoids automatic submissions, and requires manually reviewed baseline before scheduling. No actual scheduled task or live source search was executed here.

## 7. Separate evidence and fit semantics

The score is a fixed **35/25/20/15/5** rubric (topic, methods, experience, preparation, preferences). [`validate_score`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9/skills/monitor-phd-scholarships/scripts/phd_tracker.py#L1644-L1665) checks arithmetic and presence of explanation, not whether the cited projects/results actually match. A fit score should remain downstream of independently verified factual eligibility; a high score is never evidence of supervisor acceptance or funding commitment.

## 8. Final supplemental disposition

Keep the already-merged canonical deep audit. Add this document solely to preserve independently observed reviewer-mode loophole, threshold configurability, and trust boundary between state validation and external official-source verification. No third-party runtime tests, credentials or user CV were used; no current funded vacancy was independently verified.
