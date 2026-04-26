# Immunology — Landscape Overview

## The Big Picture

```
THE IMMUNE SYSTEM AS A DISTRIBUTED COMPUTING SYSTEM
=====================================================

  FRAMING:
  ─ Innate immunity  = firewall (pattern matching against known bad)
  ─ Adaptive immunity = ML system (learns from examples, remembers)
  ─ Tolerance        = classifier accuracy (avoid false positives)
  ─ Inflammation     = alerting and incident response
  ─ Memory           = model persistence (keeps the learned state)

  TWO-ARM ARCHITECTURE:

  ┌─────────────────────────────────────────────────────────────────┐
  │  INNATE IMMUNITY (Born with it — first 0–4 hours)               │
  │  ─────────────────────────────────────────────────              │
  │  Pattern recognition: PRRs detect PAMPs and DAMPs               │
  │  Fixed rules: TLR4 binds LPS → always triggers inflammation     │
  │  No learning: same response every time                          │
  │  Cells: Neutrophils, macrophages, NK cells, DCs, mast cells     │
  │  Soluble: Complement, cytokines, acute-phase proteins           │
  │  Response time: Minutes to hours                                │
  │                                                                 │
  │  ADAPTIVE IMMUNITY (Learned — 5–14 days for primary response)   │
  │  ─────────────────────────────────────────────────────────      │
  │  Specific recognition: BCR/TCR bind exact molecular shapes      │
  │  Learning: Clonal selection = select the "model" that fits      │
  │  Memory: Long-lived plasma cells + memory T/B cells             │
  │  Cells: B lymphocytes, T lymphocytes                            │
  │  Soluble: Antibodies (immunoglobulins)                          │
  │  Response time: Days to weeks (primary); hours (secondary)      │
  └─────────────────────────────────────────────────────────────────┘

  THEIR RELATIONSHIP:
  Innate activates adaptive (DCs present antigen to T cells)
  Adaptive refines innate (IgG opsonizes → macrophages phagocytose)
  Innate provides context (danger signals → adaptive priming)
```

---

## Cellular Cast

```
  IMMUNE CELL TAXONOMY
  =====================

  HEMATOPOIETIC STEM CELL (HSC)
       │
       ├──► MYELOID PROGENITOR
       │         │
       │         ├──► Neutrophil        First responder; phagocyte; most abundant WBC
       │         ├──► Eosinophil        Antiparasitic; allergy effector
       │         ├──► Basophil          Allergy/anaphylaxis (IgE receptor)
       │         ├──► Mast cell         Tissue-resident; IgE receptor; allergy
       │         ├──► Monocyte          Circulating precursor to macrophage
       │         ├──► Macrophage        Tissue-resident phagocyte; antigen presentation
       │         ├──► Dendritic cell    Professional antigen-presenting cell (APC)
       │         └──► (NK cell)         Innate killer; detects missing-self
       │
       └──► LYMPHOID PROGENITOR
                 │
                 ├──► B cell            Antibody producer; humoral immunity
                 │       └──► Plasma cell     Antibody secretion factory
                 │
                 ├──► T cell            Cell-mediated immunity
                 │       ├──► CD4+ helper T   Orchestrates immune response
                 │       │       ├──► Th1      Drives macrophage activation
                 │       │       ├──► Th2      Drives B cell class switching
                 │       │       ├──► Th17     Neutrophil recruitment; mucosal
                 │       │       └──► Treg     Suppresses immune response
                 │       └──► CD8+ cytotoxic T  Kills infected/cancer cells
                 │
                 └──► NK cell (also can be lymphoid)
```

---

## The Self/Non-Self Problem

```
  THE FUNDAMENTAL CHALLENGE
  ===========================

  The immune system must:
  1. DESTROY pathogens (bacteria, viruses, fungi, parasites)
  2. TOLERATE self (avoid attacking own tissues)
  3. TOLERATE commensals (gut bacteria, skin flora)
  4. TOLERATE pregnancy (fetal alloantigens)
  5. REMEMBER past encounters (immunological memory)

  FAILURE MODES:
  ┌───────────────────────────────────────────────────────────────┐
  │ Too little immunity → immunodeficiency (infections)           │
  │ Too much immunity → autoimmunity (self-attack)                │
  │ Misdirected immunity → allergy (harmless antigens)            │
  │ Tolerance failure in tumors → cancer (self-cells not killed)  │
  │ Rejection of transplant → alloimmunity                        │
  └───────────────────────────────────────────────────────────────┘

  TOLERANCE MECHANISMS:
  Central tolerance: Delete self-reactive lymphocytes during development
                     (thymus for T cells; bone marrow for B cells)
  Peripheral tolerance: Suppress mature self-reactive cells in periphery
                        (Treg cells; anergy; deletion upon re-encounter)
```

---

## Key Molecular Concepts

```
  ANTIGEN vs. EPITOPE vs. HAPTEN
  ================================

  Antigen:   Any molecule that the immune system recognizes
  Epitope:   The specific part of an antigen that the receptor binds
             (~10–15 aa for T cell; conformational for B cell)
  Hapten:    Small molecule that is not immunogenic alone; must be
             conjugated to a carrier protein to elicit a response

  IMMUNOGENICITY FACTORS:
  ─ Foreignness: More foreign = more immunogenic
  ─ Size: Large proteins more immunogenic than small peptides
  ─ Chemical complexity: Polymers > homopolymers
  ─ Degradability: Must be processed to peptide for T cell presentation
  ─ Route: subcutaneous > intradermal > intravenous for immunogenicity

  MHC: THE ANTIGEN DISPLAY SYSTEM
  ─────────────────────────────────
  MHC class I:  Displays INTRACELLULAR peptides; recognized by CD8 T cells
                Present on all nucleated cells
                Signal: "I am making this protein — is it foreign?"
  MHC class II: Displays EXTRACELLULAR peptides; recognized by CD4 T cells
                Present on professional APCs (DCs, macrophages, B cells)
                Signal: "I ate this pathogen — your response is needed"

  HLA (Human Leukocyte Antigen) = the human version of MHC
  Most polymorphic locus in human genome (>30,000 HLA alleles)
  HLA typing: critical for transplant matching, autoimmune disease risk
```

