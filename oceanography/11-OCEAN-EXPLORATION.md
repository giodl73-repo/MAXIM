# Ocean Exploration — Bathymetry Methods, Submersibles, ROVs, Argo Floats, Ocean Observing Systems

## The Big Picture

```
+===========================================================================+
|                  OCEAN OBSERVING SYSTEM LANDSCAPE                          |
|     From single-ship surveys to globally integrated sensor networks       |
+===========================================================================+
|                                                                           |
|  IN SITU (wet)                          REMOTE SENSING (dry)              |
|  ──────────────                         ─────────────────────             |
|  Ships/CTD casts   Ships of opportunity Altimetry (Jason/Sentinel)        |
|  Argo floats       Fixed moorings       SST (AVHRR, MODIS)                |
|  Gliders           Bottom observatories Ocean color (MODIS, SeaWiFS)      |
|  AUVs/ROVs         Drifters             SAR (surface roughness, waves)    |
|  Wave buoys        Tide gauges          Gravity (GRACE — water mass)       |
|                                                                           |
|  DEPTH COVERAGE:                                                          |
|  Surface:   drifters, wave buoys, saildrones, ships                       |
|  0–2000 m:  Argo (4000+ floats), CTD casts, gliders                      |
|  >2000 m:   Deep Argo, deep moorings, bottom landers                      |
|  Seafloor:  cabled observatories (OOI, NEPTUNE), ROVs, landers            |
+===========================================================================+
```

---

<!-- @editor[bridge/P2]: No old-world bridge — sonar/multibeam is pulse-echo radar applied underwater (same time-of-flight → distance conversion); ADCP Doppler shift is the same principle as police radar guns; satellite altimetry is radar ranging from orbit; data assimilation (EnKF, 4D-Var) is the same Kalman filtering used in GPS navigation and control theory -->

## Bathymetry Methods

### Historical Methods

```
LEAD LINE (pre-1920s):
  Weighted line lowered to bottom → count out length → depth recorded
  HMS Challenger: 492 deep soundings over 3.5-yr voyage
  Limitation: slow (~hours per sounding), error-prone, limited coverage

SINGLE-BEAM ECHO SOUNDER (1920s–present):
  Acoustic pulse (sonar) transmitted downward
  Travel time to bottom and back → depth = (c × TWT)/2
  c ≈ 1500 m/s in seawater
  Invention: first used commercially 1924 (Germany, ATLAS echo sounder)
  Creates single track along ship's course

SWATH BATHYMETRY / MULTIBEAM SONAR (1960s–present):
  Multiple acoustic beams fanned across track (up to 120° swath)
  Each ping: measures 256–512 depth points simultaneously
  Swath width: ~3–5× water depth (deeper = wider swath)
  Resolution: ~1–10 m in shallow water, ~50–100 m in deep ocean
  Speed: maps ~50–100 km² per hour at 12-knot ship speed
```

### Coverage Problem

```
HOW MUCH OCEAN IS MAPPED?

  High resolution direct mapping (satellite-validated multibeam):
    ~26% of ocean floor mapped at <1 km resolution (as of 2023)
    Seabed 2030 project: aims for 100% by 2030 (very ambitious)

  Satellite altimetry-derived bathymetry (Smith & Sandwell, GEBCO):
    "Maps" 100% of ocean floor — but at ~3–5 km resolution
    Method: gravity anomalies → crustal mass variations → topography
    Sufficient for large features (ridges, trenches), not for fine structure

  IMPLICATION:
    ~74% of deep ocean floor less well-mapped than Mars surface
    Mars: global 100 m resolution from MOLA laser altimeter
    Ocean: most areas: 3–5 km resolution or just ship tracklines

GEBCO (General Bathymetric Chart of the Oceans):
  Global bathymetric standard, compiled from all available data
  Current version: 15-arc-second grid (~500 m resolution)
  Actually reflects combined satellite + ship data
  Seabed 2030: international effort to compile all data into one database
```

---

## Acoustic Methods in Detail

```
SONAR VARIANTS:
  Single-beam: depth profile along track
  Multibeam: full swath coverage per ping, color-coded depth maps
  Sidescan sonar: acoustic backscatter image of seafloor texture
    (not depth — texture: sandy vs. rocky vs. sediment-covered)
    Resolution: cm-scale in shallow water; used for archaeology
  Sub-bottom profiler: lower frequency (1–10 kHz) penetrates sediment
    Images sub-surface layers to 10–100 m below seafloor
    Used for: sediment stratigraphy, buried pipelines, archaeological sites

ACOUSTIC DOPPLER CURRENT PROFILER (ADCP):
  Emits acoustic pulses, measures Doppler shift from backscatterers (plankton, bubbles)
  → current velocity profiles (not just surface) at multiple depths
  Typical range: 50–1000 m depending on frequency (lower freq = deeper range)
  Mounted on ship hull, moored, or lowered
  Also: bottom-mounted ADCP looking up through water column

LONG-RANGE ACOUSTICS (SOFAR):
  See 01-OCEAN-PHYSICS.md — SOFAR channel
  RAFOS floats: receive SOFAR pulses from moored sound sources → Lagrangian tracking
  Acoustic thermometry: travel time of sound pulses across basin → average temperature
    Heard Island Feasibility Test (1991): sound from Heard Island detected globally
    Climate change monitoring: ocean warming increases sound speed → travel time decreases
```

