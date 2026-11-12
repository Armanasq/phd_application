# abono200/phd-admissions-platform — focused source review

- **Review date:** 2026-11-11
- **Pinned upstream commit:** [6e5fd0ff3416f3ee7926636d1369ffa46e26c48b](https://github.com/abono200/phd-admissions-platform/commit/6e5fd0ff3416f3ee7926636d1369ffa46e26c48b); latest commit observed 2026-07-12.
- **Category:** static university dossier catalog and client-side application dashboard.
- **Review state:** DEEP_REVIEW_DOCUMENTED. Inspected handbook, sample dossiers, parser, generated JSON and React application; no runtime tests.
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

## Additional code-and-claim trace — 2026-11-12

At `6e5fd0ff3416f3ee7926636d1369ffa46e26c48b`, inspected the 267-line `PhD_Admissions_Handbook.md`, one representative institutional dossier `dossiers/mit.md`, `platform/scripts/parse_dossiers.js` (127 lines), the 19-object `platform/src/data/db.json` generated catalog (schema and non-personal sample fields), and targeted source regions of the 1,500+ line `platform/src/App.tsx` (not all 75 kB line-by-line). The Node parser transforms YAML-like per-school frontmatter into JSON without a current authoritative policy source registry or field-level official claim spans. Dossiers contain hard-coded `funding_guaranteed: true`, stipend amounts, tuition coverage, GRE and English waiver assertions; these are author-compiled claims, **not verified 2026/27 university rules**. Applicant-specific personal facts were deliberately not reproduced in this review.

**Critical metric validity:** `App.tsx` lines 205–232 implement a user-facing “Compute Admissions Probability” calculator as a hard-coded score: start at 50; add 10/20 for GPA bands, 15 for MPhil, 8 per publication (capped 25), 3 per research year (capped 10), 5/10 for subjective letters; set `admissionProb=Math.min(score,99)` and `fundingProb=Math.min(score+10,100)`. No enrollment outcomes, target university acceptance denominators, calibration procedure, likelihood model, or funding-offer observation supports these percentages. The statement `// Funding is guaranteed if admitted` is not universally true across countries, programs, sponsors or applicant categories. Displayed probabilities should **not** influence funding/applicant decisions; replace them with clearly qualitative, uncertainty-aware readiness flags or a validated statistical model with disclosed cohort scope.

The React UI persists admission status, CRM notes, document state and application details in browser `localStorage`; these are self-reported user workflow fields rather than university-verified submission receipts. An introductory “full waiver + stipend for all” UI label conflates nominal program funding policy with applicant-specific award entitlement. No live official policy recheck, CV privacy test, React build, admissions outcomes evaluation or runtime execution occurred.

**Transfer:** reproducible source-to-schema parsing for 19 university dossiers, program comparison, applicant tracking and research-methodology fit notes. Do not carry over quantitative acceptance/funding percentages, hard-coded guarantees or personalized admissions data. Require per-school, per-cycle official URL, exact excerpt, region/international fee coverage, deadline/timezone and last verification. [calculator](https://github.com/abono200/phd-admissions-platform/blob/6e5fd0ff3416f3ee7926636d1369ffa46e26c48b/platform/src/App.tsx#L205-L232), [parser](https://github.com/abono200/phd-admissions-platform/blob/6e5fd0ff3416f3ee7926636d1369ffa46e26c48b/platform/scripts/parse_dossiers.js), [example dossier](https://github.com/abono200/phd-admissions-platform/blob/6e5fd0ff3416f3ee7926636d1369ffa46e26c48b/dossiers/mit.md).
