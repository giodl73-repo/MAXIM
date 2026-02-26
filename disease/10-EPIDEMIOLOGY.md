# 10 — Epidemiology & Public Health

## Study Design, Transmission, R₀, Outbreak Investigation, Screening, Global Burden

---

## Big Picture: Epidemiological Thinking

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   EPIDEMIOLOGY — CORE FRAMEWORK                         │
├───────────────────┬─────────────────────────────────────────────────────┤
│  DESCRIPTIVE      │  Who (person), where (place), when (time)           │
│  EPIDEMIOLOGY     │  Disease surveillance, case reports, outbreak desc. │
├───────────────────┼─────────────────────────────────────────────────────┤
│  ANALYTIC         │  Study design: RCT > cohort > case-control >        │
│  EPIDEMIOLOGY     │    cross-sectional > ecological                     │
│                   │  Measures: RR, OR, NNT, attributable risk            │
├───────────────────┼─────────────────────────────────────────────────────┤
│  INFECTIOUS DX    │  R₀, herd immunity, transmission dynamics,          │
│  EPIDEMIOLOGY     │  epidemic curves, outbreak investigation             │
├───────────────────┼─────────────────────────────────────────────────────┤
│  PUBLIC HEALTH    │  Screening (Wilson-Jungner), prevention levels,      │
│                   │  vaccines, surveillance systems, IHR                │
├───────────────────┼─────────────────────────────────────────────────────┤
│  GLOBAL BURDEN    │  GBD, DALY, NCD transition, demographic transition  │
└───────────────────┴─────────────────────────────────────────────────────┘

Core question types:
  Incidence/prevalence → descriptive
  Cause/association → analytic (cohort, case-control, RCT)
  Transmission dynamics → infectious epi
  Policy decisions → cost-effectiveness, screening
```

---

**Systems Bridge:** The epidemiological study design hierarchy is the same evidence quality hierarchy used in any empirical discipline — it is not biology-specific, it is epistemology. The principle: the closer the study design comes to a controlled experiment, the fewer confounds are unaccounted for, and the stronger the causal claim.

```
Design              Causal claim strength    Analogy
──────────────────────────────────────────────────────────────────────
RCT (randomized     Strong — randomization   A/B test: random assignment
controlled trial)   controls confounders     eliminates selection bias
                    by design

Cohort (prospective) Moderate — exposure     Observational logging: track
                    measured before outcome; a defined cohort forward in time;
                    confounders measured,    can measure incidence and
                    statistically adjusted   compute relative risk (RR)

Case-control        Weaker — retrospective   Post-hoc log analysis: start
(retrospective)     selection; recall bias;  from known outcomes, look back
                    can only compute OR,     at what differed; selection
                    not RR                   bias and recall bias degrade
                                             causal inference

Cross-sectional     Weakest for causality    A snapshot / point-in-time
                    — exposure and outcome   metric — can't tell which
                    measured simultaneously  came first

Ecological          Confounded by            Aggregate metrics — group-level
                    aggregation fallacy      correlation ≠ individual-level
                                             correlation
```

**RR vs OR:** Relative Risk (RR) is a prospective ratio — "how much more likely is disease in exposed vs unexposed" — and is directly interpretable. Odds Ratio (OR) is what you compute when you can't measure incidence (case-control design starts from outcome, not population) — it approximates RR well when disease prevalence is low ("rare disease assumption"). When prevalence is high, OR overestimates RR. The confusion between OR and RR in the literature is a systematic bias toward inflated effect sizes in case-control studies on common diseases.

## 1. Epidemiological Measures

### Frequency Measures

```
INCIDENCE RATE (IR): New cases per person-time at risk
  IR = (new cases) / (person-time at risk)
  Units: cases per 1,000 person-years
  Use: how fast does disease occur?

CUMULATIVE INCIDENCE (CI) = Attack Rate:
  CI = (new cases during period) / (population at risk at start)
  Units: proportion (0–1) or percent
  Use: risk over defined period; outbreak attack rates

PREVALENCE (P): Existing cases in population at a point (or period) in time
  Point prevalence = (cases at moment) / (total population)
  Period prevalence = (cases during period) / (total population)
  Relationship: P ≈ IR × Duration (when P low and disease chronic)

SECONDARY ATTACK RATE (SAR):
  (new cases in exposed household) / (susceptible household contacts)
  Measures household transmission efficiency
