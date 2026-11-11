# Repository review session — 20261112-phdbench-keith-4e23

- Target: https://github.com/Armanasq/phd_application
- Integration: dedicated GitHub branch and guarded PR into main
- Branch: `research/repository-audit-20261112-phdbench-keith-4e23`
- Base main snapshot: `220428776b2018690a982816cb7c8bb119d8fcd1`
- Date: 2026-11-12
- State: SOURCE_AUDITS_COMPLETE; GUARDED_PR_PENDING
- Isolation: only `research/sessions/20261112-phdbench-keith-4e23/`, never shared CSVs or other sessions' files
- Workspace: branch-scoped authenticated GitHub API; no local clone or upstream runtime is claimed

## Assigned investigations

1. `Nikhil-Rao20/phdbench` — multi-user shared PhD lead board and private application tracking; inspect Firestore security rules, authorization boundary, submission proof, persistent identity, sync, test coverage, deployment.
2. `KeithBH/phd-positions` — single-page EU manufacturing/industrial-AI PhD directory; inspect full embedded data and logic, provenance, update semantics, deadline and opportunity verification.

At assignment both were untriaged in the main candidate queue and were not named in the published branch ownership manifests inspected. Private and unpublished other-session work is not observable.

## Checks

- [x] Pin upstream revisions, enumerate full trees and history.
- [x] Inspect relevant code/data/security/auth/tests and track uninspected scope.
- [x] Write deep static reviews with exact source links and validated limitations.
- [x] Deduplicate findings against earlier tracker/source reviews.
- [ ] Compare complete diff, inspect current main and available CI.
- [ ] Open and merge guarded PR; verify files on main.

No third-party credentials, live user data, submissions, outreach or arbitrary upstream code execution will be used. Runtime behavior cannot be inferred from static source alone.

## Results

- Deep static review: reviews/nikhil-rao20-phdbench.md (source-level authorization and status-evidence defects; runtime/emulator NOT_RUN).
- Complete static single-file + data review: reviews/keithbh-phd-positions.md (192 parsed records, stale counters and status mismatches; live opening NOT_VERIFIED).
- Synthesis: cross-repository-synthesis.md.
- All modifications confined to this session's directory; canonical inventory intentionally unchanged pending coordination.
