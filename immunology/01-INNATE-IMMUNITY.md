# Innate Immunity

## The Big Picture

```
INNATE IMMUNITY: THE ALWAYS-ON FIREWALL
=========================================

  DESIGN PRINCIPLES:
  ─ Fast: responds within minutes (no clonal expansion needed)
  ─ Broad: recognizes patterns shared by classes of pathogens
  ─ Non-specific: same response regardless of which Salmonella strain
  ─ Non-adaptive: does not improve with repeated exposure

  WHAT IT DETECTS:
  PAMPs: Pathogen-Associated Molecular Patterns
    ─ Molecules made by microbes but NOT by mammalian cells
    ─ LPS (lipopolysaccharide) from gram-negative bacteria
    ─ Peptidoglycan from gram-positive bacteria
    ─ Flagellin (bacterial flagella protein)
    ─ Double-stranded RNA (viral replication intermediate)
    ─ Unmethylated CpG DNA (bacterial/viral DNA pattern)
    ─ Zymosan (fungal cell wall component)

  DAMPs: Damage-Associated Molecular Patterns
    ─ Molecules released from DAMAGED SELF cells
    ─ HMGB1, IL-1α, S100 proteins (nuclear/cytoplasmic)
    ─ ATP released from dying cells
    ─ Mitochondrial DNA
    ─ Uric acid crystals (gout!)
    ─ Signal: "Something bad is happening even without pathogen"

  ┌──────────────────────────────────────────────────────────────┐
  │ PAMP: "I see something foreign" → antimicrobial response     │
  │ DAMP: "I see damage" → repair/inflammation response          │
  │                                                              │
  │ Together they define the "danger model" of immunity:         │
  │ Immune activation = foreign + dangerous (or damage alone)    │
  └──────────────────────────────────────────────────────────────┘
```

---

## Pattern Recognition Receptors (PRRs)

### Toll-Like Receptors (TLRs)

```
  TOLL-LIKE RECEPTORS: THE ORIGINAL FIREWALLS
  =============================================

  13 human TLRs. Each recognizes specific molecular patterns.
  Located on: cell surface (TLR1/2/4/5/6) or endosomes (TLR3/7/8/9)

  ┌───────────────────────────────────────────────────────────────┐
  │ TLR  LIGAND          PATHOGEN TYPE       LOCATION             │
  ├───────────────────────────────────────────────────────────────┤
  │ TLR1/2 Lipopeptides  Gram+ bacteria     Cell surface          │
  │ TLR2   Lipoteichoic  Gram+ bacteria     Cell surface          │
  │ TLR3   dsRNA         RNA viruses        Endosome              │
  │ TLR4   LPS           Gram- bacteria     Cell surface          │
  │ TLR5   Flagellin     Flagellated bact.  Cell surface          │
  │ TLR7   ssRNA         RNA viruses        Endosome              │
  │ TLR8   ssRNA         RNA viruses        Endosome              │
  │ TLR9   CpG DNA       Bacteria/DNA virus Endosome              │
  └───────────────────────────────────────────────────────────────┘

  TLR SIGNALING CASCADE:
  TLR detects PAMP
       │
       ▼ MyD88 adapter (most TLRs) or TRIF adapter (TLR3, TLR4)
       │
       ▼ IRAK kinases activated
       │
       ▼ TRAF6 ubiquitination
       │
       ├──► NF-κB activation → inflammatory cytokine genes
       │    (TNF, IL-6, IL-1β, IL-12, chemokines)
       │
       └──► IRF3/7 activation (TRIF pathway) → Type I IFN genes
            (IFN-α, IFN-β → antiviral state)

  LPS DETECTION (the classic example):
  LPS binds LBP (serum protein) → transfers to CD14 on macrophage
  → MD-2 binds LPS → TLR4:MD-2 complex activated
  → NF-κB → TNF, IL-6, IL-1β release → sepsis if overwhelming
```

### NLRs and Inflammasome

