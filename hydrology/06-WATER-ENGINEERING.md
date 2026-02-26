# Water Engineering — Dams and Reservoirs, Levees, Stormwater Management, Water Supply Design

## The Big Picture

<!-- @editor[diagram/P2]: Diagram is a flat taxonomy grid of infrastructure categories — doesn't show how they connect (e.g., storage feeds supply and irrigation; stormwater and flood protection interact; hydropower requires dam storage); rework as a flow diagram showing water path through infrastructure systems -->
```
+===========================================================================+
|                   WATER INFRASTRUCTURE TAXONOMY                            |
+===========================================================================+
|                                                                           |
|  STORAGE / REGULATION          FLOOD PROTECTION        SUPPLY             |
|  ────────────────────          ──────────────────       ──────            |
|  Dams and reservoirs           Levees / floodwalls      Intakes           |
|  Detention basins              Flood bypasses            Pipelines         |
|  Retention ponds               Emergency spillways       Treatment plants  |
|                                Floodplain buyouts        Distribution      |
|                                                                           |
|  STORMWATER                    IRRIGATION                ENERGY            |
|  ────────────                  ──────────                ──────────        |
|  Sewer networks                Canals/ditches            Hydropower        |
|  Green infrastructure          Drip irrigation           Pumped storage    |
|  Bioswales / rain gardens      Groundwater pumping       Run-of-river      |
|  Permeable pavement                                                        |
+===========================================================================+
```

---

## Dams and Reservoirs

### Dam Types

```
GRAVITY DAM:
  Resists water pressure by weight of dam itself
  Material: mass concrete or roller-compacted concrete (RCC)
  Cross-section: triangular profile (widest at base, where hydrostatic pressure max)
  Forces: water pressure (horizontal), weight (vertical), uplift (pore pressure in foundation)
  Safety: factor of safety against sliding ≥ 1.5, against overturning ≥ 2.0
  Examples: Grand Coulee (US), Hoover (US), Three Gorges (China)

ARCH DAM:
  Transfers water pressure laterally to canyon walls (abutments)
  Can be very thin → less concrete → lower cost in narrow canyons
  Requires: sound canyon wall rock (carries horizontal arch thrust)
  Profile: curved in plan view; arch-gravity: curved + heavy
  Examples: Hoover is actually arch-gravity; Vajont (collapsed 1963)

EMBANKMENT DAM:
  Earth or rock fill; most common dam type worldwide
  Two types:
    Earthfill: compacted clay core (impervious) + gravel/rock shells
    Rockfill: rock shells + clay or concrete core (or geomembrane face)
  FAILURE MODE: OVERTOPPING (most common earthfill failure)
    → designed with large emergency spillways to prevent overtopping
    Internal erosion (piping): seepage through dam entrains soil particles
      → progressive erosion → internal tunnel → failure
      → prevents by: filter and drainage layers, compaction
  Examples: Tarbela (Pakistan — largest by volume), Aswan High Dam (Egypt)

BUTTRESS DAM:
  Hollow: concrete face supported by buttresses (fins)
  Less concrete than gravity dam; requires sound foundation
  Rare today (RCC made gravity dams cheaper)
```

### Reservoir Hydraulics

