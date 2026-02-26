# Passive Sensors: Multispectral, Hyperspectral, Thermal

## The Big Picture

Passive optical sensors record reflected solar energy (shortwave: 0.4-2.5 um) and/or thermally emitted energy (longwave TIR: 8-14 um). The fundamental question is spectral design: how many bands, where, and how wide? The answer determines what science is possible.

```
SPECTRAL SAMPLING STRATEGIES
                                              Spectral resolution
BROAD BANDS                                  NARROW CONTIGUOUS
(multispectral)                              (hyperspectral)
    |          |     |    |                  ||||||||||||||||||||||||
    |   Blue   | NIR | SW |                  ||||||||||||||||||||||||
    |          |     |    |                  ||||||||||||||||||||||||
  0.4         0.7   1.0  2.5 um           0.4                     2.5 um
  4-12 bands typical                      200-400 bands typical
  30-100m spatial resolution              10-30m spatial resolution
  Large swath, frequent revisit           Smaller swath, less frequent

THERMAL BANDS
   |     |
   | 10  | 12 um        2-8 TIR bands (ASTER: 5; Landsat TIRS: 2; ECOSTRESS: 8)
   TIR window
```

---

## Multispectral Sensors: Resolution Taxonomy

Spatial resolution and spectral resolution trade against each other within a fixed detector budget. The dominant operational sensors:

```
+----------------+----------+------+--------+---------+--------+
| Sensor         | Platform | GSD  | Bands  | Swath   | Revisit|
+----------------+----------+------+--------+---------+--------+
| OLI-2 / TIRS-2 | Landsat 9| 30m  | 9+2TIR | 185 km  | 16 day |
| MSI            | Sent-2   | 10m  | 13     | 290 km  | 5 day  |
| MODIS          | Terra/   | 250m | 36     | 2330 km | daily  |
|                | Aqua     |-1km  |        |         |        |
| SuperDove      | Planet   | 3-5m | 8      | 24 km   | daily  |
| WV-3 MS        | Maxar WV3| 1.24m| 8+8SWIR| 13 km   | 1-4 day|
| SPOT-7         | SPOT-7   | 6m   | 4      | 60 km   | 26 day |
| RapidEye       | retired  | 5m   | 5+RedE | 77 km   | daily  |
+----------------+----------+------+--------+---------+--------+
```

### MODIS: The Daily Global Machine

MODIS (Moderate Resolution Imaging Spectroradiometer) is unique: 36 bands from 0.4 to 14.4 um, daily global coverage at 250m-1km. The science products it generates are the backbone of global Earth monitoring:

| Product | Bands Used | Algorithm |
|---------|------------|-----------|
| MOD13 Vegetation Index | B1 Red (620-670), B2 NIR (841-876) | NDVI and EVI |
| MOD11 Land Surface Temp | B31 (10.78-11.28 um), B32 (11.77-12.27 um) | Split-window |
| MOD09 Surface Reflectance | 7-band (B1-B7) | 6S radiative transfer |
| MOD14 Active Fire | B21 (3.96 um), B22 (3.96 um), B32 | Thermal anomaly |
| MYD28 Sea Surface Temp | TIR bands | Split-window retrieval |

---

## Vegetation Indices: The Band Ratio Arsenal

Band ratios are dimensionless and reduce illumination effects (sun angle, terrain shadows). They exploit the spectral contrast between absorption and reflectance features.

### The Physics of NDVI

```
       NIR - Red
NDVI = ---------       Range: -1 to +1
       NIR + Red

Healthy vegetation:   NIR high (~0.5), Red low (~0.05)  -> NDVI ~0.8
Bare soil:            NIR moderate, Red moderate        -> NDVI ~0.1-0.3
Water:                NIR very low, Red low             -> NDVI ~0 or negative
Snow/cloud:           both high                         -> NDVI ~0

Why this works: Chlorophyll strongly absorbs red (0.65 um).
Cell wall scattering strongly reflects NIR (0.85 um).
Their contrast maximizes for healthy vegetation.
```

### The Band Ratio Family

