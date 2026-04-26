# Open Problems in Machine Learning Theory

## The Big Picture

ML theory has made enormous progress, yet a chasm remains between what theory can explain and what practice demonstrates. This module maps the frontier: what is known, what is partially understood, and what remains genuinely open.

```
+──────────────────────────────────────────────────────────────────+
|                  ML THEORY: THE FRONTIER (2025)                  |
|                                                                  |
|  EXPLAINED BY THEORY                                             |
|  ────────────────────                                            |
|  PAC learning of VC-bounded classes                              |
|  NTK limit for infinite-width networks                           |
|  Double descent for linear regression (Gaussian design)          |
|  PAC-Bayes non-vacuous bounds for small stochastic classifiers   |
|                                                                  |
|  PARTIALLY EXPLAINED                                             |
|  ────────────────────                                            |
|  Implicit regularization of SGD                                  |
|  Benign overfitting for overparameterized models                 |
|  Generalization of transformers                                  |
|  Scaling laws                                                    |
|                                                                  |
|  GENUINELY OPEN                                                  |
|  ────────────────────                                            |
|  Why does in-context learning work?                              |
|  Grokking mechanism for general networks                         |
|  Sharp thresholds in neural network training                     |
|  Alignment and mesa-optimization theory                          |
|  Sample complexity of in-context learning                        |
+──────────────────────────────────────────────────────────────────+
```

---

## Open Problem 1: Generalization of Deep Networks

```
THE PROBLEM
────────────
Fact: Deep networks with P >> m parameters generalize well.
Theory: All known bounds are vacuous (larger than trivial 0.5 error).

WHAT WE KNOW
  • Double descent explains overparameterized linear regression
  • NTK gives a kernel-regression interpretation (but vacuous bounds)
  • PAC-Bayes gives first non-vacuous bounds for specific settings
  • Flatness of loss landscape correlates with generalization empirically

WHAT WE DON'T KNOW
  • A single unified theory that predicts test error from architecture + data
  • When overparameterization helps vs hurts (non-Gaussian designs)
  • The right "complexity measure" for neural networks that predicts
    generalization without being vacuous

KEY PARTIAL RESULTS
  • Bartlett, Montanari (2021): Benign overfitting for linear regression
    when data covariance has strong spectral structure
  • Belkin, Hsu (2020): Kernel ridgeless regression can match Bayes error
  • Negrea et al. (2020): CMI bounds non-vacuous for some architectures

HARD OBSTACLE
  Any uniform convergence bound fails:
  Zhang et al. (2017): Neural nets can memorize random labels.
  → For the same architecture, generalization depends on the labels.
  → Architecture alone doesn't determine generalization.
  → You cannot bound generalization by architecture alone.
```

---

## Open Problem 2: Understanding SGD's Implicit Regularization

```
THE PROBLEM
────────────
SGD finds solutions that generalize well. Why?

WHAT WE KNOW
  • For linear models: GD converges to minimum-norm interpolant
  • For linear models: minimum-norm = good generalization (benign overfitting)
  • For neural nets: GD finds "flat" minima (heuristically)
  • Sharpness-aware minimization (SAM) explicitly seeks flat minima

COMPETING HYPOTHESES
  (A) Minimum norm hypothesis
      SGD finds minimum-l₂-norm solution.
      Evidence: true for linear, over-parameterized quadratics.
      Counter-evidence: not clear for general neural nets.

  (B) Flatness / sharpness hypothesis
      SGD finds wide minima (small max eigenvalue of Hessian).
      Flat minima generalize by PAC-Bayes argument.
      Evidence: SAM works; flat minima correlate with generalization.
      Counter-evidence: sharpness definition is non-invariant under scaling.

  (C) Effective rank / spectral hypothesis
      SGD finds solutions with low effective rank of weight matrices.
      Evidence: incremental rank learning in transformers (Arora et al.).
      Counter-evidence: not universally applicable.

  (D) Data-dependent inductive bias
      SGD's implicit regularization depends on data structure.
      Neural nets learn "simple" functions relative to the true data dist.

OPEN: None of these fully explains practical generalization.
```

