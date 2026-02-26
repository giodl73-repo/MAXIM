# 09 — Embeddings and Vector Search

## The Big Picture

```
  The Embedding and Retrieval Stack
  ====================================

  ┌─────────────────────────────────────────────────────────────────────────┐
  │  DOCUMENTS / DATA SOURCE                                                │
  │  PDFs · web pages · database records · code · emails                   │
  └────────────────────────────┬────────────────────────────────────────────┘
                               │ chunking strategy (fixed/semantic/hierarchical)
  ┌────────────────────────────▼────────────────────────────────────────────┐
  │  CHUNKS                                                                 │
  │  ~512 token text segments with metadata (source, date, section)        │
  └────────────────────────────┬────────────────────────────────────────────┘
                               │ embedding model
  ┌────────────────────────────▼────────────────────────────────────────────┐
  │  DENSE VECTORS                                                          │
  │  float32 or int8 arrays (256–3072 dimensions)                          │
  └────────────────────────────┬────────────────────────────────────────────┘
                               │ ANN index (HNSW / IVF / PQ)
  ┌────────────────────────────▼────────────────────────────────────────────┐
  │  VECTOR INDEX                                                           │
  │  Approximate nearest neighbor structure for sub-linear search           │
  └────────────────────────────┬────────────────────────────────────────────┘
                               │ query time: embed → search → rerank
  ┌────────────────────────────▼────────────────────────────────────────────┐
  │  RETRIEVAL PIPELINE                                                     │
  │  Dense ANN + optional BM25 sparse → reciprocal rank fusion → reranker  │
  └────────────────────────────┬────────────────────────────────────────────┘
                               │
  ┌────────────────────────────▼────────────────────────────────────────────┐
  │  LLM GENERATION                                                         │
  │  Context: [retrieved chunks] + [user query] → grounded response        │
  └─────────────────────────────────────────────────────────────────────────┘
```

---

## Embedding Models

Embedding models convert text (or images) into dense vectors. The geometry of the resulting space encodes semantic similarity.

```
  Major Text Embedding Models (2024)
  ──────────────────────────────────────────────────────────────────────

  OpenAI:
    text-embedding-3-small:    1536 dims, $0.02/1M tokens   — fast, cheap, good
    text-embedding-3-large:    3072 dims, $0.13/1M tokens   — best OpenAI quality
    text-embedding-ada-002:    1536 dims, $0.10/1M tokens   — legacy, still widely used

  Open-source (self-hosted or via Ollama/HuggingFace):
    BGE-M3 (BAAI):             1024 dims, multi-lingual, multi-granularity
                                supports dense, sparse, and multi-vector retrieval
    E5-large-v2 (Microsoft):   1024 dims, strong retrieval benchmarks
    bge-large-en-v1.5:         1024 dims, top MTEB English performance
    mxbai-embed-large-v1:      1024 dims, top MTEB, instruction-following

  Cohere:
    embed-english-v3.0:        1024 dims, native int8 quantization, built-in reranker
    embed-multilingual-v3.0:   1024 dims, 100+ languages

  Dimensions vs. quality tradeoff:
    More dimensions: larger index, more memory, slower search, potentially better
    3072 vs. 1536: marginal quality gain for 2× memory and search time
    Matryoshka Representation Learning (MRL): text-embedding-3-* supports
    truncating to smaller dimensions (e.g., 256) with controlled quality loss
    → truncate to 256 dims for speed-sensitive, low-cost applications
```

### Late Interaction — ColBERT

