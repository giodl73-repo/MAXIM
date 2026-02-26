# Neural Development and Brain Formation

## The Big Picture

The nervous system is the most complex structure built by developmental biology. A single neural tube becomes the brain, spinal cord, and peripheral nervous system. Neural development involves the largest number of cell types, the most intricate wiring problem, and the longest developmental timeline (well into adulthood) of any organ system.

```
+──────────────────────────────────────────────────────────────────+
|              NEURAL DEVELOPMENT OVERVIEW                         |
|                                                                  |
|  NEURAL INDUCTION → NEURAL TUBE CLOSURE → REGIONALIZATION        |
|  Week 3              Week 3-4               Week 4-8+           |
|      ↓                    ↓                      ↓              |
|  Neural plate        Primary NT + hindbrain   Brain vesicles    |
|  forms               Secondary NT (caudal)    expand            |
|                       Defects → NTDs          Cerebral cortex   |
|                                               develops         |
|                                                                  |
|  NEUROGENESIS → MIGRATION → SYNAPTOGENESIS → PRUNING            |
|  Week 6+           Week 8-29     Week 20-birth  Birth-adulthood |
|  VZ/SVZ               Radial glia   Activity-       Experience  |
|  progenitors          guide         dependent        matters     |
+──────────────────────────────────────────────────────────────────+
```

---

## Neural Induction and Neural Plate Formation

```
NEURAL INDUCTION
─────────────────
  The organizer (Hensen's node) secretes BMP antagonists:
  Chordin, Noggin, Follistatin → block BMP signaling in dorsal ectoderm.
  Low BMP → "default neural state" → ectoderm adopts neural fate.

  SOX2 + SOX1: First neural plate markers; maintained throughout neurogenesis.
  Neural plate: thickened neuroepithelium (columnar pseudostratified).

NEURAL PLATE SHAPING
  CONVERGENT EXTENSION:
    Cells intercalate mediolaterally → plate narrows (A-P) and elongates.
    Wnt/PCP pathway (Module 03) drives this movement.
    Failure → wide, short neural plate → neural tube defects.

  BENDING OF NEURAL PLATE:
    Hinge points form at floor plate (median hinge point) and
    dorsolateral hinge points.
    Actomyosin contraction + cell shape changes → folds rise.
    Regulated by Shh (floor plate), BMP (lateral ectoderm drives closure).

NEURAL TUBE CLOSURE (Week 3-4)
  Starts in cervical region, zips both anteriorly and posteriorly.
  Closure sites:
    Multiple closure initiation sites (at least 5 in mouse, 3-4 in human).
    Anterior neuropore: closes Day 25 → anencephaly if fails.
    Posterior neuropore: closes Day 27 → spina bifida if fails.
  Caudal neural tube: secondary neurulation (condensation + cavitation, not folding).

NEURAL TUBE DEFECTS (NTDs)
  Anencephaly: Failure of anterior neuropore → no brain; lethal.
  Spina bifida aperta (myelomeningocele): Failure of posterior neuropore.
    Neural tissue + meninges protrude through vertebral defect.
    Hydrocephalus (Arnold-Chiari malformation) in 80-90%.
    Motor/sensory defects below level of lesion.
  Folic acid (vitamin B9): Required for neural tube closure.
    Mechanism: One-carbon transfer reactions (purine, thymidylate synthesis)
    → DNA synthesis for rapidly dividing neuroepithelium.
    Folate supplementation 0.4-4 mg/day BEFORE conception → 50-70% reduction in NTDs.
    This is why folate is added to grain products (US FDA mandate since 1998).
```

---

## Brain Regionalization