```
SPILLWAYS AND OUTLETS:

  SPILLWAY: overflow structure for flood routing
    Free flow (uncontrolled): water spills when reservoir fills
    Gated (controlled): gates regulate flow; allows higher surcharge storage

  SPILLWAY DESIGN FLOOD (SDF):
    How large a flood must the spillway handle?
    Consequence classification:
      Low hazard (undeveloped downstream): 10–50 yr return period
      Significant hazard: 100–500 yr
      High hazard (dense population below): 1000-yr to PMF (Probable Maximum Flood)
    PMF (Probable Maximum Flood): derived from PMP (Probable Maximum Precipitation)
      Theoretical maximum precipitation from atmospheric physics
      Used for high-hazard structures: nuclear plants, major dams

  OUTLET WORKS:
    Valve/gate structures at base of dam
    Controls releases for: downstream flow, irrigation water supply, power generation
    Must operate during and after major floods

RESERVOIR SEDIMENTATION:
  Rivers carry sediment → enters slow-moving reservoir → deposits
  Trap efficiency (TE): fraction of incoming sediment deposited
    TE ≈ function of reservoir capacity / annual inflow (Brune curve)
    TE > 95% for large reservoirs (almost all sediment trapped)

  CONSEQUENCES:
    Reservoir capacity decreases over time (most lose 1–2% per year)
    Dead storage (below lowest outlet): fills with sediment
    Downstream: sediment-starved → incision, delta retreat, beach starvation
    Colorado River: Hoover + Glen Canyon dams trap ~100% of sediment
      → Grand Canyon riverbed incised, Colorado Delta destroyed
    Major Nile Delta erosion since Aswan High Dam (1970)

  FLUSHING: periodic controlled releases to scour sediment
    Effective for thin-drawdown reservoirs; difficult for deep reservoirs
  VENTING TURBIDITY CURRENTS: allow sediment-laden floods through low-level outlets
  BYPASS CHANNEL: route sediment-laden floods around reservoir
```

---

## Levees

```
LEVEE TYPES:
  Earthen: compacted soil embankment (most common)
  Concrete floodwall: vertical structure (urban areas, limited space)
  Sheet pile: steel or concrete sections driven into ground (temporary, emergency)

LEVEE DESIGN:
  Height = design flood water surface elevation + freeboard
    Freeboard: safety margin, typically 0.5–1.5 m (protects against wave action, uncertainty)
  Side slopes: 2H:1V to 3H:1V (flatter is more stable)
  Foundation: key trench or cutoff wall to prevent underseepage

LEVEE FAILURE MODES:
  Overtopping: flood exceeds levee height → water flows over → rapid erosion
    → 75%+ of levee failures historically
  Seepage/piping: water seeps through or under levee → internal erosion
    → detectable by: wet spots on land side, sand boils (artesian sand eruptions)
  Slope failure: saturated levee → reduced shear strength → sliding failure
    Saturation-induced failure: typically occurs AFTER flood recedes
    (seepage pressure highest when flood drops rapidly)

LEVEE SYSTEMS AND FALSE SECURITY:
  Levees rated to specific event (e.g., 100-yr event)
  Property development fills in behind levees (because "protected")
  When exceeded: CATASTROPHIC failure (no gradual flooding)
    vs. unleveed floodplain: gradual inundation, lower damage
  New Orleans Katrina 2005: levees failed at BELOW design event
    → risk was much higher than advertised → "levee effect" of encouraging floodplain development
  Sacramento-San Joaquin Delta: 1100 km of aging levees protecting
    ~1 million hectares below sea level → "California's Katrina waiting to happen"
```

---

## Stormwater Management

### Urban Hydrology and Impervious Cover

```
URBAN EFFECTS ON HYDROLOGY:
  Impervious surfaces (roofs, roads, parking): fast runoff response
    CN goes from 55–70 (natural) to 90–98 (urban)
    Tc (time of concentration) decreases dramatically: 6 hr → 1 hr
    Peak flow increases: typically 3–10× natural
  Stormwater drainage systems: storm sewers accelerate runoff to streams
  Combined sewers: mix stormwater + sanitation → overflow during storms (CSOs)
    → water quality problem; phase-out in US required by Clean Water Act

TRADITIONAL ("GRAY") STORMWATER INFRASTRUCTURE:
  Storm sewers: pipes (concrete, HDPE) collecting runoff from streets
  Inlet: curb catch basin → collector pipe → outfall to stream
  Design: Rational method, 5-yr or 10-yr return period event
  Limitations: only manages quantity; doesn't remove pollutants; expensive

CONVENTIONAL DETENTION BASIN:
  Pond that temporarily stores stormwater during storms
  Outlet: small orifice + spillway
  Design: attenuate post-development peak flow to pre-development rates
  Volume: computed from routing (detention ∝ time × Qin - Qout)
  Limitation: volume-based — can control 2-yr and 10-yr peaks but not water quality well
```

