# Session research manifest — 2cabbe82

- Session ID: `2cabbe82`
- Started: 2026-11-12 UTC
- Repository: `Armanasq/phd_application`
- Base snapshot: `c33758e2373e8726ed4d4ba58aaab736d83c43de`
- Isolated branch: `research/repository-audit-20261112-2cabbe82`
- Session status: all 10 assigned repositories have session-specific investigation artifacts; local runtime validation and canonical integration remain blocked/pending.

## Coordination and isolation

Published branches observed at initial coordination:
- `main`
- `research/repository-audit-20261112-0001-7f3c`
- `research/session-gpt6-20261112-01`
- `research/repository-audit-20261112-2cabbe82`

The other research branches pointed to the baseline commit and had no published commits or manifests at initial inspection. No pull requests were open. No other repository-level assignment could be established from published records. Unsaved work in other ChatGPT sessions is not observable. The session wrote only under `research/sessions/2cabbe82/` on its dedicated branch.

## Verified baseline

Latest `main` commit at baseline: `c33758e2373e8726ed4d4ba58aaab736d83c43de`.

The latest committed `RESEARCH_STATUS.md` and independently parsed candidate/review CSVs reported:
- 404 unique raw discovery candidates
- 63 review records: 8 `DEEP_REVIEW_DOCUMENTED`, 55 `PRELIMINARY_FOCUSED`
- 330 `UNTRIAGED`
- 2 `SCREENED_INCLUDE` awaiting review
- 9 `SCREENED_EXCLUDE`

These are baseline values, not current main-branch totals. The eight canonical deep reviews are static; independent upstream runtime validation was not established. Discovery saturation is not established.

## Assigned batch — 10/10 session artifacts

1. `simitii/CS-Grad-School-Applications-Reading-List` — full one-file corpus inspection; no executable code.
2. `siddu1998/Graduate-Admissions` — complete repository artifact inventory and history; PDFs intentionally not content-audited because the corpus includes personal application/referee material and no license was established.
3. `dxeledx/PhdInfoHub` — model, evidence extraction, cycle semantics, concurrency and stale-worker architecture supplement.
4. `TSTS09/Grad-Admission-Agent` — active routes, auth wiring, CORS, dashboard injection surface and test/server mismatch supplement.
5. `yongruiyu/CS_APP_Agent` — search heuristics, typed extraction, source attribution, merge and cache semantics supplement.
6. `monees007/phd_application_tracker` — mobile/extension capture, Gemini extraction, Firestore, import recovery, reminders and key storage review.
7. `stealth-startup-2026/scholarship-scraper` — structured award extraction, bundle decomposition, international eligibility tri-state and cache supplement.
8. `swadhinbiswas/fundmystudy-scraper` — source adapters, approval-state flaw, source-prefixed deduplication, funding and date semantics supplement.
9. `mdsamhussain1996/vidyasetu-scholarship-portal` — source hashes, annual-cycle rollover, evidence and verification lifecycle supplement.
10. `D2Simon/PhDHub` — local JSON persistence, Docker network exposure, email/AI trust boundary and private-data separation supplement.

## Artifacts owned by this session

All artifacts are additive under `research/sessions/2cabbe82/`. The per-repository reports are stored in `reviews/`. No global inventory, canonical review, shared schema, global status, issue, or another session's directory was modified.

## Cross-repository findings

1. **Discovery is not verification.** Every crawler/agent must create source observations and extraction candidates; only independent source review can promote a claim.
2. **Unknown must remain first-class.** Funding, international eligibility, fee coverage, deadline year, supervisor hiring and admissions outcome must not collapse to false/true or assumed/confirmed.
3. **Evidence needs claim-level lineage.** Preserve exact URL, source snapshot/hash, fetch time, publication/cycle, text span and verifier decision for each field.
4. **Use typed domain decomposition.** Program, vacancy, award, sub-award, funding component, application requirement, applicant class and cycle are different entities.
5. **Keep private applicant state separate.** Documents, email, referee data and personal profile must not be stored in public research inventory.
6. **Treat web pages and email as untrusted input.** LLM extraction must not follow embedded instructions; URL fetching requires SSRF/redirect controls.
7. **State transitions must be server-enforced and auditable.** Crawlers cannot approve opportunities; sending and submission require explicit user action and immutable proof.
8. **Concurrency needs leases and stale-worker rejection.** PhdInfoHub's run/unit tokens and revision history are a useful pattern; cache/hash advancement must happen only after successful ingestion.

## Validation and integration limits

- Container DNS could not resolve `github.com`; no local clone/worktree, dependency installation, test execution or upstream runtime reproduction is claimed.
- Source-level inspection was performed through authenticated GitHub access. Reports explicitly state uninspected files and non-executed checks.
- The siddu1998 PDF bodies were not analyzed; recommendation-letter/private material was excluded.
- No claims are made that source-level findings are runtime-proven or that any third-party system is production-safe.
- The branch is not merged. Mainline inventory and canonical reviews remain untouched. A draft PR should be created only after rechecking current main, comparing the complete diff and obtaining an integration review.

## Progress

- Assigned repositories: 10
- Session-specific review/supplement artifacts: 10
- Session branch commits: 10 artifact commits plus manifest updates
- Local clone/runtime validation: blocked by container DNS
- Canonical integration: pending separate diff review and PR
