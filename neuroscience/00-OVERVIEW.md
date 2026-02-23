# Neuroscience — Brain Architecture Overview

## The Big Picture

```
    NEUROSCIENCE LANDSCAPE
    ══════════════════════════════════════════════════════════

    LEVELS OF ANALYSIS
    ┌─────────────────────────────────────────────────────────┐
    │                    BEHAVIOR / COGNITION                  │
    │         (perception, memory, decision, language)         │
    ├─────────────────────────────────────────────────────────┤
    │                 CIRCUITS & SYSTEMS                       │
    │   (visual pathway, motor system, hippocampus, PFC)       │
    ├─────────────────────────────────────────────────────────┤
    │             SYNAPSES & LOCAL CIRCUITS                    │
    │     (EPSPs, LTP, inhibitory interneurons, columns)       │
    ├─────────────────────────────────────────────────────────┤
    │             SINGLE NEURONS (biophysics)                  │
    │    (Hodgkin-Huxley, cable theory, dendritic computation) │
    ├─────────────────────────────────────────────────────────┤
    │                 MOLECULES & GENES                        │
    │   (ion channels, receptors, second messengers, CRISPR)   │
    └─────────────────────────────────────────────────────────┘
    Each level has its own theories, methods, and explanatory power.
    Neuroscience is the science of bridging ALL these levels.
```

---

## Brain Anatomy Hierarchy

```
    CENTRAL NERVOUS SYSTEM
    │
    ├── SPINAL CORD
    │   ├── Dorsal horns (sensory input from periphery)
    │   ├── Ventral horns (motor output to muscles)
    │   └── Central pattern generators (CPGs): locomotion, breathing
    │
    └── BRAIN
        │
        ├── BRAINSTEM (evolutionarily oldest)
        │   ├── Medulla oblongata: breathing, heart rate, swallowing
        │   ├── Pons: sleep/wake, facial motor, relay to cerebellum
        │   └── Midbrain (mesencephalon): eye movement (SC, oculomotor),
        │         dopamine (VTA, SNc), auditory relay (IC)
        │
        ├── CEREBELLUM ("little brain")
        │   ├── ~50% of brain's neurons
        │   ├── Motor coordination, timing, error-based learning
        │   └── Purkinje cells: largest neurons in CNS
        │
        ├── DIENCEPHALON
        │   ├── Thalamus: sensory relay station (except olfaction)
        │   │             LGN (vision), MGN (auditory), VP (somatosensory)
        │   │             Pulvinar (attention), MD (PFC relay)
        │   └── Hypothalamus: homeostasis (T, hunger, thirst, sex)
        │                      circadian clock (SCN), pituitary control
        │
        └── TELENCEPHALON (cerebral hemispheres)
            ├── BASAL GANGLIA
            │   ├── Striatum: putamen (sensorimotor) + caudate (cognitive)
            │   ├── Globus pallidus (GP): interna (GPi) + externa (GPe)
            │   ├── Subthalamic nucleus (STN): indirect pathway hyperdirect
            │   └── Substantia nigra pars reticulata (SNr): output
            │
            ├── LIMBIC SYSTEM (emotion, memory, motivation)
            │   ├── Hippocampus: episodic memory, spatial navigation
            │   ├── Amygdala: fear, threat detection, emotional learning
            │   ├── Cingulate cortex (ACC, PCC): conflict, attention, DMN
            │   └── Entorhinal cortex: hippocampal gateway, grid cells
            │
            └── NEOCORTEX (6 layers, human: ~2500 cm² area)
                ├── Frontal lobe: motor cortex, PFC, Broca's area
                ├── Parietal lobe: somatosensory, spatial, attention
                ├── Temporal lobe: auditory, Wernicke's, face areas, hippocampus
                └── Occipital lobe: visual cortex V1-V5
```

---

## Cortical Lobes and Major Functions

