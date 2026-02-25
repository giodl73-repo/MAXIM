# Public Health — Landscape Overview

## The Big Picture: Population vs. Clinical Medicine

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        HEALTH INTERVENTION SPECTRUM                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  CLINICAL MEDICINE          PUBLIC HEALTH           POLICY / SYSTEMS          │
│  (individual level)         (population level)      (structural level)        │
│                                                                               │
│  ┌──────────────┐           ┌──────────────┐        ┌──────────────┐          │
│  │ Diagnosis    │           │ Surveillance  │        │ Health system│          │
│  │ Treatment    │           │ Epidemiology  │        │ design       │          │
│  │ Follow-up    │           │ Vaccination   │        │ Financing    │          │
│  │ Cure/manage  │           │ Health promo  │        │ Workforce    │          │
│  └──────────────┘           └──────────────┘        └──────────────┘          │
│         │                         │                        │                  │
│    Downstream:              Midstream:               Upstream:                │
│    Treat disease            Reduce risk at           Change conditions         │
│    after onset              population level         that create risk          │
│                                                                               │
│  NNT ≈ 1 patient            NNT = thousands          NNT = policy lever       │
│  High visibility            Low individual           Structural/invisible      │
│                             visibility                                         │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘

NNT = number needed to treat (or reach) for one outcome prevented
```

## Three Levels of Prevention

```
┌──────────────────┬──────────────────────────┬──────────────────────────────┐
│  PRIMARY         │  SECONDARY               │  TERTIARY                    │
│  (before disease)│  (early detection)       │  (limit disability)          │
├──────────────────┼──────────────────────────┼──────────────────────────────┤
│ Vaccines         │ Cancer screening         │ Cardiac rehab                │
│ Seat belts       │ BP measurement           │ Diabetes management          │
│ Fluoridation     │ HIV testing              │ Stroke physical therapy      │
│ Smoking bans     │ Neonatal screening       │ Opioid treatment programs    │
│ Safe sex ed      │ Mammography              │ Disability services          │
├──────────────────┼──────────────────────────┼──────────────────────────────┤
│ Goal: prevent    │ Goal: catch early,       │ Goal: prevent progression,   │
│ disease onset    │ intervene before         │ reduce disability burden     │
│                  │ advanced disease         │                              │
└──────────────────┴──────────────────────────┴──────────────────────────────┘

PRIMORDIAL prevention: address social determinants before individual risk
factors emerge (e.g., poverty reduction → reduced CVD risk decades later).
Often most powerful. Least visible. Hardest to measure.
```

## The Public Health System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      PUBLIC HEALTH SYSTEM LAYERS                             │
│                                                                               │
│  GLOBAL          WHO, PAHO, UNICEF, Global Fund, Gavi, CEPI                  │
│     │            International Health Regulations (IHR 2005)                 │
│     ↓            Coordinates across 194 member states                        │
│  NATIONAL        CDC (US), ECDC (EU), UKHSA (UK), PHAC (Canada)             │
│     │            National surveillance, immunization schedules                │
│     ↓            Sets standards, allocates federal resources                 │
│  STATE/REGIONAL  State health departments (50 in US)                         │
│     │            Regional public health labs, epidemiologists                │
│     ↓            Primary regulatory authority in US for most PHLaws          │
│  LOCAL           County/city health departments                               │
│     │            Front-line inspection, community programs                   │
│     ↓            Restaurant inspection, STI clinics, WIC                     │
│  COMMUNITY       FQHCs, CHCs, NGOs, schools, workplaces, pharmacies          │
│                  Point of contact with individuals                            │
└─────────────────────────────────────────────────────────────────────────────┘

FQHC = Federally Qualified Health Center (sliding-scale primary care)
CHC  = Community Health Center
WIC  = Women, Infants, Children nutrition program
```

## Core Disciplines

| Discipline | Core Question | Key Methods |
|---|---|---|
| **Epidemiology** | What causes disease in populations? | Cohort, case-control, RCT, surveillance |
| **Biostatistics** | How do we measure and infer? | Regression, survival analysis, meta-analysis |
| **Health behavior** | Why do people do what they do? | Survey, behavioral theory, nudge design |
| **Environmental health** | What exposures harm populations? | Exposure assessment, GIS, toxicology |
| **Health policy / economics** | How do systems and incentives shape health? | Cost-effectiveness, comparative systems |
| **Global health** | How do we reduce global health inequity? | DALY burden, program evaluation |
| **Social epidemiology** | How do social structures cause disease? | SES gradients, structural racism metrics |
| **Occupational health** | How does work harm workers? | Cohort studies, regulatory standards |

## Healthy People Framework (US)

The US federal framework sets decade-long, measurable public health objectives:

```
Healthy People 2030 structure:
  ├── Leading Health Indicators (20 high-priority measures)
  ├── Health Objectives (~358 measurable, time-bound goals)
  └── Evidence-Based Resources (proven intervention catalog)

Example objectives (HP2030):
  IID-08: ≥90% of children with 2-dose MMR coverage
  AHS-01: Increase % of people with a usual primary care provider
  TU-01:  Reduce adult cigarette smoking to ≤6.1%
  NWS-04: Reduce obesity prevalence (target: 36.0%)
  OA-01:  Reduce rate of older adults falling
```

## Determinants of Health — Full Causal Chain

