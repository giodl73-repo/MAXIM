# Remote Sensing Applications: Agriculture, Forestry, Urban, Disaster, Cryosphere, Ocean

## The Big Picture

Remote sensing translates physical measurements (reflectance, backscatter, elevation, temperature) into actionable information about Earth systems. Each application domain uses a specific combination of sensor types, wavelengths, and processing algorithms tailored to the physical processes involved.

```
APPLICATION DOMAINS

                    SENSOR COMBINATION
            Optical    Thermal    SAR    LiDAR    Microwave
            (VIS/SWIR) (TIR)      (cm)   (LiDAR)  (passive)
            -------------------------------------------------
Agriculture |  [XXX]   |  [X]   |  [X] |        |  [X]   |
Forestry    |  [X]     |        |  [XX]|  [XXX] |        |
Urban       |  [XX]    |  [X]   |  [XX]|  [XX]  |        |
Disaster    |  [X]     |        |  [XXX]|       |        |
Cryosphere  |  [X]     |  [X]   |  [XX]|  [XX]  |  [XX]  |
Ocean       |  [X]     |  [XX]  |  [X] |        |  [XX]  |

[XXX] = primary sensor   [XX] = important   [X] = supplementary
```

---

## Agriculture

### Crop Type Mapping

Crops have distinct spectral and phenological signatures. Temporal signatures (how NDVI changes through the growing season) are often more discriminating than single-date spectral values:

```
PHENOLOGICAL PROFILES (NDVI over time)

Winter wheat:
  NDVI  |         /\
  0.8   |        /  \
  0.6   |       /    \
  0.4   |      /      \___
  0.2   |___  /            ___
        J F M A M J J A S O N D

Corn:
  NDVI  |             /\
  0.8   |            /  \
  0.6   |           /    \
  0.4   |          /      \
  0.2   |_________/        \___
        J F M A M J J A S O N D

Each crop type has characteristic: emergence date, peak, senescence, harvest
Classification using time-series features (NDVI amplitude, timing) + ML
Sentinel-2 (5-day, 10m) is the standard for field-scale crop mapping
```

### Yield Estimation

```
NDVI-BASED YIELD ESTIMATION

  Simple: yield ~ NDVI * solar radiation * conversion efficiency
  (NDVI approximates fAPAR: fraction of absorbed PAR)

  Advanced models:
    DSSAT, APSIM: process-based crop models
    Remotely sensed LAI, soil moisture as inputs
    Data assimilation (Kalman filter): update model state with RS observations

  Limitations: NDVI saturates at high LAI; atmospheric effects in cloudy regions
  Better index: EVI, CCCI (Canopy Chlorophyll Content Index using red-edge)
```

### Soil Moisture

```
ACTIVE:  Sentinel-1 (C-band backscatter)
  sigma0 ~ dielectric constant ~ soil moisture (rough empirical relationship)
  Change detection approach: temporal relative soil moisture
  Works at 20-40m scale (field level)
  Limitation: only surface (~5cm), vegetation mask required

PASSIVE: SMAP (Soil Moisture Active Passive, L-band passive microwave)
  L-band (1.4 GHz) brightness temperature -> soil moisture inversion
  ~40km spatial resolution (microwave footprint)
  Global daily coverage
  Depth: ~5cm, with freeze/thaw product
  SMAP Enhanced: 9km (with Sentinel-1 downscaling algorithm)
```

---

## Forestry

### Above-Ground Biomass (AGB) Estimation

```
DATA FUSION APPROACH (current best practice)

  ICESat-2 + GEDI (LiDAR):
    Accurate canopy height at sample locations
    Along-track only, sampling gaps

  Sentinel-1 (SAR):
    L-band backscatter ~ biomass (saturates ~100 t/ha for C-band)
    Continuous spatial coverage

  Sentinel-2 (Optical):
    Spectral features (NDVI, red-edge): proxy for canopy structure
    Cloud masking limitation in tropical forests

  FUSION:
    Train ML model: ICESat-2/GEDI height -> AGB (using allometric equations)
    Extrapolate to full coverage using Sentinel-1/2 as wall-to-wall predictors
    Current global maps: ESA CCI Biomass, GEDI L4B, Lang et al. 2022 (Nature)
```

### Deforestation Alerts

```
GLAD ALERT SYSTEM (Global Land Analysis and Discovery, UMD):
  Sentinel-1 + Landsat: 30m daily-to-weekly alerts
  Decision tree: anomaly in time series -> loss flag
  Amazon, tropics primary application
  Available: Global Forest Watch (globalforestwatch.org)

RADD ALERT (Radar for Detecting Deforestation):
  Sentinel-1 only: works in cloud-covered tropics
  C-band backscatter change: forest loss visible even through clouds
  Detects forest -> non-forest conversion within 1-3 weeks

BURN SEVERITY: dNBR
  dNBR = NBR_prefire - NBR_postfire
  NBR = (NIR - SWIR2) / (NIR + SWIR2)
  Threshold dNBR: high severity > 0.66; low severity 0.1-0.27
  USGS burn severity mapping uses Landsat dNBR
```

