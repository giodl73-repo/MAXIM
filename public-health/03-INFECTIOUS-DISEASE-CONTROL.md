# Infectious Disease Control

## Transmission Dynamics — The Big Picture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   INFECTIOUS DISEASE TRANSMISSION FRAMEWORK                 │
│                                                                               │
│  PATHOGEN         HOST            ENVIRONMENT       TRANSMISSION            │
│  ─────────────    ─────────────   ─────────────     ─────────────────────   │
│  Infectivity      Susceptibility  Temperature       Direct contact          │
│  Virulence        Immunity        Humidity          Airborne droplets       │
│  Incubation pd    Age/genetics    Crowding          Fomites                 │
│  Shedding rate    Comorbidities   Sanitation        Vector (mosquito etc)   │
│  Mutation rate    Behavior        Healthcare access  Sexual / bloodborne    │
│                                                                               │
│  INFECTION CHAIN:                                                             │
│  Reservoir → Portal of exit → Mode of transmission → Portal of entry        │
│  → Susceptible host → Infection → (back to reservoir or dead end)           │
│                                                                               │
│  BREAK ANY LINK → INTERRUPT TRANSMISSION                                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

## R₀ and Rt — The Fundamental Numbers

```
BASIC REPRODUCTION NUMBER R₀:
  Average number of secondary cases one infected person generates
  in a fully susceptible population.

  R₀ = β × c × D
  where:
    β = probability of transmission per contact
    c = contact rate (contacts/day)
    D = infectious duration (days)

  R₀ < 1: pathogen goes extinct (each case causes <1 new case)
  R₀ = 1: endemic equilibrium
  R₀ > 1: epidemic growth (cases grow exponentially initially)

REPRESENTATIVE R₀ VALUES:
  Measles:      12-18    (most transmissible common pathogen)
  Pertussis:    12-17
  Smallpox:     5-7
  COVID-19 WT:  2.5-3.5  (Alpha/Delta 5-6, Omicron 8-15)
  HIV:          2-5
  SARS:         2-4
  Seasonal flu: 1.2-1.4
  Ebola:        1.5-2.5

EFFECTIVE REPRODUCTION NUMBER Rt:
  The actual average secondary cases at time t, accounting for:
  - Fraction of population already immune (S/N)
  - Any control measures in effect
  - Behavioral changes

  Rt = R₀ × (S/N) × (effect of interventions)

  When Rt < 1: outbreak is shrinking
  When Rt > 1: outbreak is growing
  Rt is estimated in real-time from reported cases + serial interval
```

## Herd Immunity Threshold — The Fixed-Point Argument

```
HERD IMMUNITY THRESHOLD (HIT):
  The fraction of population that must be immune to drive Rt < 1.

  At endemic equilibrium with fraction p immune:
    Rt = R₀ × (1 - p)

  Set Rt = 1, solve for p:
    1 = R₀ × (1 - p*)
    p* = 1 - 1/R₀
    p* = (R₀ - 1)/R₀

  THIS IS A FIXED-POINT THEOREM ON THE COMPARTMENTAL MODEL.
  The immune fraction p* is the value that makes the system's
  feedback loop neutral (gain = 1).

EXAMPLES:
  Measles (R₀=15):   p* = 14/15 = 93%
  COVID-19 WT (R₀=3): p* = 2/3 = 67%
  COVID-19 Omicron (R₀=12): p* = 11/12 = 92%
  Seasonal flu (R₀=1.3): p* = 0.3/1.3 = 23%

CAVEATS:
  1. Assumes homogeneous mixing (everyone contacts everyone equally)
  2. In heterogeneous networks, herd immunity is achieved at LOWER
     coverage if high-degree nodes (superspreaders) are preferentially
     immunized — targeting reduces effective R₀ more than random vaccination
  3. Immunity wanes → herd immunity threshold must be maintained
  4. Spatial clustering of unvaccinated creates local vulnerabilities
     even when global coverage exceeds HIT
```

## SIR Model — Formal Framework