```
  ColBERT (Khattab & Zaharia, 2020) — Multi-vector retrieval
  ────────────────────────────────────────────────────────────────────

  Standard embedding: entire document → single vector
  Limitation: one vector must represent all document semantics

  ColBERT: each token → its own vector (late interaction)
    Query: q_1, q_2, ..., q_m  →  [v_1, v_2, ..., v_m]  (per-token vectors)
    Doc:   d_1, d_2, ..., d_n  →  [u_1, u_2, ..., u_n]

  Similarity (MaxSim):
    score(q, d) = Σ_i max_j(v_i · u_j)
    Each query token finds its best-matching document token

  Why it's better:
    Single-vector: "bank" averaged with "financial" and "river" loses precision
    ColBERT: the token "bank" in context of "river bank" matches "river" tokens specifically

  Cost:
    Storage: ~128 dims × token_count per document (vs. 1536 dims per chunk)
    A 1M-document corpus at avg 256 tokens = 256M vectors stored
    Inference: MaxSim is an inner product — fast with PLAID indexes

  Use ColBERT when:
    Precision matters more than cost/storage
    Complex multi-concept queries where averaging loses semantics
    Implemented in: RAGatouille library, Vespa, Weaviate (experimental)
```

---

## Vector Similarity Fundamentals

```
  The three similarity metrics you'll actually use:
  ──────────────────────────────────────────────────────────────────────

  Cosine similarity:
    sim(a, b) = (a · b) / (‖a‖ × ‖b‖)
    Range: [-1, 1] (1 = identical direction, 0 = orthogonal, -1 = opposite)
    Measures: directional similarity, magnitude-invariant
    When to use: DEFAULT for most text embeddings
                 Most embedding models produce unit-norm vectors → cosine = dot product

  Dot product:
    sim(a, b) = a · b = Σ_i a_i × b_i
    Range: (-∞, ∞)
    Measures: magnitude + direction
    When to use: embeddings explicitly trained with dot product objective (Cohere embed-v3)
                 When magnitude encodes relevance strength (query-document retrieval)

  L2 / Euclidean distance:
    dist(a, b) = ‖a - b‖ = √(Σ_i (a_i - b_i)²)
    Range: [0, ∞) (lower = more similar)
    When to use: when vectors are NOT normalized
                 K-means clustering on embeddings

  Normalization matters:
    If ‖a‖ = ‖b‖ = 1 (unit norm): cosine = dot product (same thing)
    OpenAI, most BGE/E5 models: produce unit-norm vectors by default
    If unsure: normalize before indexing and use dot product

  Common mistake:
    Using L2 distance with unit-norm vectors "because it's simpler"
    L2 and cosine give different rankings for non-normalized vectors
    For unit-norm: L2² = 2 - 2·cosine (monotonically equivalent, but slower)
```

---

## ANN Algorithms

### HNSW — Hierarchical Navigable Small World

```
  HNSW (Malkov & Yashunin, 2018) — The Standard
  ──────────────────────────────────────────────────────────────────────

  Structure: multi-layer proximity graph

  Layer 0 (densest):  ALL vectors, each connected to M nearest neighbors
  Layer 1:           ~1/ef vectors (random subset)
  Layer 2:           ~1/ef² vectors (sparser)
  ...
  Top layer:         1-2 entry points

  Search:
    Enter at top layer, greedy traverse toward query
    Drop to layer below, greedy traverse
    Continue to layer 0, return top-K

  Why it works:
    Long-range "highways" at upper layers (like highway network routing)
    Local search at layer 0 (like local roads)
    Expected complexity: O(log N) per query

  Key parameters:
    M:    number of connections per node (typical: 16–64)
          Higher M → better recall, more memory, slower build
    ef_construction: beam width during index build (typical: 128–400)
          Higher → better index quality, slower build time
    ef:   beam width at query time (typical: 64–256)
          Higher → better recall, slower query
          ef must be ≥ k (number of results requested)

  Memory per vector:
    ≈ (M × 2 + extra) × 4 bytes per vector
    For M=16, 1.5M vectors: ~200 MB index overhead above raw vector storage

  Used by: pgvector, Qdrant, Weaviate, Pinecone (default for new indexes)
```

### IVF — Inverted File Index

