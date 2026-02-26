# Signaling Pathways: Wnt, Notch, Hedgehog

## The Big Picture

Three signaling pathways — Wnt, Notch, and Hedgehog — are deployed repeatedly throughout development. Understanding their core mechanics is essential; their biology is re-used in nearly every organ context and all three are cancer-relevant.

```
+──────────────────────────────────────────────────────────────────+
|          THREE CORE DEVELOPMENTAL SIGNALING PATHWAYS            |
|                                                                  |
|  Wnt/β-catenin    Notch              Hedgehog                   |
|  ─────────────    ──────────         ──────────                  |
|  Diffusible       Juxtacrine         Diffusible (lipid-modified) |
|  ligand           (cell contact)     ligand                     |
|  GPCR-like        Ligand AND         GPCR-like receptor          |
|  response         receptor on same   signaling                   |
|  cell             or neighboring     via Gli TFs                 |
|                   cell               through primary cilium      |
|                                                                  |
|  Used in:         Used in:           Used in:                   |
|  Stem cells       Cell fate choice   Neural tube (floor plate)   |
|  Axis patterning  Lateral inhibition Limb patterning (ZPA)       |
|  Colon epithelium Angiogenesis       Cerebellum development      |
|  Colorectal CA    T-ALL              Basal cell carcinoma         |
+──────────────────────────────────────────────────────────────────+
```

---

## Wnt/β-Catenin Pathway

```
CANONICAL WNT PATHWAY MECHANICS
─────────────────────────────────

  WNT OFF STATE:
  ┌─────────────────────────────────────────────────────┐
  │  β-catenin is continuously phosphorylated by         │
  │  DESTRUCTION COMPLEX:                               │
  │    APC + Axin + GSK3β + CK1                        │
  │    ↓                                                │
  │    P-β-catenin → ubiquitination → proteasomal       │
  │    degradation                                      │
  │    ↓                                                │
  │    β-catenin levels in cytoplasm: LOW               │
  │    TCF/LEF transcription factors: REPRESSED         │
  └─────────────────────────────────────────────────────┘

  WNT ON STATE:
  ┌─────────────────────────────────────────────────────┐
  │  Wnt ligand binds Frizzled (GPCR-like) + LRP5/6     │
  │    ↓                                                │
  │  Dishevelled (Dvl) activated                        │
  │    ↓                                                │
  │  Destruction complex INHIBITED:                     │
  │    Axin sequestered at LRP → complex disrupted      │
  │    ↓                                                │
  │  β-catenin accumulates (not phosphorylated)         │
  │    ↓                                                │
  │  β-catenin → nucleus → binds TCF/LEF                │
  │    ↓                                                │
  │  Transcription of target genes: c-Myc, Cyclin D1,  │
  │    Axin2, LGR5 (stem cell marker), etc.             │
  └─────────────────────────────────────────────────────┘
```

**Key regulators and their levels:**

```
Wnt SIGNAL MODULATORS
──────────────────────
  Secreted inhibitors (block Wnt):
    Dkk1/2/3/4: bind LRP5/6 coreceptor → prevent Frizzled-LRP complex
    sFRP (secreted Frizzled-related proteins): decoy Frizzled receptors
    Sclerostin/SOST: binds LRP5/6; expressed in bone; anti-osteogenic

  Agonists (enhance Wnt):
    RSPO (R-spondin) proteins: bind LGR4/5/6 → prevent Frizzleds from
    being degraded → more receptors available → amplified Wnt signaling
    RSPO + Wnt combinations define intestinal stem cell niche

CANCER MUTATIONS (Wnt pathway)
  APC mutations: ~80% of colorectal cancer.
    APC normally promotes β-catenin phosphorylation.
    Loss-of-function APC → destruction complex fails → constitutive β-catenin activation.
    This is the "gatekeeper" mutation for colorectal cancer.
  β-catenin gain-of-function: Cannot be phosphorylated → constitutive activation.
    Hepatocellular carcinoma, endometrial cancer, desmoid tumors.
  WNT pathway drugs:
    Porcupine inhibitors: Block Wnt secretion (all Wnts palmitoylated by Porcupine).
    Tankyrase inhibitors: Stabilize Axin → destroy more β-catenin.
    Under clinical investigation; toxicity to GI stem cells is dose-limiting.
```

