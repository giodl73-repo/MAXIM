# 09 — GPS and Digital Mapping

## From Atomic Clocks to Slippy Maps

GPS and the web mapping revolution it enabled are the two most consequential changes to everyday cartography in human history. In 2000, knowing your precise location required specialized equipment and expertise. By 2010, every smartphone carried a 3m-accurate positioning system and a vector-rendered map of the entire world. Understanding how this works — from orbital mechanics to tile servers to routing algorithms — is understanding the infrastructure underpinning modern navigation, logistics, and location-based services.

```
GPS → DIGITAL MAP STACK
══════════════════════════════════════════════════════════════════════

  POSITIONING:
  GPS satellites (orbital mechanics + atomic clocks)
    ↓ radio signals (L1/L2 frequencies)
  GPS receiver (trilateration → position fix)
    ↓ WGS84 (lat/lon/altitude)

  MAPPING DATA:
  OpenStreetMap contributors / Google surveys
    ↓ vector data (roads, POIs, buildings)
  Tile server (renders map tiles at each zoom level)
    ↓ z/x/y tile coordinates
  CDN (caches tiles globally)
    ↓ HTTP tile requests

  WEB APPLICATION:
  JavaScript (Leaflet / MapboxGL / Google Maps API)
    ↓ combines: GPS position + map tiles + routing
  User: sees themselves as a dot on a map
         gets turn-by-turn directions
         sees live traffic overlay

══════════════════════════════════════════════════════════════════════
```

---

## GPS Architecture — How It Works

GPS (Global Positioning System) is NAVSTAR GPS, a US military system that became operational in 1995. It consists of three segments: space, control, and user.

```
GPS SYSTEM ARCHITECTURE
══════════════════════════════════════════════════════════════════════

  SPACE SEGMENT:
  ┌──────────────────────────────────────────────────────────┐
  │  24 operational satellites (+ spares, currently ~31)    │
  │  6 orbital planes, 4 satellites per plane               │
  │  Altitude: 20,200 km (medium Earth orbit)               │
  │  Inclination: 55° (covers ±55° latitude well)           │
  │  Orbital period: ~11h 58min (2 orbits per sidereal day) │
  │  Guarantee: 4+ satellites visible anywhere on Earth     │
  │             > 95% of time (more typically 6–12 visible) │
  │                                                          │
  │  Each satellite carries:                                 │
  │  - 2–4 cesium atomic clocks (accurate to 1ns/day)       │
  │  - Transmitters broadcasting on L1 (1575.42 MHz) and    │
  │    L2 (1227.60 MHz)                                      │
  └──────────────────────────────────────────────────────────┘

  CONTROL SEGMENT:
  ┌──────────────────────────────────────────────────────────┐
  │  Master Control Station: Schriever AFB, Colorado        │
  │  Ground antennas: 5 worldwide monitoring stations       │
  │  Functions:                                              │
  │  - Monitor satellite health and clock accuracy          │
  │  - Upload corrected ephemeris (position) data           │
  │  - Update navigation message                            │
  │  - Manage constellation (retirements, launches)         │
  └──────────────────────────────────────────────────────────┘

  USER SEGMENT:
  ┌──────────────────────────────────────────────────────────┐
  │  Any device with a GPS receiver chip                    │
  │  Smartphone chip: ~$5; survey-grade receiver: $15,000+  │
  │  Passive receiver: only receives, does not transmit     │
  │  Privacy note: GPS is one-way — no one knows where you  │
  │  are from GPS alone (apps are different)                │
  └──────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════
```

---

## How GPS Actually Works — The Physics

The key insight: GPS is a time-measurement system that converts time differences into distance differences into position.