```
  NOD-LIKE RECEPTORS (NLRs): CYTOPLASMIC SENSORS
  =================================================

  NOD1, NOD2: Cytoplasmic sensors for bacterial peptidoglycan
  ─ NOD2 mutation → Crohn's disease (defective bacterial sensing)
  ─ NOD2 activates NF-κB → IL-12, TNF production

  INFLAMMASOME: The cytoplasmic kill switch
  ┌────────────────────────────────────────────────────────────┐
  │ NLRP3 inflammasome (most studied):                         │
  │                                                            │
  │ SIGNAL 1 (priming): LPS → NF-κB → NLRP3 + IL-1β mRNA       │
  │ SIGNAL 2 (activation): ATP, uric acid crystals,            │
  │   silica crystals, bacterial toxins, mitochondrial ROS     │
  │                                                            │
  │ NLRP3 + ASC + Caspase-1 → INFLAMMASOME complex             │
  │                                                            │
  │ Caspase-1 cleaves:                                         │
  │   Pro-IL-1β → mature IL-1β (potent inflammatory cytokine)  │
  │   Pro-IL-18 → mature IL-18 (IFN-γ inducer)                 │
  │   Gasdermin D → pore in membrane → PYROPTOSIS              │
  │   (inflammatory cell death — releases all contents)        │
  │                                                            │
  │ DISEASE CONNECTIONS:                                       │
  │ Gout: Uric acid crystals activate NLRP3 → IL-1β → pain     │
  │ Cryopyrinopathies: Gain-of-function NLRP3 mutations        │
  │ COVID-19: Hyperactive inflammasome → cytokine storm        │
  └────────────────────────────────────────────────────────────┘
```

### RLRs and cGAS-STING

```
  RIG-I-LIKE RECEPTORS (RLRs): CYTOPLASMIC RNA SENSORS
  ======================================================

  RIG-I: Detects 5'-triphosphate dsRNA (viral replication product)
         Signals via MAVS (mitochondrial antiviral signaling)
         → IRF3 phosphorylation → Type I IFN gene expression

  MDA5: Detects long dsRNA (>1 kb)
        Also signals via MAVS → Type I IFN
        Different virus specificity: picornaviruses (MDA5) vs.
        influenza/VSV (RIG-I)

  cGAS-STING: DNA SENSOR
  ┌───────────────────────────────────────────────────────────┐
  │ cGAS (cyclic GMP-AMP synthase):                           │
  │   Detects cytoplasmic double-stranded DNA                 │
  │   Activated by: viral DNA, bacterial DNA, self-DNA        │
  │   (micronuclei, mitochondrial DNA leak)                   │
  │                                                           │
  │ cGAS catalyzes: GTP + ATP → cGAMP (cyclic dinucleotide)   │
  │                                                           │
  │ cGAMP binds STING (ER-resident adapter)                   │
  │       │                                                   │
  │       ▼ TBK1 kinase                                       │
  │       │                                                   │
  │       ▼ IRF3 phosphorylation                              │
  │       │                                                   │
  │       ▼ Type I IFN gene expression → antiviral state      │
  │                                                           │
  │ THERAPEUTIC: STING agonists as cancer immunotherapy       │
  │ DISEASE: cGAS-STING activates on self-DNA in SLE, AGS     │
  └───────────────────────────────────────────────────────────┘
```

---

## Complement System

```
  COMPLEMENT: THE SERUM ATTACK SYSTEM
  =====================================

  ~30 serum proteins that form a cascade resulting in:
  1. Direct bacterial killing (Membrane Attack Complex, MAC)
  2. Opsonization (C3b coating → phagocytosis)
  3. Inflammation (C3a, C5a anaphylatoxins → mast cell activation)
  4. Immune complex clearance

  THREE ACTIVATION PATHWAYS:
  ┌──────────────────────────────────────────────────────────────────┐
  │                                                                  │
  │  CLASSICAL                 LECTIN                  ALTERNATIVE   │
  │  ─────────                 ──────                  ───────────   │
  │  Antibody (IgG/IgM)        MBL binds               Spontaneous   │
  │  binds antigen             mannose on              C3 hydrolysis │
  │  → C1q recognizes          pathogen surface        → low-level   │
  │  Fc regions                → MASP1/2 activated     activation    │
  │                                                                  │
  │  C1q:C1r:C1s complex       MBL:MASP2 complex       properdin     │
  │       │                         │                    stabilizes  │
  │       └─────────────────────────┴────────────────────┘           │
  │                                 │                                 │
  │                         C4 → C4a + C4b                           │
  │                         C2 → C2a + C2b                           │
  │                         C3 convertase: C4b2a                     │
  │                                 │                                 │
  │                           C3 → C3a + C3b                         │
  │                                 │                                 │
  │                    ┌────────────┴────────────┐                   │
  │                    │                         │                   │
  │              C3b OPSONIZES             C3b + C3b → C5 convertase │
  │              bacteria for              → C5 → C5a + C5b          │
  │              phagocytosis              → C5b678 + C9 → MAC       │
  │                                                                  │
  │  C3a, C5a = ANAPHYLATOXINS → Mast cell degranulation             │
  │  MAC (C5b-9) = punches hole in bacterial membrane → lysis        │
  └──────────────────────────────────────────────────────────────────┘

  COMPLEMENT DEFICIENCIES:
  C3 deficiency: Recurrent encapsulated bacterial infections
  MBL deficiency: Increased early childhood infections
  C5–9 deficiency: Susceptibility to Neisseria meningitidis
  Properdin deficiency (X-linked): Meningococcal disease
  C1 inhibitor deficiency: Hereditary angioedema (HAE) — swelling
```