```
    LEFT HEMISPHERE (dominant for language in ~95% right-handers):

    FRONTAL    │ PARIETAL
    ───────────┼───────────
    Primary motor (precentral gyrus) │ Primary somatosensory (postcentral)
    Premotor / SMA                   │ Posterior parietal (spatial attention)
    Broca's area (44,45: speech prod)│ Angular gyrus (reading, calculation)
    DLPFC (working memory, executive)│ Supramarginal gyrus (phonological loop)
    OFC (reward, value)              │
    VMPFC (emotion, default mode)    │

    ───────────┼───────────
    TEMPORAL   │ OCCIPITAL
    Primary auditory (Heschl's)     │ V1 (primary visual)
    Superior temporal (Wernicke's,46)│ V2, V3, V4 (color, shape)
    Inferior temporal (object recog) │ V5/MT (motion)
    Fusiform face area (FFA)         │ Calcarine fissure
    Parahippocampal place area (PPA) │
    Hippocampus (deep)               │

    INSULA (buried in lateral sulcus):
    Anterior: interoception, pain, disgust, taste
    Posterior: somatosensory, vestibular

    CINGULATE (medial surface):
    ACC (32,24): conflict detection, error signaling
    PCC (23,31): default mode network, mind-wandering
    Retrosplenial: spatial context, memory retrieval
```

---

## Neurotransmitter Systems

```
    ┌──────────────────────────────────────────────────────────────────┐
    │  NEUROTRANSMITTER REFERENCE                                      │
    │                                                                  │
    │  Glutamate — EXCITATORY (main fast excitatory)                  │
    │  Source: widely distributed cortical neurons                    │
    │  Receptors:                                                      │
    │    AMPA: fast (2-4ms), Na⁺/K⁺ permeable, not Mg-blocked        │
    │    NMDA: slow (50-500ms), Ca²⁺ permeable, Mg²⁺ block at rest   │
    │    → NMDA requires BOTH presynaptic glutamate release AND       │
    │      postsynaptic depolarization to remove Mg²⁺ block           │
    │    → NMDA = coincidence detector = Hebb's rule in hardware     │
    │    Kainate: modulatory                                           │
    │    mGluR: metabotropic (slow, G-protein coupled)                │
    │                                                                  │
    │  GABA — INHIBITORY (main fast inhibitory)                       │
    │  Source: local interneurons (~20-30% of neurons in cortex)      │
    │  Receptors:                                                      │
    │    GABA_A: ionotropic, Cl⁻ channel → hyperpolarization          │
    │            benzodiazepines (Valium) potentiate → anxiolytic     │
    │            barbiturates, alcohol also act here                  │
    │    GABA_B: metabotropic, K⁺ current → slow IPSP                │
    │                                                                  │
    │  Dopamine (DA) — NEUROMODULATOR (reward, motor, salience)      │
    │  Source: VTA → limbic, PFC; SNc → striatum (nigrostriatal)     │
    │  Receptors: D1 (cAMP↑, Gs), D2 (cAMP↓, Gi) — see basal ganglia│
    │  Parkinson's: SNc dopamine neuron death → striatal DA deficit   │
    │  Schizophrenia: DA hyperactivity in mesolimbic pathway          │
    │  Reward prediction error (RPE): Schultz 1997                    │
    │                                                                  │
    │  Serotonin (5-HT) — NEUROMODULATOR (mood, sleep, GI)           │
    │  Source: raphe nuclei → widespread (entire brain + enteric NS)  │
    │  5-HT1A, 5-HT2A, 5-HT3 (ionotropic), 5-HT4-7 (metabotropic)  │
    │  SSRIs (Prozac) block serotonin reuptake → antidepressant       │
    │  Psilocybin / LSD: 5-HT2A agonists                             │
    │                                                                  │
    │  Acetylcholine (ACh) — MEMORY, ATTENTION, NMJ                  │
    │  Source: basal forebrain (BF) → cortex + hippocampus (memory)   │
    │          brainstem nuclei → thalamus (arousal)                  │
    │  Receptors: nicotinic (ionotropic), muscarinic (metabotropic)   │
    │  Alzheimer's: BF cholinergic degeneration → memory failure      │
    │  NMJ: ACh → nicotinic → end-plate potential → muscle AP        │
    │                                                                  │
    │  Norepinephrine (NE) — AROUSAL, ATTENTION, STRESS              │
    │  Source: locus coeruleus (LC) → entire brain                   │
    │  α1, α2, β1, β2 receptors                                       │
    │  LC firing rate correlates with pupil dilation (arousal index)  │
    └──────────────────────────────────────────────────────────────────┘
```

