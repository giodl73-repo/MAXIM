# Neurons & Signals — Ion Channels, Action Potentials, Synapses

---

## Big Picture

```
STIMULUS
   │
   ▼
RECEPTOR / TRANSDUCTION
(convert physical stimulus → electrical signal)
   │
   ▼
ACTION POTENTIAL GENERATION
(all-or-nothing spike, travels down axon)
   │
   ▼
SYNAPTIC TRANSMISSION
(chemical: neurotransmitter → receptor → postsynaptic potential)
   │
   ▼
INTEGRATION
(dendrites sum EPSPs and IPSPs → decides to fire or not)
   │
   ▼
OUTPUT SPIKE (or not)

KEY: The neuron is an integrate-and-fire device with
     analog integration and binary (spike) output.
```

---

## Membrane Potential

### Ion Gradients

Maintained by Na⁺/K⁺-ATPase (active pump, uses ATP).

```
ION       INSIDE      OUTSIDE    E_rev (Nernst)
Na⁺       12 mM       145 mM     +67 mV
K⁺        155 mM      4 mM       -98 mV
Cl⁻       4 mM        123 mM     -90 mV
Ca²⁺      100 nM      2 mM       +123 mV

Resting membrane potential: V_m ≈ -65 to -70 mV
(dominated by K⁺ leak channels → V_m near E_K)
```

**Nernst equation** (equilibrium potential for ion X):

```
E_X = (RT/zF) ln([X]_out/[X]_in)

At 37°C: E_X = (61.5/z) log₁₀([X]_out/[X]_in) mV

R = 8.314 J/mol·K, F = 96,485 C/mol, z = charge
```

**Goldman equation** (actual V_m with multiple ions):

```
V_m = (RT/F) ln[ P_K[K⁺]_o + P_Na[Na⁺]_o + P_Cl[Cl⁻]_i ]
                [ P_K[K⁺]_i + P_Na[Na⁺]_i + P_Cl[Cl⁻]_o ]

P_X = membrane permeability to ion X
At rest: P_K : P_Na : P_Cl ≈ 1 : 0.04 : 0.45
During AP: P_Na/P_K reverses → V_m swings toward +50 mV
```

---

## Ion Channels

Transmembrane proteins forming selective aqueous pores.

```
CHANNEL TYPES:
┌────────────────────────────────────────────────────────────┐
│ Voltage-gated: open/close based on V_m                    │
│   Na_v (voltage-gated Na⁺): AP upstroke, inactivates fast │
│   K_v (voltage-gated K⁺):   AP repolarization, slow       │
│   Ca_v (voltage-gated Ca²⁺): synaptic release trigger     │
│                                                            │
│ Ligand-gated: open when neurotransmitter binds            │
│   nAChR (nicotinic ACh): Na⁺/K⁺ cation channel           │
│   NMDA-R: Na⁺/Ca²⁺, requires both ligand + voltage        │
│   GABA_A: Cl⁻, inhibitory                                 │
│                                                            │
│ Mechanically-gated: pressure / stretch                     │
│   Piezo1/2: touch, proprioception                         │
│                                                            │
│ Leak / background: always open at rest                    │
│   K2P family: set resting potential                       │
└────────────────────────────────────────────────────────────┘
```

### Channel Selectivity

```
Na_v selectivity filter: DEKA ring (Asp-Glu-Lys-Ala)
  • Na⁺ (diameter 0.19 nm) passes; K⁺ (0.27 nm) blocked
  • Selectivity from dehydration + re-solvation energy difference

K_v selectivity filter: TVGYG sequence (signature in all K channels)
  • 4 backbone carbonyl oxygens replace hydration shell of K⁺
  • K⁺ passes; Na⁺ too small → wrong geometry → blocked
  (Nobel 2003: Roderick MacKinnon — first K-channel crystal structure)
```

---

## Action Potential

### Hodgkin-Huxley Model (1952)

Nobel 1963. Quantitative description of AP generation in squid giant axon.

