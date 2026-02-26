# Earth Observation Platforms: Missions, Sensors, Archives

## The Big Picture

The EO platform landscape divides cleanly into free/government and commercial tiers, and within each tier by resolution and capability. The 2008 Landsat free data policy — and ESA's matching it with Sentinel in 2014 — transformed the field by enabling global-scale science that was previously cost-prohibitive.

```
EO MISSION LANDSCAPE

                    SPATIAL RESOLUTION
         COARSE (>250m)     MODERATE (10-100m)    FINE (<10m)
         |                  |                     |
  FREE   | MODIS (250m-1km) | Landsat 9 (30m)     | (rare -- EMIT 60m)
  /      | GOES (500m-2km)  | Sentinel-2 (10m)    |
  GOVT   | Suomi NPP VIIRS  | Sentinel-1 (5x20m)  |
         |                  | NISAR (3-10m)       |
  -------+------------------+---------------------+----
         |                  | RapidEye (5m) [end] | Planet Dove (3-5m)
  COMM-  |                  | SPOT-7 (6m)         | SkySat (0.5m)
  ERCIAL |                  | Pleiades (2m)       | WorldView-3 (0.3m)
         |                  |                     | Maxar (0.3m)
```

---

## Landsat Program: The 50-Year Record

No other EO system matches Landsat for archive depth and calibration consistency.

```
LANDSAT LINEAGE

  Landsat 1 (1972)  -> MSS: 4 bands, 80m, first 16-bit EO satellite
  Landsat 2 (1975)  -> MSS
  Landsat 3 (1978)  -> MSS + first TIR attempt (failed)
  Landsat 4 (1982)  -> TM: Thematic Mapper, 7 bands, 30m/120m -- major leap
  Landsat 5 (1984)  -> TM: operated 28.5 years (record)
  Landsat 6 (1993)  -> FAILED TO ORBIT
  Landsat 7 (1999)  -> ETM+: added 15m panchromatic, SLC-off failure 2003
  Landsat 8 (2013)  -> OLI + TIRS: 11 bands, 30m/100m, still operational
  Landsat 9 (2021)  -> OLI-2 + TIRS-2: improved radiometric resolution (14-bit)
```

### Landsat 9 Specifications

| Parameter | OLI-2 | TIRS-2 |
|-----------|-------|--------|
| Spectral bands | 9 (0.43-2.29 um) | 2 (10.9, 12.0 um) |
| Spatial resolution | 30m (15m pan) | 100m (resampled 30m) |
| Swath width | 185 km | 185 km |
| Radiometric resolution | 14-bit | 12-bit |
| SNR (representative) | >294:1 (NIR) | NEDT < 0.4 K |
| Repeat cycle | 16 days | 16 days |
| Orbit | Sun-synchronous, 705km, 98.2 deg | same |
| Equatorial crossing | 10:00 AM descending | same |

**Free archive access**: USGS Earth Explorer (earthexplorer.usgs.gov), Google Earth Engine, Microsoft Planetary Computer, AWS.

**Collection 2**: USGS reprocessed entire archive with consistent Level-2 surface reflectance algorithm (LaSRC). Collection 2 is the current standard -- do not mix with Collection 1.

**Landsat + Sentinel Harmonized (HLS)**: NASA product that harmonizes Landsat 8/9 and Sentinel-2 surface reflectance to a common grid (30m, MGRS tiles), BRDF-corrected. Enables combined time series. Available on LP DAAC.

---

## Sentinel Constellation (Copernicus Programme)

ESA's Copernicus is the European counterpart to Landsat -- free, open, operational.

### Sentinel-1: C-Band SAR

| Parameter | Value |
|-----------|-------|
| Frequency | C-band, 5.405 GHz (lambda = 5.547 cm) |
| Primary mode | IW (Interferometric Wide Swath): 250km, 5x20m |
| Secondary modes | EW (Extra Wide): 400km, 20x40m; SM (StripMap): 80km, 5m |
| Polarization | IW land: VV+VH; EW ocean: HH+HV |
| Revisit | 6 days (A+B), 12 days (A alone) |
| Orbit | SSO, 693km, 98.2 deg |
| Data volume | SLC ~4.5 GB, GRD ~700 MB per scene |
| Archive | 2014-present (S-1A), 2016-present (S-1B) |
| Access | Copernicus Data Space, ASF DAAC, Google Earth Engine |