---

## Glial Cells

Not just "support cells" — active participants in brain function.

```
    ASTROCYTES (~50% of brain cells by volume):
    • Ensheath synapses (tripartite synapse: pre + post + astrocyte)
    • Recycle glutamate: glutamate → glutamine (astrocyte) → back to neuron
    • Maintain K⁺ homeostasis (spatial buffering)
    • Blood-brain barrier (BBB) maintenance via end-feet on capillaries
    • Calcium waves: gliotransmission, modulate synaptic strength
    • Glycogen storage (fuel for neurons during high activity)

    OLIGODENDROCYTES:
    • Myelinate central nervous system axons (PNS: Schwann cells)
    • One oligodendrocyte myelinates ~50 axon segments
    • Myelin = insulating lipid membrane: speeds conduction, saltatory propagation
    • Multiple sclerosis: autoimmune demyelination → slowed/blocked conduction

    MICROGLIA:
    • Brain-resident immune cells (derived from bone marrow precursors)
    • "Resting" state: surveying, extending/retracting processes
    • Activated: phagocytosis of debris, dead cells, synaptic pruning
    • Synaptic pruning: microglia eliminate excess synapses during development
    • Complement-tagged synapses: C3, C1q → microglial engulfment
    • Neuroinflammation in Alzheimer's: microglia fail to clear amyloid properly
```

---

## Scale: Brain by the Numbers

```
    ┌─────────────────────────────────────────────────────────────┐
    │  Human Brain Scale                                          │
    │                                                             │
    │  Volume:         1350 cm³ (1.35 L)                         │
    │  Mass:           1400 g (1.4 kg)                           │
    │  Power:          20 W (2% body, 20% oxygen consumption)    │
    │                                                             │
    │  Neurons:        86 × 10⁹ (86 billion)                    │
    │  Cortex neurons: 16 × 10⁹ (70% glutamatergic)             │
    │  Cerebellum:     69 × 10⁹ (mostly granule cells)          │
    │  Glia:           85 × 10⁹ (roughly 1:1 ratio with neurons) │
    │                                                             │
    │  Synapses:       10¹⁴ (100 trillion!) per brain            │
    │  Per neuron avg: ~7,000 synaptic inputs                    │
    │  Cortical neuron: up to 100,000 synapses                   │
    │                                                             │
    │  Firing rates:   0.1-100 Hz (typical cortical: 1-10 Hz)    │
    │  Typical spike:  1-2 ms duration, ~100 mV amplitude        │
    │  Resting Vm:     -70 mV                                    │
    │  Action potential threshold: -55 mV                        │
    │  Refractory period: 1-2 ms (absolute), 5-10 ms (relative)  │
    │                                                             │
    │  Conduction velocity: 0.5-80 m/s (myelinated: faster)     │
    │  Cortex thickness: 2-4 mm                                  │
    │  Cortical surface area: 2500 cm² (unfolded, A4 paper size) │
    └─────────────────────────────────────────────────────────────┘
```

---

## Measurement Methods

