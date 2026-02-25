# B Cells and Antibodies

## The Big Picture

```
B CELLS AND ANTIBODIES: HUMORAL IMMUNITY
==========================================

  THE COMBINATORIAL MATH OF ANTIBODY DIVERSITY
  =============================================

  VDJ RECOMBINATION generates the antibody repertoire:

  HEAVY CHAIN V-D-J SEGMENTS (human):
  V segments:    ~40
  D segments:    ~25
  J segments:     6
  Combinatorial: 40 × 25 × 6 = 6,000 VDJ combinations

  LIGHT CHAIN V-J SEGMENTS:
  κ chain: ~40 V × 5 J = 200
  λ chain: ~30 V × 4 J = 120

  ADDITIONAL DIVERSITY:
  Junctional diversity (N-nucleotide additions at junctions): ~10⁸
  Combinatorial joining of heavy + light chain: × 6,000 × ~320

  TOTAL THEORETICAL DIVERSITY: ~10¹⁸ unique antibodies
  (More than one for every human who has ever lived × 10⁸)

  Then somatic hypermutation in germinal centers adds further
  diversity to selected clones — effectively a local search
  on top of the pre-existing random sampling.

  ┌──────────────────────────────────────────────────────────────┐
  │ ANTIBODY STRUCTURE                                            │
  │                                                               │
  │              ┌─────────────────────────┐                     │
  │              │   VH │     │ VL          │   Variable (Fab)    │
  │   Antigen ──►│   VH │     │ VL          │   domains           │
  │   binding    │   CH1│     │ CL          │   (antigen contact) │
  │              └──────┤     ├────────────┘                     │
  │                     │Hinge│                                   │
  │              ┌──────┤     ├────────────┐                     │
  │              │   CH2│     │ CH2         │   Constant (Fc)     │
  │              │   CH2│     │ CH2         │   regions           │
  │              │   CH3│     │ CH3         │   (effector func.)  │
  │              └─────────────────────────┘                     │
  │                                                               │
  │  Two heavy chains (VH-CH1-CH2-CH3) + Two light chains (VL-CL)│
  │  Disulfide bonds link chains                                  │
  │  Y-shaped: Two Fab arms + One Fc base                        │
  └──────────────────────────────────────────────────────────────┘
```

---

## VDJ Recombination Mechanism

```
  VDJ RECOMBINATION: HOW THE RECEPTOR GENE IS BUILT
  ===================================================

  CONCEPT: Modular gene assembly from pre-existing V, D, J segments
           at the DNA level. Each B cell assembles its own unique receptor.

  THE SEGMENTS IN GERMLINE DNA:
  Chromosome 14 (heavy chain locus):
  [V1][V2]...[V40] ─── [D1]...[D25] ─── [J1]...[J6] ─── [C]

  RECOMBINATION SIGNAL SEQUENCES (RSS):
  12-RSS and 23-RSS flank each segment
  12-23 rule: Only 12-RSS can pair with 23-RSS for joining
  This enforces V-D, D-J joining order (not V-V or D-D)

  STEP 1: D-J JOINING (heavy chain)
  RAG1/RAG2 complex recognizes RSS → hairpin cleavage
  Artemis + DNA-PKcs: hairpin opening
  TdT (terminal deoxynucleotidyl transferase): adds random N-nucleotides
  Ligation → D-J joint with N-nucleotides (JUNCTIONAL DIVERSITY)

  STEP 2: V-(D-J) JOINING (heavy chain)
  V segment selected → joins to D-J joint
  Another round of N-nucleotide addition
  If no productive rearrangement → other allele rearranges

  STEP 3: LIGHT CHAIN (κ then λ if κ fails)
  V-J joining (no D segment for light chain)
  N-nucleotide addition at V-J junction
  Productive rearrangement → κ or λ light chain expressed

  ALLELIC EXCLUSION:
  Once productive rearrangement made → RAG shut down
  Each B cell expresses only ONE heavy chain allele
  (and predominantly one light chain allele)
  → Each B cell has ONE specificity

  CDR3: The most diverse region
  The V-D-J junction encodes CDR3 (Complementarity Determining Region 3)
  CDR3 is the primary antigen contact loop
  3 CDRs per chain × 2 chains = 6 CDR loops per antibody contact surface
```

---

## Antibody Classes (Isotypes)

