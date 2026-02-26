# 02 — Antivirals & Vaccines

## Antiviral Drug Classes, HIV/Influenza/Herpes/HCV/HBV, Vaccine Platforms

---

**Systems Bridge:** The viral replication cycle is a pipeline with discrete stages, each a potential drug target: attachment → entry → uncoating → replication → assembly → release. Antivirals block specific pipeline stages — entry inhibitors block the handshake; polymerase inhibitors (NRTIs, NNRTIs, NS5B inhibitors) block the core replication transform; protease inhibitors block the post-translation processing step; integrase inhibitors block the write to the host genome; neuraminidase inhibitors block the release/egress step. This staging also explains why drug resistance is stage-specific: a mutation in the RT active site confers NRTI resistance without affecting entry or integration.

Vaccine platforms map directly to deployment strategies for code that needs to run in a new environment:

```
Platform          Analogy                         Mechanism
──────────────────────────────────────────────────────────────────────────
Live-attenuated   Full build, reduced privileges  Whole pathogen, weakened
(MMR, varicella,  — runs the full program but     (live replication → broad
oral polio)       throttled; can revert           cellular + humoral immunity)

Inactivated       Snapshot / read-only image      Killed pathogen (no
(flu shot, IPV,   — cannot replicate or evolve;   replication); less durable
Hep A)            very stable                     immunity; often need boosters

Subunit/protein   API surface only — just the     Antigen protein alone (no
(Hep B, HPV,      interface that triggers the     genome, no replication);
pertussis acell.) response, no internal state     highly specific, safe

mRNA (COVID-19    JIT-compiled instruction set:   mRNA delivered → host cells
Pfizer/Moderna)   ship the code, let the host     manufacture the antigen
                  run it; transient, no           transiently → immune response
                  persistence after execution

Viral vector      Container-based delivery:       Adenovirus vector carries
(COVID-19 J&J,    pack your payload in a          antigen gene; vector is
Ebola)            standard container that the     the delivery mechanism, not
                  host already knows how to       the antigen itself
                  execute
```

## Big Picture: Antiviral Target Map

```
┌──────────────────────────────────────────────────────────────────────────┐
│              ANTIVIRAL DRUG TARGETS (by viral life cycle stage)          │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ENTRY / ATTACHMENT                                                      │
│    Fusion inhibitors: enfuvirtide (HIV gp41), maraviroc (CCR5 antagonist)│
│    Neuraminidase inhibitors: prevent release + re-entry (influenza)      │
│    Omalizumab/REGN-COV2: antibodies blocking receptor binding           │
│                                                                          │
│  REVERSE TRANSCRIPTASE (RNA → DNA)                                      │
│    NRTIs: chain terminators (lack 3'-OH for extension)                  │
│    NNRTIs: allosteric, non-competitive RT inhibitors                     │
│    (HIV-specific; also HBV uses RT to synthesize pgRNA → DNA)           │
│                                                                          │
│  INTEGRATION (HIV integrase)                                             │
│    INSTIs: block strand transfer into host chromosome                   │
│                                                                          │
│  VIRAL PROTEASE                                                          │
│    HIV protease inhibitors (PIs): polyprotein cleavage blockade         │
│    HCV NS3/4A protease inhibitors (-previr)                             │
│    SARS-CoV-2 3CL protease: nirmatrelvir                               │
│                                                                          │
│  POLYMERASE / REPLICATION                                                │
│    Nucleoside/tide analogs: acyclovir (HSV TK-activated), ganciclovir   │
│    HCV NS5B: sofosbuvir (-buvir)                                        │
│    Influenza PB2: baloxavir                                             │
│    COVID-19 RdRp: remdesivir                                            │
│                                                                          │
│  NS5A PROTEIN (HCV replication complex)                                 │
│    NS5A inhibitors (-asvir): daclatasvir, ledipasvir, velpatasvir       │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 1. HIV Antiretroviral Therapy

### HIV Life Cycle → Drug Targets

```
1. Attachment: gp120 binds CD4 + CCR5/CXCR4 co-receptor
2. Fusion: gp41 hairpin → membrane fusion → viral core entry
3. Reverse transcription: RNA → DNA (by viral RT, error-prone → mutation rate)
4. Nuclear import + Integration: IN (integrase) catalyzes strand transfer
5. Transcription: host RNA pol II transcribes proviral DNA
6. Translation + Processing: viral proteases cleave Gag/Pol polyproteins
7. Budding + Maturation: immature virions → infectious particles

