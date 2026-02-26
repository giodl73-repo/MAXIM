# Neuroscience → AI Bridge — Systematic Comparisons

## Overview

<!-- @editor[diagram/P2]: Overview block compares brain vs AI as text lists -- replace with ASCII correspondence diagram mapping neuroscience mechanisms to AI analogs with connection lines -->
```
    NEUROSCIENCE ←──────────────────────────── AI / ML

    Biology: evolved over 500M years    Math: developed over 80 years
    Wet, hot, noisy, 20W                Dry, cool, precise, 700W per chip
    Self-organizing, self-repairing     Engineered, manually updated
    Online, continuous learning         Mostly batch, offline training

    THE HONEST TRUTH:
    Most AI is not "brain-inspired" in any deep sense.
    The similarities are real but shallow; the differences are deep.
    Understanding BOTH directions is where the interesting science is.
```

---

## 1. Neuron: Hodgkin-Huxley vs Artificial (ReLU) Neuron

```
    BIOLOGICAL H-H NEURON:
    ──────────────────────
    Input:  Continuous synaptic currents (EPSPs, IPSPs, neuromodulation)
    Integration: C_m dV/dt = Σ g_i(V-E_i) (nonlinear, voltage-dependent)
    Output: Spike train (all-or-nothing, 0.5-1 ms duration)
    Rate:   0-1000 Hz (typical cortical: 0.1-10 Hz average)
    Temporal: continuous time, precise spike timing matters
    State:  Continuous V + gating variables m, h, n (memory within spike)
    Energy: ~10 pJ per spike
    Noise:  High (stochastic channels, thermal noise, quantal release)

    ARTIFICIAL RELU NEURON:
    ──────────────────────
    Input:  Weighted sum of continuous-valued activations
    Integration: z = Σ w_i x_i + b (linear)
    Output: f(z) = max(0,z) (continuous, rate-like)
    Rate:   Analogous to firing rate, not spikes
    Temporal: synchronous layers, discrete time steps
    State:  No internal state (stateless between examples)
    Energy: ~0.1-1 pJ per multiply-add (GPU)
    Noise:  Zero (deterministic); dropout ≈ artificial noise

    KEY DIVERGENCES:
    1. SPIKING vs RATE: HH produces spikes; ReLU is continuous rate code
       Spiking preserves precise timing; rate code throws timing away
       Spiking networks (SNNs) closer to biology but harder to train
    2. TEMPORAL DYNAMICS: HH has adaptation, bursting, refractory period
       → same input can produce different outputs at different times
       ReLU: same input ALWAYS same output (stateless within a layer)
    3. DENDRITIC COMPUTATION: HH neuron has ~10,000 active dendritic compartments
       Each can perform nonlinear computation (NMDA spike = threshold gate)
       → Single neuron ≈ small neural network
       ReLU neuron: point unit, no spatial extent
    4. ENERGY: HH neuron burns ATP for every spike regardless of signal
       → Sparse firing (1-5%) is efficient
       ReLU: dense activation (50-80% active typical ResNet layer)
       → MoE (mixture of experts) more like sparse biological coding
```

---

## 2. Plasticity: STDP/Hebb vs Backpropagation

