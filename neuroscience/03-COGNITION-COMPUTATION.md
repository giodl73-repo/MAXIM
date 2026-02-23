# Cognition & Computation — Neural Codes, Attractor Networks, Predictive Coding

---

## Big Picture

```
BEHAVIORAL OBSERVATION                    NEURAL MECHANISM
(animal learns, perceives, decides)        (spike trains, synaptic weights)
        │                                          │
        └──────────── GAP ──────────────────────────┘

COMPUTATIONAL NEUROSCIENCE fills the gap with three levels:
1. WHAT IS COMPUTED? (Marr's computational level)
2. HOW IS IT REPRESENTED? (algorithmic level — neural codes)
3. HOW IS IT IMPLEMENTED? (physical level — ions, spikes, circuits)
```

---

## Neural Codes

How is information encoded in neural activity?

### Rate Codes

```
DEFINITION: Information carried by average firing rate over a time window T

EVIDENCE FOR RATE CODE:
• Muscle force ∝ motoneuron firing rate
• Orientation tuning curve: V1 neuron fires more to preferred orientation
• Direction tuning: MT cell fires maximally for one direction of motion

LIMITATIONS:
• Slow: 100 ms window → 10 bits/s max per neuron (rate ~ 0-100 Hz)
• Ignores timing of individual spikes
• Metabolically expensive for high rates
```

### Temporal Codes

```
DEFINITION: Information in precise timing of spikes

SPIKE TIMING PRECISION: In many neurons: ±1-2 ms reproducibility
(Mainen & Sejnowski 1995: same current → same spikes in vitro)

PHASE CODING: Spike phase relative to oscillation (theta, 4-8 Hz)
  Hippocampal place cells: spike phase relative to theta wave
  encodes position MORE precisely than rate alone (Jensen & O'Keefe)

SEQUENCE CODES: Ordered spike sequences during quiescent periods
  (hippocampal replay during sleep: spatiotemporal compression ~6-20×)

SPARSE CODE: Only ~1-5% neurons active at any moment
  Maximizes information capacity: log₂(C(N,k)) bits for N neurons, k active
  Energy efficient; but requires pattern completion for noise tolerance
```

### Population Codes

```
VECTOR AVERAGING (direction tuning):
  M1 motor cortex: each neuron has preferred direction d_i
  Population vector: P = Σ r_i · d_i
  Georgopoulos (1986): population vector points toward actual movement direction

PROBABILISTIC (Bayesian) POPULATION CODE:
  r_i ~ Poisson(f_i(s))   where f_i(s) = tuning curve for stimulus s
  Log-likelihood: log p(r|s) = Σ r_i log f_i(s) - Σ f_i(s)
  Optimal decoder: maximum likelihood estimator (Fisher information bound)

DIMENSIONALITY: Neural population activity lives on low-D manifold
  Typical: 100s of neurons, ~10-20 D of actual variance
  "Neural manifold" — revealed by PCA, GPFA, UMAP on population recordings
```

---

## Attractor Networks

### Hopfield Network

Content-addressable associative memory (Hopfield, 1982).

```
ARCHITECTURE: N binary neurons (±1), fully connected
              J_ij = (1/N) Σ_μ ξ_i^μ · ξ_j^μ   (Hebbian learning rule)
              ξ^μ = μ-th stored pattern

DYNAMICS: s_i(t+1) = sign(Σ_j J_ij s_j(t))
          Energy: E = -½ Σ_{ij} J_ij s_i s_j

ATTRACTOR STATES: Stored patterns are energy minima
  Network "falls into" nearest stored pattern → pattern completion

CAPACITY: ~0.14N patterns (Amit, Gutfreund, Sompolinsky)
          Above capacity → spurious attractors (mixtures of patterns)

MODERN VERSION: Krotov-Hopfield (2016), Dense Associative Memory
  E = -Σ F(Σ_i ξ_i^μ s_i) with polynomial/exponential F
  Capacity: ~α N^(p-1) for p-th order → exponential with modern formulation
  → Connection to Transformer attention (Ramsauer et al. 2021)
```

### Continuous Attractor Networks (Ring Attractor)

```
RING ATTRACTOR:
  Neurons arranged in ring; each neuron i has preferred direction θ_i
  Local excitation + surround inhibition → "bump" of activity
  Bump position = encoded angle (head direction, working memory, etc.)

E_i = W_0 + W_1 cos(θ_i - θ_j) (Mexican hat connectivity)

BUMP DYNAMICS:
  Stable: bump stays until perturbed (persistent state = working memory)
  Path integration: velocity input shifts bump continuously
  → Grid cell and head direction cell models use this architecture

CONTINUOUS ATTRACTOR → PATH INTEGRATION:
  dθ/dt ∝ angular velocity input
  Drift = accumulation of integration errors → periodically corrected by sensory cues
```

---

## Predictive Coding

Theory that the brain is a hierarchical predictive machine (Rao & Ballard 1999; Friston 2005+).

