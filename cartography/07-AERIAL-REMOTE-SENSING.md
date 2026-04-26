# 07 — Aerial and Remote Sensing

## Seeing Earth from Above

Remote sensing is the acquisition of information about a surface without physical contact. Applied to Earth observation, it spans from 19th-century balloon photography to modern satellite constellations imaging the entire planet daily. The unifying thread: different parts of the electromagnetic spectrum reveal different properties of the surface, and each sensor technology opens a new layer of the world to systematic observation.

```
REMOTE SENSING — HISTORY AND TECHNOLOGY STACK
══════════════════════════════════════════════════════════════════════

  PLATFORM EVOLUTION:
  1858  Balloon (Nadar — first aerial photo, Paris)
  1880s Kite photography (Batut — systematic aerial surveys)
  1906  Pigeon camera (Neubronner — attached to carrier pigeons)
  1914+ Fixed-wing aircraft (WWI — systematic aerial survey)
  1946  V-2 rocket — first space photographs
  1956  U-2 spyplane — systematic denied-area photography
  1960  Corona — first reconnaissance satellite (film return)
  1972  Landsat 1 — first civilian multispectral satellite
  1986  SPOT 1 — French civilian high-resolution satellite
  1999  IKONOS — first 1m commercial satellite
  2000  SRTM — 11-day Space Shuttle radar mission, global DEM
  2010s Drone/UAV — accessible sub-meter mapping
  2013  Planet Labs — constellation for daily global coverage
  2015  Maxar (DigitalGlobe) — 31cm commercial resolution

  SENSOR EVOLUTION:
  ├── Optical (film): visible spectrum, analog
  ├── Optical (digital): visible spectrum, digital
  ├── Multispectral: multiple visible + near-IR bands
  ├── Hyperspectral: 100+ narrow spectral bands
  ├── Thermal infrared: surface temperature
  ├── LiDAR: active laser ranging (3D point cloud)
  └── SAR: synthetic aperture radar (microwave, all-weather)

══════════════════════════════════════════════════════════════════════
```

---

## Balloon and Kite Photography

Gaspard-Félix Tournachon, known as Nadar, was a French photographer and balloonist who took the first aerial photograph in 1858 — an image of Petit-Bicêtre (near Paris) from a tethered balloon at ~80m altitude. The photograph does not survive; the earliest surviving aerial photograph is from Boston, 1860 (James Wallace Black, from a balloon at ~400m altitude, showing downtown Boston).

Nadar's ambition was to use aerial photographs for topographic mapping. He correctly identified the potential — overhead imagery eliminates the perspective foreshortening that makes ground-level surveying difficult in complex terrain. However, 19th-century balloons were too unstable and cameras too slow to produce consistently mappable imagery.

Arthur Batut (1882) systematized kite photography for aerial survey: a kite at known altitude with a camera on a timer. The approach produced systematic overlapping images of agricultural land for crop assessment and cadastral survey. This is the first systematic remote sensing program for civilian geographic purposes.

The military recognized the value faster. By 1914, all major powers were developing aerial reconnaissance. The camera replaced the sketching observer in the observer aircraft role within the first year of WWI.

---

## WWI Aerial Survey — The Industrialization of Overhead Intelligence

```
WWI AERIAL PHOTOGRAPHY — SYSTEMATIC INTELLIGENCE
══════════════════════════════════════════════════════════════════════

  BEFORE WWI:
  - Aerial photos: curiosities, occasional survey use
  - Photo interpretation: no formal discipline
  - Coverage: sporadic, ad hoc

  BY 1918:
  - RFC (Royal Flying Corps) alone: 10,000 aerial photos/day
  - German: similar scale
  - Dedicated photo interpretation schools (stereoscopic methods)
  - Systematic sortie planning to cover specific areas
  - 4-hour turnaround: fly → develop → print → brief

  TECHNICAL METHODS:
  ┌──────────────────────────────────────────────────────────┐
  │  STEREOSCOPIC INTERPRETATION:                            │
  │  Two photos of same area from slightly different positions│
  │  → 3D effect when viewed with stereo viewer              │
  │  → height of features estimable from parallax            │
  │  → craters, trenches, fortifications classified          │
  │                                                          │
  │  OVERLAP PLANNING:                                       │
  │  Photos taken with 60% overlap (fore-aft)                │
  │  30% sidelap between flight lines                        │
  │  Enables stereo coverage; enables photogrammetry later   │
  └──────────────────────────────────────────────────────────┘

  INTELLIGENCE PRODUCTS:
  - Artillery target location (gun battery positions)
  - Trench mapping (daily updates as positions changed)
  - Camouflage detection (shadows, shapes)
  - Supply route identification
  - Bomb damage assessment (BDA — did it work?)

  LEGACY:
  The photo interpretation doctrine, overlap standards, and
  stereo analysis methods developed in WWI were used through
  WWII, Cold War aerial reconnaissance, and form the basis
  of modern photogrammetric survey standards.

══════════════════════════════════════════════════════════════════════
```

