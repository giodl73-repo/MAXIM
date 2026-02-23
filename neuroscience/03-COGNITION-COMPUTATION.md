# Cognition and Computation — Neural Codes, Attractor Networks, Predictive Coding

## The Big Picture

```
    COGNITIVE NEUROSCIENCE LANDSCAPE
    ══════════════════════════════════════════════════════════

    COMPUTATIONAL APPROACHES TO MIND:
    ┌──────────────────────────────────────────────────────┐
    │ Attractor networks (Hopfield, Hopfield→Kanerva)      │
    │ Statistical physics approach to memory               │
    ├──────────────────────────────────────────────────────┤
    │ Predictive coding / Free Energy Principle (Friston)  │
    │ Perception = Bayesian inference                      │
    ├──────────────────────────────────────────────────────┤
    │ Decision theory: drift-diffusion model               │
    │ Speed-accuracy tradeoff quantified                   │
    ├──────────────────────────────────────────────────────┤
    │ Reinforcement learning in brain:                     │
    │ Dopamine = temporal difference error                 │
    ├──────────────────────────────────────────────────────┤
    │ Working memory: persistent activity in PFC           │
    │ Limited by ~4 chunks, active maintenance             │
    ├──────────────────────────────────────────────────────┤
    │ Attention: spotlight modulation, FEF/IPS control     │
    │ → transformer self-attention analogy                 │
    ├──────────────────────────────────────────────────────┤
    │ Consciousness: GWT, IIT, predictive processing       │
    └──────────────────────────────────────────────────────┘
```

---

## Attractor Networks: Hopfield as Ising Model

### Hopfield Network

Hopfield (1982) showed that recurrent neural networks are equivalent to spin glasses.

Network of N binary neurons s_i ∈ {-1, +1}.
Weights w_ij = w_ji (symmetric), w_ii = 0.

**Energy function** (Lyapunov / Hamiltonian):

$$E = -\frac{1}{2}\sum_{i \neq j} w_{ij} s_i s_j$$

Network dynamics: s_i → sign(Σ_j w_ij s_j) (synchronous or asynchronous update).
Energy is non-increasing: ΔE ≤ 0 at each update → converges to local minimum = attractor.

### Hebbian Weight Storage

Store M patterns {ξ^μ}, μ = 1,...,M:

$$w_{ij} = \frac{1}{N}\sum_{\mu=1}^{M} \xi_i^\mu \xi_j^\mu$$

Retrieval: start with partial/noisy version of pattern → network converges to stored attractor.

```
    Connection to Ising model (statistical physics):
    Ising Hamiltonian: H = -Σ_{i<j} J_ij σ_i σ_j - h Σ_i σ_i
    Hopfield E = -½Σ w_ij s_i s_j  (same form, h=0, J=w/2, σ=s)

    TAP (Thouless-Anderson-Palmer) equations:
    Connection to spin glass mean-field theory
    Hopfield = spin glass with structured J_ij (not random)

    CAPACITY:
    For random patterns, reliable retrieval when M < α_c N
    α_c ≈ 0.138 (from statistical physics / replica method)
    → Can store ~0.14N patterns in N-neuron network
    Above capacity: "retrieval" states merge, lose pattern specificity

    Example: N = 10,000 neurons → can store ~1400 patterns
    Human visual cortex (16×10⁹ neurons): ~2×10⁹ "patterns" (oversimplified!)

    Overlap measure: m^μ = (1/N)Σ_i ξ_i^μ s_i
    At attractor for pattern μ: m^μ ≈ 1 (fully retrieved)
    During retrieval: m^μ grows from initial noisy value to ≈1
    Spurious states: mixtures of patterns (spin glass "metastable states")
```

### CA3 as Attractor Memory

```
    Hippocampal CA3 properties match Hopfield model:
    Recurrent collaterals (large): ~3M recurrent synapses per CA3 cell (in rat)
    Sparse activity (~3%): consistent with optimal Hopfield capacity scaling
    Pattern completion: partial input → full memory retrieved
    Experimental: lesion CA3 → impairs completion of fragmented memory cues
    Computational: O'Reilly & McClelland model CA3 as auto-associative Hopfield net

    Extension: Kanerva's sparse distributed memory (SDM)
    Address space is large and random patterns → sparse read/write
    Better model of hippocampus + neocortex interaction?
    → Connect to: modern transformer attention is related to SDM (Ramsauer et al. 2020)
```

