# Viral Disease

## The Big Picture: Baltimore Classification

```
VIRUS CLASSIFICATION BY GENOME → REPLICATION STRATEGY

Class I:   dsDNA          (Herpes, Adeno, Pox)       → nuclear DNA replication (mostly)
Class II:  ssDNA          (Parvovirus, Anellovirus)   → convert to dsDNA first
Class III: dsRNA          (Rotavirus, Reovirus)       → RNA-dependent RNA polymerase (RdRP)
Class IV:  +ssRNA         (Coronaviruses, Flaviviruses,→ mRNA-like, translated directly → RdRP
                           Picornaviruses, Togaviruses)
Class V:   −ssRNA         (Influenza, Paramyxo, Rhabdo,→ RdRP must be packaged (can't translate
                           Filoviruses)                  directly); −strand → +strand → mRNA
Class VI:  +ssRNA retrovirus (HIV, HTLV)              → Reverse transcriptase: RNA → dsDNA → integrates
Class VII: dsDNA w/ RNA   (Hepatitis B)               → Reverse transcriptase step; partially dsDNA

KEY INSIGHT:
  All RNA viruses except retroviruses use host-absent RdRP → major drug target
  Retroviruses use reverse transcriptase → major drug target (NRTIs, NNRTIs, integrase inhibitors)
  DNA viruses often use host DNA machinery (except large dsDNA like herpes)
```

---

<!-- @editor[bridge/P2]: No old-world bridge -- Baltimore classification maps genome type to replication strategy, analogous to how a type system maps data representation to permissible operations -->

## Universal Viral Replication Cycle

```
1. ATTACHMENT: viral surface protein binds specific host receptor
   (receptor specificity = tropism determinant)
   HIV: gp120 → CD4 (T cells, macrophages, DCs) + CCR5/CXCR4 co-receptor
   SARS-CoV-2: Spike (S protein) → ACE2 (lung, heart, gut)
   Influenza: Hemagglutinin (HA) → sialic acid (α2,3: avian; α2,6: human respiratory)
   HSV: glycoproteins gC/gD → heparan sulfate → HVEM/nectin

2. ENTRY: membrane fusion or endocytosis
   pH-independent fusion (HIV, Paramyxo): gp41/F protein at plasma membrane
   pH-dependent fusion (Influenza, Ebola): low pH in endosome triggers HA2 conformational change

3. UNCOATING: capsid removed, genome released to appropriate compartment
   DNA viruses: nucleus (use nuclear pores, except Pox which replicates in cytoplasm)
   RNA viruses: cytoplasm

4. REPLICATION:
   DNA viruses: host DNA polymerase (+ viral polymerase for herpes/pox)
   +ssRNA: ribosomes directly translate → polyprotein → viral RdRP → replication
   −ssRNA: packaged RdRP → +strand → template → −strand amplification
   Retrovirus: RT → dsDNA → nuclear import → integrase → proviral integration
   HBV: pregenomic RNA → RT → dsDNA (reverse transcription with remaining RNA template)

5. ASSEMBLY: viral proteins + genome packaged
   Budding (enveloped): ER, Golgi, or plasma membrane — acquires lipid envelope
   Lytic release (non-enveloped): cell lyses → releases virions

6. RELEASE:
   Influenza: Neuraminidase cleaves sialic acid to release virions from cell surface
   (NA inhibitors: oseltamivir/zanamivir — block release → virion clumping)
```

---

## Influenza: Antigenic Variation

```
GENOME: 8 separate RNA segments (allows reassortment)

SURFACE PROTEINS:
  Hemagglutinin (HA): 18 subtypes (H1-H18) — binds sialic acid receptor
  Neuraminidase (NA): 11 subtypes (N1-N11) — cleaves sialic acid for release

ANTIGENIC DRIFT: Point mutations in HA/NA → gradual change → seasonal flu variants
  → Annual vaccine reformulation (WHO predicts next year's strains)

ANTIGENIC SHIFT: Reassortment between human + animal (avian/swine) flu strains
  → New HA/NA combination → no population immunity → PANDEMIC potential
  Requires co-infection of single cell (often pig: receptor for both avian and human strains)
  1918 H1N1 ("Spanish flu"): ~50M deaths (highest death toll pandemic in history)
  1957 H2N2, 1968 H3N2, 2009 H1N1 (swine) — all shifts

PATHOGENESIS:
  Attaches to upper (α2,6) and lower (α2,3) respiratory sialic acid
  Avian strains (H5N1, H7N9): prefer α2,3 → lung alveolar cells → high pathogenicity
    but poor human-to-human transmission (sparse α2,3 in upper airway)
  HA cleavage by furin (high-path avian) vs respiratory proteases (human) — virulence determinant

DRUG TARGETS:
  M2 ion channel inhibitors: amantadine/rimantadine (all current strains resistant)
  NA inhibitors: oseltamivir (Tamiflu), zanamivir — reduce severity if given early (< 48 hr)
  Cap-dependent endonuclease inhibitor: baloxavir marboxil (newer)
```

