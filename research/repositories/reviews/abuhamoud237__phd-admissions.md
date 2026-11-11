# abuhamoud237/phd-admissions — PhD-by-research workflow portal review

**Date:** 2026-11-11 · **Commit:** [f4c5edb90ed4d4a612fa1402a788cd8853da18b3](https://github.com/abuhamoud237/phd-admissions/commit/f4c5edb90ed4d4a612fa1402a788cd8853da18b3) · **State:** PRELIMINARY_FOCUSED

**Verdict:** REFERENCE — useful workflow description, not a complete application system. **Risk:** static_shell_external_forms_uninspected_no_data_model.

## Product and actors

The complete repository contains one file, `index.html`: an Arabic, right-to-left landing page for an Engineering College PhD-by-Research-Only process at Wadi Al-Shati University. It separates student and academic-supervisor journeys and provides a reference-number status inquiry route. It is a static process-explanation/navigation page, not a backend.

## Student workflow described

1. Submit an application and supporting documents.
2. Scientific council of the selected department reviews it.
3. After preliminary approval, use a reference number to view supervisor-proposed topics.
4. Select a topic; the council reviews the selection and consults the supervisor.
5. Following approval, obtain supervisor contact details and prepare a research proposal.
6. Topic is associated with three courses/subject areas. A comprehensive exam is described as occurring three months after topic approval and includes proposal presentation, written examination and oral interview.
7. Final registration follows successful completion of the exam.
8. The page states semester progress reports, a maximum 36-month thesis period and at least three papers, one indexed in Scopus or Web of Science.

These are claims stated by the page, not independently verified university regulations.

## Supervisor workflow described

A supervisor registers, submits at least one proposed research topic, associates three relevant courses/areas with each topic, and waits for scientific-council review. Approved topics become available to applicants; the page describes email notification and subsequent communication with the council chair.

## Workflow dependencies

`Applicant → Application → Department review → Provisional approval → Topic catalogue → Topic selection → Supervisor approval → Proposal → Course package → Comprehensive exam → Final registration → Progress reports → Thesis/publications`

The supervisor-side path is `Supervisor registration → Eligibility/review → Proposed topics → Course mapping → Council approval → Published topic availability`.

A real implementation would require explicit entities for applicants, supervisors, departments, applications, uploaded documents, topics, topic-course mappings, decisions, reference numbers, exam attempts, progress reports and publication evidence. It would also need versioned policy rules, permissions, notifications and audit events. None is implemented in this repository.

## Integration boundary and defects

Registration, supervisor onboarding and status inquiry point to external Google Apps Script URLs. Their source code, database schema, authorization and retention behavior are absent and were not inspected. The page retains `REPLACE_WITH_DEPLOYED_URL` metadata and a legacy `REPLACE_WITH_SUPERVISOR_FORM_EXEC_URL` link. Inline JavaScript only switches sections. No validation, persistence, migrations, backend or tests exist.

## Decision

Use only as a workflow-description reference. Verify every stated duration, publication requirement and exam rule against official regulations before relying on it.

**Evidence:** [repository](https://github.com/abuhamoud237/phd-admissions) · [pinned HTML](https://github.com/abuhamoud237/phd-admissions/blob/f4c5edb90ed4d4a612fa1402a788cd8853da18b3/index.html).