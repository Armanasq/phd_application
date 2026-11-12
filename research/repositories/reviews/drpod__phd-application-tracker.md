# Focused static investigation — drPod/phd-application-tracker

**Date:** 2026-11-12. **Pinned source:** `9f04c013a45f1abec598deda4fe6cb5ff78346fc`. **Level:** PRELIMINARY_FOCUSED (source-path review, not execution or complete application threat-model audit). **License:** no license file or grant observed in the enumerated tree; verify before reuse.

## Purpose and implemented architecture
A Next.js/React applicant workspace for creating programs, deadlines and requirements, uploading a CV/SOP/transcript, assigning documents to programs, and maintaining per-program progress in Supabase. The [README](https://github.com/drPod/phd-application-tracker/blob/9f04c013a45f1abec598deda4fe6cb5ff78346fc/README.md) is an unmodified Next.js scaffold rather than architecture documentation; evidence was obtained from its 95-entry source tree, [program hooks](https://github.com/drPod/phd-application-tracker/blob/9f04c013a45f1abec598deda4fe6cb5ff78346fc/lib/hooks/usePrograms.ts), [document hooks](https://github.com/drPod/phd-application-tracker/blob/9f04c013a45f1abec598deda4fe6cb5ff78346fc/lib/hooks/useDocuments.ts), [Supabase storage](https://github.com/drPod/phd-application-tracker/blob/9f04c013a45f1abec598deda4fe6cb5ff78346fc/lib/supabase/storage.ts), Next [proxy](https://github.com/drPod/phd-application-tracker/blob/9f04c013a45f1abec598deda4fe6cb5ff78346fc/proxy.ts) and [browser auth tests](https://github.com/drPod/phd-application-tracker/blob/9f04c013a45f1abec598deda4fe6cb5ff78346fc/tests/auth.spec.ts).

## Concrete data flow and positive patterns
- `usePrograms()` checks Supabase `auth.getUser()`, queries by `user_id` and orders by deadline; mutation methods include both object ID and caller `user_id` constraints.
- `useDocuments()` retrieves documents by `user_id`, then fetches associated `document_programs` for each row. Document creation writes metadata and subsequently creates program mappings. React Query invalidates listing caches after mutations.
- The app uses Supabase auth and Playwright smoke tests for login/navigation. These are sensible UX patterns, but cannot substitute for server-enforced Row Level Security (RLS) and storage policy reviews.

## Code-established privacy and integrity concerns
1. [Storage upload](https://github.com/drPod/phd-application-tracker/blob/9f04c013a45f1abec598deda4fe6cb5ff78346fc/lib/supabase/storage.ts) writes applicant files into `documents` and derives a `getPublicUrl(...)`. If the bucket is public, sensitive transcripts, SOPs and CVs become accessible to anyone possessing the URL. No SQL storage policy or RLS migration was found in the reviewed tracked tree; **actual deployed bucket privacy is unknown**. Require private bucket, authenticated object ownership and short-lived signed URLs; never publish credentials or applicant uploads.
2. [Document replacement](https://github.com/drPod/phd-application-tracker/blob/9f04c013a45f1abec598deda4fe6cb5ff78346fc/lib/hooks/useDocuments.ts) tries to delete the previous object *before* uploading replacement or updating the DB row. If upload/database update fails, the original file can be lost. Reconcile after successful new object write and DB update, not before.
3. Document create: storage write, metadata insert and `document_programs` insertion are separate steps with no transaction/compensation; partial failures can orphan files or rows. Document update deletes all associations and recreates without an atomic transaction and does not check delete errors.
4. `useDeleteDocument` deletes a row but does not delete its storage object; the old content can remain after applicant removal (retention/privacy issue).
5. No tracked RLS SQL migrations were visible, so ownership enforcement by Supabase itself cannot be assessed. The client-side `eq(user_id)` is good query hygiene but not a security boundary; private document policies must be verified on the server.
6. [Playwright auth tests](https://github.com/drPod/phd-application-tracker/blob/9f04c013a45f1abec598deda4fe6cb5ff78346fc/tests/auth.spec.ts) inspect basic form visibility/navigation; they do not verify user isolation, storage privacy, atomic document mutation or file lifecycle.

## Comparison and decisions
Compared with the [local-first doctoral tracker](https://github.com/chuyaowang/nl-phd-tracker), this system provides multi-program document mapping at the cost of cloud storage and stronger privacy obligations. Compared with the in-repository SQLite admissions intelligence system, it offers a richer UI, not a verified employer funding/eligibility pipeline. **Verdict: ADAPT UX AND DATA-MODEL PATTERNS ONLY; do not reuse storage handling for sensitive applicant records.** Validate licenses, RLS, signed URLs, object ownership, cleanup, concurrency and failure-injection tests before reassessing. This focused inspection does not establish deployed behavior, security certification, current PhD opportunity quality or admissions outcomes.

## Evidence scope and next inspection
Additional code such as the settings UI, Next.js middleware/SSR, schema migration provisioning and production environment was not independently executed. Read `lib/supabase/middleware.ts`, storage bucket settings and database policies, end-to-end document upload/overwrite/delete tests and running app logs in a private fixture deployment before upgrading to a deep-verified implementation review. Do not ingest or store any personal document data.


## 1. Source objective and scope

Additional deep static audit at [`9f04c013a45f1abec598deda4fe6cb5ff78346fc`](https://github.com/drPod/phd-application-tracker/commit/9f04c013a45f1abec598deda4fe6cb5ff78346fc). Determine whether private applicant documents, institution/program state and access controls remain safe across Supabase storage, browser hooks and deletion. Source inspection only, **not** runtime security verification.

## 2. Implementation architecture

Next.js/React application: Supabase Auth session middleware, React Query program/requirement/document hooks, private-program state, storage adapter for CV/SOP/PS/writing samples, link table of assigned program IDs, per-program requirements checklist and a static Playwright UI suite. Reviewed `lib/hooks/useDocuments.ts` (269 lines), `usePrograms.ts` (179), `lib/supabase/storage.ts` (92), `middleware.ts` (71), `components/documents/DocumentsPanel.tsx` (373), `UploadDialog.tsx` (237), `lib/types.ts` (38) and `tests/auth.spec.ts` / `tests/app.spec.ts` (88/36).

## 3. Actual dataflow and custody

Program queries and mutations read `supabase.auth.getUser()` and use `.eq('user_id',user.id)`; document queries have the same owner filter. Upload paths are namespaced under `user.id/`. A saved `documents` row links storage URL and type/status, and `document_programs` stores assigned program IDs. Client-side user filters are a positive measure but are **not a substitute for deployment RLS/storage authorization rules**; none were found in the inspected tracked source or exercised against a real Supabase project.

## 4. Confirmed source-level risks

**P0 conditional privacy risk:** `lib/supabase/storage.uploadFile()` calls `getPublicUrl(data.path)` and stores the result. A publicly configured `documents` bucket would expose sensitive CV/SOP/transcripts to anyone holding the link. Whether the actual bucket is public is **unknown**; this is an insecure interface assumption, not confirmation of an exposed deployment. Require a private bucket with RLS/policies, user-scoped object paths and short-lived signed URLs.

**P1 non-atomic operations:** `useUpdateDocument` replaces `document_programs` assignments by deleting then reinserting rows; partial failure can leave assignments empty. The upload+documents insert+link associations and deletion+storage delete run across multiple independently failing calls without transaction/compensation. `DocumentsPanel` catches storage deletion failures and continues the record deletion attempt. Cross-user association writes need RLS on both `documents` and `document_programs`.

## 5. Identity, provenance and admissions authority

Program statuses (researching/applying/submitted/decision), deadlines, attached document statuses (draft/final) and university names are applicant-entered state. No source owner verifies a program's scholarship, international tuition coverage, deadline cutoff or submitted receipt. A "submitted" status is not proof of portal acceptance.

## 6. Reusable methods and cross-repo distinctions

Reuse structured program/requirements and private document attachment design; Supabase session helper, per-UID query constraints and explicit program-document edges are stronger than a global public JSON GitHub sync. Replace public URL usage with signed short-lived access and add receipt-backed applicant activity, versioned source evidence and transactional association updates.

## 7. Tests and observed operations

`tests/app.spec.ts` asserts app/program/documents pages redirect unauthenticated browsers to sign-in; `tests/auth.spec.ts` covers form validation/navigation. They do **not** demonstrate storage bucket private visibility, authenticated cross-user RLS, safe signed URLs, file deletion atomicity or reliable application submission. No test was executed in this audit. Upstream default branch was inspected; license was not recognized in GitHub metadata.

## 8. Verdict and remaining validation

**ADAPT ONLY AFTER PRIVATE STORAGE AND TRANSACTION REPAIRS**. Verify bucket policies and RLS through controlled dummy accounts, test cross-user relation writes, expiry of signed file links, failed storage operations, backup/restore and audit logs. Independently check official program eligibility, funding and deadlines. No applicant document, personal contact or university live application was accessed.

Pinned source links: [documents hook](https://github.com/drPod/phd-application-tracker/blob/9f04c013a45f1abec598deda4fe6cb5ff78346fc/lib/hooks/useDocuments.ts), [storage](https://github.com/drPod/phd-application-tracker/blob/9f04c013a45f1abec598deda4fe6cb5ff78346fc/lib/supabase/storage.ts), [program hook](https://github.com/drPod/phd-application-tracker/blob/9f04c013a45f1abec598deda4fe6cb5ff78346fc/lib/hooks/usePrograms.ts), [middleware](https://github.com/drPod/phd-application-tracker/blob/9f04c013a45f1abec598deda4fe6cb5ff78346fc/lib/supabase/middleware.ts), [UI tests](https://github.com/drPod/phd-application-tracker/blob/9f04c013a45f1abec598deda4fe6cb5ff78346fc/tests/app.spec.ts).