Drug targets:
  Step 1: CCR5 antagonist (maraviroc)
  Step 2: Fusion inhibitor (enfuvirtide)
  Step 3: NRTI/NNRTI
  Step 4: INSTI
  Step 6: PI
```

### Drug Classes

**NRTIs (Nucleoside/Nucleotide Reverse Transcriptase Inhibitors):**
- Require intracellular phosphorylation (nucleoside → triphosphate)
- Lack 3'-OH → chain termination
- Tenofovir (TDF/TAF), emtricitabine (FTC), abacavir (ABC), lamivudine (3TC), zidovudine (AZT)
- TAF (tenofovir alafenamide): prodrug, lower systemic tenofovir → less nephrotoxicity/bone density loss
- ABC + HLA-B*5701 → hypersensitivity (test before prescribing); fatal if rechallenge

**NNRTIs (Non-Nucleoside RTIs):**
- Allosteric pocket in RT, no phosphorylation needed
- Efavirenz (central nervous system effects — "EFV dreams"), rilpivirine (requires food, pH-dependent), doravirine
- Potent CYP3A4 inducers (efavirenz) → major drug interactions

**PIs (Protease Inhibitors):**
- Inhibit HIV protease (aspartyl protease) → immature non-infectious virions
- Darunavir, atazanavir, lopinavir — all boosted with ritonavir or cobicistat
- **Ritonavir/cobicistat** = pharmacokinetic boosters: inhibit CYP3A4 → ↑ PI bioavailability; not used as antivirals at current doses
- Class toxicities: lipodystrophy, insulin resistance, dyslipidemia, GI

**INSTIs (Integrase Strand Transfer Inhibitors):**
- Block integration of viral DNA into host chromosome
- Dolutegravir (DTG), bictegravir (BIC), cabotegravir, raltegravir, elvitegravir
- High genetic barrier to resistance (DTG/BIC): favored first-line
- Dolutegravir: potential neural tube defects if conception in first trimester → counseling needed

**Entry/Fusion Inhibitors:**
- Maraviroc: CCR5 antagonist; requires tropism testing (viral tropism assay for CCR5 vs CXCR4) — only ~70% patients are CCR5-tropic
- Enfuvirtide: SC injection; gp41 fusion inhibitor; rarely used (SC administration burden)

### ART Regimens

```
Current standard (DHHS Guidelines):
  PREFERRED regimens (2024):
    BIC/TAF/FTC (Biktarvy): single-tablet, once daily, high barrier to resistance
    DTG + TAF/FTC (Symtuza-equivalent): dolutegravir-based
    CAB/RPV long-acting (Cabenuva): monthly IM injections — adherence alternative

  2-drug regimens (maintenance):
    DTG + 3TC: virologically suppressed patients; avoid if HBV co-infection (3TC alone insufficient)

Resistance mutations:
  M184V: NRTI (emtricitabine/lamivudine resistance) → also ↑ susceptibility to TDF (advantageous)
  K103N: NNRTI class resistance (efavirenz)
  T315I: "gatekeeper" mutation → INSTI + some other class resistance
  High barrier drugs (DTG/BIC) require multiple mutations → rarely fail virologically

U=U (Undetectable = Untransmittable):
  Virologically suppressed person on ART → zero sexual transmission risk
  PARTNER, PARTNER2, Opposites Attract studies confirmation
```

---

## 2. Influenza Antivirals

**Neuraminidase (NA) inhibitors:**
```
Influenza surface: HA (hemagglutinin, attachment) + NA (neuraminidase, release)

NA function: cleaves sialic acid on host cell surface → releases progeny virions
  If blocked → virus stuck, can't spread to new cells

