# Repository review: houwei1228/PhD_Fit

## Review disposition
- Review depth: deep static implementation review.
- Upstream snapshot: main at 1e95411ee0c2425c0ce77b658456e3110a7789f6.
- Tracked files: 21; test modules: 3.
- Last pushed: 2026-09-20.
- GitHub metadata: no issues, no pull requests, no declared license.
- Runtime: not executed; no local checkout or outbound GitHub access was available.

## Product and architecture
PhD_Fit is a local-first Streamlit application backed by SQLite. It combines:
- opportunity discovery through Tavily;
- page extraction and position parsing;
- LLM-based applicant/position fit assessment;
- supervisor matching and scoring;
- deadline and application-status monitoring;
- deduplication and discovery history;
- local document storage and export;
- optional school-account credential storage.

The status-monitoring path is deliberately more deterministic than the fit-analysis path. It uses Tavily extraction/search and Python rules to distinguish target-cycle evidence, historical deadlines, open calls, closed calls, and cases requiring manual verification.

## Main workflows
1. Discover candidate positions using search queries and keyword-based relevance scoring.
2. Extract the source page and structured position fields.
3. Assess the applicant's fit using an OpenAI Responses API call.
4. Search and score supervisors using research fit, publications, recent activity, experience, mentorship, and visibility.
5. Monitor the target intake year, currently defaulting to 2027, and retain evidence excerpts and verification confidence.
6. Save opportunities, documents, and school-account records locally.

The discovery relevance score is a search-ranking heuristic. It is not the same as applicant eligibility, research fit, funding fit, or probability of admission. These dimensions must remain separate in the consolidated tracker.

## Scoring and decision logic
The supervisor score uses weighted components for research fit, publications, recent activity, experience, mentorship, and visibility. The implementation assigns star levels using code thresholds and evidence-count gates.

The position-fit path uses a separate 0–100 assessment and assigns A/B/C/D levels. A hard-gate risk is represented separately from the score, but the implementation only demotes the result when eligibility_fit is below a numeric threshold. A high total score with a populated hard_gate_risks list can therefore remain in a high tier.

## Important implementation findings

### 1. Hard-gate risks do not always override high scores
The scoring helper checks hard_gate_risks together with eligibility_fit < 8 before demoting an A/S-level result. A populated hard-gate list with a higher eligibility_fit value does not trigger the demotion. This weakens the meaning of a hard gate.

Hard constraints should be represented as typed, independently validated conditions. If a non-negotiable eligibility constraint fails, the system should block or downgrade the opportunity regardless of total score.

### 2. Specification and implementation thresholds diverge
The product specification documents different supervisor star thresholds from scoring.py. The runtime uses the code thresholds, not the prose specification. This makes historical and future evaluations difficult to compare.

Introduce a versioned scoring policy, one source of truth for thresholds, and regression tests asserting the documented values.

### 3. Aggregate scores are not fully reconciled with component scores
PositionFitAssessment contains a total_score alongside a component breakdown, but there is no validator proving that the aggregate equals the weighted components. Supervisor evidence items also carry URLs and relevance descriptions without exact supporting quotations. Scores are therefore not fully reproducible from stored evidence.

Store score-policy version, component values, source evidence, and calculation output. Recompute aggregate scores deterministically rather than trusting a second LLM-generated total.

### 4. Discovery score can be mistaken for applicant fit
The discovery candidate score is derived from search terms and opportunity keywords. It ranks search leads, not the user's academic eligibility or research suitability. The UI and schema should label it retrieval_relevance rather than fit_score.

### 5. Arbitrary URL retrieval lacks SSRF and resource controls
services/fetcher.py uses requests.get against supplied URLs with a timeout, but the reviewed implementation does not enforce a public-IP-only policy, block localhost/private/link-local addresses, validate redirect destinations, or impose a response-size limit. If the app is exposed to untrusted users or runs on a network with sensitive internal services, this creates SSRF and resource-exhaustion risk.

The README positions the app as a private single-user local tool, which narrows but does not eliminate the risk. Restrict URL fetching to approved public hosts and enforce redirect, MIME, size, and decompression limits.

### 6. Environment example is stale
The code reads APP_SECRET_KEY for Fernet credential encryption, while .env.example documents APP_ENCRYPTION_KEY. This can cause operators to configure the wrong variable and silently fail to encrypt saved credentials.

### 7. Local security is conditional
The login gate is optional: when APP_LOGIN_PASSWORD is absent, the app allows access. Fernet encryption protects saved school-account passwords only when APP_SECRET_KEY is configured. The SQLite database and uploaded application documents are not encrypted by this mechanism.

This is acceptable only under the stated private local-use assumption. Document the trust boundary and recommend encrypted storage/backup for CVs, transcripts, and other application documents.

### 8. Monitoring evidence is not uniformly authoritative
The monitor builds an evidence bundle from official_url or the position URL and searches the same site. If the stored URL is an aggregator or a non-official page, the same-site search can reinforce the wrong source. The monitor retains excerpts and a verification confidence, but source authority should be validated before treating the domain as official.

## Positive patterns worth retaining
- Separate deterministic status monitoring from LLM-based fit assessment.
- Target-intake-year-aware deadline logic.
- Explicit historical-deadline handling.
- Conservative manual-verification states for ambiguous cases.
- Canonical URL and title/snippet-based deduplication.
- Local storage and optional encrypted credentials.
- Tests for monitoring logic, deduplication, and discovery history.

## Gaps
- No license declared.
- No issues or pull requests.
- No general CI workflow was identified.
- Only three test modules are present; no live integration or calibration dataset was inspected.
- No runtime test was executed.
- No verified admission outcomes are stored to calibrate scores against real results.

## Recommended corrections
1. Make hard-gate rules independent of aggregate scores.
2. Version the scoring policy and reconcile the specification with code.
3. Rename search relevance scores and separate them from applicant fit.
4. Add field-level evidence and quote verification for extracted facts and supervisor claims.
5. Harden URL fetching against SSRF, redirects, oversized responses, and unsupported MIME types.
6. Fix the environment-variable mismatch and make credential-encryption state visible.
7. Store documents outside the source tree with encryption, access controls, and backup policy.
8. Require an official-source classification before same-site status monitoring.

## Evidence and coverage
- Repository: https://github.com/houwei1228/PhD_Fit/tree/1e95411ee0c2425c0ce77b658456e3110a7789f6
- README, product specification, changelog, environment example, app, database layer, scoring, models, security, document storage/export, fetcher, opportunity monitor, OpenAI service, and all test modules inspected.
- No issue or pull-request history.
- Static review completed; runtime and test execution blocked by the unavailable local checkout.