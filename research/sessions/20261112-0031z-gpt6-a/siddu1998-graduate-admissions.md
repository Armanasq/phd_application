# Repository investigation — siddu1998/Graduate-Admissions

**Review date:** 2026-11-12  
**Upstream:** https://github.com/siddu1998/Graduate-Admissions  
**Pinned default-branch commit:** [`71d1750175b1cca2bca78fe738765b0c42c58c0a`](https://github.com/siddu1998/Graduate-Admissions/commit/71d1750175b1cca2bca78fe738765b0c42c58c0a)  
**Commit date:** 2023-03-06  
**Review state:** PRELIMINARY_CONTENT_BLOCKED; README and complete tree inspected, PDF body review not completed.  
**Applicability:** historical SOP comparison and document-portfolio analysis.

## 1. Repository structure and author intent

The repository contains 40 tree entries:
- 20 statement-of-purpose / statement-of-intent PDFs;
- 3 recommendation-letter PDFs;
- university folders for Brown, CMU, Columbia, Cornell, EPFL, Imperial, MIT, Oxford, Purdue, UBC, UCSC, UIUC, UMCP, UNC-Chapel Hill, and USC;
- one README.

The README explicitly describes the documents as the author's own SOPs across 2020 and 2021 application cycles. It notes repetition between drafts and the transition between MS and PhD statements. It also links a Reddit graduate-admissions thread and a YouTube admissions playlist.

This is a personal application-document archive, not an admissions guide, verified outcome dataset, or reusable SOP template library.

## 2. Document inventory and limitations

The filenames show a useful cross-program comparison set:
- multiple versions for CMU, Cornell, Purdue, and USC;
- explicit MS/PhD distinctions for several institutions;
- a UBC statement of intent whose filename says supervisors were contacted;
- separate materials for EPFL, Imperial, Oxford, MIT, and other programs.

The archive contains three recommendation-letter PDFs in a `Recommendations/` folder. Those are third-party confidential-style documents. I did not inspect, quote, or reproduce their contents. Their public presence does not establish that recommenders consented to public redistribution.

### PDF access blocker

The GitHub tree and file metadata are accessible, but the PDFs are binary. The GitHub file API returned base64 payloads; the available PDF readers require an attached/mounted file, and the local runtime could not resolve GitHub for download. The PDF content itself has therefore not been reviewed in this session. This is a real completion blocker, not a claim that the PDFs were read.

No inference is made about the content quality, applicant identity, admission outcome, or funding outcome of any statement.

## 3. Source provenance and integrity

- Default branch: `main`.
- Latest commit: 2023-03-06, README update.
- No issues or pull requests returned.
- One branch returned.
- No LICENSE file in the recursive tree.
- No source code, tests, data model, workflow, or structured outcome metadata.

The README's first-person description supports that these are the author's application materials. It does not establish that every application was successful, that a particular document led to admission, or that the text can be reused by others.

The lack of a license and the personal nature of the documents make verbatim redistribution or use as templates inappropriate without explicit permission.

## 4. Research value

The collection can support a structured comparative study after the PDFs are made available for content review:
- how the research narrative changes between MS and PhD applications;
- how faculty fit is expressed across universities;
- how the applicant describes prior work and future research;
- how statements are adapted to institution/program context;
- which material is reused and which is tailored;
- how a statement of purpose differs from a statement of intent.

The most useful methodological approach is to compare document structure and argumentation, not copy sentences. Each statement should be annotated with degree type, field, program, cycle, source page limits, research experience, methods/results, faculty fit, and verified outcome status. Without those labels, cross-document comparisons can confound MS and PhD objectives or different program requirements.

## 5. Evidence limitations and handling rules

- **No outcome labels:** admission, rejection, waitlist, scholarship, and funding results are not recorded in the README.
- **Cycle age:** the stated application cycles are 2020 and 2021; requirements and prompt wording may have changed.
- **Degree-level mixing:** the README says MS and PhD SOPs are both present.
- **Institution-specific constraints:** page limits, prompts, faculty contact rules, and funding models differ; the same statement structure is not necessarily portable.
- **Selection bias:** a single applicant's document set is not a representative sample of admitted or rejected applicants.
- **Privacy:** recommendation letters may expose recommender identities, signatures, institutional details, and third-party personal information.
- **Copyright:** no license is present; do not reproduce text or redistribute the PDFs.

## 6. Recommended disposition for the admissions framework

Use the repository as a candidate source for private, permission-aware document analysis, not as a public source of applicant outcomes.

If the PDF bodies become available in a reviewable form:
1. Inspect SOPs only; keep recommendation letters excluded unless explicit authorization is established.
2. Extract structure and argument patterns without copying text.
3. Record the application cycle, degree type, program prompt, page limit, and research area for each document.
4. Separate verified outcomes from assumptions; the existence of an SOP is not proof of admission.
5. Compare MS and PhD statements separately.
6. Derive a reusable rubric for research readiness, evidence of contribution, faculty fit, and program-specific tailoring.

## 7. Final disposition

**TREE_AND_README_REVIEW_COMPLETE**.  
**PDF_CONTENT_REVIEW_BLOCKED** by binary file access in the current environment.  
**RECOMMENDATION_LETTERS_NOT_INSPECTED** for privacy reasons.  
**NO_ADMISSION_OR_FUNDING_OUTCOME_INFERENCE_SUPPORTED**.

This repository is potentially useful as a personal historical SOP corpus. It cannot yet receive a deep content-level review, and none of its documents should be treated as proven successful examples.