Drugs: oseltamivir (oral), zanamivir (inhaled), peramivir (IV)
  oseltamivir = Tamiflu: prodrug (ethyl ester) → oseltamivir carboxylate
  Effective vs influenza A and B
  Resistance: H275Y mutation (oseltamivir-specific; zanamivir usually retained)
  Treatment window: within 48h of symptom onset (modest benefit)
  Prophylaxis: close contact exposure, institutional outbreaks
  High-risk indications: elderly, immunocompromised, severe illness, hospitalized
```

**Baloxavir marboxil (Xofluza):**
- Inhibits cap-dependent endonuclease (PA subunit of RNA polymerase complex)
- Prevents viral mRNA synthesis
- Single dose oral; active vs influenza A and B
- PA-I38X mutations reduce susceptibility (particularly common in children, who shed virus longer)

---

## 3. Herpesvirus Antivirals

### Acyclovir — Mechanism (Viral TK Activation)

```
Acyclovir (guanosine analog, no 3'-OH):

1. Enter infected cell
2. Herpes viral thymidine kinase (TK) phosphorylates acyclovir → acyclovir monophosphate
   (HSV/VZV TK is far more efficient than cellular TK → selective toxicity)
3. Cellular kinases phosphorylate to triphosphate → acyclovir-TP
4. Acyclovir-TP:
   a. Competes with dGTP for viral DNA polymerase (much higher affinity than cellular polymerase)
   b. Incorporated → chain termination (no 3'-OH)
   c. Dead-end complex: polymerase + template + acyclovir-TP → irreversible inactivation

Selectivity: depends on viral TK for initial phosphorylation
  TK-deficient mutants → acyclovir resistance (reduced activation)
  TK-intact + DNA polymerase mutation (less common, more virulent)
```

| Drug | Target Virus | Notes |
|------|-------------|-------|
| Acyclovir | HSV1/2, VZV (lower potency) | IV for encephalitis/disseminated; PO for genital/labial |
| Valacyclovir | HSV1/2, VZV | Prodrug (valine ester) → 3–5× ↑ bioavailability vs acyclovir |
| Famciclovir | HSV1/2, VZV | Penciclovir prodrug; PO |
| Ganciclovir | CMV (also HSV less preferred) | CMV UL97 kinase phosphorylates (TK-independent) → triphosphate |
| Valganciclovir | CMV | Ganciclovir prodrug; oral for CMV retinitis/prophylaxis in transplant |
| Foscarnet | CMV (ganciclovir-resistant), HSV (acyclovir-resistant), HHV-6 | Pyrophosphate analog; NO TK needed; blocks pyrophosphate site of viral DNA pol; nephrotoxic, chelates Ca²⁺ |
| Cidofovir | CMV, HSV (acyclovir-resistant), adenovirus | Nucleotide (monophosphate given IV); nephrotoxicity requires probenecid co-administration |
| Letermovir | CMV (prophylaxis in HSCT) | Inhibits CMV terminase complex (novel target, not polymerase); used for prevention |

**CMV resistance:** UL97 mutations (ganciclovir resistance, foscarnet/cidofovir active). UL54 (DNA pol) mutations (cross-resistance ganciclovir + foscarnet). Letermovir-resistant UL56 mutations emerging.

---

## 4. HCV Direct-Acting Antivirals (DAAs)

```
HCV genome (single-strand + RNA):
  5'UTR → core → E1 → E2 → p7 → NS2 → NS3/4A → NS4B → NS5A → NS5B → 3'UTR

Drug targets:
  NS3/4A protease inhibitors (-previr): cleave viral polyprotein; simeprevir, grazoprevir, glecaprevir, voxilaprevir
  NS5B nucleotide polymerase inhibitor (-buvir): sofosbuvir; chain terminator; high barrier to resistance
  NS5A inhibitor (-asvir): replication complex; ledipasvir, velpatasvir, pibrentasvir; low barrier to resistance alone

Pan-genotypic regimens (cover all 6 HCV genotypes):
  SOF/VEL (Epclusa): sofosbuvir + velpatasvir; 12 weeks; all genotypes; cirrhosis OK
  GLE/PIB (Mavyret): glecaprevir + pibrentasvir; 8 weeks (non-cirrhotic GT1–6); renal-safe
  SOF/VEL/VOX (Vosevi): + voxilaprevir; for DAA-experienced patients

Cure rates: >95% with pan-genotypic regimens
  "Cure" = SVR12 (sustained virologic response at 12 weeks post-treatment = undetectable HCV RNA)
  SVR = hepatic fibrosis regression, ↓ HCC risk, ↓ all-cause mortality

Key drug interactions:
  Sofosbuvir is P-gp substrate → rifampin (P-gp inducer) → ↓ SOF → DAA failure
  NS5A inhibitors have significant drug interactions with HIV ART (integrase inhibitors mostly compatible)
```

---

## 5. HBV Antivirals

**HBV replication peculiarity:** RNA → reverse transcriptase → DNA (uses RT like HIV, hence NRTI efficacy).

**Key drugs:**
- **Tenofovir (TDF/TAF):** First-line; nucleotide RT inhibitor; low resistance rate; active vs lamivudine-resistant HBV
- **Entecavir:** Guanosine analog; high barrier to resistance; inactive vs 3TC-resistant HBV (pre-existing mutations)
- **Lamivudine:** High resistance (YMDD mutation); rarely first-line; used when TDF/ETV unavailable
- **Pegylated interferon-α (Peg-IFN):** Finite course (48 weeks); chance of HBsAg loss (~10%); significant side effects (flu-like, depression, cytopenia)

**Treatment goal:** Suppress viral replication (HBV DNA undetectable) → prevent cirrhosis/HCC. NOT curative (cccDNA persists in nucleus as minichromosome → reservoir). HBsAg loss rare.

**HBV co-infection with HIV:** Both tenofovir and emtricitabine/lamivudine are active against HBV → use TDF/TAF + FTC/3TC as NRTI backbone in co-infected patients; stopping these = HBV flare.

---

## 6. SARS-CoV-2 Antivirals

```
Nirmatrelvir/ritonavir (Paxlovid):
  Nirmatrelvir: peptidomimetic inhibitor of 3CL (main) protease (Mpro)
    → Blocks polyprotein cleavage → abortive viral replication
  Ritonavir: pharmacokinetic booster (CYP3A4 inhibitor) → ↑ nirmatrelvir exposure
  Indication: high-risk COVID-19, non-hospitalized, within 5 days of symptom onset
  Efficacy: 89% reduction in hospitalization (EPIC-HR trial in unvaccinated)
  Drug interactions: major (CYP3A4 substrates — statins, immunosuppressants, anticoagulants)
  Rebound: ~10–15% clinical rebound after completing 5-day course (virologic basis unclear)

Remdesivir (Veklury):
  Adenosine nucleotide analog → inhibits viral RdRp (RNA-dependent RNA polymerase)
  Incorporated → premature chain termination + delayed chain termination
  Indication: hospitalized COVID-19 (reduces time to clinical improvement)
  IV formulation limits outpatient use (inhaled form in development)
  Also: approved for COVID-19 outpatient (3-day IV infusion at infusion centers)

Molnupiravir (Lagevrio):
  Ribonucleoside analog (prodrug of N-hydroxycytidine → NHC-TP)
  Incorporated into viral RNA → lethal mutagenesis (error catastrophe)
  Lower efficacy vs Paxlovid; limited to when Paxlovid unavailable
  Theoretical concern: mutagenic to host cells (genotoxicity studies reassuring in practice)

Monoclonal antibodies (COVID):
  Rapidly outdated as variants emerge (immune evasion of spike epitopes)
  Bamlanivimab, casirivimab/imdevimab — inactive vs Omicron and beyond
  Current status: limited/no authorized mAbs for Omicron subvariants (2024)
```

---

## 7. Vaccine Platforms

### Mechanism by Type

```
LIVE-ATTENUATED:
  Pathogen grown under non-optimal conditions → reduced virulence
  Replicates in host → robust innate + T + B response → durable immunity
  Often single dose; mimics natural infection without disease
  Risks: reversion to virulence (rare; OPV → VDPV), contraindicated in immunocompromised
  Examples: MMR (measles/mumps/rubella), VZV (varicella/zoster), BCG, yellow fever, OPV, rotavirus

INACTIVATED (KILLED):
  Whole pathogen killed by chemical or heat
  Humoral response; weaker cellular immunity; no replication risk
  Requires adjuvant + boosters
  Examples: IPV (Salk), influenza (IIV), hepatitis A, rabies

SUBUNIT/RECOMBINANT:
  Specific protein(s) only — no live pathogen
  Recombinant protein expressed in yeast/insect cells/mammalian cells
  VLPs (virus-like particles): assembled protein shells — no nucleic acid; mimic virus structure
  Examples: Hep B (HBsAg in yeast), HPV (VLPs: L1 protein), pertussis (acellular = specific proteins)
  Adjuvants essential: AS04 (alum + MPL) in Cervarix; AS01B (MPL + QS-21) in Shingrix → enhanced response

CONJUGATE:
  Polysaccharide antigens poorly immunogenic (T-independent response only → no memory, no booster effect)
  Conjugated to carrier protein (CRM197 = diphtheria toxoid mutant) → T-dependent response → memory
  Examples: Hib (PRP-T/PRP-CRM), PCV (pneumococcal), MenACWY (meningococcal)

TOXOID:
  Inactivated exotoxin → neutralizing antibodies (anti-toxin, not anti-bacterial)
  Examples: tetanus (TT), diphtheria (DT), Tdap

mRNA VACCINES:
  mRNA encapsulated in lipid nanoparticles (LNPs)
  LNPs → endosomal uptake → mRNA enters cytoplasm → translated by ribosomes → antigen expressed
  Host cells present antigen on MHC I + II → CD8+ and CD4+ T cell + B cell response
  mRNA: degraded within days; does NOT integrate into DNA (no nuclear entry mechanism)
  Pseudouridine modification (Karikó/Weissman Nobel 2023): ↓ innate immune recognition → ↑ stability/translation
  Examples: BNT162b2 (Pfizer-BioNTech), mRNA-1273 (Moderna) — COVID-19; mRNA influenza in trials

VIRAL VECTOR:
  Adenovirus (replication-defective) carries insert gene for antigen
  Infects cells → antigen expressed → immune response
  Examples: ChAdOx1 (Oxford/AstraZeneca COVID-19), Ad26.COV2.S (J&J), rVSV-ZEBOV (Ebola)
  Limitation: pre-existing adenovirus immunity can reduce effectiveness
  Advantage: potent T-cell response

ADJUVANTS — mechanism:
  Alum (aluminum salts): depot effect + NALP3 inflammasome activation → IL-1β → ↑ innate response
  AS04 (alum + MPL): MPL (monophosphoryl lipid A) = TLR4 agonist → NF-κB → T helper activation
  AS01B: MPL + QS-21 (saponin) → Th1-biased response; used in Shingrix, malaria vaccine (RTS,S)
  MF59 (squalene oil-in-water emulsion): DAMP release at injection site → innate activation
  CpG (ODN 1018): TLR9 agonist; Heplisav-B (HBV vaccine for adults) → stronger/faster response
```

---

## 8. Immunization Schedules

### ACIP Childhood Schedule (Key Milestones)

```
Birth:          HepB (dose 1)
2 months:       DTaP, IPV, Hib, PCV15/20, RV (rotavirus), HepB (dose 2)
4 months:       DTaP, IPV, Hib, PCV15/20, RV
6 months:       DTaP, IPV, Hib (if needed), PCV15/20, HepB (dose 3), Influenza (yearly thereafter)
12–15 months:   Hib (booster), PCV (booster), MMR (1), VZV (1), HepA (1)
15–18 months:   DTaP (booster)
18–23 months:   HepA (2)
4–6 years:      DTaP (5th), IPV (4th), MMR (2nd), VZV (2nd)
11–12 years:    Tdap, MenACWY (1st), HPV (2-dose series if starting <15)
16 years:       MenACWY (booster), MenB (if desired, 2-dose)
16–18 years:    HPV (3-dose if started ≥15)
```

### Adult Vaccines

```
Influenza: annually (all adults)
Td/Tdap: Tdap once, then Td every 10 years; Tdap in each pregnancy (27–36 weeks)
Zoster (Shingrix): 2 doses, ≥50 years; preferred over Zostavax (live); >90% efficacy
PCV15/20 or PPSV23: ≥65 years; high-risk conditions earlier
HPV (Gardasil 9): up to age 45 (shared decision making 27–45); closes before exposure ideally
COVID-19: updated annually (bivalent mRNA)
RSV vaccines (Abrysvo, Arexvy): ≥60 years; 2023 FDA approval; also maternal RSVpreF vaccine
```

### Travel Vaccines

```
Yellow Fever: required for some countries (endemic equatorial Africa/Americas); live attenuated; long-lasting; viscerotropic/neurotropic adverse events (rare but severe)
Typhoid: Ty21a (live oral, 4 doses) or Vi polysaccharide (IM, single dose, booster q2y)
Japanese Encephalitis: Asia travelers; Ixiaro (inactivated, 2-dose)
Meningococcal (ACWY + B): required for Saudi Arabia (Hajj); college freshmen; asplenic patients
Rabies: pre-exposure for wildlife workers/lab; post-exposure requires wound care + RIG + vaccine series
Cholera: Vaxchora (live oral, CVD 103-HgR strain); travelers to endemic areas
Hepatitis A: any traveler to endemic area; 2-dose series (Havrix/Vaqta)
```

---

## Decision Cheat Sheet

| Pathogen | Drug of Choice | Mechanism | Duration |
|---------|---------------|-----------|---------|
| HSV encephalitis | Acyclovir IV | TK-activated chain terminator | 14–21 days |
| HSV genital (1st) | Valacyclovir | Prodrug of acyclovir | 7–10 days |
| VZV (shingles) | Valacyclovir or famciclovir | TK-activated | 7 days |
| CMV retinitis | Valganciclovir PO | UL97-activated chain terminator | Induction + maintenance |
| Acyclovir-resistant HSV | Foscarnet | Pyrophosphate analog, no TK needed | 14–21 days |
| Ganciclovir-resistant CMV | Foscarnet or cidofovir | No UL97 needed | — |
| HIV (initial) | BIC/TAF/FTC | INSTI + NRTI dual | Lifelong |
| HCV (any genotype) | GLE/PIB or SOF/VEL | NS3 + NS5A or NS5B | 8–12 weeks |
| HBV | TDF or TAF or entecavir | NRTI (reverse transcriptase) | Long-term/indefinite |
| Influenza A/B | Oseltamivir | Neuraminidase inhibitor | 5 days |
| COVID-19 (high-risk) | Nirmatrelvir/ritonavir | 3CL protease inhibitor | 5 days |

---

## Common Confusion Points

**Acyclovir selectivity mechanism:** Acyclovir is NOT specifically taken up by infected cells — it enters all cells. Selectivity comes from viral TK being much better at phosphorylating acyclovir than cellular TK. CMV has no TK → ganciclovir needed (uses UL97 kinase). Foscarnet bypasses this entirely (no kinase needed).

**Ritonavir's role in Paxlovid:** Ritonavir does NOT add antiviral activity against SARS-CoV-2. It inhibits CYP3A4, which metabolizes nirmatrelvir — boosting its plasma levels 10-fold. Same principle as ritonavir-boosted HIV PIs.

**HCV cure vs HBV suppression:** DAAs cure HCV (SVR12 = permanent, cccDNA is absent in HCV). HBV cccDNA persists despite undetectable serum HBV DNA → stopping therapy usually causes relapse. HCV cure; HBV suppression only.

**mRNA vaccines and DNA:** mRNA never enters the nucleus (no import signal; cytoplasmic translation only). mRNA cannot reverse transcribe into host DNA (human cells lack efficient reverse transcriptase for mRNA; LINE-1 elements can rarely do this but not clinically significant).

**Live vaccines and immunocompromise:** MMR, VZV, yellow fever, BCG, OPV, rotavirus = live → contraindicated in severe immunosuppression (HIV CD4 <200, TNF inhibitors, high-dose steroids, post-HSCT). Inactivated, subunit, mRNA = safe in immunocompromised (may need extra doses for response).

**Adjuvant purpose:** Without adjuvant, purified proteins are poorly immunogenic (B-cell response only, no germinal center, no memory). Adjuvants create "danger signal" context → innate activation → dendritic cell maturation → robust adaptive response. Why alum works is still partially understood; NALP3 inflammasome model dominant.