```
GPS POSITIONING — STEP BY STEP
══════════════════════════════════════════════════════════════════════

  STEP 1: Each satellite continuously broadcasts:
  ├── Its precise position at time T (from ephemeris data)
  └── The precise time T (from atomic clock)

  STEP 2: GPS receiver receives signals from multiple satellites.
  ├── Signal travels at speed of light c ≈ 3×10⁸ m/s
  └── Travel time Δt = distance / c

  STEP 3: Receiver measures pseudorange:
  ┌────────────────────────────────────────────────────────┐
  │  Pseudorange = c × (receiver time) - (satellite time)  │
  │  "Pseudo" because receiver clock is not as accurate    │
  │  as the satellite's atomic clock                       │
  │  → receiver clock error adds unknown offset to all     │
  │     pseudoranges equally                               │
  └────────────────────────────────────────────────────────┘

  STEP 4: Trilateration (NOT triangulation):
  ┌────────────────────────────────────────────────────────┐
  │  TRIANGULATION: measures angles → derives distances    │
  │  TRILATERATION: measures distances → derives position  │
  │                                                        │
  │  From satellite S1 at known position: receiver is on  │
  │  a sphere of radius r1                                 │
  │  From satellite S2: receiver is on a sphere of r2      │
  │  Two spheres intersect in a circle                    │
  │  From satellite S3: receiver is at one of two points  │
  │  (one is usually in space — eliminated)               │
  │  3 satellites → unique position (in 2D, or 3D if alt known)│
  │                                                        │
  │  BUT: receiver clock error → need a 4th satellite     │
  │  4th satellite provides the equation needed to solve  │
  │  for receiver clock error simultaneously with position│
  │                                                        │
  │  4 unknowns: x, y, z, t (clock error)                 │
  │  4 satellites: 4 equations → unique solution          │
  └────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════
```

The clock error elimination is elegant: by adding a 4th satellite, the system solves for the receiver's clock offset as a fourth unknown alongside the three spatial coordinates. Consumer GPS receivers have quartz clocks accurate to microseconds; the atomic-clock-derived correction from the 4th satellite brings effective timing accuracy to nanoseconds, enabling meter-level positioning.

---

## Selective Availability and the Clinton Decision

```
SELECTIVE AVAILABILITY — INTENTIONAL DEGRADATION
══════════════════════════════════════════════════════════════════════

  CONTEXT:
  GPS was a US military system. The military was concerned that
  adversaries would use GPS for precision missile guidance.

  SELECTIVE AVAILABILITY (SA):
  ├── Implemented: 1990 (Gulf War era)
  ├── Method: dithering the satellite clock signals with
  │   controlled error, changing pseudorandomly
  ├── Civilian accuracy: ~100m horizontal (with SA on)
  ├── Military accuracy: ~10m (with P(Y) encrypted code)
  └── Effect: civilians got a degraded service

  WORKAROUND (DGPS):
  ┌────────────────────────────────────────────────────────┐
  │  Place a reference GPS receiver at a known location    │
  │  Measure the SA error in real time                     │
  │  Broadcast the correction to nearby receivers          │
  │  Result: errors cancel → ~1m accuracy                  │
  │                                                        │
  │  Coast Guard DGPS network: established 1990s           │
  │  WAAS (Wide Area Augmentation System): 2003 for aviation│
  └────────────────────────────────────────────────────────┘

  THE CLINTON DECISION (May 1, 2000):
  ┌────────────────────────────────────────────────────────┐
  │  Executive order: turn off Selective Availability      │
  │  Rationale:                                            │
  │  - DGPS and foreign GNSS systems already provide       │
  │    workarounds — SA no longer provides security        │
  │  - Economic value of precise GPS enormous              │
  │  - Commercial GPS market would benefit                 │
  │                                                        │
  │  Immediate effect:                                     │
  │  Civilian GPS accuracy: 100m → 10m (same night)        │
  │  Overnight, every civilian GPS receiver improved 10×   │
  └────────────────────────────────────────────────────────┘

  POST-SA ACCURACY:
  ├── Civilian GPS: ~3–5m (UNAIDED)
  ├── WAAS-augmented: ~1m
  ├── DGPS: ~0.3m
  └── RTK (Real-Time Kinematic): ~1–2 cm

══════════════════════════════════════════════════════════════════════
```

---

## Other GNSS Constellations