### Green Infrastructure (GI) / Low-Impact Development (LID)

```
PRINCIPLE: Manage stormwater where it falls — retain, infiltrate, evapotranspire
  Rather than: collect fast → pipe → stream

BIORETENTION (RAIN GARDEN):
  Shallow depression planted with native plants + engineered soil mix
  Stormwater enters → pools → infiltrates through engineered media
  Media: sand-compost mix → supports plant growth + treats runoff quality
  Underdrain: perforated pipe at bottom (if native soils too impermeable)
  Size: typically 5–20% of contributing impervious area
  Water quality: removes: TSS 85–90%, TN 40–60%, TP 60–80%, metals 85–95%
  Flood control: depends on sizing

PERMEABLE PAVEMENT:
  Pervious concrete, porous asphalt, interlocking pavers with gaps
  Runoff infiltrates through surface → storage in gravel base → drain/infiltrate
  Load-bearing: can support vehicles (parking lots, low-traffic roads)
  Maintenance: vacuum sweeping to prevent clogging (critical!)
  Not suitable: fine-grained soils (slow infiltration), steep slopes, spill areas

GREEN ROOF:
  Extensive: 3–10 cm growing media, succulents (Sedum), 10–30 kg/m²
  Intensive: 15–100+ cm growing media, garden, 50–300 kg/m²
  Stormwater retention: 40–80% of annual rainfall retained (evapotranspired)
  Cooling: significant urban heat island mitigation
  Structural requirement: extensive adds ~12 kg/m² to existing structure

BIOSWALE / VEGETATED SWALE:
  Open channel with vegetation, designed to slow runoff + allow infiltration
  Check dams: small berms slow flow in swale → longer residence time
  Replaces: traditional concrete-lined drainage channels
  Works for: linear drainage paths (roadsides, parking lot borders)

TREE BOXES / INFILTRATION TRENCHES:
  Underground storage + tree canopy interception
  Continuous walls of soil alongside roads
  Intercepts roof runoff + sidewalk runoff
  Very effective per $ in dense urban areas

GI PERFORMANCE METRICS:
  Retention: total stormwater volume captured (not released)
  Detention: peak flow attenuation (delay and slow)
  Water quality: pollutant removal (%) for TSS, nutrients, metals
  In practice: GI designed to manage "small frequent storms" (80th percentile ~1–1.5 inch event)
  Extreme events: GI supplemented by conventional detention basins
```

---

## Water Supply Design

### Source Types and Reliability

```
SOURCE SELECTION CRITERIA:
  Quantity: adequate annual yield to meet demand (with safety factor)
  Reliability: 95–99% probability of meeting demand in any year
  Quality: treatability (less costly to treat = better source)
  Location: proximity to demand (pump costs, pipe lengths)
  Regulatory: permitting, senior water rights, interstate compact

SOURCE TYPES:
  Surface water: rivers, lakes, reservoirs
    + High yield, renewable
    - Variable quality and quantity; vulnerable to drought; requires treatment
  Groundwater: wells in aquifers
    + Usually better quality (natural filtration), reliable, distributed
    - Can be overdrafted (non-renewable), subsidence, contamination risk
  Rainwater harvesting: roof collection → cisterns
    + No pumping energy
    - Variable supply, limited capacity, requires treatment
  Treated wastewater (direct/indirect potable reuse):
    + Large volume, consistent
    - Public acceptance, advanced treatment required
    Indirect reuse: discharged to stream/aquifer, then re-withdrawn (existing de facto reuse)
    Direct potable reuse (DPR): treat to drinking water standards → direct to distribution
```

