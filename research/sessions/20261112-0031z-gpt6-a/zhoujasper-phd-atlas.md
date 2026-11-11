# Deep repository investigation — zhoujasper/phd-atlas

**Review date:** 2026-11-12  
**Upstream:** https://github.com/zhoujasper/phd-atlas  
**Pinned public commit:** [`8f4318eda901020b61d91abfc82411943200c70f`](https://github.com/zhoujasper/phd-atlas/commit/8f4318eda901020b61d91abfc82411943200c70f)  
**Source revision marker:** `347ea3d80056`  
**Review state:** DEEP_STATIC_REVIEW_COMPLETE; RUNTIME_VALIDATION_NOT_PERFORMED  
**Applicability:** high for application lifecycle, source-evidence, secure agent integration, local-first persistence, and concurrency architecture.

> The commit SHA above is the public main commit reported by GitHub on 2026-10-13. Its Git tree SHA is `47be03f3fb1ca14dfc95dc2cc6a252ac964c9f96`, distinct from its commit SHA. This public repository is a generated public edition, not the full private development source.

## 1. Scope and evidence boundary

The default branch contains 1,961 recursive tree entries. The public product is personal-only; the README explicitly excludes team collaboration from this distribution. The declared stack is React 19, TypeScript 6, Vite 8, Express 5, Zod, SQLite, optional MySQL/MariaDB/PostgreSQL/SQL Server adapters, Vitest, Testing Library, Playwright, and Electron.

Inspected source areas include:
- README, installation, deployment, contribution, changelog, release notes, TODO, license, package scripts, CI/release workflows.
- Local SQLite storage schema, external database adapters, write/revision paths, encryption envelope, and storage tests.
- Application schemas, mutation acknowledgements, delta validation, offline cache/replay, and tests.
- Codex authorization, Express middleware integration, permissions references, API reference, skill, and authorization tests.
- Discover research orchestration, source registry, school adapters, live health, source crawler, outbound network policy, source grounding, quality gate, OpenAlex/ROR/Crossref/Europe PMC evidence collection, checkpoints, and tests.
- Electron main/preload/window policy/runtime launcher and integrity checks.

Runtime execution was not possible in this environment: a local Git remote lookup failed at DNS resolution. I did not run third-party code or claim local test execution. GitHub Actions provides a published CI result for this exact revision, described below.

## 2. Product and intended workflow

PhD Atlas is a self-hosted workspace for the lifecycle of a doctoral application:
1. Discover and compare programs and principal investigators.
2. Convert a discovery result into an application record.
3. Maintain a dossier of supervisor, research direction, funding, deadlines, tasks, and required documents.
4. Track correspondence and meetings.
5. Reuse profile materials and manage file versions.
6. Track submission state, reminders, calendar events, backups, exports, and audit events.
7. Optionally expose account-scoped natural-language operations through Codex/Claude integrations.

The product separates the personal application workflow from its discovery and agent capabilities. This is important: an LLM discovery result is not itself an application, funding commitment, or submission.

## 3. Persistence and data model

### 3.1 Local SQLite

The default local operational store is SQLite. The schema contains separate domain tables for users, applications, profile assets, mail/correspondence, notifications, sessions, credentials, quotas, backups, audit records, and related entities. Application and profile content use structured JSON payload columns alongside indexed identity, owner, status, and revision fields.

The application model is validated with Zod contracts. Mutation handling separates user-authored content from server-authoritative fields and computes canonical hashes for each.

### 3.2 External SQL adapters

MySQL/MariaDB, PostgreSQL, and SQL Server support is implemented through a different persistence abstraction than a conventional normalized multi-database ORM.

The external adapters use a single state row (ID 1) containing:
- a serialized SQLite workspace snapshot in a BLOB/binary payload;
- a monotonically increasing revision;
- update metadata.

Therefore, selecting PostgreSQL or MySQL does not make each domain entity a native relational table in that external database. The external DB is a durable snapshot backend for the SQLite workspace.

**Trade-off:** this simplifies portability and allows the same SQLite domain model to operate over several external database engines. However, each durable mutation can require serialization and persistence of the whole workspace snapshot. Cost and contention grow with workspace size; the single external state row also creates a global synchronization point across users. It is not the architecture I would choose for a high-write, horizontally scaled multi-tenant platform.

### 3.3 Concurrency and write acknowledgement

The inspected write path includes:
- tenant-scoped write lanes;
- SQLite `BEGIN IMMEDIATE` transactions;
- expected tenant revision checks;
- stale-baseline detection;
- server-authority and user-editable content hashes;
- conditional external revision writes;
- transactional quota reservation;
- durable external synchronization before ordinary mutation acknowledgement.

PostgreSQL uses revision-conditional `ON CONFLICT` updates; MySQL uses transactional conditional upsert/locking; SQL Server uses transactional locking with `UPDLOCK` and `HOLDLOCK`. An older revision cannot silently replace a newer state, and equal-revision/different-payload writes are treated as conflicts.

This is a strong pattern for the admissions workspace: acknowledge a mutation only after the durable write succeeds, and make concurrency conflicts explicit rather than silently applying last-write-wins.

### 3.4 Encryption

The encryption boundary must be described precisely:
- The external snapshot encoder encrypts the payload when the configured encryption-at-rest policy is enabled. The inspected code has a plaintext path when that policy is disabled.
- SQLite sealing is separately configurable.
- The durable envelope supports authenticated encryption (AES-256-GCM and ChaCha20-Poly1305) with integrity/tamper detection.
- The discovery checkpoint writer uses the general `encryptPayload` function; unlike the optional external snapshot setting, this path writes encrypted checkpoint payloads.
- The product documentation describes separate encryption handling for backups and vault assets.

Do not describe all external database snapshots as unconditionally encrypted. The effective encryption-at-rest policy is a deployment decision that must be checked.

## 4. Agent authorization and route enforcement

The Codex integration is more than a bearer-token wrapper.

Inspected implementation:
- 256-bit random token material is generated for the authorization.
- Only a hash of the token is persisted.
- Authorizations are bound to an account and a versioned scope set.
- The device flow requires a user-approved authorization exchange.
- Scope definitions are finite and explicit.
- Authorizations have bounded lifetime (up to 365 days) and idle expiry (180 days).
- Route policy distinguishes read, write, discovery, correspondence, profile, and settings capabilities.
- Unknown or sensitive route families are denied rather than automatically inheriting broad access.
- Administrative, authentication, bootstrap, impersonation, and unavailable Team routes are excluded from the personal Codex capability surface.
- Scope-version changes require reauthorization.

The Express integration in `server/index.js` wires token verification and authorization policy into the API middleware path before ordinary route handling. This is stronger evidence than the standalone permission documentation.

The tests cover scope classification, authorization state, route policy, expiry, and account boundaries. Nevertheless, source inspection cannot prove that future routes will always be added to the route policy correctly; route inventory and default-deny regression tests should remain mandatory.

## 5. Discover research pipeline

### 5.1 Orchestration

`server/discover-research.js` implements a multi-stage research pipeline rather than a single web-search prompt:

1. Build an applicant research profile and normalized target criteria.
2. Plan research terms and query strategy.
3. Select curated school sources and discover additional institutions.
4. Crawl official institution pages.
5. Hydrate relevant official links and program evidence.
6. Build program leads and principal-investigator candidates.
7. Collect scholarly metadata for candidate researchers.
8. Run program extraction, advisor extraction, and separate verification-agent passes.
9. Ground the returned claims against the fetched evidence index.
10. Apply quality and coverage checks.
11. Publish verified results incrementally and persist checkpointed progress.

The agent context minimizes profile data by excluding applicant name, pronouns, signatures, and writing-style preferences. It retains relevant research interests and eligibility inputs such as citizenship/region when needed for funding analysis. This is a useful minimization pattern, but citizenship and location remain sensitive inputs that should be explicitly disclosed to users when sent to an external model provider.

### 5.2 Bounded source coverage

The source registry contains **145 curated school entries** across:
- US: 46
- UK: 22
- EU: 36
- Canada: 11
- Singapore: 4
- China: 10
- Hong Kong: 4
- Australia: 12

The code defines bounded limits including:
- up to 192 dynamic institution sources;
- up to 640 school-source crawls;
- up to 1,920 hydrated links;
- up to 2,000 program leads;
- up to 500 researcher candidates;
- up to 8 scholarly works per advisor and 20 recent works per researcher.

School adapter validation requires four typed seed kinds (faculty, departments, research, doctoral), separately from the school's official root URL. The adapters are organized in ten source batches. This is more systematic than a flat university URL list.

**Geographic gap:** the pinned curated registry contains no entries for New Zealand, Norway, Luxembourg, or Ireland. Switzerland *is* represented by ETH Zurich and EPFL. Missing countries may be discovered dynamically through broader OpenAlex/ROR discovery, but they lack curated first-class seed coverage. New Zealand is mapped to OTHER rather than a dedicated region. This makes coverage dependent on dynamic discovery and region selection/caps.

### 5.3 External research sources

Institution discovery uses OpenAlex and ROR. Scholarly evidence uses OpenAlex and Crossref, with Europe PMC added for life-science/medical disciplines. Researcher matching uses institution affiliation, domain, ORCID where available, and name/affiliation similarity.

These are useful discovery signals, not proof that a person is currently faculty, eligible to supervise, or recruiting. Without ORCID, some matching relies on normalized names and affiliation similarity, which can merge homonyms or miss name variants. Final PI identity still requires an official profile.

### 5.4 Crawler security

The official-source crawler has strong network controls:
- HTTPS-only target policy;
- allowed-host checks;
- DNS resolution and public-address validation;
- pinned connection to the validated address;
- redirect validation rather than unrestricted automatic following;
- robots.txt handling, with fail-closed behavior when policy cannot be established (except defined not-found responses);
- bounded page/link/request processing;
- prompt-injection suspicion checks and untrusted-page treatment.

External vacancy aggregators are treated as lead generators, not authoritative evidence for program funding, deadlines, or supervisor recruitment. This separation should be preserved.

### 5.5 Evidence grounding and limitations

Program facts are grounded against pages fetched in the current research run and associated with the matching official institution. Prompt-injection-suspected pages are excluded from claim support. This materially reduces cross-university contamination and unsupported LLM output.

However, the final grounding checks are not full semantic entailment:
- deadline checks rely substantially on date-string presence/normalization;
- amount checks can rely on numeric/text presence in page content;
- recruitment checks use lexical evidence patterns;
- the inspected logic does not establish a complete temporal-validity check for every deadline or recruiting statement.

A value can appear on an official page but refer to another program, year, currency, or fee category. A currently fetched page can still contain an expired deadline. The verifier is a separate LLM role/pass, but not independent corroboration if it uses the same model/provider and the same source pool.

The quality gate distinguishes hard integrity failures from coverage warnings. `quality.passed` can be true while `coveragePassed` is false; partial results may be retained with warnings. This is preferable to fabricating completeness, but the UI and downstream consumer must not interpret a passing integrity gate as exhaustive global coverage.

The pipeline's `evidence-exhaustive` completion definition is scoped to the supplied evidence batch. It is not proof of global institution or vacancy exhaustiveness.

### 5.6 Checkpointing and worker admission

The research checkpoint implementation uses:
- encrypted payloads;
- atomic temporary-file/rename writes;
- a 72-hour TTL;
- a 32 MB payload limit;
- 0700 directory / 0600 file permissions;
- bounded memory admission and recovery from previous checkpoint versions.

Worker admission reserves memory and rejects/defer jobs when resource limits are exceeded. These are useful production reliability patterns for long-running research tasks.

### 5.7 Live adapter validation

Static adapter validation checks schema, required source kinds, host structure, and date formatting. The live health runner is an optional mode; the normal CI tree gate invokes the structural verifier without the `--live` flag. The static gate therefore does not prove that every university page is currently reachable or still matches its selector.

The live health checker uses page content/path keyword matching to validate declared source kinds. That is useful as a health signal but weaker than a semantic check of page function. A `verifiedAt` date is not, by itself, evidence that the adapter was recently revalidated.

## 6. Offline mode and privacy

Offline support stores personal application snapshots and an edit queue in browser local storage. It signs cached content with HMAC-SHA256, uses a bounded offline lease (up to 72 hours), filters out server-authoritative fields, and revalidates ownership/scope when queued edits are replayed. Conflict handling preserves a recoverable base and records divergent edits rather than blindly overwriting all server state.

**Important limitation:** this is integrity protection, not confidentiality protection. The offline snapshot and queue are not encrypted by the inspected local-storage path, and the HMAC key is also held in local storage. This can detect accidental or unsophisticated modification, but it does not protect personal application data from same-origin script execution, browser-profile compromise, or a person with access to the local browser profile. Do not treat HMAC as encryption.

The server replay path is materially stronger: it rechecks the authenticated owner and mutation scope and restores server-authoritative fields before applying queued edits.

## 7. Desktop and deployment architecture

The current main branch's Electron implementation uses:
- `contextIsolation: true`;
- `nodeIntegration: false`;
- sandboxed renderer;
- restrictive session permission handling;
- navigation allowlists;
- local runtime bound to loopback;
- a preload bridge with a narrow exposed API;
- a startup integrity manifest for selected critical assets.

The README states that desktop packages are unsigned; published SHA-256 checksums are the available distribution integrity check. The integrity manifest is useful against accidental modifications but is not a substitute for a signed release.

The public branch is personal-only. The old `desktop-macos-app` branch is not an active integration candidate: it is one commit ahead and seven behind main, has no PR, and its unique commit sets a development environment in the packaged desktop launcher. Main contains a more developed hardened desktop implementation. Do not merge the old branch without a fresh diff and security review.

## 8. Development history, issues, releases, and validation

- Main commit: `8f4318eda901020b61d91abfc82411943200c70f`, 2026-10-13 21:33 UTC.
- Public source revision marker: `347ea3d80056`.
- Latest release returned: `v0.1.6`, published 2026-10-13.
- Branches: `main`, `desktop-macos-app`.
- Pull requests: none returned.
- One issue (#2, email verification code delivery) is closed; no comments or closure explanation were returned, so the reason for closure is unknown.
- Recursive tree: 1,961 entries.
- Test/spec file inventory: 503 files by filename pattern.
- Latest CI run for the exact main commit: success, 2026-10-13. `verify:tree` invokes four Vitest shards and additional plugin tests, typecheck, lint, build, security and adapter-structure checks. The CI result is evidence that this gate passed at that revision, not proof of current external source freshness or runtime behavior in this audit.
- Latest release-update workflow for the same commit: success.
- Local runtime/test execution: NOT PERFORMED in this session due GitHub DNS/network failure.

## 9. Critical limitations and adoption decisions

### Adopt or adapt

1. Source-to-claim provenance and separation of official facts from lead-only sources.
2. Evidence-bound incremental publication with explicit partial-coverage status.
3. Revision-based concurrency, durable acknowledgements, and authority/user-content separation.
4. Default-deny agent scopes and account-bound authorization.
5. SSRF-resistant, robots-aware official-source crawling.
6. Encrypted durable checkpoints, bounded resource admission, and resumable long-running research.
7. Multi-provider scholarly metadata enrichment followed by official-profile verification.
8. Typed application contracts, structured workflow records, and explicit offline conflict handling.

### Do not copy unchanged

1. Single-row whole-workspace external database snapshots for a large high-write multi-tenant system.
2. Browser local-storage HMAC as a confidentiality/security control.
3. Lexical date/amount/recruitment matching as final semantic verification.
4. A separate LLM verifier as a substitute for independent sources or human review.
5. A global-coverage claim based on a bounded curated registry and dynamic discovery caps.
6. OpenAlex/Crossref author matches as proof of current faculty status or recruiting.
7. Unsigned desktop distribution as equivalent to signed software provenance.

### Application to `phd_application`

The strongest transfer is the evidence architecture, not the UI. Each repository/program/supervisor claim should have:
- a canonical source and revision/date;
- an extracted claim with field-level provenance;
- a verification method and confidence state;
- source-dependence links;
- a freshness/expiry rule;
- explicit lead-only versus official-source status;
- a separate decision record for eligibility, funding, application, and offer.

The current project already has a source ledger, claims, repository relations, and a relational SQLite migration. PhD Atlas provides implementation patterns for the application lifecycle and secure agent operations, while the current `phd_application` source policy should remain stricter than its lexical claim grounding.

## 10. Final disposition

**DEEP_STATIC_REVIEW_COMPLETE** for the major architecture and security-critical paths enumerated above; this does **not** mean all 1,961 tree entries were individually read.  
**RUNTIME_VALIDATION_NOT_PERFORMED**.  
**CURRENT LIVE SOURCE VALIDATION_NOT_PERFORMED**.  
**NOT A VERIFIED SOURCE OF CURRENT FUNDED VACANCIES**.

The project is a strong engineering reference for personal PhD application management, scoped agent access, and long-running research orchestration. It is not evidence that any discovered position is currently open, fully funded, or suitable for a particular applicant.

## 11. Pinned implementation evidence anchors

The following source references are pinned to the exact public commit; they identify the implementation supporting the principal conclusions, not runtime certification:

| Finding | Inspected source |
|---|---|
| Local SQLite schema, tenant revisions and mutation transactions | [`server/storage.js`](https://github.com/zhoujasper/phd-atlas/blob/8f4318eda901020b61d91abfc82411943200c70f/server/storage.js) |
| External snapshot persistence and revision conflict handling | [`server/databaseConnection.js`](https://github.com/zhoujasper/phd-atlas/blob/8f4318eda901020b61d91abfc82411943200c70f/server/databaseConnection.js) |
| Authenticated encryption, key derivation and payload format | [`server/crypto.js`](https://github.com/zhoujasper/phd-atlas/blob/8f4318eda901020b61d91abfc82411943200c70f/server/crypto.js) |
| Codex token/scope policy and middleware wiring | [`server/codexAuthorization.js`](https://github.com/zhoujasper/phd-atlas/blob/8f4318eda901020b61d91abfc82411943200c70f/server/codexAuthorization.js), [`server/index.js`](https://github.com/zhoujasper/phd-atlas/blob/8f4318eda901020b61d91abfc82411943200c70f/server/index.js) |
| Discovery agent/research stages and evidence partition | [`server/discover-research.js`](https://github.com/zhoujasper/phd-atlas/blob/8f4318eda901020b61d91abfc82411943200c70f/server/discover-research.js), [`server/discover-agent-plan.js`](https://github.com/zhoujasper/phd-atlas/blob/8f4318eda901020b61d91abfc82411943200c70f/server/discover-agent-plan.js) |
| Curated school registry and typed adapter acceptance | [`server/discover-source-registry.js`](https://github.com/zhoujasper/phd-atlas/blob/8f4318eda901020b61d91abfc82411943200c70f/server/discover-source-registry.js), [`server/discover-school-adapters/adapter-validator.js`](https://github.com/zhoujasper/phd-atlas/blob/8f4318eda901020b61d91abfc82411943200c70f/server/discover-school-adapters/adapter-validator.js) |
| Scholarly metadata enrichment and institution/name reconciliation | [`server/discover-scholarly-data.js`](https://github.com/zhoujasper/phd-atlas/blob/8f4318eda901020b61d91abfc82411943200c70f/server/discover-scholarly-data.js) |
| Official-source network policy, SSRF and robots controls | [`server/discover-source-crawler.js`](https://github.com/zhoujasper/phd-atlas/blob/8f4318eda901020b61d91abfc82411943200c70f/server/discover-source-crawler.js), [`server/pinnedHttpsFetch.js`](https://github.com/zhoujasper/phd-atlas/blob/8f4318eda901020b61d91abfc82411943200c70f/server/pinnedHttpsFetch.js) |
| Publication quality gate and encrypted recovery checkpoints | [`server/discover-quality.js`](https://github.com/zhoujasper/phd-atlas/blob/8f4318eda901020b61d91abfc82411943200c70f/server/discover-quality.js), [`server/discover-research-checkpoint.js`](https://github.com/zhoujasper/phd-atlas/blob/8f4318eda901020b61d91abfc82411943200c70f/server/discover-research-checkpoint.js) |
| Client offline storage and replay | [`src/offline.ts`](https://github.com/zhoujasper/phd-atlas/blob/8f4318eda901020b61d91abfc82411943200c70f/src/offline.ts), [`server/offlineReplay.js`](https://github.com/zhoujasper/phd-atlas/blob/8f4318eda901020b61d91abfc82411943200c70f/server/offlineReplay.js) |
| Desktop IPC/navigation/security | [`desktop/main.mjs`](https://github.com/zhoujasper/phd-atlas/blob/8f4318eda901020b61d91abfc82411943200c70f/desktop/main.mjs), [`desktop/windowPolicy.mjs`](https://github.com/zhoujasper/phd-atlas/blob/8f4318eda901020b61d91abfc82411943200c70f/desktop/windowPolicy.mjs) |
| Published passing CI for inspected commit | [GitHub Actions run 38471456238](https://github.com/zhoujasper/phd-atlas/actions/runs/38471456238) |

**Evidence hierarchy:** source code and pinned CI establish implementation and tested gate behavior only. They do not independently validate current advertised positions, applicant eligibility, external university page freshness, or a production deployment.
