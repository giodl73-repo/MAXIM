# InSAR: Interferometric SAR — DEM Generation and Deformation Monitoring

## The Big Picture

InSAR (Interferometric Synthetic Aperture Radar) exploits the phase of SAR signals. Standard SAR uses amplitude (intensity); InSAR uses phase. Two SAR images of the same area from slightly different positions or times yield a phase difference map — an interferogram — that encodes topography (position difference) or surface deformation (time difference).

```
INSAR GEOMETRY

  Pass 1                Pass 2
  (S1)                  (S2)
    |                    |
    |  B = baseline      |  <- perpendicular baseline B_perp
    |  (spatial or       |     = geometric difference
    |   temporal diff)   |
    |                    |
    v                    v
   .______________________.
   |                      |
   |   SURFACE / DEFORMATION MAP                |
   |                      |
   phi_interferogram = phi_1 - phi_2

   phi contains:
     1. Topographic phase (depends on B_perp and height z)
     2. Deformation phase (depends on line-of-sight movement)
     3. Atmospheric phase delay (troposphere, ionosphere)
     4. Noise (decorrelation, thermal)
```

---

## Phase and Wavelength: The Measurement Principle

Each SAR image pixel has a complex value: amplitude and phase. Phase encodes the round-trip path length to the scatterer, modulo 2*pi (one wavelength = one full cycle = 2*pi radians):

```
phi = (4*pi / lambda) * R   (modulo 2*pi)

where R = one-way slant range, lambda = wavelength

Phase difference between two passes:
  delta_phi = phi_1 - phi_2 = (4*pi / lambda) * (R_1 - R_2)

  R_1 - R_2 = path difference due to:
    a) slightly different geometry (baseline -> topography)
    b) surface moved toward/away from sensor between passes (deformation)
    c) atmosphere changed (tropospheric water vapor, ionosphere)
```

### Sensitivity Numbers

```
DISPLACEMENT SENSITIVITY (line-of-sight)

  C-band (Sentinel-1): lambda = 5.547 cm
    One fringe (2*pi phase) = lambda/2 = 2.77 cm displacement
    mm-level precision with many measurements (PS-InSAR)

  L-band (ALOS-2): lambda = 23.6 cm
    One fringe = lambda/2 = 11.8 cm displacement
    Less sensitive to small deformation, but better coherence

TOPOGRAPHIC SENSITIVITY

  delta_phi_topo = (4*pi * B_perp * h) / (lambda * R * sin(theta))

  For TanDEM-X (X-band, 3.1cm, small baseline ~250m):
    1 fringe = ~7m height difference
    After phase unwrapping: global 12m DEM, 2m vertical accuracy

  For Sentinel-1 (C-band, large orbit tubes):
    Baselines typically 10-150m
    Less topographic sensitivity -> good for deformation (topo not saturated)
```

---

## From Interferogram to Deformation Map

Processing chain:

```
STEP 1: SAR IMAGE PAIR
  SLC_1 (date 1) + SLC_2 (date 2)
  Must be co-registered to sub-pixel accuracy (<0.01 pixel)
  Precise orbits required (Sentinel-1: 1cm orbit accuracy)

STEP 2: INTERFEROGRAM FORMATION
  phi_int = angle(SLC_1 * conj(SLC_2))
  Flattened by removing topographic phase estimated from DEM
  Result: fringes = deformation + atmosphere + noise

STEP 3: COHERENCE ESTIMATION
  |gamma| = |<SLC_1 * conj(SLC_2)>| / sqrt(<|SLC_1|^2> * <|SLC_2|^2>)
  Coherence map tells you where phase is trustworthy
  Low coherence regions (forest, water): mask out

STEP 4: FILTERING
  Goldstein filter: adaptive spectral filter in frequency domain
  Reduces phase noise, preserves fringe structure
  Filter strength alpha: 0=no filter, 1=maximum

STEP 5: PHASE UNWRAPPING
  Wrapped interferogram: phase values in (-pi, +pi)
  Must "unwrap" to recover continuous phase
  Algorithms: SNAPHU (Statistical-cost, Network-flow Phase Unwrapping)
              Region growing, Branch-cut methods
  Ambiguity: one wavelength = one fringe -> 2.8cm/fringe C-band

STEP 6: CONVERSION TO LOS DISPLACEMENT
  d_LOS = (lambda / 4*pi) * phi_unwrapped
  Units: cm or mm of line-of-sight displacement
  Not vertical displacement -- correction requires InSAR decomposition

STEP 7: GEOCODING
  Radar coordinates (range, azimuth) -> map coordinates (lat/lon)
  Requires DEM for precise geocoding
```

