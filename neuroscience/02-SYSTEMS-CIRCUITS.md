# Neural Systems and Circuits

## The Big Picture

```
    SYSTEMS NEUROSCIENCE LANDSCAPE — WITH CROSS-SYSTEM CONNECTIONS
    ══════════════════════════════════════════════════════════════════

    VISUAL SYSTEM                        MOTOR SYSTEM
    retina → LGN → V1 → V2-V5           M1 → CST → spinal cord → muscle
       ↓ ventral (IT: what)                 ↑ disinhibition
       ↓ dorsal (MT/parietal: how/where) ┌──┴────────────────────┐
       └──→ MOTOR PLANNING (parietal) ───┤  BASAL GANGLIA        │
       └──→ MEMORY (hippocampus) ────────┤  action selection     │
                                         │  (Go/NoGo)            │
    HIPPOCAMPUS                          └──────────────┬────────┘
    EC → DG → CA3 → CA1 → subiculum              ↑ also feeds motor
       │    │                                           │
       │    └──→ pattern separation                  CEREBELLUM
       │         (orthogonalize)                    error correction
       └──→ consolidation during sleep SWRs             │
              ↓                                         │ forward model
         NEOCORTEX (long-term memory)                   ↓
              ↑ index (hippocampal indexing theory) motor output correction
              ↑ retrieval cue reactivates cortex

    Cross-system interactions:
    • BG + cerebellum BOTH feed thalamus → M1: parallel channels for action
    • Visual dorsal stream → parietal → motor: visuomotor transformation
    • Hippocampus → prefrontal → BG: episodic memory gates action selection
    • Cerebellum ↔ BG: connected via thalamus; cerebellar timing + BG selection = coordinated action

    Common themes across systems:
    • Hierarchical processing (simple → complex features)
    • Feedforward + feedback (bidirectional at every level)
    • Lateral inhibition (contrast enhancement, winner-take-all selection)
    • Topographic maps (visual retinotopy, auditory tonotopy, motor somatotopy)
    • Oscillatory synchronization for inter-area communication
```

---

## Visual System

### Retina

```
    LIGHT → PHOTORECEPTORS → INNER RETINAL NEURONS → GANGLION CELLS → OPTIC NERVE

    Photoreceptors:
    Rods: ~120M, scotopic (low light), not at fovea, single pigment (rhodopsin)
    Cones: ~6M, photopic (bright light), 3 types (S/M/L: blue/green/red)
    Fovea: ~50,000 cones in 0.3mm², one-to-one pathway to ganglion cells → high acuity

    Phototransduction cascade (cone example):
    Photon → isomerizes retinal (11-cis → all-trans) in opsin
    → Activates transducin (G_t) → activates PDE6 (phosphodiesterase)
    → Hydrolyzes cGMP → closes cGMP-gated channels → hyperpolarization (!)
    → Reduces glutamate release onto bipolar cells
    Note: photoreceptors hyperpolarize to light (unlike most sensory systems)

    BIPOLAR CELLS: first synapse (chemical)
    ON bipolars: mGluR6 → hyperpolarized in dark, depolarized in light
    OFF bipolars: iGluR → depolarized in dark, hyperpolarized in light

    HORIZONTAL CELLS: lateral inhibition between photoreceptors and bipolars
    → Creates center-surround receptive fields via signal subtraction

    CENTER-SURROUND RECEPTIVE FIELD (lateral inhibition mechanism):
    ON-center cell: responds to spot of light in center (excitation), inhibited by surround
    OFF-center cell: inhibited by center light, excited by surround light
    This enhances edges and contrast → efficient coding principle
```

### Lateral Geniculate Nucleus (LGN)

```
    6 layers in each LGN (contralateral eye drives layers 1,4,6; ipsilateral drives 2,3,5)
    Layer crossing at optic chiasm: nasal fibers cross, temporal stay ipsilateral
    → Both LGNs receive info from both eyes (half each)
    → Damage to left optic radiation → right visual field deficit (homonymous hemianopia)

    Parallel pathways:
    M (magnocellular) layers 1,2: large cells, fast, motion, coarse depth
    P (parvocellular) layers 3-6: small cells, slower, color, fine detail
    K (koniocellular) between layers: color (S-cone), diffuse projections
```

