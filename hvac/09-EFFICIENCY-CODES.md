# HVAC Efficiency & Codes

## The Big Picture

HVAC efficiency regulation operates at three levels: federal minimum standards (floor),
voluntary programs (Energy Star, etc.), and building codes (IECC climate zones).
The 2023 DOE test procedure change created widespread confusion — the same equipment
scores ~15% lower under new SEER2/HSPF2 ratings than old SEER/HSPF. Plus the IRA 2022
created significant tax incentives that change the economics of high-efficiency choices.

```
+----------------------------------------------------------------------+
|                    EFFICIENCY REGULATION HIERARCHY                    |
|                                                                      |
|  FEDERAL DOE MINIMUMS (mandatory floor)                              |
|  └── National Appliance Energy Conservation Act (NAECA)              │
|      └── Updated 2023: SEER2/EER2/HSPF2 test procedures             │
|                                                                      |
|  VOLUNTARY ABOVE-CODE PROGRAMS                                       |
|  ├── ENERGY STAR (EPA/DOE co-program)                                │
|  ├── AHRI Certified (equipment rating certification)                 │
|  └── NEEP Cold Climate ASHP Specification                            │
|                                                                      |
|  BUILDING CODES (new construction + replacements)                    |
|  ├── IECC (International Energy Conservation Code)                   │
|  │   ├── Climate zones 1–8                                           │
|  │   ├── Insulation minimums                                         │
|  │   ├── Air sealing requirements                                    │
|  │   └── Mechanical system minimums                                  │
|  └── State amendments (states adopt/modify IECC)                     │
|                                                                      |
|  INCENTIVE PROGRAMS                                                  |
|  ├── IRA 2022 §25C tax credits (residential)                         │
|  ├── IRA 2022 HEERA rebates (income-qualified)                       │
|  └── Utility rebate programs                                         │
+----------------------------------------------------------------------+
```

---

## Section 1: The 2023 DOE Test Procedure Change

The most confusing thing in HVAC ratings right now. Same equipment, different test,
different number. Critical to understand when comparing pre-2023 and post-2023 specs.

```
  WHY THE CHANGE:
  Old SEER test conditions were easy — low external static pressure,
  controlled lab conditions that didn't reflect real installation.
  New SEER2 test uses:
  - Higher external static pressure (0.5" w.c. → 0.1" above old for cooling)
  - Lower outdoor temp for heat pump heating test
  - More realistic of how equipment actually performs

  NUMERICAL IMPACT:
  Old SEER → New SEER2: ~4–7% lower (same equipment)
  Old HSPF → New HSPF2: ~4–11% lower (same equipment)

  Rule of thumb: SEER2 ≈ SEER × 0.95
                 HSPF2 ≈ HSPF × 0.85 (larger adjustment for heating)

  EXAMPLES:
  ┌────────────────────────────────┬────────┬────────┐
  │ Equipment Example              │  SEER  │ SEER2  │
  ├────────────────────────────────┼────────┼────────┤
  │ Standard efficiency AC         │ 14.0   │ 13.4   │
  │ Mid-efficiency AC              │ 16.0   │ 15.2   │
  │ High-efficiency variable speed │ 22.0   │ 21.0   │
  │ Mini-split single zone         │ 25.0   │ 24.0+  │
  └────────────────────────────────┴────────┴────────┘

  NEVER compare old SEER to SEER2 directly.
  "Old equipment was 16 SEER; new is 15.2 SEER2" → new is actually better.
```

---

## Section 2: Federal Minimum Efficiency Standards (2023)