---

## DEM Generation: TanDEM-X

TanDEM-X uses two satellites flying in tight formation (simultaneous acquisition, no temporal decorrelation):

```
TanDEM-X CONFIGURATION

  TerraSAR-X + TanDEM-X: twin X-band satellites
  Fly in helix formation: baseline 150-500m perpendicular
  Same-pass interferometry: both receive same pulse from TerraSAR-X

  Single-pass (simultaneous): eliminates temporal decorrelation
  Both images at exact same time -> no vegetation motion, no deformation signal
  Pure topographic phase

  GLOBAL DEM PRODUCT:
    Coverage: global, 80N to 84S
    Resolution: 12m (0.4 arcsec), 30m, 90m (public)
    Vertical accuracy: 4m absolute, 2m relative (90% linear error)
    Available: 12m via DLR, 90m free, 30m Copernicus DEM (GLO-30)

  Copernicus DEM GLO-30 (30m): derived from TanDEM-X, free since 2021
    Replaced SRTM as standard DEM for most EO applications
    Significantly better in mountainous terrain than SRTM
```

---

## Deformation Applications

### Earthquake Coseismic Mapping

```
EARTHQUAKE EXAMPLE: 2003 Bam, Iran (Mw 6.6)
  Envisat ASAR (C-band), pre/post interferogram
  Swath: ~100km width, single scene
  Fringe rate at fault rupture: >20 fringes/km = saturated near epicenter

  WHAT YOU CAN MEASURE:
    Coseismic slip distribution (fault geometry + slip)
    Surface rupture location (fringe discontinuity)
    Far-field displacement field (compare to elastic dislocation models)
    Moment tensor verification (InSAR independent of seismology)

  InSAR has detected co- and post-seismic deformation for hundreds of earthquakes
  Sentinel-1 + free archive = nearly global coseismic monitoring
```

### Volcanic Inflation/Deflation

```
VOLCANIC MONITORING
  Magma intrusion into chamber -> surface inflation -> radar moves toward satellite
  Positive deformation (toward satellite) -> negative phase shift in interferogram

  EXAMPLE: Sierra Negra, Galapagos (2005 inflation)
    2.5m of vertical inflation detected by InSAR (ENVISAT)
    Inflation modeled as sill at 2.1km depth
    30-day precursor inflation before eruption

  L-band (ALOS-2): better coherence over rugged, vegetated volcanic terrain
  Sentinel-1: 6-day revisit -> near-real-time monitoring
```

### Urban Subsidence

```
SUBSIDENCE MONITORING
  Mexico City: built on lake bed (ancient Lake Texcoco)
  Ground water extraction -> clay consolidation -> subsidence
  InSAR measurement: 25-30 cm/year in some districts
  PS-InSAR: mm-level precision on individual buildings

  Other subsidence cases:
    Jakarta, Indonesia: 25 cm/yr (groundwater + load)
    Po Delta, Italy: natural compaction + gas extraction
    Houston Texas: 5-10 cm/yr historical
    Central Valley, California: drought-related, up to 60 cm/yr (2012-2016)
```

---

## Multi-Temporal InSAR: PS-InSAR and SBAS

Standard InSAR on a single pair is limited by decorrelation. Multi-temporal methods use time series of dozens of scenes:

```
PS-InSAR (Persistent Scatterer):
  Identify pixels that maintain phase coherence across many scenes
  PSs = individual bright stable reflectors (buildings, rocks, pylons)
  Dense urban: 100-1000 PSs/km2
  Rural: 1-10 PSs/km2

  Processing:
    1. Master-slave pairs: all scenes relative to one master
    2. Phase stability analysis: identify PSs (amplitude dispersion index < 0.25)
    3. Linear + seasonal deformation model fit at each PS
    4. Atmospheric phase screen (APS) estimation and removal
    5. Velocity map (mm/yr) at each PS

  Precision: 0.1-1 mm/yr velocity in good conditions

SBAS (Small BAseline Subset):
  Use all pairs with small spatial and temporal baselines
  Distributed scatterers (DS): averages over many scatterers in one pixel
  Better in rural, agricultural, lightly vegetated areas
  Trades PS density for coverage area

IMPLEMENTATIONS:
  GAMMA Remote Sensing (commercial): industry standard
  SNAP + StaMPS: free, widely used for research
  MintPy (NASA): Python, ISCE-compatible, ARIA products
  LiCSBAS: Sentinel-1 specific, automatic processing
  ARIA (JPL): automatic Sentinel-1 interferogram generation + ARIA-S1-GUNW products
```

---

## Coherence: What Decorrelates

```
TEMPORAL DECORRELATION BY LAND COVER (C-band, 6-day revisit)

  Urban: 0.7-0.95  (stable corner reflectors, buildings)
  Rock outcrop: 0.6-0.9 (stable, no change)
  Bare soil (dry): 0.5-0.8 (moisture variation degrades)
  Agriculture: 0.1-0.5 (plants grow, harvested, plowed)
  Forest (temperate): 0.1-0.3 (leaves move in wind, canopy changes)
  Forest (tropical): 0.0-0.15 (daily rain, fast growth -> rapid decor)
  Water surface: ~0.0 (random scattering each pass)

L-BAND ADVANTAGE (ALOS-2, NISAR):
  Longer wavelength: penetrates through leaf canopy to stable branches/trunks
  Coherence in tropical forest: 0.2-0.5 vs. 0.0-0.15 for C-band
  Critical for volcano monitoring and deforestation in tropics
```

---

## Decision Cheat Sheet

| Application | InSAR Approach | Sensor | Time Baseline |
|-------------|----------------|--------|---------------|
| Coseismic slip map | Single pair | Sentinel-1 | Shortest after quake |
| Volcanic inflation | Single pair or time series | Sentinel-1 / ALOS-2 | Days to weeks |
| Urban subsidence | PS-InSAR | Sentinel-1 | 5+ years archive |
| Infrastructure monitoring | PS-InSAR | Sentinel-1, TerraSAR-X | Annual |
| Agricultural deformation | SBAS | Sentinel-1 | Season-scale |
| Global DEM | TanDEM-X simultaneous | TanDEM-X | Same pass |
| Landslide early warning | Coherence change + PS | Sentinel-1 | 6-12 day pairs |
| Post-disaster damage map | Coherence ratio before/after | Sentinel-1 | Pre + immediate post |

---

## Common Confusion Points

**"Phase = displacement"** -- Phase wraps. One cycle (2*pi, one fringe) = lambda/2 displacement. You must unwrap the phase to get absolute displacement, and phase unwrapping can fail in areas of rapid deformation or low coherence.

**InSAR measures line-of-sight (LOS), not vertical** -- For a satellite at ~40 degree incidence angle, 1cm of vertical displacement appears as ~0.7cm of LOS displacement. Decomposing into vertical and horizontal components requires ascending + descending pass data.

**Atmospheric delay is a noise source, not just ignorable** -- A 1km atmospheric delay gradient (common in mountainous areas) can look like 1-2cm of deformation. Multi-temporal approaches (PS-InSAR) separate temporally uncorrelated atmosphere from slowly varying deformation. Single-pair InSAR cannot distinguish atmosphere from deformation.

**Coherence is not just about vegetation** -- Even urban areas can lose coherence if they change (construction, demolition). Water is always incoherent. Bare agricultural soil can be coherent in the dry season and incoherent after tillage. The temporal baseline matters: longer = more decorrelation in all land cover types.
