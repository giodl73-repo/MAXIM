# Cytokines and Immune Signaling

## The Big Picture

```
CYTOKINES: THE SIGNALING NETWORK OF IMMUNITY
==============================================

  FRAMING: Cytokines are the messaging protocol of the immune system.
  Each cytokine = a typed message (IL-6, TNF, IFN-γ...)
  Each receptor = a handler with defined downstream logic
  Signal transduction = the event handler execution
  JAK-STAT = the canonical signal processing pipeline
  NF-κB = the inflammatory transcription master regulator

  CYTOKINE CLASSES:
  ┌──────────────────────────────────────────────────────────────┐
  │ INTERLEUKINS (IL-1 through IL-38)                            │
  │   Originally "between leukocytes" but also from other cells  │
  │   Each numbered in order of discovery                        │
  │                                                               │
  │ INTERFERONS (IFN)                                            │
  │   Type I: IFN-α, IFN-β (antiviral; all nucleated cells)     │
  │   Type II: IFN-γ (immune activation; T cells + NK cells)    │
  │   Type III: IFN-λ (antiviral; mucosal/epithelial)           │
  │                                                               │
  │ TUMOR NECROSIS FACTOR (TNF) SUPERFAMILY                     │
  │   TNF, LTα, RANKL, BAFF, APRIL, FasL, TRAIL                │
  │   25 ligands → 29 receptors; diverse effects                 │
  │                                                               │
  │ CHEMOKINES (~50 members)                                     │
  │   Chemoattractants: direct cell migration                    │
  │   CXC, CC, C, CX3C subfamilies by cysteine pattern          │
  │                                                               │
  │ COLONY-STIMULATING FACTORS (CSFs)                           │
  │   G-CSF, M-CSF, GM-CSF: control myeloid differentiation    │
  │   Used clinically to boost neutrophil counts post-chemo     │
  │                                                               │
  │ TRANSFORMING GROWTH FACTORS (TGF)                           │
  │   TGF-β: Pleotropic; suppressive in immune context         │
  └──────────────────────────────────────────────────────────────┘

  CYTOKINE COMMUNICATION MODES:
  Autocrine:   Cell signals to itself (IL-2 → T cell self-stimulation)
  Paracrine:   Signals to nearby cells (IL-12 from DC → T cell)
  Endocrine:   Systemic (IL-6 → liver → acute-phase proteins)
  Juxtacrine:  Membrane-bound ligand, requires contact (TNF, FasL)
```

---

## JAK-STAT Signaling

```
  JAK-STAT: THE CANONICAL CYTOKINE SIGNAL TRANSDUCTION PATHWAY
  ==============================================================

  ANALOGY: Like an event-driven webhook system:
  ─ Cytokine = the HTTP request
  ─ Receptor = the endpoint URL
  ─ JAK activation = request preprocessing
  ─ STAT phosphorylation = payload transformation
  ─ Gene transcription = the downstream handler logic

  ARCHITECTURE:
  ┌────────────────────────────────────────────────────────────────┐
  │  EXTRACELLULAR                                                  │
  │      Cytokine (e.g., IFN-γ)                                    │
  │           │                                                     │
  │  ─────────┼──────────────── MEMBRANE ──────────────────────── │
  │           │                                                     │
  │      Receptor dimerization (IFNγR1 + IFNγR2)                  │
  │           │                                                     │
  │      JAK1  JAK2 (associated with receptor chains)              │
  │      (pre-bound to receptor intracellular domains)             │
  │           │ trans-phosphorylation activates JAKs               │
  │           ▼                                                     │
  │      STAT protein phosphorylation (STAT1 for IFN-γ)           │
  │      STAT dimer formation                                      │
  │           │                                                     │
  │  ─────────┼──────────────── NUCLEUS ──────────────────────── │
  │           ▼                                                     │
  │      pSTAT dimer binds GAS elements                           │
  │      → ISG (interferon-stimulated gene) transcription          │
  └────────────────────────────────────────────────────────────────┘

  JAK-STAT SPECIFICITY TABLE:
  ┌────────────────────────────────────────────────────────────────┐
  │ Cytokine     │ JAKs used    │ STAT activated │ Effect         │
  ├──────────────┼──────────────┼────────────────┼────────────────┤
  │ IFN-α/β     │ JAK1, TYK2  │ STAT1, STAT2   │ Antiviral ISGs │
  │ IFN-γ       │ JAK1, JAK2  │ STAT1          │ MHC↑, Th1      │
  │ IL-2        │ JAK1, JAK3  │ STAT5          │ T cell prolif. │
  │ IL-4        │ JAK1, JAK3  │ STAT6          │ Th2, IgE       │
  │ IL-6        │ JAK1, JAK2  │ STAT3          │ Acute phase    │
  │ IL-12       │ JAK2, TYK2  │ STAT4          │ Th1, NK activ. │
  │ IL-21       │ JAK1, JAK3  │ STAT3          │ Tfh, GC        │
  │ GM-CSF      │ JAK2        │ STAT5          │ Myeloid diff.  │
  └────────────────────────────────────────────────────────────────┘

  JAK INHIBITORS (targeted immunosuppression):
  Tofacitinib: JAK1/3 inhibitor → RA, UC, psoriatic arthritis
  Baricitinib: JAK1/2 inhibitor → RA, COVID-19 cytokine storm
  Ruxolitinib: JAK1/2 inhibitor → myelofibrosis, GVHD
  Upadacitinib: Selective JAK1 → RA, UC, atopic dermatitis

  JAK inhibitors are orally bioavailable (vs. injectable biologics)
  → approved for many autoimmune diseases; increasing market share
```

