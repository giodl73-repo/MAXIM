# Global Health

## Global Health Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      GLOBAL HEALTH GOVERNANCE ECOSYSTEM                     │
│                                                                             │
│  UN SYSTEM          WHO    UNICEF   World Bank   UNFPA   UNDP               │
│       │             │        │          │          │       │                │
│       └─────────────┴────────┴──────────┴──────────┴───────┘                │
│                               ↕                                              │
│  MULTILATERAL        Global Fund (HIV/TB/Malaria)                            │
│  PARTNERSHIPS        Gavi (vaccines)                                         │
│                      CEPI (epidemic preparedness vaccines)                   │
│                      UNITAID (access to medicines)                           │
│                      Roll Back Malaria                                        │
│                               ↕                                              │
│  BILATERAL            PEPFAR (US), USAID, UK-FCDO, DFID (legacy),           │
│  DONORS               JICA (Japan), KfW (Germany), AUSAID                   │
│                               ↕                                              │
│  PHILANTHROPIC        Gates Foundation, Wellcome Trust,                      │
│  FOUNDATIONS          Rockefeller, Open Philanthropy                         │
│                               ↕                                              │
│  ACADEMICS &          IHME (GBD), LSHTM, Johns Hopkins, UCSF,               │
│  RESEARCH             Harvard T.H. Chan, Oxford                              │
│                               ↕                                              │
│  IMPLEMENTING         MSF, IRC, PIH, CARE, PSI, local NGOs,                 │
│  NGOS                 national health ministries                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## WHO Governance Structure

```
WHO STRUCTURE:
  World Health Assembly (WHA):
    194 member states, meets annually (Geneva, May)
    Sets policy, approves budget, elects Director-General
    Each member state = 1 vote (regardless of size/GDP)

  Executive Board (EB):
    34 member states, meets twice/year
    Implements WHA decisions, nominates DG

  Secretariat:
    ~7,000 staff; HQ Geneva; 6 Regional Offices:
    AFRO (Congo), AMRO/PAHO (Washington), EMRO (Cairo),
    EURO (Copenhagen), SEARO (New Delhi), WPRO (Manila)

  Budget (2022-23): ~$6.1B
    Assessed contributions: member states pay based on GDP/population (~16%)
    Voluntary contributions: earmarked donations (~84%)
    Problem: ~84% voluntary = donors control priorities, undermines WHO independence

DIRECTOR-GENERAL:
  Elected by WHA for 5-year term, maximum 2 terms
  Currently: Dr. Tedros Adhanom Ghebreyesus (since 2017)
  First African DG. Ethiopian public health background.
  COVID-19 controversy: timing of PHEIC declaration (Jan 30, 2020 vs. earlier);
  China political sensitivity; delayed international travel advice.
```

## Measuring Global Health Burden — DALY Methodology

```
DALY = DISABILITY-ADJUSTED LIFE YEAR
  One DALY = one year of healthy life lost
  DALYs = YLL + YLD

  YLL (Years of Life Lost due to premature mortality):
    YLL = N × L
    where N = number of deaths, L = expected years lost
    L = life expectancy at age of death (GBD uses standard life table)
    Standard life expectancy: 88.9 years for females (Japan reference)
    Male/female unified standard: 88.9 years for both (GBD 2010+)

    Example: Death at age 30 → L ≈ 58.9 years
    YLL = 1 × 58.9 = 58.9 DALYs

  YLD (Years Lived with Disability):
    YLD = P × DW × L
    where P = prevalent cases, DW = disability weight (0-1), L = duration
    DW ranges from ~0 (near-perfect health) to 1 (death)

    Disability weights from multi-country surveys:
    Mild hearing loss: ~0.01
    Moderate depression: ~0.16
    Severe stroke (long-term consequences): ~0.32
    Dementia (moderate): ~0.38
    AIDS (before ART): ~0.582

    DW IS A UTILITY FUNCTION over health states.
    0 = perfect health, 1 = death. Additive.
    Connection to decision theory: DW is a health utility;
    DALY calculation is expected disutility.

  BURDEN COMPARISON:
    Global DALYs (2019): ~2.5 billion
    Top causes:
    1. Neonatal disorders:        195M DALYs
    2. Ischemic heart disease:    182M
    3. Stroke:                     143M
    4. Lower respiratory infections: 137M
    5. Diabetes:                   110M
    6. COPD:                       104M
    7. Depression (unipolar):      103M
    8. Lower back pain:            83M

  Note: Depression and back pain are huge burden despite low mortality.
  DALY captures morbidity that mortality-based measures miss entirely.
```

