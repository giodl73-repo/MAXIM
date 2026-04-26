# 05 — Triangulation and Geodesy

## Measuring Earth Precisely

Geodesy is the science of measuring the Earth's shape, size, orientation in space, and gravitational field. It is the foundation on which all cartography rests: before you can make accurate maps, you need to know the accurate shape and size of what you're mapping. Geodesy makes cartography legally and scientifically defensible.

```
GEODESY PROBLEM HIERARCHY
══════════════════════════════════════════════════════════════════════

  LEVEL 1: What is the shape of the Earth?
  ├── First approximation: sphere (Eratosthenes, ~240 BCE)
  ├── Better: oblate spheroid (Newton, ~1687; confirmed ~1740)
  ├── Better still: reference ellipsoid (parameterized)
  └── Best physical approximation: geoid

  LEVEL 2: What reference surface do we use for coordinates?
  ├── Reference ellipsoid (mathematical approximation)
  │   defines latitude/longitude/height
  └── Geoid (physical surface of constant gravity)
      defines mean sea level / orthometric height

  LEVEL 3: How do we position features on this surface?
  ├── Historical: triangulation networks (angles + one baseline)
  ├── Modern: GNSS (GPS + GLONASS + Galileo + BeiDou)
  └── Both: combined in national geodetic surveys

  LEVEL 4: What datum are we using?
  ├── Each reference ellipsoid + positioning = a datum
  ├── NAD27, NAD83 (North America)
  ├── WGS84 (GPS global), ETRS89 (Europe)
  └── Local datums worldwide (hundreds exist)

══════════════════════════════════════════════════════════════════════
```

---

## Triangulation — The Core Method

Triangulation is the technique that enabled accurate national surveys before electronic measurement was possible. The principle is simple; the execution was heroic.

```
TRIANGULATION PRINCIPLE
══════════════════════════════════════════════════════════════════════

  STEP 1: Measure a baseline precisely
  ┌──────────────────────────────────────────────────────────┐
  │  A ─────────────────────────────────── B                 │
  │  ←────── known length L exactly ──────→                  │
  │                                                          │
  │  Method: lay calibrated rods end-to-end on flat ground   │
  │  UK Hounslow Heath baseline (1784): 5 miles,             │
  │  measured to 1.4 inches accuracy (error < 0.001%)        │
  └──────────────────────────────────────────────────────────┘

  STEP 2: Measure angles to a third point
  ┌──────────────────────────────────────────────────────────┐
  │               C                                          │
  │              /│\                                         │
  │             / │ \                                        │
  │            /  │  \                                       │
  │           /α  │  β\                                      │
  │  A ──────────────────── B                                │
  │                                                          │
  │  Instrument: theodolite (precision angle measurement)    │
  │  Measure: angle α at A, angle β at B                     │
  │  The triangle ABC is fully determined:                   │
  │  - Third angle γ = 180° - α - β                          │
  │  - Side AC = L × sin(β) / sin(γ)     (law of sines)      │
  │  - Side BC = L × sin(α) / sin(γ)                         │
  │  ∴ Position of C is known exactly                        │
  └──────────────────────────────────────────────────────────┘

  STEP 3: Extend the network
  ┌──────────────────────────────────────────────────────────┐
  │  C is now known → use AC and BC as new baselines         │
  │  Measure angles to new point D → position D              │
  │  Continue outward across the entire country              │
  │                                                          │
  │  Network of triangles covers entire territory            │
  │  Only ONE baseline measured directly (the rest derived)  │
  │  Error accumulates but slowly (random errors cancel,     │
  │  systematic errors managed by occasional baseline checks)│
  └──────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════
```

### The Power of Triangulation

A single precisely measured baseline of 8 km, combined with angle measurements at a few hundred points, can position features across a continent. The 19th-century Great Trigonometrical Survey of India covered 3 million km² using a single baseline measured at Sironj in 1800.

The instrument enabling this was the theodolite — a precision angle measurement device. The best 19th-century theodolites could measure angles to fractions of an arc-second (~0.0003°). At 100 km range, this corresponds to a positional error of roughly 0.5m.

---

## The Great Trigonometrical Survey of India (1802–1871)