```
CONDUCTANCE-BASED MODEL:

C_m dV/dt = -g_Na(V-E_Na) - g_K(V-E_K) - g_L(V-E_L) + I_ext

g_Na = ḡ_Na · m³h    (m = activation, h = inactivation)
g_K  = ḡ_K  · n⁴     (n = activation, slow)
g_L  = ḡ_L             (leak, constant)

Gating variable x (m, h, n):
dx/dt = α_x(V)(1-x) - β_x(V)x

α, β: empirically measured voltage-dependent rate constants
```

**AP waveform phases:**

```
V_m
 +40 mV ────────╮
                 │  ← Na⁺ channels open: rapid depolarization
                 │
   0 mV         │
                 │
 -65 mV ──╮     │    ╭─────── Na⁺ channels INACTIVATE
           │     ╰────╯        K⁺ channels OPEN → repolarization
           │
 -80 mV   ╰──────────────── hyperpolarization (K⁺ still open)
                               return to rest (Na⁺ pump + leak)

Duration: ~1–2 ms
Absolute refractory: ~1 ms (Na⁺ inactivated, can't re-fire)
Relative refractory: ~2–3 ms (threshold elevated)
```

**Propagation:**

```
Unmyelinated: depolarization spreads to adjacent membrane → local circuit current
  Speed: 0.5–2 m/s, proportional to √(diameter)

Myelinated: myelin sheath (Schwann cells / oligodendrocytes) insulates axon
  AP jumps between Nodes of Ranvier (saltatory conduction)
  Speed: 70–120 m/s (proportional to diameter, not √diameter)
  Energy efficient: Na⁺ enters only at nodes
  MS (multiple sclerosis): demyelination → slowed/blocked conduction
```

---

## Simplified Neuron Models

For computational work (full HH is expensive to simulate at scale):

```
LEAKY INTEGRATE-AND-FIRE (LIF):
τ_m dV/dt = -(V - V_rest) + R_m I(t)

If V reaches threshold V_th: fire spike, reset V → V_reset, refractory τ_ref

Parameters: τ_m ~ 10–20 ms, V_th ~ -55 mV, V_rest ~ -65 mV

EXPONENTIAL INTEGRATE-AND-FIRE (EIF):
τ_m dV/dt = -(V-V_rest) + Δ_T exp((V-V_T)/Δ_T) + R_m I

Δ_T = slope factor (~2 mV): captures AP initiation curve

ADAPTIVE EXPONENTIAL (AdEx):
Adds adaptation current w: τ_w dw/dt = -w + b·δ(spike)
Models spike-frequency adaptation, bursting
```

---

## Synaptic Transmission

### Chemical Synapse Sequence

```
1. AP arrives at presynaptic terminal
2. Depolarization → voltage-gated Ca²⁺ channels (Ca_v2.1, Ca_v2.2) open
3. Ca²⁺ influx → SNARE complex activation → vesicle fusion
4. Neurotransmitter (NT) released into synaptic cleft (20 nm)
5. NT diffuses → binds postsynaptic receptor
6. Receptor opens ion channel (ionotropic) or activates G-protein (metabotropic)
7. Ion flow → EPSP or IPSP
8. NT cleared: reuptake (transporters), enzymatic degradation, diffusion

Release probability p_r: 0.1–0.9 (probabilistic, quantal)
One quantum (vesicle): ~5,000 NT molecules → ~0.5 mV EPSP
```

### Neurotransmitters

```
EXCITATORY:
  Glutamate    → AMPA-R (fast Na⁺/K⁺), NMDA-R (Na⁺/Ca²⁺, Mg²⁺ block at rest)
                  mGluR (G-protein, slow modulation)
  Acetylcholine → nAChR (fast, NMJ, autonomic ganglia, basal forebrain)
                   mAChR (G-protein, heart, smooth muscle, cortex)

INHIBITORY:
  GABA → GABA_A (Cl⁻ channel, fast: benzodiazepines potentiate)
          GABA_B (K⁺ channel via G-protein, slow)
  Glycine → Cl⁻ channel (spinal cord interneurons; strychnine blocks)

MODULATORY:
  Dopamine   → D1 (cAMP↑), D2 (cAMP↓); reward prediction error
  Serotonin  → 5-HT1/2 (mood, SSRI target), 5-HT3 (ion channel)
  Noradrenaline → α, β adrenergic; attention, arousal
  Acetylcholine → cortical arousal / cholinergic system (Alzheimer's target)
```

