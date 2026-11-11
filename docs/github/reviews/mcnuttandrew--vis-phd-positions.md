# mcnuttandrew/vis-phd-positions

- **Assessment date:** 2026-11-11
- **Canonical repository:** https://github.com/mcnuttandrew/vis-phd-positions
- **Inspected snapshot:** 1f784d7b74091954db90840c7215108d7a3a46e8
- **Category:** HISTORICAL_VACANCY_DATASET
- **Review depth:** focused repository inspection (not a complete audit)
- **Inspected material:** README.md; src/routes/+page.ts; static/positions-24-25.tsv; tree; HEAD commit message
- **Verdict:** REFERENCE_HISTORICAL

## Distinct practical value
Self-reported lab/supervisor recruitment dataset for visualization containing names, research interests, claimed hiring cohorts and contact channels. Its data mapping code offers an example of separating source fields from normalized rows.

## Verified limitations and risks
Historical TSV is for 2024/25 positions; last commit explicitly says 'deprecate in favor of alexs thing'. README is default Svelte boilerplate. Records are not live vacancies, and contact details must not be used without validating current affiliation.

## Candidate-specific action
Use only for old lead discovery and schema inspiration; do not present past positions as currently open.

## Not inspected or demonstrated
Alternate replacement resource not verified; current supervisor availability unverified.

**Evidence rule:** Never treat a historical scholarship, applicant guide, or last-update timestamp as proof of 2026-27 policy. The repository's documented behavior is not a substitute for runtime validation.
