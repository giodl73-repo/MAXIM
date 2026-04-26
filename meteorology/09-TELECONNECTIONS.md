# Teleconnections — ENSO, NAO, MJO, PDO, AO

## The Big Picture

Teleconnections are statistical relationships between climate anomalies in geographically remote regions. They reflect coherent large-scale patterns of atmospheric or ocean-atmosphere variability that modulate weather patterns globally — the primary source of seasonal-scale predictability beyond the 2-week weather forecast limit.

**Mathematical basis:** Teleconnection patterns are defined by Empirical Orthogonal Functions (EOFs) — which are exactly PCA applied to spatiotemporal climate fields. The NAO is the leading eigenvector of the North Atlantic sea-level pressure covariance matrix. The PDO is the leading eigenvector of North Pacific SST anomalies. The MJO's RMM index is the projection onto the two leading EOFs of combined OLR and zonal wind anomalies. EOF decomposition finds the orthogonal modes that explain maximum variance — the same eigendecomposition of a covariance matrix used in dimensionality reduction everywhere in data science.

```
+------------------------------------------------------------------+
|                    TELECONNECTION HIERARCHY                      |
|                                                                  |
|  TIMESCALE     PATTERN         ORIGIN         PREDICTABILITY     |
|  ----------    -----------     ----------     ----------------   |
|  30–90 days    MJO             Tropical       2–4 weeks          |
|                                intraseasonal                     |
|  Seasonal      ENSO            Ocean-atm      6–12 months        |
|  (3–9 months)  (El Niño/La     coupling in    ahead              |
|                 Niña)          tropical Pac.                     |
|  Decadal       PDO, AMO        Ocean SST      Statistical        |
|  (decades)     (Pacific/       variability    tendency only      |
|                Atlantic deca.)                                   |
|  Weeks         NAO, AO         Jet stream/    1–3 weeks          |
|                                stratosphere                      |
+------------------------------------------------------------------+
```

---

## ENSO — El Niño-Southern Oscillation

The dominant mode of interannual climate variability. Ocean-atmosphere coupling in the tropical Pacific that modulates global weather on 3–7 year cycles.

### Normal Conditions (La Niña-neutral)

```
TROPICAL PACIFIC — NORMAL STATE:

WEST                                      EAST
Papua New                                 South America
Guinea/                                   (Peru/Ecuador)
Indonesia
                    Trade winds
              ←←←←←←←←←←←←←←←←←←←←←
WARM SST              Thermocline         COLD SST
(28°C+)         ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈    (23°C)
                ≈ warm surface layer ≈
                ____cold thermocline____
                (upwelling cold water
                 reaches surface in east)
Deep              → Walker Circulation ←  Shallow
warm pool           (rising in west,       warm pool
                     sinking in east)
```

### El Niño — Warm Phase

```
EL NIÑO STATE:
WEST                                      EAST
              Trade winds weaken
              ← ← ← (weaker)
WARM SST                                  WARM SST
(26°C)         ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈    (26°C!)
               ≈  thermocline deepens ≈  (upwelling
               ≈  in east ≈              suppressed)

Walker Circulation REVERSES or weakens:
- Rising motion over central/eastern Pacific
- Drought in Australia/Indonesia/Philippines
- Flooding in Peru/Ecuador
```

### La Niña — Cold Phase

```
LA NIÑA STATE:
Stronger than normal trade winds
← ← ← ← ← ← (stronger) ←
VERY WARM              VERY COLD SST
WEST                   (enhanced upwelling)
Enhanced Walker Circulation:
- More intense rainfall: Australia, SE Asia, India, Amazon
- Drought: SW US, Peru/Ecuador, East Africa (some seasons)
- Active Atlantic hurricane season
```

### Global ENSO Teleconnections

