# Vaccines and Immunization

## Vaccine Landscape

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        VACCINE TECHNOLOGY SPECTRUM                           │
│                                                                               │
│  PLATFORM          MECHANISM              EXAMPLES         THERMAL STABILITY │
│  ──────────────────────────────────────────────────────────────────────────  │
│  Live attenuated   Weakened pathogen,     MMR, varicella,  +2–8°C (fragile) │
│                    replicates in host,    OPV, yellow     Freeze-sensitive   │
│                    broad immune response  fever, BCG                         │
│                                                                               │
│  Inactivated/      Killed whole pathogen  IPV, Hep A,     +2–8°C            │
│  whole pathogen    or toxoid             flu (IIV),       More stable        │
│                                          rabies, typhoid                     │
│                                                                               │
│  Subunit/protein   Purified antigen       Hep B, Tdap,    +2–8°C            │
│                    component only         HPV, pertussis,  Adjuvant required │
│                                          meningococcal                       │
│                                                                               │
│  Viral vector      Adenovirus carries     AstraZeneca      +2–8°C           │
│                    antigen gene           (COVID), Ebola   (some ≤ −20°C)   │
│                                          (rVSV), Johnson  Moderate stability │
│                                                                               │
│  mRNA              Lipid nanoparticle     Pfizer-BioNTech  Pfizer: ≤−60°C  │
│                    delivers mRNA →        (COVID),         Moderna: ≤−20°C  │
│                    host cells make        Moderna (COVID)  Ultra-cold chain  │
│                    antigen                                                    │
│                                                                               │
│  DNA plasmid       Plasmid DNA → mRNA     inovio (trials)  +2–8°C           │
│                    → antigen expression   ZyCoV-D (India)  Stable            │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Immunological Mechanism

```
PRIMARY VACCINATION RESPONSE:
  Antigen encountered → innate immunity activation →
  antigen-presenting cells (APCs) process antigen →
  present on MHC II to T-helper cells →
  ├── B cells activated → plasma cells → antibody production (IgM, then IgG)
  ├── CD8+ T cells activated → cytotoxic T lymphocytes (kill infected cells)
  └── Memory B and T cells formed (persist for years-decades)

  Lag: 7-21 days for primary response. Antibody peaks ~4 weeks.

BOOSTER (SECONDARY) RESPONSE:
  Memory cells activated → rapid (days), large, high-affinity antibody
  response. Affinity maturation: B cells in germinal centers compete
  for antigen → higher-affinity variants selected (somatic hypermutation).

CORRELATES OF PROTECTION:
  Antibody titer: most common — serum neutralizing antibody level
  IgG threshold: varies by pathogen
  Limitations: titer doesn't capture T-cell immunity or mucosal IgA
  Mucosal IgA: critical for pathogens entering at mucosa (flu, COVID)
  → Injectable vaccines may induce poor mucosal protection
  → Nasal/oral vaccines (OPV, live flu mist) better for mucosal immunity

ADJUVANTS — enhance immunogenicity of subunit vaccines:
  Alum (aluminum salts): oldest, widely used, Th2 response
  AS01B (GSK): liposome + MPL + QS-21 (Shingrix, RTS,S/AS01)
  MF59 (Seqirus): squalene emulsion (flu vaccines)
  AS03 (GSK): squalene + DL-α-tocopherol + Tween 80
  CpG 1018 (Dynavax): TLR9 agonist (Heplisav-B)
```

## Vaccine Efficacy vs. Effectiveness vs. Impact

```
VACCINE EFFICACY (VE) from RCT:
  VE = 1 − (Attack rate vaccinated / Attack rate unvaccinated)
  VE = 1 − RR
  Example: COVID-19 mRNA: VE ≈ 95% against symptomatic disease (trials)

  Measured under:
  - Ideal conditions (protocol-mandated dosing)
  - Selected population (trial inclusion criteria)
  - Against specific endpoint (often symptomatic disease)
  - Short follow-up window

VACCINE EFFECTIVENESS from observational study:
  Same formula, but measured in real-world conditions:
  - All comers in target population
  - Variable adherence, administration technique
  - Extended follow-up
  - Multiple variants/strains circulating
  Usually lower than efficacy.
  COVID-19 mRNA effectiveness vs. severe disease: ≥90% initially,
  waned to ~70-80% by 6 months against Omicron.

POPULATION IMPACT / EFFECTIVENESS:
  Coverage × Effectiveness × (1 + indirect protection effect)
  Herd protection: vaccinating person A also protects unvaccinated person B
  by reducing probability A infects B.
  At high coverage, total protection exceeds individual effectiveness.

VACCINES THAT DIFFER ON ENDPOINTS:
  Transmission prevention → affects onward spread (herd immunity)
  Symptomatic disease prevention → reduces burden on healthcare
  Severe disease/hospitalization prevention → reduces mortality
  A vaccine can score low on transmission prevention but high on
  severe disease prevention — this matters for policy calculation.
```

