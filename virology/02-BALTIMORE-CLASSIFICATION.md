# Baltimore Classification System

## The Big Picture

David Baltimore (1971, Nobel 1975) proposed classifying viruses by the relationship
between their genome and mRNA production. This is more fundamental than host range
or disease type because it reveals the replication strategy.

```
┌──────────────────────────────────────────────────────────────────┐
│              BALTIMORE CLASSIFICATION — ALL 7 CLASSES            │
│                                                                  │
│  The Central Question:                                           │
│  "How does the virus produce mRNA from its genome?"              │
│                                                                  │
│  Class I   dsDNA    → mRNA  (like host; use host or viral pol)   │
│  Class II  ssDNA    → dsDNA → mRNA                               │
│  Class III dsRNA    → mRNA  (viral RdRp required)                │
│  Class IV  +ssRNA   = mRNA  (genome IS the mRNA)                 │
│  Class V   -ssRNA   → mRNA  (viral RdRp required for first step)│
│  Class VI  ssRNA-RT → DNA   → mRNA  (reverse transcription)      │
│  Class VII dsDNA-RT → mRNA  (with RT in replication cycle)       │
│                                                                  │
│  KEY DIVISION: RNA vs DNA genome                                 │
│  DNA viruses: generally lower mutation rate, larger genomes      │
│  RNA viruses: very high mutation rate, smaller genomes           │
│  Retroviruses: RNA genome → DNA intermediate → integrates        │
└──────────────────────────────────────────────────────────────────┘
```

---

## Class I: dsDNA Viruses

Genome: double-stranded DNA. Replication uses host DNA polymerase (mostly nuclear)
or viral DNA polymerase (poxviruses, cytoplasmic).

```
  GENOME → TRANSCRIPTION → mRNA → PROTEIN
   (dsDNA)      (cellular RNA pol)

  EXAMPLES AND PROPERTIES:
  ─────────────────────────
  Herpesviruses:
    HSV-1/2 (oral/genital herpes), VZV (chickenpox/shingles),
    EBV (Epstein-Barr, mononucleosis, Burkitt's lymphoma),
    CMV (cytomegalovirus), KSHV (Kaposi's)
    Genome: 125-240 kb linear dsDNA
    Feature: LATENCY — genome maintained as episome in nucleus
    HSV-1 in sensory ganglia, EBV in B cells — can reactivate

  Poxviruses:
    Smallpox (Variola), vaccinia (vaccine strain), monkeypox
    Genome: 130-375 kb; brick-shaped virion
    Cytoplasmic replication (unique for dsDNA) — carries own RNA pol
    Variola: eradicated by vaccination 1980; only natural human disease
    ever eradicated

  Adenoviruses:
    Common cold, epidemic keratoconjunctivitis, hemorrhagic cystitis
    Genome: 26-45 kb; icosahedral, non-enveloped
    Used extensively as gene therapy/vaccine vectors (ChAdOx in COVID vaccines)

  Papillomaviruses:
    HPV; circular dsDNA ~8 kb; integrate into host genome → cervical cancer
    E7 oncoprotein inactivates Rb (cell cycle brake)
    Vaccine (Gardasil) prevents HPV types 16/18 → >95% cervical cancer prevention
```

---

## Class II: ssDNA Viruses

Genome: single-stranded DNA. Must first synthesize complementary strand to form
dsDNA intermediate before transcription.

```
  GENOME (ssDNA) → dsDNA intermediate → mRNA
                   (host DNA pol in nucleus)

  EXAMPLES:
  ─────────
  Parvoviruses:
    B19 (fifth disease in children, aplastic crisis in sickle cell)
    AAV (adeno-associated virus): most used gene therapy vector
    Small: ~5 kb; icosahedral, non-enveloped
    Require host cell in S phase for replication

  Circoviruses:
    PCV2 (porcine circovirus 2): economically important in pigs
    TTV (Torque teno virus): infects essentially all humans, no known disease
    Smallest known viral genomes (~1.7-2.1 kb)
    Circular ssDNA; rolling circle replication
```

---

## Class III: dsRNA Viruses

Genome: double-stranded RNA, always segmented. Must carry their own RdRp because
cells have no dsRNA → mRNA machinery (and dsRNA would trigger innate immune alarm).

```
  GENOME (dsRNA segments) → mRNA (via viral RdRp inside capsid)

  KEY POINT: Transcription occurs INSIDE the intact capsid particle.
  If dsRNA were exposed in cytoplasm, RIG-I/MDA5 would detect it → type I IFN.
  The capsid is a transcription factory that hides the dsRNA from innate sensors.

  EXAMPLES:
  ─────────
  Reoviruses: respiratory/enteric; icosahedral; generally benign
  Rotaviruses: leading cause of pediatric diarrhea worldwide
    11 segments; responsible for ~200,000 deaths/year in children
    Oral vaccine (Rotarix, RotaTeq) effective
  Bluetongue virus: livestock pathogen; 10 segments; vector: Culicoides midges
```