```
  CENTRAL AIR CONDITIONERS:
  ┌─────────────────────────────────────────────────────────────────┐
  │ North (states 1): 13.4 SEER2 minimum                           │
  │ South/Southwest (states 2): 14.3 SEER2 minimum                 │
  │ (Different because AC runs more in hot climates → bigger impact) │
  └─────────────────────────────────────────────────────────────────┘

  HEAT PUMPS (ASHP):
  ┌─────────────────────────────────────────────────────────────────┐
  │ National: 14.3 SEER2, 7.5 HSPF2 minimum                       │
  └─────────────────────────────────────────────────────────────────┘

  GAS FURNACES:
  ┌─────────────────────────────────────────────────────────────────┐
  │ National: 80% AFUE minimum                                      │
  │ (2023 DOE attempt at 92% AFUE national minimum was blocked      │
  │ by court challenge from furnace industry and northern states)    │
  │ Some northern utilities require 95% for rebates                 │
  └─────────────────────────────────────────────────────────────────┘

  OIL FURNACES: 80% AFUE
  GAS BOILERS: 82% AFUE (hot water), 82% AFUE (steam)
  HEAT PUMP WATER HEATERS: Separately regulated; UEF (Uniform Energy Factor)

  INVENTORY RULE:
  Equipment manufactured before 2023 with old SEER ratings can still be
  installed after Jan 1, 2023 from existing inventory. This created a
  stockpile rush in late 2022 and inventory irregularities into 2024.
```

---

## Section 3: Energy Star Thresholds

Energy Star is voluntary — significantly above federal minimums:

```
  ENERGY STAR THRESHOLDS (current):
  ┌─────────────────────────────────────────────────────────────────┐
  │ CENTRAL AC:                                                     │
  │ Split: ≥ 16.0 SEER2 (variable speed)                           │
  │        ≥ 15.2 SEER2 (two-stage)                                │
  │                                                                 │
  │ HEAT PUMPS:                                                     │
  │ ≥ 15.2 SEER2 (cooling) AND ≥ 8.1 HSPF2 (heating)              │
  │                                                                 │
  │ GAS FURNACES:                                                   │
  │ ≥ 95% AFUE                                                     │
  │                                                                 │
  │ BOILERS:                                                        │
  │ ≥ 90% AFUE (oil), ≥ 90% AFUE (gas)                            │
  │                                                                 │
  │ HEAT PUMP WATER HEATERS:                                        │
  │ ≥ 2.0 UEF (Energy Factor); best are 3.5+ UEF                   │
  └─────────────────────────────────────────────────────────────────┘

  WHY ENERGY STAR MATTERS:
  - Required for most IRA §25C tax credits
  - Required for many utility rebate programs
  - Signals commitment to above-code performance
  - Not all Energy Star equipment is the same — SEER2 16 barely qualifies;
    SEER2 26 greatly exceeds it
```

---

## Section 4: IRA 2022 Tax Credits (§25C)

The Inflation Reduction Act created the most significant residential HVAC
incentives in decades. Effective for equipment installed Jan 1, 2023 – Dec 31, 2032.

```
  §25C ENERGY EFFICIENT HOME IMPROVEMENT CREDIT:
  30% of cost up to per-category annual caps

  ┌────────────────────────────────────┬────────────────────────────┐
  │ Category                           │ Annual Credit Cap          │
  ├────────────────────────────────────┼────────────────────────────┤
  │ Heat pump (ASHP) — Energy Star     │ $2,000/year                │
  │ Heat pump water heater — Energy Star│ $2,000/year (shared cap)  │
  │                                    │ ($2,000 total for both)    │
  ├────────────────────────────────────┼────────────────────────────┤
  │ Central AC — highest efficiency    │ $600/year                  │
  │ Gas furnace — 95% AFUE            │ $600/year (shared with AC) │
  │ Gas boiler — 95% AFUE             │ $600/year (shared)         │
  ├────────────────────────────────────┼────────────────────────────┤
  │ Insulation + air sealing           │ $1,200/year                │
  │ Windows + skylights                │ $600/year                  │
  │ Exterior doors                     │ $500/year                  │
  │ Home energy audit                  │ $150/year                  │
  ├────────────────────────────────────┼────────────────────────────┤
  │ TOTAL ANNUAL CAP                   │ $3,200/year                │
  │ (sum of all categories combined)   │                            │
  └────────────────────────────────────┴────────────────────────────┘

  KEY NUANCES:
  - Non-refundable credit (applies against tax liability; no refund if $0 tax due)
  - Annual cap — can spread improvements across years to maximize benefit
  - GSHP (geothermal heat pump): SEPARATE 30% credit (§25D) — NO annual cap
    (also covers solar, fuel cells, battery storage)
  - Must be primary residence
  - Manufacturer Certificate needed for compliance

  HEERA (High-Efficiency Electric Home Rebate Act):
  - Separate program from §25C; upfront rebates at point of sale
  - Income-qualified: full rebate for ≤80% area median income;
    50% rebate for 80–150% AMI; none above 150% AMI
  - Rolled out through state energy offices starting 2024
  - Heat pump rebate: up to $8,000 for heat pump (+ $4,000 for panel upgrade)
```

