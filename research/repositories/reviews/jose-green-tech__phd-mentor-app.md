# Jose-GREEN-TECH/Phd-mentor-app — deep static repository review

**Reviewed:** 2026-11-12. **Pinned upstream:** [3d355d25db0275e7f6b454b928a0f825956d7d82](https://github.com/Jose-GREEN-TECH/Phd-mentor-app/commit/3d355d25db0275e7f6b454b928a0f825956d7d82).  
**State:** DEEP_REVIEW_DOCUMENTED — source and trust-boundary review; runtime and deployment NOT_TESTED.  
**Verdict:** adapt document/workflow staging only; reject unauthenticated model proxy and unsafe HTML insertion.

## 1. Intended system

A client-side scholarship and PhD-application mentor with checklist, local scholarship tracker, CV/SOP/research-proposal/document review, AI chat, and deadline calendar export. Twelve tracked files split the UI into JS modules and a Vercel-style `api/generate.js` Gemini proxy. This is not a scholarship feed sourced from official university listings.

## 2. Dataflow and architecture

The browser uses `localStorage` to persist applicant profile, scholarship rows, document reviews, checklist and chat. `scripts/gemini.js` constructs model prompts and posts `model` plus arbitrary `body` to `/api/generate`; that endpoint appends a private server-side Gemini API key and forwards request content to Google. The frontend reads PDFs and DOCX documents client-side before sending extracted text to the model for review. A local tracker stores status and generates downloadable ICS reminders.

## 3. API authorization and financial exposure

The POST-only proxy checks only that `model` and `body` are present. No authentication, caller authorization, payload size limit, accepted-model allowlist, per-user quota, timeout, structured body validation, or cost budget is enforced in the inspected serverless handler. A publicly deployed endpoint may therefore let arbitrary callers spend the operator's Gemini quota and submit arbitrary prompts/models. The API key is held server-side, but protecting the key alone does **not** protect the paid API capability.

## 4. Browser HTML injection

The chat renderer transforms untrusted user/model text into HTML using regex replacements **without HTML escaping**, then inserts the generated string via `element.innerHTML`. Review results (`summary`, `keywords_missing`, strengths, weaknesses and suggestions) and manually editable scholarship names, URLs and fields are likewise interpolated into HTML template strings and assigned to `innerHTML`. A malicious source/model response or applicant-entered HTML can therefore create a DOM injection/XSS surface. Replace with safe DOM text nodes or a sanitizing Markdown renderer, URL scheme validation and narrowly scoped attributes.

## 5. Factual accuracy and cycles

The application seeds a set of named scholarships with hardcoded **2024–2025 deadlines**, generalized “Full Funding” descriptions, percentage field matches, and country/program eligibility suggestions. These are illustrative seed rows rather than current-cycle official notices. Some seeds mix Master's-only and doctoral grants, as well as distinct scholarship/fellowship pathways. No source snapshot, verification timestamp, applicant-country scope, current eligibility decision or funder-level evidence is present.

The AI document score (0–100) and letter grades come from a free-form LLM prompt, **not an established rubric calibrated against admissions outcomes**. No evidence demonstrates admission probability, current scholarship availability or referee acceptance.

## 6. Applicant privacy and data boundaries

The document reviewer accepts CVs, SOPs, recommendation letters and transcripts and transmits extracted text and profile details to an external model. The repository does not establish a consent prompt, sensitive-content redaction, data-retention contract or field-level minimization before transmitting this private information. `localStorage` is not encrypted and is vulnerable to script-origin compromise. Recommendation letters are especially sensitive third-party documents; they should not be uploaded by applicants without appropriate authorization.

The .ics export uses UTC 09:00–10:00 without a program-specific timezone or source-defined deadline cutoff, and interpolates manually entered title/URL without ICS escaping; a reminder is not authoritative deadline verification.

## 7. Validation and maintenance gaps

Inspected proxy, Gemini integration, app state, tracker, document review and chat renderer. No test files or CI workflow appeared in the complete 12-file tree. Client-visible model IDs and tuition/funding assertions may be stale; model availability and API billing were not tested. No app deployment, browser exploit, Gemini call, OCR, PDF extraction or user data transmission was performed.

Pinned evidence: [API proxy](https://github.com/Jose-GREEN-TECH/Phd-mentor-app/blob/3d355d25db0275e7f6b454b928a0f825956d7d82/api/generate.js), [chat renderer](https://github.com/Jose-GREEN-TECH/Phd-mentor-app/blob/3d355d25db0275e7f6b454b928a0f825956d7d82/scripts/chat.js), [document renderer](https://github.com/Jose-GREEN-TECH/Phd-mentor-app/blob/3d355d25db0275e7f6b454b928a0f825956d7d82/scripts/documents.js), [tracker](https://github.com/Jose-GREEN-TECH/Phd-mentor-app/blob/3d355d25db0275e7f6b454b928a0f825956d7d82/scripts/tracker.js), [model prompts](https://github.com/Jose-GREEN-TECH/Phd-mentor-app/blob/3d355d25db0275e7f6b454b928a0f825956d7d82/scripts/gemini.js), [state and seeded awards](https://github.com/Jose-GREEN-TECH/Phd-mentor-app/blob/3d355d25db0275e7f6b454b928a0f825956d7d82/scripts/app.js).

## 8. Transfer to PhD Atlas

Preserve the conceptual separation between applicant profile, document preparation, application status and reminder events. Do not reuse the current API proxy or HTML rendering. Require authenticated and metered model requests, server-validated model/body schemas, bounded prompt sizes, source-to-claim provenance and a human review requirement. Put private applicant files under protected storage, never public pages; use consent and data minimization before external model calls. Store deadline timezone, originating official URL, cycle and evidence state separately from calendar events.
