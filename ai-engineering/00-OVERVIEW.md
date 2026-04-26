# 00 — AI Engineering Landscape

## The Big Picture

```
The AI Engineering Stack — Full Field Map
==========================================

  ┌─────────────────────────────────────────────────────────────────────────┐
  │  BUSINESS LAYER                                                         │
  │  Product requirements · KPIs · build vs. buy · cost governance          │
  └──────────────────────────────┬──────────────────────────────────────────┘
                                 │
  ┌──────────────────────────────▼──────────────────────────────────────────┐
  │  APPLICATION LAYER                                                      │
  │  Prompt engineering · RAG pipelines · Agents · Orchestration            │
  │  [03-ORCHESTRATION.md]  [04-AGENTS.md]  [09-VECTOR-DATABASES.md]        │
  └──────────────────────────────┬──────────────────────────────────────────┘
                                 │
  ┌──────────────────────────────▼──────────────────────────────────────────┐
  │  EVALUATION LAYER                                                       │
  │  Evals harness · LLM-as-judge · A/B testing · regression suites         │
  │  [02-EVALS-HARNESS.md]                                                  │
  └──────────────────────────────┬──────────────────────────────────────────┘
                                 │
  ┌──────────────────────────────▼──────────────────────────────────────────┐
  │  MODEL LAYER                                                            │
  │  Foundation model (frozen)    Fine-tuned adapter (LoRA/QLoRA)           │
  │  Provider API (OpenAI/Anthropic/Azure) or self-hosted (vLLM/Ollama)     │
  │  [01-LLM-CONCEPTS.md]  [06-FINE-TUNING.md]  [08-INFERENCE-DEPLOYMENT]   │
  └──────────────────────────────┬──────────────────────────────────────────┘
                                 │
  ┌──────────────────────────────▼──────────────────────────────────────────┐
  │  INFRASTRUCTURE LAYER                                                   │
  │  GPU clusters · KV cache · quantization · serving frameworks            │
  │  Safety filters · logging · guardrails                                  │
  │  [05-SAFETY.md]  [07-MULTIMODAL.md]  [08-INFERENCE-DEPLOYMENT.md]       │
  └──────────────────────────────┬──────────────────────────────────────────┘
                                 │
  ┌──────────────────────────────▼──────────────────────────────────────────┐
  │  DATA LAYER                                                             │
  │  Embeddings · vector stores · chunking · hybrid search                  │
  │  [09-VECTOR-DATABASES.md]                                               │
  └─────────────────────────────────────────────────────────────────────────┘
```

---

## Field Taxonomy — What "AI Engineering" Actually Is

These three roles share vocabulary but solve different problems.

```
  ┌─────────────────────────────────────────────────────────────────────┐
  │                     THE CONFUSION ZONE                              │
  │                                                                     │
  │   ML Research        Data Science         AI Engineering            │
  │   ──────────         ────────────         ──────────────            │
  │   Novel              Insights from        LLMs in production        │
  │   architectures      data                 applications              │
  │   New training       Statistical          Prompt eng. · RAG         │
  │   algorithms         modeling             Agents · Evals            │
  │   Published at       SQL + pandas +       REST APIs ·               │
  │   NeurIPS/ICML       sklearn              streaming · cost          │
  │                                                                     │
  │   PRODUCES:          PRODUCES:            PRODUCES:                 │
  │   Model weights      Dashboards,          Products, APIs,           │
  │   Architecture       reports,             services backed           │
  │   papers             ML pipelines         by foundation models      │
  │                                                                     │
  │   WHO: DeepMind,     WHO: analytics       WHO: most software        │
  │   OpenAI research,   teams, Kaggle        engineers building        │
  │   academic labs      competitors          with LLM APIs             │
  └─────────────────────────────────────────────────────────────────────┘
```

**You are here**: AI Engineering. You're a software engineer who uses foundation models as components — you don't train them from scratch or run statistical experiments on tabular data.

---

## Provider Landscape

