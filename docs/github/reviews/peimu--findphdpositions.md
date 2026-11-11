# PeiMu/findPhdPositions

- **Assessment date:** 2026-11-11
- **Canonical repository:** https://github.com/PeiMu/findPhdPositions
- **Inspected snapshot:** 48d4a69563a143731060b6cdb9ef8d05fc9b4c75
- **Category:** SUPERVISOR_DISCOVERY
- **Review depth:** focused repository inspection (not a complete source audit)
- **Inspected material:** README.md; spider.py; tree
- **Verdict:** REFERENCE

## Distinct practical value
Attempts to discover researchers by conference publication authorship and public researcher profiles; publication-centric matching is directionally stronger than generic faculty keyword searches.

## Verified limitations and risks
Uses brittle HTML parsing and regex against conference pages/Google Scholar plus an optional paid scraper proxy; most recent source update 2023. Names/publication lists alone do not prove supervisor availability or funding.

## Candidate-specific action
Use bibliographic graph APIs and recent lab publications to implement a maintainable equivalent; retain author disambiguation and institution provenance.

## Not inspected or demonstrated
No spider execution or live site verification.

**Source rule:** External funding, admissions and visa claims cited by the repository require fresh verification at original official sources. No tool was installed, code executed or external action authorized merely by this review.
