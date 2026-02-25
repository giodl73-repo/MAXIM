# Connections: Statistical Mechanics, Information Theory, and Machine Learning

## The Big Picture

Statistical mechanics, information theory, and machine learning share a deep mathematical
identity. Boltzmann entropy and Shannon entropy are the same object. The maximum entropy
principle (Jaynes) shows that equilibrium statistical mechanics is Bayesian inference applied
to physical systems. Energy-based models in ML are Boltzmann distributions over configuration
space. The Boltzmann machine is a stochastic Ising model trained by likelihood maximization.
Free energy in physics is the evidence lower bound (ELBO) in variational inference. Stochastic
processes in finance are Langevin equations with market-specific drift and noise. These are not
analogies — they are literal mathematical equivalences.

```
THREE-WAY EQUIVALENCE
═══════════════════════════════════════════════════════════════════════════════

  STATISTICAL MECHANICS          INFORMATION THEORY          MACHINE LEARNING
  ──────────────────────         ──────────────────          ────────────────────
  Boltzmann entropy              Shannon entropy             Categorical cross-entropy
  S = −k Σ pᵢ ln pᵢ             H = −Σ pᵢ log₂ pᵢ          H = −Σ pᵢ log qᵢ

  Partition function Z           Normalizing constant        Model evidence (marginal)
  Z = Σ e^{-βE_i}                                            Z = ∫ p(x|θ) p(θ) dθ

  Helmholtz free energy F        Negative log-evidence       ELBO / Variational bound
  F = −kT ln Z = U − TS          F = −log Z                  F = ⟨log p/q⟩ = KL − log Z

  Boltzmann distribution         Maximum entropy dist.       Energy-based model (EBM)
  P(x) = e^{-E(x)/kT}/Z         P(x) = e^{-λᵢ fᵢ(x)}/Z     P(x) = e^{-E_θ(x)}/Z

  Temperature T                  Lagrange multiplier         Inverse temperature β (noise)

  Gibbs sampling                 MCMC                        Stochastic inference
  Phase transition               Model selection threshold   Generalization transition
```

---

## Boltzmann Entropy = Shannon Entropy

**Shannon (1948)**: The unique measure H of uncertainty/information that is:
1. Continuous in the probabilities pᵢ
2. Maximized for uniform distribution
3. Additive for independent systems

    H = −Σᵢ pᵢ log₂ pᵢ    (bits; same formula, log base 2 instead of natural log)

**Boltzmann-Gibbs entropy**:

    S = −k_B Σᵢ pᵢ ln pᵢ    (nats × k_B)

**Identical mathematical structure**: S = k_B × (ln 2) × H. The factor k_B ln 2 converts from information-theoretic bits to thermodynamic units (J/K).

This is not a coincidence or analogy. Boltzmann's S and Shannon's H are the same measure of uncertainty/missing information, applied to different contexts. The units differ (J/K vs bits) but the formula is the same.

```
ENTROPY AS MISSING INFORMATION:

  Physical interpretation: S = k_B × (information missing about the microstate)
  Given macrostate (T, P, N), we know the macroscopic state.
  But we don't know which microstate among the Ω possible ones.
  Missing information = log₂(Ω) bits = k_B ln Ω thermodynamic entropy.

  Example: 1 mole of ideal gas
  Ω ~ e^{N} where N = 6×10²³
  S ~ Nk_B ~ 10 J/K
  Missing info ~ N bits ~ 10²³ bits (absurdly large — we truly know nothing
  about the microstate)
```

---

## Jaynes Maximum Entropy Principle

E.T. Jaynes (1957) reinterpreted statistical mechanics as Bayesian inference:

**Principle**: The equilibrium distribution is the probability distribution that maximizes entropy (uncertainty) subject to whatever constraints you know.

**Microcanonical ensemble**: Known: energy E (exact). MaxEnt distribution = uniform over microstates with H = E. This is just S = k ln Ω.

**Canonical ensemble**: Known: mean energy ⟨E⟩ = U. Maximize:

    S = −k Σ pᵢ ln pᵢ    subject to: Σ pᵢ = 1, Σ pᵢ Eᵢ = U

Lagrangian (see variational-calculus/03-CONSTRAINTS.md):

    L = −Σ pᵢ ln pᵢ − λ₀(Σ pᵢ − 1) − λ₁(Σ pᵢ Eᵢ − U)