```
GLOBAL NAVIGATION SATELLITE SYSTEMS
══════════════════════════════════════════════════════════════════════

  GPS (NAVSTAR):
  ├── Operator: US Space Force
  ├── Satellites: 31 operational
  ├── Altitude: 20,200 km
  ├── Fully operational: 1995
  └── Codes: C/A (civilian), P(Y) (military)

  GLONASS (Global Navigation Satellite System):
  ├── Operator: Russia
  ├── Satellites: 24 operational (target)
  ├── Altitude: 19,100 km (slightly lower than GPS)
  ├── Fully operational: 1995 (degraded after Soviet collapse;
  │   rebuilt to full constellation by 2011)
  ├── Key difference: uses frequency division multiplexing
  │   (GPS uses code division; GLONASS uses different frequencies
  │   for each satellite)
  └── Most smartphones: receive GPS + GLONASS

  GALILEO:
  ├── Operator: European Union (GSA)
  ├── Satellites: 30 planned, ~27 operational (2024)
  ├── Altitude: 23,222 km (higher than GPS → better geometry)
  ├── Fully operational: 2016 (initial), complete: 2020+
  ├── Accuracy: ~1m civilian (vs GPS ~3m) — more precise signal
  └── Key: fully independent of US military control

  BEIDOU (BDS, formerly COMPASS):
  ├── Operator: China
  ├── Satellites: 35 (mixed MEO + GEO + IGSO)
  ├── Fully operational: 2020 (global coverage)
  ├── Coverage: enhanced accuracy over China
  └── Used in: all Chinese phones, Belt and Road infrastructure

  RECEIVING MULTIPLE CONSTELLATIONS:
  Modern GPS chips receive all four (GPS+GLONASS+Galileo+BeiDou).
  More satellites visible → better geometry (GDOP) → better accuracy.
  Typical smartphone with all-constellation chip: ~2m accuracy.

══════════════════════════════════════════════════════════════════════
```

---

## Differential GPS, WAAS, and RTK

```
GPS ACCURACY ENHANCEMENT METHODS
══════════════════════════════════════════════════════════════════════

  BASE CONCEPT:
  Any GPS error affects all receivers in an area similarly.
  If you know where a reference receiver IS, you can measure
  the current GPS error and broadcast a correction.

  WAAS / SBAS (Satellite-Based Augmentation System):
  ├── US: WAAS; Europe: EGNOS; Japan: MSAS; India: GAGAN
  ├── Ground reference stations at known positions
  ├── Compute error; upload to geostationary satellites
  ├── Geostationary satellites broadcast correction on GPS freq
  ├── Any WAAS-enabled receiver gets <1m accuracy
  └── Aviation-grade: certified for IFR approaches (APV-I)

  DGPS (Differential GPS):
  ├── Local reference station broadcasts real-time corrections
  ├── Accuracy: 0.3–1m
  └── US Coast Guard operated for harbor/coastal navigation

  RTK (Real-Time Kinematic):
  ┌────────────────────────────────────────────────────────┐
  │  Uses carrier phase, not just code phase               │
  │                                                        │
  │  Code phase: measure signal arrival time → ~3m         │
  │  Carrier phase: measure phase of the 19cm carrier wave │
  │  → sub-cm accuracy after integer ambiguity resolution  │
  │                                                        │
  │  RTK: base station + rover; corrections over radio     │
  │  Range: ~10km from base station                        │
  │  Accuracy: 1–2cm horizontal, 3–5cm vertical            │
  │  Use: survey, machine control, precision agriculture   │
  └────────────────────────────────────────────────────────┘

  PPP (Precise Point Positioning):
  ├── No local base station needed
  ├── Uses precise satellite orbit + clock products
  │   (IGS: downloaded or broadcast)
  ├── Convergence time: 30–60 minutes
  └── Accuracy: 2–5cm globally (no base station required)

══════════════════════════════════════════════════════════════════════
```

---

## The Web Mapping Revolution

The transformation from paper maps and Mapquest to Google Maps represents more than a technology change — it changed the cognitive relationship between people and geographic space.

