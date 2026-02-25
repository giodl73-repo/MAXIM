# Pandemic Biology: Emergence and Spread

## The Big Picture

Pandemics emerge when a virus from an animal reservoir acquires the ability to
spread efficiently in a naive human population. The mathematical epidemiology
framework — built on the basic reproduction number R₀ — predicts transmission
dynamics, herd immunity thresholds, and intervention effects.

```
┌──────────────────────────────────────────────────────────────────┐
│                   PANDEMIC BIOLOGY LANDSCAPE                      │
│                                                                    │
│  EMERGENCE                SPREAD                  CONTROL        │
│  ────────                 ─────────               ───────        │
│  Spillover from animals   R₀ determines           Herd immunity  │
│  Host range expansion     exponential growth      Vaccination    │
│  Reassortment             Serial interval         NPIs           │
│  Genetic adaptation       Generation time         Antivirals     │
│  Zoonosis                 Superspreading          Quarantine      │
│                                                                    │
│  KEY EQUATION:                                                   │
│  R_eff = R₀ × (1 - p_immune) × (1 - p_NPI)                     │
│                                                                    │
│  R_eff < 1:  epidemic declines                                   │
│  R_eff = 1:  endemic equilibrium                                 │
│  R_eff > 1:  epidemic grows                                      │
└──────────────────────────────────────────────────────────────────┘
```

---

## Basic Reproduction Number R₀

R₀ (R-naught) = the average number of secondary infections produced by one
infectious individual in a completely susceptible population.

```
  FORMAL DEFINITION:
  ───────────────────
  R₀ = β × D

  β = transmission rate (probability of transmission per contact × contact rate)
  D = duration of infectious period

  Alternatively:
  R₀ = β × D × c

  β = probability of transmission given a contact
  D = duration of infectious period
  c = contact rate

  GENERATION TIME vs. SERIAL INTERVAL:
  ──────────────────────────────────────
  Generation time (Tg): time from infection of index case to infection of
                        secondary case (cannot be directly observed)
  Serial interval (SI): time between symptom onset in index case and
                        symptom onset in secondary case (observable)
  SI ≈ Tg when incubation periods are similar
  SI can be negative (pre-symptomatic transmission possible when incubation
  period is longer than generation time)

  R₀ and initial exponential growth rate r:
  ────────────────────────────────────────────
  If generation time Tg is fixed:  R₀ ≈ e^(r × Tg)
  If generation time varies:       R₀ = (1 + r × Tg)^n
                                   (depends on distribution model)

  This allows estimating R₀ from initial epidemic doubling time alone.
```

---

## R₀ Values of Known Pathogens

```
  PATHOGEN              R₀ RANGE      NOTABLE FEATURES
  ─────────────         ────────      ─────────────────
  Measles               12-18         Highest known; airborne; >95% vaccination
                                      needed for herd immunity
  Mumps                 4-7
  Smallpox              3-7           Eradicated; one of highest R₀ among controlled diseases
  Polio                 4-6           Near eradication with OPV/IPV
  SARS-CoV-2 (original) 2.5-3.5
  SARS-CoV-2 (Delta)    5-8
  SARS-CoV-2 (Omicron)  9-15          Very high; lower severity per infection
  Influenza H1N1 2009   1.2-1.4       Relatively low; seasonal flu ~1.1-1.4
  SARS-CoV-1 2003       2-5
  Ebola (West Africa)   1.5-2.5       Low R₀ but high CFR
  HIV                   2-5           Long infectious period; sexual transmission
  Rabies                <1            (in humans; zoonotic only; no h-h transmission)
  Norovirus             14-21         Cruise ships; very low infectious dose

  R₀ > 1 required for epidemic; R₀ < 1 means infection dies out
  Natural variation: R₀ is not fixed — it varies by setting, density, behavior
```

---

## Herd Immunity Threshold

The fraction of the population that must be immune to prevent epidemic growth:

```
  DERIVATION:
  ──────────
  Effective reproduction number: R_eff = R₀ × S  (S = fraction susceptible)
  Epidemic stops when R_eff ≤ 1:
  R₀ × S ≤ 1
  S ≤ 1/R₀
  Fraction immune needed: 1 - S ≥ 1 - 1/R₀

  HERD IMMUNITY THRESHOLD (HIT):
  ───────────────────────────────
  HIT = 1 - 1/R₀

  R₀ = 2:    HIT = 0.50 (50% immune)
  R₀ = 3:    HIT = 0.67 (67%)
  R₀ = 5:    HIT = 0.80 (80%)
  R₀ = 10:   HIT = 0.90 (90%)
  R₀ = 15:   HIT = 0.93 (93%)  ← measles
  R₀ = 18:   HIT = 0.94 (94%)

  Implications for vaccine coverage targets:
  ─────────────────────────────────────────
  Measles: >95% vaccination coverage required
  Polio: >80-85% required for elimination
  COVID-19 (original): ~65-70% (but variants changed this)
  COVID-19 (Omicron): ~90-93% (near-impossible by vaccination alone)
```

---

## The SIR Model — Mathematical Foundation

