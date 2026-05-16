# 08 — Inference Optimization and Serving

## The Big Picture

```
  LLM Inference — The Full Stack
  ================================

  ┌──────────────────────────────────────────────────────────────────────┐
  │  REQUEST                                                             │
  │  Prompt tokens (input) → KV Cache (prefill) → Output tokens (decode) │
  └──────────────────────────────┬───────────────────────────────────────┘
                                 │
  ┌──────────────────────────────▼───────────────────────────────────────┐
  │  ATTENTION LAYER                                                     │
  │  Attention(Q,K,V) — the quadratic bottleneck                         │
  │  Optimizations: FlashAttention, MQA, GQA, linear attention           │
  └──────────────────────────────┬───────────────────────────────────────┘
                                 │
  ┌──────────────────────────────▼───────────────────────────────────────┐
  │  MEMORY LAYER                                                        │
  │  KV cache management — the primary GPU memory constraint             │
  │  PagedAttention (vLLM): virtual memory paging for KV cache           │
  │  Prefix caching: reuse KV state for repeated system prompts          │
  └──────────────────────────────┬───────────────────────────────────────┘
                                 │
  ┌──────────────────────────────▼───────────────────────────────────────┐
  │  COMPUTE LAYER                                                       │
  │  Quantization: FP16 → INT8 → INT4 (size, quality, speed tradeoffs)   │
  │  Speculative decoding: draft model accelerates large model           │
  └──────────────────────────────┬───────────────────────────────────────┘
                                 │
  ┌──────────────────────────────▼───────────────────────────────────────┐
  │  SERVING LAYER                                                       │
  │  Continuous batching · Request scheduling · Load balancing           │
  │  vLLM · TGI · SGLang · Triton · Ollama                               │
  └──────────────────────────────┬───────────────────────────────────────┘
                                 │
  ┌──────────────────────────────▼───────────────────────────────────────┐
  │  DEPLOYMENT PATTERN                                                  │
  │  Serverless API · Dedicated GPU cluster · Edge/local                 │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## KV Cache — The Central Memory Problem

```
  Why KV Cache Exists
  ───────────────────────────────────────────────────────────────────────

  Autoregressive decoding: generate one token at a time.
  To generate token t_n, attention needs Q, K, V for all tokens t_1...t_{n-1}.

  Without caching (naive):
    At each step, recompute K and V for ALL previous tokens
    Step n: n × d_model matrix multiplications
    Total compute: O(n²) per token generated → catastrophically slow

  With KV cache:
    Store K and V tensors for all previously processed tokens
    At step n: compute K, V only for the NEW token t_n
    Append to cache. Compute attention using cached K, V.
    Total compute: O(n) per token generated

  Memory footprint formula:
    KV cache bytes = 2 × num_layers × num_heads × d_head × context_len × bytes_per_element

  Example: Llama-3-8B
    num_layers = 32, num_heads = 32, d_head = 128 (= 4096/32), FP16 = 2 bytes
    context_len = 8192 tokens
    2 × 32 × 32 × 128 × 8192 × 2 = ~4.3 GB per sequence

  For batched serving at context_len=8192, batch_size=16:
    4.3 GB × 16 = ~69 GB — exceeds a single A100 80GB with model weights

  This is why context length and batch size are the primary
  serving constraints, not raw compute.
```

### Prefix Caching

```
  Prefix Caching — Reuse KV State Across Requests
  ──────────────────────────────────────────────────────────────────────

  Observation: many requests share the same prefix (system prompt)
    System prompt: 2000 tokens
    User message: 100 tokens
    Total: 2100 tokens → 2000 of those computed identically for every request

  Prefix caching:
    On first request: compute and store KV cache for the system prompt prefix
    On subsequent requests: if prefix matches, skip prefill for those tokens
    Only prefill the user-specific portion

  Savings:
    Cost: avoid paying for 2000 tokens of input on every request
    Latency: TTFT reduced by (prefix_tokens / total_tokens) × prefill_time

  Provider support:
    Anthropic: prompt caching API — explicitly mark prefix for caching
    OpenAI: automatic prompt caching for identical prefixes ≥ 1024 tokens
    Azure OpenAI: follows OpenAI behavior

  Application pattern:
    Always put your system prompt FIRST and keep it stable
    Vary only the user content (which comes after)
    Consistent formatting matters: byte-for-byte prefix match required
