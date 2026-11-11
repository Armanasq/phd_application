# MahdiAmrollahi/agentic-rag-persian — Persian doctoral-policy RAG implementation audit

**Review date:** 2026-11-12  
**Repository:** https://github.com/MahdiAmrollahi/agentic-rag-persian  
**Repository ID:** 1288712091  
**Pinned commit:** [066cf74d103084ceb8e9236bcf5062d4686a4ef8](https://github.com/MahdiAmrollahi/agentic-rag-persian/commit/066cf74d103084ceb8e9236bcf5062d4686a4ef8)  
**Review state:** DEEP_REVIEW_DOCUMENTED (notebook architecture and complete computational code static review; PDF body and runtime NOT_TESTED).  
**Verdict:** Reject executable tool dispatch as-is; adapt only lightweight multilingual retrieval and explicit search-before-answer workflow.

## 1. Intended problem and evidence domain

This single-notebook educational project implements a Persian-language ReAct-style retrieval agent over a bundled doctoral admissions call and regulation PDF. It claims to answer factual admission questions, summarize conditions and calculate point totals. The README attributes the default PDF to an Iranian science-and-technology university and describes a professor-directed admission route. That attribution and the PDF's current applicability are **not independently verified** in this pass. This is not a current global admissions dataset, nor a validated admission or eligibility engine.

## 2. Complete source inventory and actual architecture

The pinned tree has exactly three files: README.md (2,841 bytes), agentic_rag_assignment.ipynb (361,680 bytes), and a Persian-named admissions-regulation PDF (313,680 bytes). The notebook has 68 cells: 41 code cells and 27 Markdown cells. No package lockfile, Python tests, CI workflow, external source ledger or LICENSE file was found. GitHub exposed one commit and no issues or pull requests at the inspected revision.

The notebook uses PyMuPDF for text extraction, overlapping character windows (configured around 1,000 characters with 200-character overlap), sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 to embed chunks, scikit-learn cosine similarity over NumPy arrays, and OpenRouter through the OpenAI Python SDK. It uses a plain JSON ReAct prompt to choose between search, summarize, calculator and a final answer.

Despite README installation instructions listing faiss-cpu, the inspected retrieval implementation computes cosine similarities directly; a persistent FAISS index or vector database is not part of the active retrieval code.

Source: [README](https://github.com/MahdiAmrollahi/agentic-rag-persian/blob/066cf74d103084ceb8e9236bcf5062d4686a4ef8/README.md), [complete notebook](https://github.com/MahdiAmrollahi/agentic-rag-persian/blob/066cf74d103084ceb8e9236bcf5062d4686a4ef8/agentic_rag_assignment.ipynb).

## 3. Data and tool flow

PDF pages -> extracted text -> one flat string -> overlapping character chunks -> multilingual embeddings -> cosine-ranked top-k chunks -> search_tool observation -> LLM JSON action -> optional summarizer or calculator -> final_answer.

The search tool returns top-five chunks and similarity scores but drops document page identities and source spans. It concatenates chunks into a free-text observation string. The agent appends each action and observation to a growing prompt-history string. Factual-search-before-answer and calculator-for-arithmetic constraints are imposed **in prompt text only**, not enforced by independent typed state transitions.

The notebook includes fifteen demonstration query cells about minimum GPA, language requirements, research points, eligibility, table summaries and arithmetic. Saved stream outputs are examples, not a supervised validation set with ground-truth citations or blind scoring.

## 4. Critical security and correctness findings

- **Arbitrary evaluation:** The implementation of calculator_tool(expression) directly executes Python eval(expression), where expression is supplied by the LLM action argument. This is a code-execution boundary crossing from untrusted document/user/model text. No sandboxing, AST allowlist or arithmetic parser is implemented. Do not run the agent on untrusted queries/documents in this form.
- **Unbounded agent loop:** agent(question) runs while True, with no per-turn tool/LLM call budget, deadline, repetition detector or fallback. Malformed or adversarial responses may cause uncontrolled cost and latency.
- **Unvalidated tool dispatch:** After parsing a JSON response, the code accesses action["tool"] and action["arg"] and indexes tools[tool_name] without validating the action schema or allowed tool argument types. Invalid JSON/tool names can raise errors, and the model prompt does not guarantee conformance.
- **Retry exception-state defect:** ask_llm(prompt) catches exceptions for ten requests with fixed 15-second sleeps. If every attempt fails, the local variable response is never assigned before the final return statement. There is no bounded exponential backoff, per-request timeout policy, or clear failure signal.
- **No source citations:** Retrieval results contain chunk text and similarity score but no PDF page offsets or exact supporting passages in the final answer contract. A generated regulatory conclusion cannot be independently traced to an original source passage.
- **No freshness or contradiction control:** The source PDF is a single, bundled snapshot. There is no current official URL check, amendment/version handling, conflict resolution, registration deadline verification or applicant-specific eligibility status.

These findings are static. No exploit or remote request was executed.

## 5. Retrieval, multilingual and evaluation limitations

Overlapping character windows can split Persian words, section boundaries and tabular criteria; no page/heading structure survives. The similarity search is not calibrated as a factual confidence score. PDF text extraction quality for Persian/RTL text and embedded tables is not verified in this pass. The top-five-only context can omit distant table footnotes or cross-referenced clauses, and the agent may accumulate redundant chunks across search rounds.

The summarization tool sends retrieved passages to the same model, without a strict separation of untrusted document instructions. The JSON fence-stripping repair helper is tolerant, but does not validate the expected schema or guarantee escape-sequence fidelity. The notebook does not contain a formal corpus-level question/answer evaluation, citation-accuracy measurement, retrieval recall, latency budget, or regression test.

## 6. Privacy, licensing and operational scope

The repository README points to OpenRouter and a free-tier model. No present-day model availability, actual costs or API compatibility were independently tested. The notebook variable containing an API credential was not copied or published here; no external account was accessed. The bundled PDF was not downloaded or reproduced. The existence of a public PDF is not proof of a reuse license or of valid 2026 application policy; its current official source and legal status require checking. The repository has no independent license file.

The code operates as a personal notebook demonstration. It lacks service isolation, applicant authentication, persistence controls, privacy separation, observability and reproducible deployment constraints.

## 7. Comparison and transferable design

Its strength relative to ungrounded LLM answers is an explicit source-search tool and a modest embedding/retrieval stack. A production doctoral-policy agent should retain multilingual preprocessing and model-independent structured tool routing, but replace all unsafe or ambiguous execution boundaries:

1. Replace eval with a deterministic arithmetic expression parser and numeric bounds; keep tool execution isolated.
2. Represent the agent as a finite state machine with typed actions, maximum iterations, deadlines, retries and a clear abstention state.
3. Preserve PDF page number, source URL/edition, passage offsets and content hashes; emit field-level citations.
4. Use robust Persian PDF and table extraction QA, page-aware chunking, duplicate suppression and evaluation fixtures.
5. Separate current official eligibility requirements from old calls and unverified third-party copies; treat missing or contradictory information as UNKNOWN.
6. Validate model and dependency versions, costs, and runtime tests before any use in personal admissions decisions.

Compared with the evidence-aware SihengTao planner and multi-host research-app-toolkit, this notebook demonstrates a minimal tool router but lacks the same operational safeguards; the calculator is specifically unsafe.

## 8. Review decision and empirical boundary

**DEEP_REVIEW_DOCUMENTED — BLOCK executable reuse.** The README, full notebook source and cell organization, 15 demonstration queries, import/dependency path, tool implementations, retrieval, agent loop, and metadata/commit/issue history were inspected. The bundled PDF's text was not independently analyzed and its university attribution remains unverified. No notebook cells, third-party API calls, dependency installation, runtime tests, PDF processing, or vulnerability exploit was performed. This review establishes implementation-level risks, **not** a confirmed answer to any Iranian PhD admissions rule.
