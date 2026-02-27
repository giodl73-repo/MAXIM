# Fossil Fuels and the Transition

## The Big Picture

Fossil fuels still supply ~80% of global primary energy and will continue to for decades.
The transition is not a switch — it's a multi-decade replacement of capital stock with
50-year lifetimes. Understanding the transition requires understanding stranded assets,
carbon capture as bridge technology, methane leakage as the sleeper problem, and the
political economy of communities whose economies depend on what must go away.

```
FOSSIL FUEL TRANSITION — SECTOR-BY-SECTOR PHASE-OUT SEQUENCE
══════════════════════════════════════════════════════════════════════

EASE OF          SECTOR                REPLACEMENT            TIMELINE
DISPLACEMENT                          TECHNOLOGY
──────────────────────────────────────────────────────────────────────
Easiest    ┌── Coal power            Wind/solar + storage    2020s–2030s
           │   (already uneconomic    (LCOE crossover done)
           │    vs new renewables)
           │
           ├── Gas peaking           BESS 4-hr + demand      2025–2035
           │   (load-following)      response
           │
           ├── Light road transport  EVs (BEV, battery cost  2025–2040
           │   (passenger cars)      at parity now)
           │
           ├── Gas baseload power    Nuclear + long-duration  2030–2045
           │   (firm capacity role)  storage + VRE overbuild
           │
           ├── Industrial heat       Green H₂, electric arc,  2030–2050
           │   (steel, cement,       heat pumps (>150°C hard)
           │    chemicals)
           │
           ├── Heavy road freight    BEV trucks + H₂ FCEV    2035–2050
           │   (long-haul trucking)  (range-dependent)
           │
Hardest    └── Aviation + shipping   SAF, e-fuels, ammonia,   2040–2060+
               (energy density       green methanol
                constraints)          (no battery solution)
══════════════════════════════════════════════════════════════════════
```

```
FOSSIL FUEL ROLE IN GLOBAL ENERGY (2023)

  PRIMARY ENERGY:
  Coal:    ~26%  (~156 EJ/yr)
  Oil:     ~31%  (~186 EJ/yr)   ← almost all transport
  Gas:     ~23%  (~138 EJ/yr)
  Total FF:~80%  (~480 EJ/yr)

  ELECTRICITY GENERATION:
  Coal:    ~36% of global electricity (~10,800 TWh)
  Gas:     ~23% of global electricity (~7,000 TWh)
  Oil:     ~3%  (small islands, remote)
  Total FF:~62% of global electricity

  CO₂ EMISSIONS:
  Energy sector: ~37 GtCO₂/yr
  Coal power:    ~9.5 GtCO₂/yr (single largest source)
  Oil products:  ~11 GtCO₂/yr (mostly transport)
  Gas:           ~7.5 GtCO₂/yr
  Industrial:    ~9 GtCO₂/yr (cement, steel, chemicals)

  PACE OF TRANSITION:
  Coal share of electricity: 40% (2015) → 36% (2023) → target ~7% (IEA NZE 2030)
  The 2030 coal target requires retiring ~2,000 GW in 7 years.
  Current retirement pace: ~50 GW/yr in OECD; ~0 net in China (still adding)
```

---

## Energy System Inertia — Why Transition is Slow

```
  CAPITAL STOCK TURNOVER RATES:

  Asset Type          Typical Lifetime   Implication
  ──────────────────  ─────────────────  ──────────────────────────────
  Coal power plant    30-50 years        Plants built 1990s run to 2040s
  Natural gas plant   20-40 years        Plants built 2010s run to 2050s
  Oil refinery        40-60 years        Long-lived, capital-intensive
  Industrial furnace  20-40 years        Steel/cement capex amortized
  Buildings (HVAC)    20-30 years        Retrofit requires deliberate policy
  Vehicle fleet       12-15 years        EVs displace ICE gradually
  Aircraft            25-30 years        Aviation decarbonizes slowly

  THE LOCK-IN MATH:
  Every new coal plant built today locks in 30+ years of CO₂ emissions
  Every new gas plant locks in 20+ years
  IEA NZE: "No new fossil fuel development beyond approved projects" (from 2021)
  → This is why IEA says no new coal mines, no new oil/gas fields

  EXISTING FLEET VS POLICY:
  Even closing new investment today, the already-built fleet runs ~2040-2060
  Global coal plant fleet: ~2,200 GW, average age ~13 years (young in Asia)
  Asia coal buildout: China + India + SE Asia added ~500 GW in 2010-2023
  This is the "committed emissions" problem — ~600 GtCO₂ already baked in
  if all current fossil fuel infrastructure runs to end of life
```