```
    ┌────────────────────────────────────────────────────────────────────┐
    │  NEURAL RECORDING AND IMAGING METHODS                             │
    │                                                                    │
    │  Method        │ What measured   │ Resolution      │ Invasive?   │
    │  ─────────────────────────────────────────────────────────────    │
    │  Patch clamp   │ Single channel  │ pA, 1 ms        │ Yes (cell)  │
    │  (whole cell)  │ currents, Vm    │                 │             │
    │  ──────────────────────────────────────────────────────────────   │
    │  Sharp electrode│ Vm intracellular│ mV, 1 ms        │ Yes         │
    │  ──────────────────────────────────────────────────────────────   │
    │  Single-unit   │ AP timing       │ ms, 1 neuron     │ Yes (probe) │
    │  recording     │ (spike times)   │                 │             │
    │  ──────────────────────────────────────────────────────────────   │
    │  Multielectrode│ Population      │ ms, 10-1000      │ Yes (array) │
    │  array (MEA)   │ activity        │ neurons          │             │
    │  Neuropixels   │ Local spikes    │ ms, ~1000 units  │ Yes (probe) │
    │  ──────────────────────────────────────────────────────────────   │
    │  Field poten.  │ Local pop.      │ LFP: 1-500 Hz   │ Yes (wire)  │
    │  (LFP)         │ dendritic summ. │ γ,θ,δ,SWR bands  │             │
    │  ──────────────────────────────────────────────────────────────   │
    │  EEG           │ Cortical surface│ 10ms, cm²        │ No (scalp)  │
    │                │ field poten.    │ (low spatial res)│             │
    │  MEG           │ Magnetic field  │ 1ms, ~5mm        │ No          │
    │                │ of neural curr. │                 │             │
    │  ──────────────────────────────────────────────────────────────   │
    │  fMRI (BOLD)   │ Blood oxygen    │ 1s, ~2-3mm       │ No          │
    │                │ level dep.      │ (indirect)       │             │
    │  PET           │ Glucose/dopamine│ minutes, cm      │ No (tracer) │
    │  ──────────────────────────────────────────────────────────────   │
    │  Calcium       │ Neural activity │ 30-100 ms, μm    │ Yes (virus) │
    │  imaging       │ via Ca²⁺ proxy  │                 │             │
    │  ──────────────────────────────────────────────────────────────   │
    │  Optogenetics  │ Control (causal)│ 1ms on, ms off   │ Yes (virus) │
    │  (ChR2, halorh)│ specific cells  │                 │             │
    └────────────────────────────────────────────────────────────────────┘
```

---

## Evolutionary Perspective

```
    TRIUNE BRAIN MODEL (MacLean) — oversimplified but useful heuristic:

    Fish → Brainstem only
    Basic survival: breathing, heart rate, reflexes, basic hunger/fear

    Reptile → + Basal ganglia
    Action selection, habitual behavior, territorial behavior

    Early mammals → + Limbic system (hippocampus, amygdala, cingulate)
    Episodic memory, social bonding, emotional learning

    Primates → + Large prefrontal cortex
    Abstract reasoning, language, planning, theory of mind

    ─────────────────────────────────────────────────────────────
    BRAIN VOLUMES (fraction of total):
    Species     │ Neocortex %  │ PFC %  │ Intelligence proxy
    ────────────┼──────────────┼────────┼──────────────────
    Rat         │ 22%          │ 3.5%   │ Maze, social
    Cat         │ 30%          │ 3.5%   │ Flexible behavior
    Macaque     │ 60%          │ 11.5%  │ Tool use (limited)
    Chimpanzee  │ 72%          │ 17%    │ Social learning, symbols
    Human       │ 76%          │ 29%    │ Language, abstract thought

    Key human specialization: absolute PFC size AND connectivity
    (not just relative size — human brain has 1000× more cortical neurons than mouse)
    Cortical folding (gyrification) to pack more surface in fixed skull volume
    Human: gyrification index ~2.5 (monkey ~1.7, rat ~1.0 = smooth)
```

