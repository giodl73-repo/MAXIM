# Virus-Host Interactions and Tropism

## The Big Picture

Viral tropism — which cells and tissues a virus can infect — determines disease
manifestation, transmission route, and pandemic potential. Tropism is determined
primarily by receptor distribution and post-entry replication capacity.

```
┌──────────────────────────────────────────────────────────────────┐
│               VIRUS-HOST INTERACTION LAYERS                      │
│                                                                  │
│  MOLECULAR LEVEL:    Receptor recognition → entry mechanism      │
│  CELLULAR LEVEL:     Restriction factors, innate sensors         │
│  TISSUE LEVEL:       Barrier crossing, cell type specificity     │
│  ORGANISM LEVEL:     Immune response, pathogenesis               │
│  POPULATION LEVEL:   Transmission, herd immunity, evolution      │
│                                                                  │
│  TROPISM DETERMINANTS:                                           │
│  1. Receptor expression (necessary)                              │
│  2. Co-receptor expression (necessary for some)                  │
│  3. Cellular replication machinery compatibility                 │
│  4. Restriction factor landscape                                 │
│  5. Innate immune signaling in that cell type                    │
└──────────────────────────────────────────────────────────────────┘
```

---

## Receptor Usage — The First Gate

Receptors determine which cells a virus can attach to. They are not "virus receptors"
by design — they are normal cellular proteins co-opted by viruses.

```
  VIRUS             RECEPTOR              CO-RECEPTOR       CELL TYPE TARGETED
  ─────             ────────              ───────────       ──────────────────
  HIV-1             CD4                   CCR5 / CXCR4      CD4+ T cells, macrophages
  SARS-CoV-2        ACE2                  TMPRSS2           Type II pneumocytes, gut
  Influenza A/B     Sialic acid (α-2,6)   —                 Upper resp. epithelium
  Influenza (avian) Sialic acid (α-2,3)   —                 Lower resp., waterfowl gut
  Rabies            AChR (nAChR), NCAM,   —                 Neurons, muscle
                    p75NTR
  Poliovirus        PVR (CD155)           —                 Motor neurons, gut epithelium
  EBV               CR2 (CD21)            —                 B lymphocytes
  CMV               PDGFR-α, integrins    NRP2              Fibroblasts, endothelium
  HSV-1             Nectin-1, HVEM        —                 Epithelium, neurons
  Rhinovirus C      CDHR3                 —                 Ciliated airway epithelium
  Measles           CD46 (vaccine)        —                 Immune cells, epithelium
                    CD150 (SLAM) (wild)
  HPV               α6 integrin, HSPG     L2-EGFR           Keratinocytes
  Ebola             NPC1                  (endosomal)       Dendritic cells, macrophages
  Adeno-assoc virus AAVR (KIAA0319L)      various           Broad (type depends on capsid)
```

### ACE2 and SARS-CoV-2 Tropism

```
  ACE2 expression levels across tissues (human):
  ────────────────────────────────────────────────
  Very high: small intestine enterocytes, kidney tubular cells
  High:      nasal goblet cells, type II alveolar cells, colon enterocytes
  Moderate:  heart, liver, testis
  Low:       brain, immune cells

  This distribution explains:
  - Respiratory entry (nasal + alveolar ACE2)
  - GI symptoms (intestinal ACE2)
  - Multi-organ complications (cardiac, renal involvement)
  - Male reproductive outcomes (testicular ACE2 — still studied)

  TMPRSS2 co-factor:
  ─────────────────
  Serine protease; cleaves S at S2' site enabling direct plasma membrane fusion
  High in airways (where S entry is most efficient)
  Camostat (TMPRSS2 inhibitor) tested as antiviral — limited clinical success
  Cells without TMPRSS2 use endosomal cathepsins (slower, less efficient)
```

---

## Receptor Evolution — The Red Queen at the Molecular Level

Viruses evolve to use receptors; hosts evolve receptor variants to resist. This
arms race shapes protein sequences on both sides.

