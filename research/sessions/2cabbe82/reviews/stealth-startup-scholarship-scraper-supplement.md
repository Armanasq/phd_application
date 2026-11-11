# scholarship-scraper — supplemental implementation investigation

- Existing canonical pin: `dee3edaa40ed8c06821d337721259e146d79caf7`
- Additional files inspected: `requirements_extractor.py`, `scholarship_common.py`, `unsw/verify_international.py`, `usyd/verify_usyd_international.py`, plus the repository's 36 KB `AGENTS.md) import/operations guide.
- Status: static implementation review; no tests or live scholarship source fetches executed.

## Additional findings

The extraction module uses the Anthropic SDK against a DeepSeek Anthropic-compatible endpoint. It exposes three structured tool contracts: requirement extraction, bundle splitting and row QA. Tool-use responses are parsed as structured `block.input` rather than free-form JSON. Inputs are pre-extracted eligibility/application text rather than raw HTML. Cache keys include model and source text parts, and results are persisted in SHA-256-addressed JSON files.

This is a deliberate token/cost architecture: the scraper sends compact semantic sections, caches deterministic extraction inputs, and can run without an API key by falling back to raw eligibility text or deterministic detection. The classifier's offline fallback is regex-based; splitter failure causes a skip-and-log path rather than inventing child awards.

The long operational guide records concrete source-shape failure lessons:
- one source page can list several awards with different titles, codes, amounts and criteria;
- multiple recipients of one award are not multiple awards;
- several monetary amounts can describe one award's stipend/allowance structure;
- broad course-code regexes can be mistaken for award identifiers;
- aggregator pages that merely link elsewhere should not be imported as awards;
- application requirement JSON must match the downstream UI's expected contract.

## Critical interpretation

The code's three LLM tools are structured extractors/classifiers, not independent verification. The system still needs source-level evidence spans and human review. The international eligibility checks are particularly dangerous where absence of a restriction is converted to positive eligibility. Preserve tri-state logic and require affirmative official evidence for an international applicant.

## Transfer

Adopt the parent/child award decomposition, typed award fields, raw payload retention, separate `source_last_synced_at` and `last_verified_at`, model/tool structured outputs, and cache keyed to model plus source content. Improve with quote-span validation, tri-state citizenship eligibility, reviewer identity, exact source host verification and a separate independent verification state.

## Remaining gaps

The current session did not independently fetch the live Australian university pages, validate the 2026/27 scholarship terms, run the source tests, inspect all downstream Supabase SQL migrations, or verify the nested UI/UX skill's relationship to the scholarship scraper. The root repository includes a substantial nested UI/UX skill subtree that appears separate from the Australia scholarship pipeline; treat it as unrelated unless a direct integration is demonstrated.