---

## Class IV: +ssRNA Viruses

Genome: positive-sense single-stranded RNA. The genome IS directly translatable —
it serves as mRNA immediately upon entry. This is the largest and most diverse
Baltimore class.

```
  GENOME (+ssRNA) → Translation (directly) → Proteins (including RdRp)
                 ↘ RdRp produces -strand
                 ↘ -strand template → new +strand genomes

  ADVANTAGE: Fast replication — ribosomes translate immediately after entry
             No need to carry RdRp in virion (unlike Class V)
             But: means infected cell starts making protein before innate immune
             response can mobilize

  MAJOR EXAMPLES:
  ────────────────
  Coronaviruses:
    SARS-CoV-2, SARS-CoV-1, MERS-CoV, seasonal HCoV-229E, NL63, OC43, HKU1
    ~30 kb genome — largest known RNA genome (near theoretical limit for RNA)
    Encodes proofreading exonuclease (nsp14 ExoN): unusually low error rate
    for an RNA virus (~10⁻⁶ per base — 10-100× lower than typical RNA viruses)
    Replication occurs in ER-derived double-membrane vesicles (DMVs)

  Flaviviruses:
    Dengue (~390 million infections/year), Zika, West Nile, Yellow fever, HCV
    Positive-sense; icosahedral nucleocapsid + envelope
    Single polyprotein → cleaved by viral + host proteases

  Picornaviruses:
    Poliovirus, rhinovirus (cold), HAV, enterovirus D68, foot-and-mouth
    ~7.5 kb; IRES-mediated cap-independent translation
    Single polyprotein (2A/3C protease cleavage) → 11-13 functional proteins
    Poliovirus replication cycle is only ~6 hours

  Togaviruses/Alphaviruses:
    Rubella, Chikungunya, Ross River
    +ssRNA with 5' cap; non-structural polyprotein + structural polyprotein
    from two ORFs

  Caliciviruses:
    Norovirus (cruise ship vomiting disease), Sapovirus
    Non-enveloped; very stable; low infectious dose (~18 virions for norovirus)
    Major foodborne illness pathogen
```

---

## Class V: -ssRNA Viruses

Genome: negative-sense single-stranded RNA (complementary to mRNA). Cannot be
directly translated. Must carry RdRp in the virion to produce the first +strand
mRNA before any viral proteins can be made.

```
  VIRION contains: Genome (-ssRNA) + RdRp (packaged in virion)
  Upon entry: RdRp transcribes -genome → +mRNA immediately
  +mRNA → viral proteins → replicate genome

  SEGMENTED vs. NON-SEGMENTED:
  ──────────────────────────────
  Non-segmented (Mononegavirales):
    Single -ssRNA molecule, 10-30 kb
    Examples: Rabies virus, Ebola/Marburg, Measles, Mumps, RSV, Nipah
    Linear genome; replication in cytoplasm

  Segmented (Orthomyxoviruses, Bunyaviruses):
    Genome in multiple pieces
    Influenza A/B/C: 8, 8, 7 segments respectively
    Replication in nucleus (unlike most RNA viruses)
    Hantavirus, Rift Valley fever: 3 segments

  INFLUENZA SEGMENTATION — KEY EVOLUTIONARY CONSEQUENCE:
  ────────────────────────────────────────────────────────
  When two different influenza strains infect the same cell:
  → 8 segments from strain A + 8 segments from strain B
  → Random assortment during packaging
  → Up to 2⁸ = 256 possible segment combinations
  → This is REASSORTMENT: antigenic shift (major)

  The 1918, 1957, 1968, 2009 pandemic strains all arose by reassortment
  between human and avian (or swine) influenza strains.
```

---

## Class VI: ssRNA-RT Viruses (Retroviruses)

Genome: positive-sense ssRNA, but NOT directly translated as viral genome.
Replicated through a DNA intermediate via reverse transcriptase.

```
  GENOME (+ssRNA) → Reverse transcription → dsDNA → Integration → mRNA + new genomes

  TWO COPIES of RNA genome per virion (diploid genome)

  REVERSE TRANSCRIPTION STEPS:
  ──────────────────────────────
  1. tRNA primer anneals to PBS (primer binding site) on genomic RNA
  2. RT synthesizes −strand DNA (using RNA as template), with RNase H activity
     destroying the RNA template behind the growing DNA strand
  3. DNA synthesis jumps via LTR sequences (strand transfer)
  4. Second strand DNA synthesis → dsDNA (proviral DNA)
  5. Integrase (IN) catalyzes integration into host chromosome → PROVIRUS

  SIGNIFICANCE OF INTEGRATION:
  ──────────────────────────────
  Once integrated, HIV provirus is part of the host genome.
  Every time the cell divides, the provirus is replicated.
  In latently infected cells: no viral gene expression → invisible to immune system
  → This is why HIV cannot be cured by current antiretrovirals:
    drugs suppress replication but do not eliminate the latent reservoir (resting CD4+ T cells)

  EXAMPLES:
  ─────────
  Lentiviruses: HIV-1, HIV-2, SIV, feline immunodeficiency virus (FIV)
  Simple retroviruses: MLV (mouse leukemia virus), HTLV-1/2 (T-cell leukemia)
  Endogenous retroviruses (ERVs): ~8% of human genome are remnants of ancient
    retroviral integrations; most are defective; some co-opted for host functions
    (syncytins: placental fusion proteins derived from retroviral env genes)
```

