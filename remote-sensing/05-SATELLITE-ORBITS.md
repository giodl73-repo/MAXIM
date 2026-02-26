# Satellite Orbits: Mechanics, Sun-Synchronous, Revisit Trade-offs

## The Big Picture

The orbit a satellite occupies determines what it can see, when, and how often. Remote sensing missions are mostly in Low Earth Orbit (LEO), with a subset in Geosynchronous (GEO). The dominant LEO design for Earth observation is the **Sun-Synchronous Orbit (SSO)**: a near-polar orbit whose precession exactly compensates for Earth's revolution around the Sun, ensuring the satellite always crosses the equator at the same local solar time.

```
ORBIT ALTITUDE CLASSES

  GEO 35,786 km  +-----------+  Full disk coverage, fixed position
                 |  GOES     |  5 min refresh, ~2km resolution
                 |  Meteosat |  Cannot see poles well
  +-----------+  |  Himawari |
                 +-----------+

   MEO 2,000-   +-----------+  GPS, GLONASS (nav, not EO)
   35,786 km    |  GPS      |
                +-----------+

   SSO 400-     +-----------+  Most EO missions
   1000 km      |  Landsat  |  Near-polar sun-synchronous
                |  Sentinel |  10-16 day full coverage
                |  Planet   |
                +-----------+

   ISS 408 km   +-----------+  Inclined orbit (51.6 deg)
                |  ISS      |  Not sun-synchronous
                |  EMIT     |  Limited to 51.6 deg N/S latitude
                |  GEDI     |
                +-----------+
```

---

## Keplerian Orbital Elements

Six numbers completely specify an orbit:

```
  a = semi-major axis (size: determines period via Kepler's 3rd law)
  e = eccentricity (shape: 0=circle, 1=parabola)
  i = inclination (tilt relative to equatorial plane)
  RAAN = right ascension of ascending node (longitude of ascending node)
  omega = argument of perigee (where in orbit is closest approach)
  nu = true anomaly (where the satellite is now along the orbit)

For circular LEO EO missions:
  e ~ 0 (circular orbit)
  a ~ 6778 km (= 6371 km Earth radius + 407 km altitude)
  i ~ 97-99 degrees (retrograde! slightly more than 90 deg for SSO)
```

**Kepler's Third Law for circular orbit**:
```
  T^2 = (4*pi^2 / mu) * a^3

  mu = G * M_Earth = 3.986e14 m^3/s^2
  T = 2*pi * sqrt(a^3 / mu)

  At a = 6778 km:  T = 92.6 minutes (~15 orbits/day)
  At a = 7178 km:  T = 100 minutes (~14.4 orbits/day)
```

---

## Sun-Synchronous Orbit: The Engineering

The Earth is not a perfect sphere -- the equatorial bulge (J2 perturbation) causes orbital plane precession. SSO exploits this:

```
NATURAL PRECESSION (J2 effect)

  For a satellite at inclination i and altitude h:
  dRAAN/dt = -3/2 * (R_E/a)^2 * (J2/T) * cos(i)

  where J2 = 1.08263e-3 (Earth's oblateness coefficient)

  To match Earth's orbital rate around Sun: dRAAN/dt = +360 deg/year
    = +0.9856 deg/day (eastward)

  For prograde orbits (i < 90 deg), precession is westward (-cos).
  Need RETROGRADE orbit (i > 90 deg) to get positive precession.

  Typical SSO parameters:
    h = 705 km, i = 98.2 deg -> precession = +0.986 deg/day  [Landsat]
    h = 786 km, i = 98.6 deg -> precession = +0.986 deg/day  [Sentinel-2]
    h = 693 km, i = 98.2 deg -> precession = +0.986 deg/day  [Sentinel-1]
```

The result: the orbital plane maintains a fixed angle relative to the Sun-Earth line. The satellite crosses the equator at the same **Local Solar Time (LST)** on every pass.

```
WHY SAME LOCAL SOLAR TIME MATTERS

Without SSO:
  Pass 1: 10:30 AM -- shadows point southwest, sun angle 45 deg
  Pass 2 (3 months later): 4:00 PM -- shadows point east, sun angle 30 deg
  -> Images incomparable due to different illumination geometry

With SSO (e.g., 10:30 AM descending node):
  Every pass: 10:30 AM local solar time
  Sun angle, shadow length, illumination direction: consistent
  -> Time series analysis is valid
  -> Seasonal changes not confused with illumination changes
```

**Descending vs. ascending node**: Most optical EO satellites use a descending (south-going) daytime pass with local solar time ~10-11 AM. Sentinel-1 SAR uses ascending (north-going) pass. The morning (10 AM) time was chosen to minimize cloud cover (clouds tend to build in the afternoon).

---

## Repeat Cycle and Ground Track Geometry

A sun-synchronous satellite does not cover the same ground track every orbit. It has a repeat cycle after which the ground tracks exactly repeat:

```
GROUND TRACK GEOMETRY

  Each orbit advances by delta_lambda (deg) in longitude:
    delta_lambda = 360 / (orbits_per_day) - precession_per_orbit

  For Landsat 9 (16-day repeat, 233 orbits per cycle):
    Day 1: tracks 1, 18, 35, 52... (every 233rd track spacing)
    Day 2: tracks shifted by 1/16 of total ground width
    Day 16: full coverage achieved

  Landsat WRS-2: 233 paths (north-south strips), each 185km wide
    Adjacent paths overlap at equator: ~7.6 km overlap
    Adjacent paths overlap at 60 deg latitude: ~50%
    Polar regions: maximum overlap

  SWATH vs SPATIAL RESOLUTION TRADE:
    Wide swath (low GSD): MODIS 2330km, daily global
    Moderate swath (moderate GSD): Landsat 185km, 16-day global
    Narrow swath (high GSD): WorldView-3 13km, 1-4 day (opportunistic)
```

