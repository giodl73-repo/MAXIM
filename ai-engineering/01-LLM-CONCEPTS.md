# 01 — LLM Concepts

## The Big Picture

```
What an LLM Actually Is
========================

  A large language model is a probability distribution over token sequences:

    P(t_n | t_1, t_2, ..., t_{n-1})

  Given a sequence of tokens, predict the next one.
  Trained to maximize log-likelihood of next-token prediction over a corpus.
  Everything else — reasoning, code generation, instruction following — is
  emergent behavior from scale applied to this simple objective.

  The architecture: Transformer (Vaswani et al., 2017)
  The training regime: pre-training + RLHF / DPO / SFT alignment
  The deployment interface: completion API or chat API
```

```
The LLM Stack — Layers You Interact With
==========================================

  ┌─────────────────────────────────────────────────────────────┐
  │  Your application                                           │
  │  System prompt + user messages + context                    │
  ├─────────────────────────────────────────────────────────────┤
  │  API (OpenAI / Anthropic / Azure OpenAI / Bedrock / etc.)   │
  │  - Model selection                                          │
  │  - Sampling parameters (temperature, top_p, etc.)          │
  │  - Token limits, rate limits, cost                          │
  ├─────────────────────────────────────────────────────────────┤
  │  Inference infrastructure                                   │
  │  - KV cache                                                 │
  │  - Batching, speculative decoding                           │
  │  - Quantization                                             │
  ├─────────────────────────────────────────────────────────────┤
  │  Model weights (frozen after training)                      │
  │  - Pre-trained on internet-scale corpus                     │
  │  - Fine-tuned (SFT) on instruction-following examples       │
  │  - Aligned (RLHF / DPO) on human preference data           │
  └─────────────────────────────────────────────────────────────┘
```

---

## Tokens — The Fundamental Unit

Everything in an LLM operates on tokens, not characters or words. Understanding tokenization explains a range of surprising model behaviors.

### Byte-Pair Encoding (BPE)

```
BPE algorithm (Sennrich et al. 2015, adopted by GPT family):
  Start: vocabulary = individual bytes (256 entries)
  Repeat until target vocab size (50k–100k):
    Count all adjacent token pairs in corpus
    Merge the most frequent pair into a single new token
  Result: frequent subwords become single tokens

Examples (GPT-4 tokenizer):
  "tokenization"   → ["token", "ization"]       2 tokens
  "untokenizable"  → ["un", "token", "izable"]  3 tokens
  " Hello"         → [" Hello"]                 1 token (leading space matters)
  "hello"          → ["hello"]                  1 token
  "HELLO"          → ["HE", "LLO"]             2 tokens (different case = different token)
  "12345"          → ["123", "45"]             2 tokens (numbers vary)
  "1+1=2"          → ["1", "+", "1", "=", "2"] 5 tokens
```

```
Why tokens matter for applications:

  Counting and arithmetic:
    "How many letters in 'strawberry'?"
    Model sees ["str", "awberry"] — the letter boundaries don't align with tokens
    Early models got this wrong; newer models use chain-of-thought to work around it

  Whitespace sensitivity:
    " Python" ≠ "Python" — different tokens, different probabilities
    Prompt formatting affects token sequences, which affects outputs

  Cost:
    ~4 chars/token for English prose (rule of thumb)
    Code is token-denser (more symbols, less common subwords)
    100k token context window ≈ 400k characters ≈ ~300 pages of text

  Tokenizer matters:
    GPT-4: cl100k_base (100k vocab)
    Claude: similar BPE, different vocabulary
    Llama: SentencePiece with 32k vocab (less efficient for English)
    Different tokenizers = different token counts for same text
```

### Context Window

```
The context window is the maximum sequence length the model can attend to.
Everything outside the window is invisible — hard truncation, not fading memory.

  GPT-4o:         128k tokens   (~100k words, ~300 pages)
  Claude 3.5:     200k tokens   (~150k words, ~450 pages)
  Gemini 1.5 Pro: 1M tokens
  Llama 3.1:      128k tokens

Performance degrades within the window:
  "Lost in the middle" effect (Liu et al. 2023):
  Models recall content at the beginning and end of context better
  than content buried in the middle. For RAG and long-context tasks,
  placement of critical information matters.

  Prefill vs decode:
    Prefill: process all input tokens in parallel (fast, O(n) compute)
    Decode: generate output tokens one at a time (slow, sequential)
    Long contexts are expensive in decode because of KV cache size
```

