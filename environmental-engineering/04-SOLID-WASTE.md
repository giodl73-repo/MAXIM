# Solid Waste Management

## The Big Picture

Solid waste management is a hierarchy: prevention first, disposal last. The engineering
challenge is designing systems that divert material from landfills while remaining
operationally and economically viable.

```
  WASTE MANAGEMENT HIERARCHY
  (preferred → least preferred)

  ┌─────────────────────────────────────────────────────────────┐
  │  1. SOURCE REDUCTION (Prevention)                           │
  │     Design products to use less material / be more durable  │
  │     Extended Producer Responsibility (EPR) — EU standard    │
  ├─────────────────────────────────────────────────────────────┤
  │  2. REUSE                                                   │
  │     Product repair, resale, remanufacturing                 │
  │     Microsoft Circular Centers — refurbish servers          │
  ├─────────────────────────────────────────────────────────────┤
  │  3. RECYCLING                                               │
  │     Material recovery → reprocessed into new products       │
  │     MRF (materials recovery facility)                       │
  ├─────────────────────────────────────────────────────────────┤
  │  4. COMPOSTING / ANAEROBIC DIGESTION                        │
  │     Organic material → compost / biogas                     │
  ├─────────────────────────────────────────────────────────────┤
  │  5. ENERGY RECOVERY                                         │
  │     Waste-to-energy combustion, landfill gas utilization    │
  ├─────────────────────────────────────────────────────────────┤
  │  6. TREATMENT                                               │
  │     Reduce toxicity / volume before disposal                │
  ├─────────────────────────────────────────────────────────────┤
  │  7. DISPOSAL (Landfill)                                     │
  │     Final sink — engineered containment                     │
  └─────────────────────────────────────────────────────────────┘
```

**Regulation**: Municipal solid waste (MSW) is RCRA Subtitle D (non-hazardous solid waste).
Hazardous waste is RCRA Subtitle C. These run under completely different regulatory regimes.

---

## MSW Characterization

```
  U.S. MSW COMPOSITION (EPA, 2018 — 292 million tons/yr, 4.9 lb/capita/day)

  ┌──────────────────────┬─────────┬────────────────────────────────┐
  │ Material             │ % by Wt │ Notes                          │
  ├──────────────────────┼─────────┼────────────────────────────────┤
  │ Food scraps          │  22%    │ Fastest-growing; best          │
  │                      │         │ candidate for AD/composting    │
  ├──────────────────────┼─────────┼────────────────────────────────┤
  │ Paper / cardboard    │  23%    │ Highest recycled fraction      │
  │                      │         │ OCC (old corrugated cardboard) │
  │                      │         │ = high-value recyclable        │
  ├──────────────────────┼─────────┼────────────────────────────────┤
  │ Plastics             │  12%    │ Only ~8% recycled; highly      │
  │                      │         │ variable recyclability by resin │
  ├──────────────────────┼─────────┼────────────────────────────────┤
  │ Yard trimmings       │  12%    │ Largely composted or mulched   │
  ├──────────────────────┼─────────┼────────────────────────────────┤
  │ Metals               │   9%    │ Aluminum: >90% recovery rate   │
  │                      │         │ Steel: ~70% recovery           │
  ├──────────────────────┼─────────┼────────────────────────────────┤
  │ Rubber/leather/tex.  │   8%    │ Largely landfilled             │
  ├──────────────────────┼─────────┼────────────────────────────────┤
  │ Wood                 │   6%    │                                │
  ├──────────────────────┼─────────┼────────────────────────────────┤
  │ Glass                │   4%    │ Heavy, low value, breakage;    │
  │                      │         │ challenging to recycle         │
  ├──────────────────────┼─────────┼────────────────────────────────┤
  │ Other                │   4%    │                                │
  └──────────────────────┴─────────┴────────────────────────────────┘

  Diversion rate (recycling + composting): ~32% in U.S. (well below EU 50–70%)
  Landfill: ~50%; Energy recovery (WTE): ~12%; Combustion (no recovery): ~6%
```

---

## Materials Recovery Facility (MRF)

A MRF sorts commingled recyclables into marketable commodity streams. The sort line is a **multi-stage classification pipeline**: each stage applies a different classifier to the stream using a different feature space — disc screens classify by size, NIR optical sorters classify by spectral signature (reflectance wavelength), eddy current separators classify by electrical conductivity, and AI-enhanced systems (ZenRobotics, AMP Robotics) use computer vision classification on the conveyor stream. This is a physical implementation of a streaming classification architecture with cascaded binary and multi-class classifiers.

