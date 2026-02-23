# Session 16 — Neuroscience

## Purpose

A graduate-level neuroscience reference for a physicist/mathematician/AI engineer who needs
to understand: how neurons compute, how circuits implement cognition, and critically, the
systematic mapping between biological neuroscience and modern AI. The fourth file (04-AI-BRIDGE)
is the unique contribution — a rigorous, two-way comparison that goes beyond the usual vague
"the brain inspired neural networks" narrative.

## Learner Profile

Giovanni Della-Libera, VP Engineering at Microsoft, MIT double major Math + TCS, age 52.
AI/ML background: transformers, RLHF, agents. Physics background: QM, E&M, statistical mechanics.
Needs: the biological substrate that AI is attempting to implement, with exact mathematical
connections and honest identification of where biology and AI diverge.

## Directory Structure

```
C:\src\reference\neuroscience\
├── 00-OVERVIEW.md            ← Anatomy hierarchy, NT systems, measurement methods, evolution
├── 01-NEURONS-SIGNALS.md     ← Hodgkin-Huxley model, Nernst/GHK, cable theory, synaptic transmission
├── 02-SYSTEMS-CIRCUITS.md    ← Visual system, motor, cerebellum, basal ganglia, hippocampus, LTP
├── 03-COGNITION-COMPUTATION.md ← Hopfield/Ising, predictive coding, FEP, DDM, dopamine RPE, WM, attention
└── 04-AI-BRIDGE.md           ← Systematic neuroscience→AI comparisons across 13 dimensions
```

## Artifact Index

| File | Topic | Status | ~Lines |
|------|-------|--------|--------|
| `00-OVERVIEW.md` | Brain anatomy, NTs, glia, scale, methods, evolution | ✅ Complete | 480 |
| `01-NEURONS-SIGNALS.md` | HH model, Nernst/GHK, cable theory, synaptic transmission | ✅ Complete | 680 |
| `02-SYSTEMS-CIRCUITS.md` | Vision, motor, cerebellum, BG, hippocampus, LTP | ✅ Complete | 680 |
| `03-COGNITION-COMPUTATION.md` | Hopfield, FEP, DDM, dopamine RL, WM, attention, consciousness | ✅ Complete | 720 |
| `04-AI-BRIDGE.md` | 13-dimension bio/AI comparison + open problems table | ✅ Complete | 840 |

## Key Themes

### Biophysics of Computation
The Hodgkin-Huxley model is a system of 4 coupled ODEs that produces action potentials.
This is NOT metaphorical — it's the actual biophysics, derived from voltage-clamp experiments
on squid axon. Every neuroscience computation reduces to this level, then aggregates upward.

### Multiple Levels of Description
Neuroscience has no "correct" level of analysis. Synaptic LTP implements Hebb's rule
implements associative memory implements episodic memory implements spatial navigation.
All these descriptions are simultaneously true. The skill is knowing which level to use.

### The Dopamine-TD Connection
The exact mathematical connection between biological dopamine reward prediction errors and
temporal difference (TD) learning is one of the clearest cases of neuroscience → AI translation.
δ = r + γV(s') - V(s) is computed by dopamine neurons and by PPO value functions. Same equation,
different substrate.

### The AI-Brain Gap
File 04 is deliberately honest about what AI does NOT have: catastrophic forgetting, lack
of sleep consolidation, no oscillatory dynamics, no sparse coding, energy efficiency gap.
This sets research agenda, not just historical credit.

## Key Equations Reference

| Equation | Source | Significance |
|----------|--------|-------------|
| C_m dV/dt = -g_Na m³h(V-E_Na) - g_K n⁴(V-E_K) - ... | Hodgkin-Huxley | Action potential dynamics |
| E_K = (RT/zF)ln([K]_out/[K]_in) | Nernst | Ionic equilibrium potential |
| V_m = (RT/F)ln(P_K[K]_o + ...) | Goldman-Hodgkin-Katz | Resting membrane potential |
| λ = √(r_m/r_i) | Cable theory | Electrotonic length constant |
| E = -½Σ w_ij s_i s_j | Hopfield | Attractor network energy |
| Capacity ≈ 0.14N | Hopfield analysis | Associative memory capacity |
| δ_t = r_t + γV(s_{t+1}) - V(s_t) | Bellman/Schultz | Dopamine = TD error |
| F = KL[q(z)||p(z|x)] - log p(x) | Free Energy Principle | Variational inference = perception |
| dX = μ dt + σ dW_t | Drift-Diffusion | Decision accumulator |

## Session Log

| Date | Activity |
|------|----------|
| 2026-02-22 | Session 16 initiated. All 5 neuroscience modules authored. |
|            | Existing stubs replaced with full reference content. |
|            | Total: ~3400 lines of neuroscience reference. |
|            | 04-AI-BRIDGE includes 13 systematic comparisons and open problems table. |