---

## Stranded Asset Risk

```
  DEFINITION:
  Stranded asset = asset that loses value before end of physical life
  due to external factors (policy, technology change, market shift)

  IEA UNBURNABLE CARBON:
  ┌───────────────────────────────────────────────────────────────┐
  │  PROVEN global fossil fuel reserves:                           │
  │    Coal:  ~900 GtC equivalent (~3,300 GtCO₂)                 │
  │    Oil:   ~190 GtC equivalent (~700 GtCO₂)                   │
  │    Gas:   ~140 GtC equivalent (~515 GtCO₂)                   │
  │                                                               │
  │  Carbon budget for 1.5°C (2024): ~250 GtCO₂                  │
  │  Carbon budget for 2°C (2024):   ~1,150 GtCO₂                │
  │                                                               │
  │  Conclusion: ~80% of proven reserves are "unburnable"         │
  │  under 1.5°C; ~50% under 2°C                                  │
  └───────────────────────────────────────────────────────────────┘

  FINANCIAL STRANDED ASSET RISK:
  Oil majors' proven reserves on balance sheet: ~$2-4T valuation
  If reserves are "unburnable," book value is impaired
  Transition risk: regulatory carbon price, demand destruction (EVs)
  Physical risk: pipeline/infrastructure in flood zones, permafrost

  WHO IS EXPOSED:
  State-owned oil companies (Saudi Aramco, ADNOC, NIOC): largest reserves
  IOCs (ExxonMobil, Shell, BP): beginning to diversify/reduce capex
  Coal utilities: already experiencing stranded plant economics in US/EU
  Pension funds: embedded fossil fuel exposure (divestment debate)

  COUNTER-ARGUMENT (from oil/gas industry):
  Oil demand for petrochemicals, plastics won't fall with EVs
  LNG is displacing coal in Asia → net CO₂ benefit
  CCS can keep some assets viable
  1.5°C scenarios may not materialize — policy execution is uncertain
```

---

## Carbon Capture and Storage (CCS)

CCS is the technology that could allow some continued fossil use while meeting climate targets,
or remove CO₂ from the atmosphere directly.

Amine scrubbing is a direct application of gas-liquid absorption/stripping (see `chemical-eng/04-SEPARATIONS.md`). The absorber is a packed column gas-liquid contactor; the stripper is a thermal desorber; the MEA regeneration cycle is the classic stripping operation. The 15-25% energy penalty is dominated by reboiler duty for MEA regeneration at 110-120 C — the same thermodynamic constraint governing distillation column energy costs.

### Point-Source Post-Combustion Capture

