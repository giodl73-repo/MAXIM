# Adaptive Immunity

## The Big Picture

```
ADAPTIVE IMMUNITY: LEARNED, SPECIFIC, REMEMBERED
=================================================

  THE ML ANALOGY (not metaphor — formal parallel):
  ┌──────────────────────────────────────────────────────────────────┐
  │  ML System                 │  Adaptive Immune System             │
  ├────────────────────────────┼─────────────────────────────────────┤
  │  Training data             │  Antigen exposure (infection/vaccine)│
  │  Model parameters          │  BCR/TCR receptor sequences          │
  │  Training (gradient desc.) │  Clonal selection + affinity matur. │
  │  Inference                 │  Effector cell response              │
  │  Model persistence         │  Long-lived memory cells             │
  │  Ensemble of models        │  Memory B + T cell pool              │
  │  Catastrophic forgetting   │  Immune senescence (aging)           │
  └──────────────────────────────────────────────────────────────────┘

  CHARACTERISTICS:
  ─ Specificity: Each lymphocyte has ONE receptor recognizing ONE shape
  ─ Diversity: ~10¹⁸ potential receptor sequences in the repertoire
  ─ Self-tolerance: Self-reactive cells deleted in development
  ─ Memory: Long-lived cells persist after infection clears
  ─ Clonality: One matching cell → proliferates → clones of identical cells

  TWO ARMS:
  HUMORAL  (B cells → antibodies):
    Targets: Extracellular pathogens, toxins, viruses
    Effectors: Immunoglobulins circulate in serum/secretions

  CELL-MEDIATED (T cells → cytokines + killing):
    Targets: Intracellular pathogens, tumors, transplanted organs
    Effectors: Cytokines (help), perforin/granzyme (kill)
```

---

## Lymphocyte Development

### B Cell Development (Bone Marrow)

```
  B CELL DEVELOPMENT
  ===================

  SITE: Bone marrow (primary lymphoid organ)

  DEVELOPMENTAL STAGES:
  Hematopoietic stem cell
       │
       ▼ Commitment to lymphoid lineage
  Common lymphoid progenitor
       │
       ▼ Transcription factors: Ikaros, E2A, EBF1, Pax5
  Pro-B cell
       │ VDJ recombination of IMMUNOGLOBULIN HEAVY CHAIN gene
       ▼ (D-J joining first, then V-DJ joining)
  Pre-B cell
       │ Pre-B cell receptor (μ heavy chain + surrogate light chain)
       │ Signals: proliferate + stop heavy chain rearrangement
       ▼
  Immature B cell
       │ VJ recombination of IMMUNOGLOBULIN LIGHT CHAIN gene
       │ IgM expressed on surface
       ▼ CENTRAL TOLERANCE CHECKPOINT
       │ If IgM binds self-antigen → CLONAL DELETION or receptor editing
  Mature naïve B cell
       │ Exits bone marrow to blood/spleen
       ▼ Encounters antigen in periphery → activated
  Germinal center reaction → Plasma cell + Memory B cell

  CENTRAL TOLERANCE MECHANISMS IN B CELLS:
  ─ Clonal deletion: Strong BCR self-reactivity → apoptosis
  ─ Receptor editing: RAG genes reactivate → new light chain rearranged
  ─ Anergy: B cell still alive but functionally unresponsive
```

### T Cell Development (Thymus)