---

## Non-Canonical Wnt Pathways

```
PLANAR CELL POLARITY (PCP) PATHWAY
────────────────────────────────────
  Wnt signals through Frizzled but NOT through β-catenin.
  Downstream: Rho/Rac GTPases → cytoskeleton organization.
  Function: Orient cells within a tissue plane.
    Aligns hair cells in cochlea (inner ear orientation)
    Convergent extension: cells intercalate to elongate tissue
    Neural tube closure (critical!)

  PCP DEFECTS
    Neural tube defects (NTDs): Wnt/PCP required for neural tube closure.
    Inner ear hair cell misorientation → balance/hearing defects.
    Situs inversus (Node cilia orientation).

WNT-Ca²+ PATHWAY
  Another non-canonical branch.
  Frizzled → Gq → PLC → IP3 → Ca²+ release.
  Downstream: CaMKII, calcineurin, NFAT.
  Less characterized developmentally; immune cell signaling.
```

---

## Notch Pathway

```
NOTCH PATHWAY MECHANICS
─────────────────────────
  Juxtacrine: Ligand and receptor must be on adjacent cells.
  No diffusion. Creates sharp boundaries, not gradients.

  LIGANDS (on signaling cell): Delta-like (DLL1, DLL3, DLL4), Jagged (JAG1, JAG2)
  RECEPTOR (on receiving cell): Notch 1-4

  MECHANISM
  ┌──────────────────────────────────────────────────────────┐
  │  1. Ligand (Delta) on Cell A binds Notch on Cell B       │
  │  2. Notch ectodomain pulled off by ADAM metalloprotease  │
  │     (trans-endocytosis: ligand cell pulls on Notch)      │
  │  3. Remaining Notch stub cleaved by γ-secretase          │
  │     (same protease that cleaves APP in Alzheimer's)      │
  │  4. NICD (Notch Intracellular Domain) released           │
  │  5. NICD → nucleus → binds CSL/RBPjk                     │
  │  6. Activates target genes: HES1, HES5, HEY1             │
  │     (basic helix-loop-helix repressors)                  │
  │  7. HES genes repress Atonal, Neurogenin, Ascl1          │
  │     → Cell B does NOT become a neuron (or whatever fate) │
  └──────────────────────────────────────────────────────────┘

  LATERAL INHIBITION (the key Notch function)
  ─────────────────────────────────────────────
  When one cell begins to differentiate (say, a neuron precursor):
    → It upregulates Delta on its surface.
    → Delta activates Notch in neighbors.
    → Neighbors: ↑HES1 → represses neural fate TFs.
    → Neighbors CANNOT become neurons.
  Net result: Only ONE cell out of a group differentiates.
  Pattern: spaced neurons amid a sea of non-neurons.
  This is how the nervous system avoids making too many neurons.
```

---

## Notch in Development and Disease

```
NOTCH FUNCTIONS ACROSS CONTEXTS
──────────────────────────────────
  Context              Notch Function
  ──────────────────── ──────────────────────────────────────────────
  Nervous system       Lateral inhibition → neuron spacing
                       Maintains neural stem cell pool
  Inner ear            Hair cell specification (1 per 6 supporting cells)
  Intestinal crypt     Absorptive vs secretory fate (Notch→absorptive)
  Vasculature          Arterial vs venous fate; VEGF tip vs stalk cell
  T-cell development   Multiple checkpoints; thymic selection
  Pancreas             Acinar vs islet fate

NOTCH IN CANCER
  Gain-of-function:
    T-ALL (T-cell acute lymphoblastic leukemia): NOTCH1 mutations > 60%
    → Activating mutations in NRR (prevents proteolysis without ligand)
    → Constitutive NICD release → immortalization of T-cell progenitors
    Treatment: γ-secretase inhibitors (GSIs) — clinical trials
    Problem: GSIs cause GI toxicity (intestinal secretory cells require Notch OFF)

  Loss-of-function:
    Alagille syndrome: JAG1 mutations → liver, heart, vertebral defects
    CADASIL: NOTCH3 mutations → vascular dementia, stroke
    Squamous cell carcinoma: NOTCH1/2 tumor suppressors in skin

FRINGE PROTEINS: Modulate Notch-Ligand Selectivity
  Lunatic/Manic/Radical Fringe: GlcNAc-transferases; modify Notch EGF repeats
  → Preferential activation by Delta vs Jagged
  Critical for somitogenesis (boundary precision depends on Fringe modulation)
```