---

## Photogrammetry — From Stereopairs to 3D Measurement

Photogrammetry is the science of making measurements from photographs. The foundational insight: if you know where two cameras were when they took overlapping photos of the same scene, you can calculate the 3D position of anything visible in both photos from the parallax (the apparent shift in position between the two views).

```
PHOTOGRAMMETRIC MEASUREMENT PRINCIPLE
══════════════════════════════════════════════════════════════════════

  STEREO PAIR GEOMETRY:
  ┌──────────────────────────────────────────────────────────┐
  │    Camera 1                    Camera 2                  │
  │      ●                            ●                      │
  │     /|\                          /|\                     │
  │    / | \                        / | \                    │
  │   /  |  \                      /  |  \                   │
  │  /   |   \                    /   |   \                  │
  │ ─────────────────── TARGET ────────────────────────────  │
  │         ●                        ●                       │
  │         same feature visible in both images              │
  └──────────────────────────────────────────────────────────┘

  PARALLAX:
  Feature appears at different position in image 1 vs image 2.
  Parallax Δp = b·f / H (for vertical photography)
  where b = baseline (camera separation), f = focal length, H = height
  Height of feature = H - H·f / (f + p/2)

  REQUIREMENTS:
  ├── Known camera positions and orientations (or calculable from GCPs)
  ├── Overlapping images (60% fore-aft for stereo)
  ├── Ground Control Points (GCPs): surveyed points visible in photos
  │   for absolute positioning (connecting to real-world coordinates)
  └── Feature matching: identify same point in both images
      (human eye through stereoviewer; now computer vision)

  PRODUCTS:
  ├── Orthophoto: aerial photo corrected for relief displacement
  │   (flat, planimetrically correct — can measure distances)
  ├── DEM (Digital Elevation Model): raster of height values
  ├── DSM (Digital Surface Model): height including buildings/trees
  ├── DTM (Digital Terrain Model): bare-earth (veg/bldg removed)
  └── 3D point cloud: dense set of 3D measured points

  MODERN: Structure from Motion (SfM)
  ├── Many overlapping photos from any angle (drone, phone)
  ├── Computer vision finds matching features automatically
  ├── Bundle adjustment solves for camera positions + 3D structure
  └── Produces: point cloud → mesh → orthophoto + DEM
      (the iPhone LiDAR/photogrammetry apps use this)

══════════════════════════════════════════════════════════════════════
```

---

## CORONA — First Reconnaissance Satellite (Declassified 1995)

CORONA was a classified US satellite program that operated from 1960 to 1972. Its existence was publicly acknowledged in 1978; its imagery was declassified in 1995. The declassification created an immediate windfall for environmental scientists, archaeologists, and historians.

```
CORONA SATELLITE PROGRAM
══════════════════════════════════════════════════════════════════════

  TECHNICAL SPECIFICATIONS:
  ├── Orbital altitude: ~160 km
  ├── Resolution: ~2m (KH-4B, later missions)
  │   (Earlier KH-1: ~12m; improved progressively)
  ├── Film: exposed in orbit, recovered by film canister
  │   ("bucket" reentry capsule caught by aircraft over Pacific)
  ├── Camera: panoramic scan across ground track
  ├── Coverage: approximately 10M km² per mission
  └── Missions: 145 total (1960–1972); 102 returned usable imagery

  TECHNICAL CHALLENGE — FILM RETURN:
  ┌──────────────────────────────────────────────────────────┐
  │  No digital transmission possible in 1960                │
  │  Film exposed in orbit → put in reentry capsule          │
  │  Capsule separates → reenters atmosphere → parachute     │
  │  JC-130 aircraft "catches" parachute before it hits water│
  │  Film developed, duplicated, analyzed                    │
  │  Turnaround: days to weeks                               │
  │  Compare to: modern Maxar EarthWatch → image in hours    │
  └──────────────────────────────────────────────────────────┘

  INTELLIGENCE ACHIEVEMENTS:
  ├── First mission (1960): more Soviet territory photographed
  │   than all U-2 flights combined
  ├── Counted Soviet bomber/missile force
  │   (confirmed US was overestimating Soviet capability)
  ├── Identified ICBM deployment sites
  ├── Monitoring arms treaties verification (SALT)
  └── Global geodetic control — calibrated Soviet maps to WGS84

  SCIENTIFIC WINDFALL (post-1995 declassification):
  ├── Archaeological sites visible in 1960s imagery, now destroyed
  │   (Fertile Crescent site looting visible before/after)
  ├── Glacial retreat documented over 50+ year span
  ├── Historical land use change (deforestation, urbanization)
  ├── Wetland loss documented
  └── "Time machine" imagery for environmental baselines

══════════════════════════════════════════════════════════════════════
```