```

---

## Attention Optimizations

### FlashAttention

```
  Standard attention: the memory bottleneck
  ──────────────────────────────────────────
  Attention(Q, K, V) = softmax(QK^T / √d_k) V

  QK^T ∈ ℝ^{N × N}  →  N = context length
  For N = 8192: QK^T is 8192 × 8192 = 67M elements × FP16 = 134 MB
  For N = 128k:  128k × 128k = 16B elements — 32 GB just for attention matrix

  Problem: HBM (GPU high-bandwidth memory) bandwidth, not FLOPs, is the bottleneck.
  Reading/writing the N×N attention matrix to HBM is slow.

  FlashAttention (Dao et al. 2022):
    Tile the computation to fit in fast SRAM (on-chip cache)
    Never materialize the full N×N matrix in HBM
    Compute softmax in blocks with online normalization
    Mathematically identical result, IO-aware implementation

  Memory: O(N) instead of O(N²) — does not store full attention matrix
  Speed: 2–4× faster than standard attention for long sequences
  Used by: virtually every production LLM inference system

  FlashAttention-2 (2023): better work partitioning, fewer non-GEMM ops
  FlashAttention-3 (2024): H100-specific optimizations (async pipelines)
```

### Multi-Query Attention (MQA) and Grouped Query Attention (GQA)

```
  Multi-Head Attention (MHA) — baseline
  ────────────────────────────────────────────────────
  h heads → each head has separate Q, K, V projections
  KV cache stores h_KV separate K and V tensors per layer

  Multi-Query Attention (MQA) — Shazeer 2019
  ────────────────────────────────────────────────────
  Multiple Q heads share a SINGLE K and V head
  KV cache: 1 K tensor + 1 V tensor per layer (vs. h)
  Memory: h× reduction in KV cache
  Speed: faster decode (less KV to load from HBM per step)
  Cost: slight quality degradation on tasks requiring diverse attention patterns
  Used by: Falcon, PaLM, early Gemini

  Grouped Query Attention (GQA) — Ainslie et al. 2023
  ────────────────────────────────────────────────────
  Compromise: g groups, each group shares K and V
  g < h: more capacity than MQA, less KV cache than MHA

  Example (Llama-3):
    h_Q = 32 query heads
    h_KV = 8 KV heads (groups)
    4:1 sharing ratio
    KV cache reduction: 4× vs. MHA, quality closer to MHA than MQA

  MHA  ──→  GQA  ──→  MQA
  full KV   partial    single
  cache     sharing    KV head
  Max quality          Max memory efficiency

  Production reality (2024+): GQA is the default.
  Llama 3, Mistral, Gemma, Phi all use GQA.
```

---

## Speculative Decoding

```
  Speculative Decoding (Chen et al. 2023)
  ──────────────────────────────────────────────────────────────────────

  Problem:
    Large model (e.g., Llama-3-70B) is memory-bandwidth bound in decode
    Each new token requires loading 140 GB of weights from HBM
    Hardware utilization during decode is 30-50% — the GPU is mostly waiting

  Insight:
    A small model (e.g., Llama-3-8B) can generate k draft tokens quickly
    The large model can VERIFY k tokens in one parallel forward pass
    (Because verification is like prefill — process k tokens at once, fast)

  Algorithm:
    1. Draft model generates k tokens speculatively: t_1, t_2, ..., t_k
    2. Target (large) model processes all k+1 tokens in one forward pass
    3. Compare draft distribution p(t_i) vs. target distribution q(t_i)
    4. Accept t_i with probability min(1, q(t_i)/p(t_i))
    5. First rejection: resample from corrected distribution, discard rest
    6. Repeat

  Properties:
    Distribution-preserving: outputs are identical in distribution to
    sampling directly from the large model (provably)
    Speedup: 2–3× for typical natural language
    Higher speedup when draft and target agree often (similar domains)

  Variants:
    Medusa: multiple "heads" on single model generate parallel drafts
    Self-speculative: early exit layers of same model as draft
    EAGLE: extrapolation-based draft model

  When not helpful:
    When target model distribution is very different from draft (mismatched domains)
    Short sequences (< 50 tokens) — overhead outweighs benefit