---

## Submersibles

### Crewed Research Submersibles

```
ALVIN (WHOI):
  Operational since 1964 (multiple hull replacements, essentially rebuilt)
  Current depth rating: 4,500 m (new titanium hull → 6,500 m by ~2024)
  Famous dives: Galapagos Rift (1977, first hydrothermal vents),
                RMS Titanic (1986, 3800 m depth)
  ~5000 dives total
  Crew: 2 scientists + 1 pilot, 9-hr maximum dive

NAUTILE (IFREMER, France): 6,000 m
MIR I & II (Russia): 6,000 m — used in James Cameron's Titanic film
SHINKAI 6500 (JAMSTEC, Japan): 6,500 m — deepest crewed submersible after Trieste/Limiting Factor
LIMITING FACTOR (Inkfish/Caladan Oceanic):
  Full ocean depth rated (11,000 m) — commercial vessel
  Victor Vescovo descends: all 5 ocean deeps in 2018–2019
  Challenger Deep: 10,928 m (deepest crewed dive since Trieste 1960)

BATHYSCAPHE TRIESTE (1960):
  Jacques Piccard + Don Walsh: 10,916 m, January 23, 1960
  First humans to reach the deepest point — not repeated for 52 years
```

### Remotely Operated Vehicles (ROVs)

```
ROV OPERATING PRINCIPLE:
  Surface ship (control room) ────────────────────────────────►
                                 Tether (umbilical): power + comms
                                 ────────────────────────────────────►
                                                      ROV (subsea)
                                                      cameras, manipulators,
                                                      sensors, sample containers

TETHER:
  Delivers power (typically 50–200 kW electrical)
  Returns real-time HD video, sensor data
  Length: 100 m to 10+ km for ultra-deep ROVs
  Fiber-optic core for high-bandwidth video

MAJOR DEEP-SEA ROVS:
  Jason/Jason II (WHOI): 6,500 m — US academic workhorse
  Hercules (Ocean Exploration Trust/E/V Nautilus): 4,000 m
  SuBastian (Schmidt Ocean Institute/R/V Falkor): 4,500 m
  ROPOS (Canada): 5,000 m
  Victor 6000 (IFREMER): 6,000 m
  Kaiko (JAMSTEC): 11,000 m — reached Challenger Deep 1995

ADVANTAGES OVER CREWED:
  Unlimited bottom time (no life support, CO₂ buildup, crew fatigue)
  No risk to human life
  Can work in highly toxic environments (H₂S-rich vent fluids)
  Real-time streaming — larger scientific audience
  Easier to work multiple ROVs from one ship
```

### Autonomous Underwater Vehicles (AUVs)

```
AUV CLASSIFICATION:

SURVEY AUVs:
  Torpedo-shaped, propeller-driven
  Speed: 1–2 m/s, range: 50–200 km on batteries
  Carries: multibeam sonar, sidescan, sub-bottom profiler
  Use: detailed bathymetric mapping of small areas
  Example: ABE, Sentry (WHOI), Hugin (Kongsberg), Autosub (NOC)

OCEAN GLIDERS:
  Buoyancy-driven (no propeller)
  Pitch controlled by internal mass shift → saw-tooth path through water
  Speed: ~0.25 m/s, range: 1,000–5,000 km on batteries
  Duration: weeks to months per deployment
  Carries: CTD (temperature, salinity, depth), O₂, chlorophyll, sometimes ADCP
  Use: mesoscale transects, long-term monitoring, hurricane surveys
  Types: Seaglider (UW), Spray (Scripps/SIO), Slocum (Teledyne)

SAILDRONE:
  Wind-propelled surface vehicle (wing sail)
  Solar-powered sensors, satellite comms
  Duration: up to 12+ months
  Covers: surface meteorology, SST, O₂, CO₂, waves
  New capability: hurricane surveys at surface (survived Cat-4 interior, 2021)

WAVE GLIDER (Liquid Robotics):
  Surface float + submerged glider connected by tether
  Wave energy converted to forward propulsion
  Long endurance (months), low energy use
```

---

## Argo Float Program