---

## Landsat — Multispectral Civil Monitoring

Landsat 1 (launched 1972, originally ERTS-1: Earth Resources Technology Satellite) was the first civilian Earth observation satellite. It established the paradigm of multispectral scanning that dominates satellite remote sensing today.

```
MULTISPECTRAL IMAGING — THE ELECTROMAGNETIC SPECTRUM AS TOOL
══════════════════════════════════════════════════════════════════════

  Different wavelengths reveal different surface properties:

  ┌────────────────────────────────────────────────────────────┐
  │  VISIBLE (0.4–0.7 μm): what the eye sees                   │
  │  ├── Blue (0.45–0.52 μm): atmosphere scatter, water depth  │
  │  ├── Green (0.52–0.60 μm): vegetation health (peak reflect)│
  │  └── Red (0.63–0.69 μm): vegetation chlorophyll absorption │
  │                                                            │
  │  NEAR-INFRARED (0.77–0.90 μm):                             │
  │  ├── Strong reflection by healthy green vegetation         │
  │  ├── Absorption by water                                   │
  │  └── Used for: NDVI (vegetation index), land/water boundary│
  │                                                            │
  │  SHORT-WAVE INFRARED (1.55–2.35 μm):                       │
  │  ├── Soil moisture content                                 │
  │  ├── Rock/mineral discrimination                           │
  │  └── Cloud vs snow discrimination                          │
  │                                                            │
  │  THERMAL INFRARED (10.4–12.5 μm):                          │
  │  ├── Surface temperature (not reflected — emitted)         │
  │  ├── Urban heat island mapping                             │
  │  ├── Volcanic activity, wildfire detection                 │
  │  └── Ocean/lake surface temperature                        │
  │                                                            │
  │  MICROWAVE (1 mm – 1 m): SAR (see below)                   │
  │  ├── Penetrates clouds (no atmospheric window needed)      │
  │  └── Night imaging possible (active — its own energy)      │
  └────────────────────────────────────────────────────────────┘

  FALSE COLOR COMPOSITES:
  ┌────────────────────────────────────────────────────────────┐
  │  RGB channels mapped to non-visible bands → false color    │
  │                                                            │
  │  Classic Landsat false color (bands 4-3-2 = NIR-R-G):      │
  │  - Healthy vegetation: bright RED (high NIR)               │
  │  - Urban areas: blue-grey                                  │
  │  - Bare soil: brownish                                     │
  │  - Water: dark blue to black                               │
  │                                                            │
  │  Why: red channel carries NIR (invisible to eyes) →        │
  │  vegetation shows as red because plants strongly reflect   │
  │  NIR but absorb visible red                                │
  └────────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════
```

### NDVI — Normalized Difference Vegetation Index

NDVI = (NIR - Red) / (NIR + Red)

Healthy green vegetation strongly reflects NIR and absorbs red. NDVI ranges from -1 to +1:
- NDVI > 0.5: dense healthy vegetation (tropical forest)
- NDVI 0.2–0.5: moderate vegetation (croplands, grasslands)
- NDVI < 0.1: bare soil, rock, water

NDVI is computed from every Landsat scene and has been used to:
- Monitor deforestation annually since 1972
- Track drought and desertification
- Estimate crop yields (food security forecasting)
- Monitor wildfire burn severity and recovery
- Detect illegal logging (sudden NDVI drop in forested areas)

The 50-year Landsat archive is one of the most scientifically valuable environmental datasets in existence.

---

## LiDAR — Active Laser 3D Mapping

LiDAR (Light Detection and Ranging) fires laser pulses at the surface and measures the travel time of the returned pulse. The result is a dense point cloud of 3D measurements.