---

## SARS-CoV-2 / COVID-19

```
CLASSIFICATION: Betacoronavirus; +ssRNA; largest RNA genome (~30 kb)

ENTRY MECHANISM:
  Spike protein (S): S1 (receptor binding domain, RBD) binds ACE2
  TMPRSS2 (transmembrane serine protease): cleaves S → enables fusion
  Furin cleavage site in S (unique to SARS-CoV-2 vs SARS-CoV-1): ↑ entry efficiency

REPLICATION:
  Positive-sense RNA → translated → ~28 proteins
  NSP12 (RdRP): antiviral target (remdesivir — nucleoside analog, competes with ATP)
  Extensive subgenomic RNAs for structural proteins (S, E, M, N)

VARIANT EVOLUTION:
  RBD mutations (e.g., K417, E484, N501): affect ACE2 affinity + Ab binding
  Delta: ↑ transmissibility (furin site changes), ↑ viral load, partial immune evasion
  Omicron: ~30 mutations in Spike → extensive immune evasion; XBB/BQ1/JN.1 subvariants
  Antigenic distance from original strain: vaccine updates (bivalent → monovalent updated)

IMMUNOPATHOLOGY:
  Most disease severity from immune over-reaction, not direct viral killing
  "Cytokine storm": IL-6, TNF, IL-1β → ARDS, multi-organ dysfunction
  Treatments: dexamethasone (↓ mortality in severe disease), IL-6 inhibitor (tocilizumab)

ANTIVIRALS:
  Paxlovid (nirmatrelvir + ritonavir): Mpro (main protease) inhibitor; ritonavir boosts levels via CYP3A4 inhibition
  Remdesivir: RdRP inhibitor (IV, inpatient)
  Molnupiravir: mutagenic nucleoside analog (↑ mutation rate → error catastrophe)
```

---

## HIV: Retroviral Pathogenesis

```
TROPISM:
  HIV-1 gp120 binds CD4 (primary receptor) + CCR5 or CXCR4 co-receptor
  R5-tropic (CCR5): infects macrophages + resting CD4+ T cells (transmitted strains)
  X4-tropic (CXCR4): infects T cells predominantly (later, more pathogenic)

LIFE CYCLE:
  gp120+gp41 complex → receptor binding → membrane fusion → capsid enters cytoplasm
  Reverse transcriptase (RT): ssRNA → (+)ssDNA → dsDNA (RNase H degrades template RNA)
  Integrase: dsDNA import to nucleus → integration as provirus (permanent, heritable)
  → Transcription (Tat transactivation) → Viral mRNA → Protease cleaves Gag/Gag-Pol polyproteins → mature virion

LATENCY: Integrated provirus in resting CD4+ T cells → invisible to immune system
  Cannot be eradicated with current antiretrovirals (no ART penetrates latent reservoir)
  HIV cure requires eliminating latent reservoir ("shock and kill" or "block and lock" strategies)

CD4 DECLINE:
  Normal CD4 count: 500–1,500 cells/μL
  AIDS diagnosis: CD4 < 200 OR AIDS-defining illness
  Depletion mechanism: direct viral cytopathic effect + CD8 CTL killing of infected cells + bystander apoptosis

ANTIRETROVIRAL DRUG CLASSES (ART):
  NRTI (nucleoside RT inhibitor): tenofovir, emtricitabine, abacavir — chain termination
  NNRTI (non-nucleoside RT inhibitor): efavirenz, rilpivirine — allosteric RT inhibitor
  PI (protease inhibitor): darunavir, atazanavir — block Gag/Pol maturation
  INSTI (integrase strand transfer inhibitor): dolutegravir, bictegravir — block proviral integration
  Entry inhibitors: maraviroc (CCR5 antagonist), enfuvirtide (fusion inhibitor)
  Current standard: 3-drug combination → suppress viral replication to undetectable
  "Undetectable = Untransmittable" (U=U): viral load < 200 copies/mL → no sexual transmission
```