---

## The Transformer Architecture

The MIT TCS framing: a Transformer is a sequence-to-sequence function that applies learned attention to weighted sums of value vectors. The theory you need to understand modern LLMs.

### Attention — The Core Operation

```
Scaled dot-product attention:

  Attention(Q, K, V) = softmax(QK^T / √d_k) V

  Q: queries    (what am I looking for?)
  K: keys       (what do I have?)
  V: values     (what do I return if matched?)
  d_k: key dimension (√d_k scaling prevents softmax saturation)

  For a sequence of n tokens:
    Q, K, V ∈ ℝ^{n × d}
    QK^T ∈ ℝ^{n × n}  — attention matrix, all-pairs similarity
    After softmax: each row sums to 1 (a probability distribution over positions)
    Output: weighted sum of V rows

  Quadratic complexity: O(n²) in sequence length
    This is why long contexts are expensive
    Flash attention: IO-aware tiling reduces memory, same math
    Linear attention variants: approximate attention in O(n) — active research
```

### Multi-Head Attention

```
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) W^O

  head_i = Attention(QW_i^Q, KW_i^K, VW_i^V)

  Each head learns a different attention pattern:
    Head 1 might track syntactic dependencies
    Head 2 might track coreference
    Head 3 might track positional relationships
  The linear combination of heads = richer representation than any single head
```

### The Full Transformer Block

```
Transformer layer (repeated L times):

  x → LayerNorm → MultiHeadAttention → residual add
    → LayerNorm → FFN (feed-forward network) → residual add

  FFN nonlinearity — what changed since the original paper:
    FFN(x) = max(0, xW_1 + b_1)W_2 + b_2    (ReLU, 2017 original — now obsolete)
    FFN(x) = SiLU(xW_1) ⊙ (xW_3) W_2        (SwiGLU, Llama/Mistral/Gemma/modern)

  SwiGLU adds a gating projection W_3 — three weight matrices instead of two.
  Net effect: ~33% more FFN parameters for the same d_ff; typically shrink d_ff
  to compensate. SwiGLU trains faster and achieves better perplexity than ReLU
  at the same total parameter count. This is why modern models outperform same-size
  ReLU variants despite identical depth.

  Pre-LN (LayerNorm before attention/FFN) is now standard vs. original Post-LN.
  Pre-LN stabilizes training at large scale — Post-LN requires warm-up scheduling
  to prevent early-layer gradient explosion.

Parameter count formula (dense transformer, approximate):
  d_model: hidden dimension (e.g., 4096 for 7B, 8192 for 70B, 12288 for GPT-3)
  d_ff:    FFN dimension (~2.67× d_model for SwiGLU; ~4× for ReLU)
  L:       number of layers

  Embedding params:   vocab_size × d_model     (shared input/output in most models)
  Attention per layer: 4 × d_model²            (Q, K, V, O projections)
  FFN per layer:       ~8 × d_model²            (SwiGLU: 3 projections × ~2.67× d_model)
  Total params ≈ 12 × L × d_model²             (rough: attention + FFN dominate)

  Llama-3-8B:  d_model=4096, L=32  → 32 × 12 × 4096² ≈ 6.4B (excl. embedding)
  GPT-3 175B:  d_model=12288, L=96 → 96 × 12 × 12288² ≈ 175B ✓
```

### Positional Encoding

Attention is permutation-equivariant without positional information (the attention matrix treats all positions symmetrically). Positional encoding breaks the symmetry.

```
Absolute (original): add fixed sinusoidal vectors to token embeddings
  sin(pos / 10000^{2i/d}) for even dimensions
  cos(pos / 10000^{2i/d}) for odd dimensions

Rotary Position Embedding (RoPE — GPT-NeoX, Llama, Mistral, modern default):
  Rotate Q and K vectors by an angle proportional to position
  Dot product QK^T naturally encodes relative position (angle difference)
  Extends to longer contexts more gracefully than absolute
  Can be extended via positional interpolation / YaRN for context extension

ALiBi (Press et al. 2021): add position-dependent bias to attention logits
  Simple, training-free length generalization
  Used in: MPT, BLOOM

NoPE (some architectures): no explicit positional encoding
  Relies on attention patterns + causal masking to encode position
  Debated — seems to work at scale despite the theory concern
```