---

## NF-κB Signaling

```
  NF-κB: THE MASTER INFLAMMATORY TRANSCRIPTION FACTOR
  =====================================================

  Five family members: RelA (p65), RelB, c-Rel, p50, p52
  Most common form: p65/p50 heterodimer

  RESTING STATE:
  IκB (inhibitor of κB) retains NF-κB in cytoplasm → inactive

  CANONICAL PATHWAY (TLR, TNF, IL-1R):
  ┌────────────────────────────────────────────────────────────┐
  │ LPS → TLR4 → MyD88 → IRAK1/4 → TRAF6                    │
  │ TNF → TNFR1 → TRADD → RIP1 → TRAF2                      │
  │ IL-1 → IL-1R → MyD88 → IRAK1/4 → TRAF6                  │
  │                  │                                         │
  │                  ▼                                         │
  │             IKK complex (IKKα + IKKβ + NEMO)             │
  │                  │ phosphorylates IκB                     │
  │                  ▼                                         │
  │         IκB → polyubiquitinated → 26S proteasome          │
  │                  │                                         │
  │                  ▼                                         │
  │         NF-κB freed → nuclear translocation               │
  │                  │                                         │
  │                  ▼                                         │
  │         κB element binding → gene transcription           │
  │                                                             │
  │ GENES ACTIVATED:                                           │
  │   TNF, IL-6, IL-1β, IL-12 (proinflammatory cytokines)    │
  │   COX-2 (prostaglandin synthesis)                          │
  │   iNOS (nitric oxide synthesis)                            │
  │   ICAM-1, VCAM-1 (adhesion molecules)                     │
  │   Bcl-2, Bcl-xL (anti-apoptotic)                         │
  └────────────────────────────────────────────────────────────┘

  NON-CANONICAL PATHWAY (LTβR, BAFF-R, CD40):
  NIK (NF-κB inducing kinase) → IKKα → p100 → p52 + RelB
  Regulates: Lymph organ development, B cell survival, Treg

  THERAPEUTIC TARGET:
  Corticosteroids (dexamethasone): Upregulate IκBα → retain NF-κB
  → broad anti-inflammatory
  Direct IKK inhibitors: Being studied but complex toxicity
```

---

## Key Cytokines in Detail

### Interleukins

