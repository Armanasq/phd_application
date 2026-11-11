# ekotwidodo/awesome-phd-positions — source-pinned resource-index review

- Inspected upstream commit: `1482cb17635e35246ed69cd28648e8ed77d39075` (5 July 2026).
- Inspected tree: `6fcd316ae672c83a79036c45cceccc915cc080c8`; two tracked files: README.md and CONTRIBUTING.md.
- Review date: 2026-11-12.
- Review state: PRELIMINARY_FOCUSED. Both source files were read; linked vacancy portals and live job records were not independently verified.
- Verdict: useful source-registry input, **not** evidence of currently available funded doctoral positions.

## Scope and actual information model

The README is a human-curated index of doctoral vacancy search destinations grouped into 16 countries, plus multidisciplinary European job boards and doctoral-programme/scholarship portals. Countries span Austria, Belgium, Denmark, Estonia, Finland, France, Germany, Ireland, Italy, Luxembourg, the Netherlands, Norway, South Korea, Sweden, Switzerland and the United Kingdom. Entries point to university recruitment sites, national or disciplinary vacancy aggregators, and programme admission pages; they are not individual current job postings.

The repository has no crawler, API, source snapshot store, per-vacancy extraction, normalized funding fields, date model, job-status monitor, or independent eligibility checks. The contribution process accepts GitHub pull requests for new resource links and fixes. There is no automated validation or health-monitoring workflow in the two-file tree. README declares CC0 1.0, but no separate LICENSE file is present in the inspected tree.

## Source authority and reliability

The list combines different evidence classes: official institutional recruiting portals, general-purpose job boards, programme guidance, and broad funding-programme landing pages. A link to a university careers portal does not prove that a supervisor is recruiting, that a vacancy is individually funded, or that international applicants are eligible.

For example, Switzerland contains institution-level sources for ETH, EPFL, universities and independent research institutes; the Netherlands section directs readers to AcademicTransfer. These links are useful discovery seeds for the project's country dossiers but must be independently fetched, dated and evaluated before any opportunity is labelled open or funded.

A cited EURAXESS URL contains the literal filter token `php_positions`, which may not correspond to a doctoral-position category; its live search behavior was not tested. Some resource URLs use HTTP or generic institutional pages. No per-link last-checked, failure reason, source-type classification, version history of linked pages or job ID is recorded.

## Implementation and transferable method

The list suggests an efficient **source registry** rather than a vacancy database: assign each entry a normalized institution/provider identity, geography, authority class, search granularity, fetch policy, discovery timestamp, source URL, last-successful check and error state. Emit independently sourced vacancy objects only after inspecting primary job content. Keep funding, duration, tuition, deadlines, nationality, and project/supervisor availability as separate, evidence-backed fields.

The repository is a discovery-input complement to this project's opportunity and evidence registers. A source may appear in several curated indexes; common links do not provide independent corroboration. This project should deduplicate source URLs and distinguish source discovery from opportunity verification.

## History, issues, and limits

The inspected upstream revision last changed the ELRA link on 5 July 2026. No issues or pull requests were returned by the upstream repository searches at review time. Every source file in the two-file tree was inspected, but linked external sites were not crawled and no link-health or vacancy-state guarantee is made.

Primary files:
- [README at pinned commit](https://github.com/ekotwidodo/awesome-phd-positions/blob/1482cb17635e35246ed69cd28648e8ed77d39075/README.md)
- [Contribution guidance at pinned commit](https://github.com/ekotwidodo/awesome-phd-positions/blob/1482cb17635e35246ed69cd28648e8ed77d39075/CONTRIBUTING.md)
