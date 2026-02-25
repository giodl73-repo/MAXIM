# Autoimmunity

## The Big Picture

```
AUTOIMMUNITY: WHEN TOLERANCE FAILS
=====================================

  PREVALENCE: ~5–8% of the population has an autoimmune disease
  ~80 recognized autoimmune diseases; 70% of patients are female
  Annual cost in US: >$100 billion (disability + treatment)

  TOLERANCE MECHANISMS THAT FAIL:
  ┌──────────────────────────────────────────────────────────────┐
  │ CENTRAL TOLERANCE                                             │
  │   Thymus (T cells): Clonal deletion of self-reactive clones │
  │   Bone marrow (B cells): Deletion + receptor editing        │
  │   FAILURE: AIRE mutations → APECED (multi-organ autoimmunity)│
  │                                                               │
  │ PERIPHERAL TOLERANCE                                         │
  │   Anergy: Self-antigen without co-stimulation → T cell silent│
  │   Treg suppression: FoxP3+ cells actively suppress          │
  │   Deletion: Persistent antigen → activation-induced death   │
  │   Ignorance: Sequestered self-antigens (eye, testis, brain) │
  │   FAILURE: Loss of Treg, bystander activation, molecular    │
  │             mimicry, epitope spreading                       │
  └──────────────────────────────────────────────────────────────┘

  AUTOIMMUNITY TRIGGERS:
  ┌──────────────────────────────────────────────────────────────┐
  │ Genetic predisposition (HLA + non-HLA genes)                 │
  │          + Environmental trigger                              │
  │                                                               │
  │ Environmental triggers:                                       │
  │   Infections: Molecular mimicry, bystander activation       │
  │   Drugs: DILI, drug-induced SLE (procainamide, hydralazine) │
  │   Microbiome changes: Dysbiosis associated with IBD, T1D    │
  │   UV light: SLE flares; Vitamin D regulation                │
  │   Hormones: Explains female predominance                     │
  │   Stress: Neuroendocrine → immune dysregulation             │
  └──────────────────────────────────────────────────────────────┘
```

---

## Tolerance Mechanisms in Detail

### Molecular Mimicry

```
  MOLECULAR MIMICRY
  ==================

  MECHANISM: Pathogen antigen structurally resembles self-antigen.
  Immune response to pathogen also reacts to self.

  CLASSIC EXAMPLES:
  ┌────────────────────────────────────────────────────────────────┐
  │ RHEUMATIC FEVER:                                               │
  │ Streptococcus M protein → antibodies cross-react with        │
  │ cardiac myosin and valvular endothelium → rheumatic carditis  │
  │ Prevention: Penicillin for strep throat (→ prevents RF)       │
  │                                                                 │
  │ GUILLAIN-BARRÉ SYNDROME (GBS):                                │
  │ Campylobacter jejuni lipooligosaccharide resembles gangliosides│
  │ (GM1, GD1a) on peripheral nerve axons                         │
  │ Anti-ganglioside antibodies → motor nerve damage              │
  │ Classic post-infectious ascending paralysis                   │
  │                                                                 │
  │ ANKYLOSING SPONDYLITIS (AS):                                  │
  │ HLA-B27 + Klebsiella nitrogenase hypothesis (contested)       │
  │ HLA-B27 heavy chain → CD8 T cell response                    │
  │                                                                 │
  │ MULTIPLE SCLEROSIS:                                            │
  │ EBV infection → anti-GlialCAM × anti-EBNA1 cross-reaction    │
  │ (2022 Bjornevik study: 32x increased MS risk after EBV)       │
  └────────────────────────────────────────────────────────────────┘
```

### Epitope Spreading

```
  EPITOPE SPREADING
  ==================

  MECHANISM: Initial immune response to one self-antigen
  → tissue damage → release of other self-antigens
  → secondary autoimmune responses to new epitopes
  → amplification cascade

  EXAMPLE: In rheumatoid arthritis:
  Initial response to citrullinated peptides (ACPA)
  → joint inflammation → cartilage destruction
  → Collagen type II fragments released → anti-collagen Abs
  → Further inflammation → more antigens released
  → Disease perpetuates even if initial trigger resolved

  CLINICAL IMPLICATION:
  ─ Early treatment is most important (before spreading)
  ─ "Window of opportunity" for biologic therapy in RA
  ─ Explains why longstanding disease is harder to put into remission
```

