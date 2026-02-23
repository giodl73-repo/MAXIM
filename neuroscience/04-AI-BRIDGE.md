# Neuroscience → AI Bridge

---

## Big Picture

```
NEUROSCIENCE                        AI / ML

Receptive fields (V1)    ────→     Convolutional layers (CNN)
STDP, Hebbian learning   ────→     Backpropagation (approximate)
TD learning / dopamine   ────→     Q-learning, Actor-Critic RL
Attractor networks       ────→     Associative memory, Hopfield / Transformers
Predictive coding        ────→     Variational autoencoders, world models
Sparse coding            ────→     Autoencoders, dictionary learning
Place / grid cells       ────→     Positional embeddings, spatial representations
Inhibitory interneurons  ────→     Normalization layers, attention gates
Working memory (PFC)     ────→     LSTM memory cells, context in Transformers
```

---

## CNNs from Visual Cortex

### The Hubel-Wiesel → LeCun Path

```
1959: Hubel & Wiesel — cat V1 experiments
  Simple cells: linear oriented filter (Gabor-like), position-specific
  Complex cells: position-invariant (pool simple cells)

1980: Fukushima — Neocognitron
  S-cells (simple, position-specific) alternating with C-cells (complex, pooling)
  → First convolutional + pooling architecture

1989: LeCun — LeNet
  Shared weights + convolution (from simple cells)
  Max-pooling (from complex cells: invariance to small translations)
  Gradient descent training

2012: AlexNet (Krizhevsky, Sutskever, Hinton)
  Deep CNN: 8 layers, GPU training, ImageNet → top-5 error 15.3% vs 26.2% runner-up
  → Modern deep learning era

CNN HIERARCHY MIRRORS VISUAL HIERARCHY:
  Layer 1: Gabor-like edge detectors (as in V1)
  Layer 2: corners, textures (as in V2)
  Layer 4: object parts (as in V4)
  Layer 7+: whole object categories (as in IT)
  (Zeiler & Fergus 2014: visualizing CNN features; matches visual system)
```

### What CNNs Got Wrong (and Neuroscience Helps)

```
ADVERSARIAL EXAMPLES: Small pixel perturbation → wrong class
  Visual system far more robust → different invariance mechanisms?
  Possible neural fix: feedback/recurrent connections (V1↔higher)

TEXTURE BIAS: CNNs heavily texture-biased; humans shape-biased
  (Geirhos et al. 2019)
  Fix: data augmentation, shape-biased training, style transfer

VENTRAL vs DORSAL: CNNs mostly capture ventral ("what")
  Dorsal stream ("where/how") less well modeled
  Action-recognition models, spatial transformers → progress

RECURRENCE: Most CNNs feedforward; cortex has massive recurrent connections
  Recurrent CNNs (Liao & Poggio) match human performance on occluded images
  → CORnet-S (DiCarlo lab) best brain-score on V1-V4-IT benchmarks
```

---

## Reinforcement Learning from Dopamine

### Temporal Difference Learning

**Schultz et al. (1997)** — the key experiment:

```
PHASE 1 (Untrained):
  CS → [no response]
  Juice (US) → dopamine burst  ← "reward surprise"

PHASE 2 (Training, CS predicts US):
  CS → dopamine burst  ← prediction shifts to CS
  Juice → [no change]  ← expected → no RPE

PHASE 3 (CS but no US):
  CS → dopamine burst
  Expected juice time → dopamine dip  ← negative RPE

This is EXACTLY the TD-learning prediction error:
  δ_t = r_t + γ V(s_{t+1}) - V(s_t)
```

### Actor-Critic Architecture in Basal Ganglia

```
CRITIC (Ventral striatum / nucleus accumbens):
  V(s): state value function
  Receives dopamine δ as training signal
  Updates: ΔV(s) = α δ

ACTOR (Dorsal striatum / putamen):
  π(a|s): action policy
  Modulated by dopamine: D1 → potentiate; D2 → suppress
  Updates: Δπ ∝ δ × eligibility trace

TD ERROR BROADCAST:
  Dopamine neurons in SNc/VTA project broadly:
  → Striatum: update action values / policies
  → PFC: update working memory contents
  → Hippocampus: modulate memory formation (novelty / reward)
  → Amygdala: update fear/reward associations

SEROTONIN:
  Possible role: discount factor γ (patience vs impulsivity)
  5-HT agonists → increased patience (Daw et al. model)
  Also encodes expected reward over longer timescales (Lüth et al.)
```

