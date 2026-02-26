<!-- @editor[bridge/P3]: No CS/engineering analogy bridge — checkpoint inhibitors parallel removing rate limiters on an already-provisioned service; CAR-T parallels hot-patching a running process with a new event handler that bypasses the normal dispatch table (MHC) -->
# Immunotherapy

## The Big Picture

```
CANCER IMMUNOTHERAPY: USING THE IMMUNE SYSTEM TO FIGHT CANCER
===============================================================

  WHY CANCER ESCAPES IMMUNITY (the problem):
  ┌────────────────────────────────────────────────────────────────┐
  │  NORMAL                         CANCER                        │
  │  MHC I displays self-peptides   MHC I downregulated           │
  │  No co-stimulation → T cell     PD-L1 upregulated → T exhaustion│
  │   ignored                        Tregs recruited to tumor      │
  │  No "eat me" signal             MDSCs suppress T cells         │
  │                                  IDO: Trp depletion → anergy  │
  │                                  TGF-β: anti-inflammatory      │
  └────────────────────────────────────────────────────────────────┘

  IMMUNOTHERAPY APPROACHES:
  ┌──────────────────────────────────────────────────────────────────┐
  │ CHECKPOINT INHIBITORS                                             │
  │   Remove the brakes on T cells                                   │
  │   Anti-PD-1/PD-L1, anti-CTLA-4, anti-LAG-3, anti-TIM-3        │
  │                                                                   │
  │ CELL THERAPIES                                                    │
  │   Engineer patient's own immune cells                           │
  │   CAR-T cells, TIL therapy, CAR-NK                              │
  │                                                                   │
  │ BISPECIFIC ANTIBODIES                                            │
  │   Physically bring T cells to tumor cells                       │
  │   CD3 × tumor antigen                                           │
  │                                                                   │
  │ CANCER VACCINES                                                  │
  │   Elicit tumor-specific T cells                                  │
  │   Neoantigen vaccines (personalized); off-the-shelf             │
  │                                                                   │
  │ CYTOKINE THERAPY                                                 │
  │   IL-2, IFN-α (older), IL-15, IL-21 (newer)                    │
  │                                                                   │
  │ ONCOLYTIC VIRUSES                                                │
  │   Viruses that selectively replicate in cancer cells             │
  │   T-VEC (talimogene laherparepvec): Herpes-based, melanoma      │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Checkpoint Inhibitors

```
  PD-1/PD-L1 AXIS: THE PRIMARY TUMOR CHECKPOINT
  ================================================

  PD-1 (Programmed Death 1):
  ─ Receptor on T cells (upregulated after activation)
  ─ Ligands: PD-L1 (CD274) and PD-L2 (CD273)
  ─ PD-1:PD-L1 → ITIM + ITSM in PD-1 cytoplasmic tail
    → SHP-2 phosphatase → dephosphorylate TCR signaling molecules
    → T cell exhaustion/inhibition

  TUMOR PD-L1 EXPRESSION:
  ─ Many tumors upregulate PD-L1 (driven by IFN-γ in tumor microenv.)
  ─ PD-L1+ tumor: More likely to respond to anti-PD-1/PD-L1
  ─ But response correlation is imperfect (even PD-L1- can respond)

  ANTI-PD-1 DRUGS:
  ┌────────────────────────────────────────────────────────────────┐
  │ Pembrolizumab (Keytruda): anti-PD-1 IgG4                     │
  │   ~30+ FDA approvals across cancer types                      │
  │   First pan-tumor approval: MSI-H/dMMR (any solid tumor)     │
  │   TMB-H (tumor mutational burden high) approval              │
  │                                                                 │
  │ Nivolumab (Opdivo): anti-PD-1 IgG4                           │
  │   Melanoma, NSCLC, RCC, HCC, gastric, cervical, more         │
  │   Combined with ipilimumab: "ipi+nivo" combination standard  │
  │                                                                 │
  │ Cemiplimab (Libtayo): anti-PD-1                               │
  │   CSCC (cutaneous squamous cell carcinoma) as primary         │
  └────────────────────────────────────────────────────────────────┘

  ANTI-PD-L1 DRUGS:
  Atezolizumab (Tecentriq): NSCLC, urothelial, TNBC
  Durvalumab (Imfinzi): NSCLC, biliary, HCC
  Avelumab (Bavencio): Merkel cell carcinoma, urothelial

  ANTI-CTLA-4: IPILIMUMAB
  ┌────────────────────────────────────────────────────────────────┐
  │ CTLA-4 mechanism:                                              │
  │   CTLA-4 expressed on activated T cells + Tregs              │
  │   Higher affinity for B7 than CD28 → competes                │
  │   CTLA-4:B7 → removes B7 from APC surface (trans-endocytosis)│
  │   → other T cells can't get CD28 signal → dampened response  │
  │                                                                 │
  │ Ipilimumab (Yervoy): First checkpoint inhibitor (2011)       │
  │   Melanoma (monotherapy or with nivolumab)                    │
  │   Higher toxicity than anti-PD-1 alone                       │
  │   Combination ipi+nivo: better response but more side effects │
  │                                                                 │
  │ Tremelimumab (Imjudo): anti-CTLA-4                           │
  │   Combined with durvalumab (anti-PD-L1) → HCC, NSCLC        │
  └────────────────────────────────────────────────────────────────┘

  NEXT-GENERATION CHECKPOINTS:
  <!-- @editor[content/P2]: Typo — "approal" should be "approval" -->
  Anti-LAG-3 (relatlimab): First LAG-3 approal combined with nivo
  Anti-TIM-3: Phase II/III trials for several tumors
  Anti-TIGIT (vibostolimab, tiragolumab): Active development
  Anti-VISTA, anti-NKG2A: Earlier development

  IMMUNE-RELATED ADVERSE EVENTS (irAEs):
  ┌────────────────────────────────────────────────────────────────┐
  │ Mechanism: Checkpoint inhibitors remove tolerance constraints  │
  │   → T cells attack normal tissues                             │
  │                                                                 │
  │ COMMON:                                                        │
  │ Dermatitis (rash): Very common (30–50% with CTLA-4)          │
  │ Thyroiditis (hypothyroidism): Common with PD-1 (5–10%)       │
  │ Pneumonitis: 5% with PD-1; potentially life-threatening       │
  │ Hepatitis: CTLA-4 > PD-1                                     │
  │ Colitis: CTLA-4 > PD-1 (grade 3–4: ~15% with ipi)          │
  │                                                                 │
  │ MANAGEMENT:                                                    │
  │ Grade 1: Continue, monitor                                    │
  │ Grade 2: Hold checkpoint; oral steroids                       │
  │ Grade 3–4: Permanently discontinue; high-dose IV steroids    │
  │            Infliximab for steroid-refractory colitis          │
  └────────────────────────────────────────────────────────────────┘