∂L/∂pₙ = 0:  −ln pₙ − 1 − λ₀ − λ₁ Eₙ = 0
⟹  pₙ = e^{−1−λ₀} e^{−λ₁ Eₙ}

From normalization: λ₁ = β = 1/k_BT and e^{−1−λ₀} = 1/Z.

    pₙ = e^{-β Eₙ}/Z    **Boltzmann distribution from MaxEnt**

**Grand canonical ensemble**: Known: ⟨E⟩ = U and ⟨N⟩. Add Lagrange multiplier for ⟨N⟩ → chemical potential μ. Grand canonical distribution emerges.

```
JAYNES VIEW — IMPLICATIONS:

  1. Statistical mechanics is NOT a special branch of physics.
     It is the application of probability theory (Bayesian inference)
     to physical systems with constrained information.

  2. Temperature β is a Lagrange multiplier — the "price" for
     the constraint ⟨E⟩ = U.

  3. The second law follows from entropy maximization:
     When constraints are lifted, entropy increases to the new maximum.

  4. ANY system where you know only certain expectation values
     can be treated by MaxEnt → exponential family distributions.

  BRIDGE TO ML: Exponential family distributions in ML are exactly
  MaxEnt distributions subject to the specified sufficient statistics.
  Logistic regression, Gaussian distributions, Poisson regression —
  all are MaxEnt for different constraint types.
```

---

## Energy-Based Models

In machine learning, an **energy-based model (EBM)** assigns an energy E_θ(x) to each configuration x, with the model distribution:

    P_θ(x) = e^{-E_θ(x)} / Z_θ    where Z_θ = ∫ e^{-E_θ(x)} dx

This is exactly the Boltzmann distribution at β = 1 (or the energy is already measured in units of k_BT).

**Training an EBM**: Maximize log-likelihood:

    ℓ(θ) = Σ_x^{train} log P_θ(x) = Σ_x^{train} [−E_θ(x) − log Z_θ]

Gradient:

    ∂ℓ/∂θ = −∂E_θ(x)/∂θ|_{x=data} + ⟨∂E_θ(x)/∂θ⟩_{model}

```
EBM GRADIENT = DATA MINUS MODEL STATISTICS:

  ∂ℓ/∂θ = −E_data[∇_θ E] + E_model[∇_θ E]

  "Push down" energy of training data.
  "Push up" energy of model samples.

  The model statistics E_model[...] require sampling from P_θ(x).
  → MCMC (Gibbs sampling, Langevin dynamics, HMC).

  This is the contrastive divergence algorithm (Hinton 2002):
  approximate E_model by running MCMC for k steps from data.

  BRIDGE: Training an EBM by contrastive divergence IS:
  - Running a Glauber dynamics (Gibbs sampling of Ising model)
  - For k steps
  - And computing the "correlation with data" vs "correlation at model"

  The physics analogy: "data" = low-energy configurations (ground state).
  "Model" = thermal distribution. Training pushes the model to match data.
```

---

## Boltzmann Machine

A Boltzmann machine is a stochastic recurrent neural network with:
- Visible units v ∈ {0,1}^n (observed data)
- Hidden units h ∈ {0,1}^m (latent variables)
- Symmetric weight matrix W and biases

**Energy function**:

    E(v, h) = −vᵀ W h − bᵀ v − cᵀ h

**Model distribution**:

    P(v, h) = e^{-E(v,h)} / Z    (exactly Boltzmann, β=1)

**Restricted Boltzmann Machine (RBM)**: No visible-visible or hidden-hidden connections. Hidden units are conditionally independent given visible:

    P(hⱼ = 1 | v) = σ(Wⱼ·v + cⱼ)    (sigmoid = Fermi-Dirac at β=1, μ = Wⱼ·v + cⱼ)

```
RBM ↔ PHYSICS CONNECTIONS:

  RBM unit activation P(hⱼ=1|v) = σ(Wⱼ·v + cⱼ)
  ↔ Fermi-Dirac: P(state occupied) = 1/(1+e^{-β(μ−ε)})
     with β=1, μ−ε = Wⱼ·v + cⱼ

  Contrastive divergence training of RBM
  ↔ Gibbs sampling of Ising model

  Deep Boltzmann Machine (stacked RBMs)
  ↔ Hierarchical spin model

  Training RBM by CD = approximate maximum likelihood
  ↔ Equilibrating a physical system at a target temperature
```