```
  ┌──────────────────────────────────────────────────────────────────────────┐
  │                      FOUNDATION MODEL PROVIDERS                          │
  │                                                                          │
  │  PROPRIETARY API (managed inference, no weights released)                │
  │  ┌─────────────┬─────────────┬─────────────┬───────────────────────┐     │
  │  │  OpenAI     │  Anthropic  │  Google     │  Azure OpenAI         │    │
  │  │  GPT-4o     │  Claude 3.5 │  Gemini 1.5 │  Same OpenAI models   │    │
  │  │  GPT-4o-mini│  Claude 3   │  Gemini 2.0 │  + Azure compliance   │    │
  │  │  o1/o3      │  Haiku      │  Flash/Pro  │  + VNET isolation     │    │
  │  │  Whisper    │             │             │  + managed identity   │    │
  │  │  DALL-E 3   │             │  Imagen     │  + your Azure bill    │    │
  │  └─────────────┴─────────────┴─────────────┴───────────────────────┘    │
  │                                                                          │
  │  OPEN WEIGHTS (download, self-host, fine-tune)                           │
  │  ┌─────────────┬─────────────┬─────────────┬───────────────────────┐    │
  │  │  Meta       │  Mistral    │  Microsoft  │  Other                │    │
  │  │  Llama 3.1  │  Mistral 7B │  Phi-3/4    │  Qwen (Alibaba)       │    │
  │  │  405B/70B/  │  Mistral    │  Small/Mini │  Gemma (Google)       │    │
  │  │  8B         │  Large      │  Efficient, │  DeepSeek (China)     │    │
  │  │  HF license │  Mixtral    │  instruction│                       │    │
  │  │             │  (MoE)      │  tuned      │                       │    │
  │  └─────────────┴─────────────┴─────────────┴───────────────────────┘    │
  │                                                                          │
  │  PLATFORMS (hosted open models, inference APIs)                          │
  │  ┌────────────────────────────────────────────────────────────────┐      │
  │  │  Together.ai · Groq · Fireworks · Replicate · AWS Bedrock      │      │
  │  └────────────────────────────────────────────────────────────────┘      │
  └──────────────────────────────────────────────────────────────────────────┘
```

### Provider Selection Matrix

| Dimension | OpenAI | Anthropic | Google | Azure OpenAI | Open weights |
|-----------|--------|-----------|--------|-------------|--------------|
| **Top capability** | GPT-4o, o1/o3 | Claude 3.5 Sonnet | Gemini 1.5 Pro | Same as OpenAI | Llama 3.1 405B |
| **Context window** | 128k | 200k | 1M | Same as OpenAI | 128k |
| **Cost** | Mid | Mid | Mid-low | Same + Azure markup | Infra cost only |
| **Data privacy** | Data used in training (opt out) | Stronger privacy stance | Data policy varies | Azure compliance boundary | Full control |
| **Fine-tuning** | GPT-4o-mini, GPT-3.5 | Not public API | Gemini fine-tune | Azure fine-tune | Full — any method |
| **Enterprise compliance** | SOC 2 | SOC 2 | SOC 2 | FedRAMP, HIPAA, GDPR | Depends on deployment |
| **Agentic / tool use** | Strong | Strong | Good | Same as OpenAI | Model-dependent |
| **Multimodal** | Vision, audio | Vision (Claude 3+) | Vision, audio, video | Same as OpenAI | LLaVA, Whisper |

**Azure OpenAI is not just "Azure-hosted OpenAI"**. It routes traffic through Microsoft's Azure infrastructure with managed identity, VNET support, your Azure billing, and Microsoft's data processing agreements — critical for Microsoft shops with existing compliance frameworks. The models are identical; the infrastructure and compliance story is what you're paying for.

---

## Key Metrics That Drive Architecture Decisions

