# Nuclear Energy Systems

## The Big Picture

Nuclear is the only large-scale technology that provides firm, zero-carbon, high-capacity-factor
electricity. It does not depend on weather. A single 1 GW nuclear plant generates more
electricity in a year (~7.9 TWh) than ~4-5 GW of solar. The engineering is solved; the
economics are broken. Understanding why requires separating the physics from the finance,
and the existing fleet from new construction.

Note: Nuclear physics (fission reaction, neutron cross-sections, reactor criticality,
radioactive decay chains) is covered in `nuclear/`. This guide covers engineering,
economics, plant designs, and the role in decarbonization.

```
NUCLEAR POWER ECONOMICS SPECTRUM

  Existing fleet          New builds (Gen III+)    Gen IV / SMR       Fusion
  (already built)         (AP1000, EPR)             (future)           (research)
  ─────────────────────── ─────────────────────── ─────────────────── ─────────
  Very low LCOE           Very high LCOE           Unknown             Not commercially
  $25-40/MWh             $100-200/MWh             (first-of-a-kind)   available yet
  (marginal cost)        (all-in, capital-heavy)
  CF: 90-95%              CF: 90-95% (when built)   CF: 90-95%          —
  Paid off               Financing = 60-70% cost    SMR thesis: factory  —
  Safe to operate        Long construction (10-15yr) standardization      —
  Retirement risk         Overrun risk               reduces cost         —
  (political)

  KEY INSIGHT: The existing US nuclear fleet (93 reactors, ~95 GW)
  is economically valuable clean energy that must not be prematurely retired.
  New nuclear construction in the West has an unsolved economics problem.
```

---

## Nuclear Plant Economics — Deep Dive

### Why Capital Cost Dominates

```
  NUCLEAR LCOE BREAKDOWN (new build, Gen III+):

  ┌────────────────────────────────────────────────────────────────┐
  │  OVERNIGHT CAPITAL COST (OCC):   ~$6,000-10,000/kW installed  │
  │  "What it would cost if built overnight (no financing)"        │
  │  US: ~$8,000-10,000/kW (AP1000 Vogtle: ~$9,000/kW)          │
  │  South Korea (KEPCO APR-1400): ~$2,500-4,000/kW (export)     │
  │  China (CPR-1000, Hualong): ~$2,000-3,000/kW                 │
  │                                                                │
  │  FINANCING COST (Interest During Construction — IDC):          │
  │  10-year construction × 8% WACC = enormous IDC                │
  │  IDC adds ~30-60% to overnight cost                           │
  │  Final "all-in" cost: $10,000-18,000/kW                      │
  │                                                                │
  │  ANNUAL FIXED O&M:               ~$150-200/kW-yr             │
  │  Fuel cycle (enrichment + fab):  ~$10-15/MWh                 │
  │  Decommissioning fund:           ~$1-2/MWh (set aside now)   │
  │                                                                │
  │  LCOE (new build, US, 2024):     ~$100-200/MWh               │
  │  Vogtle Units 3&4 all-in est:    ~$180/MWh                   │
  │                                                                │
  │  COMPARISON:                                                   │
  │  LCOE existing US nuclear:        ~$25-40/MWh (capital paid)  │
  │  LCOE new utility solar:          ~$30-55/MWh                 │
  │  LCOE new onshore wind:           ~$25-50/MWh                 │
  └────────────────────────────────────────────────────────────────┘

  The economics problem: nuclear's LCOE is ~3-5× wind/solar in the US.
  The reliability argument: nuclear provides capacity value that solar/wind can't fully match.
  The capacity value + LCOE comparison is the real debate.
```

### The Learning Curve Problem — Why Nuclear Costs Went Up