---

## Urban Remote Sensing

### Impervious Surface Mapping

```
SPECTRAL APPROACH:
  Impervious = concrete, asphalt, metal: high SWIR reflectance, low NIR
  Confusion with bare soil (both bright in red/SWIR)

  V-I-S model (Ridd 1995): urban = Vegetation + Impervious + Soil
  Spectral unmixing: endmembers = pure veg, pure impervious, pure soil
  Fractional impervious cover at subpixel level from Landsat 30m

SAR APPROACH:
  Double-bounce scattering from building walls + ground = bright
  Urban texture: high backscatter variation (PolSAR decomposition)
  Sentinel-1 urban extent maps at 10m
```

### Thermal Urban Heat Islands

```
UHI MAPPING:
  Landsat TIRS LST (100m): daytime surface temperature
  ECOSTRESS (70m): multiple times per day (ISS orbit)

  Urban core vs. rural reference:
    Typical UHI intensity: 2-10 K
    Parks: 2-5 K cooler than surrounding urban
    Green roofs: detectable 1-3 K cooling
    Water bodies: strong cooling effect

  Application: city planning, heat-related health risk mapping
  Diurnal cycle: ECOSTRESS captures peak afternoon heat stress

BUILDING HEIGHT AND 3D CITY MODEL:
  LiDAR (airborne, 10-20 pts/m2):
    Building segmentation, height extraction, LoD2 3D models
  SAR (TerraSAR-X spotlight, 1m):
    Building shadow + layover -> height estimation
    SAR tomography: 3D reconstruction from multiple angles
```

---

## Disaster Response

### Flood Mapping

```
SAR FLOOD DETECTION (C-band, VV):

  PHYSICS: Open water -> very smooth surface -> specular reflection
    Near-nadir incidence: specular -> radar signal bounces away
    Sentinel-1 VV over water: sigma0 < -20 dB (very low)
    Vegetation/soil: -15 to -5 dB (brighter)

  ALGORITHM:
    1. Threshold sigma0: water if < -18 dB (simple thresholding)
    2. Change detection: water_t - water_ref (flood = newly dark)
    3. Machine learning: trained on labeled flood events

  CHALLENGES:
    Flooded vegetation: double-bounce -> BRIGHT (not dark!)
    Wind on water: increases roughness -> less dark
    Urban flooding: complex scattering patterns

  SYSTEMS:
    Copernicus Emergency Management Service (CEMS): automated SAR-based flood maps
    ARIA Team (JPL): automatic Sentinel-1 flood products
    GFM (Global Flood Monitoring): automated near-real-time

OPTICAL (clear sky only):
  MNDWI thresholding from Sentinel-2
  Accurate, higher resolution, but requires cloud-free image (problematic during floods)
```

### Earthquake Damage Proxy Maps

```
SAR COHERENCE CHANGE DETECTION

  Before earthquake: high coherence in urban areas (stable buildings)
  After earthquake: low coherence where buildings collapsed (random scattering)

  Damage Proxy Map = coherence_before - coherence_after
  High coherence change -> likely damage

  Sentinel-1 pair (6-day repeat):
    Before pair: coherence ~0.6-0.8 (stable urban)
    After pair: coherence ~0.1-0.3 (damaged buildings collapsed)
    Detection rate: moderate damage detectable; total collapse = strong signal

  ARIA damage proxy maps: automated, available within 24-48hr of event
  Limitations:
    False positives: construction, agriculture
    Cannot distinguish structural damage type
    Optical inspection needed for confirmation
```

---

## Cryosphere

### Sea Ice Classification

```
SAR POLARIMETRY FOR SEA ICE:

  FIRST-YEAR ICE (FYI) vs. MULTI-YEAR ICE (MYI):
    FYI: one winter old, flat, lower backscatter (HH), smooth surface
    MYI: survived summer melt, rough ridges, very high HH backscatter
    C-band HH/VV ratio: MYI > FYI (volume scattering from brine inclusions melted out)

  RADARSAT Constellation Mission: dedicated sea ice monitoring
  Sentinel-1 EW mode (400km swath): daily Arctic coverage

PASSIVE MICROWAVE:
  AMSR-2 (18.7 + 36.5 GHz): sea ice concentration daily 6.25km
  Algorithm: ASI (Artist Sea Ice) uses brightness temperature gradient
  SIC = sea ice concentration: 0-100%
  Continuous record: SMMR (1978), SSM/I (1987), AMSR-E (2002), AMSR-2 (2012)
  Critical: September minimum (Arctic) trend = -13%/decade since 1979
```

### Ice Sheet and Glacier Dynamics

