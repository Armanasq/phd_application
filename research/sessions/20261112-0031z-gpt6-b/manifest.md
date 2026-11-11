# Source research session manifest — 20261112-0031z-gpt6-b

**Date:** 2026-11-12
**Branch:** `research/repository-audit-20261112-0031z-gpt6-b`
**Base main commit:** `9dc8b670d20497a5412b7ffc599aa4e2a8569fd8`
**Status:** ONE_NEW_DEEP_STATIC_REVIEW plus ONE_INDEPENDENT_SUPPLEMENT READY_FOR_PR; third-party runtime execution NOT performed.

## Assignment

The following two currently untriaged repository identities are claimed exclusively for this session's static source investigation:
1. `fsuitoal-code/phd-application-command-center` — local-first application manager, Python/FastAPI/SQLAlchemy, Alembic migrations, Claude-assisted research with source provenance and workflow tests.
2. `Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor` — portable agent skill and Python SQLite tracker for funded PhD monitoring, independent critic reviews, source completeness, deduplication, eligibility and scheduler safety.

Before this claim, both entries were `UNTRIAGED` in the canonical candidate CSV at the indicated main snapshot. Inspected open branch file lists did not show the two repository names. Private, unsaved work from other sessions is not visible.

## Isolation

- All changes are restricted to `research/sessions/20261112-0031z-gpt6-b/` until validated mainline reconciliation.
- No concurrent branch is rebased, force-pushed, deleted, merged, or modified.
- No third-party executable is run with user credentials.
- No unofficial vacancy, applicant eligibility, acceptance probability, or funding claim is promoted to verified.
- Commit-pinned source references, implementation evidence and explicit untested scope are required.
- After static review: verify diff, open PR, require passing Research integrity CI, merge to `main`; reconcile canonical index in a separate coordinated change.

## Progress

- [x] Checked live canonical queue states and active branch file lists.
- [x] Created isolated branch from exact main commit.
- [x] Pinned both upstream main commits and Git tree SHAs; examined README, domain model, agent policy, persistence, tests and history.
- [x] [Command center](fsuitoal-command-center.md) new deep static review, [PhD monitor](mhrnqaruni-monitor-supplement.md) supplemental findings, and [cross-source engineering synthesis](synthesis.md).
- [ ] Review only this session's changed paths, run GitHub PR Research integrity checks, and merge if clean.
- [ ] Reconcile canonical review rows/index against fresh main: only the command center remained untriaged at last snapshot. The monitor's canonical `DEEP_REVIEW_DOCUMENTED` report was already merged by a concurrent session; do not create a duplicate row.

## Verified source pins and conclusions

| Repository | Commit | Git tree | Result |
|---|---|---|---|
| `fsuitoal-code/phd-application-command-center` | `ea240bc0189038881306ccd34a5b9cbf525aaebd` | `87cf714b7f0df7f90582955f785529e9597c3668` | Deep static: strong fail-closed data migration; overly broad `*.ac.uk` fetch permission and unverified model-supplied citations; runtime NOT tested |
| `Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor` | `b5198427c4a53c6ec62cf6cb0f2dc60dce5f9ff9` | `48b24fb9ab305d7ad06c7ce57f29551af289fcbe` | Supplemental static findings only; canonical full structured review already exists on `main`. Self-review can satisfy publication; CI source tests passed, live search NOT tested |

No admissions vacancy was verified; neither third-party source was executed or given credentials. All files in this batch are additive and confined to the session-owned folder.

## Live parallel-session reconciliation

A fresh canonical check found that `Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor` had already been promoted from `UNTRIAGED` to `DEEP_REVIEW_DOCUMENTED` in another session during this investigation, using the same pinned upstream commit. The overlapping report was removed from this branch's final diff, leaving only an incremental supplement. The command center remained `UNTRIAGED` at that check. This project must not double-count the two parallel review efforts.
