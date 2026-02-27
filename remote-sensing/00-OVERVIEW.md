# Remote Sensing — Landscape and Taxonomy

*Seeing from afar. Measuring what you cannot touch.*

## The Big Picture

Remote sensing acquires information about a target without physical contact. A sensor collects energy — reflected sunlight, emitted thermal radiation, or backscattered radar pulses — and from that signal alone reconstructs what the surface looks like, what it is made of, and how it is changing. The entire field is organized along three axes: **what energy you measure** (EM spectrum band), **where you measure from** (platform), and **what question you are answering** (application domain).

```
                        THE REMOTE SENSING LANDSCAPE
    ┌─────────────────────────────────────────────────────────────────┐
    │                        EM SPECTRUM BANDS                        │
    │  VIS    NIR    SWIR    TIR    Passive μW    Active Radar/LiDAR │
    │ 0.4-0.7 0.7-1.3 1.3-2.5 8-14μm  1mm-1m      1mm-1m (coherent)│
    └────────┬──────┬──────┬──────┬──────────┬──────────┬─────────────┘
             │      │      │      │          │          │
    ┌────────┴──────┴──────┴──────┴──────────┴──────────┴─────────────┐
    │                         PLATFORMS                                │
    │                                                                  │
    │  Ground        UAV/Drone     Airborne       LEO Sat    GEO Sat  │
    │  (surface)     (50-500m)     (1-15km)     (400-800km) (35,786km)│
    │  point meas    field scale   regional     continental  full disk │
    │  continuous    on-demand     on-demand     days-weeks   minutes  │
    └────────┬──────┬──────┬──────┬──────────┬──────────┬─────────────┘
             │      │      │      │          │          │
    ┌────────┴──────┴──────┴──────┴──────────┴──────────┴─────────────┐
    │                    PROCESSING PIPELINE                           │
    │  Raw DN → Radiometric Cal → Geometric Correction → Ortho       │
    │       → Atmospheric Correction → Analysis-Ready Data (ARD)      │
    └────────┬──────┬──────┬──────┬──────────┬──────────┬─────────────┘
             │      │      │      │          │          │
    ┌────────┴──────┴──────┴──────┴──────────┴──────────┴─────────────┐
    │                   APPLICATION DOMAINS                            │
    │                                                                  │
    │  LAND           OCEAN          ATMOSPHERE        ICE/CRYO       │
    │  crop maps      SST            aerosol depth     sea ice conc   │
    │  deforestation  chlorophyll    ozone profiles    ice sheet mass │
    │  urban growth   oil spills     cloud height      glacier vel    │
    │  soil moisture  ocean wind     water vapor       snow cover     │
    │  burn severity  bathymetry     temperature       permafrost     │
    └─────────────────────────────────────────────────────────────────┘
```

Read this diagram top-down: pick your **band** (what physics you exploit), choose your **platform** (where you observe from), run through the **processing pipeline** (remove instrument and atmospheric artifacts), and produce an **information product** for a specific domain.

---

## Passive vs. Active: The Core Split

Every sensor falls into one of two families, determined by where the energy comes from.

```
PASSIVE                                    ACTIVE
───────────────────────────────────────────────────────────────────
Energy source   Sun or Earth's own heat    Sensor's own transmitter
Signal path     Sun → surface → sensor     Sensor → surface → sensor
                (shortwave) or             (radar pulse or laser)
                surface → sensor (thermal)
Night capable?  Thermal only (TIR)         Yes — carries own illumination
Cloud capable?  No (optical); yes (μW)     SAR: yes. LiDAR: mostly no
Spectral info   Many bands (10-285)        Few "bands" but phase + polarization
Spatial detail  Sub-meter (commercial)     SAR: 1-100m. LiDAR: cm-level
3D capable?     Stereo photogrammetry      LiDAR directly; InSAR for cm-scale Δh
Strengths       Color, chemistry, temp     Structure, deformation, all-weather
Free data       Landsat, Sentinel-2, MODIS Sentinel-1 SAR (free, global)
Expensive data  LiDAR airborne surveys     WorldView 0.3m commercial optical
```