**Note**: Sentinel-1B had a power anomaly in 2021 and was decommissioned in 2022. Sentinel-1C launched December 2023 to replace it. As of 2024, S-1A and S-1C together restore 6-day revisit.

### Sentinel-2: MultiSpectral Imager

| Band | Name | Center (nm) | Width (nm) | GSD |
|------|------|-------------|------------|-----|
| B1 | Coastal aerosol | 443 | 20 | 60m |
| B2 | Blue | 490 | 65 | 10m |
| B3 | Green | 560 | 35 | 10m |
| B4 | Red | 665 | 30 | 10m |
| B5 | Vegetation Red Edge | 705 | 15 | 20m |
| B6 | Vegetation Red Edge | 740 | 15 | 20m |
| B7 | Vegetation Red Edge | 783 | 20 | 20m |
| B8 | NIR | 842 | 115 | 10m |
| B8A | Narrow NIR | 865 | 20 | 20m |
| B9 | Water vapour | 945 | 20 | 60m |
| B10 | Cirrus | 1375 | 30 | 60m |
| B11 | SWIR-1 | 1610 | 90 | 20m |
| B12 | SWIR-2 | 2190 | 180 | 20m |

**Three red-edge bands (B5, B6, B7)** at 705/740/783nm: the key differentiator from Landsat. Red edge is highly sensitive to chlorophyll content and early stress detection.

**5-day revisit** (A+B): ~290km swath. Free Level-2A (surface reflectance) available. Tiled in 110x110km MGRS tiles.

---

## MODIS: The Global Daily Monitor

MODIS (Moderate Resolution Imaging Spectroradiometer) on Terra (morning) and Aqua (afternoon) provides daily global coverage since 2000.

| Parameter | Value |
|-----------|-------|
| Orbit | SSO, Terra: 10:30 AM descending; Aqua: 1:30 PM ascending |
| Swath | 2330 km |
| Bands | 36 (0.4-14.4 um) |
| Resolution | 250m (B1-2), 500m (B3-7), 1km (B8-36) |
| Temporal coverage | Terra: Feb 2000-present; Aqua: May 2002-present |
| Data access | LP DAAC, LAADS DAAC, NASA Earthdata, Google Earth Engine |

Key science products (all free):

| Product | Algorithm | Use |
|---------|-----------|-----|
| MOD09/MYD09 | 6S RT atmospheric correction | Surface reflectance, 7 bands |
| MOD11/MYD11 | Split-window LST | Land surface temperature 1km |
| MOD13/MYD13 | NDVI/EVI | Vegetation index 250m, 500m, 1km |
| MOD14/MYD14 | Thermal anomaly | Active fire detection global daily |
| MOD10/MYD10 | NDSI | Snow cover daily 500m |
| MOD17 | MOD15 LAI + climate | Gross primary production (GPP) |
| MCD43 | BRDF/Albedo | Corrected reflectance nadir view |
| MODOCGA | Ocean color | Chlorophyll concentration (Case 1) |

---

## NISAR: Next Generation L+S Band SAR

NISAR (NASA-ISRO Synthetic Aperture Radar) is a joint NASA-ISRO mission launched January 2024:

| Parameter | L-band | S-band |
|-----------|--------|--------|
| Wavelength | 24 cm (1.26 GHz) | 9.4 cm (3.2 GHz) |
| Resolution | 6m x 6m (InSAR mode) | 3m x 3m |
| Swath | 240 km | 240 km |
| Revisit | 12 days global | 12 days global |
| Polarization | Full pol option | Full pol option |

Science objectives:
- Cryosphere: ice sheet velocity, sea ice
- Solid earth: co/interseismic deformation, volcanic activity
- Ecosystem: forest biomass (L-band penetration), wetlands
- Hydrology: soil moisture, flood mapping

Dual-frequency: L penetrates vegetation, S provides complementary surface information. The combination enables biomass estimation that neither band alone can achieve.

---

## Commercial High-Resolution: Planet, Maxar, Airbus

### Planet Labs