| Index | Formula | Physical Target | Key Application |
|-------|---------|-----------------|-----------------|
| NDVI | (NIR-Red)/(NIR+Red) | Chlorophyll contrast | Vegetation cover, biomass |
| EVI | 2.5*(NIR-Red)/(NIR+6*Red-7.5*Blue+1) | Canopy structure | Reduces aerosol, saturation issues vs. NDVI |
| NDWI (Gao) | (NIR-SWIR1)/(NIR+SWIR1) | Canopy water content | Vegetation moisture stress |
| NDWI (McFeeters) | (Green-NIR)/(Green+NIR) | Open water | Lake/river mapping |
| MNDWI | (Green-SWIR1)/(Green+SWIR1) | Open water + built | Urban water detection |
| NBR | (NIR-SWIR2)/(NIR+SWIR2) | Burn severity | dNBR = pre-fire minus post-fire |
| NDSI | (Green-SWIR1)/(Green+SWIR1) | Snow vs. cloud | Snow cover mapping |
| SAVI | (NIR-Red)/(NIR+Red+L)*(1+L) L=0.5 | Sparse veg | Low vegetation cover adjustment |
| BSI | (SWIR1+Red-NIR-Blue)/(SWIR1+Red+NIR+Blue) | Bare soil | Agriculture, erosion mapping |

**EVI vs. NDVI**: NDVI saturates above LAI ~3 (dense forest). EVI corrects for aerosols (blue band term) and canopy background. Use NDVI for sparse-to-moderate vegetation; EVI for dense canopy or aerosol-prone regions (Amazon, smoke).

---

## Hyperspectral Sensors: The Spectral Fingerprint Machine

Hyperspectral (imaging spectroscopy) records hundreds of contiguous narrow bands (typically 5-10 nm bandwidth) versus multispectral's handful of broad bands (50-200 nm bandwidth). The result is a full reflectance spectrum for every pixel.

```
MULTISPECTRAL pixel:
  [Blue=0.12] [Green=0.18] [Red=0.07] [NIR=0.45] [SWIR=0.25]
  Five numbers. Limited spectral discrimination.

HYPERSPECTRAL pixel:
  [0.400=0.03] [0.410=0.04] [0.420=0.05] ... [2.490=0.08] [2.500=0.07]
  280 numbers. Full reflectance spectrum = "spectral fingerprint"
  Can match to spectral libraries for mineral identification,
  species discrimination, snow grain size, water chemistry.
```

### Key Hyperspectral Sensors

| Sensor | Platform | Bands | Range (um) | GSD | Status |
|--------|----------|-------|------------|-----|--------|
| AVIRIS-NG | Aircraft | 432 | 0.38-2.51 | 3-10m | NASA JPL, operational |
| DESIS | ISS | 235 | 0.40-1.00 | 30m | DLR/Teledyne, operational |
| PRISMA | Satellite | 250 | 0.40-2.50 | 30m | ASI (Italy), free archive |
| EnMAP | Satellite | 228 | 0.42-2.45 | 30m | DLR, 2022--, free |
| EMIT | ISS | 285 | 0.38-2.50 | 60m | NASA JPL, 2022--, free |
| HyspIRI | Proposed | 213 | 0.38-2.50 | 60m | NASA concept |

### Spectral Unmixing

Most hyperspectral pixels contain a mixture of materials (soil + vegetation + shade). Spectral unmixing decomposes the pixel spectrum as a linear combination of "endmember" spectra:

```
Pixel reflectance = sum_i (f_i * r_i) + noise

where:
  f_i = fractional abundance of endmember i (sum to 1)
  r_i = pure spectral signature of endmember i

Endmembers: measured in field (ASD spectrometer), from library (USGS),
            or extracted from the image itself (N-FINDR, VERTEX algorithms)
```

Applications: mineral mapping (clay vs. carbonate vs. iron oxide mixtures), burn severity (char vs. green vs. bare soil fractions), coral reef health (coral vs. algae vs. bleached coral fractions).

---

## Thermal Infrared (TIR) Sensors

TIR sensors measure emitted radiation from the Earth's surface (8-14 um). Key operational sensors:

| Sensor | Platform | Bands (um) | GSD | Key Science |
|--------|----------|------------|-----|-------------|
| TIRS-2 | Landsat 9 | 10.9, 12.0 | 100m | LST, urban heat, agriculture |
| ASTER TIR | Terra | 8.125-11.65 (5 bands) | 90m | Emissivity, geology, volcanoes |
| ECOSTRESS | ISS | 8.28-12.05 (8 bands) | 38x69m | ET, plant water stress, LST |
| VIIRS | S-NPP/JPSS | 10.76-12.27 (2 bands) | 750m | LST, fire, daily global |
| ABI | GOES | 10.3, 11.2, 12.3, 13.3 um | 2km | Cloud, SST, storm tracking |

### Land Surface Temperature (LST) Retrieval