```
    BIOLOGICAL PLASTICITY (Hebb + STDP):
    ─────────────────────────────────────
    Hebb's rule: Δw_ij ∝ x_i x_j  (co-activity)
    STDP (Spike Timing Dependent Plasticity):
      pre before post (δt > 0): LTP  ΔW = A+ exp(-δt/τ+)
      post before pre (δt < 0): LTD  ΔW = -A- exp(+δt/τ-)
      Window: ~20ms for LTP, ~20ms for LTD

    LOCAL LEARNING: depends only on pre and post activity
    No weight transport problem
    No teacher signal required (self-organized)
    Ongoing, real-time, online

    BACKPROPAGATION:
    ────────────────
    δL/δw_ij = δL/δz_j × x_i  (chain rule)
    δL/δz_j requires:
    1. Error signal from DOWNSTREAM (not local)
    2. Knowledge of all upstream weights (weight transport problem)
    3. Forward pass stored (memory expensive)
    4. Batch or mini-batch (not online)

    BIOLOGICAL PLAUSIBILITY OF BACKPROP? No.
    But nature does gradient descent somehow — evidence:
    Predictive coding implements approximation to backprop (Millidge 2020)
    Feedback alignment: random backward weights work almost as well (Lillicrap 2016)
    Target propagation: propose target activations, compute local errors
    → Biology may implement something functionally equivalent without exact backprop

    KEY DIVERGENCES:
    1. LOCAL vs GLOBAL: Hebb local; backprop global (end-to-end credit assignment)
    2. BIDIRECTIONAL WEIGHT SYMMETRY: backprop needs forward=backward weights exactly
       Biology: distinct forward (excitatory) and backward (feedback) pathways
    3. CONTINUOUS vs EPISODIC: STDP online; backprop requires discrete forward pass
    4. Catastrophic forgetting: backprop on new task destroys old knowledge
       Biology: complementary learning systems (hippocampus fast, cortex slow)
       CLS theory: hippocampus learns individual episodes; cortex slowly extracts statistics
```

---

## 3. V1 Simple Cells → Convolutional Filters

```
    BIOLOGICAL V1 SIMPLE CELLS:
    ───────────────────────────
    Receptive field: ~0.1-0.5° of visual angle
    Response: linear sum of inputs from LGN with ON/OFF center arrangement
    Selectivity: ONE preferred orientation, ONE spatial frequency
    Mathematical form: Gabor filter
    g(x,y) = exp(-(x²/σ_x² + y²/σ_y²)) cos(2πfx + φ)

    Each V1 neuron = ONE Gabor filter applied at ONE location
    Cortical magnification: more V1 for fovea than periphery

    CNN CONVOLUTIONAL FILTERS:
    ──────────────────────────
    Learned 2D filter of size k×k applied at ALL locations (weight sharing)
    First-layer CNN filters: learn Gabor-like edges (LeCun, MNIST 1990)
    Multiple filters per layer: multiple channels (like multiple V1 orientations)
    Weight sharing: same filter at every spatial location = translational equivariance

    The key insight: natural images have translational statistics
    → same edge detector useful everywhere → weight sharing is optimal
    → V1 evolved the same solution: same orientation columns tile visual space

    HISTORICAL CHAIN: Hubel & Wiesel (1959) → Fukushima Neocognitron (1980) → LeCun (1989)
    LeCun explicitly cited V1 receptive field work as motivation for CNNs

    DIVERGENCES:
    Biological: Gabor filters in V1 are followed by normalization circuits
    Complex cells = sum of simple cells at different phases = phase-invariant (= max-pooling)
    Non-classical RF surround suppression = divisive normalization
    CNN batch norm ≈ divisive normalization (but simpler, not biologically realistic)
    Feedback from higher areas modifies V1 responses → no analog in feedforward CNN
```

---

## 4. Cortical Columns vs Transformer Layers

```
    NEOCORTICAL COLUMN (6 LAYERS):
    ──────────────────────────────
    Layer 1 (molecular): apical tufts, top-down inputs
    Layer 2/3: corticocortical output, feedforward to higher areas
    Layer 4: thalamocortical input (main sensory input)
    Layer 5: output to brainstem, SC, subcortex, feedback to L6
    Layer 6: feedback to thalamus, claustrum

    Within-column: feedforward (L4 → L2/3 → L5 → L6) and feedback (L6 → L4 via thalamus)
    Between columns: lateral inhibition (L2/3 ↔ interneurons), skip connections (L5 → L2/3)
    Top-down feedback: higher area L5/6 → lower area L1/2/3 (strong!)
    Bottom-up feedforward: lower area L2/3 → higher area L4

    TRANSFORMER LAYER:
    ──────────────────
    Self-attention: all-to-all interactions within context window
    FFN: pointwise MLP (analogous to within-neuron processing)
    Skip connections: residual stream (Layer 1 in cortex has modulatory inputs)
    No explicit layer structure corresponding to L1-L6

    WEAK ANALOGIES:
    Thalamic relay → attention gate (both select which info to propagate)
    Skip connections (L2/3 → L5) → residual stream in transformer
    Bottom-up L2/3 → next L4 = feedforward layers
    Top-down L5/6 → lower L1 = feedback in transformer (some architectures)

    KEY DIVERGENCES:
    1. Feedback is DOMINANT in cortex: ~70% of synapses are feedback or recurrent
       Transformers: typically feedforward only (encoder-decoder has some feedback)
    2. Temporal structure: cortex has oscillations (gamma, theta, alpha)
       Transformers: no temporal dynamics within a layer
    3. Cell type diversity: cortex has 100+ distinct cell types
       Transformers: identical "neurons" in each layer
    4. Modulatory axes: cortex has DA, ACh, NE neuromodulation changing gain
       Transformers: no equivalent to neuromodulatory state
```

