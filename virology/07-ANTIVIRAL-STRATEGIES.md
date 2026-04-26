# Antiviral Drugs and Resistance Mechanisms

## The Big Picture

Antiviral drug development faces a core challenge: viruses use host machinery for
most steps of replication. Selectively targeting the virus without harming the host
requires identifying virus-specific targets. The major classes of antivirals map
directly onto stages of the replication cycle.

```
┌──────────────────────────────────────────────────────────────────┐
│               ANTIVIRAL TARGET MAP                               │
│                                                                  │
│  REPLICATION STEP          DRUG CLASS            TARGET EXAMPLES │
│  ─────────────────         ──────────            ─────────────── │
│  Attachment                Entry inhibitors      Maraviroc (HIV) │
│  Membrane fusion           Fusion inhibitors     Enfuvirtide (HIV)│
│  Genome release            Capsid inhibitors     Lenacapavir     │
│  Viral polymerase          NRTIs/NNRTIs/NAs      AZT, Sofosbuvir │
│  RNA replication           RdRp inhibitors       Remdesivir      │
│  Protease cleavage         Protease inhibitors   Lopinavir,      │
│                                                   Nirmatrelvir   │
│  Integrase                 INSTIs                Dolutegravir    │
│  Neuraminidase             NA inhibitors         Oseltamivir     │
│  Capsid assembly           Capsid assembly inhib.Lenacapavir     │
│  Nuclear export            Cap-snatching inhib.  Baloxavir (flu) │
│  Immune evasion block      IFN inducers          Type I IFN      │
│                                                                  │
│  GENERAL PRINCIPLE: virus-specific enzymes are the best targets  │
│  (no host counterpart = selective toxicity)                      │
└──────────────────────────────────────────────────────────────────┘
```

---

## Nucleoside/Nucleotide Analogs (NAs)

The largest and most successful class of antivirals. These are prodrugs that mimic
natural nucleosides/nucleotides and are incorporated by viral polymerases.

### Mechanism

```
  NUCLEOSIDE ANALOG MECHANISM:
  ──────────────────────────────
  1. Drug (modified nucleoside) enters cell
  2. Phosphorylated by cellular kinases to triphosphate form
     (NRTIs need 3 phosphorylations; NtRTIs come pre-phosphorylated at 1 level)
  3. Viral polymerase incorporates the analog instead of natural nucleotide
  4. Chain termination: missing 3'-OH prevents next nucleotide addition
     OR mutagenic incorporation: altered base pairing → mutation accumulation
     OR active site blockade

  KEY: Viral polymerases often have different structural/kinetic properties
  from host DNA polymerases → some analogs are preferentially incorporated
  by viral enzymes → selectivity
```

### Important Nucleoside Analogs by Virus