**The bridge to distributed systems**: Passive sensors are like **log collectors** — they record whatever the environment emits (reflected sunlight = application logs). Active sensors are like **synthetic probes** — they inject a signal and measure the response (radar pulse = health check ping). Both approaches have value; the choice depends on what you need to observe and under what conditions.

---

## The EM Spectrum Windows

The atmosphere is not uniformly transparent. Only certain wavelength ranges reach the sensor — atmospheric gases (H2O, CO2, O3) absorb the rest. These "atmospheric windows" define what remote sensing can measure.

```
  WAVELENGTH (micrometers, log scale)
  0.2        0.4   0.7  1.0   1.5   2.5      8    14         1000
   |          |    |    |     |     |         |    |           |
   +--[XXX]---+====+====+=[X]=+====+=[XXX]===+====+====[====]+
              VIS  NIR   SWIR            MIR   TIR      MICROWAVE
               |    |     |                    |         |
              [1]  [2]   [3]                  [4]       [5]

[X] = atmospheric absorption (O3, H2O, CO2 block these bands)
 =  = atmospheric window (sensor sees through)

[1] Visible 0.4-0.7 μm:   Blue/green/red. Vegetation color, water color, geology.
[2] NIR 0.7-1.3 μm:       Strong vegetation reflection (red edge). Biomass proxy.
[3] SWIR 1.3-2.5 μm:      Moisture stress, mineral mapping, snow vs. cloud.
[4] TIR 8-14 μm:          Land surface temperature. Emitted radiation. Night-capable.
[5] Microwave 1mm-1m:     SAR radar. Penetrates cloud, rain, canopy. All-weather.
```

---

## The Four Resolutions: Fundamental Trade-offs

Every sensor is characterized by four orthogonal resolution axes. Improving one almost always degrades another — the physics and engineering constraints force trade-offs.

```
                    SPATIAL           SPECTRAL
                    (pixel size)      (# of bands, bandwidth)
                         \               /
                          \             /
                    ┌──────────────────────┐
                    │   SENSOR DESIGN      │
                    │   TRADE-OFF SPACE    │
                    └──────────────────────┘
                          /             \
                         /               \
                    TEMPORAL           RADIOMETRIC
                    (revisit time)     (bit depth, SNR)

THE TRADE-OFFS:
  Spatial ↑  → Swath ↓ → Revisit ↑ (fewer orbits cover the globe)
  Spectral ↑ → Photons/band ↓ → SNR ↓ → need wider pixels (Spatial ↓)
  Temporal ↑ → Need wider swath or constellation → Spatial ↓
  Radiometric ↑ → Larger aperture, longer dwell → Cost ↑
```

| Resolution Type | Definition | Range | Trade-off |
|----------------|------------|-------|-----------|
| **Spatial** | Ground footprint per pixel | 0.3m (WorldView) to 40km (SMAP) | Finer pixels = narrower swath = longer revisit |
| **Spectral** | Number and width of bands | 4 bands (PAN+RGB) to 285 (EMIT) | More bands = less light per band = lower SNR |
| **Temporal** | Time between repeat observations | 5 min (GOES) to 91 days (ICESat-2) | Faster revisit = wider swath = coarser spatial |
| **Radiometric** | Sensitivity to signal differences | 8-bit (256 DN) to 14-bit (16384 DN) | Higher bit depth = better faint-signal detection |

**The observability parallel**: Think of spatial resolution as your **sampling rate** — how fine-grained your measurements are. Spectral resolution is **dimensionality** — how many distinct metrics you capture per observation (CPU, memory, disk vs. blue, green, red, NIR, SWIR). Temporal resolution is your **polling interval** — how often you check. Radiometric resolution is your **dynamic range** — can you distinguish a 1% signal change from noise? Every monitoring system makes these same four trade-offs.

---

## Platform Taxonomy

