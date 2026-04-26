# Viral Biology

## The Big Picture

```
BALTIMORE CLASSIFICATION: THE FORMAL VIRAL TAXONOMY
=====================================================

  CONCEPT: Classify viruses by genome type and replication strategy.
  David Baltimore, 1971. The logical framework the field needed.

  Central dogma: DNA → RNA → Protein
  Virus strategy: How does THIS genome get to mRNA (→ protein)?

  ┌──────────────────────────────────────────────────────────────────┐
  │  CLASS │ GENOME      │ STRATEGY              │ EXAMPLES          │
  ├────────┼─────────────┼───────────────────────┼───────────────────┤
  │  I     │ dsDNA       │ Transcription → mRNA  │ Herpes, Adeno,    │
  │        │             │ (like eukaryotes)      │ Pox, HPV          │
  ├────────┼─────────────┼───────────────────────┼───────────────────┤
  │  II    │ ssDNA (+)   │ ssDNA → dsDNA → mRNA  │ Parvovirus, AAV,  │
  │        │             │                       │ Circovirus        │
  ├────────┼─────────────┼───────────────────────┼───────────────────┤
  │  III   │ dsRNA       │ Segmented genome;      │ Rotavirus,        │
  │        │             │ virion RdRp makes mRNA │ Reovirus          │
  ├────────┼─────────────┼───────────────────────┼───────────────────┤
  │  IV    │ ssRNA (+)   │ Genome = mRNA         │ SARS-CoV-2,       │
  │        │             │ (directly translated) │ Poliovirus, HCV,  │
  │        │             │                       │ Dengue, Zika      │
  ├────────┼─────────────┼───────────────────────┼───────────────────┤
  │  V     │ ssRNA (−)   │ Virion RdRp makes      │ Influenza, Ebola, │
  │        │             │ (+) strand first       │ Measles, Rabies,  │
  │        │             │                        │ RSV               │
  ├────────┼─────────────┼───────────────────────┼───────────────────┤
  │  VI    │ ssRNA (+)   │ Reverse transcription │ HIV-1, HIV-2,     │
  │        │ retroviruses│ RNA→DNA → integrates  │ HTLV              │
  ├────────┼─────────────┼───────────────────────┼───────────────────┤
  │  VII   │ dsDNA       │ RNA intermediate       │ Hepatitis B,      │
  │        │ pararetrovir│ (partially dsDNA)      │ Cauliflower mosaic│
  └────────┴─────────────┴───────────────────────┴───────────────────┘

  KEY INSIGHT: The classification predicts what enzymes the virus must
  carry. Class V viruses MUST bring their own RdRp (RNA-dependent RNA
  polymerase) because host cells don't make (−) strand RNA. Class VI
  must bring reverse transcriptase. Class I uses host RNA pol II.
```

---

## Virion Structure

```
  VIRION ANATOMY
  ===============

  MINIMUM COMPONENTS:
  1. Genetic material (DNA or RNA; single- or double-stranded; linear or circular)
  2. Capsid protein shell

  OPTIONAL (but common):
  3. Lipid envelope (from host membrane, with viral proteins)
  4. Matrix proteins (under envelope)
  5. Viral enzymes (RT, integrase, RdRp, helicase, etc.)

  CAPSID ARCHITECTURES:
  ┌────────────────────────────────────────────────────────────────┐
  │ ICOSAHEDRAL (most viruses):                                    │
  │   20 equilateral triangular faces                              │
  │   Mathematically optimal packing for sphere-like protein shell │
  │   Triangulation number (T): determines size/complexity         │
  │   Examples: Adenovirus (T=25), Poliovirus (T=1), AAV (T=1)   │
  │                                                                  │
  │ HELICAL:                                                         │
  │   Protein subunits spiral around nucleic acid                  │
  │   Common in plant viruses (TMV) + enveloped animal viruses     │
  │   Examples: Influenza, Measles, Rabies, RSV                    │
  │                                                                  │
  │ COMPLEX (none of the above):                                   │
  │   Poxviruses: "Brick-shaped"; most complex known               │
  │   Bacteriophage T4: Icosahedral head + helical tail            │
  └────────────────────────────────────────────────────────────────┘

  ENVELOPED vs. NON-ENVELOPED:
  ┌────────────────────────────────────────────────────────────────┐
  │ ENVELOPED:                                                     │
  │   Lipid bilayer from host cell (usually ER or plasma membrane) │
  │   Viral glycoproteins embedded (hemagglutinin, gp120, etc.)    │
  │   Fragile: Disrupted by detergent, drying, stomach acid        │
  │   → Usually transmitted through close contact, respiratory     │
  │   Examples: HIV, Influenza, SARS-CoV-2, CMV, EBV             │
  │                                                                  │
  │ NON-ENVELOPED (naked):                                         │
  │   Capsid directly exposed                                      │
  │   Resistant: Survives on surfaces, stomach acid, detergent     │
  │   → Often fecal-oral transmission; highly contagious           │
  │   Examples: Poliovirus, Norovirus, Rotavirus, Adenovirus, HPV  │
  └────────────────────────────────────────────────────────────────┘
```

