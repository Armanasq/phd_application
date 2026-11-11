# Session manifest — audit-20261112-0001-7f3c

- Session ID: audit-20261112-0001-7f3c
- Repository: https://github.com/Armanasq/phd_application
- Current working branch: main
- Latest observed main baseline: 64ab963cce38105c5ab878a168a894b2bb1118a9
- Status: first batch merged and canonically reconciled; second batch in progress
- First batch: archna1212/PHD-OPENINGS; Ariaeimehr/PHD-Position-Finder; arbitan/ScholarshipWebsite
- Next batch: atomdbc/scholarship_scraper; dhcoders/JobsACUK-WebScraper; evamaxfield/phd; D4vidHuang/PhD_scanner

## PR and validation history

PR [#7](https://github.com/Armanasq/phd_application/pull/7) added the first-batch reports and synthesis. It was merged into main at c8132e3e620d20a5bf6dfc39a3f9db9e605f5968 by the repository owner. The PR had no merge conflict; GitHub reported mergeable=true.

The PR workflow passed scripts/validate.py but failed tests/test_import_research.py because the test expected 35 repository audits while the then-current CSV contained 63. This was a stale test expectation, not a conflict caused by the session artifacts. A subsequent mainline commit changed the assertion to derive the expected count from the canonical repositories.csv. No successful post-fix CI run has been observed; do not claim the suite is verified.

## First-batch results and canonical reconciliation

1. archna1212/PHD-OPENINGS — exact source mirror of Aghababaei/PhD-Seeker; excluded as an independent implementation.
2. Ariaeimehr/PHD-Position-Finder — deep static review completed; canonical review record now exists at research/repositories/reviews/ariaeimehr__phd-position-finder.md.
3. arbitan/ScholarshipWebsite — excluded as an academic-publication keyword collision.

A parallel session reconciled the canonical inventory and relations after these findings. The current main inventory reports 67 review records (9 deep static, 58 preliminary), 18 exclusions, 319 untriaged candidates, and zero screened-in candidates awaiting first review. The candidate inventory remains 404 identities. The canonical relation ledger has six rows, including the PHD-OPENINGS MIRROR_OF relation.

The earlier simitii/siddu assignment was not retained by this session: PR #6 already merged their session reports, and later mainline commits registered them in the canonical inventory. The earlier branch research/repository-audit-20261112-0001-7f3c remains superseded and must not be merged.

## Parallel coordination

Visible active assignments were checked before selecting the next batch. The next four repositories are untriaged in the canonical candidate CSV and are not listed in the published scopes of the active sessions inspected. Published coordination cannot reveal unsaved work in other ChatGPT conversations.

Active branches observed include:
- research/repository-audit-20261112-0031z-gpt6-a
- research/repository-audit-gpt6-20261111-2031z
- research/session-gpt6-20261112-01-integration
- research/repository-audit-gpt6-20261112-0002b (no published manifest observed)

## Current artifacts

First batch reports and synthesis are under research/sessions/audit-20261112-0001-7f3c/. Canonical review/exclusion records were added separately by mainline integration; session reports are not counted as additional independent reviews.

## Outstanding consistency issues

- METHODOLOGY.md and synthesis/repository-systematic-review.md still contain older screening totals.
- RESEARCH_STATUS.md and synthesis/source-dependency-crosswalk.md still report five repository relations, while data/repository_relations.csv now has six.
- These are shared consolidated documents. They are recorded for coordinated reconciliation, not independently rewritten while parallel sessions remain active.

## Next batch

- atomdbc/scholarship_scraper — full-stack scholarship ingestion and AI extraction system; deep static review in progress.
- dhcoders/JobsACUK-WebScraper — single-file Jobs.ac.uk scraper; static review in progress.
- evamaxfield/phd — personal doctoral archive with application materials and interview/planning notes; privacy-bounded review.
- D4vidHuang/PhD_scanner — repository metadata reports zero size and no content; verify empty-repository disposition.

No runtime execution, tests, Docker launch, live scraping, or notification delivery is claimed for these repositories.