```
  SOLAR LEARNING CURVE:    Every doubling of capacity → ~20% cost reduction
  NUCLEAR "LEARNING CURVE": Costs INCREASED with more construction

  WHY NUCLEAR COSTS WENT UP:
  ┌────────────────────────────────────────────────────────────────┐
  │  1970s-1980s:                                                  │
  │  • Three Mile Island (1979) → regulatory ratchet               │
  │  • Chernobyl (1986) → safety requirement retrofit mid-build    │
  │  • Regulatory changes mid-construction = costly retrofits      │
  │                                                                │
  │  1990s-2000s (hiatus):                                        │
  │  • No new builds in US for ~30 years                          │
  │  • Workforce and supply chain atrophied                       │
  │  • Engineering knowledge partially lost                        │
  │                                                                │
  │  2010s (nuclear renaissance, failed):                         │
  │  • First-of-a-kind (FOAK) projects with new designs           │
  │  • Regulatory uncertainty, contractor inexperience            │
  │  • Westinghouse AP1000 at Vogtle: $14B → $35B+ (budget)     │
  │  • VC Summer (SC): cancelled after $9B spent                 │
  │  • Westinghouse bankrupt 2017 (Toshiba took $10B loss)       │
  │                                                                │
  │  CONTRAST WITH FRANCE (1970s-1990s):                         │
  │  58 reactors, standardized N4 design, rapid sequential build │
  │  Cost: ~$1,500-2,500/kW (1990s dollars)                      │
  │  Key: series production of identical units                    │
  │  Korea/China: same strategy, achieving low costs today        │
  └────────────────────────────────────────────────────────────────┘
```

---

## Generation III+ Reactors

Currently operating or under construction globally.

### AP1000 (Westinghouse)

```
  AP1000 DESIGN PRINCIPLES:

  Passive safety: gravity + natural convection, no pumps/diesel required
  ┌────────────────────────────────────────────────────────────────┐
  │  Emergency Core Cooling:                                       │
  │  • Water tanks above reactor (gravity drain on actuation)     │
  │  • Core Makeup Tanks: pressurized N₂ injection               │
  │  • No AC power required for 72 hours                         │
  │                                                               │
  │  Passive Residual Heat Removal:                               │
  │  • Steam condenses on steel containment wall                  │
  │  • Wall cooled by water flowing down exterior                 │
  │  • Air convection removes heat from cooling water             │
  │  • Works indefinitely without operator action                 │
  └────────────────────────────────────────────────────────────────┘

  Rating: 1,117 MWe (net)
  Design life: 60 years
  Refueling: 24-month cycle (vs 18-month typical)
  Modular construction: many components factory-fabricated

  US DEPLOYMENT — Vogtle Units 3 & 4 (Georgia):
  First US nuclear build in 40 years
  First AP1000s in US
  Unit 3: online July 2023
  Unit 4: online March 2024
  Cost: ~$35B total for 2 units (~$9,000/kW)
  Schedule: 7 years behind original schedule
  Lesson: FOAK + regulatory + contractor issues compound; N-th-of-a-kind will be cheaper
```

### EPR (EDF / Framatome)

```
  EPR — European Pressurized Reactor:
  Rating: 1,650 MWe (largest commercial reactor)
  Safety: 4× redundant safety trains, "core catcher" for severe accident
  Fuel: 4.5% enriched UO₂; mixed oxide (MOX) capable

  STATUS — troubled construction history:
  Olkiluoto 3 (Finland): started 2005, online 2023 (17 years, budget 3×)
  Flamanville 3 (France): started 2007, online 2024 (~17 years, budget 4×)
  Hinkley Point C (UK): 2× EPR, started 2017, completion ~2031+ at $39B
  Taishan 1&2 (China): started 2009, online 2018/2019 — much faster (Chinese execution)

  EPR lesson: complex design, construction execution was inadequate in Finland/France.
  Same design built faster/cheaper in China because of workforce and project management.
```

### VVER-1200 (Rosatom)

```
  VVER-1200 (Water-Water Energy Reactor):
  Rating: 1,198 MWe
  Russian design, primarily for export
  Notable: "Core catcher" — molten core spreads into specialized structure below reactor
  Passive safety: ECCS gravity-driven, 72-hour passive cooling

  Geopolitical constraint: post-Ukraine invasion sanctions affect VVER fuel supply
  Countries with VVERs reconsidering dependency (Hungary, Czech Republic, Bulgaria)
  USA/EU sanctions on Rosatom complicate fuel supply chain
```

---

## Generation IV Concepts

Six reactor concepts defined by the Generation IV International Forum (GIF), selected
for potential commercialization by 2030-2040. Status varies widely.