```
  AMINE SCRUBBING (most deployed technology):

  Flue gas (CO₂ ~10-15% from coal, ~4-8% from gas)
       │
       │  Absorber column: flue gas contacts 30% MEA (monoethanolamine) solution
       │  CO₂ + MEA → carbamate (chemical reaction, exothermic)
       │  Clean gas (N₂, O₂, water vapor) exits
       v
  Rich MEA solution (loaded with CO₂)
       │  Pump to stripper column
       v
  Stripper (110-120°C steam heating)
       │  CO₂ + MEA → CO₂ gas released + lean MEA regenerated
       │  CO₂ stream compressed to ~100 bar for transport/injection
       v
  Lean MEA recycled back to absorber

  CAPTURE RATE: 85-90% of CO₂ from flue gas stream
  ENERGY PENALTY: 15-25% of plant output consumed by capture process
    → A 1,000 MW coal plant needs ~200 MW for CO₂ capture
    → Plant effective output: 800 MW
    → LCOE increases by ~50-70%

  STATUS:
  Sleipner (Norway, North Sea): 1 Mt CO₂/yr since 1996 — world's first CCS
  Boundary Dam (Saskatchewan): 1 Mt/yr from coal plant (operating)
  Quest (Alberta): 1 Mt/yr from oil sands upgrader
  Petra Nova (Texas): coal CCS — suspended 2020 (economics), restarted 2023

  SCALE GAP:
  Current CCS capacity: ~50 Mt CO₂/yr globally
  IEA NZE 2030 target: ~1,600 Mt CO₂/yr
  Scale-up required: 32× in 7 years
  Realistic by 2030? Not if based purely on announced projects.
  45Q tax credit (USA): $85/tonne CO₂ for geologic storage — improving economics
```

### The Allam-Fetvedt Cycle

```
  ALLAM CYCLE — Near-zero emission natural gas, no post-combustion scrubbing:

  ┌──────────────────────────────────────────────────────────────────┐
  │  OXYFUEL COMBUSTION:                                             │
  │  Burn natural gas with PURE OXYGEN (from air separation unit)   │
  │  → Flue gas is almost entirely CO₂ + H₂O (no N₂)              │
  │  → After H₂O condenses: pure CO₂ stream                        │
  │  → No need for amine scrubbing                                  │
  │                                                                  │
  │  WORKING FLUID: supercritical CO₂ (sCO₂) at 300 bar, 1,150°C  │
  │  CO₂ turbine drives generator → very high efficiency (~51-54%) │
  │  Exhaust CO₂ recycled as working fluid (most goes back in)     │
  │  Small fraction: sequestered or sold                            │
  │                                                                  │
  │  NET EMISSIONS: ~0.05 kg CO₂/kWh (vs ~0.43 for standard CCGT) │
  │                                                                  │
  │  DEMO PLANT:                                                     │
  │  NET Power (NET Power LLC, now merged with OXY) — La Porte, TX  │
  │  50 MW thermal demonstration, operated 2018-2022                │
  │  Full-scale plant: 280 MW proposed in Wyoming/TX (EPC stage)   │
  │  Timeline: commercial operation ~2025-2027                      │
  └──────────────────────────────────────────────────────────────────┘
```

### Direct Air Capture (DAC)

```
  DAC — Removing CO₂ directly from the atmosphere (~0.04% concentration):

  HARDER THAN POINT-SOURCE because concentration is 300× lower:
  Coal plant flue gas: ~12% CO₂ → DAC ~0.04% CO₂
  More air must be processed, more energy per tonne captured

  PROCESS (liquid solvent, Climeworks/Carbon Engineering approach):

  STEP 1: CO₂ absorption
  Ambient air + KOH solution → K₂CO₃ + H₂O
  (air contactor — large structure, high airflow)

  STEP 2: Carbonate slurry
  K₂CO₃ + Ca(OH)₂ → CaCO₃ + 2 KOH
  (causticizer — regenerates KOH)

  STEP 3: Calcination
  CaCO₃ → CaO + CO₂  (at ~900°C, requires significant heat)
  (kiln — energy-intensive step)

  STEP 4: CaO hydration
  CaO + H₂O → Ca(OH)₂  (recycles the lime)

  Pure CO₂ stream → compress → geological injection or use

  CURRENT COSTS:
  Climeworks (Orca, Iceland): ~$1,000/tonne CO₂ (2021)
  Climeworks (Mammoth, Iceland, 36 kt/yr): ~$600-800/tonne CO₂ (2024)
  Carbon Engineering/Occidental (DAC1, Texas): target $400-600/tonne
  Learning curve target: $100-150/tonne by 2035, $50-100/tonne eventually
  DOE target (Earthshot): $100/tonne by 2030

  Thermodynamic minimum: ~$20-50/tonne CO₂ (irreversible work to concentrate
  from 400 ppm) — physical lower bound, not achievable practically

  IRA 45Q credit (2022): $180/tonne for DAC with geologic storage
  → Makes current Climeworks economics nearly viable

  SCALE:
  Current global DAC: ~0.01 Mt CO₂/yr
  IEA NZE 2030: 85 Mt/yr needed from DAC → 8,500× scale-up required
  CO₂ removal needed by 2050 (IEA NZE): ~1,900 Mt/yr (DACCS + BECCS)

  KEY PLAYERS:
  Climeworks (Switzerland): Orca (Iceland, 4,000 t/yr), Mammoth (36,000 t/yr)
  Carbon Engineering (Canada, acquired by Occidental/Oxy 2023): 1 Mt/yr DAC1 in TX
  Heirloom (California): accelerated mineral weathering, not thermal process
  Microsoft: purchased 333,000 tonnes of CDR (carbon dioxide removal) from Climeworks (2023)
```