```
┌──────────────────┬────────────┬──────────────┬────────────┬───────────┐
│ Platform         │ Altitude   │ Swath        │ Revisit    │ Cost/km²  │
├──────────────────┼────────────┼──────────────┼────────────┼───────────┤
│ Geostationary    │ 35,786 km  │ Full disk    │ 5-15 min   │ Very low  │
│ (GOES, Himawari) │            │ (~11,000 km) │            │ (free)    │
├──────────────────┼────────────┼──────────────┼────────────┼───────────┤
│ LEO polar orbit  │ 400-800 km │ 10-2,900 km  │ Days-weeks │ Low/free  │
│ (Landsat, S-1/2) │            │              │            │           │
├──────────────────┼────────────┼──────────────┼────────────┼───────────┤
│ LEO non-SSO      │ 400-600 km │ Varies       │ Irregular  │ Low/free  │
│ (ISS: EMIT, ECOST)│           │              │            │           │
├──────────────────┼────────────┼──────────────┼────────────┼───────────┤
│ Airborne manned  │ 1-15 km   │ 0.5-50 km    │ On-demand  │ High      │
│ (AVIRIS, LVIS)   │            │              │            │           │
├──────────────────┼────────────┼──────────────┼────────────┼───────────┤
│ UAV / Drone      │ 50-500 m   │ 0.05-5 km    │ On-demand  │ Moderate  │
├──────────────────┼────────────┼──────────────┼────────────┼───────────┤
│ Ground-based     │ Surface    │ Point-100 m  │ Continuous │ High      │
│ (TLS, phenocams) │            │              │            │           │
└──────────────────┴────────────┴──────────────┴────────────┴───────────┘

ALTITUDE vs. DETAIL (the fundamental constraint):
  Higher → sees more area per pass → revisits faster → but coarser pixels
  Lower  → finer pixels → smaller coverage → revisits slower or costs more

GEO: weather monitoring. You sacrifice spatial detail for temporal cadence.
LEO: land/ocean science. Balance of spatial detail and global coverage.
Airborne/UAV: precision agriculture, LiDAR surveys. Best detail, no repeat.
```

---

## The Processing Pipeline

Raw sensor output is meaningless without calibration. Each processing level removes one category of artifact, progressively isolating the Earth-surface signal from instrument and atmospheric contamination.

```
  ┌───────────────┐
  │ Raw DN        │  Digital numbers from detector — uncalibrated integers.
  │ (Level 0)     │  No physical meaning without sensor-specific gain/offset.
  └───────┬───────┘
          │  RADIOMETRIC CALIBRATION
          v
  ┌───────────────┐
  │ At-sensor     │  DN → radiance (W/m²/sr/μm) using lab-measured gain/offset.
  │ Radiance      │  Removes detector non-uniformity, dead pixels, striping.
  │ (Level 1)     │
  └───────┬───────┘
          │  GEOMETRIC CORRECTION + ORTHORECTIFICATION
          v
  ┌───────────────┐
  │ Geolocated    │  Sensor model + GCPs + DEM → map projection.
  │ Imagery       │  Removes terrain parallax, platform jitter, Earth curvature.
  │ (Level 1T)    │
  └───────┬───────┘
          │  ATMOSPHERIC CORRECTION
          v
  ┌───────────────┐
  │ Surface       │  Remove atmospheric path radiance and absorption.
  │ Reflectance   │  Methods: DOS (dark object subtraction, simple), 6S/MODTRAN
  │ (Level 2)     │  (radiative transfer, physics-based), LaSRC (Landsat).
  └───────┬───────┘
          │  ANALYSIS + PRODUCT GENERATION
          v
  ┌───────────────┐
  │ ARD /         │  Band math (NDVI, NBR), classification (land cover),
  │ Products      │  temperature retrieval, deformation maps, flood extent.
  │ (Level 3+)    │
  └───────────────┘
```