---

## Innate Immune Cells

### Neutrophils

```
  NEUTROPHILS: THE FIRST RESPONDERS
  ====================================

  Most abundant leukocyte: ~60% of WBCs in blood
  Lifespan: 6–8 hours in blood; 1–4 days in tissue
  First to arrive at infection site (within 30–60 min)

  KILLING MECHANISMS:
  1. Phagocytosis: Engulf → phagosome → fuse with lysosome
     Lysosome contents: lysozyme, defensins, MPO (myeloperoxidase)
     MPO + H₂O₂ + Cl⁻ → HOCl (bleach) — kills bacteria

  2. Reactive oxygen species (ROS): NADPH oxidase
     O₂ + e⁻ → O₂•⁻ → H₂O₂ → •OH (hydroxyl radical)
     Chronic granulomatous disease (CGD): NADPH oxidase mutation
     → inability to kill catalase-positive bacteria

  3. NETs (Neutrophil Extracellular Traps):
     Neutrophil releases chromatin + antimicrobial proteins
     Physical web that traps bacteria
     Can also cause immunopathology (excess NETs in SLE, COVID)

  4. Degranulation: Release pre-formed mediators
     Primary granules: MPO, elastase, lysozyme
     Secondary granules: lactoferrin, collagenase
```

### Macrophages and Dendritic Cells

```
  MACROPHAGES: TISSUE PHAGOCYTES + ORCHESTRATORS
  ================================================

  ORIGIN: Monocytes migrate from blood → differentiate in tissue
  OR: Yolk-sac derived (liver Kupffer cells, brain microglia)
  Lifespan: Months to years in tissue

  POLARIZATION:
  ┌──────────────────────────────────────────────────────────┐
  │ M1 (classical activation):                               │
  │   Stimulated by: LPS, IFN-γ                              │
  │   Functions: Killing bacteria, pro-inflammatory          │
  │   Products: NO (nitric oxide), TNF, IL-6, IL-12          │
  │                                                          │
  │ M2 (alternative activation):                             │
  │   Stimulated by: IL-4, IL-13, IL-10                      │
  │   Functions: Wound healing, parasite killing             │
  │   Products: IL-10, TGF-β, arginase                       │
  │                                                          │
  │ (M1/M2 is oversimplified; real macrophages exist on      │
  │  a spectrum with many activation states)                 │
  └──────────────────────────────────────────────────────────┘

  TISSUE-RESIDENT MACROPHAGE NAMES:
  Liver: Kupffer cells
  Brain: Microglia
  Lung: Alveolar macrophages
  Skin: Langerhans cells (actually DC-related)
  Peritoneum: Peritoneal macrophages
  Bone: Osteoclasts

  DENDRITIC CELLS (DCs):
  ─ Professional antigen-presenting cells (APCs)
  ─ THE bridge between innate and adaptive immunity
  ─ Immature DCs: sample environment → sense PAMPs → mature
  ─ Mature DCs: upregulate MHC II + co-stimulatory molecules
    (CD80/B7-1, CD86/B7-2) → migrate to lymph nodes
  ─ Present antigen to naïve T cells → activate adaptive arm
```

### NK Cells

```
  NATURAL KILLER (NK) CELLS: INNATE KILLERS
  ==========================================

  CONCEPT: Detect missing-self + induced-self

  MISSING-SELF:
  Normal cells express MHC class I → NK cells leave them alone
  Infected cells or cancer cells DOWNREGULATE MHC I
  (to hide from CD8 T cells)
  → NK cells detect MHC I absence → KILL

  INDUCED-SELF:
  Stressed cells upregulate NKG2D ligands (MICA, MICB, RAE-1)
  → NK cells detect NKG2D ligands → KILL

  BALANCE: Activating vs. inhibitory receptors
  ┌──────────────────────────────────────────────────────────┐
  │ INHIBITORY: KIRs (Killer Immunoglobulin-like Receptors)  │
  │   Bind MHC I → "Cell is normal, don't kill"              │
  │                                                          │
  │ ACTIVATING: NKG2D, NCRs (NKp30, NKp44, NKp46)            │
  │   Bind stress ligands → "Kill this cell"                 │
  │                                                          │
  │ Kill happens when: Activating > Inhibitory               │
  └──────────────────────────────────────────────────────────┘

  KILLING MECHANISMS:
  1. Perforin + Granzyme B: Same as CD8 T cells
     Perforin pores → granzyme enters → caspase activation → apoptosis
  2. ADCC: Antibody-Dependent Cellular Cytotoxicity
     NK cells have FcγRIII (CD16) → bind antibody-coated targets → kill
  3. Death receptor: NK cells express FasL → target Fas → apoptosis
```