---

## 5. Biological Attention vs Self-Attention

```
    BIOLOGICAL SPATIAL ATTENTION:
    ─────────────────────────────
    Top-down: FEF/IPS decide where to attend based on task goals
    Effect: MULTIPLICATIVE gain of V1-V4 responses at attended location
    Mechanism: top-down corticocortical signals + possibly thalamic gating (pulvinar)
    Feature-based: attending to red objects enhances V4 "red-tuned" neurons globally
    Temporal: sustained (seconds) or captured by salient stimuli (reflexive, 50ms)

    TRANSFORMER SELF-ATTENTION:
    ───────────────────────────
    Attention(Q,K,V) = softmax(QK^T/√d_k) V
    Q = query (what I'm looking for)
    K = key (what's available)
    V = value (what to retrieve)
    All positions attend to all positions = all-to-all → quadratic cost

    REAL ANALOGY:
    Q ↔ task representation (what the FEF/IPS "wants")
    K ↔ feature representation in sensory areas
    V ↔ actual neural response to retrieve
    Similarity Q·K ↔ relevance match (retinotopic similarity + feature similarity)
    Softmax ↔ winner-take-all normalization (Recurrent cortical competition)

    KEY DIVERGENCES:
    1. MULTIPLICATIVE vs ADDITIVE: biological attention is gain (multiply)
       Self-attention: softmax weights then sum → weighted average not gain
    2. SPATIAL LOCALITY: biological attention operates on 2D spatial grid
       Self-attention: operates on sequence positions (1D), or patchwise (ViT)
    3. TEMPORAL DYNAMICS: biological attention unfolds over 50-500ms
       Self-attention: computed in one forward pass (instantaneous)
    4. CROSS-AREA ATTENTION: biological attention involves many areas interacting
       Self-attention: within-layer, not between "hierarchical" layers of a model
```

---

## 6. Working Memory vs KV Cache

```
    PFC WORKING MEMORY:
    ───────────────────
    Capacity: ~4 chunks (Cowan 2001)
    Duration: seconds to minutes (active maintenance required)
    Mechanism: persistent neural firing, recurrent attractor
    Content: any modality (visual, spatial, verbal, abstract)
    Updating: effortful, subject to interference
    Failure mode: distractor → activity collapse → information lost
    Information loss: partial degradation, not complete

    TRANSFORMER KV CACHE:
    ─────────────────────
    Capacity: context length tokens (2K to 200K+ tokens in GPT-4/Claude)
    Duration: entire context window (never degrades within context)
    Mechanism: stored key-value pairs from previous tokens
    Content: token representations, all modalities
    Updating: append-only (no active interference with earlier tokens)
    Failure mode: context truncation (early tokens may be lost or diluted)
    Information loss: all-or-nothing at context boundary

    KEY SIMILARITIES:
    Both: limited capacity, recent items more accessible
    Both: retrieve via content-addressing (attention/recognition)

    KEY DIVERGENCES:
    1. CAPACITY: PFC ~4 chunks; KV cache ~200K tokens
       BUT: "chunks" are semantically compressed; tokens are not compressed
       BOTH fail at ~4 "objects" in strict sensory working memory experiments
    2. ACTIVE MAINTENANCE: PFC requires ongoing neural activity; KV cache is static
    3. GATING: PFC selectively updates (attend → update WM); KV accumulates all
    4. CONSOLIDATION: PFC → hippocampus → neocortex (multi-timescale)
       KV cache → no consolidation path; in-weights learning requires training
```