```
THREE PRIMARY BRAIN VESICLES (Week 4)
───────────────────────────────────────
  Prosencephalon (forebrain) → telencephalon + diencephalon
  Mesencephalon (midbrain)   → midbrain structures
  Rhombencephalon (hindbrain) → metencephalon (pons + cerebellum) + myelencephalon (medulla)

  5 SECONDARY BRAIN VESICLES (Week 5)
  Telencephalon → cerebral cortex, basal ganglia, hippocampus, amygdala
  Diencephalon → thalamus, hypothalamus, optic cup (retina)
  Mesencephalon → superior/inferior colliculi, substantia nigra, VTA
  Metencephalon → pons, cerebellum
  Myelencephalon → medulla oblongata

AP REGIONALIZATION SIGNALS
  Anterior → Posterior gradient: secreted factors from anterior neural ridge

  REGION      SIGNAL          TRANSCRIPTION FACTORS
  ──────────  ──────────────  ──────────────────────────────────────
  Forebrain   FGF8 from ANR   Foxg1, Nkx2.1, Pax6, Emx2
              + Wnt inhibitor
  Midbrain    FGF8 from IsO   En1/2, Otx2/Gbx2 boundary
  Hindbrain   Retinoic acid   HOX genes (r1-r8, Module 04)
  Spinal cord RA + Wnt        Cdx genes, Hox genes

ISTHMIC ORGANIZER (IsO)
  Junction between midbrain (Otx2+) and hindbrain (Gbx2+) = Isthmus.
  This boundary secretes FGF8 (into hindbrain → cerebellum) + Wnt1 (into midbrain).
  Crucial for cerebellum and colliculi formation.
  IsO deletion → cerebellum and midbrain structures absent.

DV PATTERNING OF SPINAL CORD
  Floor plate (ventral) → Shh gradient:
    V3: Nkx2.2 → motor neuron subtypes (interneurons)
    V2/V1: Dbx1/2 → interneurons
    V0: Dbx1 → excitatory interneurons
  Dorsal → BMP4/7 + Wnt:
    dI1: Atoh1 → deep dorsal horn
    dI4-6: Pax2 → inhibitory interneurons
    Roof plate: sensory relay neurons
```

---

## Neurogenesis: Making Neurons and Glia

```
NEURAL PROGENITOR TYPES
────────────────────────
  VENTRICULAR ZONE (VZ): Adjacent to ventricle
    Radial glia: apical progenitors; bipolar; soma at ventricular surface
    Functions: Progenitor cell + scaffold for migration

  SUBVENTRICULAR ZONE (SVZ): Secondary progenitor zone
    Intermediate progenitors (IPs): basal progenitors; non-apical
    Expanded SVZ in primates → more neurons → bigger cortex

CELL CYCLE AND NEUROGENESIS
  Early cortical development: Symmetric divisions → expand progenitor pool
  Later: Asymmetric division → one progenitor + one neuron (or IP)
  Asymmetry mechanism:
    Apical vs basal cell fate determinants (Numb, Notch, TRIM32)
    unequal segregation between daughter cells
    Daughter touching ventricle → progenitor fate
    Daughter moving away → neuron fate (or IP)

NEURONAL BIRTH ORDER
  "Inside-out" cortical layering:
    First-born neurons → deepest layers (layers 5, 6)
    Later-born neurons → superficial layers (layers 2, 3)
    Each wave must MIGRATE PAST all previously born neurons.
    Layer 6 TF: Tbr1
    Layer 5 TF: Ctip2 (Bcl11b)
    Layer 4 TF: Rorβ
    Layer 2/3 TF: Satb2, Brn2

GLIOGENESIS
  After peak neurogenesis: same progenitors switch to gliogenesis.
  Timing controlled by: ↑EGFR, ↑CNTF/LIF, JAK-STAT signaling.
  Oligodendrocyte progenitors (OPCs): from ventral subpallium, migrate dorsally.
  Astrocytes: from VZ/SVZ; notch → Hes5 → astrocyte fate.
  Timing: mouse: mostly postnatal; human: mostly 3rd trimester-early postnatal.
```

---

## Neuronal Migration