```
WEB MAP EVOLUTION TIMELINE
══════════════════════════════════════════════════════════════════════

  1993  MapServ (Steve Walters): first web GIS prototype
  1996  MapQuest launches: first major web map service
        Print-and-carry; no interaction; static images
  1998  Google founded; begins geographic data collection
  2004  OpenStreetMap founded (Steve Coast, UK)
        Wikipedia model applied to maps
  2005  Google Maps launches (February 8, 2005)
        AJAX + slippy map = revolutionary UX
        Smooth pan/zoom without page reload
        Later (2005): Google Maps API opened
  2005  Google Earth 3D viewer (acquired Keyhole)
  2006  OpenStreetMap reaches critical mass (UK)
  2008  Google Street View (US, then global rollout)
  2009  Bing Maps, HERE Maps competitive
  2010  Mobile GPS + Google Maps on every smartphone
  2012  Apple Maps launches (and embarrasses itself)
  2014  Mapbox launched, funded, growing
  2015  OpenStreetMap has more road data than Google in many regions
  2020s Planet-scale mapping: every address has Street View,
        every road has routing, billions of daily queries

══════════════════════════════════════════════════════════════════════
```

### The AJAX Slippy Map — What Google Maps Invented

```
GOOGLE MAPS UX INNOVATION (2005)
══════════════════════════════════════════════════════════════════════

  BEFORE (MapQuest, TerraServer):
  ├── Click button → full page reload → new static image
  ├── Pan = re-center → reload
  ├── Zoom = click zoom in button → reload
  └── Result: clunky, frustrating, best-effort

  GOOGLE MAPS INNOVATION:
  ├── Map = HTML div with positioned tile images
  ├── Each 256×256px tile: loaded asynchronously (AJAX)
  ├── Pan = CSS translate the tile container
  │   → new tiles loaded at edges, old ones drop off
  ├── Zoom = fade in new zoom level's tiles over old
  └── Result: fluid, continuous, responsive

  THE TILE SCHEME:
  ┌────────────────────────────────────────────────────────┐
  │  Zoom 0:  1 tile  = whole world (very small)           │
  │  Zoom 1:  4 tiles (2×2 grid)                          │
  │  Zoom 2: 16 tiles (4×4 grid)                          │
  │  Zoom n: 4ⁿ tiles (2ⁿ × 2ⁿ grid)                     │
  │  Zoom 18: 68 billion tiles (house-level detail)        │
  │                                                        │
  │  Tile URL: https://maps.example.com/tiles/{z}/{x}/{y}.png│
  │                                                        │
  │  At zoom 18: each tile covers ~75m × 75m at equator    │
  └────────────────────────────────────────────────────────┘

  PROJECTION: Web Mercator (EPSG:3857)
  ├── Entire world fits in a square
  ├── Tiles are square (Mercator makes this clean)
  ├── Scale factor at equator = 1; at poles = ∞
  └── Accepted trade-off: Greenland looks as big as Africa
      (most users zoom in to their city — they don't notice)

══════════════════════════════════════════════════════════════════════
```

---

## OpenStreetMap — The Wikipedia of Maps

