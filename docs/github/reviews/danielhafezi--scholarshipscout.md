# danielhafezi/ScholarshipScout

- **Assessment date:** 2026-11-11
- **Canonical repository:** https://github.com/danielhafezi/ScholarshipScout
- **Inspected snapshot:** 1fcd85b17b08f564c3d8a8d13d790f0c79419b07
- **Category:** VACANCY_SCRAPER
- **Review depth:** focused repository inspection (not a complete source audit)
- **Inspected material:** readme.md; ScholarshipScout.ipynb (notebook code cells); root tree
- **Verdict:** REJECT_AS_IS

## Distinct practical value
Notebook experiments with ScholarshipDB/FindAPhD collection, async HTTP, keyword/country search and CSV/XLSX output; useful historical sketch.

## Verified limitations and risks
Structured extract_info explicitly returns empty placeholder strings. Installation references requirements.txt absent from checked tree; model/API and source filtering not independently tested. Repository not changed since 2024. No verification that retrieved listings are funded.

## Candidate-specific action
Do not use its output as proof of full funding. Reimplement normalised extract/verify pipeline with official vacancy checks.

## Not inspected or demonstrated
Not executed; no live site smoke tests or security testing.

**Evidence rule:** The GitHub source is the artifact for this repository assessment. Source claims about external universities, visas or funding remain unverified until checked at the respective primary authority. This review does not claim tests ran successfully.