---

## Training — Pre-training → Alignment

### Pre-training

```
Objective: next-token prediction (autoregressive LM)

  Loss = -Σ log P(t_i | t_1, ..., t_{i-1})

  Data: filtered internet text + books + code + specialized corpora
  Scale: GPT-3 = 300B tokens; Llama 3 = 15T tokens; GPT-4 = estimated 10T+
  Compute: GPT-4 estimated ~$100M training run
  Hardware: 1k–10k H100/A100 GPUs, 2–6 months

  What pre-training produces:
    A model that completes text plausibly
    Latent knowledge extracted from corpus
    NOT an assistant — will complete "How do I make a bomb?" with instructions
```

### Alignment

Getting from "text completer" to "helpful, harmless, honest assistant":

```
Step 1: Supervised Fine-Tuning (SFT)
  Dataset: (prompt, ideal response) pairs written by human contractors
  Training: standard LM fine-tuning on response tokens only
  Result: model that follows instruction format
  Problem: doesn't capture nuanced human preferences about quality

Step 2: Reward Model Training
  Dataset: same prompt, two model responses, human preference label
  Training: binary classifier — which response is better?
  Result: a model R(prompt, response) ∈ ℝ scoring response quality

Step 3: RLHF (Reinforcement Learning from Human Feedback)
  Use PPO to maximize R while staying close to SFT model (KL penalty)
  KL penalty prevents reward hacking (mode collapse to high-reward gibberish)
  Complex, unstable training

Step 3 (alternative): DPO (Direct Preference Optimization)
  Reframes RLHF as a direct optimization on preference pairs
  No explicit reward model, no RL training loop
  More stable, simpler, similar or better results
  Now the dominant alignment technique (2023+)

Step 3 (alternative): Constitutional AI (Anthropic's approach)
  Model critiques and revises its own outputs against a set of principles
  Reduces need for human preference labels
  Used for Claude's alignment
```

---

## Inference — Sampling and Decoding

### Temperature and Sampling

```
At each decoding step, the model outputs logits z ∈ ℝ^|vocab|

Softmax: p_i = exp(z_i / T) / Σ exp(z_j / T)
  T = temperature
  T → 0: argmax decoding (greedy, deterministic)
  T = 1: sample from the model's distribution
  T > 1: flatter distribution, more random
  T < 1: sharper distribution, more deterministic

top_p (nucleus sampling):
  Sort tokens by probability descending
  Keep smallest set whose cumulative probability ≥ p
  Sample from that set
  p = 0.9: dynamic vocabulary size, adapts to distribution shape
  More principled than top_k for variable distributions

top_k:
  Keep k highest probability tokens, sample from them
  k = 1: greedy
  Less principled than top_p (k=50 is very different for flat vs sharp distributions)

Practical guidance:
  Factual retrieval, code, structured output: low temperature (0.0–0.3)
  Creative writing, brainstorming: higher temperature (0.7–1.0)
  Never use high temperature for structured output (JSON, etc.) — use json_mode
```

### KV Cache

```
KV Cache — the critical inference optimization
===============================================

  Autoregressive decoding: generate one token at a time
  Each new token needs attention over all previous tokens
  Naively: recompute K and V for all previous tokens at every step

  KV cache: store K and V tensors from all previous tokens
  At each new token: only compute Q for new token, reuse cached K and V
  Memory: O(n × layers × d_model × 2) per sequence
  For Llama-7B, 4k context: ~800MB per sequence — significant at scale

  Implications for LLM serving:
    Throughput is limited by KV cache memory, not compute
    Paged attention (vLLM): manages KV cache like virtual memory
    Batch size limited by total KV cache that fits in GPU memory

  Prompt caching (API feature):
    Providers (Anthropic, OpenAI) cache the KV state of the system prompt
    If the same system prompt prefix is reused, prefill is free
    Critical for: chatbots with long system prompts, document Q&A
    Can reduce latency by 80% and cost by 90% for long-context use cases
```

### Speculative Decoding