```
  GEN IV REACTOR FAMILIES:

  ┌──────────────────────────────────────────────────────────────────┐
  │  SODIUM FAST REACTOR (SFR) — most advanced                      │
  │  Coolant: liquid sodium (~500°C)                                │
  │  Spectrum: fast neutrons (no moderator)                         │
  │  Fuel breeding: can breed Pu from U-238 (extends fuel supply)   │
  │  Waste: burns long-lived actinides → less radiotoxic waste      │
  │  Safety: sodium fire risk (water reaction) — passive cooling    │
  │  Examples: TerraPower Natrium (US), China CFR-600, Russia BN-800│
  │                                                                  │
  │  MOLTEN SALT REACTOR (MSR) — fuel dissolved in coolant          │
  │  Coolant: fluoride salt (FLiBe or other) at 600-750°C          │
  │  Fuel: dissolved UF₄ or ThF₄ (thorium cycle possible)         │
  │  Online refueling (no shutdown needed for fuel change)          │
  │  Walk-away safe: fuel drains to freeze plug if power lost       │
  │  Examples: Terrestrial Energy IMSR, Kairos KP-FHR, ThorCon     │
  │                                                                  │
  │  HIGH-TEMPERATURE GAS (HTGR) — used for industrial heat        │
  │  Coolant: helium at 700-1,000°C                                 │
  │  Fuel: TRISO particles (fuel encased in ceramic layers)         │
  │  Inherently safe: fuel can't melt (ceramic has ~2,000°C limit)  │
  │  Heat output: can drive steam turbines or direct H₂ production  │
  │  Examples: X-energy Xe-100 (USA), HTR-PM (China — operating)   │
  │                                                                  │
  │  LEAD-COOLED FAST REACTOR (LFR)                                 │
  │  Coolant: liquid lead or Pb-Bi eutectic                         │
  │  Very high neutron economy; natural convection cooling          │
  │  Examples: Russia BREST-OD-300 (under construction)            │
  │                                                                  │
  │  SUPERCRITICAL WATER REACTOR (SCWR)                             │
  │  Coolant: supercritical water (>374°C, >22 MPa)                │
  │  Higher thermal efficiency (~44%); familiar LWR fuel cycle      │
  │  R&D stage; no demonstration projects yet                       │
  │                                                                  │
  │  GAS-COOLED FAST REACTOR (GFR)                                  │
  │  Fast spectrum + helium cooling — early R&D stage              │
  └──────────────────────────────────────────────────────────────────┘
```

### TerraPower Natrium — Case Study

```
  NATRIUM (TerraPower + GE-Hitachi):
  Type: Sodium Fast Reactor + integrated molten salt thermal storage
  Rating: 345 MWe (base) → 500 MWe peak (using storage)
  Coolant: liquid sodium at ~500°C
  Fuel: metallic uranium fuel (U-Zr alloy), developed from EBR-II experience

  UNIQUE FEATURE — Integrated thermal storage:
  Reactor → heats molten salt tanks (during off-peak)
  Salt tank → boosts steam turbine to 500 MWe (during peak demand)
  Result: constant 345 MW reactor output, but dispatchable 345-500 MW to grid
  This addresses the "nuclear can't flex" criticism

  STATUS:
  US site: Kemmerer, Wyoming (retiring coal plant site)
  DOE funding: ~$2B (Advanced Reactor Demonstration Program)
  Timeline: First operations ~2030 (ambitious)
  Workforce: partnering with coal plant workers in Kemmerer (just transition)
  Bill Gates personally involved (TerraPower founded by Gates)
```

---

## Small Modular Reactors (SMRs)

<!-- @editor[bridge/P3]: The SMR factory-learning thesis is exactly the Azure/cloud economics argument applied to nuclear: large bespoke on-premises data centers (Gen III+ like EPR) → standardized commodity units at scale (SMRs). The "FOAK problem" (first-of-a-kind cost penalizes early adopters) is the same as the Azure reserved capacity pricing: the discount only materializes at committed volume, and someone has to pay for the first N units before the learning curve kicks in. Microsoft's hyperscaler experience — paying above-spot for early-generation server hardware to drive learning curve for next-generation — is directly analogous to the DOE ARDP funding model. -->
The economic thesis for SMRs: factory-built, serial-manufactured reactors should achieve
lower costs than unique large projects. Like commercial aviation (Boeing assembly line) vs
custom ships. The thesis is credible but unproven at commercial scale.

