# Stem Cells: Pluripotency and Differentiation

## The Big Picture

Stem cells are defined by two properties: self-renewal (can make more stem cells) and potency (can generate differentiated cell types). The hierarchy from totipotent zygote to committed progenitor is a one-way cascade under normal conditions — until reprogramming broke that assumption.

```
+──────────────────────────────────────────────────────────────────+
|              STEM CELL POTENCY HIERARCHY                         |
|                                                                  |
|  TOTIPOTENT: Can make ALL cell types including trophectoderm     |
|  Zygote, 2-cell blastomere                                      |
|       ↓                                                          |
|  PLURIPOTENT: Can make all embryonic cell types (3 germ layers) |
|  Epiblast, ESC, iPSC                                            |
|       ↓                                                          |
|  MULTIPOTENT: Can make all types within a tissue/lineage        |
|  HSC (all blood), NSC (neurons + glia + oligodendrocytes)       |
|       ↓                                                          |
|  OLIGOPOTENT: 2-3 lineages                                      |
|  Common myeloid progenitor (CMP): myeloid cell types            |
|       ↓                                                          |
|  UNIPOTENT: One cell type                                       |
|  Spermatogonial stem cell (sperm only)                          |
|       ↓                                                          |
|  TERMINALLY DIFFERENTIATED: No further division in most cases   |
|  Neurons, cardiomyocytes, erythrocytes                          |
+──────────────────────────────────────────────────────────────────+
```

---

<!-- @editor[bridge/P2]: No CS/engineering bridge. The stem cell potency hierarchy is a "type hierarchy with narrowing casts" — totipotent is the base class, each step down restricts the interface. The niche concept maps to "dependency injection" — the environment determines behavior, not the cell alone. Bivalent chromatin is "feature flags on developmental genes — poised but not active." -->
## Embryonic Stem Cells (ESCs)

```
ESC DERIVATION AND PROPERTIES
───────────────────────────────
  Source: Inner cell mass (ICM) of blastocyst
  Derivation: Isolated ICM + LIF/FGF2/BMP4 signaling → ESC lines
  Key properties:
    Self-renewal: Indefinite proliferation (rare among mammalian cells)
    Pluripotency: Differentiate into any somatic cell type
    Normal karyotype (if properly cultured)
    Unique gene expression: Oct4, Sox2, Nanog, KLF4, Rex1...

PLURIPOTENCY TRANSCRIPTION FACTOR NETWORK
  OCT4 (Pou5f1): Homeodomain TF; essential for ICM identity.
                 Oct4 KO → no ICM → trophectoderm only.
  SOX2: HMG-box TF; redundant in ICM but required for epiblast.
  NANOG: Homeobox TF; prevents primitive endoderm fate.
         Nanog KO → only primitive endoderm from ICM (no epiblast).

  The core circuit:
    Oct4, Sox2, Nanog → activate each other (mutual reinforcement)
    Oct4, Sox2, Nanog → repress differentiation genes
    Oct4, Sox2, Nanog → activate themselves (auto-regulatory loops)
    This creates a self-sustaining pluripotency state.

  BISTABILITY
  Oct4-Sox2-Nanog and Cdx2 (TE) are mutually repressive switches.
  Inside cell: Oct4 high → Cdx2 low → ICM.
  Outside cell: Hippo signaling → Cdx2 activates → Oct4 repressed → TE.
  Two stable states, not a continuum.

EPIGENETIC STATE OF ESCs
  Bivalent chromatin domains: simultaneously H3K4me3 (active) + H3K27me3 (repressive).
  Developmental genes: in bivalent state → poised but not active.
  Upon differentiation: Lose H3K27me3 (become active) OR lose H3K4me3 (silenced).
  This bivalency allows rapid, coherent activation or silencing upon differentiation.
```

---

## Pluripotency States

```
NAIVE vs PRIMED PLURIPOTENCY
──────────────────────────────
  TWO DISTINCT PLURIPOTENT STATES:

  NAIVE (pre-implantation epiblast):
    Mouse: LIF + 2i conditions (MEK inhibitor + GSK3 inhibitor)
    Human naive: more recently established (2015+)
    Properties:
      Both X chromosomes active (female cells)
      Can contribute to chimera (mouse)
      Global DNA hypomethylation
      Bivalent genes poised
      Express Rex1, Dppa3, Klf4

  PRIMED (post-implantation epiblast = EpiSC):
    Human ESCs are mostly in this state
    Properties:
      One X inactivated (female)
      Cannot contribute to mouse chimera
      FGF/Activin dependent
      Higher DNA methylation
      Partially restricted gene expression

  THE GROUND STATE
  Naive pluripotency with 2i: "ground state" — remove all external lineage signals.
  Result: Uniform, stable pluripotency; least differentiation-prone.
  Alternative to serum/LIF: more uniform, less noisy.

TRANSITION: NAIVE → PRIMED → DIFFERENTIATION
  Naive → Primed: FGF/ERK activation, X inactivation, global methylation.
  Primed → Differentiation: Lineage-specific signals (BMP, Wnt, Activin/Nodal, FGF)
  → Remove Sox2, Nanog, Oct4 from lineage genes → activate germ-layer TFs.
```

