# simitii/CS-Grad-School-Applications-Reading-List — source-level investigation

- Review date: 2026-11-12
- Repository ID: 226577750
- Default branch: master
- Inspected snapshot: 189be53b9299ded95d7a6517b6d5760d4286df70
- Repository: https://github.com/simitii/CS-Grad-School-Applications-Reading-List
- Review state: DEEP_REVIEW_DOCUMENTED (static content audit; no runtime component)
- Confidence: High for structure and link taxonomy; medium for linked-source utility; low for current applicability beyond 2019.

## 1. Problem and intended audience

The author describes a compilation of resources used during their 2019 graduate applications. It is a curated discovery index for CS graduate applicants, covering general advice, admissions perspectives, SOP guidance, successful essay examples, rankings, and prospective-advisor questions. It is not a vacancy finder, funding database, application tracker, eligibility engine, or evidence-verification system.

## 2. Complete structure and artifacts

The recursive default-branch tree contains exactly one tracked file: README.md (2,434 bytes). There is no application code, data schema, structured metadata, tests, CI, release process, or runtime.

The README has six substantive groups: general graduate-school advice; admissions-process reflection; SOP guidance; successful essay examples; CS program rankings; and questions to ask a prospective PhD advisor. It links to 16 external resources, including a 2019 NLP applicant-perspectives synthesis, faculty-authored CS admissions advice, university writing guidance, sample SOP PDFs, CSRankings, and an advisor-visit question guide. A link is a retrieval pointer, not proof that the target is current or authoritative.

## 3. Information architecture and implied workflow

The curation order implies a preparation sequence: understand the admissions process; learn how faculty and committees evaluate research potential; prepare an SOP using institution-specific instructions; compare examples for structure; identify departments and faculty by research fit; and prepare questions for advisor meetings. This is an editorial taxonomy, not an executable workflow. There are no prerequisites, decision states, application records, reminders, funding gates, or submission evidence.

## 4. Evidence and source-quality assessment

The repository itself is a secondary index. Its most useful linked source is Nelson Liu et al., “Student Perspectives on Applying to NLP PhD Programs” (2019), a synthesis of twelve recently successful applicants, primarily about US NLP PhD programs. It explicitly cautions that contributors are not admissions authorities and experiences do not generalize uniformly. This is a small selected sample, not a representative dataset.

The linked source reports recurring themes: faculty fit was the dominant school-selection consideration for respondents; some preferred at least two relevant faculty; many applied to roughly 8–13 programs, which is descriptive rather than a target quota; recommendation letters were consistently ranked highly; publications were useful signals but not universally necessary; prior faculty email was not universally helpful; and interviews often probed the applicant’s research choices, reasoning, conclusions, and learning.

These are preparation hypotheses, not calibrated admissions rules. The cohort is historical, field-specific, and geographically skewed. The README links university writing pages and sample essays without preserving access dates, version snapshots, author consent, program-cycle context, or source-dependency metadata.

## 5. Technical and operational assessment

There is no software implementation to execute or test. The only maintained artifact is a Markdown list. It has no structured fields for URL, original author, source type, publication/access date, geographic scope, cycle, last-checked timestamp, availability, or confidence. Link rot and changed university policies can silently degrade the resource.

The commit history contains seven README-only commits from December 2019 through March 2020. The latest update is 2020-03-02. The repository has no open issues or pull requests. No license file is present in the inspected tree; do not assume linked essays or PDFs are licensed for redistribution.

## 6. Limitations and failure modes

- Temporal drift: source guidance and examples are from 2015–2020, not current 2026/27 policy.
- Geographic bias: content is strongly US/CS-oriented and does not model salaried European doctoral employment, international tuition, immigration, or country-specific funding.
- Selection bias: successful applicants’ retrospective accounts omit unsuccessful applicants and do not establish causal success factors.
- Source dependence: faculty advice and applicant-perspective posts recur across curated repositories. Multiple links do not create independent evidence.
- Missing provenance: official guidance, personal advice, anecdotes, rankings, and essay examples are not distinguished structurally.
- Document safety: public essay examples should not be copied; distinctive prose and personal information require care.
- Maintenance: link availability and current policy status have not been verified.

## 7. Reusable methods and adoption decision

Adopt as a discovery taxonomy, not an admissions decision authority. Preserve separate classes for process advice, faculty perspectives, official writing requirements, sample documents, rankings, and advisor-meeting preparation. Convert each link into a source record with canonical URL, original author, source class, publication/access date, geography, field, cycle, supported claims, last verification, and dependency edges.

Translate useful qualitative advice into evidence-backed actions: build a broad faculty/program set then narrow it using recent papers, methods, advising capacity, and funded openings; ask recommenders for research-specific evidence; present a truthful research narrative grounded in contributions, decisions, experiments, failures, and conclusions; follow current official SOP instructions; and contact faculty only when invited or when there is a well-founded research discussion.

Do not infer acceptance probabilities, publication thresholds, or universal email strategies from this repository.

## 8. Cross-repository relationships and evidence

This repository shares original sources with shaily99/advice, pliang279/awesome-phd-advice, and other curation lists. The Nelson Liu article is one underlying source, not multiple independent observations. It overlaps conceptually with jedyang97/awesome-cs-phd-application-advice and poloclub/awesome-grad-school.

External source inspected: https://blog.nelsonliu.me/2019/10/24/student-perspectives-on-applying-to-nlp-phd-programs/. Its disclaimer and US/NLP scope should accompany any extracted recommendation.

## 9. Coverage and verification

Inspected: complete recursive tree; full README; repository metadata and default branch; seven-commit history; open issues and pull requests; and the linked applicant-perspective source.

Not performed: runtime tests (not applicable); exhaustive verification of every external link; license/legal review of third-party documents; interviews with authors/respondents; or independent outcome validation.

Final disposition: deep static review complete for this one-file curation repository. Retain as a historical discovery index with strong source-quality and transferability caveats.
