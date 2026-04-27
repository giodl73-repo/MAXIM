# Hydrology — Overview: Hydrological Cycle, Global Freshwater Inventory, Field Branches

## The Big Picture

```
+===========================================================================+
|                    THE GLOBAL HYDROLOGICAL CYCLE                          |
|          Water movement through atmosphere, land, and ocean               |
+===========================================================================+
|                                                                           |
|              ATMOSPHERE (~13,000 km³, ~0.001%)                           |
|             ↗ Evaporation     Precipitation ↘                            |
|           505,000 km³/yr         Rain/Snow                               |
|               ↑                     ↓                                    |
|    OCEAN                          LAND SURFACE                           |
|   (1,335,000,000 km³             Interception                            |
|       97.5% of all water)        Infiltration ──► SOIL MOISTURE          |
|                                  Runoff ─────► RIVERS & STREAMS          |
|                                     ↓                                    |
|                              GROUNDWATER RECHARGE                        |
|                              AQUIFERS (30,100,000 km³)                   |
|                                     ↓                                    |
|                              Baseflow / Springs                          |
|                                     ↓                                    |
|                              Back to rivers → ocean                      |
|                                                                           |
+===========================================================================+
|  ANNUAL FLUXES (approximate):                                             |
|  Ocean evaporation:  ~436,000 km³/yr                                      |
|  Land evapotranspiration: ~69,000 km³/yr                                  |
|  Ocean precipitation: ~391,000 km³/yr                                     |
|  Land precipitation: ~111,000 km³/yr                                      |
|  River discharge to ocean: ~42,000 km³/yr                                 |
|  Net P-E imbalance drives freshwater from land to ocean                   |
+===========================================================================+
```

---

## Global Freshwater Inventory

```
FRESHWATER DISTRIBUTION:

  Total water on Earth: ~1,385,000,000 km³

  Saltwater (oceans + saline lakes): 97.5% → 1,350,000,000 km³
  Freshwater: 2.5% → 35,000,000 km³

  FRESHWATER BREAKDOWN:
    Ice caps / glaciers / snow:    68.7%    24,064,000 km³
    Groundwater:                   30.1%    10,530,000 km³
    Surface water + other:          0.9%       315,000 km³
      ├─ Lakes:          87%            274,000 km³
      ├─ Swamps/wetlands: 11%            32,000 km³
      └─ Rivers:          2%              2,120 km³
    Soil moisture:                  0.05%    16,500 km³
    Atmosphere:                     0.04%    12,900 km³
    Biota (living organisms):       0.003%     1,100 km³

  ACCESSIBLE FRESHWATER (practically exploitable):
    ~200,000 km³ in lakes, rivers, shallow groundwater
    ~0.6% of all freshwater, ~0.015% of all water on Earth
```

---

## Water Residence Times

```
COMPONENT               RESIDENCE TIME        IMPLICATIONS
──────────────────────────────────────────────────────────────────
Atmosphere              ~8–10 days            Fast turnover; rainfall patterns
Soil moisture           Weeks–months          Controls plant availability
Rivers                  Weeks                 Rapid response to precipitation
Lakes (small)           Months–years          Moderate response to loading
Lakes (large)           Decades–centuries     Great Lakes: ~200 yr (Lake Ontario)
Groundwater (shallow)   Months–decades        Recoverable; responds to pumping
Groundwater (deep)      Centuries–millennia   Fossil water; non-renewable on human timescale
Antarctic ice sheet     100,000+ years        Long-term archive; slow response
Ocean deep water        1,000–2,000 years     Thermohaline timescale

HYDROLOGICAL CYCLE RENEWAL RATES:
  River water renewed every ~16 days by precipitation/runoff
  Soil moisture every ~1–2 months
  Shallow groundwater every ~30–300 years
  Deep groundwater every 1,000–10,000 years
  → These timescales determine recovery time from contamination and drought
```

---

## The Hydrological Cycle — Key Fluxes