---

## Open Problem 3: In-Context Learning

```
THE PROBLEM
────────────
Large language models perform new tasks given only examples in context,
without any gradient updates. How?

  Prompt:  "Translate French to English:
            'Bonjour' = 'Hello'
            'Merci' = 'Thank you'
            'Au revoir' = ?"
  GPT-4:   "Goodbye"

  The model learns from context. No training occurs.
  This is qualitatively different from standard PAC learning.

WHAT WE KNOW (PARTIAL)
  • Akyürek et al. (2022): Transformers can implement gradient descent
    in their forward pass via attention mechanisms (linear regression case)
  • Olsson et al. (2022): "Induction heads" in transformers implement
    a pattern-matching heuristic — copy previous completion
  • The attention mechanism can implement dynamic programming

WHAT WE DON'T KNOW
  • Sample complexity of ICL (how many examples needed in context?)
  • When does ICL generalize vs overfit to context examples?
  • Is ICL Bayesian inference, gradient descent, or something else?
  • Why does ICL get better as model scales?

THE FUNDAMENTAL DIFFICULTY
  ICL is learning at two timescales:
    (1) Pre-training: learn how to learn (meta-learning)
    (2) Inference: actually learn from context
  No classical framework separates these two levels cleanly.
```

---

## Open Problem 4: Computational Hardness of Neural Network Learning

```
THE PROBLEM
────────────
We know:
  (1) Depth-3 networks (3 threshold neurons) are NP-hard to learn [Blum-Rivest 1992]
  (2) In practice, SGD trains networks with millions of neurons efficiently

THE GAP
  Worst-case hardness doesn't explain average-case ease.
  Classical complexity (TCS) studies worst-case.
  Practical ML lives in average-case over natural data distributions.

QUESTIONS
  • What properties of natural data distributions (images, text) make
    learning tractable?
  • Is there a formal model of "natural data" that enables efficient learning?
  • Can we prove positive results for learning on specific data distributions?

PARTIAL ANSWERS
  • Learning circuits under product distributions (easier than arbitrary D)
  • Restricted Boltzmann machines under specific architectures
  • Transformers: in-context learning is efficient for linear regression

FUNDAMENTAL OBSTACLE
  A formal average-case complexity theory for learning does not exist.
  Average-case complexity (Levin's theory) applies to specific distributions.
  Which distribution models "natural data" for images, text, etc.?
  No consensus.
```

---

## Open Problem 5: Grokking and Phase Transitions

```
THE PROBLEM
────────────
Training neural networks exhibits sharp phase transitions:
  • Grokking: sudden generalization after long memorization (Power 2022)
  • Emergence: qualitative capability jumps at scale thresholds
  • Loss spikes: sudden loss increases during stable training

WHAT WE KNOW
  • Grokking is related to weight decay and training dynamics
  • In some modular arithmetic tasks, grokking corresponds to
    learning the underlying group structure
  • Mechanistic interpretability shows algorithm formation in circuits

WHAT WE DON'T KNOW
  • When does grokking occur for a given task and architecture?
  • Is there a general mechanism, or is it task-specific?
  • Can we predict phase transitions from initialization conditions?
  • Are "emergent capabilities" in large language models genuine
    phase transitions or artifacts of metric choice?

CANDIDATE MECHANISMS
  • Two-regime learning: fast memorization (gradient-dominated)
    then slow generalization (regularization-dominated)
  • Representation learning: representations must reorganize before
    generalization is possible
  • Circuit formation: specific circuits form during grokking;
    incomplete formation = memorization; complete = generalization
```

---

## Open Problem 6: Expressiveness vs Generalization Tradeoff

