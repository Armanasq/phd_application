# Deep static review — erikpsw/phd-application-pipeline

## 1. Identification and source snapshot
- Canonical repository: https://github.com/erikpsw/phd-application-pipeline, author/owner erikpsw.
- GitHub API license MIT; not a fork, source commit `c445dcbe6a7b71363fbe3b5ae0c285449a0ceeeb` (2026-06-22), checked 2026-11-11.
- Type: applicant-oriented Codex-compatible workflow instructions, a separately bundled outreach sub-workflow and deterministic Python draft generator. Global, including ME/CS/robotics/operations research; Feishu and Gmail host integrations targeted.
- API inspection found no open or closed issues or public releases in sampled endpoints. This means **no reported issues found in the inspected endpoint**, not that the tool has no defects.

## 2. Problem, audience and assumptions
The project addresses multi-professor targeting, proposal-specific evidence selection, Feishu/Lark tracker management, Gmail draft preparation and faculty-reply triage. It assumes an **agent host** with authenticated read/write connectors, a real candidate CV and email account, original PI research pages and the ability to persist a state table. Its output cannot prove a professor is recruiting or a student has submitted an application.

## 3. Documentation, algorithms, implementation and provenance
- [Core workflow skill](https://github.com/erikpsw/phd-application-pipeline/blob/c445dcbe6a7b71363fbe3b5ae0c285449a0ceeeb/SKILL.md) contains onboarding keys, advisor search, scoring, tracker fields, Gmail draft and reply-classification stages. It explicitly prohibits sending without approval and warns not to invent applicant accomplishments.
- [Outreach sub-workflow](https://github.com/erikpsw/phd-application-pipeline/blob/c445dcbe6a7b71363fbe3b5ae0c285449a0ceeeb/phd-outreach-email/SKILL.md) requires a recent real research detail verified on lab/university site, one main pitch angle, at most two candidate evidence points and final message audit. Good design rule: source-specific preparation before text generation.
- [Python email generator](https://github.com/erikpsw/phd-application-pipeline/blob/c445dcbe6a7b71363fbe3b5ae0c285449a0ceeeb/phd-outreach-email/scripts/generate_email.py) implements deterministic draft assembly from JSON with required-field validation, whitespace normalization, name parsing and a small forbidden-hype phrase filter. **Executable code exists for draft text**, but the Feishu/Gmail connector actions are agent instructions, not independently running app code in this repository. No such external integration was run here.
- [Status taxonomy](https://github.com/erikpsw/phd-application-pipeline/blob/c445dcbe6a7b71363fbe3b5ae0c285449a0ceeeb/references/status-taxonomy.md) distinguishes drafts, sent, replies, follow-ups, positive signals, unclear funding and non-recruiting. Properly says positive faculty reply is not an admission offer.
- [Setup guide](https://github.com/erikpsw/phd-application-pipeline/blob/c445dcbe6a7b71363fbe3b5ae0c285449a0ceeeb/references/setup-guide.md) documents credential/connector dependency. No independent operational data showing email delivery or successful 2027 admission was observed.

## 4. Critical methodological assessment
Strengths: explicit user-approval gate, single specific scientific bridge rather than generic flattery, project-evidence restraints, separation of generated drafts vs sent correspondence, deduplication and classified reply states, actual draft-generation source.
Limitations: actual discovery/PI verification is performed by an external agent, and a declarative skill cannot assure source accuracy or persistent API access. There is no field-level source-to-claim verifier, current scholarship/timing revalidation, visa eligibility, salary sustainability or official vacancy gating in the inspected workflow. Deterministic template can over-regularize letters; neither an external email API nor Gmail draft is implemented in the small generator. Prompt-only claims about running full pipeline are conditional on host capabilities.
Privacy: applicant CV, private contacts and emails are potentially read/written by connected cloud services. Authorization must be user-scoped, consented, and separately logged for *draft creation* and *sending*. Do not commit applicant identity or external credentials.
Quality evidence: commit history is effectively one-day initial publication; no releases, production deployments, tests or selected-outcome measurements observed. Neither validity nor success rate was independently measured. License MIT does not automatically permit reusing another user's private data.

## 5. Applicability to international PhD campaign
Adopt evidence constraints, source-specific PI pitch, no invented publication, 2–3 bullet proposal and stage-specific status. Contacting every prospective supervisor is **not** universally necessary: EPFL EDIC explicitly permits no prior PI arrangement, while employment-style direct hire and lab-led scholarships may recommend contact. Template must be preceded by official current supervisor availability, vacancy funding and exact national process.
A 2026 ETH RobotX or Soft Robotics deadline is not satisfied by creating a draft; actual employer submission and confirmation are distinct from emails.

## 6. Comparators and dependencies
- [fanyi3017-stack/phd-application-research-agent](https://github.com/fanyi3017-stack/phd-application-research-agent) is a much longer multi-stage instruction system; both depend on a capable external runtime rather than shipping an entire automated PhD backend.
- [KhanShaheb34/profreach](https://github.com/KhanShaheb34/profreach) offers a real authenticated web app with model endpoint and browser data; erikpsw has simpler portability but weaker built-in state persistence.
- [SihengTao/phd-application-planner](https://github.com/SihengTao/phd-application-planner) defines stronger claim-specific provenance and structured validation.
- Gmail/Feishu are external services, not independent confirmation of scholarship or academic relevance.

## 7. Research judgment
**ADAPT concept, reference implementation for draft-only format, DO NOT TREAT AS OPERATING AUTONOMOUS ADMISSIONS SYSTEM.** Suitable for evidence-based outreach preparation when a PI should actually be contacted. Improve via claim registry, consent receipts, college/PI portal rules, contact-vs-submission separation, privacy boundaries and hard funding gate. Reproduction of connector workflows and delivered emails is **NOT TESTED**.

## 8. Evidence limits and open questions
Permalinks and API observations above are the evidence. Not independently inspected: every setup-guide instruction and every source reached by an agent, actual Feishu data update, Gmail authenticated draft, generated text output under malformed input, dependency lock/compatibility, or how a user uninstalls/revokes connected permissions. A safe local fixture test can validate the Python draft generator without authorizing external communication.