---

## Predictive Coding

### The Helmholtz Inference Machine

Helmholtz (1867): "Perception is unconscious inference."
The brain infers the most likely cause of sensory input.

**Hierarchical generative model**:

```
    Higher cortex generates predictions about lower-level activity:
    High level:  r₃ = hidden state of world
    Predictions: ↓ (descending: what we EXPECT to see)
    Prediction errors: ↑ (ascending: what SURPRISES us)

    Level 3 (e.g., PFC):   representation r₃, predicts r₂
         ↓ predictions
    Level 2 (e.g., V5/MT):  r₂, predicts r₁
         ↓ predictions
    Level 1 (e.g., V1):    r₁, predicts sensory input s
         ↓ predictions
    Sensory input (retina): s

    Prediction error computation:
    ε_i = s_i - Σ_j w_ij r_j  (error = data - prediction)
    Errors propagate UP, predictions propagate DOWN

    Learning: update representations and weights to minimize prediction errors
    → This IS the brain's goal: reduce surprise, optimize predictions
```

### Rao-Ballard Predictive Coding Model (1999)

$$\tau_r \dot{r} = -r + f(U^T \varepsilon_1) - k_2 \varepsilon_2$$

$$\varepsilon_1 = s - U r$$

where r = representation, U = prediction weights, ε₁ = prediction error.

```
    Biological implementation:
    Prediction neurons (deep layers 2/3, layer 6): send top-down predictions
    Error neurons (superficial layers 2/3): encode prediction error, send up
    This matches the layer-specific connectivity of cortex!
    Layer 6 → layer 4 (top-down feedback)
    Layer 2/3 → higher areas (feedforward)

    Experimental support:
    Repetition suppression: repeated stimuli → reduced V1 response
    (prediction perfectly formed → small error → less activity)
    Mismatch negativity (MMN): EEG component to unexpected deviant tone
    (prediction error propagates to auditory cortex)
    Predictive code in V1: surround suppression = spatial prediction
    (center response reduced by surround = predicted context)
```

---

## Free Energy Principle (Karl Friston)

The most ambitious computational theory of brain function.

### Variational Free Energy

For a generative model p(x,z) of observations x and latent states z,
with recognition distribution q(z):

$$\boxed{F = E_q[\log q(z) - \log p(x,z)] = \text{KL}[q(z) \| p(z|x)] - \log p(x)}$$

Since KL ≥ 0: F ≥ -log p(x) (F is an upper bound on surprise)
Minimizing F over q → q → p(z|x) (posterior inference) AND -log p(x) → 0 (maximize evidence)

**Active inference**: organisms also ACT to minimize F.
Instead of just updating beliefs (q) to match reality, act to make reality match beliefs (predictions).

```
    FREE ENERGY = SURPRISE bound ≥ actual surprise
    Minimizing F = minimizing expected surprise
                 = maintaining homeostasis (same thing!)

    Two ways to minimize F:
    1. Update internal model q(z) to match sensory input (PERCEPTION/LEARNING)
    2. Change sensory input by acting (ACTION)

    Reflex: spinal cord minimizes F locally (proprioceptive prediction errors → muscle action)
    Voluntary movement: high-level predictions generate proprioceptive predictions → motor action
    No separate motor commands: action IS prediction error minimization

    Variational Bayes interpretation:
    F = KL[q(z)||p(z|x)] - log p(x)
      = -ELBO (Evidence Lower BOund from VAEs!)
    → Connect to ai-engineering/VAE: same math, same structure
    FEP says brain does approximate Bayesian inference via ELBO optimization
    → Not just a metaphor — exact same mathematical framework
```

---

## Bayesian Brain

Perception as posterior inference: prior × likelihood → posterior.

