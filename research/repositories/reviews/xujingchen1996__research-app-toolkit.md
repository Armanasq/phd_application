# xujingchen1996/research-app-toolkit — source-pinned multi-host workflow audit

**Reviewed:** 2026-11-12  
**Repository:** https://github.com/xujingchen1996/research-app-toolkit  
**Repository ID:** 1204458572  
**Pinned revision:** [eb42c516a960b0e9e44b6c39e27184b6088d5d27](https://github.com/xujingchen1996/research-app-toolkit/commit/eb42c516a960b0e9e44b6c39e27184b6088d5d27)  
**Review state:** DEEP_REVIEW_DOCUMENTED — risk-focused complete core-source inspection; upstream runtime and tests NOT_TESTED.  
**Verdict:** Adapt evidence-aware prompt and local workspace patterns; verify host permissions and claims before operational reuse.

## 1. Research scope and intended users

Research Application Toolkit v0.3.0 is an npm-distributed set of PhD/MRes/MPhil application workflows. Its nine named skills cover CV analysis, CV polishing, supervisor matching, school selection, cold-email drafting, application documents, research-gap analysis, interview preparation, and interview presentation preparation. It is not a live vacancy database, admissions-prediction model, evidence-verified supervisor roster, or an automated outbound contact service. Current recruitment, funding, eligibility and application dates still require separate official-source verification.

The latest inspected revision was published 2026-10-14. The repository has an MIT LICENSE, 76 tracked files, 52 directories, Node.js >=20 requirement, and an optional DeepSeek Harness peer dependency. No third-party package installation or outbound request was made in this review.

## 2. Implementation and host integration

Three separate host surfaces are implemented:

- **Claude Code:** slash commands, helper agent, nine skills, and a local profile template; marketplace installer under ~/.claude.
- **Codex:** distinct bilingual skill files, codex/memory.md template, plugin manifest, marketplace/config registration, and an installer-managed local cache symlink.
- **DeepSeek Harness (DSH):** preset configuration, nine adapted skills, four UI pages (profile, school/supervisor, documents/outreach, interview), a local workbench backed by .ra/memory.md and .ra/workbench.json, a model tool ra_workbench, and a local HTTP state endpoint.

The Node CLI ratk install selects detected hosts or explicit --claude/--codex/--dsh/--all flags. The DSH installation copies a bundle; activation still requires the host's plugin manager. This is host integration and workflow scaffolding, not a hosted admissions SaaS.

Source: [npm manifest](https://github.com/xujingchen1996/research-app-toolkit/blob/eb42c516a960b0e9e44b6c39e27184b6088d5d27/package.json), [CLI](https://github.com/xujingchen1996/research-app-toolkit/blob/eb42c516a960b0e9e44b6c39e27184b6088d5d27/bin/ratk.js), [installer](https://github.com/xujingchen1996/research-app-toolkit/blob/eb42c516a960b0e9e44b6c39e27184b6088d5d27/lib/installer.js).

## 3. Data flow and persistence contract

DSH's store implements a four-kind model: schools, professors, documents, interviews. The model-tool and UI routes both call operate(), which reads workspace-local Markdown and JSON. Each update requires the SHA-256 revision of the previous content, and a per-workspace Promise queue serializes concurrent writes inside the process. It preserves unknown record fields across updates. The read operation does not create files, and writes require an authorized non-read-only sandbox policy.

The workbench validates record title, date *format* (YYYY-MM-DD), bounded text lengths, ID shape, and source URL prefix; it checks workspace paths and refuses symlinks at .ra and file boundaries. Record content and profile are mutable locally, not externally verified. A directory's permission boundary is delegated to the host; the toolkit does not implement independent cloud identity or cross-device synchronization.

Source: [store](https://github.com/xujingchen1996/research-app-toolkit/blob/eb42c516a960b0e9e44b6c39e27184b6088d5d27/dsh/lib/store.mjs), [UI/model adapter](https://github.com/xujingchen1996/research-app-toolkit/blob/eb42c516a960b0e9e44b6c39e27184b6088d5d27/dsh/lib/index.mjs).

## 4. Research methods and evidence boundaries

The Codex professor-match skill instructs source searches of official faculty/lab pages and recent publications, checking for recruiting signals and explicitly marking public recruitment unconfirmed when absent. The gap-analysis skill separates methodological, applied, theoretical and engineering gaps; it warns against recycling authors' own future-work statements as novel proposals. The cold-email skill drafts personalized messages grounded in verified supervisor context and explicitly avoids fabricating papers read or achievements.

These are **instructional process contracts**, not proofs that an underlying LLM will implement every guard correctly. No calibration dataset, real application outcome evaluation, professor-match benchmark, or independent source-evidence registry is shipped in the inspected core.

Source: [supervisor match](https://github.com/xujingchen1996/research-app-toolkit/blob/eb42c516a960b0e9e44b6c39e27184b6088d5d27/codex/skills/professor-match/SKILL.md), [research gaps](https://github.com/xujingchen1996/research-app-toolkit/blob/eb42c516a960b0e9e44b6c39e27184b6088d5d27/codex/skills/gap-analysis/SKILL.md), [email drafting](https://github.com/xujingchen1996/research-app-toolkit/blob/eb42c516a960b0e9e44b6c39e27184b6088d5d27/codex/skills/cold-email/SKILL.md).

## 5. Test and maintenance evidence

The repository includes Node native test suites for installer marketplace updates, temp-home installation, DSH preinstall without its host, package resource resolution, store revisions and concurrent edits, read-only mode, symlink rejection, HTTP/model-tool data consistency, local origin rejection, and UI session lifecycle. The check script validates source syntax, formats and resource files; package.json exposes npm test and npm run check.

Tests were **inspected but not run**. Their presence supports implementation intent, not a certified pass, host compatibility, privacy certification or verified real-world recruitment results. Recent commits include the DSH integration in October 2026; issue/PR history inspected has two open promotional listing issues and one closed README-translation PR, not a comprehensive reliability record.

Source: [DSH tests](https://github.com/xujingchen1996/research-app-toolkit/blob/eb42c516a960b0e9e44b6c39e27184b6088d5d27/dsh/tests/studio.test.mjs), [installer tests](https://github.com/xujingchen1996/research-app-toolkit/blob/eb42c516a960b0e9e44b6c39e27184b6088d5d27/test/installer.test.js), [check script](https://github.com/xujingchen1996/research-app-toolkit/blob/eb42c516a960b0e9e44b6c39e27184b6088d5d27/scripts/check.mjs).

## 6. Security, privacy and failure analysis

- The DSH tool and UI are protected by host session/preset lookup and sandbox-policy checks. The local /ra-api/state HTTP GET endpoint uses a sessionId lookup; POST additionally checks the Origin header when supplied. No separate per-request bearer token is apparent in the inspected adapter. Deployment exposure and host network restrictions must be verified before assuming cross-process confidentiality.
- Symlink checks reduce traversal risk but are filesystem checks followed by a write, not a demonstrated atomic no-follow write. Cross-process optimistic concurrency also depends on host filesystem semantics; the in-memory queue only serializes writers inside one Node process.
- Source URLs are checked for an http(s) prefix, not parsed against an explicit trusted-host policy. The YYYY-MM-DD validator checks shape, not calendar validity. Such fields are working notes, not verified funding evidence.
- The installer backs up an existing target before copying, but an interrupted copy has no explicit rollback path. ensureCodexCacheLink removes an existing plugin cache path before creating a symlink; that behavior is confined to a fixed path but could discard unrelated data mistakenly stored there.
- Academic outreach remains a draft workflow. The DSH preset requires explicit authorization before sending/submitting; the inspected source does not evidence autonomous email delivery.
- Workbench files can contain sensitive CV, research profile and correspondence. They should remain private, access-controlled and excluded from public Git.

## 7. Cross-repository interconnections and transferability

This toolkit complements, rather than replaces, a structured PhD application intelligence service. Its strongest transferable patterns are separation of host-specific prompts, explicit profile preconditions, reusable local research context, source-first faculty review, revision-gated state changes, and draft-only outreach. Unlike live vacancy scrapers, it does not persist independent source snapshots or verify amounts, fee categories or recruitment decisions.

A PhD Atlas integration would pair these workflow skills with a versioned source registry, field-level claim/evidence graph, applicant-specific eligibility and an explicit authorization state machine. Do not convert profile matching scores or prompt-derived funding labels into calibrated admission probabilities.

## 8. Final decision and uninspected scope

**Decision:** DEEP_REVIEW_DOCUMENTED; adapt process and persistence patterns, do not treat generated guidance as authoritative current policy. Full recursive tree, package/host manifests, installer and CLI, DSH state and HTTP/model adapter, representative skills, tests, and commit/issue history were inspected. Not performed: npm install/test/check/pack, DSH/Claude/Codex host launches, HTTP penetration test, symlink race test, live professor search, recruitment verification, external email action, full audit of every prompt variant, or applicant outcome evaluation.