```
  MRF SORT LINE (clean MRF — pre-sorted recyclables)

  Tipping floor
      |
      v
  Pre-sort conveyor
  (manual removal of obvious contaminants — plastic bags, tanglers)
      |
      v
  Disc screen (OCC separator)
  (large corrugated cardboard overs → OCC baling line)
      |
      v
  Fiber screen (newspaper / mixed paper)
  (paper overs to fiber baling line)
      |
      v
  Glass breaker (optional — removes glass early)
      |
      v
  Metering drum → conveyors to sorting deck
      |
      +──> Optical sorters (NIR near-infrared)
      |    Identifies plastic resin types:
      |    PET (#1) → HDPE (#2) → PP (#5) sorted separately
      |    Air jets kick materials into chutes
      |
      +──> Eddy current separator
      |    Induced currents in non-ferrous metals → repel aluminum cans
      |    Ferrous metals removed earlier by overhead magnet
      |
      v
  Residuals (everything that doesn't get captured) → landfill

  OPTICAL SORTER DETAIL:
  NIR identifies polymers by characteristic absorption spectra;
  AI-enhanced systems (ZenRobotics, AMP Robotics) add computer vision
  for brand/type identification; significantly improves purity
  Clean MRF: requires <10% contamination in input
  China National Sword (2018): China imposed <0.5% contamination threshold
  → most US MRFs could not meet this → recycling markets collapsed
  Currently recovering: OCC, cardboard, aluminum, steel, #1 PET, #2 HDPE
  Still challenged: #3-#7 plastics, glass, mixed paper
```

---

## Recycling Economics

Not all recycling is economically viable — secondary materials markets determine fate.

```
  COMMODITY VALUE SPECTRUM (approximate, volatile)

  ┌──────────────────┬──────────────┬──────────────────────────────┐
  │ Material         │ Market Value │ Notes                        │
  ├──────────────────┼──────────────┼──────────────────────────────┤
  │ Aluminum         │ $1,500+/ton  │ Infinite recyclability;     │
  │ (UBC cans)       │              │ 95% energy savings vs.       │
  │                  │              │ primary; always profitable   │
  ├──────────────────┼──────────────┼──────────────────────────────┤
  │ OCC cardboard    │ $50–200/ton  │ Volume driver of recycling   │
  │                  │              │ economics; volatile market   │
  ├──────────────────┼──────────────┼──────────────────────────────┤
  │ Steel            │ $100–300/ton │ 70% energy savings; reliable │
  │                  │              │ market via scrap yards       │
  ├──────────────────┼──────────────┼──────────────────────────────┤
  │ HDPE natural     │ $200–600/ton │ High-value plastic           │
  │ (milk jugs)      │              │                              │
  ├──────────────────┼──────────────┼──────────────────────────────┤
  │ PET clear        │ $100–400/ton │ Bottle-to-bottle recycling   │
  │ (soda bottles)   │              │                              │
  ├──────────────────┼──────────────┼──────────────────────────────┤
  │ Mixed paper      │ -$0 to $50/t │ Often negative value;        │
  │                  │              │ China National Sword wrecked │
  │                  │              │ the market                   │
  ├──────────────────┼──────────────┼──────────────────────────────┤
  │ Glass            │ -$20 to $10/t│ Heavy; crushing lowers value;│
  │                  │              │ often landfilled or used as  │
  │                  │              │ daily cover at landfills     │
  ├──────────────────┼──────────────┼──────────────────────────────┤
  │ Plastics #3–#7   │ Negative     │ No viable market in most     │
  │ (mixed/colored)  │              │ regions; goes to landfill    │
  └──────────────────┴──────────────┴──────────────────────────────┘

  MRF economics: revenue from commodity sales vs. processing cost
  (~$50–120/ton processing). When commodity values drop, municipalities
  pay "processing fees" rather than receiving revenue.
```

---

## Composting

Controlled aerobic decomposition of organic material — carbon cycling with intentional
end products.