```

---

## CAR-T Cell Therapy

```
  CAR-T: GENETICALLY ENGINEERED T CELL THERAPY
  ================================================

  CONCEPT: Retarget patient's T cells to recognize tumor antigen
           using an artificially constructed receptor (CAR).
           Connects T cell killing machinery to ANY antigen,
           bypassing MHC restriction requirement.

  CAR STRUCTURE:
  ┌────────────────────────────────────────────────────────────────┐
  │                                                                 │
  │  EXTRACELLULAR                INTRACELLULAR                    │
  │  ─────────────                ─────────────                   │
  │  scFv (antibody fragment)     CD3ζ (ITAM signaling)           │
  │  binds tumor antigen          + Co-stimulatory domains         │
  │  (no MHC needed!)             CD28 or 4-1BB or both           │
  │       │                                                         │
  │  Hinge (spacer)                                                │
  │       │                                                         │
  │  Transmembrane domain                                           │
  │       │                                                         │
  │  ─────┼─────────────────────────────────────────────────────  │
  │       │ PLASMA MEMBRANE                                         │
  └────────────────────────────────────────────────────────────────┘

  CAR GENERATIONS:
  1st gen: CD3ζ only — poor persistence
  2nd gen: CD3ζ + one co-stimulatory (CD28 or 4-1BB) — current standard
  3rd gen: CD3ζ + two co-stimulatory — mixed results
  4th gen (TRUCK): Also encode secreted cytokine (IL-12) — "armored CAR"

  MANUFACTURING PROCESS (ex vivo gene engineering):
  ┌────────────────────────────────────────────────────────────────┐
  │ 1. Leukapheresis: Collect patient T cells from blood          │
  │ 2. T cell stimulation: Activate with anti-CD3/anti-CD28 beads │
  │ 3. Viral transduction: Lentivirus or retrovirus delivers CAR  │
  │    gene into T cell genome → stable expression                │
  │ 4. Expansion: ~2 weeks in cytokine-supplemented media         │
  │ 5. Quality control: CAR expression, potency, sterility        │
  │ 6. Infusion: Patient receives lymphodepleting chemo first     │
  │    (cyclophosphamide + fludarabine → creates space for CAR-T) │
  │ 7. CAR-T infused → encounters antigen → expand and kill      │
  └────────────────────────────────────────────────────────────────┘

  CONNECTION TO CRISPR (→ genomics/07-CRISPR.md):
  CAR-T engineering increasingly uses CRISPR:
  ─ Knock out PD-1 (less exhaustion)
  ─ Knock out TCR (for allogeneic "off-the-shelf" CAR-T)
  ─ Knock out HLA-A/B (reduce graft rejection)
  ─ Knock in CAR at safe harbor locus (TRAC site)

  APPROVED CAR-T THERAPIES (as of 2024):
  ┌────────────────────────────────────────────────────────────────┐
  │ Tisagenlecleucel (Kymriah): CD19 CAR; B-ALL, DLBCL           │
  │ Axicabtagene ciloleucel (Yescarta): CD19 CAR; DLBCL, FL      │
  │ Lisocabtagene maraleucel (Breyanzi): CD19 CAR; DLBCL          │
  │ Brexucabtagene autoleucel (Tecartus): CD19 CAR; MCL, B-ALL  │
  │ Idecabtagene vicleucel (Abecma): BCMA CAR; multiple myeloma  │
  │ Ciltacabtagene autoleucel (Carvykti): BCMA CAR; myeloma      │
  └────────────────────────────────────────────────────────────────┘

  CAR-T TOXICITIES:
  Cytokine Release Syndrome (CRS): T cell explosion → cytokine storm
    → fever, hypotension, hypoxia; tocilizumab treatment
  Immune Effector Cell-Associated Neurotoxicity Syndrome (ICANS):
    → encephalopathy, seizures; dexamethasone treatment
  Cytopenias: Lymphodepletion + immune activation → prolonged neutropenia
  On-target off-tumor: If antigen on normal tissues (CD19 → kills all B cells)
