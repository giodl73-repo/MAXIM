# T Cells

## The Big Picture

```
T CELLS: CELLULAR IMMUNITY COORDINATORS AND KILLERS
=====================================================

  TCR DIVERSITY (same combinatorial logic as BCR):
  ┌────────────────────────────────────────────────────────────────┐
  │ α/β TCR (dominant, 95% of circulating T cells):                │
  │   α chain: V (~50) × J (~61) = ~3,050                          │
  │   β chain: V (~54) × D (2) × J (~14) = ~1,512                │
  │   Combinatorial: ~4.6 million                                  │
  │   + Junctional diversity: ~10¹⁸ total                          │
  │                                                                │
  │ γ/δ TCR (5%, mucosal surfaces, skin):                          │
  │   More limited diversity                                       │
  │   Recognize non-peptide antigens (lipids, stress molecules)    │
  │   First responders at epithelial barriers                      │
  └────────────────────────────────────────────────────────────────┘

  T CELL FUNCTIONAL MAP:
  ┌──────────────────────────────────────────────────────────────┐
  │                                                              │
  │  CD4+ T CELLS (helper/coordinator)                           │
  │  ─────────────────────────────────                           │
  │  Recognize: peptide on MHC CLASS II (professional APCs)      │
  │                                                              │
  │  SUBSETS:                                                    │
  │  Th1 ──► macrophage activation + IFN-γ (intracellular bact.) │
  │  Th2 ──► B cell help + IL-4/5/13 (parasites + allergy)       │
  │  Th17 ─► neutrophil recruitment + IL-17 (fungi, extrac. bact)│
  │  Tfh ──► germinal center B cell help + IL-21                 │
  │  Treg ─► suppression + IL-10, TGF-β (tolerance)              │
  │                                                              │
  │  CD8+ T CELLS (cytotoxic)                                    │
  │  ──────────────────────────                                  │
  │  Recognize: peptide on MHC CLASS I (all nucleated cells)     │
  │  Kill: infected cells, tumor cells, allografts               │
  │  Mechanism: Perforin + Granzyme B → target apoptosis         │
  │             FasL:Fas → target apoptosis                      │
  │             Cytokine secretion: IFN-γ, TNF                   │
  └──────────────────────────────────────────────────────────────┘
```

---

## TCR Structure and Signaling

```
  TCR COMPLEX: THE RECOGNITION MACHINE
  ======================================

  TCR HETERODIMER: α chain + β chain (non-covalent)
  ─ Variable domains: VDJ-encoded → antigen recognition
  ─ Constant domains: Cα + Cβ → membrane anchoring
  ─ Short cytoplasmic tails: No signaling capacity

  CD3 COMPLEX (the signaling module):
  TCR is non-covalently associated with CD3 complex:
  CD3γ, CD3δ, CD3ε, CD3ζ (ζ-chain)
  All have ITAMs in cytoplasmic tails

  TCR:CD3 ACTIVATION CASCADE:
  MHC:peptide binds TCR
       │ + CD4 or CD8 (co-receptor) stabilizes complex
       │ Lck (kinase on CD4/CD8 intracellular tail) activated
       │
       ▼ Lck phosphorylates ITAMs on CD3ζ
       │
       ▼ ZAP-70 recruited → phosphorylated by Lck
       │
       ▼ ZAP-70 phosphorylates LAT (scaffold) and SLP-76
       │
       ├──► PLCγ1 → IP3 + DAG
       │       IP3 → ER Ca²⁺ release → CRAC channels → sustained Ca²⁺
       │       Ca²⁺ → calcineurin → NFAT dephosphorylation → nucleus
       │       DAG → PKCθ → IKK → NF-κB
       │
       ├──► Ras → Raf → MEK → ERK → AP-1 transcription
       │
       └──► PI3K → PIP3 → Akt → survival + metabolism
       │
       ▼ DOWNSTREAM GENES:
       IL-2 (autocrine proliferation)
       IL-2R (receptor upregulation)
       Bcl-2 (anti-apoptotic, survival)
       Differentiation transcription factors

  IMMUNOLOGICAL SYNAPSE:
  When T cell contacts APC, receptors and signaling molecules
  reorganize into a structure called the immunological synapse:
  Center (cSMAC): TCR + CD3 + PKCθ (signaling zone)
  Perimeter (pSMAC): LFA-1 + ICAM-1 (adhesion ring)
  This structure sustains signaling and directs secretion
```