```
  HIV (NRTIs — Nucleoside RT Inhibitors):
  ─────────────────────────────────────────
  Zidovudine (AZT, ZDV): thymidine analog; chain terminator
                           First approved antiretroviral (1987)
                           Resistance: M184V, TAMs (thymidine analog mutations)
  Lamivudine (3TC): cytidine analog; well-tolerated; also active vs. HBV
                    Resistance: M184V (emerges rapidly; reduces viral fitness)
  Tenofovir (TDF/TAF): adenosine analog; nucleotide (pre-phosphorylated at one level)
                       Backbone of current HIV regimens; also first-line HBV
                       Resistance: K65R (rare; compromises RT processivity)
  Emtricitabine (FTC): cytidine analog; similar to 3TC; combined with tenofovir
  Abacavir (ABC): guanosine analog; HLA-B*57:01 screening required (hypersensitivity)

  SARS-CoV-2 / other RNA viruses (RdRp inhibitors):
  ────────────────────────────────────────────────────
  Remdesivir (GS-5734): adenosine analog; chain terminator for RdRp
                         Active vs. SARS-CoV-2, Ebola, RSV (broad spectrum)
                         Mechanism: incorporated by nsp12 RdRp → terminates
                         strand extension 3 nucleotides after incorporation
                         ("delayed chain terminator" — bypasses ExoN proofreading)
                         Modest clinical benefit in COVID-19 (IV formulation)

  Molnupiravir (EIDD-2801): N4-hydroxycytidine prodrug
                              Mutagenic: incorporated as both C and U → transitions
                              Oral; approved for COVID-19; ~30% hospitalization reduction
                              Concern: potential mutagenicity — ongoing monitoring

  Sofosbuvir (Sovaldi): uridine analog for HCV NS5B (RdRp)
                         Component of Harvoni/Epclusa; curative HCV treatment
                         >95% sustained virologic response (SVR = functional cure)
                         Pan-genotypic activity; resistance uncommon clinically

  HBV (active vs. both HBV RT and HIV RT):
  ────────────────────────────────────────
  Entecavir: guanosine analog; inhibits HBV polymerase initiation, priming,
             and extension; first-line HBV therapy
  Tenofovir (same as for HIV): also first-line; resistance is very rare
  Resistance: HBV resistance mutations overlap with HIV resistance mutations
              (same enzyme RT, different context)

  Herpesviruses:
  ───────────────
  Acyclovir (ACV): guanosine analog; selectively activated by HSV thymidine kinase
                   Only cells with HSV TK phosphorylate ACV → triphosphate form
                   → Incorporated by HSV DNA pol → chain termination
                   HSV TK mutants: no phosphorylation → resistance (in immunocompromised)
                   Resistance rate: <1% in immunocompetent; up to 5% in immunocompromised
  Ganciclovir (GCV): HSV/CMV; activated by HCMV UL97 kinase (similar logic)
                      Valganciclovir (oral prodrug) for CMV retinitis prophylaxis
  Cidofovir: nucleotide analog (pre-phosphorylated); active vs. broad DNA viruses
             without virus-specific kinase requirement; nephrotoxic
  Brincidofovir (CMX001): lipid conjugate of cidofovir; better oral availability
                           Reduced nephrotoxicity; approved for smallpox (tecovirimat also)
```

---

## Non-Nucleoside RT Inhibitors (NNRTIs)

Distinct from NRTIs: do not require phosphorylation; bind allosteric hydrophobic
pocket adjacent to HIV RT active site → lock RT in inactive conformation.

```
  BINDING SITE: NNRTI pocket (non-competitive inhibitor — not competing with nucleotide)

  MECHANISM:
  RT p66 subunit: NNRTI binds ~10 Å from catalytic site
  → Conformational change → thumb and fingers of RT unable to flex properly
  → DNA synthesis impaired (not blocked, but severely slowed)

  KEY NNRTI RESISTANCE MUTATION: K103N
  K103N: most common NNRTI resistance mutation
  Near the NNRTI pocket entrance; K103N blocks pocket access
  Resistant to: efavirenz, nevirapine (first generation)
  Second generation (rilpivirine, etravirine): different binding geometry → K103N does NOT confer resistance

  CLINICAL USE:
  Efavirenz (EFV): once-daily; CNS side effects (vivid dreams, dizziness)
  Rilpivirine (RPV): less side effects; more potent vs. some resistant strains
  Doravirine (DOR): newer; active vs. K103N; few drug interactions
```

---

## HIV Protease Inhibitors

HIV Gag and Gag-Pol polyproteins must be cleaved by HIV PR to produce mature
functional proteins. Protease inhibitors (PIs) mimic the transition state of peptide
cleavage.

```
  HIV PR MECHANISM:
  ──────────────────
  Aspartyl protease; active as homodimer
  Cleaves at Phe-Pro and other hydrophobic junctions in Gag and Gag-Pol
  Without cleavage: immature non-infectious particle

  PI MECHANISM:
  PR recognizes substrate as extended β-strand
  Transition state: tetrahedral carbon at cleavage site
  PIs contain hydroxyethylene or hydroxyethylamine isostere mimicking this
  → Bind PR active site tightly (Kd picomolar)
  → Prevent polyprotein processing → immature non-infectious virions produced

  KEY PIs:
  ─────────
  Lopinavir/ritonavir (Kaletra): lopinavir is the active PI; ritonavir
    is a pharmacokinetic booster (inhibits CYP3A4 → increases lopinavir levels)
    This "pharmacokinetic boosting" strategy used broadly
  Darunavir/cobicistat: current clinical standard
    Darunavir: second-generation PI; active vs. many resistant viruses
    Cobicistat (COBI): CYP3A4 inhibitor (booster; no antiviral activity itself)
  Nirmatrelvir (Paxlovid component): SARS-CoV-2 Mpro (3CL protease) inhibitor
    Mpro is viral-specific aspartyl protease; no human counterpart (human cathepsins
    are structurally distinct) → good selectivity
    Co-formulated with ritonavir (pharmacokinetic booster)
    ~89% reduction in hospitalization if given within 5 days of symptom onset

  RESISTANCE MECHANISMS (HIV PI):
  ─────────────────────────────────
  Primary: mutations at PI binding site (I50V/L, V82A/F, I84V, D30N etc.)
  Secondary: mutations outside active site restore PR activity or
             compensate for fitness cost of primary mutations
  PI resistance requires multiple mutations → harder to achieve than NRTI/NNRTI resistance
```

