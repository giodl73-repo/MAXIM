# Hodgkin-Huxley Model — Action Potential from Gated Conductances

## The Big Picture

```
┌──────────────────────────────────────────────────────────────────────────┐
│              HODGKIN-HUXLEY MODEL LANDSCAPE                               │
│                                                                            │
│  BIOLOGICAL REALITY               MODEL ABSTRACTION                       │
│  ──────────────────               ─────────────────                       │
│  Na⁺ channel: opens, then inact.  m³h: m=activation, h=inactivation      │
│  K⁺ channel: opens slowly         n⁴: n=delayed rectifier gating          │
│  Lipid bilayer                    Capacitor C_m                           │
│  Ion pumps (Na/K-ATPase)          Not modeled (sets initial conditions)   │
│                                                                            │
│  THE MODEL EQUATION:                                                       │
│  C_m dV/dt = -g_Na m³h (V-E_Na) - g_K n⁴ (V-E_K) - g_L(V-E_L) + I_ext  │
│                                                                            │
│  BRIDGE TO COMPUTING:                                                      │
│  Biological neuron: H-H model (1952)                                      │
│      ↓  abstraction                                                        │
│  McCulloch-Pitts neuron (1943): threshold unit                            │
│      ↓  generalization                                                     │
│  Perceptron (Rosenblatt, 1958): weighted sum + threshold                  │
│      ↓  nonlinearity                                                       │
│  Modern artificial neuron: weighted sum + activation function             │
│  What was kept: firing threshold, weight sum, activation                  │
│  What was discarded: time, ion channels, refractory period, cable theory  │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Section 1 — The Experimental Foundation (Squid Giant Axon)

Hodgkin and Huxley used the squid giant axon (1 mm diameter — enormous by
biological standards) for voltage clamp experiments. The giant axon allowed:

1. Easy electrode insertion without special microelectrode techniques
2. Perfusion of the axon interior (replace cytoplasm with defined solutions)
3. High-quality voltage clamp: control V_m precisely, measure resulting current

**Voltage clamp method:**

```
  Feedback amplifier holds V_m at command voltage V_c
  Measures the current I needed to hold V_m = V_c

  At V_c = -70 mV (rest): I ≈ 0
  Step to V_c = 0 mV:
    Early current: inward (~Na⁺ influx), then turns off (inactivation)
    Late current: outward (~K⁺ efflux), maintained
    Capacitive transient at step onset (C_m × dV/dt)

  Ion isolation:
    Replace Na⁺ with choline (same charge, impermeable) → only K⁺ current
    Subtract: (total current) - (K⁺ only) = Na⁺ current

  This pharmacological dissection revealed separate Na⁺ and K⁺ conductances.
```

**Gating current:** When S4 voltage sensors move in the electric field, they
carry a small charge displacement before any ions flow. This "gating current"
is detectable with very low-noise electronics. It confirmed the charged sensor
hypothesis and directly measured ~12 e per channel moved per gating event.

---

## Section 2 — The Hodgkin-Huxley Equations

### The Master ODE

```
  C_m dV/dt = I_ion + I_ext

  I_ion = -[g_Na m³h (V - E_Na) + g_K n⁴ (V - E_K) + g_L (V - E_L)]

  Parameters (squid axon, ~6°C):
    C_m = 1 μF/cm²
    g_Na = 120 mS/cm²   (maximal Na⁺ conductance)
    g_K  = 36 mS/cm²    (maximal K⁺ conductance)
    g_L  = 0.3 mS/cm²   (leak: Cl⁻ and others)
    E_Na = +55 mV
    E_K  = -77 mV
    E_L  = -54.4 mV
```

### Gating Variables

Each gating variable represents the probability that a single gate is in the
open conformation. They are first-order kinetic ODEs:

```
  dm/dt = α_m(V)(1-m) - β_m(V)m

  Steady-state:  m_∞(V) = α_m / (α_m + β_m)
  Time constant: τ_m(V) = 1 / (α_m + β_m)

  Similarly for h (Na⁺ inactivation gate) and n (K⁺ activation gate).

  All rate constants α and β are voltage-dependent.
  Hodgkin and Huxley fit them empirically from voltage clamp data.
