# Immune System

## The Big Picture: Two-Tier Defense

```
IMMUNE SYSTEM
┌──────────────────────────────────────────────────────────────────┐
│  INNATE IMMUNITY (first hours)                                   │
│  Fast · Generic · No memory                                      │
│  Barriers, phagocytes, NK cells, complement, inflammation        │
│  Pattern recognition: PAMPs (pathogen patterns) via PRRs         │
│  Fails to clear? → activates adaptive                            │
├──────────────────────────────────────────────────────────────────┤
│  ADAPTIVE IMMUNITY (days to weeks)                               │
│  Slow · Specific · Memory                                        │
│  T cells (cell-mediated) + B cells (humoral/antibody)            │
│  Antigen-specific receptor repertoire (~10⁷ unique)              │
│  Second exposure: 100–1,000× faster, larger response            │
└──────────────────────────────────────────────────────────────────┘

Both branches interact constantly:
  Innate APC (dendritic cell) → presents antigen → activates T cells
  T helper cells → activate B cells
  Antibodies opsonize → phagocytes kill better
  Cytokines coordinate everything
```

---

## Innate Immunity: First Responders

### Physical and Chemical Barriers

```
Skin: stratified squamous epithelium + keratin + sebum (fatty acids, pH ~5)
Mucosae: mucus layer (traps pathogens) + cilia (mucociliary escalator)
          IgA secretion (dimeric), lysozyme, defensins
Stomach: pH ~1.5–2 (kills most ingested pathogens)
Urinary tract: flushing + low pH + THP (uromodulin) as decoy receptor
Respiratory: nasal turbinates (impaction), cough/sneeze reflex
```

### Pattern Recognition Receptors (PRRs)

Innate cells don't have antigen-specific receptors — they recognize conserved **PAMPs** (pathogen-associated molecular patterns) and **DAMPs** (danger-associated molecular patterns from damaged self):

| PRR family | Location | Recognizes | Effect |
|------------|----------|-----------|--------|
| Toll-like receptors (TLR1–13) | Membrane + endosomal | LPS (TLR4), flagellin (TLR5), dsRNA (TLR3), CpG DNA (TLR9) | NF-κB → cytokines; IRF3 → interferons |
| NOD-like receptors (NLRs) | Cytoplasm | Bacterial fragments, cellular stress | NLRP3 inflammasome → caspase-1 → IL-1β + IL-18 |
| RIG-I / MDA5 | Cytoplasm | Viral RNA (dsRNA/ssRNA) | Type I IFN (IFN-α/β) production |
| cGAS-STING | Cytoplasm | Foreign/self cytoplasmic DNA | IFN-β, inflammatory cytokines |

### Phagocytes

**Neutrophils** (PMNs): first to arrive (within 1–2 hours)
- Killing mechanisms: respiratory burst (NADPH oxidase → superoxide → H₂O₂ → HOCl), neutrophil extracellular traps (NETs), lysosomal enzymes, defensins
- Short-lived (~12–18 hr), form pus

**Macrophages**: tissue-resident (Kupffer cells in liver, microglia in brain, alveolar macrophages, osteoclasts)
- Phagocytosis, antigen presentation to T cells (MHC II)
- Cytokine production: TNF-α, IL-1β, IL-6, IL-12
- Classical (M1): pro-inflammatory; Alternative (M2): anti-inflammatory, wound repair

**Dendritic cells (DCs)**: key link between innate and adaptive
- Sample peripheral tissues → migrate to lymph nodes
- Present antigen on MHC I (cross-presentation) and MHC II
- Provide "signal 2" (co-stimulation: CD80/86–CD28) required to activate T cells

### Natural Killer Cells (NK)

Kill infected/tumor cells without requiring MHC-peptide recognition:
```
NK cell activation balance:
  Activating signals (NKG2D, NCR) from "stress ligands" on target
  Inhibitory signals (KIR, NKG2A) from MHC I on normal cells

  Normal cell: lots of MHC I → inhibitory signal dominates → NOT killed
  Virus-infected/tumor: downregulate MHC I (to hide from T cells)
    → loss of inhibitory signal → NK activation → kill target
```

---

## Inflammation

Cardinal signs: **PRISH** — Pain, Redness, Increased warmth, Swelling, Loss of function (functio laesa)

```
ACUTE INFLAMMATION SEQUENCE:

Tissue injury / pathogen
  ↓
Mast cell degranulation: histamine + tryptase (vasodilation, ↑ permeability)
  ↓
Vasodilation (arterioles) → Redness, Warmth
  ↓
↑ Vascular permeability (venules) → fluid and proteins leak → Swelling (edema)
  ↓
Neutrophil margination → rolling (selectins) → firm adhesion (integrins/ICAMs)
  → diapedesis → chemotaxis (IL-8/CXCL8, C5a, LTB4) → phagocytosis
  ↓
Resolution (if infection cleared):
  Neutrophil apoptosis → macrophage efferocytosis → anti-inflammatory resolution phase
  (resolvins, protectins from omega-3 FAs)

Chronic inflammation (if not resolved):
  Macrophage + lymphocyte dominated
  Tissue destruction + fibrosis
  Granuloma formation (TB, sarcoid, Crohn's): macrophage cluster + multinucleate giant cells
```