```
EL NIÑO (NH winter typical impacts):
  WETTER THAN NORMAL:           DRIER THAN NORMAL:
  Southern US (Dec–Feb)         Pacific NW (winter)
  Gulf Coast                    Great Plains (winter)
  Peru/Ecuador                  Brazil (NE)
  East Africa (Oct–Dec)         Australia, SE Asia
  California (most years)       Caribbean (some areas)

LA NIÑA (NH winter typical impacts):
  WETTER:                       DRIER:
  Pacific NW                    SW US
  Great Plains (spring)         California
  SE US (some seasons)          Gulf Coast
  Australia, SE Asia            NE Brazil
```

**ENSO indices:**
- **Niño 3.4**: SST anomaly in equatorial Pacific (5°N–5°S, 120–170°W)
- **Niño 4**: Western equatorial Pacific
- **MEI (Multivariate ENSO Index)**: Combined atmospheric + oceanic

---

## MJO — Madden-Julian Oscillation

The dominant mode of tropical intraseasonal variability. An eastward-propagating pulse of enhanced and suppressed convection circling the tropics:

```
MJO LIFECYCLE (one cycle = 30–90 days, typically 45–50):

     PHASE:   1    2    3    4    5    6    7    8
              Africa  Indian  Maritime  Pacific  western  →
                      Ocean   Continent  Ocean   hemisphere

              [+]   [+]   [+]   [+]  [+]  → (active convection pulse)
              (quiet)  (quiet)  (quiet)      (enhanced convection)

MJO PHASES (Wheeler-Hendon Real-Time Multivariate MJO, RMM):
  Defined by two principal components (RMM1, RMM2)
  Phase diagram: circle; distance from center = amplitude
  Phase 1: Africa/western Indian Ocean
  Phase 2-3: Indian Ocean (enhanced precip; Asia/Australia active)
  Phase 4-5: Maritime continent
  Phase 6-7: Pacific Ocean
  Phase 8: Western hemisphere
```

**MJO teleconnections to extratropics:**

| MJO Phase | US Winter Impact | Mechanism |
|----------|----------------|-----------|
| 2–3 | Enhanced cold air outbreaks East US | Rossby wave train from tropics |
| 6–7 | Warmer than normal, East US | Rossby wave opposite |
| 4–5 | Variable; Maritime Continent signal weak | Complex interactions |

**MJO and hurricanes:**
- MJO active phase over Gulf/Caribbean → higher Atlantic hurricane activity
- MJO suppressed phase → reduced activity
- Extends hurricane forecasting skill by ~10 days when MJO is well-defined

**MJO and winter blocking** — MJO influences jet stream waviness and blocking frequency 2–4 weeks later. The primary source of week 3–4 forecasting skill.

---

## NAO — North Atlantic Oscillation

The leading mode of atmospheric variability in the North Atlantic/European sector:

```
NAO DEFINITION:
  Pressure difference between Azores High and Icelandic Low
  (can also be defined as leading EOF of NH SLP anomalies)

NAO+ (positive phase):           NAO- (negative phase):
  Strong Azores High               Weak Azores High
  Deep Icelandic Low               Weak Icelandic Low
  ↓                                ↓
  Enhanced westerlies              Weaker westerlies
  Mild, wet European               Cold, stormy Europe
  winters (UK, Scandinavia)        (blocking pattern common)
  Dry in SW Europe                 Wet in Mediterranean
  (Iberia, Morocco)
  Cold in Labrador/                Warm in Labrador/NE Canada
  Greenland

+-----------------------------+   +------------------------------+
|    NAO+                     |   |    NAO-                      |
|    (Stormy NW Europe)       |   |    (Cold UK/Blocking)        |
|    L                        |   |    H                         |
|   (low)      H              |   |   (low)     L                |
| ICELANDIC  AZORES           |   | ICELANDIC  AZORES            |
|   LOW      HIGH             |   |   LOW      HIGH              |
+-----------------------------+   +------------------------------+
```

**NAO prediction** — NAO is driven by both tropical (ENSO/MJO) forcing and internal atmospheric variability. Predictability 2–4 weeks ahead is limited but real; dominated by MJO influence.

---

## AO and PV — Arctic Oscillation and Polar Vortex

