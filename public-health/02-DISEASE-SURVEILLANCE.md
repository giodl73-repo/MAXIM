# Disease Surveillance

## Surveillance System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DISEASE SURVEILLANCE ECOSYSTEM                            │
│                                                                               │
│  DATA SOURCES           COLLECTION                ANALYSIS & ACTION          │
│                                                                               │
│  Clinicians/hospitals ──→ Passive/Mandatory ──→ Case counting               │
│  Laboratories ──────────→ Lab reporting ────→ Cluster detection             │
│  Pharmacies ────────────→ Syndromic ───────→ Signal generation              │
│  Emergency depts ───────→ Real-time feeds ─→ Alert thresholds               │
│  Mortality registries ──→ Vital statistics → Trend analysis                 │
│  Social media/news ─────→ Event-based ────→ Risk assessment                 │
│  Traveler screening ────→ PoE surveillance → Response activation            │
│                                                                               │
│  FEEDBACK LOOP: surveillance → public health action → disease control       │
│                 → changed disease pattern → updated surveillance             │
└─────────────────────────────────────────────────────────────────────────────┘

This is a distributed sensor network with:
  - Highly variable sensitivity across reporters
  - Systematic underreporting (iceberg phenomenon)
  - Heterogeneous data quality
  - Variable reporting latency
  - Missing data patterns correlated with burden
```

## Passive vs. Active vs. Sentinel Surveillance

```
┌──────────────────┬─────────────────────────┬────────────────────────────────┐
│  PASSIVE         │  ACTIVE                 │  SENTINEL                      │
├──────────────────┼─────────────────────────┼────────────────────────────────┤
│ Reporters submit │ System proactively       │ Selected high-quality sites    │
│ on own initiative│ contacts reporters       │ report all cases actively      │
│                  │                          │                                │
│ Low cost         │ Higher cost              │ Medium cost                    │
│ High coverage    │ Better completeness      │ Best data quality              │
│ Low completeness │ Timely for outbreaks     │ Not population-representative  │
│                  │                          │                                │
│ NNDSS (US)       │ Active TB contact tracing│ FluView sentinel physicians    │
│ MMWR case counts │ CDC enhanced surveillance│ EuroFlu sentinel network       │
│                  │                          │ WHO sentinel influenza sites   │
└──────────────────┴─────────────────────────┴────────────────────────────────┘
```

## Notifiable Disease Systems

### United States — NNDSS

```
NNDSS: National Notifiable Diseases Surveillance System
  ├── ~120 nationally notifiable conditions (CDC/CSTE list)
  ├── State health departments collect → report to CDC
  ├── Legally mandated reporting (state law, not federal)
  ├── Electronic Lab Reporting (ELR) increasingly automated
  └── Published weekly in MMWR (Morbidity and Mortality Weekly Report)

Tier 1 (immediate reporting, 24 hours):
  Anthrax, botulism, cholera, hemorrhagic fevers, SARS, smallpox, plague

Tier 2 (standard reporting, 3 business days):
  HIV, TB, hepatitis, STIs, foodborne outbreaks, meningitis

  Data completeness varies: TB ≈ 95% reported; STIs ≈ 50–70%
  Gonorrhea: estimated 1.6M cases/yr vs ~700K reported → ~2× multiplier
```

### WHO Global Surveillance

```
IHR 2005 — International Health Regulations:
  194 member states must:
  ├── Develop core surveillance capacities (Annex 1A)
  ├── Report potential PHEICs within 24 hours of assessment
  ├── Maintain points-of-entry (PoE) surveillance
  └── Respond to WHO requests for information

  PHEIC = Public Health Emergency of International Concern
  (declared: H1N1 2009, Polio 2014, Ebola 2014, Zika 2016,
   COVID-19 2020, Monkeypox 2022)

WHO Event Information System (EIS):
  Internal tracking of outbreak rumors and media reports
  → feeds into outbreak verification → IHR notifications