---

## CD4 T Helper Subsets

```
  TH DIFFERENTIATION: CONTEXT-DEPENDENT SPECIALIZATION
  ======================================================

  MASTER TRANSCRIPTION FACTOR and CYTOKINE ENVIRONMENT:

  NAIVE CD4 T CELL
       │
       ├── IL-12 + IFN-γ → T-bet TF → TH1
       │
       ├── IL-4 → GATA3 TF → TH2
       │
       ├── TGF-β + IL-6 (+ IL-21, IL-23) → RORγt TF → TH17
       │
       ├── CXCR5 expression + IL-21 → Bcl-6 TF → TFH
       │
       └── TGF-β (alone, no IL-6) → FoxP3 TF → TREG

  TH1 — INTRACELLULAR PATHOGEN IMMUNITY:
  ┌────────────────────────────────────────────────────────────┐
  │ Cytokines produced: IFN-γ (main), TNF, IL-2                │
  │ Effector functions:                                        │
  │   IFN-γ → macrophage "classical activation" (M1)           │
  │   IFN-γ → upregulates MHC I on all cells                   │
  │   IFN-γ → promotes CD8 T cell differentiation              │
  │   IFN-γ → antiviral/antibacterial macrophage killing       │
  │ Pathogens targeted: Mycobacterium tuberculosis, Listeria,  │
  │                     viruses, Leishmania                    │
  │ Disease: Excessive Th1 → autoimmunity (MS, Crohn's)        │
  └────────────────────────────────────────────────────────────┘

  TH2 — ALLERGIC AND ANTIPARASITIC IMMUNITY:
  ┌────────────────────────────────────────────────────────────┐
  │ Cytokines: IL-4, IL-5, IL-13, IL-9                         │
  │ IL-4: B cell class switching → IgE; promotes Th2           │
  │ IL-5: Eosinophil activation and recruitment                │
  │ IL-13: Mucus production, airway smooth muscle contraction  │
  │ Functions: IgE production → mast cell arming               │
  │            Eosinophil activation → antiparasitic           │
  │            Mucus → barrier to expel parasites              │
  │ Pathogens: Helminths (worms)                               │
  │ Disease: Asthma, atopic dermatitis, food allergy           │
  │ Therapy target: Anti-IL-4 (dupilumab), anti-IL-5           │
  │                 (mepolizumab), anti-IgE (omalizumab)       │
  └────────────────────────────────────────────────────────────┘

  TH17 — MUCOSAL AND ANTIFUNGAL IMMUNITY:
  ┌────────────────────────────────────────────────────────────┐
  │ Cytokines: IL-17A, IL-17F, IL-22, IL-21                    │
  │ IL-17: Recruits neutrophils → antimicrobial defense        │
  │ IL-22: Epithelial barrier maintenance + antimicrobial      │
  │ Functions: Antifungal (Candida, Aspergillus defense)       │
  │            Extracellular bacterial defense at barriers     │
  │ Pathogens: Candida, Klebsiella, Staphylococcus             │
  │ Disease: Psoriasis (excess IL-17); IBD; ankylosing spondy  │
  │ Therapy: Anti-IL-17A (secukinumab → psoriasis, AS)       │
  │          Anti-IL-23 (guselkumab → blocks Th17 induction) │
  └────────────────────────────────────────────────────────────┘

  REGULATORY T CELLS (TREG):
  ┌────────────────────────────────────────────────────────────┐
  │ Master TF: FoxP3 (mutations → IPEX syndrome: fatal         │
  │   multi-organ autoimmunity)                                │
  │ Mechanisms of suppression:                                 │
  │   1. IL-10: anti-inflammatory cytokine                     │
  │   2. TGF-β: suppresses effector T cells                  │
  │   3. IL-35: suppressive (minor)                            │
  │   4. CTLA-4 (high on Treg): outcompetes CD28 for B7      │
  │   5. IL-2 consumption: Treg expresses high CD25 (IL-2R)  │
  │      → depletes local IL-2 → starves effector cells      │
  │   6. Direct cytotoxicity: Kill effector T cells via Gzm  │
  │                                                            │
  │ TREG IMPORTANCE:                                           │
  │   Anti-tumor immunity: Tregs in tumor → poor prognosis   │
  │   Transplant tolerance: Treg expansion → graft tolerance   │
  │   Autoimmunity: Treg deficiency → autoimmune disease       │
  └────────────────────────────────────────────────────────────┘
```