### Primary Visual Cortex (V1)

Hubel and Wiesel (Nobel 1981): discovered orientation selectivity and ocular dominance columns.

```
    Simple cells (V1 Layer 4, also layer 6):
    Respond to oriented edges at specific angle and position
    Model: linear sum of LGN inputs arranged in rows
    Gabor function approximation: g(x,y) = exp(-x²/2σ_x² - y²/2σ_y²)cos(2πfx + φ)
    → Gabor filter ≈ V1 simple cell receptive field

    CNN/GABOR BRIDGE (direct biological motivation):
    LeCun's convolutional neural networks (1989) were explicitly motivated by Hubel & Wiesel.
    The architectural isomorphism:
      LGN center-surround cells  ←→  early CNN filters (edge detectors, Laplacian of Gaussian)
      V1 simple cells (Gabor RF) ←→  first convolutional layer filters (oriented edges)
      V1 complex cells           ←→  max-pooling over phase-shifted simple cells (position invariance)
      V2/V4 (texture, curvature) ←→  deeper CNN layers (more complex feature selectivity)
      IT cortex (object identity) ←→  final CNN layers (class-selective units)

    The weight sharing in CNNs (same filter applied across all spatial positions) is
    the mathematical formalization of the biological observation that similar receptive
    field properties appear at every location in the visual field (translation invariance
    of the processing machinery, not of the representation).

    Key divergence: V1 also implements divisive normalization (responses normalized by
    local population activity) — this is not in basic CNNs but is in some newer architectures
    (local response normalization in AlexNet was an approximate version).

    Full systematic treatment: see 04-AI-BRIDGE.md.

    Complex cells (V1 layers 2,3,5):
    Respond to oriented edges regardless of exact position within RF
    Model: sum of simple cells with different phases
    → Position invariance, direction selectivity, end-stopping

    Cortical columns in V1:
    ┌────────────────────────────────────────────────────────────┐
    │  HYPERCOLUMN (~1mm²): processes all orientations (0-180°), │
    │  all spatial frequencies, for one patch of visual field    │
    │                                                            │
    │  Orientation columns: 0°→180° rotates around "pinwheels"  │
    │  Ocular dominance columns: alternating L/R stripes ~0.5mm  │
    │  Spatial frequency columns: high-to-low across surface     │
    │                                                            │
    │  Layer organization (V1 example):                          │
    │  Layer 4C: LGN input (M to 4Cα, P to 4Cβ)                 │
    │  Layer 2/3: corticocortical output to V2, V4               │
    │  Layer 5: output to superior colliculus, pulvinar           │
    │  Layer 6: feedback to LGN                                  │
    └────────────────────────────────────────────────────────────┘
```

### Beyond V1: Visual Hierarchy

```
    V1 → V2 → V3/V3A → V4 → IT (inferior temporal)
         ↘          ↘ V5/MT (middle temporal)
                         ↓
    VENTRAL STREAM ("what"):
    V1 → V2 → V4 → IT → perirhinal → hippocampus
    Color, texture, shape, object identity, face recognition
    Hubel: "each synapse doubles the complexity of selectivity"
    IT cortex: face cells (respond to faces but not scrambled faces)
    Jennifer Aniston neuron: single neuron responds specifically (Quiroga et al. 2005)

    DORSAL STREAM ("where/how"):
    V1 → V2 → MT/V5 → MST → VIP → parietal → frontal
    Motion, depth, spatial location, visuomotor control
    MT lesion: patient can see objects but not motion (akinetopsia, Zihl 1983)
    Parietal lesion: spatial neglect (hemispatial), Balint's syndrome

    MT (V5): motion processing
    Direction-selective cells (50% of MT)
    Speed-selective cells
    Optic flow patterns → MST → self-motion perception
    Lesion/TMS: impairs motion perception, smooth pursuit eye movements
```

---

## Motor System

### Primary Motor Cortex (M1)

