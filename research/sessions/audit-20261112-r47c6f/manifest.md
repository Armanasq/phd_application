# Independent repository investigation manifest

- Session ID: `audit-20261112-r47c6f`
- Date: 2026-11-12
- Repository: `Armanasq/phd_application`
- Base `main` SHA: `de7008f6f35e07ef12d776de1c0b2d51e1319218`
- Isolated research branch: `research/repository-audit-20261112-r47c6f`
- Write scope: `research/sessions/audit-20261112-r47c6f/` only
- Integration target: `main`, through a reviewed PR and non-destructive merge
- Coordination: published branches, prior session manifests, current inventory, open issues, and open PRs inspected before claiming; unpublished work of parallel conversations remains unknown
- Local worktree: not used; branch-scoped GitHub API is the isolated workspace
- Canonical CSV indexes, review ledger, shared schemas, issues, other session directories, and historical records: read-only during investigation

## Independent scope and baseline

| Canonical repository ID | Baseline state | Assigned audit |
|---|---|---|
| `dinglhmds/Search-PhD-Positions` | UNTRIAGED | Multi-agent search, evidence, parser, email drafting and output reliability |
| `heyulanKiara/django-phd-scholarship` | UNTRIAGED | Django admissions data model, API, authentication, workflow and security |
| `DefangChen/CS_Professors` | UNTRIAGED | Source-document content, update history and usefulness as faculty lead |
| `Janjs/Web-Scraping-PhD-positions` | UNTRIAGED | Historical vacancy scraper, source implementation and reproducibility |
| `D4vidHuang/PhD_scanner` | UNTRIAGED | Confirm empty Git tree and document evidence-based exclusion |

None of these five identities appears in the current canonical review table or published active-session ownership manifests examined before this claim. No other session's ownership is displaced.

## Quality and progress

- [x] Current `main`, branches, manifests, prior PR integrations, candidate and review CSVs, and issue #3 inspected.
- [x] Disjoint batch selected; session branch created at pinned `main` SHA.
- [x] Inspect source trees and relevant implementations at pinned upstream commits.
- [x] Verify development history, issues and PRs, licensing, tests and actual capabilities (source-level; runtime NOT_TESTED).
- [x] Produce source-pinned per-repository reports, explicit coverage and limitations.
- [x] Produce cross-repository synthesis and an incremental inventory proposal.
- [ ] Validate the branch diff and CI, reconcile upstream changes, then merge safely to `main`.

## Constraints

Do not claim tests were executed without recorded commands and results. Avoid publishing private applicant material, credentials or personal records; use code and documented public interfaces only. No application submissions or outreach are authorized.

## Completed investigation artifacts

- Five source-pinned, session-scoped individual reports (two technically detailed, one curated source corpus, one historical scraper, one empty-repository exclusion).
- One cross-repository synthesis with canonical triage proposals, evidence gates and transferability conclusions.
- 3 proposed canonical source reviews; 2 proposed exclusions.
- No third-party code, employer site, email server or credential executed; no private applicant files handled.
- Shared canonical inventory/counts pending integration against latest main; all earlier concurrent work must be preserved.