---

## Class VII: dsDNA-RT Viruses (Hepadnaviruses)

Genome: partially dsDNA (unusual). Replication involves reverse transcription from
an RNA intermediate (pregenomic RNA).

```
  REPLICATION CYCLE:
  ───────────────────
  dsDNA genome → nucleus → complete dsDNA (cccDNA) → mRNA + pgRNA
  pgRNA → RT → new dsDNA (relaxed circular) → packaged into new virion

  cccDNA (covalently closed circular DNA): persists in nucleus
  → Very hard to eliminate; basis of chronic hepatitis B

  EXAMPLES:
  ─────────
  Hepatitis B virus (HBV):
    3.2 kb; partially dsDNA with a nick
    Infects hepatocytes specifically (NTCP receptor)
    Chronic infection → cirrhosis, hepatocellular carcinoma
    ~250 million people chronically infected worldwide
    Effective vaccine available (recombinant HBsAg)

  Duck hepatitis B, Ground squirrel hepatitis B: animal models
```

---

## Baltimore Classification — Antiviral Implications

```
  DRUG TARGET       CLASSES AFFECTED      EXAMPLES
  ──────────────    ─────────────         ─────────────────
  Viral RdRp        III, IV, V            Remdesivir (SARS-CoV-2, Ebola)
                                          Sofosbuvir (HCV)
                                          Baloxavir (influenza)
  Viral protease    IV (polyprotein)      HIV PI, HCV NS3/4A inhibitors
                    VI (Gag-Pol)          Ritonavir, nirmatrelvir (Paxlovid)
  Reverse           VI, VII               Zidovudine, tenofovir (HIV)
  transcriptase                           Entecavir, tenofovir (HBV)
  Integrase         VI                    Raltegravir, dolutegravir (HIV)
  Capsid assembly   I (herpesviruses)     Letermovir (CMV)
  Neuraminidase     V (influenza)         Oseltamivir, zanamivir
  Viral entry       IV (SARS-CoV-2)       Remdesivir, ritonavir-boosted, bebtelovimab

  RNA virus RNA polymerases: no cellular counterpart → good drug targets
  Reverse transcriptase: no cellular counterpart → good drug target
  DNA viruses using host pol: harder to target selectively (cytotoxic)
```

---

## Decision Cheat Sheet

| Class | Genome | Key feature | Example |
|-------|--------|-------------|---------|
| I | dsDNA | Latency, large genomes | Herpes, pox |
| II | ssDNA | Small, need replicating cells | AAV, parvovirus |
| III | dsRNA | Segmented, transcription in capsid | Rotavirus |
| IV | +ssRNA | Largest class, genome = mRNA | Coronavirus, HIV |
| V | -ssRNA | Must carry RdRp, segmented = reassortment | Influenza, Ebola |
| VI | ssRNA-RT | Integration, latency, no cure | HIV |
| VII | dsDNA-RT | cccDNA persistence | Hepatitis B |

---

## Common Confusion Points

**+ssRNA genome is not the same as cellular mRNA.** It may lack a 5' cap, use IRES
(internal ribosome entry site), or have other non-standard features. "Positive sense"
means the same polarity as mRNA, not that it is structurally identical to mRNA.

**Class VI and Class IV both have ssRNA genomes but are completely different.**
Retroviruses (Class VI) encode reverse transcriptase and use DNA intermediates;
their genome is NOT directly translated as viral mRNA — it is the template for RT.
+ssRNA viruses (Class IV) directly serve as mRNA.

**Segmented genomes and reassortment.** Reassortment requires co-infection of a
single cell by two different strains. Both sets of 8 segments mix during assembly.
This is antigenic shift (large antigenic change) vs. point mutation-based antigenic
drift (small changes). Pandemic influenza = shift; seasonal variation = drift.

**HIV integrase vs. retroviral integration.** Integrase performs two reactions:
3'-processing (cuts 2 nucleotides from each end of viral DNA) and strand transfer
(inserts into host chromosome). INSTI drugs (integrase strand transfer inhibitors)
block the strand transfer step. Integration is irreversible — no enzyme removes
the provirus.