```
  SMR DEFINITION:
  Generally < 300 MWe (though definitions vary; some say <1,000 MWe = "modular")
  Factory-fabricated modules → rail/truck shippable → site assembly

  ECONOMIC THESIS:
  Traditional 1 GW nuclear: $8,000-10,000/kW (unique, large, site-built)
  SMR factory 300 MW: $5,000-8,000/kW target (factory learning curve after N units)
  After 100+ units: potentially $3,000-4,000/kW?

  ECONOMIC REALITY — The FOAK problem:
  SMR FOAK (first commercial plant) is expensive
  Series discount only arrives with 10-100 units
  Who will pay FOAK price while waiting for series price?
  Government (DOE ARDP), strategic buyers (utilities, military bases, hyperscalers?)
```

### SMR Designs — Status 2024

```
  NuScale VOYGR (light water SMR):
  Rating: 77 MWe per module (designed for up to 12 modules = 924 MWe)
  First NRC-approved SMR design (Jan 2023)
  Passive safety: modules sit in pool of water (natural convection cooling)
  STATUS: UAMPS (Utah project) CANCELLED Dec 2023 — cost escalation
    Original estimate: $5,000/kW → revised to $9,000+/kW
    Customers withdrew → insufficient subscriptions
  Lesson: FOAK + small module → doesn't automatically beat large Gen III+

  Kairos Power KP-FHR (pebble-bed fluoride salt):
  Type: Fluoride Salt-cooled High-temperature Reactor (FHR)
  Fuel: TRISO pebbles (ceramic, inherently safe) in liquid fluoride salt
  Rating: ~140 MWe
  Operating temp: 650°C (high-efficiency steam cycle)
  STATUS: NRC licensing, Hermes demo (10 MW thermal) construction started 2023
  Google PPA: signed for 500 MW starting 2035 (6-7 × KP-FHR units)
  Interesting: same TRISO fuel as X-energy; different coolant

  TerraPower Natrium (SFR):
  Described above. 345/500 MWe. Most advanced Gen IV in US. 2030 target.

  X-energy Xe-100 (pebble-bed HTGR):
  Rating: 80 MWe per module (up to 4-pack = 320 MWe)
  Fuel: TRISO pebbles in graphite matrix
  Coolant: helium at 750°C
  Online fueling (continuous pebble addition → no refueling outage)
  Applications: process heat (H₂ production, desalination) + electricity
  STATUS: DOE ARDP funding; Dow Chemical industrial site collaboration
  Timeline: First plant ~2030

  Rolls-Royce SMR (UK):
  Rating: 470 MWe (actually a mid-size modular reactor)
  Light water PWR design
  Standardized UK-built factory modules
  UK government backing (Great British Nuclear)
  STATUS: Regulatory review (RAMI phase); no funding commitment yet (2024)

  BWRX-300 (GE-Hitachi):
  Rating: 300 MWe (boiling water reactor, 10th evolution of BWR)
  Natural circulation (no large recirculation pumps)
  STATUS: NRC review; Ontario Power Generation selected for Darlington site
    First deployment: ~2029 (Canada)
```

---

## Waste Management

```
  NUCLEAR WASTE CATEGORIES:

  HIGH-LEVEL WASTE (HLW):
  • Spent nuclear fuel (SNF) from reactor core
  • Currently stored in:
    1. Spent fuel pools (wet storage, first 5-10 years after discharge)
       — must be cooled (decay heat: ~1% of reactor power initially)
    2. Dry cask storage (after cooling — now standard for 10+ year old fuel)
  • Long-term disposal: deep geological repository (DGR)
  • Only operating DGR: WIPP (New Mexico) — accepts transuranic waste only
  • Yucca Mountain (Nevada): fully licensed, $15B spent, politically blocked
  • Finland: ONKALO repository under construction (world's first SNF DGR)
    1,000 ft granite, 100,000+ year containment design lifetime

  INTERMEDIATE-LEVEL WASTE:
  • Reactor components, filters, resins
  • Near-surface disposal possible after decades of decay
  • Less challenging than HLW

  LOW-LEVEL WASTE:
  • Protective clothing, tools, lightly contaminated materials
  • Shallow burial at licensed sites
  • Volume large; radiological risk small

  VOLUME PERSPECTIVE:
  All US nuclear HLW (60 years of operation): ~90,000 tonnes
  Would fit in a Walmart supercenter footprint
  Compare: coal ash from 60 years: hundreds of billions of tonnes
  → Volume is not the problem; political acceptability is
```

