# 10-CELL-BIOLOGY — Cell Biology

> Organelles, membranes, transport, signal transduction, cytoskeleton,
> cell cycle, apoptosis. The eukaryotic cell as a highly integrated machine
> with ~20,000 protein species coordinating in ~10 µm.

---

## Prokaryote vs Eukaryote

```
Feature              Prokaryote                Eukaryote
──────────────────────────────────────────────────────────────────
Size                 0.1–10 µm                 10–100 µm
Nucleus              No (nucleoid region)       Yes (membrane-bound)
Genome               Circular, ~4 Mb (E.coli)  Linear chromosomes, ~3 Gb (human)
Membrane-bound       No                        Yes (ER, Golgi, mitochondria...)
  organelles
Ribosomes            70S (30S + 50S)           80S (40S + 60S); 70S in organelles
Cell wall            Peptidoglycan (bacteria)  None (animal); cellulose (plant); chitin (fungi)
Division             Binary fission             Mitosis/meiosis
Transcription +      Coupled                   Uncoupled (nuclear envelope separates)
  translation
Introns              Rare                      Abundant (~95% of genes)
Histone proteins     No (HU protein analog)    Yes (octamer)
Cytoskeleton         Tubulin-like (FtsZ, MreB) Actin, tubulin, intermediate filaments
```

---

## Organelle Map

```
EUKARYOTIC CELL:

  ┌─────────────────────────────────────────────────────────────┐
  │  NUCLEUS: DNA storage, transcription, pre-mRNA processing   │
  │    Nucleolus: rRNA synthesis (RNA Pol I), ribosome assembly  │
  │    Nuclear pores (~120 MDa): selective bidirectional transport│
  ├─────────────────────────────────────────────────────────────┤
  │  ENDOPLASMIC RETICULUM (ER):                                │
  │    Rough ER: ribosomes on surface → secretory/membrane proteins│
  │    Smooth ER: lipid synthesis, Ca²⁺ storage, drug metabolism │
  ├─────────────────────────────────────────────────────────────┤
  │  GOLGI APPARATUS: protein modification, sorting, secretion  │
  │    cis (receives from ER) → medial → trans (sorts to destinations)│
  │    Modifications: glycosylation, sulfation, phosphorylation  │
  │    Sorts to: lysosomes, plasma membrane, secretion          │
  ├─────────────────────────────────────────────────────────────┤
  │  MITOCHONDRIA: ATP production, apoptosis, Ca²⁺ homeostasis  │
  │    Outer membrane: VDAC (porin) — permeable to small molecules│
  │    Inner membrane: ETC, ATP synthase — impermeable (cristae) │
  │    Matrix: TCA cycle, β-oxidation, mtDNA, 70S ribosomes     │
  ├─────────────────────────────────────────────────────────────┤
  │  LYSOSOMES: degradation depot                               │
  │    pH ~4.5–5 (V-type H⁺-ATPase)                            │
  │    ~60 acid hydrolases (proteases, lipases, nucleases)      │
  │    Receives: endosomes, autophagosomes                      │
  ├─────────────────────────────────────────────────────────────┤
  │  PEROXISOMES: oxidative reactions                           │
  │    β-oxidation of very long chain fatty acids (VLCFAs)      │
  │    H₂O₂ generation + catalase-mediated destruction         │
  │    Bile acid synthesis, plasmalogen synthesis               │
  └─────────────────────────────────────────────────────────────┘
```

---

## Membrane Structure and Transport

### Fluid Mosaic Model

```
Lipid bilayer (see 06-BIOMOLECULES.md):
  ~5 nm thick, phospholipid + cholesterol + sphingolipid
  Lateral diffusion: fast (~µm²/s), flip-flop: slow (need flippase)
  Leaflet asymmetry: PS, PE inner; PC, SM outer (maintained by flippases)
  Lipid rafts: cholesterol + sphingomyelin microdomains, enriched in GPI-anchored proteins

Membrane proteins:
  Integral (transmembrane): span bilayer (α-helix or β-barrel)
  Peripheral: associate with surface (electrostatic, myristoylation, GPI anchor)
  Functions: channels, transporters, receptors, enzymes, structural
```

### Transport Mechanisms

