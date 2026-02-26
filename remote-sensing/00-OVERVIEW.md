# Remote Sensing — Landscape and Taxonomy

## The Big Picture

Remote sensing: acquiring information about Earth's surface without physical contact. A sensor measures energy — emitted or reflected — and reconstructs what the target looks like. Everything else follows from the physics of how energy interacts with matter.

```
+------------------------------------------------------------------+
|                    ENERGY SOURCE                                 |
|  Sun (passive shortwave)   Earth itself (passive thermal)        |
|  Sensor's own transmitter (active: radar, LiDAR)                |
+------------------------------------------------------------------+
         |                          |                   |
         v                          v                   v
+----------------+      +--------------------+   +------------+
|  PASSIVE       |      |  PASSIVE THERMAL   |   |   ACTIVE   |
|  OPTICAL       |      |  (8-14 µm TIR)     |   |            |
|  (UV/VIS/NIR/  |      |  Earth emits own   |   | SAR: radar |
|   SWIR)        |      |  radiation 24/7    |   | LiDAR: laser|
|  Works daytime |      |  Works day+night   |   | Works any  |
|  clear sky     |      |  clear sky only    |   | time, wx   |
+----------------+      +--------------------+   +------------+
         |                          |                   |
         +----------+---------------+-------------------+
                    |
                    v
+------------------------------------------------------------------+
|               PROCESSING PIPELINE                                |
|  Raw DN -> Radiometric Cal -> Geometric Correction -> Ortho      |
|       -> Atmospheric Correction -> Analysis-Ready Data (ARD)     |
+------------------------------------------------------------------+
                    |
                    v
+------------------------------------------------------------------+
|               INFORMATION PRODUCTS                               |
|  Land cover maps, Vegetation indices, DEMs, Deformation maps     |
|  SST, Flood extents, Biomass estimates, Crop yield forecasts     |
+------------------------------------------------------------------+
```

---

## Passive vs. Active: The Core Split

```
PASSIVE                              ACTIVE
-----------------------------------------
Records ambient energy               Transmits own energy, records return
Sun -> surface -> sensor             Sensor -> surface -> sensor
No sun = no signal (visible)         Works at night, through cloud
Day only (optical)                   All-weather, day/night (SAR, LiDAR)
High spatial detail (sub-meter)      SAR: moderate (1-100m typical)
Many spectral bands possible         SAR: few "bands" but phase info
Dominated by surface reflectance     Backscatter = roughness + dielectric
Cannot measure topography directly   LiDAR measures 3D directly
Free: Landsat, Sentinel-2            LiDAR aircraft surveys: expensive
```

---

## The EM Spectrum Windows

Only certain wavelength ranges actually reach the sensor — atmospheric gases absorb or scatter the rest.

```
  WAVELENGTH (micrometers)
  0.2        0.4   0.7  1.0   1.5   2.5      8    14        1000
   |          |    |    |     |     |         |    |           |
   +--[XXX]---+====+====+=[X]=+====+=[XXX]===+====+====[====]+
              VIS  NIR   SWIR           MIR   TIR      MICROWAVE
               |    |     |                    |         |
              [1]  [2]   [3]                  [4]       [5]

[X] = atmospheric absorption windows (O3 blocks UV; H2O/CO2 block SWIR bands)
 =  = transmission window (sensor can see through here)

[1] Visible 0.4-0.7 um:    Blue/green/red. Vegetation color, water color.
[2] NIR 0.7-1.3 um:        Strong vegetation reflection (red edge). Biomass.
[3] SWIR 1.3-2.5 um:       Moisture stress, geology, snow/ice vs. cloud.
[4] TIR 8-14 um:           Land surface temperature. Volcanic heat. Night.
[5] Microwave 1mm-1m:      SAR. Penetrates cloud, rain, vegetation canopy.
```

---

## Platform Taxonomy

```
+------------------+----------+------------+----------+-----------+
| Platform         | Altitude | Swath      | Revisit  | Cost/km2  |
+------------------+----------+------------+----------+-----------+
| Geostationary    | 35,786km | full-disk  | 5-15 min | very low  |
| satellite        |          | (~11,000km)|          | (free)    |
+------------------+----------+------------+----------+-----------+
| LEO polar orbit  | 400-800km| 10-2900km  | days-wks | low/free  |
| (Landsat,        |          | (varies)   |          |           |
| Sentinel, Planet)|          |            |          |           |
+------------------+----------+------------+----------+-----------+
| Airborne         | 1-15km   | 0.5-50km   | on-demand| high      |
| (manned aircraft)|          |            |          |           |
+------------------+----------+------------+----------+-----------+
| UAV / drone      | 50-500m  | 0.05-5km   | on-demand| moderate  |
+------------------+----------+------------+----------+-----------+
| Ground-based     | surface  | point-100m | cont.    | high      |
| (TLS, phenocams, |          |            |          |           |
| eddy covariance) |          |            |          |           |
+------------------+----------+------------+----------+-----------+
```

---

## The Processing Pipeline

