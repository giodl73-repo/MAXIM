# NLP Foundations
## From N-Grams to Transformers — The Mathematical Path to LLMs

```
NLP ARCHITECTURE EVOLUTION

  N-grams         Word2Vec / GloVe      LSTM / Seq2Seq       Transformer
  (1990s)         (2013–2014)           (2014–2017)          (2017–present)
  ────────────    ─────────────────     ────────────────     ─────────────────
  Sparse counts   Dense embeddings      Sequence modeling    Attention is all
  Smoothing       PMI factorization     Attention (additive) Scaled dot product
  Perplexity      PPMI → SVD → skip     Encoder-Decoder      BERT / GPT / T5
  Fixed vocab     Subword (FastText)    Bottleneck problem   Scaling laws
```

---

## 1. Statistical Language Models

**Language model**: assigns probability to sequences of words. Core task: compute P(w₁, w₂, ..., wT).

**Chain rule**:
```
  P(w₁,...,wT) = Π_{t=1}^T P(wₜ | w₁,...,wₜ₋₁)
```

**n-gram model**: Markov assumption — only last (n-1) words matter:
```
  P(wₜ | w₁,...,wₜ₋₁) ≈ P(wₜ | wₜ₋ₙ₊₁,...,wₜ₋₁) = C(wₜ₋ₙ₊₁,...,wₜ) / C(wₜ₋ₙ₊₁,...,wₜ₋₁)

  Unigram (n=1): P(w) = C(w)/N
  Bigram  (n=2): P(wₜ | wₜ₋₁) = C(wₜ₋₁wₜ) / C(wₜ₋₁)
```

**Data sparsity problem**: C(unseen n-gram) = 0 → P = 0 → product = 0. Need smoothing.

**Kneser-Ney smoothing** (best practical n-gram):
```
  P_{KN}(w|context) = max(C(context, w) - d, 0) / C(context)
                     + λ(context) · P_{KN-lower}(w | shorter context)

  d ≈ 0.75 (discount)
  λ: normalizing constant
  P_{KN-lower}: recursively smoothed lower-order model

  Innovation: continuation probability — P_continuation(w) ∝ # contexts w completes
  "San Francisco" → Francisco has high continuation (many contexts precede it)
  Better than uniform backoff.
```

**Perplexity**: standard metric for language models:
```
  PP(W) = P(w₁,...,wT)^{-1/T} = exp(-(1/T) Σ log P(wₜ | w₁:ₜ₋₁))
  = exp(cross-entropy of model on test set)

  Lower PP = better model. PP=k means model is "k-way confused" at each step.
  Intuition: branching factor — if all words equally likely at each step, PP = vocab size.
```

---

## 2. Distributional Semantics

**Distributional hypothesis** (Harris 1954, Firth 1957): "You shall know a word by the company it keeps." Words that appear in similar contexts have similar meanings.

**Word-context matrix**: count co-occurrences within a window:
```
  M ∈ ℝ^{|V| × |V|}:  M_{ij} = count(wordᵢ appears in context of wordⱼ)

  Problem: raw counts dominated by function words (the, a, of...)
```

**PMI (Pointwise Mutual Information)**:
```
  PMI(w, c) = log( P(w,c) / P(w)P(c) ) = log( C(w,c)·N / C(w)·C(c) )

  PPMI (Positive PMI): max(PMI, 0)  — zeroes out negative associations
```

**SVD dimensionality reduction**:
```
  M ≈ U Σ Vᵀ,  keep top d singular vectors

  Word vectors: rows of U·Σ^{0.5}  (or just U)
  This gives dense, low-dimensional word representations.
  Captures semantic similarity: cosine(vec(king), vec(queen)) is high.
```

---

## 3. Word2Vec

**Skip-gram model** (Mikolov et al. 2013):
```
  Predict context words from center word:
    Maximize: Σ_t Σ_{-c≤j≤c, j≠0} log P(wₜ₊ⱼ | wₜ)

    P(o | c) = exp(uₒᵀ vᵢ) / Σ_{w∈V} exp(uₙᵀ vᵢ)   ← softmax

  Two matrices: input embeddings V (word as center) and output embeddings U (word as context)
  Full softmax over |V|=10⁵⁻⁶ words → too expensive
```

**Negative sampling**:
```
  Replace softmax with binary classification: is (word, context) a real pair?
    J = log σ(uₒᵀ vᵢ) + Σ_{k=1}^K E_{wₖ~P_n(w)}[log σ(-uₖᵀ vᵢ)]

  K=5-20 negative samples drawn from unigram distribution P_n(w) ∝ f(w)^{3/4}
  (³⁄₄ power: boosts rare words, reduces common words)
  Efficient: O(K) per example instead of O(|V|)
```