---

## CD8 Cytotoxic T Cells

```
  CD8 T CELLS: CELLULAR KILLERS
  ================================

  KILLING MECHANISM 1: Perforin-Granzyme
  ┌────────────────────────────────────────────────────────────┐
  │ CD8 T cell recognizes target via TCR:MHC I interaction     │
  │ Forms immunological synapse with target cell               │
  │                                                            │
  │ Lytic granule exocytosis (polarized toward target):        │
  │   Perforin: oligomerizes in membrane → pore formation      │
  │   Granzyme A, B: enter via perforin pores + mannose-6-P  │
  │                  receptor-mediated endocytosis             │
  │   Granzyme B: cleaves caspase-3 directly → apoptosis     │
  │               cleaves BID → mitochondrial apoptosis        │
  │   Granzyme A: single-strand DNA nicking → apoptosis        │
  │                                                            │
  │ Killing: CD8 kills target in <5 minutes; then moves on   │
  │ Serial killing: One CD8 can kill multiple target cells   │
  └────────────────────────────────────────────────────────────┘

  KILLING MECHANISM 2: FasL-Fas
  CD8 upregulates FasL (CD95L) upon activation
  Targets expressing Fas (CD95) → FasL:Fas → caspase-8 → apoptosis
  Slower than perforin pathway; more relevant in tissue

  KILLING MECHANISM 3: TNF, LTα
  CD8 secretes TNF → TNFR1 on target → apoptosis or NF-κB
  Context-dependent: can kill or can just suppress virus

  CD8 T CELL DIFFERENTIATION STATES:
  ┌────────────────────────────────────────────────────────────┐
  │ Naïve (CD62Lhi CD44lo):   Haven't seen antigen             │
  │                                                            │
  │ Effector (KLRG1hi CD127lo): Acute response                 │
  │   Short-lived; immediate killing capacity                  │
  │   Most die as infection clears (contraction phase)         │
  │                                                            │
  │ Memory precursor (KLRG1lo CD127hi):                        │
  │   Long-lived; rapidly proliferate on re-exposure           │
  │                                                            │
  │ MEMORY SUBSETS:                                            │
  │   TCM (central memory): Secondary lymph organs; fast resp  │
  │   TEM (effector memory): Peripheral tissue; immediate kill │
  │   TRM (tissue-resident): Stays in tissue; first local resp │
  │   TSCM (stem cell memory): Lymph; longest-lived; self-renew│
  │                                                            │
  │ EXHAUSTION: Chronic antigen (tumors, HIV):                 │
  │   Progressive loss of effector function                    │
  │   PD-1hi TOX+ BATF+ → exhausted state                    │
  │   Anti-PD-1 (pembrolizumab) partially reinvigorates        │
  └────────────────────────────────────────────────────────────┘
```

---

## T Cell Exhaustion

```
  T CELL EXHAUSTION: CHRONIC STIMULATION FAILURE
  ================================================

  CONTEXT: Cancer, chronic viral infection (HIV, HCV, HBV)
  CAUSE: Persistent high antigen load

  EXHAUSTION HIERARCHY:
  Progenitor exhausted (Tpex):
    TCF1+ SLAMF6+ PD-1int
    Self-renewing pool; respond to anti-PD-1

  Terminally exhausted (Tex):
    TOX+ PD-1hi TIM-3+ LAG-3+ CD39+
    No self-renewal; proliferative capacity lost
    Even anti-PD-1 only partly restores function

  EXHAUSTION MARKERS (checkpoint receptors):
  PD-1 (programmed death 1): TIM-3, LAG-3, CTLA-4, TIGIT
  Increased inhibitory receptor expression = more exhausted

  THERAPEUTIC IMPLICATIONS:
  Anti-PD-1/PD-L1: Reinvigorates Tpex cells → response
  Response rate limited by: Tex fraction, tumor microenvironment
  Combining checkpoints (anti-PD-1 + anti-LAG-3/TIM-3): Better response
  Anti-CTLA-4 + anti-PD-1 (ipi + nivo): Synergistic but more toxicity
```

