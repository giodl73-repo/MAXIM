# 06 — Fine-Tuning and Model Adaptation

## The Big Picture

```
The Fine-Tuning Spectrum — Where Your Work Falls
=================================================

  BASE MODEL (pre-trained on internet-scale text)
  No instruction following · Will complete anything · No alignment
       │
       │ Full fine-tuning: update ALL parameters
       │ - Full task adaptation
       │ - Catastrophic forgetting risk
       │ - Compute cost: same as pre-training fraction
       │
       ├──────────────────────────────────────────────────────────
       │
       │ SFT (Supervised Fine-Tuning): fine-tune on (prompt, response) pairs
       │ - Teaches instruction following format
       │ - Typical data scale: 1k–100k examples
       │ - The first alignment step
       │
       ├──────────────────────────────────────────────────────────
       │
       │ PEFT (Parameter-Efficient Fine-Tuning)
       │ - LoRA: add low-rank adapter matrices, train only those
       │ - QLoRA: 4-bit quantized base + LoRA adapters
       │ - DoRA: decompose weights into magnitude + direction
       │ - Prefix tuning: prepend trainable tokens to each layer
       │ - Prompt tuning: single soft token prefix (smallest PEFT)
       │
       ├──────────────────────────────────────────────────────────
       │
       │ Alignment fine-tuning: shape behavior to human preferences
       │ - RLHF: reward model → PPO optimization
       │ - DPO: direct optimization on preference pairs (no RM)
       │ - ORPO / SimPO: simplifications of DPO
       │
       ▼
  ADAPTED MODEL
  Instruction-following · Domain-specific · Aligned to preferences
```

---

## Full Fine-Tuning

Full fine-tuning updates every parameter in the model. Rarely the right choice for application engineers.

```
  FULL FINE-TUNING MECHANICS
  ───────────────────────────────────────────────────────────────────

  What it does:
    Initialize from pre-trained checkpoint
    Compute gradient of loss w.r.t. ALL parameters
    Update all weights via optimizer (Adam, AdamW)

  Compute requirements (approximate):
    Training memory ≈ 16 bytes × parameter_count
      (FP32 weights + gradients + optimizer state)
    Llama-3-8B:  8B × 16 bytes = 128 GB  (won't fit on single A100 80GB)
    Llama-3-70B: 70B × 16 bytes = 1.1 TB (requires 16× A100s minimum)

  Catastrophic forgetting:
    Fine-tuning on narrow data → model "forgets" general capabilities
    Measured by: degradation on held-out general benchmarks (MMLU, etc.)
    Mitigation: mix general data into fine-tuning corpus (replay)
    Reality check: if you need the base model to stay general,
    you probably want PEFT, not full fine-tuning

  When full fine-tuning is justified:
    ✅ Domain shift so large that adapter capacity is insufficient
    ✅ You need maximum task performance (final % matters)
    ✅ You have the compute and a dedicated model deployment
    ✅ Continual pre-training on proprietary corpus
    ❌ Most application engineering scenarios — use PEFT
```

---

## PEFT — Parameter-Efficient Fine-Tuning

The dominant approach for application engineers. Trains a tiny fraction of parameters while keeping the base model frozen.

### LoRA (Low-Rank Adaptation)

```
  LoRA: The Core Idea (Hu et al. 2021)
  ─────────────────────────────────────────────────────────────────

  For a weight matrix W ∈ ℝ^{d × k} (pre-trained, frozen):
  Instead of computing full ΔW ∈ ℝ^{d × k} during fine-tuning,
  approximate it with a low-rank decomposition:

    ΔW = A · B      where A ∈ ℝ^{d × r}, B ∈ ℝ^{r × k}, r << min(d,k)

  Forward pass:
    h = W₀x + ΔWx = W₀x + (AB)x

  W₀ stays frozen. Only A and B are trained.

  Parameter reduction:
    Full ΔW: d × k parameters
    LoRA:    d × r + r × k = r(d + k) parameters
    For d=4096, k=4096, r=16: 16×8192 = 131k vs. 16.7M = 99.2% reduction

  Typical rank values:
    r = 8–16:   general-purpose fine-tuning, good quality/cost tradeoff
    r = 32–64:  complex task adaptation, more capacity
    r = 4:      minimal, style/format adaptation only
    r = 128+:   approaching full fine-tuning territory

  Which layers to apply LoRA to:
    Attention projections: Q, K, V, O (standard, most common)
    FFN layers: additional capacity, more parameters
    All linear layers: maximum adaptation (DoRA territory)

  At inference:
    Option 1: keep A, B separate → add ΔWx at runtime (hot-swappable)
    Option 2: merge into base: W = W₀ + AB → no runtime overhead

  Implementation:
    HuggingFace PEFT library: peft.LoraConfig(r=16, lora_alpha=32, ...)
    Axolotl: yaml config, wraps PEFT
    LLaMA-Factory: full fine-tuning framework, LoRA/QLoRA native
```