**Why atmospheric correction matters**: Without it, you cannot compare images from different dates, different sensors, or even different parts of the same scene (the atmosphere is a different "filter" at every pixel depending on path length, aerosol load, and water vapor). Atmospheric correction is the equivalent of **normalizing your telemetry** so that metrics from different hosts, different SDKs, and different time zones are comparable.

---

## Key Missions at a Glance

| Mission | Agency | Type | Spatial Res | Bands | Revisit | Archive | Access |
|---------|--------|------|-------------|-------|---------|---------|--------|
| Landsat 9 | USGS/NASA | Multispectral + TIR | 30m / 100m | 11 | 16 day | 1972– | Free |
| Sentinel-2 A/B | ESA | Multispectral | 10/20/60m | 13 | 5 day | 2015– | Free |
| Sentinel-1 A/B | ESA | C-band SAR | 5×20m (IW) | Dual pol | 6 day | 2014– | Free |
| MODIS (Terra/Aqua) | NASA | Spectroradiometer | 250m–1km | 36 | Daily | 2000– | Free |
| NISAR | NASA/ISRO | L+S band SAR | 3–10m | Dual pol | 12 day | 2024– | Free |
| Planet Dove/SuperDove | Planet Labs | Multispectral | 3–5m | 8 | Daily | — | Commercial |
| ICESat-2 | NASA | Photon-counting LiDAR | 17m footprint | 532nm | 91 day | 2018– | Free |
| GOES-18 | NOAA | 16-channel imager | 500m–2km | 16 | 5–15 min | 2022– | Free |
| WorldView-3 | Maxar | Multi+SWIR+CAVIS | 0.31m PAN | 29 | 1–4 day | — | Commercial |
| EMIT | NASA/JPL | Hyperspectral (ISS) | 60m | 285 | Varies | 2022– | Free |

**The free data revolution**: Landsat (since 2008 open access), Sentinel (born open), and MODIS made planetary-scale analysis possible. Before open archives, a single Landsat scene cost $600. Now Google Earth Engine, Microsoft Planetary Computer, and AWS Open Data serve petabytes at zero cost. This is the remote sensing equivalent of the open-source movement — the sensor hardware is expensive, but the data is free.

---

## Vegetation Indices: Band Math as Feature Engineering

The simplest and most powerful remote sensing products come from ratios of spectral bands. A vegetation index combines bands where healthy vegetation has a strong contrast — typically high NIR reflectance (cell wall scattering) vs. low red reflectance (chlorophyll absorption).

```
                 Reflectance
                 │
           0.5   │              ┌─── Healthy vegetation
                 │             /│    (high NIR, low red)
           0.4   │            / │
                 │           /  │
           0.3   │          /   │
                 │         /    │
           0.2   │    ────/     │    Stressed vegetation
                 │   /          │    (lower NIR, higher red)
           0.1   │──/───────────│─── Bare soil (flat across bands)
                 │              │
           0.0   └──────┬───┬──┴────────
                       Red  NIR
                      0.65  0.85 μm

   RED EDGE: The sharp reflectance jump from ~0.68 to ~0.75 μm.
   Healthy plants: steep red edge. Stressed plants: red edge shifts blueward.
   Sentinel-2 has 3 red-edge bands (B5, B6, B7) specifically for this.
```

| Index | Formula | Range | What It Measures |
|-------|---------|-------|-----------------|
| **NDVI** | (NIR − Red) / (NIR + Red) | −1 to +1 | Green vegetation density. Saturates at LAI ~3. |
| **EVI** | 2.5 × (NIR − Red) / (NIR + 6×Red − 7.5×Blue + 1) | −1 to +1 | Canopy structure. Reduces soil/atmosphere noise. |
| **NDWI** | (Green − NIR) / (Green + NIR) | −1 to +1 | Open water detection. |
| **MNDWI** | (Green − SWIR) / (Green + SWIR) | −1 to +1 | Modified water index. Better in urban areas. |
| **NBR** | (NIR − SWIR2) / (NIR + SWIR2) | −1 to +1 | Burn severity. ΔNBR = pre-fire minus post-fire. |
| **NDSI** | (Green − SWIR1) / (Green + SWIR1) | −1 to +1 | Snow cover (snow reflects green, absorbs SWIR). |
| **SAVI** | 1.5 × (NIR − Red) / (NIR + Red + 0.5) | −1 to +1 | Soil-adjusted veg index. For sparse canopy. |