```
  EXAMPLE: HIV and CCR5
  ──────────────────────
  CCR5Δ32: 32-nucleotide deletion in CCR5 gene → truncated protein
  Homozygous CCR5Δ32 (1-2% North Europeans): highly resistant to HIV-1 infection
  Heterozygous: slower progression
  CCR5Δ32 frequency elevated in Northern Europe:
    Possible positive selection: unclear agent (plague? smallpox?)
    Genetic drift also possible (founder effect)

  Timothy Ray Brown ("Berlin patient"): cured of HIV by bone marrow transplant
  from CCR5Δ32/Δ32 donor → CCR5-negative immune system → HIV reservoir eliminated
  (Two subsequent patients: City of Hope and London patient similarly treated)

  EXAMPLE: TRIM5α
  ────────────────
  TRIM5α: cytoplasmic restriction factor; recognizes retroviral capsids in cytoplasm
  → Premature uncoating → abortive infection
  Human TRIM5α: blocks N-MLV (murine virus) but NOT HIV-1
  Rhesus TRIM5α: blocks HIV-1 efficiently
  → Single amino acid differences in the capsid-binding SPRY domain determine specificity
  → Ongoing arms race between retroviral capsids and TRIM5α
```

---

## Innate Immune Sensing — The Second Gate

Even if a virus gets inside a cell, innate sensors may detect it:

```
  PATTERN RECOGNITION RECEPTORS (PRRs):
  ────────────────────────────────────────
  RIG-I (DDX58):    cytoplasmic; detects 5'-triphosphorylated dsRNA/ssRNA
                    Activated by: influenza, Sendai virus, RNA viruses generally
  MDA5 (IFIH1):     cytoplasmic; detects long dsRNA
                    Activated by: picornaviruses, coronaviruses
  cGAS-STING:       cytoplasmic; detects dsDNA
                    Activated by: HSV, HIV (reverse transcription products)
                    HIV capsid normally shields DNA from cGAS until after integration
  TLR7/8:           endosomal; detects ssRNA → activated in plasmacytoid DCs
  TLR9:             endosomal; detects unmethylated CpG DNA (herpesvirus)
  TLR3:             endosomal; detects dsRNA

  SIGNALING OUTCOME:
  ───────────────────
  RIG-I/MDA5 → MAVS (mitochondrial) → IRF3/IRF7 → type I IFN (IFN-α/β)
  cGAS-STING → IRF3/IRF7 + NF-κB → type I IFN + inflammatory cytokines
  TLR signaling → MyD88 or TRIF → IRF3/IRF7, NF-κB → IFN + TNF + IL-6, etc.

  TYPE I INTERFERON RESPONSE:
  ────────────────────────────
  IFN-α/β secreted → binds IFNAR on self and neighboring cells
  → JAK-STAT → ISGF3 (STAT1-STAT2-IRF9) → ISRE promoters → hundreds of ISGs
  (interferon-stimulated genes)

  Key ISGs:
  ISG15:    ubiquitin-like modifier; ISGylates viral and host proteins
  Mx1:      GTPase; blocks nuclear export of influenza RNPs (major antiviral)
  OAS/RNaseL: 2'-5'-oligoadenylate synthetase activates RNase L → RNA degradation
  PKR:      dsRNA-dependent kinase → phosphorylates eIF2α → global translation shutoff
  IFIT1-3:  bind viral RNA caps, impair translation
  TRIM56:   ubiquitin ligase; restricts STING signaling
  APOBEC3G: cytidine deaminase; mutates HIV reverse transcripts
  Tetherin:  prevents release of enveloped viruses from cell surface
```

---

## Restriction Factors — Intrinsic Cellular Antiviral Proteins

Distinct from innate immune signaling; cell-intrinsically expressed:

```
  RESTRICTION FACTOR   TARGET         MECHANISM               VIRAL COUNTERMEASURE
  ─────────────────   ──────         ─────────               ────────────────────
  TRIM5α              Retroviral     Capsid recognition →     Capsid evolution
                      capsids        premature uncoating
  APOBEC3G/H          HIV, others    C→U deamination in       Vif (targets APOBEC3
                                     ssDNA → hypermutation     for proteasomal
                                                               degradation)
  Tetherin (BST-2)    Enveloped      Anchors virus to cell    Vpu (HIV), K5 (KSHV),
                      viruses        surface after budding     ORF3a candidates
  SAMHD1              HIV in         dNTP pool depletion       Vpx (HIV-2/SIV mac)
                      macrophages    → RT can't replicate      induces SAMHD1
                      & DCs                                    degradation
  MxA                 Influenza,     Sequesters viral RNPs    M1 protein co-opt/
                      others                                   evolve around Mx
  IFITM1/2/3          Enveloped      Inhibits membrane fusion  Overcame in H1N1
                      viruses        in endosomes              (2009 H1N1 less
                                                               sensitive to IFITM)
  ZAP (ZC3HAV1)       RNA viruses    Binds CpG-rich RNA →     CpG suppression in
                                     RNA degradation           viral genomes
```