```
  COMPOSTING PROCESS REQUIREMENTS

  Feedstocks: food scraps, yard trimmings, agricultural residuals,
              cardboard (C source), manure (N source)

  C:N ratio: 25–35:1 optimal for rapid decomposition
    If too high (>40:1): slow decomposition, N deficient
    If too low (<20:1): N volatilization (ammonia odor), anaerobic zones

  Moisture: 40–60% (by weight) — squeezable but not dripping
  Particle size: 0.5–2 inches — balance surface area vs. airflow resistance
  Temperature: 55–65°C during active decomposition → pathogen kill
    PFRP (Process to Further Reduce Pathogens): 55°C for 3 days minimum
    for EPA 503 Class A or equivalent

  COMPOSTING SYSTEMS:
  ┌──────────────────┬───────────────────────────────────────────────┐
  │ System           │ Notes                                         │
  ├──────────────────┼───────────────────────────────────────────────┤
  │ Windrow          │ Long rows turned by machine; low capital;    │
  │                  │ large land area; odor risk                    │
  ├──────────────────┼───────────────────────────────────────────────┤
  │ Aerated static   │ Forced air through static pile; no turning;   │
  │ pile (ASP)       │ faster (~21 days); enclosed with biofilter    │
  │                  │ controls odors                                │
  ├──────────────────┼───────────────────────────────────────────────┤
  │ In-vessel        │ Rotating drum or tunnel; fully enclosed;     │
  │ (drum/tunnel)    │ fastest (7–10 days); highest capital;        │
  │                  │ urban siting viable; no odor issues          │
  └──────────────────┴───────────────────────────────────────────────┘

  AD vs. composting: AD produces biogas + digestate in 15–30 days;
  composting requires 3–8 weeks but is simpler. AD is preferred where
  energy recovery is the priority; composting where land is available
  and product quality (mature compost) is priority.
```

---

## Landfill Engineering (Subtitle D)

Subtitle D sanitary landfill is the engineering design standard for MSW disposal.

```
  LANDFILL CROSS-SECTION

  Final cover system
  ├── Vegetative layer (erosion protection)
  ├── Drainage layer (lateral drainage of infiltration)
  ├── Barrier layer (18" compacted clay + 40-mil geomembrane) — 10⁻⁷ cm/s
  └── Foundation/grading layer

  WASTE MASS
  (compacted daily in cells, 6:1 slope, daily cover = 6" soil or ADC)

  Primary liner system:
  ├── 60-mil HDPE geomembrane (textured for friction on clay)
  ├── 24" compacted clay liner (k ≤ 10⁻⁷ cm/s) — composite liner
  └── Leak detection layer (between primary and secondary liner)

  Secondary liner:
  ├── 60-mil HDPE geomembrane
  └── 24" compacted clay (or equivalent GCL — geosynthetic clay liner)

  Leachate collection and removal system (LCRS):
  ├── Gravel drainage blanket over liner
  ├── Perforated collection pipes (4–6" HDPE, 50–100 ft spacing)
  ├── Sumps with pumps at low points
  └── Collected leachate → on-site pretreatment or WWTP
```

### Leachate Management

```
  LEACHATE COMPOSITION (typical)

  BOD₅: 2,000–30,000 mg/L (young landfill, acetogenic phase)
         10–500 mg/L     (mature landfill, methanogenic phase)
  COD:   5,000–80,000 mg/L
  NH₃-N: 500–2,000 mg/L (often the binding constraint for treatment)
  Heavy metals: variable — Pb, Cd, Hg, As
  PFAS: increasingly detected — leachate from consumer product disposal

  LEACHATE TREATMENT OPTIONS:
  ├── Discharge to POTW (common — simplest, but PFAS concern)
  ├── On-site biological treatment (MBR + RO common for high-quality)
  └── Leachate recirculation (bioreactor landfill — accelerates degradation)
```

### Landfill Gas

```
  LFG GENERATION

  Anaerobic decomposition of organic waste produces:
  ~50% CH₄ / ~50% CO₂ (plus trace H₂S, NMOC)

  LFG generation rate (modified EPA First Order Decay model):
  Q_CH4 = k · L₀ · M · e^(-k·t)
    k   = waste decay rate (yr⁻¹) — higher for wetter/warmer climates
    L₀  = methane generation potential (~100 m³/Mg waste)
    M   = mass of waste in year of disposal
    t   = time since waste disposal

  LFG COLLECTION SYSTEM:
  ├── Vertical extraction wells: perforated pipes drilled into waste mass,
  │   spaced 50–300 ft, connected to header pipes under vacuum
  ├── Horizontal trenches: for active phases (top-slope installed)
  └── Wellfield with blower/flare station; vacuum ≈1–5" H₂O

  LFG UTILIZATION:
  ┌──────────────┬─────────────────────────────────────────────────┐
  │ Use          │ Notes                                           │
  ├──────────────┼─────────────────────────────────────────────────┤
  │ Flare        │ Baseline; destroys CH₄ (21× GWP) → CO₂;      │
  │              │ EPA NSPS requires flare or energy recovery      │
  │              │ for ≥34 Mg/hr NMOC emission rate               │
  ├──────────────┼─────────────────────────────────────────────────┤
  │ Direct power │ Engine-generator sets at landfill;              │
  │ generation   │ 30–35% electrical efficiency; can supply grid   │
  ├──────────────┼─────────────────────────────────────────────────┤
  │ RNG          │ Clean, upgrade to pipeline-quality CH₄;        │
  │              │ highest revenue; qualifies for D3 RIN credits  │
  │              │ (Renewable Fuel Standard)                       │
  ├──────────────┼─────────────────────────────────────────────────┤
  │ Direct use   │ Industrial boiler, kiln, greenhouse heating     │
  └──────────────┴─────────────────────────────────────────────────┘

  LMOP: EPA Landfill Methane Outreach Program — technical assistance
  for LFG energy projects; database of all US LFGTE projects
```