### Reservoir Yield Analysis

```
SAFE YIELD OF RESERVOIR:
  Maximum constant draft that can be maintained throughout a critical drought
  Critical drought: worst sequence of below-average inflows in historical record

  MASS CURVE METHOD (Ripple, 1882):
    Plot cumulative inflow vs. time
    Required storage = maximum deficit between cumulative demand and cumulative inflow
    Graphically: largest "sag" on the mass balance curve

  STOCHASTIC ANALYSIS:
    Generate synthetic streamflow sequences (preserve mean, variance, lag-1 autocorrelation)
    Monte Carlo: thousands of simulations → yield-reliability-storage relationships
    Design: select storage for desired reliability (95%, 99%, etc.)

  RULE CURVES:
    Operating rules: when to release, when to withhold, conservation pool levels
    Flood control pool: empty space reserved for flood storage at top of reservoir
    Conservation pool: stored water for supply
    Dead storage: below outlets (sedimentation sink)
    ┌──────────────────────┐ ← Top of dam (emergency spillway crest)
    │ Flood control pool   │ ← Empty in winter, can store flood
    ├──────────────────────┤ ← Conservation (full) pool
    │ Conservation pool    │ ← Water supply, hydropower, recreation
    │                      │
    ├──────────────────────┤ ← Minimum pool
    │ Dead storage         │ ← Below outlets, fills with sediment
    └──────────────────────┘
```

### Water Distribution Systems

```
DISTRIBUTION SYSTEM DESIGN:
  Pressure requirement: minimum 140 kPa (20 psi) at service connections
                        280+ kPa (40 psi) at fire hydrants
  System pressure: controlled by storage tanks / pressure zones
  Pressure zones: separate zones for elevation differences (>45 m → separate zone)
  Network modeling: Hardy-Cross or Newton-Raphson node-based analysis
    (Iterative solution to nonlinear pipe network equations — same as circuit analysis)

PIPE SIZING (Hazen-Williams):
  V = 0.849 × C × R^0.63 × S^0.54    (velocity in m/s)
  Q = A × V

  C = Hazen-Williams coefficient (roughness):
    Ductile iron (new): C = 130
    Ductile iron (old): C = 100–120
    PVC: C = 150
    Concrete: C = 120

  Friction loss: h_f = 10.67 × L × Q^1.852 / (C^1.852 × D^4.87)

PIPE MATERIALS:
  Ductile iron (DI): standard for large mains (100–1200 mm), 50+ yr life
  PVC: service lines and smaller mains (12–400 mm), corrosion-resistant
  HDPE: flexible, trenchless installation, corrosion-resistant
  Concrete cylinder: large-diameter water mains (600–3600 mm)
  Lead service lines: LEGACY PROBLEM
    Used extensively pre-1950 in US
    Still present in ~6–10 million US homes (estimate)
    Corrosion → lead leaching → especially harmful to children (neurotoxic)
    Lead service line replacement programs: ~$60 billion national need

WATER DEMAND:
  Per capita: 200–400 L/day (US, includes commercial/industrial)
    Residential: ~150–250 L/person/day
  Peak day: 1.5–2.5 × average day (seasonal variation, summer irrigation)
  Peak hour: 2–4 × average day (morning/evening peaks)
  Fire demand: 30–60 L/s for 2 hr (for residential areas — larger for commercial)
  System must meet: max hour domestic + fire demand simultaneously
```

---

## Hydropower