---

## Hematopoietic Stem Cells (HSCs)

```
THE HEMATOPOIETIC HIERARCHY
─────────────────────────────
  HSC (Long-term, LT-HSC)
     │  Self-renewal: Years
     │  Location: Bone marrow niche
     ↓
  Short-term HSC (ST-HSC)
     │  Limited self-renewal
     ↓
  ┌───────────────────────────────────┐
  │ Multipotent Progenitor (MPP)       │
  └───┬───────────────────────────────┘
      │
  ┌───┴──────────────────┐
  │                      │
  CMP                   CLP
  (Common Myeloid)      (Common Lymphoid)
  │                      │
  ├── Granulocyte-         ├── B-cell progenitor → B cells/plasma cells
  │   monocyte prog        ├── T-cell progenitor → T cells (thymus)
  │   → neutrophils,       └── NK progenitor → NK cells
  │   monocytes, macrophages
  ├── MEP (megakaryocyte-erythroid)
      → Red blood cells (erythrocytes)
      → Platelets (from megakaryocytes)

DAILY PRODUCTION
  Humans: ~500 billion blood cells/day from HSCs.
  Erythrocytes: 200 billion/day; each lives ~120 days.
  Neutrophils: ~100 billion/day; each lives hours.
  HSC quiescence: Most HSCs are dormant (G0); activated for reconstitution.

HSC NICHE (BONE MARROW)
  Endosteal niche: Osteoblasts secrete CXCL12 → CXCR4 on HSC → retention.
  Perivascular niche: Sinusoidal endothelial cells + Leptin receptor+ MSCs.
  Signals maintaining HSC:
    CXCL12 (CXCR4): retention + quiescence
    SCF/KitL (Kit): survival/proliferation
    Thrombopoietin/Mpl: self-renewal
    Angiopoietin-1 (Tie2): quiescence
  Exiting niche: G-CSF → CXCL12 downregulation → HSC mobilization to blood.
  Clinical: Plerixafor (CXCR4 antagonist) + G-CSF → HSC mobilization for transplant.
```

---

## Neural Stem Cells (NSCs)

```
ADULT NEUROGENESIS
───────────────────
  Historically believed: No new neurons in adult brain.
  Now established (in rodents): Two neurogenic niches in adult brain.

  1. SUBVENTRICULAR ZONE (SVZ)
     Radial glia-like NSC → transit amplifying progenitors → neuroblasts
     → Migrate along rostral migratory stream → olfactory bulb
     → Granule cells + periglomerular interneurons

  2. SUBGRANULAR ZONE (SGZ) in Hippocampus
     Radial glia-like NSC → IPC → newborn dentate granule neurons
     → Integrate into existing hippocampal circuits
     → Function: Memory formation, pattern separation

  HUMAN NEUROGENESIS DEBATE
  Rodent: well established.
  Human: controversial.
  Spalding et al. (2013, ¹⁴C dating): ~700 new neurons/day in human hippocampus.
  Sorrells et al. (2018): No newborn neurons in adult human hippocampus.
  Boldrini et al. (2018): Neurogenesis persists into 8th decade.
  Status: Debated; methodological issues in detecting rare newborn neurons.

NSC REGULATION
  Quiescence maintained by: Notch, BMP4 (from SVZ astrocytes)
  Activation: FGF2, EGF, VEGF, Shh
  Differentiation: BDNF, NT-3 (neurotrophin) → neuronal fate
  Oligodendrocyte: PDGF, T3 (thyroid hormone)
  Astrocyte: CNTF, LIF (JAK-STAT)
```

---

## Intestinal Stem Cells: The Prototypical Adult Tissue Stem Cell