### BECCS (Bioenergy + Carbon Capture and Storage)

```
  BECCS CONCEPT:
  1. Grow biomass (plants absorb CO₂ from atmosphere)
  2. Burn biomass for energy (releases CO₂)
  3. Capture that CO₂ and store it underground
  Net result: NEGATIVE emissions — CO₂ removed from atmosphere

  BECCS IN IPCC SCENARIOS:
  Most AR6 1.5°C scenarios require 1-10 GtCO₂/yr of BECCS by 2050
  This is controversial:

  LAND USE CONTROVERSY:
  ┌────────────────────────────────────────────────────────────────┐
  │  To remove 2 GtCO₂/yr via BECCS requires:                     │
  │  ~250-500 million hectares of energy crops                     │
  │  (compare: total global cropland ~1,400 million hectares)      │
  │  → Competes with food production, biodiversity, water          │
  │                                                                │
  │  BECCS optimists: dedicated energy crops on marginal land     │
  │  BECCS critics:   any food-quality land diversion → famine    │
  │  Reality: BECCS has a physical land limit                      │
  │  "Negative emission technologies are not a license to emit"   │
  │                     — Kevin Anderson, et al.                   │
  └────────────────────────────────────────────────────────────────┘
```

---

## Methane Leakage — The Sleeper Problem

Natural gas is marketed as a "bridge fuel" — cleaner than coal. This is true only if
methane leakage rates are low. Methane is 84× more potent as a greenhouse gas than CO₂
over 20 years (GWP₂₀ = 84). Over 100 years, GWP₁₀₀ = 28.

```
  THE LEAKAGE MATH:

  Natural gas power plant CO₂ intensity: ~0.41 kg CO₂/kWh (CCGT)
  Coal power plant CO₂ intensity:        ~1.00 kg CO₂/kWh

  Gas wins on CO₂ only. But if methane leaks:
  Total warming effect = CO₂ from combustion + (methane leaked × GWP)

  Breakeven leakage rate (gas ≡ coal over 20 years): ~3.2%
  Above 3.2% upstream leakage: gas is WORSE than coal for 20-yr climate impact

  ACTUAL LEAKAGE RATES:
  US average (EPA estimate): ~1.2-1.5% of production
  But: super-emitter events dominate; distribution is highly skewed

  SUPER-EMITTERS:
  Small number of facilities responsible for large fraction of emissions
  ~5% of sites → ~50% of total methane emissions
  Hard to detect with ground monitoring; satellite detection is changing this

  SATELLITE DETECTION:
  GHGSat (Canada): satellite constellation, 25m resolution
  MethaneSAT (Environmental Defense Fund): 1 km resolution, quantitative mass balance
  TROPOMI (ESA Sentinel-5P): global daily coverage, lower resolution
  Permian Basin (Texas/NM): largest studied US super-emitter region
  ~3.5% of Permian Basin production leaks (higher than average)

  POLICY IMPLICATIONS:
  Blue hydrogen credibility: depends on <1% upstream leakage being verifiable
  IRA methane fee: $900-1,500/tonne for excess methane emissions (>0.2% waste)
  EU methane regulation 2024: mandatory monitoring, reporting, verification

  PERMAFROST FEEDBACK:
  ~1,500 GtCO₂-equivalent of CH₄ and CO₂ locked in permafrost
  Arctic warming 2-4× faster than global average
  "Methane bomb" scenario: non-linear feedback if permafrost thaws rapidly
  Current estimates: gradual release (decades) not a "bomb" — but uncertainty large
```

