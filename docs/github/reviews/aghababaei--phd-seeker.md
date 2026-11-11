# Aghababaei/PhD-Seeker

- **Assessment date:** 2026-11-11
- **Canonical repository:** https://github.com/Aghababaei/PhD-Seeker
- **Inspected snapshot:** 93ad22ea8bc0a04bbf566613650b36a58ff2c063
- **Category:** VACANCY_SCRAPER
- **Review depth:** focused repository inspection (not a complete source audit)
- **Inspected material:** README.md; phdseeker/main.py; phdseeker/repo.yaml; tree
- **Verdict:** ADAPT_CONCEPTS

## Distinct practical value
Compact packaged Python CLI scrapes ScholarshipDB and FindAPhD with configurable source selectors, concurrent fetching and CSV/XLSX export.

## Verified limitations and risks
Source CSS selectors are fragile, site rights/robots requirements not validated, duplicate removal remains a README TODO, vacancy funding is not primary-source verified. GPL-3.0 imposes reuse duties and should not be copied into unrelated software without license review.

## Candidate-specific action
Use adapter/query configuration concepts only. Add canonical URL, duplicate fingerprints, retrieval times, funding claims and official employer verification.

## Not inspected or demonstrated
No live scraper execution; no comparison against currently rendered target websites.

**Source rule:** External funding, admissions and visa claims cited by the repository require fresh verification at original official sources. No tool was installed, code executed or external action authorized merely by this review.