```
INTESTINAL CRYPT STEM CELL NICHE
──────────────────────────────────
  Columnar basal crypt cells (CBCs): Lgr5+ cells at crypt base.
  Rapidly cycling (~daily). Self-renewing + multipotent.
  Lgr5: R-spondin receptor. Marks active stem cells.
  Turn over every 3-5 days (entire intestinal epithelium).

  NICHE SIGNALS
  Wnt:  Paneth cells at crypt base secrete Wnt3, Wnt11
        + R-spondin (RSPO1/3) from stromal cells → ↑Frizzled
        → β-catenin → stem cell maintenance
  Notch: Paneth cells express Dll4 → Notch on CBC → HES1 → absorptive fate
  EGF:  Mesenchyme + Paneth → EGFR → proliferation
  BMP:  From villus mesenchyme → inhibit Wnt → differentiation toward villus

  LGAIN HIERARCHY
  LGR5+ CBC → TA cells (transit amplifying, rapid cycling) →
  Mature cells: enterocytes, goblet cells, enteroendocrine, Paneth (±tuft cells)
  Paneth cells: at crypt base, provide niche signals BACK to LGR5+ cells
  (amazing feedback: the differentiated Paneth cell maintains its own progenitor)

ORGANOIDS (mini-guts)
  Sato et al. (2009): Isolated LGR5+ cells + Wnt/Rspondin/EGF/Noggin → 3D crypt organoids.
  Self-organizing intestinal epithelium in Matrigel.
  Applications:
    Disease modeling: IBD, colorectal cancer
    Drug screening: personalized (patient-derived organoids)
    Regenerative medicine: transplant organoid-derived epithelium (clinical trials)
```

---

## Stem Cell Fate Control: Key Concepts

```
SYMMETRIC vs ASYMMETRIC DIVISION
──────────────────────────────────
  SYMMETRIC: Daughter cells both same fate.
    → Expansion: 1 stem cell → 2 stem cells (amplify pool)
    → Depletion: 1 stem cell → 2 differentiated (exhaust pool)

  ASYMMETRIC: Daughters have different fates.
    → Stem cell homeostasis: 1 stem cell → 1 SC + 1 progenitor
    Mechanism: Unequal segregation of cell-fate determinants.
    Drosophila neuroblast: Numb + Prospero segregate basally → daughter differentiates.

THE NICHE CONCEPT
  Schofield (1978) coined "niche": microenvironment that maintains stem cell identity.
  Remove cell from niche → differentiation.
  Transplant into a niche → stem cell renewal.
  The niche is as important as the cell.

COMPETITION AMONG STEM CELLS
  Stem cells compete for niche space.
  "Supercompetitors": higher fitness → displace weaker stem cells.
  Relevant to cancer initiation: oncogenic mutation in one stem cell → competitive advantage → clonal expansion.
  Colon cancer: APC mutation in one LGR5+ cell → Wnt gain → outcompetes normal cells → clone.
```

---

<!-- @editor[content/P2]: Cancer stem cell hypothesis absent — a major stem cell topic: the idea that tumors are maintained by a stem-like subpopulation (CSCs) with implications for therapy resistance and relapse. Would fit naturally after the "Competition Among Stem Cells" section. -->
## Decision Cheat Sheet

| Stem Cell Type | Self-Renewal | Potency | Niche Signals | Clinical Relevance |
|---------------|-------------|---------|--------------|-------------------|
| Embryonic (ESC) | Unlimited | Pluripotent | LIF, FGF2, Activin | Disease modeling, cell therapy |
| iPSC | Unlimited | Pluripotent | Same as ESC | Patient-specific therapy |
| HSC (LT-HSC) | Long-term | Multipotent (all blood) | CXCL12, SCF, TPO | Bone marrow transplant |
| NSC (adult) | Limited | Multipotent (CNS) | FGF2, EGF, Notch | Neurological disease |
| LGR5+ intestinal | Unlimited (in situ) | Multipotent (intestinal) | Wnt, EGF, Notch | Organoid therapy, IBD |
| Satellite cell (muscle) | Quiescent; activated by injury | Myogenic | HGF, FGF | Muscular dystrophy |

---

## Common Confusion Points

**"ESC vs iPSC — functionally equivalent?"**
Largely yes in terms of potency, but not identical. iPSCs retain some epigenetic memory of the somatic cell they came from. Residual methylation patterns can bias differentiation toward the original cell type. This fades over multiple passages. Additionally, iPSCs carry all mutations from the patient's somatic cells (accumulate with age). For modeling genetic diseases: iPSCs are essential. For clinical therapy: the epigenetic and mutational state of the starting cell matters.

**"If HSCs can make all blood cells, why can't they make liver cells?"**
In normal homeostasis: No. HSC commitment → hematopoietic lineage. The HSC niche + intrinsic epigenetic state locks it into hematopoietic programs. In extreme injury models (parabiosis, bone marrow transplant + CCl4 liver injury): rare events where hematopoietic cells contribute to liver epithelium occur by cell fusion (not transdifferentiation). Genuine transdifferentiation requires reprogramming interventions.

**"Adult neurogenesis debate — does it matter clinically?"**
Substantially. If the human hippocampus generates new neurons throughout life, then: depression may involve reduced neurogenesis (SSRIs promote neurogenesis — this may be a mechanism); exercise (proven neurogenesis stimulus in rodents) has additional benefit; traumatic brain injury has recovery potential via new neurons. If adult human neurogenesis is minimal, these mechanisms don't apply. The debate has real therapeutic implications.
