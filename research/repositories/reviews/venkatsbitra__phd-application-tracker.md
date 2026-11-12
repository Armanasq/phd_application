# Deep static audit — VenkatSBitra/phd-application-tracker

**Pinned Git tree:** `80545b811e3c6533595f4a57ab584cb8b7075b0f` ([immutable inventory](https://api.github.com/repos/VenkatSBitra/phd-application-tracker/git/trees/80545b811e3c6533595f4a57ab584cb8b7075b0f)). **Inspected:** 2026-11-12. **Runtime:** NOT_TESTED. **Funding/eligibility:** NOT_VERIFIED.

## 1. Objective and relevance

Assess source implementation and reusability for PhD discovery/application, without claiming actual admission or current offers.

## 2. Source architecture and execution

Next.js Firebase client references global universities, professors and applications collections without user predicates; React AuthContext gates UI against NEXT_PUBLIC_ALLOWED_EMAIL. Real Firestore rules not inspected, so public access is NOT established. Historical professor email state transitions and contact counts are user claims.

## 3. Algorithms and data contracts

Source modules inspected: [src/services/firestore.ts](https://github.com/VenkatSBitra/phd-application-tracker/blob/main/src/services/firestore.ts), [src/contexts/AuthContext.tsx](https://github.com/VenkatSBitra/phd-application-tracker/blob/main/src/contexts/AuthContext.tsx), [src/lib/firebase.ts](https://github.com/VenkatSBitra/phd-application-tracker/blob/main/src/lib/firebase.ts). The tree was inventoried, but external endpoints and binary resources were not exercised. Source metadata/links or user-defined status fields do not independently prove eligibility, scholarship funding or submission.

## 4. Confirmed code-level risks

**P0: CLIENT_SIDE_EMAIL_AUTH_AND_UNSCOPED_FIRESTORE.** Next.js Firebase client references global universities, professors and applications collections without user predicates; React AuthContext gates UI against NEXT_PUBLIC_ALLOWED_EMAIL. Real Firestore rules not inspected, so public access is NOT established. Historical professor email state transitions and contact counts are user claims. The finding concerns inspected code; actual live-service exposure or exploitation remains untested.

## 5. Provenance and verification limits

A future implementation must preserve original issuer URL, crawl time, exact quoted claim, intake cycle, deadline timezone, funding coverage and eligibility status. Treat missing confirmation as UNKNOWN, not OPEN or FULLY_FUNDED.

## 6. Interconnections and transferable methods

Separate data ingestion, candidate matching, human review and applicant private state. Comparable reviewed systems show that crawled opportunities and editable application status fields are not authoritative source facts. Any reusable architecture requires evidence and security hardening.

## 7. Recommendation and priority

**P0 — do not adopt unmodified.** Address CLIENT_SIDE_EMAIL_AUTH_AND_UNSCOPED_FIRESTORE, restrict external network access and add source/identity validation before migration into the PhD research workflow.

## 8. Required tests and closure conditions

Not run: source snapshot comparison, live provider checks, runtime tests, auth/permission tests, network attack reproduction, multiuser isolation and deadline verification. Add unit tests for the specific defect, incomplete source responses, false openings, concurrent updates, exact IDs and authorization.