```
INPUTS:
  - At-sensor TIR radiance (from Level 1)
  - Atmospheric water vapor profile (from NWP: NCEP, ERA5)
  - Surface emissivity (from ASTER emissivity database, or estimated)

STEP 1: Atmospheric correction
  Remove upwelling and downwelling atmospheric emission
  Correct for atmospheric absorption (transmittance)
  -> At-surface radiance

STEP 2: Emissivity correction
  L_surface = emissivity * B(lambda, T_surface)
  Invert for T_surface using Planck function
  -> Land Surface Temperature

ACCURACY:
  Standard algorithms: ~1-2 K absolute
  ECOSTRESS: <1.5 K target
  Factors: emissivity uncertainty, atmospheric column water
```

**Urban heat island detection**: Compare LST in urban core vs. surrounding rural land. Vegetated parks appear 3-8 K cooler. Concrete/asphalt: high temperatures. Green roofs: detectable cooling. Spatial pattern directly visible at 30-100m resolution.

---

## Radiometric Calibration Chain

The chain from raw detector output to physically meaningful surface reflectance:

```
STEP 1: DN -> At-sensor radiance
  L = gain * DN + offset
  Gain and offset from preflight lab calibration,
  updated by onboard calibration systems (solar diffuser panels)
  Units: W/m2/sr/um

STEP 2: At-sensor radiance -> TOA reflectance
  rho_TOA = pi * L * d^2 / (ESUN * cos(theta_s))
  where:
    d = Earth-Sun distance (AU, varies ~3%)
    ESUN = exoatmospheric solar irradiance for the band
    theta_s = solar zenith angle
  Dimensionless: 0-1 scale
  Removes illumination geometry. Still has atmospheric signal.

STEP 3: TOA -> Surface reflectance (atmospheric correction)
  METHODS:
  a) Dark Object Subtraction (DOS): subtract minimum DN in each band
     Assumes "dark" pixel = 0% surface reflectance.
     Fast, no auxiliary data. Approximate but widely used.

  b) MODTRAN/6S radiative transfer:
     Full physics simulation of atmospheric absorption + scattering
     Requires atmospheric profile (water vapor, ozone, aerosol)
     Source: NCEP reanalysis, radiosonde data
     Most accurate. Used by USGS LaSRC (Landsat Collection 2)

  c) ACOLITE:
     Specialized for aquatic environments (ocean, lakes, rivers)
     Dark spectrum fitting using SWIR (water absorbs completely)
     More accurate than DOS for water applications

  d) iCOR / Py6S / FORCE:
     Open-source implementations of 6S for Sentinel-2
```

---

## Decision Cheat Sheet

| Need | Sensor Choice | Reason |
|------|---------------|--------|
| Global vegetation monitoring daily | MODIS (Terra/Aqua) | Daily global, 36 bands, free |
| 10m land cover with time series | Sentinel-2 | 5-day revisit, free, 13 bands |
| 50-year change detection | Landsat (OLI) | Archive from 1972, consistent calibration |
| Sub-meter commercial mapping | WorldView-3, Maxar | 0.31m PAN, commercial |
| Mineral / geology mapping | Hyperspectral (EMIT, PRISMA) | SWIR spectral fingerprinting |
| Land surface temperature | Landsat TIRS, ECOSTRESS | Split-window LST algorithms |
| Fire monitoring global daily | MODIS, VIIRS | MIR bands, daily, global |
| Cloud-free coverage tropics | SAR (not passive) | Passive optical fails in cloud |
| Vegetation water stress | ECOSTRESS TIR | Evapotranspiration from LST |
| Daily global snow cover | MODIS MOD10 | NDSI algorithm, daily |

---

## Common Confusion Points

**NDVI vs. EVI**: Not interchangeable. NDVI saturates in dense canopy (Amazon, boreal forest). EVI is better there. NDVI is simpler and more validated historically. For global consistency with existing literature, NDVI remains dominant.

**30m spatial resolution = 30m pixel**, not 30m feature detection. The theoretical spatial frequency limit (Nyquist) means you can reliably detect features ~3x the pixel size. A 30m pixel can detect a 90m road; a 5m pixel can detect a 15m road.

**Multispectral is not hyperspectral** -- 13 bands (Sentinel-2) cannot identify individual minerals or species. For mineralogy or plant species discrimination, you need 200+ contiguous narrow bands and corresponding spectral libraries.

**SWIR requires InGaAs detectors**, not silicon. Silicon detectors stop working above ~1.1 um. Landsat OLI uses HgCdTe for SWIR. WorldView-3's SWIR focal plane is expensive. This is one reason commercial SWIR imagery costs more than VIS/NIR.
