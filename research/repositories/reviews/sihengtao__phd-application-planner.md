# Deep review — SihengTao/phd-application-planner

## 1. Repository identification
- **Canonical:** https://github.com/SihengTao/phd-application-planner
- **Owner:** SihengTao. MIT license (GitHub API). Created July 2026; inspected 2026-11-11 at commit `3ce7b573904b94000b562f90c3cefee694874794`; most recent commit 2026-10-27. No GitHub releases observed.
- **Category:** research/workflow software; program/PI matching, source checks, decision dashboard and export. Global and cross-disciplinary, with substantial US-specific sample fields.
- **Review mode:** implementation, schema, tests and methodology source inspected; **TESTS NOT EXECUTED** by this review.

## 2. Problem definition and applicant assumptions
A Claude Code/Codex workflow takes user intake, researches programs and advisors, creates a structured evidence-aware dataset, validates it and builds marimo/Excel outputs. Assumes an LLM agent with web research/host capabilities, reliable instructions, and the user's relevant private profile. Not a national authority and not an autonomous source-of-truth backend.

## 3. Architecture and observed code
- [Entry skill contract](https://github.com/SihengTao/phd-application-planner/blob/3ce7b573904b94000b562f90c3cefee694874794/SKILL.md): intake → research → check_data → build_data → marimo/Excel results, with checkpoint files and private note semantics.
- [Schema](https://github.com/SihengTao/phd-application-planner/blob/3ce7b573904b94000b562f90c3cefee694874794/reference/schema.md): canonical `_wf_result.json`, stable program/advisor IDs, source records, field-level claim references, null for unresolved data; separate research output from application tracker and PIs.
- [Source policy](https://github.com/SihengTao/phd-application-planner/blob/3ce7b573904b94000b562f90c3cefee694874794/reference/source_policy.md): `claimPaths`, access dates, effective application cycle, first-pass vs independent `confirmed/corrected/conflict/unresolved` status; online link reachability does not substantiate claim text.
- [Python validation implementation](https://github.com/SihengTao/phd-application-planner/blob/3ce7b573904b94000b562f90c3cefee694874794/assets/data_quality.py): stdlib checks types, enumerations, duplicate IDs, high-risk fields, source cross-refs, URL/date shapes, online checks with 50-URL cap and time budget, private/loopback IP blocking for SSRF prevention.
- [Test suite](https://github.com/SihengTao/phd-application-planner/blob/3ce7b573904b94000b562f90c3cefee694874794/tests/test_data_quality.py): tests duplicates, invalid policy/booleans, false verification, reconciliation conflicts, SSRF/redirect guards and validator report atomic-write failure behavior. Presence is verified, passing tests were **not** independently observed.
- [Build/export code](https://github.com/SihengTao/phd-application-planner/blob/3ce7b573904b94000b562f90c3cefee694874794/assets/build_data.py): validation gates, temporary files, rollback-protected derived JSON commit. `requirements.txt` lists marimo, numerical, plotting and Excel packages with minimum but not lock-pinned versions.
- [Merged PR #2](https://github.com/SihengTao/phd-application-planner/pull/2) added concise tracker exports; no external release is verified.

## 4. Critical methodological assessment
**Strengths:** explicit distinction between source presence and claim verification; conflict supersession; offline safe structure check; stable entity IDs; bounded network checking; XlsxWriter/openpyxl output escaping for spreadsheet formula injection (documented, not independently executed). Better data-engineering methodology than most prompt-only admission agents.

**Limits:** independent evidence research requires a *second actor to actually retrieve and judge source content*. A validator reading a `confirmed` label in JSON cannot prove that a human/model genuinely verified what the PDF says; semantic truth remains outside mechanical checks. A global source-count metric is not review quality. `program_id` stable only if institutional name canonicalization remains consistent; maintainer warns not to rekey from list order. `nearbyFood` feature is unrelated to funded PhD admissions and should not contaminate priority ranking. US-only examples and optional applicant-specific floor estimates should not become globally hardcoded.

**Security/operational:** private notes are excluded from exported workbooks by default according to spec. Verify runtime storage locations, file permissions, actual user data leakage and redaction before importing anything. Extensive 80KB validator and marimo UI have not been end-to-end run here. External program funding and deadlines depend wholly on researcher source quality, not code generation.

## 5. Relevant admissions practice
Adopt the idea of **field-level traceability** for program deadline, international funding, supervisor recruiting evidence and language-exemption gates. Reject blanket verified badges. Candidate must still check official international tuition/immigration; staffing models are national exceptions.

## 6. Comparative assessment
Compared with [fanyi3017-stack/phd-application-research-agent](https://github.com/fanyi3017-stack/phd-application-research-agent), this project includes concrete schema, data quality scripts and tests instead of only a multilingual agent prompt. Compared with [zhoujasper/phd-atlas](https://github.com/zhoujasper/phd-atlas), narrower intake/research workflow but richer explicitly described independent-claim checking; PhD Atlas has more operational applicant CRM. These are complementary, not independent outcome studies.

## 7. Judgment
**ADAPT METHODOLOGY (priority).** Use separate evidence retrieval, factual reconciliation, stable keys, structural verification, and draft-only exports in the current local-first repository. Do not vendor third-party code without verifying license and tests; do not adopt the restaurant subsystem. High confidence in implemented validation *logic existing*, unknown in real-world retrieval accuracy and runtime reliability.

## 8. Evidence and unresolved work
All source links above point to pinned snapshot or GitHub PR. Not reviewed: complete UI components (~113KB dashboard), full ~80KB validator line-by-line, integration with web provider credentials, actual Marimo startup, third-party dependency versions and independent repeated data-check run. No claims of passed third-party tests.