---

## Oil in Transport — Displacement Trajectory

```
  ROAD TRANSPORT (75% of transport energy):

  BEV DISPLACEMENT CURVE:
  2020: BEV 4% of new car sales globally
  2023: BEV 18% of new car sales globally
  IEA NZE 2030: 60% of new car sales must be EV
  2035: EU/UK ban on new ICE car sales (agreed)
  2035: China informal target ~100% NEV new sales
  2050: IEA NZE — essentially no new ICE car sales

  Economic tipping point (BEV TCO < ICE TCO):
  Many markets already reached (especially Norway, China)
  US: ~2025-2027 in most segments (battery cost key driver)
  India: ~2028-2030 (energy is cheaper, vehicles must be cheaper too)

  HARD CASES:
  Long-haul aviation:
  • Jet-A energy density: 43 MJ/kg
  • Best Li-ion: 0.7 MJ/kg (61× worse)
  • Battery flight range feasible: <1,000 km (short-haul, small aircraft)
  • Long-haul (10+ hours): physics requires liquid fuel for decades
  • Solution candidates:
    SAF (sustainable aviation fuel): drop-in, costs 3-5× jet fuel
    H₂ (cryogenic, requires new airframes): Airbus ZEROe ~2035 target
    Synthetic kerosene (Fischer-Tropsch from CO₂ + green H₂)
  • EU ReFuelEU: 2% SAF by 2025, 70% SAF by 2050 (blending mandate)

  Ocean shipping (~10% of transport energy):
  • Bunker fuel (HFO): 40+ MJ/kg
  • Current fleet: ~90,000 vessels, 25-year lifetimes
  • Alternative fuels in play:
    LNG: lower SOx/NOx, ~20% lower CO₂ (but methane slip risk)
    Methanol: lower energy density, MAN B&W engines available now
    NH₃: zero CO₂, toxic, engine development in progress
    H₂: too low volumetric density for most routes
  • IMO 2050: net-zero shipping by 2050 (from 2008 baseline)
  • IMO 2023-2024 milestone: CII (Carbon Intensity Indicator) compliance ratings
```

---

## Just Transition

The human side of fossil fuel phase-out. Energy policy that ignores this creates
backlash that slows or reverses transition (see German coal phase-out politics).

```
  FOSSIL FUEL EMPLOYMENT (US, 2023):
  ┌────────────────────────────────────────────────────────────────┐
  │  Coal mining:              ~42,000 direct jobs                  │
  │  Oil and gas extraction:   ~150,000 direct jobs                 │
  │  Oil/gas pipeline:         ~125,000                             │
  │  Petroleum refining:       ~65,000                              │
  │  Coal power plants:        ~70,000                              │
  │  Total (direct):           ~450,000                             │
  │                                                                 │
  │  Multiplier (indirect/induced): 3-5×                            │
  │  Total employment impact:  ~1.5-2 million                       │
  │                                                                 │
  │  Compare: clean energy (2023):                                  │
  │  Solar: ~270,000; Wind: ~130,000; EV: ~30,000 (growing)        │
  │  Net job trajectory: MORE total jobs in clean energy            │
  │  Problem: jobs are in different places, require different skills │
  └────────────────────────────────────────────────────────────────┘

  CONCENTRATED COMMUNITIES:
  Appalachian coal: WV, KY, VA — economically dependent, limited alternatives
  Powder River Basin (WY): largest US coal producing region
  Gulf Coast oil/gas: Beaumont, Port Arthur TX — refinery hubs
  Ruhr Valley (Germany): coal phase-out complete (2018), 25 years of transition program
  Hunter Valley (Australia): coal export region, transition under political stress

  POLICY TOOLS:
  IRA "Energy Communities": bonus ITC/PTC for clean energy built in retiring fossil areas
  DOE Opportunity Zones: technical assistance for community economic diversification
  EU Just Transition Fund: ~€55B for coal/carbon-intensive regions
  TerraPower Natrium: Kemmerer, WY — deliberate siting at closing coal plant community

  THE TRANSITION TIMELINE MATTERS:
  Rapid closure (years): economic shock, political backlash, inadequate retraining
  Gradual closure (decades): workers can transition naturally through attrition
  Support programs: retraining (takes 2-4 years for skilled trades), infrastructure
  What doesn't work: promises without funding, retraining programs that don't lead to jobs
```

