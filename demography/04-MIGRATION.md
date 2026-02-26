# Migration

## Migration Landscape

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MIGRATION TAXONOMY                                        │
│                                                                               │
│  BY GEOGRAPHY:         BY DURATION:          BY MOTIVATION:                 │
│  International         Temporary/circular    Economic (labor)               │
│  Internal/domestic     Seasonal              Forced/humanitarian            │
│    Rural-urban         Semi-permanent        Family reunification           │
│    Urban-rural (return)Permanent             Environmental/climate          │
│    Region to region                          Education                      │
│                                                                              │
│  BY DOCUMENTATION:     BY DIRECTION:                                        │
│  Documented/legal      Emigration (leaving)                                 │
│  Undocumented/irregular Immigration (arriving)                              │
│  Asylum seekers        Return migration                                     │
│  Refugees              Transit migration                                    │
│                                                                               │
│  SCALE (2020):                                                               │
│  ~281M international migrants = 3.6% of world population                    │
│  ~1B+ internal migrants (domestic rural-urban)                              │
│  ~100M forcibly displaced (2023 — new record)                               │
│  ~26M refugees under UNHCR mandate (2023)                                   │
│  ~5.4M asylum seekers pending decisions                                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Classic Theoretical Models

### Ravenstein's Laws (1885)

The foundation of migration theory, remarkably durable:

1. Most migrants travel short distances (distance-decay)
2. Migration proceeds step by step (urban hierarchy climbing)
3. Long-distance migrants prefer commercial/industrial centers
4. Each migration stream produces a compensating counter-stream
5. Urban natives are less migratory than rural natives
6. Females predominate in short-distance migration; males in long-distance
7. Economic motives predominate

### Everett Lee's Push-Pull Model (1966)

```
ORIGIN (push factors)          DESTINATION (pull factors)
─────────────────────          ────────────────────────────
Unemployment/low wages    →    Employment/high wages
Political persecution    →    Political freedom
Environmental degradation →   Resource availability
Conflict, violence       →    Safety, stability
Limited education        →    Educational opportunities
Land scarcity            →    Land abundance
                     MINUS
INTERVENING OBSTACLES:
  Distance (cost, information, culture)
  Immigration policies (legal barriers)
  Information asymmetry
  Social networks (or lack thereof)
  Physical geography (deserts, seas)

DECISION FUNCTION:
  Migrate if: E[benefits at destination] − E[costs of migrating] > E[benefits at origin]
  Where E[·] = expected value accounting for uncertainty and risk aversion

  Probability of migrating depends on:
  - Size of wage/income differential
  - Strength of networks at destination (reduce information/cost)
  - Immigration policy enforcement
  - Individual characteristics (age, education, risk tolerance)
```

### Gravity Model

```
GRAVITY MODEL OF MIGRATION:
  M_ij = K × (P_i^α × P_j^β) / D_ij^γ

  where:
  M_ij = migration flow from i to j
  P_i  = population of origin i
  P_j  = population of destination j
  D_ij = distance between i and j
  K, α, β, γ = parameters

  The same form as Newton's law of gravitation — larger, closer → more interaction.

  TYPICAL EMPIRICAL FINDINGS:
  γ ≈ 2: migration falls off as square of distance
    (though long-distance international migration less distance-sensitive
     than short-distance internal migration)
  α, β ≈ 0.5-1.0

  EXTENSIONS:
  Wilson's doubly-constrained model: enforce both origin and destination totals
  Negative binomial regression: better for count data with overdispersion
  Heckman selection models: migrant pool is non-random (selected)
```

## Migration Selectivity

Migration is not random. Migrants differ systematically from both the origin and destination populations:

```
POSITIVE SELECTION (high-skilled migration):
  Migrants typically have higher education, skills, motivation,
  risk tolerance than average at origin.
  Evidence: international labor migrants earn more on average than
  similar-background non-migrants.
  Reason: higher return to skills in destination country (especially
  for those moving from low- to high-income countries)

  Chiswick's finding (1978): immigrants to the US earn less than
  natives at arrival but catch up and eventually EXCEED comparable
  native earnings within 10-15 years. (Later contested by Borjas:
  depends on origin country and period.)

NEGATIVE SELECTION:
  Occurs when origin country has high inequality + costly migration.
  Those from top of origin distribution don't gain as much from moving.
  Those from bottom can't afford to move.
  Middle of distribution most likely to migrate (negative selection
  relative to origin top; positive relative to origin bottom).

ROY MODEL:
  Formal framework for migration selection.
  Workers select location based on return to their skills.
  If skill returns are high at destination relative to origin:
  → positively selected migrants (skilled workers choose to move)
  If skill returns are similar: more negative selection

  Roy (1951) original context was occupational selection; Borjas applied to migration.

HEALTH SELECTIVITY — "HEALTHY MIGRANT EFFECT":
  International migrants are healthier than both origin and destination averages.
  Reason: physical/economic requirements of migration self-select healthy individuals.
  Dilution over time: immigrants converge toward destination health patterns.
  For labor migrants: health advantage erodes as they age in destination country.
```