**SGNS = PPMI matrix factorization** (Levy & Goldberg 2014):
```
  With infinite data, skip-gram with negative sampling implicitly factorizes:
  M_{wc} = PPMI(w,c) - log(k)

  Word2Vec is doing a specific form of matrix factorization!
  Connects neural word vectors to the classical distributional semantics framework.
```

**Analogy task**: king - man + woman ≈ queen
```
  Explanation: vec(king) - vec(man) ≈ vec(royalty)
  vec(woman) + vec(royalty) ≈ vec(queen)

  Works because: linear substructure in semantic space
  3CosAdd: argmax_{b*} cos(b*, b - a + a*)
```

---

## 4. GloVe

**Global Vectors** (Pennington et al. 2014) — directly factorize the co-occurrence matrix:

```
  Let Xᵢⱼ = count(word i appears in context of word j)
  Pᵢⱼ = Xᵢⱼ / Xᵢ  (conditional probability)

  Observation: ratios of probabilities encode meaning:
    P(ice|k) / P(steam|k) is large for k="solid", small for k="gas"

  Model: wᵢᵀ w̃ⱼ + bᵢ + b̃ⱼ = log Xᵢⱼ

  Loss: J = Σᵢⱼ f(Xᵢⱼ) (wᵢᵀ w̃ⱼ + bᵢ + b̃ⱼ - log Xᵢⱼ)²
          ↑
     weighting function: f(X) = (X/x_max)^α for X < x_max, else 1
     Caps contribution of frequent pairs
```

Final word vectors: sum of word embedding and context embedding wᵢ + w̃ᵢ.

**Word2Vec vs GloVe**:
```
  Word2Vec: stochastic, learns from local context windows
  GloVe:    batch, directly models global co-occurrence statistics
  In practice: similar quality; GloVe easier to train consistently
  Both: FastText adds subword information (handles OOV, morphology)
```

**FastText**: represent word as sum of character n-gram embeddings:
```
  vec("playing") = vec("<pla") + vec("lay") + vec("ayi") + ... + vec("ing>")

  Handle out-of-vocabulary words by summing known subword embeddings.
  Strong for morphologically rich languages.
```

---

## 5. RNNs and the Vanishing Gradient Problem

**RNN** (Elman 1990):
```
  hₜ = tanh(Wxhₜ₋₁ + Wxₜ + b)
  yₜ = Wyₒhₜ

  hₜ: hidden state (encodes all history up to t)
```

**Vanishing gradient problem** (Bengio et al. 1994):
```
  ∂L/∂h₁ = ∂L/∂hT · Π_{t=2}^T ∂hₜ/∂hₜ₋₁
                    ↑
          product of T-1 Jacobians

  Each ∂hₜ/∂hₜ₋₁ = diag(tanh'(·)) · Whh

  If ‖Whh‖ < 1 and tanh'(·) < 1: product → 0 exponentially (vanish)
  If ‖Whh‖ > 1: product → ∞ exponentially (explode)

  Gradient clipping: ‖g‖ > threshold → g ← g · threshold/‖g‖  (fixes explosion)
  Vanishing: harder to fix — LSTM is the solution
```

---

## 6. LSTM

**Long Short-Term Memory** (Hochreiter & Schmidhuber, 1997):
```
  Cell state cₜ:  long-term memory (slow-changing, linear dynamics)
  Hidden state hₜ: short-term memory / output (fast-changing)

  Gates (all sigmoid → output in [0,1]):
    fₜ = σ(Wf[hₜ₋₁, xₜ] + bf)      forget gate: how much of cₜ₋₁ to keep
    iₜ = σ(Wi[hₜ₋₁, xₜ] + bi)      input gate: how much to write to cell
    oₜ = σ(Wo[hₜ₋₁, xₜ] + bo)      output gate: how much of cell to expose

  Cell candidate: c̃ₜ = tanh(Wc[hₜ₋₁, xₜ] + bc)

  Cell update:  cₜ = fₜ ⊙ cₜ₋₁ + iₜ ⊙ c̃ₜ
                     ↑                ↑
                 keep old cell     write new info

  Hidden state: hₜ = oₜ ⊙ tanh(cₜ)
```

**Why LSTM avoids vanishing gradients**:
```
  ∂cₜ/∂cₜ₋₁ = fₜ   ← forget gate controls gradient flow

  If fₜ ≈ 1 (remember): gradient flows through unchanged (additive update path)
  The additive update cₜ = fₜ⊙cₜ₋₁ + ... creates a "constant error carousel"
  No repeated matrix multiplication on the cell state path → no exponential vanishing
```

