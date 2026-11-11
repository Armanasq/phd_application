# zxcgzx/phd-application-tracker

- **Assessment date:** 2026-11-11
- **Canonical repository:** https://github.com/zxcgzx/phd-application-tracker
- **Inspected snapshot:** 8826e96755f4d76854e00725226ff92fed59af18
- **Category:** TRACKER_IMPLEMENTATION
- **Review depth:** focused repository inspection (not a complete source audit)
- **Inspected material:** README.md; crawler/main.py; base_scraper.py; supabase_sync.py; database/schema.sql; scheduled workflow; root tree
- **Verdict:** REJECT_AS_IS

## Distinct practical value
Demonstrates configurable two-level faculty crawler, Supabase sync, status tracking, daily scheduled CI, collaboration and exports.

## Verified limitations and risks
CRITICAL SECURITY: synchronization source embeds a Supabase service-role JWT fallback in published code. Public-read RLS policies need scrutiny; privacy rules are unsuitable for confidential applications. Scraper selectors are site-specific and university configuration is manual. Do not copy embedded credentials.

## Candidate-specific action
Reuse only abstract crawler/adaptor and event-ledger ideas after independent secure reimplementation; never import its credentials. Owner should rotate/revoke any exposed service-role key; no external action taken.

## Not inspected or demonstrated
No execution, complete RLS review or penetration test. No proof that any credential remains valid.

**Evidence rule:** The GitHub source is the artifact for this repository assessment. Source claims about external universities, visas or funding remain unverified until checked at the respective primary authority. This review does not claim tests ran successfully.
