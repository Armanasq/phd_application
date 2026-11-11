# bchen002/Doctoral-Supervisor-Skill — focused workflow review

- **Review date:** 2026-11-11
- **Pinned upstream commit:** [7e3920af7454d6bc19ba2e718bfc55072e28abbb](https://github.com/bchen002/Doctoral-Supervisor-Skill/commit/7e3920af7454d6bc19ba2e718bfc55072e28abbb); latest commit observed 2026-06-03.
- **Category:** agent skill for doctoral research supervision and project-memory continuity.
- **Review state:** PRELIMINARY_FOCUSED. Reviewed skill, routing rules, memory protocol, weekly execution protocol, schemas and prompt-based test cases; no host runtime tests.
- **License:** no explicit license metadata or license file confirmed.

## 1. Problem and intended user

A session-oriented supervisor assistant helps a doctoral researcher maintain project continuity, prepare meetings, develop research questions, review writing and track weekly execution. It is not an admissions discovery tool, but its memory-governance design is transferable.

## 2. Architecture and routing

The skill classifies incoming work as explicit supervision session, non-session assistance, explicit memory/update request or mechanism development. It reads only the minimum relevant memory files. The proposed memory model separates stable project map, current focus, current week, session index/logs, topical logs, article cards, user profile and interaction feedback.

## 3. Strongest design contribution: a write gate

The protocol separates read-only checks, staged exploratory ideas, confirmed factual progress, stable architecture and unclear updates. It avoids treating every research-related conversation as a session and prevents tentative ideas from silently overwriting durable project memory. The weekly protocol separates completed, unfinished/blocked, capacity, carry-forward and next-week candidates.

Relevant files: [SKILL.md](https://github.com/bchen002/Doctoral-Supervisor-Skill/blob/7e3920af7454d6bc19ba2e718bfc55072e28abbb/supervisor-skill/SKILL.md), [routing rules](https://github.com/bchen002/Doctoral-Supervisor-Skill/blob/7e3920af7454d6bc19ba2e718bfc55072e28abbb/supervisor-skill/commands/routing_rules.md), [memory protocol](https://github.com/bchen002/Doctoral-Supervisor-Skill/blob/7e3920af7454d6bc19ba2e718bfc55072e28abbb/supervisor-skill/protocols/project_memory_protocol.md), [weekly protocol](https://github.com/bchen002/Doctoral-Supervisor-Skill/blob/7e3920af7454d6bc19ba2e718bfc55072e28abbb/supervisor-skill/protocols/weekly_execution_protocol.md).

## 4. Useful workflow patterns

- Explicit routing before memory access.
- Smallest-file read policy.
- Separation of stable architecture from current focus and weekly tasks.
- Session closure as a deliberate handover rather than an automatic side effect.
- Specialized skills return candidate updates; the supervising memory layer controls whether and where those updates become durable.

## 5. Limitations

The repository is a prompt/protocol package, not an executable application or persistent memory engine. Its test cases are natural-language scenarios and expected behaviors, not unit/integration tests. Correct behavior depends on the host agent respecting file paths, routing and write gates. It does not implement source verification, admissions evidence, application state transitions or privacy controls by itself.

## 6. Testing and maturity

Schemas and example memory files provide useful structural conventions. No runtime agent, schema validator or automated test runner was executed. Manual prompt tests cannot establish deterministic behavior across model versions or hosts.

## 7. Adoption judgment

**ADAPT THE MEMORY GOVERNANCE PATTERN.** Apply the read/write gate to PhD Atlas research notes, candidate-specific claims and application state. Use explicit provenance and confirmation for changes to stable candidate facts. Do not adopt a session-first interaction model for every ordinary task.

## 8. Unresolved work

Test routing and write-gate behavior against adversarial/ambiguous prompts; add executable schema validation; specify concurrent writes and recovery; integrate claim/source provenance; define deletion, retention and backup controls.