**GRU** (Gated Recurrent Unit, Cho et al. 2014) — simplified LSTM:
```
  zₜ = σ(Wz[hₜ₋₁, xₜ])     update gate (combine reset + input)
  rₜ = σ(Wr[hₜ₋₁, xₜ])     reset gate
  h̃ₜ = tanh(W[rₜ⊙hₜ₋₁, xₜ])  candidate
  hₜ = (1-zₜ)⊙hₜ₋₁ + zₜ⊙h̃ₜ   no separate cell state

  Fewer parameters than LSTM; comparable performance on most tasks.
```

---

## 7. Seq2Seq and Attention

**Seq2Seq** (Sutskever et al. 2014) — encoder-decoder for translation:
```
  Encoder: RNN processes source sequence → final hidden state c (context vector)
  Decoder: RNN generates target sequence using c as initial state

  Bottleneck problem: entire source compressed into fixed-size vector c
  Long sequences → c forgets early tokens → poor performance on long sentences
```

**Bahdanau Attention** (2015) — soft attention:
```
  At each decoder step t, compute attention over all encoder hidden states:

  Score function (additive):
    eₜⱼ = vᵀ tanh(Wa sₜ₋₁ + Ua hⱼ)    ← compatibility of decoder state sₜ₋₁ with encoder state hⱼ

  Attention weights:
    αₜⱼ = exp(eₜⱼ) / Σₖ exp(eₜₖ)        softmax over source positions

  Context vector:
    cₜ = Σⱼ αₜⱼ hⱼ                       weighted sum of encoder states

  Decoder: sₜ = RNN(sₜ₋₁, yₜ₋₁, cₜ)     use per-step context

  Key: αₜⱼ is a soft alignment — interpretable attention matrix
```

**Why attention solves bottleneck**: instead of one context vector c for the entire sequence, the decoder gets a different context cₜ at each step, computed as a weighted sum over all encoder states. Long-range dependencies can be captured directly.

---

## 8. Transformer

**Scaled dot-product attention** (Vaswani et al. 2017):
```
  Attention(Q, K, V) = softmax(QKᵀ / √d_k) V

  Q ∈ ℝ^{n×d_k}, K ∈ ℝ^{m×d_k}, V ∈ ℝ^{m×d_v}

  Comparison to Bahdanau:
    Bahdanau: additive attention (MLP scorer), RNN context
    Vaswani:  multiplicative attention (dot product), parallelizable
    √d_k scaling: prevents softmax saturation as d_k grows
```

**Why √d_k scaling** (formal argument):
```
  Q, K entries ~ N(0,1) independently
  (Q·K^T)_{ij} = Σ_{l=1}^{d_k} q_{il} k_{jl}
  E[(q_il k_jl)²] = 1  (product of two unit Gaussian vars)
  Var(q_i · k_j) = d_k  →  std(q_i · k_j) = √d_k

  Without scaling: softmax input std grows as √d_k
  For d_k=64: std≈8 → extreme softmax → near one-hot → vanishing gradient on non-max
  With /√d_k: normalize to unit std → well-conditioned softmax
```

**Positional encodings** (sinusoidal):
```
  PE(pos, 2i)   = sin(pos / 10000^{2i/d_model})
  PE(pos, 2i+1) = cos(pos / 10000^{2i/d_model})

  Linear attention property: PE(pos+k) can be expressed as linear function of PE(pos)
  Proof: sin(a+b) = sin(a)cos(b) + cos(a)sin(b) — each frequency dimension rotates
  The rotation matrix Mₖ exists such that PE(pos+k) = Mₖ PE(pos)
  → Relative position can be computed from absolute encodings

  Why not learned? Generalize to sequence lengths longer than training.
  Modern: RoPE (rotary position embedding) — directly bakes rotation into Q,K matrices
```

**Full Transformer block**:
```
  x → LayerNorm → MultiHeadSelfAttention → (+) → x'
  x' → LayerNorm → FFN(2-layer MLP, d_ff=4d_model, GELU) → (+) → output

  Pre-norm (modern): LayerNorm before sublayer, not after (stable training)
  Post-norm (original): LayerNorm after residual connection
```

**Complexity**: O(n²d) in sequence length n. For n=2048, d=1024: ~4B operations per layer. For n=32K: 256B — quadratic wall.

---

## 9. BERT and Bidirectional Pretraining

**BERT** (Devlin et al. 2018) — bidirectional encoder:
```
  Architecture: Transformer encoder (no decoder)

  Two pretraining tasks:

  1. Masked Language Model (MLM):
     15% of tokens replaced:
       80% → [MASK]
       10% → random word
       10% → unchanged
     Predict original token at masked positions
     Loss: CE on masked positions only

  2. Next Sentence Prediction (NSP):
     Input: [CLS] Sentence A [SEP] Sentence B [SEP]
     Binary classification: is B the next sentence after A?
     (Later work: NSP is not helpful; dropped in RoBERTa)

  Input representation:
    Token embedding + Segment embedding (A vs B) + Position embedding
    [CLS] token: classification representation (attended over all tokens)
```