---

## Section 5: IECC Climate Zones

The International Energy Conservation Code divides the US into 8 climate zones.
Prescriptive requirements for insulation, windows, air sealing, and mechanical systems
vary by zone.

```
  CLIMATE ZONE MAP:
  ┌─────┬──────────────────────────────────────────────────────────┐
  │ Zone│ Description / Example Cities                             │
  ├─────┼──────────────────────────────────────────────────────────┤
  │  1  │ Very Hot/Humid — Miami, Honolulu                         │
  │  2  │ Hot/Humid — Houston, Tampa, Phoenix (2B = hot/dry)       │
  │  3  │ Warm/Mixed — Atlanta, Dallas, Los Angeles (3B = hot/dry) │
  │  4  │ Mixed — Seattle, DC, Baltimore, Denver (4B = marine)     │
  │  5  │ Cool — Chicago, Minneapolis (southern), Boston           │
  │  6  │ Cold — Minneapolis, Billings, Burlington                 │
  │  7  │ Very Cold — International Falls, Duluth (subarctic US)   │
  │  8  │ Subarctic — Fairbanks, AK                               │
  └─────┴──────────────────────────────────────────────────────────┘

  IECC REQUIREMENTS VARY BY ZONE:
  ┌─────────────────────────┬────────────────────────────────────────┐
  │ Requirement             │ Zone 3 vs Zone 6                       │
  ├─────────────────────────┼────────────────────────────────────────┤
  │ Wall cavity insulation  │ R-13 vs R-13+10ci                      │
  │ Ceiling insulation      │ R-38 vs R-49                           │
  │ Window U-factor         │ 0.35 vs 0.30                           │
  │ Window SHGC             │ 0.25 vs no requirement (want solar gain)│
  │ Air sealing (ACH50)     │ 3.0 vs 3.0 (same)                     │
  │ Duct sealing            │ ≤4 CFM25/100 sqft (all zones)         │
  └─────────────────────────┴────────────────────────────────────────┘

  STATE ADOPTION:
  States adopt IECC on their own schedule; amendments are common
  Many states still on 2015 or 2018 IECC (current is 2021)
  California: Title 24 (more stringent than IECC in many areas)
  Florida: Florida Building Code (IECC basis + amendments)
  Local jurisdiction further amends state code
```

---

## Section 6: Manual J/D/S Triad — The Design Standards

```
  ACCA MANUAL TRIAD:
  ┌─────────────────────────────────────────────────────────────────┐
  │                                                                 │
  │  MANUAL J (Load Calculation)                                    │
  │  "How much heating/cooling does this building need?"            │
  │  → Room-by-room sensible and latent BTU/hr loads               │
  │  → Design day outdoor conditions                                │
  │  → Output: required equipment capacity range                    │
  │                                                                 │
  │           ↓                                                     │
  │                                                                 │
  │  MANUAL S (Equipment Selection)                                 │
  │  "What specific equipment matches the Manual J loads?"          │
  │  → Select equipment at AHRI-certified conditions                │
  │  → Overcapacity limits: typically no more than 15% for AC,     │
  │    40% for heating (allows some oversizing for design day)      │
  │  → Matches equipment SHR to building SHR                       │
  │                                                                 │
  │           ↓                                                     │
  │                                                                 │
  │  MANUAL D (Duct Design)                                         │
  │  "How do we distribute that heating/cooling to each room?"      │
  │  → Duct sizes based on Manual J room-by-room airflow needs     │
  │  → Friction rate calculation from available static pressure     │
  │  → Supply and return sizing; register/grille sizing             │
  │                                                                 │
  └─────────────────────────────────────────────────────────────────┘

  REALITY CHECK:
  - New construction: increasingly required by IECC; most contractors do it
  - Replacement equipment: rarely performed (rule of thumb prevails)
  - Result: most replacement equipment in US is oversized by 30–100%
  - Most replacement ductwork is never evaluated
  - Most occupants never know because they compare to worse old equipment

  CODES REQUIRING MANUAL J:
  IECC 2018+ requires Manual J for new construction in adopting states
  Some AHJs (local building departments) require for replacements
  Energy Star Certified Homes program requires all three
  Energy Star HVAC Design Credit requires Manual J + S + D
```