## GBD — Global Burden of Disease Study

```
GBD METHODOLOGY:
  Led by IHME (Institute for Health Metrics and Evaluation, Univ. of Washington)
  Annual updates since GBD 1990.
  ~9,000 disease/injury/risk factor combinations.
  369 diseases, 87 risk factors, 204 countries/territories.

DATA SOURCES:
  Mortality: vital registration, censuses, surveys, verbal autopsies
  Morbidity: surveys, health records, registries, literature
  Risk factors: exposure surveys, systematic reviews

KEY METHODOLOGICAL FEATURES:
  Cause of death redistribution: "garbage codes" (ill-defined causes)
    redistributed to underlying causes using regression models
  Spatiotemporal Gaussian process regression (ST-GPR): fills data gaps
    across geography and time; Bayesian smoothing
  DisMod-MR: Bayesian meta-regression tool for disease modeling
    Simultaneously models incidence, prevalence, remission, case-fatality
    Ensures internal consistency of these related measures

  Comparative Risk Assessment (CRA):
    Estimates attributable burden if risk exposure were at theoretical minimum
    Population Attributable Fraction (PAF) × total burden = attributable DALYs
    Key finding: tobacco, high blood pressure, high fasting glucose, high BMI,
    ambient PM2.5 are top attributable risk factors globally

LIMITATIONS:
  Data quality varies enormously (vital registration <60% complete in SSA)
  Model uncertainty propagates and can be large
  DW determination requires cross-cultural validity assumptions
  Results sensitive to model specifications
```

## Key Global Health Initiatives

### PEPFAR

```
PEPFAR (President's Emergency Plan for AIDS Relief):
  Launched: 2003 by President George W. Bush
  Budget: >$100B total through 2023
  Scale: 20.5M people on antiretroviral therapy (ART) through PEPFAR-funded programs
  Impact: estimated 25M+ lives saved

  Structure: US government bilateral aid; operates through USAID, CDC, DoD, State Dept
  Focus: 50 countries primarily in sub-Saharan Africa
  Key programs: ART treatment, prevention (PMTCT, HTC, PrEP), care, health systems

  CONTROVERSIES:
  - PEPFAR's ABC approach ("Abstinence, Be faithful, use Condoms") —
    A and B mandated to receive portion of prevention funding → diversion from
    proven condom promotion; lifted under Obama, reinstated under Bush/Trump
  - Generic vs. branded ARVs: Bush initially restricted to brand-name drugs;
    generic ARV use eventually approved dramatically reducing per-patient cost
  - Prostitution pledge: recipients could not support legalization of sex work
    → impeded reaching sex workers most at risk; Supreme Court blocked enforcement

  LESSON: Technical success (scale, coverage) coexists with political
  compromises that limit effectiveness. Evaluate programs on population
  health metrics, not only coverage metrics.
```

### Gavi and CEPI

```
GAVI (THE VACCINE ALLIANCE):
  Est. 2000. Public-private partnership.
  Partners: WHO, UNICEF, World Bank, Gates Foundation, vaccine manufacturers.
  Mechanism: pooled procurement, co-financing, advance market commitments
  Scale: >1B children immunized, ~17M deaths prevented
  COVAX: COVID-19 pooling — received 1B doses commitment but
         dose nationalism + manufacturing bottlenecks → missed coverage targets

CEPI (COALITION FOR EPIDEMIC PREPAREDNESS INNOVATIONS):
  Est. 2017 (Oslo). Response to Ebola failures.
  Mission: accelerate vaccine development for epidemic threats
  Focus: MERS, Nipah, Lassa, Rift Valley fever, SARS (then SARS-CoV-2!)
  COVID: co-led COVAX vaccine pillar with Gavi
  Speed achievement: CureVac, Moderna, Oxford vaccines were all CEPI-funded
    Oxford/AstraZeneca candidate from near-zero to phase 3 in ~9 months
```

