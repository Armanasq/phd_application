# abono200/phd-admissions-platform — focused source review

- **Review date:** 2026-11-11
- **Pinned upstream commit:** [6e5fd0ff3416f3ee7926636d1369ffa46e26c48b](https://github.com/abono200/phd-admissions-platform/commit/6e5fd0ff3416f3ee7926636d1369ffa46e26c48b); latest commit observed 2026-07-12.
- **Category:** static university dossier catalog and client-side application dashboard.
- **Review state:** PRELIMINARY_FOCUSED. Inspected handbook, sample dossiers, parser, generated JSON and React application; no runtime tests.
- **License:** no explicit license metadata or license file confirmed.

## 1. Problem and intended user

A US-focused CS PhD dashboard combines university dossiers, professor matching, application tracking, document checklists, comparison, cost-of-living and an admission-score calculator. The data and narrative are personalized to a particular applicant profile, not a neutral global admissions catalog.

## 2. Architecture and data flow

Markdown dossier files contain a small YAML-like front matter and narrative body. A custom Node parser reads those files and emits `db.json`; a React/TypeScript SPA imports that JSON and stores application statuses, notes, CRM logs and document progress in browser localStorage. There is no live source refresh or server-side data service in the inspected implementation.

Relevant files: [parser](https://github.com/abono200/phd-admissions-platform/blob/6e5fd0ff3416f3ee7926636d1369ffa46e26c48b/platform/scripts/parse_dossiers.js), [App.tsx](https://github.com/abono200/phd-admissions-platform/blob/6e5fd0ff3416f3ee7926636d1369ffa46e26c48b/platform/src/App.tsx), [MIT dossier](https://github.com/abono200/phd-admissions-platform/blob/6e5fd0ff3416f3ee7926636d1369ffa46e26c48b/dossiers/mit.md).

## 3. Useful product patterns

- Dossier-based institution detail pages with structured funding, requirements, deadlines and faculty sections.
- Comparison view and per-application status/document tracking.
- A localStorage-backed personal workspace without mandatory backend deployment.
- Separating dossier source material from generated front-end JSON.

## 4. Critical factual and methodological defects

The inspected dossiers present funding as guaranteed for five years, tuition waivers, stipend ranges, language rules, deadlines, rankings and faculty-project descriptions without claim-level source citations or evidence snapshots. These are high-impact claims and cannot be trusted as current facts merely because they appear in a polished dossier.

The calculator assigns arbitrary points for GPA, MPhil, publication count, research years and recommendation strength, then labels the resulting score as admission probability and adds ten points for funding probability. No training data, calibration, cohort definition, uncertainty interval or validation is provided. The output is not an admissions probability. It is especially misleading when the defaults encode another applicant's profile.

The dossiers contain internal contradictions and generic statements: the inspected MIT dossier both describes strict English-test requirements and suggests an exception/alternative test, while presenting a universal five-year funding guarantee. Faculty matching is based on short manually written summaries rather than current publications, methods, availability or funding evidence.

## 5. Parser and application limitations

The YAML parser is handwritten for a narrow front-matter subset. It does not provide general YAML parsing, schema validation or structured error reporting. The front-end data is a static build artifact; there is no source refresh, historical change tracking or claim-level provenance. localStorage persistence is browser-specific and has no built-in encrypted backup or multi-device synchronization.

## 6. Privacy and verification boundary

The repository includes a personal applicant profile and tailored application narrative. Do not copy its private/personal details or treat the dossiers as generic applicant data. No current official admissions pages were independently checked as part of this code review. No test suite was executed.

## 7. Adoption judgment

**REJECT AS A FACT SOURCE; ADAPT THE DOSSIER UI CONCEPT.** Reuse the information architecture only after replacing the dataset with source-backed, cycle-specific claims and separating research-fit assessment from admission probability. Remove probability labels unless statistically calibrated.

## 8. Unresolved work

Verify every deadline, stipend, tuition and English requirement against current official pages; build a structured schema and YAML parser; add field-level citations, evidence dates and contradiction handling; test local export/import and migration; redesign the calculator as transparent criteria scoring rather than probability.