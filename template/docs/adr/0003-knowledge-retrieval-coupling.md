# 3. Knowledge retrieval (scientific corpus) is a coupled module, not template furniture

Date: 2026-06 (template authoring date)

## Status

Accepted. The coupling point (this ADR + the `knowledge_retrieval` flag + a
knowledge-map row) ships now; the retrieval engine itself is under active
development in its own repository and is coupled per project once available. The
coupling is intentionally temporary/per-project — see Decision.

## Context

Some projects need retrieval over a corpus of scientific articles containing
equations, figures, and tables (e.g. systematic-review or methods work). The
initial instinct was "GraphRAG + Query Routing". A focused review (2026-06)
challenged that and produced these findings:

- VERIFIED: for text-and-table documents, a **hybrid** retriever (BM25 + dense)
  is the strongest base; sparse BM25 alone often beats dense (T2-RAGBench, EACL
  2026 / arXiv 2506.12071).
- VERIFIED (correction): the "+17.4% over RRF / +39% over dense" figures we
  previously carried are **misattributed** — the real hybrid-over-base gain is
  modest (~+2.5% MRR, ~+5% absolute). A cross-encoder **reranker HURT** on
  table-heavy data — do not assume it helps; A/B-test it.
- PRIMARY-SOURCE, not vote-verified: **MinerU / VLM extractors** lead on
  scientific-PDF parsing (OmniDocBench, CVPR 2025); evaluate formula extraction
  with **LLM-as-judge semantic equivalence**, not character matching.
  **LazyGraphRAG** (Microsoft, 2024-11-25) claims ~0.1% of full-GraphRAG
  indexing cost and ~700x lower per-query cost — treat as a vendor claim.
  **BenchmarkQED** (MIT) measures local-vs-global query mix to decide if a graph
  is even needed.

## Decision

1. The retrieval **engine lives in its OWN repository** (extracted/evolved from
   `ms-rie-orchestrator`), exposed to the agent as an **MCP server**, and is
   **coupled per project**. It is NOT vendored into this template and NOT placed
   in the `psotobverse-utils` plugin (which must stay domain-free).
2. This template carries only the **coupling stub**: the copier question
   `knowledge_retrieval` (`none` | `hybrid` | `graph`, default `none`), this ADR,
   and a conditional knowledge-map row. With `none`, the project uses directed
   reading via the knowledge-map and nothing else.
3. **Engineering strategy when the engine is built** (escalation ladder, cheapest
   first): hybrid (BM25 + dense, MinerU for multimodal extraction) → add **query
   routing** only when there is more than one query type → add a **graph
   (LazyGraphRAG)** ONLY if a BenchmarkQED-style local-vs-global evaluation shows
   global/multi-hop queries that hybrid fails. Commit the **recipe** (ingestion +
   index config), never the index.
4. Use of any heavy retrieval/verification is governed by
   `.claude/policies/verification-effort.md`.

## Consequences

- The template stays lean; projects that need retrieval attach the module via
  MCP; the engine improves independently and propagates without re-cloning.
- One-time per-project coupling (add the MCP server, set `knowledge_retrieval`).
- Engine internals are deferred to a dedicated build; this ADR is superseded by a
  new ADR once that engine and its measured eval exist.