```
PASSIVE (no energy, down gradient):
  Simple diffusion:      small nonpolar (O₂, CO₂, steroid hormones, N₂)
  Facilitated diffusion: polar/charged molecules through channel or transporter
    Channels: aquaporins (H₂O), ion channels (K⁺, Na⁺, Cl⁻, Ca²⁺)
    Transporters (carriers): GLUT (glucose), uniporters

ACTIVE (energy required, against gradient):
  Primary active:        directly couples ATP hydrolysis
    Na⁺/K⁺-ATPase:      3 Na⁺ out, 2 K⁺ in per ATP; maintains resting potential
    Ca²⁺-ATPase (SERCA): pumps Ca²⁺ into ER; Ca²⁺ release triggers muscle contraction
    H⁺-ATPase (V-type):  acidifies lysosomes, vacuoles
    ABC transporters:    ATP-binding cassette; drug efflux (MDR1/P-gp), CFTR (Cl⁻)

  Secondary active (cotransport): couples to Na⁺ gradient created by Na⁺/K⁺-ATPase
    Symport (same direction):  SGLT1 (Na⁺ + glucose); Na⁺/amino acid
    Antiport (opposite):       Na⁺/Ca²⁺ exchanger; Na⁺/H⁺ exchanger

VESICULAR TRANSPORT:
  Endocytosis: plasma membrane → early endosome → late endosome → lysosome
    Clathrin-mediated: receptor-ligand (LDL/LDL-R, transferrin, EGF)
    Caveolae: cholesterol-rich flask-shaped invaginations; signal transduction
    Macropinocytosis: large membrane ruffles; non-specific uptake
    Phagocytosis: large particles (bacteria) by macrophages, neutrophils
  Exocytosis: vesicle fusion with plasma membrane
    Constitutive: continuous (ECM proteins, growth factors)
    Regulated: triggered by signal (neurotransmitter release, insulin secretion)
```

---

## Vesicular Trafficking

```
ER → Golgi → destinations

COAT PROTEINS select cargo and curve membrane:
  COPII: ER → Golgi (anterograde)
         Sar1-GTP recruits Sec23/Sec24 (inner coat), then Sec13/Sec31 (outer)
  COPI:  Golgi → ER (retrograde); intra-Golgi (retrograde)
         ARF1-GTP recruits coatomer complex
  Clathrin: Golgi → lysosome; plasma membrane → endosome

SNARE proteins mediate fusion:
  v-SNARE (vesicle): synaptobrevin (VAMP)
  t-SNARE (target): syntaxin + SNAP-25
  Trans-SNARE complex (zipper): pulls membranes together → fusion
  NSF + αSNAP: disassemble cis-SNAREs after fusion (recycle)

TARGETING signals:
  KDEL (Lys-Asp-Glu-Leu): ER retrieval sequence on soluble proteins
  KKXX: ER retrieval on membrane proteins
  Mannose-6-phosphate (M6P): lysosomal targeting (added in Golgi, receptor in TGN)
  Nuclear localization signal (NLS): Lys/Arg-rich → importin α/β
  Mitochondrial targeting sequence (MTS): N-terminal amphipathic helix → TOM/TIM
```

---

## Signal Transduction

### GPCR Cascade

```
EXTRACELLULAR SIGNAL (hormone, neurotransmitter, odorant)
       ↓
GPCR (7-transmembrane receptor): conformational change
       ↓
G protein (α·GDP·βγ): α subunit exchanges GDP → GTP (activated)
       ↓
Effectors (depend on Gα subtype):
  Gαs:  ↑ adenylyl cyclase → ↑ cAMP → PKA (protein kinase A)
  Gαi:  ↓ adenylyl cyclase → ↓ cAMP
  Gαq:  ↑ PLCβ → IP₃ + DAG
          IP₃ → Ca²⁺ release from ER
          DAG + Ca²⁺ → PKC (protein kinase C)
  Gα12/13: → Rho GEF → Rho → cytoskeletal changes

Termination:
  Gαs GTPase activity → GDP → inactive (intrinsic timer ~30s–10min)
  GPCR phosphorylation (GRK) → β-arrestin binding → receptor internalization

Second messengers:
  cAMP: activates PKA → phosphorylates many substrates
  IP₃: opens IP₃R Ca²⁺ channels on ER
  DAG: activates PKC
  Ca²⁺: calmodulin (CaM) → CaM-kinases, calcineurin, myosin light chain kinase
```

<!-- @editor[bridge/P3]: Natural bridge to CS/software — signal transduction cascades are event-driven architectures with amplification, feedback, and timeout (GTPase timer). GPCR → second messenger → kinase cascade mirrors pub/sub with message amplification. The learner's software architecture background makes this connection natural. -->
### RTK / RAS / MAPK Cascade

