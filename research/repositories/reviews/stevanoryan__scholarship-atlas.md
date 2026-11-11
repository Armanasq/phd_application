# stevanoryan/scholarship-atlas — source-pinned preliminary investigation

**Snapshot:** 9c2b5c3c8ca0aa1ca18f91d82fbdbcc9988ce59f; **inspection date:** 2026-11-12; **state:** PRELIMINARY_FOCUSED; **independent runtime/source verification:** NOT_PERFORMED.

## Scope and structure

Scholarship Atlas is a single-file HTML/JavaScript scholarship ledger, not an official scholarship agency. The README reports 172 opportunities spanning undergraduate, master's and doctoral study, with funding/stage/status filters. Source is 272,271 characters in index.html, with six arrays DATA/MORE/MORE2/MORE3/MORE4/MORE5, entries carrying id, country, issuer, stages, open, deadline, funding, descriptions, applicant checklists and cited official webpages.

## Evidence and time correctness

The UI says dates checked 2–6 November 2026, but many entries explicitly mark dates EXPECTED based on previous cycles. The app calculates 'Open now'/'Upcoming' from the user's browser date; that is a computed display state, not independent confirmation of an active recruitment or funding offer. The first inspected entry is a master's programme, showing why an inclusive scholarship list cannot be treated as a list of doctoral positions. The financing strings 'Fully funded' and 'Partially funded' are author-curated attributes, not proof of eligibility, salary, tuition remission or employer offer.

## Transfer, limitations, disposition

Useful patterns: stable source IDs, explicit estimated-date labeling, official-source outbound links per entry, per-award document checklists, application stages, client-side sorting and user-controlled checkboxes. Do not bulk-import status/funding as authoritative. For each target verify official 2026/27 PDF or employer portal, applicant citizenship and academic stage, stipend/tuition conditions, and expiry in the source timezone. No live link check, runtime execution, source-by-source eligibility audit or independent 172-record verification performed. This is PRELIMINARY_FOCUSED.

Pinned [README](https://github.com/stevanoryan/scholarship-atlas/blob/9c2b5c3c8ca0aa1ca18f91d82fbdbcc9988ce59f/README.md) and [index data and date logic](https://github.com/stevanoryan/scholarship-atlas/blob/9c2b5c3c8ca0aa1ca18f91d82fbdbcc9988ce59f/index.html).