---

## Inflammation: The Acute Response

```
  ACUTE INFLAMMATION: COORDINATED VASCULAR RESPONSE
  ===================================================

  CARDINAL SIGNS: Rubor (redness), Calor (heat), Tumor (swelling),
                  Dolor (pain), Functio laesa (loss of function)

  VASCULAR CHANGES:
  ┌──────────────────────────────────────────────────────────────┐
  │ 1. Vasodilation: Histamine, prostaglandins → blood flow ↑    │
  │    → Redness + heat                                          │
  │                                                              │
  │ 2. Increased permeability: Histamine, bradykinin             │
  │    → Plasma proteins leak into tissue → edema (swelling)     │
  │    → Fibrin deposition → clot formation at site              │
  │                                                              │
  │ 3. Leukocyte extravasation (rolling → adhesion → diapedesis)│
  │    Chemokines (IL-8/CXCL8) → leukocyte rolling on selectins│
  │    → integrin activation → firm adhesion (ICAM-1:LFA-1)      │
  │    → diapedesis through vessel wall → chemokine gradient     │
  └──────────────────────────────────────────────────────────────┘

  PROSTAGLANDIN PATHWAY:
  Phospholipids → Arachidonic acid (via PLA₂)
  Arachidonic acid + COX-1/COX-2 → Prostaglandins + Thromboxane
  PGE₂: fever (hypothalamic) + pain sensitization + vasodilation

  NSAIDs (aspirin, ibuprofen): COX inhibitors → block PG synthesis
  Selective COX-2 inhibitors (celecoxib): less GI side effects

  SYSTEMIC ACUTE-PHASE RESPONSE:
  IL-6 + IL-1β → liver → acute-phase protein production
  ─ CRP (C-reactive protein): opsonin, complement activator
  ─ SAA (serum amyloid A)
  ─ Fibrinogen: clotting
  ─ Complement components: C3, factor B
  ─ Ferritin: sequesters iron from bacteria
  IL-1β + TNF → hypothalamus → fever (PGE₂)
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| First responder to bacterial infection | Neutrophils (30–60 min) |
| Pattern recognition receptor for LPS | TLR4 (cell surface) |
| Pattern recognition receptor for viral dsRNA | TLR3 (endosomal) + RIG-I (cytoplasmic) |
| What is a cytokine storm? | Excessive PRR activation → uncontrolled IL-6/TNF loop |
| How does complement kill bacteria? | MAC (C5b-9) punches membrane holes |
| What does C3b do? | Opsonizes bacteria → phagocytosis |
| How do NK cells spare normal cells? | KIR receptors detect MHC I (inhibitory) |
| What activates the inflammasome? | Signal 1 (LPS) + Signal 2 (ATP/crystals) |
| Anti-inflammatory drug target for gout? | NLRP3 inflammasome → IL-1β → Anakinra/Canakinumab |
| TLR7/8 in mRNA vaccine context | Detect vaccine mRNA → innate activation |

---

## Common Confusion Points

**PAMPs vs. DAMPs**: PAMPs are foreign patterns (from microbes). DAMPs are endogenous danger signals (from damaged self). Both activate innate immunity via PRRs, but through different sensors. Gout is a DAMP-driven disease — uric acid crystals are self-derived.

**Complement classical pathway does not require innate**: The classical pathway is activated by antibody-antigen complexes — it's the interface between adaptive (antibodies) and innate (complement). The alternative and lectin pathways are purely innate.

**Neutrophils don't present antigen**: Neutrophils kill rapidly and die. They are not antigen-presenting cells and don't activate adaptive immunity directly. Dendritic cells are the key link to adaptive immunity.

**Inflammasome two-signal requirement prevents accidental activation**: Signal 1 (NF-κB priming) alone doesn't cause caspase-1 activation. You need both priming AND the activation signal (crystal/ATP/etc). This is a safety mechanism to avoid autoactivation.

**NK cells and MHC I**: NK cells kill targets WITHOUT MHC I (missing-self). CD8 T cells kill targets presenting specific peptide ON MHC I (specific recognition). These are complementary strategies — viruses that downregulate MHC I to escape T cells are killed by NK cells instead.
