# Session research manifest — 20261112-0031z-gpt6-a

**Review date:** 2026-11-12  
**Working branch:** `research/repository-audit-20261112-0031z-gpt6-a`  
**Original base commit:** [`c33758e2373e8726ed4d4ba58aaab736d83c43de`](https://github.com/Armanasq/phd_application/commit/c33758e2373e8726ed4d4ba58aaab736d83c43de)  
**Main branch observed during reconciliation:** [`e821fcdbf572c96b5be617a2626f6def68f8ab3d`](https://github.com/Armanasq/phd_application/commit/e821fcdbf572c96b5be617a2626f6def68f8ab3d)  
**State:** MERGED_TO_MAIN via [PR #8](https://github.com/Armanasq/phd_application/pull/8) at commit [`451ec6cd8d25f4b4826c819ca3454873264b5eed`](https://github.com/Armanasq/phd_application/commit/451ec6cd8d25f4b4826c819ca3454873264b5eed); upstream runtime validation NOT performed.

## Coordination and noninterference

- The original branch was created at an earlier main snapshot. It is intentionally not rebased via a force-push.
- This session may write only under `research/sessions/20261112-0031z-gpt6-a/`.
- Canonical inventory, generated index, opportunity records, issue status, and other sessions' directories are not modified here.
- Latest inspection observed merged PR #6 (ten investigations), PR #7 (three investigations), other active session branches, and no open PRs at that instant.
- The two historical-resource reviews were already merged through [PR #6](https://github.com/Armanasq/phd_application/pull/6), then reconciled to canonical preliminary records by another session. This branch's redundant drafts were removed before PR preparation.
- Other agents' private, unsaved progress cannot be observed through GitHub; no unpublished ownership or success is inferred.
- GitHub API connector is used for source inspection and branch-scoped writes. A local `git ls-remote` still fails because `github.com` cannot be DNS-resolved in the code runtime; no local upstream test execution is claimed.

## Assigned repository outcomes

| Upstream | Pinned commit | Session disposition | Evidence record |
|---|---|---|---|
| `zhoujasper/phd-atlas` | `8f4318eda901020b61d91abfc82411943200c70f` | DEEP_STATIC_REVIEW_COMPLETE for representative major domain, persistence, authorization, discovery, and security-critical implementation paths; runtime NOT_TESTED | [PhD Atlas review](zhoujasper-phd-atlas.md) |
| `zxcgzx/phd-application-tracker` | `8826e96755f4d76854e00725226ff92fed59af18` | DEEP_STATIC_REVIEW_COMPLETE for crawler, database, frontend, CI and security paths; deployment and exploitability NOT_TESTED | [Supervisor-tracker review](zxcgzx-phd-application-tracker.md) |
| `simitii/CS-Grad-School-Applications-Reading-List` | `189be53b9299ded95d7a6517b6d5760d4286df70` | Already integrated in main via PR #6; no duplicate review to merge | [Published review](../2cabbe82/reviews/simitii-cs-grad-school-reading-list.md) |
| `siddu1998/Graduate-Admissions` | `71d1750175b1cca2bca78fe738765b0c42c58c0a` | Already integrated in main via PR #6; PDF body and recommendation-letter contents NOT reviewed | [Published review](../2cabbe82/reviews/siddu1998-graduate-admissions.md) |

## Source-level evidence and method

1. Pin upstream commits and Git tree SHAs separately. GitHub recursive tree lookup with a branch ref returns the branch commit SHA in this connector; the actual Git tree hash comes from the commit object's `commit.tree.sha`.
2. Inspect current repository README/tree/config/history/issue/PR status and selected critical modules.
3. Trace claims through actual program code rather than trusting marketing descriptions.
4. Separate observed implementation, source-level risk, operator recommendation, and untested hypothesis.
5. No key-bearing code or downloaded recommendation-letter content is redistributed. No credential was authenticated or tested.
6. The two new reports include commit-pinned GitHub source links for independent inspection.
7. Runtime validation is not implied by static review or upstream historical CI results.
8. A passing source-integrity test in `phd_application` cannot independently verify the correctness of third-party implementation claims or university vacancies.

## Engineering synthesis

PhD Atlas provides reference patterns for:
- explicit field authority and optimistic revision handling;
- durable mutation acknowledgements and conflict detection;
- separated lead-only and official-source evidence in discovery;
- bounded long-running research with encrypted checkpoints;
- account- and scope-bound agent credentials, default-deny endpoint policy;
- guarded official-page crawling and canonical source provenance.

The simpler Supabase tracker provides negative examples:
- public service-role JWT fallback and permissive read/write RLS;
- interpolated GitHub Actions input passed to `eval`;
- stored HTML injection via uncontrolled templates;
- missing official-source provenance for recruiting/funding;
- import/schema mismatch and unreliable crawl success accounting.

No facts in these reports establish that a supervisor is currently accepting students, that funding exists, or that an application has been submitted.

## Integration plan

- **COMPLETED:** the two deep reports, provenance note and manifest were merged through [PR #8](https://github.com/Armanasq/phd_application/pull/8). The research-integrity PR workflow and resulting main push workflow passed.
- **COMPLETED BY PARALLEL INTEGRATION:** the two reports were copied byte-for-byte into `research/repositories/reviews/` and their existing canonical rows promoted to `DEEP_REVIEW_DOCUMENTED` in commit [`ffba448362720cd5bfdcbfb40f117f924c16d70a`](https://github.com/Armanasq/phd_application/commit/ffba448362720cd5bfdcbfb40f117f924c16d70a). Blob SHA equality was verified for both canonical/session copies. This session did not overwrite shared canonical files.
- **VERIFIED:** canonical `data/repositories.csv` and generated `research/repositories/index.md` both show the two upstreams as `DEEP_REVIEW_DOCUMENTED`; the current index-generation check passed.
- Do not close issue #3 merely because this small subset is reviewed; the latest canonical inventory still contains hundreds of outstanding candidate/review records.
- Do not merge unrelated active branches or silently close unrelated issues.

**This session is a bounded research increment, not completion of the 404-repository program.**