## Global Health Equity

```
INCOME AND HEALTH GRADIENT:

  Under-5 mortality (deaths per 1000 live births, 2021):
  Low-income countries:          56
  Lower-middle-income:           34
  Upper-middle-income:           14
  High-income:                    5
  (World average:                37)

  Life expectancy range: ~53 years (Chad) to ~85+ years (Japan, Switzerland)
  IHD mortality 10-30× higher in low-income vs. high-income countries

PROXIMATE CAUSES OF HEALTH INEQUITY:
  Access: physical, financial, informational barriers to care
  Quality: health worker density, equipment, supply chain
  Risk factors: tobacco marketing in LMICs, polluting industry relocation
  Social determinants: poverty, education, sanitation, nutrition

STRUCTURAL CAUSES (CSDH framework):
  Historical: colonialism's lasting effects on health systems
  Economic: debt, trade regimes that impede health investment
  Political: power asymmetries in global health governance (one-country-one-vote
             at WHA but donor earmarking controls resources)

COMMISSION ON SOCIAL DETERMINANTS OF HEALTH (WHO, 2008):
  Chair: Michael Marmot
  Key finding: most health inequity avoidable and caused by conditions in
    which people are born, grow, live, work, age
  "The social gradient in health": health improves with every step up
  the social ladder — not just poor vs. rich, but gradient throughout

MARMOT REVIEW (UK, 2010, 2020):
  Documented widening health inequalities in England.
  Social gradient in life expectancy: 9+ year gap between most and least deprived.
  Austerity (2010-2020): first sustained fall in life expectancy in 100+ years.
```

## Lancet Commissions

Major catalytic reports that shaped global health policy:

| Commission | Year | Key Contribution |
|---|---|---|
| Macroeconomics and Health (Sachs) | 2001 | Health investment → economic growth; estimated returns to health |
| Commission on Investing in Health | 2013 | $370B/year investment → prevent 10M deaths/year |
| Lancet Countdown on Climate | 2015+ | Annual tracking of 43 health-climate indicators |
| Commission on SNRI Drug Policy | 2016 | Harm reduction over criminalization for drug policy |
| EAT-Lancet Commission on Food | 2019 | Planetary health diet; food system → both health and environment |
| Global Burden of Obesity | 2024 | 1B people now obese globally |

## Decision Cheat Sheet

| Global health question | Key concept/resource |
|---|---|
| Compare disease burden across countries | GBD study (IHME); DALYs by cause and country |
| Measure health gain from an intervention | DALYs averted; cost per DALY averted |
| Fund vaccines for poorest countries | Gavi mechanisms; AMC model |
| Respond to novel epidemic threat | CEPI for vaccine R&D; WHO IHR/PHEIC for coordination |
| Understand HIV treatment scale-up | PEPFAR: 20M+ on ART, model of bilateral scale |
| Address health inequity root causes | CSDH framework; social determinants action |
| Evaluate global health governance | WHO structure; voluntary vs. assessed contributions |

## Common Confusion Points

**DALY and QALY are both utility-based metrics but used differently**: DALYs used for burden of disease estimation and prioritization (GBD, WHO). QALYs used for cost-effectiveness analysis in clinical and health policy decisions (NICE thresholds, US cost-effectiveness analyses). DALY = lost health (higher = worse); QALY = health gained (higher = better). They use the same underlying utility framework but in opposite directions.

**WHO authority vs. reality**: WHO can declare PHEICs, set guidelines, coordinate — but cannot compel member states to act. All real authority rests with national governments. IHR 2005 has no enforcement mechanism. COVID-19 demonstrated this clearly: WHO guidance was routinely ignored by member states.

**GBD vs. WHO official statistics**: GBD and WHO often publish different numbers for the same cause. GBD redistributes garbage codes, uses modeling to fill data gaps, and applies consistent methodology. WHO official stats often reflect reported national data with less modeling. For comparison purposes, GBD is usually preferred. For national policy, countries use their own vital registration.

**Aid effectiveness**: Scale (lives saved, vaccines delivered) ≠ sustainability. Donor-dependent programs create parallel systems, undermine national health systems, distort health worker salaries, and collapse when donor priorities shift. Long-term sustainability requires domestic resource mobilization and health system strengthening.