```

### Mortality Measures

```
CASE FATALITY RATE (CFR):
  Deaths / confirmed cases — biased by testing; measures disease severity

INFECTION FATALITY RATE (IFR):
  Deaths / all infections (including asymptomatic)
  IFR < CFR always; requires seroprevalence data to estimate denominator

CAUSE-SPECIFIC MORTALITY RATE:
  Deaths from cause X per 100,000 population per year

YEARS OF POTENTIAL LIFE LOST (YPLL):
  Sum (reference age − age at death) for each premature death
  Weights deaths of young people more heavily
```

---

## 2. Study Designs

### Evidence Hierarchy

```
                         ┌──────────────────────────┐
                         │   SYSTEMATIC REVIEW /    │  Highest
                         │     META-ANALYSIS        │  evidence
                         └───────────┬──────────────┘
                                     │
                         ┌───────────┴──────────────┐
                         │   RANDOMIZED CONTROLLED  │
                         │       TRIAL (RCT)        │
                         └───────────┬──────────────┘
                                     │
              ┌──────────────────────┼─────────────────────┐
              │                      │                      │
   ┌──────────┴───────┐   ┌──────────┴───────┐   ┌─────────┴────────┐
   │   COHORT study   │   │  CASE-CONTROL    │   │  CROSS-SECTIONAL │
   │(prospective/retro│   │    study         │   │     study        │
   └──────────────────┘   └──────────────────┘   └──────────────────┘
              │
   ┌──────────┴───────┐
   │    ECOLOGICAL    │  Lowest evidence
   │      study       │  (group-level data)
   └──────────────────┘
```

### Study Design Comparison

| Design | Direction | Exposure assessment | Outcome | Best for | Measure | Limitations |
|--------|-----------|---------------------|---------|---------|---------|------------|
| RCT | Forward | Randomized at enrollment | Incidence | Efficacy of intervention | RR, NNT | Expensive, ethical limits, external validity |
| Prospective cohort | Forward | At enrollment (before outcome) | Incidence | Rare exposures, natural history | RR, RD | Expensive, long, loss to follow-up |
| Retrospective cohort | Forward (analysis) | Historical records | Incidence | Occupational exposures, existing data | RR, RD | Recall bias, incomplete records |
| Case-control | Backward | After outcome (recall) | Prevalence | Rare outcomes, multiple exposures | OR (approximates RR if rare) | Recall/selection bias, can't calculate IR |
| Cross-sectional | Snapshot | Same time as outcome | Prevalence | Prevalence estimation, screening | Prevalence ratio | Temporal ambiguity (cause ≠ effect) |
| Ecological | Group-level | Group aggregates | Group aggregates | Hypothesis generation | Correlation | Ecological fallacy (group ≠ individual) |

---

## 3. Measures of Association

### Relative Risk (RR) — from Cohort or RCT

```
          Exposed    Unexposed
Disease    a           b
No disease c           d

Incidence in exposed = a / (a+c)
Incidence in unexposed = b / (b+d)

RR = [a/(a+c)] / [b/(b+d)]
  RR = 1.0 → no association
  RR > 1.0 → positive association (risk factor)
  RR < 1.0 → negative association (protective)
  95% CI excludes 1.0 → statistically significant
```

### Odds Ratio (OR) — from Case-Control

```
OR = (a × d) / (b × c)  [cross-product ratio from 2×2 table]
  Approximates RR when disease is rare (<10%)
  Used when can't calculate true incidence (case-control)
  Always further from null (1.0) than corresponding RR
```

### Attributable Risk and NNT

```
ARD (attributable risk difference / risk difference):
  ARD = Incidence(exposed) − Incidence(unexposed)
  Absolute excess risk

PAR (population attributable risk):
  PAR = [P(exp) × (RR−1)] / [P(exp) × (RR−1) + 1]    (Levin's formula)
  Fraction of disease in total population attributable to exposure
  Relevant for public health intervention decisions

NNT (number needed to treat):
  NNT = 1 / ARD
  Number of patients to treat to prevent 1 outcome
  Context-dependent: NNT=10 for fatal disease ≠ NNT=10 for mild symptom
```

### Confounding and Bias

```
CONFOUNDING:
  Confounder: associated with exposure AND outcome; not on causal pathway
  Classic: smoking confounds coffee→heart disease association
  Control: randomization (RCT), restriction, matching, stratification,
           multivariate regression, propensity scores

SELECTION BIAS:
  Systematic difference in who enters/stays in study
  Types: healthy worker effect, Berkson's bias (hospital controls ≠ community),
         loss to follow-up, volunteer bias

INFORMATION BIAS:
  Misclassification of exposure or outcome
  Non-differential misclassification → biases toward null
  Differential (recall) bias → biases in either direction
  Observer bias → use blinding

EFFECT MODIFICATION (interaction):
  Effect of exposure differs by level of third variable
  NOT a bias — biological phenomenon; report stratum-specific effects
```

---

## 4. R₀ and Transmission Dynamics

### R₀ (Basic Reproduction Number)

```
R₀ = average number of secondary cases per infectious case
     in a FULLY SUSCEPTIBLE population

R₀ = β × c × D
  β = transmission probability per contact
  c = contact rate (contacts per unit time)
  D = infectious duration

R₀ > 1 → epidemic can grow
R₀ < 1 → epidemic dies out
R₀ = 1 → endemic equilibrium

EFFECTIVE REPRODUCTION NUMBER (Rₑ):
  Rₑ = R₀ × S/N    (S = susceptibles, N = total population)
  Rₑ = R₀ × (1 − immunization coverage)
  When Rₑ < 1 → epidemic declining
```

### Herd Immunity Threshold

```
Herd immunity threshold (HIT) = 1 − 1/R₀

Derivation:
  For epidemic to stop: Rₑ < 1
  Rₑ = R₀ × (1−p) where p = immune fraction
  R₀ × (1−p) = 1 when p = 1 − 1/R₀

Disease-specific thresholds:
  Measles:   R₀ = 12–18 → HIT = 92–94%
  Pertussis: R₀ = 12–17 → HIT = 92–94%
  Polio:     R₀ = 5–7   → HIT = 80–86%
  COVID-19 (Wuhan): R₀ = 2–3 → HIT = 50–67%
  COVID-19 (Delta): R₀ ≈ 6–7 → HIT = 83–86%
  Mumps:     R₀ = 4–7   → HIT = 75–86%
  Smallpox:  R₀ = 5–7   → HIT = 80–85%

WHY measles outbreaks occur despite ~92% coverage:
  Clustering of unvaccinated individuals → local Rₑ > 1 in pockets
  Sub-national variation more important than national average
```

### Epidemic Curve Types

```
POINT SOURCE:
  All cases exposed to source at same time (single peak)
  Incubation period distribution → sharp narrow curve
  Example: Salmonella from contaminated potato salad at single event

PROPAGATED (person-to-person):
  Multiple peaks, each separated by ~1 incubation period
  Exponential growth potential
  Example: influenza, norovirus outbreak

CONTINUOUS SOURCE:
  Prolonged plateau or gradual slope (ongoing exposure)
  Example: contaminated water supply, air/environmental contamination

MIXED:
  Point source then propagated (common in restaurant + household spread)
```

---

## 5. Outbreak Investigation — Step-by-Step

```
STEP 1: Prepare for field work
  Assemble team, safety equipment, IRB considerations, notifications

STEP 2: Establish existence of epidemic
  Compare observed cases to expected (historical baseline, endemic level)
  Control for seasonal variation

STEP 3: Verify diagnosis
  Lab confirmation of pathogen; clinical + epidemiological criteria

STEP 4: Construct a working case definition
  Confirmed / probable / suspected (based on lab / clinical / epidemiological)
  Broad (sensitive) for epidemic curve → narrow (specific) for risk factors

STEP 5: Find and count cases (line listing)
  Name, age, sex, onset date, exposure history, clinical features
  Descriptive epi: person / place / time

STEP 6: Perform descriptive epidemiology
  Attack rates by characteristic (food eaten, area visited, etc.)
  Generate epidemic curve, map cases

STEP 7: Develop hypotheses
  Based on descriptive data; biological plausibility; literature

STEP 8: Evaluate hypotheses analytically
  Cohort study (defined population): RR, AR%
  Case-control study (undefined population): OR
  Environmental/lab testing to confirm vehicle

STEP 9: Implement control measures
  Should not wait for definitive confirmation
  Source control: remove contaminated product, treat water, quarantine
  Host-directed: vaccination, prophylaxis, isolation, contact tracing

STEP 10: Communicate findings
  Report to public health authorities; peer-reviewed publication
```

---

## 6. Transmission Routes and Control Implications

```
ROUTE           MECHANISM                    CONTROL
──────────────────────────────────────────────────────────────────
Contact
  Direct        Physical contact (touch,      Hand hygiene, gloves,
                sex, bite, blood)             condoms, needles
  Indirect      Fomites (surfaces/objects)   Surface disinfection,
                                              clean technique
Droplet         >5–10 μm; travel <1–2 m;     Surgical mask, droplet
                land on mucous membranes     precautions
Airborne        <5 μm aerosols; travel >2m;  N95, negative pressure
                remain suspended             room, HVAC filtration
                (TB, measles, COVID-19)
Fecal-oral      Contaminated food/water;      Water treatment, hand
  (enteric)     index: outbreak in children   hygiene, food safety
Vectorborne     Insect vector required        Vector control (bednets/
                (malaria/dengue/Lyme/WNV)    insecticides), repellent
Vertical        Mother → child (in utero,     Antiretroviral PrEP,
                perinatal, breastfeeding)     C-section (HSV/HIV),
                                              avoid breastfeeding (HIV)
Zoonotic        Animal reservoir → human      Surveillance, culling,
                (rabies, anthrax, plague)     vaccination of animals

CONTACT PRECAUTIONS: Direct/indirect — gown + gloves
DROPLET PRECAUTIONS: Surgical mask, private room, 1 m distance
AIRBORNE PRECAUTIONS: N95 + negative pressure room
STANDARD PRECAUTIONS: Hand hygiene + PPE for all patients
```

---

## 7. Surveillance Systems

### Passive vs Active

```
PASSIVE SURVEILLANCE:
  Healthcare providers voluntarily report to public health
  Low cost but underreporting (10–90% underreported depending on disease)
  Sentinel surveillance: subset of sites reports in detail
  Notifiable disease list (US: CDC + state health depts)

ACTIVE SURVEILLANCE:
  Public health actively seeks cases (contacts, healthcare facilities)
  More complete; resource-intensive
  Used during outbreaks, elimination campaigns

SYNDROMIC SURVEILLANCE:
  Pre-diagnostic signals (ED chief complaints, pharmacy sales, 911 calls)
  Earlier detection but less specific
  BioSense (CDC), ER chief complaint data
  Useful for novel agent or bioterrorism detection

MOLECULAR SURVEILLANCE:
  Whole-genome sequencing (WGS) of pathogens
  PulseNet (foodborne — real-time MLST/WGS clustering)
  SARS-CoV-2: GISAID, CDC variant surveillance
  Wastewater epidemiology (WBE): polio, COVID-19 — population-level early warning
```

### International Health Regulations (IHR)

```
WHO IHR (2005): legally binding framework for 196 countries
Public Health Emergency of International Concern (PHEIC):
  - Declared by WHO DG
  - Triggers coordinated international response
  - Examples: H1N1 (2009), Ebola (2014, 2019), COVID-19 (2020), Mpox (2022, 2024)

4 Core capacities required: surveillance, reporting, response, risk communication

JEE (Joint External Evaluation): IHR implementation assessment → Global Health Security Index
```

---

## 8. Screening Principles

### Wilson-Jungner Criteria (WHO, 1968)

```
1.  Disease is an important health problem
2.  Natural history well understood
3.  Recognizable latent or early symptomatic stage
4.  Treatment at early stage more effective than late
5.  Suitable test exists
6.  Test acceptable to population
7.  Adequate facilities for diagnosis and treatment
8.  Agreed policy on who to treat
9.  Economically balanced (cost of screening vs cost of untreated)
10. Continuing process (not one-time)
```

### Screening Test Statistics

```
           Disease+   Disease−
Test+         TP         FP       PPV = TP/(TP+FP)
Test−         FN         TN       NPV = TN/(TN+FN)
           Sensitivity  Specificity
           TP/(TP+FN)   TN/(TN+FP)

SENSITIVITY: probability of + test if disease present
  High sensitivity → few false negatives → good for RULING OUT (SnNout)
  Use when: miss = dangerous (HIV, cancer)

SPECIFICITY: probability of − test if disease absent
  High specificity → few false positives → good for RULING IN (SpPin)
  Use when: FP = costly/harmful (unnecessary treatment)

PREDICTIVE VALUES DEPEND ON PREVALENCE:
  PPV = (sensitivity × prevalence) / [sensitivity × prevalence + (1−specificity) × (1−prevalence)]
  Even perfect test has low PPV when disease rare

EXAMPLE: HIV test (sensitivity 99.9%, specificity 99.9%)
  In high-risk population (prevalence 1%): PPV ≈ 91% (good)
  In low-risk population (prevalence 0.01%): PPV ≈ 9% (9 FP per 1 TP)
  → Confirms: screen high-risk populations first

ROC CURVE: Sensitivity (y) vs 1−Specificity (x) across thresholds
  AUC = overall discrimination ability; AUC 0.5 = random; 1.0 = perfect
  Choice of cut-off depends on relative costs of FP vs FN
```

### Screening — Lead Time and Length Bias

```
LEAD TIME BIAS:
  Screening advances diagnosis date (early detection)
  But disease course unchanged → apparent ↑ survival even if no benefit
  Control: measure cause-specific mortality, not survival time

LENGTH BIAS (length-time bias):
  Slow-progressing (indolent) cancers exist longer in presymptomatic window
  → Disproportionately detected by screening
  Screened cancers appear to have better prognosis (they're the slow ones)
  Overdiagnosis: detection of disease that would never have caused symptoms

OVERDIAGNOSIS:
  Real problem in prostate (PSA), thyroid, breast cancer screening
  Harms: treatment side effects from treating "cancers" that were never destined to kill
  Balance against benefit of detecting aggressive cancers early
```

---

## 9. Vaccines and Population Immunity

### Vaccine Types and Mechanisms

| Type | Examples | Mechanism | Advantages | Limitations |
|------|---------|-----------|------------|-------------|
| Live-attenuated | MMR, varicella, yellow fever, OPV, BCG | Replicates in host → robust T+B memory | Long-lasting, single dose often sufficient | Reversion risk, CI in immunocompromised |
| Inactivated (whole) | IPV, flu (some), Hep A, rabies | Killed pathogen; humoral response | Stable, no reversion | Weaker response; adjuvant + boosters needed |
| Subunit/protein | Hep B (HBsAg), pertussis (acellular), HPV (VLP), meningococcal | Specific antigen; adjuvanted | Safe, precise | Less immunogenic; multiple doses |
| Toxoid | Tetanus, diphtheria | Inactivated toxin → anti-toxin antibodies | Highly effective against toxin | Only toxin protection, not infection |
| mRNA | COVID-19 (mRNA-1273, BNT162b2) | mRNA → cell produces antigen → immune response | Rapid development, no live pathogen, scalable | Cold chain requirements (original formulations) |
| Viral vector | AstraZeneca COVID-19, J&J COVID-19, Ebola | Adenovirus carries antigen gene | Potent T-cell response | Pre-existing vector immunity can reduce response |

**Cold chain:** Vaccines must be stored at 2-8°C (some at −20°C/−70°C); breaks at any point (warehouse → transport → clinic) can inactivate vaccines. Critical for developing-world programs.

**WHO EPI (Expanded Programme on Immunization):** Since 1974; core antigens (BCG, OPV/IPV, DTP, HepB, Hib, measles). Global immunization coverage ~85% (2023).

**Vaccine hesitancy:** WHO top-10 global health threat. Drivers: complacency (disease not feared), convenience (access), confidence (safety concerns). 1998 Wakefield Lancet (retracted) — MMR/autism fraud — persistent impact on measles rates.

---

## 10. Global Burden of Disease

### DALY (Disability-Adjusted Life Year)

```
DALY = YLL + YLD
  YLL (years of life lost): premature mortality
    YLL = N deaths × (L − age at death), where L = standard life expectancy
  YLD (years lived with disability):
    YLD = prevalence × disability weight (0–1 scale) × duration

Disability weight examples:
  Mild anemia: 0.005
  Moderate depression: 0.145
  Severe HIV/AIDS: 0.582
  Complete blindness: 0.195
  Quadriplegia: 0.57

1 DALY = 1 lost year of healthy life
Cost-effectiveness threshold (WHO): <1–3× GDP per capita per DALY averted = cost-effective
```

### Demographic and Epidemiological Transition

```
DEMOGRAPHIC TRANSITION MODEL:
Stage 1: High birth/death rates; stable low population (pre-industrial)
Stage 2: Death rate ↓ (sanitation/antibiotics); birth rate stays high → population explosion
Stage 3: Birth rate ↓; slower growth
Stage 4: Low birth/death rates; aging population; natural decrease possible

EPIDEMIOLOGICAL TRANSITION (Omran):
Stage 1: Pestilence and famine dominate — infectious disease
Stage 2: Receding pandemics — infectious disease declining
Stage 3: Degenerative and man-made diseases dominate — NCDs
Stage 4 (modern): Delayed degenerative diseases — cancer/CVD in elderly
                   Re-emerging infections (AMR, zoonoses)

CURRENT GLOBAL BURDEN (GBD 2019):
Leading causes of death:
  1. Ischemic heart disease
  2. Stroke
  3. COPD
  4. Lower respiratory infections (pneumonia)
  5. Neonatal disorders
  6. Trachea/lung cancer
  7. Alzheimer's and dementia
  8. Diabetes
  9. Diarrheal diseases
  10. Kidney disease

Regional variation:
  SSA: HIV, malaria, TB, neonatal, diarrheal still major
  LMIC: double burden: NCDs ↑ while infectious diseases remain
  High-income: CVD, cancer, dementia dominate

DALY contributors vs mortality:
  Mental disorders, MSK disorders, neurological — high DALY, lower mortality
  → Disability burden often invisible in mortality statistics
```

---

## Decision Cheat Sheet

| Question | Best Design | Key Measure |
|----------|-------------|-------------|
| Does drug X prevent disease Y? | RCT | RR, NNT |
| Does exposure Z cause disease Y in general population? | Cohort | RR, ARD |
| What caused this outbreak of rare disease? | Case-control | OR |
| What % of population has disease now? | Cross-sectional | Prevalence |
| Can group-level data suggest an association? | Ecological | Correlation (hypothesis only) |
| How contagious is pathogen? | R₀ calculation | R₀, HIT |
| Is this screening test worth deploying? | Wilson-Jungner + cost-effectiveness | Sensitivity, specificity, PPV, DALY |

### Confounding vs Effect Modification

| Feature | Confounding | Effect modification |
|---------|-------------|---------------------|
| Definition | Third variable distorts association | Third variable changes magnitude of association |
| Stratum-specific estimates | Similar (same direction) | Different across strata |
| Action | Remove/control (statistical adjustment) | Report separately; do not remove |
| Example | Age confounds smoking-cancer (smokers older) | Sex modifies aspirin-MI effect |

---

## Common Confusion Points

**R₀ vs Rₑ:**
R₀ = theoretical reproduction number in 100% susceptible population. Rₑ = actual "effective" R as population gains immunity. Epidemic grows when Rₑ > 1; herd immunity = Rₑ drops below 1.

**OR vs RR — when to use which:**
OR from case-control; RR from cohort/RCT. When disease is rare (prevalence <10%), OR ≈ RR. When disease is common (e.g., 30% outcome rate), OR inflates the association relative to RR — this is the "rare disease assumption."

**Sensitivity vs PPV:**
Sensitivity is fixed property of the test (in the diseased population). PPV depends on prevalence — same test, lower-risk population → lower PPV. High false positive rates when screening low-prevalence populations.

**Lead time vs length bias:**
Lead time: early detection shifts diagnosis date earlier but doesn't extend life → inflates survival times. Length bias: screening catches slow cancers disproportionately → screened patients look better because they have indolent disease, not because screening helped.

**Attack rate vs incidence rate:**
Both are cumulative incidence (risk = proportion). "Attack rate" = term used in outbreak investigation for short-duration outbreaks. Incidence rate = events per person-time (used for chronic disease epidemiology).

**CFR vs IFR:**
CFR = deaths / confirmed cases (biased by testing coverage; always ≥ IFR). IFR = deaths / all infections. COVID-19 CFR early pandemic ~1–3% (limited testing) vs IFR ~0.1–0.2% (seroprevalence studies). IFR is the truer estimate of lethality.

**Herd immunity thresholds are minimum, not targets:**
HIT assumes uniform random mixing. Real populations cluster → effective coverage needs to be higher than HIT in some subgroups to prevent local Rₑ > 1. "Herd immunity at 95%" doesn't mean outbreaks can't occur in pockets of <80% coverage.
