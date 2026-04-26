# Immune Evasion Strategies

## The Big Picture

Every successful human pathogen has evolved mechanisms to defeat or evade at least
some arm of the immune response. Understanding evasion explains why some viruses
cause chronic infections, why some escape vaccines, and why cytokine storms occur
(immune response overreacts to compensate for virus evasion).

```
┌──────────────────────────────────────────────────────────────────┐
│                IMMUNE EVASION — FULL LANDSCAPE                   │
│                                                                    │
│  TARGET         EVASION STRATEGY                  EXAMPLES       │
│  ─────────      ─────────────────                 ────────       │
│  Innate         Block IFN induction               Flu NS1        │
│  sensing        Degrade sensing molecules         SARS nsp3 PLpro │
│                 Sequester dsRNA from RIG-I        Coronavirus DMVs│
│                 cGAS/STING inhibition             Adenovirus E1A │
│                                                                    │
│  IFN signaling  Block JAK-STAT pathway            Paramyxovirus V│
│                 Degrade STAT1/STAT2               Simian virus 5 │
│                                                                    │
│  MHC-I          Downregulate MHC-I                HIV Nef, HCMV  │
│  presentation   Block TAP (peptide transport)     HSV ICP47      │
│                 Retain MHC-I in ER/Golgi          HCMV US2/US11  │
│                                                                    │
│  CTL killing    Prevent apoptosis                 EBV BHRF1, FLIP │
│                 Target NK cell sensors            HCMV UL18      │
│                                                                    │
│  Antibodies     Antigenic variation               HIV gp120 glycan│
│                 Decoy antigens                    HIV shed gp120 │
│                 Structural shielding              Sialylation    │
│                                                                    │
│  Complement     Complement regulators             HSV gC, EBV    │
│                                                                    │
│  Latency        Hide genome in resting cells      HSV, EBV, HIV  │
└──────────────────────────────────────────────────────────────────┘
```

---

## Innate Immune Evasion

### Blocking IFN Induction

**Influenza NS1:**
```
  NS1 (non-structural protein 1, 26 kDa) is the major innate antagonist of influenza.

  Mechanisms:
  1. RNA binding: NS1 sequesters dsRNA, preventing RIG-I and PKR activation
  2. TRIM25 inhibition: TRIM25 ubiquitinates RIG-I for activation; NS1 binds
     TRIM25 and blocks RIG-I ubiquitination → no IFN signaling
  3. CPSF30 binding: NS1 blocks host mRNA 3'-processing → prevents ISG mRNA
     from being polyadenylated and exported (host cell shutoff)
  4. PI3K activation: NS1 activates PI3K → Akt → prevents premature apoptosis

  Pandemic strains often have NS1 mutations affecting effector binding:
  1918 pandemic H1N1 NS1: highly effective IFN antagonist
  Avian H5N1 NS1: hyperinduces cytokines (overcomes IFN block paradoxically)
```

**SARS-CoV-2 and coronaviruses:**
```
  Multiple evasion mechanisms:
  nsp3 (PLpro): deubiquitinase activity strips ISG15/ubiquitin from
                signaling proteins → blocks IFN signaling
  nsp14 ExoN:   removes dsRNA markers → less RIG-I/MDA5 activation
  nsp15 EndoU:  cleaves viral dsRNA within DMVs before it escapes
  nsp1:         binds ribosome; blocks host mRNA translation
  ORF6:         blocks nuclear import by binding KPNA2 (importin-α)
  ORF3b, ORF9c: additional IFN pathway inhibitors
  DMV formation: sequesters dsRNA from cytoplasmic sensors
```

### Blocking IFN Signaling

Even after IFN is produced, viruses block JAK-STAT signaling:

```
  Paramyxoviruses (V protein):
  Mumps V binds STAT1 and STAT2 → prevents phosphorylation
  PIV2 V: targets STAT2 for proteasomal degradation
  Simian virus 5: degrades STAT1
  Nipah V: nuclear STAT sequestration

  Adenovirus:
  E1A: binds histone deacetylase complexes → represses ISG promoters
  VA RNA I: decoy dsRNA → saturates PKR without activating it

  Result: even if IFN is made, the JAK-STAT cascade is blocked in
  virus-infected cells (autocrine protection) and sometimes neighboring cells
```

---

## MHC Class I Evasion

CTLs (cytotoxic CD8 T cells) recognize infected cells via MHC-I presenting viral
peptides. Viruses that can hide from CTLs can establish persistent infections.

### Downregulation Mechanisms