---

## Replication Cycles

### Lytic vs. Lysogenic (Bacteriophage)

```
  BACTERIOPHAGE LIFECYCLES (two strategies)
  ===========================================

  LYTIC CYCLE:
  ┌────────────────────────────────────────────────────────────────┐
  │ 1. Adsorption: Phage tail fibers bind specific bacterial       │
  │    surface receptor (LPS, pili, outer membrane protein)        │
  │ 2. Injection: DNA (sometimes RNA) injected into bacterium      │
  │ 3. Early gene expression: Phage takes over host machinery      │
  │ 4. DNA replication: Phage genome amplified                     │
  │ 5. Late gene expression: Capsid proteins, tail fibers          │
  │ 6. Assembly: Phage particles assembled                         │
  │ 7. Lysis: Holins + lysins burst bacterial cell wall            │
  │    Release: 50–200 new phage particles                         │
  │    Time: ~30–60 minutes                                        │
  └────────────────────────────────────────────────────────────────┘

  LYSOGENIC CYCLE (temperate phages):
  ┌────────────────────────────────────────────────────────────────┐
  │ 1. Phage injects DNA                                           │
  │ 2. Integration: Phage DNA integrates into bacterial chromosome │
  │    via site-specific recombination (attB × attP)               │
  │ 3. PROPHAGE: Integrated phage genome silenced                  │
  │    CI repressor: Blocks lytic gene expression                  │
  │ 4. Replication with host: Prophage copied every cell division  │
  │ 5. INDUCTION: UV, mitomycin C, DNA damage                      │
  │    → RecA cleaves CI repressor → lytic cycle begins            │
  │                                                                  │
  │ MEDICAL IMPORTANCE OF LYSOGENY:                                │
  │   Prophages encode many bacterial virulence factors:           │
  │   Shiga toxin: stx1/stx2 on lambdoid phage in E. coli O157   │
  │   Cholera toxin: ctx on CTXφ phage in V. cholerae              │
  │   Diphtheria toxin: tox gene on corynephage β                  │
  │   Scarlet fever toxin: on phage in S. pyogenes                 │
  └────────────────────────────────────────────────────────────────┘
```

### Animal Virus Replication

```
  GENERAL ANIMAL VIRUS REPLICATION CYCLE
  =========================================

  STEP 1: ATTACHMENT (tropism determination)
  Viral surface protein binds specific cell surface receptor
  Examples:
  ─ HIV gp120 → CD4 (helper T cells, macrophages)
  ─ SARS-CoV-2 spike → ACE2 (lung epithelium, gut, kidney)
  ─ Influenza HA → Sialic acid (respiratory tract)
  ─ EBV gp350 → CR2/CD21 (B cells)
  ─ Rabies → nAChR + p75NTR (neurons)

  Receptor binding = tropism = which cells/tissues virus infects

  STEP 2: ENTRY
  Enveloped: Membrane fusion (direct or after endocytosis)
  ─ pH-dependent (influenza: requires endosomal acidification)
  ─ pH-independent (HIV: fuses directly at plasma membrane)
  Non-enveloped: Endocytosis → endosome → pore/disruption

  STEP 3: UNCOATING
  Capsid dissolves in cytoplasm; genome released

  STEP 4: GENOME REPLICATION (location varies by genome type)
  DNA viruses: Usually nucleus (use host DNA pol or own pol)
  RNA viruses: Usually cytoplasm (must bring own RdRp/RT)
  Influenza: Segmented (−)RNA; replicates in NUCLEUS (unusual)
  Poxvirus: Large dsDNA; replicates entirely in cytoplasm (unusual)

  STEP 5: TRANSCRIPTION → TRANSLATION
  mRNA synthesis using genome or host transcription
  Translation at host ribosomes

  STEP 6: ASSEMBLY
  New genomes + capsid proteins → new virions
  Budding (enveloped) or lysis (non-enveloped)
```

