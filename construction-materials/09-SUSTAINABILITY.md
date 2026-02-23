# Construction Materials — Sustainability and Embodied Carbon

## The Big Picture: Whole-Life Carbon of Buildings

```
BUILDING CARBON: LIFECYCLE STAGES (EN 15978 / ISO 21931)
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  PRODUCT & CONSTRUCTION STAGES  USE STAGE           END OF LIFE       BEYOND│
│  ┌───────────────────────────┐  ┌────────────────┐  ┌────────────┐  ┌────┐  │
│  │ A1  │ A2  │ A3  │ A4 │ A5│  │B1│B2│B3│B4│B5│B6│  │C1│C2│C3│C4│  │ D  │  │
│  │ Raw │Transp│Manuf│Transp│Constr│  │In│Maint│Repr│Refurb│Oper│  │Dem│Transp│Waste│Disp│  │Net ben│  │
│  │ mat.│ to  │ ure │ to  │-uct.│  │  │aint │air │bish │-ational│  │  │      │prcs │osal│  │efit   │  │
│  └───────────────────────────┘  └────────────────┘  └────────────┘  └────┘  │
│         EMBODIED CARBON                OPERATIONAL       EOL         CIRCULARITY│
│         (A1–A5 = upfront)              CARBON (B6)                           │
│                                                                              │
│  CARBON TYPES:                                                               │
│  Upfront embodied (A1–A5): majority locked-in at practical completion       │
│  Operational (B6): heating, cooling, lighting, hot water — energy in use    │
│  Biogenic: carbon in wood = stored CO₂ from photosynthesis (can be negative)│
│  Process: cement calcination CO₂ = chemical reaction, not fuel combustion  │
│                                                                              │
│  WHY A1–A5 (UPFRONT EMBODIED) IS NOW THE PRIORITY:                          │
│  1. Operational carbon B6: solved or being solved (insulation + heat pumps) │
│  2. Upfront embodied: released on day 1 of occupation; permanent if forest  │
│     does not regrow fast enough                                              │
│  3. Carbon budget: 1.5°C target requires near-zero emissions by 2050       │
│     → new buildings built 2025–2050 contribute embodied in that budget     │
│     → cannot wait for operational savings to offset upfront emissions      │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Operational Carbon: The Solved Problem (Nearly)

### Passivhaus Approach

```
PASSIVHAUS ENERGY BALANCE PRINCIPLE
──────────────────────────────────────────────────────────────────────────────
  STANDARD PASSIVHAUS CRITERIA (PHPP):
    Heating demand:      ≤ 15 kWh/m²/yr
    Cooling demand:      ≤ 15 kWh/m²/yr (or ≤ 10 W/m² peak)
    Primary energy:      ≤ 120 kWh/m²/yr  (PH Classic)
    Air tightness:       ≤ 0.6 ACH at 50 Pa (n50)
    Thermal bridges:     Ψ ≤ 0.01 W/mK at all junctions

  vs UK national average new-build:
    Heating demand: ~60–100 kWh/m²/yr
    Primary energy: ~150–200 kWh/m²/yr

  HOW PASSIVHAUS WORKS:
  ┌──────────────────────────────────────────────────────────────────────────┐
  │                                                                          │
  │  GAINS:                        LOSSES:                                  │
  │  Solar gains through glazing   Fabric heat loss: U × A × ΔT            │
  │  Internal gains: people,       Ventilation heat loss: V_dot × ρ_air    │
  │    appliances, lighting         × c_p × ΔT × (1 − η_MVHR)             │
  │                                                                          │
  │  PASSIVHAUS STRATEGY:                                                    │
  │  1. Super-insulate: U_wall ≤ 0.10–0.15 W/m²K                          │
  │  2. Triple glazing: U_w ≤ 0.80 W/m²K; south-facing gains               │
  │  3. Thermal bridge-free: Ψ ≤ 0.01 W/mK at all junctions               │
  │  4. Air-tight: n50 ≤ 0.6 ACH → stop infiltration losses               │
  │  5. MVHR: mechanical ventilation with heat recovery η ≥ 75%            │
  │     → ventilation losses nearly eliminated                              │
  │  6. Result: internal + solar gains = space heating demand               │
  │     → no boiler needed in most climates (only top-up from small HP)   │
  │                                                                          │
  │  MVHR: MECHANICAL VENTILATION WITH HEAT RECOVERY                        │
  │  Extract stale air from wet rooms → recover ~85% heat in heat exchanger │
  │  → supply pre-warmed fresh air to living rooms                          │
  │  Net ventilation heat loss: < 2% of extraction flow heat content       │
  │                                                                          │
  └──────────────────────────────────────────────────────────────────────────┘
