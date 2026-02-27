# Air Quality Engineering

## The Big Picture

Air quality regulation works on two parallel tracks: criteria pollutants (NAAQS — six
pollutants with ambient standards based on human health) and hazardous air pollutants
(187 listed HAPs — technology-based standards). GHG regulation runs alongside both.

```
  AIR QUALITY REGULATORY STRUCTURE

  ┌─────────────────────────────────────────────────────────────────┐
  │                  CLEAN AIR ACT (CAA, 1970)                     │
  ├───────────────────┬─────────────────────┬───────────────────────┤
  │  CRITERIA         │  HAZARDOUS AIR      │  GHG / CLIMATE        │
  │  POLLUTANTS       │  POLLUTANTS (HAPs)  │  EMISSIONS            │
  │  ──────────       │  ──────────────     │  ─────────────        │
  │  NAAQS set        │  187 listed HAPs    │  Endangerment         │
  │  (6 pollutants)   │  NESHAP rules       │  Finding (2009)       │
  │  Primary: health  │  MACT standard      │  GHGRP (Part 98)      │
  │  Secondary: welfare    (max achievable  │  >25,000 MT CO₂e/yr  │
  │                   │  control tech)      │                        │
  │  SIP: states must │                     │  GHG PSD review for   │
  │  show attainment  │  Residual risk      │  major sources        │
  │  Nonattainment    │  review (10⁻⁶       │                        │
  │  → stricter new   │  excess cancer      │                        │
  │  source review    │  risk threshold)    │                        │
  └───────────────────┴─────────────────────┴───────────────────────┘
           ↓                    ↓                      ↓
  ┌──────────────────────────────────────────────────────────────────┐
  │              PERMITTING SYSTEM                                   │
  │  Minor source permit: PTE < major thresholds                    │
  │  PSD (Prevention of Significant Deterioration): attainment areas │
  │    → BACT (best available control technology), increment analysis │
  │  NSR (New Source Review): nonattainment areas                   │
  │    → LAER (lowest achievable emission rate) + offsets           │
  │  Title V operating permit: major sources (≥100 tpy criteria,   │
  │    ≥10 tpy single HAP, ≥25 tpy total HAPs)                     │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Criteria Pollutants and NAAQS

The six criteria pollutants have both primary (health) and secondary (welfare/visibility)
NAAQS. Standards are reviewed every 5 years under the CAA.

```
  NATIONAL AMBIENT AIR QUALITY STANDARDS (current)

  ┌──────────┬────────────┬──────────────────────────────────────────┐
  │ Pollutant│ Standard   │ Health Basis / Notes                     │
  ├──────────┼────────────┼──────────────────────────────────────────┤
  │ PM₂.₅    │ 9 μg/m³    │ Annual (most recently tightened, 2024); │
  │          │ 35 μg/m³   │ 24-hour; fine particles penetrate        │
  │          │            │ deep lung / cardiovascular effects;      │
  │          │            │ highest public health impact             │
  ├──────────┼────────────┼──────────────────────────────────────────┤
  │ PM₁₀     │ 150 μg/m³  │ 24-hour; coarse particles — upper       │
  │          │            │ respiratory effects                      │
  ├──────────┼────────────┼──────────────────────────────────────────┤
  │ O₃       │ 70 ppb     │ 8-hour (2015); secondary photochemical  │
  │ (ozone)  │            │ pollutant: NO₂ + VOC + sunlight →       │
  │          │            │ O₃; respiratory irritant; widespread    │
  │          │            │ nonattainment                            │
  ├──────────┼────────────┼──────────────────────────────────────────┤
  │ NO₂      │ 100 ppb    │ 1-hour; 53 ppb annual; combustion       │
  │          │            │ source; O₃ precursor; respiratory        │
  ├──────────┼────────────┼──────────────────────────────────────────┤
  │ SO₂      │ 75 ppb     │ 1-hour; coal combustion / smelting;     │
  │          │            │ acid rain precursor; respiratory         │
  ├──────────┼────────────┼──────────────────────────────────────────┤
  │ CO       │ 35 ppm     │ 1-hour; 9 ppm 8-hour; incomplete        │
  │          │            │ combustion; hemoglobin binding           │
  ├──────────┼────────────┼──────────────────────────────────────────┤
  │ Pb       │ 0.15 μg/m³ │ Rolling 3-month average; neurotoxin;   │
  │          │            │ near smelters and some industrial sites  │
  └──────────┴────────────┴──────────────────────────────────────────┘
