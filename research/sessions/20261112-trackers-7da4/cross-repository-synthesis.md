# Cross-review synthesis — evidence-aware PhD source collection and applicant trackers

**Session:** 20261112-trackers-7da4
**Source audits:** [physical10086/phd-application-tracker](reviews/physical10086-phd-application-tracker.md) · [PankidT/phd_tracker](reviews/pankidt-phd-tracker.md)
**Date:** 2026-11-12
**Evidence boundary:** Pinned GitHub source and committed schema. No third-party data crawling or private sheet access.

| Layer | Quantum PhD opportunity tracker | Published-Sheets Svelte tracker | Required research architecture |
| --- | --- | --- | --- |
| Discovery | Python Serper/Bing RSS + visits result URLs | No search: public Sheets HTML parser | Discovery separated from authoritative employer-source verification |
| Scheduling | README says daily Actions but no workflow is tracked | Manual refresh, deploy workflow only | Explicit scheduled run, monitored execution, failure conditions |
| 'Verified' | Successful HTTP retrieval; generic text matching | No employer verification; app progress from sheet | Verified job ID, employer, type, eligibility, funding and dates independently |
| Deadline | Regex from page, reused when source changes | Any invalid/unknown date becomes 'rolling' | Explicit known / verified rolling / unknown / invalid + timezone |
| Canonical identity | URL canonicalization drops all query parameters, title-only duplicate filter | 32-bit hash of university/link-label/deadline | Stable employer vacancy ID, source URL and cycle with controlled aliases |
| Applicant status | Client localStorage plus publicly committed seed history | Public published sheet progress | Private, authorized applicant workflow and evidence-backed submission history |
| Evidence durability | No immutable snapshot or field spans | No upstream source snapshot, client fetch time only | Timestamped capture, content hash, source span, check status |
| Tests | No tests or scheduled workflow in source snapshot | No tests; deployment uses build without typecheck | Parser fixtures, unit and integration tests, CI + live telemetry |

## Priority conclusions

1. **Source availability is not job availability.** A reachable page with 'PhD' and two topical keywords can describe a general research group, not a funded opening; a sheet status may describe one applicant's progress, not current university recruitment. Store separate evidence-status dimensions.
2. **Unknown is not rolling, and historic is not current.** Admissions dates must have the publishing institution's timezone and a current-cycle verification stamp. No fallback from parse failure to rolling, no assumption that last_checked HTTP success confirms a valid deadline.
3. **Cross-session state needs durable identity.** URL queries and title edits are semantically relevant in some employment portals; deadline changes should not change the canonical vacancy key. Revalidate redirect URLs and collisions without destructive updates.
4. **Keep personal applications out of public source datasets.** Static seed code and published Google Sheets expose any included private profile, statuses and notes. Use role-controlled applicant namespaces and redacted research observations.
5. **A real monitoring pipeline has observable execution.** A document claiming daily jobs is not a scheduled workflow. Record job config, last attempted run, last successful run, updated records and structured failures. If a sheet parser suddenly returns zero, do not declare a successful sync.

## Suggested adversarial tests

- Feed a generic university page mentioning "PhD" and "quantum": no verified vacancy without a specific employer opportunity record.
- Edit an employer URL's job-ID query parameter: preserve distinct jobs; change an opportunity title or deadline: retain logical identity with a revised observation.
- Feed date blank, malformed and ambiguous locale: never automatically mark verified rolling.
- Detect a Google pubhtml structure change (row ID/header/column positions) as a schema error, not as zero current opportunities.
- Round-trip full backup → edit application stage → refresh: preserve all imported user edits and source overrides.
- Demonstrate no user-private profile/contact history leaks into public seed JSON, browser assets or published sheets.
- Require HTTP(S) URL schemes after redirect unwrapping and before navigable links.
- Verify monitor workflow configuration, source-check timestamps, timeout/backoff and publisher robots/terms.

## Integration decision

Both repositories were untriaged in the 404-item candidate inventory when claimed. They are **deep static investigations** with inspectable, pinned evidence. No canonical CSV/state mutation is included because simultaneous inventory writers need a separate reconciliation transaction. Research is isolated to this session and can be merged without touching other branches.

**Source URLs:** [Python collector](https://github.com/physical10086/phd-application-tracker/blob/60e477d6a3671b2ebb7a1c7ff958464f544e7cbb/scripts/update_opportunities.py), [browser tracker](https://github.com/physical10086/phd-application-tracker/blob/60e477d6a3671b2ebb7a1c7ff958464f544e7cbb/app.js), [Sheets parser](https://github.com/PankidT/phd_tracker/blob/16986762c20b100554de2c799301374586ad2c87/src/lib/data/loadPositions.ts), [Svelte state](https://github.com/PankidT/phd_tracker/blob/16986762c20b100554de2c799301374586ad2c87/src/lib/data/store.svelte.ts).
