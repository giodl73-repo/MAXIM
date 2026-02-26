# Active Sensors and SAR: Synthetic Aperture Radar

## The Big Picture

SAR (Synthetic Aperture Radar) transmits coherent microwave pulses and records both the amplitude and phase of the return signal. The "synthetic aperture" is the key trick: by processing the Doppler history of returns as the satellite moves along its orbit, it synthesizes an antenna far larger than physically possible. The result: fine azimuth resolution despite a small physical antenna, and penetration through cloud, smoke, and vegetation canopy.

```
SAR GEOMETRY
                      SATELLITE MOVING ->
                        |
            ............v............     AZIMUTH direction
          ..  SATELLITE TRACK         ..  (along-track, Doppler processed)
        ..                              ..
       | <---- RANGE direction -------> |  (cross-track, time delay)
       |        (slant range)           |
       |          /                     |
       |         /   LOOK ANGLE         |
       |        / theta                 |
       v       v                        v
  ----+-------+----------+-----------+-----   GROUND
      |NEAR   |          |           |FAR|
      |RANGE  |          |           |   |
      +-------+----------+-----------+---+
              <------- SWATH WIDTH ------>
```

---

## Range vs. Azimuth Resolution

These two dimensions are resolved by completely different physics:

```
RANGE RESOLUTION (cross-track)
  Determined by pulse bandwidth (chirp rate):
  delta_r_slant = c / (2 * BW)
  delta_r_ground = c / (2 * BW * sin(theta))

  where BW = transmitted bandwidth, theta = incidence angle
  Sentinel-1: BW = 100 MHz -> delta_r_slant = 1.5m
  Can be improved freely by increasing bandwidth -- no orbital constraint

AZIMUTH RESOLUTION (along-track)
  Real aperture: delta_az = lambda * R / D_real  (terrible: km scale)
  where lambda = wavelength, R = range, D_real = antenna length

  Synthetic aperture: delta_az = D_real / 2  (half the physical antenna length)
  INDEPENDENT OF RANGE AND WAVELENGTH
  Sentinel-1: antenna ~12m -> delta_az = 6m
  This is the key SAR magic: longer wavelength -> larger real aperture
  needed BUT azimuth resolution stays fixed at D_real/2
```

The synthetic aperture works because the satellite stores all coherent returns from a ground target over the entire time the target is within the antenna beam. The target enters the beam, stays lit for an integration time T_int, then exits. That time span defines the "synthetic aperture length." Doppler processing (a chirp compression in the frequency domain) focuses the returns to a fine point.

---

## SAR Frequency Bands: Penetration vs. Resolution Trade-off

```
BAND    WAVELENGTH    FREQUENCY    PENETRATION       RESOLUTION    SENSORS
-----------------------------------------------------------------------
Ka      0.8 cm        35 GHz      Surface only       Very fine     Experimental
Ku      1.7 cm        18 GHz      Surface            Fine          TerraSAR-X mode
X       3.1 cm        9.6 GHz     Low penetration    Fine (1-3m)   TerraSAR-X, COSMO
C       5.6 cm        5.3 GHz     Moderate           Moderate (5m) Sentinel-1, RADARSAT
S       9.4 cm        3.2 GHz     Moderate+          Moderate      NISAR (S-band)
L       24 cm         1.2 GHz     Deep (vegetation)  Coarser       ALOS-2, NISAR (L)
P       70 cm         0.43 GHz    Very deep (soil)   Coarser       BIOMASS (ESA)

KEY TRADE-OFF:
  Longer wavelength -> deeper penetration -> worse azimuth resolution
                    -> less affected by temporal decorrelation
                    -> larger antenna required for same delta_az

  C-band (Sentinel-1): balance of penetration, resolution, and hardware cost
  L-band (NISAR): deep vegetation penetration for biomass estimation;
                  also better coherence over forests for InSAR
  X-band: excellent for urban mapping and DEM generation (TanDEM-X)
```

---

## Backscatter Coefficient Sigma-0

The received power depends on four factors. The backscatter coefficient sigma^0 (sigma-naught, dB units) is the normalized radar cross-section:

```
sigma^0 depends on:

1. SURFACE ROUGHNESS (relative to wavelength)
   Smooth (water at low wind): specular reflection away from sensor -> LOW sigma^0
   Rough (urban, vegetation): diffuse scattering toward sensor -> HIGH sigma^0
   Bragg resonance: periodic surface roughness matching lambda -> sharp peak

2. DIELECTRIC CONSTANT (permittivity)
   High water content -> high dielectric constant -> stronger reflection
   Dry soil: epsilon_r ~ 3-5
   Wet soil: epsilon_r ~ 15-25
   Water: epsilon_r ~ 80
   Ice (fresh): epsilon_r ~ 3.2 (low -- transparent to radar)
   Sea ice (multiyear): complex mixture

3. GEOMETRY / INCIDENCE ANGLE
   Steep incidence: more surface scattering
   Shallow incidence: more volume scattering from canopy

4. SCATTERING MECHANISM
   Surface scattering: direct bounce off ground
   Volume scattering: multiple bounces within canopy or snowpack
   Double-bounce: tree trunk + ground corner reflector -> very bright
```

### Sigma-0 Typical Values (C-band, VV polarization, ~35 deg incidence)

| Surface | sigma^0 (dB) | Reason |
|---------|--------------|--------|
| Calm water | -25 to -15 | Specular, near-zero backscatter |
| Wet soil | -15 to -5 | High dielectric, rough surface |
| Dry soil | -20 to -10 | Low dielectric |
| Forest (closed) | -10 to 0 | Volume + double-bounce |
| Urban grid (aligned) | -5 to +15 | Double-bounce from building facades |
| Corner reflectors | +20 to +30 | Retroreflective geometry |

---

## Polarimetry: The Information Multiplier

A SAR transmits and receives in H (horizontal) or V (vertical) polarization. The polarimetric scattering matrix [S] relates transmitted to received:

```
       | S_HH  S_HV |   | E_H_received |      | E_H_transmitted |
  [S] =|             | = |              | from |                 |
       | S_VH  S_VV |   | E_V_received |      | E_V_transmitted |

For monostatic SAR: S_HV = S_VH (reciprocity theorem)
Quad-pol data: HH, VV, HV (= VH) -- 3 independent channels
Dual-pol (Sentinel-1 IW default): VV + VH, or HH + HV
Single-pol: VV or HH
```

### Pauli Decomposition

Decompose quad-pol covariance matrix into physically interpretable scattering mechanisms:

```
[k_Pauli] = (1/sqrt(2)) * [S_HH + S_VV, S_HH - S_VV, 2*S_HV]

Red  channel = |S_HH - S_VV| / sqrt(2) -> Double-bounce (buildings, tree trunks)
Blue channel = |S_HH + S_VV| / sqrt(2) -> Odd-bounce / surface scatter
Green channel = |2 * S_HV|   / sqrt(2) -> Volume scatter (vegetation, snow)
```

### Freeman-Durden 3-Component Decomposition

More sophisticated physical model:

```
sigma_0 = f_s * (surface scatter)  + f_d * (double-bounce) + f_v * (volume)

Surface: modeled as rough surface Bragg scatter
Double: modeled as dihedral corner reflector (trunk+ground)
Volume: modeled as randomly oriented dipoles (vegetation canopy)

Outputs: power fractions f_s, f_d, f_v summing to total power
Applications: forest cover, wetland detection, urban structure
```

---

## SAR Acquisition Modes

SAR systems trade swath width against resolution:

```
+----------------------+--------+----------+-------+---------------------+
| Mode                 | Swath  | Res(range| Looks | Use Case            |
|                      | (km)   | x azimuth)|      |                     |
+----------------------+--------+----------+-------+---------------------+
| StripMap             | 80km   | 5x5m     | 1     | Standard mapping    |
| ScanSAR (Sentinel IW)| 250km  | 5x20m    | 3-5   | Wide area, time     |
|                      |        |          |       | series (InSAR)      |
| Spotlight            | 10km   | 1-2m     | 1     | High-res urban,     |
|                      |        |          |       | ship detection      |
| Wide Swath (EW)      | 400km  | 20x40m   | 5     | Sea ice, ocean      |
| ScanSAR (RADARSAT-2) | 500km  | 25-100m  | 4+    | Global ocean        |
+----------------------+--------+----------+-------+---------------------+

Looks = number of independent looks averaged for speckle reduction
Multi-look: reduces speckle (coherent noise) at cost of resolution
```

---