## Immunization Schedules

```
US ACIP RECOMMENDED CHILDHOOD SCHEDULE (birth to 6 years):
  Birth:          Hepatitis B (dose 1)
  1-2 months:     HepB (2), DTaP (1), Hib (1), PCV15 (1), IPV (1), RV (1)
  4 months:       DTaP (2), Hib (2), PCV (2), IPV (2), RV (2)
  6 months:       HepB (3), DTaP (3), Hib (3), PCV (3), IPV (3), Flu (1)
  12-15 months:   Hib (4), PCV (4), MMR (1), Varicella (1), HepA (1)
  15-18 months:   DTaP (4)
  4-6 years:      DTaP (5), IPV (4), MMR (2), Varicella (2)

SCHEDULE RATIONALE:
  - Doses timed to maximize immune response (maturation of immune system)
  - Early protection from high-risk pathogens (HepB vertical transmission)
  - Boosters required to maintain protective titers
  - Combination vaccines (DTaP, MMRV) reduce injection burden

ADOLESCENT ADDITIONS:
  11-12 years: Tdap, MenACWY, HPV (series begins)
  16 years:    MenACWY booster, MenB (option)

ADULT SCHEDULE:
  Annual flu, COVID-19 (updated formula)
  Shingrix (RZV) at age 50 (2-dose, VE >90% vs. shingles)
  PCV20 at age 65 (pneumococcal)
  Tdap booster every 10 years
```

## Cold Chain — Supply Chain Operations

```
COLD CHAIN REQUIREMENTS:

  +2–8°C  (standard refrigerator)
    └── Most inactivated, subunit, viral vector vaccines
    └── Many live vaccines (but cannot freeze)

  ≤−20°C  (deep freeze)
    └── OPV (oral polio), varicella stock, some flu vaccines
    └── Moderna COVID-19 mRNA

  ≤−60°C to ≤−80°C  (ultra-cold)
    └── Pfizer-BioNTech COVID-19 mRNA (original formulation)
    └── Required ultra-cold storage equipment globally

COLD CHAIN COMPONENTS:
  Manufacturer → National store → Regional store → District store
  → Health post → Vaccination point

  Each transfer: risk of temperature excursion
  Monitoring: electronic data loggers, vaccine vial monitors (VVM)
  VVM: irreversible color change indicator on vial — shows cumulative
       heat exposure. Invented for low-resource settings.

COLD CHAIN FAILURE MODES:
  Power outages → refrigerator failures → overheating
  Freeze damage: many vaccines freeze-sensitive (alum precipitates
    into clumps, reduced immunogenicity — "Shake Test" to detect)
  Improper packing: ice packs placed against freeze-sensitive vaccines
  "Hot storage" problem: vaccines stored in unrefrigerated homes

OPTIMIZATION PROBLEM:
  Minimize temperature excursions subject to cost, access, coverage constraints.
  This is supply chain optimization under uncertainty — stochastic programming.
  WHO UNICEF track: 10-20% of vaccines arrive compromised in low-income settings.
  "Last mile" is hardest: remote health posts without reliable power.
```

## Vaccine Hesitancy