```
  +-------------+
  | Raw DN      |  Digital numbers from detector -- uncalibrated
  | (Level 0)   |  No physical meaning without sensor calibration
  +-------------+
        |
        v  RADIOMETRIC CALIBRATION
  +-------------+
  | At-sensor   |  DN -> radiance (W/m2/sr/um) using gain/offset
  | Radiance    |  Removes detector artifacts, normalizes bands
  | (Level 1)   |
  +-------------+
        |
        v  GEOMETRIC CORRECTION + ORTHORECTIFICATION
  +-------------+
  | Geolocated  |  Sensor model + GCPs + DEM -> map projection
  | Imagery     |  Removes terrain distortion (parallax effects)
  | (Level 1T)  |
  +-------------+
        |
        v  ATMOSPHERIC CORRECTION
  +-------------+
  | Surface     |  Remove atmospheric path radiance and absorption
  | Reflectance |  Methods: DOS, 6S/MODTRAN radiative transfer, LaSRC
  | (Level 2)   |
  +-------------+
        |
        v  ANALYSIS + PRODUCT GENERATION
  +-------------+
  | ARD /       |  Indices (NDVI, NBR), land cover classification,
  | Products    |  temperature retrieval, deformation maps, flood extent
  | (Level 3+)  |
  +-------------+
```

The physical meaning of the pipeline: each step removes an instrument or atmospheric artifact, leaving only the Earth-surface signal. Without atmospheric correction, you cannot compare images from different dates or sensors — the atmosphere is a different "filter" each day.

---

## Key Missions at a Glance

| Mission | Agency | Sensor Type | Resolution | Bands | Revisit | Archive |
|---------|--------|-------------|------------|-------|---------|---------|
| Landsat 9 | USGS/NASA | OLI-2 + TIRS-2 | 30m / 100m | 11 | 16 day | 1972-- free |
| Sentinel-2 A/B | ESA | MSI (passive optical) | 10/20/60m | 13 | 5 day | 2015-- free |
| Sentinel-1 A/B | ESA | C-band SAR | 5x20m IW | HH/VV/HV/VH | 6 day | 2014-- free |
| MODIS | NASA | Spectroradiometer | 250m-1km | 36 | daily | 2000-- free |
| NISAR | NASA/ISRO | L+S band SAR | 3-10m | dual pol | 12 day | 2024-- |
| Planet Dove | Planet Labs | Multispectral | 3-5m | 8 | daily | commercial |
| ICESat-2 | NASA | Photon-counting LiDAR | 17m footprint | 532nm | 91 day | 2018-- |
| GOES-18 | NOAA | ABI (16-channel imager) | 500m-2km | 16 | 5-15 min | 2022-- free |
| WorldView-3 | Maxar | Multispectral + SWIR | 0.31m PAN | 29 | 1-4 day | commercial |
| EMIT | NASA/JPL | Hyperspectral (ISS) | 60m | 285 bands | varies | 2022-- free |

---

## Connection to GIS and Earth System Science

Remote sensing is the primary data input layer for GIS and Earth system models.

```
REMOTE SENSING                    GIS / EARTH SYSTEM MODELING
+-------------------+            +-------------------------+
|  Satellite imagery|  ------>   |  Vector + raster layers |
|  SAR backscatter  |  ------>   |  Land cover maps        |
|  LiDAR point cloud|  ------>   |  DEMs, terrain analysis |
|  Thermal infrared |  ------>   |  LST products           |
|  Microwave SSM/I  |  ------>   |  Snow/ice/soil moisture |
+-------------------+            +-------------------------+
                                          |
                                          v
                               +-------------------------+
                               |  Earth System Models    |
                               |  Climate models (CMIP6) |
                               |  Carbon cycle models    |
                               |  Hydrological models    |
                               |  Crop yield models      |
                               +-------------------------+
```

The field sits at the intersection of physics (radiative transfer), engineering (sensor design, orbital mechanics), signal processing (SAR coherence, LiDAR waveform), and geoscience/ecology (interpreting what the numbers say about the real world).

---

## Section Map

| File | Topic |
|------|-------|
| 01-EM-SPECTRUM.md | Atmospheric windows, scattering, absorption, Planck function |
| 02-PASSIVE-SENSORS.md | Multispectral, hyperspectral, thermal -- calibration to products |
| 03-ACTIVE-SENSORS-SAR.md | SAR principles, polarimetry, backscatter physics |
| 04-LIDAR.md | Time-of-flight, point clouds, airborne/terrestrial/space LiDAR |
| 05-SATELLITE-ORBITS.md | SSO, repeat cycles, revisit vs. resolution trade-off |
| 06-IMAGE-PROCESSING.md | Geometric correction, atmospheric correction, classification |
| 07-INSAR.md | Interferometric SAR: DEM generation, deformation monitoring |
| 08-PLATFORMS.md | Landsat, Sentinel, MODIS, NISAR, Planet -- specs and archives |
| 09-APPLICATIONS.md | Agriculture, forestry, urban, disaster, cryosphere, ocean |

---

## Common Confusion Points

**"Remote sensing = satellite imagery"** -- No. Remote sensing includes airborne LiDAR, ground-based radiometers, underwater sonar, and medical imaging. Satellite is just the most visible platform context.

**"Passive sensors see through clouds"** -- Only passive microwave sensors (SSM/I, AMSR-2) can. Optical passive sensors (Landsat, Sentinel-2, MODIS) require clear sky. This is why SAR is critical for tropical regions with persistent cloud cover.

**"Higher resolution = better"** -- Resolution trades against swath width, revisit frequency, and cost. A 0.3m commercial image covers a tiny area once per week at high cost. A 30m Landsat image covers a continent every 16 days free. Better depends entirely on the scientific question.

**"Level 2 surface reflectance = ready to use"** -- It's atmospherically corrected but may still need cloud masking, co-registration, and validation. USGS ARD (Analysis Ready Data) does most of this preprocessing automatically.

**Reflectance vs. radiance**: Reflectance is dimensionless (0-1 scale), the ratio of reflected to incoming solar irradiance -- comparable across dates and sensors. Radiance (W/m2/sr/um) depends on sun angle and atmosphere -- not directly comparable between scenes.