---

## 7. Hippocampal Memory vs RAG

```
    HIPPOCAMPAL INDEXING THEORY (Teyler & DiScenna 1986):
    ──────────────────────────────────────────────────────
    Hippocampus stores INDEX to distributed cortical memory
    Memory = set of cortical pattern links, pointer stored in hippocampus
    Recall: retrieve hippocampal index → reactivate cortical patterns
    Fast encoding: single-trial learning of new episodes (one-shot!)
    Slow consolidation: hippocampus → neocortex via SWR replay during sleep
    Capacity: millions of episodes
    Search: content-addressable (partial cue → full memory)

    RAG (RETRIEVAL-AUGMENTED GENERATION):
    ─────────────────────────────────────
    External database stores chunks of text/knowledge
    Query encoded → vector search (FAISS, cosine similarity)
    Top-k chunks retrieved → appended to context → generate answer
    Fast encoding: add to database in real-time (no training required!)
    "Consolidation": fine-tuning on retrieved content (periodic, not automatic)

    KEY SIMILARITIES:
    Both: separate fast storage + slow generalization
    Both: content-addressable retrieval (partial match → full item)
    Both: decouple "storage" from "processing"
    Both: recent work scales capacity by adding more storage

    KEY DIVERGENCES:
    1. ENCODING: hippocampus encodes rich spatiotemporal context automatically
       RAG: requires explicit chunking, embedding, indexing (not automatic)
    2. SLEEP REPLAY: hippocampus consolidates during sleep = unsupervised transfer
       No RAG equivalent; requires explicit fine-tuning decision
    3. PATTERN COMPLETION: CA3 fills in degraded memories (Hopfield attractor)
       RAG: retrieves nearest chunk; doesn't "fill in" missing info
    4. EPISODIC vs SEMANTIC: hippocampus handles both episodes and schemas
       RAG: mostly factual/semantic; poor at episodic "when/where" recall
```

---

## 8. Dopamine RPE vs RLHF Reward Model

```
    DOPAMINE TEMPORAL DIFFERENCE SIGNAL (Schultz):
    ──────────────────────────────────────────────
    δ_t = r_t + γV(s_{t+1}) - V(s_t)

    V(s) = expected future reward from state s (encoded in striatum)
    δ > 0: unexpected reward → dopamine burst (positive TD error)
    δ < 0: expected reward omitted → dopamine dip (negative TD error)
    δ = 0: expected reward delivered → dopamine flat

    Biological implementation:
    SNc/VTA dopamine neurons → compute δ_t directly
    → signal to striatum: update V(s) and action weights
    Learning: w → w + α δ_t ∇_w V(s) (TD update, dopamine = α × δ)
    Timescale: seconds (matches TD discount γ ~ 0.9-0.99)

    RLHF REWARD MODEL:
    ──────────────────
    Human rater compares two LLM outputs: A preferred to B
    Reward model R_φ(s,a) trained to predict preferences
    RLHF objective: maximize E[R_φ(x,y)] - β KL[π_θ||π_ref]
    PPO update: update π_θ using advantage = δ_t from reward model
    δ_t(PPO) = R_φ(x,y) + γV(s_{t+1}) - V(s_t)  ← EXACT BELLMAN EQUATION

    EXACT MATHEMATICAL CONNECTION:
    R_φ = dopamine signal architecture
    V(s) = value network = striatum
    γ = discount factor = same in both
    α = learning rate = dopamine modulation strength
    PPO advantage = TD error = δ_t
    π_θ = policy = corticostriatal motor circuits
    KL regularization = not present biologically (or: prior policy = behavior prior)

    KEY DIVERGENCE:
    Biological: online, trial-by-trial, real-time, no stored gradients
    RLHF: offline episodes, batched updates, explicit gradient computation
    Biological: one reward circuit for the whole organism (every goal same DA)
    RLHF: separate reward models per task (specialized head)
    Biological: reward is internal (hunger, pain, pleasure) AND external
    RLHF: reward is always external human preference
```

