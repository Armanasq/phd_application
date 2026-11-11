# Canonical integration status — repository audit 2026-11-12

**Status: IMPLEMENTED ON MAIN BY PARALLEL MAINLINE INTEGRATION.** This file is an audit trail; do not replay the proposed writes.

## Implemented first-batch dispositions

| Repository | Canonical disposition | Mainline evidence |
|---|---|---|
| archna1212/PHD-OPENINGS | SCREENED_EXCLUDE; exact mirror | data/exclusions.csv and data/repository_relations.csv record the duplicate/mirror lineage to Aghababaei/PhD-Seeker |
| Ariaeimehr/PHD-Position-Finder | DEEP_REVIEW_DOCUMENTED, static; runtime NOT_TESTED | data/repositories.csv and research/repositories/reviews/ariaeimehr__phd-position-finder.md |
| arbitan/ScholarshipWebsite | SCREENED_EXCLUDE; academic-publication keyword collision | data/exclusions.csv |

The earlier simitii and siddu candidate records were also reconciled after PR #6, using the session-specific reports already merged under research/sessions/2cabbe82/.

## Current canonical counts

As observed on main after the parallel integration commits:

- 404 candidate identities;
- 67 review records: 9 deep static and 58 preliminary;
- 18 documented exclusions;
- 319 untriaged candidates;
- 0 screened-in candidates awaiting first review.

Check: 67 + 18 + 319 = 404.

The repository relation ledger contains six rows, including the PHD-OPENINGS MIRROR_OF relation.

## PR and test history

PR #7 merged at c8132e3e620d20a5bf6dfc39a3f9db9e605f5968. The PR's initial CI run failed because tests/test_import_research.py still asserted 35 repository audits while the register contained 63. A later mainline test commit derives the expected audit count from repositories.csv. The fix is present in source, but a successful post-fix CI run has not been observed.

## Remaining documentation reconciliation

The main inventory and several reports are now updated, but these consolidated documents still contain older figures:
- METHODOLOGY.md: earlier 53-review/340-untriaged baseline.
- synthesis/repository-systematic-review.md: earlier review, inclusion, and untriaged totals.
- RESEARCH_STATUS.md and synthesis/source-dependency-crosswalk.md: five relations versus six rows in data/repository_relations.csv.

These are shared documents and require one coordinated, source-of-truth update. Do not replay first-batch candidate or exclusion changes.
