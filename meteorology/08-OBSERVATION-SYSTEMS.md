# Observation Systems — Radiosonde, Doppler Radar, Satellites

## The Big Picture

An NWP model is only as good as its initial conditions. Observations fill the atmosphere with data. The observing system is a heterogeneous network: surface stations, upper-air soundings, weather radar, geostationary satellites, polar orbiters, aircraft, and ocean buoys — each measuring different variables at different resolution, frequency, and coverage.

```
+------------------------------------------------------------------+
|              GLOBAL ATMOSPHERIC OBSERVING SYSTEM                  |
|                                                                   |
|  SPACE-BASED                                                      |
|  Geostationary (GOES-East/West, Meteosat, Himawari)              |
|  → Continuous imagery; lightning; AMVs                           |
|  Polar orbiters (NOAA-20, MetOp, Suomi NPP)                     |
|  → Soundings, sea ice, ocean color, ozone                        |
|  GPS Radio Occultation (COSMIC-2)                                |
|  → Temperature/humidity profiles globally                        |
|                                                                   |
|  AIR-BASED                                                        |
|  Radiosondes (~800 sites, 2x/day)                                |
|  Aircraft (AMDAR/ACARS; thousands of daily profiles)             |
|  Dropsondes (hurricane reconnaissance)                           |
|                                                                   |
|  SURFACE-BASED                                                    |
|  Weather radar (NEXRAD, C-band networks)                        |
|  Surface stations (ASOS, SYNOP, AWS)                            |
|  Ocean buoys (Argo floats, TRITON, TAO/TRITON array)            |
|  Profilers (wind, RASS temperature)                              |
+------------------------------------------------------------------+
```

---

## Radiosonde — Upper-Air Observation Workhorse

A radiosonde is an instrument package attached to a helium/hydrogen weather balloon:

```
PACKAGE COMPONENTS:
  Temperature sensor: thermistor rod (~1°C accuracy)
  Humidity sensor: hygristor or capacitance sensor
  Pressure: baroswitch or GPS altitude
  GPS tracking: wind from balloon drift (u, v at each level)
  Radio transmitter: 400–406 MHz

FLIGHT PROFILE:
  Launch: ~30–40 g balloon
  Ascent rate: ~5–6 m/s (balloon expands as P decreases)
  Altitude: ~30–35 km (balloon bursts; ~2 hour flight)
  Horizontal drift: up to 200 km from launch
  Data: T, Td, P, wind at each second of ascent

GLOBAL NETWORK:
  ~800 upper-air stations worldwide
  00 UTC and 12 UTC daily (0Z and 12Z, synoptic times)
  Sparse over ocean; polar regions; developing world
  → Major data gap filled by satellites
```

**Radiosonde data uses:** Initial conditions for NWP, sounding analysis (CAPE/CIN), pilot briefings, climatological records.

**SkewT-LogP soundings** — standard visualization format for radiosonde data. Temperature and dewpoint plotted vs log(pressure). Used operationally by forecasters to assess stability, cloud layers, precipitation type.

---

## Doppler Weather Radar

**NEXRAD (WSR-88D)** — US network of 160 S-band (10 cm wavelength) Doppler radars:

```
OPERATIONAL PARAMETERS:
  Wavelength: 10 cm (S-band)
  Frequency: 2.7–3.0 GHz
  Peak transmit power: 750,000 W
  Antenna diameter: 8.5 m
  Beamwidth: ~1°
  Rotation rate: ~3–6 RPM (volume scan: 5–6 minutes)
  Altitude range: ~460 m to ~80,000 m (distance-dependent)
  Range: ~460 km (Doppler wind ~230 km)

WHAT IT MEASURES:
  Reflectivity (Z): power returned by hydrometeors (rain/hail/snow)
  Velocity (V): Doppler shift = radial component of hydrometeor motion
  Spectrum width (W): turbulence/rotation within beam
  [Dual-pol adds: ZDR, CC, KDP]
```