---

## 9. Cerebellum Forward Model vs Model-Based RL

```
    CEREBELLUM:
    ────────────
    Receives: efference copy (copy of motor command to spinal cord)
    Predicts: expected sensory consequences of action
    Compares: actual sensory feedback vs prediction
    Error:    climbing fiber error signal → Purkinje cell LTD
    Output:   corrective motor signal BEFORE sensory feedback arrives
    Timescale: 10-100ms predictions (ahead of 200ms sensory feedback loop)

    MODEL-BASED RL FORWARD MODEL:
    ─────────────────────────────
    World model: T(s, a) → s' (predict next state given action)
    Reward model: R(s, a) → r
    Planning: rollout simulated trajectories → evaluate return → update policy
    Model-based vs model-free: cerebellar forward model IS model-based

    ANALOGIES:
    Cerebellum forward model = world model T(s,a)
    Inferior olive error signal = training supervision signal for T
    Purkinje cell LTD = parameter update in T
    Cerebellar output nucleus = planned correction applied online

    DIVERGENCES:
    Biological: prediction within ONE movement (100ms horizon)
    Model-based RL: planning over many steps (seconds to longer)
    Biological: one forward model per effector context
    RL: single universal world model
    Biological: automatic, unconscious
    RL: explicit planning, can be deliberate
```

---

## 10. Catastrophic Forgetting vs Complementary Learning Systems

```
    CATASTROPHIC FORGETTING (neural networks):
    ──────────────────────────────────────────
    Train network on task A → learns well
    Train on task B → overwrites weights → loses task A
    Gradient descent updates all weights shared between tasks
    → Interference proportional to overlap in representations

    Solutions:
    EWC (Elastic Weight Consolidation): penalize changes to important weights
    Importance: Fisher information I(θ) of old task
    L_new = L_B + λ Σ_i F_i(θ_i - θ_A,i)²
    ≈ Biological: synapse-level importance gating (Kaski & Vanhatalo, 2015)

    Progressive networks: add new columns for new tasks, no forgetting
    LoRA fine-tuning: update only low-rank delta, preserve base weights
    → These are engineered solutions to a biological problem

    COMPLEMENTARY LEARNING SYSTEMS (McClelland, McNaughton, O'Reilly 1995):
    ──────────────────────────────────────────────────────────────────────────
    Two systems with different learning rates:
    Hippocampus: FAST learning, one-shot episode storage, high interference
    Neocortex: SLOW learning, gradual extraction of statistics, no interference

    Interaction:
    New episode → immediately stored in hippocampus
    Sleep: hippocampus replays → neocortex slowly integrates
    Over many replays: neocortex extracts statistical regularities (semantic memory)
    Hippocampus can then release old episode (transfer complete)

    Neural implementation:
    Hippocampus: sparse, high-dimensional codes → minimal interference
    Neocortex: distributed, overlapping codes → good generalization, bad single-episode

    THIS IS WHAT AI LACKS:
    No automatic fast storage + slow consolidation dual system
    No sleep replay that integrates new knowledge with old
    Training requires seeing each example many times (humans: once!)
    → Few-shot learning (GPT-4, etc.) is partial solution via in-context learning
       but uses KV cache, not actual weight update
```

---

## 11. Neural Oscillations — No AI Analog (Yet)