### Revisit Time vs. Resolution: Fundamental Trade-off

```
+------------------+--------+----------+---------+
| Sensor           | GSD    | Swath    | Revisit |
+------------------+--------+----------+---------+
| MODIS            | 250m   | 2330km   | daily   |
| Sentinel-2 A+B   | 10m    | 290km    | 5 days  |
| Landsat 9        | 30m    | 185km    | 16 days |
| SPOT-6/7         | 6m     | 60km     | 26 days |
| Planet Dove      | 3-5m   | 24km     | daily*  |
| SkySat           | 0.5m   | 6km      | 2-7 days*|
| WorldView-3      | 0.31m  | 13km     | 1-4 days*|
+------------------+--------+----------+---------+
* Constellation: many satellites, not single-orbit coverage
```

The fundamental trade-off exists because a satellite moves at fixed speed (~7.5 km/s). Wider field of view = larger image per pass = more ground covered = faster global repeat. But wider FOV means smaller telescope focal length for the same detector area = coarser GSD. You cannot escape this geometric constraint.

**Planet's solution**: launch hundreds of small satellites. 200+ Doves = daily global 3-5m coverage. The trade-off is dodged by adding more platforms, not changing per-satellite physics.

---

## Geostationary Orbit (GEO)

At 35,786 km, orbital period = 24 hours exactly. Satellite appears stationary relative to Earth.

```
GEO SATELLITES FOR REMOTE SENSING

  GOES (Geostationary Operational Environmental Satellites):
    GOES-West (135.4 W): covers western Americas + Pacific
    GOES-East (75.2 W):  covers eastern Americas + Atlantic
    Sensor: ABI (Advanced Baseline Imager), 16 channels
    Full disk every 15 min, CONUS every 5 min, mesoscale 60 sec

  ADVANTAGES:
    - Continuous temporal coverage (minutes to seconds)
    - Severe weather monitoring, hurricane tracking
    - Diurnal cycle resolved (watch clouds form and dissipate)
    - No revisit gap -- always staring at same area

  DISADVANTAGES:
    - Pixel size at nadir: 500m (visible), 2km (thermal)
    - Polar areas poorly observed (high off-nadir angle)
    - Parallax error for clouds at altitude (cloud top vs. bottom different position)
    - High orbit = weak signal -> requires large telescope for same SNR
    - Cannot do InSAR or lidar from GEO (not yet operational)
```

---

## Orbit Determination and GPS in Orbit

Modern EO satellites carry onboard GPS receivers for precision orbit determination (POD):

```
GNSS-based POD for EO satellites

  Onboard GPS receiver: records pseudorange + carrier phase
  Post-processing (ground): precise orbit determination
  Accuracy: 1-5 cm (for InSAR-quality orbits, key for Sentinel-1)

  Sentinel-1 POD specifications:
    Restituted orbit (3h after pass): 5 cm RMS
    Precise orbit (20 days after): 1 cm RMS
    -> Used for InSAR processing where orbit error = phase error

  Orbit error effect on InSAR:
    1 cm orbit error at 700km altitude -> ~0.5 mm phase error
    For mm-level deformation detection: precise orbits required
```

---

## Decision Cheat Sheet

| Requirement | Orbit Choice | Mission Examples |
|-------------|--------------|-----------------|
| Daily global optical | Low SSO + wide swath | MODIS, VIIRS |
| Daily global optical 3-5m | Constellation LEO SSO | Planet Dove |
| 5-day 10m optical | SSO, 290km swath | Sentinel-2 A+B |
| 16-day historical archive | SSO, 185km swath | Landsat |
| Minutes refresh, weather | GEO (35,786km) | GOES, Meteosat |
| Sub-meter commercial | SSO, narrow swath, tasking | WorldView, Pleiades |
| All-weather 6-day | SSO C-band SAR | Sentinel-1 |
| L-band SAR global 12-day | SSO L-band SAR | NISAR |
| Poles (ice, cryosphere) | SSO (near-polar coverage) | CryoSat-2, ICESat-2 |
| Continuous ocean/SST | GEO or daily-global LEO | GOES ABI, VIIRS |

---

## Common Confusion Points

**"Sun-synchronous" means the satellite orbits the Sun** -- No. Sun-synchronous means the orbital plane precesses at exactly the rate needed to maintain a constant angle with the Earth-Sun line. The satellite still orbits Earth.

**Inclination > 90 degrees = retrograde** -- SSO satellites fly slightly retrograde (west-to-east isn't quite right; they go south to north, but the orbital plane tilts slightly backward). An inclination of 98.2 degrees means retrograde by 8.2 degrees from polar. The equatorial bulge J2 then precesses the orbit eastward at 0.986 deg/day to match Earth's revolution.

**Revisit != repeat cycle** -- Landsat 9 has a 16-day repeat cycle. But if Landsat 8 is still operating, adjacent ground tracks are filled in by Landsat 8's offset orbit, giving an effective 8-day revisit. Sentinel-2A alone = 10-day revisit; A+B combined = 5-day revisit.

**Orbital altitude degrades over time** -- Atmospheric drag at LEO altitudes (especially < 600km) causes orbital decay. Satellites fire thrusters periodically to maintain altitude. ISS requires regular reboosts from visiting spacecraft due to drag at 408km altitude.
