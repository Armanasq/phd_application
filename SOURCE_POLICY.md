# Evidence and source policy
Effective 2026-11-11. Applies to repositories, admissions claims, and strategy.

## Verification has two orthogonal axes
1. **Retrieval:** retrieved, partial, inaccessible, blocked, missing, not checked.
2. **Claim status:** SUPPORTED_PRIMARY, SUPPORTED_SECONDARY, FIRSTHAND_SINGLE, CORROBORATED_FIRSTHAND, HISTORICAL, INFERENCE, CONFLICT, UNVERIFIED.

A working URL does not make an assertion true. A university-domain page may be official for one claim but not another. Current cycle, target degree, international status and departmental exception must match the exact case.

## Required claim fields
`claim_id, subject, predicate, value, units, valid_cycle, country, source_url, source_type, locator, accessed_on, status, independent_recheck, next_recheck, discrepancy, decision_effect`. Unknown is null/UNKNOWN; unsupported funding never becomes CONFIRMED_FULL simply through wording in an aggregator.

## Funding and time rules
Separate: **admission eligibility**, **fee-status**, **funding eligibility**, **funding decision**, **offer expected date**, **enrollment date** and **money/contract start**. Student award and paid employee contract differ. Fully funded evaluation requires (a) tuition/fees and *international* fee difference, (b) gross stipend/salary and duration, (c) sustainable location-specific costs, (d) contingent restrictions, (e) insurance/tax/benefits where relevant. A university “minimum stipend” is not an actual individual offer.

## Repository audit limits
Code source file+SHA demonstrates what is present; README documents claims; tests demonstrate intended behavior but cannot prove passing until executed. Issue titles show reported symptoms, not necessarily verified root causes. Last metadata update may be stars or events; use **commit date** for substantive maintenance. Do not reuse code without compatibility/license/security analysis.

## Applicant experience limits
One forum claim is FIRSTHAND_SINGLE or UNVERIFIED_ANONYMOUS, never an institutional selection rule. An allegation about bias is not evidence of system-wide bias. Contradictory stories are retained without selective weighting, and self-selection/survivorship bias must be noted.

## Verification before action
Before submitting: re-open primary application portal and program conditions on action date, cross-check applicant documents/private credentials, ensure stipend and eligibility gates, record authorization and confirmation receipt. No “submitted”, “sent”, “offer”, or “accepted” state without direct documentary evidence.

## Privacy / attribution
Preserve canonical URLs and upstream commit SHAs, not full copyrighted pages, PDFs, credential-like strings or someone else's documents. Limit quotes to necessary short excerpts; write original critical commentary. Cite every consequential empirical claim in same paragraph or table row.