**Bayesian theorem applied to perception**:
$$p(\text{world state} | \text{sensory data}) = \frac{p(\text{sensory data} | \text{world state}) \cdot p(\text{world state})}{p(\text{sensory data})}$$

```
    Prior p(world): what the brain EXPECTS based on past experience
    Likelihood p(data|world): what sensory data is consistent with that world state
    Posterior p(world|data): belief about world state AFTER seeing data

    Cue combination (Ernst & Banks 2002, vision + touch):
    Two independent estimates, ẑ₁ (visual, σ₁²) and ẑ₂ (haptic, σ₂²)
    Optimal combination: ẑ = (ẑ₁/σ₁² + ẑ₂/σ₂²) / (1/σ₁² + 1/σ₂²)
    Variance: σ² = 1/(1/σ₁² + 1/σ₂²)
    Human behavior matches this prediction → brain computes optimal Bayesian estimate

    Visual illusions = prior dominating:
    Hollow face illusion: prior (faces are convex) overrides actual depth cues
    Brightness illusions: prior (uniform illumination) affects perceived lightness
    Size-weight illusion: heavy priors from visual size → misestimate weight
    Motion in pictures: prior (retinal motion = object motion, not eye motion)
```

---

## Drift-Diffusion Model (DDM) for Decision Making

Simple perceptual decisions: is stimulus moving left or right? Correct or incorrect?

**Stochastic accumulator model**:

$$dX = \mu \, dt + \sigma \, dW_t$$

where:
- X = accumulated evidence (decision variable)
- μ = drift rate (signal strength, positive = right, negative = left)
- σ = noise amplitude
- W_t = Wiener process (Brownian motion)

**Boundaries**: absorbing barriers at θ (correct for "right") and -θ (correct for "left").

```
    First passage time T to reach ±θ → reaction time distribution.

    Key results:
    Mean RT = θ/μ × tanh(μθ/σ²)   (for 0 start)
    Error rate = 1/(1 + exp(2μθ/σ²))  (logistic function of signal/noise)

    Speed-accuracy tradeoff:
    Wide boundaries (large θ): slower, more accurate
    Narrow boundaries (small θ): faster, more errors
    → "Response caution" or "urgency" is a single parameter θ

    Neural evidence:
    LIP (lateral intraparietal cortex) neurons in monkey:
    Firing rate builds during motion discrimination task
    Rate increases approximately linearly until threshold → decision
    Rate = accumulated sensory evidence (matches X in DDM)
    Threshold crossing → saccadic eye movement decision

    Urgency signal: μ can vary during trial (start low, increase as deadline approaches)
    Non-stationary DDM needed for time-pressure paradigms
```

---

## Reinforcement Learning in the Brain

### Dopamine as Temporal Difference Error

**Schultz experiment (1997)**: Record dopamine neurons during classical conditioning.

```
    Initial: Reward delivered unexpectedly
    DA neurons: fire at time of REWARD (unexpected = large positive error)

    After training: conditioned stimulus (CS) predicts reward reliably
    CS onset:  DA neurons FIRE (now CS is the surprise, predicts reward)
    Reward time: DA neurons UNCHANGED (expected reward = no error)

    Omission of expected reward:
    CS onset: DA neurons fire (as before)
    Reward time: DA neurons PAUSE (below baseline = negative prediction error)

    This is exactly the TD error:
    δ_t = r_t + γV(s_{t+1}) - V(s_t)
    Unexpected reward:   δ > 0 → DA fires
    Expected reward:     δ ≈ 0 → DA baseline
    Omitted reward:      δ < 0 → DA pauses

    Exact mathematical connection to TD learning:
    DA neurons compute δ_t = r_t + γV(s') - V(s)
    V(s) = value function (expected future reward from state s)
    Striatum = V(s) (value function implemented by striatal neurons)
    OFC = model-based V(s) (Daw et al. 2005: dual system)
```

### Model-Free vs Model-Based RL in the Brain