```
    Somatotopic map (Penfield's homunculus):
    Medial: leg, trunk
    Lateral: arm, hand, face (disproportionately large: fine motor control)

    Precentral gyrus (BA4): M1, largest pyramidal (Betz) cells in cortex
    Premotor cortex (PMC, BA6 lateral): learned motor sequences, observation (mirror neurons?)
    Supplementary motor area (SMA, BA6 medial): bimanual coordination, self-initiated actions
    Readiness potential (Bereitschaftspotential): SMA/M1 activity 500ms before voluntary movement

    M1 neurons encode:
    Population vector: weighted sum of preferred directions → predicts actual direction
    Force: firing rate correlates with force (Evarts)
    Muscle synergies: groups of muscles co-activated
    Reach velocity, reach end-point (different cell populations)
```

### Corticospinal Tract (CST)

```
    Direct monosynaptic pathway: M1 → spinal motor neuron → muscle
    This is a PRIMATE SPECIALIZATION (rodents have much weaker CST)
    → Enables fine digit control (precision grip — uniquely primate)
    → CST damage (stroke) → loss of fine motor control (can't button shirt)

    CST anatomy:
    Pyramidal cells (layer 5 M1) → axons through internal capsule
    → Brainstem → pyramidal decussation (90% cross at medullary pyramids)
    → Lateral corticospinal tract → motor neurons in ventral horn
    → 10% ipsilateral: anterior corticospinal tract (proximal muscles)

    Total CST: ~1M axons per side
    Largest axons: Betz cells → 4-20 μm diameter → fastest conduction (60-70 m/s)

    Alpha motor neurons:
    Large cells in ventral horn, the "final common pathway"
    Receive input from: CST, interneurons, Ia fibers (spindle stretch)
    Motor unit: one motor neuron + all muscle fibers it innervates
    Type I (slow-twitch, fatigue-resistant): smaller motor neurons recruited first
    Type II (fast-twitch, fatigue rapidly): larger motor neurons recruited later
    Henneman size principle: ascending order of recruitment by motor unit size
```

### Cerebellum: Error-Based Learning

```
    Input:
    Mossy fibers (from spinal cord, pons, vestibular): to granule cells + DCN
    Climbing fibers (from inferior olive ONE per Purkinje cell): teaching signal

    Processing:
    Granule cells (most numerous in brain: ~70 × 10⁹): relay mossy to Purkinje
    Purkinje cells: ONLY output of cerebellar cortex, large, elaborate dendrites
    Inhibitory (GABA), project to deep cerebellar nuclei (DCN)
    Basket/stellate cells: inhibit Purkinje (feed-forward inhibition)

    Output:
    Deep cerebellar nuclei (DCN): dentate (lateral, largest → thalamus → M1/PFC)
                                   interpositus (midline → red nucleus, spinal)
                                   fastigial (medial → vestibular, spinal)

    THE CEREBELLAR LEARNING MODEL (Marr-Albus-Ito):
    Climbing fiber carries error signal (actual - predicted outcome)
    Causes LTD (long-term depression) at activated granule-Purkinje synapses
    → Next time same mossy fiber pattern → Purkinje fires LESS → DCN disinhibited less
    → Effectively: learn to suppress erroneous motor commands

    This is an internal forward model:
    Motor command sent → forward model predicts sensory consequences
    Compare to actual sensory feedback → error signal
    → Cerebellum predicts consequences and corrects BEFORE they happen
    → Without cerebellum: ataxia (tremor, coordination loss, dysmetria)
    → Cerebellar timing: 10-100ms range → critical for motor timing
```

---

## Basal Ganglia: Action Selection

### Circuit Structure