```
    OSCILLATION BAND REFERENCE:
    Band      Freq      Brain region    Function (tentative)
    ──────────────────────────────────────────────────────────
    Delta     0.5-4 Hz  Cortex, thalamus Deep sleep, consolidation
    Theta     4-8 Hz    Hippocampus, EC Navigation, episodic memory, WM
    Alpha     8-13 Hz   Occipital, parietal Idle/inhibition, attention gating
    Beta      13-30 Hz  Motor, sensory   Motor control, top-down attention
    Gamma     30-100 Hz Visual, sensory  Feature binding, attention, WM
    SWR       150-250 Hz Hippocampus    Sleep replay, memory consolidation

    THETA-GAMMA COUPLING (working memory):
    Theta cycle (~125ms) contains gamma cycles (~25ms = ~5 gamma cycles per theta)
    Each gamma cycle holds one WM item: 5-7 items per theta cycle
    → Explains Miller's magical number 7: theta oscillation capacity!
    Proposed: different items in WM at different gamma phases within theta cycle

    GAMMA BINDING:
    Visual feature binding: "what" and "where" processed in different areas
    Hypothesis: synchronized gamma (40Hz) binds features into unified percept
    Controversial: not all evidence supports binding-by-synchrony

    SHARP-WAVE RIPPLES (SWR):
    Only occur during slow-wave sleep and quiet rest
    CA3 → CA1: synchronous burst → ~200 Hz ripple in CA1
    Replay is COMPRESSED (~20×) and can be REVERSED (future planning?)
    Disrupting SWRs (mild perturbation at SWR onset) → impairs recall next day

    WHY NO AI ANALOG:
    Transformers have no temporal dimension within a layer
    No oscillatory competition between representations
    No sleep phase for offline consolidation
    Possible future: temporal spiking networks could implement oscillatory dynamics
    → Sparse representation × temporal coding could be far more efficient
```

---

## 12. Sparse Coding vs Dense Transformers

```
    BIOLOGICAL SPARSE CODING (Olshausen & Field 1996):
    ──────────────────────────────────────────────────
    Primary visual cortex: ~1-5% of V1 neurons active at any time
    Sparse code: most neurons silent → efficient energy use, large capacity
    Redundancy reduction: remove correlations → independent components
    ICA / sparse dictionary learning recovers Gabor-like filters from natural images
    → V1 LEARNED sparse codes from natural image statistics

    Computationally: overcomplete dictionary D, sparse code s, image x:
    min_s ||x - Ds||² + λ||s||₁   (LASSO = L1 sparse coding)
    → This IS what V1 computes (approximately)

    DENSE TRANSFORMER ACTIVATIONS:
    ───────────────────────────────
    Standard transformer: ~60-80% of neurons active per token
    Energy-inefficient: nearly all parameters engaged for every token
    Semantic richness: dense representation distributes meaning everywhere

    MIXTURE OF EXPERTS (MoE) → SPARSITY:
    MoE: route each token to k of N expert FFN blocks
    GPT-4 rumored: 8 of 120 experts per token (k=8/N=120 → 6.7% sparse)
    Dramatically more parameter-efficient: total params >> active params
    → Closer to brain's sparse coding principle
    → But routing algorithm ≠ lateral inhibition in cortex

    BRAIN-LIKE SPARSE CODING IN AI (future directions):
    k-WTA (k-Winners Take All): artificial version of lateral inhibition
    L1 regularization: promotes sparse activations
    Binary/ternary activations: extreme sparsity (SNNs)
```

---

## 13. Energy Efficiency Gap

```
    BRAIN:                          MODERN LLM:
    ─────────────────────────────────────────────────────
    Power:      20 W               700 W (A100 training)
    "Synapses": 10¹⁴ per brain     175B parameters (GPT-3)
    Energy/op:  ~10⁻¹⁵ J (synapse) ~10⁻¹² J (FLOP in GPU)
    Efficiency: ~2×10¹⁴ ops/W      ~3×10¹⁵ FLOPs/W (A100)
    Throughput: ~10¹⁴ ops/s        ~3×10¹⁵ FLOPs/s (A100)

    On raw FLOPs/W: A100 looks MORE efficient than brain!
    BUT: this comparison is misleading because:
    1. Brain "operations" (spikes + synaptic events) > 1 FLOP each
    2. Brain generalizes from 1 example; LLM needs billions
    3. Brain does learning + inference simultaneously
    4. Brain does multimodal, embodied, open-world vs narrow task

    LANDAUER LIMIT:
    Minimum energy per irreversible bit operation: k_B T ln 2
    At 37°C: 2.87×10⁻²¹ J per bit erasure
    Modern GPU bit operation: ~10⁻¹⁸ J (1000× above Landauer limit)
    Brain synapse: ~10⁻¹⁵ J (10⁶× above Landauer limit — still room to improve)
    Both are far above the Landauer limit → neither is thermodynamically efficient

    BIOLOGICAL TRICKS FOR EFFICIENCY:
    1. Sparse firing (~1% active): 100× savings vs dense coding
    2. Analog computation: graded potentials in dendrites (no ADC/DAC cost)
    3. Short-range wiring: most synapses local (cortex: 90% within 1mm)
    4. Asynchronous: no global clock (no synchronization overhead)
    5. Myelination: fast long-range with minimal spike energy
    → SNN chips (Intel Loihi 2, IBM TrueNorth) implement some of these
```