```
ARGO CONCEPT:
  Autonomous profiling floats, drift freely with ocean currents
  Mission: global ocean temperature + salinity profiles to 2000 m
  Launched: 2000 pilot; global array (~3000 floats) by 2007

ARGO FLOAT OPERATING CYCLE:
  ┌─────────────────────────────────────────────────┐
  │  Surface: GPS fix + data transmission (6-12 hr) │
  │       │                                          │
  │       ▼ Descend to "parking depth" (1000 m)     │
  │  Drift at parking depth (9–10 days)              │
  │       │                                          │
  │       ▼ Descend to profiling depth (2000 m)      │
  │  Ascend slowly through water column (6–10 hr)    │
  │  Measure T + S continuously (CTD sensor)         │
  │       │                                          │
  │       ▼ Return to surface                        │
  │  Transmit profile via Iridium satellite          │
  │       Loop back to park depth                    │
  └─────────────────────────────────────────────────┘

  Cycle duration: 10 days (standard)
  Float lifespan: ~3–5 years (battery limited)
  Each float cost: ~$15,000–$25,000

ARGO NETWORK (2024):
  ~3,900 active floats globally
  >700 measurements per day
  3.4 million profiles in database (launched through 2024)
  Geographic coverage: all major ocean basins

EXTENSIONS:
  Deep Argo: 6,000 m (uses different pump technology, larger pressure housing)
    ~200 floats operational as of 2024
  BGC-Argo (Biogeochemical): adds O₂, pH, NO₃, chl, PAR, backscatter
    ~600+ floats; tracks biological and chemical properties
  Polar Argo: ice-tethered profilers (ITP) for Arctic under-ice sampling
```

---

## Fixed Moorings and Bottom Observatories

```
SURFACE MOORING:
  Buoy at surface: meteorology (wind, T, humidity, precip), SST, waves
  Subsurface instruments: CTD, ADCP, current meters at multiple depths
  Anchored by chain/rope to seafloor anchor
  Examples: TAO/TRITON array (equatorial Pacific/Indian, ~70 moorings — El Niño monitoring)
            PIRATA array (equatorial Atlantic)
            OceanSITES: global network of ~400 time-series moorings

RAPID MOORING ARRAY (26°N):
  Monitors AMOC continuously since 2004
  ~40 moorings across Atlantic: Western Boundary, Eastern Boundary, mid-basin
  Measures volume transport of deep western boundary current + surface layer
  Key result: AMOC ~17–18 Sv mean; ~15% decline observed 2004–2024 (debated)

CABLED SEAFLOOR OBSERVATORIES:
  NEPTUNE Canada (now Ocean Networks Canada):
    800 km fiber-optic cable, Juan de Fuca tectonic plate
    Provides power + broadband comms to instruments on seafloor
    Instruments: seismometers, pressure sensors, cameras, CTDs, hydrophones
  OOI (Ocean Observatories Initiative, NSF):
    Multiple arrays: Pioneer (NW Atlantic Shelf), Irminger Sea, Southern Ocean
    Combination of moored + profiler + glider systems
  EMSO (European Multidisciplinary Seafloor and water column Observatory):
    Network across European seas and Atlantic

BOTTOM LANDERS:
  Instrument platform lowered to seafloor, works autonomously
  No tether — free-fall deployment
  Recovery: acoustic release command → drops weights → buoyantly ascends
  Duration: weeks to months
  Carries: sediment trap, ADCP, camera, chemical sensors
  Used in: hadal zones (up to 11 km depth), remote areas
```

---

## Remote Sensing from Space

```
SATELLITE OCEANOGRAPHY SUITE:

ALTIMETRY (sea surface height):
  Radar pulse to ocean surface, measures return time
  Resolution: ~7 cm vertical, ~7 km spatial, 10-day repeat
  Products: sea surface height anomaly (SSHA) → geostrophic currents, eddies,
            El Niño state, sea level rise trend
  Satellites: TOPEX/Poseidon (1992), Jason-1/2/3, Sentinel-6 Michael Freilich

SEA SURFACE TEMPERATURE (SST):
  Infrared radiometers: AVHRR (since 1978), MODIS (2000–present), VIIRS
  Resolution: 1 km, multiple overpasses per day
  Limitation: clouds block IR
  Microwave SST (AMSR, WindSat): cloud-penetrating, ~25 km resolution

OCEAN COLOR / CHLOROPHYLL:
  Reflected sunlight in visible wavelengths
  Chlorophyll absorption at 443 nm → [Chl] from ocean color algorithm
  SeaWiFS (1997–2010), MODIS-Aqua (2002–), PACE (2024–)
  Used for: primary production, bloom monitoring, harmful algal blooms

SEA ICE:
  Passive microwave: distinguish ice from water, measure concentration
  SSMI/SSMIS (1979–present): ~25 km resolution, daily global maps
  Active SAR (Sentinel-1): 10–100 m resolution, ice type discrimination

SURFACE WIND STRESS:
  Scatterometers: measure Bragg-scattering from wind-roughened surface
  QuikSCAT (1999–2009), ASCAT, HY-2B
  Key input for: forcing ocean circulation models, operational forecasting
  ~25 km resolution, 2-day repeat (global coverage)

GRAVITY / OCEAN MASS:
  GRACE/GRACE-FO: measures changes in Earth's gravity field (distance between two satellites)
  Products: ocean bottom pressure changes, ice mass loss, groundwater
  ~300 km resolution, monthly
  Used to: track AMOC variability, ice sheet mass balance, groundwater depletion
```