```
LIDAR OPERATION — PRINCIPLE AND PRODUCTS
══════════════════════════════════════════════════════════════════════

  AIRBORNE LIDAR (typical):
  ├── Aircraft altitude: 600–2,000m
  ├── Laser pulse rate: 100,000–500,000 pulses/second
  ├── Scan angle: ±15–25° from nadir (scanning mirror)
  ├── Point density: 1–50 points/m² depending on altitude
  ├── Range accuracy: ~15 cm vertical, ~15 cm horizontal
  └── Result: dense point cloud (billions of points per dataset)

  MULTIPLE RETURNS:
  ┌──────────────────────────────────────────────────────────┐
  │  Laser pulse hits vegetation canopy:                     │
  │  - 1st return: top of canopy                             │
  │  - 2nd return: mid-canopy                                │
  │  - Last return: ground (through gaps in canopy)          │
  │                                                          │
  │  Multiple return recording enables:                      │
  │  - DSM (Digital Surface Model): from 1st returns         │
  │  - DTM (Digital Terrain Model): from last returns        │
  │  - Canopy height model: DSM - DTM                        │
  └──────────────────────────────────────────────────────────┘

  BARE-EARTH STRIPPING:
  Separate the last-return ground points from vegetation.
  Filter and interpolate → bare-earth DEM under forest cover.

  This is archaeology's killer application:
  Jungle-covered ruins are invisible in optical imagery
  but fully visible in bare-earth LiDAR DEM.

  ARCHAEOLOGICAL DISCOVERIES:
  ├── Caracol (Belize, 2010): 176 km² of Maya lowland city
  │   revealed in 10 hours of LiDAR vs 25 years on foot
  ├── Angkor Wat, Cambodia: extensive urban network
  │   previously unknown around the temple complex
  ├── Pacunam survey (Guatemala, 2018): 60,000+ Maya structures
  │   in 2,100 km² — showing Maya population ~10× previous estimates
  └── Medieval English field systems under forest cover

══════════════════════════════════════════════════════════════════════
```

### Terrestrial LiDAR

Ground-based LiDAR scanners (total station on steroids — capture millions of points in minutes) are used for:
- Building/facade documentation (architecture, historic preservation)
- As-built surveys (industrial plants, tunnels)
- Mine volumetric calculation
- Crime scene documentation
- Rock slope stability assessment (detecting millimeter movement)

---

## SAR — Synthetic Aperture Radar

SAR is the remote sensing modality that works when everything else fails: cloudy, rainy, dark, nighttime. It uses microwave energy (1cm–1m wavelength) that penetrates clouds and is not affected by solar illumination.

```
SAR — HOW IT WORKS AND WHAT IT SHOWS
══════════════════════════════════════════════════════════════════════

  PRINCIPLE — ACTIVE ILLUMINATION:
  ┌──────────────────────────────────────────────────────────┐
  │  Radar transmits microwave pulse toward Earth            │
  │  Pulse reflects off surface → returns to sensor          │
  │  Measure: amplitude (how much returned) + phase          │
  │  Time of return → distance → geometry                    │
  └──────────────────────────────────────────────────────────┘

  SYNTHETIC APERTURE:
  A real aperture radar would need an antenna km long to
  achieve high resolution. Instead:
  SAR uses the spacecraft's motion to synthesize a long
  aperture by combining returns from many positions along
  the flight track. The "aperture" is the flight path length.
  Result: high azimuth resolution without huge antenna.

  WHAT SAR SEES:
  ├── Surface roughness: rough surfaces backscatter more
  ├── Dielectric constant: affects reflectivity
  │   (water has high dielectric constant → dark in SAR)
  ├── Geometry: corner reflectors (buildings, edges) → bright
  ├── Urban areas: very bright (double-bounce off walls + ground)
  └── Vegetation: moderate return (volume scattering)

  KEY APPLICATIONS:
  ├── FLOOD MAPPING: water is dark (specular reflection away)
  │   Floods visible even under cloud cover → emergency response
  │
  ├── OIL SPILL DETECTION: smooth water surface → dark patches
  │
  ├── SHIP DETECTION: bright point targets in dark ocean
  │   (illegal fishing, military tracking)
  │
  ├── BUILDING DAMAGE ASSESSMENT:
  │   Compare pre/post earthquake/conflict SAR
  │   Damaged buildings change SAR signature
  │   Available within hours of event
  │
  ├── DEM GENERATION (InSAR):
  │   Two SAR images from slightly different positions
  │   Phase difference → topographic height
  │   SRTM (2000): 11-day shuttle mission using InSAR
  │   → first near-global 30m DEM
  │
  └── GROUND DEFORMATION (DInSAR):
      Phase difference between two dates → surface movement
      Millimeter accuracy over hundreds of km
      Used for: volcano monitoring, earthquake displacement,
      landslide detection, aquifer depletion subsidence

══════════════════════════════════════════════════════════════════════
```

### InSAR Applications in Detail

