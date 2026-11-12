# ktwu01/Awesome-Academic-CV — deep academic-CV guide and license review

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/ktwu01/Awesome-Academic-CV | **Pinned revision:** [`05c4b39379315ac3419fe9391c42c2d01de09d9b`](https://github.com/ktwu01/Awesome-Academic-CV/commit/05c4b39379315ac3419fe9391c42c2d01de09d9b) | **State:** DEEP_REVIEW_DOCUMENTED (static full-text review) | **Decision:** use conceptual CV quality checklist only; prohibit copying/derivation until license conflict and permissions are resolved.

## 1. Identity, actual purpose and corpus

A small text-only guide for preparing research-focused CVs for doctoral applicants, postdoctoral researchers and academic/industry R&D candidates. The tracked eight-file repository includes README, checklist, best examples, content tips, formatting guidelines, common mistakes and a LICENSE. Last observed default-branch commit: 2025-06-11. It has no admissions database, vacancy crawler, empirical application outcome dataset, formal source-checking framework, tests, or CI.

The guide provides narrative and layout suggestions, not proof that any exemplar received an admission, scholarship or faculty appointment.

## 2. Academic writing and CV structure

`Checklist.md` requires accurate contact information, logically ordered education and research sections, current publication records and explicit differentiation of peer-reviewed publications from preprints/manuscripts. `Content-Tips.md` encourages problem/contribution/outcome bullets, quantitative claims when supported, publication citations, specific teaching roles and project code links.

These are useful editorial practices. The suggested one-to-two-page maximum is **not** a universal academic standard: established researchers and some institution-specific CV formats require substantially longer publication records. Any reported impact percentage must be traceable to the applicant's own verified experiment or institutional source, not filled from an example.

## 3. Examples and factual validity

`Best-examples.md` links several external research CVs and includes illustrative LaTeX/Markdown CVs for early-stage PhD, senior PhD, postdoctoral, industry research and fellowship applications. The examples include names, sample affiliations, journal entries and output metrics. They are illustrative formatting data; no claim of authorship, publication indexing, degree award or admissions result was independently verified.

Some illustrative citations use non-resolving placeholder DOI forms such as `10.xxxx/...`; these must never be imported into an applicant's bibliography. The guide references `examples/Postdoc_Compact.tex`, but the complete eight-file repository does **not** contain an `examples/` folder or that target file. That is a broken source reference, not a usable linked template.

## 4. Formatting and reproducibility

`Formatting-Guidelines.md` proposes typographic and spacing conventions, concise evidence-oriented bullets, clean PDF filenames, page metadata, monochrome legibility, and XeLaTeX/ModernCV options. These are advice rather than mandatory program rules. It also contains a malformed Markdown formatting row in the XeLaTeX section and a recommendation to run an “automated linter” that is not present in the source tree.

There is no build/test workflow, PDF compile fixture, link checker, metadata validator or evidence-backed layout study. The guidance cannot be accepted as a reproducible compiled template suite without implementation and render testing.

## 5. Critical licensing conflict

The README labels the content as “MIT License · Free to use and adapt with attribution,” **but the repository's actual `LICENSE` file is Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**, which restricts commercial use and sharing derivatives. These statements materially conflict. Do **not** interpret the README's MIT sentence as permission to adapt and redistribute the materials, especially inside a commercial or publicly republished CV generator, without clarification from the owner and legal review.

The two known forks `kokomomo250/Awesome-Academic-CV` and `ktwugoat/Awesome-Academic-CV` are derivatives of this project; at the inspected snapshot, they share the same fork tree and commit with each other, but **not** the latest parent commit. They are not independent admissions evidence. Do not multiply guide corroboration or assume a downstream fork changes the parent's license.

## 6. Evidence hierarchy and common mistakes

`Common-Mistakes.md` warns against vague achievements, unverified metrics, mixed publication states, excessive clutter and weak scientific contribution descriptions. These are broadly reasonable heuristics but do not establish causal admission success. The collection has no comparison cohort, acceptance statistics, institution-specific eligibility checklist or official source verification.

The guide sometimes mixes professional résumés, formal academic CVs, ATS optimization and doctoral applications; these formats require distinct emphasis and length. Selection should be driven by target instructions and verifiable scientific claims.

## 7. Transfer decision

Retain only *concepts* of version-controlled master CV, target-specific research narrative, source-backed DOI/title/year metadata, discrete publication states, applicant contributions, clear dates and a final PDF visual check. For any generated applicant CV:
1. Start from original user-owned text and verified publications.
2. Preserve a machine-readable source of truth and per-claim provenance.
3. Confirm program-specific section order, file type and page limit.
4. Render and visually verify PDF layout, fonts, links and metadata.
5. Keep personal contact, referee data and unpublished research material private.
6. Do not copy or adapt this guide's protected source text or example CVs until the licensing conflict is resolved.

## 8. Pinned evidence and validation limits

- [README and MIT claim](https://github.com/ktwu01/Awesome-Academic-CV/blob/05c4b39379315ac3419fe9391c42c2d01de09d9b/README.md)
- [Actual CC BY-NC-ND 4.0 LICENSE](https://github.com/ktwu01/Awesome-Academic-CV/blob/05c4b39379315ac3419fe9391c42c2d01de09d9b/LICENSE)
- [Applicant content checklist](https://github.com/ktwu01/Awesome-Academic-CV/blob/05c4b39379315ac3419fe9391c42c2d01de09d9b/Checklist.md)
- [Mistakes and publication-state advice](https://github.com/ktwu01/Awesome-Academic-CV/blob/05c4b39379315ac3419fe9391c42c2d01de09d9b/Common-Mistakes.md)
- [Research impact writing tips](https://github.com/ktwu01/Awesome-Academic-CV/blob/05c4b39379315ac3419fe9391c42c2d01de09d9b/Content-Tips.md)
- [Formatting guide](https://github.com/ktwu01/Awesome-Academic-CV/blob/05c4b39379315ac3419fe9391c42c2d01de09d9b/Formatting-Guidelines.md)
- [Examples and broken path](https://github.com/ktwu01/Awesome-Academic-CV/blob/05c4b39379315ac3419fe9391c42c2d01de09d9b/Best-examples.md)

**DEEP_REVIEW_DOCUMENTED — full static Markdown corpus inspected.** No external example CVs, DOI records, underlying academic outcomes, PDF compilations, copyright legal opinions or third-party acceptance rates were independently validated. The repository provides advice, not an official admissions standard.
