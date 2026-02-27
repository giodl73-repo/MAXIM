# Information Theory → ML, Cryptography & Quantum

---

## Big Picture

```
INFORMATION THEORY
        │
        ├──→ MACHINE LEARNING
        │    Cross-entropy loss = negative log-likelihood = expected code length
        │    KL divergence = training objective (VAE, RNVP, EM)
        │    Mutual information = feature relevance, IB principle
        │    MDL = model selection criterion
        │
        ├──→ CRYPTOGRAPHY
        │    Perfect secrecy = H(key) ≥ H(plaintext) (Shannon 1949)
        │    Computational secrecy = poly-time distinguishability
        │    Entropy as randomness source (key generation, IV)
        │    AES: Shannon's confusion+diffusion, modern standard
        │
        └──→ QUANTUM INFORMATION
             von Neumann entropy S(ρ) = -Tr(ρ log ρ)
             Holevo bound: I(X;Y_quantum) ≤ S(ρ) − Σ pᵢ S(ρᵢ)
             Quantum channel capacity, quantum error correction
             BB84 key distribution: information-theoretically secure
```

---

## Information Theory → Machine Learning

### Cross-Entropy Loss = Optimal Code Length

```
MODEL: q_θ(y|x) = neural network output (softmax probabilities)
TRUE DIST: p(y|x)

CROSS-ENTROPY LOSS:
  L(θ) = E_{(x,y)~data} [-log q_θ(y|x)]
        = H(p, q_θ) = H(p) + KL(p||q_θ)

INTERPRETATION:
  H(p): irreducible entropy of true distribution (cannot optimize)
  KL(p||q_θ): extra bits from using model q instead of true p
  → Minimizing cross-entropy = minimizing KL(p||q_θ) = MLE!

  Optimal code: assign -log q_θ(y|x) bits to label y → Huffman-optimal
  Neural network training = finding optimal compressor for labels given inputs

CATEGORICAL CROSS-ENTROPY (classification):
  L = -Σ_c y_c log q_c   (y = one-hot, q = softmax outputs)
  = -log q_{true class}   (just the log prob of correct class)

BINARY CROSS-ENTROPY:
  L = -y log q - (1-y) log(1-q)   (y ∈ {0,1})
  = h(y,q) = binary cross-entropy
```

### KL Divergence in Generative Models

```
MAXIMUM LIKELIHOOD:
  max_{θ} E[log p_θ(x)] = min_{θ} KL(p_data || p_θ)   (forward KL)
  → mode-averaging: p_θ spreads to cover all modes of p_data

VARIATIONAL INFERENCE (VI):
  Want: p(z|x) = p(x|z)p(z)/p(x)   (intractable posterior)
  Approximate: q_φ(z|x) ≈ p(z|x)
  Minimize: KL(q_φ(z|x) || p(z|x)) → maximize ELBO

ELBO (Evidence Lower BOund):
  log p(x) ≥ E_q[log p(x|z)] - KL(q_φ(z|x) || p(z))
               └──────────────┘   └───────────────────┘
               Reconstruction        Regularization
               (accuracy)            (complexity)

VAE (Variational Autoencoder, Kingma & Welling 2014):
  Encoder: q_φ(z|x) = N(μ_φ(x), σ_φ(x)²)  (amortized inference)
  Decoder: p_θ(x|z)
  Loss: reconstruction + KL to N(0,I)
  KL = ½ Σ (μ² + σ² - log σ² - 1)  (Gaussian-Gaussian KL, closed form)
  Reparameterization: z = μ + σ·ε, ε~N(0,I) → differentiable sampling
```

### Mutual Information in ML