## Diaspora Networks and Migration Systems

```
NETWORK EFFECTS ON MIGRATION:
  Once a migration stream is established, networks dramatically lower
  barriers for subsequent migrants from same origin.
  Mechanisms:
  - Information: existing migrants provide accurate information on
    destination labor market, housing, social services
  - Financial: savings transferred back; loans for migration costs
  - Social: housing on arrival, job referrals, cultural community
  - Legal: guidance on documentation, visa processes

  Network effect: each additional migrant raises probability that
  a potential migrant from same community will migrate.
  Creates self-reinforcing migration streams and corridors.

MIGRATION SYSTEMS THEORY:
  Migration flows are embedded in bilateral relationships
  (colonial ties, trade links, investment, cultural affinity).
  Major corridors reflect historical connections:
    Mexico → US (proximity + labor history + networks)
    India → UAE/UK/US (former colonial ties + professional migration)
    Morocco → France/Spain (colonial + labor history)
    Philippines → Saudi Arabia/UAE/US (labor export policy + networks)

CUMULATIVE CAUSATION (Massey):
  Migration causes conditions in origin community that make further
  migration more likely (not less).
  Mechanisms:
  - Networks: information, social capital
  - Culture of migration: normalized as life strategy for young adults
  - Relative deprivation: comparison to neighbors who migrated → want to migrate
  - Distribution of land: migrants invest remittances in land → less productive
    use than if they stayed
  - Human capital depletion: best-educated leave → remaining less skilled
  Implication: migration streams are inherently persistent once established;
  don't automatically self-correct via wage convergence.
```

## Remittances

```
REMITTANCES — GLOBAL SCALE:
  2023: ~$860B in global remittances (formal channels)
  Informal channels: additional 30-50%
  Largest recipient countries (absolute):
    India: ~$125B, Mexico: ~$67B, China: ~$50B, Philippines: ~$40B, Egypt: ~$28B
  Largest relative to GDP (remittance-dependent):
    Tonga: ~50% GDP, Samoa: ~30%, Lebanon: ~25%, Kyrgyzstan: ~30%

REMITTANCE CHARACTERISTICS:
  More stable than FDI or ODA (resilient during financial crises — migrants
    send MORE during home-country downturns to support families)
  Countercyclical: destination country recession → less; origin recession → more
  Micro-level impact: consumption, education, health, housing in receiving households
  Macro-level impact: significant FX inflows; can cause Dutch disease (currency appreciation
    → domestic tradables less competitive)

COSTS OF REMITTANCE TRANSFER:
  Average global cost: ~6% in 2023 (vs. SDG target of 3%)
  Sub-Saharan Africa highest corridor fees: ~8-10%
  Mobile money (M-Pesa, Wave): disrupting traditional providers
  Blockchain-based transfer: potential for cost reduction
```

## Brain Drain vs. Brain Gain

```
BRAIN DRAIN:
  Emigration of skilled workers → loss of human capital from origin country.
  Mechanism:
  Develop medical school → train doctors → doctors emigrate for 3-10× salary
  → origin country subsidized destination country's health system

  Affected sectors: medicine, nursing, engineering, IT, academia
  Worst cases: sub-Saharan Africa medical brain drain
    Ghana trains doctors who practice primarily in UK, Canada, US
    Ethiopia: 50-80% of medical graduates emigrate within 5 years of training
    Caribbean nurses: majority practice abroad

BRAIN GAIN / CIRCULATION:
  Counter-arguments and counter-evidence:
  1. Brain drain incentivizes additional education investment ("brain gain")
     Mountford/Vidal model: prospect of emigration → more invest in education
     → some stay → origin benefits even if some emigrate
  2. Diaspora provides: remittances, technology transfer, investment, trade networks
  3. Return migration: some emigrants return with skills, capital, networks
     (India/China IT professionals: Silicon Valley → Bangalore/Shenzhen)
  4. For very small countries: option is brain drain OR brain overflow
     (can't employ all skilled workers domestically)

  NET ASSESSMENT: For small, poor, health-sector-depleted countries, brain drain
  is a genuine development problem despite positive spillovers from diaspora.
  For large MICs (India, China): brain circulation story more convincing.
```