**Band math = feature engineering**: In machine learning, you compute derived features from raw inputs (interaction terms, ratios, differences). NDVI is literally `(feature_A - feature_B) / (feature_A + feature_B)` — a normalized difference. Every vegetation index is a hand-engineered feature designed to maximize sensitivity to one physical property while minimizing confounders. The remote sensing community has been doing feature engineering since 1973 (Rouse et al. invented NDVI), decades before the term existed in ML.

---

## Change Detection: Time Series as the Core Technique

Remote sensing becomes most powerful when you compare images over time. Single-date snapshots tell you **what is there**. Time series tell you **what changed** — deforestation, urban growth, flood extent, glacier retreat, crop phenology.

```
CHANGE DETECTION APPROACHES

1. IMAGE DIFFERENCING (simplest)
   ΔX = X_after - X_before
   Threshold: |ΔX| > T → "change"
   Works for: burn scars (ΔNBR), floods (ΔSigma0), deforestation (ΔNDVI)

2. TIME-SERIES ANOMALY DETECTION
   Model: fit trend + seasonal → predict expected value
   Anomaly: |observed - predicted| > threshold → breakpoint
   Algorithms: BFAST, LandTrendr, CCDC

   NDVI   │   ___     ___     ___
          │  /   \   /   \   /   X──── deforestation event
          │ /     \_/     \_/     \    (abrupt drop)
          │/                       \___
          └──────────────────────────── time
              yr1     yr2     yr3

3. SAR COHERENCE CHANGE (for radar)
   Coherence_before - Coherence_after
   Low → surface changed (earthquake damage, construction, flood)
   Used: damage proxy maps, subsidence monitoring

4. OBJECT-BASED CHANGE DETECTION
   Segment images into objects → classify → compare classes
   Better for urban change than pixel-level methods
```

**The monitoring parallel**: Change detection is **alerting on anomalies** in your time series. BFAST (Breaks For Additive Season and Trend) decomposes an NDVI time series into trend + seasonality + remainder — structurally identical to how you decompose server metrics to separate daily patterns from actual incidents. LandTrendr fits segmented regression to Landsat archives, flagging breakpoints. Same principle as change-point detection in SRE dashboards.

---

## The Observability Bridge

Remote sensing is **observability for the planet**. The conceptual parallels to distributed systems telemetry are deep and exact:

```
DISTRIBUTED SYSTEMS              REMOTE SENSING
─────────────────────────────────────────────────────────
Prometheus / Grafana             Satellite constellation
Metrics endpoint                 Spectral band
Sampling rate                    Spatial resolution
Polling interval                 Temporal resolution (revisit)
Dynamic range / bit depth        Radiometric resolution
Feature engineering              Band math (NDVI, NBR, EVI)
Time-series anomaly detection    Change detection (BFAST, CCDC)
Dashboard / alerting             GIS / early warning system
Log level (DEBUG vs ERROR)       Processing level (L0 → L2 → L3)
Health check ping                Active radar pulse (SAR)
Passive log collection           Passive optical sensor
Span / trace across services     Multi-sensor data fusion
Data lake (S3, BigQuery)         Cloud archive (GEE, Planetary Computer)
Normalization (units, timezone)  Atmospheric correction (reflectance units)
Sampling bias                    Cloud contamination / orbital gaps
```

The principle is the same: you cannot touch the thing you are measuring (a running production service; the Amazon rainforest canopy at 700 km altitude). You design instruments that observe from the outside, calibrate them to remove systematic artifacts, normalize the data so observations from different times and places are comparable, compute derived features that amplify the signal you care about, and set up alerts when something changes. The physics differs — photons not packets — but the information architecture is identical.

---

## Connection to GIS and Earth System Science