```
COMPARTMENTAL SIR MODEL:
  S(t) = Susceptible, I(t) = Infectious, R(t) = Recovered/immune
  N = S + I + R (constant population)

  dS/dt = -β × S × I / N
  dI/dt =  β × S × I / N − γ × I
  dR/dt =  γ × I

  R₀ = β/γ (transmission rate / recovery rate)

  EPIDEMIC THRESHOLD:
    Epidemic occurs only if dI/dt > 0 at t=0:
    β × S/N − γ > 0
    S/N > γ/β = 1/R₀
    → epidemic grows if susceptible fraction > 1/R₀

  FINAL SIZE EQUATION (total fraction infected, R_∞):
    1 − R_∞ = exp(−R₀ × R_∞)    (transcendental equation, solved numerically)

EXTENSIONS:
  SEIR: adds E (exposed/latent) compartment
  SEIRS: immunity wanes, susceptibles return
  Age-structured: age-specific contact matrices
  Network models: contact network topology matters for heterogeneous mixing
```

## Quarantine, Isolation, and Contact Tracing

```
TERMINOLOGY (often confused):

  ISOLATION:   Separate INFECTED individuals from those not infected
               Duration: until no longer infectious
               Applied to: confirmed cases, probable cases

  QUARANTINE:  Separate EXPOSED individuals who may become infectious
               Duration: one incubation period maximum
               Applied to: close contacts of cases

  INCUBATION PERIOD determines quarantine duration:
    COVID-19:  5-day median, 14-day maximum → 14-day quarantine
    Ebola:     2-21 days → 21-day quarantine
    Measles:   7-18 days → 21-day quarantine
    Flu:       1-4 days → 5-7 day quarantine

CONTACT TRACING PROCESS:
  1. Case identified → interview for contacts
  2. Contacts enumerated (backward: who infected case? forward: who did case infect?)
  3. Contacts notified (index notification vs. partner notification)
  4. Contacts monitored or quarantined per protocol
  5. Contacts who develop symptoms → test/isolate → new cases → repeat

  EFFECTIVENESS depends on:
  - Fraction of transmission that occurs before symptoms (presymptomatic)
  - Speed of tracing relative to serial interval
  - Contact density (more contacts per case → more labor per case)

  DIGITAL CONTACT TRACING (COVID-19):
    Bluetooth proximity → exposure notification apps (Apple-Google API)
    Advantage: speed, passive exposure detection
    Limitation: smartphone penetration, false proximity (walls), uptake
    Evidence: limited demonstrated impact due to low adoption
```

## Non-Pharmaceutical Interventions (NPIs)

```
NPI CATEGORIES:
  Individual:        Masks, hand hygiene, symptom monitoring
  Environmental:     Ventilation, HEPA filtration, UV-C, surface disinfection
  Physical distancing: Maintain distance, reduce contact rate
  Social distancing:   School closure, workplace closure, gathering limits
  Travel measures:     Travel restrictions, border screening, quarantine on entry
  Community:           Stay-home orders, lockdowns

MECHANISM:
  All NPIs reduce c (contact rate) in R₀ = β × c × D
  Some reduce β (masks reduce transmission probability per contact)

NPI EFFECTIVENESS ESTIMATES (from COVID-19 evidence):
  Mask wearing (N95/FFP2): 70-85% reduction in infection risk (well-fitted)
  Surgical mask:           ~50-60% reduction
  School closures:         Rt reduction 15-25% (varies by age mixing)
  Non-essential business closures: Rt reduction 20-40%
  Stay-home orders:        Rt reduction 15-30% (effect over and above other measures)
  Combination of measures: Near-complete suppression possible (New Zealand 2020)

EVIDENCE QUALITY: Mostly observational (RCTs not feasible for lockdowns).
  Causal identification challenges: concurrent measures, behavioral response,
  simultaneity of policy changes across jurisdictions.
  Bangladesh RCT on masks: gold standard for mask effectiveness.
```

## Outbreak Investigation Case: Cholera

```
Cholera outbreak investigation (archetype for point-source outbreaks):

  John Snow's 1854 Broad Street pump investigation — founding act of
  field epidemiology.

  Method:
  1. Spot map of cases → clustering around Broad Street pump
  2. Attack rate analysis: households using pump vs. others
  3. Natural experiment: brewery workers (drank beer, not water) → no cases
  4. Intervention: removed pump handle
  5. Causal inference without microscopy or germ theory

  This is still the template 170 years later:
  Descriptive epi (who/where/when) → hypothesis generation →
  analytical study (cohort/case-control) → intervention

  Modern parallel: cloud reliability postmortem.
  Same structure: detect anomaly → spot map (trace IDs affected) →
  timeline → hypothesis → confirm → remediate → write up.
```