The structural analog: LoRA is the Adapter pattern. The frozen base model is a stable, expensive-to-change interface. The A and B matrices are the lightweight specialization layer — same stable base, different behavior profiles. Swapping LoRA adapters = swapping adapter implementations.

### QLoRA

```
  QLoRA (Dettmers et al. 2023) — Fine-tuning large models on consumer hardware
  ──────────────────────────────────────────────────────────────────────────────

  Stack:
    NF4 quantization:  base model weights quantized to 4-bit NormalFloat
                       designed for normally distributed weights (they are)
    Double quantization: quantize the quantization constants → saves ~0.5 GB
    Paged optimizer:    swap optimizer states to CPU when GPU OOM

  Memory comparison (Llama-3-70B):
    Full FP16:     140 GB  (2× A100 80GB minimum)
    Full BF16:     140 GB
    QLoRA (NF4):   ~35 GB  (fits on 1× A100 80GB, 2× 24GB consumer GPUs)

  Quality:
    QLoRA 4-bit + LoRA ≈ full 16-bit LoRA at same rank
    ~1–2% quality gap vs. full fine-tuning on most tasks
    For most applications: indistinguishable in production

  Practical setup:
    bitsandbytes library → quantizes base model on load
    PEFT → LoRA adapters on top of quantized model
    Training with gradient checkpointing → further memory savings

  When to use QLoRA vs LoRA:
    QLoRA: you have consumer GPUs (24GB each) or need 70B on 1 A100
    LoRA:  you have ample GPU memory and want fastest training
```

### DoRA, Prefix Tuning, Prompt Tuning

```
  DoRA (Weight-Decomposed Low-Rank Adaptation, 2024)
    Decomposes W into magnitude (‖W‖) and direction (W/‖W‖)
    Applies LoRA to the direction component only
    Better approximates full fine-tuning behavior
    ~5–10% better than LoRA at same rank on instruction tuning tasks

  Prefix Tuning (Li & Liang 2021)
    Prepends learnable "virtual tokens" (prefix) to K and V at each layer
    The prefix vectors are trainable; the base model is frozen
    Analogy: adding a trained preamble that conditions every attention head
    Strength: strong for generation tasks with fixed output format
    Weakness: less effective for tasks requiring deep weight modification

  Prompt Tuning (Lester et al. 2021)
    Simplest PEFT: add k trainable tokens to the input embedding only
    No modifications to attention layers
    At scale (10B+ params): approaches fine-tuning quality
    At smaller scales: significantly underperforms LoRA
    Use case: lightweight style/format adaptation on very large models

  IA³ (Infused Adapter by Inhibiting and Amplifying Inner Activations)
    Scales K, V, and FFN activations by learned vectors
    Extremely parameter-efficient (~0.01% of model parameters)
    Strong for few-shot tasks; underperforms LoRA on standard SFT
```

---

## SFT — Supervised Fine-Tuning

```
  SFT Pipeline
  ────────────────────────────────────────────────────────────────────

  1. Dataset curation
       ┌─────────────────────────────────────────────────────────┐
       │  (system_prompt, user_turn, assistant_response) triples │
       │                                                         │
       │  Format: ShareGPT (multi-turn) or Alpaca (single-turn)  │
       │  ShareGPT:                                              │
       │    {"conversations": [                                  │
       │      {"from": "system", "value": "..."},                │
       │      {"from": "human",  "value": "..."},                │
       │      {"from": "gpt",    "value": "..."}                 │
       │    ]}                                                   │
       │                                                         │
       │  Data quality >> quantity                               │
       │  500 clean examples often beat 50k noisy ones           │
       └─────────────────────────────────────────────────────────┘

  2. Token masking
       Input tokens (prompt):   loss = 0 (don't train on these)
       Output tokens (response): loss = cross-entropy (train on these)

       Why: you want the model to learn to produce the response,
       not to memorize the prompts. Loss only flows from response tokens.

  3. Training hyperparameters (typical LoRA SFT)
       Learning rate:  1e-4 to 3e-4 (higher than pre-training)
       LR schedule:    cosine decay with 3–5% warmup
       Batch size:     32–128 (limited by GPU memory)
       Epochs:         1–3 (more epochs → overfitting on small datasets)
       Dropout:        0.05–0.1 on LoRA matrices

  4. Evaluation during training
       Held-out split (10–20% of data): perplexity on response tokens
       Task-specific evals: run your eval suite every N steps
       Early stopping: stop when eval metric plateaus or degrades
```