Remote sensing is the primary data-input layer for geographic information systems and Earth system models. It feeds every downstream model with calibrated, georeferenced observations.

```
REMOTE SENSING DATA                    DOWNSTREAM SYSTEMS
┌─────────────────────────┐           ┌──────────────────────────┐
│ Satellite imagery       │──────────>│ GIS (vector+raster)      │
│ SAR backscatter         │──────────>│ Land cover classification │
│ LiDAR point clouds      │──────────>│ DEMs, terrain analysis   │
│ Thermal infrared        │──────────>│ Surface temperature maps │
│ Passive microwave       │──────────>│ Snow/ice/soil moisture   │
│ Hyperspectral           │──────────>│ Mineral/species mapping  │
└─────────────────────────┘           └────────────┬─────────────┘
                                                   │
                                                   v
                                      ┌──────────────────────────┐
                                      │ Earth System Models       │
                                      │ Climate models (CMIP6)    │
                                      │ Carbon cycle (ORCHIDEE)   │
                                      │ Hydrological (VIC, SWAT)  │
                                      │ Crop yield (DSSAT, APSIM) │
                                      │ Fire risk (EFFIS)         │
                                      └──────────────────────────┘
```

The field sits at the intersection of **physics** (radiative transfer, Planck function, scattering theory), **engineering** (sensor design, orbital mechanics, antenna theory), **signal processing** (SAR coherence, LiDAR waveform decomposition, spectral unmixing), and **geoscience** (interpreting what the numbers say about forests, oceans, ice sheets, and cities).

---

## Section Map

| File | Topic |
|------|-------|
| 01-EM-SPECTRUM.md | Atmospheric windows, scattering regimes, Planck function, solar vs. thermal crossover |
| 02-PASSIVE-SENSORS.md | Multispectral, hyperspectral, thermal — calibration through to products |
| 03-ACTIVE-SENSORS-SAR.md | SAR principles: range/azimuth resolution, polarimetry, backscatter physics |
| 04-LIDAR.md | Time-of-flight, point clouds, airborne/terrestrial/bathymetric/space LiDAR |
| 05-SATELLITE-ORBITS.md | Sun-synchronous, geostationary, repeat cycles, revisit vs. resolution |
| 06-IMAGE-PROCESSING.md | Geometric correction, atmospheric correction, classification algorithms |
| 07-INSAR.md | Interferometric SAR: DEM generation, surface deformation, PS-InSAR |
| 08-PLATFORMS.md | Landsat, Sentinel, MODIS, NISAR, Planet — detailed specs and data access |
| 09-APPLICATIONS.md | Agriculture, forestry, urban, disaster response, cryosphere, ocean |

---

## Decision Cheat Sheet

*Which sensor for which question?*