---

## HLA Associations

```
  HLA GENETICS AND AUTOIMMUNE DISEASE
  =======================================

  HLA: THE STRONGEST GENETIC RISK FACTOR FOR MOST AUTOIMMUNE DISEASES

  ┌─────────────────────────────────────────────────────────────────┐
  │ DISEASE           HLA ALLELE      RELATIVE RISK               │
  │ Ankylosing spondylitis  B*27:05    ~30–100x (strongest known)  │
  │ Type 1 Diabetes   DR3-DQ2          ~3x                         │
  │                   DR4-DQ8          ~4x                          │
  │                   DR3/DR4          ~20x (combined)             │
  │ Rheumatoid Arthritis DRB1*04:01    ~3–5x (shared epitope)     │
  │ Multiple sclerosis  DRB1*15:01     ~3x                          │
  │ SLE                DR2, DR3        ~2–3x                        │
  │ Celiac disease     DQ2, DQ8        ~Required (necessary not suf)│
  │ Narcolepsy         DQB1*06:02      ~1,000x (strongest!)        │
  └─────────────────────────────────────────────────────────────────┘

  WHY HLA?
  HLA determines which peptides are presented to T cells.
  Specific alleles present self-peptides in conformations that
  activate T cells (i.e., present self-peptides as if "foreign").

  SHARED EPITOPE HYPOTHESIS (RA):
  HLA-DRB1 alleles *0401, *0404, *0405, *0101:
  All contain "QKRAA" sequence in DRβ chain peptide-binding groove
  This epitope preferentially presents citrullinated peptides
  → Anti-citrullinated protein antibodies (ACPA) = RA biomarker

  GENOME-WIDE ASSOCIATION STUDIES IN AUTOIMMUNITY:
  Non-HLA loci also important:
  ─ PTPN22 (R620W): T/B cell activation threshold
    Risk allele in RA, T1D, SLE, GD, vitiligo
  ─ IL23R: Th17 pathway; Crohn's, AS, psoriasis
  ─ STAT4: IFN signaling; SLE, RA, T1D
  ─ CTLA4: T cell checkpoint; T1D, celiac, Graves'
```

---

## Major Autoimmune Diseases

### Type 1 Diabetes (T1D)

```
  TYPE 1 DIABETES
  ================

  TARGET: Pancreatic β cells (insulin-producing)
  MECHANISM: CD8+ T cells directly kill β cells
             CD4+ T cells promote β cell killing via IFN-γ
             Autoantibodies: Anti-insulin, anti-GAD65, anti-IA2, anti-ZnT8

  PATHOPHYSIOLOGY:
  ─ Years before clinical diabetes: autoantibodies accumulate
  ─ β cell mass slowly destroyed (silent phase)
  ─ Clinical onset when ~80–90% β cell mass lost → insulin-deficient
  ─ Ketoacidosis risk without insulin

  GENETICS:
  HLA: DR3-DQ2/DR4-DQ8 → high risk
  HLA: DR2-DQ6 → protective (!)
  PTPN22 R620W: Reduced T cell activation threshold → auto-reactivity
  Multiple other loci (INS gene VNTR, CTLA4, IL2RA)

  TREATMENT (current): Insulin replacement
  PREVENTION: Teplizumab (anti-CD3) delays onset by ~3 years in at-risk
              First immunotherapy to delay autoimmune diabetes (2022)
```

### Multiple Sclerosis (MS)

