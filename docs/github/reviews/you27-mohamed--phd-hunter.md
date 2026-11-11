# you27-mohamed/PhD-Hunter

- **Assessment date:** 2026-11-11
- **Canonical repository:** https://github.com/you27-mohamed/PhD-Hunter
- **Inspected snapshot:** 1054afc3258eb909a2faad42bba17d9c548c36aa
- **Category:** AGGREGATOR_AND_SCRAPER
- **Review depth:** focused repository inspection (not a complete source audit)
- **Inspected material:** README.md; phd_hunter/academic_scraper.py; phd_hunter/linkedin_scraper.py; tree
- **Verdict:** REJECT_AS_IS

## Distinct practical value
Separates academic-source scraping and LinkedIn search, with CLI, CSV, Selenium browser automation and dedicated test files.

## Verified limitations and risks
CRITICAL: __main__ example in a checked-in Python file contains what appears to be an email/password pair. Do not copy or attempt authentication with it; validity is unknown. Anti-detection LinkedIn scraping raises terms/compliance concerns; the README's 'legally compliant' and 90% test coverage claims were not independently verified. Cached pyc files are committed. GPL-3.0 dependencies need attribution review.

## Candidate-specific action
Do not run its login scraper or reuse secrets. Prefer official vacancy feeds and site-compliant access; only learn from adapter separation.

## Not inspected or demonstrated
No tests run, legal opinion, license compliance verification, or live credential validation.

**Source rule:** External funding, admissions and visa claims cited by the repository require fresh verification at original official sources. No tool was installed, code executed or external action authorized merely by this review.
