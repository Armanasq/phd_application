# ibrar-saeed-dev/scholarship_scraper — deep static code audit

**Source:** https://github.com/ibrar-saeed-dev/scholarship_scraper; **Git tree SHA:** `16d5ef8c63b8464e07aa03e80a5f7f441d79a01e` ([snapshot inventory](https://api.github.com/repos/ibrar-saeed-dev/scholarship_scraper/git/trees/16d5ef8c63b8464e07aa03e80a5f7f441d79a01e)); inspected 2026-11-12. **Execution:** NOT_TESTED. **Official eligibility/funding:** NOT_INDEPENDENTLY_VERIFIED.

## 1. Objective

Inspect implementation, source authority, candidate dataflow and privacy constraints.

## 2. System purpose and architecture

Expo UI reads Supabase scholarships where is_active=true, filters degree, country and university; Deno scraper defines official-source adapters, but some DAAD/Fulbright/Schwarzman handlers explicitly return empty arrays, while other award fields are static assertions. It marks old deadlines inactive without checking issuer changes.

## 3. Modules and source provenance

[src/app/index.tsx](https://github.com/ibrar-saeed-dev/scholarship_scraper/blob/main/src/app/index.tsx), [supabase/functions/scraper/index.ts](https://github.com/ibrar-saeed-dev/scholarship_scraper/blob/main/supabase/functions/scraper/index.ts). Git tree pinned above; source paths are browser links to tracked files.

## 4. Confirmed risks

**STATIC_FUNDING_ASSERTIONS_AND_EMPTY_PROVIDER_ADAPTERS (P1).** Expo UI reads Supabase scholarships where is_active=true, filters degree, country and university; Deno scraper defines official-source adapters, but some DAAD/Fulbright/Schwarzman handlers explicitly return empty arrays, while other award fields are static assertions. It marks old deadlines inactive without checking issuer changes. This is code-level evidence, not an executed exploit or a claim that any service is currently deployed.

## 5. Evidence quality and funding controls

No issuer-validated applicant eligibility, current funding package, source timestamp, exact deadline timezone or actual submission receipt was independently verified. Do not promote scraped defaults or checkbox state into formal policy evidence.

## 6. Cross-repository transfer

Source registry, mobile filters and Supabase CRUD are reusable only with field-level authority, current intake and nationality verification. Separate source snapshots, extracted claims, program identity, applicant documents and auditable state transitions.

## 7. Disposition

**P1: architecture only after security, source-validation and correctness repairs.** Do not treat an open flag as proof of funded intake.

## 8. Tests and remaining limitations

No builds, browser/API calls, real applicant data, issuer verification, security exploit or model evaluation executed. Run fixtures for source changes, empty responses, permission checks, bad deadlines, conflict merges and the identified issue.