**How Doppler velocity works:**

```
RADAR PULSE → hydrometeors → echo return
If hydrometeors MOVING TOWARD radar: higher frequency return (blue shift)
If hydrometeors MOVING AWAY: lower frequency (red shift)
If perpendicular: no Doppler shift

f_shift = 2V_r/λ

V_r = radial velocity (component toward/away from radar)

LIMITATION: Aliasing when V_r > Nyquist velocity
  V_nyquist = λ × PRF / 4  (PRF = pulse repetition frequency)
  At long range, PRF must be low → Nyquist velocity low → aliasing
  STAGGERED PRF (SZ-2 algorithm) partially resolves this
```

**Dual-polarization (2013 NEXRAD upgrade):**

```
TRANSMIT: Horizontal AND vertical pulses alternating

DIFFERENTIAL REFLECTIVITY (ZDR):
  ZDR = ZH/ZV (ratio of horizontal to vertical reflectivity)
  Large ZDR (+1 to +4 dB): oblate drops = large raindrops
  ZDR ≈ 0: spherical particles = small rain, hail (tumbling), snow

CORRELATION COEFFICIENT (CC or ρhv):
  1.0 = all same type (rain, snow)
  < 0.97: mixed types (rain+hail, debris, insects)
  < 0.8: tornado debris!

SPECIFIC DIFFERENTIAL PHASE (KDP):
  Proportional to liquid water content
  Immune to partial beam blockage and attenuation
  Better QPE in heavy rain

MELTING LAYER DETECTION:
  "Bright band" = ring of high reflectivity where snow melts
  → CC drops, ZDR enhanced → marks 0°C level altitude
```

**Tornado vortex signature (TVS)** — tight azimuthal velocity shear: gate-to-gate velocity difference ≥ 70 kt over < 2 km azimuthal width. Used for tornado warnings.

---

## Geostationary Satellites (GOES)

**GOES-16 (GOES-East) and GOES-18 (GOES-West)** — NOAA's current generation:

```
ORBIT: Geostationary (35,786 km altitude); appears fixed over equator
  GOES-East: ~75°W (covers Americas, Atlantic)
  GOES-West: ~137°W (covers western Americas, Pacific)
  Advantage: Continuous monitoring of same area
  Disadvantage: Lower resolution at high latitudes (oblique view)

ADVANCED BASELINE IMAGER (ABI):
  16 channels (6 visible, 10 infrared)
  Full-disk: 10-minute scan; CONUS: 5 min; Mesoscale: 1 min (severe weather)
  Resolution: 0.5 km (visible), 1 km (near-IR), 2 km (IR)

KEY CHANNEL USES:
  Band 2 (0.64 μm):     Visible; cloud structure during daylight
  Band 9 (6.9 μm):      Water vapor (mid-troposphere); jet streams
  Band 13 (10.3 μm):    "Clean IR window"; cloud top temperature
                        → cloud top height (cold = high top)
  Band 16 (13.3 μm):    CO₂ absorption; cloud top pressure

GEOSTATIONARY LIGHTNING MAPPER (GLM):
  Maps total lightning (CG + IC) continuously at 2-km, 2ms resolution
  → Rapid increases in IC lightning = updraft intensification
  → Lightning jump = tornado/severe weather precursor
```

**Atmospheric Motion Vectors (AMVs)** — track cloud features or water vapor features between successive images to derive wind vectors. Thousands of wind observations per image; critical input to NWP data assimilation over data-sparse regions.

---

## Polar-Orbiting Satellites

**NOAA-20, Suomi NPP, MetOp-A/B/C** — orbit ~830 km altitude, pole-to-pole:

```
ORBIT TYPE: Sun-synchronous (crosses equator at same local time each day)
Period: ~101 minutes → ~14 orbits/day
Ground track: Different swath each orbit; full global coverage ~daily

KEY INSTRUMENTS:
  CrIS (Cross-track Infrared Sounder): 1305 channels; T and H₂O profiles
  ATMS (Advanced Technology Microwave Sounder): Temperature, precipitable water
  VIIRS (Visible Infrared Imaging Radiometer Suite): Imagery, fire, sea ice, SST
  OMPS (Ozone Mapping and Profiler Suite): Ozone, SO₂ (volcanic)
  CERES (Clouds and Earth's Radiant Energy System): Earth's energy budget
```

**Microwave sounders vs infrared** — Microwaves penetrate clouds; infrared cannot. Microwave sounders provide temperature and moisture profiles even in cloudy regions — critical input for NWP in cloudy tropical areas.

**GPS Radio Occultation (RO)** — COSMIC-2 constellation: GPS signals bent by the atmosphere as they pass through the limb. Bending angle → refractivity → temperature + water vapor profiles. Extremely accurate; near-uniform global coverage; valuable in data-sparse ocean/polar regions.

---

## Surface Observation Networks

**ASOS (Automated Surface Observing System)** — US network of ~900 stations:
- Temperature, dewpoint, wind (direction + speed + gusts), visibility, ceiling
- Precipitation type and rate (heated tipping bucket + freezing rain sensor)
- Pressure (altimeter setting), sky condition (ceilometer)
- METAR format reports: hourly + special observations when conditions change

**Mesonet** — dense automated surface networks:
- Oklahoma Mesonet: 120 stations, 5-minute data; model for others
- AgriMet, CoCoRaHS (volunteer precipitation)
- Personal weather stations (Weather Underground, Tempest)

**Ocean Observations:**
- **Argo floats** — 4,000 autonomous floats; profile T + S to 2000 m depth every 10 days
- **TRITON/TAO buoys** — tropical Pacific array; ENSO monitoring
- **Drifting buoys** — surface T, pressure, location via satellite
- **VOS (Volunteer Observing Ships)** — merchant ships report weather obs

---

## Decision Cheat Sheet

| Observation need | Best source |
|-----------------|-------------|
| Current storm reflectivity/type | NEXRAD composite (high-res) |
| Tornado vortex detection | WSR-88D velocity + TVS algorithm |
| Hail vs rain discrimination | Dual-pol ZDR, CC, KDP |
| Upper-air T, humidity, wind profile | Radiosonde sounding (00Z/12Z) |
| Continuous mesoscale T, humidity, wind | ASOS + mesonet surface obs |
| Convective storm tops, rapid development | GOES mesoscale sector (1-min) |
| Lightning activity intensification | GOES-16 GLM lightning mapper |
| Hurricane intensity | Dropsonde (WC-130 reconnaissance) + SFMR surface wind |
| Ocean heat content (hurricane fuel) | Argo floats + altimetry |
| NWP data assimilation ocean/polar | Satellite sounders (CrIS, ATMS) + GNSS-RO |

---

## Common Confusion Points

**Radar range vs resolution** — NEXRAD has 460 km maximum range but the beam rises with distance (Earth curvature + beam propagation). At 250 km range, the lowest beam is ~5 km above ground → misses low-level features like tornadoes. "Cone of silence" directly above the radar (<0.5° elevation angle issues).

**Radar reflectivity and rainfall** — The Z-R relationship is empirical and highly uncertain. Dual-pol improves QPE but still has ~30–50% error. Gauges are the ground truth — radar is a spatial estimator, not a precision rain gauge.

**Geostationary vs polar** — Geostationary provides *continuous* time resolution but fixed location (lower resolution at high latitudes). Polar provides better resolution/coverage at all latitudes but only visits any given location twice daily. Both are needed.

**METAR vs TAF** — METAR is an *observation* (what's happening now). TAF is a *forecast* (Terminal Aerodrome Forecast, valid 24–30 hours). Both use similar coded format.