---

## Integrase Strand Transfer Inhibitors (INSTIs)

HIV integrase performs strand transfer — the final step of viral DNA integration.

```
  MECHANISM:
  ────────────
  Integrase active site contains Mg²⁺ chelating residues (D64, D116, E152)
  INSTIs: chelate the Mg²⁺ ions + bind hydrophobic pocket
          → Displace 3'-processed viral DNA from active site
          → Strand transfer step (not 3'-processing) is blocked

  Current first-line INSTIs:
  ───────────────────────────
  Dolutegravir (DTG): recommended first-line worldwide (WHO)
    Very high genetic barrier to resistance
    Resistance requires R263K (primary) + compensatory mutations
    R263K severely impairs integrase activity → fitness cost very high

  Bictegravir (BIC): similar to DTG; slightly different resistance profile
  Raltegravir (RAL): first approved INSTI; lower genetic barrier (N155H, Q148H)
  Cabotegravir (CAB): long-acting injectable (every 2 months) for treatment + PrEP
```

---

## Neuraminidase Inhibitors (Influenza)

Influenza NA cleaves sialic acid from host glycoproteins. Without NA, newly budded
virions remain anchored to the cell surface — they cannot spread.

```
  NA ACTIVE SITE:
  ───────────────
  Sialic acid binding pocket; highly conserved across influenza A subtypes
  Transition state: sialic acid oxacarbenium ion

  DRUGS:
  ────────
  Oseltamivir (Tamiflu, oral): sialic acid transition state mimic
    Reduces illness duration ~1 day if given within 48h of symptoms
    Reduces hospitalization risk; useful for prophylaxis in high-risk
    Resistance: H275Y mutation in NA (~1% seasonal H3N2, >99% adamantane-resistant H1N1
    strains before 2009; now rare with current seasonal strains)

  Zanamivir (Relenza, inhaled): similar mechanism; less bioavailable; inhaled
  Peramivir (Rapivab, IV): for hospitalized patients
  Laninamivir (Inavir, Japan): long-acting, single dose

  H275Y RESISTANCE:
  ─────────────────
  Seasonal H1N1 2008-2009: near-100% H275Y rate in Northern Hemisphere
  (oseltamivir widely used → selected for H275Y)
  2009 pandemic H1N1: initially oseltamivir-sensitive (different NA background)
  H275Y reduces NA catalytic efficiency but is compensated in some strains
  → Strains with H275Y + compensatory mutations (e.g., I223V) have near-normal fitness
```

---

## Baloxavir — Cap-Snatching Inhibitor

```
  TARGET: influenza PA endonuclease (cap-snatching)
  Influenza RdRp PB2 binds host pre-mRNA 5' cap
  PA cleaves 10-14 nt from host mRNA (capped fragment)
  This fragment serves as primer for viral mRNA synthesis

  Baloxavir marboxil: prodrug; active form is baloxavir acid
  Binds PA endonuclease active site (two-metal mechanism like integrases)
  → Prevents cap-snatching → no viral mRNA priming → no viral gene expression

  ADVANTAGES over oseltamivir:
  - Single oral dose sufficient
  - Different mechanism → no cross-resistance with NA inhibitors
  - Reduces viral load faster

  RESISTANCE:
  I38T/M/F at PA: reduces baloxavir binding; can emerge rapidly in treated patients
  (single point mutation → confers resistance, unlike oseltamivir which needs H275Y
  with fitness cost)
  Resistance concern: limits baloxavir utility in some contexts
```