The GTS is the most ambitious triangulation survey ever completed. It ran the length of the Indian subcontinent from south to north — approximately 2,400 km — in one continuous chain, and then extended across the subcontinent.

```
GREAT TRIGONOMETRICAL SURVEY — KEY FACTS
══════════════════════════════════════════════════════════════════════

  Director: William Lambton (1802–1823), then George Everest (1823–1843)
  Duration: ~70 years (1802–1871)
  Coverage: ~3 million km² of the Indian subcontinent

  Scale of operation:
  ├── Theodolite: Lambton's instrument weighed 500 kg
  │   Required 12 men to carry; required masonry towers to support
  ├── Triangulation towers: 30–60m tall, built from stone/brick
  │   Purpose: see over jungle canopy and intervening terrain
  ├── Field parties: 700+ men per team (porters, soldiers, workers)
  └── Duration per triangle: days to weeks per point (clearing
      vegetation, building towers, making measurements)

  Major achievements:
  1. First accurate measurement of the Indian subcontinent's extent
  2. Discovery that the Himalayas were taller than the Andes
     (previously assumed the Andes were the world's highest mountains)
  3. First measurement of "Peak XV" (later named Everest)
     as the world's highest mountain
  4. Detection of gravitational anomaly caused by Himalayan mass
     (deflection of plumb bob — see Geoid section below)

  The Everest calculation (1852):
  ┌────────────────────────────────────────────────────────────┐
  │  Radhanath Sikdar (mathematician/computer) calculated      │
  │  height of Peak XV from triangulation angles observed      │
  │  at 6 stations, 150–200 km from the peak                   │
  │                                                            │
  │  Required atmospheric refraction correction                │
  │  Required geoid undulation correction                      │
  │  Required parallax correction for Earth's curvature        │
  │                                                            │
  │  Result: 29,002 feet (8,839m)                              │
  │  Modern value: 8,848.86m (as of 2020 Chinese survey)       │
  │  Error: ~10m = 0.1%                                        │
  │  From 150km away, without ever setting foot near it        │
  └────────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════
```

The GTS also revealed something unexpected: the plumb bobs used to establish vertical reference were being deflected by the gravitational pull of the Himalayan mass. Plumb bobs define "vertical" — if you're measuring heights from a plumb bob reference and the plumb bob is pulled sideways by a mountain, your heights are wrong. This discovery led directly to the concept of the geoid.

---

## The Struve Geodetic Arc

Parallel to the Indian survey, Friedrich Georg Wilhelm Struve measured a meridian arc from the Black Sea to the Arctic Ocean (1816–1855) — a chain of 258 triangulation stations spanning 2,820 km across 10 countries (then: Norway, Russia, Finland, Estonia, Latvia, Lithuania, Belarus, Moldova, Ukraine, Romania).

The Struve Arc was the first accurate measurement of a long meridian arc, which allowed precise calculation of the Earth's shape parameters — specifically, the degree of polar flattening. It is a UNESCO World Heritage Site (2005).

---

## The Geoid — What "Sea Level" Actually Means

"Sea level" sounds simple. It is not. The mathematical concept required to define it precisely is the geoid.

```
GEOID — DEFINITION AND RELATIONSHIP TO OTHER SURFACES
══════════════════════════════════════════════════════════════════════

  THREE SURFACES:
  ┌──────────────────────────────────────────────────────────────┐
  │                     TOPOGRAPHIC SURFACE                      │
  │  (actual terrain — mountains, valleys, ocean floor)          │
  │                          ↕ terrain height above geoid        │
  │  ~~~~~~~~~~~~~~~~~~~ GEOID ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ │
  │  (equipotential surface of Earth's gravity field)            │
  │  (physically: where mean sea level would be everywhere)      │
  │  (deviates from ellipsoid by ±100m due to mass distribution) │
  │                          ↕ geoid undulation N                │
  │  - - - - - - - - - REFERENCE ELLIPSOID - - - - - - - - - -   │
  │  (mathematical approximation: flattened sphere)              │
  │  (used for coordinate calculations)                          │
  └──────────────────────────────────────────────────────────────┘

  WHAT THE GEOID IS:
  - The surface of equal gravitational potential (plus rotation)
  - Where water would settle if all the land were removed
  - The "physical" definition of sea level
  - Lumpy: pulls toward dense rock, away from less dense regions

  GEOID UNDULATION (N):
  h(ellipsoidal) = H(orthometric) + N
  where:
  h = GPS-measured height above ellipsoid
  H = actual height above sea level (orthometric)
  N = geoid undulation (±100m globally)

  PRACTICAL CONSEQUENCE:
  GPS gives ellipsoidal height (h).
  Engineering, elevation contours, flood mapping need orthometric height (H).
  You need a geoid model (EGM2008, GEOID18) to convert.
  Ignoring this error can be up to 100m in some regions.

══════════════════════════════════════════════════════════════════════
```