### Key Inflammatory Cytokines

| Cytokine | Source | Key effects |
|----------|--------|-------------|
| TNF-α | Macrophages, T cells | Fever, cachexia, ↑ adhesion molecules, septic shock mediator |
| IL-1β | Macrophages (NLRP3 → caspase-1) | Fever (PGE₂ in hypothalamus), acute phase response, leukocyte activation |
| IL-6 | Macrophages, fibroblasts | Acute phase proteins (CRP, fibrinogen, complement, ferritin via liver), B cell differentiation |
| IL-8 (CXCL8) | Macrophages, endothelium | Neutrophil chemotaxis |
| IL-12 | DCs, macrophages | Drives Th1 differentiation, activates NK cells |
| Type I IFNs (α/β) | All infected cells (DCs most) | Antiviral state, MHC I upregulation, NK activation |
| IFN-γ | Th1 cells, NK cells | Classical macrophage activation, ↑ MHC I+II, anti-intracellular pathogens |

---

## Complement System

Plasma protein cascade that kills pathogens directly and assists phagocytosis:

```
THREE ACTIVATION PATHWAYS:
  Classical:   IgM/IgG bound to antigen → C1q → C1r/s → C4 → C2 → C3
  Lectin:      MBL (mannose-binding lectin) on pathogen surface → MASPs → C4 → C2 → C3
  Alternative: Spontaneous C3 hydrolysis on pathogen surfaces → amplification loop

ALL CONVERGE:
  C3 → C3b (opsonin, deposited on surface) + C3a (anaphylatoxin, histamine release)
  C3b → C5 convertase → C5a (most potent anaphylatoxin, chemotactic) + C5b
  C5b + C6, C7, C8, C9 (polymerize) → MEMBRANE ATTACK COMPLEX (MAC, C5b-9)
    → ion pore in bacterial membrane → osmotic lysis

FUNCTIONS:
  Opsonization: C3b + iC3b → phagocyte CR1/CR3 binding → enhanced phagocytosis
  Inflammation: C3a + C5a → mast cell degranulation, neutrophil recruitment
  Lysis: MAC → direct kill (gram-negative bacteria, some viruses)
  Clearance: C1q binds apoptotic cells → complement mediates clearance
```

---

## Adaptive Immunity: T Cells

### T Cell Development and Activation

```
Bone marrow progenitor → Thymus
  Positive selection: T cells must recognize self-MHC (or die by neglect)
  Negative selection: T cells that bind self-MHC + self-peptide with HIGH affinity → apoptosis
  Result: T cell repertoire recognizes self-MHC + foreign peptide (but not self-peptides strongly)

TCR (T cell receptor): heterodimer (αβ or γδ) + CD3 complex
  Recognizes: peptide + MHC (both required — MHC restriction)
  CD4: co-receptor for MHC II (helper T cells)
  CD8: co-receptor for MHC I (cytotoxic T cells)
```

### MHC I vs MHC II

```
MHC I (HLA-A, B, C):
  Present on: ALL nucleated cells
  Loads: endogenous peptides (intracellular proteins, viral)
  Peptides: 8–10 amino acids (TAP transporter into ER, peptide loading)
  Activates: CD8+ cytotoxic T cells (CTLs)
  Logic: "look inside me — am I infected or cancerous?"

MHC II (HLA-DR, DP, DQ):
  Present on: Professional APCs only (DCs, macrophages, B cells)
  Loads: exogenous peptides (phagocytosed bacteria, external antigens)
  Peptides: 13–25 amino acids (endosomal processing, invariant chain)
  Activates: CD4+ helper T cells
  Logic: "look what I ate — are there pathogens in the environment?"

Cross-presentation: DCs can load exogenous antigens onto MHC I
  → activate CTLs against extracellular pathogens (important for antitumor immunity, vaccines)
```

### T Helper Cell Subsets