```
FEATURE SELECTION:
  Select features X₁,...,Xk that maximize I(X₁...Xk ; Y)
  mRMR (max Relevance Min Redundancy):
    Score(Xᵢ) = I(Xᵢ;Y) - (1/|S|)Σ_{Xⱼ∈S} I(Xᵢ;Xⱼ)

INFORMATION BOTTLENECK (IB, Tishby et al. 1999):
  Find compressed representation T of X that maximizes I(T;Y) while minimizing I(T;X)
  max I(T;Y) - β I(T;X)
  β controls compression vs accuracy tradeoff
  Deep network layers as information bottleneck (Tishby & Schwartz-Ziv 2017):
    Claim: early layers = representation, later = compression toward labels
    Controversy: result depends on activation function, not universally accepted

CONTRASTIVE LEARNING (SimCLR, MoCo):
  InfoNCE loss ≈ lower bound on mutual information I(z₁;z₂) between views
  L_InfoNCE = -log [exp(z₁·z₂/τ) / Σⱼ exp(z₁·zⱼ/τ)]
  = -I(z₁;z₂) + log(N)   (N = batch size, positive pair vs negatives)
  Training: maximize MI between augmented views → learn invariant representations
```

### Minimum Description Length (MDL)

```
MDL PRINCIPLE: Best model = one that compresses data most
  MDL(M, D) = L(M) + L(D|M)   [total description length in bits]
  = |model| + |data given model|

TWO-PART MDL: encode model + encode residuals with model
  Optimal model minimizes sum → Occam's razor formalized

RELATION TO BIC:
  MDL ≈ -log L(θ̂) + (p/2) log n   (for smooth models, p parameters)
  BIC = -2 log L(θ̂) + p log n
  → MDL = BIC/2 + const: same model selection criterion

NORMALIZED MAXIMUM LIKELIHOOD (NML):
  "Ideal" MDL: encode x as -log[p(x|θ̂(x)) / Σ_{x'} p(x'|θ̂(x'))]
  Minimax regret: NML minimizes worst-case regret over all sequences
  COMP (complexity of model class): -log Z_n where Z_n = normalizing constant

STOCHASTIC COMPLEXITY (Rissanen):
  MDL unifies model selection, compression, and Bayesian inference
  MDL ≈ MAP with Jeffrey's prior for regular models
```

---

## Information Theory → Cryptography

### Shannon's Perfect Secrecy (1949)

```
SYSTEM: plaintext M, key K, ciphertext C = E_K(M)

PERFECT SECRECY: I(M;C) = 0  (ciphertext reveals nothing about plaintext)
  Equivalent: p(M=m | C=c) = p(M=m) for all m, c

THEOREM (Shannon): Perfect secrecy requires H(K) ≥ H(M)
  Proof: H(M|C) = H(M) (perfect secrecy)
         H(K) ≥ H(M|C) = H(M)  (key uniquely determines plaintext from ciphertext)

ONE-TIME PAD: K = uniform random bits, C = M ⊕ K
  • Perfect secrecy (I(M;C) = 0): proved by Shannon
  • Key must be: (1) truly random, (2) as long as M, (3) never reused
  • Two-time pad attack: C₁⊕C₂ = M₁⊕M₂ → statistical attacks break both messages

COMPUTATIONAL SECRECY: relax to "polynomial-time indistinguishable"
  PRF (pseudo-random function): computationally indistinguishable from random
  Semantic security: I(M;C) not exactly 0, but no poly-time adversary can distinguish
  → AES-256 is computationally secure (no known attack better than brute force)
```

### Entropy in Cryptographic Systems

```
KEY GENERATION: keys must have sufficient entropy
  AES-256: requires 256 bits of TRUE entropy from OS random source
  CSPRNG (cryptographically secure PRNG): /dev/urandom, CryptGenRandom
  Entropy sources: hardware interrupts, thermal noise, quantum noise (QRNG)

ENTROPY STARVATION: Low-entropy keys → catastrophic
  Debian OpenSSL bug (2008): removed entropy seeding code → only 32K possible keys
  Predictable IVs: Android Bitcoin wallets (2013) → reused k in ECDSA → private key leaked
  Low-entropy nonces in NIST Dual EC DRBG: suspected NSA backdoor

DIFFERENTIAL ENTROPY and SECURITY:
  Uniform key K over {0,1}^n: H(K) = n bits → maximum entropy
  Password entropy: H("password") ≈ 20 bits (not 64 despite 8 chars)
  → Entropy estimate requires proper character distribution model

HASH FUNCTIONS and ENTROPY:
  SHA-256: 256-bit output → collision resistance: 2^128 operations (birthday)
  Preimage resistance: 2^256 operations
  Entropy compression: SHA-256(x) has at most H(x) bits of entropy (data processing)
  → Hash cannot create entropy, only transform/mix it
```