```

---

## Bispecific Antibodies

```
  BISPECIFIC ANTIBODIES: REDIRECTING T CELLS
  ============================================

  CONCEPT: Engineer one antibody to bind TWO DIFFERENT antigens:
  Arm 1: CD3ε on T cell (activates T cell)
  Arm 2: Tumor-associated antigen (targets cancer cell)

  MECHANISM:
  ┌────────────────────────────────────────────────────────────┐
  │  Bispecific antibody physically bridges:                   │
  │                                                             │
  │  T cell ─── [CD3 arm] ─── Bispecific ─── [TAA arm] ─── Tumor│
  │                                                             │
  │  Creates "immunological synapse" between T cell and tumor  │
  │  TCR not involved → bypasses MHC restriction              │
  │  Any T cell can be redirected (not antigen-specific)       │
  │  → Very fast cytotoxicity (minutes)                        │
  └────────────────────────────────────────────────────────────┘

  APPROVED BISPECIFICS:
  ┌────────────────────────────────────────────────────────────────┐
  │ Blinatumomab (Blincyto): CD19×CD3 BiTE format               │
  │   First approved T cell engager (2014)                       │
  │   B-ALL, CLL; continuous IV infusion (short half-life)       │
  │                                                                 │
  │ Catumaxomab: anti-EpCAM × anti-CD3 × Fc binding to APC     │
  │   Malignant ascites (Europe, withdrawn; EU)                  │
  │                                                                 │
  │ Mosunetuzumab (Lunsumio): CD20×CD3                          │
  │   Follicular lymphoma (approved 2022)                        │
  │                                                                 │
  │ Talquetamab (Talvey): GPRC5D×CD3                            │
  │   Multiple myeloma (approved 2023)                           │
  │                                                                 │
  │ Teclistamab (Tecvayli): BCMA×CD3                            │
  │   Multiple myeloma (approved 2022)                           │
  └────────────────────────────────────────────────────────────────┘

  ADVANTAGES OVER CAR-T:
  ─ Off-the-shelf (no patient-specific manufacturing)
  ─ Engages ALL T cells (including memory, naïve)
  ─ Reversible (stop infusion → activity fades)

  DISADVANTAGES vs. CAR-T:
  ─ Requires continuous infusion (short half-life BiTEs)
  ─ Less potent for large tumor burdens
  ─ CRS also occurs (usually less severe than CAR-T)