```
RADIAL MIGRATION (cortical neurons)
─────────────────────────────────────
  Neurons climb radial glial fibers from VZ/SVZ to cortical plate.
  LOCOMOTION MODE: Nucleus moves in saltatory steps (nucleokinesis).
    Leading process extends (actin/microtubule)
    Centrosome moves first
    Nucleus pulled forward (ACTG1, LIS1 dynein complex)
  Radial glia fiber = the track; neuron = the train.

  REELIN SIGNAL (stopping)
    Cajal-Retzius cells in marginal zone secrete Reelin.
    Reelin → DAB1 → stops migration in correct layer.
    Reeler mutant mouse: cortical layers INVERTED (new neurons stop below old ones)
    → "Scrambled" cortex.

TANGENTIAL MIGRATION (interneurons)
  Cortical interneurons originate in GANGLIONIC EMINENCES (GE) in subpallium.
  Lateral GE (LGE) → striatal interneurons + olfactory neurons
  Medial GE (MGE) → PV+ and SST+ cortical interneurons (most abundant)
  Caudal GE (CGE) → Reelin+, VIP+ interneurons

  Tangential migration: long-range, over many days, along multiple routes.
  Chemoattractants: NRG1/ErbB4, CXCL12/CXCR4.
  Chemorepellents: Slit/Robo, Ephrin/Eph.

MIGRATION DISORDERS
  Lissencephaly ("smooth brain"): absent gyri
    LIS1 (PAFAH1B1): component of dynein complex; haploinsufficiency → lissencephaly
    DCX (Doublecortin): X-linked; microtubule-binding; males → lissencephaly, females → band heterotopia
  Periventricular heterotopia: neurons fail to migrate, remain near ventricle
    FLNA (Filamin A): X-linked; females affected; mutations → heterotopia, epilepsy
  Polymicrogyria: too many small gyri; usually COL4A1, PIK3R2, GPR56 mutations
```

---

## Axon Guidance

```
AXON NAVIGATION TO TARGET
───────────────────────────
  Growth cone: motile tip of growing axon.
    Structure: central domain (microtubules) + peripheral (actin-rich filopodia)
    Function: Integrates attractive + repulsive signals → steers axon.

  GUIDANCE CUE TYPES
  ────────────────────
  ATTRACTIVE:  Filopodia extend toward attractive cue.
    Netrin-1/DCC: Midline crossing cue (commissural axons)
    GDNF/GFRα1: Motor axon → NMJ guidance
    BDNF/TrkB: Cortical axon → hippocampus
    Semaphorin/Plexin (some): Can be attractive

  REPULSIVE:   Filopodia retract; axon turns away.
    Ephrin/Eph: Topographic mapping (retina → superior colliculus)
    Slit/Robo: Midline repulsive (prevents re-crossing after first cross)
    Semaphorin3A/NP1: Olfactory axon repulsion
    Netrin-1/UNC5: Long-range repulsion

SPINAL CORD COMMISSURAL AXON MODEL
  Classic model for midline crossing (floor plate):

    Commissural axon:
    DORSAL → attracted by Netrin-1 from floor plate (via DCC receptor)
    CROSSING midline → floor plate
    CROSSED → Slit from floor plate now repels via Robo receptor
               (Robo was silenced during approach; now activated)
    POST-CROSSING → repelled; cannot re-cross → turns anteriorly

  RETINOTOPIC MAPPING (topographic projection)
  Retinal ganglion cells (temporal → EphA high, nasal → EphA low)
  → Project to superior colliculus
  SC: posterior → EphrinA high, anterior → EphrinA low
  High EphA retinal axon = repelled by high EphrinA = projects anteriorly in SC
  Creates point-to-point topographic map.
```

---

## Synaptogenesis and Synaptic Pruning

```
SYNAPTOGENESIS
───────────────
  Neurons reach approximate target → form synapses.
  Initial synapses: activity-independent (driven by molecular matching).
  Molecular recognition: Neuroligin (post) / Neurexin (pre) — "synaptic velcro"
  More specificity: LRRTMs, Cadherins, Teneurins, Slit/Robo at synapse

  TIMELINE (human cortex):
    Week 23: First synapses
    Week 34-birth: Rapid synapse formation
    Birth-2 years: Peak synaptic density
    Peak: ~15,000 synapses/neuron (much more than adult)

SYNAPTIC PRUNING (activity-dependent)
  Excess synapses eliminated by:
  (1) Complement-mediated: C1q tags "weak" synapses → microglia phagocytose via C3/CR3
  (2) "Use it or lose it": Synapses with low/correlated activity → pruned
      High-frequency firing synapses → strengthened (LTP-like mechanism)
  (3) BDNF/TrkB: Supports strong synapses; withdrawal from weak ones

  PRUNING TIMELINE
  Visual system: Primary visual cortex — pruning after critical period (Module below)
  Prefrontal cortex: Pruning continues into early adulthood (>25 years)
  This is why adolescent/young adult brain is susceptible to psychiatric illness
  (schizophrenia onset during peak prefrontal pruning)

  AUTISM SPECTRUM DISORDER
  Theories: Aberrant synaptic pruning, altered synapse maturation.
  SHANK3, NRXN1, NLGN3/4: synaptic scaffold and adhesion proteins → autism.
  Excess synapse density observed in some ASD post-mortem brains.
  Pruning as a potential mechanism: mTOR pathway mutations reduce autophagy → synapses over-retained.
```

