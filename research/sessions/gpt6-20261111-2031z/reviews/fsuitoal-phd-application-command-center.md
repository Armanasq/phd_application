# Repository review: fsuitoal-code/phd-application-command-center

## Review disposition
- Review depth: deep static implementation review.
- Upstream snapshot: main at ea240bc0189038881306ccd34a5b9cbf525aaebd.
- Tracked files: 154; backend test files: 25; Alembic migration files: 27.
- Last pushed: 2026-11-02.
- GitHub metadata: no open issues, no pull requests, no declared license.
- Runtime: not executed; no local checkout or outbound GitHub access was available.

## Product and architecture
This is a local-first, single-user PhD application workspace. The frontend is React, TypeScript, and Vite. The backend is FastAPI with Pydantic models, SQLite persistence, Alembic migrations, and the Claude Agent SDK.

The main entities and workflows are:
- programs and universities;
- application status and tasks;
- deadlines and requirements;
- faculty profiles and faculty research dossiers;
- source-backed program notes;
- local application documents;
- notes and research history.

The frontend exposes a dashboard, program list, and program detail tabs for overview, faculty, documents, and notes. A user can add a program manually or start a Claude research pass.

## Research execution and data flow
The program research path is intentionally constrained:
1. The user supplies a program and an official URL.
2. The backend derives a domain boundary from that URL.
3. Claude Agent SDK is allowed to use WebFetch only within the derived domain; WebSearch and unrelated tools are denied.
4. The model returns structured program facts, deadlines, requirements, and source-backed notes.
5. The application merges researched facts with existing records and preserves human confirmation as a separate step.

The faculty-dossier path is broader. It uses WebSearch and WebFetch, rejects a deny-list of search-engine hosts, and synthesizes research activity and advising context into a dossier. This is useful for discovery but does not have the same strict official-domain boundary as the program-research path.

## Important implementation findings

### 1. Domain-boundary calculation is not public-suffix aware
The registrable-domain helper approximates the boundary by taking the last two hostname labels. For a host such as ox.ac.uk, this reduces the boundary to ac.uk. The resulting allowlist can treat unrelated academic hosts under that suffix as the same institution domain.

This is a real trust-boundary defect, not merely a formatting issue. Use a Public Suffix List-aware library and compare normalized registrable domains. Also reject IP literals, localhost, private and link-local address ranges, unsupported schemes, and redirect destinations outside the allowlist.

### 2. Source quotations are not mechanically verified
Research-note schemas require a source URL and quotation, and the UI can create a text-fragment link. However, the application does not compare the generated quotation against the fetched source content before storing it. The prompt requests exact quotations, but prompt compliance is not verification.

Persist the retrieved source text or a content hash and verify quote containment before promoting a note to evidence-backed status.

### 3. Manual facts are labelled as program-confirmed
The create schemas default manually entered deadlines, requirements, and notes to CONFIRMED_BY_PROGRAM with needs_human_verification=false. The implementation comments treat user-entered facts as already confirmed, but the field name communicates external confirmation by the university.

User confirmation and official-source confirmation are different states. A user may enter an unverified date from an aggregator or an email. The data model should distinguish USER_ENTERED, OFFICIAL_SOURCE, MODEL_RESEARCHED, and UNKNOWN, with verification status independent of source type.

### 4. Migration backfill overstates provenance
The deadline-source migration backfills legacy records as CONFIRMED_BY_PROGRAM and marks them as not requiring human verification. The previous records do not necessarily contain evidence proving that the university confirmed them. This migration preserves UI convenience but creates a provenance claim unsupported by stored evidence.

Legacy records should be labelled LEGACY_UNVERIFIED or require review unless an original official source is available.

### 5. Deadline and requirement evidence is less complete than note evidence
Program notes can carry source URL and quote fields. Deadline and requirement models primarily retain source classification, notes, and verification state; they do not provide equivalent field-level URL/quote provenance. As a result, a researched date or requirement can be separated from the page and exact passage that supported it.

Attach evidence records to individual facts rather than relying on a general program note.

### 6. Faculty research has a broader trust boundary
The faculty-dossier workflow uses a deny-list of search-engine hosts rather than an allowlist of official university, lab, publication, or researcher sources. The model prompt requests credible sources, but the application does not enforce source authority or verify every quote against retrieved content.

Use explicit source tiers and preserve a structured evidence list for each faculty claim.

### 7. Deployment boundary is local-only
The project is designed for a private single-user workspace. The backend does not provide a multi-user authentication and authorization model. The frontend's in-memory research store also means an in-flight pass can be lost on a full browser reload. These are acceptable constraints for a local prototype, but the application should not be exposed publicly without authentication, authorization, CSRF protections, rate limits, and hardened network fetching.

## What is implemented versus what remains unproven
The repository contains a substantial implementation: API routes, typed models, migrations, frontend pages, local document handling, and tests. The existence of a feature in the UI is not evidence that its research output is correct. No upstream runtime execution was possible in this session, so no claim is made that the application starts or that tests pass.

## Reusable design patterns
- Local-first storage with an explicit application-data directory.
- Typed entities and schema validation.
- Separate program research and faculty research workflows.
- Human confirmation as an explicit workflow step.
- Source notes with URLs and text-fragment links.
- Alembic migrations and focused tests.
- Separate program, faculty, document, and note views.

## Recommended corrections
1. Replace the two-label domain approximation with PSL-aware parsing and redirect/IP validation.
2. Separate source type from verification state; never default user-entered data to official confirmation.
3. Add field-level evidence records for deadlines, requirements, funding, and eligibility.
4. Verify quotations against fetched page content and store retrieval timestamps/content hashes.
5. Add explicit source tiers to faculty dossiers.
6. Preserve research-run provenance, including the actual model, prompt version, tool calls, source URLs, and evidence.
7. Keep the application local-only until a real auth and security boundary exists.

## Evidence and coverage
- Repository: https://github.com/fsuitoal-code/phd-application-command-center/tree/ea240bc0189038881306ccd34a5b9cbf525aaebd
- Backend main/config/path/migration modules, program/faculty routes, models, schemas, research agents, frontend route and program-detail pages, test files, and migration history inspected.
- No issues or pull requests were present.
- No license declared.
- Static review completed; runtime and test execution blocked by the unavailable local checkout.