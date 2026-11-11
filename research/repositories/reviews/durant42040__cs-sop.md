# durant42040/cs-sop — deep static repository review

**Reviewed:** 2026-11-12. **Pinned upstream:** [f73b264b9563ea939ab7e298362a5292ddb9d5f8](https://github.com/durant42040/cs-sop/commit/f73b264b9563ea939ab7e298362a5292ddb9d5f8).  
**Review state:** DEEP_REVIEW_DOCUMENTED, static code and methodology inspection; not an independent applicant survey.  
**Verdict:** reference reproducible applicant-profile evidence design; reject population admissions probability inference.

## 1. Purpose and sample composition

A standalone React/TypeScript browser for CS PhD applicant profiles. Its README reports **127 applicant profiles across 46 destination schools**, covering undergraduate institutions, research projects, mentors, publication/status evidence and linked historical statements of purpose. Adapted data derives from the CS PhD Statements of Purpose collection and Tsinghua Feiyue Database. The profiles are *selected public examples*, not a probability sample of applicants, admitted candidates, or the full set of applicants.

## 2. Architecture and data structure

The 27-file TypeScript/Vite project stores structured profiles as `exampleSchools` in `lib/applicant-examples.ts` (~590 kB). Each school has program name, applicant list and identifiers. Applicants have source links, education and major, application year, research experiences and paper arrays; each paper can distinguish `Accepted`, `Submitted`, `Conditionally accepted`, `Preprint` or `In preparation`. The UI filters schools and applicants, groups research by institution, sorts works and links to original SOP and bibliographic sources.

Explicit status modeling and application-time snapshots are strengths relative to lists that indiscriminately count later academic papers.

## 3. Research questions and counted metrics

`scripts/count-conferences.mjs` classifies recorded venues using regex dictionaries, deduplicates papers by normalized title **within each applicant**, and counts `Accepted` full main-conference works separately from workshops, journals, Findings, abstracts, short papers, and conditional submissions. Multi-school profiles can appear under different destination institutions. The script writes JSON and text reports and documents provisional categories and unresolved cases.

Publication analysis is an observed *descriptive statistic of saved examples*. It cannot estimate an individual's admission probability, universal publication requirements or program selectivity. An applicant with zero recorded accepted papers may still have unpublished or otherwise missing evidence. The code explicitly warns that empty inventories are a calculation placeholder, not verified absence.

## 4. Methodological and statistical caveats

The script marks every `student.usable = true`; it includes all included profiles in school denominators. Applicants with no paper inventory contribute numeric zero to an average despite the explicit inability to establish a true zero. This yields a **downward-biased count for incompletely documented profiles** and a difficult-to-interpret mean. Conversely, the sample may overrepresent applicants who publicized SOPs, admission outcomes or research achievements, creating selection bias in unknown directions for general applicants.

The classification regex uses manually maintained conference names and infers work status from labels. A label “Accepted” without a dated official acceptance artifact is not independently reverified; a venue’s year alone need not establish acceptance before the application deadline. The method acknowledges unresolved venue classification and application-time gaps, but its plots should display sample size, missingness and status-confidence rather than imply population benchmarks.

## 5. Source lineage, deduplication and privacy

The project provides SOP and CV links, per-research source URLs and a dated `paperReview` object for many examples. Profile additions and zero-paper audits are documented. These are useful traceability patterns.

The data may include names, education and professional history supplied in public source documents. This repo's inclusion is not evidence that each person consented to aggregation in a new product or model training. The review did not inspect or reproduce linked personal CV PDFs or SOP bodies. Before redistribution, confirm personal data and source terms; preserve the option to correct/retract inaccurate profile information.

## 6. Licensing, build and tests

`LICENSE-CONTENT.md` licenses adapted profile content under **CC BY-NC-SA 4.0**, with original SOPs separately owned by their authors. Noncommercial/share-alike obligations apply to content reuse. The repository uses Node >=22.13, Vite, React 19 and TypeScript; package scripts include `build`, `typecheck` and `test`. Test execution and build were not performed; the package script alone does not show that all tests exist or pass.

## 7. Evidence and verification boundary

Inspected README, content licensing, source data shapes, browser component, publication-statistics component, conference-count script and dated audit reports. The exact completeness and correctness of all 127 profiles or external linked paper records were not individually reverified. The QS university-ranking references are a separate source class and do not establish research fit or admission probability.

Evidence: [README](https://github.com/durant42040/cs-sop/blob/f73b264b9563ea939ab7e298362a5292ddb9d5f8/README.md), [profile data](https://github.com/durant42040/cs-sop/blob/f73b264b9563ea939ab7e298362a5292ddb9d5f8/lib/applicant-examples.ts), [count script](https://github.com/durant42040/cs-sop/blob/f73b264b9563ea939ab7e298362a5292ddb9d5f8/scripts/count-conferences.mjs), [profile audit](https://github.com/durant42040/cs-sop/blob/f73b264b9563ea939ab7e298362a5292ddb9d5f8/docs/zero-paper-audit.txt), [content license](https://github.com/durant42040/cs-sop/blob/f73b264b9563ea939ab7e298362a5292ddb9d5f8/LICENSE-CONTENT.md).

## 8. Transfer to PhD Atlas

Retain an applicant-example **research evidence** corpus separate from scholarship and faculty opportunities. Preserve cycle, applicant role, source URL, paper status at application time, provenance and confidence; normalize institution identity before counting. Report selection bias, missing evidence and unknown applicant outcomes. Benchmark any fit model only on a valid labeled/consented dataset; publication counts, university ranking and web visibility are not calibrated chances of admission. Adapted source content must not be copied into commercial systems without resolving the CC BY-NC-SA licensing constraints.