---

## Hazardous Waste Management (RCRA Subtitle C)

Hazardous waste requires a completely different cradle-to-grave management system.

```
  WHAT MAKES A WASTE "HAZARDOUS" UNDER RCRA?

  ┌──────────────────────────────────────────────────────────────────┐
  │  LISTED WASTES (EPA has pre-determined these are hazardous):     │
  │  F-list: non-specific source wastes (e.g., spent chlorinated     │
  │           solvents — F001-F005)                                  │
  │  K-list: specific industry source wastes (e.g., K001 wood        │
  │           preserving, K051 API separator sludge)                 │
  │  P-list: acutely hazardous commercial chemical products          │
  │  U-list: toxic commercial chemical products                      │
  ├──────────────────────────────────────────────────────────────────┤
  │  CHARACTERISTIC WASTES (any waste exhibiting these properties): │
  │  D001: Ignitability — flash point <60°C                         │
  │  D002: Corrosivity — pH <2 or >12.5                             │
  │  D003: Reactivity — unstable, water-reactive, cyanide/sulfide   │
  │  D004–D043: Toxicity — TCLP test (Toxicity Characteristic       │
  │             Leaching Procedure) for 40 listed contaminants       │
  │             above regulatory threshold concentrations            │
  └──────────────────────────────────────────────────────────────────┘
```

### Generator Categories

```
  GENERATOR CLASSIFICATION (revised 2017)

  ┌────────────┬────────────────┬───────────────────────────────────┐
  │ Category   │ Generation     │ Key Requirements                  │
  ├────────────┼────────────────┼───────────────────────────────────┤
  │ LQG        │ ≥1,000 kg/mo   │ 90-day on-site storage limit;    │
  │ (large     │ (≥2,205 lb/mo) │ full waste characterization;      │
  │ quantity)  │                │ personnel training; contingency   │
  │            │                │ plan; RCRA Subpart BB leak detec. │
  ├────────────┼────────────────┼───────────────────────────────────┤
  │ SQG        │ 100–1,000 kg/mo│ 270-day on-site storage limit;    │
  │ (small     │                │ basic contingency plan; training  │
  │ quantity)  │                │                                   │
  ├────────────┼────────────────┼───────────────────────────────────┤
  │ VSQG       │ <100 kg/mo     │ No time limit on storage;         │
  │ (very      │                │ must send waste to permitted TSD  │
  │ small qty) │                │ or reclaim; minimal paperwork     │
  └────────────┴────────────────┴───────────────────────────────────┘
```

### Cradle-to-Grave Manifest System

```
  HAZARDOUS WASTE MANIFEST FLOW

  Generator (LQG/SQG)
      |
      | Completes Uniform Hazardous Waste Manifest
      | (identifies waste, generator, transporter, TSDF)
      v
  Licensed Transporter
      |
      | Transports under DOT placarding requirements
      | (49 CFR — hazmat placards on vehicle)
      v
  Treatment, Storage, or Disposal Facility (TSDF)
      |
      | Receives waste; signs manifest; returns copy to generator
      | Treats: incineration, neutralization, solidification
      | Stores: tank, container, containment building
      | Disposes: hazardous waste landfill (Subtitle C cell)
      v
  RCRA Annual Report and Biennial Report to EPA
```

### Land Disposal Restrictions (LDRs)

```
  LDRs require treatment to "best demonstrated available technology"
  (BDAT) levels before land disposal.
  Prohibition: certain hazardous wastes cannot be landfilled without
  treatment. Examples:
  ├── Dilution is not treatment (you cannot add water to reduce concentration)
  ├── Spent solvents: incineration + metals treatment
  └── Wastewater with metals: precipitation/filtration before disposal

  COMMON TREATMENT TECHNOLOGIES (Subtitle C):
  ├── High-temperature incineration: 850–1200°C; destroys organics;
  │   >99.99% DRE for listed hazardous organic compounds
  ├── Chemical neutralization: acid/base wastes
  ├── Precipitation: metals as hydroxides or sulfides
  ├── Stabilization/solidification: cement or pozzolan immobilizes metals
  └── Bioremediation: for contaminated soils (see 05-REMEDIATION.md)
```

