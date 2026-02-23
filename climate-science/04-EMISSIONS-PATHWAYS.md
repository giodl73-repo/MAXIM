# Emissions & Pathways

## RCP/SSP Scenarios, Carbon Budget Math, Sector Contributions, Net Zero

## The Big Picture

```
EMISSIONS → TEMPERATURE: THE CAUSAL CHAIN

  Human activity
  (fossil fuels, land use, industry)
          ↓ CO₂, CH₄, N₂O, HFCs
  Atmospheric concentration
  (CO₂: 280 ppm pre-industrial → 424 ppm 2024)
          ↓ radiative forcing (ΔF = 5.35 × ln(C/C₀))
  Global mean temperature anomaly
          ↓ physical and biological responses
  Impacts (sea level, extremes, ecosystems)

  SCENARIO FRAMEWORK:
    We can't predict future emissions (political/economic choice)
    → Model multiple plausible futures as scenarios
    → Each scenario produces a probability distribution of outcomes
    → Policy analysis compares outcomes across scenarios

  TEMPERATURE TARGETS (Paris Agreement, 2015):
    "Well below 2°C above pre-industrial levels"
    "Pursuing efforts to limit to 1.5°C"
    Current trajectory: ~2.5-3°C with current policies
    Current pledges (NDCs): ~2.0-2.4°C
    Both insufficient for Paris goals
```

---

## Scenario Framework: RCPs and SSPs

```
  GENERATION 1: REPRESENTATIVE CONCENTRATION PATHWAYS (RCPs)
  Used in CMIP5 / IPCC AR5 (2013)

  ┌─────────────────────────────────────────────────────────────────┐
  │  RCP    │ Forcing by 2100 │ CO₂ equiv. 2100 │ ~Temperature     │
  ├─────────────────────────────────────────────────────────────────┤
  │  RCP 2.6│ 2.6 W/m²       │ ~450 ppm        │ ~1.6°C           │
  │  RCP 4.5│ 4.5 W/m²       │ ~650 ppm        │ ~2.4°C           │
  │  RCP 6.0│ 6.0 W/m²       │ ~850 ppm        │ ~3.0°C           │
  │  RCP 8.5│ 8.5 W/m²       │ ~1370 ppm       │ ~4.3°C           │
  └─────────────────────────────────────────────────────────────────┘

  GENERATION 2: SHARED SOCIOECONOMIC PATHWAYS (SSPs)
  Used in CMIP6 / IPCC AR6 (2021)
  Better: combines socioeconomic narrative WITH emissions level

  ┌───────────────────────────────────────────────────────────────────────┐
  │  SSP     │ Narrative               │ Warming 2100  │ Character        │
  ├───────────────────────────────────────────────────────────────────────┤
  │ SSP1-1.9 │ Sustainability          │ ~1.0°C        │ Aggressive CDR   │
  │ SSP1-2.6 │ Sustainability          │ ~1.8°C        │ Strong mitigation│
  │ SSP2-4.5 │ Middle of the road      │ ~2.7°C        │ Current policies+│
  │ SSP3-7.0 │ Regional rivalry        │ ~3.6°C        │ Fragmentation    │
  │ SSP5-8.5 │ Fossil fuel dev.        │ ~4.4°C        │ High-end fossil  │
  └───────────────────────────────────────────────────────────────────────┘

  SSP NARRATIVES MATTER:
    SSP1: global cooperation, low inequality, circular economy
    SSP3: nationalism, fragmentation, limited climate cooperation
    Same forcing level can arise from very different socioeconomic paths
    The narrative drives which sectors decarbonize and when

  RCP 8.5 / SSP5-8.5 DEBATE:
    Originally framed as "business as usual"
    Updated analysis: coal expansion required makes this
    increasingly unlikely as a central scenario
    Still useful as "high end tail" for risk analysis
    Not necessarily the baseline trajectory
```

---

## Carbon Budget Mathematics