---

## T Cell Memory

```
  IMMUNOLOGICAL MEMORY: T CELL PERSISTENCE
  ==========================================

  SIGNALS REQUIRED FOR MEMORY FORMATION:
  1. TCR signal (antigen recognition)
  2. Co-stimulation
  3. Inflammatory cytokines (IL-12, IFN-γ) = Signal 3
  Without Signal 3: CD8 memory forms poorly

  MAINTENANCE:
  Naïve T cells: Require periodic TCR contact with MHC:self-peptide + IL-7
  Memory T cells: Maintained by IL-7 + IL-15 (homeostatic cytokines)
  Antigen-independent survival — memory persists even if pathogen gone

  SECONDARY RESPONSE:
  ─ Memory cells: 100–1000x more precursors than naïve pool
  ─ Lower activation threshold (don't need as much co-stimulation)
  ─ Faster effector differentiation (< 24 hrs vs. 5–7 days)
  ─ Reach target tissues faster (TEM are pre-positioned in tissues)

  QUANTITATIVE EXAMPLE (flu immunity):
  After primary flu infection: 1 in 10⁶ T cells specific for flu
  After primary response peaks: 1 in 1,000 T cells flu-specific
  After contraction: 1 in 10,000 T cells flu-specific (100x more than start)
  After second exposure: 1 in 100 T cells flu-specific within days

  VACCINE DESIGN IMPLICATION:
  Vaccines must drive the memory formation phase.
  Two doses: prime (establish clone) + boost (amplify memory pool)
  Adjuvants: Provide the innate "danger" signals (Signal 3 equivalent)
```

---

## Decision Cheat Sheet

| Goal | Which T Cell |
|------|-------------|
| Kill infected cells (virus/intracellular bacteria) | CD8 cytotoxic T cells |
| Activate macrophages to kill intracellular bacteria | Th1 (IFN-γ) |
| Help B cells make IgE / fight parasites | Th2 (IL-4) |
| Recruit neutrophils to mucosal surface (fungi) | Th17 (IL-17) |
| Help B cells in germinal center (antibody) | Tfh (IL-21) |
| Suppress immune responses | Treg (FoxP3, IL-10, TGF-β) |
| What gets blocked by checkpoint inhibitors? | PD-1 (on T cells) or PD-L1 (on tumor) |
| What is T cell exhaustion? | Chronic antigen → progressive function loss + PD-1 |
| Why is Signal 3 needed? | Inflammatory context ensures CD8 memory |
| What receptor does CTLA-4 compete with? | CD28 (competes for B7 binding) |

---

## T Cell Systems Architecture: Authentication, Synapse, and Exhaustion

