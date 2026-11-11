# Cross-repository architecture and evidence crosswalk — PhD application platforms

**Prepared:** 2026-11-12. **Evidence boundary:** implementation-level static inspection of pinned GitHub revisions. No current program policy, user eligibility, funding award, deployed service, penetration test or third-party runtime is verified.

This crosswalk integrates four independently scoped reviewed source projects:
- [xujingchen1996/research-app-toolkit](../../../repositories/reviews/xujingchen1996__research-app-toolkit.md) — multi-host application workflow prompts and local state.
- [ssine/willow](../../../repositories/reviews/ssine__willow.md) — historical admission-outcome statistics and unrestricted MongoDB API.
- [sushil3710/PHD_Admission_Portal](../../../repositories/reviews/sushil3710__phd-admission-portal.md) — institution-side admission cycles, document submission, eligibility and decision messaging.
- [Ariaeimehr/PHD-Position-Finder](../../../repositories/reviews/ariaeimehr__phd-position-finder.md) — vacancy discovery/notification pipeline.
- [atomdbc/scholarship_scraper](reviews/atomdbc__scholarship_scraper.md) — general scholarship extraction with browser and LLM.

## 1. Distinct entities that must not be conflated

| Domain entity | Representative implementation | Evidence required to trust a claim |
|---|---|---|
| Raw discovered vacancy | Ariaeimehr and atomdbc crawlers | Employer-specific canonical URL, fetched page and timestamp |
| Funding offer terms | Not independently verified by either crawler | Award/salary or contract source, period, international fee coverage, nationality/visa restrictions |
| Institution/program/cycle | Willow and sushil3710 | Current official program page and local cutoff timezone |
| Applicant research profile | xujingchen1996, Willow | Consent-based, revisioned CV/publication evidence; keep private |
| Submitted application | sushil3710 | Portal receipt, submission ID, timestamp, final artifact checksum |
| Admission decision | sushil3710 applicant status vs Willow anecdotal result | Institution-issued decision with applicant consent and source identity |
| Outreach email | xujingchen1996 draft vs sushil3710 result mail | Explicit sending authority and delivery receipt, separate from generation |
| Source verification state | Missing or weak across sampled systems | Claim-level status, immutable source observation, independent check and contradiction handling |

**Key rule:** A scrape finding is not a funded doctoral offer. A dashboard record is not verified eligibility. A generated email is not an email sent. A historical applicant outcome cannot establish present admission probability.

## 2. Trust-boundary comparison

1. **External URL to crawler:** atomdbc's Playwright worker follows user-controlled URLs without a strong private-network/redirect policy; Ariaeimehr applies funding/geography labels based on heuristics and static defaults. Source adapters must isolate egress, bound visits and retain raw evidence rather than granting truth status to extracted text.
2. **Crawler text to LLM:** atomdbc sends source text to an AI extraction step, but an LLM-generated confidence score is not calibrated evidence and may contain instruction-bearing source content. Use a typed output proposal with source-span attribution and a separately verified field status.
3. **Applicant data to public API:** Willow exposes unrestricted GET/PUT collection operations; sushil3710 has per-handler JWT checks but leaves critical file/email routes without authorization and handles sensitive material in public-looking file directories. Use central authentication, least-privilege row checks, private object storage and privacy-preserving aggregate views.
4. **Model/agent to local workspace:** xujingchen1996 uses workspace-local record files, revision hashes, sandbox-policy gates and host-scoped integration. These are more useful for controlled drafting, but need stronger cross-process isolation and explicit user confirmation for external actions.
5. **Admin bulk change to applicants:** sushil3710 ingests spreadsheet decisions row by row, drops a final row unconditionally, and sends emails from a separate handler. A proper lifecycle requires dry-run preview, schema/identity validation, reviewer authorization, transaction boundaries and an append-only decision/notification log.

## 3. Minimum target data model

`Source` -> `FetchAttempt` -> `Snapshot` -> `RawRecord` -> `ExtractedClaim` -> `VerificationDecision` -> `CanonicalOpportunity`.

A verified opportunity can be linked to `Institution`, `Program`, `Lab`, `RecruitingSupervisor`, `FundingTerms`, `EligibilityRule`, `Deadline` and one or more source-alias records.

On the user side, `ApplicantProfileRevision`, `EvidenceArtifact`, `ApplicationDraft`, `SubmissionReceipt`, `InstitutionDecision` and `CommunicationReceipt` are private records with independent access policies. `ApplicationStatus` must be derived from permitted transitions and recorded evidence; never inferred from a UI button state, a source-link existence check, or an agent's generated narrative.

For outreach and alerts, persist an outbox with `PENDING`, `RETRYABLE_FAILURE`, `SENT`, `CONFIRMED`, `CANCELLED` and `DEAD_LETTER` states. Do not mark a vacancy permanently notified merely because it was observed; mark successful delivery from the transport receipt.

## 4. Required engineering acceptance tests

- Canonical URL normalization, SSRF redirect/private-IP blocks, page-budget/timeouts, source parser fixture drift detection and immutable HTML/PDF hashes.
- Official-source funding and eligibility tests, including missing/unawarded/conditional statuses, applicant-dependent foreign tuition and offer dates.
- API authorization per role, applicant/tenant and resource; prohibit unrestricted MongoDB queries and unsafe SQL table-name composition.
- File uploads: type/size validation, random names, no public static access to private records and safe deletion.
- Explicit consent and provenance for historical applicant examples; small-n and survivorship caveats on distribution charts.
- Signed/authorized admission transitions, complete copy/field mapping, spreadsheet dry-run and transactional import.
- Read-only skill/workspace tests, revision conflicts, symlink safety, external-action approval, email outbox idempotency.
- Runtime integration tests and privacy/security scans before any claim of production readiness.

## 5. PhD application strategy implication

For the researcher's AI/robotics PhD campaign, the most useful output of these projects is an **evidence-aware decision workspace**, not another unverified position list or admission-probability widget. Search and supervisor matching remain discovery processes. Each funding and eligibility decision must be verified against a current official call or contract, and each submission/offer must have applicant-specific proof. Historic outcomes can improve interview preparation and narrative structure but do not calibrate 2026–2027 admission odds.

## 6. Verification limitations

The linked source audits inspect code paths, configs, models and available tests without executing third-party runtime. No personal PDF/CV, confidential letter, uploaded .env, real OTP, email address, or API credential was extracted or copied. Security findings are design-level code observations, not evidence that any live installation is exposed or compromised.