```
  IVF (Inverted File) — Cluster-Based Approximate Search
  ──────────────────────────────────────────────────────────────────────

  Build:
    K-means cluster all vectors into nlist clusters (typical: 1000–4096)
    Each vector assigned to its nearest centroid
    Build inverted list: centroid_id → [vector_ids]

  Search:
    Embed query
    Find nprobe nearest centroids (nprobe < nlist, typically 32–128)
    Search only vectors in those nprobe clusters
    Return top-K across all searched clusters

  Accuracy vs. speed tradeoff:
    nprobe = 1:       fast, low recall
    nprobe = nlist:   exact search (defeats the purpose)
    nprobe = nlist/8: good recall (>95%) at 8× speedup

  Memory: compact — just vector data + centroid assignments
  vs. HNSW: IVF uses less memory but has worse recall at same speed

  When to use IVF over HNSW:
    Memory-constrained (IVF is more compact)
    Very large datasets (> 100M vectors) where HNSW memory is prohibitive
    When recall > 95% is not required
```

### PQ — Product Quantization

```
  Product Quantization — Compress Vectors
  ──────────────────────────────────────────────────────────────────────

  Problem: 1M vectors × 1536 dims × 4 bytes = 6 GB just for raw vectors

  PQ: compress each vector from d dimensions to a short code

  Method:
    Split d-dim vector into m subvectors of d/m dims each
    Quantize each subvector to nearest centroid (k = 256 centroids per sub)
    Store: m bytes per vector (1 byte = centroid index per subvector)

  Example:
    1536-dim, m=96 subspaces → 16-dim each, k=256 → 96 bytes per vector
    Compression: 1536 × 4 = 6144 bytes → 96 bytes = 64× reduction
    Quality: approximate distance computation via lookup table

  IVFPQ = IVF + PQ:
    Cluster with IVF, compress residuals with PQ
    Used by: Faiss (Facebook's vector search library, the foundational impl)
    Practical: billions of vectors on a single machine

  ScaNN (Google): similar idea with better distance approximation
```

---

## Vector Databases

```
  Vector Database Comparison
  ──────────────────────────────────────────────────────────────────────

  ┌──────────────┬───────────────────────────────────────────────────────┐
  │  pgvector    │  PostgreSQL extension                                 │
  │              │  HNSW + IVF indexes (v0.5+ supports HNSW)            │
  │              │  SQL-native: JOIN, filter, transaction semantics      │
  │              │  Exact and approximate search                         │
  │              │  Azure Database for PostgreSQL supports it natively   │
  │              │  Best for: already have Postgres; moderate scale      │
  │              │  Scale: up to ~10M vectors on one Postgres instance   │
  └──────────────┴───────────────────────────────────────────────────────┘
  ┌──────────────┬───────────────────────────────────────────────────────┐
  │  Pinecone    │  Managed, serverless or pod-based                     │
  │              │  Proprietary ANN algorithm (optimized for recall)     │
  │              │  Serverless: pay per query, auto-scale               │
  │              │  Native hybrid search (dense + sparse)               │
  │              │  Best for: teams that want zero ops; enterprise SaaS  │
  │              │  Cost: serverless ~$0.08/1M query units              │
  └──────────────┴───────────────────────────────────────────────────────┘
  ┌──────────────┬───────────────────────────────────────────────────────┐
  │  Weaviate    │  Open-source, cloud-managed available                 │
  │              │  HNSW index                                           │
  │              │  Hybrid search: native BM25 + vector                 │
  │              │  GraphQL and REST API                                 │
  │              │  Modules: text2vec, qna, generative                  │
  │              │  Best for: hybrid search; GraphQL preference         │
  └──────────────┴───────────────────────────────────────────────────────┘
  ┌──────────────┬───────────────────────────────────────────────────────┐
  │  Qdrant      │  Open-source, Rust, strong payload filtering          │
  │              │  HNSW + scalar quantization                          │
  │              │  Efficient filtered search (filter before ANN)       │
  │              │  Named vectors (multiple per point)                  │
  │              │  Best for: metadata-rich filtering + vector search   │
  └──────────────┴───────────────────────────────────────────────────────┘
  ┌──────────────┬───────────────────────────────────────────────────────┐
  │  Milvus      │  Open-source, distributed, enterprise                 │
  │              │  Multiple index types (HNSW, IVF, PQ, GPU indexes)  │
  │              │  Scale: billions of vectors across cluster           │
  │              │  Zilliz Cloud: managed Milvus                       │
  │              │  Best for: massive scale; on-prem enterprise         │
  └──────────────┴───────────────────────────────────────────────────────┘
  ┌──────────────┬───────────────────────────────────────────────────────┐
  │  Chroma      │  Open-source, embedded (in-process) or server mode   │
  │              │  Simple Python API                                    │
  │              │  No persistence tuning needed                        │
  │              │  Best for: local prototyping, small-scale RAG POC   │
  └──────────────┴───────────────────────────────────────────────────────┘
```