```
IMMUNOLOGICAL SYNAPSE ↔ MUTUAL AUTHENTICATION HANDSHAKE
──────────────────────────────────────────────────────────────────────────────
T CELL AUTHENTICATION REQUIREMENTS:
  A T cell activates only when ALL of the following are simultaneously satisfied:

  SIGNAL 1 (antigen specificity):
    TCR must bind the correct peptide:MHC complex
    This is the specific credential check — locks to one peptide-MHC pair
    Neither TCR nor MHC alone is sufficient

  SIGNAL 2 (co-stimulation — context check):
    CD28 must bind B7 (CD80/CD86) on the APC
    B7 is only upregulated on activated, mature APCs
    → Ensures the APC has detected a real threat (PAMP/DAMP present)
    → Prevents activation against self-antigens displayed without danger signals

  SIGNAL 3 (cytokine context — determines differentiation):
    Cytokines (IL-12, IL-4, TGF-β, etc.) in the local environment
    Analogous to: environment variables injected at container startup
    → Same antigen + same co-stimulation → different T cell type depending on context

  SECURITY MODEL:
    Without Signal 2 → T cell anergy (permanent inactivation)
    Without Signal 3 → T cell activates but differentiates poorly
    All three needed → proper activation + correct differentiation

    This is mutual authentication:
    T cell verifies APC (requires specific MHC:peptide + B7)
    APC is only activated when it has detected a genuine PAMP/DAMP
    → Prevents spurious activation against harmless self-antigens

  IMMUNOLOGICAL SYNAPSE = the physical interface assembly:
    cSMAC (central zone): TCR + CD3 + PKCθ (signaling zone)
    pSMAC (perimeter):    LFA-1 + ICAM-1 (adhesion ring, "socket lock")
    Equivalent: TLS mutual authentication + connection establishment
    The synapse concentrates signaling molecules and directs secretion
    toward the target — precisely oriented cytolytic delivery

T CELL EXHAUSTION ↔ THREAD STARVATION / RESOURCE DEPLETION
──────────────────────────────────────────────────────────────────────────────
NORMAL RESPONSE:
  Acute infection → antigen spike → T cell clone expands → clears infection
  → antigen cleared → contraction → memory persists

EXHAUSTION CONTEXT:
  Chronic antigen (tumor, HIV, HCV) → T cells never get "done"
  → Continuous TCR signaling → progressive epigenetic changes → dysfunction

EXHAUSTION AS RESOURCE DEPLETION:
  Normal effector T cell: thread with queue, processes tasks, can dequeue
  Exhausted T cell: thread starved by infinite queue depth that never drains
    → First: effector functions degrade (less IL-2, less proliferation)
    → Then: cytotoxicity reduced (perforin/granzyme lower)
    → Finally: all effector function lost; cell expresses "stop" markers

CHECKPOINT RECEPTORS = RATE LIMITERS IN OVERCROWDED QUEUE:
  PD-1, TIM-3, LAG-3, CTLA-4: All inhibitory receptors
  Upregulated under chronic stimulation
  Evolutionary purpose: prevent immunopathology from unchecked T cell activity
  Cancer exploitation: tumor upregulates PD-L1 → activates rate limiter → T cells idle
  Anti-PD-1 therapy: removes rate limiter → queue can drain → T cells resume killing

PROGENITOR vs. TERMINAL EXHAUSTION:
  Tpex (progenitor): has self-renewal capacity → responds to anti-PD-1
  Tex (terminal): replication blocked, function irreversible lost
  Analogous to: thread pool with warm-standby threads (Tpex recoverable)
                vs. permanently crashed threads (Tex → need new thread)
──────────────────────────────────────────────────────────────────────────────
```

## Common Confusion Points

**CD4 vs. CD8 is about MHC restriction, not function**: CD4 recognizes MHC II (on APCs). CD8 recognizes MHC I (on all cells). Both can kill, both can produce cytokines — but their recognition restriction determines what they monitor. CD8 monitors "what are YOU making?" (your MHC I). CD4 monitors "what have professional APCs found?" (their MHC II).

**Th1/Th2/Th17 differentiation is plastic, not irreversible**: Unlike B cell class switching (irreversible DNA recombination), T cell subset differentiation is largely driven by transcription factors that can be overwritten in different cytokine environments. Some Th17 cells can convert to Th1 under IL-12. Tregs can lose FoxP3 in inflammatory conditions. This plasticity complicates in vivo biology.

**T cell memory requires antigen clearance**: During chronic infection (HIV, some tumors), antigen never clears → T cells never enter memory phase → exhaustion instead. This is fundamentally different from acute infection where pathogen is cleared, effectors die, and a small memory pool persists.

**Co-stimulation blockade in transplant vs. cancer**: Blocking CD28:B7 (belatacept = CTLA-4-Ig) suppresses T cell activation → used to prevent transplant rejection. In cancer, blocking CTLA-4 (which normally competes with CD28) removes the brake → T cells activate more → fight cancer. Same pathway, opposite therapeutic goal.