**BERT vs GPT directionality**:
```
  BERT (encoder):  bidirectional — attends to all positions in both directions
    → strong representations for classification, NER, QA (understanding)
    → can't generate left-to-right (masked positions in training)

  GPT (decoder):   causal/autoregressive — attends only to past positions
    → natural for text generation
    → left-to-right language model: P(w_t | w_1,...,w_{t-1})

  T5 (encoder-decoder): encoder sees full input, decoder generates output
    → general-purpose: translation, summarization, QA all as text-to-text
```

**Fine-tuning**:
```
  Classification: [CLS] → dense → softmax
  Sequence labeling (NER): each token → dense → softmax
  Span extraction (QA): start/end head over all positions
  ≤ 10K labeled examples typically sufficient (BERT features are powerful)
```

---

## 10. Scaling Laws and LLMs

**Kaplan scaling laws** (OpenAI, 2020):
```
  L(N) ∝ N^{-0.076}    (parameters, infinite data)
  L(D) ∝ D^{-0.095}    (data tokens, infinite parameters)
  L(C) ∝ C^{-0.050}    (compute)

  Smooth power laws — no "emergent threshold" in cross-entropy (though accuracy can show thresholds)
```

**Chinchilla** (DeepMind, 2022):
```
  L(N, D) = E + A/N^α + B/D^β

  Optimal for fixed compute C ≈ 6ND:
    N_opt ∝ C^{0.5}
    D_opt ∝ C^{0.5}
    → N ≈ 20D  (train for 20 tokens per parameter)

  GPT-3 (175B, 300B tokens): undertrained — should have used ~3.5T tokens
  Chinchilla (70B, 1.4T tokens): better than GPT-3 with less compute
```

**Emergent abilities**: see 11-DEEP-LEARNING-THEORY.md for full treatment. In NLP:
```
  Chain-of-thought reasoning emerges ~62B params
  Few-shot learning: appears ~100M params (GPT-2 level)
  Instruction following: needs fine-tuning (RLHF, instruction tuning)
```

---

## 11. Decision Cheat Sheet

| Task | Approach | Notes |
|------|----------|-------|
| Text classification | BERT fine-tune | Standard, fast |
| Token classification (NER) | BERT fine-tune | Per-token head |
| Extractive QA | BERT fine-tune | Span head |
| Text generation | GPT fine-tune | Causal LM |
| Seq-to-seq (translation, summarization) | T5 / mT5 | Text-to-text |
| Multilingual | mBERT, XLM-R | Shared multilingual vocab |
| Embedding / semantic similarity | Sentence-BERT | Siamese fine-tuning |
| Very long context | Longformer, BigBird | Sparse attention |
| LLM alignment | RLHF / DPO | See 12-REINFORCEMENT-LEARNING.md |

---

## 12. Common Confusion Points

1. **"Attention in Transformers = attention in Bahdanau Seq2Seq"** — Related but different. Bahdanau: additive attention, RNN context. Transformer: scaled dot-product, fully parallel, no RNN, multi-head. Transformer attention is self-attention — each position attends to all others in the same sequence.

2. **"BERT can be used for generation"** — Standard BERT cannot. It's a bidirectional encoder; autoregressive generation requires causal masking. BART and T5 use encoder-decoder for generation. UniLM/BERT can be adapted but it's not natural.

3. **"Positional encodings encode absolute position"** — Sinusoidal encodings encode absolute position, but have the relative position property (linear transformation). Modern encodings (RoPE, ALiBi) directly encode relative position, which generalizes better.

4. **"Word2Vec captures meaning"** — Word2Vec captures distributional similarity — words in similar contexts. It encodes stereotypes and biases present in the training corpus. "Doctor-nurse" analogy encodes gender bias. "Meaning" in a deep sense is more complex.

5. **"Perplexity is the quality metric for LLMs"** — Perplexity measures held-out likelihood under the model. A lower perplexity model isn't necessarily better at tasks. GPT-4 may have higher perplexity on some domains than a smaller specialized model that still outperforms it on tasks.

6. **"LSTM solves the vanishing gradient problem"** — LSTM mitigates vanishing gradients via the additive cell state pathway. But with very long sequences, gradients can still vanish. Transformers avoid this entirely by having direct connections from every position to every other position.

7. **"Scaling always beats architecture"** — Scaling laws hold for language modeling loss. For specific tasks, architecture choices (e.g., RoPE for long context, mixture-of-experts for efficiency) matter independently of scale. Chinchilla showed it's not just about parameter count.