---

## E-Waste

Electronic waste is the fastest-growing waste stream globally.

```
  E-WASTE SCALE (2022)

  Global generation: 53 million metric tons/year → growing 2 Mt/yr
  Formal recycling rate: ~17% globally
  Informal sector risk: acid leaching, open burning → heavy metal exposure

  VALUABLE MATERIALS IN E-WASTE:
  ├── Gold (200–400 ppm in circuit boards vs. 5 ppm in gold ore)
  ├── Silver, palladium, copper, aluminum
  └── Rare earth elements in magnets (neodymium, dysprosium)

  REGULATORY LANDSCAPE:
  ├── EU WEEE Directive: producer take-back, collection targets
  ├── US: no federal law; 25 states have e-waste laws (usually manufacturer
  │   fee-funded take-back programs — manufacturer responsibility)
  └── Basel Convention: restricts export of hazardous waste (including
      e-waste) from OECD to non-OECD countries; US not a party

  MICROSOFT DATA CENTER CONTEXT:
  ├── Server decommission generates: motherboards, DIMMs, SSDs, HDDs,
  │   power supplies, networking equipment, UPS batteries
  ├── RCRA characterization: spent lithium batteries (D003 reactive
  │   characteristic); some electronics may be P/U listed
  ├── Microsoft Circular Centers: on-campus refurbishment and
  │   reuse/resale of server components (direct reuse pathway)
  └── Data destruction: NIST 800-88 media sanitization for decommissioned
      storage (encryption + overwrite + physical destruction for TS data)
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What makes a waste hazardous? | RCRA listed (F/K/P/U) OR characteristic (TCLP for toxicity, ignitability, corrosivity, reactivity) |
| Generator produces 500 kg/mo hazardous waste — what rules apply? | SQG — 270-day on-site storage limit, basic contingency plan, licensed transporter required |
| Can I mix hazardous and non-hazardous waste to reduce concentration? | No — dilution is not treatment; mixing may make entire volume hazardous (mixture rule) |
| Landfill leachate contains PFAS — discharge to POTW? | Check POTW permit limits and pretreatment requirements; PFAS pass-through is a regulatory concern |
| Recycling program keeps losing money on glass | Glass is near-zero or negative value; consider glass-to-aggregate pathway or market as beneficiation rather than recycling |
| Closed landfill site — what's the liability? | 30-year post-closure monitoring and maintenance obligation; LFG collection continues; groundwater monitoring wells |
| Server battery disposal — hazardous waste? | Lithium batteries: D003 (reactive) characteristic; must manifest as hazardous unless below VSQG threshold (<100 kg/mo) |
| How do I increase recycling rate? | Single-stream collection increases participation but decreases purity; dual-stream or source separation increases purity |

---

## Common Confusion Points

**RCRA Subtitle C vs. D**: Subtitle D is for non-hazardous solid waste (MSW landfills, industrial solid waste). Subtitle C is for hazardous waste. A Subtitle D landfill cannot legally accept Subtitle C hazardous waste — doing so converts the Subtitle D facility into an unpermitted RCRA Subtitle C TSD, triggering major liability.

**Recycling rate calculation**: EPA's "recycling rate" includes composting. The US rate of ~32% includes yard trimmings composting. The "true" material recycling rate (excluding composting) is ~24%.

**Mixture rule and derived-from rule**: If a listed hazardous waste is mixed with a non-hazardous waste, the entire mixture is listed hazardous. If a hazardous waste is treated and residue results (e.g., incinerator ash), the residue is still listed unless formally delisted by EPA petition. These rules are strict liability traps.

**PFAS in biosolids vs. PFAS in e-waste leachate**: Two different PFAS sources in the solid waste world. Biosolids PFAS comes from industrial PFAS uses entering the sewer system. E-waste/landfill leachate PFAS comes from consumer products (packaging, clothing treatments, non-stick cookware). Both end up in leachate and complicate disposal pathways.

**"Zero waste to landfill" definitions vary**: Microsoft and many companies define "zero waste to landfill" as >90% diversion, not literally 100%. Residuals sent to waste-to-energy (WTE) combustion are often counted as "diverted" even though they are not recycled. Understanding the measurement methodology is critical for sustainability report interpretation.