---

## Hepatitis Viruses: Comparison

```
        HBV              HCV               HAV              HEV
Genome  dsDNA (partial)  +ssRNA            +ssRNA           +ssRNA
Trans.  Blood/sexual/    Blood/IV drug/    Fecal-oral       Fecal-oral (Asia)
        perinatal        vertical (rare)
Acute   10%→chronic      ~80%→chronic      Self-limited      Dangerous in pregnancy
Chronic 95% neonatal,    ~80%              Never             Never
        5% adults
Cancer  HCC (HBV DNA     HCC (via          No               No
        integration)     cirrhosis)
Vaccine Yes (recombinant No                Yes              Yes (limited avail.)
        HBsAg, 3 doses)
Antiviral TDF/TAF/entecavir Direct-acting   Supportive       Supportive (ribavirin)
          (not curative— antivirals (DAAs):
          suppress)       SVR12 = cure
                          NS3/4A, NS5A, NS5B

HBV SEROLOGY:
  HBsAg: surface antigen — present in active infection (acute or chronic)
  HBsAb: protective antibody (after vaccination or cleared infection)
  HBcAb IgM: acute infection
  HBcAb IgG: past exposure
  HBeAg: high replication/infectivity
  Window period: HBsAg gone but HBsAb not yet → only HBcAb IgM present
```

---

## Herpesvirus Family: Latency

All herpesviruses (dsDNA) establish **lifelong latency** in specific cell types:

| Virus | Primary disease | Latency site | Reactivation |
|-------|----------------|-------------|--------------|
| HSV-1 | Oral herpes (cold sores) | Trigeminal ganglion | Cold, stress, UV → fever blisters |
| HSV-2 | Genital herpes | Sacral ganglia | Stress, illness → genital ulcers |
| VZV | Varicella (chickenpox) | Dorsal root ganglia | Herpes zoster (shingles) — dermatomal vesicles |
| CMV | Mononucleosis syndrome; severe in immunocompromised (retinitis, pneumonitis, colitis) | Monocytes/macrophages | Reactivation in transplant/AIDS |
| EBV | Infectious mononucleosis (atypical lymphocytosis, Monospot) | Memory B cells | Oncogenic: Burkitt lymphoma (c-MYC translocation), NPC, Hodgkin's, PTLD |
| HHV-8 (KSHV) | Kaposi's sarcoma (AIDS-defining illness), Castleman's disease | B cells | AIDS/immunosuppression |

**Herpesvirus anti-viral drugs**: Acyclovir/valacyclovir (HSV/VZV — need viral thymidine kinase to activate), ganciclovir/valganciclovir (CMV — broader activation, more toxic), foscarnet (pyrophosphate analog — for acyclovir/ganciclovir resistance).

---

## HPV: Oncogenic Mechanism

```
HPV TYPES:
  Low-risk (6, 11): condylomata (genital warts) — E6/E7 don't degrade p53/Rb efficiently
  High-risk (16, 18): cervical cancer (~70%), oropharyngeal cancer, anal cancer, vulvar cancer

ONCOGENIC MECHANISM:
  HPV infects basal epithelial cells (at transformation zone of cervix)
  E6 oncoprotein → binds p53 → ubiquitin-mediated degradation → loss of cell cycle arrest
  E7 oncoprotein → binds Rb (retinoblastoma protein) → releases E2F transcription factor
    → uncontrolled S-phase entry
  Both: genomic instability → accumulation of mutations → invasive carcinoma

PROGRESSION: Normal → CIN 1 (LSIL) → CIN 2 → CIN 3 (HSIL/CIS) → Invasive carcinoma
  CIN 2-3: treated (cryotherapy, LEEP) to prevent invasive disease
  E6/E7 integration into host genome: loss of E2 (viral repressor) → ↑↑ E6/E7 expression

VACCINATION:
  Gardasil 9: targets HPV 6, 11, 16, 18, 31, 33, 45, 52, 58
  VLP (virus-like particle) vaccine — no live virus, no DNA
  ~90% reduction in CIN2-3 if vaccinated before exposure
  Recommended: 9–26 years; shared decision-making 27–45
```

---

## Viral Immune Evasion