```
    MODEL-FREE (habit system, striatum):
    TD learning: update V(s) after each transition
    Slow to adapt to reward changes
    Computationally cheap: no model required
    Striatal lesions: disrupt reward-based learning

    MODEL-BASED (goal-directed system, PFC + hippocampus):
    Maintain model of environment: P(s'|s,a) and R(s,a)
    Plan using mental simulation (forward model)
    Adapt quickly to reward changes
    OFC + DLPFC: track outcome identities and values

    ARBITRATION (Daw et al. 2005):
    Brain uses reliability to switch between systems
    High model uncertainty → use model-free
    Low uncertainty → use model-based
    Prefrontal cortex arbitrates based on uncertainty

    Implications for addiction:
    Drugs override both systems: hijack DA reward signal
    → Over-value drug-associated states
    → Habits shift control to model-free striatum
    → Impaired inhibitory control from PFC
    → Three-stage model: impulsivity → compulsivity → habit
```

---

## Working Memory: Persistent Activity in PFC

### Fuster-Goldman-Rakic Paradigm

Delayed response task: see sample, delay, test. PFC neurons fire throughout the delay.

```
    PFC neuron activity during delayed match-to-sample:
    Sample on:   neurons fire selectively (preferred object/direction)
    Delay:       SAME neurons continue firing at elevated rate
    Test on:     response if match; no response if non-match
    → Activity "bridges the temporal gap" = short-term memory buffer

    Mechanisms of persistent activity:
    1. Recurrent excitation: attractor state (bump attractor in ring model)
       Self-sustaining activity via excitatory recurrent connections
       Network → stable "memory" state after input removed
       Destabilized by distractors → memory loss

    2. Intrinsic bistability: single neurons with two stable states
       Persistent activity maintained by Ca²⁺-activated conductances
       Plateau potentials (in some PFC neurons)

    3. Synaptic facilitation: short-term enhancement
       Activity leaves "trace" in enhanced synaptic weights
       Works for seconds; no spike required during all of delay

    Capacity (~4 chunks):
    Miller (1956): "magic number 7 ± 2" (short-term memory spans)
    Cowan (2001): true working memory capacity ≈ 4 chunks
    Explanation from attractor model: multiple bumps of activity in PFC
    Bump = one item; maximum stable bumps = ~4 (due to competition)

    Individual differences in WM capacity correlate with:
    PFC volume, dopamine D1/D2 balance, COMT genotype (Val158Met)
    → WM capacity predicts fluid intelligence, academic performance
```

---

## Attention

### Spatial Attention: Posner and Feature-Based Attention

```
    POSNER CUEING PARADIGM (1980):
    Valid cue (80%): cue → target at cued location → fast RT
    Invalid cue (20%): cue → target opposite location → slow RT

    Neural correlates:
    FEF (frontal eye field) + IPS (intraparietal sulcus): voluntary attention control
    SC (superior colliculus): reflexive attention to sudden onset
    Pulvinar (thalamus): attentional gating between cortical areas

    GAIN MODULATION:
    Attention doesn't add a constant to response, it MULTIPLIES baseline
    Attended location → V1/V2/V4 neurons fire more to same stimulus
    Unattended → same neuron fires less
    Δ = attention gain × contrast response function (Moran & Desimone 1985)

    FEATURE-BASED ATTENTION:
    Attend to color red → V4 neurons preferring red fire more everywhere in visual field
    Attend to vertical orientation → V1 neurons preferring vertical enhanced
    Top-down biasing: search representation in IT/PFC → bias matching features globally

    Connection to self-attention in transformers:
    Q (query) = top-down attention representation
    K (key) = feature representations in sensory areas
    V (value) = actual neural response to be weighted
    Similarity(Q,K) → attention weight → weighted sum of V
    Both biological and transformer attention = selecting relevant content from stored representations
    But biological attention is gain modulation (multiplicative), not pure softmax
```

---

## Consciousness

### Global Workspace Theory (Dehaene)