---

## Free Energy in ML — Variational Inference

In Bayesian inference, you have a posterior P(z|x) (latent z, observed x) that is intractable. Variational inference introduces a tractable approximate posterior q(z):

**Evidence Lower Bound (ELBO)**:

    log P(x) ≥ ⟨log P(x,z)⟩_{q(z)} − ⟨log q(z)⟩_{q(z)}
               = ⟨log P(x,z)⟩_q + H(q)
               = −F[q]    (free energy!)

where F[q] = ⟨log q/P⟩ = KL(q||P) − log P(x) is the variational free energy.

**The ML ELBO is the physics free energy**:

```
STATISTICAL MECHANICS           VARIATIONAL INFERENCE (ELBO)
─────────────────────────────  ────────────────────────────────────
Free energy F = U − TS         Variational free energy F[q] = ⟨E⟩_q − H(q)
U = ⟨E⟩_P (internal energy)    ⟨E⟩_q (expected energy under q)
S = H(P) (entropy)             H(q) = −Σ q log q (entropy of q)
Boltzmann distribution P*      True posterior P(z|x)
Approximate distribution       Variational family q(z; φ)
Minimize F over distributions  Maximize ELBO over φ
Both are convex optimization   Both are convex optimization

F is minimized by the true P (at T=1).
ELBO is tight when q = P(z|x).
In both cases: the gap is the KL divergence KL(q||P).
```

**Variational Autoencoders (VAE)**: A specific variational inference scheme where:
- The decoder parameterizes P(x|z) (generative model, likelihood)
- The encoder parameterizes q(z|x) (approximate posterior)
- Training maximizes the ELBO: ⟨log P(x|z)⟩ − KL(q(z|x) || P(z))

The ELBO has a physics interpretation: − (energy of reconstruction) + (entropy of latent code relative to prior). Maximizing ELBO = minimizing variational free energy at β = 1.

---

## Connections to Finance — Stochastic Processes

The mathematics of statistical mechanics and financial mathematics are largely identical.

```
PHYSICS ↔ FINANCE DICTIONARY:

  Langevin equation:  dX = μ dt + σ dW_t  (geometric Brownian motion)
  μ = drift (expected return),  σ = volatility (noise amplitude)

  Fokker-Planck equation ↔ Black-Scholes PDE for option pricing
  P(x,t) = prob. density of position → V(S,t) = option value

  Black-Scholes equation:
  ∂V/∂t + (1/2)σ²S² ∂²V/∂S² + rS ∂V/∂S − rV = 0

  This IS a Fokker-Planck equation for the option value.
  "Diffusion coefficient" = (1/2)σ²S²,  "drift" = rS.

  Free energy minimization ↔ Risk-neutral pricing (arbitrage-free)
  Temperature T ↔ Volatility σ (measures uncertainty/fluctuations)
  Partition function Z ↔ Moment generating function of returns
  Ising phase transition ↔ Market crash (collective herding behavior)
```

**Path integral formulation of option pricing** (Feynman-Kac):

The Black-Scholes formula for a European option is:

    V(S₀, 0) = e^{-rT} ∫ payoff(S_T) × P(S_T | S₀) dS_T

where P is the lognormal transition probability — the exact propagator of GBM. This is the path integral formula for the partition function, with time replaced by −iT (Wick rotation connects quantum mechanics to thermal field theory; same Wick rotation connects finance to QM).

---

## Stochastic Gradient Descent as Langevin Dynamics

Mini-batch stochastic gradient descent (SGD) can be analyzed as a discretized Langevin equation:

    θ_{t+1} = θ_t − η ∇L(θ_t; B_t)

where B_t is a random mini-batch. The gradient noise from mini-batching:

    ∇L(θ; B_t) = ∇L(θ) + ξ_t    (true gradient + noise)

The noise ξ_t has variance proportional to η/B (learning rate / batch size).

**Stochastic Gradient Langevin Dynamics** (SGLD, Welling-Teh 2011) adds explicit noise to sample from the posterior:

    θ_{t+1} = θ_t − (η/2) ∇U(θ_t) + √η × N(0, I)

This converges to P(θ) ∝ e^{-U(θ)} (the posterior) rather than just finding a mode. The "temperature" of exploration is controlled by η.