```
Growth factor (EGF, PDGF, FGF, insulin) binds RTK
       ↓
Receptor dimerization → trans-autophosphorylation of cytoplasmic tyrosines
       ↓
Adaptor proteins (Grb2 via SH2 domain) recruit SOS (GEF)
       ↓
SOS activates RAS: RAS·GDP → RAS·GTP
       ↓
RAS·GTP activates RAF (MAP3K)
       ↓
RAF phosphorylates MEK (MAP2K)
       ↓
MEK phosphorylates ERK (MAPK) at Thr and Tyr
       ↓
ERK: phosphorylates transcription factors (Elk-1, Fos), cytoskeletal proteins,
     enters nucleus → immediate early genes (FOS, JUN, MYC) → proliferation

Termination:
  RAS has intrinsic GTPase (slow) → GAPs (RasGAP) accelerate
  Phosphatases (PP2A, DUSP) dephosphorylate ERK
  Receptor internalization + lysosomal degradation

RAS mutations: found in ~30% of all cancers (KRAS: pancreatic, colorectal, lung)
  KRAS G12D: prevents GAP-accelerated GTP hydrolysis → constitutively active
```

### PI3K / AKT / mTOR

```
RTK (or GPCR-Gβγ) → PI3K: phosphorylates PIP₂ → PIP₃
PTEN: phosphatase, reverses PI3K → tumor suppressor (most commonly mutated in cancer)

PIP₃ recruits PDK1 + AKT to membrane → PDK1 phosphorylates AKT → active
AKT targets:
  GSK3 (inhibit) → stabilize glycogen synthesis, β-catenin
  FOXO (inhibit) → suppress apoptosis genes
  TSC1/2 (inhibit) → activates mTORC1
  BAD (inhibit) → suppress apoptosis

mTORC1 (activated by AKT + amino acids + energy):
  → S6K, 4E-BP1 phosphorylation → ↑ protein synthesis, ↑ ribosome biogenesis
  → inhibits autophagy
  Rapamycin/rapalogs: inhibit mTOR (immunosuppressant, cancer therapy)
```

---

## Cytoskeleton

```
Filament type    Monomer        Diameter   Dynamics       Functions
──────────────────────────────────────────────────────────────────────
Actin (F-actin)  G-actin (42kD) 7 nm       Treadmilling   Cell shape, motility,
                                            (ARP2/3 branching) cytokinesis, adhesion
Microtubules     α/β-tubulin    25 nm      Dynamic         Mitotic spindle,
                 (heterodimer)             instability     intracellular transport,
                                            (GTP hydrolysis) cilia/flagella
Intermediate     Cell-type      10 nm      Stable          Mechanical stress,
filaments        specific                                  nuclear lamina (lamins),
  (vimentin,     (no NTP)                                  nerve axons (neurofilaments)
  keratin, lamin)

MOTOR PROTEINS:
  Myosin II: actin tracks, toward (+) end → muscle contraction, cytokinesis
  Kinesin:   microtubule tracks, toward (+) end (away from centrosome) → anterograde transport
  Dynein:    microtubule tracks, toward (−) end (toward centrosome) → retrograde transport, cilia

Centrosome: MTOC (microtubule organizing center); γ-TuRC nucleates microtubules
Cilia/flagella: 9+2 arrangement of microtubule doublets; dynein arm power stroke
```

---

## Cell Cycle

```
G1 ──→ S ──→ G2 ──→ M ──→ G1
(gap 1) (DNA synth) (gap 2) (mitosis)
               ↕
              G0 (quiescent)

CHECKPOINTS:
  G1/S checkpoint (Restriction point):
    RB phosphorylation by CDK4/6-CyclinD → releases E2F → S-phase genes
    p21/p27 (CKIs) inhibit CDK → pause
    p53/p21 axis: DNA damage → p53 activated → p21 → CDK inhibition → arrest

  G2/M checkpoint:
    CDK1-CyclinB (MPF, maturation promoting factor): active → mitosis entry
    ATM/ATR: DNA damage kinases → Chk1/Chk2 → CDC25 degradation → CDK1 inactive

  Spindle assembly checkpoint (SAC, in M):
    MCC (mitotic checkpoint complex): inhibits APC/C until all kinetochores attach
    Unattached kinetochore → Mad2/BubR1/Bub3 → inhibit CDC20-APC/C
    Once all attached → APC/C-CDC20 activates → Securin/Cyclin B degradation → anaphase

MITOSIS PHASES:
  Prophase:    chromatin condenses, mitotic spindle assembles, centrosomes separate
  Prometaphase: nuclear envelope breaks down (in animals); kinetochores capture MTs
  Metaphase:   chromosomes align at metaphase plate; SAC satisfied
  Anaphase:    Securin degraded → Separase cleaves cohesin → sister chromatids separate
               APC/C-CDC20 → CyclinB degradation → CDK1 inactivation
  Telophase:   nuclear envelopes reform; chromosomes decondense
  Cytokinesis: actin-myosin contractile ring constricts → two daughter cells
```

---

## Apoptosis

Programmed cell death: ~50–70 billion cells/day in adult human.
Morphology: cell shrinkage, chromatin condensation, membrane blebbing, apoptotic bodies.
Contrast with necrosis: uncontrolled, inflammatory.

