# Cross-repository synthesis — local application command center vs funded PhD monitor

**Date:** 2026-11-12  
**Scope:** Two source-pinned, third-party static investigations. Not a validated sample of doctoral opportunities.

## 1. Different products, complementary state machines

| Boundary | `fsuitoal-code/phd-application-command-center` | `Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor` |
|---|---|---|
| Primary task | Personal application dossier and user-owned workflow | Recurring funded doctoral vacancy evaluation and retained history |
| Storage | SQLite/SQLAlchemy; Alembic with pre-upgrade backup | SQLite stdlib; versioned schema, run lock, backups and append-only evaluation events |
| Research | Claude Agent SDK, official-domain program fetch and wider faculty fetch | Executing agent researches; Python only validates packets and manages state |
| Evidence | Model-authored quotes + URL, human-verification flag; no independent captured-page quote match | Caller-declared fact/authority/timestamp metadata and hash-bound review; no external page authentication |
| Fatal trust gap | Last-two-label domain scope admits unrelated `*.ac.uk` pages; source quotes unverified | Caller can assert `PRIMARY` evidence; `SELF_SECOND_PASS` satisfies reviewer-PASS gate |
| Candidate identity | Program-centric local relational ID and faculty membership | Official requisition scoped by authority, URL aliases, fingerprint collision review |
| Funding | Notes/requirements, no complete applicant-specific finance contract | Typed salary/tuition/stipend/international fee route and eligibility gates |
| User actions | Explicit steps, documents and outreach flags | No submission/outreach; explicit manual baseline before scheduling |
| Operational limits | No AI budget ceilings; local data path fail-closed | One writer, CV/profile/config snapshots, source coverage and CSV formula defenses |
| Empirical validation | 24 test files inventoried; no upstream Actions history returned | Python 3.11 Ubuntu/Windows unit CI successful at pinned commit, not live search |

## 2. Combined design for `phd_application`

Use two distinct aggregates:
- **Evidence / Opportunity**: source snapshots, fetched URL and redirect chain, issuing institution and requisition, observed fields and dated claims, funding and eligibility decisions, reviewer identity, source coverage and audit events.
- **User Application**: program/supervisor decisions, program-specific document versions, checklist states, correspondence, commitments, submission receipts, and deadlines.

An opportunity must not silently become an application and a user checklist completion must not certify an institutional submission.

Enforce each gate at a separate boundary:

1. `source_registry` provides institution and host identity, not a name or public-suffix guess.
2. A deterministic crawler fetches the permitted official source, validates DNS/redirect and archives the exact evidence content hash.
3. Extraction returns typed candidate claims with spans, URLs, observed cycle and unknown/conflict states.
4. Source verification resolves actual quote/span, program and cycle scope, date, funding class, fees and nationality applicability.
5. Distinct reviewer attestations are tied to immutable evidence snapshots; self-review is labeled differently from independent validation.
6. Hard gates yield `PUBLISH/HOLD/REJECT/UNDER_THRESHOLD` before fit ranking.
7. The application workflow remains user-authorized, with immutable proof of actual external actions.
8. The system records complete/partial/failed coverage, stale sources, conflicting revisions and explicit retries.

## 3. Operational controls

- Use database revision-and-content-hash optimistic concurrency, bound writes, append-only history, safe backup/migration paths and periodic restore validation.
- Avoid single-writer SQLite if the platform becomes a public multiuser application. Use authenticated server endpoints and user/tenant ownership policies.
- Put per-request bytes/time, agent budget, retry and context ceilings around research; checkpoint before emitting expensive terminal JSON.
- Add regression tests for `ac.uk`, `edu.au`, official-site path confusion, URL aliases, same-name researchers, stale cached claims, reviewer-mode misuse, formula injection, fee coverage and separate funding deadlines.
- Keep independently verified facts separate from model-supplied confidence and subjective fit scores.

## 4. Evidence boundaries

The two upstream source trees were pinned, read and inspected in critical paths. No third-party tests were locally executed and no CV data or credentials were provided. The upstream CI passing result belongs to the scholarship monitor's own test suite; it does not certify external vacancy accuracy. `phd_application`'s structural CI likewise cannot validate live third-party claims.
