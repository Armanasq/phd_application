# abilcode/rag_task_pnu — source, data and evaluation investigation

**Date:** 2026-11-11 · **Commit:** [a1b523940ae9ac23c472c03e559289a07a5de4fa](https://github.com/abilcode/rag_task_pnu/commit/a1b523940ae9ac23c472c03e559289a07a5de4fa) · **State:** PRELIMINARY_FOCUSED

**Verdict:** REFERENCE ONLY — cybersecurity RAG, not a PhD admissions resource. **Risk:** domain_mismatch_weak_retrieval_and_invalid_evaluation.

## Scope and architecture

The README describes a cybersecurity assistant. The runtime has two LangChain agent layers: `MainAgent` uses a conversational ReAct agent with `gpt-4o-mini`, `ConversationBufferMemory`, one tool and a three-iteration cap; `QACycberSecAgent` uses `OpenAIFunctionsAgent`, a tool-enabled prompt, three JSON few-shot examples and a separate manually maintained history truncated to ten messages. The two memory stores have different boundaries. CLI and Gradio both call the same agent; the Gradio layer has an unused `conversation_history` member and reinitializes the agent to clear memory.

## Retrieval and ingestion

`RAGRetriever` loads a committed Chroma database from `./chroma_db` using OpenAI embeddings. General retrieval uses `similarity_search(k=3)`. Topic retrieval expands each topic into six variants and merges results by content hash. There is no score threshold, hybrid search, reranker, metadata filter, source authority model or evidence-entailment check. The builder assigns generic `qa_facts` metadata rather than original source URLs.

`create_chromadb.py` splits `qa_facts.txt` on blank lines, creates documents, then applies 1,000-character chunks with 200-character overlap. It deletes the existing database directory before rebuilding, so an interrupted rebuild can destroy the previous index; there is no atomic index swap or versioned ingestion manifest.

## Data lineage

The data notebook downloads `preemware/pentesting-eval`, writes a CSV, then creates `qa_facts.txt`. The checked-in CSV has 246 data rows; the fact corpus has 1,948 lines and 284,878 characters. The notebook hard-codes 240 rows: 216 training examples and 24 test examples, leaving six rows out of both splits. It uses Python `eval()` to parse choices. The evaluation code repeats `eval()` when choices are strings.

## Evaluation validity

The checked-in report uses 36 examples and records semantic similarity mean `0.0381`, BLEU/ROUGE/term coverage all `0`, completeness `0.7`, mean latency `2.46s` and median latency `1.04s`. The report nevertheless describes semantic understanding as strong. The detailed-results JSON uses a numeric answer label as `ground_truth` while comparing it to natural-language model output, so BLEU/ROUGE and semantic similarity are not valid answer-quality comparisons. Term coverage is also zero because the ground-truth term set is empty. The performance notebook's confidence-word and reasoning-word counts are surface indicators, not calibrated confidence or evidence correctness.

## Engineering findings

- `main.py` still labels the CLI “Hotel Assistant”, indicating domain drift.
- Dependencies pin LangChain 0.0.352 and OpenAI 0.27.8.
- No automated tests cover ingestion, retrieval relevance, tool selection or answer correctness.
- Retrieval failures are returned as free-text error strings rather than typed outcomes.
- The database snapshot is committed, but reproducibility and source provenance are weak.

## Transfer and decision

The reusable ideas are a separate orchestration layer, tool adapters, offline corpus construction and explicit evaluation datasets. Rebuild these with deterministic source manifests, original-source provenance, atomic versioned indexes, safe JSON parsing, retrieval evaluation, evidence checks and task-valid metrics. Do not adopt this repository as an admissions system.

**Inspected:** README, main/QA/evaluation agents, retrieval tools, Chroma builder, CLI/Gradio UI, both notebooks, requirements, `qa_facts.txt`, dataset CSV, evaluation report and detailed results.