```

---

## Tumor Microenvironment (TME)

```
  TUMOR MICROENVIRONMENT: WHY IMMUNOTHERAPY FAILS
  ==================================================

  The tumor is not just cancer cells — it's a complex ecosystem:

  ┌────────────────────────────────────────────────────────────────┐
  │  CELLULAR COMPONENTS:                                           │
  │                                                                  │
  │  Cancer cells: Express neoantigens, downregulate MHC I,        │
  │               upregulate PD-L1, secrete TGF-β                  │
  │                                                                  │
  │  Tumor-associated macrophages (TAMs):                           │
  │    M2-polarized → IL-10, TGF-β, VEGF (pro-tumor)               │
  │    Target: CSF1R inhibitors to deplete M2 TAMs                 │
  │                                                                  │
  │  MDSCs (Myeloid-derived suppressor cells):                     │
  │    Immature myeloid cells → IDO, arginase, ROS suppression    │
  │    Deplete L-arginine → T cells can't make TCR ζ-chain         │
  │                                                                  │
  │  Tregs:                                                         │
  │    Recruited via CCR4 (CCL17/22 from tumor)                   │
  │    Consume IL-2 → starve effector T cells                     │
  │    Target: Anti-CCR4 (mogamulizumab) depletes tumor Tregs     │
  │                                                                  │
  │  Tumor-infiltrating lymphocytes (TILs):                        │
  │    CD8+ TIL density: strong predictor of survival             │
  │    Exhausted state (PD-1hi TOX+): limited killing potential    │
  │                                                                  │
  │  PHYSICAL BARRIERS:                                             │
  │    Desmoplastic stroma (pancreatic cancer) → T cell exclusion  │
  │    Abnormal vasculature → poor T cell trafficking              │
  │    Hypoxia → immunosuppressive M2 polarization                 │
  └────────────────────────────────────────────────────────────────┘

  BIOMARKERS PREDICTING CHECKPOINT RESPONSE:
  ─ PD-L1 expression (IHC): Imperfect but used for treatment eligibility
  ─ TMB (tumor mutational burden): More neoantigens → better response
  ─ MSI-H/dMMR: Best predictor; pan-cancer pembrolizumab approval
  ─ TIL density: High TIL → better response
  ─ CXCL13: T follicular helper marker → response to checkpoint
  ─ IFN-γ gene signature: "Inflamed" vs. "desert" vs. "excluded" TME
```

---

## Decision Cheat Sheet

| Scenario | Approach |
|----------|---------|
| MSI-H/dMMR solid tumor | Pembrolizumab (pan-tumor approval) |
| Melanoma (first line) | Nivolumab ± ipilimumab or pembrolizumab |
| PD-L1 high NSCLC | Pembrolizumab monotherapy |
| Relapsed/refractory B-ALL | Blinatumomab (CD19×CD3) or CAR-T |
| Relapsed/refractory DLBCL | Anti-CD19 CAR-T (axicabtagene) |
| Multiple myeloma (relapsed) | BCMA CAR-T or BCMA×CD3 bispecific |
| CRS after CAR-T | Tocilizumab (anti-IL-6R) |
| irAE (immune colitis grade 3) | Discontinue checkpoint; IV steroids; infliximab |
| Checkpoint toxicity in MS patient | Avoid checkpoint inhibitors (demyelination risk) |
| Allogeneic off-the-shelf CAR-T | CRISPR-edited (TCR KO + HLA KO) + CAR knock-in |

---

## Common Confusion Points

**Checkpoint inhibitors work by removing brakes, not adding accelerators**: Anti-PD-1 does not directly stimulate T cells. It removes an inhibitory signal that was blocking existing tumor-reactive T cells. If there are no tumor-reactive T cells (immunological desert tumor), checkpoint inhibitors don't work — there's nothing to remove the brake from.

**CAR-T bypasses MHC, checkpoint inhibitors don't**: CAR-T cells use a synthetic receptor that directly recognizes antigen on the tumor cell surface — no MHC presentation needed. This is the advantage. Checkpoint inhibitors enhance endogenous T cells that DO need MHC I presentation. Tumors that downregulate MHC I escape checkpoint inhibitors but may be susceptible to CAR-T (if antigen is still surface-accessible).

**CD4 T cells matter for checkpoint response**: Most of the checkpoint inhibitor story is told in terms of CD8 T cells killing tumors. But CD4 T cells are critical for CD8 maintenance, tumor recognition, and macrophage activation. Tumors with defective MHC II and no CD4 T cell infiltration respond poorly.

**On-target off-tumor toxicity**: CAR-T targeting CD19 eliminates ALL B cells (tumor + normal) → B cell aplasia → patients need IVIG for life. This is acceptable for leukemia. Targeting ubiquitous antigens (like carbonic anhydrase IX on renal cell carcinoma) would also hit liver, causing hepatotoxicity — requires very careful target selection.