```
  T CELL DEVELOPMENT IN THE THYMUS
  ===================================

  SITE: Thymus (primary lymphoid organ; involutes with age)

  ENTRY: Bone marrow-derived T cell progenitors enter thymus

  STAGE 1: CORTEX — POSITIVE SELECTION
  ┌─────────────────────────────────────────────────────────────┐
  │ Double-positive (CD4+CD8+) thymocytes                       │
  │ TCR must be able to bind self-MHC (at least weakly)         │
  │                                                             │
  │ Test: Cortical thymic epithelial cells present self-peptide │
  │       on MHC I and MHC II                                   │
  │                                                             │
  │ Result:                                                     │
  │   Binds MHC I: Become CD8+ T cell (single positive)         │
  │   Binds MHC II: Become CD4+ T cell (single positive)        │
  │   Binds neither: Die by neglect (~95% of thymocytes)        │
  │                                                             │
  │ Why positive selection?: Ensures T cells can recognize      │
  │ self-MHC molecules (which display foreign peptides in       │
  │ infection) — TCRs that can't bind MHC are useless           │
  └─────────────────────────────────────────────────────────────┘

  STAGE 2: MEDULLA — NEGATIVE SELECTION
  ┌─────────────────────────────────────────────────────────────┐
  │ Single-positive thymocytes encounter medullary DCs + mTECs  │
  │ mTECs express AIRE (AutoImmune REgulator) transcription     │
  │ factor → express tissue-restricted antigens (insulin, etc.) │
  │                                                             │
  │ Test: Does TCR bind self-peptide:self-MHC too strongly?     │
  │                                                             │
  │ Result:                                                     │
  │   Binds self-peptide too strongly: CLONAL DELETION (apopt.) │
  │   Intermediate binding → TREG development                   │
  │   Appropriate binding: Survive, mature, exit to periphery   │
  │                                                             │
  │ Why negative selection?: Removes self-reactive T cells      │
  │ before they can cause autoimmunity                          │
  │                                                             │
  │ AIRE mutations → APECED syndrome (multi-organ autoimmunity) │
  └─────────────────────────────────────────────────────────────┘

  CHECKPOINT SUMMARY:
  Double-positive → Single-positive: Positive selection (learn MHC restriction)
  Single-positive → Mature: Negative selection (delete self-reactive)

  ~2% of thymocytes survive both checkpoints and exit as mature T cells
```

---

## Clonal Selection Theory

```
  CLONAL SELECTION: THE CORE PRINCIPLE OF ADAPTIVE IMMUNITY
  ===========================================================

  MACFARLANE BURNET'S THEORY (1957, Nobel Prize 1960):

  Before antigen exposure:
  ┌───┐  ┌───┐  ┌───┐  ┌───┐  ┌───┐  ┌───┐  ┌───┐
  │TCR│  │TCR│  │TCR│  │TCR│  │TCR│  │TCR│  │TCR│
  │ A │  │ B │  │ C │  │ D │  │ E │  │ F │  │ G │
  └───┘  └───┘  └───┘  └───┘  └───┘  └───┘  └───┘
  Each T cell: unique receptor, 1 copy in repertoire

  Antigen X enters:

  ┌───┐  ┌───┐  ┌───┐  [X binds C]  ┌───┐  ┌───┐  ┌───┐
  │TCR│  │TCR│  │TCR│               │TCR│  │TCR│  │TCR│
  │ A │  │ B │  │ C │ ◄───X         │ D │  │ E │  │ F │
  └───┘  └───┘  └───┘               └───┘  └───┘  └───┘
                  ↓ CLONAL EXPANSION
           ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ (1,000s of copies)
           │ C │ │ C │ │ C │ │ C │ │ C │
           └───┘ └───┘ └───┘ └───┘ └───┘
           All identical clones — same receptor
           All become effector cells (fight infection)
           Some become memory cells

  After infection clears:
  Most effector clones die → small pool of memory C cells persist

  PREDICTIONS OF CLONAL SELECTION (all verified):
  ✓ Each lymphocyte has one antigen specificity
  ✓ Antigen selects which cells respond (not what specificity to make)
  ✓ Clonal expansion amplifies the response
  ✓ Memory cells are antigen-specific
  ✓ Self-reactive clones are deleted
```

---

## Antigen Presentation via MHC

