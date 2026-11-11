# Independent repository source audit — audit-20261112-r47c6f-b

- Started: 2026-11-12.
- Base main commit: 42773d67a494ac747a3fbb94ba65c8a7a2792796.
- Research branch: research/repository-audit-20261112-r47c6f-b.
- Session-owned write scope: research/sessions/audit-20261112-r47c6f-b/ only.
- Canonical CSVs, all other agents' work and branches remain unchanged during source investigation.
- Intended integration: source-pinned reports via PR/squash merge into main; any canonical index changes require a fresh main snapshot and exact-head compare/merge.
- Disjoint targets confirmed UNTRIAGED at start: neuronalX/phd-and-postdoc-positions; nishanchettri/PhD-positions-electronic-engineering; renzoe/positions_internships_phd_postdoc; serdark/academic-jobs-scraper; realrezi/Medical-PhD-Scraper.
- No claim of locking another session's unpublished work. This manifest is the public coordination record.

## Initial audit scope

- serdark/academic-jobs-scraper — live scheduled scraper, persisted seen-job dataset, API and validation issues.
- realrezi/Medical-PhD-Scraper — SeleniumBase source, filtering, persistence, security, and credibility.
- nishanchettri/PhD-positions-electronic-engineering — all source Markdown, maintained links and vacancy freshness.
- neuronalX/phd-and-postdoc-positions — historical README and two PDFs, binary text access to be verified.
- renzoe/positions_internships_phd_postdoc — historical README and four PDFs, binary access to be verified.

## Validation gate

- [x] Mainline and candidate states rechecked, distinct session branch/paths reserved.
- [x] Inspect complete relevant source files at pinned commits; PDF documents unavailable, explicitly blocked.
- [x] Verify GitHub history, issues/PRs, licensing and test evidence (static/remote metadata only).
- [x] Record per-repository findings and explicit document-access limitations.
- [x] Record cross-repository synthesis and conservative screening proposals.
- [ ] Validate additive diff, CI and merge to main without overwriting concurrent changes.

No secret values or private applicant records may be copied into review outputs. Tests, web crawling and outbound email are not authorized by an audit alone.

## Scope completed

- serdark and realrezi: deep source-level **static** reviews; no upstream runtime.
- nishanchettri: complete source Markdown read; four external historical offers unverified.
- neuronalX and renzoe: README/tree read, **6 PDFs unparsed**. Their status is SCREENED_INCLUDE pending document review, not full completion.
- Cross-repo methods/results synthesized; canonical state remains subject to fresh-main reconciliation and parallel sessions.