```

## Syndromic Surveillance

Traditional surveillance: clinician diagnoses → reports → data enters system → analysis.
Lag: days to weeks. Too slow for rapidly evolving outbreaks.

Syndromic surveillance uses pre-diagnostic signals:

```
SYNDROMIC DATA SOURCES:
  ├── ED chief complaints ("fever + rash", "difficulty breathing")
  ├── Over-the-counter pharmaceutical sales (antidiarrheal surge)
  ├── School/workplace absenteeism rates
  ├── Poison control center calls
  ├── Emergency medical service dispatch codes
  ├── Google search trends (Google Flu Trends — later failed badly)
  └── Social media NLP (HealthMap, ProMED)

SIGNAL DETECTION ALGORITHMS:
  CUSUMv (cumulative sum):
    St = max(0, St-1 + xt - μ - k)
    Alert when St > h (threshold)
    k = allowance (usually 0.5σ above baseline)
    h = decision interval

  EARS (Early Aberration Reporting System, CDC):
    C1/C2/C3 methods — compare current week to recent baseline
    C2: if observed > mean + 3×SD of prior 7 weeks → alert

  CUSUM tradeoffs:
    Lower h → faster detection, more false alarms
    Higher h → slower detection, fewer false alarms
    Sensitivity/specificity tradeoff identical to diagnostic testing