---

## Hybrid Search

```
  Hybrid Search — Dense + Sparse Combined
  ──────────────────────────────────────────────────────────────────────

  Problem with pure dense (vector) search:
    Great for semantic similarity ("what does this mean?")
    Poor for exact term matching ("find 'SQL Server 2019 CU17' specifically")
    Technical terms, proper nouns, code identifiers often not well-embedded

  Problem with pure sparse (BM25/TF-IDF) search:
    Great for keyword matching
    Poor for semantic similarity ("car" vs "automobile" → no match)
    Misses paraphrase and conceptual similarity

  BM25 recap (the standard sparse retrieval algorithm):
    Score(D, Q) = Σ_q IDF(q) × (f(q,D) × (k+1)) / (f(q,D) + k × (1 - b + b×|D|/avgdl))
    IDF: inverse document frequency — rare terms score higher
    f(q,D): term frequency in document
    k, b: tuning parameters (typical: k=1.2, b=0.75)
    Same conceptual foundation as SQL Server Full-Text Search

  Hybrid fusion: combine dense and sparse rankings
  ─────────────────────────────────────────────────
  Method 1: Reciprocal Rank Fusion (RRF) — the standard
    For each document, from each ranking:
      score_rrf = Σ_r 1 / (k + rank_r(d))   where k=60 is typical
    Sum across dense and sparse rankings
    Re-sort by combined RRF score
    Advantage: rank-based, doesn't require score normalization

  Method 2: Weighted linear combination
    score_hybrid = α × score_dense + (1-α) × score_sparse
    Requires normalizing scores to same scale (tricky)
    α typically 0.6–0.8 (favor dense) for general QA

  When hybrid beats pure dense:
    ✅ User queries contain specific names, IDs, technical terms
    ✅ Domain has controlled vocabulary (medical, legal, finance)
    ✅ Short documents (little context for embedding model to work with)
    ✅ Users expect keyword matching alongside semantic search

  Native hybrid search support:
    Weaviate, Pinecone: built-in
    Qdrant, pgvector: bring your own BM25 (Elasticsearch or custom)
    Azure Cognitive Search: native hybrid since 2023 with semantic reranker
```

---

## Chunking Strategy