```

### Na⁺ Channel: m³h

The Na⁺ conductance uses three activation gates (m) and one inactivation gate (h):

```
  g_Na_actual = g_Na × m³ × h

  Physical interpretation:
    m: activation gate — opens rapidly on depolarization
    h: inactivation gate — closes slowly on sustained depolarization
    (h is "hindering" gate — starts open, closes after activation)

  Three m gates: empirical — fits the sigmoidal activation curve
  (corresponds loosely to 3 independent voltage sensors needing activation)

  Voltage dependence:
    α_m(V) = 0.1 × (25-V) / [exp((25-V)/10) - 1]
    β_m(V) = 4 × exp(-V/18)
    α_h(V) = 0.07 × exp(-V/20)
    β_h(V) = 1 / [exp((30-V)/10) + 1]

  (V in mV, relative to rest; V = 0 means resting potential)
```

### K⁺ Channel: n⁴

The K⁺ conductance uses four activation gates (n):

```
  g_K_actual = g_K × n⁴

  n: activation gate — opens more slowly than m; no inactivation

  α_n(V) = 0.01 × (10-V) / [exp((10-V)/10) - 1]
  β_n(V) = 0.125 × exp(-V/80)
```

### Action Potential: Phase-by-Phase Analysis

```
  PHASE        TIME     WHAT HAPPENS                    GATES
  ─────────────────────────────────────────────────────────────────────
  Resting      t < 0    V_m = -65 mV                    m ≈ 0, h ≈ 1, n ≈ 0.3

  Stimulus     t = 0    I_ext depolarizes to threshold   gating begins
               (~0 ms)  (threshold ≈ -55 mV; about       (if below threshold:
                         10 mV above rest)                graded response decays)

  Rising phase 0-1 ms   Na⁺ channels open (m increases) m → 1, h still 1
                         Inward Na⁺ current > outward K⁺ g_Na large
                         Positive feedback (V ↑ → m ↑ →   K⁺ channels still
                         more depolarization)              mostly closed
                         V → E_Na ≈ +55 mV               (n slow)

  Peak         ~1 ms     V ≈ +40 mV                     m ≈ 1, h → 0 (closing)
                          Na⁺ channels begin inactivating n increasing

  Repolariz.   1-2 ms    Na⁺ inactivation complete       m high, h → 0
                          K⁺ channels now open            g_Na → 0
                          Outward K⁺ current drives V down n → 1

  Undershoot   2-4 ms    V passes through E_K ≈ -77 mV  n still high (K⁺ open)
  (hyperpol.)             K⁺ channels slow to close       h recovering

  Refractory   4-10 ms   Absolute: Na⁺ h still = 0;     h near 0 (absolute)
                          no new AP possible              h recovering (relative)
                          Relative: V below rest; h low
                          (need larger stimulus)
  ─────────────────────────────────────────────────────────────────────
```

### Threshold and All-or-None Behavior

The action potential is all-or-none: below threshold, the response decays;
at or above threshold, a full action potential fires. This arises from the
positive feedback loop between Na⁺ channel opening and depolarization:

```
  Below threshold:
    Small depolarization → small m increase → small Na⁺ current
    Outward leak + K⁺ current > inward Na⁺ → V returns to rest

  At threshold:
    Na⁺ inward current exactly matches outward currents
    Unstable equilibrium (saddle point in phase space)

  Above threshold:
    Positive feedback:  V↑ → m↑ → g_Na↑ → I_Na↑ → V↑ → ...
    Na⁺ current "wins" → full AP

  Mathematical: Hopf bifurcation (Type II) or saddle-node
  bifurcation (Type I) depending on neuron type
```

---

## Section 3 — Cable Theory: Signal Propagation

### The Cable Equation

An axon is not a point — it extends spatially. Signals propagate along the axon
as they do along a lossy electrical cable (Kelvin's submarine cable equation, 1855):

```
  λ² ∂²V/∂x² - τ_m ∂V/∂t = V - V_rest

  λ = sqrt(r_m / r_a) = space constant [m]
  τ_m = r_m × c_m = time constant [s]

  r_m = membrane resistance per unit length [Ω·m]
  r_a = axial (intracellular) resistance per unit length [Ω/m]
  c_m = membrane capacitance per unit length [F/m]

  Passive (subthreshold) signals decay exponentially:
    V(x) = V₀ exp(-x/λ)   (steady-state spatial profile)

  For unmyelinated mammalian axon:
    λ ≈ 0.1-1 mm → signal decays severely over mm distances
    → Active propagation (AP) is needed for long-distance signaling