```

---

## Embodied Carbon: Life Cycle Assessment

### LCA Framework

```
LCA STAGES IN DETAIL (EN 15978 / EN ISO 14040/14044)
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  A1  RAW MATERIAL EXTRACTION:  mining, quarrying, forestry                  │
│      For cement: CaCO₃ quarrying; clay/shale mining                         │
│      For steel: iron ore mining; coking coal mining                         │
│      For timber: forestry operations; transport to mill                     │
│                                                                              │
│  A2  TRANSPORT to manufacturing site                                         │
│      Global supply chains → shipping CO₂ often significant                 │
│                                                                              │
│  A3  MANUFACTURING:                                                          │
│      Cement: kiln (1450°C); ~0.83 tCO₂/t OPC clinker                       │
│      Steel BOF: blast furnace + converter; ~1.9 tCO₂/t steel                │
│      Steel EAF: electric arc (scrap); ~0.4–0.6 tCO₂/t steel                │
│      CLT: sawmill + adhesive + press; ~0.3–0.5 tCO₂/t CLT panel            │
│      Glass: float line (1600°C); ~0.7–1.0 tCO₂/t glass                    │
│                                                                              │
│  A4  TRANSPORT to construction site                                          │
│      Typically < 5–10% of total embodied carbon; varies                    │
│                                                                              │
│  A5  CONSTRUCTION PROCESS:                                                   │
│      Concrete waste: typically 2–5% of ordered volume wasted               │
│      Temporary works: formwork (timber + reuse factor); scaffolding        │
│      Energy: diesel plant, tower cranes, site lighting                     │
│                                                                              │
│  B1  IN USE (carbon release from materials — e.g., adhesive VOC)            │
│  B2  MAINTENANCE (repainting, recaulking, etc.)                             │
│  B3  REPAIR (structural repair — uncommon in LCA)                          │
│  B4  REPLACEMENT (replace short-life components: glazing seals, carpet)    │
│  B5  REFURBISHMENT (major building lifecycle event)                         │
│  B6  OPERATIONAL ENERGY (heating, cooling, lighting, hot water)            │
│  B7  OPERATIONAL WATER (embodied carbon in water treatment, pumping)        │
│                                                                              │
│  C1  DECONSTRUCTION/DEMOLITION                                               │
│  C2  TRANSPORT to waste processing                                          │
│  C3  WASTE PROCESSING (recycling, sorting)                                  │
│  C4  DISPOSAL (landfill)                                                    │
│                                                                              │
│  D   BEYOND BOUNDARY (reuse, recovery, recycling potential)                 │
│      Steel: high scrap value → D credit                                     │
│      CLT: structural reuse credit (if designed for disassembly)            │
│      Concrete: downcycled to aggregate (C3/D credit, small)                │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Biogenic Carbon: Timber