```
Naive CD4+ T cell → activated by DC (signal 1: TCR + MHC II; signal 2: CD28 + CD80/86)

CYTOKINE ENVIRONMENT DURING ACTIVATION DETERMINES FATE:

IL-12, IFN-γ  → TH1: IFN-γ producer → activate macrophages, CTLs
                     Defense against intracellular pathogens (Mycobacteria, Listeria, viruses)
                     Role in autoimmunity (Crohn's, MS, T1DM)

IL-4          → TH2: IL-4, IL-5, IL-13 → B cell class switch to IgE, eosinophil activation
                     Defense against helminths; drives allergy/asthma

TGF-β + IL-6  → TH17: IL-17, IL-22 → neutrophil recruitment, epithelial defense
                     Defense against extracellular bacteria + fungi (Candida)
                     Role in psoriasis, IBD, ankylosing spondylitis

TGF-β (alone) → Treg: FoxP3+, produces IL-10 + TGF-β
                     Suppress immune responses, maintain peripheral tolerance
                     Prevent autoimmunity; can suppress antitumor immunity

IL-21         → TFH (follicular helper): support germinal center reaction + B cell responses
```

### CD8+ Cytotoxic T Cells (CTLs)

Kill target cells by:
1. **Perforin/granzymes**: perforin pores in target membrane → granzyme B enters → caspase cascade → apoptosis
2. **Fas-FasL interaction**: CTL Fas ligand binds target Fas → death receptor pathway → apoptosis
3. **Cytokines**: IFN-γ, TNF (inflammatory killing)

---

## Adaptive Immunity: B Cells and Antibodies

### B Cell Activation and Germinal Center

```
B cell: BCR (surface IgM) recognizes antigen
  ↓
T-dependent response (most protein antigens):
  B cell ingests antigen → presents on MHC II → cognate Th2/TFH recognizes it
  CD40 (B cell) + CD40L (T cell) = co-stimulation signal
  Cytokines (IL-4, IL-21) drive proliferation + germinal center formation

GERMINAL CENTER (lymph node follicle):
  Rapid B cell proliferation (centroblasts)
  Somatic hypermutation: activation-induced cytidine deaminase (AID) mutates V region
  Affinity maturation: cells with higher BCR affinity for antigen selected (survive)
                        cells with lower affinity die (apoptosis)
  Isotype switching: AID again — changes constant region:
    IgM → IgG (systemic, complement, phagocytosis)
    IgM → IgA (mucosal immunity)
    IgM → IgE (allergy, antiparasite)
  ↓
Plasma cells: migrate to bone marrow → long-lived, constitutive Ab secretion
Memory B cells: circulate, rapid response on re-exposure
```

### Immunoglobulin Classes

```
STRUCTURE: 2 heavy chains + 2 light chains (κ or λ)
  Fab region (variable): antigen binding (tip of Y)
  Fc region (constant): effector functions — complement activation, FcR binding

CLASS  MW      Properties and functions
IgM    900kDa  Pentamer; first produced in response; best complement activator
               Does NOT cross placenta; found in serum only
IgG    150kDa  Most abundant in serum; 4 subclasses (IgG1–4)
               ONLY antibody to cross placenta (neonatal protection)
               Opsonization, ADCC, complement (IgG1/3)
               Secondary response dominant
IgA    160-    Monomer (serum) or dimer (secretory, with J chain + secretory component)
       385kDa  Dominant at mucosal surfaces (gut, respiratory, breast milk)
               No complement activation; prevents pathogen adherence
IgE    190kDa  Lowest serum concentration; Fc binds mast cells and basophils
               Cross-linking by antigen → immediate hypersensitivity (allergy, anaphylaxis)
               Defense against helminths (worm expulsion)
IgD    185kDa  Surface of naive B cells; signaling receptor; minimal serum function
```

---

## Immunological Memory

```
PRIMARY RESPONSE (first exposure):
  Lag: 5–7 days
  Peak: ~14 days
  Antibody class: IgM first, then IgG
  Magnitude: moderate

SECONDARY RESPONSE (re-exposure):
  Lag: 1–3 days
  Peak: much higher (~100–1000× antibody levels)
  Antibody class: IgG dominant (memory class-switched)
  Magnitude: large and sustained

Basis:
  Memory B cells: long-lived, lower activation threshold, rapid proliferation
  Memory T cells (TCM, TEM, TSCM): faster and stronger recall response
  Memory is antigen-specific
```

---

## Immune Tolerance

```
CENTRAL TOLERANCE (delete self-reactive cells at origin):
  T cells: thymic negative selection (AIRE expression allows thymic DCs to present
           peripheral self-antigens → clonal deletion of high-affinity self-reactive T cells)
  B cells: receptor editing or clonal deletion in bone marrow

PERIPHERAL TOLERANCE (suppress remaining self-reactive cells):
  Anergy: T cell encounters antigen without co-stimulation → functional unresponsiveness
  Regulatory T cells (Treg): FoxP3+, secrete IL-10 + TGF-β, CTLA-4 high expression
  Activation-induced cell death (AICD): Fas/FasL — activated T cells eliminate each other
  Checkpoint receptors:
    CTLA-4 (CD152): on T cells, competes with CD28 for CD80/86 → dampens activation
    PD-1: on activated T cells; PD-L1/L2 on tumor cells → "don't kill me" signal

CHECKPOINT BLOCKADE (cancer immunotherapy):
  anti-CTLA-4 (ipilimumab) + anti-PD-1 (pembrolizumab, nivolumab) + anti-PD-L1
  Release brakes on T cells → enhanced antitumor immunity
  Side effects: immune-related adverse events (irAEs) — autoimmune-like
```