## Internal Migration and Urbanization

```
RURAL-URBAN MIGRATION MECHANICS (Harris-Todaro Model, 1970):
  Migration decision based on expected urban wage, not actual:
  W_rural = p_employed × W_urban_formal
  where p_employed = probability of finding formal sector employment

  Migration continues until: W_rural = p_employed × W_urban
  Even high urban unemployment doesn't stop migration if W_urban_formal
  is high enough (probability × wage still exceeds rural wage).

  This explains: continued rural-urban migration in cities with 30-40%
  unemployment rates (Lagos, Dhaka, etc.)

  CRITIQUE: Model treats employment as search problem;
  ignores informal sector (most urban poor earn something);
  ignores non-economic migration motives.

INTERNAL MIGRATION IN CHINA:
  ~300M rural-urban migrants (the "floating population")
  Hukou system: household registration tied to birthplace → limits
    access to urban schools, healthcare, social services without local hukou
  Reform path: gradual relaxation; still significant constraint
  Economic effect: massive labor reallocation from low-productivity agriculture
    to higher-productivity manufacturing → major driver of Chinese growth
```
<!-- @editor[content/P2]: Internal migration section covers only Harris-Todaro + China — India's internal migration (~450M, largest absolute flow) and US Sunbelt/Rustbelt patterns are significant gaps for this topic -->

## Climate Migration

```
CLIMATE MIGRATION — PROJECTIONS:
  World Bank Groundswell report: 216M internal climate migrants by 2050
  (agricultural failure, water scarcity, sea-level rise, heat stress)
  High-end estimates: 1B+ international climate migrants (low probability, high impact)

  CURRENT EVIDENCE:
  - Bangladesh: coastal flooding/cyclones → internal displacement → Dhaka growth
  - Sahel: desertification → Sahelian migration to coastal West Africa + North Africa
  - Pacific islands: sea-level rise (Kiribati, Maldives) → early movers
  - Hurricane Maria (Puerto Rico 2017): >400,000 to mainland US

  COMPLICATIONS:
  - Distinguish climate-driven from economic migration (often both)
  - Most climate migration will be internal, not international
  - Poorest most exposed but least able to migrate (migration requires resources)
  - "Trapped populations": too poor to move, most vulnerable
```

## Decision Cheat Sheet

| Migration question | Framework |
|---|---|
| What drives international migration flows? | Push-pull model; Roy model for selection |
| Why do migration streams persist after wage gap narrows? | Network effects; cumulative causation |
| Are migrants selected on skill? | Roy model; empirically: mostly positively selected |
| What's the health status of recent immigrants? | Healthy migrant effect; deteriorates over time |
| Impact of remittances on origin country? | Consumption/education/health gains at household level; FX at macro level |
| How much does brain drain cost origin countries? | Case-by-case; severe in small, health-sector-depleted countries |
| What migration is climate change causing? | Primarily internal; displacement from flood/drought; poorest most trapped |

## Common Confusion Points

**Refugees vs. migrants vs. asylum seekers**: Refugees = legally recognized protection under 1951 Refugee Convention (persecution-based). Asylum seekers = applied for refugee status, pending decision. Migrants = broad category including all who change residence, regardless of reason. Economic migrants are not refugees even if fleeing poverty.

**Undocumented immigration ≠ illegal immigration**: "Illegal" is politically loaded and technically imprecise. Many undocumented people entered legally and overstayed visas. Some have pending legal cases. Usage of "undocumented" or "unauthorized" is more accurate.

**Immigration and wages — the economics is contested**: Borjas (Harvard) finds immigration suppresses wages for low-skill native workers, especially among competing groups (prior immigrants). Card (Berkeley, Nobel 2021) finds minimal wage effects using Mariel Boatlift natural experiment. Disagreement reflects methodological differences in comparison group construction. Most economists find aggregate GDP gains from immigration; distributional effects vary.

**Brain drain is not a permanent loss**: Diaspora networks, return migration, remittances, and technology transfer partially offset the direct human capital loss. The net assessment depends on country size, skill intensity of emigration, diaspora engagement, and receiving country policies. Binary "drain" framing misses the complexity.