### Confusion and Diffusion (Shannon)

```
Two design principles for block ciphers (Shannon 1949):

CONFUSION: Each ciphertext bit depends complexly on several key bits
  Implementation: non-linear S-boxes
  AES S-box: x → x^{-1} in GF(2^8) + affine transformation
             8-bit input → 8-bit output, nonlinear, no fixed points, no opposite fixed points

DIFFUSION: Each plaintext bit affects many ciphertext bits
  Implementation: permutation + mixing operations
  AES MixColumns: each output byte = linear combination of 4 input bytes over GF(2^8)
  AES ShiftRows: permute bytes across columns

AES-128 ROUND FUNCTION:
  AddRoundKey → SubBytes (S-box, confusion) → ShiftRows (diffusion) → MixColumns (diffusion)
  × 10 rounds
  Avalanche effect: 1 bit change → ~50% of output bits change (Shannon diffusion achieved)
```

---

## Quantum Information Theory

### Quantum States and Entropy

```
QUANTUM STATE: density matrix ρ (generalizes classical probability distribution)
  Pure state: ρ = |ψ⟩⟨ψ|, rank 1
  Mixed state: ρ = Σᵢ pᵢ |ψᵢ⟩⟨ψᵢ|, Tr(ρ) = 1, ρ ≥ 0

VON NEUMANN ENTROPY:
  S(ρ) = -Tr(ρ log ρ) = -Σᵢ λᵢ log λᵢ
  where λᵢ = eigenvalues of ρ

  S(ρ) = 0: pure state (no classical uncertainty)
  S(ρ) = log d: maximally mixed state (d = dimension)
  Like Shannon entropy but for quantum states

QUANTUM MUTUAL INFORMATION:
  I(A;B) = S(ρ_A) + S(ρ_B) - S(ρ_AB)
  Satisfies analogous inequalities to classical MI
  But: I(A;B) can exceed classical bound due to entanglement correlations
```

### Holevo Bound

```
QUESTION: How much classical information in n qubits?

SUPERDENSE CODING: Alice and Bob share 1 EPR pair (2 qubits entangled)
  Alice sends 1 qubit → Bob receives 2 classical bits
  → 1 qubit + 1 ebit (entanglement) = 2 classical bits

HOLEVO BOUND: Without entanglement, n qubits can convey at most n classical bits
  χ(ε) = S(Σᵢ pᵢ ρᵢ) - Σᵢ pᵢ S(ρᵢ)   (Holevo χ quantity)
  I(X;Y) ≤ χ(ε)   (classical info from quantum ensemble)

QUANTUM CHANNEL CAPACITY:
  C₁ = max χ(ε)   (classical capacity)
  Q = coherent information   (quantum capacity)
  EA-C = max [I(X;Y)] with entanglement-assisted = log d (full entanglement)
```

### BB84 Quantum Key Distribution

```
PROTOCOL (Bennett & Brassard 1984):

1. Alice sends qubits in one of 4 states: {|0⟩, |1⟩, |+⟩, |−⟩}
   Two bases: Z-basis {|0⟩,|1⟩} and X-basis {|+⟩,|−⟩}

2. Bob measures each qubit in random Z or X basis

3. Sieve: Alice and Bob compare bases (public) → keep bits where bases match
   → Raw key: 50% of original bits (random basis agreement)

4. Error correction + privacy amplification
   → Final key: H_∞(K|Eve) bits long

SECURITY:
  No-cloning theorem: Eve cannot copy quantum states → any measurement disturbs state
  Error rate threshold: if QBER > 11%: abort (eavesdropping detected)
  Information-theoretic security: based on quantum mechanics laws, not computational hardness
  → Secure against quantum computers!

KEY RATE: r ≥ 1 - 2h(e)  where e = quantum bit error rate (QBER)
  At e=0.05: r ≥ 1 - 2×0.286 = 0.43 bits per sieved bit

PRACTICAL DEPLOYMENTS:
  ID Quantique, Toshiba: fiber-based QKD
  Chinese Micius satellite (2016): intercontinental QKD over 4600 km
  Limitations: distance (~100 km without quantum repeater), cost, complexity
```