---

## Fusion — State of Play

Fusion power (combining light nuclei, typically D-T, releasing energy) has been
"30 years away" for 60 years. Recent events changed the calculus.

```
  FUSION PROGRESS TIMELINE:

  Dec 2022: NIF (National Ignition Facility, California)
  • ICF (inertial confinement fusion) experiment
  • Laser-driven compression of D-T fuel pellet
  • ACHIEVEMENT: fusion energy > laser energy delivered to target
    1.9 MJ in → 3.15 MJ fusion out (ignition: Q_scientific > 1)
  • Note: laser-to-grid efficiency ~0.25%; total system Q << 1
  • But: proof that ignition is achievable — fundamental physics milestone

  ITER (International Thermonuclear Experimental Reactor):
  • 35-nation project in Cadarache, France
  • D-T burning tokamak: 500 MW thermal out, 50 MW heating in → Q = 10
  • First plasma: originally 2025, now ~2026-2027+
  • Full DT operation: ~2035
  • Purpose: prove Q > 10 sustained; NOT a power plant
  • Cost: ~$20B+ (most expensive science project ever)
  • ITER will NOT generate electricity — it's purely a physics experiment

  SPARC (Commonwealth Fusion Systems):
  • MIT spinout (Bob Mumgaard, Dennis Whyte's group)
  • HTS (high-temperature superconducting) magnets: 20 Tesla (vs ITER's 13T)
  • High-field tokamak: can be much smaller for same Q
  • SPARC: D-T plasma, Q>2 goal, ~2025-2027
  • ARC: follow-on power plant design, ~100 MW net electricity, 2030s
  • $2B raised (Commonwealth, Google, Khosla, others)
  • Microsoft connection: CFS received Microsoft investment

  HELION ENERGY (Microsoft PPA):
  • Pulsed FRC (field reversed configuration) — not a tokamak
  • D-He3 and D-D fuel path (avoids tritium supply chain)
  • World's first commercial fusion PPA: Microsoft (signed 2021)
  • Contract: deliver electricity to grid by 2028 (with penalty provisions)
  • 50 MW target; Trenta record: achieved plasma at >100 million °C
  • Status (2024): still in plasma physics phase; 2028 timeline aggressive
  • Honest assessment: if it slips to 2030-2035, it's still transformative

  BROADER FUSION LANDSCAPE (private companies):
  TAE Technologies, Helion, CFS, Zap Energy, First Light Fusion,
  General Fusion, Tokamak Energy — ~$6B+ private investment as of 2024

  THE ENGINEERING GAP:
  ┌────────────────────────────────────────────────────────────────┐
  │  Even after ignition (plasma physics):                         │
  │  • Tritium breeding (T must be bred from Li-6 in blanket)    │
  │  • Neutron activation of structural materials (activation)    │
  │  • Materials survival (14 MeV neutrons damage everything)     │
  │  • Remote handling for activated components                   │
  │  • Heat exchange to steam turbine (~40% thermal efficiency)   │
  │  • Grid-scale economics ($0.05-0.10/kWh competitive target)  │
  │                                                                │
  │  D-T fusion produces:                                          │
  │  80% of energy: fast neutrons (14 MeV) — hard to capture      │
  │  20% of energy: alpha particles (3.5 MeV) — heat the plasma   │
  └────────────────────────────────────────────────────────────────┘
```

---

## Nuclear's Role in Clean Energy Transition