---

## Synaptic Plasticity

### Short-Term Plasticity

```
FACILITATION: successive APs → more Ca²⁺ → more vesicle release → larger EPSP
  τ_facilitation ~ 100 ms
  Observed at: calyx of Held, some cortical synapses

DEPRESSION: vesicle pool depletion → smaller EPSP
  τ_recovery ~ 1–10 s
  Observed at: high-release-probability synapses

Tsodyks-Markram model:
u_i = u_(i-1) + U(1-u_(i-1))
x_i = x_(i-1) - u_i x_(i-1)     (available vesicle fraction)
EPSP_i ∝ u_i x_(i-1) A          (A = absolute synaptic weight)
```

### Long-Term Potentiation (LTP)

Hebbian plasticity: "neurons that fire together, wire together" (Hebb 1949).

```
NMDA RECEPTOR (NMDAR) as coincidence detector:
  Requires: 1) presynaptic glutamate release
             2) postsynaptic depolarization to remove Mg²⁺ block
  → Mg²⁺ block at rest: NMDAR is BOTH ligand-gated AND voltage-gated
  → Only opens when pre and post active simultaneously

LTP induction (CA1 hippocampus):
  1. Coincident firing → NMDAR opens → Ca²⁺ influx
  2. Ca²⁺ → CaMKII activation (calcium/calmodulin-dependent kinase)
  3. CaMKII → AMPAR phosphorylation + insertion into membrane
  4. More AMPA-Rs → larger EPSP → potentiation

LTP expression: early (0–3 h): AMPAR trafficking
               late (>3 h): protein synthesis, new synapses (CREB pathway)
```

### Long-Term Depression (LTD)

```
mGluR-LTD (Cerebellar, also hippocampal):
  Weak/asynchronous activity → moderate Ca²⁺ → phosphatase activation
  → AMPAR internalization → smaller EPSP

STDP (Spike-Timing Dependent Plasticity):
  Δt = t_post - t_pre
  Δt > 0 (post after pre): LTP (causal → strengthen)
  Δt < 0 (post before pre): LTD (acausal → weaken)
  Time window: ±20–40 ms

STDP learning rule: Δw ∝ A+ exp(-Δt/τ+) for Δt>0
                        -A- exp(+Δt/τ-) for Δt<0
```

---

## Receptive Fields and Neural Coding

```
RECEPTIVE FIELD: the region in stimulus space that drives a neuron's response

Simple cell (V1): responds to oriented bar at specific location and orientation
  → Can be modeled as linear spatial filter (Gabor function)

Spatial frequency tuning: Fourier-like analysis by V1 cells

Rate code: information in average firing rate over 100 ms window
Place cell: fires when animal is in specific spatial location (O'Keefe 1971)
Grid cell: fires in hexagonal spatial pattern (Moser & Moser 2005, Nobel 2014)
Time code: information in precise spike timing (phase coding, sequences)

Population code: information distributed across many neurons
  Neural manifold: neural activity lives on low-D manifold in N-D space
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What sets resting potential? | K⁺ leak channels (V_m ≈ E_K = -98 mV, raised slightly by Na⁺ leak) |
| Why is AP all-or-nothing? | Positive feedback: depolarization → Na⁺ channels open → more depolarization |
| What limits max firing rate? | Absolute refractory period (~1 ms) → max ~500-1000 Hz |
| What makes NMDA special? | Both ligand-gated AND voltage-gated (Mg²⁺ block) → coincidence detector |
| What mediates LTP? | Ca²⁺ through NMDAR → CaMKII → AMPAR insertion |
| How does myelin help? | Saltatory conduction: 10× speed increase, energy efficient |
| GABA: excitatory or inhibitory? | Usually inhibitory (Cl⁻ in) but can be excitatory in development (reversed Cl⁻ gradient) |