---

## Hedgehog Pathway

```
HEDGEHOG PATHWAY MECHANICS
────────────────────────────
  Ligands: Sonic Hedgehog (Shh), Desert Hedgehog (Dhh), Indian Hedgehog (Ihh)
  Requires: Lipid modification (cholesterol at C-terminus, palmitate at N-terminus)
           Dispatched (DISP): releases Shh from producing cell
           Heparan sulfate proteoglycans: facilitate diffusion

  HEDGEHOG OFF STATE:
  ┌────────────────────────────────────────────────────────────┐
  │  PATCHED (PTCH1): 12-transmembrane receptor                │
  │  Normally INHIBITS Smoothened (SMO)                        │
  │  SMO is inactive → CI/Gli processed into repressor form    │
  │  Gli3-R: repressor → target genes OFF                      │
  │  (via Suppressor of Fused, kinase phosphorylation)         │
  └────────────────────────────────────────────────────────────┘

  HEDGEHOG ON STATE:
  ┌────────────────────────────────────────────────────────────┐
  │  Shh binds PTCH1 → PTCH1 moves away from cilium           │
  │    ↓                                                       │
  │  SMO accumulates in primary cilium → activated             │
  │    ↓                                                       │
  │  Full-length Gli2/Gli1 → activator form (Gli-A)            │
  │  Gli2-A → nucleus → activates target genes:               │
  │    Ptch1 (feedback), Gli1, Cyclin D/E, Bcl-2              │
  └────────────────────────────────────────────────────────────┘

  PRIMARY CILIUM REQUIREMENT
  The Hedgehog pathway in vertebrates runs THROUGH the primary cilium.
  All components (PTCH1, SMO, Gli proteins) traffic in/out of cilia.
  Mutations in ciliary genes → Hedgehog signaling defects.
  Ciliopathies (Bardet-Biedl, Joubert, Meckel syndromes): Hh defects.
```

---

## Hedgehog in Development

```
SHH FUNCTIONS BY ORGAN
────────────────────────
  NEURAL TUBE
    Shh from notochord and floor plate → ventral-to-dorsal gradient.
    High Shh (ventral): motor neuron specification (Nkx2.2, Olig2 TFs)
    Low Shh (dorsal): interneuron types (Pax7, Dbx TFs)
    Very precise: 5 different motor neuron subtypes from Shh concentration.

  LIMB BUD (Zone of Polarizing Activity, ZPA)
    ZPA (posterior limb mesenchyme) secretes Shh.
    Shh gradient anterior-to-posterior:
    Posterior (high Shh) → little finger identity (5th digit, HOXD13 high)
    Anterior (low Shh) → thumb identity (1st digit)
    Classic ZPA transplant experiment:
      Graft ZPA to anterior of a second limb bud → mirror image digits
      (6 digits: 2345-5432 instead of 12345)

  CEREBELLUM
    Shh from Purkinje cells → drives granule cell precursor proliferation.
    Medulloblastoma: 25-30% have activating Hh mutations (→ granule cells over-proliferate)

  BRAIN MIDLINE (forebrain)
    Prechordal plate Shh → ventral forebrain specification.
    Shh mutations → holoprosencephaly (failure to separate brain hemispheres).
    Alcohol → depletes cholesterol → reduces Shh modification → holoprosencephaly risk.
```

---

## Hedgehog in Cancer and Therapy