```
  Chunking: How You Split Documents Matters More Than Choice of VectorDB
  ──────────────────────────────────────────────────────────────────────────

  Fixed-size chunking:
    Split at every N tokens, overlap by O tokens
    N=512, O=64 is a common baseline
    Simple, reproducible, no dependencies
    Problem: splits mid-sentence, mid-concept

  Sentence / paragraph chunking:
    Split at sentence boundaries (spaCy, NLTK sentence tokenizer)
    Respects natural language units
    Variable chunk size (20–800 tokens)
    Problem: long paragraphs may exceed context; short sentences lose context

  Hierarchical (parent-document retrieval):
    Index: small child chunks (128 tokens) → precise retrieval
    Store: parent chunks (512 tokens) → full context for generation
    At retrieval: find child chunk, return parent chunk to LLM
    Best for: long documents where precise retrieval matters

  Semantic chunking:
    Embed every sentence
    Split where cosine similarity between adjacent sentences drops
    Produces topic-coherent chunks
    Cost: embed every candidate split point
    Best for: high-value corpora, research documents

  Structural chunking:
    Use document structure: Markdown headers, HTML tags, PDF sections
    Keep section + subsection text together
    Best for: structured documents (wikis, manuals, code)

  Metadata augmentation:
    Add chunk_id, source, date, section, parent_chunk_id to each vector
    Enable pre-filtering: only search chunks from [specific document]
    Critical for multi-tenant applications
```

---

## Reranking

```
  Reranking — Why the First-Pass ANN Retrieval Isn't the Final Answer
  ──────────────────────────────────────────────────────────────────────

  ANN retrieval returns top-K candidates quickly (milliseconds)
  Reranking re-scores those K candidates more accurately (slower)

  Why bi-encoder (ANN) ≠ cross-encoder quality:
    Bi-encoder: embed query and document independently → dot product
    Cross-encoder: see BOTH query and document together → richer interaction
    Cross-encoder: much slower (can't pre-compute), much more accurate

  Cross-encoder reranking pipeline:
    1. ANN retrieval: top-100 candidates in <10ms
    2. Cross-encoder reranking: score all 100 with (query, chunk) pairs
       Typically 100–200ms for 100 candidates
    3. Return top-5 to LLM

  Reranking models:
    Cohere Rerank:       managed API, strong multilingual
    bge-reranker-large:  open-source, strong English quality
    ms-marco-MiniLM-L6:  fast, lighter weight, good quality
    LLM-as-reranker:     ask GPT-4/Claude to rank chunks by relevance
                         most accurate but expensive (full token cost per chunk)

  ColBERT as reranker:
    Late interaction model
    Faster than cross-encoder (token-level MaxSim, precomputed doc vectors)
    Better than bi-encoder quality
    Positioned between bi-encoder speed and cross-encoder quality

  When to add a reranker:
    Precision matters more than latency (research, legal, compliance)
    Your ANN retrieval recall is good but precision is poor
    Budget for +100-200ms latency per query
```

---

## The Full RAG Pipeline

```
  End-to-End RAG Architecture
  ──────────────────────────────────────────────────────────────────────

  OFFLINE (ingestion):
  Documents
    → loader (LangChain, LlamaIndex, Unstructured.io)
    → chunker (strategy per document type)
    → [metadata enrichment: title, date, section, summary]
    → embedding model (text-embedding-3-large or BGE)
    → vector DB upsert (+ optional BM25 index)

  ONLINE (query):
  User query
    → [query rewriting: hypothetical document embedding, HyDE]
    → embed query
    → ANN search → top-100 dense candidates
    → [BM25 search → top-100 sparse candidates]
    → [RRF fusion → merged ranking]
    → reranker (cross-encoder) → top-5 chunks
    → prompt assembly:
        "Use the following context to answer the question.
         Context: [chunk_1] [chunk_2] [chunk_3] [chunk_4] [chunk_5]
         Question: {user_query}
         Answer:"
    → LLM generation
    → [citation extraction: which chunks were used?]

  Advanced patterns:
    HyDE (Hypothetical Document Embedding):
      Generate a hypothetical answer → embed it → use as query vector
      Better retrieval for factual questions
      Cost: one LLM call before retrieval

    Query decomposition:
      Complex question → sub-questions → retrieve for each → merge
      Better for multi-hop reasoning

    Iterative retrieval:
      Generate partial answer → identify gaps → retrieve again
      Used in: RAG-Fusion, FLARE, Self-RAG
```

---

## Old World → New World Bridges

