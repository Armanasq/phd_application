# Main-branch research session — 2026-11-12

**Target:** `Armanasq/phd_application`, direct commits on `main`.  
**Status:** FIVE_SOURCE_REVIEWS_PUBLISHED; THREE_CANONICAL_RECONCILIATIONS_PUBLISHED; INTEGRITY_CI_CHECK_PENDING.  
**Session identifier:** `20261112-0112-gpt6-main`  
**Observed main at this manifest:** `aaf6dd7d295eac61893f9d36c54a91b5d14a10bc`.

## Source reviews published directly on main

1. `reviews/atul-pandey-career-academic-tracker.md` — deep source investigation of an unfinished FastAPI/frontend prototype. Another concurrent session independently classified the source as `SCREENED_EXCLUDE`; that original exclusion remains authoritative and was not overwritten.
2. `reviews/imsankalp-phd-application-tracker.md` — deep supplemental code review of Gmail-linked application sync, status parser and OAuth risks. Another session previously registered a canonical deep review; no duplicate review row was introduced.
3. `reviews/jaykishanj-phd-finder.md` — full deep static audit and new canonical record, pinned to `809cb3cc4edef615fe12eea1cb53f28a73b10d8b`. Identified the `--daily --report` GUI early-return defect, ambiguous deadline handling and crawler source-security gaps.
4. `reviews/neuronalx-phd-postdoc-positions.md` — preliminary review and canonical record, pinned `861f31226775d882303891ca877d7fd313a138e9`. Historical 2023 Inria PhD/postdoctoral offer archive; PDF bodies NOT_INSPECTED.
5. `reviews/renzoe-positions-internships-phd-postdoc.md` — preliminary review and canonical record, pinned `3b2cf283e34d0b47ebdd567f0b07de7b67e93885`. Historical 2022–2025 laboratory recruitment PDF archive; PDF bodies NOT_INSPECTED.

## Canonical repository artifacts updated

- `research/repositories/reviews/jaykishanj__phd_finder.md`
- `research/repositories/reviews/neuronalx__phd-and-postdoc-positions.md`
- `research/repositories/reviews/renzoe__positions_internships_phd_postdoc.md`
- `data/repositories.csv` — three new records, no prior row altered.
- `data/github_discovery_candidates.csv` — transitions for exactly these three identities.
- `research/repositories/index.md` — deterministic regeneration.
- `RESEARCH_STATUS.md` — recomputed summary at the last review snapshot.

## Concurrency and provenance

Other ChatGPT sessions were actively committing to `main`. Two prepared atomic Git-object commits were **not published**, because the branch-head update failed while main advanced. The session then used GitHub's content API with existing file blob SHA preconditions, preserving others' edits. Three alias notes and five original session notes were additive; canonical CSV, index and status writes succeeded sequentially against their current content revisions.

Another session had already audited `imsankalp` at an earlier commit and excluded the ATUL prototype. Those statuses were left untouched rather than duplicated. Other sessions' branches, issues, PRs and reviews were not modified. Issue #3 remains open, correctly reflecting the incomplete global review effort.

## Evidence and validation limits

- This is **static source inspection**, not runtime or penetration validation.
- Third-party tools, cloud credentials, email accounts, and external recruitment endpoints were not executed or authenticated.
- University opportunity truth, funding, legal eligibility and recruitment status were NOT independently established by these source-code reports.
- PDF binary contents remain uninspected; their reports are **preliminary**, not deep.
- GitHub Actions is responsible for research-integrity validation after pushes; a commit acknowledgement is not a test result.