```

---

## Quantization

```
  Quantization: Compress Model Weights to Reduce Memory
  ──────────────────────────────────────────────────────────────────────

  Weight precision tradeoff:
  ┌─────────┬──────────┬──────────────────┬────────────────────────────┐
  │  Format │  Bits    │  Llama-3-70B size│  Quality vs. FP16          │
  ├─────────┼──────────┼──────────────────┼────────────────────────────┤
  │  FP32   │  32 bits │  280 GB          │  Reference (rarely used)   │
  │  BF16   │  16 bits │  140 GB          │  ≈ FP16, better range      │
  │  FP16   │  16 bits │  140 GB          │  Standard baseline         │
  │  INT8   │  8 bits  │  70 GB           │  ~0.5% quality loss        │
  │  INT4   │  4 bits  │  35 GB           │  ~1-2% quality loss        │
  │  INT3   │  3 bits  │  26 GB           │  Noticeable degradation    │
  │  INT2   │  2 bits  │  18 GB           │  Significant degradation   │
  └─────────┴──────────┴──────────────────┴────────────────────────────┘

  Activation quantization vs. weight quantization:
    Weight-only: compress weights to INT4/INT8, activations stay FP16
    W8A8: weights AND activations in INT8 (faster matmuls, trickier)

  Major quantization algorithms:
  ┌─────────────────────────────────────────────────────────────────────┐
  │  GPTQ (Frantar et al. 2022)                                         │
  │    Post-training quantization, weight-only                          │
  │    Minimizes layer-wise quantization error with second-order info   │
  │    INT4, per-group quantization (128 weights share scale factor)    │
  │    Supported by: AutoGPTQ, vLLM, TGI                                │
  │                                                                     │
  │  AWQ (Lin et al. 2023)                                              │
  │    Activation-Aware Quantization                                    │
  │    Identifies 1% of "salient" weights and protects them at FP16     │
  │    Better than GPTQ on many tasks at same bit width                 │
  │    Fast inference (custom CUDA kernels)                             │
  │    Supported by: AutoAWQ, vLLM, llama.cpp                           │
  │                                                                     │
  │  GGUF (llama.cpp format)                                            │
  │    Flexible quantization: Q2_K, Q3_K, Q4_K, Q5_K, Q6_K, Q8_0        │
  │    CPU and Apple Silicon optimized                                  │
  │    Used by: llama.cpp, Ollama, LM Studio, Jan                       │
  │    Q4_K_M is the standard local-deployment choice                   │
  │                                                                     │
  │  SmoothQuant                                                        │
  │    Smooth activation outliers → enables W8A8 without quality loss   │
  │    Used in production serving (NVIDIA TensorRT-LLM)                 │
  └─────────────────────────────────────────────────────────────────────┘