---

## The Adaptive Immune Response: Overview

```
  ADAPTIVE IMMUNE RESPONSE TIMELINE
  ===================================

  DAY 0: INFECTION
  ─ Pathogen enters tissue
  ─ Innate immune cells detect PAMPs → cytokines released
  ─ Dendritic cells engulf pathogen → migrate to lymph node

  DAY 1–4: ACTIVATION PHASE
  ─ DC presents antigen peptide (on MHC) to naïve T cells
  ─ T cell with matching TCR recognizes MHC:peptide complex
  ─ Signal 1 (TCR:MHC) + Signal 2 (CD28:B7 co-stimulation)
  ─ T cell activated → proliferates clonally

  DAY 4–7: EFFECTOR PHASE
  ─ Effector T cells migrate to infection site
  ─ CD8 T cells kill infected cells
  ─ CD4 Th cells activate macrophages; help B cells
  ─ B cells proliferate in germinal centers → antibody production
  ─ Affinity maturation: higher-affinity antibodies selected

  DAY 7–14: PEAK RESPONSE
  ─ Antibody titers peak
  ─ Infected cell killing peaks
  ─ Pathogen cleared

  DAY 14–30: CONTRACTION
  ─ ~90–95% of effector cells die (apoptosis)
  ─ Small population survives → memory cells

  LIFETIME: MEMORY
  ─ Long-lived plasma cells in bone marrow secrete antibodies for life
  ─ Memory T cells: respond faster/stronger on re-exposure
  ─ Secondary response: 100–1000x faster; much higher titer

  ANALOGY: Clonal selection is training a new ML model;
           memory is caching the trained model weights.
```

---

## File Roadmap

| File | What It Covers |
|------|----------------|
| 01-INNATE-IMMUNITY.md | PRRs (TLRs/NLRs/RLRs), complement, innate cells, inflammation |
| 02-ADAPTIVE-IMMUNITY.md | Lymphocyte development, clonal selection, MHC I/II, antigen presentation |
| 03-B-CELLS-ANTIBODIES.md | VDJ recombination, germinal centers, antibody isotypes, BCR signaling |
| 04-T-CELLS.md | TCR diversity, thymic selection, CD4 subsets, CD8 cytotoxic T cells |
| 05-CYTOKINES.md | Interleukins, interferons, JAK-STAT signaling, NF-kB, chemokines |
| 06-VACCINES.md | Vaccine types, mRNA/LNP, adjuvants, herd immunity, failure modes |
| 07-IMMUNOTHERAPY.md | Checkpoint inhibitors, CAR-T, bispecific antibodies, tumor microenvironment |
| 08-AUTOIMMUNITY.md | Tolerance mechanisms, molecular mimicry, major autoimmune diseases |
| 09-IMMUNODEFICIENCY.md | Primary immunodeficiencies, HIV/AIDS, transplant immunology, immunosenescence |

---

## Decision Cheat Sheet

| Question | Where to Look |
|----------|--------------|
| What recognizes pathogens first? | Innate — PRRs (TLRs/NLRs) — 01 |
| How does complement kill bacteria? | Innate — complement cascade — 01 |
| How does the body learn to fight infection? | Adaptive — clonal selection — 02 |
| How are antibodies made? | B cells — VDJ recombination — 03 |
| How does a T cell kill infected cells? | CD8 T cells — 04 |
| What is a cytokine storm? | Cytokines — uncontrolled loop — 05 |
| How do mRNA vaccines work? | Vaccines — LNP/innate sensing — 06 |
| How do checkpoint inhibitors work? | Immunotherapy — PD-1/CTLA-4 — 07 |
| Why does MS occur? | Autoimmunity — tolerance failure — 08 |
| What happens to the immune system with HIV? | HIV/CD4 depletion — 09 |

---

## Common Confusion Points

**Antigen vs. antibody**: An antigen is whatever triggers a response. An antibody is what B cells produce — a Y-shaped protein that specifically binds an antigen. Antigens are the inputs; antibodies are the learned outputs.

**Innate vs. adaptive: time scale difference**: Innate immunity activates within minutes to hours — it's always on and uses fixed pattern-recognition rules. Adaptive immunity takes 5–14 days for a primary response because B and T cells must find the right antigen, proliferate, and differentiate. This is why vaccines need a few weeks to provide protection.

**MHC class I vs. II directs which T cell responds**: Class I (all cells) → CD8 cytotoxic T cells (kill the presenting cell). Class II (professional APCs only) → CD4 helper T cells (coordinate the response). This makes biological sense: if any cell is infected (presents viral peptide on MHC I), CD8 cells kill it. If professional APCs are showing you what they ate, CD4 cells organize the broader response.

**Inflammation is not always bad**: Acute inflammation is a coordinated response essential for pathogen clearance. Chronic inflammation is pathological. The same mechanisms that fight infection (cytokines, reactive oxygen species) cause tissue damage when dysregulated.
