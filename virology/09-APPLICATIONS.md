# Viruses as Tools: Phage Therapy and Gene Delivery

## The Big Picture

Viruses are sophisticated molecular machines that evolved to efficiently: find
target cells, enter them, and deliver genetic material. These same properties
make viruses powerful tools for medicine, research, and biotechnology.

```
┌──────────────────────────────────────────────────────────────────┐
│                  VIRUSES AS TOOLS — LANDSCAPE                     │
│                                                                    │
│  GENE THERAPY VECTORS:       RESEARCH TOOLS:                     │
│  ─────────────────────       ────────────────                    │
│  AAV: in vivo gene delivery  Phage lambda: genetic engineering   │
│  Lentivirus: stable insert   Phage T4/T7: protein expression     │
│  Adenovirus: transient       CRISPR delivery                     │
│  expression, vaccines        Reporter gene systems               │
│                                                                    │
│  PHAGE THERAPY:              ONCOLYTIC VIRUSES:                  │
│  ──────────────              ─────────────────                   │
│  Bacteriophage kill           Engineered viruses that            │
│  specific bacteria            selectively kill tumor cells       │
│  Alternative to antibiotics   T-Vec (oncolytic HSV) approved     │
│                                                                    │
│  mRNA VACCINES:              VIRAL DIAGNOSTICS:                  │
│  ─────────────               ──────────────────                  │
│  Lipid nanoparticle (not      qRT-PCR, serology                  │
│  viral but virus-inspired)    Phage display                      │
│  COVID-19 vaccines                                               │
└──────────────────────────────────────────────────────────────────┘
```

---

## Viral Gene Therapy Vectors

Gene therapy requires delivering genetic material into specific cells with:
- High efficiency
- Appropriate cell tropism
- Appropriate expression duration
- Safety (no pathogenicity or insertional mutagenesis)

### Adeno-Associated Virus (AAV) — The Workhorse

```
  BIOLOGY:
  ─────────
  Baltimore Class II (ssDNA)
  Small (~25 nm, ~4.7 kb genome)
  Non-pathogenic in humans
  Requires helper virus (adenovirus, herpesvirus) for productive infection
  Naturally integrates at AAVS1 locus on chromosome 19 (rarely in therapeutic context)
  For gene therapy: recombinant AAV (rAAV) does NOT integrate — forms episomal circles
  → Not permanently integrated (limitation for dividing cells; advantage for safety)

  SEROTYPES AND TROPISM:
  ───────────────────────
  Different AAV serotypes (AAV1-13+) have different capsid proteins → different tropism
  AAV2:  broad; retina, muscle, liver
  AAV5:  CNS, retina
  AAV8:  liver (very efficient)
  AAV9:  CNS (crosses blood-brain barrier); muscle, heart
  AAVrh10: CNS
  Selection of serotype determines which tissues are targeted

  MANUFACTURING:
  ───────────────
  HEK293 cells + transfection with:
  1. Transfer plasmid (therapeutic gene flanked by ITRs — inverted terminal repeats)
  2. Rep/Cap plasmid (replication + capsid proteins)
  3. Helper plasmid (adenoviral helper genes E2A, E4, VA)
  → Three-plasmid transient transfection
  Purification: CsCl ultracentrifugation, iodixanol gradients, ion exchange
  Vector genome (vg) titer: by qPCR, ddPCR, capsid ELISA

  APPROVED AAV GENE THERAPIES (as of 2024):
  ────────────────────────────────────────────
  Glybera (2012, EU only): lipoprotein lipase deficiency; AAV1-LPL; first approved
  Luxturna (2017): RPE65 mutation → Leber congenital amaurosis; AAV2-RPE65; subretinal
  Zolgensma (2019): SMA type 1 (spinal muscular atrophy); AAV9-SMN1; IV; ~$2.1M/dose
  Hemgenix (2022): hemophilia B; AAV5-FIX; liver-targeted; ~$3.5M/dose (one-time)
  Roctavian (2023): hemophilia A; AAVhu37-FVIII
  Elevidys (2023): Duchenne muscular dystrophy; AAV-rh74-microdystrophin

  LIMITATIONS:
  ─────────────
  4.7 kb packaging limit (large genes cannot fit: DMD full-length FVIII)
  Solutions: dual-vector split-intein trans-splicing; mini-genes; high-capacity capsids
  Pre-existing anti-AAV antibodies: ~30-60% of humans have NAbs → exclusion criteria
  Re-dosing: neutralizing antibodies after first dose block repeat administration
  Episomal maintenance: lost in rapidly dividing cells (not suitable for liver
                          in neonates; dividing stem cells)
```