```
  KEY INTERLEUKINS
  =================

  IL-1β: Pyrogenic + inflammatory
  ─ Source: Macrophages (NLRP3 inflammasome)
  ─ Effects: Fever (hypothalamic PGE₂); IL-6 induction
  ─ Blocks: Anakinra (IL-1R antagonist) → RA, gout, CAPS
  ─ Selective IL-1β block: Canakinumab → recurrent pericarditis, MAS

  IL-2: T cell proliferation
  ─ Source: Activated T cells (autocrine)
  ─ Receptor: IL-2R (CD25/CD122/CD132 heterotrimer) on T cells
  ─ High-affinity IL-2R (CD25) = on activated T cells + Tregs
  ─ Clinical: High-dose IL-2 → cancer immunotherapy (side effects severe)
  ─ Low-dose IL-2: Selective Treg expansion → autoimmune disease trials

  IL-4: Th2 and IgE
  ─ Source: Th2 cells, mast cells, basophils
  ─ Effects: B cell class switch → IgE; Th2 differentiation
  ─ Block: Dupilumab (anti-IL-4Rα → blocks IL-4 + IL-13)
  ─ Indication: Atopic dermatitis, asthma, CRS with nasal polyps

  IL-5: Eosinophil survival
  ─ Source: Th2 cells
  ─ Effects: Eosinophil differentiation + survival
  ─ Block: Mepolizumab, reslizumab → severe eosinophilic asthma

  IL-6: Acute phase + pleiotropic
  ─ Source: Macrophages, DCs, stromal cells
  ─ Effects: Liver → acute-phase proteins (CRP, fibrinogen)
             Hypothalamus → fever; T cell → Th17 differentiation
             B cell → plasma cell differentiation
  ─ Block: Tocilizumab (anti-IL-6R) → RA, cytokine release syndrome
  ─ Clinical importance: IL-6 levels predict COVID-19 severity

  IL-10: Anti-inflammatory
  ─ Source: Macrophages, Tregs, Th2, exhausted T cells
  ─ Effects: Inhibits macrophage activation → TNF, IL-12, IL-6↓
             Promotes B cell survival and Ig secretion
  ─ Dual role: Anti-inflammatory but also helps tumor immune evasion

  IL-12: Th1 polarizing
  ─ Source: DCs and macrophages (in response to bacteria)
  ─ Effects: IFN-γ induction from T cells + NK cells
             Th1 polarization (via STAT4)
  ─ Block: Anti-p40 subunit: ustekinumab → psoriasis, Crohn's
           (blocks IL-12 AND IL-23 since they share p40 subunit)

  IL-17A: Neutrophil mobilizer
  ─ Source: Th17, ILC3, γδ T cells
  ─ Effects: IL-8 (CXCL8) production → neutrophil recruitment
             G-CSF → neutrophil production in bone marrow
  ─ Block: Secukinumab (anti-IL-17A) → psoriasis, AS, PsA
           Ixekizumab → similar indications

  IL-23: Th17 maintenance
  ─ Source: DCs, macrophages
  ─ Effects: Maintains Th17 cells in tissue (after differentiation)
  ─ Block: Risankizumab (anti-p19, IL-23 specific) → psoriasis, IBD
           Guselkumab, mirikizumab → similar

  IL-33: Alarmin / DAMP
  ─ Source: Epithelial cells (released on damage/allergen)
  ─ Receptor: ST2 on mast cells, ILC2s, Th2 cells
  ─ Effects: Activates type 2 response; ILC2 → IL-5/13
  ─ Block: Itepekimab → asthma; tezepelumab (anti-TSLP, upstream)
```

---

## Interferons

```
  INTERFERON BIOLOGY
  ===================

  TYPE I INTERFERONS (IFN-α/β): ANTIVIRAL STATE
  ┌────────────────────────────────────────────────────────────────┐
  │ INDUCTION:                                                      │
  │ Viral dsRNA → RIG-I/MDA5 → MAVS → IRF3/7 → IFN-β gene       │
  │ Viral DNA → cGAS → STING → TBK1 → IRF3 → IFN-β gene          │
  │ Viral ssRNA → TLR7/8 (endosomal) → IRF7 → IFN-α              │
  │                                                                  │
  │ AUTOCRINE + PARACRINE SIGNALING:                                │
  │ IFN-β secreted → binds IFNAR1/2 on same + neighbor cells      │
  │ → JAK1/TYK2 → STAT1/STAT2 → ISGF3 complex                    │
  │ → Hundreds of ISGs (Interferon-Stimulated Genes)               │
  │                                                                  │
  │ ANTIVIRAL MECHANISMS:                                           │
  │   PKR: Phosphorylates eIF2α → translation shutdown             │
  │   OAS/RNase L: Degrades viral RNA                              │
  │   Mx1/Mx2: GTPases that interfere with viral replication      │
  │   TRIM5α: Restriction factor for retroviruses                  │
  │   APOBEC3G: Mutates HIV reverse transcript                     │
  │   Tetherin (BST-2): Tethers enveloped viruses to cell surface  │
  └────────────────────────────────────────────────────────────────┘

  TYPE II INTERFERON (IFN-γ): IMMUNE ACTIVATION
  ┌────────────────────────────────────────────────────────────────┐
  │ SOURCE: CD4+ Th1 cells, CD8+ T cells, NK cells                 │
  │ RECEPTOR: IFNγR1/IFNγR2 → JAK1/JAK2 → STAT1 homodimer        │
  │ → GAS element binding                                          │
  │                                                                  │
  │ EFFECTS (immunological, not directly antiviral):               │
  │   Macrophage M1 activation → iNOS, ROS, phagocytosis          │
  │   MHC I and II upregulation on all cells                       │
  │   Antigen processing: TAP, LMP2/7 (proteasome subunits) ↑     │
  │   Th1 polarization (positive feedback via STAT4)               │
  │   B cell class switching → IgG2a (mouse) / IgG1,3 (human)    │
  └────────────────────────────────────────────────────────────────┘

  THERAPEUTIC INTERFERONS:
  IFN-α: Former standard for HCV and HBV; largely replaced by DAAs
  IFN-β: Multiple sclerosis (reduces relapse rate by ~30%)
  IFN-γ: Chronic granulomatous disease (augments neutrophil killing)
```

