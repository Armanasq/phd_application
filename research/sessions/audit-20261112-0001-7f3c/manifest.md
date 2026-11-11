# Session manifest — audit-20261112-0001-7f3c

- Session ID: audit-20261112-0001-7f3c
- Repository: https://github.com/Armanasq/phd_application
- Working branch: main (per current instruction)
- Latest observed main baseline before this update: 64ab963cce38105c5ab878a168a894b2bb1118a9
- Status: first and second batch canonical reconciliation completed on main; expanded source audits and evidence-crosswalk published; global mapping remains incomplete
- First batch: archna1212/PHD-OPENINGS; Ariaeimehr/PHD-Position-Finder; arbitan/ScholarshipWebsite
- Second batch: atomdbc/scholarship_scraper; dhcoders/JobsACUK-WebScraper; evamaxfield/phd; D4vidHuang/PhD_scanner

## PR and validation history

PR [#7](https://github.com/Armanasq/phd_application/pull/7) added the first-batch reports and synthesis. It was merged into main at c8132e3e620d20a5bf6dfc39a3f9db9e605f5968 by the repository owner. GitHub reported mergeable=true; no merge conflict occurred.

The PR workflow passed scripts/validate.py but failed tests/test_import_research.py because the test expected 35 repository audits while the then-current CSV contained 63. This was a stale test expectation, not a conflict caused by the session artifacts. A subsequent mainline commit changed the assertion to derive the expected count from the canonical repositories.csv. No successful post-fix CI run has been observed; do not claim the suite is verified.

## First-batch results and canonical reconciliation

1. archna1212/PHD-OPENINGS — exact source mirror of Aghababaei/PhD-Seeker; excluded as an independent implementation.
2. Ariaeimehr/PHD-Position-Finder — deep static review completed; canonical review record exists at research/repositories/reviews/ariaeimehr__phd-position-finder.md.
3. arbitan/ScholarshipWebsite — excluded as an academic-publication keyword collision.

A parallel session reconciled the canonical inventory and relations after these findings. The current main inventory reports 67 review records (9 deep static, 58 preliminary), 18 exclusions, 319 untriaged candidates, and zero screened-in candidates awaiting first review. The candidate inventory remains 404 identities. The canonical relation ledger has six rows, including the PHD-OPENINGS MIRROR_OF relation.

The earlier simitii/siddu assignment was not retained by this session: PR #6 already merged their session reports, and later mainline commits registered them in the canonical inventory. The earlier branch research/repository-audit-20261112-0001-7f3c remains superseded and must not be merged.

## Second-batch results

1. atomdbc/scholarship_scraper — deep static review of the 92-entry FastAPI/SQLAlchemy/Playwright/Next.js platform. Identified missing Playwright dependency, unauthenticated/SSRF-prone URL ingestion, worker/session and retry-state defects, LLM evidence gaps, broken field mappings, and frontend/backend contract issues. Runtime NOT_TESTED.
2. dhcoders/JobsACUK-WebScraper — deep static review of the only Python script. Identified refresh-unit error, cross-job deadline assignment, missing HTTP timeout/retry, and absent persistence/dedup. Runtime NOT_TESTED.
3. evamaxfield/phd — preliminary privacy-bounded review of a personal doctoral archive. Interview notes and planning structure inspected; personal CV/statement PDFs not opened or copied.
4. D4vidHuang/PhD_scanner — excluded as an empty repository; metadata size zero and no branches/content.

Second-batch artifacts are under research/sessions/audit-20261112-0001-7f3c/next-batch/. No canonical CSV, global status, generated index, or shared relation file was modified.

## Parallel coordination

Published active assignments were checked before selecting the second batch. The four repositories were UNTRIAGED in the canonical candidate CSV and were not listed in the published scopes of the active sessions inspected. Published coordination cannot reveal unsaved work in other ChatGPT conversations.

Active branches observed:
- research/repository-audit-20261112-0031z-gpt6-a
- research/repository-audit-gpt6-20261111-2031z
- research/session-gpt6-20261112-01-integration
- research/repository-audit-gpt6-20261112-0002b (no published manifest observed)

## Mainline reconciliation snapshot — 2026-11-12

The prior second-batch proposal has been incorporated into the canonical register. At the inspected mainline checkpoint after the added audits and exclusions, 404 discovered candidates were classified as 152 REVIEW_RECORDED + 143 SCREENED_EXCLUDE + 109 UNTRIAGED + 0 SCREENED_INCLUDE. These are a dated checkpoint, not a live dashboard. Other sessions may advance the register; recompute from the CSVs.

Expanded session investigations published:
- research/repositories/reviews/xujingchen1996__research-app-toolkit.md — deep static audit of multi-host local applicant research and instruction workflows;
- research/repositories/reviews/sushil3710__phd-admission-portal.md — deep static institution-side admissions security/dataflow audit;
- research/repositories/reviews/ssine__willow.md — deep static historical applicant-statistics and privacy audit;
- research/sessions/audit-20261112-0001-7f3c/next-batch/screening-nonadmissions-five.md — five source-backed out-of-scope decisions;
- research/sessions/audit-20261112-0001-7f3c/next-batch/architecture-and-evidence-crosswalk.md — cross-repo evidence, privacy and workflow architecture synthesis.

Other sessions simultaneously excluded six separate unrelated repositories. This session independently excluded K-Graduate/application as a pet-adoption app; no other session branches were altered.

The research-integrity CI detected a stale generated index after concurrent register changes and a broken local Markdown link in the new crosswalk. The index was regenerated at f614b196bbbbe4e71777168ec43785f130edc560; a successful CI run verified that index commit. The crosswalk link was subsequently corrected at 8045cc1fac0eb88c534a3e386dce1b60e71800b6; verify its latest CI run before claiming final status.

## Outstanding documentation consistency issues

- METHODOLOGY.md and synthesis/repository-systematic-review.md still contain older screening totals.
- RESEARCH_STATUS.md and synthesis/source-dependency-crosswalk.md still report five repository relations while data/repository_relations.csv contains six.
- These are shared consolidated documents. They are recorded for coordinated reconciliation, not independently rewritten while parallel sessions remain active.

## Validation boundary

All repository reviews are source-level static inspections. No third-party code was cloned or executed. No runtime tests, Docker startup, live scraping, database migration execution, LLM calls, or notification delivery are claimed. No personal contact details, recommendation letters, CV contents, or statement text are reproduced.