```
  THE TWO MHC PRESENTATION PATHWAYS
  ====================================

  MHC CLASS I: ENDOGENOUS ANTIGEN PRESENTATION
  ┌────────────────────────────────────────────────────────────────┐
  │ SOURCES: Cytoplasmic proteins (normal cellular + viral)        │
  │                                                                │
  │ PATHWAY:                                                       │
  │ 1. Proteasome degrades cytoplasmic proteins → 8–10 aa peptides │
  │ 2. TAP transporter moves peptides into ER                      │
  │ 3. MHC I α-chain + β₂-microglobulin + peptide assemble in ER   │
  │ 4. Complex traffics to cell surface                            │
  │                                                                │
  │ RESULT: MHC I:peptide on surface says:                         │
  │   "This is what I'm making inside. Is it foreign?"             │
  │                                                                │
  │ RECOGNIZED BY: CD8+ cytotoxic T cells (via TCR + CD8 co-recep) │
  │ PRESENT ON: All nucleated cells (ubiquitous)                   │
  │                                                                │
  │ Virally infected cell: Viral peptides on MHC I → CD8 kills it  │
  └────────────────────────────────────────────────────────────────┘

  MHC CLASS II: EXOGENOUS ANTIGEN PRESENTATION
  ┌────────────────────────────────────────────────────────────────┐
  │ SOURCES: Extracellular proteins taken up by endocytosis        │
  │                                                                │
  │ PATHWAY:                                                       │
  │ 1. APC engulfs pathogen/protein by phagocytosis/macropinocy.   │
  │ 2. Phagosome fuses with lysosome → acid pH, proteases          │
  │ 3. Proteins degraded to ~13–25 aa peptides                     │
  │ 4. MHC II α+β chains + Ii (invariant chain) in ER              │
  │ 5. MHC II:Ii traffics to late endosome/lysosome                │
  │ 6. Ii degraded → CLIP occupies binding groove                  │
  │ 7. HLA-DM (chaperone) exchanges CLIP for pathogen peptide      │
  │ 8. MHC II:peptide traffics to surface                          │
  │                                                                │
  │ RECOGNIZED BY: CD4+ helper T cells (via TCR + CD4 co-recep.)   │
  │ PRESENT ON: DCs, macrophages, B cells (professional APCs)      │
  │                                                                │
  │ DC ingests pathogen: Pathogen peptides on MHC II → CD4 help    │
  └────────────────────────────────────────────────────────────────┘

  CROSS-PRESENTATION (special case):
  Some DCs can load EXOGENOUS antigens onto MHC CLASS I
  Mechanism: Phagosome-to-cytosol transfer → proteasome → TAP → MHC I
  Importance: Priming CD8 T cells against viruses that don't infect DCs
  Critical for: Cancer immunotherapy, DNA/mRNA vaccines
```

---

## T Cell Activation: The Two-Signal Model

```
  TWO SIGNALS REQUIRED FOR T CELL ACTIVATION
  ============================================

  ONE SIGNAL ALONE IS NOT ENOUGH:

  SIGNAL 1: Antigen-specific (TCR)
  TCR + co-receptor (CD4 or CD8) bind MHC:peptide
  Activates: Lck, ZAP-70 kinases → PLCγ → IP3 + DAG
  IP3 → Ca²⁺ release → calcineurin → NFAT
  DAG → PKC → NF-κB
  → IL-2 gene transcription (up to a point)

  SIGNAL 2: Antigen-nonspecific (Co-stimulation)
  CD28 on T cell binds B7 (CD80/86) on activated APC
  Amplifies IL-2 signaling; prevents anergy; promotes survival

  COMBINED (both signals):
  Full IL-2 production → autocrine T cell proliferation
  Differentiation into effector cells

  SIGNAL 1 ALONE (no co-stimulation):
  T cell becomes ANERGIC — functionally unresponsive
  Cannot respond even if later re-stimulated
  This is a PERIPHERAL TOLERANCE MECHANISM

  CO-STIMULATORY CHECKPOINTS (exploited by cancer/immunotherapy):
  ┌───────────────────────────────────────────────────────────┐
  │ CTLA-4: Competes with CD28 for B7 binding                 │
  │   Higher affinity than CD28 → INHIBITS T cell activation  │
  │   Expressed after activation → dampens response           │
  │   Anti-CTLA-4 (ipilimumab): blocks inhibition → more      │
  │   T cell activation → cancer immunotherapy                │
  │                                                           │
  │ PD-1: Checkpoint expressed on chronic stimulation         │
  │   Binds PD-L1 (on tumor cells) → inhibits T cell          │
  │   Anti-PD-1 (pembrolizumab/nivolumab): reinvigorates      │
  │   exhausted T cells → tumor killing                       │
  └───────────────────────────────────────────────────────────┘

  THREE SIGNALS FOR FULL CD8 T CELL ACTIVATION:
  Signal 1: TCR:MHC I:peptide
  Signal 2: CD28:B7 co-stimulation
  Signal 3: Inflammatory cytokines (IL-12, IFN-γ from innate)
  Signal 3 is needed for durable CD8 memory formation
```