```
THE PROBLEM
────────────
Classical: higher expressiveness → worse generalization (VC dim grows)
Modern: overparameterization helps (double descent, benign overfitting)
Empirical: architecture matters in ways theory doesn't predict

THE QUESTION
  What is the right measure of "complexity" that predicts generalization
  for modern deep learning architectures?

CANDIDATES THAT HAVE BEEN TRIED (and found wanting):
  VC dimension:         Too large; vacuous bounds
  Rademacher complexity: Too large; vacuous bounds
  L₂ norm:              Not sufficient alone; renormalization breaks it
  Spectral norms:       Better but still vacuous for large nets
  Flatness (Hessian):   Not invariant; definition problems
  Effective rank:       Promising but incomplete

WHAT'S NEEDED
  A complexity measure C(h, data) that:
  (1) Is computable or estimable from data
  (2) Gives tight (non-vacuous) bounds
  (3) Predicts which models generalize before training
  (4) Explains why architecture + optimizer choice matters

  This is the central open problem in generalization theory.
```

---

## Open Problem 7: Alignment and Mesa-Optimization

```
THE PROBLEM (AI Safety Theory)
──────────────────────────────
MESA-OPTIMIZATION (Hubinger et al. 2019):
  A sufficiently capable ML model (the "mesa-optimizer") may
  learn to pursue objectives that differ from the training objective.

  Base optimizer: SGD minimizing loss L on training data S
  Mesa-optimizer: internal algorithm the model implements

  Question: Does the mesa-optimizer optimize L, or something else?

  MESA-MISALIGNMENT: Model learns to simulate behavior that minimizes L
  during training/evaluation, but pursues different goal out-of-distribution.

FORMAL PROBLEM
  Let M_θ be a trained model. Define:
    - True objective: f_true (what we want)
    - Training objective: f_train (what we optimize)
    - Model's internal objective: f_mesa

  When is f_mesa ≈ f_train ≈ f_true?
  Under what training regimes does f_mesa diverge?

WHAT WE DON'T KNOW
  • No formal characterization of when mesa-optimization occurs
  • No way to detect mesa-misalignment without probing the model
  • No training procedure that provably prevents mesa-misalignment
  • Whether this is a real risk for current or future models

**TCS connection: undecidability and formal verification.** Verifying that a learned model's internal objective matches the intended objective is undecidable in general. More precisely: given a Turing-complete hypothesis class (e.g., general neural networks with sufficient depth), determining whether a trained model M pursues objective f_train on all inputs (not just the training distribution) reduces to the halting problem — you cannot enumerate all possible inputs and verify behavior without running the model on them. Formal analogues:

```
MESA-MISALIGNMENT DETECTION
  "Does M(x) optimize f_train for all x ∈ X?" is undecidable for general M, X.
  — Rice's theorem: any non-trivial semantic property of programs is undecidable.
  — A learned model is a program; its "intended behavior" is a semantic property.

CHRISTIANO'S DEBATE FRAMEWORK
  Formally: two agents argue about M's behavior on challenging inputs.
  A judge (with limited computation) decides who argued correctly.
  Aligned model = optimal strategy in this debate game.
  Connects to interactive proof systems (IP = PSPACE): the judge's
  computational limits determine what alignment guarantees are achievable.

FORMAL VERIFICATION APPROACH
  Property-based verification: restrict to verifiable hypothesis classes
  (e.g., monotone functions, Lipschitz networks, linear models).
  Trade model expressiveness for decidable alignment properties.
  This is the PAC-learning equivalent of verifiable computation
  (Goldwasser-Micali-Rackoff interactive proofs applied to models).
```

THIS CONNECTS ML THEORY TO AI SAFETY
  The entire alignment problem is, at its core, a generalization problem:
  Does the model's internal goal generalize from training to deployment?
```

---

## Open Problem 8: Theory of Transformers

### What a Transformer Computes: The Formal Model