```
  THE RELIABILITY ARGUMENT:
  ┌────────────────────────────────────────────────────────────────┐
  │  Grid need: firm, zero-carbon power for the hours when         │
  │  solar and wind are not available                              │
  │                                                                │
  │  Nuclear matches this: 90%+ CF, weather-independent           │
  │  1 GW nuclear = ~4-5 GW solar + 4-8 hours storage             │
  │  (rough equivalence for annual energy; not identical for       │
  │   hourly reliability)                                          │
  │                                                                │
  │  Without nuclear: 100% renewable requires                      │
  │  • Massive overbuilding (3-5× peak demand)                    │
  │  • Long-duration storage (weeks) — not commercially available │
  │  • Massive transmission (continent-scale)                      │
  │                                                                │
  │  With nuclear: much more tractable grid architecture           │
  └────────────────────────────────────────────────────────────────┘

  IEA NZE 2050: nuclear capacity doubles from 413 GW (2022) to ~812 GW (2050)
  IPCC AR6: most 1.5°C scenarios retain or grow nuclear

  POLITICAL ECONOMY:
  Pro-nuclear: France (75% nuclear electricity), South Korea, UAE, China (55 GW building)
  Anti-nuclear: Germany (all closed 2023), Austria, Denmark, Belgium (reversing)
  Mixed/pragmatic: USA (Vogtle complete, some SMR interest), UK (Hinkley Point C, SMR)
  Japan: restarting fleet post-Fukushima (political challenge, progress slow)

  MICROSOFT CONTEXT:
  Microsoft + TerraPower (Bill Gates) — connection to Natrium
  Microsoft + Helion PPA (fusion, 2028)
  Microsoft + Kairos Google PPA (nuclear)
  Hyperscalers need 24/7 CFE → nuclear is the natural complement to wind/solar
  Data center siting near nuclear plant: direct co-location being explored
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Existing US nuclear LCOE? | $25-40/MWh (capital paid off, marginal fuel cost low) |
| New nuclear LCOE (US, Gen III+)? | $100-200/MWh (capital cost + financing dominate) |
| Nuclear capacity factor? | 90-95% — highest of any generation source |
| Why did nuclear costs go UP? | Lost learning: regulatory ratchet + 30yr hiatus + FOAK |
| AP1000 in US? | Vogtle 3&4, Georgia — online 2023/2024, first in 40 years |
| NuScale SMR status? | CANCELLED (UAMPS 2023) — cost overruns |
| Most advanced US Gen IV? | TerraPower Natrium (SFR + molten salt storage), Kemmerer WY ~2030 |
| Google nuclear PPA? | Kairos Power KP-FHR, 500 MW starting 2035 |
| Microsoft fusion PPA? | Helion Energy, 50 MW by 2028 (ambitious) |
| ITER: will it generate electricity? | No — purely a physics experiment; proves Q>10 |
| NIF ignition: commercial relevance? | Proves physics; enormous engineering gap remains |
| Nuclear waste volume (all US)? | ~90,000 tonnes — fits in one building; political problem, not volume |
| Where does nuclear win vs wind/solar? | Firm capacity, 24/7 CFE, high-density land use, no weather dependence |

---

## Common Confusion Points

**"Nuclear can't be a climate solution because of waste"**
The waste volume is tiny and manageable. Finland is building a working geological repository.
Coal waste (fly ash, bottom ash) is orders of magnitude larger in volume and contains heavy metals.
The nuclear waste objection is political, not engineering. Engineers consider it solvable.

**"SMRs will be cheap because they're small"**
Smallness creates economies of scale problems (smaller means higher $/kW, not lower).
The SMR bet is on factory learning and standardization, not size per se.
NuScale's cancellation shows FOAK SMRs can cost as much as large plants per kW.
The thesis may hold at unit 10, 20, or 100; it almost certainly fails at unit 1.

**"Nuclear is too slow to matter for climate"**
New nuclear builds take 10-15 years. But:
1. Existing nuclear must not be retired (immediate, no construction needed)
2. Gen IV and SMR timeline: ~2030-2035 for first plants; meaningful by 2040
3. The 2050 target gives 25-30 years — nuclear can scale in that window
4. The alternative (100% wind/solar + storage) may have its own deployment limits

**"Fusion will replace fission before 2040"**
Almost certainly not. Even if SPARC achieves Q>2 by 2027 and ARC starts 2033,
first commercial fusion: best case 2035-2040, most likely 2040-2050+.
The engineering from ignition to grid power is enormous. Fusion will complement,
not replace, fission in the 2050 energy mix.

**"Chernobyl and Fukushima prove nuclear is too dangerous"**
Chernobyl: RBMK design with positive void coefficient (physically unstable — banned everywhere except Soviet bloc) + operator errors that violated procedures.
Fukushima: BWR design with all safety systems powered; backup diesel generators failed (tsunami). ~1 direct radiation death. ~2,200 evacuation-stress deaths (suicide, health neglect).
Modern Western designs (AP1000, EPR, Gen IV) have passive safety — no operator action needed.
Deaths per TWh: nuclear ~0.07 (statistical); wind ~0.04; solar ~0.02; coal ~24.6; gas ~2.8.
Nuclear is statistically the safest major energy source.