### Deep RL Connection

```
DQN (Mnih et al. 2014, DeepMind): Q(s,a) from raw pixels via CNN
  Explicitly inspired by dopamine + basal ganglia architecture
  Experience replay: random sampling from buffer
  → Echoes hippocampal replay during sleep (consolidation)
  Target network: stabilizes training
  → Echoes two-timescale learning (fast hippocampus, slow cortex)

SUCCESSOR REPRESENTATION (SR):
  M(s,s') = expected future state occupancy
  V(s) = Σ_s' M(s,s') R(s')
  → Separates transition model from reward function
  Hippocampal prediction of future states (Stachenfeld et al. 2017)
  Predicts hippocampal remapping patterns in reward learning
```

---

## Hopfield Networks → Transformers

```
CLASSIC HOPFIELD (1982):
  Energy: E = -½ Σ_{ij} W_{ij} s_i s_j
  Capacity: 0.14 N patterns (linear)

MODERN HOPFIELD (Krotov & Hopfield 2016, Ramsauer et al. 2021):
  Energy: E = -Σ_μ F(Σ_i ξ_i^μ s_i) + ½ s·s
  F(x) = x^p (polynomial) or exp(x) (exponential)
  Capacity: O(N^(p-1)) for polynomial → EXPONENTIAL for exp

TRANSFORMER SELF-ATTENTION as Hopfield retrieval:
  One update step of modern Hopfield network with exp(·):
  y = softmax(β ξ^T s) · ξ  → matches attention: Attention(Q,K,V) = softmax(QK^T/√d) V

  Mapping:
    Patterns ξ → Keys K
    Query s   → Query Q
    Values V  → stored patterns
    β = 1/√d_k (temperature = 1/√d_k)

  → Self-attention IS a Hopfield memory retrieval step
  → Transformers stack many such retrieval layers
  → Context length = number of patterns stored in KV cache

BIOLOGICAL PARALLEL:
  CA3 autoassociative attractor (mossy fiber → recurrent collaterals)
  Completes partial patterns → exact Hopfield behavior
  CA1 + Hopfield-like: pattern separation + completion balance
```

---

## Predictive Coding → Generative Models

```
BRAIN AS GENERATIVE MODEL:
  Hierarchy of predictions:
  PFC → predicts → sensory cortex
  Each area: prediction (top-down) vs error (bottom-up)

  Friston's Free Energy Principle:
  Organisms minimize free energy (= surprise = negative evidence lower bound)

  F = -ELBO = KL[q(z)||p(z)] - E_q[log p(x|z)]
  = Complexity + Accuracy^{-1}

  PERCEPTION: gradient descent on F wrt posterior q(z)
              ≈ Variational inference

  LEARNING: gradient descent on F wrt generative model parameters
            ≈ Variational autoencoder (VAE) training

  ACTION: minimize F by changing x (acting on world)

VAE = Generative model with amortized inference
  → Bottom-up encoder ≈ error units (prediction error)
  → Top-down decoder ≈ prediction units (generative model)
```

---

## Sparse Coding → Dictionary Learning

```
SPARSE CODING HYPOTHESIS (Olshausen & Field, 1996):
  V1 learns to represent natural images with sparse, overcomplete bases
  min ||x - Φa||² + λ||a||₁
  x = image patch, Φ = dictionary, a = sparse coefficients, λ = sparsity penalty

RESULT: Learned dictionary Φ consists of oriented Gabor wavelets
        → Matches V1 simple cell receptive fields!
        → Emerged purely from statistics of natural images

AI CONNECTIONS:
  LASSO (regression): same L1 penalty
  Sparse autoencoders (SAE): used for mechanistic interpretability of LLMs
    → Find sparse linear representation of transformer internals
    → "Superposition hypothesis": features stored in superposition of neurons
    → SAE disentangles → finds human-interpretable features
  K-SVD: dictionary learning algorithm → compressed sensing
```

---

## Grid Cells → Positional Encodings