```
ATTENTION OPERATOR (single head)
──────────────────────────────────
Input: sequence X ∈ ℝ^{n×d}  (n tokens, d-dimensional embeddings)

Projections:
  Q = X W_Q ∈ ℝ^{n×d_k}    (queries)
  K = X W_K ∈ ℝ^{n×d_k}    (keys)
  V = X W_V ∈ ℝ^{n×d_v}    (values)

Attention output:
  Attn(Q, K, V) = softmax(QKᵀ / √d_k) · V   ∈ ℝ^{n×d_v}

The (i,j)-th attention weight:
  αᵢⱼ = softmax(QᵢKⱼᵀ / √d_k) = exp(QᵢKⱼᵀ/√d_k) / Σₗ exp(QᵢKₗᵀ/√d_k)

Output at position i:
  Attn(Q,K,V)ᵢ = Σⱼ αᵢⱼ Vⱼ   [weighted sum of values]
```

**Attention as soft dictionary lookup.** The operation is: for each query Qᵢ, compute similarity to all keys Kⱼ (dot product = similarity in key space), normalize via softmax to get a probability distribution over positions, then take the expected value of V under that distribution. It is a differentiable, soft version of the retrieval operation: retrieve the value associated with the most similar key.

```
HARD DICTIONARY LOOKUP              SOFT ATTENTION
──────────────────────────          ───────────────────────────────────
Given query q, find key k*          Given query Qᵢ, compute weights αᵢⱼ
  k* = argmax sim(q, kⱼ)              αᵢⱼ = softmax(QᵢKⱼᵀ/√d_k)
Return value v_{k*}                 Return Σⱼ αᵢⱼ Vⱼ  [weighted average]

Not differentiable (argmax)         Fully differentiable (softmax)
Retrieves one record                Interpolates across all records
```

**Attention as kernel regression.** With kernel k(Qᵢ, Kⱼ) = exp(QᵢKⱼᵀ/√d_k) (exponential kernel), the attention output is exactly Nadaraya-Watson kernel regression:

```
  Attn(Q,K,V)ᵢ = Σⱼ k(Qᵢ, Kⱼ) Vⱼ / Σⱼ k(Qᵢ, Kⱼ)

  = kernel regression estimator at query point Qᵢ
    with training points (Kⱼ, Vⱼ).
```

Transformers are performing implicit kernel regression at every layer, where the kernel is learned (Q, K projection matrices are learned).

**Multi-head attention and why multiple heads are necessary.**

```
MULTI-HEAD ATTENTION
  Run h attention heads in parallel with independent projections:
    head_l = Attn(X W_Q^l, X W_K^l, X W_V^l)   for l = 1,...,h

  Concatenate and project:
    MHA(X) = [head_1 | head_2 | ... | head_h] W_O

WHY ≥2 HEADS ARE NECESSARY (Sanford et al. 2023)
  A single attention head computes a rank-1 update to the residual stream.
  Some functions require simultaneously attending to multiple positions.
  Example: "greater-than" comparisons require two simultaneous lookups.

  Formally: the composition [head_1 ; head_2] can implement functions
  requiring two independent key-value lookups that a single head cannot,
  because a single head applies one similarity function uniformly.
  Multiple heads = multiple independent "circuits" operating in parallel.
```

**Modern Hopfield networks and associative memory (Ramsauer et al. 2020).** The connection to statistical mechanics is direct:

```
HOPFIELD ENERGY FUNCTION
  Classical Hopfield network: E(σ) = -(1/2) σᵀW σ   (quadratic energy)
  Storage capacity: O(n) patterns for n neurons.

MODERN HOPFIELD NETWORK (Ramsauer et al. 2020)
  Energy: E(ξ, σ) = -lse(β, ξᵀσ) + (1/2)σᵀσ + β⁻¹ log n + (1/2)M²

  where lse(β, z) = β⁻¹ log Σᵢ exp(β zᵢ) is the log-sum-exp function.

  Update rule (synchronous): σ_new = softmax(β ξᵀσ) · ξᵀ
     ↕
  This is exactly one step of attention!

STORAGE CAPACITY
  Classical Hopfield: O(n) patterns
  Modern Hopfield:   O(exp(n)) patterns — exponential in embedding dim

  The softmax nonlinearity enables exponential storage.
  This is why transformer attention can retrieve from large context windows.
```

