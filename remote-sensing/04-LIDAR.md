# LiDAR Systems: Airborne, Terrestrial, Bathymetric, and Space

## The Big Picture

LiDAR (Light Detection and Ranging) measures range by timing laser pulses. Unlike SAR's coherent microwave, LiDAR uses short-wavelength laser pulses (532nm-1064nm) to measure 3D structure at centimeter-level accuracy. The output is a point cloud: millions of (x, y, z) coordinate triplets with intensity and sometimes RGB color.

```
LIDAR TAXONOMY

                    LIDAR
                      |
        +-------------+-------------+
        |             |             |
   AIRBORNE      TERRESTRIAL     SPACE-BASED
   (ALB)         (TLS/MLS)       (ICESat-2,
                                  GEDI)
        |
   +---------+----------+
   |         |          |
 Discrete  Full       Photon
 return    waveform   counting
   |         |
 1-5 pulses Entire    ICESat-2: single photon
 per pulse  return    events. ~20 photons/m
 recorded   digitized
```

---

## Physics: Time-of-Flight Ranging

LiDAR measures distance using the travel time of a laser pulse:

```
LASER fires pulse at time t=0
         |
         | pulse travels at c = 3e8 m/s
         v
    TARGET (ground, tree, building, water surface)
         |
         | reflected pulse returns to detector
         v
DETECTOR records return at time t = 2R/c

Range: R = c * t / 2

EXAMPLE:
  Return time: 6.67 microseconds
  Range: (3e8 m/s * 6.67e-6 s) / 2 = 1000 m exactly

RANGE RESOLUTION:
  Timing accuracy ~ 1 nanosecond -> range precision ~ 15 cm
  State-of-art: < 1 cm range accuracy
  Position accuracy: limited by GPS/IMU accuracy (typically 5-15cm absolute)
```

**Pulsed vs. continuous wave**:
- Pulsed (most LiDAR): single pulse, measure round-trip time. Unambiguous range up to c/(2*PRF). At PRF=200kHz: max range = 750m. Above this: range ambiguity.
- Continuous wave (phase-based): modulate CW laser, measure phase difference. Works for close-range TLS (< 100m). Cannot handle multiple simultaneous returns.

---

## Airborne LiDAR: System Architecture

```
AIRBORNE LIDAR SYSTEM (ALS / ALB)

+-------+   +--------+   +-------+   +-------------+
| Laser | ->| Scanner|-> | Optics|-> | Detector    |
| (1064 |   |(rotating    | beam  |   | (APD: Avalanche
|  nm)  |   | mirror,|   | expand|   | PhotoDiode) |
+-------+   | polygon|   +-------+   +-------------+
            | or MEMS|                     |
            +--------+                     v
                                    +-------------+
+-------+   +-------+              | Waveform    |
| GNSS  | ->| IMU   |              | digitizer   |
| (GPS/ |   |(3-axis|              | (discrete   |
| GLONASS   | accel +              |  return OR  |
+-------+   | gyro) |             | full waform)|
            +-------+             +-------------+
                |                       |
                v                       v
         +-------------------------------+
         |    Direct Georeferencing      |
         |  Position + Attitude -> X,Y,Z |
         +-------------------------------+
                        |
                        v
                   POINT CLOUD
              (x, y, z, intensity, return#)
```

### Survey Design Parameters

| Parameter | Typical Range | Trade-off |
|-----------|---------------|-----------|
| Flying altitude | 500-2000m AGL | Low = dense pts, small swath; High = sparse pts, wide swath |
| Pulse repetition freq (PRF) | 50-400 kHz | High PRF = more pulses = higher density OR higher speed |
| Scan angle (half-angle) | 15-25 deg | Wide = wider swath but lower density at edges |
| Scan frequency | 50-200 Hz | High = denser across-track points |
| Point density | 1-50 pts/m2 | Specification depends on application |
| Swath width | 200-1000m | Function of altitude and scan angle |

**Required point density by application**:
- Vegetation structure (canopy height model): 2-8 pts/m2
- Topographic mapping (bare earth DEM): 1-2 pts/m2
- Building extraction: 10-20 pts/m2
- Powerline detection: 30-50 pts/m2

---

## Discrete Return vs. Full-Waveform

