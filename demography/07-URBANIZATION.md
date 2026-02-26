# Urbanization

## The Urban Transition

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    GLOBAL URBANIZATION TREND                                 │
│                                                                               │
│  % Urban:                                                                     │
│                                                                               │
│  1800: ~3%    Cities: London 1M, Beijing 1M (only two ≥ 1M)                │
│  1900: ~13%   Industrial revolution → urban growth in Europe, N. America    │
│  1950: ~29%   Post-WWII industrialization; developing world urbanizing       │
│  2007: ~50%   MILESTONE: First time more people in cities than rural        │
│  2023: ~56%   4.4B urban dwellers                                            │
│  2050: ~68%   Projected; 6.7B urban (net growth = megacity equivalents)     │
│                                                                               │
│  CURRENT REGIONAL URBANIZATION RATES:                                       │
│  North America: 83%  | South America: 83%  | Europe: 75%                    │
│  Asia: 52%           | Africa: 44% (fastest growing, absolute largest growth)│
│  Oceania: 68%        |                                                        │
│                                                                               │
│  URBAN GROWTH HOTSPOTS 2023-2050:                                           │
│  India: +416M urban                                                          │
│  China: +255M urban                                                          │
│  Nigeria: +189M urban                                                        │
│  These 3 countries = ~35% of global urban growth                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Why Cities Exist — Economic Geography

```
URBAN AGGLOMERATION ECONOMIES:
  Cities exist because co-location generates economic returns exceeding costs.
  Three sources (Marshall 1890):
  1. Labor market pooling: larger pool → better job-worker matches
     Workers don't quit every time a firm closes; firms hire in large pool
  2. Input sharing: specialized suppliers can reach scale serving many nearby firms
     (legal, accounting, specialized manufacturing)
  3. Knowledge spillovers: ideas diffuse through proximity
     "Knowledge is in the air" (Marshall) — face-to-face interaction, informal

  MODERN FORMALIZATION (Glaeser, Lucas & Rossi-Hansberg):
  μ(density) = total factor productivity premium from density
  Empirical estimate: doubling city density → ~2-6% productivity increase
  (varies by sector; highest for information-intensive industries)

URBAN SCALING LAWS (Bettencourt et al. 2007):
  Y ∝ N^β   where N = city population, Y = urban metric

  SUPERLINEAR (β > 1): socioeconomic metrics scale faster than population
  GDP per capita: β ≈ 1.13
  Innovation (patents, R&D): β ≈ 1.15-1.20
  Wages: β ≈ 1.10
  Crime: β ≈ 1.15
  → 2× city population → 2^1.15 ≈ 2.22× more GDP, innovation, AND crime

  SUBLINEAR (β < 0.85): infrastructure scales slower than population (efficiency)
  Road lane miles: β ≈ 0.83
  Total electrical cable: β ≈ 0.84
  → Infrastructure economies of scale: larger cities more efficient per capita

  LINEAR (β ≈ 1): employment, housing units scale proportionally

  MECHANISM: Superlinear social metrics from increased interaction rate per person
  (interaction rate ∝ N/area; area ∝ N^{0.85} due to density increase → per-person
  contact ∝ N^{0.15} → returns > linear)

  CONNECTION TO INFORMATION THEORY: Superlinear scaling of knowledge production
  reflects network effects — see information-theory/ and Zipf in next section.
```

## Zipf's Law and Urban Hierarchy