```

---

## Serving Frameworks

```
  LLM Serving Frameworks — What Runs What Where
  ──────────────────────────────────────────────────────────────────────

  ┌──────────┬──────────────────────────────────────────────────────────┐
  │  vLLM    │  Open-source, Python, the production standard            │
  │          │  PagedAttention: KV cache managed like virtual memory    │
  │          │  (pages, copy-on-write, flexible memory allocation)      │
  │          │  Continuous batching: no fixed batch timeout             │
  │          │  OpenAI-compatible API                                   │
  │          │  Supports: Llama, Mistral, Gemma, Phi, Qwen, etc.        │
  │          │  Multi-GPU with tensor parallelism (tp=4 for 4 GPUs)     │
  └──────────┴──────────────────────────────────────────────────────────┘
  ┌──────────┬──────────────────────────────────────────────────────────┐
  │  TGI     │  Text Generation Inference (HuggingFace)                 │
  │          │  Production-grade, Docker-based                          │
  │          │  Flash Attention, continuous batching                    │
  │          │  Strong HuggingFace ecosystem integration                │
  │          │  Powers HuggingFace Inference Endpoints                  │
  └──────────┴──────────────────────────────────────────────────────────┘
  ┌──────────┬──────────────────────────────────────────────────────────┐
  │  SGLang  │  Structured Generation Language                          │
  │          │  RadixAttention: prefix caching via radix tree           │
  │          │  Efficient for multi-turn and structured output tasks    │
  │          │  Growing adoption for reasoning/agent workloads          │
  └──────────┴──────────────────────────────────────────────────────────┘
  ┌──────────┬──────────────────────────────────────────────────────────┐
  │  Ollama  │  Local deployment, developer-friendly                    │
  │          │  GGUF models, CPU + GPU support                          │
  │          │  One command: ollama run llama3                          │
  │          │  Not designed for high-throughput production             │
  └──────────┴──────────────────────────────────────────────────────────┘
  ┌──────────┬──────────────────────────────────────────────────────────┐
  │  Triton  │  NVIDIA Triton Inference Server                          │
  │          │  Supports TensorRT-LLM, FasterTransformer                │
  │          │  Enterprise, K8s-native, model ensemble support          │
  │          │  Bridge: this is to LLMs what IIS is to web apps         │
  └──────────┴──────────────────────────────────────────────────────────┘
```

### Continuous Batching vs. Static Batching

```
  Static batching (pre-vLLM):
    Wait for B requests → batch them → process together
    Problem: requests have different output lengths
    Short requests must wait for long ones to finish
    GPU underutilized during decode of long sequences

  Continuous batching (vLLM, TGI):
    As soon as one request finishes decoding, add a new one to the batch
    Batch composition changes dynamically
    GPU stays fully utilized
    Throughput: 2-5× higher than static batching at same GPU

  Batch size vs. latency tradeoff:
    Larger batch → higher GPU utilization → higher throughput
    Larger batch → more requests share the GPU → higher latency per request
    Typical production target: 80-90% GPU utilization
```

---

## Deployment Patterns and Cost Model

```
  Deployment Pattern Decision Tree
  ──────────────────────────────────────────────────────────────────────

  < 1M tokens/day?
      → Use managed API (OpenAI/Anthropic/Azure AOAI)
        No infra, no ops, pay per token

  1M–100M tokens/day, variable load?
      → Managed API + prompt caching
        Optimize prompts, cache system prompts

  > 100M tokens/day or cost-sensitive?
      → Evaluate self-hosting
        Break-even analysis: GPU cost vs. API cost

  Strict data residency / air-gapped / compliance?
      → Private deployment required
        Azure OpenAI (VNET) or self-hosted
```

### Cost Comparison (2024 approximate)

```
  API costs (per 1M tokens, input/output):
  ┌──────────────────────────┬────────────┬─────────────┐
  │  Model                   │  Input     │  Output     │
  ├──────────────────────────┼────────────┼─────────────┤
  │  GPT-4o                  │  $2.50     │  $10.00     │
  │  GPT-4o-mini             │  $0.15     │  $0.60      │
  │  Claude 3.5 Sonnet       │  $3.00     │  $15.00     │
  │  Claude 3 Haiku          │  $0.25     │  $1.25      │
  │  Gemini 1.5 Pro          │  $1.25     │  $5.00      │
  │  Gemini 1.5 Flash        │  $0.075    │  $0.30      │
  └──────────────────────────┴────────────┴─────────────┘

  Self-hosted infrastructure (cloud GPU, hourly):
    1× A100 80GB:     ~$2.50-3.50/hr     → Llama-3-8B (high throughput)
    2× A100 80GB:     ~$5-7/hr           → Llama-3-70B (fp16)
    4× A100 80GB:     ~$10-14/hr         → Llama-3-70B (high batch)
    1× A100 80GB:     ~$2.50-3.50/hr     → Llama-3-70B (AWQ 4-bit)

  Break-even example (Llama-3-70B vs. Claude 3.5 Sonnet):
    Self-host at 4× A100: $14/hr = $336/day
    At $3/1M tokens: need 112M tokens/day to break even on input alone
    At 1:2 input:output ratio: ~37M total tokens/day

  Reality check: factor engineering + ops cost.
    If you have the GPU know-how (you do — AKS clusters are familiar),
    break-even is well under 100M tokens/day for Sonnet-tier quality.