```
BIOGENIC CARBON ACCOUNTING IN TIMBER
──────────────────────────────────────────────────────────────────────────────
  SEQUESTRATION IN GROWTH:
    Photosynthesis: 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂  → wood = stored CO₂
    Approximate: 1 m³ of softwood stores ~0.9–1.1 tCO₂ (biogenic)
    CLT panel: ~0.45–0.55 m³ solid timber per m³ panel
    → ~0.45–0.55 tCO₂ biogenic credit per m³ panel

  RELEASE ON END-OF-LIFE:
    Combustion: CO₂ released immediately (biogenic → atmosphere)
    Decomposition: CO₂ + CH₄ (methane) released over years to decades
    Structural reuse: biogenic C stored further → additional credit (D stage)
    Landfill (waterlogged): minimal release for centuries (archaeological wood)

  CARBON BALANCE:
    Sustainably managed forest: forest carbon stock maintained/growing
    → biogenic C stored in buildings is effectively additional to baseline
    → when building demolished/burned → C returns to atmosphere → "carbon bank"
    → bank is valid only if replaced trees sequester equivalent amount in same period

  REPORTING CONVENTIONS:
    EN 15978: biogenic C reported SEPARATELY from fossil/process carbon
    → do not mix biogenic credit with fossil emissions (different permanence)
    RICS whole-life carbon: biogenic as additional module
    IPCC approach: report separately; biogenic sink in land-use sector
    GWP_biogenic: separate column from GWP_fossil in EPD (Environmental Product Declaration)

  COMMON MISTAKE:
    Treating timber as "carbon neutral" because it's biogenic → wrong
    The carbon balance depends on:
    1. Forest management (additionality of growth vs baseline)
    2. End-of-life scenario (reuse vs combust vs landfill)
    3. Time period (50-year building life vs forest rotation 40–80 years)
    4. Substitution effect (timber instead of steel = steel emissions avoided)
    Properly accounting for all four is necessary; none alone is sufficient
```

---

## Structural Frame Embodied Carbon Comparison