### Lentiviral Vectors

```
  BASIS: HIV genome stripped of pathogenic genes; retains integration machinery
  KEY ADVANTAGE over AAV: stable integration → permanent gene expression in
                           dividing cells

  VECTOR DESIGN:
  ───────────────
  Self-inactivating (SIN) design:
  - 3'-LTR U3 deleted → after integration, LTR promoter inactive
  - Transgene driven by internal promoter (EF1α, PGK, etc.)
  - Cannot produce replication-competent virus (RCL) — safety requirement

  Production: HEK293T cells; four-plasmid (or three-plasmid) system:
  1. Gag/Pol plasmid (structural proteins)
  2. Rev plasmid (RRE-CRM1 export)
  3. VSV-G envelope plasmid (pseudotyped with vesicular stomatitis G protein)
     VSV-G: very broad tropism; infects virtually all mammalian cells
  4. Transfer plasmid (therapeutic gene + ψ packaging signal)

  Pseudotyping with VSV-G:
  Replaces HIV envelope (CD4/CCR5 tropic) with VSV-G
  → Broad tropism; infects many cell types
  → Can be tropism-modified by using other envelopes (Cocal, BaEV, measles env)
    for targeting specific cell types (e.g., hematopoietic stem cells)

  CLINICAL APPLICATIONS:
  ───────────────────────
  Ex vivo gene therapy for:
  - Adenosine deaminase SCID (ADA-SCID): Strimvelis (γ-retroviral vector, not lentiviral);
    Libmeldy (lentiviral) — approved EU
  - β-thalassemia: betibeglogene autotemcel (Zynteglo) — approved 2022
  - Sickle cell disease: lovotibeglogene autotemcel (Lyfgenia) — approved 2023
  - Metachromatic leukodystrophy: atidarsagene autotemcel (Libmeldy)
  - CAR-T cell therapy: lentiviral delivery of chimeric antigen receptor
    (Yescarta, Kymriah, Breyanzi, etc.)

  INSERTIONAL MUTAGENESIS RISK:
  ───────────────────────────────
  Historical: γ-retroviral vector (Moloney MLV-based) trials for ADA-SCID in France
  (2000): 5 of 10 patients developed T-cell leukemia due to integration near LMO2
  (proto-oncogene); promoter-less SIN design dramatically reduces this risk
  Lentiviral SIN vectors: integration not near oncogene promoters;
  integration sites favor gene bodies (less oncogenic potential than γ-retroviruses)
```

### Adenoviral Vectors

```
  BASIS: Adenovirus genome, typically Ad5 or chimp adenovirus (ChAd)
  KEY FEATURE: Transient expression (does not integrate); very high efficiency

  Applications:
  - Vaccines: ChAdOx1 (AstraZeneca COVID-19 vaccine); Ad26.COV2.S (Janssen)
              Ebola vaccine (VSV-EBOLA, rVSV platform); Merck Ad5-HIV
  - Cancer gene therapy: transient expression of therapeutic gene in tumor
  - Research: transient protein expression

  Safety concern: pre-existing anti-Ad5 antibodies (high prevalence globally)
  → Chimp adenovirus serotypes (ChAd63, ChAdOx) avoid human anti-Ad5 immunity
  Rare complication: vaccine-induced immune thrombocytopenia and thrombosis (VITT)
  associated with ChAdOx1-S (AstraZeneca COVID vaccine) — ~1/100,000 cases
```

---

## mRNA Vaccines — Virus-Inspired, Not Viral

The COVID-19 mRNA vaccines are not viral vectors — they use synthetic mRNA in
lipid nanoparticles (LNPs). But the technology is deeply informed by virology.