| Question | Sensor / Mission | Band | Why |
|----------|-----------------|------|-----|
| Vegetation health / greenness? | Sentinel-2, Landsat 9 | Red + NIR (NDVI) | Chlorophyll absorbs red; healthy plants reflect NIR |
| Crop type at field scale? | Sentinel-2 time series | VIS/NIR/red-edge | Phenological profiles unique per crop |
| Vegetation moisture stress? | Sentinel-2 | SWIR + NIR | Liquid water absorbs SWIR |
| Burn severity? | Landsat 9 | NIR + SWIR2 (dNBR) | Fire destroys NIR reflectance, increases SWIR |
| Land surface temperature? | Landsat TIRS, ECOSTRESS | TIR (10–12 μm) | Peak Planck emission at ~300K |
| Active fire detection? | MODIS, VIIRS | MIR (3.7 μm) | Hot targets radiate strongly at short TIR |
| Snow vs. cloud? | Sentinel-2, Landsat | SWIR (1.6 μm) | Snow absorbs SWIR; cloud reflects it |
| Mineral / lithology mapping? | ASTER, EMIT, Sentinel-2 | SWIR (2.0–2.5 μm) | Clay, carbonate, iron-oxide absorption features |
| Flood extent (any weather)? | Sentinel-1 SAR | C-band (5.6 cm) | Water = specular = dark in radar. All-weather. |
| Earthquake / volcano deformation? | Sentinel-1 InSAR | C-band phase | mm-scale surface displacement from phase diff |
| Forest biomass? | NISAR (L-band), GEDI LiDAR | L-band + 1064nm | Deep canopy penetration + direct height measurement |
| Sea ice classification? | Sentinel-1, RADARSAT | C-band HH/VV | Multi-year ice vs. first-year ice backscatter |
| Ocean chlorophyll / color? | MODIS Aqua, Sentinel-3 OLCI | Blue/Green ratio | Phytoplankton absorb blue, reflect green |
| Sea surface temperature? | MODIS, VIIRS, GOES ABI | TIR split-window | Dual-band atmospheric correction for SST |
| Atmospheric aerosol / haze? | Sentinel-2 B1, MODIS | Blue (0.44 μm) | Rayleigh scattering maximized at short λ |
| Topography / 3D structure? | Airborne LiDAR, ICESat-2 | 1064nm / 532nm | Direct range measurement → DEM + canopy height |
| Soil moisture (global)? | SMAP, NISAR | L-band (passive/active) | Deep microwave penetration to soil surface |
| Daily global monitoring? | MODIS, VIIRS, Planet | VIS/NIR/TIR | Wide swath + daily revisit at moderate resolution |
| Sub-meter urban detail? | WorldView-3, Pleiades | PAN + multispectral | 0.3m commercial; building-level discrimination |

---

## Common Confusion Points

**"Remote sensing = satellite imagery."** No. Remote sensing includes airborne LiDAR, ground-based radiometers, drone-based multispectral, shipboard radar, and even medical imaging (ultrasound is active remote sensing of tissue). Satellite is the most visible platform, but the physics applies at every altitude.

**"Passive sensors see through clouds."** Only passive **microwave** sensors (SSM/I, AMSR-2) can. Passive **optical** sensors (Landsat, Sentinel-2, MODIS) require clear sky — cloud droplets scatter visible/NIR/SWIR completely. This is why SAR is indispensable for tropical forests and monsoon regions with persistent cloud cover.

**"Higher resolution is always better."** Resolution trades against swath width, revisit time, spectral richness, and cost. A 0.3m WorldView image covers a tiny area once per week at commercial rates. A 30m Landsat image covers continents every 16 days for free. A 250m MODIS pixel delivers daily global coverage. "Better" depends entirely on the question. If you need daily NDVI trends over the Amazon, MODIS at 250m beats WorldView at 0.3m.

**"Level 2 surface reflectance = ready to analyze."** It is atmospherically corrected, but it may still have clouds (need masking), slight misregistration (need co-registration for change detection), and sensor-specific quirks (BRDF effects at off-nadir angles). USGS ARD (Analysis Ready Data) handles most of this automatically, but always inspect your inputs.

**"NDVI tells you everything about vegetation."** NDVI saturates at leaf area index ~3 (dense canopy). Beyond that, all forests look the same in NDVI regardless of biomass differences. EVI reduces saturation. For actual biomass estimation, you need LiDAR (canopy height) or L-band SAR (backscatter correlates with wood volume). NDVI is a screening tool, not a complete answer.

**"Reflectance and radiance are interchangeable."** Reflectance is dimensionless (0–1), the fraction of incoming solar energy reflected. Radiance (W/m²/sr/μm) depends on sun angle, Earth-sun distance, and atmosphere — it changes every hour. You **must** convert to reflectance before comparing scenes from different dates or sensors. Skipping this step is like comparing CPU utilization percentages across machines with different core counts without normalizing.

**"Near-infrared is thermal infrared."** NIR (0.7–1.3 μm) is reflected solar energy — same physics as visible light, just outside human eye range. TIR (8–14 μm) is emitted thermal energy — the surface radiating heat according to the Planck function. They differ by an order of magnitude in wavelength and completely different physics. Conflating them is a category error.