```

---

## Old World → New World Bridges

```
  IIS web farm / App Service scaling     LLM serving infrastructure
  ──────────────────────────────────────────────────────────────────
  Web workers (IIS app pools)        →   vLLM worker processes
  Connection pool size               →   Batch size + KV cache budget
  CPU saturation metric              →   GPU VRAM utilization metric
  Application insights request trace →   LLM span traces (token counts)
  Load balancer                      →   Routing layer across vLLM replicas
  Azure App Service plan (auto-scale)→   AKS + KEDA (event-driven autoscale)

  IIS/ASP.NET request processing     LLM decode
  ──────────────────────────────────────────────────────────────────
  First byte time (TTFB)             →   TTFT (time to first token)
  Request throughput (req/sec)       →   Token throughput (tokens/sec)
  Worker thread pool                 →   GPU compute units
  Output buffer flush                →   SSE streaming chunks
```

---

## Common Confusion Points

**Quantization doesn't degrade quality linearly.**
The relationship between bit width and quality is not linear. INT8 is nearly lossless (< 0.5% quality degradation) on most tasks. INT4 (Q4_K_M) loses 1-2%. Going from INT4 to INT3 often causes a large quality cliff because the representation becomes too coarse for critical weight values. INT8 → use it; INT4 → test carefully; INT3/INT2 → only for extreme memory constraints.

**Continuous batching doesn't guarantee low latency.**
Continuous batching maximizes throughput, not per-request latency. Under heavy load with a large continuous batch, individual request latency can be high (requests wait to enter the batch). For latency-sensitive workloads, cap batch size or use priority queuing. This is the same tradeoff as a thread pool: more workers = more throughput but not necessarily faster individual responses under contention.

**KV cache is the primary GPU memory constraint, not model weights.**
For a Llama-3-70B model at INT4 (35 GB), you have ~45 GB remaining on a 80 GB GPU. At 8k context length per sequence: 4.3 GB × 10 sequences = 43 GB KV cache. You can serve ~10 concurrent long-context sequences before running out of memory. This explains why commercial providers charge extra for long contexts: it's not compute, it's memory.

**Speculative decoding requires matched vocabularies.**
Draft and target models must share the same tokenizer and vocabulary. You can't use Phi-3 as a draft for Llama-3 — different tokenizers, different token distributions. Typical pairs: Llama-3-8B drafts for Llama-3-70B; both are Meta models with identical tokenizers.

---

## Cross-References

- `cloud-architecture/01-CLOUD-MODELS.md` — hosting choices, managed services, and responsibility boundaries.
- `ai-engineering/06-FINE-TUNING.md` — adapted models and adapters that must be served efficiently.
- `computer-architecture/01-ISA-FUNDAMENTALS.md` — hardware abstraction baseline for inference performance tradeoffs.

## Decision Cheat Sheet

| If you need to diagnose... | Start With | Key Caveat |
|---|---|---|
| Whether managed API or self-hosting fits | Latency, data-control, and operations constraints | Owning GPUs adds scheduler, observability, and capacity-planning work |
| Whether a model fits one GPU | Weight, activation, and KV-cache memory estimates | Quantized weights are only part of the footprint; long context can dominate |
| Whether throughput is batching-bound | vLLM continuous-batching traces | Higher throughput may increase tail latency; measure the service SLO, not tokens/sec alone |
| Whether prefill cost dominates | Prompt length distribution and prefix-cache hit rate | Prefix caching only helps repeated prefixes; random long prompts still pay full prefill |
| Whether decode speed is the bottleneck | Tokens/sec by phase with FlashAttention enabled | FlashAttention helps attention cost but not every serving bottleneck |
| Whether speculative decoding helps | Acceptance rate between draft and target models | Poor draft alignment can add complexity without speedup |
| Whether structured generation is reliable | Constrained decoding with schema-invalid examples | JSON mode is not business validation; still validate semantics downstream |
| Whether multi-GPU scaling is worth it | Tensor-parallel benchmark under real concurrency | More GPUs can reduce per-request latency while worsening cost per token |