```
  COMPARTMENTS:
  ─────────────
  S = susceptible fraction of population
  I = infectious fraction
  R = removed (recovered + immune, or deceased)

  DIFFERENTIAL EQUATIONS:
  ─────────────────────────
  dS/dt = -β·S·I
  dI/dt = β·S·I - γ·I
  dR/dt = γ·I

  β = transmission rate; γ = recovery rate; D = 1/γ = infectious duration
  R₀ = β/γ

  EPIDEMIC CURVE:
  ────────────────
  Peak when dI/dt = 0 → S = γ/β = 1/R₀
  → Epidemic peaks when susceptible fraction drops to 1/R₀
  After peak: I declines exponentially

  FINAL EPIDEMIC SIZE:
  ─────────────────────
  Final fraction infected Z satisfies: Z + e^(-R₀·Z) = 1
  For R₀ = 2: Z ≈ 80% of population infected
  For R₀ = 3: Z ≈ 94%
  (Even with herd immunity at 50% and 67%, epidemic overshoots past HIT
   before declining → "overshoot")

  EXTENSIONS:
  ───────────
  SEIR: add Exposed (E) compartment (latent period)
  SIRD: add Disease (D = dead) compartment separate from R
  Age-structured: different β and γ for age groups
  Network models: heterogeneous contact patterns, superspreaders
```

---

## Viral Emergence — Zoonosis to Pandemic

Most pandemic-causing viruses originate in animals (zoonosis). The path from animal
reservoir to pandemic involves several steps:

```
  SPILLOVER EVENT CHAIN:
  ──────────────────────
  1. RESERVOIR HOST: virus circulates asymptomatically
     (bats: coronaviruses, Ebola, Nipah, Hendra, rabies
      birds: influenza
      rodents: hantaviruses, Lassa
      primates: HIV, Ebola, HTLV)

  2. AMPLIFYING HOST (optional): intermediate host amplifies virus
     (camels: MERS-CoV
      pigs: 2009 H1N1 origin
      palm civets: SARS-CoV-1
      pangolins or other: possibly SARS-CoV-2?)

  3. SPILLOVER: virus infects a human (dead-end or limited transmission)
     Requirements: receptor compatibility; restricted innate immune block

  4. ADAPTATION: virus acquires mutations enabling human-to-human transmission
     Key changes needed:
     - Receptor binding to human receptor (not just animal)
     - Upper respiratory tropism (for respiratory spread)
     - Stability in respiratory droplets/aerosols
     - Evasion of human innate immune restriction factors

  5. SUSTAINED HUMAN-TO-HUMAN TRANSMISSION:
     R₀ > 1 in humans; geographic spread

  6. PANDEMIC: global spread in immunologically naive population

  SARS-CoV-2 EMERGENCE:
  ──────────────────────
  December 2019: cluster of pneumonia in Wuhan, China
  January 2020: novel betacoronavirus identified; genome sequenced
  March 2020: WHO declares pandemic
  Closest bat coronavirus: RaTG13 (96.2% genomic similarity to SARS-CoV-2)
  But: SARS-CoV-2 has unique furin cleavage site (PRRAR) absent in close relatives
  Receptor-binding domain: well-adapted to human ACE2 without obvious intermediate
  Exact emergence route: debated; lab origin hypothesis not conclusively excluded
```

---

## Influenza Pandemics — Historical Pattern

```
  YEAR    SUBTYPE   ORIGIN              CFR        DEATHS ESTIMATE
  ────    ───────   ──────              ─────      ─────────────────
  1918    H1N1      Unknown (bird?)     2-3%       ~50-100 million
          "Spanish flu"
  1957    H2N2      Reassortant (China) ~0.1%      1-4 million
  1968    H3N2      Reassortant (HK)   ~0.1%      1-4 million
  1977    H1N1      Lab accident?       Low        Mild (H1N1 circulated 1918-1957)
  2009    H1N1      Swine reassortant   ~0.01-0.02% 150,000-500,000
  (H5N1   H5N1      Avian              ~60%       <1,000 (no human-human spread)
  ongoing)

  1918 WHY SO SEVERE?
  ────────────────────
  1. Second wave (fall 1918): particularly virulent variant
  2. Cytokine storm: high pathogenicity in young adults (1918 unusual: W-shaped
     mortality curve — high in young adults, not just elderly + infants)
  3. Secondary bacterial pneumonia (no antibiotics in 1918)
  4. No prior immunity in population
  5. PB1-F2: particularly proapoptotic in 1918 strain

  2009 H1N1 WHY MILD?
  ────────────────────
  1. Low R₀ initially (~1.4)
  2. Elderly had some cross-reactive immunity from 1918-related strains
  3. Not particularly virulent per infection
  4. Rapid vaccine development (early immunization of key groups)
```

---

## Non-Pharmaceutical Interventions (NPIs)

Before vaccines or drugs, NPIs modify β (transmission rate):