---

## Germinal Center and Affinity Maturation

```
  GERMINAL CENTER REACTION
  =========================

  LOCATION: B cell zones of lymph nodes and spleen

  PROCESS:
  ┌──────────────────────────────────────────────────────────────┐
  │ Activated B cell → Germinal Center (GC)                      │
  │                                                              │
  │ DARK ZONE: Rapid proliferation of centroblasts               │
  │   Activation-induced cytidine deaminase (AID) enzyme         │
  │   Introduces targeted mutations in VDJ region                │
  │   (somatic hypermutation) — ~10⁻³ per bp per generation      │
  │   (vs. ~10⁻⁹ in rest of genome)                              │
  │                                                              │
  │ LIGHT ZONE: Selection of high-affinity variants              │
  │   Mutated B cells (centrocytes) compete for antigen          │
  │   Antigen held on Follicular DCs (FDCs) as immune complexes  │
  │   High-affinity BCR captures more antigen → internalize      │
  │   Present to Tfh (T follicular helper) cells → get help      │
  │   High affinity → survive + re-enter dark zone               │
  │   Low affinity → die by apoptosis                            │
  │                                                              │
  │ ANALOGY: Gradient descent on the affinity landscape          │
  │   Random mutations (AID) = gradient perturbation             │
  │   Antigen competition = fitness function                     │
  │   Multiple rounds = optimization iterations                  │
  └──────────────────────────────────────────────────────────────┘

  OUTPUT OF GERMINAL CENTER REACTION:
  ─ Long-lived plasma cells → high-affinity antibody production
    (migrate to bone marrow; secrete Ab for decades)
  ─ Memory B cells → rapid response on re-exposure
  ─ Isotype switching: IgM → IgG, IgA, or IgE
    (AID also mediates class switch recombination)
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Where do B cells mature? | Bone marrow |
| Where do T cells mature? | Thymus |
| What kills self-reactive thymocytes? | Negative selection (medullary DCs + AIRE) |
| What ensures T cells can bind MHC? | Positive selection (cortical TECs) |
| Why do T cells need two signals? | Prevents anergy; requires APC with pathogen context |
| What is cross-presentation? | DCs loading external antigen onto MHC I → prime CD8 T cells |
| What is affinity maturation? | Somatic hypermutation + selection in germinal centers |
| What mediates somatic hypermutation? | AID (activation-induced cytidine deaminase) |
| What is clonal anergy? | T cell silence from Signal 1 without Signal 2 |
| What does CTLA-4 do? | Competes with CD28 for B7 → inhibits T cell activation |

---

## Common Confusion Points

**Positive vs. negative selection in thymus**: Both are about survival, but they test opposite things. Positive selection: T cells that can bind SELF-MHC survive (needed to be useful). Negative selection: T cells that bind SELF-PEPTIDE:SELF-MHC TOO STRONGLY die (to prevent autoimmunity). Only the narrow middle band survives.

**MHC restriction**: T cells only recognize antigen when it's presented ON MHC of the same species. A human T cell can't recognize influenza peptide floating free — it must see it on human MHC I or II. This is why cross-presentation is important for vaccines: you need antigen inside the MHC pathway, not just floating around.

**CD4 vs. CD8: not just about "helper vs. killer"**: CD4 T cells include Tregs (suppressive), not just helpers. Some CD4 cells are cytotoxic in certain contexts. CD8 cells can also produce cytokines. The CD4/CD8 labels are about co-receptor, which determines MHC class recognition — the functional outcomes are more complex.

**Why 95% of thymocytes die**: The TCR rearrangement is random (→ diversity), but most randomly generated TCRs can't bind self-MHC at all (die in positive selection) or bind too well to self-peptide (die in negative selection). 2–5% survival is normal and sufficient to generate a full T cell repertoire.