```
DOVE CONSTELLATION (Planet Labs)
  200+ CubeSat 3U satellites in SSO
  Sensor: 4-band (B,G,R,NIR) + newer 8-band SuperDove
  GSD: 3-5m (PlanetScope)
  Swath: 24.6 km
  Revisit: daily (global), <1 day for most land areas
  Archive: 2014-present
  Access: Planet.com (subscription), some research programs free

SKYSAT CONSTELLATION
  21 satellites
  GSD: 0.5m (video capable: 30fps HD video)
  Swath: ~6.6 km
  Revisit: 2-7 days

BASEMAPS: Planet Global Basemap (monthly, quarterly) -- seamless cloud-free mosaic
```

### Maxar / WorldView Series

| Satellite | GSD (PAN) | GSD (MS) | Launch |
|-----------|-----------|----------|--------|
| WorldView-1 | 0.46m | -- | 2007 |
| WorldView-2 | 0.46m | 1.8m | 2009 |
| WorldView-3 | 0.31m | 1.24m | 2014 |
| WorldView-4 | 0.31m | 1.24m | 2016 (failed 2019) |
| Legion (6 sats) | 0.30m | 1.2m | 2021-2022 |

WorldView-3 unique: 8 SWIR bands (1195-2365nm) at 7.5m for mineralogy.

---

## Hyperspectral Missions in Detail

| Mission | Operator | Bands | Range | GSD | Status |
|---------|----------|-------|-------|-----|--------|
| PRISMA | ASI (Italy) | 250 | 0.4-2.5 um | 30m | Operational 2019, free |
| EnMAP | DLR (Germany) | 228 | 0.42-2.45 um | 30m | Operational 2022, free |
| EMIT | NASA/JPL (ISS) | 285 | 0.38-2.5 um | 60m | 2022--, free |
| DESIS | DLR/Teledyne (ISS) | 235 | 0.4-1.0 um | 30m | 2018--, free |
| HyperScout | cosine BV | 45 | 0.4-1.0 um | 30m | Commercial |

---

## Decision Cheat Sheet

| Need | Mission | Why |
|------|---------|-----|
| Historical change 1972+ | Landsat 1-9 | Only 50-year archive with consistent sensor calibration |
| Free 10m optical time series | Sentinel-2 A+B | 5-day revisit, free, 13 bands including red-edge |
| All-weather C-band SAR free | Sentinel-1 | 6-day revisit, free archive 2014+ |
| Daily global monitoring | MODIS, VIIRS | Wide swath, daily, 36 bands |
| Daily 3-5m global | Planet Dove | Constellation = daily everywhere |
| Sub-meter commercial | WorldView, Pleiades | 0.3-0.5m PAN, tasking |
| Vegetation biomass (SAR) | NISAR L-band | Deep penetration, 12-day global |
| Mineral mapping hyperspectral | EMIT, PRISMA, EnMAP | 30-60m, SWIR to 2.5 um |
| Weather + storm tracking | GOES-18, Meteosat | GEO, 5 min refresh, 16 channels |
| Global DEM free | Copernicus DEM (GLO-30) | 30m, from TanDEM-X, free since 2021 |

---

## Common Confusion Points

**Sentinel-1B failure (2022)** -- S-1B failed in December 2021. Until S-1C launched (December 2023), only S-1A was operating, cutting revisit from 6 to 12 days. Time series analyses must account for this gap.

**Landsat Collection 1 vs Collection 2** -- Collection 2 has reprocessed the full archive with improved calibration and new atmospheric correction algorithm (LaSRC). Do not mix C1 and C2 in the same time series. Earth Engine now serves C2 as default.

**Planet's "daily" coverage is probabilistic** -- Planet targets daily imaging but cloud cover, off-nadir tasking, and satellite passes mean actual clear acquisitions vary by region. In tropical areas, daily clear observations are rare even with daily tasking.

**MODIS is end-of-life** -- Terra launched 1999 (operating beyond design life), Aqua 2002 (same). Their successors are VIIRS on Suomi NPP (2011) and JPSS series. VIIRS has 5 imagery bands at 375m and 16 moderate-resolution bands. For long-term continuity, some products use MODIS+VIIRS combined.