---

## Policy Tools — Carbon Pricing and IRA

### Carbon Pricing

```
  CARBON TAX:
  Simple: $X per tonne CO₂ emitted
  Revenue: goes to government (can be revenue-neutral via rebates)
  Certainty: predictable price → investment signal
  Problem: no quantity certainty (can't guarantee emissions outcome)
  Examples: BC carbon tax ($65 CAD/tonne, 2023), EU carbon border adjustment

  CAP AND TRADE (ETS — Emissions Trading System):
  Government sets a cap on total emissions
  Permits issued (auction or free) = total allowable emissions
  Companies buy/sell permits → market sets price
  Certainty: quantity of emissions guaranteed by cap
  Problem: price volatility (can collapse if recession reduces demand)
  Examples: EU ETS (€60-80/tonne, 2024), California/RGGI

  SOCIAL COST OF CARBON (SCC):
  Biden admin (2022): $51/tonne CO₂ (used for policy cost-benefit analysis)
  Research estimates: $75-200/tonne (accounting for tail risks)
  Market carbon prices: far below SCC in most jurisdictions
  → Carbon is systematically underpriced relative to its true cost
```

### IRA Tax Credits (Key Provisions)

```
  INFLATION REDUCTION ACT (2022) — largest US climate legislation:

  Clean hydrogen production credit (Section 45V):
  $3/kg H₂ for Tier 1 (<0.45 kg CO₂/kg H₂) — essentially green H₂
  $1/kg for Tier 2 (<1.5 kg CO₂/kg H₂)
  $0.60/kg for Tier 3 (<2.5 kg CO₂/kg H₂)
  Duration: 10 years from construction start

  Carbon capture credit (Section 45Q):
  $85/tonne for geological storage (enhanced)
  $60/tonne for EOR (enhanced oil recovery) use
  $180/tonne for direct air capture to geological storage
  $130/tonne for DAC to EOR

  Clean electricity PTC/ITC (Section 45Y / 48E):
  ~$26-28/MWh for wind/solar (PTC) or 30% ITC
  Bonus for: domestic content (+10%), energy communities (+10%)
  Storage: 30% ITC standalone (first time!)

  Methane fee (Section 136):
  $900/tonne for excess methane (>0.2% waste intensity) in 2024
  Rising to $1,500/tonne in 2026+
  Applies to oil/gas production, processing, transmission

  TOTAL ESTIMATED COST: ~$369B over 10 years (Moody's revised upward to ~$800B
  as take-up exceeds projections)
  CLEAN ENERGY INVESTMENT UNLEASHED: ~$3T (BNEF estimate) through 2030
```

---

## Decarbonization Scenarios — Sector by Sector