---

## Key Viral Examples

### HIV (Class VI)

```
  HIV REPLICATION (covered in immunology/09 — summary)
  ======================================================
  gp120:CD4:CCR5 → membrane fusion → reverse transcriptase → dsDNA
  → Integrase → provirus → transcription + translation → budding
  Unique: Integrates permanently → latent reservoir challenge
  Drug targets: Reverse transcriptase (NRTIs/NNRTIs), Integrase (INSTIs),
               Protease (PIs), Entry (CCR5 antagonist, fusion inhibitor)
```

### Influenza (Class V)

```
  INFLUENZA: THE ANNUAL PROBLEM VIRUS
  =====================================

  STRUCTURE: (−)ssRNA, 8 segments; enveloped
  Surface proteins:
  ─ HA (Hemagglutinin): Binds sialic acid; vaccine target
    18 subtypes (H1–H18) based on amino acid sequence
  ─ NA (Neuraminidase): Cleaves sialic acid → release
    11 subtypes (N1–N11)
  ─ M2: Ion channel; target of amantadine (now largely resistant)

  ANTIGENIC VARIATION:
  Antigenic drift: Gradual mutations in HA/NA (point mutations)
    → Annual vaccine reformulation needed
    → "Original Antigenic Sin" complicates universal vaccines

  Antigenic shift: Sudden change via reassortment
    → Two influenza strains infect same cell (e.g., pig cell)
    → Segments mix: Novel HA+NA combination emerges
    → Population has no immunity → PANDEMIC POTENTIAL
    → 1918 H1N1, 1957 H2N2, 1968 H3N2, 2009 H1N1 (swine)

  NEURAMINIDASE INHIBITORS (antivirals):
  Oseltamivir (Tamiflu), zanamivir (Relenza), baloxavir
  Block NA → new virions can't release from infected cells
  Effective if started early (48h) → reduces duration by 1–2 days

  REPLICATION SUBTLETY:
  Influenza replicates in NUCLEUS — unusual for RNA virus
  Nuclear import: vRNP (viral ribonucleoprotein) → nuclear pore
  Reason: Needs host splicing machinery for M2/NS2 mRNA processing
```

### SARS-CoV-2 (Class IV)

```
  SARS-COV-2: THE EXEMPLAR CLASS IV RNA VIRUS
  =============================================

  GENOME: +ssRNA, ~30 kb, largest RNA viral genome known
  Proteins: 4 structural (S, E, M, N) + 16 non-structural (nsp1–16)

  SPIKE (S) PROTEIN:
  ─ Binds ACE2 (angiotensin-converting enzyme 2)
  ─ S1 subunit: RBD (receptor-binding domain) contacts ACE2
  ─ S2 subunit: Fusion machinery
  ─ Furin cleavage site at S1/S2: Contributes to high transmissibility
  ─ TMPRSS2: Host serine protease activates fusion at plasma membrane

  REPLICATION COMPARTMENT: ER-derived double-membrane vesicles
  ─ Replicase complex (RdRp + exonuclease) produces (−) strand then (+)
  ─ ExoN proofreading: Why coronaviruses have low error rate for RNA virus
  ─ ~30 kb genome requires fidelity mechanism (others average 10–15 kb)

  ANTIVIRAL TARGETS:
  ─ Paxlovid (nirmatrelvir/ritonavir): Mpro (main protease) inhibitor
  ─ Remdesivir: Adenosine analogue → RdRp inhibitor; chain terminator
  ─ Molnupiravir: Mutagenic nucleoside → viral error catastrophe
```

---

## Viral Evolution