```
  CARBON BUDGET = cumulative CO₂ emissions consistent with
                  staying below a temperature threshold

  WHY CUMULATIVE? Temperature correlates with TOTAL CO₂
  emitted since pre-industrial, not annual rate
  (TCRE: Transient Climate Response to cumulative Emissions
   ≈ 0.45°C per 1000 GtCO₂ — IPCC AR6 best estimate)

  REMAINING BUDGET (from Jan 2023, IPCC AR6):
  ┌──────────────────────────────────────────────────────────┐
  │  Target    │ Probability │ Remaining budget (GtCO₂)     │
  ├──────────────────────────────────────────────────────────┤
  │  1.5°C     │ 50%        │ ~380 GtCO₂                   │
  │  1.5°C     │ 67%        │ ~300 GtCO₂                   │
  │  2.0°C     │ 50%        │ ~1230 GtCO₂                  │
  │  2.0°C     │ 67%        │ ~900 GtCO₂                   │
  └──────────────────────────────────────────────────────────┘

  CONTEXT:
    Current annual emissions: ~40 GtCO₂/year
    At current rate: 1.5°C budget (50%) depleted in ~9.5 years
    At current rate: 2.0°C budget (50%) depleted in ~31 years

  BUDGET UNCERTAINTIES (±range is ±220 GtCO₂ for 1.5°C):
    ECS uncertainty (ECS range 2.5-4°C per AR6)
    Non-CO₂ forcing evolution (CH₄, aerosols)
    Earth system feedbacks not fully captured
    Permafrost and methane feedbacks could reduce budget further

  IMPORTANT: The budget is a FLOW, not a STOCK:
    Spending the budget faster doesn't change the eventual
    equilibrium temperature — it changes WHEN we arrive
    High short-term emissions → need deeper later reductions
    or larger carbon removal to stay within budget
```

---

## Sector Contributions to Global Emissions

```
  GLOBAL GHG EMISSIONS BY SECTOR (IPCC AR6, 2019 baseline):

  ┌───────────────────────────────────────────────────────────────┐
  │  ENERGY SYSTEMS (electricity/heat production)   ~34%         │
  │    Coal power plants: ~20%                                    │
  │    Oil and gas: remainder of energy sector                    │
  │    Decarbonization: fastest sector (solar/wind cost collapse) │
  │                                                               │
  │  INDUSTRY                                       ~24%         │
  │    Steel: ~8% (iron ore reduction with coking coal)          │
  │    Cement: ~4% (CaCO₃ → CaO + CO₂ — process emissions)      │
  │    Chemicals, petrochemicals, aluminum                        │
  │    Hard to decarbonize: process emissions, high-temp heat     │
  │                                                               │
  │  AGRICULTURE, FORESTRY, LAND USE (AFOLU)        ~22%         │
  │    Livestock methane (enteric fermentation): ~5%              │
  │    Deforestation: ~12% (land use change flux)                 │
  │    Rice paddies, fertilizer N₂O                               │
  │    Hard: biological processes; food security constraints      │
  │                                                               │
  │  TRANSPORT                                      ~16%         │
  │    Road vehicles: ~12% (BEV transition underway)             │
  │    Aviation: ~2.5% (growing; hard to decarbonize)            │
  │    Shipping: ~1.7% (growing; exploring NH₃/methanol)         │
  │                                                               │
  │  BUILDINGS                                       ~6%         │
  │    Mostly space heating and cooling                           │
  │    + hot water, cooking                                       │
  │    Solution: electrification + clean grid                     │
  └───────────────────────────────────────────────────────────────┘

  THE DECARBONIZATION DIFFICULTY SPECTRUM:

  EASY (technology available, cost competitive):
    Solar PV, wind (already cheapest electricity in most regions)
    Battery electric vehicles (cost parity approaching 2025-2027)
    LED lighting (essentially complete transition)

  MEDIUM (technology available, deployment ramping):
    Grid storage, long-distance transmission
    Heat pumps for space heating
    Building efficiency upgrades

  HARD (deep technical/economic challenges):
    Aviation: energy density requirements; SAF ~3-5× cost
    Shipping: ammonia/methanol; infrastructure challenge
    Steel: hydrogen-DRI replacing coking coal; cost premium
    Cement: process CO₂ from CaCO₃; CCS needed
    Agriculture: methane from ruminants; land conversion limits
```