Differential InSAR (DInSAR) is one of the most powerful tools in modern geophysics. By comparing the radar phase of two images taken at different times, you can detect surface movement of millimeters to centimeters.

Applications:
- **Mexico City subsidence**: aquifer overexploitation causes the city to sink; some neighborhoods have subsided 10m since 1950, still sinking ~30cm/year — measurable with InSAR
- **Volcanic inflation**: magma intrusion inflates a volcano's summit by centimeters to meters before an eruption — InSAR provides early warning
- **Post-earthquake mapping**: the 2010 Haiti earthquake surface deformation was mapped by InSAR within days, guiding search and rescue priorities
- **Glacier flow**: Arctic and Antarctic ice sheet dynamics, flow rates, calving front positions

---

## The Electromagnetic Spectrum as Observational Tool

```
WAVELENGTH → WHAT YOU SEE — REFERENCE TABLE
══════════════════════════════════════════════════════════════════════

  Band        Wavelength   Platform      Primary use
  ──────────────────────────────────────────────────────
  Visible     0.4–0.7μm   Most sensors  Base imagery, RGB
  Near-IR     0.7–1.0μm   Multispectral Vegetation, water
  SWIR-1      1.0–1.7μm   Landsat, SPOT Soil moisture, minerals
  SWIR-2      1.7–2.5μm   Landsat       Mineral mapping
  Thermal IR  8–14μm      Landsat TIR   Surface temperature
  Microwave   1mm–100cm   SAR systems   Cloud penetration, deform

  Atmospheric windows (where atmosphere is transparent):
  ├── Visible + NIR: 0.3–1.4μm (with some absorption bands)
  ├── SWIR windows: 1.6μm, 2.2μm
  ├── Thermal window: 8–14μm
  └── Microwave: essentially transparent (weak water vapor abs)

  What clouds block: visible, NIR, SWIR, thermal
  What clouds don't block: microwave (SAR)

══════════════════════════════════════════════════════════════════════
```

---

## Modern Constellation — Daily Global Coverage

The economics of remote sensing changed fundamentally after 2013. Planet Labs launched constellations of small, cheap satellites ("Doves") — CubeSats about the size of a shoebox — rather than a few expensive large satellites.

| Constellation | Operator | Resolution | Revisit | Key feature |
|--------------|---------|-----------|---------|------------|
| PlanetScope | Planet | 3m | Daily | Daily global coverage |
| SkySat | Planet | 0.5m | Multiple/day | High resolution rapid tasking |
| WorldView-3 | Maxar | 0.31m | ~1 day | Highest commercial resolution |
| Sentinel-2 | ESA | 10m | 5 days | Free; 13 spectral bands |
| Landsat 8/9 | USGS/NASA | 30m | 16 days | Free; 50-year archive continuity |
| Copernicus SAR | ESA | 5m | 6 days | Free; C-band SAR |

The transition from "imagery as scarce intelligence asset" to "imagery as commodity" is complete. Planet Labs generates ~1 petabyte of imagery per day.

---

## Common Confusion Points

**"Remote sensing is just satellite photography."** Photography (optical passive imaging) is one modality. LiDAR (active optical), SAR (active microwave), and thermal (passive emitted infrared) reveal completely different aspects of the surface and cannot be substituted for each other.

**"LiDAR gives you the surface height."** LiDAR gives you a point cloud — heights at discrete measured points. You produce a DEM by interpolating between those points. The difference between DSM (includes buildings/trees) and DTM (bare earth) requires classification algorithms applied to the raw point cloud.

**"SAR images look like photographs."** SAR images look like photographs of a radar-reflective world, which is not the visual world. Smooth water is black. Rough water is lighter. Urban areas are very bright. Specular metal surfaces create bright artifacts. Interpreting SAR requires learning a different visual vocabulary.

---

## Decision Cheat Sheet

| Question | Sensor | Notes |
|----------|-------|-------|
| What is the surface look like? | Optical (RGB) | The visual baseline |
| How much vegetation is there? | NIR / NDVI | Landsat, Sentinel-2 |
| What is the surface temperature? | Thermal IR | Landsat Band 10/11 |
| 3D bare-earth terrain model | LiDAR | Best for archaeology, forestry |
| Works through clouds, at night | SAR | Sentinel-1, PALSAR |
| Millimeter surface movement | InSAR / DInSAR | Geophysics, infrastructure |
| Highest possible resolution | SkySat / WorldView | Commercial, costly |
| Free global coverage | Landsat, Sentinel | Best for research |
| Daily monitoring | PlanetScope | 3m, free for research |
| Building damage after event | SAR change detection | Available in hours |
