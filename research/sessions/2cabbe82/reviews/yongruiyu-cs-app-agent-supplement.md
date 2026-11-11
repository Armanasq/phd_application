# yongruiyu/CS_APP_Agent — supplemental implementation investigation

- Existing canonical review pin: `5b644384787993d27443434f0319819654bb491c`
- Status: additional static inspection of search, collection, schema, cache and completeness checker; no runtime execution.

## Intended control loop

The agent researches one school/program at a time. The sequence is:
1. Search for a likely official graduate admissions page.
2. Extract typed fields from page content.
3. If critical facts are absent, search the original hostname for a more specific requirements page.
4. Merge newly found values into missing fields.
5. Preserve a URL per populated section.
6. Run deterministic completeness checks and issue a bounded targeted follow-up.
7. Persist program research as Markdown/cache artifacts.

The `ProgramInfo` schema covers deadline, language requirements, local/international tuition, funding, duration, courses and `field_sources`. This is a meaningful move from unstructured chat to a typed fact bundle.

## Search heuristics and false positives

`tools/search.py` excludes a list of noisy domains and ranks URL paths with admissions-related tokens. Its `_is_official` predicate accepts any host ending in a recognized education TLD or containing a school-name token after punctuation stripping. This is a ranking heuristic, not an institutional domain allowlist. An unrelated or spoofed host can satisfy the string test; officialness must be verified against a known domain registry or official link from the institution.

## Collection and provenance semantics

`tools/collect.py` extracts fields through an LLM, and when the result is sparse it searches the same domain for a richer page. It merges only fields that were missing in the first result and records a source URL for each section. This supports incremental fact recovery, but:
- a section URL is not proof that its page entails the displayed value;
- no exact quote/span validation is applied;
- conflicting values are not represented as competing claims;
- merge logic keeps the first populated value, potentially preserving a stale or wrong fact;
- program identity is supplied by the caller and is not necessarily revalidated against the page.

## Completeness checker

The checker treats deadline, TOEFL and IELTS as critical for retry; the full required set also includes waiver policy, tuition, funding and program length. It can prompt targeted follow-up for missing fields and requires a source line under each section. The approach is deterministic and auditable, but its mandatory TOEFL/IELTS assumption is not universal across all countries/programs, and a blank field may mean genuinely not applicable rather than missing.

## Cache correctness

The cache wraps new entries with a timestamp and expires them after seven days. Legacy unwrapped entries are returned indefinitely. There is no evidence in this code of invalidation based on source content hash or admission-cycle change. A 7-day TTL is also not sufficiently cycle-aware for volatile deadlines unless near-deadline refresh is prioritized and source hashes are checked.

## Atlas transfer

Adopt one-program-at-a-time research, typed field schemas, section-level provenance, bounded retry and deterministic completeness checking. Improve with:
- institution-verified host allowlists and redirect validation;
- claim-level evidence spans and source snapshot hashes;
- explicit conflict objects and reviewer decisions;
- program/cycle identity validation;
- applicability-aware required fields;
- cache keys including cycle, applicant class and source revision;
- recheck triggers based on deadline proximity and source update detection.

## Files examined

`tools/search.py`, `tools/collect.py`, `tools/cache.py`, `checker.py`, and `models.py`, plus the orchestration and test paths described in the canonical review.

## Outstanding verification

No LLM/web provider call or tests were executed. Inspect full agent orchestration, cache migration behavior, output writer, and tests at the exact current upstream HEAD; verify official host false-positive fixtures and conflicting fact behavior.