```
Speculative decoding (Chen et al. 2023):
  Problem: large model generates tokens slowly (memory bandwidth bound)
  Solution: use a small draft model to generate k tokens speculatively
            large model verifies all k tokens in one forward pass (parallel)
            Accept tokens up to first disagreement, reject the rest

  Speedup: 2–3× on typical text generation
  Requirement: draft model must be compatible in vocabulary and distribution
  Used by: Google (Gemini), Anthropic (Claude), increasingly standard
```

---

## Context Engineering

The term "prompt engineering" undersells what's actually happening. You're constructing the input context that conditions the model's distribution.

If you've built with dependency injection frameworks (Spring, ASP.NET Core, Guice, any IoC container), the mental model transfers directly:

```
DI / IoC pattern          Context engineering equivalent
──────────────────        ────────────────────────────────────────────────
DI container config   →   System prompt (stable config assembled at startup;
                           injected into every request; sets capabilities,
                           persona, constraints, output format)

Runtime-resolved deps →   Retrieved documents (RAG results fetched at request
                           time based on the specific query; analogous to
                           resolving a repository or service at runtime
                           rather than wiring it statically)

Composed execution    →   Full messages array (system + history + retrieved
  context                  docs + tool outputs + current task; the assembled
                           execution context the model reasons over)
```

The model has no global state — everything it knows about the current request is in the messages array, the same way a stateless service has everything it needs injected into the request scope. "Memory" in LLM apps is just retrieval + injection, the same way a stateless service "remembers" per-request context via DI scope.

### The Context Window as Working Memory

```
System prompt      → stable instructions, persona, constraints
Conversation hist. → what was said (within window limit)
Retrieved docs     → RAG results (see below)
Tool outputs       → results from function calls
Current task       → the immediate request

All of this is just text. The model has no memory beyond the context window.
"Memory" in LLM apps = retrieval + context injection.
```

### Prompting Patterns

```
Zero-shot:
  Just the task. No examples.
  "Classify this review as positive or negative: ..."

Few-shot:
  Task + k examples before the actual input.
  "Review: Great product! → Positive
   Review: Total waste of money. → Negative
   Review: It's okay I guess. → ?"
  In-context learning: model learns the task from examples without weight update

Chain-of-thought (CoT):
  Elicit intermediate reasoning steps before the final answer.
  "Let's think step by step..."
  Dramatically improves multi-step reasoning tasks
  Works because tokens generated mid-chain condition subsequent tokens

ReAct (Reason + Act):
  Interleave reasoning traces with tool calls
  Thought: I need to look up X
  Action: search("X")
  Observation: [search results]
  Thought: Given these results, the answer is...
  This is the backbone of most agent frameworks (03-ORCHESTRATION, 04-AGENTS)

Structured output:
  Constrain output to JSON / XML / specific format
  Options: json_mode API parameter, tool_use with a single tool,
           grammar-constrained decoding (llama.cpp, Outlines library)
```

### RAG — Retrieval-Augmented Generation