---

## Ocean Modeling

```
OCEAN GENERAL CIRCULATION MODELS (OGCM):
  Solve Navier-Stokes + thermodynamics + salt conservation on ocean grid
  Numerical schemes: finite difference, finite element, spectral

  RESOLUTION CLASSIFICATION:
    1° grid (110 km): "low resolution" — misses mesoscale eddies
    0.25° grid (28 km): "eddy-permitting" — partially resolves eddies
    0.1° grid (11 km): "eddy-resolving" — resolves mesoscale eddies
    0.01° grid: experimental — approaching submesoscale

  MAJOR OPERATIONAL MODELS:
    NEMO (Nucleus for European Modelling of the Ocean): European standard
    MOM6 (GFDL/NOAA): US academic standard
    HYCOM (HYbrid Coordinate Ocean Model): US Navy operational
    ROMS (Regional Ocean Modeling System): regional, high-resolution studies

  COUPLED MODELS:
    Ocean + atmosphere + sea ice → Earth System Models (ESMs)
    Used for IPCC projections, seasonal forecasting, climate attribution

  DATA ASSIMILATION:
    Combine model prediction with observations (Argo, altimetry, SST)
    → Ocean state estimate (4D-Var, EnKF methods — same as weather data assimilation)
    Products: HYCOM analysis (operational), ECCO (research reanalysis)
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What percentage of ocean floor is well-mapped? | ~26% by multibeam (2023); rest only at 3–5 km resolution from satellite gravity |
| How does multibeam sonar work? | Fan of acoustic beams measures depth at multiple angles simultaneously, swath = ~3–5× water depth |
| What does Argo measure? | Temperature and salinity profiles 0–2000 m (BGC-Argo adds O₂, pH, nutrients, chlorophyll) |
| What is the Argo cycle? | Park at 1000 m (10 days) → descend to 2000 m → ascend profiling → surface → transmit → repeat |
| What is RAPID? | Array of moorings at 26°N monitoring AMOC volume transport since 2004 |
| What does altimetry measure? | Sea surface height (SSH) → geostrophic currents, SSHA, sea level rise trend |
| What is an ocean glider? | Buoyancy-driven AUV with no propeller; weeks-long endurance at 0.25 m/s |
| What is a cabled seafloor observatory? | Fiber-optic network delivering power + comms to seafloor instruments (OOI, NEPTUNE) |

---

## Common Confusion Points

**Argo floats vs. drifters**: Argo floats are profiling (dive to 2000 m, measure CTD, surface to transmit). Drifters (SVP drifters, CODE drifters) are surface-drifting buoys tracking ocean currents at the surface (15 m drogue depth). Both free-drifting, completely different depth ranges and measurements.

**ROV vs. AUV**: ROV = tethered (cable to ship), controlled in real-time, unlimited power. AUV = autonomous (no tether), pre-programmed, battery-limited. ROVs are better for detailed scientific work; AUVs better for large-area surveys. The tether gives ROVs unlimited bottom time and power but limits range from ship.

**Altimetry doesn't measure depth directly**: Satellite altimetry measures distance from satellite to sea surface. This gives sea surface HEIGHT relative to a geoid reference — not ocean depth. Seafloor bathymetry is derived from GRAVITY anomalies (a different measurement) not altimetry return time.

**Model resolution and skill**: Higher resolution isn't always better for all applications. A 1° model run for 1000+ years of climate simulation may give better climate statistics than a 0.1° model run for 50 years. Resolution choice involves compute budget tradeoffs. Eddies matter for some processes (heat transport, tracer mixing) but average out for others (large-scale thermohaline patterns) over long timescales.

**Real-time ocean observing is still very sparse**: Despite Argo, TAO/TRITON, satellites, large parts of the ocean (Southern Ocean, Arctic under-ice, all depths > 2000 m, most of the seafloor) are still poorly observed. Weather has hourly global surface data from thousands of stations + radiosondes + satellites. Ocean state estimation is fundamentally more uncertain — vast volume, difficult access, sparse observations.

<!-- @editor[content/P3]: CTD instrument absent — the CTD (Conductivity-Temperature-Depth) rosette is the most fundamental oceanographic instrument and never explained in this guide; deserves a brief section covering the rosette package, Niskin bottles, and cast workflow -->