```
  HIV Nef:
  ─────────
  Nef (negative regulatory factor, ~27 kDa):
  1. Downregulates MHC-I from cell surface: binds AP-1 clathrin adaptor →
     endocytosis of MHC-I → lysosomal degradation
  2. Downregulates CD4 (prevents superinfection, promotes viral release)
  3. Activates infected cell (promotes viral replication)

  Effect: HIV-infected cells present fewer viral peptides → CTL surveillance reduced
  Nef is required for high viral loads and AIDS progression in SIV model
  Nef-deleted SIV: low viral load, no AIDS in macaques

  HCMV (Cytomegalovirus):
  ──────────────────────
  Encodes 4 separate MHC-I evasion genes:
  US2: E3 ubiquitin ligase → retrotranslocates MHC-I from ER to cytoplasm
       → proteasomal degradation
  US3: retains MHC-I in ER (blocks transport to Golgi)
  US6: blocks TAP (transporter associated with antigen processing) →
       peptides cannot enter ER to load onto MHC-I
  US11: similar to US2; different E3 activity; different HLA allele specificity

  HSV ICP47:
  ──────────
  ICP47 binds TAP with very high affinity (Kd ~100 nM for human TAP)
  → Blocks peptide transport into ER → empty MHC-I molecules unstable
  → MHC-I does not reach cell surface
  Murine ICP47 is much weaker — HSV TAP block is human-specific
```

### NK Cell Escape and the "Missing Self" Problem

```
  NK CELLS: MISSING SELF SURVEILLANCE
  ─────────────────────────────────────
  NK cells have activating and inhibitory receptors
  Inhibitory receptors (KIR, NKG2A): bind MHC-I → inhibit killing
  "Missing self": when virus downregulates MHC-I, NK inhibitory signal lost
  → NK cells kill the MHC-I-low cells

  This creates a dilemma for viruses:
  Keep MHC-I high → CTL can see viral peptides
  Reduce MHC-I → NK cells kill the cell

  HCMV SOLUTION — MHC-I DECOYS:
  ───────────────────────────────
  HCMV UL18: viral MHC-I homolog; binds inhibitory receptor LIR-1 on NK cells
             → NK inhibition maintained without presenting viral peptides
  HCMV UL40: encodes peptide that binds HLA-E (non-classical MHC-I) →
             HLA-E inhibits NK cells via NKG2A
  Net effect: HCMV simultaneously downregulates HLA-A/B/C (avoids CTL)
              while providing decoy MHC-I signals (avoids NK)
```

---

## Antibody Evasion

### HIV gp120 Glycan Shield

```
  HIV gp120 OUTER DOMAIN:
  ─────────────────────────
  gp120 is covered in N-linked glycans (~50% of molecular weight)
  These glycans are host-derived (added in ER/Golgi of infected cell)
  → Immune system tolerates "self" glycans
  → gp120 is "camouflaged" by host glycans

  Neutralization epitopes accessible: only the CD4-binding site and a few others
  Key: broadly neutralizing antibodies (bnAbs) can access:
  - CD4 binding site (CD4bs): deep pocket, not easily glycan-shielded
  - MPER (gp41 membrane proximal external region)
  - V2 apex (quaternary epitope on trimer)
  - V3-glycan supersite

  Most antibodies raised during natural infection: strain-specific
  (bind hypervariable loops on gp120 → easy for virus to mutate)
  HIV vaccine challenge: generating bnAbs that access shielded conserved epitopes
```

### Antigenic Variation

```
  INFLUENZA ANTIGENIC DRIFT:
  ───────────────────────────
  Mutations in HA and NA accumulate over time:
  - Random mutations (RdRp error rate ~10⁻⁴)
  - Neutral mutations tolerated on surface loops
  - Mutations at antibody contact residues positively selected (immune escape)

  Key HA antigenic sites (Sa, Sb, Ca1, Ca2, Cb):
  Mutations in these sites prevent antibody binding → seasonal flu vaccine
  needs annual updating

  Antigenic cartography (Smith et al. 2004):
  Map antibody cross-reactivity → visualize antigenic evolution
  H3N2 drift: ~8 amino acid changes per year in antigenic sites
  → Vaccine updated annually by WHO consensus

  INFLUENZA ANTIGENIC SHIFT:
  ───────────────────────────
  Reassortment brings entirely new HA and/or NA subtype
  No pre-existing antibody immunity in population
  → Pandemic potential (see 08-PANDEMIC-BIOLOGY)
```

---

## Latency as Immune Evasion