```

### Myelination and Saltatory Conduction

For long-range signaling (e.g., 1-meter motor neurons), passive decay is
unacceptable. Myelination solves this:

```
  UNMYELINATED AXON:                    MYELINATED AXON:
  AP propagates continuously            AP jumps between Nodes of Ranvier
  Speed: 0.5-2 m/s                      Speed: 50-100 m/s (saltatory)
  High metabolic cost (continuous       Low metabolic cost (Na/K-ATPase
  Na/K-ATPase activity along axon)      only at nodes)

  Myelin effect on cable parameters:
    r_m ↑ (myelin is electrically insulating) → λ ↑ dramatically
    c_m ↓ (myelin adds series capacitance)     → τ_m ↓
    Combined: λ >> internode distance → AP jumps without active regen.

  Multiple sclerosis: demyelination → slowed conduction, fatigue,
  weakness (axon lengths now exceed λ → signals fail to propagate)
```

### Conduction Velocity Scaling

```
  Unmyelinated axon:   v ∝ sqrt(d)   (d = axon diameter)
  Myelinated axon:     v ∝ d

  For squid giant axon (d = 1 mm unmyelinated):  v ≈ 25 m/s
  For mammalian myelinated fiber (d = 20 μm):    v ≈ 100 m/s
  → Myelination gets ~100× faster conduction at 50× smaller diameter
```

---

## Section 4 — Bridge to Artificial Neural Networks

### What Biology Provided

The historical path from Hodgkin-Huxley to modern deep learning:

```
  1943: McCulloch-Pitts (MP) neuron
    y = Θ(Σ wᵢxᵢ - θ)    (Θ = Heaviside step function)
    Inspired by biology: all-or-none firing, threshold
    Ignored: time dynamics, ion channels, refractory period, cable theory

  1958: Rosenblatt's Perceptron
    y = sign(Σ wᵢxᵢ + b)
    Added: learning rule for weights
    Ignored: same biological details, plus hidden layers

  1986: Backpropagation (Rumelhart, Hinton, Williams)
    Replaced step function with differentiable sigmoid
    This is the crucial break from biology: need smooth activation for gradients

  Modern deep learning (2012-present):
    y = f(Wx + b)   f = ReLU, GELU, sigmoid, tanh
    Stacked layers; trained by gradient descent

  KEPT from biology:      DISCARDED from biology:
  ─────────────────────   ──────────────────────────────────────
  Nonlinear activation    Temporal dynamics (spikes, timing)
  All-or-none threshold   Refractory periods
  Weighted summation      Compartmental structure (dendrites)
  Network organization    Cable equation (spatial signal decay)
  Excitation/inhibition   Ion channel gating kinetics
  Layer hierarchy         Specific neurotransmitter chemistry
```

### Spiking Neural Networks (SNNs)

Spiking neural networks attempt to re-incorporate the temporal dynamics:

```
  Leaky Integrate-and-Fire (LIF) neuron:

  τ_m dV/dt = -(V - V_rest) + R × I(t)

  When V reaches threshold V_th:
    Emit spike → V reset to V_reset
    Refractory period τ_ref enforced

  Advantages: closer to biology, sparse coding, event-driven
  Challenges: non-differentiable threshold → hard to train
  Workaround: surrogate gradients (approximate step function with sigmoid
  during backprop)

  Current state: SNNs approach (but rarely exceed) ANN accuracy on
  standard benchmarks; power-efficient on neuromorphic hardware
  (Intel Loihi, IBM TrueNorth) but not yet competitive at scale
```

### What the H-H Model Teaches AI Practitioners

1. **Nonlinearity is essential.** The all-or-none AP requires nonlinear positive
   feedback (Na⁺ channel opening). Linear systems cannot produce thresholding.
   Artificial activations serve the same purpose: without them, deep networks
   collapse to linear transformations regardless of depth.

2. **Time matters in biology, was dropped in ANN.** Biological neurons integrate
   synaptic inputs over ~5-10 ms time windows. The temporal pattern of spikes
   carries information (rate coding vs. temporal coding). ANNs are stateless
   (per-input); only RNNs/LSTMs/Transformers reintroduce temporal structure.

3. **Adaptation is biological but unusual in ANN.** The Na⁺ inactivation gate
   (h) is adaptation: a sustained stimulus causes the neuron to stop firing.
   This prevents saturation and encodes change rather than absolute value.
   Only dropout and some normalization schemes loosely mimic this.

4. **Compartmental integration is lost.** Dendritic computation (pattern matching
   in single dendrites, NMDA spikes) is lost in the point-neuron approximation.
   Multi-compartment models (NEURON, Brian2) recover this at high computational cost.

---

## Section 5 — Beyond Hodgkin-Huxley

### Other Neuron Models and Their Tradeoffs

```
  ┌────────────────────────────────────────────────────────────────────┐
  │  MODEL            │  DETAIL │  TRACTABLE │  CAPTURES                │
  │  ─────────────── │  ─────  │  ─────────  │  ──────────────────────  │
  │  H-H (4 var)      │  High   │  Moderate   │  AP shape, channel kinet.│
  │  FitzHugh-Nagumo  │  Low    │  High       │  Threshold, refractory   │
  │  (2 var)          │         │             │  excitable dynamics      │
  │  Izhikevich (2 var│  Low    │  High       │  20 firing patterns of   │
  │  + reset rules)   │         │             │  real neurons            │
  │  Morris-Lecar     │  Med    │  High       │  Bursting, phase plane   │
  │  (2 var)          │         │             │  analysis tractable      │
  │  Multi-compartment│  High   │  Low        │  Dendritic computation,  │
  │  (100s of compart)│         │             │  realistic morphology    │
  └────────────────────────────────────────────────────────────────────┘