```
PRECIPITATION:
  Global mean: ~1000 mm/yr land surface (wide range: <25 mm/yr desert to >11,000 mm/yr tropics)
  Forms: rain, snow, sleet, hail, fog drip (interception of fog by vegetation)

EVAPOTRANSPIRATION (ET):
  Combined: soil evaporation + plant transpiration
  Potential ET (PET): energy-limited, ignores water availability
  Actual ET (AET): water-limited in dry climates; energy-limited in wet
  AET ~ 60% of global land precipitation (remainder becomes runoff/recharge)

  Penman-Monteith equation (FAO standard):
    λET = (Δ(R_n - G) + ρ_a c_p (e_s - e_a)/r_a) / (Δ + γ(1 + r_s/r_a))
    where λ = latent heat of vaporization, R_n = net radiation, r_a = aerodynamic resistance
    r_s = surface (canopy) resistance, e_s - e_a = vapor pressure deficit

RUNOFF:
  Quick flow (direct runoff): rain excess → overland flow (Hortonian) or
    saturation excess → channel rapidly
  Baseflow: groundwater discharge sustaining river between storm events
  Runoff ratio: R/P (runoff/precipitation) — varies from 0.1 (arid) to 0.8 (wet mountains)
```

---

## Field Branches

| Branch | Core Focus | Key Methods |
|--------|-----------|-------------|
| Surface water hydrology | Rainfall-runoff, streamflow, floods | Stream gauges, rainfall-runoff models |
| Groundwater hydrology (hydrogeology) | Aquifers, wells, Darcy's law, solute transport | Wells, pump tests, tracer tests |
| Watershed hydrology | Catchment water balance, landscape routing | DEM analysis, hydrological models |
| Engineering hydrology | Design floods, dams, levees, urban drainage | Frequency analysis, HEC-RAS/HMS models |
| Hydrometeorology | Precipitation, evaporation, snow | Weather radar, snow surveys, satellites |
| Ecohydrology | Plant-water interactions, transpiration | Eddy covariance flux towers, isotope tracers |
| Hydroclimatology | Drought, climate-hydrology coupling | PDSI, SPI, paleoclimate proxies |
| Water quality hydrology | Contaminant transport, treatment | Chemical sampling, sorption models |

---

## Water Budget at Different Scales

```
CATCHMENT WATER BALANCE:
  P = ET + ΔS + Q

  P  = precipitation
  ET = evapotranspiration
  ΔS = change in storage (groundwater + soil moisture + snow)
  Q  = streamflow (discharge)

  On multi-year average: ΔS ≈ 0 (storage doesn't trend up or down)
  → P = ET + Q (long-term balance)
  → Runoff = P - ET
  → Aridity index: PET/P: >1 = arid, <1 = humid

BUDYKO FRAMEWORK:
  AET/P = f(PET/P)  (Budyko curve)

  Limits:
    AET ≤ P (can't evaporate more than it rains — water-limited arid end)
    AET ≤ PET (can't exceed potential — energy-limited humid end)

  Most catchments fall near the Budyko curve:
    AET/P ≈ 1 - exp(-PET/P) + ... (various functional forms proposed)

  Deviations from Budyko curve indicate groundwater mining, inter-basin transfers,
  or measurement error
```

---

## How the Subdirectories Connect

```
00-OVERVIEW ──── Hydrological cycle, freshwater inventory (this file)

01-PRECIPITATION-RUNOFF ──── Rainfall-runoff, infiltration, SCS method, unit hydrograph
        │
        ▼
02-WATERSHED-ANALYSIS ──── DEM analysis, watershed delineation, Strahler order, network
        │
        ├──► 03-GROUNDWATER ──── Darcy's law, aquifers, well hydraulics
        │
        └──► 04-RIVERS-FLOODPLAINS ──── Channel morphology, Manning, sediment transport

05-LAKES-WETLANDS ──── Stratification, eutrophication, peatlands, carbon

06-WATER-ENGINEERING ──── Dams, reservoirs, levees, urban drainage design

07-WATER-QUALITY ──── Contaminant transport, treatment trains, WQI

08-FLOODS-DROUGHTS ──── Frequency analysis, return periods, PDSI/SPI, early warning

09-GLOBAL-FRESHWATER ──── Scarcity, virtual water, transboundary rivers, aquifer depletion
```

---

## CS and Engineering Bridges

The hydrological cycle maps cleanly to CS and engineering abstractions:

```
HYDROLOGY CONCEPT             CS / ENGINEERING EQUIVALENT
──────────────────────────────────────────────────────────────────────────────
Water balance (P = ET+Q+ΔS)   Conservation law / bookkeeping invariant
                               Same structure as charge balance in a circuit,
                               mass balance in a reactor, or packet counts in
                               a router (in = out + Δstored)

Drainage network              Directed acyclic graph (DAG)
  Watershed                     → connected component rooted at outlet
  Tributary confluence          → node merge (two edges → one)
  Strahler stream order         → level in a binary-merging tree
  Flow accumulation             → topological sort, then upstream cell count
  Watershed delineation         → BFS/DFS on reversed flow-direction grid

Unit hydrograph (UH)          Linear time-invariant (LTI) system
  Catchment impulse response    → Q = UH ⊛ P_excess (discrete convolution)
  Multi-event superposition     → same math as FIR filter applied to signal

Groundwater flow (Darcy)      Diffusion PDE (heat equation)
  Hydraulic head gradient       → potential gradient (voltage)
  Darcy flux = -K ∇h            → Ohm's law (J = -σ ∇V)
  Aquifer transmissivity T      → sheet conductance; well network = resistor mesh

Kriging (rain gauge interp.)  Gaussian process regression
  Variogram model               → covariance kernel (RBF, Matérn)
  Kriging estimate              → GP posterior mean (same closed-form solution)

Flood frequency analysis      Extreme value theory (EVT)
  GEV / GPD distributions       → tail distributions for max-stable processes
  Return period T               → 1/P(exceedance) per year; not "one per T years"

Water balance model           Discrete-time state-space model
  ΔS = f(P, ET, Q, ...)         → state transition equation; Kalman filtering
                                   used directly for data assimilation
```

## Cross-Library Connections

| Topic | Covered elsewhere |
|-------|-------------------|
| Climate forcing of hydrological cycle | natural-sciences/14-ATMOSPHERE-CLIMATE.md |
| River delta morphology | oceanography/09-COASTAL-SYSTEMS.md |
| Dam and levee structural design | structural/, construction-materials/ |
| Groundwater contamination remediation | environmental engineering principles |
| Drought and climate variability | paleontology/10-PALEOCLIMATOLOGY.md |
| Isotope tracers in water | natural-sciences/01-ATOMIC-QUANTUM.md |
| Water scarcity governance | economics/ |
| PDEs for groundwater flow | mathematics/ (PDEs) |

---

## Decision Cheat Sheet

| You want to understand... | Go to |
|---------------------------|-------|
| How rain becomes streamflow; infiltration; SCS CN method | 01-PRECIPITATION-RUNOFF |
| Watershed delineation from DEMs; Strahler order; drainage patterns | 02-WATERSHED-ANALYSIS |
| Darcy's law; confined vs. unconfined aquifers; pumping wells | 03-GROUNDWATER |
| River channel shape; Manning equation; meanders; sediment | 04-RIVERS-FLOODPLAINS |
| Lake stratification; eutrophication; wetland carbon | 05-LAKES-WETLANDS |
| Dam types; reservoir routing; levee design; stormwater | 06-WATER-ENGINEERING |
| Contaminant plumes; water treatment train; WQI | 07-WATER-QUALITY |
| 100-year flood; return period; Palmer Drought Index | 08-FLOODS-DROUGHTS |
| Global water scarcity; transboundary rivers; aquifer depletion | 09-GLOBAL-FRESHWATER |

---

## Common Confusion Points

**Groundwater is NOT the same as an underground lake**: Most aquifers are porous rock (sandstone, gravel) with water filling the pore spaces — not open underground caves. Karst aquifers (limestone) do have open conduits, but they're the exception. Groundwater moves through pores at velocities of centimeters to meters per DAY, not rivers.

**Evaporation vs. evapotranspiration**: Evaporation is from open water and bare soil. Transpiration is from plant stomata (leaves). Evapotranspiration (ET) is the combined total from vegetated land surfaces. In forested catchments, transpiration >> evaporation — trees are major water consumers. Deforestation typically increases runoff because you remove transpiration.

**Streamflow units**: Discharge Q = volume per time = m³/s (cumecs) or ft³/s (cfs). Yield = mm of runoff depth over catchment area (volume normalized by area). 1 mm of runoff over 1 km² = 1000 m³ = ~11.6 L/s continuous for 24 hours. Converting mm/day to m³/s: Q(m³/s) = P(mm/day) × A(km²) / 86.4

**Water table is not a flat plane**: The water table follows topography (at reduced amplitude). It rises under hills and falls toward streams. The slope of the water table drives groundwater flow toward streams and rivers. Springs emerge where the water table intersects the ground surface.

**Consumptive use vs. diversion**: Agricultural water diversion from rivers is not consumed 100% — return flows go back to rivers or infiltrate. Consumptive use is the fraction that actually evaporates or transpires (does not return). Irrigation is ~70% consumptive use; municipal water is ~20–30% consumptive (the rest goes back to rivers via wastewater treatment).