---

## Net Zero: Definition and Math

```
  "NET ZERO" ≠ "ZERO EMISSIONS"

  NET ZERO = gross emissions balanced by carbon removal
    Residual emissions (from hard-to-decarbonize sectors)
    OFFSET by Carbon Dioxide Removal (CDR)

  ┌───────────────────────────────────────────────────────────────┐
  │  NET ZERO 2050 (example pathway):                            │
  │                                                              │
  │  2050 Gross emissions:  ~5-10 GtCO₂/year residual           │
  │  (from: aviation, shipping, agriculture, some industry)      │
  │  CDR required:          ~5-10 GtCO₂/year removal            │
  │  NET:                   ≈ 0                                  │
  │                                                              │
  │  For 1.5°C: this must be NET NEGATIVE after 2050:           │
  │  CDR > gross emissions (withdrawing past cumulative)         │
  └───────────────────────────────────────────────────────────────┘

  TYPES OF CDR:
    Natural: afforestation, soil carbon, blue carbon
      → Permanence risk (fire, land-use change reverses)
      → Co-benefits: biodiversity, water
      → Limited total capacity (~few GtCO₂/yr)
    BECCS (bioenergy + CCS): grow biomass, burn it, capture CO₂
      → Large land/water requirements
      → Current deployment: minimal
    DAC (Direct Air Capture): chemical/physical CO₂ from air
      → Current cost: $300-1,000/tCO₂
      → Theoretical minimum: ~$50-100/tCO₂
      → Current scale: ~0.01 MtCO₂/year (trivial)
      → Required for 1.5°C: GtCO₂-scale by 2050

  TIMING MATTERS:
    Deep cuts EARLY = less CDR required later
    Delaying cuts = must remove more carbon later
    Each year of current emissions = multi-decadal CDR
    "Net zero by 2070 with overshoot" vs "net zero by 2050"
    are fundamentally different risk profiles

  OVERSHOOT PATHWAYS:
    Most IPCC 1.5°C scenarios involve TEMPORARY overshoot:
    Temperature peaks at ~1.6-1.7°C then pulled back by CDR
    Risk: tipping elements triggered during overshoot period
    may not reverse even if temperature subsequently drops
    (hysteresis — see 03-FEEDBACKS-TIPPING)
```

---

## Carbon Pricing Mechanisms

```
  THE BASIC PROBLEM:
    CO₂ emissions are an externality (cost imposed on others)
    Emitter pays nothing; society bears the cost
    Carbon pricing = internalize the externality

  CARBON TAX:
    Set price per tonne CO₂ ($/tCO₂)
    Let quantity (emissions reduction) be determined by market
    ADVANTAGE: price certainty (predictable investment signal)
    DISADVANTAGE: quantity uncertainty (how much will reduce?)
    Examples:
      Sweden: ~130 USD/tCO₂ (world's highest; ~1991)
      British Columbia: ~65 CAD/tCO₂
      US: no national carbon tax

  CAP AND TRADE (ETS):
    Set total quantity of permitted emissions (the cap)
    Issue tradeable allowances; total = cap
    Emitters must hold allowance for each tonne emitted
    ADVANTAGE: quantity certainty (cap guarantees total)
    DISADVANTAGE: price volatility (economic shocks move price)
    Examples:
      EU ETS: largest system; ~60-100 EUR/tCO₂ (2022-2024)
      California (WCI): linked with Quebec
      RGGI (US Northeast): power sector only
      China ETS: launched 2021; covers power sector;
                  currently at very low prices (~10 USD/tCO₂)

  EU CARBON BORDER ADJUSTMENT MECHANISM (CBAM):
    Imports into EU from countries without carbon pricing
    must purchase CBAM certificates = equivalent EU ETS price
    Covers: steel, cement, aluminum, fertilizers, electricity
    Phase-in: 2023 reporting; financial obligations from 2026
    Rationale: prevent "carbon leakage" (production moving to
    lower-regulation regions)
    First carbon border price in international trade history

  SOCIAL COST OF CARBON (SCC):
    Theoretical: economic cost of emitting 1 tonne CO₂
    US EPA (2023): ~$190/tCO₂ (Biden administration update)
    Range in literature: $50-$1,000+/tCO₂
    (depends heavily on discount rate and tail risk weighting)
    Used for regulatory cost-benefit analysis
    Not the same as market carbon price
```