### Quantum Error Correction

```
PROBLEM: Quantum states are fragile (decoherence, noise)
  Cannot clone: no backup copies (no-cloning theorem)
  Continuous errors: bit flip, phase flip, both, arbitrary rotation

SOLUTION: Encode logical qubit into multiple physical qubits

SHOR CODE (1995): [[9,1,3]] code
  Encodes 1 logical qubit into 9 physical qubits
  Protects against arbitrary single-qubit errors (bit flip + phase flip)
  First quantum error-correcting code

STABILIZER CODES (CSS framework):
  Calderbank-Shor-Steane codes
  Encode k logical qubits into n physical qubits
  Error detection: measure stabilizer generators (commuting Pauli operators)
  → Syndrome tells you error without measuring logical state

SURFACE CODE (topological):
  Arranges qubits in 2D grid, local parity checks
  Threshold: ~1% physical error rate → scales to fault-tolerant quantum computing
  Most promising path to large-scale QC (Google Sycamore, IBM Heron)
  Overhead: ~1000 physical qubits per logical qubit at threshold → enormous cost
```

---

## Decision Cheat Sheet

| ML Concept | IT Foundation | Connection |
|------------|--------------|------------|
| Cross-entropy loss | Cross-entropy H(p,q) = H(p) + KL(p\|\|q) | Minimizing loss = minimizing KL = MLE |
| VAE ELBO | Rate-distortion + KL | ELBO = -reconstruction - KL to prior |
| InfoNCE contrastive | Mutual information I(X;Y) | Lower bound on MI |
| MDL / BIC | Kolmogorov complexity | Shortest description = best model |
| IB principle | I(T;X), I(T;Y) | Compress X to keep Y |
| GAN training | JS divergence | min max = minimizing JSD between distributions |
| DDPM (denoising diffusion) | Variational bound (forward KL) | ELBO on data log-likelihood; loss = weighted denoising MSE |
| Score-based models (Song) | Score matching (Hyvärinen) | min E[‖∇log p_θ - ∇log p_data‖²]; equivalent to denoising at each noise level |

| Crypto Concept | IT Foundation | Connection |
|----------------|--------------|------------|
| Perfect secrecy | I(M;C) = 0 | OTP achieves; requires H(K)≥H(M) |
| Semantic security | Computational indistinguishability | Poly-time I(M;C) ≈ 0 |
| AES S-box | Shannon confusion | Nonlinear, high algebraic degree |
| AES MixColumns | Shannon diffusion | Linear diffusion across bytes |
| QBER threshold | Fano inequality | Error rate bounds Eve's information |

---

## Common Confusion Points

**InfoNCE is a lower bound on MI, not MI itself.** Maximizing InfoNCE does not guarantee maximizing true mutual information — the bound can be loose, especially in high dimensions. The gap depends on the critic architecture and batch size.

**The IB "deep learning compresses" claim is contested.** Tishby (2017) proposed that deep learning implicitly performs information bottleneck compression during training. Subsequent work (Saxe et al. 2018) showed this is activation-function-dependent: networks with saturating activations (tanh) exhibit compression; ReLU networks generally do not. Do not treat this as settled theory.

**Perfect secrecy (IT) vs semantic security (computational) are categorically different.** Perfect secrecy (I(M;C) = 0) holds against unbounded adversaries — no computational assumption. Semantic security holds against polynomial-time adversaries only. These are not just "relaxed" versions of each other; they are different frameworks with different threat models.

**GAN "minimizes JSD" holds only at discriminator optimality.** The theoretical result (Goodfellow 2014) assumes the discriminator achieves its optimum at each training step. In practice, the discriminator is never optimal, and the actual training dynamics are a complex saddle-point game, not JSD minimization.