```
  IMMUNOGLOBULIN ISOTYPES
  ========================

  All B cells start with IgM, then undergo class switching.
  Isotype = which constant region (CH2-CH3) is used.
  AID (same enzyme as somatic hypermutation) mediates class switch.

  ┌──────────────────────────────────────────────────────────────────┐
  │  IgM                                                              │
  │  ─────                                                           │
  │  First antibody produced in primary response                     │
  │  Pentameric: 5 Y-shapes joined → 10 antigen-binding arms        │
  │  Excellent at complement activation (classical pathway)          │
  │  On B cell surface as monomer (BCR)                             │
  │  Half-life: ~10 days                                             │
  ├──────────────────────────────────────────────────────────────────┤
  │  IgG (4 subclasses: IgG1–4)                                     │
  │  ───────────────────────────                                     │
  │  Most abundant in serum                                          │
  │  Only antibody that crosses the placenta (FcRn transporter)     │
  │  Neonatal protection until ~6 months from maternal IgG          │
  │  Opsonization: IgG1/3 → FcγR on macrophages → phagocytosis     │
  │  ADCC: NK cells (FcγRIII/CD16) + IgG → kill coated target      │
  │  Half-life: ~21 days (FcRn recycling)                           │
  │  IgG4: No complement, no ADCC → used therapeutically (no effec) │
  ├──────────────────────────────────────────────────────────────────┤
  │  IgA (dimeric in secretions)                                    │
  │  ─────────────────────────                                       │
  │  Dominant isotype at mucosal surfaces: gut, lung, breast milk   │
  │  Secretory IgA (sIgA): dimer + J chain + secretory component    │
  │  Neutralizes pathogens before they cross epithelium             │
  │  Most abundant antibody in the body (total mass, gut lumen)     │
  │  Half-life: ~5–6 days                                           │
  ├──────────────────────────────────────────────────────────────────┤
  │  IgE                                                             │
  │  ────                                                            │
  │  Lowest serum concentration of any isotype                      │
  │  Binds high-affinity FcεRI on mast cells and basophils         │
  │  Cross-linked by allergen → degranulation → allergy/anaphylaxis │
  │  Evolved for: Helminth parasite killing                         │
  │  Half-life: 2.5 days (but can persist bound to mast cells)     │
  ├──────────────────────────────────────────────────────────────────┤
  │  IgD                                                             │
  │  ────                                                            │
  │  Low serum levels; co-expressed with IgM on naïve B cells      │
  │  Function poorly understood; some role in upper respiratory     │
  └──────────────────────────────────────────────────────────────────┘
```

---

## BCR Signaling and B Cell Activation

```
  BCR SIGNALING CASCADE
  ======================

  MEMBRANE-BOUND ANTIBODY (BCR):
  IgM or IgD monomer on surface
  Non-covalently associated with: Igα (CD79a) + Igβ (CD79b)
  Igα/Igβ have ITAMs (Immunoreceptor Tyrosine-based Activation Motifs)

  ACTIVATION:
  Antigen cross-links multiple BCRs
       │
       ▼ BCR aggregation → Lyn kinase phosphorylates ITAMs
       │
       ▼ Syk kinase recruited to phospho-ITAMs
       │
       ▼ BLNK scaffold protein activated
       │
       ├──► PLCγ2 → IP3 + DAG
       │           │      └──► PKCβ → NF-κB
       │           └──► Ca²⁺ → calcineurin → NFAT
       │
       └──► PI3K → Akt → survival, metabolic reprogramming
       │
       ▼ B cell activation, proliferation, upregulate MHC II

  CD21 CO-RECEPTOR COMPLEX (amplifies BCR signal):
  Complement-coated antigen: C3d tag on antigen
  CD21 (CR2) recognizes C3d → co-ligates BCR
  CD21:CD19:CD81 complex → 1,000-1,000x signal amplification
  → Lower antigen dose required for B cell activation

  T-DEPENDENT vs. T-INDEPENDENT ACTIVATION:
  ┌────────────────────────────────────────────────────────────┐
  │ T-DEPENDENT (most protein antigens):                       │
  │   Requires CD4 Tfh cells for full germinal center reaction │
  │   CD40 (B cell) : CD40L (T cell) → survival + GC entry   │
  │   Cytokines (IL-21, IL-4, IL-10) → isotype switching     │
  │   Result: High-affinity IgG, IgA, IgE + memory B cells   │
  │                                                             │
  │ T-INDEPENDENT (polysaccharides, LPS):                      │
  │   Repeating epitopes cross-link BCR directly               │
  │   TLR signals provide additional stimulus                  │
  │   Result: Mainly IgM; limited class switching; no memory  │
  │   Problem: Encapsulated bacteria have polysaccharide       │
  │   capsules → limited protection without conjugate vaccine  │
  └────────────────────────────────────────────────────────────┘
```

---

## Antibody Functions