OpenStreetMap (OSM) is the most successful collaborative geographic database in existence. Founded in 2004 by Steve Coast in the UK (partially in response to the Ordnance Survey's restrictive data licensing), it now contains more data than any commercial mapping service for many parts of the world.

```
OPENSTREETMAP — DATA MODEL AND COMMUNITY
══════════════════════════════════════════════════════════════════════

  DATA MODEL:
  Three primitive types:
  ├── NODE: a point (lat/lon) with optional tags
  │   Examples: a fire hydrant, a bus stop, a POI
  │
  ├── WAY: an ordered list of nodes
  │   Closed way (first=last node): polygon (building, park)
  │   Open way: line (road, river, power line)
  │
  └── RELATION: a multi-purpose grouping primitive
      Multipolygon: complex polygon with holes
      Route relation: bus/subway/hiking route
      Turn restriction: "no left turn" at intersection

  TAGGING:
  Any primitive can have key=value tags.
  Not a fixed schema — folksonomy with conventions.
  Conventions documented at wiki.openstreetmap.org
  ├── highway=motorway (major road)
  ├── amenity=hospital
  ├── building=yes (or residential, commercial, etc.)
  ├── name=Main Street
  └── opening_hours=Mo-Sa 09:00-17:00

  QUALITY:
  ├── Roads: generally good in developed world
  ├── Buildings: complete footprints in many cities
  ├── POIs: variable (volunteer-driven → gaps)
  ├── Developing world: often better than commercial
  │   (Humanitarian OSM: crisis mapping, HOT team)
  └── Freshness: some areas updated daily; some stale

  DATA ACCESS:
  ├── Full planet dump: ~80 GB compressed (weekly)
  ├── Overpass API: query current data by region/type
  ├── Geofabrik downloads: country/region extracts
  └── OSM2PGSQL: import into PostGIS for analysis

══════════════════════════════════════════════════════════════════════
```

---

## Vector Tiles — The Modern Standard

The original web map used raster tiles (pre-rendered PNGs). Vector tiles (format finalized as Mapbox Vector Tile in 2014) are better in almost every respect.

```
RASTER TILES vs VECTOR TILES
══════════════════════════════════════════════════════════════════════

  RASTER TILES:
  ├── Pre-rendered PNG/JPEG images
  ├── Fixed style (one style = one tile pyramid)
  ├── Not scalable (pixelate if over-zoomed)
  ├── Large storage (full pyramid = terabytes)
  ├── Text labels: burned in, can't rotate with map
  └── Simple: static file serving, works everywhere

  VECTOR TILES (MVT/PBF):
  ├── Binary protobuf containing geometry + attributes
  │   (much smaller than raster: 10–100× smaller)
  ├── Styled CLIENT-SIDE (style is a JSON document)
  │   One vector tile dataset → infinite visual styles
  ├── Scalable (geometry, not pixels → no pixelation)
  ├── Labels: positioned and rotated client-side
  ├── Interactivity: click feature → get its attributes
  └── Requires more powerful client (WebGL via MapboxGL)

  HOW VECTOR TILES WORK:
  ┌────────────────────────────────────────────────────────┐
  │  Server: tile/{z}/{x}/{y}.mvt                          │
  │  Content: protobuf-encoded geometry + properties       │
  │           for all features in that tile's area         │
  │           clipped to tile boundary                     │
  │           generalized to zoom level                    │
  │                                                        │
  │  Client (MapboxGL):                                    │
  │  1. Request tile                                       │
  │  2. Decode protobuf → geometry + properties            │
  │  3. Apply style rules (JSON) to features               │
  │  4. Render via WebGL to canvas                         │
  └────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════
```

---

## Navigation and Routing

Turn-by-turn navigation is a graph problem over a road network, enhanced with real-time data.

```
ROUTING PIPELINE
══════════════════════════════════════════════════════════════════════

  DATA:
  ├── Road network graph: nodes (intersections) + edges (road segments)
  │   Each edge: length, speed limit, road type, turn restrictions
  ├── Turn restrictions: "no left turn", "no U-turn"
  └── Traversal cost: time (for fastest) or distance (for shortest)

  BASIC ROUTING:
  Dijkstra's algorithm: O(E log V) with binary heap
  A* with Euclidean heuristic: faster in practice for point-to-point
  Contraction Hierarchies: state-of-the-art for road networks
  ├── Preprocessing: create shortcut edges, order nodes by importance
  ├── Query: bidirectional Dijkstra on contracted graph
  ├── Speed: milliseconds for any city-pair query
  └── Used by: Graphhopper, OSRM, Valhalla (open source)

  TURN-BY-TURN INSTRUCTIONS:
  ├── Road name extraction
  ├── Turn angle classification (left/right/straight/u-turn)
  ├── Landmark detection ("turn right at the McDonald's")
  └── Instruction localization (language, units)

  REAL-TIME ENHANCEMENTS:
  ┌────────────────────────────────────────────────────────┐
  │  TRAFFIC DATA:                                         │
  │  Sources: probe data (GPS tracks from phones/fleet),   │
  │           toll reader / loop detector feeds,           │
  │           incident reports (user-reported + municipal) │
  │                                                        │
  │  Google Maps: anonymized GPS from Android phones       │
  │  Waze: crowdsourced incident reports                   │
  │  HERE: commercial probe data + traffic sensors         │
  │                                                        │
  │  TRAFFIC-WEIGHTED ROUTING:                             │
  │  Edge weight = f(distance, current_speed, time_of_day) │
  │  Dynamic re-routing: as traffic changes, reroute       │
  └────────────────────────────────────────────────────────┘

  ETA PREDICTION:
  ├── Historical speed data by road × time-of-day × day-of-week
  ├── Current incident data
  ├── Weather conditions
  └── ML models on historical actual travel times

══════════════════════════════════════════════════════════════════════
```

---

## Location-Based Services Ecosystem

```
LBS ECOSYSTEM — WHAT GPS + MAPS ENABLES
══════════════════════════════════════════════════════════════════════

  NAVIGATION:
  ├── Turn-by-turn (Waze, Google Maps, Apple Maps)
  ├── Pedestrian navigation
  ├── Multimodal (transit + walk + bike)
  └── Indoor navigation (Bluetooth beacons, WiFi triangulation)

  LOGISTICS:
  ├── Routing: UPS, FedEx, Amazon last-mile
  ├── Fleet tracking: trucks, trains, aircraft (AIS/ADS-B)
  └── Supply chain: warehouse location optimization

  RIDE-SHARING / DELIVERY:
  ├── Real-time driver-passenger matching
  ├── Dynamic pricing (surge)
  ├── ETA display
  └── Driver position real-time tracking

  GEOFENCING:
  ├── Alert when asset enters/leaves a polygon
  ├── Retail: alert when customer near store
  └── Safety: construction site, school zone

  SPATIAL ANALYTICS:
  ├── Site selection: optimal location for new store
  ├── Market analysis: customer density around locations
  └── Urban planning: transit access coverage

  PRIVACY IMPLICATIONS:
  ├── GPS chip: passive, no tracking (one-way signal)
  ├── Apps: upload your location to servers
  ├── Cell tower data: carriers know your location 24/7
  ├── Advertising ID: cross-app location tracking
  └── Data brokers: buy/aggregate/resell location history
      (used for: ads, insurance, surveillance, law enforcement)

══════════════════════════════════════════════════════════════════════
```

---

## Common Confusion Points

**"GPS triangulates your position."** GPS uses trilateration (measuring distances from known points), not triangulation (measuring angles). Triangulation is what the Great Survey of India used. GPS measures time delays → pseudoranges → position by intersection of spheres.

**"GPS requires 3 satellites."** Technically 3 for 2D position if you know your altitude. Practically 4 minimum because the receiver's clock is not synchronized to GPS time. 4 satellites solve for x, y, z, and clock offset simultaneously.

**"Google Maps uses GPS data."** Google Maps uses GPS data indirectly — probe data from Android devices informs traffic, and your device's GPS chip provides positioning. The map tiles are served by Google, not by GPS. GPS gives you "where you are"; map tiles give you "what's around you."

**"EPSG:4326 is GPS data."** EPSG:4326 is the WGS84 geographic coordinate system. GPS provides WGS84 coordinates. But the coordinate system exists independently of GPS — Ptolemy's coordinate system uses the same framework. GPS is a tool for measuring WGS84 coordinates; 4326 is the coordinate system definition.

---

## Decision Cheat Sheet

| Task | Tool | Notes |
|------|------|-------|
| Get position to 3m | Consumer GPS | All smartphones |
| Get position to 1m | WAAS/SBAS | Aviation-grade receivers |
| Survey position to 1cm | RTK GPS | Base station + rover |
| Road navigation | Google Maps / Waze / Apple Maps | Real-time traffic |
| Open, hackable routing | OSRM / Graphhopper | Self-hosted, OSM data |
| Open map tiles | OpenStreetMap / Mapbox | Free for dev |
| Custom web map | Leaflet + OSM tiles | Simple; free |
| Custom styled map | MapboxGL JS | Vector tiles; WebGL |
| Offline maps | MBTiles + Mapsforge | Mobile apps |
| Location privacy | Airplane mode / disable Location | GPS = passive; apps are not |