---

## Bridge to Learner's Prior Knowledge

### Statistical Mechanics Bridge
Neural dynamics = many-body system:
- N = 86×10⁹ neurons, each a binary (firing/not) or rate variable
- Mean field theory of neural populations (Wilson-Cowan equations)
- Phase transitions in neural activity: asleep ↔ awake, seizure ↔ normal
- Critical branching ratio σ = 1 (avalanche statistics, power law in spontaneous activity)

### Quantum / EM Bridge
- Hodgkin-Huxley = nonlinear RLC circuit (see 01-NEURONS-SIGNALS.md)
- Resting potential = Nernst/Goldman equation from electrochemistry
- Neuronal noise: thermal Johnson noise, channel shot noise (k_B T / C_m ~ 1 mV at 300K)
- Optogenetics uses light → channelrhodopsin ion channel → precisely controlled current

### Distributed Systems Bridge
- Brain = massively parallel, fault-tolerant, self-organizing distributed system
- Graceful degradation: neurons die every day, behavior persists (redundancy)
- No central clock, no global coordinator: local rules → global behavior
- Neural oscillations (theta, gamma) = distributed synchronization protocol
- Winner-take-all competition = consensus among uncertain processors

### AI/ML Bridge
See 04-AI-BRIDGE.md for systematic comparison.
Short version: transformers are loosely inspired by cortical hierarchy +
attention; RLHF reward models implement Bellman equations like dopamine RPE;
RAG ≈ hippocampal indexing; but neuroscience has mechanisms AI doesn't yet.

---

## Decision Cheat Sheet — What Method for What Question?

| Question                                  | Best Method(s)                      |
|-------------------------------------------|-------------------------------------|
| Spike timing of identified neuron in vivo | Single-unit recording, Neuropixels  |
| Whole-brain activation during task        | fMRI (BOLD), MEG                    |
| Causally test if area X is needed         | TMS, DREADD, optogenetics, lesion   |
| Track single neuron during learning       | Chronic recording (weeks/months)    |
| Map synaptic connectivity                 | EM connectomics (Janelia FlyWire)   |
| Oscillation frequency, EEG rhythm         | EEG, LFP                           |
| Ion channel kinetics                      | Patch clamp (whole-cell, outside-out)|
| Population activity (100s of neurons)     | Two-photon calcium imaging          |
| Neuromodulator release                    | Voltammetry (FSCV), RuBisCO        |
| Gene expression in single neurons         | scRNA-seq (post-mortem or SMART-seq)|

---

## Common Confusion Points

**Neurotransmitters vs neuromodulators**: Fast neurotransmitters (glutamate, GABA) act at
specific synapses within milliseconds via ionotropic receptors, changing the postsynaptic
neuron's membrane potential directly. Neuromodulators (dopamine, serotonin, ACh, NE)
typically act diffusely (volume transmission), use G-protein coupled receptors, and modulate
the excitability or plasticity of large neuronal populations — they "tune the gain" rather
than fire single synaptic volleys.

**Action potentials are all-or-nothing, but rate codes and timing codes coexist**:
Individual spikes are stereotyped (~100 mV, 1-2 ms). But information is encoded in
WHEN and HOW OFTEN neurons fire. Rate code = firing rate carries information (primary motor cortex:
firing rate ~ force). Temporal code = precise spike timing carries information
(auditory brainstem: submillisecond interaural timing differences). Both exist in the brain.

**fMRI measures BOLD, not neural spikes**: The BOLD (blood-oxygen-level-dependent) signal
measures changes in deoxyhemoglobin via T2* magnetic resonance. It's an indirect proxy for
neural activity via neurovascular coupling. Latency: ~2-6 s. Spatial resolution: 2-3 mm standard.
It correlates with local field potentials (dendritic currents) more than spike rates. fMRI
is the workhorse of human cognitive neuroscience but has severe temporal limitations.