```
RAG Architecture
=================

  Query
    ↓
  Embed query → dense vector (e.g., text-embedding-3-large)
    ↓
  Vector search → top-k similar chunks from index
    ↓
  Augment prompt with retrieved chunks:
    "Using only the following context, answer the question:
     [chunk 1]
     [chunk 2]
     [chunk 3]
     Question: ..."
    ↓
  LLM generates grounded answer

  Why RAG:
    Keeps model knowledge current (no retraining for new documents)
    Reduces hallucination (model can cite specific source text)
    Scales to large corpora (millions of docs, only fetch relevant)
    Cheaper than fine-tuning

  RAG components:
    Ingestion:  document → chunks → embeddings → vector store
    Retrieval:  query → embedding → ANN search → top-k chunks
    Generation: prompt assembly → LLM → response + citations

  Chunking strategies — tradeoff matrix:

  ┌──────────────────┬──────────────────┬──────────────────────┬──────────────────┐
  │ Strategy         │ Quality          │ Cost/Complexity      │ When to use      │
  ├──────────────────┼──────────────────┼──────────────────────┼──────────────────┤
  │ Fixed size       │ Low — cuts mid-  │ Fastest, cheapest,   │ Baseline / proof │
  │ (512 tokens)     │ sentence, misses │ zero dependencies    │ of concept;      │
  │                  │ semantic bounds  │                      │ uniform docs     │
  ├──────────────────┼──────────────────┼──────────────────────┼──────────────────┤
  │ Sentence /       │ Medium — respects│ Fast; sentence       │ Prose documents  │
  │ paragraph        │ natural breaks,  │ tokenization adds    │ (articles, PDFs, │
  │                  │ variable chunk   │ minor overhead       │ support tickets) │
  │                  │ size             │                      │                  │
  ├──────────────────┼──────────────────┼──────────────────────┼──────────────────┤
  │ Hierarchical     │ High — retrieves │ 2× index size;       │ Long documents   │
  │ (parent/child)   │ child chunk,     │ more complex         │ with structure   │
  │                  │ injects parent   │ retrieval logic      │ (manuals, books, │
  │                  │ for full context │                      │ legal contracts) │
  ├──────────────────┼──────────────────┼──────────────────────┼──────────────────┤
  │ Semantic         │ Highest — splits │ Expensive: embed     │ High-value       │
  │ (embed + cluster │ at embedding     │ every candidate      │ corpora where    │
  │  similarity)     │ similarity breaks│ split point          │ retrieval        │
  │                  │                  │                      │ precision matters│
  └──────────────────┴──────────────────┴──────────────────────┴──────────────────┘

  Decision tree:
    Prototype / quick PoC?           → Fixed size (512 tokens, 64 overlap)
    Production prose documents?      → Sentence splitter
    Long structured docs?            → Hierarchical (parent/child)
    Maximum retrieval quality?       → Semantic chunking
    Mixed structure (PDF, HTML, MD)? → Structure-aware + sentence splitter
    LLM budget for metadata?        → Add QuestionsAnsweredExtractor (LlamaIndex)

  Always add chunk overlap (10% of chunk size) to avoid losing context at boundaries.
```

---

## Fine-Tuning vs Prompting

```
When to fine-tune vs when to prompt:

  Prompting (few-shot / RAG):
    ✅ Task changes frequently
    ✅ Limited training data
    ✅ Need to use latest model versions
    ✅ Quick iteration
    ✅ Transparent (behavior visible in prompt)
    ❌ Long repeated instructions burn context tokens (cost)
    ❌ Complex style/format hard to maintain consistently

  Fine-tuning (SFT on your data):
    ✅ Consistent style/format/persona at scale
    ✅ Compress long system prompts into model weights
    ✅ Domain-specific vocabulary / jargon
    ✅ Latency-sensitive (shorter prompts)
    ❌ Requires 100–10,000+ quality examples
    ❌ Model snapshot — doesn't update with new information
    ❌ Debugging is harder (behavior in weights, not visible)
    ❌ Doesn't help with knowledge cutoff (use RAG for that)

  PEFT (Parameter-Efficient Fine-Tuning):
    LoRA: train low-rank decomposition matrices ΔW = AB^T added to frozen W
          Rank r << d_model → 1% of parameters, ~90% of full fine-tune quality
          Used via: HuggingFace PEFT, Axolotl, LLaMA-Factory
    QLoRA: LoRA + quantized base model (4-bit) → fine-tune large models on consumer GPUs
```

The fine-tuning workflow maps directly to the software build/test/release cycle:

```
Software CI/CD                    Fine-tuning equivalent
──────────────────────────────    ─────────────────────────────────────────────
Test suite                    →   Training + eval dataset
  (inputs + expected outputs)       (prompts + ideal completions)

Build artifact                →   Fine-tuned model checkpoint
  (compiled binary, docker image)   (adapter weights or full model weights)

Quality gate / SLO            →   Eval metric threshold
  (test pass rate, error budget)    (task-specific score vs. baseline)

Canary deploy → measure →     →   Fine-tune → eval → iterate
  roll back or promote              (same loop: measure before promoting)

CI/CD pipeline                →   MLOps pipeline
  (GitHub Actions, Azure DevOps)    (HuggingFace AutoTrain, Azure ML, Vertex AI)
```

