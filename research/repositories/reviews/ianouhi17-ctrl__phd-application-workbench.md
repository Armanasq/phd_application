# ianouhi17-ctrl/phd-application-workbench — deep static admissions operations review

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/ianouhi17-ctrl/phd-application-workbench | **Pinned revision:** [`4bece08790a727a9abce1e6eb400715234b0b731`](https://github.com/ianouhi17-ctrl/phd-application-workbench/commit/4bece08790a727a9abce1e6eb400715234b0b731) | **State:** DEEP_REVIEW_DOCUMENTED (workflow-document audit, native tracker workbook not inspected) | **Verdict:** adapt operations checklists after institution-specific official-source gating.

## 1. Scope and architecture

A field-agnostic, local-first PhD application planning workbench, last updated 2026-06-16. The 30-entry tree contains MIT licensing, a basic `index.html` launcher, Chinese/English Markdown templates, one `00_总控/申请总控.xlsx` spreadsheet, and organized folders for timeline, school/PI selection, CV/research narrative, outreach, SOP, recommendation letters, final submission, interviews and offer comparison.

This is an **editable private operations kit**, not a live funded-vacancy feed, research paper database, or autonomous application agent. The README explicitly tells users to keep completed personal records private.

## 2. End-to-end application lifecycle

The directory encodes a coherent sequence:
1. Build a broad program and PI list, then narrow by scientific fit, funding, rules and deadlines.
2. Develop a one-page research trajectory and factual CV before mass-generating university-specific statements.
3. Track faculty readings, contact attempts, meetings and follow-ups.
4. Prepare SOP and personal-statement source narratives, plus recommendation packets.
5. Verify portal requirements, file submissions, waiver decisions, referee tasks and source deadlines.
6. Save submission receipts and prepare interviews/offer comparisons after actual applications.

The weekly-plan and timeline files are operational checklists; they do not execute any external interaction or prove that a faculty member is hiring.

## 3. Research-fit and document methodology

`02_CV与研究叙事/Research_Summary模板.md` asks for research background, problem/method, the applicant's specific contribution, result/status, future questions, faculty fit, and publications/code/data. The SOP template similarly separates prior projects, method outputs and institution-specific advisors/resources. This is a strong causal narrative design: research claims should be traceable to actual work, not a list of technologies.

The school/advisor matching templates should be extended with verified recent publications, accepted collaborators, official enrollment eligibility, lab funding and active supervision evidence. Suggested PI counts in the timeline are productivity heuristics, not universally appropriate institutional requirements.

## 4. Contact and authorization boundaries

The outreach template includes a first-contact, follow-up and post-submission update. A post-submission message assumes an application was actually submitted; it must be sent only after saving a portal receipt. These are illustrative drafts, not proof that outreach is appropriate or authorized in all institutions. Contact frequency is a plan, not evidence of a successful strategy.

The recommending-referee package separates research area, specific observed applicant contributions and school deadlines. It is appropriate to provide supporting material to a willing referee, but the referee must author and submit a genuine independent recommendation. Never generate fraudulent recommendation letters or publish private referee contacts in a public repository.

## 5. Temporal and financial gates

The `时间线.md` supplies a 2026-to-April-2027 timeline, including November/December application preparation and a sample April 15 decision target. Specific program dates vary by country, funding route, department and intake; the timeline is **not an authoritative deadline source**. The pre-submission checklist explicitly includes application fees, fee waivers, language/GRE requirements, faculty preferences, funding questions and recommendation deadlines.

The offer comparison should separate international tuition coverage, salary/stipend, insurance, employment status, contract duration, supervisor availability and relocation/visa eligibility. These are not automatically represented by one “funded” flag.

## 6. Privacy, editability and missing runtime validation

The README recommends publishing a clean template only, and keeping filled-in CVs, letters, program lists and outreach logs in a private copy. This is an appropriate public/private boundary. The `index.html` is a file launcher rather than an authenticated data store. The native Excel tracker might contain formulas, filters or data validation, but its cells and calculation logic were **NOT inspected** in this review. No actual portal submission, file conversion, sending, spreadsheet test or browser UI validation was performed.

The workbench has no per-opportunity source provenance ledger, immutable receipt evidence model or automatic official-web verification, so its manual statuses must not be treated as externally validated facts.

## 7. Transfer and implementation recommendations

Use the top-level operational state machine, weekly review loop, research-specific CV narrative, applicant-specific statement tailoring and receipt/referee checklist. Integrate it with the PhD workspace's evidence-backed application readiness model: verified program requirements, source checked-on timestamps, applicant-private authorized evidence, `UNKNOWN` gates, and state transitions enforced only by receipts. Maintain separate professor research fit and guaranteed stipend/tuition eligibility.

Any preconfigured timeline should be replaceable by exact institution/cycle dates and timezone-specific deadlines. Keep private applicant documents outside public Git.

## 8. Pinned sources and limits

- [README and privacy policy](https://github.com/ianouhi17-ctrl/phd-application-workbench/blob/4bece08790a727a9abce1e6eb400715234b0b731/README.md)
- [Timeline](https://github.com/ianouhi17-ctrl/phd-application-workbench/blob/4bece08790a727a9abce1e6eb400715234b0b731/00_%E6%80%BB%E6%8E%A7/%E6%97%B6%E9%97%B4%E7%BA%BF.md)
- [Weekly plan](https://github.com/ianouhi17-ctrl/phd-application-workbench/blob/4bece08790a727a9abce1e6eb400715234b0b731/00_%E6%80%BB%E6%8E%A7/%E5%91%A8%E8%AE%A1%E5%88%92.md)
- [Research summary template](https://github.com/ianouhi17-ctrl/phd-application-workbench/blob/4bece08790a727a9abce1e6eb400715234b0b731/02_CV%E4%B8%8E%E7%A0%94%E7%A9%B6%E5%8F%99%E4%BA%8B/Research_Summary%E6%A8%A1%E6%9D%BF.md)
- [SOP template](https://github.com/ianouhi17-ctrl/phd-application-workbench/blob/4bece08790a727a9abce1e6eb400715234b0b731/04_SOP%E4%B8%8E%E6%96%87%E4%B9%A6/SOP%E4%B8%BB%E7%89%88%E6%9C%AC%E6%A8%A1%E6%9D%BF.md)
- [Supervisor outreach](https://github.com/ianouhi17-ctrl/phd-application-workbench/blob/4bece08790a727a9abce1e6eb400715234b0b731/03_%E5%A5%97%E7%A3%81/%E5%A5%97%E7%A3%81%E9%82%AE%E4%BB%B6%E6%A8%A1%E6%9D%BF.md)
- [Referee briefing](https://github.com/ianouhi17-ctrl/phd-application-workbench/blob/4bece08790a727a9abce1e6eb400715234b0b731/05_%E6%8E%A8%E8%8D%90%E4%BF%A1/%E6%8E%A8%E8%8D%90%E4%BA%BA%E6%9D%90%E6%96%99%E5%8C%85%E6%A8%A1%E6%9D%BF.md)
- [Final submission checklist](https://github.com/ianouhi17-ctrl/phd-application-workbench/blob/4bece08790a727a9abce1e6eb400715234b0b731/06_%E7%94%B3%E8%AF%B7%E6%8F%90%E4%BA%A4/%E6%8F%90%E4%BA%A4%E5%89%8D%E6%A3%80%E6%9F%A5%E6%B8%85%E5%8D%95.md)
- [Native tracker workbook path](https://github.com/ianouhi17-ctrl/phd-application-workbench/blob/4bece08790a727a9abce1e6eb400715234b0b731/00_%E6%80%BB%E6%8E%A7/%E7%94%B3%E8%AF%B7%E6%80%BB%E6%8E%A7.xlsx)

**DEEP_REVIEW_DOCUMENTED — static Markdown workflow only.** The substantive source methodology and relevant text artifacts were inspected; workbook binary internals, private records, dynamic UI, official deadlines and external institutional terms remain unverified. No contact/submission was performed.