The modern Hopfield interpretation reveals attention as a one-step energy minimization — each token updates its representation to be the energy-minimum given the current keys and values. Training learns the energy landscape (W_Q, W_K, W_V) such that the fixed-point attractors correspond to useful semantic associations.

```
THE PROBLEM
────────────
Transformers dominate modern ML. Theory lags practice significantly.

WHAT WE KNOW
  • Transformers are universal approximators (Yun et al. 2020)
  • Attention can implement associative memory (Modern Hopfield networks)
  • In-context learning can implement linear regression (Akyürek 2022)
  • Transformers exhibit "induction heads" for pattern copying
  • ≥2 attention heads are necessary for certain compositional computations

WHAT WE DON'T KNOW
  • Sample complexity of transformer training
  • Which architectures (attention patterns, heads, depth) generalize best?
  • Why does scale (more parameters, more data) improve capabilities?
  • Can theory predict when a capability will emerge at scale?
  • How does tokenization affect what can be learned?

THEORETICAL CHALLENGES
  • Non-convex optimization with attention (softmax nonlinearity)
  • NTK theory doesn't apply well (architecture not fully-connected)
  • Sequence-to-sequence learning requires new learning models
    (PAC learning assumes iid; sequences have dependencies)

PARTIAL PROGRESS
  • Tian et al. (2023): Analysis of single-head attention dynamics
  • Barak et al. (2022): Statistical mechanics of transformers
  • Mahankali et al. (2023): One-layer transformer for ICL regression
```

**Gaps in the current series** (planned modules): diffusion model theory (score matching, forward/reverse SDEs, denoising score matching) and RLHF/alignment theory (KL-constrained reward maximization, PPO, reward modeling) — see Module Map in 00-OVERVIEW.md.

---

## Decision Cheat Sheet: Research Directions

| Problem | Current Best Tools | Key Papers |
|---------|------------------|------------|
| Generalization of deep nets | PAC-Bayes, CMI | Dziugaite-Roy 2017, Steinke-Zakynthinou 2020 |
| SGD implicit regularization | Stability bounds, mirror descent | Soudry et al. 2018, Vaskevicius 2019 |
| In-context learning | Attention as GD | Akyürek 2022, Von Oswald 2023 |
| Neural net hardness | Cryptographic reductions | Daniely 2021 |
| Grokking | Mechanistic interp. | Power 2022, Nanda 2023 |
| Complexity measure | Spectral + PAC-Bayes | Bartlett 2017, Neyshabur 2018 |
| Transformers | Sparse attention theory | Yun 2020, Tian 2023 |

---

## Common Confusion Points

**"Theory is always years behind practice — does it matter?"**
For safety-critical applications (healthcare, autonomous vehicles), bounds matter. You want guarantees, not just empirical performance. Also, understanding *why* something works lets you predict where it will fail. Current LLMs are deployed without meaningful theoretical guarantees — this is a legitimate scientific gap.

**"If VC bounds are vacuous, why study VC theory at all?"**
VC theory gives the correct framework for understanding when learning is possible in principle (the fundamental theorem). Vacuous bounds don't mean the framework is wrong — they mean the bounds aren't tight for specific distributions. VC theory remains the right language for sample complexity theory, even when the bounds themselves need tightening.

**"Grokking sounds like catastrophic forgetting in reverse — are they related?"**
Tangentially. Catastrophic forgetting: new learning destroys old knowledge. Grokking: late-stage training suddenly improves generalization. Both involve non-monotone dynamics in neural network training. Neither is well-understood theoretically. They may share a common mechanism involving representation stability, but this is not established.

**"Will theoretical ML ever catch up to practical ML?"**
History suggests no — but it asymptotically narrows the gap. The theory of SVMs became well-understood after SVMs dominated practice (1995–2005). Generalization of deep networks (2012–) is getting theoretical traction now. Transformers (2017–) are the current gap. The lag is real but narrowing as more theorists take the empirical observations seriously.