The ultimate strategy: no viral gene expression = no antigen = immune system
cannot detect or eliminate the infected cell.

```
  HSV LATENCY:
  ─────────────
  Genome: episomal circular dsDNA in sensory neuron nuclei
  Expression: only LAT (latency-associated transcript)
  LAT: sponge for miRNAs that would induce apoptosis? Stabilizes latency?
       Exact function debated
  No viral proteins on cell surface → no CTL recognition
  Neurons: MHC-I expression naturally low → further reduces CTL visibility

  EBV LATENCY:
  ─────────────
  Multiple latency programs:
  Latency 0: no viral gene expression (memory B cells)
  Latency I: only EBNA1 (EBNA1 evades proteasomal processing → no MHC-I presentation)
  Latency II: EBNA1 + LMP1/LMP2 (in germinal center B cells)
  Latency III: all EBV latency antigens expressed (immunoblastic lymphoma profile)
  Switching between programs mediates EBV biology

  HIV LATENCY:
  ─────────────
  Integrated provirus in resting memory CD4+ T cells: transcriptionally silent
  Mechanism: epigenetic repression of LTR (H3K27me3, DNA methylation)
  Low levels of NF-κB and P-TEFb in resting cells → no Tat → no viral transcription
  T cell memory: decades-long lifespan → latent reservoir
  "Shock and kill": HDAC inhibitors or PKC agonists to reactivate + immune clearance
  (Not yet clinically successful at curing HIV)
```

---

## Cytokine Storm — When Evasion Overdrives the Response

Sometimes immune evasion + tissue damage triggers excessive cytokine production:

```
  CYTOKINE STORM MECHANISM:
  ──────────────────────────
  Virus replicates extensively (early evasion of innate response)
  → Large viral antigen load accumulates
  → Innate immune sensors eventually triggered en masse
  → Massive cytokine/chemokine secretion: TNF-α, IL-1β, IL-6, IL-18, IFN-γ
  → Positive feedback loops (cytokines induce more cytokines)
  → Vascular leak, DIC (disseminated intravascular coagulation), multi-organ failure

  Examples where this occurs:
  H5N1 avian influenza: high virus titer in lower respiratory tract
                         before immune response responds → cytokine storm in lung
  COVID-19 severe disease: hyperinflammatory syndrome in some patients
                            IL-6 blocking (tocilizumab) moderately effective
  Ebola: massive viremia → macrophage activation → cytokine storm → shock
  MAS (macrophage activation syndrome): secondary to severe infections generally

  Why? Viruses that evolved to suppress innate immune signaling may trigger
  compensatory responses that overshoot when the innate block is eventually
  overcome or when the adaptive response amplifies.
```

---

## Decision Cheat Sheet

| Immune arm | Key evasion strategy | Example |
|-----------|---------------------|---------|
| IFN induction | Sequester dsRNA, block RIG-I | Flu NS1, SARS-CoV-2 DMVs |
| IFN signaling | Block JAK/STAT | Paramyxovirus V, SARS ORF6 |
| MHC-I / CTL | Downregulate MHC-I | HIV Nef, HCMV US2-US11, HSV ICP47 |
| NK cells | Decoy MHC-I | HCMV UL18, UL40 |
| Antibodies | Glycan shield, antigenic variation | HIV gp120, flu HA drift |
| Adaptive immune memory | Latency | HSV in neurons, EBV in B cells, HIV resting CD4 |

---

## Common Confusion Points

**IFN evasion is not the same as not triggering IFN.** Viruses use several strategies:
(1) prevent IFN from being made (block sensing), (2) block IFN signaling in the same
cell, (3) block IFN signaling in neighboring cells. Some do all three.

**MHC-I downregulation creates a problem with NK cells.** This is why HCMV
evolved decoy MHC-I molecules. Viruses that only downregulate MHC-I without a
backup NK evasion strategy tend to be controlled by NK cells more effectively.

**CTL escape mutations are a major driver of HIV evolution within a patient.**
HIV evolves rapidly in HLA-specific CTL epitopes during infection. The CTL pressure
is strong enough to select for amino acid changes in CTL epitopes within weeks of
infection. This is why HIV diversity within a patient increases over time in immune
pressure-exposed regions.

**Cytokine storm is not "too much immunity."** It is more precisely: excessive
cytokine signaling with inadequate functional antiviral immunity. The cytokines
cause collateral damage without clearing the infection. This is why immunosuppression
(steroids, IL-6 blockers) can help in severe COVID-19 despite the fact that the
patient is fighting a virus.