```
ICESat-2 SURFACE ELEVATION CHANGE:
  dh/dt from repeat passes (91-day cycle)
  Ice sheet mass balance: dM/dt = rho_ice * dh/dt * Area - SMB terms
  Greenland: -280 Gt/yr ice loss (2003-2019, ICESat + Grace)

GLACIER VELOCITY (feature tracking):
  Match distinctive features (crevasses, moraines) between two optical images
  Pixel displacement / time = velocity
  Sentinel-2 monthly: 1000m resolution velocity (displacement >> pixel size)
  Optical with sub-pixel: 0.1 pixel accuracy = 1m/month at 10m pixel size
  SAR speckle tracking: intensity-based feature tracking in SAR images
```

---

## Ocean

### Sea Surface Temperature (SST)

```
TIR SST RETRIEVAL:

  AVHRR split-window algorithm (NOAA operational):
    SST = a0 + a1*T11 + a2*(T11-T12) + a3*(T11-T12)^2 + ...

  MODIS Level-3 SST: 4km daily, 9km monthly
  GOES ABI: hourly SST, 2km (US coastal waters)

  Accuracy: ~0.3-0.5 K (bulk SST)
  Skin SST (0.1mm depth): what TIR measures; bulk T slightly warmer

  DIURNAL WARMING:
    Near-surface layer can warm 1-5 K during calm sunny days
    GOES captures diurnal SST cycle completely
```

### Ocean Color

```
OCEAN COLOR (chlorophyll-a):

  Algorithm (NASA OC4/OC3):
    Chl-a = 10^(a0 + a1*X + a2*X^2 + ...) where X = log10(max(Rrs443,Rrs490)/Rrs555)
    Rrs = remote sensing reflectance in blue-green ratio

  Product: MODIS Aqua OCx, VIIRS, Sentinel-3 OLCI (300m)
  Application: phytoplankton bloom detection, eutrophication, HABs

  CHALLENGES: Coastal (Case 2) water = non-algal particles + CDOM + suspended sediment
    Standard ocean color algorithms fail in turbid coastal water
    Need specialized algorithms (Mixture Density Networks, POLYMER, C2RCC)
```

### Ocean Surface Wind and Wave

```
SAR OCEAN APPLICATIONS:

  Oil spills: dampen capillary waves -> dark patch in SAR image
    Detection: threshold sigma0 in C-band VV
    Risk: dark spots from natural surfactants, rain cells

  Ship detection: bright targets on dark background
    Automatic ship detection (CFAR algorithm) in Sentinel-1
    AIS cross-reference: confirm, identify dark vessels

  Wind speed: CMOD5/CMOD7 geophysical model function
    sigma0 = f(U10, chi) where chi = wind direction relative to look angle
    C-band scatterometers (MetOp ASCAT): dedicated wind measurement
```

---

## Decision Cheat Sheet

| Application | Primary Sensor | Secondary | Key Algorithm |
|-------------|---------------|-----------|---------------|
| Crop type mapping | Sentinel-2 (time series) | Sentinel-1 | Random Forest + phenology |
| Soil moisture field-scale | Sentinel-1 | SMAP (coarse) | Change detection |
| Forest AGB | LiDAR + Sentinel-1 | Sentinel-2 | Data fusion ML |
| Deforestation alerts | Sentinel-1 SAR | Landsat | RADD, GLAD |
| Burn severity | Landsat (dNBR) | -- | dNBR threshold |
| Urban heat island | Landsat TIRS, ECOSTRESS | -- | Split-window LST |
| Flood mapping | Sentinel-1 GRD | Sentinel-2 | Threshold + change detection |
| Earthquake damage | Sentinel-1 (coherence) | -- | Coherence change ratio |
| Sea ice type | RADARSAT / Sentinel-1 | AMSR-2 | Polarimetric decomposition |
| Glacier velocity | Sentinel-2 / Sentinel-1 | ICESat-2 | Feature tracking |
| SST | MODIS, VIIRS, GOES ABI | -- | Split-window |
| Ocean chlorophyll | MODIS Aqua, OLCI | -- | OC4 band ratio |

---

## Common Confusion Points

**"SAR sees flooded areas as dark"** -- Only open water flood. Flooded forest creates double-bounce (tree trunks vertical in water), which appears bright in SAR. Flooded urban areas are complex. "Dark = flood" only applies to flooded bare fields or open water bodies.

**NDVI saturation in forests** -- NDVI above LAI ~3 plateaus near 0.8-0.9 regardless of biomass differences. Radar backscatter (L-band) and LiDAR are better biomass estimators for high-biomass forests. EVI reduces saturation somewhat.

**Damage proxy maps are proxies** -- Coherence change detects something changed in the radar scattering characteristics. Buildings collapsing changes radar returns dramatically. But so does construction, vegetation change, or soil disturbance. Ground truth is required before declaring damage.

**Ocean color algorithms fail near coasts** -- MODIS standard OC4 chlorophyll algorithm assumes optically deep "Case 1" water dominated by phytoplankton. Coastal "Case 2" waters with suspended sediment, river discharge, and CDOM give completely wrong chlorophyll values with the standard algorithm.