---

<!-- @editor[structure/P2]: Missing Decision Cheat Sheet -- Open Problems table is "what solving X unlocks" not "use X when Y". Add: "To understand [AI concept], study [neuroscience mechanism]" format -->
## Open Problems: Neuroscience × AI Table

| Neuroscience mystery | What solving it would unlock for AI |
|---------------------|-------------------------------------|
| How does the brain learn from 1-10 examples? | True few-shot learning without large-scale pre-training |
| Mechanism of sleep replay / memory consolidation | Continuous lifelong learning without catastrophic forgetting |
| How do oscillations bind representations? | Temporal coding → 100× more information per neuron |
| Mechanism of dendritic computation (NMDA spikes) | Replacing point-neuron approximation → deeper dendritic networks |
| How does PFC maintain >4 items with practice? | Chunking / compression → higher effective WM capacity |
| What makes the brain's RL sample-efficient? | Model-based + model-free hybrid RL with minimal exploration |
| How does selective attention arise from bottom-up/top-down interactions? | Dynamic computation graphs (not static weights) |
| How does the brain represent abstract concepts compositionally? | Systematic generalization (transformers struggle with this) |
| How does neocortex do unsupervised slow feature extraction? | Self-supervised learning closer to biological theory |
| What is the algorithmic basis of causal inference in PFC? | Causal reasoning, not just pattern matching |
| Why does damage to cerebellum impair timing but not consciousness? | Temporal computation separated from awareness |
| How do grid cells implement the hex lattice? | Systematic metric structure in learned embeddings |

---

<!-- @editor[bridge/P3]: Natural bridge to .NET/Azure expertise unused -- Azure Service Bus as neurotransmitter broadcast, VSTS gated check-in as BG NoGo pathway, Azure CDN caching as cortical memory consolidation. Supplementary flavor per style contract -->
## Common Confusion Points

**"AI is inspired by the brain" is mostly myth**: Perceptrons (Rosenblatt 1957) were inspired
by neurons. CNNs were inspired by V1. But transformers were inspired by attention in machine
translation (Bahdanau 2015), not biological attention. LSTMs were invented to solve vanishing
gradients, not to model hippocampus. Most modern AI is engineering progress, not neuroscience
translation. The real insight is in the OTHER direction: AI tools help us understand brains.

**Backpropagation is not "how the brain learns"**: Despite popular claims, the brain
doesn't compute gradients via backpropagation (weight transport problem alone makes it
implausible). But the brain DOES gradient descent in some functional sense (it improves
on objective functions). The question is what the biological implementation is.
Predictive coding, target propagation, and contrastive Hebbian learning are candidates.

**Bigger transformers are not "closer to the brain"**: GPT-4 size (~1.8T parameters?) is much
larger than the number of synapses in the brain (~10^14), but each parameter is a single
scalar vs each synapse involves complex molecular machinery. More parameters means better
approximation of the training distribution, not closer to biological intelligence.

**The RLHF-dopamine connection is real but not identical**: The Bellman equation and TD
learning are the same math in both cases. But biological RL is sample-efficient (learn from
single trials), uses model-based planning (OFC/hippocampus), and integrates multiple reward
modalities (hunger, pain, social reward, novelty). RLHF uses one scalar reward (human
preference), needs millions of examples, and has no model of the task.