---

## TNF/TNFR Superfamily

```
  TNF AND ITS CLINICAL BLOCKADE
  ================================

  TNF (Tumor Necrosis Factor):
  ─ Primarily: Macrophages, DCs in response to LPS/PAMPs
  ─ Form: Membrane-bound + soluble (cleaved by TACE/ADAM17)
  ─ Receptors: TNFR1 (all cells) and TNFR2 (immune cells)

  TNFR1 SIGNALING:
  ┌────────────────────────────────────────────────────────────┐
  │ TNFR1 + TNF → TRADD → TRAF2 + RIP1                       │
  │                │                │                           │
  │                ▼                ▼                           │
  │             NF-κB            Caspase-8                     │
  │          (survival,         (apoptosis)                     │
  │           inflammation)                                     │
  │                                                             │
  │ Which pathway?                                             │
  │ NF-κB active (inflammation) → survival genes               │
  │ NF-κB inactive → apoptosis                                 │
  │ RIP1 inhibitor → RIPK3 → necroptosis (if caspase blocked)  │
  └────────────────────────────────────────────────────────────┘

  TNF BLOCKING DRUGS (anti-TNF biologics):
  ┌────────────────────────────────────────────────────────────────┐
  │ Infliximab (Remicade): chimeric anti-TNF mAb                  │
  │ Adalimumab (Humira): fully human anti-TNF mAb                 │
  │   → World's best-selling drug for years (~$20B/yr peak)       │
  │ Etanercept: TNFR2-Fc fusion protein (decoy receptor)          │
  │ Certolizumab: PEGylated anti-TNF Fab (no ADCC, no FcRn)      │
  │                                                                 │
  │ INDICATIONS: RA, psoriasis, psoriatic arthritis, AS, IBD,     │
  │              juvenile idiopathic arthritis, uveitis            │
  │                                                                 │
  │ SIDE EFFECTS:                                                  │
  │   Infections (especially TB reactivation — screen first!)     │
  │   Lymphoma risk (small increase)                              │
  │   Demyelination (MS-like) — contraindicated in MS            │
  └────────────────────────────────────────────────────────────────┘
```

---

## Chemokines

```
  CHEMOKINES: DIRECTIONAL CELL MIGRATION
  =========================================

  FUNCTION: Gradient-directed migration (chemotaxis)
  Cell at low [chemokine] → moves toward high [chemokine]
  Critical for: Leukocyte recruitment to infection sites

  NOMENCLATURE:
  CC chemokines: Adjacent cysteines (e.g., CCL2, CCL5)
  CXC chemokines: One amino acid between cysteines (e.g., CXCL8)
  CX3C: Three amino acids between (e.g., CX3CL1/Fractalkine)

  KEY CHEMOKINES:
  ┌──────────────────────────────────────────────────────────────┐
  │ CXCL8 (IL-8): Neutrophil chemoattractant — bacterial infec. │
  │                                                               │
  │ CCL2 (MCP-1): Monocyte + DC chemotactic — chronic inflam.   │
  │                                                               │
  │ CXCL10 (IP-10): T cell + NK chemoattractant (IFN-γ-induced) │
  │                                                               │
  │ CCL5 (RANTES): T cell + eosinophil + DC recruitment          │
  │                                                               │
  │ CXCL12 (SDF-1): Bone marrow homing + HSC retention         │
  │   CXCR4 receptor: Used by HIV-1 as co-receptor              │
  │                                                               │
  │ CCL19/CCL21: T cell homing to lymph nodes (via CCR7)        │
  │              Expressed by lymph node stromal cells            │
  │                                                               │
  │ CXCL13: B cell homing to B cell follicles (via CXCR5)      │
  └──────────────────────────────────────────────────────────────┘

  THERAPEUTIC: CCR5 blockers
  CCR5 = co-receptor for HIV-1 entry
  Maraviroc (CCR5 antagonist): HIV-1 entry blocker
  CCR5Δ32 homozygotes: Naturally resistant to R5-tropic HIV
  Berlin Patient (Timothy Ray Brown): Cured of HIV after receiving
  CCR5Δ32 stem cell transplant (2008)
```

