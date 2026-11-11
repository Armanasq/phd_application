# Research session: application and opportunity trackers

- Session: 20261112-trackers-7da4
- Repository: https://github.com/Armanasq/phd_application
- Base main: 71e7931133fe471d81199173d14611e80caae9a8
- Isolated branch: research/repository-audit-20261112-trackers-7da4
- State: IN_PROGRESS
- Write scope: research/sessions/20261112-trackers-7da4/ only
- Planned merge: source-referenced reports + synthesis via GitHub PR after diff and CI verification
- Worktree limitation: GitHub branch-scoped APIs; no local worktree or credentialed external runtime claimed

## Disjoint assignments

1. physical10086/phd-application-tracker — pinned main 60e477d6a3671b2ebb7a1c7ff958464f544e7cbb; 16-file static+Python opportunity monitor; source freshness, links, state transitions, privacy and scheduling.
2. PankidT/phd_tracker — pinned main 16986762c20b100554de2c799301374586ad2c87; Svelte/TypeScript Google Sheets tracker; audit source loading, sheet trust, schema, deadlines, statuses, deployment and safety.

Both were UNTRIAGED in canonical data/github_discovery_candidates.csv. Existing main review paths and published branch manifests checked before assignment had no claims for these canonical identities. Unpublished work in other conversations is unknown.

## Validation requirements

- Inspect source implementation and documented behavior at pinned upstream revision.
- Distinguish code implementation, README claims, observed source data, and unknown runtime behaviors.
- Record any uninspected binary/private contents and do not expose applicant-private information.
- Do not invoke third-party crawlers, Google credentials, submission or email services.
- Update only files within this session's directory. Never rewrite the canonical inventory, other agents' files, issues or main directly.