```
STRUCTURAL FRAME COMPARISON (kgCO₂e/m² GROSS FLOOR AREA)
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  (Based on RICS guidance, LETI reports, IStructE embodied carbon data)     │
│                                                                              │
│  FRAME TYPE                kgCO₂e/m² GFA    NOTES                           │
│  ─────────────────────────────────────────────────────────────────────────  │
│  RC flat slab              80–160            Depends on concrete strength,  │
│                                              rebar kg/m³, cement type       │
│  RC flat slab (50% GGBS)   50–110            GGBS substitution ~30% savings │
│  RC flat slab (70% GGBS)   40–90             Further reduction; code limits  │
│  Structural steel (BOF)    90–180            BOF route; high scrap content  │
│  Structural steel (EAF)    60–120            EAF scrap-based; ~40% less     │
│  Mass timber CLT            30–80  (gross)   Plus biogenic sequestration    │
│  Mass timber CLT            −10 to +30 (net) If biogenic credit included   │
│  Hybrid CLT + steel core   50–100            Typical commercial mass timber │
│  Precast concrete           70–140            Includes transport premium     │
│                                                                              │
│  LETI TARGETS (London Energy Transformation Initiative, 2020):              │
│  2025:  <700 kgCO₂e/m² whole building embodied (A1–A5)                    │
│  2030:  <500 kgCO₂e/m² whole building embodied                             │
│  Net zero embodied:  <300 kgCO₂e/m² whole building (aggressive; GLA London)│
│                                                                              │
│  Note: structural frame is 30–50% of whole-building A1–A5 embodied carbon  │
│  → foundation, façade, fit-out, MEP add the rest                           │
│                                                                              │
│  REDUCING EMBODIED IN CONCRETE FRAMES:                                      │
│  → Specify GGBS/fly ash replacement: 40–50% GGBS = ~25–35% CO₂ reduction  │
│  → Optimise rebar quantity (BIM analysis; avoid over-specification)         │
│  → Use UHPC or post-tensioned slabs to reduce concrete volume              │
│  → Design for adaptability → longer building life → embodied amortized     │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Circular Economy in Construction

```
CIRCULAR ECONOMY PRINCIPLES IN CONSTRUCTION
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  LINEAR ECONOMY:  Extract → Manufacture → Build → Use → Demolish → Landfill │
│                                                                              │
│  CIRCULAR ECONOMY:                                                           │
│    Design for Disassembly (DfD): reversible connections → components reused │
│    Material passports: BIM-embedded data → future use database              │
│    Deconstruction (not demolition): careful dismantling vs bulk demolition  │
│    Urban mining: building stock as resource bank                            │
│                                                                              │
│  DESIGN FOR DISASSEMBLY PRINCIPLES:                                          │
│  1. Accessible connections: exposed or accessible bolts vs cast-in          │
│  2. Reversible: bolt/screw not weld; timber screws not adhesive glulam      │
│  3. Standardized components: designed to current standards for future reuse │
│  4. Documented: material passports; as-built drawings; QR codes on elements│
│  5. Separation of layers: structure / envelope / fit-out at different lifespans│
│     (Brand's shearing layers: Site 0–∞; Structure 30–300yr; Skin 20yr; Services 7–15yr)│
│                                                                              │
│  MATERIAL RECYCLABILITY:                                                     │
│    Steel: 97%+ theoretically recyclable; in practice ~86% collected from   │
│      buildings; high-value market for scrap; embodied carbon of EAF scrap  │
│      ~0.4 tCO₂/t vs BOF ~1.9 tCO₂/t                                       │
│    Concrete: ~99% recycled as aggregate (C3 stage) but DOWNCYCLED           │
│      Recycled concrete aggregate (RCA) used in sub-base, non-structural;   │
│      properties inferior to virgin aggregate for structural concrete        │
│      "Closed-loop" structural concrete recycling: experimental; not yet     │
│      commercial (concrete composition knowledge needed; separating C from S)│
│    Timber/CLT: reversible screw connections → structural reuse possible     │
│      Structural reuse: 2nd-use CLT panels, glulam beams                    │
│      "Design for reuse" specifically sizes CLT for multiple use cycles     │
│    Glass: recyclable but mixed cullet → not float glass quality             │
│      Currently: crushed glass → road aggregate, foam glass insulation       │
│      True closed-loop float glass recycling: possible but market limited    │
│                                                                              │
│  MATERIAL PASSPORTS:                                                         │
│    BIM models → material quantities, specifications, connection types        │
│    RFID or QR codes on structural elements → scan to retrieve data          │
│    Netherlands: Dutch Madaster platform — building "bank accounts"           │
│    EU: Construction Product Regulation (CPR) revision → passports mandated  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Bio-Based Materials

### Hempcrete

```
HEMPCRETE: MATERIAL AND PERFORMANCE
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  COMPOSITION:                                                                │
│  Hemp shiv (hurds): woody core of Cannabis sativa stem, after retting      │
│    Particle size: 3–20 mm; density 100–140 kg/m³; ~50% hollow              │
│  Lime binder: hydraulic lime (NHL 2 or NHL 3.5) + air lime putty           │
│  Water: mix to paste consistency                                            │
│  Hemp:lime ratio: typically 1:1 to 1:2 by weight                          │
│                                                                              │
│  CURING:                                                                    │
│  Carbonation (air lime): CO₂ + Ca(OH)₂ → CaCO₃; weeks to months           │
│  Hydraulic set (NHL): days to weeks                                         │
│  Minimum cure before loading: 28 days                                       │
│                                                                              │
│  STRUCTURAL PROPERTIES:                                                      │
│  Compressive strength: 0.2–1.5 MPa  ← NOT structural in bending/shear     │
│  → hempcrete is an INFILL MATERIAL, not a load-bearing structural element  │
│  → always used with timber frame or other structural system                │
│                                                                              │
│  THERMAL AND HYGRIC PROPERTIES:                                              │
│    λ = 0.06–0.12 W/mK  (better than brick; worse than mineral wool)        │
│    ρ = 200–400 kg/m³  (light; good specific heat)                          │
│    c_p ≈ 1,700 J/kgK (similar to timber → decent thermal mass)             │
│    Vapour resistance μ: 2–6 (highly breathable; moisture-buffering)        │
│    → "hygric flywheel": absorbs/releases moisture → regulates interior RH  │
│                                                                              │
│  CARBON ACCOUNTING:                                                          │
│    Hemp growth: sequesters ~1.6–3 tCO₂/ha/year during growing season      │
│    Hemp shiv embodied carbon: −0.3 to −0.5 kgCO₂/kg (biogenic credit)    │
│    Lime binder: +0.4–0.6 kgCO₂/kg (calcination + carbonation net)         │
│    Hempcrete panel 300 mm: potentially near carbon-neutral or net-negative  │
│    Uncertainty: biogenic carbon accounting conventions (temporary storage)  │
│                                                                              │
│  APPLICATIONS:                                                               │
│  Cast-in-place: temporary formwork; cast hemp-lime in lifts around frame   │
│  Pre-cast blocks: smaller-scale projects; easier quality control            │
│  Spray-applied: mechanical application onto frame                           │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Straw Bale Construction

```
STRAW BALE: STRUCTURAL AND THERMAL
──────────────────────────────────────────────────────────────────────────────
  BALE TYPES:
    Standard (two-string): 450 × 350 × 950 mm; ~20–25 kg
    Three-string (Nebraska style): 450 × 600 × 1200 mm; ~35–50 kg
    Density: ~80–120 kg/m³ (varies; denser = stronger + better insulation)

  CONSTRUCTION SYSTEMS:
  Load-bearing (Nebraska/stacked): bales stacked as masonry; roof load direct to bales
    → structural; bales in compression; suitable for single-storey; code gap issue
    → hazel rods/rebar pins through bales for stability
    Compressive strength: 0.2–0.8 MPa → adequate for one storey residential

  Post-and-beam infill: timber frame carries structural loads; bales = infill
    → most widely used in UK/Europe; clearer structural path; easier code compliance

  THERMAL PERFORMANCE:
    λ = 0.05–0.10 W/mK  (bale oriented flat; varies with grain direction + density)
    U-value (450 mm bale + render both sides): ~0.13 W/m²K  ← excellent
    → exceeds Passivhaus wall requirement without additional insulation layers

  RENDER:
    External: hydraulic lime render (NHL 2/3.5) 25–35 mm; weather protection
    Internal: lime plaster; vapour-permeable; hygric buffering
    Must remain breathable: NO cement render (locks moisture → rot)

  FIRE:
    Compressed straw: burns slowly; char layer forms; much safer than loose straw
    Renders: prevent flame spread → 30–60 min fire resistance achievable
    UK Building Regs Part B: covered by some local authority relaxations

  MOISTURE:
    Critical: straw must stay below 20% moisture content → below rot threshold
    Design strategy: ventilated gap behind external render (UK: rain risk)
      OR very wide eaves overhang (protect from rain)
    Foundation: keep bales above DPC and above flood risk

  CARBON:
    Straw is an agricultural by-product (waste from grain harvest)
    Embodied carbon of bales: very low (transport + baling energy only)
    Net carbon negative possible with lime renders (lime is close to neutral cycle)
```

### Bamboo

```
BAMBOO AS STRUCTURAL MATERIAL
──────────────────────────────────────────────────────────────────────────────
  SPECIES: Guadua angustifolia (Americas), Moso (Asia) — best for structure
  GROWTH: culm (stem) reaches full height in 60–90 days; 4–5 year maturity
    → replenishes far faster than any timber species
    → 3–8 m height at structural maturity; diameter 80–150 mm

  STRUCTURAL PROPERTIES (Guadua angustifolia, dried):
    Tensile strength (// culm): 100–200 MPa  ← comparable to mild steel specifically
    Compressive strength (// culm): 40–80 MPa
    Bending strength: 60–120 MPa
    E (// culm): 17,000–22,000 MPa  (similar to structural timber)
    Density: 500–900 kg/m³ (varies; outer layer denser)
    Note: hollow tube geometry → efficient structural section

  SPECIFIC STRENGTH:
    σ_u / ρ: 100–200 MPa / 700 kg/m³ ≈ 0.14–0.29 kNm/kg
    Compare: steel A36 = 400/7850 = 0.051 kNm/kg  → bamboo specific strength
    significantly higher → weight-efficient material

  CHALLENGES:
    Connections: hollow tube makes bolted connections difficult → specialized fittings
    Moisture: untreated bamboo rots; borax or other treatment required for interior
    Durability: surface must be protected from rain and soil contact
    Standardization: significant natural variability between culms and species
    Codes: no international structural code; bespoke engineering assessment

  ISO 22156: Bamboo structures — design, which provides some guidance
  INBAR (International Bamboo and Rattan Organisation): technical standards developing
```

---

## Rating Systems and Standards

```
BUILDING RATING SYSTEMS COMPARISON
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  SYSTEM        ORIGIN  WHAT IT MEASURES            KEY METRIC               │
│  ────────────────────────────────────────────────────────────────────────   │
│  LEED          USA     Energy, water, materials,   Points 26–110 → Cert/    │
│                        health, transport            Silver/Gold/Platinum    │
│                        Operational focus            40% credits energy-relat │
│                        Not Passivhaus standard      No absolute energy limit │
│                                                                              │
│  BREEAM        UK      Breadth: energy, water,      Pass/Good/VG/Exc/Outst  │
│                        transport, ecology, pollu.   % score by category     │
│                        Materials credits include    Mandatory min standards  │
│                        embodied carbon option       Widely used UK (mandatory│
│                                                     for some public funding) │
│                                                                              │
│  Passivhaus    DE/AT   Energy performance only:     Absolute kWh/m²/yr      │
│  (PHPP)                Heating ≤15; cooling ≤15;    Air tightness n50        │
│                        air tightness ≤0.6 ACH       Binary: meets or fails  │
│                        Not sustainability           Gold standard energy     │
│                                                                              │
│  WELL          USA     Health and wellbeing:        Concepts: Air, Water,   │
│                        Air, water, light, thermal   Light, Nourishment,     │
│                        comfort, acoustics, biophilia Mind, Movement, Comfort │
│                        No energy focus              Complementary to LEED   │
│                                                                              │
│  Living Bldg   USA     Highest bar: net positive    Net zero or positive     │
│  Challenge            water, energy, carbon         ALL petals must pass    │
│                        Beauty + biophilic design     Very few buildings cert │
│                                                                              │
│  NABERS        AU      Actual operational energy:   Star ratings 0–6        │
│                        Measured in use (not predicted) Widely used commercial│
│                        No embodied carbon metric    AU/NZ origin             │
│                                                                              │
│  GAPS IN ALL SYSTEMS: No current major rating system adequately measures    │
│  whole-life carbon (A1–C4 per EN 15978) in a rigorous standardized way.    │
│  LETI, RIBA 2030 targets, GLA London Plan: provide embodied carbon limits   │
│  but these are planning guidance, not certification schemes.                 │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Refrigerants and Whole-Building F-Gas Issue

```
REFRIGERANT GWP IMPACT ON WHOLE-BUILDING CARBON
──────────────────────────────────────────────────────────────────────────────
  HVAC and refrigeration systems use refrigerants: HFCs (hydrofluorocarbons)
  GWP (100-year): CO₂ = 1 (reference)

  COMMON REFRIGERANTS:
    R-410A:  GWP = 2,088  ← dominant in HVAC; being phased out
    R-32:    GWP = 675    ← replacement; lower GWP; mildly flammable (A2L)
    R-134a:  GWP = 1,430  ← legacy
    R-407C:  GWP = 1,774
    R-744 (CO₂):  GWP = 1  ← transcritical CO₂; low GWP; high pressure system
    R-717 (NH₃):  GWP = 0  ← ammonia; zero GWP; toxic (industrial only)
    Natural refrigerants (propane R-290): GWP = 3; flammable A3

  EU F-Gas Regulation: HFCs phasing down 79% by 2030 (relative to 2015 baseline)
    → R-410A banned in new systems from 2025 (EU) → R-32 or lower GWP
    → HFCs entirely phased out EU by 2050 target

  WHY THIS MATTERS FOR EMBODIED CARBON:
    Typical office building (1,000 m²): 20 kg R-410A charge (chiller system)
    Direct CO₂eq: 20 kg × 2,088 = 41.8 tCO₂eq
    Leakage rate: 2–5% per year typical for HVAC systems
    Annual leakage: 0.8–2.1 tCO₂eq/year per system
    Over 15-year service life: 12–31 tCO₂eq leaked per system
    → comparable to A1–A5 embodied carbon of significant structural elements
    → not included in typical building embodied carbon calculations
    → inclusion in B3 (maintenance/replacement) when refrigerant topped up

  WHOLE-BUILDING CARBON TARGET COMPLIANCE:
    Designers must now account for refrigerant leakage in whole-life carbon
    Natural refrigerants or CO₂ systems increasingly specified on net-zero targets
```

---

## Adaptive Reuse: The Embodied Carbon Argument

```
ADAPTIVE REUSE vs NEW BUILD: CARBON ANALYSIS
──────────────────────────────────────────────────────────────────────────────
  EMBODIED CARBON OF DEMOLITION + NEW BUILD:
    Demolition (C1–C4): ~20–50 kgCO₂e/m²
    New build A1–A5:  ~300–700 kgCO₂e/m² (depending on system)
    Total: ~320–750 kgCO₂e/m² emitted on completion day

  EMBODIED CARBON OF ADAPTIVE REUSE (retain structure):
    Demolition of fit-out: ~5–15 kgCO₂e/m²
    New fit-out (interior, MEP, facade):  ~100–250 kgCO₂e/m²
    Total: ~105–265 kgCO₂e/m²  → 60–70% reduction in upfront embodied

  OPERATIONAL CARBON COMPARISON:
    Old building refurbished to high energy standard: ~30–50 kWh/m²/yr
    New Passivhaus equivalent: ~15–20 kWh/m²/yr
    → operational carbon difference: ~10–30 kWh/m²/yr
    → at UK grid: ~5–15 kgCO₂e/m²/yr currently (declining as grid decarbonizes)

  CARBON PAYBACK PERIOD:
    Additional embodied carbon of new build vs retrofit: ~200–500 kgCO₂e/m²
    Annual operational saving of new build vs retrofit: ~5–15 kgCO₂e/m²/yr
    Carbon payback: 200–500 / 5–15 = 13–100 YEARS
    → in many cases, the new build never pays back its upfront carbon before
      the building needs refurbishing again
    → this analysis is now driving policy toward reuse

  UK GOVERNMENT: 2023 NPPF (National Planning Policy Framework): reuse
    should be considered before demolition in planning decisions
    RICS / IStructE guidance: structural engineer brief should include
    "feasibility of retention" as first-pass assessment
```

---

## Whole-Building Energy Modeling

```
ENERGY MODELLING TOOLS
──────────────────────────────────────────────────────────────────────────────
  TOOL          OWNERSHIP     STRENGTHS                USES
  ──────────────────────────────────────────────────────────────────────────
  EnergyPlus    US DOE; free  Detailed simulation;     Research; compliance
                              many modules; scripted   checking; post-design
                              open; Python API         analysis

  IES-VE        Commercial    Integrated: EPC, Venti-  UK commercial; planning
                (UK £)        lation, CFD, MVHR        submissions; BREEAM
                              ApacheHVAC + ApacheSim   Great GUI; consultants

  TRNSYS        Commercial    Transient; component      Complex systems; HVAC
                              based; research-oriented  sizing; solar thermal

  DesignBuilder EnergyPlus    GUI for EnergyPlus;      ASHRAE 90.1 compliance
                frontend      LEED calculations        US market; improving

  PHPP          iPHA; cheap   Passivhaus certification  PH design; accurate for
  (Passivhaus   licensed      Steady-state monthly     simple to complex forms
  Planning Pkg)               calculation; Excel       Not for HVAC sizing

  SAP / RdSAP   DCLG (UK)     UK regulatory calcu-     UK Part L; EPC ratings
                               lation; operational      Mandatory compliance
                               energy rating            Simplified; not for design

  HONEYBEE/     Free (Python) Ladybug/Honeybee +        Parametric early design
  LADYBUG        GH plugins   EnergyPlus backend        Grasshopper/Rhino users
                              Parametric study fast     Research + architecture

  TYPICAL WORKFLOW:
  Early design: PHPP or simplified RICS energy calcs → quick fabric decisions
  Detailed design: IES-VE or EnergyPlus → HVAC sizing; overheating check
  Planning submission: IES-VE for BREEAM; SAP for Part L compliance
  Post-occupancy: compare measured vs predicted → close the performance gap
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| New build vs adaptive reuse — carbon argument? | Retain structure if feasible: saves ~200–500 kgCO₂e/m² upfront; payback for new build often > 30 yr |
| How to reduce concrete frame embodied carbon fastest? | Specify 40–50% GGBS replacement in all concrete — single largest lever; 25–40% reduction |
| Passivhaus vs LEED — which for energy performance? | Passivhaus: absolute energy standard; LEED: relative points. Passivhaus for genuine energy performance. |
| CLT "carbon negative" claim — valid? | Only if biogenic credit included AND sustainable forestry AND specific EOL scenario assumed. Report separately from fossil. |
| Where is embodied carbon NOT currently captured in ratings? | LEED and BREEAM have limited embodied carbon credits; whole-life carbon in EN 15978 is not yet mandatory in most codes |
| Refrigerant choice — priority in net-zero building? | Specify low-GWP (GWP < 150); CO₂ (R-744) or propane (R-290) systems where feasible; avoid R-410A |
| Bamboo structural in temperate climate? | Requires drying, treatment, specialist connections; not mainstream code coverage; consult specialist |
| Straw bale — why does render type matter? | Straw must breathe: lime render (vapour-permeable). Cement render: traps moisture → rot |

---

## Common Confusion Points

**Operational carbon is NOT solved — but it IS solvable.** The technology exists (super
insulation, triple glazing, MVHR, heat pumps). The policy and market delivery
mechanisms are still catching up. The point is that in a well-designed new building,
operational carbon CAN be near zero. Embodied carbon CANNOT yet be near zero with
conventional materials — hence it dominates the challenge for 2025–2050.

**BREEAM "Excellent" does not mean low embodied carbon.** BREEAM awards points across
many categories. A building with excellent transport links and good ecology can achieve
"Excellent" with average structural specification. BREEAM Mat 01 (responsible sourcing)
and Ene 01 (energy) are the relevant credits, but they don't together constitute a whole-
life carbon assessment. A BREEAM "Excellent" building can have high embodied carbon.

**LCA results are meaningless without system boundary statement.** Two LCA studies of
"the same material" will give different results if one uses A1–A5 and the other A1–C4.
Always check: what stages are included? Is biogenic carbon included or excluded? What
is the functional unit (per kg? per m²? per m of building life?)? EPDs (Environmental
Product Declarations) standardize this via EN 15804, but comparisons still require care.

**Carbon storage in timber is temporary, not permanent.** A 50-year timber building
releases biogenic carbon when demolished. This is not "free" carbon — it is borrowed
from the forest carbon cycle. The climate benefit is real but time-limited, and depends
entirely on the forest management system. Deforesting to build CLT buildings would be
catastrophic even though the timber "stores carbon."

**Passivhaus operational energy targets are absolute, not percentage improvements.**
Building Regulations (Part L, UK) and similar codes use "percentage improvement over
baseline" (TER/BER). This allows builders to achieve compliance while building leaky
buildings if the baseline is set low enough. Passivhaus uses absolute kWh/m²/yr — no
games, no baselines. This is why Passivhaus buildings actually perform as designed, and
why compliance-minimum Part L buildings have a large performance gap in practice.
