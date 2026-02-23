# Neural Systems & Circuits

---

## Big Picture

```
SENSORY IN          MOTOR OUT
    │                    ▲
    ▼                    │
Thalamus ────────→ Motor cortex
    │                    │
    ▼                    │
Sensory cortex      Basal ganglia ← Striatum ← Dopamine (VTA)
    │               (action selection, reward learning)
    ▼
Higher cortex (PFC, parietal) → Executive function, working memory
    │
    ▼
Hippocampus → Episodic memory, spatial navigation

KEY ARCHITECTURE: Thalamus as relay + gate. Cortex as hierarchical processor.
Basal ganglia and cerebellum as error-correcting feedback loops.
```

---

## Visual System

The most thoroughly studied sensory system. Blueprint for how sensory cortex works.

### Retina → V1 Pathway

```
Photon
  → Photoreceptor (rod: dim light; cone: color/detail)
  → Bipolar cell
  → Retinal ganglion cell (RGC)
     Center-surround receptive field (ON or OFF center)
     → optic nerve → optic chiasm (nasal fibers cross)
  → Lateral Geniculate Nucleus (LGN) of thalamus
     M-layers (magnocellular): motion, low spatial freq
     P-layers (parvocellular): color, high spatial freq
     K-layers (koniocellular): color opponent, S-cone
  → Primary visual cortex V1 (striate cortex, area 17)

V1 MAP: Retinotopic — cortical area proportional to visual acuity
        Fovea (central): overrepresented (1° of fovea = ~10 mm cortex)
        Periphery: underrepresented
```

### V1 Receptive Fields (Hubel & Wiesel, Nobel 1981)

```
SIMPLE CELL: linear spatial filter
  Oriented gabor-like receptive field
  ON region (excitatory) and OFF region (inhibitory) side-by-side
  Responds to oriented edge or bar at specific position and orientation
  → "Simple" because response predictable from linear model

COMPLEX CELL: nonlinear
  Responds to oriented bar at ANY position within RF
  Phase-invariant → built from many simple cells (energy model)

HYPERCOMPLEX (end-stopped): end-stopped
  Responds to short bar or corner, suppressed by long bar
  → Detects line terminations and corners

ORIENTATION COLUMNS:
  Neurons in a column prefer same orientation
  Orientation preference rotates ~180° across ~1 mm (pinwheel singularities)
  Ocular dominance columns: alternating L/R eye preference
  Hypercolumn: complete set of orientation + ocular dominance (~1 mm²)
```

### Visual Hierarchy

```
V1 → V2 → V4 → IT cortex           (VENTRAL: "what" pathway — object recognition)
V1 → V2 → MT/V5 → MST → parietal   (DORSAL: "where/how" pathway — motion, action)

Response properties become more complex up the hierarchy:
V1: oriented edges, spatial frequency
V4: color, shape
IT (inferotemporal): faces, objects, categories
  • "Grandmother cell" debate: single neurons encode specific complex objects?
  • Population code more likely: Jennifer Aniston cell paper (Quiroga 2005) shows
    sparse but not single-cell encoding
```

---

## Auditory System

```
Sound wave → Cochlea (frequency decomposition — mechanical Fourier transform)
  Basilar membrane: tonotopic — base responds to high freq, apex to low freq
  Hair cells (inner): transduce mechanical → electrical
    Tip links → stretch → mechanically gated K⁺/Ca²⁺ channels
  → Auditory nerve (AN) → Cochlear nucleus → Superior olive (binaural)
  → Inferior colliculus → Medial geniculate nucleus (MGN, thalamus)
  → Primary auditory cortex (A1): tonotopic map

BINAURAL PROCESSING (sound localization):
  Interaural time difference (ITD): < 700 μs → azimuth (horizontal)
  Jeffress model: coincidence detector array (delay lines)
  Interaural level difference (ILD): high freq → elevation/azimuth
```

---

## Motor System

### Hierarchy

```
INTENTION (prefrontal, premotor)
  │
  ▼
MOTOR CORTEX (M1) — primary motor cortex
  │ Somatotopic map (homunculus: hand/face overrepresented)
  │ Upper motor neurons (UMN)
  │
  ▼
SPINAL CORD — lower motor neurons (LMN, alpha motor neurons)
  │ Segmental reflex circuits (interneurons, Renshaw cells)
  │
  ▼
MUSCLE (neuromuscular junction — NMJ)
  Acetylcholine → nAChR → motor end plate potential → twitch

MODULATION BY:
  Basal ganglia: action selection, suppress competing programs
  Cerebellum: timing, error correction, learned coordination
```

### Cerebellum

```
FUNCTION: Forward model / error correction for motor commands

Inputs:
  Mossy fibers (pontine nucleus → granule cells): efference copy
  Climbing fibers (inferior olive → Purkinje cells): error signal

Purkinje cell: sole output of cerebellar cortex → inhibitory
  Simple spikes (100 Hz): continuous modulation
  Complex spike: climbing fiber input → ~1 Hz → motor error signal

CEREBELLAR LEARNING (Marr-Albus-Ito model):
  Climbing fiber fires when movement error occurs
  → LTD of parallel fiber → Purkinje cell synapse
  → Purkinje inhibition of deep nucleus changes
  → Motor correction learned

Analogy: Purkinje cell = SUPERVISED LEARNING unit
         Climbing fiber = error teacher signal
```