```
ZIPF'S LAW FOR CITIES:
  Rank × Size ≈ constant
  P_r ∝ 1/r^α   where α ≈ 1

  More precisely:
  P_r = P_1 / r^α
  where P_r = population of city ranked r, P_1 = largest city population

  EMPIRICAL REGULARITY:
  For the US city size distribution: α ≈ 1.0 (Zipf exponent ≈ 1)
  2nd-largest city ≈ 1/2 the largest
  3rd-largest city ≈ 1/3 the largest
  10th-largest city ≈ 1/10 the largest

  US 2020 (Metro Statistical Areas):
  1. New York: 20.1M → rank × size = 20.1M
  2. Los Angeles: 13.2M → 2 × 13.2 = 26.4M (slight deviation)
  3. Chicago: 9.5M → 3 × 9.5 = 28.5M
  4. Dallas: 7.7M → 4 × 7.7 = 30.8M
  Average: roughly consistent with Zipf

  LOG-LOG PLOT:
  log(rank) vs. log(size) → approximately linear with slope ≈ -1
  → Power law distribution of city sizes

  THEORY: WHY ZIPF?
  Multiple mechanisms proposed; no single consensus:
  - Gibrat's law (proportional random growth): if cities grow proportionally
    with independent random shocks → Pareto/power law in long run
  - Yule process (preferential attachment)
  - Self-organized criticality
  - Convergent point of network and sorting dynamics

  CONNECTION TO INFORMATION THEORY:
  Zipf's law appears across: city sizes, word frequencies, firm sizes,
  income distributions, earthquake magnitudes, solar flare intensities.
  The ubiquity suggests a deep mathematical/information-theoretic origin.
  Zipf (1949): minimization of effort → power law; connection to
  minimum description length / entropy maximization (see information-theory/)

PRIMATE CITIES:
  When the Zipf distribution is NOT followed — one city dominates enormously.
  Paris: French population largest city / second city ≈ 8-10× (not 2×)
  Bangkok, Jakarta, Kinshasa, Lagos: similarly primate
  Causes: colonial capital development; political centralization;
    poor secondary city development; road network hub-and-spoke

  PRIMATE CITY PROBLEMS:
  Economic overconcentration → congestion costs; high land costs;
  regional inequality (rural/secondary city vs. capital gap);
  political instability (large capital population can threaten government)
```

## Megacities and Urban Systems

### City Size Definitions (UN) and Megacities (2023)

| Size class | Population threshold | Examples |
|---|---|---|
| Small city | < 500,000 | |
| Medium city | 500,000 – 1M | |
| Large city | 1M – 5M | |
| Mega city | > 5M | |
| Very large megacity | > 10M | See below |

**Megacities > 10M (2023, approx.):**