```
WHO "3 C" MODEL OF VACCINE HESITANCY:
  Confidence:  Trust in vaccine safety, efficacy, health system, governments
  Complacency: Risk of disease perceived as low (familiarity breeds complacency)
  Convenience: Physical access, cost, information availability, time

DRIVERS BY CLUSTER:
  Philosophical/religious:  Personal or religious beliefs against vaccination
  Safety concerns:          Fears about adverse effects (real and imagined)
  Medical mistrust:         Historical abuses (Tuskegee, forced sterilization)
  Information environment:  Social media misinformation amplification
  Structural:               Access barriers (cost, geography, hours)

COMMON HISTORICAL UNFOUNDED FEARS:
  MMR-autism: Wakefield 1998 Lancet paper (fraudulent, retracted 2010)
    Meta-analyses of millions of children: no association
  Thimerosal (mercury preservative): removed from most vaccines 2001
    Autism rates continued rising after removal: no causal link
  "Too many too soon": pediatric immune system can handle thousands
    of antigens simultaneously — 14-vaccine schedule is tiny fraction
    of immune system capacity

RESPONSE STRATEGIES (evidence-based):
  Motivational interviewing > confrontational correction
  Presumptive announcement ("Your child is due for X") > participatory
    ("What vaccines do you want today?") — increases uptake
  Trusted messenger: family physician > public health official > celebrity
  School entry requirements: most effective mandates; philosophical exemptions
    weaken herd protection
  Reminder-recall: reducing friction (appointment reminders) effective for
    complacency, not for confident refusal
```

## GAVI and Global Immunization

```
GAVI (VACCINE ALLIANCE):
  Est. 2000. Public-private partnership: WHO, UNICEF, World Bank,
  Bill & Melinda Gates Foundation, vaccine manufacturers, donor governments.

  Mission: accelerate vaccine access in low-income countries
  Mechanism: advance market commitments (AMCs), co-financing, pooled procurement
  Scale: funded vaccines for 1B+ children, prevented ~17M deaths (est.)
  COVAX: COVID-19 vaccine pooling mechanism (mixed results — dose nationalism)

ADVANCE MARKET COMMITMENTS (AMC):
  Problem: Manufacturers won't invest R&D for diseases primarily of the poor
    (no profitable market)
  Solution: Donor pledges to subsidize purchase of vaccine if developed
    → creates guaranteed demand → justifies R&D investment
  Pneumococcal AMC (2009): first pilot; accelerated availability of PCV13
    for low-income countries

GLOBAL VACCINE COVERAGE (2022 WHO/UNICEF):
  DTP3 (3-dose diphtheria-tetanus-pertussis): 84% globally
  MCV2 (2-dose measles): 74% globally
  Target: ≥95% for measles herd immunity
  ~23M children under-immunized in 2022 (post-COVID setback from ~18M)
```

## Decision Cheat Sheet

| Vaccine question | Key consideration |
|---|---|
| Why live vaccine vs. subunit? | Breadth of immunity (live) vs. safety/stability (subunit) |
| Why adjuvant in a subunit vaccine? | Innate activation needed — pure protein weakly immunogenic alone |
| How many doses and why? | Primary series builds memory; boosters required when titers wane |
| Why not vaccinate immunocompromised with live vaccine? | Risk of vaccine-strain disease; use inactivated alternatives |
| Coverage needed for herd immunity? | p* = 1 − 1/R₀ (measles needs ~93%) |
| Why did mRNA need ultra-cold? | LNP stability; newer formulations now room-temp stable |
| Why cold chain matters for global programs? | Up to 20% vaccines compromised at delivery; VVM monitors this |
| How to address hesitancy? | Motivational interviewing; presumptive announcement; mandates with enforcement |

## Common Confusion Points

**Vaccine safety reporting systems (VAERS, Yellow Card) are not incidence data**: VAERS is passive reporting — anyone can report anything. VAERS counts are not event rates; they require denominator (doses administered) and comparison to background rates. Misuse of VAERS data drives misinformation. The Vaccine Safety Datalink (VSD) uses linked healthcare records — proper epidemiological analysis.

**Live vs. live-attenuated**: Live vaccines are attenuated (weakened), not wild-type virus. Attenuation typically achieved through serial passage in non-human cells. Reversion to virulence is rare but documented (oral polio vaccine → vaccine-derived poliovirus VDPV in under-immunized populations).

**VE ≠ protection against infection**: VE is commonly measured against symptomatic disease (easier to count). Protection against infection (sterilizing immunity) typically lower. A vaccine with VE = 90% against symptomatic disease may have VE = 60% against any infection. Implications for transmission and herd immunity calculations differ.

**Immunosenescence**: Immune response to vaccination weakens with age. Older adults need higher-dose flu vaccines (Fluzone High-Dose) or adjuvanted vaccines (FLUAD) to achieve comparable titers. Shingrix's powerful AS01B adjuvant achieves >90% VE in adults 70+ — notably better than older Zostavax.