The geoid is lumpy because Earth's interior is not uniform. Dense rock (iron-rich crust, subducting slabs) pulls the geoid upward; less dense regions (oceanic crust, salt domes) pull it downward. The maximum geoid undulation is about +85m (in the Arctic Ocean, near Iceland) to about -106m (in the Indian Ocean, south of India). This is not a small effect.

---

## Reference Ellipsoids and Datums

```
REFERENCE ELLIPSOID — PARAMETERIZATION
══════════════════════════════════════════════════════════════════════

  An oblate spheroid (ellipsoid of revolution) is defined by:
  ├── Semi-major axis a (equatorial radius)
  ├── Semi-minor axis b (polar radius)
  └── Flattening f = (a-b)/a

  WGS84 (World Geodetic System 1984):
  ├── a = 6,378,137.0 m (equatorial radius)
  ├── b = 6,356,752.3 m (polar radius)
  ├── f = 1/298.257223563
  └── Used by GPS; the global standard today

  GRS80 (Geodetic Reference System 1980):
  ├── a = 6,378,137.0 m (same as WGS84)
  ├── f = 1/298.257222101 (very slightly different)
  └── Used by NAD83, ETRS89; essentially identical to WGS84

  Historical ellipsoids (still embedded in old datums):
  ├── Clarke 1866: used in NAD27 (North America)
  │   a = 6,378,206.4 m (bigger equatorial radius than WGS84)
  └── Airy 1830: used in OSGB36 (UK maps)
      a = 6,377,563.4 m

══════════════════════════════════════════════════════════════════════
```

### The Datum Problem — Why GPS Coordinates Don't Match Paper Maps

A datum is a combination of: a reference ellipsoid + an origin point + an orientation. Different datums produce different coordinates for the same physical location on Earth.

```
DATUM COMPARISON — NAD27 vs NAD83 vs WGS84
══════════════════════════════════════════════════════════════════════

  NAD27 (North American Datum 1927):
  ├── Ellipsoid: Clarke 1866
  ├── Origin: Meades Ranch, Kansas (the "center" of North America)
  ├── Orientation: fit to the North American triangulation network
  └── Problem: local fit to North America; poor globally;
      the US is not at the correct position on a global system

  NAD83 (North American Datum 1983):
  ├── Ellipsoid: GRS80 (essentially same as WGS84)
  ├── Origin: Earth's center of mass
  ├── Orientation: consistent with global VLBI measurements
  ├── Difference from NAD27: up to ~200m in horizontal position
  └── Difference from WGS84: millimeters (functionally same)

  WGS84 (World Geodetic System 1984):
  ├── Ellipsoid: WGS84 ellipsoid
  ├── Origin: Earth's center of mass
  ├── Used by: GPS, Google Maps, OpenStreetMap
  └── Updated: WGS84 is actually a series of realizations
      (G730, G873, G1150, G1674, G1762, G2139)
      each refined as GPS measurements accumulated

  PRACTICAL CONSEQUENCE:
  A geographic feature at NAD27 coordinates (45°N, 120°W)
  is NOT at the same physical location as WGS84 (45°N, 120°W).
  Difference: up to 200m in the contiguous US.

  Real-world problem:
  Old US paper maps: NAD27
  GPS receiver output: WGS84
  If you navigate with a GPS to old map coordinates,
  you can be 100–200m off your target.

══════════════════════════════════════════════════════════════════════
```