```
  VIRAL EVOLUTION: RAPID ADAPTATION
  ====================================

  ERROR-PRONE REPLICATION:
  ─ RNA-dependent RNA polymerases (RdRp): ~10⁻⁴ to 10⁻⁵ errors/base/cycle
  ─ DNA polymerases: ~10⁻⁸ to 10⁻¹⁰ errors/base/cycle
  ─ RNA viruses = "quasispecies": Population of related but not identical variants
  ─ Each infected cell produces swarm of mutant genomes

  QUASISPECIES MODEL:
  Not a single viral sequence — a CLOUD of sequences
  Consensus sequence ≠ dominant sequence (may not even exist individually)
  High fitness virus = fit average of the cloud, not any single variant
  Implication: Anti-mutagen drugs (ribavirin) can push past error threshold
    → Lethal mutagenesis → quasispecies goes extinct (viral suicide)

  SELECTIVE PRESSURE:
  Immune selection: Antibodies select for escape mutations in surface proteins
    → Influenza HA antigenic drift; HIV env hypervariability
  Drug selection: Antiviral drugs select for resistance mutations
    → HIV RT resistance (AZT: K65R, M184V)
    → HCV NS5A resistance; SARS-CoV-2 Paxlovid resistance (Mpro mutations)
  Transmission selection: Variants that transmit better outcompete others
    → SARS-CoV-2 Omicron: More infectious, less severe, more immune evasive

  RECOMBINATION:
  RNA viruses: Some recombine (coronaviruses: template switching)
  Influenza: Segment reassortment (more dramatic) → new pandemic strains
  Retroviruses: Frequent recombination during reverse transcription
    → HIV diversity within a single patient
```

---

## Lysogenic Conversion and Phage Ecology

```
  BACTERIOPHAGES: THE MOST ABUNDANT BIOLOGICAL ENTITIES
  =======================================================

  NUMBERS: ~10³¹ phage particles on Earth (10x more than bacteria)
  ~10⁷ phages per mL of ocean water
  Marine phages kill ~50% of bacteria in ocean daily

  PHAGE ECOLOGY:
  "Kill the winner": When a bacterial species becomes too abundant,
  its specific phage amplifies → brings it back down → diversity maintained

  PHAGE THERAPY:
  Using phages to treat antibiotic-resistant infections
  Historically abandoned when antibiotics arrived (1940s)
  Reviving as last-resort therapy for pan-resistant infections
  Challenges: Phage resistance, narrow host range, regulatory
  FDA compassionate use cases: Several documented successes (UC San Diego)

  PHAGE AS MOLECULAR TOOLS:
  λ phage: Classic molecular biology vector (gene cloning)
  M13 phage display: scFv antibody libraries (→ antibody drugs)
  T4 DNA ligase: Essential molecular biology enzyme (from T4 phage)
  Cas proteins: CRISPR-Cas system discovered in bacteria as anti-phage defense
```

---

## Decision Cheat Sheet

| Virus Type | Genome | Needs Own Polymerase? | Example |
|-----------|--------|----------------------|---------|
| Class I dsDNA | dsDNA | No (host pol II) | Herpesvirus, Adenovirus |
| Class IV (+)RNA | ssRNA | No (genome = mRNA) | SARS-CoV-2, poliovirus |
| Class V (−)RNA | ssRNA | Yes (RdRp essential) | Influenza, measles, Ebola |
| Class VI Retrovirus | ssRNA | Yes (RT + integrase) | HIV, HTLV |
| Enveloped | Lipid bilayer | Fragile (detergent kills) | HIV, influenza |
| Non-enveloped | Protein capsid | Resistant (surfaces, gut) | Norovirus, poliovirus |
| Lytic phage | dsDNA (many) | Kills bacterium rapidly | T4, T7 |
| Lysogenic phage | dsDNA | Integrates silently | Lambda, CTXφ |

---

## Common Confusion Points

**Virus multiplication uses "burst size," not "doubling"**: Bacteria divide (one → two). Viruses burst (one infected cell → hundreds of new virions). The yield per infected cell is the "burst size" — ~100–1000 virions released per infected cell. "Viral doubling time" is not a useful concept; it depends on burst size × host cell replication.

**Antigenic drift vs. antigenic shift**: Drift = small gradual changes in HA/NA by point mutation (→ annual flu vaccine update needed). Shift = sudden large change from reassortment between two influenza strains (→ pandemic potential because no prior immunity). Drift keeps happening; shift is rare but catastrophic when it occurs.

**Enveloped viruses are fragile**: HIV is fragile outside the body (minutes on surfaces). Non-enveloped norovirus survives weeks on surfaces. This is why HIV requires blood/genital contact while norovirus spreads via fomites and aerosolized vomit/feces.

**Latent vs. lysogenic vs. chronic infection**: Lysogenic = phage DNA integrated into bacterial chromosome. Latent = virus genome hidden in host cells, not actively replicating (HSV in neurons, HIV in CD4 memory T cells). Chronic = virus replicating continuously at low level (HBV, HCV before cure). These are distinct biological states.
