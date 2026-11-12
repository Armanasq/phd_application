# chinasatokolo/csGraduateApps — one-file doctoral applicant-support directory audit

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/chinasatokolo/csGraduateApps | **Pinned source:** [`d31a1d1eee4acba1fc5f5dfa6c3d26f6294d7e00`](https://github.com/chinasatokolo/csGraduateApps/commit/d31a1d1eee4acba1fc5f5dfa6c3d26f6294d7e00) | **State:** DEEP_REVIEW_DOCUMENTED (full static source-content review) | **Decision:** use as historical applicant-support discovery directory; verify each program's 2026/27 availability separately.

## 1. Purpose and maintained artifact

A curator-maintained list of graduate application support programs and practical CS doctoral application advice for applicants with limited institutional support, emphasizing underrepresented applicants and primarily US universities. The complete default-branch tree contains only a `README.md` and `LICENSE`. There is no application platform, research crawler, vacancy database, structured funding model, test suite or CI pipeline. Last observed upstream push: 2025-09-29.

The README distinguishes degree types (PhD, master's, both) and repeatedly uses `Status Unknown` when it lacks a current cycle update. This is a useful representation of uncertainty; it is not proof any given application assistance program is currently accepting participants.

## 2. Program coverage and source taxonomy

The README table links many university-department mentoring/application review initiatives, including US CS and cognate departments and a small number of international examples. Rows include school, support-program/department link, deadline, applicable degree level and comments. A mixture of Google Forms, university admissions pages, institutional support pages, and community project pages occurs in the same field, so provenance authority varies substantially.

These are **application-support programs** (mentoring, statement review, advice), not doctoral degree admission offers or funded researcher employment contracts. Some are targeting underrepresented applicants and may have eligibility restrictions; applicant ethics and actual program constraints matter.

## 3. Time-sensitive evidence

Many rows are marked `TBD` and `Status Unknown`; dated examples explicitly refer to October/November 2025, and a University of Washington note refers to a September 2025 cycle. These dates must not be forwarded into the 2026/27 intake. The README says it was updating 2025–2026 deadlines, not 2026–2027. At the review date, the renewal status of each link is unknown unless independently retrieved from its official program.

A Google Form that remains online is not sufficient proof of an open/current support program. Each downstream link needs current institution, year, availability and eligibility verification.

## 4. Admissions strategy and scientific-fit methodology

The curator's firsthand advice separates university brand ranking from supervisor fit: identify multiple professors whose active research aligns with the applicant rather than selecting a program solely by a generic rank. This is a qualitative applicant experience, not a validated predictive selection model. It is a useful input for building a research-fit dossier requiring recent papers, methodology fit, lab funding and supervision evidence.

The resource section links research-statement writing, CS SOP corpora, graduate-school preparation guides, fellowship resources and success/advisor discussions. These are separate evidence genres: official admissions advice, peer examples, historical guides and personal reflections.

## 5. Inclusion and source-bias considerations

Support is intended primarily for applicants with limited access to admissions mentoring. Automatically signing up multiple support services without checking specific criteria can divert limited volunteer resources. The directory is US/CS-heavy and not comprehensive across countries or robotics-oriented labs. Applicant support cannot substitute for fee, visa, degree equivalence, language score, tuition or stipend verification.

The list is editorial rather than sampled research: there is no empirical denominator, nonparticipant control, unbiased success-rate estimate or verified outcomes.

## 6. Licensing and data handling

The README footer explicitly identifies a Creative Commons Attribution-NonCommercial 4.0 license (see the license link in the source). Treat reuse of the curated text as noncommercial and attributed unless a separate license grant permits otherwise. Linked external program data and personal essay examples may carry other rights; the directory does not license its outbound sources for copying.

No user-private application data is tracked by this GitHub directory, but original third-party SOPs or personal records linked in it must not be redistributed as public training or research fixtures without permission.

## 7. Transfer decision and required next checks

Adopt: eligibility-aware support-program discovery separate from funding positions, explicit Unknown status, supervisor-fit-first rationale, and original-source links. Build normalized `SUPPORT_PROGRAM` entities with eligibility, school, department, service type, edition/cycle, official URL, last confirmed date and capacity rather than merging these entries with funded doctoral vacancies. Require per-cycle rechecks and prioritization of applicants who meet the target support criteria.

Do not count old assistance-program application dates as open 2026/27 admissions deadlines, and do not treat peer anecdotes as causal odds.

## 8. Pinned evidence and validation limits

- [Entire README and program list](https://github.com/chinasatokolo/csGraduateApps/blob/d31a1d1eee4acba1fc5f5dfa6c3d26f6294d7e00/README.md)
- [Repository LICENSE](https://github.com/chinasatokolo/csGraduateApps/blob/d31a1d1eee4acba1fc5f5dfa6c3d26f6294d7e00/LICENSE)
- [Pinned commit](https://github.com/chinasatokolo/csGraduateApps/commit/d31a1d1eee4acba1fc5f5dfa6c3d26f6294d7e00)

**DEEP_REVIEW_DOCUMENTED — complete GitHub text corpus, not downstream independent verification.** No university support forms, external advice PDFs, applicant identities, runtime or current cycle availability were independently accessed.
