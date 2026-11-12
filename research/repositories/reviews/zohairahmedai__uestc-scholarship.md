# zohairahmedai/uestc-scholarship — 2026 recruitment landing-page audit

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/zohairahmedai/uestc-scholarship | **Pinned source:** [`eb9c12091c20837fd94cefdadc8080cb390e523e`](https://github.com/zohairahmedai/uestc-scholarship/commit/eb9c12091c20837fd94cefdadc8080cb390e523e) | **State:** DEEP_REVIEW_DOCUMENTED (static one-file source review, external claims unverified) | **Decision:** preserve as expired 2026 intake advertisement, not a currently open scholarship.

## 1. Publication and format

A repository containing only `index.html`, a 654-line self-contained static recruitment landing page for UESTC China Fall 2026 PhD/master's applications in AI/CS. The page includes embedded CSS and basic display scripts and imports external Bootstrap, Font Awesome and Google Fonts assets. There is no application backend, student eligibility validator, official-source updater, database, test suite, workflow or LICENSE file in the inspected tree. Latest upstream source was observed 2025-10-02.

A university name/logo and copyright footer in a third-party GitHub page do not prove the account is an institution-operated official admissions source.

## 2. Research offer and scientific themes

The landing page promotes a named faculty supervisor and advertises computer vision, large language models, vision-language models and AI agents. It references a Google Scholar profile and rankings pages. Those are *external outbound links*, not validated supervisor identity, current publication metrics, current group capacity or admission eligibility.

Source text cites paper/publication counts, citation/h-index and UESTC subject rankings for historical periods. None were independently checked or normalized for year, source version and researcher entity. Avoid transferring them as current authoritative claims.

## 3. Application window and current status

The document explicitly states:
- **Application deadline:** late February 2026 (not an exact dated time, zone or portal deadline).
- **Enrollment:** late August 2026.

Both are in the past on 2026-11-12. No later intake, rolling route or extension is documented in the repository. The page's urgency language “first come, first served” is marketing copy, not evidence of a currently open application portal. State: `HISTORICAL_2026_SOURCE`, with `CURRENT_RECRUITMENT_UNKNOWN_NOT_OPEN_VERIFIED`.

## 4. Funding component claims and internal uncertainty

The page lists a “base scholarship” as 1,500 RMB monthly plus tuition waiver, campus dormitory and medical insurance. It separately describes CSC government scholarship options of 3,500 RMB/month for PhD and 3,000 RMB/month for master's students and advertises a minimum monthly guarantee of 2,000 RMB for all students.

These amounts are *claims within a third-party promotional source*. The relation between the 1,500 RMB base stipend and the claimed 2,000 RMB minimum (possible top-up) is **not specified**, and CSC terms may involve separate selection/award conditions. The page provides no award-owner verification, formal contractual terms, duration, tuition-category detail or international applicant-specific evidence. Do not represent “all students guaranteed” as a verified personal stipend entitlement.

## 5. Eligibility and application route

The page advertises AI research experience, preferred publications, and a language condition of TOEFL 80+, IELTS 5.5+, or previous English-medium undergraduate study. These requirements may differ by specific school, nationality, teaching medium, scholarship award and intake year; no university-issued official admissions policy was independently retrieved.

Its “Apply Now” call to action is a mailto contact link, not a validated 2026 university submission portal. This source does not supply a receipt, application status API, user consent process or fee/award approval.

## 6. Trust, security and source quality

The deployment is static presentation code with no server-side applicant record handling in the inspected repository. This reduces direct backend-attack scope but creates a provenance/authenticity risk: the page can advertise institutional branding, grants and named supervisors without an institution-signed source reference or verified publication cycle. Third-party mailto contact should not be used as proof of official admission channel.

The landing page links Google Scholar, rankings and university references, yet no claim-level citation ledger, independent cross-check timestamp or original policy/award document is recorded. External fonts/CDN dependencies are not audited here.

## 7. Transfer and interpretation

Keep an immutable source observation for the Fall 2026 lab advertisement and split claims into research area, supervisor claim, language threshold claim, admission window, purported base award and CSC option. Annotate each as `SOURCE_STATED_NOT_INDEPENDENTLY_VERIFIED` and create an official-source follow-up task for any future intake. If a 2027 call is later discovered, create a separate cycle/version; do not change the expired 2026 page into a current vacancy.

The relevant system pattern is source-claim decomposition with separate proof gates, not code reuse. No private applicant documentation should be sent to the contact merely because a static page claims eligibility or stipend coverage.

## 8. Evidence and validation boundary

- [Pinned static recruitment page](https://github.com/zohairahmedai/uestc-scholarship/blob/eb9c12091c20837fd94cefdadc8080cb390e523e/index.html)
- [Pinned repository revision](https://github.com/zohairahmedai/uestc-scholarship/commit/eb9c12091c20837fd94cefdadc8080cb390e523e)

The tracked HTML page structure and substantive research, scholarships, criteria, deadline and contact sections were inspected. The official UESTC admissions system, ranking providers, claimed supervisor identity, award owner, contact legitimacy, current recruiting capacity and financial coverage were **NOT independently verified**. No application/outreach occurred. This is a deep static **source-content** audit, not a verified current opportunity record.