LoRA has an exact structural analog in OOP: the **Adapter pattern**. The frozen base
model is a stable, expensive-to-change interface (like a third-party library or a
legacy service boundary). The LoRA adapter matrices (A and B, rank r << d_model)
are the lightweight specialization layer that sits in front of it — they augment
behavior without touching the underlying implementation. Swapping LoRA adapters is
the equivalent of swapping adapter implementations: same stable base, different
behavior profiles. This is why LoRA makes multi-task serving tractable — one base
model in GPU memory, hot-swap adapter weights per request.

---

## Model Families — The Practical Map

```
Provider    Model           Context   Strengths              Use Case
══════════  ═════════════   ═══════   ══════════             ════════════════
Anthropic   Claude 3.5      200k      Reasoning, code,       Complex tasks,
            Sonnet                    instruction follow,    agentic workflows
                                      long context

            Claude 3 Haiku  200k      Fast, cheap            High-volume,
                                                             latency-sensitive

OpenAI      GPT-4o          128k      Multimodal, strong     General purpose,
                                      all-around             vision tasks

            o1, o3          128k      Deep reasoning         Math, logic,
                                      (chain-of-thought      multi-step problems
                                       baked in weights)

            GPT-4o-mini     128k      Cheap, fast            Simple tasks at scale

Google      Gemini 1.5 Pro  1M        Ultra-long context     Full codebase,
                                                             long documents

Meta        Llama 3.1       128k      Open weights           Self-hosted,
            405B / 70B                                       fine-tunable,
                                                             air-gapped deploy

Mistral     Mistral Large   128k      Strong, European       GDPR-sensitive,
                                      efficient

Cohere      Command R+      128k      RAG-optimized,         Enterprise RAG,
                                      grounding              search augmentation
```

---

## Common Confusion Points

**Hallucination is not a bug to be fixed — it's a property of the architecture.**
LLMs generate the most probable token sequence given training. For queries about facts outside training data, the model will generate plausible-sounding text that may be false. Mitigations: RAG (ground in retrieved context), citations, confidence elicitation, grounded generation with verification. There is no "fix hallucination" — there are only mitigations.

**Temperature 0 is not deterministic in practice.**
Temperature = 0 means argmax decoding, but floating point arithmetic in parallel GPU computation is not fully deterministic. Different batch sizes, different hardware, different CUDA versions can produce different outputs at temperature 0. If you need reproducibility, also set a seed where the API supports it.

**More parameters ≠ better for your task.**
A 7B model fine-tuned on domain-specific data often beats a 70B general model on that domain. Capability, cost, latency, and deployment complexity all scale with parameter count. Match model size to task requirements.

**Context length ≠ effective context length.**
A 200k token context window doesn't mean the model reasons equally well over all 200k tokens. The "lost in the middle" phenomenon means information buried deep in a long context is effectively less available. For critical information, position matters.

**RAG and fine-tuning are not alternatives.**
RAG gives current knowledge and source attribution. Fine-tuning gives consistent behavior and style. They're complementary. Many production systems use both: fine-tune for persona/format, RAG for grounding in current facts.

**The chat API is just a formatting convention.**
The chat API (system/user/assistant message roles) is syntactic sugar over a text completion. The provider concatenates messages into a formatted string (e.g., `<|system|>...<|user|>...<|assistant|>`) and runs the same completion API. Understanding this explains why the system prompt influences but doesn't rigidly constrain the model.

---

## Decision Cheat Sheet

| I need to... | Use |
|---|---|
| Ground model in private documents | RAG (embed + retrieve + inject) |
| Make model follow a consistent format/style | Fine-tuning (SFT) |
| Add recent knowledge without retraining | RAG |
| Get structured JSON output reliably | `response_format: json_object` or tool_use |
| Improve multi-step reasoning | Chain-of-thought prompting |
| Give model access to external data/APIs | Tool use / function calling |
| Run LLMs locally / air-gapped | Llama 3.1, Mistral via llama.cpp / Ollama |
| Fine-tune without a cluster | QLoRA (4-bit quantized base + LoRA adapters) |
| Compare two models on the same task | Evals (02-EVALS-HARNESS) |
| Understand why the model said something | Look at the context — it's all there |
| Reduce cost on high-volume simple tasks | Smaller model (Haiku, GPT-4o-mini) |
| Maximize quality on complex reasoning | o1/o3 or Claude 3.5 Sonnet with CoT |
| Cache repeated long system prompts | Anthropic/OpenAI prompt caching API |
