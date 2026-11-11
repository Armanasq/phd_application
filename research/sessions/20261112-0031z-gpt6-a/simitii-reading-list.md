# Deep repository investigation — simitii/CS-Grad-School-Applications-Reading-List

**Review date:** 2026-11-12  
**Upstream:** https://github.com/simitii/CS-Grad-School-Applications-Reading-List  
**Pinned default-branch commit:** `189be53b9299ded95d7a6517b6d5760d4286df70` (tree SHA; single README blob `58d7aef8ea0692802fb83e42444e61a27624bdbe))  
**Review state:** DEEP_STATIC_REVIEW_COMPLETE for the curated reading-list artifact; external-link recrawl is partial.  
**Applicability:** admissions methodology, SOP writing, advisor evaluation, historical applicant experience.

## 1. Repository shape and history

The repository has one tracked file, `README.md`, and no application code, tests, schemas, automation, or structured evidence ledger. The README says the list was compiled from resources used for the author's 2019 applications.

GitHub metadata:
- Default branch: `master`.
- Latest commit: 2020-03-02.
- One branch; no issues or pull requests returned.
- No LICENSE file was present in the recursive tree.

This is a curated bibliography, not an admissions workflow implementation or maintained policy database. The repository's age is not itself a defect for conceptual guidance, but it makes deadline, funding, immigration, ranking, and program-specific claims unsuitable for current decisions without independent verification.

## 2. Resource taxonomy and source audit

The README mixes several source classes without recording date, geography, author role, sample size, evidence class, or freshness.

### General admissions and applicant accounts

- Tim Dettmers, “Machine Learning PhD Applications — Everything You Need to Know” (2018): a personal ML PhD application guide. Useful for framing research experience, advisor/program fit, and application preparation. It is historical and largely US/CS/ML-oriented; it is not a current institutional rulebook.
- Mor Harchol-Balter, “Applying to Ph.D. Programs in Computer Science” (CMU PDF): an institutional faculty perspective, but the linked document is a 2014-era guide. Its older GRE/TOEFL and funding context must not be reused as current admissions requirements.
- Matt Might, “HOWTO: Get into grad school…”: broad general graduate-school advice. The README does not capture its publication date, evidence type, or update state.
- Nelson Liu, “Student Perspectives on Applying to NLP PhD Programs” (2019): a first-person/survey-style synthesis of 12 recently successful NLP PhD applicants. This is a small, selected, US-focused sample. It can surface process patterns but cannot estimate admission probability or represent all fields/countries.

### Admissions committee and statement-writing perspectives

- Andy Pavlo, CMU, “How to Write a Bad Statement for a Computer Science Ph.D. Admissions Application” (2015): the author says he reviewed more than 500 applications over two years and shares anonymized, modified, paraphrased examples. Its practical lesson is to lead with research interests and relevant preparation rather than generic childhood-origin stories. This remains useful as a writing heuristic, not a universal scoring rubric.
- “Inside Ph.D. admissions: What readers look for in a Statement of Purpose” (2015-era source): a reader-perspective resource. The list provides no reviewer role, sample, or currentness metadata.
- Swapneel's statement-writing guide and the University of Northern Iowa statement guide are writing resources, not institutional eligibility rules.
- Berkeley Graduate Division's statement-of-purpose page and the University of Maryland CS writing page are the closest items to official institutional guidance in this section. Their current contents were not independently verified in this pass. The README's UMD URL contains `writing-statement-of-pupose` (misspelling), so its link should be corrected or checked before reuse.

### Successful statement examples

The README links to:
- an “Successful Essays” archive dated 2007;
- an older short personal-statement PDF;
- individual CMU, Stanford/MIT, Berkeley and other applicant statements.

These are historical writing artifacts, not validated templates. The repository provides no verified application outcomes, program context, funding results, or permission metadata for reusing the text. Do not copy their prose or infer that every example led to admission. Their value is comparative structure: research trajectory, preparation, specific interests, faculty fit, and the applicant's own voice.

### Rankings and advisor evaluation

- CSRankings is a metrics-based faculty/institution discovery resource. Its methodology counts selected peer-reviewed research-track publications indexed by DBLP, uses fractional authorship, and defines faculty inclusion around full-time tenure-track researchers who can advise CS PhD students. The official site showed DBLP data updated November 2026 at review time. It is useful for finding active publication communities and faculty, not for estimating admission probability, funding availability, supervision quality, or individual research fit.
- CMU's “Questions to Ask a Prospective Ph.D. Advisor on Visit Day” (2020) is a useful checklist for advisor evaluation: mentoring style, group culture, research autonomy, funding, publication expectations, student outcomes, and career support. It reflects an author's experience and a US PhD context, so questions should be adapted to salaried European doctoral employment and other national models.

## 3. Cross-source synthesis

The strongest reusable admissions methodology is not a fixed SOP template. It is an evidence-backed argument:

1. Define a specific research problem and why it matters.
2. Demonstrate preparation through concrete research experience, methods, technical contributions, and results.
3. Explain what the applicant learned, including limitations and unresolved questions.
4. Connect the next research questions to specific faculty, labs, and institutional capabilities.
5. State why the target program's environment is necessary for the proposed development.
6. Keep the statement specific, concise, and supported by verifiable work.

The committee-perspective material converges on a useful negative rule: a statement should not substitute generic motivation or childhood anecdotes for research readiness. A research-oriented opening is generally stronger when it states a concrete technical interest and immediately supports it with relevant work.

Advisor evaluation should be treated as a separate decision process. Questions should establish:
- guaranteed versus competitive funding and the exact funding duration;
- salary/stipend, tuition, fees, and renewal conditions;
- supervision frequency and feedback practices;
- student autonomy and authorship expectations;
- lab culture, student retention, and conflict resolution;
- access to compute, equipment, datasets, and collaborators;
- publication expectations and conference support;
- career outcomes and the PI's current advising capacity.

These questions are more useful than ranking alone. A high-output lab may have no funded position, limited supervision capacity, or poor scientific fit.

## 4. Source quality and limitations

- **Temporal bias:** most references date from 2007–2020. The CMU admissions PDF is especially old for standardized-test and funding details.
- **Geographic bias:** the collection is heavily US/CS-oriented; it does not systematically cover salaried European doctoral jobs, international tuition, country-specific immigration, or non-US funding models.
- **Field bias:** NLP and machine learning experiences do not automatically generalize to robotics, SLAM, inertial navigation, or engineering doctorates.
- **Selection bias:** successful applicant accounts and “successful essays” omit unsuccessful applicants and do not define a denominator.
- **No outcome verification:** the repository does not record whether the examples resulted in admission, funding, or an offer.
- **No provenance model:** publication dates, source types, author roles, sample sizes, source revisions, and last-checked dates are not stored.
- **No source independence analysis:** multiple links may repeat the same admissions advice or refer to the same underlying guide.
- **Copyright/privacy:** personal statements are examples for analysis, not reusable text. Avoid reproducing identifiable details or full passages.
- **License:** no repository license was present; do not assume permission to redistribute the collected materials.

## 5. Reusable method for the PhD admissions workspace

Convert each external resource into a structured source record with:
- canonical URL and publisher/author;
- source class (official policy, faculty advice, applicant experience, essay example, ranking, or general guide);
- publication/update date and last verified date;
- geography, field, degree level, and application cycle;
- sample size and selection method where applicable;
- claims supported and limitations;
- source-dependence links;
- currentness and applicability status.

Use official institutional pages for requirements and funding rules; faculty accounts for decision-process heuristics; applicant experiences for qualitative process signals; rankings for initial discovery only; and essay examples for structure, never as templates. Recheck current funding, deadlines, language requirements, tuition, and visa claims against official sources.

## 6. Final disposition

**DEEP_STATIC_REVIEW_COMPLETE** for the single-file curated resource and the representative linked sources inspected.  
**FULL_EXTERNAL_LINK_RECRAWL_NOT_PERFORMED** for every bibliography entry.  
**NO_ADMISSIONS_OUTCOME_OR_PROBABILITY_INFERENCE_SUPPORTED**.

This repository is useful as a historical source-discovery index. Its greatest contribution is the combination of research-focused SOP guidance, admissions-reader perspectives, and advisor-evaluation questions. It should not be treated as a current, complete, or country-neutral admissions handbook.