```
  NPI                     MECHANISM               R₀ REDUCTION ESTIMATE
  ────                    ─────────               ─────────────────────
  Mask (medical)          Block droplet           20-40%
  Mask (N95)              Filter aerosol + droplet 50-70%
  Social distancing       Reduce contacts         40-70%
  School closure          Reduce contact rate     10-30%
  Lockdown (stay home)    Reduce contacts broadly 50-80%
  Hand hygiene            Block contact route     10-20%
  Testing + isolation     Remove infectious cases 20-50%
  Contact tracing         Remove exposed cases    10-30%
  Border restrictions     Delay importation       Delay, not prevent

  KEY INSIGHT: NPIs reduce R_eff multiplicatively
  R_eff = R₀ × (1 - p₁) × (1 - p₂) × ...
  Multiple partial NPIs can bring R_eff below 1 even when none alone would
```

---

## Vaccine-Mediated Herd Immunity — Calculation

```
  For a vaccine with efficacy VE (fraction of vaccinations that prevent infection):
  ─────────────────────────────────────────────────────────────────────────────────
  R_eff = R₀ × (1 - p × VE)

  Where p = fraction vaccinated, VE = vaccine efficacy against infection

  To achieve herd immunity:
  R₀ × (1 - p × VE) < 1
  p > (1 - 1/R₀) / VE = HIT / VE

  Example: measles
  R₀ = 15; HIT = 93%; measles vaccine VE = 97%
  p > 0.93 / 0.97 = 0.96 → need >96% coverage

  COVID-19 (Omicron):
  R₀ ≈ 12; HIT ≈ 92%; Omicron-specific vaccine VE against infection ~40%
  p > 0.92 / 0.40 = 2.3  → impossible (>100% required!)
  → Vaccination alone cannot achieve herd immunity against Omicron
  → Strategy shifts to: reduce severe disease, not prevent transmission
```

---

## Pandemic Preparedness Framework

```
  DETECTION:
  ──────────
  Genomic surveillance: sequence representative samples continuously
  Sewage surveillance: wastewater SARS-CoV-2 (detects 3-7 days before clinical cases)
  Sentinel networks: primary care surveillance, hospital admissions
  Animal-human interface: monitor farm workers, wildlife interfaces

  RESPONSE SPEED:
  ───────────────
  mRNA vaccine platform: critical advance
  SARS-CoV-2: sequence available Jan 10 2020
             mRNA vaccine in clinical trial: March 16 2020 (66 days!)
             EUA granted: December 11 2020 (just under 11 months)
  Historical comparison: influenza vaccine requires ~6 months per strain update
  mRNA platform allows <100 day response target (CEPI 100 Days Mission)

  COUNTERMEASURES:
  ─────────────────
  Broad-spectrum antivirals: remdesivir, molnupiravir (target conserved viral enzymes)
  Prototype pathogen approach: develop vaccines for prototypical viruses in each
    family; accelerate for closest relative in next outbreak
  Stockpiling: antivirals, PPE, ventilators, vaccines
  International cooperation: WHO PHEIC declaration, COVAX
```

---

## Decision Cheat Sheet

| Parameter | Formula | Implication |
|-----------|---------|-------------|
| R₀ | β × D | >1 = epidemic grows |
| Herd immunity threshold | 1 - 1/R₀ | Minimum immune fraction to stop spread |
| Vaccination coverage needed | HIT / VE | Increases if vaccine imperfect |
| R_eff with vaccination | R₀ × (1 - p·VE) | <1 = epidemic controlled |
| Doubling time | ln(2)/(r) | r from initial growth curve |
| Final epidemic size | Z: Z + e^(-R₀Z) = 1 | Fraction eventually infected |

---

## Common Confusion Points

**R₀ is not a biological constant.** It depends on contact patterns, population
density, behavior, and environment. The same influenza strain has R₀ ≈ 1.3 in a
rural community and R₀ ≈ 3 in a crowded city during winter.

**Herd immunity threshold is a tipping point, not a binary switch.** As vaccination
coverage increases, R_eff decreases continuously. At the HIT, R_eff = 1 exactly —
the epidemic is barely self-sustaining. Even below the HIT, vaccination reduces the
final epidemic size substantially.

**Infection fatality rate (IFR) and case fatality rate (CFR) are different.**
CFR = deaths / confirmed cases (depends heavily on testing). IFR = deaths / total
infections (requires seroprevalence surveys). IFR is more meaningful epidemiologically
but harder to measure. COVID-19 original strain IFR ≈ 0.5-1%; CFR appeared much higher
early because only severe cases were tested.

**Pre-symptomatic transmission complicates traditional outbreak control.**
Classical outbreak control (isolate symptomatic cases) works well when infectious
period begins after or with symptoms. When substantial transmission occurs before
symptoms (SARS-CoV-2: ~40-60% of transmission is pre-symptomatic), isolation of
symptomatic cases alone is insufficient → need test-and-trace + broader NPIs.

**Antigenic original sin (imprinting) affects pandemic response.** Immune responses
to a new flu strain are shaped by the first flu strain encountered in childhood
(original antigenic sin / immune imprinting). This affected 2009 H1N1 response:
elderly had cross-reactive H1 immunity; young adults lacked it → unusual age distribution
of severe disease. COVID-19 Omicron: extensive imprinting on Wuhan-strain spike
from vaccination + early infection shapes responses to new variants.