```
ARCTIC OSCILLATION (AO):
  Leading mode of NH winter SLP variability north of 20°N
  Closely related to NAO (AO is more hemispheric)

AO+ :           Strong polar vortex, cold air contained in Arctic
                Westerlies strong; mild mid-latitudes
                Polar jet tight and fast

AO- :           Weak polar vortex (possibly sudden stratospheric
                warming, SSW); cold air "escapes" poleward barrier
                → Cold outbreaks to mid-latitudes
                → Negative NAO often follows

POLAR VORTEX:
  Not a new term — it's the circumpolar westerly circulation
  in the stratosphere (10–50 km) centered on the winter pole

SUDDEN STRATOSPHERIC WARMING (SSW):
  Rapid T increase (30–50°C in days) in polar stratosphere
  → Polar vortex disrupted or split
  → AO/NAO goes negative 2–8 weeks later
  → Cold air outbreak risk increases substantially
  → High-impact winter events (Beast from the East, 2018;
     North American cold wave, Jan 2021)
```

---

## PDO — Pacific Decadal Oscillation

```
PDO: Decadal SST pattern in North Pacific (leading EOF of North Pacific SST)

PDO+ (warm phase):
  Warm SST: northeast Pacific coast + tropical Pacific
  Cold SST: central N. Pacific
  → Like El Niño background state
  → 1977–1998 was a warm PDO phase

PDO- (cool phase):
  Cold SST: NE Pacific coast
  Warm SST: central N. Pacific
  → Like La Niña background
  → 1947–1977 cool phase; 1998–~2015 mostly cool

PDO INFLUENCE:
  Amplifies/dampens ENSO impacts
  El Niño + PDO+ = stronger California wet winters
  El Niño + PDO- = weaker California wet winters
  Decadal salmon/anchovy fishery shifts in N. Pacific
```

---

## IOD — Indian Ocean Dipole

```
IOD:
  SST anomaly pattern in tropical Indian Ocean
  Positive IOD (+): Warm West IO, Cool East IO
  Negative IOD (-): Cool West IO, Warm East IO

+IOD: Enhanced rainfall E Africa, India (Sept-Nov)
      Drought: Indonesia, Australia
      Often accompanies El Niño

-IOD: Enhanced rainfall SE Asia, Australia
      Often accompanies La Niña
```

---

## Decision Cheat Sheet

| Seasonal forecast question | Relevant teleconnection |
|---------------------------|------------------------|
| US winter temperature anomalies | ENSO (if moderate+); NAO/AO (for cold outbreaks) |
| Australia rainfall outlook | ENSO, IOD |
| Atlantic hurricane season activity | AMO, ENSO (La Niña = more active) |
| Europe winter temperature | NAO, ENSO modulated |
| 2–4 week US temperature outlook | MJO phase + trend; AO/SSW state |
| Week 2 severe weather pattern | MJO-driven Rossby waves |
| US drought (multi-year) | PDO phase + ENSO combination |

---

## Common Confusion Points

**El Niño ≠ global warming** — El Niño temporarily raises global average temperature by ~0.1–0.2°C (warm ocean evaporates more, extra energy in system). Climate trend is underlying; El Niño/La Niña oscillates around that trend. 2023–2024 temperature records partly reflect El Niño superimposed on long-term warming.

**ENSO impacts are probabilistic, not deterministic** — A moderate El Niño increases probability of wet conditions in Southern US by maybe 60% vs climatological 40%. It does not guarantee rain. Individual years vary widely even within the same ENSO phase.

**Polar vortex is not a new phenomenon** — The stratospheric polar vortex is a permanent winter feature. Media coverage exploded in 2014 (Chicago cold wave). The term refers to the stratospheric vortex, not the tropospheric jet stream — though SSW events do eventually influence the tropospheric jet.

**NAO vs AO** — The NAO is a regional mode (North Atlantic); the AO is the hemispheric annular mode. They are highly correlated (r~0.7). Operationally, NAO is more useful for European and eastern North American forecasts; AO is better for hemispheric analyses.