When a laser pulse hits vegetation, the return is not a single sharp spike -- it is a temporal distribution of energy corresponding to the vertical distribution of surfaces hit.

```
SINGLE PULSE FIRING INTO CANOPY

Outgoing pulse                   Return waveform

     |                              Top of canopy
     |   |                             /\
     |   |  sharp                     /  \      Mid-canopy
     |   |  pulse      ->            /    \/\ /\
     |                              /         \/  \
                                   /               \
                                  /                 \_ Ground return
                                  time -->

DISCRETE RETURN: firmware detects peaks, records time+intensity of each
  First return: top of canopy
  Last return: ground surface (if pulse penetrates canopy)
  Intermediate: mid-canopy layers

FULL WAVEFORM: digitizes entire return at 1-2 ns sample rate
  More information but larger data volumes
  Enables retrieval of sub-pulse structure
  Standard for research platforms (LVIS, G-LiHT)
  Becoming standard for commercial systems
```

### DEM/DSM/CHM Derivation

Three key surfaces extracted from airborne LiDAR:

```
DSM (Digital Surface Model): Highest return = top of everything
  Includes buildings, trees, anything above bare ground

DEM (Digital Elevation Model): Lowest return after ground filtering
  = Bare earth. Penetrates vegetation to ground.

CHM (Canopy Height Model): DSM - DEM
  = Height of vegetation above ground
  Used for forest biomass estimation, tree species discrimination

              CHM
              /\  Trees  /\
DSM ====/\====/  ========/  \====  Building
DEM ___/  \_____________________/  ______
```

**Ground filtering algorithms**: Separate ground points from above-ground points:
- **Progressive Morphological Filter (PMF)**: iteratively erodes non-ground points using morphological operators. Zhang et al. 2003.
- **Cloth Simulation Filter (CSF)**: simulates cloth draping over inverted point cloud. Effective on complex terrain.
- **LASGROUND (LAStools)**: commercial implementation, widely used in production.

---

## Terrestrial LiDAR (TLS / MLS)

Ground-based scanners map 3D structure at centimeter resolution from fixed or mobile platforms.

### TLS (Tripod-Mounted)

```
SCANNER AT FIXED STATION

         360-degree horizontal scan
         +/- 30-90 degree vertical scan
         Range: 5m to 1000m (depends on reflectivity)
         Point spacing: 1cm at 20m range

SCAN REGISTRATION: Multiple stations required for complete coverage
  Overlap between scans: >30%
  Registration targets: spheres, checkerboards
  Algorithm: ICP (Iterative Closest Point)
    1. Find nearest-neighbor correspondences
    2. Solve for rigid transformation (R, t) minimizing point distance
    3. Iterate until convergence
    4. Error: typically 3-10mm RMSE between scans

APPLICATIONS:
  Forest inventory: stem diameter, tree positions, crown shape
  Architecture/heritage: mm-level building surveys (point cloud to BIM)
  Industrial: as-built documentation, deformation monitoring
  Geomorphology: rockfall volumes, cliff erosion rates
```

### MLS (Mobile Laser Scanning)

Scanner mounted on vehicle/backpack. GNSS+IMU provides trajectory. Yields continuous corridor mapping at 5-20cm accuracy. Used for road inventory, powerline mapping, urban modeling.

---

## Bathymetric LiDAR

Standard 1064nm infrared laser cannot penetrate water (absorbed in top mm). Green 532nm wavelength penetrates to ~2-5 Secchi depths:

```
BATHYMETRIC LIDAR PHYSICS

  Infrared (1064nm) ----> surface return
  Green (532nm) ----+---> surface return
                    |
                    v  refraction at water surface (Snell's law)
                   |\
                   | \  beam bends toward vertical
                   |  \
                   v   \
              BOTTOM RETURN

  Depth determination:
    t_total = time to surface + time through water + time back
    depth = (t_bottom - t_surface) * c_water / 2
    c_water ~ 2.25e8 m/s (refractive index n = 1.33)

  Depth limit:
    Clear tropical water (attenuation k ~ 0.05/m): depth ~ 40-50m
    Turbid coastal water (k ~ 0.5/m): depth ~ 5-10m
    Rule of thumb: ~3 Secchi depths maximum

SYSTEMS:
  SHOALS / CZMIL: USACE survey workhorse
  Chiroptera (Leica): up to 50m depth in clear water
  EAARL (NASA): research, coral reef mapping
```