```
    CORTEX (all areas) ──────────────────────────────────────────┐
         │                                                         │
         ▼ (glutamate, excitatory)                                 │
    STRIATUM (caudate + putamen)                                  │
         │                                                         │
         ├── DIRECT PATHWAY (Go):                                  │
         │   D1 receptor → Gs → cAMP↑ → EXCITED                   │
         │   Striatum(D1) → [inhibit GPi/SNr] → [disinhibit Thal]│
         │   → Thalamus active → Cortex active → MOVE             │
         │                                                         │
         └── INDIRECT PATHWAY (NoGo):                             │
             D2 receptor → Gi → cAMP↓ → SUPPRESSED                │
             Striatum(D2) → [less inhibit GPe] → [GPe inhibits STN]│
             STN → GPi/SNr → [inhibit Thal] → Cortex suppressed   │
             → No movement                                         │

    HYPERDIRECT PATHWAY: Cortex → STN directly (fast NoGo/cancellation)
    Used for: rapid stop-signal cancellation (SSRT), conflict resolution

    DOPAMINE from SNc modulates both:
    DA release → D1 (direct) enhanced → D2 (indirect) suppressed
    = Net: dopamine promotes selected action

    PARKINSONS DISEASE:
    SNc dopamine neurons die (80% loss before symptoms)
    → Insufficient D1 activation → insufficient disinhibition of thalamus
    → Excessive D2 release of indirect pathway → hypokinesia (rigidity, bradykinesia)
    → Tremor at rest from altered cerebellar-BG interaction
    Treatment: L-DOPA (crosses BBB → DA), DBS (deep brain stimulation in STN or GPi)

    HUNTINGTON'S DISEASE: CAG repeat in HTT → misfolded huntingtin
    → First loses indirect pathway (D2 striatum) → hyperkinesia (chorea)
    → Then direct pathway → final hypokinesia + dementia
```

### Basal Ganglia as Action Selection and RL Substrate

**Go/NoGo isomorphism with reinforcement learning**
The direct (Go) and indirect (NoGo) pathways implement a biological actor-critic architecture. The striatum receives value-weighted cortical inputs and segregates them by dopamine receptor type: D1 neurons report "value of acting" (Go); D2 neurons report "cost of acting / value of not acting" (NoGo). The net output (disinhibition of thalamus) represents the action selection decision.