| Urban agglomeration | Population | Region |
|---|---|---|
| Tokyo-Yokohama | ~37M | East Asia (world's largest) |
| Jakarta | ~34M | Southeast Asia |
| Delhi | ~32M | South Asia |
| Shanghai | ~27M | East Asia |
| Seoul | ~25M | East Asia |
| São Paulo | ~22M | Latin America |
| Mexico City | ~22M | Latin America |
| Beijing | ~22M | East Asia |
| Mumbai | ~21M | South Asia |
| New York | ~20M | North America |

Total: ~35 megacities globally.

WORLD CITY NETWORK (Sassen, Taylor):
  Global command-and-control functions concentrated in:
  Alpha++ cities: New York, London
  Alpha+: Paris, Tokyo, Singapore, Hong Kong, Los Angeles
  These cities function as nodes in the global economy, not just national capitals.
  Connectivity measured by presence of: advanced producer services
  (law, finance, accounting, consulting, advertising) offices across cities.

SECONDARY CITIES:
  Cities 500K-5M — most of future urban growth is in this tier.
  Often underresourced relative to growth speed.
  Infrastructure deficit: roads, water, sanitation, power built after population
  arrives rather than before (reactive, not proactive planning).
```

## Informal Settlements (Slums)

```
UN-HABITAT SLUM DEFINITION (one or more deficiency):
  1. Lack of access to improved water
  2. Lack of access to improved sanitation
  3. Lack of durable housing
  4. Insufficient living area (overcrowding > 3 persons/room)
  5. Lack of security of tenure

  GLOBAL SCALE:
  ~1.1B people in slums (2020)
  Sub-Saharan Africa: ~60% of urban population in slums
  South Asia: ~35%
  Southeast Asia: ~30%
  Latin America: ~20%

  Examples: Dharavi (Mumbai): ~700K in 2.4 km²; Kibera (Nairobi): ~250-500K;
            Mathare (Nairobi), Manshiyat Nasser (Cairo), Cite Soleil (Haiti)

FORMATION MECHANISM:
  Rural-urban migrants arrive faster than formal housing market can accommodate.
  Informal settlements form on vacant/marginal land:
    Riverbanks, hillslopes, railway margins, flood plains
    (Less valuable/disputed land → easier occupation)
  Community self-builds incrementally over time.
  Infrastructure added by community or NGOs; formal services absent.

SLUM UPGRADING VS. RELOCATION:
  RELOCATION: move slum residents to formal housing
    Often fails: residents return to original locations (economic livelihood)
    or new relocation sites too far from employment
  UPGRADING: formalize tenure + improve infrastructure in place
    Evidence better: improves health, economic outcomes without displacement
    Examples: Brazilian favela upgrading, South African BNG housing program
    Challenges: resistance from property owners; political will

HEALTH IN INFORMAL SETTLEMENTS:
  Overcrowding → respiratory disease transmission (TB, COVID, measles)
  Lack of sanitation → diarrheal disease (cholera, typhoid)
  Standing water → vector-borne disease (malaria, dengue in tropical cities)
  Air pollution from cooking fires + traffic
  Paradox: urban slums may have lower under-5 mortality than rural areas
    (closer to health facilities) but higher infectious disease burden
```

## Urban-Rural Health Gradient

```
URBAN HEALTH ADVANTAGE (historic):
  Access to hospitals, doctors, specialists
  Better access to emergency services
  Higher income → better nutrition, housing, sanitation
  More educated → better health behaviors

URBAN HEALTH DISADVANTAGE:
  Air pollution (traffic, industry)
  Urban heat island (climate change intensifying)
  Stress, noise, crowding
  Sedentary lifestyle (car-dependent cities)
  Processed food environments
  Mental health: social isolation in anonymous urban settings

RURAL HEALTH CHALLENGES:
  Provider shortage (physicians/hospitals concentrated in cities)
  Distance to emergency care
  Higher injury rates (agriculture, transport)
  Fewer specialty services

  US RURAL-URBAN MORTALITY GAP (widening since 1999):
  Rural US now has higher all-cause mortality than urban US
  Driven by: drug overdose, CVD, unintentional injury, suicide
  Rural populations older, lower income, higher obesity, higher uninsured rate
  "Deaths of despair" (Case & Deaton): concentrated in rural and deindustrialized regions
```

## Decision Cheat Sheet

| Urbanization question | Concept |
|---|---|
| Why do cities generate more productivity per person? | Agglomeration economies: Marshall externalities + scaling |
| Why does city size distribution follow a power law? | Zipf's law: rank × size ≈ constant; emergent from proportional random growth |
| How much more productive is a larger city? | Y ∝ N^1.15: 2× population → 2.22× GDP per capita (approximately) |
| Why is Paris so dominant vs. Lyon? | Primate city: colonial concentration + political centralization |
| How many people live in slums globally? | ~1.1B; ~60% of Sub-Saharan African urban population |
| What's the best intervention for slum improvement? | In-place upgrading + tenure security > forced relocation |
| Are cities healthier than rural areas? | Historically yes; in US today, urban advantage has narrowed/reversed for some metrics |

## Common Confusion Points

**Urban area vs. municipality**: Urban and rural are continuous, not binary. "City" boundaries may capture the legal municipality (e.g., the City of Detroit: 630,000) vs. the metro area (Detroit metro: 4.4M). International comparisons require consistent definitions. UN uses "agglomeration" to capture functional urban areas.

**Zipf's law is descriptive, not explanatory**: The empirical regularity (α ≈ 1) is remarkably consistent across many countries and time periods, but multiple mechanisms are consistent with it. Don't infer causality from the pattern; multiple distinct processes produce the same distribution.

**Agglomeration vs. congestion**: Agglomeration economies make cities productive. Congestion costs (land prices, commute time, crime, pollution) grow with density. Optimal city size is where marginal agglomeration benefit = marginal congestion cost. No city is exactly at this optimum; most large cities in developing countries are growing through their optimum (congestion >> agglomeration for late arrivals).

**Slum ≠ static**: Successful slums are dynamic. Dharavi has ~$1B/year economic output. Residents are often 2nd/3rd generation. Many slums have been upgraded over decades. Treating them as purely pathological misses their economic function as affordable entry points to urban economies.