```
HYDROPOWER POTENTIAL:
  P = η × ρ × g × Q × H

  P = power (W)
  η = efficiency (0.85–0.95 for modern turbines)
  ρ = water density (1000 kg/m³)
  g = 9.81 m/s²
  Q = flow rate (m³/s)
  H = head (height water falls, m)

  EXAMPLE: Q=100 m³/s, H=50 m, η=0.90
    P = 0.90 × 1000 × 9.81 × 100 × 50 = 44 MW

TURBINE TYPES:
  High head (>30 m): Pelton (impulse), Francis
    Pelton: very high head (200–2000 m), spoon-shaped buckets, jet deflection
    Francis: medium-high head (10–600 m), spiral casing, radial-axial flow
  Low head (<30 m): Kaplan, propeller, run-of-river bulb turbines
    Kaplan: adjustable-pitch propeller blades → efficient over wide flow range
    Best for: large rivers with small head (Columbia, St. Lawrence, Rhine)

PUMPED STORAGE HYDROPOWER (PSH):
  Largest grid-scale energy storage technology (90%+ of global grid storage by capacity)
  Off-peak: pump water uphill (cheap electricity → potential energy)
  Peak: release water to generate power (sell at peak price)
  Round-trip efficiency: ~75–80%
  Response time: <30 seconds → crucial for grid frequency regulation
  Examples: Bath County (US, 3003 MW), Hoover (US), Bieudron (Switzerland, 1269 MW)
```

---

<!-- @editor[bridge/P2]: Pipe network analysis (Hardy-Cross) is mentioned as "same as circuit analysis" but deserves a brief bridge callout — the learner has deep .NET/Azure background and will immediately grasp Kirchhoff's laws → node-loop equations in a water distribution network; also: reservoir rule curves are essentially state-machine operating policies -->

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What type of dam uses its own weight? | Gravity dam (mass concrete/RCC) |
| What causes most earthen dam failures? | Overtopping (then piping/internal erosion second) |
| What is a PMF? | Probable Maximum Flood — theoretical maximum for high-hazard dam design |
| Why do reservoirs silt up? | Slow water velocity → sediment settles; trap efficiency >95% for large reservoirs |
| What is a levee's biggest risk factor? | False security leads to floodplain development; failure of designed protection → catastrophic |
| What is the difference between detention and retention? | Detention: stores water, releases slowly; Retention: permanently stores water (infiltration/ET) |
| What is LID/GI? | Manage stormwater where it falls — infiltration, ET, retention — vs. pipe and discharge |
| Hazen-Williams vs. Manning? | H-W for pressure pipe (closed conduit); Manning for open channels (gravity flow) |

---

## Common Confusion Points

**Detention basin ≠ retention pond**: Detention basins temporarily store water and release it slowly (peak attenuation only). Retention ponds have a permanent pool and are sized for infiltration/ET/evaporation (volume reduction). Retention ponds improve water quality better than detention basins.

**Levee height is not the same as protection level**: A 100-year levee is designed for the 100-year flood profile, including backwater effects, wave action, and settlement. But "100-year protection" is a probabilistic statement — there's a 64% chance of seeing at least one 100-year event in 100 years. Also: climate change shifts the distribution so yesterday's 100-year event may be tomorrow's 10-year event.

**Green infrastructure doesn't replace conventional for large storms**: GI (rain gardens, bioretention, permeable pavement) is excellent for small, frequent storms (the 80th percentile storm ~25 mm / 1 inch). For 100-year flood events, you still need large detention basins and conveyance. A comprehensive stormwater system uses GI at the lot level + detention at the sub-basin level + major drainage at the basin level.

**Hydropower is renewable but not always sustainable**: Run-of-river hydropower has minimal storage and disruption. Large reservoir hydropower disrupts sediment transport (downstream delta starvation), floods riparian habitat, alters thermal regime, and blocks fish migration. It's not zero-impact. The Three Gorges Dam displaced ~1.4 million people and dramatically changed the Yangtze ecosystem.

**Safe yield ≠ firm yield**: Safe yield assumes historical hydrology continues unchanged. Firm yield is yield available under specified drought conditions. Under climate change, historical records don't represent future hydrology — drought sequences longer and more severe than historical record → "safe yield" analysis may overestimate actual available supply.