```

**Attainment designations** are by county and by pollutant — a county can be in attainment
for PM₂.₅ but nonattainment for ozone simultaneously. Check both when siting data centers
or evaluating permits.

---

## Hazardous Air Pollutants (HAPs)

187 HAPs listed under CAA §112 — carcinogens, neurotoxins, reproductive toxins.

```
  HAP REGULATION MECHANISM

  NESHAP (National Emission Standards for Hazardous Air Pollutants)
  ├── Source category: EPA identifies category (e.g., "reciprocating
  │   internal combustion engines > 500 hp")
  ├── MACT standard: emission standard based on the average performance
  │   of the top 12% of existing sources in the category
  │   "Best performers define the floor"
  └── Residual risk review: after MACT implementation, EPA reviews
      whether residual cancer risk > 10⁻⁵ → may tighten further

  Key HAPs for data center operators:
  ├── Diesel particulate matter (DPM) from backup generators → RICE NESHAP
  ├── Formaldehyde from new building materials → IAQ concern
  ├── Lead near certain industrial sites → site selection concern
  └── Benzene / BTEX from fuel storage tanks → remediation trigger
```

---

## Atmospheric Dispersion

<!-- @editor[bridge/P2]: The Gaussian plume equation is a Green's function solution to the advection-diffusion PDE (∂C/∂t = D∇²C − u·∂C/∂x) for a point source under steady-state conditions. The Gaussian form follows directly from the fundamental solution to the diffusion equation. Any physicist or applied mathematician with MIT background will recognize this form immediately — but it's presented here as an empirical formula without naming its derivation from the diffusion PDE. The user calibration explicitly calls out "fate and transport → diffusion equations" as the key bridge. It should be named. -->
After emission, how does the pollutant spread? Gaussian plume modeling is the standard.

```
  GAUSSIAN PLUME MODEL

  C(x,y,z) = (Q / (2π·u·σ_y·σ_z)) · exp(-y²/(2σ_y²))
              × [exp(-(z-H)²/(2σ_z²)) + exp(-(z+H)²/(2σ_z²))]

  Where:
  C = concentration (μg/m³) at point (x,y,z)
  Q = emission rate (μg/s)
  u = mean wind speed at stack height (m/s)
  H = effective stack height = physical stack + plume rise (m)
  σ_y, σ_z = lateral and vertical dispersion coefficients (m)
              (functions of downwind distance x and stability class)

  PLUME RISE (Holland equation, buoyancy and momentum):
  Δh = (F_b / u) · (1.6·x^(2/3)/u)   [buoyancy-dominated]
  F_b = buoyancy flux = g·v_s·d_s²·ΔT / (4·T_s)

  STABILITY CLASSES (Pasquill-Gifford, A–F):
  ┌───────┬────────────────────────────────────────────────────────┐
  │ Class │ Conditions / Dispersion                                │
  ├───────┼────────────────────────────────────────────────────────┤
  │ A     │ Strong insolation, light wind — very unstable;        │
  │       │ large σ_y, σ_z → rapid dilution                       │
  ├───────┼────────────────────────────────────────────────────────┤
  │ B-C   │ Moderate insolation — moderately unstable             │
  ├───────┼────────────────────────────────────────────────────────┤
  │ D     │ Overcast / nighttime — neutral; most common class     │
  ├───────┼────────────────────────────────────────────────────────┤
  │ E-F   │ Nighttime stable/calm — very stable; plume stays      │
  │       │ tight; small σ_z → worst-case ground-level impact     │
  └───────┴────────────────────────────────────────────────────────┘
```

### Regulatory Dispersion Models

```
  AERMOD (EPA preferred model for most applications):
  ├── Boundary layer meteorology (AERMET preprocessor)
  ├── Terrain preprocessing (AERMAP)
  ├── Handles complex building downwash, complex terrain
  ├── Required for: PSD permits, NAAQS compliance analysis,
  │   Title V near-field impacts, NSR permits
  └── Input data: hourly meteorological data (5 years), source parameters
                  (stack height, diameter, exit velocity, temperature, Q)

  CALPUFF (complex terrain, long-range transport):
  ├── Lagrangian puff model — not steady state
  ├── Used for complex terrain, coastal flows, long-range Class I areas
  └── Computationally intensive; class II/III PSD applications

  SCREEN3 (quick screening tool):
  └── Conservative single-source screen; identifies if full AERMOD needed
```

---

## Stationary Source Control Technologies

### Particulate Control

```
  ELECTROSTATIC PRECIPITATOR (ESP)

  Mechanism: Corona discharge ionizes gas → charges particles → attracted
  to collecting plates → rapped off into hoppers

  Deutsch-Anderson equation:
  η = 1 - exp(-w·A/Q)
    η = collection efficiency
    w = drift velocity (particle migration to plate)
    A = collecting area
    Q = gas flow rate

  Efficiency: 99–99.9%+ for PM₁₀; less effective for very small (<0.1 μm)
  and very large (>10 μm) particles (Deutsch-Anderson has a minimum).
  Applications: coal power plants (fly ash), cement kilns, paper mills
  Pros: low pressure drop, handles high temperatures, no filter media
  Cons: high capital, resistivity sensitivity (sodium → low resistivity → bounce)

  FABRIC FILTER (BAGHOUSE)

  Mechanism: Particle cake on filter bags provides depth filtration
  Cleaning: pulse-jet (most common), reverse air, shaker
  Efficiency: >99.9% PM₁₀; 99%+ PM₂.₅
  Drawback: temperature limit (Nomex bags to ~190°C; fiberglass to ~260°C),
            moisture sensitivity, pressure drop
  Applications: pharmaceutical, food processing, industrial combustion
  Advantage over ESP: consistent efficiency regardless of particle resistivity
```

### SO₂ Control (Flue Gas Desulfurization)

```
  WET FGD (most common — coal plants):
  SO₂ + CaCO₃ + ½O₂ + H₂O → CaSO₄·2H₂O (gypsum) + CO₂
  Removal efficiency: 95–99%
  Product: wallboard-grade gypsum (byproduct revenue possible)
  Requires: large absorber tower, limestone slurry prep, wastewater treatment

  DRY SORBENT INJECTION (DSI):
  Inject sodium bicarbonate or trona into flue gas duct
  Removal efficiency: 50–85% (lower than wet FGD)
  Advantage: simple retrofit, lower capital — used at smaller plants
  or where wet FGD not cost-justified
  No liquid waste — dry product collected in baghouse
```

### NOₓ Control

```
  COMBUSTION CONTROLS (primary — prevent NOₓ formation):
  ├── Low-NOₓ burners: reduce peak flame temperature, stage combustion
  ├── Overfire air (OFA): incomplete combustion zone → thermal NOₓ suppression
  ├── Flue gas recirculation (FGR): dilutes O₂ in combustion zone
  └── Typical reduction: 30–50% vs. uncontrolled

  SELECTIVE CATALYTIC REDUCTION (SCR) — most effective post-combustion:
  4NO + 4NH₃ + O₂ → 4N₂ + 6H₂O   (ammonia injection + catalyst)
  Catalyst: V₂O₅ / TiO₂ (typical) or zeolite
  Operating temperature: 280–420°C for vanadium catalyst
  Removal efficiency: 85–95% NOₓ
  Reagent: anhydrous ammonia or urea → ammonia at injector
  Slip concern: unreacted NH₃ in flue gas — typically <5 ppm limit

  SELECTIVE NON-CATALYTIC REDUCTION (SNCR):
  No catalyst; urea or ammonia injection at 870–1100°C
  Removal efficiency: 30–60% (lower than SCR)
  Lower capital; useful when operating temperature window is accessible
```

### VOC Control

```
  THERMAL OXIDIZER (TO) / REGENERATIVE THERMAL OXIDIZER (RTO):
  VOC combustion: CₓHᵧ + O₂ → CO₂ + H₂O
  TO: 760–870°C for 0.5–1 sec residence → 95–99% DRE (destruction removal)
  RTO: heat recovery on ceramic saddles → thermal efficiency 90–97%;
       most cost-effective for large continuous VOC streams
  Catalytic oxidizer: lower temperature (300–450°C with Pt/Pd catalyst);
       lower fuel cost but catalyst fouling/poisoning risk

  CARBON ADSORPTION:
  VOC adsorbs on activated carbon (GAC or carbon fiber)
  Fixed-bed adsorber → saturation → regeneration (steam or hot N₂)
  VOC recovered in concentrated form (solvent recovery) or destroyed
  Best for high-concentration, high-value VOC (solvent recovery economics)
  Limitation: high humidity reduces capacity; strongly adsorbing VOCs
  may not fully desorb (ketones, esters — preferred over benzene for GAC)
```

---

## Emergency Generator Air Permits — Data Center Relevance

This is directly operational for Microsoft data centers.

```
  BACKUP DIESEL GENERATOR PERMITTING PATH

  Generator PTE (potential to emit) depends on:
  ├── Number of engines × kW rating
  ├── Emission factors (g/hp-hr for PM, NOₓ, CO, VOC, HAPs)
  │   Tier IV Final engines: NOₓ+NMHC 0.14 g/kW-hr; PM 0.02 g/kW-hr
  └── Annual operating hours (emergency use ≤200 hr/yr for EPA RICE NESHAP)

  RICE NESHAP (NESHAP for Reciprocating Internal Combustion Engines):
  ├── Stationary RICE ≥500 hp: must meet emission limits, NSPS
  ├── Emergency RICE: limited to 100 hr/yr non-emergency (testing/readiness)
  ├── Tier 4 Final: most stringent EPA new engine standard
  │   (required for new engines > 19 kW in non-emergency service)
  └── If operating hours exceed emergency threshold → not "emergency"
      engine → full NSR/PSD/Title V applicability kicks in

  NONATTAINMENT IMPACT:
  If data center is in ozone or PM₂.₅ nonattainment area:
  ├── NOₓ from generators contributes to ozone formation
  ├── Emission offset may be required if aggregated PTE > threshold
  └── Some jurisdictions limit number of generators or require DPF+SCR
      regardless of emergency classification

  PRACTICAL CONSTRAINT: Large hyperscale data centers (100+ MW)
  may have 40–80 diesel generators → aggregated PTE can exceed
  major source thresholds even with Tier 4 engines.
  This is a real siting constraint in Houston, Phoenix, LA basin.
```

---

## Indoor Air Quality

```
  KEY IAQ PARAMETERS

  CO₂:
  ├── Outdoor: ~420 ppm (2024, rising)
  ├── ASHRAE 62.1: 15 cfm/person minimum OA rate (the actual standard)
  ├── 1000 ppm common target (≈600 ppm above outdoor = ventilation proxy)
  ├── >2500 ppm: cognitive effects measurable (Harvard study)
  └── Data centers: very low occupancy → CO₂ rarely limiting

  Radon:
  ├── EPA action level: 4 pCi/L (equivalent to smoking ~8 cigarettes/day)
  ├── Sources: soil gas from radium-226 decay, uranium geology
  ├── Enters via foundation cracks, sumps, drain tiles
  ├── Measurement: short-term test (2–7 days), long-term test (>90 days)
  └── Mitigation: sub-slab depressurization (SSD) — most effective

  Formaldehyde:
  ├── From: pressed wood, flooring, insulation off-gassing
  ├── OSHA PEL: 0.75 ppm; NIOSH REL: 0.016 ppm
  └── California CARB Airborne Toxic Control Measure limits formaldehyde
      in composite wood products

  Volatile Organic Compounds (IAQ):
  ├── "Total VOC" (TVOC): not regulated federally; WHO guidelines
  ├── Source control (low-VOC products) is primary strategy
  └── Ventilation dilution and sorption filtration (activated carbon)
```

---

## GHG Monitoring and Reporting

```
  EPA GREENHOUSE GAS REPORTING PROGRAM (40 CFR Part 98)

  Threshold: facility with >25,000 MT CO₂e/yr direct emissions
  ├── Must register and report annually to EPA via e-GGRT
  ├── Covered source categories: stationary combustion, process emissions,
  │   fugitive emissions (SF₆ from electrical switchgear — directly
  │   relevant to data centers and electrical substations)
  └── Report due: March 31 for prior calendar year

  SCOPE 1 EMISSION SOURCES AT DATA CENTERS:
  ├── Emergency diesel generators (combustion — Part 98 Subpart C)
  ├── Natural gas for backup power / heating (Subpart C)
  ├── HFCs from refrigeration/HVAC (Subpart F)
  └── SF₆ from high-voltage switchgear (Subpart DD) — high GWP (23,500)

  MEASUREMENT METHODS:
  ├── CEMS (continuous emission monitoring systems): direct stack measurement;
  │   required for large combustion units; high capital but definitive
  ├── Fuel consumption × emission factors: standard for most facilities
  │   (EPA AP-42 emission factors, updated regularly)
  └── PEMS (predictive emission monitoring systems): real-time calculation
      from process parameters vs. measured stack concentration
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| New data center in ozone nonattainment area — generator permits | Check NOₓ PTE vs. NSR threshold; may need LAER + offsets; Tier 4 + SCR may be required |
| Air permit needed for existing 15 MW generator fleet? | Calculate PTE for all generators; if >100 tpy criteria pollutant → Title V; if <100 tpy → state minor permit |
| Model air impact for new large stack | AERMOD with 5 years of hourly met data; AERMET + AERMAP preprocessing |
| Which PM control is best for my application? | High-temp gas: ESP; fine particle collection + moisture: baghouse; <100 acfm: cartridge filter |
| Need to control SO₂ from large combustion | Wet FGD (>90% efficiency, gypsum byproduct); DSI for smaller or retrofit applications |
| NOₓ limit 0.05 lb/MMBtu from boiler | Low-NOₓ burner alone likely insufficient → SCR required at that level |
| Radon found at 6 pCi/L in building | Above action level → sub-slab depressurization mitigation; retest after installation |
| What triggers GHGRP reporting? | >25,000 MT CO₂e/yr from stationary combustion or process emissions at the facility |
| SF₆ from switchgear — how to minimize? | Gas-insulated switchgear (GIS) maintenance to minimize leaks; SF₆ recycling; transition to g³ (Novec/CO₂ blend alternatives) |

---

## Common Confusion Points

**NAAQS are ambient standards, not emission limits**: The NAAQS set the concentration
allowed in outdoor air at any point. Emission limits in permits are derived from dispersion
modeling to show the source contribution does not push ambient concentrations above NAAQS.
A source can legally exceed a NAAQS contribution if it shows through modeling that the
combined ambient concentration stays within the standard.

**PSD vs. NSR**: Prevention of Significant Deterioration (PSD) applies in attainment areas —
the goal is to prevent degradation below the NAAQS. New Source Review (NSR) applies in
nonattainment areas — the goal is to reach attainment. Same basic permitting gate
(major source threshold) but different control technology requirements (BACT vs. LAER)
and offset requirements (only NSR).

**Title V is not a technology standard**: Title V is an operating permit program — it
consolidates all existing permit conditions (NESHAP, NSPS, PSD, state rules) into one
document with monitoring, recordkeeping, and reporting. Getting a Title V permit does not
mean more controls; it means more administrative burden and public visibility.

**Emergency generator "hours limit"**: The 100 hr/yr non-emergency operational limit
under EPA RICE NESHAP is for testing and maintenance. Emergency hours are not limited.
But if a generator runs >100 hr/yr non-emergency, it loses its "emergency" classification
and becomes subject to much stricter standards. Data centers must track generator hours.

**Ozone is not directly emitted**: Ozone is a secondary pollutant — it forms in the
atmosphere when NOₓ and VOCs react in sunlight. Control strategies for ozone nonattainment
target NOₓ and VOC precursors, not ozone itself. A source can have zero direct ozone
emissions but still be a significant contributor to ozone nonattainment.