```
  DESIGN:
  ────────
  Synthetic mRNA: encodes viral antigen (SARS-CoV-2 spike, modified)
  5' cap: N1-methylpseudouridine substituted for uridine → reduced innate immune
           activation (TLR7/8 do not recognize N1-meΨ RNA efficiently)
           → increased translation efficiency
  Codon optimization: human codon usage for maximum expression
  2P mutation in spike: K986P + V987P → stabilizes prefusion conformation
                        (more immunogenic than postfusion spike)

  LNP COMPOSITION:
  ─────────────────
  Ionizable lipid: DSPC analog; forms particles; releases mRNA endosomally
  Helper lipid: DSPC (1,2-distearoyl-sn-glycero-3-phosphocholine)
  Cholesterol: membrane stability
  PEG-lipid: PEGylated lipid; reduces aggregation; extends circulation time

  PFIZER-BIONTECH BNT162b2:
  ──────────────────────────
  Effective particle size: ~80-100 nm
  Ionizable lipid: ALC-0315
  mRNA: 4,284 nucleotides; N1-meΨ modified
  Encoding: full-length SARS-CoV-2 spike with 2P stabilization + furin site removed
  Efficacy (original strain): ~95% against symptomatic disease
  Efficacy (Omicron): lower against infection; maintained ~70-80% vs. severe disease

  ADVANTAGES OF mRNA APPROACH:
  ──────────────────────────────
  Speed: sequence → clinical trial < 100 days possible
  Flexibility: any protein can be encoded; swap insert for new variant
  Safety: mRNA does not integrate; degrades within days
  Manufacturing: cell-free synthesis; scalable
```

---

## Phage Therapy

Bacteriophages as antibiotics — killing pathogenic bacteria with their natural predators.

```
  RATIONALE:
  ──────────
  Antibiotic resistance crisis: >700,000 deaths/year attributable to resistant bacteria
  Phages co-evolved with bacteria over billions of years:
  Each phage strain has a defined host range (usually narrow: one or few bacterial species)
  Phages multiply at site of infection (self-amplifying, unlike antibiotics)
  Resistance can develop, but phages can also evolve

  PHAGE THERAPY HISTORY:
  ───────────────────────
  1917-1920s: d'Herelle; used in WWI; fell out of favor after antibiotics
  Soviet Union: continued development; ELIAVA Institute (Tbilisi) — largest
                phage library in world; commercial phage products available in
                former Soviet states since 1960s
  Western revival: 2010s-present; driven by antibiotic resistance crisis

  KEY CHALLENGES:
  ────────────────
  1. Host range: need to identify phage(s) that kill the specific strain
     (personalized phage therapy: isolate patient's bacteria, find or engineer matching phage)
  2. Phage resistance: bacteria develop resistance rapidly
     Solution: phage cocktails (multiple phages targeting different receptors)
     + adaptive phage therapy (co-evolve phage with patient's bacteria)
  3. Immune system: antibodies can neutralize phages; phages may trigger inflammation
  4. Biofilm penetration: phages need to penetrate biofilm to reach bacteria
  5. Regulatory: no approved phage therapy products in US or EU (compassionate use only)

  NOTABLE CASES:
  ──────────────
  2017: UC San Diego patient with Acinetobacter baumannii (pan-resistant)
        Phage cocktail from UC San Diego + US Navy + Tufts → survival
        First documented successful phage therapy in US modern era
  2019: UK patient with Mycobacterium abscessus (cystic fibrosis patient)
        Engineered phage + 2 natural phages; partial lung recovery

  PHAGE COCKTAIL DESIGN:
  ───────────────────────
  Targets: LPS (O-antigen), capsid proteins, flagella, type IV pili
  Each target: different receptor → phage resistance at target A does not
               confer resistance at target B
  If target is also a virulence factor (e.g., Type IV pili): phage resistance =
  loss of virulence → evolutionary trap for bacteria
```

---

## Oncolytic Viruses

Viruses engineered or selected to preferentially replicate in tumor cells.

```
  RATIONALE:
  ──────────
  Many tumors have defects in antiviral signaling (IFN pathway mutations)
  → Viruses that are sensitive to IFN-mediated restriction will only replicate
    in cells with defective IFN response (i.e., tumor cells in many cases)

  TALIMOGENE LAHERPAREPVEC (T-VEC, IMLYGIC) — FDA APPROVED 2015:
  ──────────────────────────────────────────────────────────────────
  Attenuated HSV-1 with:
  - ICP34.5 deleted (×2): ICP34.5 (RL1) is key neurovirulence + IFN evasion factor
    Tumor cells with PKRI pathway defects still support replication
    Normal neurons cannot be infected (safety)
  - ICP47 deleted: allows MHC-I antigen presentation of viral + tumor antigens
    → Improved CD8 T cell response to tumor
  - GM-CSF inserted: granulocyte-macrophage colony stimulating factor
    → Promotes dendritic cell maturation → anti-tumor immune response

  Indication: unresectable melanoma; direct intratumoral injection
  Mechanism: direct oncolysis + systemic anti-tumor immune response ("abscopal effect")
  Efficacy: ~16% durable response rate; modest OS benefit

  OTHER ONCOLYTIC PLATFORMS:
  ───────────────────────────
  Oncolytic NDV (Newcastle Disease Virus): IV administration; selectively kills
  certain tumors; no approved product yet
  Oncolytic adenovirus: DNX-2401, Delta-24-RGD → glioblastoma trials
  Oncolytic vaccinia: GL-ONC1, JX-594 → various tumors
  Coxsackievirus A21: CAVATAK → melanoma, bladder cancer trials
```

