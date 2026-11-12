# ummanitarian/scholarship-ummanitarian — deep static code audit

**Source:** https://github.com/ummanitarian/scholarship-ummanitarian. **Pinned Git tree SHA:** `b5055158b2fc1f7c0b3ad58ece27e141ba294dc0` ([tree](https://api.github.com/repos/ummanitarian/scholarship-ummanitarian/git/trees/b5055158b2fc1f7c0b3ad58ece27e141ba294dc0)). **Inspected:** 2026-11-12. **Runtime:** NOT_TESTED. **Official current opening, eligibility and funding:** UNKNOWN.

## 1. Scope and objective

Inspect concrete source-level implementation and determine its fit for PhD evidence and applicant workflows.

## 2. Implementation architecture

Python `scripts/source.py` fetches a mixture of official and aggregator pages, sends content to DeepSeek for scholarship extraction, and stages findings. `poll_approve.py` uses Telegram callback owner ID to promote pending records, but checks neither official issuer evidence spans nor stable award IDs; JSON state and update offset saves are non-atomic.

## 3. Source and dataflow

Inspected [scripts/source.py](https://github.com/ummanitarian/scholarship-ummanitarian/blob/main/scripts/source.py), [scripts/poll_approve.py](https://github.com/ummanitarian/scholarship-ummanitarian/blob/main/scripts/poll_approve.py), [.github/workflows/daily-poll.yml](https://github.com/ummanitarian/scholarship-ummanitarian/blob/main/.github/workflows/daily-poll.yml). The snapshot is source level; no live service testing performed.

## 4. Confirmed correctness/security risks

**MODEL_SOURCING_UNVERIFIED_AND_NONATOMIC_APPROVAL (P1).** Python `scripts/source.py` fetches a mixture of official and aggregator pages, sends content to DeepSeek for scholarship extraction, and stages findings. `poll_approve.py` uses Telegram callback owner ID to promote pending records, but checks neither official issuer evidence spans nor stable award IDs; JSON state and update offset saves are non-atomic. Statements about authentication and errors apply to inspected code; deployed rule configurations and exploitability were not tested.

## 5. Verification and external-authority constraints

Extracted scholarship records, self-reported applicant states and program pages do not establish a current official funded offer. Preserve issuer URL, source excerpt, collection timestamp, intake cycle and formal deadline/eligibility checks.

## 6. Cross-repository transferable methods

Separate source collection from candidate-eligibility verification and personal applicant state. Repository supplies useful workflow concepts only after authorization, typed claim evidence and integrity controls.

## 7. Verdict

**P1: adopt no production code until MODEL_SOURCING_UNVERIFIED_AND_NONATOMIC_APPROVAL corrected.** Preserve privacy of applicant artifacts and never infer current funding from old metadata.

## 8. Tests and open questions

No CI execution, source owner contact, candidate document read, live scraping or adversarial tests performed. Add tests for authentication, conflicting source deadlines, data replacement, dedup, persistent state, empty/incomplete HTTP pages and precision of extraction.