## Vector-Borne Disease Control

```
VECTOR-BORNE PATHOGENS:
  Mosquito: Malaria, Dengue, Zika, Chikungunya, Yellow fever, WNV
  Tick:     Lyme, RMSF, Anaplasmosis, Babesiosis, TBE
  Sand fly: Leishmaniasis
  Tsetse fly: African sleeping sickness
  Flea:     Plague, murine typhus

CONTROL STRATEGIES:
  Vector reduction: insecticides (IRS, LLINs), larviciding, source reduction
  Host protection: repellents (DEET, picaridin), protective clothing
  Biological control: Wolbachia-infected Aedes (dengue suppression)
  Sterile insect technique: release sterile males → population collapse

  Bednet impact (malaria):
  Long-lasting insecticidal nets (LLINs): most cost-effective malaria intervention
  ~40% reduction in child mortality in high-transmission settings
  Provided free → coverage scales → herd protection effects observed
```

## Antimicrobial Resistance (AMR)

```
AMR THREAT LANDSCAPE:
  WHO priority pathogens (critical):
  - Carbapenem-resistant Enterobacteriaceae (CRE)
  - Carbapenem-resistant Acinetobacter baumannii
  - Carbapenem-resistant Pseudomonas aeruginosa

  WHO priority pathogens (high):
  - MRSA, VRE, fluoroquinolone-resistant Salmonella/Neisseria
  - Extended-spectrum beta-lactamase (ESBL) E. coli/Klebsiella

  AMR MECHANISM:
  Antibiotic selection pressure → resistant variants survive →
  proliferate → spread via horizontal gene transfer (plasmids)
  → resistance genes transfer between species

  CONTROL APPROACHES:
  - Antibiotic stewardship programs: prescribe narrow spectrum, shorter courses
  - Surveillance: mandatory AMR reporting, genomic tracking
  - Infection prevention: reduce need for antibiotics
  - Pipeline: new antibiotic development (market failure → public subsidy needed)
  - Agricultural: reduce non-therapeutic agricultural antibiotic use
```

## Decision Cheat Sheet

| Control question | Tool/concept |
|---|---|
| Will this outbreak grow? | Estimate Rt — if <1, declining |
| What vaccination coverage is needed? | p* = 1 − 1/R₀ |
| How long to quarantine contacts? | Maximum incubation period |
| Is this point source or propagated? | Epidemic curve shape |
| Which contacts to prioritize for tracing? | Highest-risk exposures, presymptomatic window |
| How much do school closures help? | 15-25% Rt reduction, evidence variable |
| Control a vector-borne disease | LLIN/IRS for malaria; source reduction for dengue |
| Reduce hospital AMR | Antibiotic stewardship + contact precautions |

## Common Confusion Points

**R₀ is not a biological constant**: R₀ depends on population density, contact patterns, social behavior, and environmental factors. Measles R₀ is 15 in dense urban populations but much lower in dispersed rural settings. The same pathogen has different R₀ in different contexts.

**Herd immunity ≠ herd immunity threshold met**: Reaching the threshold doesn't mean immediate cessation. Ongoing transmission occurs until susceptible depletion works through the network. In spatially clustered populations with unvaccinated pockets, local outbreaks continue even after global HIT is exceeded.

**Serial interval vs. incubation period**: Incubation period = time from infection to symptoms (host biology). Serial interval = time from one case's symptom onset to the next case's symptom onset (transmission chain). When serial interval < incubation period, presymptomatic transmission occurs — contact tracing must happen during incubation, not after symptom onset. COVID-19 serial interval (~5 days) < incubation period (5 days) → substantial presymptomatic transmission.

**Quarantine duration debates**: "Optimal" quarantine length involves tradeoff between false-negative rate (ending quarantine before exposure manifests) and cost (compliance, economic disruption). Shortening COVID-19 quarantine from 14 days to 7 days with testing missed ~1% of cases — acceptable tradeoff given compliance collapse at 14 days.

**Case fatality rate vs. infection fatality rate**: CFR = deaths / confirmed cases (inflated by undercounting). IFR = deaths / true infections (requires seroprevalence or model). COVID-19: CFR ≈ 2-3%, IFR ≈ 0.3-1% depending on age structure and healthcare capacity.