---

## Alignment Fine-Tuning

### RLHF (Reinforcement Learning from Human Feedback)

```
  RLHF Pipeline (Christiano et al. 2017, refined by OpenAI/Anthropic)
  ──────────────────────────────────────────────────────────────────────

  Step 1: SFT model
    Fine-tune base model on (prompt, good response) pairs → π_SFT

  Step 2: Reward model
    Dataset: same prompt, two responses (y_w preferred over y_l by humans)
    Train reward model R_φ to predict: R(x, y_w) > R(x, y_l)
    Architecture: LLM with linear head → scalar reward score

  Step 3: PPO optimization
    Maximize: E[R_φ(x, y)] - β · KL(π_θ || π_SFT)
    The KL term keeps the model close to π_SFT
    Without KL penalty: reward hacking → model outputs gibberish
    that scores high on the RM without being useful
    β controls exploitation vs. staying on-distribution

  Problem with RLHF:
    Unstable PPO training (sensitive to hyperparameters)
    Two separate model training phases (SFT + RM)
    RM can be exploited (Goodhart's Law — optimizing proxy ≠ optimizing goal)
    Engineering complexity: requires 3 models in memory during PPO
```

### DPO (Direct Preference Optimization)

```
  DPO (Rafailov et al. 2023) — Why It Largely Replaced RLHF
  ──────────────────────────────────────────────────────────────────

  Key insight: the optimal policy under RLHF can be expressed in
  closed form. You can skip the explicit reward model.

  DPO loss function:
    L_DPO(θ) = -E[(x, y_w, y_l)] log σ(
      β log(π_θ(y_w|x) / π_ref(y_w|x)) -
      β log(π_θ(y_l|x) / π_ref(y_l|x))
    )

  In plain language:
    Increase probability of preferred response y_w
    Decrease probability of dispreferred response y_l
    Relative to a reference model π_ref (the SFT model)
    β controls how far to deviate from the reference

  What you need:
    Preference dataset: (prompt, chosen_response, rejected_response)
    SFT model as reference
    That's it — no reward model, no PPO

  Advantages over RLHF:
    ✅ Single training phase
    ✅ Standard supervised learning (no RL instability)
    ✅ No separate reward model to train and maintain
    ✅ Less memory (no need to keep RM loaded)
    ✅ More stable, easier to tune

  Disadvantages:
    ❌ Less flexible than RL (can't do online exploration)
    ❌ Preference data quality is critical
    ❌ Distribution shift: reference model must match your SFT model

  Variants:
    ORPO (Odds Ratio Preference Optimization):
      Combines SFT and preference optimization in one loss
      Removes need for a separate reference model
      More parameter-efficient (one training phase from base)

    SimPO (Simple Preference Optimization):
      Removes reference model entirely
      Uses length-normalized reward
      Outperforms DPO on several benchmarks with simpler setup

  Current state of the art (2024):
    Most open-source fine-tuned models use DPO or ORPO
    Closed models (GPT-4, Claude) still use proprietary RLHF variants
    DPO is the default for most application engineers doing alignment
```

---

## Fine-Tune vs. RAG — The Decision Tree

```
  START: I want to adapt model behavior for my use case
             │
             ▼
  Does the task require access to specific, frequently-updated
  facts, documents, or private data?
             │
       ┌─────┴──────┐
      YES            NO
       │              │
       ▼              ▼
  Use RAG          Is the task about consistent
  (09-VECTOR)      behavior, style, or format?
  (stop here)            │
                   ┌─────┴──────┐
                  YES            NO
                   │              │
                   ▼              ▼
              Fine-tune        Is the model currently
              (SFT / LoRA)     failing at the core
                               task with good prompting?
                                     │
                               ┌─────┴──────┐
                              YES            NO
                               │              │
                               ▼              ▼
                         Fine-tune          Improve
                         (task-specific)    prompts / CoT
```