```
GRID CELL CODE:
  Hexagonal tiling at multiple scales → "multi-scale place code"
  Dead reckoning: path integration without landmarks
  Low error over long distances due to redundant multi-scale representation

TRANSFORMER POSITIONAL ENCODING (Vaswani et al. 2017):
  PE(pos,2i)   = sin(pos / 10000^{2i/d})
  PE(pos,2i+1) = cos(pos / 10000^{2i/d})
  Multi-frequency sinusoidal → analogous to multi-scale grid code!

RECENT WORK:
  DeepMind (Banino et al. 2018): trained RL agent for navigation
  Agent spontaneously develops grid-like representations in LSTM hidden layer
  → Suggests grid-like code is computationally optimal for spatial navigation

RoPE (Rotary Position Embedding, modern transformers):
  Encodes relative positions via rotation in complex space
  → Even closer analog to phase-coded grid-cell representation
```

---

## Neuromorphic Computing

```
MOTIVATION: GPUs burn 300-700W for inference; brain uses ~20W for vastly more
APPROACH: Build hardware that mimics neural computation

SPIKING NEURAL NETWORKS (SNN):
  Neurons communicate by spikes (binary events), not continuous values
  Energy: proportional to spike count (event-driven, sparse)
  Temporal dynamics: inherent time constants, no backprop through time needed

HARDWARE:
  Intel Loihi (2018, Loihi 2 2021):
    128K neurons (Loihi), 1M neurons (Loihi 2)
    Spike-based, on-chip learning (STDP, SDP)
    ~1000× more energy-efficient than GPU for sparse spiking workloads

  IBM TrueNorth (2014):
    4096 cores, 1M neurons, 256M synapses
    70 mW at 46 billion synaptic operations/sec

  BrainScaleS (Heidelberg): analog, 10,000× real-time
  SpiNNaker (Manchester): ARM-based digital, 1M cores

CURRENT LIMITATIONS:
  Training SNNs with backprop: non-differentiable spikes → surrogate gradient methods
  Accuracy gap vs ANNs (closing for some tasks)
  Killer app: always-on edge inference (IoT, wearables, robotics)
```

---

## BCI (Brain-Computer Interfaces)

```
NEURAL DECODING (BrainGate, Neuralink):
  Record spikes from motor cortex → decode intended movement
  Spike sorting: identify single units from multi-electrode arrays

  DECODE PIPELINE:
  Multi-electrode array (Utah array, 96 electrodes)
    → Spike detection (threshold crossing)
    → Spike sorting (PCA + clustering or template matching)
    → Population activity vector
    → Linear decoder (ridge regression or Kalman filter)
    → 2D cursor position / velocity

  Performance: ~3–4 bits/s, sufficient for text entry
  Record: T5 patient (Francis) 90 words/min with Utah array + LLM correction (2023)

  LFP-BASED BCI: local field potential (bulk signal) + deep learning → competitive
  EEG-BASED: non-invasive, low bandwidth (~1-2 bits/s), P300 speller

STIMULATION:
  Deep Brain Stimulation (DBS): high-freq stimulation of STN/GPi for Parkinson's
  Cochlear implant: electrical stimulation of auditory nerve
  Visual cortex: phosphene mapping (Dobelle) → primitive visual prosthetic
```

---

## Decision Cheat Sheet

| AI Concept | Neural Inspiration | Key Paper |
|------------|-------------------|-----------|
| CNN | V1 simple/complex cells, hierarchy | Hubel & Wiesel 1959, LeCun 1989 |
| Max-pooling | Complex cell translation invariance | Fukushima 1980 |
| TD learning | Dopamine RPE | Schultz et al. 1997 |
| Actor-Critic | Basal ganglia dorsal/ventral striatum | Barto 1983, Houk et al. 1995 |
| Experience replay | Hippocampal sleep replay | McClelland et al. 1995, Mnih 2015 |
| Attention / Transformer | Modern Hopfield / CA3 pattern completion | Ramsauer et al. 2021 |
| VAE | Predictive coding / Free Energy | Friston 2005, Kingma & Welling 2014 |
| Sparse autoencoders | Sparse coding in V1 | Olshausen & Field 1996 |
| Positional encoding | Grid cell multi-scale code | Banino et al. 2018 |
| Neuromorphic (Loihi) | Spiking neurons, STDP | Mahowald & Douglas 1991 |