---

## Vaccines: Mechanisms by Type

| Type | Examples | Immune response | Advantages | Disadvantages |
|------|----------|----------------|------------|---------------|
| Live attenuated | MMR, varicella, yellow fever, oral polio | CD4+ T, CD8+ T, B cells, IgA | Strong, long-lasting, mucosal | Risk in immunocompromised; cold chain required |
| Inactivated (killed) | IPV, flu (IIV), hepatitis A, rabies | B cells → antibody (no CTL typically) | Stable, safe in immunocompromised | Weaker, often needs adjuvant + boosters |
| Subunit/protein | Hepatitis B (HBsAg), pertussis (acellular), shingles (Shingrix) | B cells + T cells (with adjuvant) | Safe, defined antigens | Less immunogenic; needs adjuvant |
| Conjugate | Hib, pneumococcal (PCV), meningococcal | T-dependent response (polysaccharide conjugated to protein carrier) | Immunogenic in infants (polysaccharide alone is T-independent, poor in < 2 yrs) | Manufacturing complex |
| mRNA | COVID-19 (Pfizer/Moderna) | LNP delivery → protein expression → MHC I + II presentation → CD8 + CD4 + B | Rapid design, strong response, no infection risk | Cold chain, novel platform |
| Viral vector | COVID-19 (AZ/J&J), Ebola (rVSV) | Antigen expression in cells → CD8 + CD4 + B | Strong CTL | Pre-existing vector immunity; adenoviral issues |
| Toxoid | Tetanus, diphtheria | Antibody (neutralizing) | Excellent track record | Booster required |

<!-- @editor[audience/P3]: Vaccine mRNA/LNP delivery and MHC I+II presentation detail may exceed what's needed for reference -- mechanism covered in T cell section above -->
**Adjuvants**: enhance immunogenicity by triggering innate immunity (TLR agonists, alum, MF59)
- Without adjuvant, soluble proteins are often tolerogenic
- Alum: NLRP3 inflammasome activation → IL-1β → DC activation

---

<!-- @editor[bridge/P2]: No old-world bridge -- innate = firewall + IDS (pattern matching, no memory), adaptive = ML-trained classifier (learns, remembers), MHC I = process attestation, MHC II = threat intelligence sharing, complement = automated incident response, tolerance = whitelisting -->
## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What must happen for naive T cell to activate? | Signal 1 (TCR + MHC-peptide) AND signal 2 (CD28 + CD80/86). Either alone → anergy |
| CD8 T cell: how does it kill? | Perforin pores + granzyme B → target apoptosis; also Fas/FasL |
| Complement terminal event? | MAC (C5b-9) forms pore in bacterial membrane → osmotic lysis |
| What's the danger of NK cells' "missing self" strategy? | NK cells can kill self cells that lost MHC I (e.g., stressed, cancerous). Normal cells survive by constantly displaying MHC I. |
| Why IgG crosses placenta but not IgM? | IgG: FcRn (neonatal Fc receptor) on placental syncytiotrophoblasts mediates transcytosis. IgM pentamer: too large. |
| Why re-vaccination schedule? | Primary response is modest/short; boosters drive germinal center, affinity maturation, memory generation |

---

## Common Confusion Points

**MHC vs HLA**
MHC (major histocompatibility complex) = generic term. HLA (human leukocyte antigen) = human version of MHC. Used interchangeably in clinical contexts.

**Opsonization speeds killing by 1,000–10,000×**
Phagocytes do phagocytose without opsonins, but IgG (Fc receptor binding) and C3b (CR1 binding) dramatically enhance uptake. This is why asplenic patients are at high risk from encapsulated bacteria (Strep pneumo, H. flu, Neisseria): the spleen clears these via opsonin-dependent phagocytosis.

**Anaphylaxis is Type I hypersensitivity**
First exposure: allergen → IgE production → IgE binds Fc on mast cells (sensitization, no symptoms).
Re-exposure: allergen cross-links mast cell–bound IgE → degranulation (histamine, tryptase, leukotrienes, prostaglandins) → systemic vasodilation, bronchospasm, urticaria.
Treatment: epinephrine (reverses vasodilation + bronchoconstriction via α₁ and β₂).

**Active vs passive immunity**
- Active: you generate the response (natural infection or vaccination) → memory
- Passive: you receive preformed antibodies (maternal IgG transplacental, IVIG, monoclonal Ab therapy) → fast protection, no memory, temporary