```
  LATENCY METRICS (what users feel)
  ───────────────────────────────────────────────────────────────────
  TTFT  Time to First Token — how long before streaming starts
        Dominated by prompt length (prefill compute) and queue depth
        For chat UX: TTFT < 500ms feels responsive

  TPS   Tokens Per Second — throughput after first token
        Dominated by model size, batch size, hardware
        GPT-4o: ~50-100 TPS (streaming feels fast)
        Llama-3 70B on A100: ~30-50 TPS (depends on batch)

  E2E   End-to-end latency — TTFT + (output_tokens / TPS)
        For 200-token response at 50 TPS: TTFT + 4 seconds

  COST METRICS (what finance feels)
  ──────────────────────────────────────────────────────────────────
  $/1M input tokens     Claude 3.5 Sonnet: $3   GPT-4o: $2.50
  $/1M output tokens    Claude 3.5 Sonnet: $15  GPT-4o: $10
  Output >> Input cost  Output tokens are 3-5× more expensive

  Rule of thumb for a 1B token/month workload:
    Claude 3.5 Sonnet:  ~$3k-15k/month (mix of input/output)
    GPT-4o-mini:        ~$150-750/month (10× cheaper than Sonnet)
    Self-hosted Llama-3 70B on 4× A100: ~$3-4k/month infra only

  CAPABILITY BENCHMARKS
  ─────────────────────────────────────────────────────────────────
  MMLU      Massive Multitask Language Understanding — knowledge breadth
  HumanEval Python code generation — pass@1 metric
  MATH      Mathematical reasoning — olympiad-level problems
  SWE-Bench Software engineering — real GitHub issues, measured by resolved
  GPQA      Graduate-level science questions

  Warning: benchmarks are saturating and gameable.
  Trust your own evals on your actual task distribution.
```

---

## Build vs. Buy vs. Fine-Tune vs. RAG — Architecture Decision Tree

```
  START: I need an LLM capability in my application
         │
         ▼
  Is this a commodity task? (summarization, classification,
  question answering over known documents, code generation)
         │
    ┌────┴────────┐
   YES            NO (novel task, specialized domain)
    │             │
    ▼              ▼
  USE API       Does the task require knowledge
  (OpenAI,      from proprietary documents / live data?
  Anthropic,         │
  Azure AOAI)   ┌────┴────────┐
                YES            NO
                │              │
                ▼              ▼
             Use RAG        Is it a style/format/persona
             (09-VECTOR)    consistency issue or a
                            knowledge/capability gap?
                              │
                         ┌────┴────────┐
                      STYLE         KNOWLEDGE /
                      /FORMAT       CAPABILITY
                        │              │
                        ▼              ▼
                   Fine-tune       Does the task require
                   (06-FINE-       very specialized
                   TUNING.md)      domain reasoning?
                                      │
                                 ┌────┴────────┐
                                YES            NO
                                 │              │
                                 ▼              ▼
                           Fine-tune +      Prompt
                           RAG combined     engineering
                                            (few-shot,
                                            CoT, etc.)
```

### Build vs. Buy Decision Matrix

| Scenario | Recommendation | Rationale |
|----------|---------------|-----------|
| Internal tool, small team, fast iteration | API (OpenAI/Anthropic) | Cheapest path to value; don't optimize prematurely |
| Enterprise with Azure contracts + compliance | Azure OpenAI | Compliance posture, billing consolidation, existing agreements |
| High volume, cost dominates | Fine-tune smaller model OR self-host | GPT-4o-mini fine-tuned beats Sonnet at 1/20th the cost for narrow tasks |
| Air-gapped / no internet / government | Self-host open weights | Llama 3.1 8B or 70B via vLLM/Ollama |
| Custom data, frequent updates | RAG over API | Don't fine-tune for knowledge freshness — RAG handles it |
| Low latency, real-time | Self-host on dedicated GPU | Managed APIs add 50-200ms network + queue latency |
| IP / data protection concern | Private deployment | Azure OpenAI VNET, or self-host |

---

## Old World → New World Bridges

```
  Azure ML Studio                     Modern LLM deployment
  ─────────────────────────────────────────────────────────────
  AutoML pipelines                →   Prompt engineering + eval harnesses
  Feature store                   →   Embedding store (vector DB)
  Model registry                  →   HuggingFace Hub / Azure model catalog
  Training compute cluster        →   Fine-tuning infra (Azure AI / Together.ai)
  Batch inference endpoint        →   Batch prediction API (OpenAI Batch)
  Real-time inference endpoint    →   Chat completion API endpoint
  Model monitoring (drift)        →   LLM observability (Langfuse, Langsmith)

  VSTS / Azure DevOps release pipelines    LLM deployment pipelines
  ────────────────────────────────────────────────────────────────
  Commit triggers build           →   Dataset change triggers eval run
  Test gate before deploy         →   Eval score threshold before model swap
  Canary deployments              →   A/B routing (10% traffic to new model)
  Rollback on error               →   Rollback to previous model version
  Release notes                   →   Model card / changelog

  App Insights                    LLM observability
  ──────────────────────────────────────────────────
  Request traces                  →   Span-level LLM traces (prompt+response)
  Dependency calls                →   Tool call traces (RAG, external APIs)
  Custom metrics                  →   Token usage, latency, cost per request
  Dashboards                      →   Langfuse, Langsmith, Phoenix (Arize)
  Alerts on SLA breach            →   Alert on eval score regression
```