---

## Tropism and Disease: Case Studies

### HIV — CD4 T Cell Depletion

```
  HIV specifically infects CD4+ T helper cells (and macrophages, DCs)
  CD4 T cells are the coordinators of adaptive immunity:
  - Help B cells make antibodies (T follicular helper)
  - Activate cytotoxic CD8 T cells
  - Recruit neutrophils, macrophages to infection sites

  Depletion below 200 cells/μL → AIDS (acquired immunodeficiency syndrome)
  → Opportunistic infections: PCP (Pneumocystis), toxoplasma, CMV, Cryptosporidium
  → AIDS-defining cancers: Kaposi's sarcoma (KSHV), Primary CNS lymphoma (EBV)

  Mechanism of CD4 decline: direct killing + bystander apoptosis + activation-
  induced cell death + CTL killing of infected cells
  Pyroptosis (caspase-1-mediated) in resting CD4 T cells that abortively replicate HIV
  accounts for most CD4 depletion in lymphoid tissue
```

### Poliovirus — Neurotropism

```
  Poliovirus enters orally → gut epithelium (primary replication)
  Most infections: asymptomatic GI infection (>90%)
  In ~1% cases: viremia → crosses blood-brain barrier
  → Infects motor neurons in anterior horn of spinal cord
  PVR (poliovirus receptor, CD155) expressed on motor neurons
  Poliovirus replication → cytolysis → flaccid paralysis

  WHY motor neurons specifically?
  CD155 is expressed broadly BUT viral replication is most effective in neurons
  + neural spread via retrograde axonal transport from gut
  Spinal cord anterior horn: high CD155, susceptible to lytic replication
```

---

## Transmission Routes and Tropism Link

```
  TRANSMISSION ROUTE          ENTRY SITE                 VIRUS EXAMPLE
  ──────────────────          ──────────                 ─────────────
  Respiratory droplets/aer.   Nasal/bronchial epithelium  Influenza, SARS-CoV-2,
                                                           measles, rhinovirus
  Fecal-oral                  GI epithelium              Poliovirus, norovirus,
                                                           rotavirus, HAV
  Sexual / mucosal            Genital mucosa             HIV, HSV-2, HPV, HBV
  Blood-borne                 Monocytes, hepatocytes     HIV, HCV, HBV
  Vector-borne (arthropod)    Skin → bloodstream         Dengue, Zika, West Nile,
                                                           Yellow fever
  Direct contact (skin)       Keratinocytes              HSV-1, HPV (warts)
  Neurological (animal bite)  Peripheral nerve → CNS     Rabies
```

---

## Decision Cheat Sheet

| Question | Key concept |
|----------|-------------|
| Why does flu affect the respiratory tract? | α-2,6 sialic acid distribution |
| Why is HIV specifically immunosuppressive? | CD4+ T cell tropism |
| What prevents HIV from infecting most cells? | TRIM5α + other restriction factors |
| How does a new virus emerge in humans? | Receptor compatibility + restriction factor evasion |
| Why does rabies cause encephalitis? | Retrograde axonal transport to CNS |
| What determines avian flu pandemic risk? | Switch from α-2,3 to α-2,6 sialic acid binding |

---

## Common Confusion Points

**Receptor expression is necessary but not sufficient for infection.** A cell with
the receptor but lacking key replication factors (co-receptors, cellular proteases,
or appropriate nuclear/cytoplasmic machinery) will not support productive infection.
This is why many tissues express ACE2 but are not efficiently infected by SARS-CoV-2.

**Tropism can change during infection.** HIV uses CCR5 (macrophage-tropic R5 virus)
early in infection; after years, CXCR4-tropic (X4) variants emerge that infect naive
T cells. This tropism switch accelerates CD4 T cell depletion and disease progression.

**Innate immune sensing has different kinetics in different cell types.** Plasmacytoid
DCs (pDCs) are specialized interferon factories — they respond to TLR7/9 stimulation
within hours. Conventional cells take longer. Viruses that target pDCs directly
(HIV infects them) or block their IFN production gain a window.

**The distinction between pathogenesis and tropism is conceptual, not physical.**
Pathogenesis (disease) emerges from the combination of viral tropism (what cells are
infected), immune response (which cells arrive and what they do), and the
physiological consequences of disrupting those cells. Two viruses with identical
tropism can cause different diseases based on how the host responds.