```

**Computing parallel**: Syndromic surveillance is analogous to anomaly detection in distributed systems monitoring — alerting on deviation from baseline before root cause is confirmed. CUSUM is the same algorithm used in quality control (Shewhart/Page). The fundamental problem is the same: minimize detection latency subject to false alarm constraints. CDC ESSENCE system = production deployment.

## Outbreak Investigation Protocol

```
OUTBREAK INVESTIGATION STEPS (CDC 10-step framework):

  1. PREPARE FOR FIELD WORK
     └── Safety protocols, data collection tools, team roles

  2. ESTABLISH EXISTENCE OF OUTBREAK
     └── Compare current counts to historical baseline (epidemic curve)

  3. VERIFY DIAGNOSIS
     └── Lab confirmation, exclude misdiagnosis, exclude surveillance artifact

  4. DEFINE AND IDENTIFY CASES
     └── Case definition: clinical + lab + epidemiological criteria
     └── Case definition spectrum: confirmed → probable → suspect

  5. DESCRIBE (PERSON, PLACE, TIME)
     └── Attack rates by demographic group
     └── Spot map: geographic clustering
     └── Epidemic curve: case counts over time

  6. DEVELOP HYPOTHESES
     └── Common source? Person-to-person? Environmental?
     └── Incubation period from curve → likely pathogen

  7. EVALUATE HYPOTHESES
     └── Analytic study: cohort (if all exposed known) or
         case-control (if too many exposed to enumerate)

  8. REFINE HYPOTHESES AND EXECUTE ADDITIONAL STUDIES
     └── Environmental investigation, food sampling, lab subtyping

  9. IMPLEMENT CONTROL AND PREVENTION MEASURES
     └── Often happens concurrently with investigation (can't wait for proof)

  10. COMMUNICATE FINDINGS
      └── Health department, public, scientific publication
```

## Epidemic Curve Interpretation

```
EPIDEMIC CURVE SHAPES:

  POINT SOURCE (common source, brief exposure):
       ██
     ████
    ██████
   ████████
  ─────────────────→ time
  Cases compressed within 1 incubation period
  Example: restaurant foodborne outbreak, single event

  CONTINUOUS COMMON SOURCE:
        ████████████
      ██████████████████
  ─────────────────────────────→ time
  Cases sustained while source active
  Example: contaminated water supply

  PROPAGATED (person-to-person):
    █       ██          ████
  ─────────────────────────────────→ time
  Successive waves, each ~1 incubation period apart
  Example: measles outbreak in school

  POINT SOURCE WITH SECONDARY SPREAD:
    ████     ██
  ─────────────────────→ time
  Initial cluster, then small secondary wave
```

## IHR Core Capacities and JEE

```
IHR ANNEX 1A — Required National Capacities:
  ├── Legislation and policy (legal framework for reporting)
  ├── Coordination (national focal point, inter-ministerial)
  ├── Surveillance (detection of unusual events)
  ├── Response (operations center, rapid response teams)
  ├── Preparedness (plans, exercises)
  ├── Risk communication (public communication capacity)
  ├── Human resources (trained epidemiologists — FETP)
  ├── Laboratory (national reference lab, specimen transport)
  ├── Points of entry (airports, seaports, ground crossings)
  ├── Zoonotic events (animal-human interface surveillance)
  ├── Food safety (foodborne disease surveillance)
  ├── Chemical events (chemical hazard detection)
  └── Radiation emergencies (radiological surveillance)

JEE (Joint External Evaluation):
  WHO voluntary peer-review of IHR capacity implementation.
  Scores 1–5 across 19 technical areas.
  Published publicly: https://extranet.who.int/sph/jee
  Used as metric for pandemic preparedness index (GHS Index).
  COVID-19 revealed: high JEE scores did not predict response quality.
```

## Iceberg Phenomenon and Ascertainment Bias

```
REPORTED CASES ← what surveillance systems count
       │
  Clinically diagnosed cases that weren't reported
       │
  Clinically diagnosed cases that weren't tested
       │
  Symptomatic cases that didn't seek care
       │
  Mild/asymptomatic cases (often majority for respiratory pathogens)
       │
TOTAL INFECTED POPULATION (true burden, often 10-100× reported)

SARS-CoV-2 example (2020):
  Seroprevalence studies → estimated true infections 10-20× reported cases
  IFR (infection fatality rate) ≈ 0.5-1%
  CFR (case fatality rate based on confirmed cases) ≈ 2-3%
  Discrepancy = iceberg phenomenon
```

## Decision Cheat Sheet

| Surveillance need | System type | Key considerations |
|---|---|---|
| Track nationally notifiable diseases | Passive/mandatory (NNDSS) | Underreporting, lag, legal framework |
| Detect outbreak before diagnosis confirmed | Syndromic (ESSENCE, BioSense) | False alarm rate, signal lag |
| Achieve high data quality on specific diseases | Sentinel network (FluView) | Not representative of all geography |
| Respond to international outbreak threat | IHR/PHEIC mechanism | 24hr notification requirement |
| Verify outbreak exists | Epidemic curve vs. historical baseline | Account for reporting artifacts |
| Investigate foodborne outbreak | Case-control among exposed | Attack rate analysis by food item |
| Assess national pandemic preparedness | JEE/IHR self-assessment | Score ≠ actual performance |

## Common Confusion Points

**Case definition changes mid-outbreak**: Alert when case counts change dramatically after case definition change. COVID-19 Wuhan counts changed when clinical criteria were added (Feb 2020) — counts spiked, looked like acceleration but was reclassification. Always annotate epidemic curves with definition changes.

**Syndromic surveillance vs. lab surveillance**: Syndromic is faster but non-specific. Lab confirmation is slow but specific. Optimal system uses syndromic for early alert, lab for confirmation. Google Flu Trends failure (2013): overfitted to search patterns that changed with media coverage, not actual flu. Big data ≠ good epidemiology.

**Outbreak vs. epidemic vs. cluster**: Outbreak = cases above expected in a defined place and time. Epidemic = widespread outbreak (sometimes used interchangeably). Cluster = geographic/temporal aggregation of cases — may or may not exceed expected rates. Always need a denominator to determine if rate is elevated.

**Reporting lag and nowcasting**: Reported cases on day T reflect infections from days T-14 (or longer). Real-time epidemic curves are right-truncated — recent counts appear to decline simply because cases haven't been reported yet. Nowcasting methods (e.g., Bayesian deconvolution) estimate true current incidence from delayed reporting.