---

## The AI Engineering Skill Stack

```
  ┌──────────────────────────────────────────────────────────────┐
  │ HIGHEST LEVERAGE FOR A VP / SENIOR ENGINEER                  │
  │                                                              │
  │ Evals design          How do you measure if this works?      │
  │ Retrieval strategy    RAG architecture, chunking, reranking  │
  │ Model selection       Which model, cost model, make/buy      │
  │ Prompt architecture   System prompt design, few-shot strat.  │
  │                                                              │
  │ IMPLEMENTATION DETAILS (delegate or learn as needed)         │
  │                                                              │
  │ Fine-tuning mechanics  LoRA setup, hyperparameters           │
  │ Serving infra          vLLM, quantization, batching          │
  │ Vector DB ops          HNSW tuning, index rebuilds           │
  └──────────────────────────────────────────────────────────────┘
```

---

## Common Confusion Points

**"AI engineering" is just another name for ML engineering.**
Not quite. ML engineering historically meant training models, managing datasets, building training pipelines, and deploying scikit-learn/TensorFlow models. AI engineering (circa 2023+) means building applications on top of foundation models via APIs — prompting, RAG, agents, evals. The training infrastructure is someone else's problem. The boundary is blurring as fine-tuning becomes more accessible.

**RAG vs. fine-tuning are competing approaches.**
They're orthogonal. RAG handles knowledge freshness and source attribution. Fine-tuning handles behavior, style, and format. Most production systems doing serious work use both: fine-tune for format/persona/domain vocabulary, RAG for current facts. Treating them as "pick one" is a category error.

**Bigger context window eliminates the need for RAG.**
A 1M token context window doesn't mean you stuff everything into context. (1) Cost: at $3/1M input tokens, filling a 1M context window costs $3 per request — orders of magnitude more than retrieving 5 relevant chunks. (2) The "lost in the middle" problem means retrieval precision still matters. (3) RAG gives you semantic search — you find the relevant needle, not just stuff the whole haystack.

**Open weights = free.**
Open weights means free software license, not free to run. Llama 3.1 70B needs 2× A100 (80GB) minimum, which costs ~$3-4/hour on cloud GPU. Factor total cost of ownership: GPU cost, serving infrastructure, engineering time, vs. $0.003/1k tokens on GPT-4o-mini.

**Benchmarks predict production performance.**
Public benchmarks (MMLU, HumanEval, etc.) measure specific static tasks. Your task distribution differs. Run your own evals on your actual workload before choosing a model.

---

## Decision Cheat Sheet

| Task | Model family | Why |
|------|-------------|-----|
| Complex reasoning, agentic, long context | Claude 3.5 Sonnet or GPT-4o | Best instruction following at cost |
| Math, hard logic, step-by-step reasoning | o1/o3 or Claude with extended thinking | Reasoning models trained for this |
| High volume simple tasks (classification, extraction) | GPT-4o-mini or Claude Haiku | 5-10× cheaper, good enough |
| RAG over enterprise documents | GPT-4o or Claude 3.5, + embeddings | Strong instruction following + grounding |
| Code generation / review | Claude 3.5 Sonnet or GPT-4o | Both strong; Sonnet slightly better on complex code |
| Document understanding (PDF, tables, images) | GPT-4V or Claude 3 vision | 07-MULTIMODAL covers this |
| Air-gapped deployment | Llama 3.1 70B or Phi-3 | Open weights, self-hosted |
| Ultra-long document (book-length) | Gemini 1.5 Pro | 1M context with strong recall |
| Speech-to-text | Whisper (OpenAI) or Deepgram | Industry standard |
| Image generation | DALL-E 3 or Stable Diffusion | Depending on control needs |
| Fine-tuning target (cost-sensitive) | GPT-4o-mini, Llama 3.1 8B | Small, fine-tunable, cheap |
| Embedding / semantic search | text-embedding-3-large, BGE-M3 | 09-VECTOR-DATABASES covers this |