```
HEDGEHOG PATHWAY CANCERS
──────────────────────────
  BASAL CELL CARCINOMA (BCC)
    Most common cancer in humans.
    90%+ have PTCH1 loss-of-function (tumor suppressor).
    PTCH1 LOF → SMO constitutively active → Gli target genes → proliferation.
    Treatment: Vismodegib (SMO inhibitor) — first FDA-approved Hh pathway drug.
    Sonic Hedgehog subgroup medulloblastoma: similar mechanism; used in children.

  MEDULLOBLASTOMA (SHH subtype)
    ~30% of medulloblastomas.
    PTCH1 or SUFU loss, SMO gain-of-function, or pathway amplification.
    Vismodegib/sonidegib in clinical use.

  RESISTANCE TO SMO INHIBITORS
    SMO mutations that prevent vismodegib binding (analogous to imatinib T315I).
    Gli2 amplification: bypass SMO entirely.
    Research: Gli inhibitors as second-line therapy.

HEDGEHOG IN NORMAL ADULT TISSUE MAINTENANCE
  Inactive in most adult tissues.
  Active in:
    Hair follicle cycling (Shh drives anagen/growth phase)
    Intestinal stem cell niche (Hh from stromal cells)
    Bone remodeling: Ihh in growth plate
```

---

## Pathway Interactions (Crosstalk)

```
WNT-NOTCH-HEDGEHOG INTERACTIONS
─────────────────────────────────
  In intestinal crypt:
    WNT HIGH (bottom of crypt) → LGR5+ stem cells → proliferation
    NOTCH HIGH (stem cells, adjacent transit amplifying) → absorptive fate
    NOTCH LOW (secretory lineage) → Atoh1 → goblet/Paneth/enteroendocrine
    HEDGEHOG from villi → BMP → inhibit Wnt in villus → differentiation

  In neural stem cells:
    NOTCH → Hes1 → maintains stem state (represses proneural genes)
    WNT → Cyclin D → promotes G1 progression → proliferation
    HEDGEHOG → Gli2 → granule precursor proliferation

  IN GENERAL:
    Wnt: often promotes proliferation/stemness
    Notch: often maintains progenitor state via lateral inhibition
    Hedgehog: often specifies ventral/positional identity; also proliferative in certain contexts
    BMP: often promotes differentiation / inhibits stemness
    These are rough tendencies — context is everything.
```

---

## Decision Cheat Sheet

| Pathway | Key Receptor | Key Effector TF | Cancer Relevance | Therapeutic |
|---------|-------------|----------------|-----------------|-------------|
| Wnt | Frizzled + LRP5/6 | β-catenin → TCF/LEF | APC mutations (CRC), CTNNB1 (HCC) | Tankyrase inh., PORCN inh. |
| Notch | Notch1-4 | NICD → CSL/RBPjk → HES | NOTCH1 in T-ALL, JAG1 in Alagille | γ-secretase inh. (GSI) |
| Hedgehog | PTCH1/2, SMO | Gli1/2/3 | PTCH1 in BCC, medulloblastoma | Vismodegib (SMO inh.) |

---

## Common Confusion Points

**"Wnt has canonical and non-canonical arms — are these really distinct?"**
They share some components (Frizzled, Dishevelled) but diverge at Dvl: canonical goes to β-catenin/TCF; PCP goes to Rho/Rac; Wnt-Ca²+ goes through PLC. In practice, a given Wnt ligand can activate multiple arms depending on which coreceptors are present. Context (cell type, available coreceptors) determines which arm is activated.

**"Notch ligand is on one cell, receptor on neighbor — can a cell signal to itself?"**
In trans (cell-to-cell): this is the canonical lateral inhibition mode. In cis (same cell): when a cell has both ligand and receptor, the ligand sequesters and downregulates the receptor — cis-inhibition. This actually enhances the sharpness of the cell fate boundary: cells with high Delta have low active Notch; cells with low Delta have high active Notch. It creates a toggle switch with very sharp boundaries.

**"Why does Hedgehog require the primary cilium in vertebrates but not Drosophila?"**
The primary cilium is a vertebrate innovation for Hedgehog signal transduction. In Drosophila, Hh signaling works via similar proteins but without the ciliary trafficking requirement. This is an example of pathway conservation with mechanistic divergence. Vertebrate ciliary requirement explains why ciliopathy syndromes (Bardet-Biedl, etc.) have Hedgehog-related phenotypes.