```
  MULTIPLE SCLEROSIS
  ==================

  TARGET: Myelin in CNS (oligodendrocytes + myelin sheath)
  LESIONS: Demyelinating plaques → impaired nerve conduction
  MECHANISM: CD4+ Th1 + Th17 cells attack myelin
             CD8+ T cells in lesions; B cells/antibodies also involved
             Blood-brain barrier breakdown → leukocyte infiltration

  CLINICAL FORMS:
  RRMS (Relapsing-Remitting): 85% at onset; episodic attacks
  SPMS (Secondary Progressive): RRMS → progressive accumulation
  PPMS (Primary Progressive): Progressive from onset

  EBV CONNECTION (2022 Science paper):
  ─ Almost 100% of MS patients have prior EBV infection
  ─ EBV nuclear antigen 1 (EBNA1) → anti-GlialCAM antibodies
  ─ Molecular mimicry: EBNA1 epitope = GlialCAM epitope
  ─ Longitudinal data (10M US military): 32x increased MS risk post-EBV
  ─ First strong causal evidence for viral trigger of autoimmunity

  TREATMENT LADDER:
  ┌────────────────────────────────────────────────────────────────┐
  │ Low efficacy (injectable/oral):                                 │
  │   IFN-β, glatiramer acetate: ~30% relapse reduction           │
  │                                                                 │
  │ Moderate efficacy (oral):                                      │
  │   Dimethyl fumarate (Tecfidera): Nrf2 activation               │
  │   Teriflunomide: DHODH inhibitor → lymphocyte reduction       │
  │   Cladribine: Lymphocyte depletion (pulse dosing)             │
  │   Siponimod/ozanimod/ponesimod: S1P receptor modulators        │
  │                                                                 │
  │ High efficacy (IV/SC biologics):                               │
  │   Natalizumab: Anti-α4 integrin → prevents CNS traffic (risk: PML)│
  │   Alemtuzumab: Anti-CD52 → lymphocyte depletion (potent)      │
  │   Ocrelizumab/ofatumumab: Anti-CD20 → B cell depletion        │
  │   Approved for PPMS: Ocrelizumab only                         │
  └────────────────────────────────────────────────────────────────┘
```

### Rheumatoid Arthritis (RA)

```
  RHEUMATOID ARTHRITIS
  ====================

  TARGET: Synovium of joints (lining of joint space)
  MECHANISM: Immune complex deposition + T/B cell activation
             → Pannus formation (synovial tissue invades cartilage)
             → Bone erosion

  KEY BIOMARKERS:
  RF (Rheumatoid Factor): IgM anti-IgG Fc; +70–80% of RA
  ACPA (Anti-Citrullinated Protein Antibody): More specific; +70%
  Both RF+ and ACPA+: Predicts aggressive erosive disease

  PATHOGENESIS:
  Citrullination: PAD4 enzyme converts arginine → citrulline in
  proteins during inflammation/NET formation
  HLA shared epitope → presents citrullinated peptides
  → ACPA production → immune complex deposition → synovial damage

  TREATMENT PYRAMID:
  ┌────────────────────────────────────────────────────────────────┐
  │ 1st LINE: Methotrexate (MTX, anchor drug)                    │
  │   Folate antagonist → anti-proliferative + anti-inflammatory  │
  │   Weekly dose; required with most biologics                   │
  │                                                                 │
  │ 2nd LINE: Biologic DMARDs                                     │
  │   Anti-TNF (adalimumab, etanercept): Most established         │
  │   Anti-IL-6R (tocilizumab, sarilumab): Alternative to anti-TNF│
  │   Anti-CD20 (rituximab): B cell depletion; seropositive RA   │
  │   CTLA-4-Ig (abatacept): Blocks T cell co-stimulation        │
  │                                                                 │
  │ 3rd LINE: JAK inhibitors (oral)                               │
  │   Tofacitinib (JAK1/3), baricitinib (JAK1/2)                 │
  │   Upadacitinib (selective JAK1)                               │
  │   Boxed warning: Cardiovascular, thromboembolic (JAKis)      │
  └────────────────────────────────────────────────────────────────┘
```

### Systemic Lupus Erythematosus (SLE)

```
  SLE: THE PROTOTYPE SYSTEMIC AUTOIMMUNE DISEASE
  ================================================

  HALLMARK: Anti-nuclear antibodies (ANA+) → near-universal
  SPECIFIC: Anti-dsDNA, Anti-Sm (diagnostic criteria)
  MECHANISM: Defective clearance of apoptotic cells
             → Nucleic acids accumulate → activate cGAS-STING + TLR7/9
             → Type I IFN signature → B cell hyperactivation → ANA

  TYPE I IFN SIGNATURE:
  Majority of SLE patients: Elevated IFN-α + IFN-inducible gene expression
  ─ Plasmacytoid DCs activated by immune complexes → massive IFN-α
  ─ Therapeutic target: Anifrolumab (anti-IFNAR1) → FDA approved 2021

  ORGAN INVOLVEMENT:
  Skin: Malar rash (butterfly), photosensitivity, discoid lupus
  Joints: Non-erosive arthritis (compare RA: erosive)
  Kidney: Lupus nephritis → class I–V (WHO) on biopsy
  CNS: Neuropsychiatric SLE (seizures, psychosis)
  Blood: Hemolytic anemia, thrombocytopenia, lymphopenia
  Serosal: Pericarditis, pleuritis

  LUPUS NEPHRITIS TREATMENT:
  Induction: Mycophenolate + hydroxychloroquine; IV cyclophosphamide
  Maintenance: Mycophenolate
  Belimumab (anti-BAFF): Reduces B cell survival → reduces flares
  Voclosporin (calcineurin inhibitor): Podocyte protection
```