```
SGD ↔ LANGEVIN EQUATION:

  Physics:   γẋ = −∂U/∂x + η(t)   (overdamped particle in potential U)
  SGD:       θ_{t+1} − θ_t = −η ∇L(θ_t; B_t)  (gradient descent with noise)

  Neural network loss L(θ) ↔ Potential energy U(x)
  Network parameters θ     ↔ Particle position x
  Learning rate η           ↔ Time step × 1/γ
  Batch noise               ↔ Thermal noise kT ~ η/B

  At small η: SGD explores the loss landscape.
  Sharp minima ↔ deep potential wells (large Hessian eigenvalues)
  Flat minima ↔ shallow potential wells
  Generalization from flat minima ↔ large entropy basin of attraction

  SGD with large learning rate or small batch size:
  behaves like a high-temperature Langevin dynamics — escapes shallow minima.
  Cooling (decay η) ↔ simulated annealing.
```

---

## Summary Table — The Unified Framework

| Concept | Stat Mech | Information Theory | Machine Learning |
|--------|----------|-------------------|-----------------|
| Uncertainty measure | Entropy S = −kΣp ln p | Shannon H = −Σp log p | Cross-entropy / KL divergence |
| Most probable distribution | Boltzmann e^{-βE}/Z | MaxEnt distribution | EBM P(x) = e^{-E(x)}/Z |
| Partition function | Z = Σ e^{-βE} | Normalizing const | Model evidence |
| Free energy | F = −kT ln Z | Negative log-evidence | ELBO (negative) |
| Temperature | T (controls fluctuations) | — | Learning rate / batch size |
| Sampling | Gibbs/MCMC | MCMC | MCMC / Langevin SGD |
| Phase transition | Symmetry breaking at T_c | — | Generalization transition |
| Order parameter | ⟨m⟩ magnetization | — | Test accuracy, sharpness |
| Spin glass | Frustrated random couplings | — | Non-convex loss landscape |

---

## Decision Cheat Sheet

| Connection | Key identity |
|-----------|-------------|
| Boltzmann ↔ Shannon entropy | S = k_B ln 2 × H (same formula, different units) |
| Canonical ensemble = MaxEnt | Boltzmann P = MaxEnt subject to ⟨E⟩ = U |
| EBM = Boltzmann distribution | P_θ(x) = e^{-E_θ(x)}/Z at β=1 |
| Train EBM by gradient | ∂ℓ/∂θ = −E_data[∇_θE] + E_model[∇_θE] |
| Variational inference ↔ free energy | ELBO = −F[q] = ⟨log P⟩_q + H(q) |
| VAE ELBO decomposition | reconstruction − KL(posterior||prior) |
| Black-Scholes ↔ Fokker-Planck | Same PDE structure, σ = volatility |
| SGD noise ↔ temperature | kT ~ η/B (learning rate / batch size) |
| Simulated annealing | Langevin dynamics with cooling schedule |

---

## Common Confusion Points

**Boltzmann and Shannon entropy are identical, not analogous**: It is common to say "Shannon entropy is analogous to Boltzmann entropy." This undersells the relationship. They are the same functional form, measured in different units. The factor of k_B is just a unit conversion. Jaynes made this precise: equilibrium stat mech IS MaxEnt inference.

**The EBM normalizing constant Z is intractable in high dimensions**: Training requires ⟨∇_θ E⟩_model, which needs samples from the model — an MCMC problem. This is why EBMs are hard to train: unlike directed graphical models (VAEs, diffusion models), the partition function Z is not available in closed form.

**Variational free energy and Helmholtz free energy differ by a sign/normalization**: In physics, F is minimized. In variational inference, ELBO = −F is maximized. The KL divergence KL(q||P) is the gap between the ELBO bound and the true log-evidence. Setting KL = 0 (q = P) achieves equality — the same condition as minimizing the physical free energy achieves the Boltzmann distribution.

**SGD is NOT Langevin dynamics unless noise is deliberately added**: Standard SGD minimizes L — it converges to a local minimum, not to a distribution. SGLD (Welling-Teh) adds explicit noise to sample from P(θ) ∝ e^{-U(θ)}. Without the added noise term, SGD is a gradient flow, not Langevin dynamics. The noise from mini-batches alone does not satisfy detailed balance.