---

## Broadly Acting Approaches

### Interferon Therapy
```
  Pegylated IFN-α (Pegasys, PegIntron):
  Used for HCV before DAAs (now rarely used)
  Used for HBV (induces HBsAg seroconversion in some)
  Used for selected HIV-AIDS complications

  Mechanism: binds IFNAR → JAK-STAT → ~300 ISGs → antiviral state
  Toxicity: flu-like symptoms, depression, bone marrow suppression
  → replaced by DAAs for HCV where possible

  Intranasal IFN: nasal spray IFN-β for respiratory viruses
  Limited evidence for COVID-19; potential prophylaxis
```

### Monoclonal Antibodies (mAbs)
```
  Therapeutic antibodies that block viral entry:
  ─────────────────────────────────────────────
  HIV: VRC01, N6LS (broadly neutralizing Abs; CD4-binding site)
       Still in trials; used for prevention in infants
  SARS-CoV-2: bebtelovimab (spike RBD); most BA.1 variants resistant
               Bamlanivimab, casirivimab: earlier generation; now obsolete vs. Omicron
  Ebola: mAb114, REGN-EB3, ZMapp — significant survival benefit in trials
  RSV: Palivizumab (prophylaxis in high-risk infants)
       Nirsevimab (Beyfortus): newer; single dose; approved 2023

  Challenge: viral evolution rapidly escapes strain-specific antibodies
  Broadly neutralizing antibodies targeting conserved epitopes: long-term goal for HIV, influenza
```

---

## Decision Cheat Sheet

| Virus | First-line drug(s) | Target | Resistance key concern |
|-------|---------------------|--------|----------------------|
| HIV | TDF/FTC + DTG (3-drug) | RT, integrase | Pre-existing mutations; M184V, R263K |
| HCV | Sofosbuvir + NS5A inhibitor | NS5B (RdRp), NS5A | Rare; pan-genotypic active |
| HBV | Tenofovir or entecavir | HBV RT | Very rare with these agents |
| Influenza | Oseltamivir (within 48h) | Neuraminidase | H275Y (currently rare) |
| HSV/VZV | Acyclovir/valacyclovir | Viral DNA pol | TK mutations (immunocompromised) |
| CMV | Ganciclovir/valganciclovir | Viral DNA pol | UL97 kinase mutations |
| SARS-CoV-2 | Nirmatrelvir/ritonavir | Mpro protease | PA31 mutations emerging |
| SARS-CoV-2 (severe) | Remdesivir (IV) | RdRp | nsp12 resistance rare |

---

## Common Confusion Points

**"Antiviral" does not mean "antibiotic."** Antibiotics target bacteria. Antivirals
target viruses. They work by completely different mechanisms. Antibiotics do not
treat viral infections.

**Nucleoside analogs require phosphorylation to become active.** The drug taken orally
is not the active form. Phosphorylation happens intracellularly. For herpesviruses,
viral thymidine kinase does the first phosphorylation step — which is why acyclovir
has selectivity: only infected cells activate it efficiently.

**Ritonavir in Paxlovid is not for antiviral activity.** Ritonavir inhibits CYP3A4,
the liver enzyme that would rapidly metabolize nirmatrelvir. Without ritonavir
co-dosing, nirmatrelvir would clear so fast it wouldn't reach therapeutic levels.
This pharmacokinetic boosting strategy was invented for HIV PIs.

**NRTI resistance and NNRTI resistance are completely different.** M184V (common
NRTI resistance) does not confer NNRTI resistance. K103N (common NNRTI resistance)
does not confer NRTI resistance. This is why combining one of each provides better
resistance protection than doubling up in the same class.

**"Curing" HCV vs. "treating" HIV — fundamentally different endpoints.** HCV can be
cured (SVR = sustained virologic response = undetectable HCV 12 weeks after treatment
completion = >99% permanent clearance). HIV cannot be cured with current antiretrovirals
(latent proviral reservoir persists indefinitely). The difference: HCV does not
integrate; HIV integration creates a permanent reservoir.