```
  WHERE DOES FOSSIL USE END AND WHEN:

  COAL (easiest to phase out — only electricity + some industrial):
  Advanced economies: coal power essentially eliminated by 2035 (IEA NZE)
  China: peak coal ~2025-2028; phase-down through 2045
  India: slower; dependent on energy access goals
  Replacement: solar + wind + BESS (cheaper than new coal already)

  GAS (harder — heating, power, industrial):
  Power sector: gas plants → peaker role → declining → CCS or H₂ blending
  Residential heating: heat pumps displace gas boilers (2030-2040 in EU/US)
  Industrial: harder; process heat requires alternatives (green H₂, heat pumps)
  LNG as coal replacement: near-term net benefit in Asia (lower CO₂ than coal)

  OIL (hardest — transport, petrochemicals):
  Passenger vehicles: BEV displacement → oil demand peak ~2025-2030
  Trucking: mix of BEV + H₂ FC → 2030-2045
  Aviation: SAF + H₂ aircraft → 2035-2060 (long tail)
  Shipping: methanol/NH₃ → 2030-2050
  Petrochemicals: not decarbonized (oil used as feedstock, not burned)
    → Could be 30-40% of remaining oil demand in 2050

  NATURAL GAS IN 2050 (IEA NZE):
  Total gas consumption falls ~75% vs 2022
  Remaining use: CCS-equipped plants (firm power), H₂ blending, industrial
  CCS on gas vs green H₂: cost race; H₂ may win in many markets by 2035-2040
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Fossil fuels % of global primary energy? | ~80% (coal 26%, oil 31%, gas 23%) |
| Typical coal plant lifetime? | 30-50 years — assets built in 2010s run to 2040s-2060s |
| What % of proven reserves are "unburnable" at 1.5°C? | ~80% (IEA unburnable carbon thesis) |
| CCS post-combustion efficiency penalty? | 15-25% of plant output consumed by capture |
| Current CCS deployed capacity? | ~50 Mt CO₂/yr globally (IEA NZE 2030 target: 1,600 Mt) |
| DAC cost today? | $600-1,000/tonne CO₂ (target: $100-150 by 2035) |
| Methane GWP (20yr)? | 84× CO₂ — gas leakage >3.2% makes gas worse than coal (20yr) |
| IRA clean H₂ credit (Tier 1)? | $3/kg for <0.45 kg CO₂/kg H₂ |
| IRA DAC credit? | $180/tonne for geological storage |
| Allam cycle: what makes it different? | Oxyfuel combustion in sCO₂; inherently captures CO₂, no amine scrubbing |
| Why aviation is hard to decarbonize? | Jet fuel: 43 MJ/kg; batteries: 0.7 MJ/kg (61× gap) |
| Social cost of carbon (US official)? | $51/tonne CO₂ (Biden admin 2022) — market prices far below this |

---

## Common Confusion Points

**"Natural gas is a clean bridge fuel"**
Only if methane leakage is <1.5-2%. At US average leakage (~1.2-1.5%), gas is
somewhat better than coal. At Permian Basin rates (~3.5%), gas is worse than coal
for near-term warming. The "bridge" argument requires aggressive leak reduction — not guaranteed.

**"CCS can save coal and gas"**
CCS adds 50-70% to the cost of coal power (energy penalty + capex for capture/storage).
At $50-80/MWh CCS-coal vs $30-55/MWh solar, CCS-coal is uncompetitive.
CCS makes more sense for industrial processes (cement, steel) where you can't
substitute electricity directly — not for power generation where alternatives exist.

**"Carbon capture and DAC are the same thing"**
No. Point-source capture (CCS): captures CO₂ from a concentrated source (~10-15%).
DAC: captures directly from ambient air (~0.04%). DAC is 300× more dilute —
requires much more energy and infrastructure per tonne captured. Different economics.
Point-source CCS can be cost-competitive now; DAC needs further learning curve.

**"EVs don't reduce emissions if powered by coal"**
Depends on numbers. Even in the dirtiest US grid (West Virginia, ~900 gCO₂/kWh),
an EV produces ~130 gCO₂/mile vs ~250 gCO₂/mile for an ICE car (EPA average).
EV wins even on coal-heavy grids because of drivetrain efficiency advantage.
And the grid is greening over time — an EV bought today will be cleaner in 10 years.

**"Just transition is a nice-to-have, not essential"**
Political economy evidence says otherwise. Germany's rapid coal phase-out faced massive
political resistance from coal regions. France's yellow vest protests were partly
triggered by fuel tax increases without rural impact mitigation. Australia's 2022
election swung partly on climate/mining job tension. Durable decarbonization
requires winning political consent from communities that lose, not just ones that gain.
