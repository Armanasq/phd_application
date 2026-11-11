# fundmystudy-scraper — supplemental implementation investigation

- Existing canonical pin: `7b9337280032d748c10fd136cf74ba8e1da7cd68`
- Status: supplemental static review of existing implementation findings; no upstream execution.

## Additional synthesis

The adapter architecture is reusable for ingestion but its identity and approval semantics are not safe as a source of truth. A source adapter should emit raw observations, not application-ready approved opportunity records. A crawler must never be allowed to promote an item into an approved state simply because parsing succeeded.

The source-prefixed dedupe key is a deliberate per-source identity, but it means the same vacancy mirrored on EURAXESS, jobs.ac.uk and an institutional portal remains three records. PhD Atlas needs a two-layer identity: upstream observation identity (source + external ID) and cross-source canonical opportunity identity (employer/program/location/title/time-window) with ambiguity-aware matching. Each upstream URL and source-specific raw payload must remain attached to the canonical record.

Funding is a set of independent claims: salary, stipend, tuition waiver, fee coverage, duration, award probability and applicant-class eligibility. Neither a generic funding label nor words such as "studentship" or "funded" in a search result establish full international funding.

Date-only values must remain local calendar dates plus source timezone and cutoff-time evidence, not arbitrary UTC instants. Ambiguous date parsing should create a review item rather than a guessed date.

## Integration recommendation

Keep the adapter/normalizer/raw-payload pattern. Place an evidence gate between ingestion and public publication, implement server-enforced review transitions, and separate user application state from source refresh. Tests should cover duplicate aliases across providers, ambiguous date formats, unknown funding, idempotent replay, and the invariant that a crawler cannot set an opportunity to verified or approved.