---

<!-- @editor[content/P2]: Datacenter-specific HVAC efficiency standards are entirely absent from this file. For this learner who manages Azure datacenters, the relevant standards are: ASHRAE TC 9.9 (Mission Critical Facilities, Data Centers, Web Hosting Facilities, and Telecommunications Facilities — defines allowable temperature/humidity envelopes for IT equipment, A1–A4 classes); ENERGY STAR for Data Centers (certifies facilities, not equipment); The Green Grid's PUE (Power Usage Effectiveness) metric — now ISO/IEC 30134-2 — as the dominant datacenter efficiency benchmark. Best-in-class hyperscale PUE: 1.1–1.2 (Microsoft, Google). US average datacenter PUE: ~1.5. AFUE, SEER2, and residential minimums are irrelevant to this learner's professional context; PUE and ASHRAE TC 9.9 are directly relevant. At minimum, a section connecting the residential/commercial efficiency framework to the datacenter domain would complete the coverage. -->
## Decision Cheat Sheet

| Question | Answer |
|---|---|
| Old SEER 16 vs new SEER2 15 — which is better? | SEER2 15 (same equipment, harder test — equivalent performance) |
| Minimum SEER2 for federal compliance (North) | 13.4 SEER2 central AC |
| Minimum SEER2 for Energy Star qualification | 16.0 SEER2 (variable speed) |
| Best IRA credit for heat pump? | §25C: $2,000 (ASHP) or §25D: 30% no cap (GSHP) |
| Heat pump water heater IRA credit? | $300 §25C; or $1,750 HEARA rebate (income-qualified) |
| What IECC zone am I in? | Check IECC map; determines insulation minimums |
| New construction HVAC code compliance tool? | Manual J + Energy Star Certified Homes program |
| Should I do Manual J for replacement? | Yes if available; prevents oversized equipment chronic problems |

---

## Common Confusion Points

**SEER2 vs SEER is not a product downgrade**: the equipment didn't get less efficient.
The test got harder. Marketing material confuses this. When you see "14 SEER2" equipment,
it's roughly equivalent to old "15 SEER" equipment at real-world conditions.

**Annual cap means annual — not lifetime**: the $2,000 heat pump credit resets each
year through 2032. If you replace a heat pump this year and your spouse's business
building needs one next year — that's two credits. You can't double up in one year,
but planning improvements across years is legal and maximizes benefit.

**§25C vs §25D**: §25C is the standard home improvement credit with annual caps ($3,200
max). §25D is the clean energy credit — covers GSHP, solar, battery storage with 30%
NO annual cap. Much more valuable for geothermal installations.

**AFUE 92% national minimum blocked**: the 2023 DOE rule would have required condensing
furnaces nationally (92% AFUE = condensing). A court blocked it because the DOE didn't
properly analyze costs to Northern states. The 80% AFUE federal minimum remains. However,
some states (California, Massachusetts) have adopted stricter state requirements.

**AHRI matching matters for rated efficiency**: SEER2 ratings are tested on matched
indoor/outdoor equipment pairs (AHRI-certified system ratings). Mixing a competitor's
indoor coil with your outdoor unit may not achieve the published system SEER2. Always
verify the indoor/outdoor combination exists in AHRI's directory for the rated efficiency.