---

## Common Autoimmune Themes

```
  SHARED FEATURES ACROSS AUTOIMMUNE DISEASES
  =============================================

  FEMALE PREDOMINANCE (most autoimmune diseases):
  ─ ~80% of autoimmune disease burden in women
  ─ X chromosome: more immune-related genes; skewed X-inactivation
  ─ Estrogen: Generally immunostimulatory
  ─ Testosterone: Generally immunosuppressive
  ─ Exceptions: AS (male predominant); T1D (equal)

  AUTOIMMUNE CLUSTERING:
  ─ Patients with one autoimmune disease have higher risk of others
  ─ "Autoimmune diathesis" — shared genetic factors (PTPN22, HLA)
  ─ Thyroid disease often co-occurs with RA, SLE, T1D

  RELAPSING-REMITTING PATTERN:
  ─ Stress, infection → flares
  ─ Pregnancy → sometimes remission (RA), sometimes flare (SLE)
  ─ Disease course correlates with immune state

  TREATMENT TARGETS SHARED:
  Anti-TNF: RA, AS, psoriasis, IBD, uveitis, psoriatic arthritis
  Anti-IL-17: Psoriasis, AS, PsA, non-radiographic axSpA
  JAK inhibitors: RA, UC, atopic dermatitis, AS, psoriasis
  Anti-CD20: RA, MS (ocrelizumab), SLE (being studied)
```

---

## Decision Cheat Sheet

| Feature | Suggests Autoimmunity? | Notable Example |
|---------|----------------------|-----------------|
| ANA+ + anti-dsDNA | SLE | Highly specific for SLE |
| RF+ + ACPA+ | RA | Predicts erosive disease |
| HLA-B27+ | AS, SpA | Ankylosing spondylitis |
| Thyroid peroxidase Ab | Hashimoto's thyroiditis | Most common in women |
| Anti-GAD65 + anti-insulin | T1D | Predict future T1D |
| Anti-acetylcholine receptor | Myasthenia gravis | Neuromuscular junction |
| Anti-Hu/Yo (paraneoplastic) | Paraneoplastic syndrome | Cancer trigger |
| FoxP3 mutation | IPEX syndrome | Fatal multi-organ autoimmunity |
| AIRE mutation | APECED | Polyendocrinopathy syndrome |
| Biologic therapy needed | After methotrexate failure in RA | Anti-TNF first-line biologic |

---

## Common Confusion Points

**Autoimmune vs. autoinflammatory**: Autoimmune diseases have specific self-reactive lymphocytes/antibodies (RA, SLE, T1D). Autoinflammatory diseases have dysregulated innate immunity without specific adaptive response (NLRP3 mutations, FMF). Some diseases overlap (mixed picture). The distinction matters for treatment: JAK inhibitors vs. IL-1 blockade.

**Molecular mimicry is compelling but hard to prove**: The EBV/MS story is the most convincing causal evidence to date. Most molecular mimicry hypotheses are correlational. The mechanism requires: sequence similarity, cross-reactive immune response, and temporal association between infection and disease — all three are hard to establish definitively.

**Positive ANA doesn't mean SLE**: ANA positivity at low titer is common (5–10% of healthy people) and can occur with infections, other autoimmune diseases, and some medications. A positive ANA is the beginning of a workup, not a diagnosis. SLE requires meeting ACR/EULAR criteria including specific high-titer antibodies (anti-dsDNA, anti-Sm) and clinical manifestations.

**Immunosuppression doesn't cure autoimmunity**: Current therapies suppress the immune response (reduce flares, prevent organ damage) but don't reprogram tolerance. Biologic therapies require continuous administration. Stopping biologic therapy usually leads to disease return. Genuine tolerance induction (as with CAR-Treg therapies in trials) is the frontier for curative therapy.
