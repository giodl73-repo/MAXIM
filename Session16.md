# Session 16 — Neuroscience

**Date:** 2026-02-22
**Track:** Engineering Sciences — Life Sciences

---

## What This Session Covers

Neuroscience from the ground up: ion channels through cognition to AI connections. The central theme is that the brain is a physical information-processing system — one that evolution optimized over 500 million years for efficiency, robustness, and adaptability in ways we are only beginning to understand and approximate in AI.

---

## Module Index

| File | Topic | Status |
|------|-------|--------|
| `neuroscience/00-OVERVIEW.md` | Field map, levels of analysis, key numbers, why this matters for AI/engineering | ✅ |
| `neuroscience/01-NEURONS-SIGNALS.md` | Ion channels, Hodgkin-Huxley model, action potentials, synaptic transmission, LTP/LTD, STDP | ✅ |
| `neuroscience/02-SYSTEMS-CIRCUITS.md` | Visual system (V1 receptive fields), motor system, cerebellum, basal ganglia, hippocampus (place/grid cells), PFC | ✅ |
| `neuroscience/03-COGNITION-COMPUTATION.md` | Neural codes (rate/temporal/population), attractor networks, predictive coding, Bayesian brain, oscillations, RL in brain | ✅ |
| `neuroscience/04-AI-BRIDGE.md` | CNNs from V1, TD learning from dopamine, Hopfield → Transformers, predictive coding → VAEs, sparse coding → SAEs, grid cells → positional encoding, neuromorphic computing, BCI | ✅ |

---

## Learning Arc

```
Ion channels (01)
   │
   └─→ Action potential → Synaptic transmission → Plasticity (LTP/LTD) (01)
          │
          └─→ Circuits: V1 hierarchy, motor loops, hippocampus, BG (02)
                 │
                 └─→ Computation: neural codes, attractors, predictive coding (03)
                        │
                        └─→ AI bridge: CNNs, RL, Transformers, neuromorphic (04)
```

---

## Key Mental Models

**Levels of analysis (Marr):** What is computed / how / in what substrate. You need all three to understand a system. Neuroscience usually works bottom-up (biology → function); AI usually works top-down (task → architecture). The two meet in computational neuroscience.

**Coincidence detection = Hebbian learning = backprop (approximate):** NMDA receptors are AND gates — they open only when pre AND post are active simultaneously. This implements Hebb's rule in hardware. Backpropagation is the credit-assignment version — biologically approximate, computationally precise.

**Basal ganglia = Actor-Critic:** Direct path (Go) = actor; dopamine RPE = critic signal. Schultz's 1997 dopamine experiments ARE the experimental validation of TD learning in biological hardware.

**Attractor dynamics = memory:** Stable firing states in recurrent networks = stored memories. Pattern completion (CA3) is associative recall. Hopfield networks formalized this; Transformers are the modern, massively scaled version.

---

## MIT / CS Theory Connections

- **Nernst / Goldman equations:** Electrochemistry + thermodynamics. E_X = (RT/zF) ln([X]_out/[X]_in)
- **Hodgkin-Huxley:** ODE system with saddle-node bifurcations. Threshold = dynamical bifurcation, not a fixed value
- **Information theory in neural codes:** Fisher information bounds on decoding precision (Cramér-Rao). Neural population codes saturate Fisher information
- **Variational inference:** Predictive coding = VI hierarchy. Free energy minimization = ELBO maximization
- **Dynamical systems:** Attractor networks are energy-based models. Phase space, limit cycles (oscillations), fixed points (memory states)

---

## Bridges to AI Engineering

| Neural biology | AI system | Notes |
|---------------|-----------|-------|
| V1 oriented filters | CNN conv layer 1 | Exact match; verified empirically |
| Complex cell pooling | Max-pool | Translation invariance |
| V4/IT hierarchy | Deep CNN layers 4-8 | CORnet scores brains |
| Dopamine RPE | TD error δ = r + γV' - V | Schultz 1997 = TD validation |
| Striatal actor | Policy network | Dorsal: habits; ventral: value |
| Hippocampal replay | Experience replay buffer (DQN) | Off-policy learning from memory |
| CA3 attractor | Transformer KV attention | Ramsauer et al. 2021 |
| Sparse V1 coding | Sparse autoencoder for LLM interp. | Anthropic/EleutherAI SAE work |
| Grid cells | Positional encodings (sin/cos, RoPE) | Banino et al. 2018 |
| Spiking neurons | Intel Loihi, IBM TrueNorth | 1000× energy efficiency |