The conversion from NAD27 to NAD83 required resurveying the entire North American triangulation network — a decade-long project (1974–1983) using modern measurement technology. It shifted every benchmark position in the country by up to 200 meters.

---

## Modern Geodesy — GNSS and Plate Tectonics

The Global Navigation Satellite System era changed geodesy from a batch process (measure a triangulation network once, fix coordinates forever) to a continuous process.

```
MODERN GEODETIC MONITORING
══════════════════════════════════════════════════════════════════════

  GNSS PRECISE POINT POSITIONING:
  ├── GPS alone: ~3m horizontal accuracy (civilian, no augmentation)
  ├── WAAS/SBAS augmented: ~1m
  ├── DGPS (differential): ~0.3m
  ├── RTK (Real-Time Kinematic): ~1–2 cm horizontal
  └── Post-processed static: sub-cm to mm (survey standard)

  CONTINUOUS GPS NETWORKS:
  ├── CORS (Continuously Operating Reference Stations): 1,900+
  │   stations in US alone, run by NOAA/NGS
  ├── IGS (International GNSS Service): global network
  ├── Each station: records position every second, continuously
  └── Data used to:
      - Detect earthquake displacement (mm-level)
      - Measure tectonic plate motion (cm/year)
      - Monitor volcano inflation (uplift precedes eruption)
      - Detect subsidence (aquifer depletion, mine collapse)
      - Measure isostatic rebound (Scandinavia rising 5–10 mm/year
        as glacial ice load removed since last ice age)

  PLATE TECTONIC MOTION — MEASURED RATES:
  ├── Pacific Plate (Hawaii to Japan): ~7 cm/year
  ├── Atlantic spreading (Mid-Atlantic Ridge): ~2.5 cm/year
  ├── India subducting under Asia: ~5 cm/year
  └── San Andreas Fault (Pacific vs N. American): ~5 cm/year

  CONSEQUENCE FOR COORDINATES:
  North America moves ~2 cm/year relative to WGS84 frame.
  Over 10 years: 20 cm of motion.
  For sub-cm precision work (airport runways, tectonic studies):
  coordinates need a reference epoch and velocity model.

══════════════════════════════════════════════════════════════════════
```

ITRF (International Terrestrial Reference Frame) is the most precise geodetic reference frame, maintained by IERS (International Earth Rotation and Reference Systems Service). Coordinates in ITRF include a time component: position at epoch T, plus velocity vector. The GPS constellation is maintained to be consistent with the most recent WGS84 realization, which is itself consistent with ITRF.

---

## Arc Measurement and Earth's Shape

One of the great geodetic controversies of the 17th–18th century was: exactly what shape is the Earth's non-sphericity? Newton predicted an oblate spheroid (flattened at poles) from gravitational theory. The Cassini family (running France's national survey) argued from their measurements that the Earth was elongated at the poles (prolate).

```
THE PROLATE/OBLATE CONTROVERSY — RESOLUTION
══════════════════════════════════════════════════════════════════════

  THE QUESTION: does 1° of latitude represent a longer arc
  near the poles or near the equator?

  OBLATE (Newton): polar flattening → longer arc near poles
  PROLATE (Cassini): equatorial bulge → longer arc near equator

  RESOLUTION EXPEDITIONS (1735–1737):
  ┌──────────────────────────────────────────────────────────┐
  │  French Academy of Sciences sent two expeditions:        │
  │                                                          │
  │  Ecuador expedition (Bouguer, La Condamine):             │
  │  Measured arc near equator (1735–44)                     │
  │  Result: 1° arc = 110,613m                               │
  │                                                          │
  │  Lapland expedition (Maupertuis, Celsius):               │
  │  Measured arc near Arctic Circle (1736–37)               │
  │  Result: 1° arc = 111,909m                               │
  └──────────────────────────────────────────────────────────┘

  Polar arc > Equatorial arc → Newton was right → OBLATE
  (Maupertuis: "I have flattened the poles and the Cassinis")

  Measured flattening:
  Lapland/Ecuador expeditions: f ≈ 1/200 (too flat — instrument error)
  Modern (WGS84): f = 1/298.26 (very slightly oblate)

  PHYSICAL EXPLANATION:
  Earth's rotation → centrifugal effect → equatorial bulge
  Equatorial radius exceeds polar radius by ~21 km
  (6,378 km vs 6,357 km — difference of 21 km)
  This makes the summit of Chimborazo (Ecuador) farther
  from Earth's center than Everest (despite being ~2.6km lower
  in elevation), because of the equatorial bulge.

══════════════════════════════════════════════════════════════════════
```