```
HYPOTHESIS: Every cortical area maintains a prediction of lower areas' activity.
            Only prediction errors (residuals) are passed upward.

ARCHITECTURE:
  Higher area → sends predictions downward
  Lower area  → computes prediction error
  Error only  → sent back up if prediction ≠ actual

BENEFITS:
  1. Compression: only transmit surprises (efficient coding)
  2. Disambiguates: prior knowledge fills in ambiguous input
  3. Learning: minimizing prediction error = learning the world model

FORMULATION (Free Energy Principle, Friston):
  F = DKL[q(z)||p(z)] - E_q[log p(x|z)]
    = complexity - accuracy (variational free energy)

  Perception: minimize F by updating beliefs q(z)
  Action: minimize F by changing sensory input (acting on world)
  → Unified theory of perception, action, and learning

PREDICTIONS:
  Mismatch negativity (MMN): EEG response to unexpected sounds
  Predictive suppression: V1 activity suppressed for predictable stimuli
  Top-down sharpening: feedback sharpens neural responses (confirmed in macaque)
```

---

## Bayesian Brain Hypothesis

```
CORE CLAIM: Brain computes optimal Bayesian inference
  posterior ∝ likelihood × prior
  p(stimulus | sensory data) ∝ p(sensory data | stimulus) × p(stimulus)

EVIDENCE:
  • Multisensory integration: visual + auditory → Bayes-optimal (Ernst & Banks 2002)
    Weight each modality by inverse variance: ŝ = (σ_A⁻² s_A + σ_V⁻² s_V)/(σ_A⁻² + σ_V⁻²)
  • Perception as prior + likelihood: prior knowledge distorts perception
    (motion aftereffect, Bayesian modeling of motion perception)
  • Motor control: minimum variance prediction (Shadmehr & Wise)

NEURAL IMPLEMENTATION:
  Population codes can implement Bayesian inference (Ma et al. 2006):
  Poisson neurons + linear readout → optimal marginalization
```

---

## Oscillations and Brain Rhythms

```
RHYTHM    FREQ (Hz)  REGION            FUNCTION
Delta     0.5–4      Neocortex, thal   Sleep (slow waves), memory consolidation
Theta     4–8        Hippocampus, EC   Spatial navigation, phase coding, encoding
Alpha     8–12       Visual cortex     Idle state, active inhibition, attention
Beta      12–30      Motor cortex, BG  Motor planning, working memory maintenance
Gamma     30–100     Widespread        Local processing, feature binding, attention
Sharp-wave ripple  ~150-250  CA1       Memory replay, consolidation during sleep

GAMMA OSCILLATIONS: arise from E/I balance (pyramidal cell ↔ PV+ interneuron)
  ING mechanism (interneuron gamma): I→E feedback
  PING mechanism (pyramidal-interneuron gamma): E→I→E cycle
  Attention increases gamma power in attended locations

THETA-GAMMA COUPLING:
  Multiple gamma cycles nested in theta trough
  Each gamma cycle = one "memory item" → multiplexed in theta
  ~7 items in 7 gamma cycles per theta → Miller's 7±2?
```

---

## Reinforcement Learning in the Brain

See 04-AI-BRIDGE.md for full treatment. Key circuit:

```
STATE (cortex, striatum)
   │
   ▼
DOPAMINE SIGNAL = Reward Prediction Error (RPE)
  δ_t = r_t + γ·V(s_{t+1}) - V(s_t)

  δ > 0: got more than expected → dopamine burst → strengthen action
  δ = 0: got exactly what expected → no dopamine change
  δ < 0: got less than expected → dopamine dip → weaken action

Schultz (1997) recording from SNc/VTA dopamine neurons in macaque:
  Naïve monkey: dopamine burst to juice delivery
  After training: burst shifts to conditioned stimulus (CS)
  At expected juice time if no juice: dopamine dip
  → Exactly matches TD-learning prediction error

ORBITOFRONTAL: value estimation (critic)
DORSAL STRIATUM: action selection (actor)
DOPAMINE: RPE broadcast signal → update weights
```

---

## Decision Making

```
DRIFT DIFFUSION MODEL (DDM):
  Decision = accumulation of noisy evidence toward threshold
  dx = μ dt + σ dW    (Wiener process with drift)
  Choose A if x hits upper threshold θ
  Choose B if x hits lower threshold -θ

  Reaction time = time to threshold + non-decision time
  Accuracy = 1/(1 + exp(-2μθ/σ²))
  Speed-accuracy tradeoff: θ ↑ → slower but more accurate

NEURAL CORRELATE:
  LIP neurons (lateral intraparietal area) during random-dot motion task:
  Ramping activity → choice threshold → decision
  Activity perfectly predicts choice even before motion starts (prior)
  Matches DDM predictions quantitatively (Shadlen & Newsome)

2-ALTERNATIVE FORCED CHOICE:
  Network model: two competing integrators with mutual inhibition
  Winner = first to threshold → same as DDM macroscopically
```

---

## Decision Cheat Sheet

| Concept | Formula / rule | Brain region |
|---------|---------------|-------------|
| Population vector | P = Σ r_i d_i | M1 |
| Hopfield capacity | 0.14 N patterns | — (model) |
| Free energy | F = KL[q‖p(z)] − E_q[log p(x\|z)] | Friston model |
| Bayesian integration | ŝ = Σ w_i s_i, w_i ∝ σ_i⁻² | Multisensory cortex |
| TD error | δ = r + γV(s') − V(s) | Dopamine neurons |
| Drift diffusion threshold | θ ↑ → slower, more accurate | LIP, DLPFC |
| Theta-gamma multiplexing | ~7 items per theta cycle | Hippocampus |