```
  SQL Full-Text Search (FTS)          Vector / hybrid search
  ──────────────────────────────────────────────────────────────
  CONTAINS(column, '"exact term"')  →  BM25 sparse retrieval
  FREETEXT(column, 'semantic query')→  Dense vector retrieval
  No conceptual equivalent          →  Semantic similarity (cosine)
  Ranking via relevance score       →  ANN search + RRF fusion
  Index: FTS catalog (.fdx, .fdt)   →  Vector index (HNSW, IVF)
  Query planner chooses index       →  nprobe / ef controls recall

  Azure Cognitive Search (now Azure AI Search)
  ──────────────────────────────────────────────────────────────
  Keyword search                    →  BM25 (unchanged)
  Semantic search (GA 2021)         →  Re-ranking via cross-encoder
  Vector search (GA 2023)           →  HNSW on dense embeddings
  Hybrid search                     →  Native RRF fusion
  Semantic ranker                   →  Cross-encoder on top of hybrid
  Azure AI Search is the Azure-native path for production RAG
  — you already have licensing, compliance, and familiarity
```

---

## Common Confusion Points

**Embeddings encode meaning, not facts.**
An embedding of "Paris is the capital of France" is not a knowledge lookup. The vector represents the semantic space of the sentence. If you ask "what is the capital of France?" the embedding is similar to the sentence above, which is why cosine search retrieves it. The LLM then reads the retrieved chunk and answers. Embeddings are retrieval, not storage of facts.

**More dimensions is not always better.**
text-embedding-3-large (3072 dims) outperforms text-embedding-3-small (1536 dims) by ~5% on MTEB benchmarks. But 3072-dim vectors cost 2× more storage and slower ANN search. For most production RAG, 1536 dims is sufficient. Consider Matryoshka truncation to 512 or 256 dims if latency is critical.

**HNSW recall is not 100% and does not scale down gracefully.**
HNSW with ef=64 typically achieves 95-99% recall. The 1-5% missed documents can be the critical answer. For compliance, medical, or legal use cases where missing a document is unacceptable, consider: exact search (pgvector), higher ef (slower but better recall), or BM25 + ANN hybrid (sparse search finds exact matches that ANN misses).

**Chunking strategy dominates retrieval quality more than vector DB choice.**
Switching from Chroma to Pinecone on the same poorly-chunked corpus will not fix your recall. The chunking strategy — how you split documents — is the highest-leverage decision in your RAG pipeline. Good chunking with pgvector outperforms bad chunking with Pinecone.

**Azure AI Search is not an inferior alternative for Azure shops.**
Azure AI Search supports native hybrid search (BM25 + HNSW), semantic reranking, and integrates with Azure AD, Private Link, and Azure OpenAI. If you're deploying on Azure, the compliance posture and ecosystem integration often outweigh the raw benchmark gap vs. Pinecone.

---

## Decision Cheat Sheet

| I need to... | Use |
|---|---|
| Start a RAG prototype quickly | Chroma (local) or pgvector (if Postgres exists) |
| Production RAG on Azure | Azure AI Search with hybrid mode |
| Managed vector search, zero ops | Pinecone serverless |
| Filtered search (metadata-heavy) | Qdrant (excellent pre-filter support) |
| Billions of vectors, on-prem | Milvus or Faiss-based custom |
| Exact + approximate in same DB | pgvector (supports both modes) |
| Hybrid search out of the box | Weaviate or Pinecone or Azure AI Search |
| Best retrieval quality | ColBERT (via RAGatouille) + reranker |
| Speed-sensitive embedding | text-embedding-3-small at 512 dims (Matryoshka) |
| Best English retrieval quality | BGE-M3 or text-embedding-3-large |
| Reranking top-100 to top-5 | Cohere Rerank API or bge-reranker-large |
| Search images by text | CLIP / SigLIP embeddings |
| Reduce embedding storage 8× | INT8 quantization (Cohere embed-v3 native) |