```

<!-- @editor[audience/P3]: The learner has dynamical systems background from MIT TCS — could briefly note the bifurcation classification (Type I: SNIC, Type II: Hopf) maps to neuron firing classes (Class 1 vs Class 2 excitability) -->
### Phase Plane Analysis of Excitability

For FitzHugh-Nagumo (2D reduction), the dynamics are visible in phase space:

```
  dv/dt = v - v³/3 - w + I
  dw/dt = ε(v + a - bw)

  v = fast variable (voltage-like)
  w = slow variable (recovery-like, corresponds to h and n)
  ε << 1: w is slow

  Phase portrait:
    V-nullcline: dv/dt = 0 → cubic curve
    w-nullcline: dw/dt = 0 → straight line

    Intersection = fixed point
    Single intersection below threshold: stable rest
    Hopf bifurcation at threshold → limit cycle oscillation
    Limit cycle = sustained AP firing (repetitive)
```

---

## Decision Cheat Sheet

| Question | H-H answer | Key concept |
|----------|------------|-------------|
| What generates the rising phase of the AP? | Na⁺ influx through opening m³h channels | Positive feedback: V↑ → m↑ → g_Na↑ → V↑ |
| What terminates the AP rising phase? | Na⁺ channel inactivation (h → 0) | h gate closes with delay after depolarization |
| What repolarizes the membrane? | K⁺ efflux through n⁴ channels | K⁺ current outward, delayed relative to Na⁺ |
| Why is there an undershoot? | n still high when Na⁺ off; pulls V toward E_K | K⁺ slow to close, V overshoots E_rest |
| What determines absolute refractory period? | h gate recovery time | h ≈ 0 → no Na⁺ current possible |
| How far does a signal passively propagate? | Exponential decay with λ = sqrt(r_m/r_a) | λ ≈ 0.1-1 mm for typical axon |
| Why is myelination fast? | λ >> internode distance → saltatory | AP regenerates only at nodes |
| What did ANN drop from H-H? | Time dynamics, refractory period, cable eq. | Point neuron, no spike timing |

---

## Common Confusion Points

**m, h, and n are probabilities, not integers.** m = 0.7 means 70% of the
independent activation gates in the channel population are open. The product m³h
gives the fraction of Na⁺ channels in the open conducting state. For large
populations, this is deterministic; for single channels, you need the stochastic
Markov formulation.

**The refractory period is about h recovery, not m.** m is fast — it can open
again immediately after the AP. The absolute refractory period is set by h: Na⁺
channels are inactivated (h ≈ 0) regardless of depolarization. No h = no Na⁺
current = no AP. The relative refractory period (larger stimulus needed) reflects
both partial h recovery and hyperpolarization from elevated n.

**H-H is a phenomenological model.** Hodgkin and Huxley had no knowledge of
protein structure — they fit functional forms to voltage clamp data. The m³h
exponents are empirical, not derived from molecular mechanism. The underlying
Markov models (based on actual channel structure: S4 helices, selectivity filters)
are more mechanistic but more complex.

**Cable theory predicts passive decay; APs overcome it.** The cable equation
describes subthreshold signals, which decay exponentially with λ. Action
potentials don't decay: the nonlinear Na⁺ channel kinetics regenerate the signal.
This is why APs are all-or-none: partial APs don't exist — either the signal
exceeds threshold and regenerates, or it decays passively.

**Artificial neurons are not computational models of real neurons.** McCulloch-
Pitts units and modern ANNs are loosely inspired by biology but are not trying
to model biological computation accurately. They are mathematical function
approximators. Computational neuroscience (H-H, multi-compartment models)
attempts actual biological fidelity; deep learning does not.
