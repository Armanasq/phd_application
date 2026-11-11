# ratulsaha2021/scholarship-agent — eight-section static source review

**Upstream revision:** `a361d74828722b36fd2cfff1ff96f4cc86e857c4`; **inspected:** 2026-11-12; **review:** DEEP_REVIEW_DOCUMENTED; **runtime validation:** NOT_PERFORMED; **source action:** READ_ONLY.

## 1. Research question and claimed functionality

The Streamlit assistant accepts CV PDFs/DOCX, pasted vacancies or screenshots, searches EURAXESS and jobs.ac.uk, drafts tailored email/SOP/research proposals and can send a user-approved email with attachments over SMTP. README demonstrates a synthetic applicant for screenshots and requires one Ollama or Groq model. This is an application-content assistant, not an authoritative funded-position corpus.

## 2. Architecture, data and boundaries

52 tracked entries, including Streamlit UI, src/chat_agent.py (~43 kB), src/hybrid_llm.py, writer, sources/euraxess.py, jobs_ac_uk.py, email_sender.py, DOCX generator, tests and asset screenshots. Opportunity listings are collected by fixed BeautifulSoup CSS selectors and relative-link expansion; output includes deadline strings but does not establish salary, funding guarantee or nationality eligibility. Local resources/ file stores extracted CV and documents; SMTP configuration is serialized to config/email_config.json including a password field (README claims gitignored, but there is no secret-vault or encryption guarantee).

## 3. Message and outbound action state machine

ChatAgent._handle_write creates a pending draft and enters waiting_send; _handle_send_response sends only after a short affirmative message, with negative/cancel guards; user can change recipient via an explicit 'to:' command. _handle_send requires a configured SMTP account and recipient and attaches CV/SOP/proposal when present, retaining draft on failure and clearing only after send_email success. This is better than systems that send on mere generation. However no queue-level idempotency key, persisted recipient approval receipt or transactional outbox was observed. The confirmation is chat state, not a system-wide approval policy.

## 4. Critical fact-check fail-open finding

HybridLLM.fact_check returns [] both when the model reports no unsupported claims AND when inference raises an exception, returns invalid JSON or has no parseable object. tests/test_documents_and_facts.py explicitly asserts this behavior in test_fact_check_tolerates_bad_output. During hybrid_generate, email drafts can skip the second post-rewrite verification to reduce delay. Consequently '[] problems' does not mean source-verified; it may mean verification was unavailable. A failed check must instead carry UNKNOWN/ERROR and block claim of fact-checked output. Sources are assembled from CV/context and vacancy text, which themselves can be unverified.

## 5. Source retrieval and model robustness

The two adapters provide direct source query URLs and parse published listing cards, but HTML selectors can drift and broad source pages may contain research-staff or unfunded roles. The model system prefers Ollama drafting and Groq fallback; the tests cover rate-limit model fallback, explicit claim correction, Word heading/tables, source text and phone parsing. These unit tests do not constitute verified real-world application or official eligibility validation. A configured Groq key can send CV-derived context outside local environment; verify user consent and data minimization.

## 6. Privacy and security risks

EmailConfig.save stores SMTP username/password in plain JSON, even if gitignored; backups or shared devices may expose it. Attachments default to saved CV and generated documents from the local profile, increasing the need for explicit attachment review. Model fact-check prompts may contain personally identifiable CV text. No external email was sent in this investigation. An application's user-visible 'fact checked' wording must be tied to a successful, parsed verifier result and exact model/source revision.

## 7. Transfer decisions and cross-study relationships

Adopt explicit draft→edit→confirm→send staging, recipient correction, no-send-on-failure, fixed DOCX export and source-specific listing parsers. Reject fail-open fact checking, automatic trust in LLM source claims, plaintext long-lived credentials, and model-confidence acceptance estimates. Compare to the synthetic-professor outreach automator: this agent's contacts come from displayed posts or explicit user input, not randomized fabricated faculty, but still require independent identity and funding confirmation.

## 8. Verdict with source links

DEEP_REVIEW_DOCUMENTED (source-only). Reuse review-first interaction concepts with durable authorization and outbox; do not promote unsupported drafted claims to verified applicant achievements. [README](https://github.com/ratulsaha2021/scholarship-agent/blob/a361d74828722b36fd2cfff1ff96f4cc86e857c4/README.md); [ChatAgent](https://github.com/ratulsaha2021/scholarship-agent/blob/a361d74828722b36fd2cfff1ff96f4cc86e857c4/src/chat_agent.py); [HybridLLM](https://github.com/ratulsaha2021/scholarship-agent/blob/a361d74828722b36fd2cfff1ff96f4cc86e857c4/src/hybrid_llm.py); [tests](https://github.com/ratulsaha2021/scholarship-agent/blob/a361d74828722b36fd2cfff1ff96f4cc86e857c4/tests/test_documents_and_facts.py); [SMTP](https://github.com/ratulsaha2021/scholarship-agent/blob/a361d74828722b36fd2cfff1ff96f4cc86e857c4/src/email_sender.py); [EURAXESS adapter](https://github.com/ratulsaha2021/scholarship-agent/blob/a361d74828722b36fd2cfff1ff96f4cc86e857c4/src/sources/euraxess.py).