| Strategy | Mechanism | Examples |
|----------|-----------|---------|
| MHC I downregulation | TAP inhibition or MHC I degradation → CTL can't see infected cells | HSV ICP47 (blocks TAP), CMV US11/US6, HIV Nef |
| Interferon antagonism | Block IFN signaling to prevent antiviral state | Influenza NS1 (blocks RIG-I), Ebola VP35, COVID-19 NSP3/16 |
| Complement evasion | Viral proteins mimic complement regulators | HSV gC (binds C3b), CMV virion incorporates host CD55/CD59 |
| Latency | Minimal viral gene expression → invisible to immune system | All herpesviruses, HIV provirus |
| Antigenic variation | Rapid mutation of surface proteins | Influenza (drift/shift), HIV (escape mutations in CTL epitopes) |
| Immunosuppression | Direct killing of immune cells | HIV (CD4+ T cell depletion), measles (immune amnesia via CD150) |
| Decoy receptors | Secrete soluble cytokine receptor analogs | Poxviruses (vaccinia encodes numerous immune evasion genes) |

---

## Oncogenic Viruses

```
Viruses cause ~15% of human cancers:

Virus         Genome  Cancer                   Mechanism
──────────────────────────────────────────────────────────────────────
HPV 16/18     dsDNA   Cervical, oropharyngeal, E6→↓p53, E7→↓Rb
                      anal, vulvar
EBV           dsDNA   Burkitt lymphoma,         c-MYC translocation
                      Hodgkin's, NPC, PTLD      (t(8;14)); LMP1 mimics
                                                CD40 (B cell activation)
HBV           dsDNA   Hepatocellular carcinoma  HBx protein disrupts
              (partial)                          DNA repair; viral DNA
                                                integration near oncogenes
HCV           +ssRNA  Hepatocellular carcinoma  Via cirrhosis; NS5A →
                                                cell cycle dysregulation
HTLV-1        +ssRNA  Adult T-cell leukemia/    Tax protein → NF-κB,
              (retro)  lymphoma (ATL)            ↑ CDK4/6, ↑ telomerase
HHV-8 (KSHV) dsDNA   Kaposi's sarcoma,         vFLIP, vCyclin, vIRF1
                      PEL, Castleman's
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why do −ssRNA viruses package RdRP? | They can't be directly translated — ribosomes only read +mRNA. The packaged RdRP makes +sense strand first. |
| Why can't we cure HIV? | Integrated provirus in resting CD4+ T cells is invisible to ART and immune system — latent reservoir |
| Why does influenza reassort easily? | Segmented genome: 8 separate RNA segments can swap between viruses in a doubly-infected cell (especially in swine) |
| Acyclovir doesn't work for CMV — why? | Acyclovir requires phosphorylation by viral thymidine kinase (TK). CMV doesn't encode TK (uses UL97 kinase); ganciclovir is phosphorylated by UL97. |
| How do NA inhibitors work? | Block neuraminidase → virion stuck attached to sialic acid on released cell surface → clumping, reduced spread |
| HCV: "cured" vs "cleared" — what does SVR mean? | SVR12 (sustained virologic response at 12 weeks post-treatment) = undetectable HCV RNA = clinical cure in ~99% of patients |

---

## Common Confusion Points

**Viremia vs viral shedding**
Viremia = virus in blood. Viral shedding = virus released from mucosal surfaces (respiratory, GI, genital). A patient can shed virus without detectable viremia (HSV2 subclinical shedding → sexual transmission). Conversely, viremia can occur without shedding (CMV in immunocompromised).

**Antibodies neutralize but don't always protect**
Neutralizing antibodies (against surface proteins: HA, Spike RBD, gp120 envelope) can block entry. Non-neutralizing antibodies can still contribute via ADCC (NK cells) and opsonization. For HIV, broadly neutralizing antibodies (bnAbs) remain a vaccine goal — difficult due to extreme glycan shield on gp120.

**mRNA vaccines: no DNA, can't alter genome**
mRNA is degraded within hours to days. No reverse transcriptase, no nuclear entry of mRNA, no integration. The concern about LINE-1 retrotransposition of mRNA vaccines has been studied and found negligible at vaccine doses.

**Measles "immune amnesia"**
Measles virus infects and kills B and T memory cells via CD150 → wipes out immunological memory built up over years, leaving individuals vulnerable to previously-encountered pathogens for months to years post-measles infection. This is one reason measles vaccination reduces child mortality broadly, not just from measles directly.