---

## Vertical Datums and Height Systems

```
HEIGHT SYSTEMS — THE VERTICAL DATUM PROBLEM
══════════════════════════════════════════════════════════════════════

  ORTHOMETRIC HEIGHT (H): height above the geoid
  ├── What elevation contours, flood maps, engineering use
  ├── "Altitude above sea level" in common speech
  └── Measured by: spirit leveling (precise, slow) or
      GPS + geoid model (fast, slightly less precise)

  ELLIPSOIDAL HEIGHT (h): height above reference ellipsoid
  ├── What GPS directly measures
  └── Not directly useful for engineering (geoid is lumpy)

  NORMAL HEIGHT: quasi-geoid based (Helmert/Normal-Orthometric)
  └── Used in some national systems (Europe, Russia)

  EXAMPLE — PRACTICAL PROBLEM:
  ┌──────────────────────────────────────────────────────────┐
  │  GPS says you're at elevation 147m (ellipsoidal)         │
  │  Geoid undulation at your location: N = -31m             │
  │  Actual orthometric height: H = 147 - (-31) = 178m       │
  │                                                          │
  │  The 31m difference matters for:                         │
  │  - Flood plain determination                             │
  │  - Drainage design (water flows downhill by gravity,     │
  │    not down the ellipsoid)                               │
  │  - Building permits in flood-risk areas                  │
  └──────────────────────────────────────────────────────────┘

  NAVD88 (North American Vertical Datum 1988):
  ├── US standard orthometric vertical datum
  ├── Origin: Father Point/Rimouski tidal gauge, Quebec
  ├── Covers: continental US and Canada
  └── NAPGD2022 (replacement in progress): GNSS-compatible
      will eliminate the GPS→orthometric conversion burden

══════════════════════════════════════════════════════════════════════
```

---

## Common Confusion Points

**"Triangulation and trilateration are the same."** No. Triangulation measures angles; positions are derived from angles + one baseline. Trilateration measures distances directly. GPS uses trilateration (measuring signal travel time → distance). The Great Trigonometrical Survey used triangulation. Modern GNSS uses trilateration.

**"WGS84 and NAD83 are the same."** Functionally the same for civilian purposes (difference < 1m). Not the same for high-precision work. NAD83 is fixed to the North American tectonic plate; WGS84 tracks the ITRF which moves relative to North America. The current difference is ~1–2m and growing.

**"Geoid = ellipsoid."** No. The geoid is a physical surface (equipotential gravity field) that undulates by up to ±100m relative to the reference ellipsoid. GPS heights are ellipsoidal; engineering heights are orthometric (above geoid). You need a geoid model to convert between them.

**"The Himalayas are the highest mountains from Earth's center."** Chimborazo in Ecuador (6,268m elevation) is actually the farthest point from Earth's center (~6,384.4 km) because of the equatorial bulge, even though Everest (8,848m elevation) is higher above sea level. "Height" is relative to which reference surface you use.

---

## Decision Cheat Sheet

| Task | CRS / Datum | Why |
|------|------------|-----|
| GPS receiver coordinates | WGS84 (EPSG:4326) | GPS native datum |
| US engineering survey | NAD83 + NAVD88 (vertical) | Legal US standard |
| UK survey | OSGB36 / ETRS89 | UK legal standard |
| EU data exchange | ETRS89 | Pan-European standard |
| Global analysis | WGS84 or ITRF | Globally consistent |
| Flood/drainage design | Orthometric height (NAVD88) | Gravity-consistent heights |
| High-accuracy survey (<1cm) | ITRF + epoch | Accounts for plate motion |
| Web mapping | WGS84 + Web Mercator tiles | Industry convention |
