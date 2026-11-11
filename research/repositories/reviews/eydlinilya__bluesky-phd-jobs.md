# Deep source audit — EydlinIlya/BlueSky-PhD-jobs

## 1. Repository identity and evidence boundary

- **Canonical:** https://github.com/EydlinIlya/BlueSky-PhD-jobs; immutable upstream commit: `352551f3ffa4b880e09635f66ea2b06d888e8ef3` (2026-11-11); examined 2026-11-12.
- **License:** Apache-2.0, as advertised by the GitHub repository metadata.
- **Purpose:** Bluesky academic job-post discovery, classification, deduplication, metadata enrichment, Supabase publication and an indexed public web experience. The current enumerated git tree is dominated by generated output; direct implementation review targeted source modules, migrations, workflow, CLI/docs and representative unit tests.
- **Method:** deep **static, risk-focused** source analysis with pinned code links. **Not performed:** live Bluesky search, OpenAI calls, Supabase mutations, deployment checks, external employer validation, third-party tests or runtime security penetration tests. The presence of tests does not mean they were run in this investigation.

## 2. Implemented design and workflow

The [pipeline runner](https://github.com/EydlinIlya/BlueSky-PhD-jobs/blob/352551f3ffa4b880e09635f66ea2b06d888e8ef3/src/pipeline/runner.py) sequences fetch → filter → dedup → publish, tracking per-stage progress in `pipeline_runs` and per-row `filter_completed` in staged records. [Bluesky source](https://github.com/EydlinIlya/BlueSky-PhD-jobs/blob/352551f3ffa4b880e09635f66ea2b06d888e8ef3/src/sources/bluesky.py) applies keyword searches, skips bot-authored quote posts, filters previously seen URIs and extracts quoted/reply metadata. [Supabase adapter](https://github.com/EydlinIlya/BlueSky-PhD-jobs/blob/352551f3ffa4b880e09635f66ea2b06d888e8ef3/src/storage/supabase.py) maintains raw staging rows, canonical posts, completion states and saved metadata, with paginated discovery of existing URIs. [Deduplication](https://github.com/EydlinIlya/BlueSky-PhD-jobs/blob/352551f3ffa4b880e09635f66ea2b06d888e8ef3/src/dedup.py) combines quoted-post lineage, normalized application URL and later textual/semantic signals, preferring newest posts where appropriate. [Publishing](https://github.com/EydlinIlya/BlueSky-PhD-jobs/blob/352551f3ffa4b880e09635f66ea2b06d888e8ef3/src/pipeline/stages/publish.py) aggregates pending rows across interrupted runs and verifies the number of saved rows before clearing staging.

Evidence-aware parts include [deadline checks](https://github.com/EydlinIlya/BlueSky-PhD-jobs/blob/352551f3ffa4b880e09635f66ea2b06d888e8ef3/src/seo.py) that avoid making invalid timestamps active, requiring a non-Bluesky application URL/title/organization/country before producing `JobPosting`-eligible content, plus classifiers that validate schema and parse source-supported deadlines. These are useful defense-in-depth patterns for a social-signal pipeline.

## 3. Algorithms and source semantics

Bluesky search is a **social signal**, not an official funded studentship database. Each retrieved social post has a URI, user handle, post timestamp, parsed raw/metadata text and optional quotation/reply provenance. Content can enter the dataset before any official employer or funding check. Normalizing application URLs while retaining nontracking query parameters is valuable; quote lineage and exact normalized URLs are relatively strong dedup evidence, but matching an application URL does not by itself prove the post author is authorized or that the contract is open to an international applicant.

The database `is_verified_job` label reflects the pipeline classifier outcome, **not a human- or institution-verified funding and eligibility determination**. Source URLs and date fields require second-stage official verification before ranking applicants or acting on deadlines.

## 4. Demonstrable failure modes

1. **Classification bypass labeled verified:** [filter stage](https://github.com/EydlinIlya/BlueSky-PhD-jobs/blob/352551f3ffa4b880e09635f66ea2b06d888e8ef3/src/pipeline/stages/filter.py) explicitly sets `is_verified_job=True` for *every* pending staging row whenever the `--no-llm` path supplies no classifier. This conflates “not classified” with “verified”; a random social post may become a positive classification without content inspection. A safe run should mark `unclassified` / `verification_pending` and prevent publication or high-confidence ranking until independently adjudicated.
2. **Source errors recorded as successful fetch:** [fetch stage](https://github.com/EydlinIlya/BlueSky-PhD-jobs/blob/352551f3ffa4b880e09635f66ea2b06d888e8ef3/src/pipeline/stages/fetch.py) catches exceptions on each source, logs and continues; it *always* sets `fetch_completed_at` on the run, even if the source failed and `all_posts` is empty. [Bluesky search retry](https://github.com/EydlinIlya/BlueSky-PhD-jobs/blob/352551f3ffa4b880e09635f66ea2b06d888e8ef3/src/sources/bluesky.py) also returns `None` on terminal 429/timeouts and the caller skips that query. Therefore partial or failed acquisition can be silently stamped complete and resume logic skips re-fetching the missed period. Require per-source/query errors, completeness guard and retryable incomplete stage state.
3. **High-water mark independent of crawl completeness:** [Supabase adapter](https://github.com/EydlinIlya/BlueSky-PhD-jobs/blob/352551f3ffa4b880e09635f66ea2b06d888e8ef3/src/storage/supabase.py) derives `since_timestamp` from the newest published post. A partly failed search followed by newer successful postings risks permanently missing older social posts unless per-query watermarks, bounded lookback and replay are used.
4. **Verification labeling:** [classifier](https://github.com/EydlinIlya/BlueSky-PhD-jobs/blob/352551f3ffa4b880e09635f66ea2b06d888e8ef3/src/llm/classifier.py) validates extracted JSON and source deadline evidence, but it cannot verify actual posting authority, funding, nationality, English proficiency, or supervisor consent. `JobPosting`-eligible SEO metadata remains a structured extraction contract rather than a guaranteed official vacancy.
5. **Social/quote ambiguity:** [dedup logic](https://github.com/EydlinIlya/BlueSky-PhD-jobs/blob/352551f3ffa4b880e09635f66ea2b06d888e8ef3/src/dedup.py) treats certain quote relationships and normalized application URLs as deterministic duplicates. Preserve the identity graph separately: repost/quote, same position and independent vacancy are different relations that should remain inspectable.
6. **Release test scope:** targeted [publish tests](https://github.com/EydlinIlya/BlueSky-PhD-jobs/blob/352551f3ffa4b880e09635f66ea2b06d888e8ef3/tests/test_publish_stage.py) and [sync-state tests](https://github.com/EydlinIlya/BlueSky-PhD-jobs/blob/352551f3ffa4b880e09635f66ea2b06d888e8ef3/tests/test_sync_state.py) demonstrate intended failure recovery but do not by themselves establish end-to-end success on a live API or absence of cross-run gaps.

## 5. Required repairs and validation

- Enforce three explicit verification states: `unclassified`, `model_classified_lead`, `official_evidence_verified`; never promote no-LLM mode to a verified positive.
- Make failed/partial search queries fail the fetch-completion gate; persist source-query retrieval coverage, errors and cursors separately, and replay bounded lookback with idempotent upserts.
- Add deterministic tests for 429/timeout/query-local partial failure, full-source failure, resumed later run, same-day repeated execution, source date changes, and quoted posts without authoritative URLs.
- Require independent official job permalink, employer, funding, deadline, nationality/citizenship and contract evidence before doctoral-applicant decision support; treat uncertain/unknown fields as unknown.

## 6. Cross-repository connections

Compared with [Academic Job Digest](https://github.com/BaseLayerAI/academic-job-digest), this repository has a more explicit four-stage resumable state machine, but depends on social-post discovery instead of direct job-board evidence. Compared with [NimaaaAI/Position-Aggregator](https://github.com/NimaaaAI/Position-Aggregator), it avoids the same nominal URL list but still needs fail-closed retrieval completeness: an API failure must never be reported as exhaustive source coverage. Compared with [Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor), it can supply *leads* but must not replace the latter's explicit evidence/verification gating.

## 7. Adoption decision and confidence

**ADAPT pipeline staging, citation lineage and error-tested dedup ideas; DO NOT treat social posts as verified fully funded PhD positions.** Source-level confidence is high for the exact `--no-llm` positive default and fetch-error completion defects because the cited code branches were inspected. Operational impact, empirical recall and external permission/coverage remain untested. License reuse requires following the repository's Apache-2.0 obligations.

## 8. Completion boundary

This is an **eight-section deep source-level static review**, not a full 19k-file artifact-by-artifact inspection or runtime certification. Completion of a production adaptation requires fixture-based test execution, SQL migration/rollback checks, source authorization, verified per-source availability, exact employer evidence and a measured miss/false-positive rate under partial outages. The review does not claim any 2026/27 vacancy, application result or eligibility outcome.