### Quantified Decision Guide

| Factor | Favor RAG | Favor Fine-tuning |
|--------|-----------|------------------|
| **Data freshness** | Updates daily/weekly | Stable for months |
| **Knowledge type** | Specific facts, documents | Style, format, persona |
| **Training data** | < 100 labeled examples | > 500 quality examples |
| **Latency budget** | Tolerates retrieval overhead (100-300ms) | Needs fast response |
| **Cost** | Pay per query (embedding + retrieval) | Upfront training cost, cheaper per query |
| **Debuggability** | Can see retrieved chunks | Behavior in weights |
| **Domain jargon** | Jargon in documents (RAG will retrieve it) | Need model to *use* jargon naturally |

---

## Evaluation

```
  Fine-tuning Eval Stack
  ──────────────────────────────────────────────────────────────────

  1. Held-out split metrics (automatic, fast)
     Perplexity on response tokens: lower = better
     Task metric: accuracy, F1, BLEU/ROUGE, pass@1 for code
     Sanity check: not the final story

  2. Capability regression testing
     Run model on general benchmarks after fine-tuning
     MMLU: knowledge breadth preserved?
     HumanEval: code capability preserved?
     Flag: > 2–3% degradation is concerning
     Fix: mix general data into fine-tuning corpus

  3. Task-specific evals (the real signal)
     Your held-out examples from your actual task distribution
     LLM-as-judge for subjective quality (02-EVALS-HARNESS.md)
     Human eval on 50–100 examples for launch gate

  4. A/B testing in production
     Shadow mode: run new model, log outputs, don't serve yet
     Canary: route 5–10% traffic to new model
     Metric: task success rate, user preference, helpfulness rating
```

---

## Common Confusion Points

**LoRA rank is not a quality knob you just crank up.**
Higher rank means more parameters and potentially more adaptation capacity, but also more risk of overfitting on small datasets. r=16 is a strong starting point. Only increase rank if you have evidence the model lacks adaptation capacity, and you have sufficient training data (> 1k examples).

**QLoRA quality is not significantly worse than full fine-tuning.**
The original QLoRA paper showed that 4-bit quantized base + LoRA adapters nearly matches full 16-bit fine-tuning on instruction following tasks. For most application tasks, the quality gap is < 2% and invisible in production. Use QLoRA if memory is the constraint.

**DPO requires SFT first.**
DPO needs a reference model (π_ref). That reference is your SFT model. You cannot skip SFT and apply DPO to the raw base model — the base model produces incoherent outputs that produce meaningless preference signals. Order: SFT → DPO.

**Fine-tuning for knowledge is a mistake.**
If the goal is "the model should know X", fine-tuning is the wrong tool. Fine-tuning on facts leads to hallucinations when the model over-generalizes patterns. Facts belong in a retrieval system. Fine-tuning is for style, format, and behavior — not for injecting knowledge.

**RLHF is mostly a closed-model concern.**
In 2024, open-source fine-tuning workflows use SFT → DPO (or ORPO). Full RLHF with PPO is complex, compute-intensive, and requires building a reward model from scratch. Unless you have an ML research team, you're doing DPO.

---

## Decision Cheat Sheet

| I need to... | Use |
|---|---|
| Adapt style/format/persona at low cost | LoRA (r=16) via HuggingFace PEFT |
| Fine-tune 70B on single A100 | QLoRA (4-bit + LoRA) |
| Teach model to follow specific output schema | SFT on 500+ (prompt, response) pairs |
| Align model to prefer certain responses | DPO on (prompt, chosen, rejected) data |
| Combine SFT + alignment in one pass | ORPO |
| Fine-tune without a reference model | SimPO |
| Maximum adaptation quality, have compute | Full fine-tuning (rare in practice) |
| Add domain vocabulary naturally | SFT on domain corpus (5k+ examples) |
| Fine-tune multiple tasks, swap at runtime | LoRA (keep adapters separate, merge at serve time) |
| Know if fine-tuning is worth it | Run evals on base model first — often prompting is enough |