```
    TWO CLASSES OF NEURAL PROCESSES:
    1. Unconscious: local, modular, automatic (most visual processing, motor habits)
    2. Conscious: global, integrated, flexible (language, reasoning, working memory)

    GLOBAL WORKSPACE ARCHITECTURE:
    Sensory modules (V1, auditory, etc.) → compete for access to global workspace
    Winner broadcasts to all of cortex via long-range neurons (especially L2/3)
    Global broadcast = conscious awareness

    NEURAL IGNITION:
    When stimulus crosses threshold: local activation (unconscious)
    + late (>300ms) ignition of frontoparietal network → P3b ERP → conscious report
    Visible vs invisible stimuli: same early V1 response, different ignition

    Predictions:
    Consciousness requires frontoparietal network (not just local area)
    Content of consciousness = what's in global workspace
    Attention + working memory = gates to workspace

    GWT in AI terms:
    Global workspace ≈ KV cache + attention mechanism
    Modules broadcasting = different retrieval heads
    The "ignition" has no clear transformer analog
```

### Integrated Information Theory (Tononi)

```
    CORE MEASURE: Φ (phi) = amount of integrated information
    Φ = irreducibility of a system's causal structure
    High Φ = system that generates more information as a whole than sum of parts

    Formal (IIT 3.0):
    Φ = D_KL(current system state || product of parts' states)
    Must minimize over all bipartitions MIP (minimum information partition)
    Φ > 0 iff system cannot be cut without information loss

    AXIOMS (intrinsic causation, composition, information, integration, exclusion)
    → Imply: Φ > 0 for every conscious experience
    Consciousness = Φ (not just "correlates with" Φ)
    Panel of experts 2023: awarded $500K, found IIT unlikely correct (adversarial collaboration)

    Controversial predictions:
    Feedforward networks: Φ = 0 (no integration) → NOT conscious
    Cerebellum (many parallel fibers, little integration): low Φ
    This is consistent with: cerebellar lesions don't affect consciousness
    But: calculating Φ is NP-hard → can't actually compute for real systems
```

---

## Decision Cheat Sheet

| Cognitive function | Neural substrate | Computational model | Key equation/result |
|-------------------|-----------------|--------------------|--------------------|
| Memory recall | CA3 attractor | Hopfield network | Capacity: 0.14N patterns |
| Perception | Hierarchical cortex | Predictive coding | ELBO minimization |
| Multisensory integration | Parietal cortex | Bayesian optimal | ẑ = Σ ẑ_i/σ_i² / Σ 1/σ_i² |
| Decision making | LIP accumulator | Drift-diffusion | First passage time to ±θ |
| Reward learning | Striatum + DA | TD learning | δ = r + γV' - V |
| Working memory | PFC persistent | Bump attractor | Capacity ~4 items |
| Attention | FEF, IPS, pulvinar | Gain modulation | Multiplicative |
| Consciousness | Frontoparietal | GWT ignition | None-formal yet |

---

## Common Confusion Points

**Free energy ≠ thermodynamic free energy**: Friston's "free energy" is variational free energy
from machine learning / statistics (F = KL[q||p] - log evidence). It's called "free energy"
by analogy with Helmholtz free energy in thermodynamics (F = U - TS), because both represent
bounds on information quantities. They're not the same F. The brain does NOT minimize
thermodynamic free energy; it minimizes variational free energy = surprise upper bound.

**Drift-diffusion model has no spatial information**: The DDM describes evidence accumulation
over time but says nothing about WHERE in the brain this happens or HOW the drift rate μ is
computed from sensory input. LIP neurons are the neural correlate, but the mapping from
stimulus to μ is itself a separate computational problem (depends on sensory processing quality,
attention, etc.). DDM is a phenomenological model of the decision process.

**Dopamine is not "the reward chemical"**: Dopamine encodes prediction error, not reward itself.
If a reward is perfectly predicted, dopamine neurons don't fire at reward time. Dopamine is
the CHANGE in expected reward — δ = actual - predicted. This is why "unexpected pleasure" is
more activating than "expected pleasure" of the same magnitude. The popular press gets this wrong.

**Global workspace theory and IIT are fundamentally different theories that can both be "right"**:
GWT is a functional theory (what role does consciousness play in cognition). IIT is an
intrinsic theory (what physical systems ARE conscious). They operate at different levels
and could both be correct. The recent adversarial collaboration found evidence against IIT's
specific predictions, not necessarily against a more general version.