```
  ANTIBODY EFFECTOR MECHANISMS
  ==============================

  NEUTRALIZATION:
  ─ Antibody binds to virus/toxin → blocks binding to host receptor
  ─ Physical blockade, not cell-dependent
  ─ Example: Anti-SARS-CoV-2 neutralizing Abs block spike:ACE2 interaction
  ─ Potency: IC50 = concentration blocking 50% infection in cell assay
  ─ Broadly neutralizing antibodies (bnAbs): bind conserved epitopes

  OPSONIZATION:
  ─ IgG coats pathogen → FcγR on macrophages/neutrophils recognize Fc
  ─ FcγRI (CD64): High affinity, monomeric IgG → macrophage activation
  ─ FcγRIII (CD16): Lower affinity; NK cells (ADCC) + macrophages
  ─ FcγRIIB: Inhibitory → feedback suppression of B cell activation
  ─ Phagocytosis >> killing of non-opsonized bacteria

  COMPLEMENT ACTIVATION:
  ─ IgM (pentamer) or IgG1/3 Fc binds C1q → classical pathway
  ─ C3b deposition on pathogen → further opsonization
  ─ MAC formation → direct killing

  ADCC (Antibody-Dependent Cellular Cytotoxicity):
  ─ IgG on target cell → NK cells recognize Fc (CD16) → kill
  ─ Key mechanism for: Trastuzumab (HER2 cancer therapy)
  ─ Also: Rituximab (anti-CD20 for B cell lymphoma)

  MAST CELL/BASOPHIL DEGRANULATION:
  ─ IgE binds FcεRI on mast cells → sensitized state
  ─ Allergen cross-links IgE:FcεRI → degranulation
  ─ Release: Histamine, leukotrienes, prostaglandins → allergy
```

---

## Therapeutic Antibodies

```
  MONOCLONAL ANTIBODIES (mAbs) AS DRUGS
  ========================================

  PRODUCTION: Hybridoma (mouse B cell × myeloma) → originally murine
  Now: Fully human antibodies from transgenic mice or phage display

  NAMING CONVENTIONS:
  -umab: fully human (e.g., adalimumab, pembrolizumab)
  -zumab: humanized (95% human, e.g., trastuzumab)
  -ximab: chimeric (70% human, e.g., rituximab, infliximab)
  -momab: murine (highly immunogenic, rarely used now)

  FORMATS:
  ┌────────────────────────────────────────────────────────────┐
  │ Full IgG (most common): Full Fc → long half-life, effectors│
  │                                                             │
  │ Fab fragment: Antigen-binding only, no Fc                  │
  │   Fast clearance → used for imaging, rapid therapy switch  │
  │   Example: Ranibizumab (eye injection, no ADCC needed)    │
  │                                                             │
  │ ScFv: Single-chain variable fragment (VH-linker-VL)       │
  │   Building block for CAR-T and bispecific constructs       │
  │                                                             │
  │ Bispecific: Two different antigen-binding arms             │
  │   Blinatumomab: CD19 (B cell) × CD3 (T cell)              │
  │   Brings T cells to kill B cell tumors                     │
  │                                                             │
  │ ADC (Antibody-Drug Conjugate):                            │
  │   Antibody + cytotoxin linked via cleavable linker         │
  │   Trastuzumab emtansine (T-DM1): HER2 → delivers toxin   │
  └────────────────────────────────────────────────────────────┘
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| First antibody in primary response | IgM (pentamer, complement activator) |
| Most abundant serum antibody | IgG |
| Only antibody crossing placenta | IgG (via FcRn) |
| Best mucosal protection | IgA (sIgA at mucosal surfaces) |
| Allergy/anaphylaxis mediator | IgE (FcεRI on mast cells) |
| What generates antibody diversity? | VDJ recombination + N-nucleotides + somatic hypermutation |
| What improves antibody quality over time? | Affinity maturation in germinal centers |
| How does rituximab kill B cells? | Anti-CD20 → ADCC + complement |
| What is a bispecific antibody? | Two specificities: one target + one effector cell (CD3/CD19) |
| Why do polysaccharide vaccines generate poor memory? | T-independent → no germinal center → mainly IgM, no class switch |

---

## Common Confusion Points

**VDJ vs. somatic hypermutation**: VDJ recombination builds the initial repertoire before antigen exposure — it's random and happens in the bone marrow. Somatic hypermutation refines the receptor sequence AFTER antigen exposure during the germinal center reaction. VDJ = initial diversity; SHM = affinity optimization.

**Antibody titer vs. functionality**: A high titer of IgG (lots of antibody) doesn't guarantee protection. What matters is whether the antibody neutralizes the pathogen, whether it's the right isotype for the tissue, and whether it targets the right epitope. Some antibodies at low titer neutralize brilliantly; others at high titer do nothing useful.

**IgG subclasses have very different effector functions**: IgG4 does not activate complement and has very low FcγR affinity — it's essentially an anti-inflammatory IgG. Therapeutic antibodies designed NOT to have effector function (e.g., checkpoint inhibitors that just block a receptor) are often engineered as IgG4 or have Fc-silent modifications.

**Class switching is irreversible at the cell level**: When a B cell switches from IgM to IgG, the DNA encoding the IgM heavy chain constant region is physically deleted (by AID-mediated recombination). The cell cannot go back to IgM. The receptor specificity (VDJ) is retained, but the isotype is permanently changed.