---

## Spaceborne LiDAR: ICESat-2

ICESat-2 (Ice, Cloud, and land Elevation Satellite-2) uses a photon-counting approach that is qualitatively different from traditional pulsed LiDAR:

```
ICESat-2 ATLAS INSTRUMENT

  Laser: 532nm, 10kHz pulse rate
  Photon-counting detectors: single photon sensitivity
  Ground footprint: 17m diameter per beam
  6 beams: 3 pairs (strong+weak) in 3 ground tracks
  Cross-track spacing: 3.3km between pairs
  Along-track spacing: 70cm (10kHz = one pulse per 70cm along track)

  Returns per meter: ~20 photons (canopy surface), ~2 (ground)

  ATL08 PRODUCT (land/vegetation):
    100m segment height statistics
    Terrain elevation (after noise photon filtering)
    Canopy height (98th percentile return height minus terrain)
    Canopy photon fraction
    RH metrics (relative height percentiles: RH25, RH50, RH75, RH98)

  NOISE CHALLENGE:
    Solar background photons ~10,000x signal during daytime
    Statistical filtering (ATLAS_SOC algorithm) separates signal from noise
    Night passes have much lower noise floor
```

**GEDI** (Global Ecosystem Dynamics Investigation): waveform LiDAR on ISS (2019-2023). Full-waveform at 25m footprint, global (51.6 deg latitude), 60m along-track spacing between footprints. Primary product: forest canopy height and above-ground biomass estimates globally.

---

## Point Cloud Processing Pipeline

```
RAW POINT CLOUD
  (x, y, z, intensity, return_number, gps_time)
        |
        v  COORDINATE TRANSFORMATION
  Projection to map coordinates (UTM, etc.)
  Requires trajectory (GNSS/IMU), flight parameters
        |
        v  NOISE REMOVAL
  Statistical outlier removal (k-NN distance threshold)
  Low-noise filter (isolated points below terrain)
        |
        v  GROUND CLASSIFICATION
  PMF / CSF algorithms
  Labels each point: ground (class 2) or non-ground
        |
        v  SURFACE GENERATION
  DEM from ground points (IDW or TIN interpolation)
  DSM from highest points (first returns)
  CHM = DSM - DEM
        |
        v  FEATURE EXTRACTION
  Individual tree segmentation (watershed on CHM)
  Building detection (height + planarity)
  Power line extraction (cylinder fitting)
```

---

## Decision Cheat Sheet

| Application | LiDAR Type | Key Specs |
|-------------|------------|-----------|
| Bare-earth DEM for hydrology | Airborne (discrete) | 2 pts/m2, ground filter |
| Forest canopy height and AGB | Airborne (full waveform) or ICESat-2 | GEDI ATL08/GEDI L4A |
| Coral reef mapping | Bathymetric LiDAR | 532nm, clear water limit |
| Building 3D models | TLS or airborne dense | 20+ pts/m2 |
| Road / powerline corridor | MLS | 10cm accuracy, continuous |
| Global vegetation structure | ICESat-2, GEDI | Space LiDAR, sampling |
| Rockfall / cliff erosion | Repeat TLS (multi-epoch) | Sub-cm change detection |
| Archaeological site mapping | Airborne, dense | Penetrate forest canopy |

---

## Common Confusion Points

**LiDAR is not radar** -- LiDAR uses laser light (visible/near-IR); radar uses microwaves. Fundamentally different wavelength range, detectors, and propagation properties. LiDAR cannot penetrate cloud; radar can.

**First return is not always "top of canopy"** -- In sparse vegetation, the first return may hit the ground. Last return is not always the ground either -- in very dense forest, the pulse may not penetrate at all. Ground filtering algorithms, not return number, classify ground points.

**Point density is not constant across the swath** -- In a typical oscillating-mirror scanner, the mirror slows at the edge of each scan line, causing higher point density at the swath edges (edge effect). This must be accounted for in density normalization.

**ICESat-2 samples, it does not map** -- ICESat-2 measures along six narrow ground tracks separated by 3.3km. It is a profiling instrument, not an area mapper. Global statistics (mean canopy height) are valid; pixel-by-pixel maps require combining with wall-to-wall optical data.