---

## Phage Display — Protein Engineering Tool

```
  PRINCIPLE:
  ──────────
  Protein of interest (e.g., antibody fragment) fused to a phage coat protein
  (typically pIII or pVIII of filamentous phage M13)
  → Each phage "displays" the protein on its surface
  → Phage genome contains the gene encoding that protein
  → Genotype-phenotype linkage: select for binding properties, recover the gene

  BIOPANNING:
  ────────────
  1. Library: 10¹⁰-10¹² different sequences displayed on phage
  2. Incubate with target antigen (protein, cell, whole organism)
  3. Wash away non-binders
  4. Elute bound phage
  5. Amplify by infecting E. coli
  6. Repeat 3-5 rounds
  → Enriches phage displaying high-affinity binders

  APPLICATIONS:
  ─────────────
  Antibody discovery: starting point for therapeutic antibody development
                       Adalimumab (Humira, first fully human antibody drug)
                       discovered by phage display (Nobel-associated, Winter group)
  Peptide library screening: find peptide binders to any target
  Enzyme evolution: select for catalytic activity
  Vaccine antigen identification: biopan against patient sera → find antigens
  Epitope mapping: determine antibody binding sites

  PHAGE DISPLAY IMPACT:
  ──────────────────────
  2018 Nobel Prize in Chemistry: George Smith (phage display) + Gregory Winter
  (therapeutic antibodies via phage display)
  >10 approved antibody drugs discovered by phage display
```

---

## Decision Cheat Sheet

| Application | Vector/Tool | Key advantage | Limitation |
|-------------|-------------|---------------|-----------|
| In vivo gene therapy (liver) | AAV8 | Non-integrating, liver tropism | 4.7 kb limit; pre-existing NAbs |
| In vivo gene therapy (CNS) | AAV9 | Crosses BBB | Same as AAV8 |
| Ex vivo stem cell gene therapy | Lentiviral SIN | Stable integration, divides | Insertional mutagenesis risk |
| Vaccination (COVID) | mRNA-LNP | Fast, flexible, no virus | Cold chain, lipid reactions |
| Vaccination (Ebola, COVID) | Adenoviral | Strong immunogenicity | Anti-Ad5 immunity |
| Antibiotic-resistant infection | Phage therapy | Kill specific bacteria | Host range, regulatory, resistance |
| Melanoma | T-Vec (HSV) | Oncolysis + immune | Low response rate |
| Antibody discovery | Phage display | Huge diversity, selectable | In vitro only |

---

## Common Confusion Points

**AAV gene therapy is not the same as AAV gene editing.** Standard rAAV delivers
a gene that is expressed episomally (no integration). AAV can also be used as a
delivery vehicle for CRISPR components (Cas9 + guide RNA) to achieve precise editing —
but the therapeutic effect is from the editing, not expression of the AAV payload.

**mRNA vaccines do not affect your DNA.** mRNA is a single-stranded ribonucleotide
sequence. It cannot be reverse-transcribed into DNA by cellular machinery (cells
lack reverse transcriptase). It degrades within 1-2 days of injection. The sequence
never enters the nucleus. This is well-established biochemistry, not a claim.

**Phage therapy resistance is manageable but real.** Bacteria can develop resistance
to phages by losing or modifying the surface receptor. However, cocktails of phages
targeting multiple different receptors make simultaneous multi-resistance unlikely.
Additionally, "training" phages against resistant strains continuously (adaptive
phage therapy) is an active area.

**Lentiviral integration and AAV integration are not equivalent risks.** Random
integration (lentiviral or retroviral) has some mutagenesis potential; insertional
oncogenesis occurred with γ-retroviral vectors. Lentiviral SIN vectors have much
lower risk due to both integration site preference (gene bodies, not promoters)
and inactive LTR design. AAV episomal persistence avoids the integration risk
entirely for post-mitotic tissues.

**Oncolytic viruses are not cancer vaccines.** They are different mechanisms.
T-Vec does have an immune-stimulating component (GM-CSF), and some "abscopal" responses
are reported, but T-Vec is primarily a local oncolytic therapy for accessible tumor
deposits, not a systemic therapy. Combining oncolytic viruses with checkpoint
immunotherapy (anti-PD1) is an active area.