### Basal Ganglia

```
COMPONENTS: Striatum (input) → GPi/SNr (output) → Thalamus → Cortex

DIRECT pathway (Go): Striatum → GPi (inhibit) → Thalamus disinhibited → Cortex ↑
INDIRECT pathway (NoGo): Striatum → GPe → STN → GPi (excite) → Thalamus inhibited → Cortex ↓

DOPAMINE FROM SNc:
  D1 receptors (direct pathway): dopamine → potentiate "Go"
  D2 receptors (indirect pathway): dopamine → suppress "NoGo"
  → Dopamine facilitates selected action, suppresses alternatives

ACTOR-CRITIC in basal ganglia:
  Striatum (actor): selects action
  Dopamine (critic): reward prediction error signal
  → See 03-AI-BRIDGE.md for TD-learning connection

PARKINSON'S: loss of SNc dopamine neurons → hypokinesia (reduced movement)
HUNTINGTON'S: striatal neurodegeneration → hyperkinesia (chorea)
```

---

## Hippocampus and Memory

### Structure

```
ENTORHINAL CORTEX ──→ DG (dentate gyrus) ──→ CA3 ──→ CA1 ──→ Subiculum
                        (mossy fibers)    (Schaffer)      └──→ EC

EC also connects directly to CA1 (temporoammonic pathway)
EC → CA3 also via perforant path

CA3: recurrent collaterals → autoassociative attractor network (pattern completion)
CA1: pattern separation output
DG: sparse coding → pattern separation input
```

### Memory Systems

```
DECLARATIVE (explicit, hippocampus-dependent):
  Episodic: "what happened, when, where" — personal experiences
  Semantic: facts and general knowledge (can consolidate to cortex)

NON-DECLARATIVE (implicit, hippocampus-independent):
  Procedural: motor skills, habits (basal ganglia)
  Priming: previous exposure speeds processing (neocortex)
  Conditioning: fear (amygdala), eyeblink (cerebellum)
  Perceptual learning

CONSOLIDATION:
  Initial encoding: hippocampus
  Slow consolidation: hippocampus ↔ neocortex dialogue during sleep (SWRs + spindles)
  Remote memories: stored in neocortex (hippocampus less needed over years)
  Patient H.M. (Molaison): bilateral hippocampectomy → severe anterograde amnesia,
  intact remote memories, intact procedural learning → defines episodic memory system
```

### Place Cells, Grid Cells, Head Direction

```
PLACE CELLS (O'Keefe 1971, Nobel 2014):
  Fire when animal in specific location (place field)
  ~300 place cells in rat CA1; together tile the environment
  Remapping: different environment → different place cell pattern

GRID CELLS (Moser & Moser 2005, Nobel 2014):
  Fire at multiple locations forming a hexagonal grid
  Grid spacing (scale) varies systematically along MEC dorsoventral axis
  → Provide metric system for space (path integration)

HEAD DIRECTION CELLS: fire when head points in specific compass direction
BORDER CELLS: fire near environmental boundaries
OBJECT VECTOR CELLS: fire relative to specific objects

COGNITIVE MAP HYPOTHESIS: hippocampus encodes spatial and relational maps;
extended to episodic memory and mental simulation of futures
```

---

## Prefrontal Cortex and Executive Function

```
PFC (prefrontal cortex) — anterior frontal lobe

DORSOLATERAL PFC (dlPFC):
  Working memory: active maintenance of information over seconds
  Persistent activity (attractor state): neurons keep firing after stimulus removed
  Delay-period activity in Fuster/Goldman-Rakic experiments
  Manipulation: mental rotation, rule application

ORBITOFRONTAL CORTEX (OFC):
  Value representation, reward expectation
  Credit assignment, reversal learning

ANTERIOR CINGULATE CORTEX (ACC):
  Conflict monitoring, error detection
  Anterior insula + ACC: interoception, pain, emotion regulation

WORKING MEMORY LIMIT: ~4 items (Cowan, 2001) — not 7±2 (Miller 1956 was chunks)
COGNITIVE CONTROL: suppression of prepotent (automatic) responses
  → DLPFC inhibits subcortical/posterior automaticity
```

---

## Decision Cheat Sheet

| System | Key structure | Key cell type | Core computation |
|--------|-------------|--------------|-----------------|
| Vision | V1, IT, MT | Simple/complex cells | Hierarchical feature extraction |
| Hearing | A1 (tonotopic) | Hair cells, AN fibers | Frequency decomposition + localization |
| Motor output | M1, spinal cord | Alpha motor neuron | Rate coding → force |
| Motor refinement | Cerebellum | Purkinje cell | Supervised error correction |
| Action selection | Basal ganglia | Striatal MSN | Actor-critic, Go/NoGo |
| Spatial memory | Hippocampus CA3 | Place cells | Pattern completion (attractor) |
| Spatial metric | MEC | Grid cells | Path integration, hexagonal code |
| Working memory | dlPFC | Pyramidal layer 3 | Attractor maintenance |
| Reward signal | VTA/SNc | Dopamine neuron | RPE = r + γV'(s') - V(s) |