---

## Neural Crest: The Fourth Germ Layer

```
NEURAL CREST CELLS
────────────────────
  Often called the "fourth germ layer" — has such broad fate and unique properties.
  Origin: Border between neural plate and surface ectoderm.
  Undergo EMT → delaminate from dorsal neural tube → MIGRATE throughout embryo.

  CRANIAL NEURAL CREST → craniofacial bones, cartilage, teeth, skull vault,
                          meninges, peripheral glia of cranial nerves.
  TRUNK NEURAL CREST → dorsal root ganglia, sympathetic ganglia,
                        adrenal medulla, melanocytes (all pigment cells).
  VAGAL/SACRAL CREST → enteric nervous system (ENS = "gut brain")

  CELL TYPES DERIVED FROM NEURAL CREST (partial list)
  ─────────────────────────────────────────────────────
  Neurons: DRG (pain/proprioception), sympathetic, parasympathetic ganglia
  Glia: Schwann cells (peripheral myelin), satellite glia
  Endocrine: Adrenal medulla chromaffin cells (adrenaline producers)
  Melanocytes: All skin/hair/iris pigment cells
  Craniofacial: Jaw, orbital bones, skull vault, middle ear ossicles
  Smooth muscle: Cardiac outflow tract, great vessel walls

NEUROCRISTOPATHIES
  Waardenburg syndrome: PAX3 or MITF mutations → pigmentation + hearing defects
  DiGeorge/22q11.2: TBX1 + neural crest → craniofacial + cardiovascular + immune
  Hirschsprung disease: GDNF/RET mutations → ENS fails to colonize colon → no peristalsis
                        Nerve cells absent from segment of colon → functional obstruction
                        Treatment: surgical resection of aganglionic colon segment
  CHARGE syndrome: CHD7 mutations → coloboma, heart, choanal atresia, retardation, GE, ears
  Melanoma: cancer of melanocytes; EMT → reactivation of neural crest migration program
```

---

## Decision Cheat Sheet

| Event | Timing | Key Signal | Defect If Fails |
|-------|--------|-----------|----------------|
| Neural induction | Week 3 | BMP inhibition | No neural plate |
| Neural tube closure | Week 3-4 | Folate/Wnt-PCP | Anencephaly, spina bifida |
| AP brain regionalization | Week 4-8 | FGF8 from organizers, RA, HOX | Absent brain regions |
| DV spinal cord patterning | Week 4-8 | Shh (ventral), BMP (dorsal) | Wrong motor/sensory subtypes |
| Cortical layering | Week 6-29 | Reelin (stopping signal) | Lissencephaly, heterotopia |
| Neural crest migration | Week 3-5 | Chemoattractants/repellents | Waardenburg, Hirschsprung, DiGeorge |
| Synaptogenesis | Week 23 - 2yr | Neurexin/neuroligin, activity | ASD-related changes |
| Synaptic pruning | Birth - adulthood | Complement, BDNF, activity | Schizophrenia, ASD |

---

## Common Confusion Points

**"The cortex forms inside-out — why doesn't the brain just build layers outside-in?"**
Because each new neuron uses the radial glia scaffold to climb out. The scaffold starts at the ventricle and reaches the outer surface. Each new neuron must pass through all existing layers to reach the leading edge. If they couldn't pass through (no locomotion mode), they'd be stuck below previous waves. This inside-out strategy is a direct consequence of the radial glia scaffold architecture.

**"Neural crest forms bone — but bone is mesoderm, right?"**
In the trunk and limbs, bone is from paraxial mesoderm (somites). In the face and skull vault, bone is from neural crest (ectoderm-derived). This is a significant embryological distinction: DiGeorge syndrome (neural crest) affects craniofacial bones; achondroplasia (FGFR3 in chondrocytes from mesoderm) affects long bones. The skeleton is heterogeneous in origin.

**"Synaptic pruning reduces synapse number — is that development going backward?"**
No — pruning increases specificity. The initial overproduction + activity-dependent elimination is analogous to competitive selection: many possible connections are offered, then only the "correctly wired" ones (based on correlated activity) are retained. This generates precise topographic maps and efficient circuits. It's more like sculpture than regression.