```
INTRINSIC PATHWAY (mitochondrial):
  Stress signals: DNA damage, oxidative stress, ER stress, growth factor withdrawal
       ↓
  BH3-only proteins (BIM, PUMA, NOXA, BID): activate BAX/BAK
       ↓
  BCL-2/BCL-XL: anti-apoptotic, sequester BH3-only proteins (survival)
  BAX/BAK: pro-apoptotic, form pores in outer mitochondrial membrane (MOMP)
       ↓
  MOMP (mitochondrial outer membrane permeabilization):
    Cytochrome c released → apoptosome (Apaf-1 heptamer + cytochrome c + procaspase-9)
       ↓
  Caspase-9 (initiator) → cleaves + activates Caspase-3/7 (executioner)
       ↓
  Caspase-3/7: cleave 100s of substrates → cell dismantled

EXTRINSIC PATHWAY (death receptor):
  FasL / TNF-α / TRAIL bind Fas / TNFR / DR4/DR5
       ↓
  FADD recruitment → Caspase-8 activation → Caspase-3/7
  (or: Bid cleavage → tBid → MOMP → amplification via intrinsic)

CONVERGENCE: both pathways activate Caspase-3 (executioner)

BCL-2 family key members:
  Anti-apoptotic: BCL-2, BCL-XL, MCL-1 (inhibitors: venetoclax → BCL-2)
  Pro-apoptotic (effectors): BAX, BAK
  Pro-apoptotic (BH3-only): BIM, PUMA, NOXA, BID, BAD
```

---

## Decision Cheat Sheet

| Question | Concept | Answer |
|----------|---------|--------|
| How does a signal reach the nucleus from outside? | Signal cascade | GPCR/RTK → second messengers → kinase cascade → TF phosphorylation |
| Why does insulin lower blood glucose? | RTK/PI3K/AKT | GLUT4 translocation to plasma membrane in muscle/fat |
| What prevents premature anaphase? | SAC | MCC inhibits APC/C-CDC20 until all kinetochores bi-orient |
| Why do cancer cells avoid apoptosis? | BCL-2 overexpression | Sequesters BH3-only proteins; prevents MOMP |
| How does a vesicle know where to go? | SNARE pairing | Specific v-SNARE / t-SNARE combinations provide targeting specificity |
| What controls cell size checkpoints? | CDK-Cyclin levels | Cyclin accumulates → CDK active → checkpoint passed → next phase |
| How does the ER sort secretory proteins? | Signal sequence | N-terminal hydrophobic signal → SRP → translocon → ER lumen |
| Why is Ca²⁺ a second messenger? | Concentration gradient | Cytoplasmic [Ca²⁺] ~100 nM vs ER/extracellular ~µM–mM → 10,000× gradient |
| What does RAS do in cancer? | Constitutive GTP binding | Mutation prevents GTPase → always-on proliferation signal |

---

## Common Confusion Points

**Signal transduction amplification is massive but not instantaneous**
One ligand molecule → one GPCR → multiple Gα activations (receptor catalytic)
→ many adenylyl cyclase → many cAMP → many PKA (each with 2 catalytic subunits)
→ many substrate phosphorylations. Amplification: 10⁶-fold possible.
But each step takes time and has termination mechanisms → signals are transient pulses.

**Apoptosis and necrosis are not just "controlled vs uncontrolled death"**
Apoptosis: active process requiring ATP and caspase activity; phagocytes recognize
PS-flipped (outer leaflet) membranes → clean engulfment → no inflammation.
Necrosis: cell lysis → DAMPs (damage-associated molecular patterns) → inflammation.
Pyroptosis (caspase-1, gasdermin), necroptosis (RIP3/MLKL): programmed but inflammatory.
The field now distinguishes ~12 forms of regulated cell death.

**The restriction point and the G1/S checkpoint are the same thing**
Restriction point (Pardee, 1974): point in G1 after which cells commit to division
regardless of growth factor withdrawal. Molecular basis: RB hyperphosphorylation
releases E2F. This is the G1/S transition point. Same thing, different names from
different eras.

**Microtubule dynamic instability is a feature, not a bug**
Microtubules stochastically switch between growth (GTP-tubulin) and shrinkage
(GDP-tubulin) — "dynamic instability." This allows rapid remodeling (spindle assembly
in minutes) and is exploited by taxol (stabilizes MTs → arrest in mitosis) and
vinca alkaloids (destabilize → prevent spindle assembly) as anticancer drugs.

**GPCR signaling duration is tightly controlled**
Gα GTPase activity limits signal (intrinsic ~minutes). RGS proteins accelerate
GTP hydrolysis (seconds). GRK phosphorylation + β-arrestin binding: receptor
desensitization + internalization. Prolonged agonist → receptor downregulation.
Drug tolerance (opioids, β-agonists) partly explained by receptor desensitization.