---

## Cytokine Storm

```
  CYTOKINE STORM: SELF-AMPLIFYING INFLAMMATION
  ==============================================

  MECHANISM:
  ┌────────────────────────────────────────────────────────────────┐
  │  Trigger: Infection, CAR-T infusion, sepsis, hemophagocytic   │
  │                                                                 │
  │  Macrophage activation → TNF, IL-6, IL-1β                    │
  │            │                                                   │
  │            ▼ (positive feedback loop)                         │
  │  More immune cell activation → more macrophages               │
  │  More cytokines → more activation                             │
  │            │                                                   │
  │            ▼ SYSTEMIC EFFECTS                                  │
  │  Fever, hypotension, capillary leak → shock                  │
  │  Liver: Ferritin production (hyperferritinemia)               │
  │  Blood: DIC (disseminated intravascular coagulation)          │
  │  Organs: Multi-organ failure (ARDS, AKI, cardiac)            │
  └────────────────────────────────────────────────────────────────┘

  TREATMENT OF CYTOKINE STORM:
  Tocilizumab (anti-IL-6R): Approved for CRS after CAR-T; COVID-19
  Dexamethasone: Suppresses NF-κB → corticosteroid
  Anakinra (anti-IL-1R): For hemophagocytic lymphohistiocytosis
  Ruxolitinib (JAK1/2 inhibitor): For steroid-refractory GVHD
  Siltuximab (anti-IL-6): Alternative to tocilizumab

  CYTOKINE RELEASE SYNDROME (CRS) GRADING:
  Grade 1: Fever only → observe
  Grade 2: Fever + hypotension/hypoxia → tocilizumab
  Grade 3: Severe hypotension + high-flow O₂ → ICU, tocilizumab + steroids
  Grade 4: Life-threatening → immediate intervention
```

---

## Decision Cheat Sheet

| Cytokine / Pathway | Function | Blocked by |
|---------------------|---------|------------|
| IL-1β | Fever, inflammasome output | Anakinra, canakinumab |
| IL-6 | Acute phase, Th17 | Tocilizumab, sarilumab |
| IL-4 + IL-13 | Th2, IgE, atopy | Dupilumab (anti-IL-4Rα) |
| IL-17A | Neutrophil recruitment, psoriasis | Secukinumab, ixekizumab |
| IL-23 | Th17 maintenance | Risankizumab, guselkumab |
| TNF | NF-κB, inflammation | Adalimumab, infliximab, etanercept |
| IFN-γ | Macrophage M1, MHC↑ | Emapalumab (HLH) |
| JAK1/2 | STAT signaling | Baricitinib, ruxolitinib |
| JAK1/3 | T cell proliferation (IL-2) | Tofacitinib, upadacitinib |
| NF-κB | All inflammatory genes | Corticosteroids (upstream) |

---

## Common Confusion Points

**IL-6 is pleotropic — context changes effect**: IL-6 + TGF-β → Th17 (pro-inflammatory). IL-6 alone with IL-21 → plasma cell differentiation. IL-6 → acute-phase response in liver (protective). Same cytokine, different cell types and co-stimuli → completely different outcomes.

**JAK inhibitors suppress broadly**: Because STATs mediate signaling from many cytokines (not just one), JAK inhibitors affect multiple pathways simultaneously. JAK1/2 inhibition (baricitinib) blocks IFN-γ, IL-6, GM-CSF signaling — it doesn't selectively block any one cytokine.

**TNF has both pro- and anti-inflammatory roles**: TNF was named for its tumor necrosis activity (first found to kill tumor cells in lab). But it's primarily pro-inflammatory in autoimmune disease. Paradoxically, anti-TNF therapy can worsen certain autoimmune conditions (IBD can worsen with etanercept) because TNF has tissue-specific regulatory roles.

**Type I vs. Type II IFN**: Type I IFN (IFN-α/β): antiviral. Type II IFN (IFN-γ): immune activation/macrophage. Similar names, very different roles and receptors. IFN-β is therapeutic for MS (immunomodulatory via Type I pathway). IFN-γ is not used for MS and might worsen it.