```
┌─────────────────────────────────────────────────────────────────────────────┐
│           DETERMINANTS OF HEALTH (Dahlgren-Whitehead concentric model)       │
│                                                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐     │
│  │  MACRO: Socioeconomic, cultural, environmental conditions           │     │
│  │  ┌───────────────────────────────────────────────────────────────┐ │     │
│  │  │  COMMUNITY: Social networks, social capital, norms            │ │     │
│  │  │  ┌─────────────────────────────────────────────────────────┐ │ │     │
│  │  │  │  LIVING/WORKING: Physical environment, employment        │ │ │     │
│  │  │  │  ┌───────────────────────────────────────────────────┐  │ │ │     │
│  │  │  │  │  INDIVIDUAL LIFESTYLE: Diet, smoking, exercise     │  │ │ │     │
│  │  │  │  │  ┌─────────────────────────────────────────────┐  │  │ │ │     │
│  │  │  │  │  │  CORE: Age, sex, constitutional genetics    │  │  │ │ │     │
│  │  │  │  │  └─────────────────────────────────────────────┘  │  │ │ │     │
│  │  │  │  └───────────────────────────────────────────────────┘  │ │ │     │
│  │  │  └─────────────────────────────────────────────────────────┘ │ │     │
│  │  └───────────────────────────────────────────────────────────────┘ │     │
│  └─────────────────────────────────────────────────────────────────────┘     │
│                                                                               │
│  Most interventions target individual level.                                  │
│  Most health INEQUALITY is generated at community and macro levels.           │
│  Most public health SPENDING is consumed at clinical/individual level.        │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Measuring Population Health — Key Metrics

| Metric | Definition | Use case |
|---|---|---|
| **Incidence rate** | New cases / person-time at risk | Etiology, vaccine efficacy |
| **Prevalence** | Existing cases / population at time T | Health planning, burden estimation |
| **Mortality rate** | Deaths / population / year | Comparative tracking |
| **Case fatality rate (CFR)** | Deaths / confirmed cases | Severity of disease |
| **Years of life lost (YLL)** | Life-years lost due to premature death | Priority setting |
| **DALY** | YLL + YLD (years lived with disability) | Global burden comparison |
| **QALY** | Quality-adjusted life year | Cost-effectiveness analysis |
| **Life expectancy** | Expected years from birth (or age x) | Overall population health |

See 10-HEALTH-METRICS.md for full methodology.

## Module Map

| Module | Core Content |
|---|---|
| 01-EPIDEMIOLOGY-FUNDAMENTALS | RR, OR, AR, NNT; study designs; confounding; Bradford Hill |
| 02-DISEASE-SURVEILLANCE | Signal detection; notifiable diseases; syndromic systems; IHR |
| 03-INFECTIOUS-DISEASE-CONTROL | R0, Rt, herd immunity threshold; outbreak response steps |
| 04-VACCINES-IMMUNIZATION | Vaccine types; immunological mechanisms; cold chain; hesitancy |
| 05-CHRONIC-DISEASE | NCD burden; screening programs; lead time bias; risk factors |
| 06-ENVIRONMENTAL-HEALTH | PM2.5; dose-response; climate-health; environmental justice |
| 07-GLOBAL-HEALTH | DALY methodology; WHO governance; global health financing |
| 08-HEALTH-POLICY | Bismarck/Beveridge/out-of-pocket; UHC dimensions; financing |
| 09-PANDEMIC-RESPONSE | PHEIC; NPI evidence; supply chain; COVID-19 lessons |
| 10-HEALTH-METRICS | DALY/QALY computation; standardization; GBD |

## Decision Cheat Sheet

| If you need to... | Use module... |
|---|---|
| Understand cause-effect for a disease | 01-EPIDEMIOLOGY-FUNDAMENTALS |
| Detect outbreaks early | 02-DISEASE-SURVEILLANCE |
| Control a pathogen in a community | 03-INFECTIOUS-DISEASE-CONTROL |
| Evaluate a vaccination program | 04-VACCINES-IMMUNIZATION |
| Reduce CVD/diabetes/cancer burden | 05-CHRONIC-DISEASE |
| Address pollution or climate-health links | 06-ENVIRONMENTAL-HEALTH |
| Compare global disease burden | 07-GLOBAL-HEALTH + 10-HEALTH-METRICS |
| Compare health systems across countries | 08-HEALTH-POLICY |
| Prepare for or learn from a pandemic | 09-PANDEMIC-RESPONSE |
| Compute DALYs or QALYs | 10-HEALTH-METRICS |

## Common Confusion Points

**Public health vs. population health vs. community health**: Often used interchangeably. Strict usage: public health = government-organized collective action; population health = any defined population (e.g., employer's workforce, insurance enrollees); community health = geographically defined community focus. Population health is the broader concept; public health is its primary institutional form.

**Prevention vs. treatment — why prevention is underfunded**: The political economy systematically underinvests in prevention: (a) benefits are invisible — nothing happened; (b) benefits are diffuse and delayed; (c) no "patient lobby" exists for prevented diseases; (d) electoral cycles don't align with decades-long prevention returns. This is a classic market failure + collective action problem requiring public coordination.

**Relative risk vs. absolute risk**: A 50% relative risk reduction in a disease with 0.0002% baseline incidence is a 0.0001% absolute reduction. NNT = 1 / ARR = 1,000,000 people to prevent one case. Public health communicators routinely confuse these. Always seek both.

**Incidence vs. prevalence**: Incidence = new cases per time period at risk. Prevalence = existing cases at a point in time. P ≈ I × D (prevalence ≈ incidence × mean duration). Interventions that reduce duration (better treatment) reduce prevalence without changing incidence. This distinction matters enormously for interpreting surveillance data.

**Efficacy vs. effectiveness**: Efficacy = works under ideal randomized trial conditions. Effectiveness = works in real-world delivery. The gap is the implementation challenge: cold chain failures, adherence, access barriers, provider variation. A 95%-efficacious vaccine delivered to 50% of the target population has 47.5% population effectiveness.
