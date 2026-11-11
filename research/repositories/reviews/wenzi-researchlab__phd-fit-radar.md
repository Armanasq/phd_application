# Deep document review — wenzi-researchlab/phd-fit-radar

## 1. Repository identity
- Canonical: https://github.com/wenzi-researchlab/phd-fit-radar; owner wenzi-researchlab; MIT license per GitHub API.
- Snapshot `cfe52cf49a75b79c36ebf01ea07faab166886c93`, last code/docs update 2026-08-16; reviewed 2026-11-11. Repository API indicates neither fork nor archive, and sampled issues/releases are empty.
- Four-file documentation corpus: [README.md](https://github.com/wenzi-researchlab/phd-fit-radar/blob/cfe52cf49a75b79c36ebf01ea07faab166886c93/README.md), [rubric.md](https://github.com/wenzi-researchlab/phd-fit-radar/blob/cfe52cf49a75b79c36ebf01ea07faab166886c93/rubric.md), [report-template.md](https://github.com/wenzi-researchlab/phd-fit-radar/blob/cfe52cf49a75b79c36ebf01ea07faab166886c93/report-template.md), MIT LICENSE. Audience global applicant/supervisor research fit; no specific funding region.

## 2. Problem and decision context
The document set proposes a disciplined **applicant-supervisor fit assessment** instead of superficial topics and keyword overlap. It examines academic eligibility, experience, research questions, methods, lab resources, degree qualification, research output and proposal feasibility. Research fit is not an acceptance prediction and cannot replace a formal call or supervisor consent.

## 3. Actual method, schemas and reproducibility
- [rubric.md](https://github.com/wenzi-researchlab/phd-fit-radar/blob/cfe52cf49a75b79c36ebf01ea07faab166886c93/rubric.md) is a long (454-line) 11-dimension qualitative framework: academic preparation, admission feasibility, research experience, topic, methods, theory, publications, supervision availability, proposal, applicant readiness and risks. It distinguishes clear, partial, not provided, verify and not applicable evidence labels.
- The rubric allows **0–5 scores**, but explicitly warns that numeric fit cannot be calculated from keywords alone. A human must judge source evidence/actual methods; a 4/5 is not a probability of admission.
- [report-template.md](https://github.com/wenzi-researchlab/phd-fit-radar/blob/cfe52cf49a75b79c36ebf01ea07faab166886c93/report-template.md) provides a 479-line report with applicant snapshot, supervisor research, evidence/gap status, eligibility, topic/method analysis, proposal/fit risk and next steps. Template prompts anonymized applicant identity.
- No runnable scoring library, live author publication integration, benchmarking code or university-specific admission database is present in the inspected four-file tree. Thus **methodological template exists, implementation does not**.

## 4. Critical methodology
Strengths: rejects naive paper-title/keyword matching, understands feasible methods may differ from identical lab subjects, includes equipment, data and PI recruitment gates, makes absence of evidence explicit, and recognizes changing applicant research.
Risks: 0–5 judgments can invite false numerical precision; no trained model or validated inter-rater reliability, no calibration to selection outcomes, no applicant-cohort counterfactuals, and users may silently overweight prestigious labs. Critical constraints (funding/visa/degree/country) are not auto-checked. A long report can appear authoritative even with largely inferred fields.
Transferability: method/resource fit applies to lab-led robotic SLAM in Switzerland/Australia and to proposal-led training in UK/Canada, but supervisor-first selection is not universal. It should never override a formal centralized EPFL EDIC route or UK overseas-fee stipulation.

## 5. Applicant action
Use an **evidence matrix**, not a synthesized acceptance score: applicant claim and verified artefact (e.g. inertial estimator with RMSE, actual documented DOI) × last 24-month lab paper with method/data, known equipment, open funded budget and verified formal master's/language gates. Score dimensions only after source capture and label unknown vs irrelevant separately. Strongest useful output is a testable proposed collaboration question, not a single prestige score.

## 6. Comparison
- [PeiMu/findPhdPositions](https://github.com/PeiMu/findPhdPositions) retrieves conference authors via web spider; WenZi offers stronger qualitative assessment but no automated author retrieval.
- [SihengTao/phd-application-planner](https://github.com/SihengTao/phd-application-planner) has *implemented* provenance validation and stable program/advisor keys, but more elaborate program intake; WenZi is a field fit/report rubric only.
- [erikpsw/phd-application-pipeline](https://github.com/erikpsw/phd-application-pipeline) emphasizes outreach and CRM rather than methodological opportunity eligibility. None independently establishes recruiting availability.

## 7. Research judgment
**ADAPT scientific-fit rubric with compulsory source/eligibility hard gates.** The distinction between authentic scientific methodological compatibility and keyword matches is substantively useful. Do not copy its 0–5 ratings as statistical admissions chances. Reproducibility of written template exists; *predictive validity is untested*.

## 8. Evidence gaps
Inspected relevant README/rubric/report sections and complete four-file tree, not a full independent semantic verification of every sentence. License and commit metadata were checked; issues/releases absent in inspected API endpoints. No third-party runtime exists to run, and no observer reliability or prospective outcome dataset was found. Future review should benchmark multiple independent human raters on actual published papers and compute disagreement rather than fabricate fit accuracy.