Dopamine from SNc encodes reward prediction error (Schultz 1997): DA bursts when reward exceeds expectation (positive RPE), DA dips when reward is worse than expected (negative RPE). This is the temporal difference (TD) error: δ = r + γV(s') - V(s). D1 synapses potentiate with DA bursts (LTP, Go pathway strengthened); D2 synapses depress with DA bursts (LTD, NoGo pathway weakened). Together they implement TD learning in biology.

**Scheduler analogy for distributed systems**
The BG architecture is a winner-take-all scheduler:
- Many cortical areas (representing competing actions/plans) send excitatory input to striatum
- The striatum selects the "best" action based on current dopamine-modulated weights
- The selected action gets disinhibited through thalamus; all others remain suppressed
- The hyperdirect pathway (cortex → STN, bypassing striatum) is the interrupt mechanism: fast NoGo that cancels the current selection (stop-signal task analog)

This maps to: N runnable processes → scheduler selects highest-priority → other processes blocked → interrupt handler can preempt. Parkinson's = scheduler stuck; Huntington's early = scheduler too permissive (too many actions allowed simultaneously → chorea).

---

## Hippocampus: Memory and Navigation

### Circuit Anatomy

```
    ┌─────────────────────────────────────────────────────────────┐
    │  HIPPOCAMPAL CIRCUIT                                         │
    │                                                             │
    │  ENTORHINAL CORTEX (EC) ─────────────────────────────┐      │
    │  (Layer II → DG, CA3)  ┌─────────────────┐          │      │
    │  (Layer III → CA1)     │                 │          │      │
    │                        ▼                 ▼          │      │
    │  DG (Dentate Gyrus)→ CA3 ──[Schaffer]→ CA1 ──→ Subiculum ──┤ │
    │  (granule cells)  (mossy)   collaterals    │                │ │
    │       │           (CA3                     ▼                │ │
    │       │           recurrent)          EC Layer V            │ │
    │       ▼                                    │                │ │
    │  High expansion:                     Neocortex ←────────────┘ │
    │  ~200,000 → 1M GCs                   (memory consolidation)   │
    └─────────────────────────────────────────────────────────────┘

    DG: pattern separation (orthogonalize similar inputs → distinct representations)
    ~95% sparsity: most cells silent most of time
    Adult neurogenesis in DG (mice confirmed; humans controversial)

    CA3: pattern completion (partial cue → full memory via recurrent connections)
    ~2% activity
    Associative recall: damaged input → restored via recurrent CA3
    Model: Hopfield network (attractor memory, see 03-COGNITION-COMPUTATION)

    CA1: mismatch detection, output stage
    Receives both EC (direct, bypassing DG/CA3) and CA3 (Schaffer collaterals)
    Compares expectation (EC) vs memory (CA3)
    → Novelty signal when mismatch

    Theta oscillations (4-12 Hz):
    Generated by medial septal nucleus cholinergic/GABAergic neurons
    Organize hippocampal processing in theta sequences (~125ms)
    Phase precession: place cell fires at different theta phases as rat traverses field
    → Time-compressed replay of spatial trajectory
```

### Place Cells and Grid Cells

```
    PLACE CELLS (O'Keefe and Dostrovsky 1971 → O'Keefe Nobel 2014):
    CA1 neurons fire when animal is at a specific location in environment
    One cell = one "place field" (1-20% of environment covered)
    Remapping: same environment → same map; new environment → new random map
    "Cognitive map": Tolman's theory implemented in hippocampus

    GRID CELLS (Moser lab 2005 → Nobel 2014 with O'Keefe):
    Entorhinal cortex neurons fire at vertices of a regular hexagonal lattice
    Grid spacing: 25 cm (MEC Layer II) to 10 m (MEC Layer III)
    Grid = internal coordinate system (GPS-like)
    Grid + place: grid cells are the metric; place cells are the map
    Head direction cells (Taube): always fire when head faces a specific direction
    Border cells: fire near walls/edges of environment

    SHARP-WAVE RIPPLES (SWR):
    High-frequency oscillation (150-200 Hz) during rest/sleep
    CA3 → CA1 spike volley → replay of recent experience
    Compressed 6-20× (100ms SWR = 1-2s of experience)
    Memory consolidation: hippocampus → cortex transfer during sleep SWRs
    Disrupting SWRs during sleep impairs subsequent memory recall
    → Hippocampal indexing theory: hippocampus holds index to cortical memory traces
```

### Long-Term Potentiation (LTP): Cellular Basis of Memory

Discovered by Bliss and Lømo, 1973 (theta burst stimulation of perforant path → dentate).

```
    INDUCTION (EARLY LTP, E-LTP, < 3 hours):
    High-frequency stimulation (HFS: 100 Hz, 1s) or theta-burst stimulation
    → Strong postsynaptic depolarization → unblock NMDA channels
    → Ca²⁺ influx through NMDA
    → Ca²⁺ activates CaMKII (calmodulin-dependent protein kinase II)
    → CaMKII phosphorylates AMPA receptors (Ser831) → higher single-channel conductance
    → CaMKII triggers AMPA receptor trafficking:
       AMPA receptors from endosomes → membrane → more receptors at synapse
    → Larger EPSP for same presynaptic release = enhanced synaptic strength

    MAINTENANCE (LATE LTP, L-LTP, > 3 hours):
    Requires: PKA, MAPK, and transcription factor CREB
    → New protein synthesis → structural changes:
      Spine enlargement (actin remodeling)
      Synapse splitting (one synapse → two)
    → Persistent because of structural change (doesn't depend on ongoing signaling)

    HEBB'S RULE in molecular form:
    "Fire together → wire together" = NMDA coincidence detection + CaMKII + AMPA trafficking
    Formal: Δw_ij = η × x_i × x_j (where w = synaptic weight, x = activity)
    NMDA: requires pre (glutamate) AND post (depolarization) → biological Hebb

    LTD (Long-Term Depression): opposite of LTP
    Low-frequency stimulation (1 Hz, 15 min) → weak Ca²⁺ influx
    → Activates calcineurin (phosphatase) → dephosphorylates AMPA receptors
    → AMPA receptor endocytosis → reduced synaptic strength
```

---

## Decision Cheat Sheet

| System/Area | Key function | Damage/Disruption effect |
|-------------|-------------|--------------------------|
| V1 | Edge detection, orientation maps | Cortical blindness in contralateral hemifield |
| V4 | Color processing | Achromatopsia (can't perceive color) |
| MT/V5 | Motion detection | Akinetopsia (sees world as snapshots) |
| IT cortex | Object/face recognition | Visual object agnosia, prosopagnosia |
| M1 | Motor commands to spinal cord | Contralateral paresis/paralysis |
| Cerebellum | Motor coordination, timing | Ataxia, dysmetria, intention tremor |
| Basal ganglia (SNc) | Action selection, motivation | Parkinson's (hypokinesia) |
| Striatum direct | Facilitating action | Loss → difficulty initiating movement |
| Hippocampus (CA1) | Episodic memory encoding | Anterograde amnesia (HM case) |
| Hippocampus (CA3) | Pattern completion | Impaired recall from partial cues |
| DG | Pattern separation | Confusing similar memories |
| Grid cells (MEC) | Spatial metric/coordinates | Navigation deficits |
| Amygdala (BLA) | Fear conditioning | Impaired fear learning, enhanced extinction |
| OFC | Value updating | Perseveration, insensitivity to outcome change |

---

## Common Confusion Points

**V1 simple cells are Gabor filters, but V1 is NOT just Gabor filter convolution**: Yes,
V1 simple cells can be well modeled by Gabor filters, and this is the direct biological
motivation for convolutional filters in CNNs (LeCun explicitly referenced this). But V1
also has normalization (divisive normalization = gain control), feedback from V2/V3, and
cross-orientation suppression. The Gabor filter captures the linear part; the normalization
makes it represent image statistics efficiently.

**Hippocampus stores memories vs consolidation**: The hippocampus is NOT permanent storage
for most memories. It's a temporary buffer/index. Memories are consolidated to neocortex
during sleep (SWR replay). Hippocampal damage → anterograde amnesia (can't form new memories),
but OLD memories before damage may be intact (remote memories are in neocortex). HM (Henry
Molaison) lost his hippocampus in 1953 surgery, had perfect memory for events before 1953
but could not form any new declarative memories.

**The 'where vs what' pathways are not rigid**: The dorsal/ventral stream distinction
is a useful framework but oversimplified. Recent work shows extensive cross-talk, and the
dorsal stream processes more than spatial location (it's more accurately "action-related").
The anterior temporal lobe in the ventral stream also has spatial properties. Use it as
a first approximation, not a law.

**LTP at a synapse does not equal learning**: LTP is the cellular mechanism of synaptic
strengthening that supports learning. But:
(1) Learning likely requires patterned LTP/LTD across many synapses, not just one
(2) Not all learning uses NMDA-dependent LTP (some uses different mechanisms)
(3) LTP can be blocked in slice without preventing learning in vivo
(4) The relationship between synaptic plasticity and behavioral learning is complex
    and active research area

## Engineering Bridges: Systems-Level Correspondences

| Neural System | Engineering / CS Analog | Key Parallel |
|---------------|------------------------|--------------|
| Visual hierarchy V1→V2→V4→IT | Convolutional neural network layers | Each layer extracts more complex features; Gabor filters = convolutional kernels; max-pooling = complex cell position invariance |
| V1 divisive normalization | Batch normalization / layer norm | Normalizes responses by local population activity; prevents saturation; efficient coding of natural images |
| Basal ganglia direct/indirect | Go/NoGo actor in RL; process scheduler | Winner-take-all action selection; dopamine = TD reward prediction error; D1/D2 = value vs cost signals |
| Cerebellum (Marr-Albus-Ito model) | Kalman filter + forward model | Predicts sensory consequences of motor command; error signal (climbing fiber) corrects model; internal model reduces feedback delay |
| Cerebellar learning (LTD at granule-Purkinje synapse) | Supervised learning with error signal | Climbing fiber = teaching signal; supervised weight update; error-based not reward-based |
| Hippocampal indexing | Database index / content-addressable memory | Hippocampus stores compressed indices to distributed cortical representations; recall = pointer dereference into cortex |
| CA3 pattern completion | Hopfield associative memory | Recurrent connections complete partial patterns; attractor dynamics; retrieval degrades gracefully (not catastrophically) |
| CA3/DG pattern separation | Locality-sensitive hashing | DG orthogonalizes similar inputs → distinct CA3 attractors; prevents false-alarm pattern completion |
| Sharp-wave ripple memory consolidation | Write-back cache flush to persistent storage | Fast hippocampal traces replayed into slow neocortex during offline (sleep) → long-term storage |
| Motor cortex population vector | Distributed read-out of high-dimensional code | No single neuron encodes direction; population weighted sum gives movement direction (Georgopoulos 1986) |
| Top-down visual attention | Query-key attention mechanism | PFC sends attention signal that gates which V4/IT neurons are amplified — selective gain control by relevance |