---

## Country Commitments and the Implementation Gap

```
  PARIS AGREEMENT MECHANISM (2015):
    Nationally Determined Contributions (NDCs):
      Each country submits own climate target + plan
      No binding enforcement mechanism (pledge and review)
      5-year cycles: "ratchet mechanism" → increasing ambition
    Net-zero pledges (distinct from NDCs):
      Long-term targets (2050 or 2060 or 2070)
      Variable legal force and specificity

  CURRENT STATE (as of 2024):
  ┌───────────────────────────────────────────────────────────┐
  │  UN Global Stocktake 2023 finding:                       │
  │  World is NOT on track to meet Paris goals               │
  │  Current NDC implementation → ~2.5°C                     │
  │  Full NDC implementation → ~2.0°C                        │
  │  Net-zero pledges (if met) → ~1.7°C                      │
  │  Gap between pledges and implementation: substantial      │
  └───────────────────────────────────────────────────────────┘

  MAJOR EMITTERS (% of global CO₂, approximate):
    China: ~31%
    United States: ~14%
    European Union: ~7%
    India: ~7%
    Russia: ~5%
    Japan: ~3%
    Top 6: ~67% of global emissions

  JUST TRANSITION:
    Common But Differentiated Responsibilities (CBDR):
      Historical emissions: developed world cumulative share >50%
      Development rights: India/Africa: per capita emissions still low
      Financing: developed nations pledged $100B/year to developing
        (2009 pledge; mostly not met)
    Distributional impacts of decarbonization:
      Coal region employment; energy cost regressive burden
      Just Transition funds (EU: €17.5B; US IRA: targeted provisions)
      Energy poverty: ~750 million without electricity access
```

---

## Decision Cheat Sheet

| Scenario question | Answer |
|---|---|
| Current trajectory without new policy | ~2.5-3°C (UNEP 2023) |
| Current pledges (NDCs) fully implemented | ~2.0-2.4°C |
| Remaining CO₂ budget for 1.5°C (50%) | ~380 GtCO₂ from 2023 |
| Years at current rate for 1.5°C budget | ~9-10 years |
| Fastest sector to decarbonize | Electricity (solar/wind cost collapse) |
| Hardest sector to decarbonize | Aviation, shipping, cement, beef |
| Net zero requires | CDR to offset residual hard-sector emissions |
| Carbon price signal in EU | EU ETS: ~60-100 EUR/tCO₂ (2022-2024) |
| Border carbon adjustment | EU CBAM: steel/cement/aluminum/fertilizer |

---

## Common Confusion Points

**Net zero by 2050 does not mean zero emissions by 2050**: It means gross emissions are balanced by removal. Aviation, some agriculture, and hard-process industries are assumed to still emit in 2050, offset by large-scale CDR. The critical question is whether the CDR technologies (DAC, BECCS) can scale fast enough.

**RCP 8.5 is not "business as usual"**: It originally was modeled that way, but requires massive coal expansion beyond current trajectories. Current coal trends make it a plausible upper tail, not the central baseline. SSP2-4.5 and SSP3-7.0 are more defensible central scenarios for current policy trajectories.

**NDCs ≠ current policy ≠ net-zero pledges**: Three different things with three different temperature outcomes. NDCs are formal pledges; current policy is what's actually implemented; net-zero pledges are long-term aspirations. The gap between all three is significant.

**Carbon budgets deplete continuously**: The 1.5°C budget is consumed by every tonne emitted today. Calculating how many years of budget remain at current rates is simple arithmetic. The practical implication: each year of delay makes the required decarbonization rate steeper.

**Carbon pricing is not the only mechanism**: Carbon taxes and cap-and-trade are theoretically efficient but politically difficult. Regulations, standards (CAFE, building codes, appliance efficiency), public investment, and industrial policy are all tools in the policy mix. Most national decarbonization involves all of these rather than carbon pricing alone.