## Coherence and Temporal Decorrelation

SAR coherence (gamma) measures how similar two complex images are over the same area:

```
gamma = |<S1 * conj(S2)>| / sqrt(<|S1|^2> * <|S2|^2>)

Range: 0 (incoherent, no phase relationship) to 1 (perfectly coherent)

DECORRELATION SOURCES:
  Temporal: surface changes between acquisitions -> decorrelates
  Spatial (baseline): slightly different viewing geometry -> geometry decorrel
  Thermal: noise in each SAR system -> small, usually negligible
  Volume: random scatterers in canopy -> volume decorrelation

TYPICAL COHERENCE VALUES (C-band, 6-day repeat):
  Urban (stable buildings): 0.7-0.9  (high: stable corner reflectors)
  Bare rock / dry soil:     0.5-0.8  (moderate-high)
  Agricultural crops:       0.1-0.4  (low: plants grow, move in wind)
  Tropical forest:          0.0-0.2  (very low: canopy motion + rain)
  Water surface:            ~0.0     (completely decorrelated each pass)

L-band penetrates to stable branches/trunks -> higher coherence in forest
C-band scatters from leaf canopy -> more temporal decorrelation
```

---

## Sentinel-1: The Operational Standard

Sentinel-1 A and B (C-band, free, open data) are the default for most SAR applications:

| Parameter | Value |
|-----------|-------|
| Frequency | C-band (5.405 GHz, lambda = 5.547 cm) |
| Primary mode | Interferometric Wide Swath (IW) |
| IW resolution | Range 5m x Azimuth 20m (single-look complex) |
| IW swath | 250 km (3 sub-swaths via TOPSAR burst mode) |
| Polarization | Dual: VV+VH (land), HH+HV (sea ice) |
| Revisit | 6-day (A+B combined over Europe), 12-day (A only) |
| Archive | 2014-present, free via Copernicus Open Access Hub |
| Data volume | ~4 GB/scene (SLC), ~700 MB (GRD) |

SLC = Single Look Complex (preserves phase for InSAR)
GRD = Ground Range Detected (detected amplitude, speckle filtered, geocoded)

---

## Decision Cheat Sheet

| Question | SAR Choice | Reason |
|----------|------------|--------|
| Flood mapping rapidly | Sentinel-1 GRD (C-band VV) | Water appears dark; C-band, free, 6-day |
| Earthquake deformation | Sentinel-1 SLC (for InSAR) | C-band coherence over rock/soil |
| Forest biomass mapping | ALOS-2 or NISAR (L-band) | Deep canopy penetration; less decorrelation |
| Urban change detection | TerraSAR-X Spotlight (X-band) | 1m resolution; high coherence buildings |
| Global ice monitoring | RADARSAT-2, Sentinel-1 EW | Wide swath; HH penetrates sea ice |
| Daily global change | Sentinel-1 ScanSAR (EW) | 400km swath, daily global coverage |
| Soil moisture | NISAR L-band, SMAP | Deep penetration to soil surface |
| Vegetation structure | BIOMASS P-band (2023+) | Deepest penetration; forest AGB |

---

## Common Confusion Points

**"SAR sees through anything"** -- Not exactly. SAR penetrates cloud (cloud droplets much smaller than microwave wavelength). But heavy rain (R > 10mm/hr) attenuates C-band significantly. X-band is affected by even moderate rain. L-band handles rain well but not ice-covered surfaces.

**Sigma-0 is in dB** -- values like -15 dB are normal. Do not interpret negative dB as "no signal." -15 dB = 0.032 in linear units. A swing from -20 dB to -5 dB (15 dB) is a factor of 31x in power.

**Speckle is not noise in the conventional sense** -- Speckle is a deterministic interference pattern from the coherent summation of many random scatterers within a resolution cell. It follows a negative exponential distribution (single-look) or chi-squared. Multi-looking (spatial averaging) reduces it but degrades resolution. Sophisticated speckle filters (Lee, Gamma-MAP, NL-SAR) trade resolution against noise.

**Azimuth resolution is NOT lambda*R/D** -- That is real-aperture resolution. SAR synthesis achieves D_real/2 regardless of range. A C-band satellite at 700km range with 12m antenna achieves 6m azimuth resolution. A real-aperture radar at the same geometry would need a 12km antenna for the same resolution.
