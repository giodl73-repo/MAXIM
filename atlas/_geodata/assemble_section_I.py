"""Assemble maps 02-04 with Natural Earth coastlines."""

def read_svg(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# Context coastlines (stroke only, no fill) for thematic overlays
CONTEXT = read_svg('world_context_int.svg')
# Light coastlines for concept maps
LIGHT = read_svg('world_light_int.svg')


# ────────────────────────────────────────────────────────────
# MAP 02 — Global Winds
# ────────────────────────────────────────────────────────────

MAP02 = r'''# 02 — Global Wind & Pressure Systems

*3♦ The Forecaster — the atmosphere's engine.*

---

## The Three-Cell Model

The atmosphere's circulation divides into three convection cells per hemisphere. This is the master pattern — everything else is a variation.

```
THREE-CELL ATMOSPHERIC CIRCULATION — CROSS-SECTION

  Altitude
  (km)
   15 ─┬──────────────────────────────────────────────────────────┬─
       │                                                          │
       │  ╭──→→→→→→→╮  ╭──→→→→→→→╮  ╭──→→→→→→→╮                 │
       │  │  HADLEY  │  │ FERREL  │  │  POLAR  │                 │
   10 ─│  │   CELL   │  │  CELL   │  │  CELL   │                 │
       │  │          │  │         │  │         │                 │
       │  ↑  (warm   ↓  ↑ (weak,  ↓  ↑ (cold   ↓                 │
       │  ↑   air    ↓  ↑ driven  ↓  ↑  dense   ↓                 │
    5 ─│  ↑  rises)  ↓  ↑  by H   ↓  ↑  air     ↓                 │
       │  ↑          ↓  ↑  and P) ↓  ↑  sinks)  ↓                 │
       │  ↑          ↓  ↑         ↓  ↑          ↓                 │
       │  ╰──←←←←←←←╯  ╰──←←←←←←╯  ╰──←←←←←←╯                 │
    0 ─┴──────────────────────────────────────────────────────────┴─
       EQ       30°N          60°N           90°N
       ↑         ↑             ↑              ↑
       ITCZ    SUBTROPICAL   POLAR          POLE
      (low P)  HIGH (high P) FRONT (low P)  (high P)
       ↕         ↕             ↕
    TRADES    WESTERLIES    POLAR EASTERLIES
    (surface   (surface      (surface
     winds)    winds)        winds)


  Mirror image in Southern Hemisphere.
  Coriolis effect deflects all winds:
    Northern Hemisphere → deflected RIGHT
    Southern Hemisphere → deflected LEFT
```

---

## Surface Wind Belts — Latitude Bands

```
GLOBAL SURFACE WINDS — LATITUDE BANDS

  90N ┌─────────────────────────────────────────────────────┐
      │         POLAR EASTERLIES  ←←←←←←←←←←              │
      │           (cold, dry, from the pole)                │
  60N ├─ ─ ─ ─ ─ POLAR FRONT (STORM ZONE) ─ ─ ─ ─ ─ ─ ─ ─┤
      │                                                     │
      │          WESTERLIES  →→→→→→→→→→→→                  │
      │         (prevailing mid-latitude winds)             │
      │          dominant wind for N.America + Europe       │
      │          drives weather systems west → east         │
      │                                                     │
  30N ├─ ─ ─ SUBTROPICAL HIGH (HORSE LATITUDES) ─ ─ ─ ─ ─ ┤
      │          dry, sinking air → DESERTS form here       │
      │          Sahara, Arabian, Sonoran, Gobi             │
      │                                                     │
      │          NE TRADE WINDS  ←←←←←↙↙↙↙↙               │
      │         (steady, reliable — powered sailing ships)  │
      │                                                     │
   EQ ├═══════ ITCZ (INTERTROPICAL CONVERGENCE ZONE) ═════╡
      │          low pressure, rising air, heavy rain       │
      │          migrates N in Jul, S in Jan                │
      │                                                     │
      │          SE TRADE WINDS  ←←←←←↗↗↗↗↗               │
      │                                                     │
  30S ├─ ─ ─ SUBTROPICAL HIGH (HORSE LATITUDES) ─ ─ ─ ─ ─ ┤
      │          Atacama, Kalahari, Australian deserts       │
      │                                                     │
      │          WESTERLIES  →→→→→→→→→→→→                  │
      │         ("Roaring Forties" at 40-50°S)             │
      │         (unimpeded by land — strongest on Earth)    │
      │                                                     │
  60S ├─ ─ ─ ─ ─ POLAR FRONT ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┤
      │         POLAR EASTERLIES  ←←←←←←←←←←              │
  90S └─────────────────────────────────────────────────────┘
```

---

## Why Deserts Form at 30°

```
THE DESERT BELT — WHY 30° LATITUDE?

       WARM MOIST AIR     cold, dry air descends
       rises at equator ──→  at ~30° latitude
            ↑                      ↓
            ↑                      ↓ compressed
            ↑                      ↓ warms
            ↑ condenses            ↓ → DRY
            ↑ → rain               ↓
            ↑                      ↓
  ──────────┼──────────────────────┼─────────── surface
        EQUATOR                  30° N or S
       (wet: Amazon,            (dry: Sahara,
        Congo, Indonesia)        Arabian, Sonoran,
                                 Atacama, Kalahari,
                                 Australian outback)

  The mechanism: air rises at ITCZ → drops moisture as tropical rain
  → flows poleward aloft → Coriolis deflects it → it piles up and
  sinks at ~30° → descending air compresses and warms → can't form
  clouds → desert.

  EVERY major hot desert on Earth sits at ~20-30° latitude.
  This is not coincidence — it's the Hadley Cell exhaust.
```

---

## The World's Deserts — Positioned by Latitude

<svg viewBox="-185 -45 370 90" width="960" height="230" xmlns="http://www.w3.org/2000/svg" style="background:#faf8f5; font-family: Georgia, serif;">

  <!-- Subtropical high bands -->
  <rect x="-180" y="-35" width="360" height="10" fill="#f5f0e8" opacity="0.4"/>
  <rect x="-180" y="20" width="360" height="10" fill="#f5f0e8" opacity="0.4"/>

  <!-- Grid -->
  <line x1="-180" y1="-30" x2="180" y2="-30" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="-20" x2="180" y2="-20" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="0" x2="180" y2="0" stroke="#e0ddd8" stroke-width="0.3"/>
  <line x1="-180" y1="20" x2="180" y2="20" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="30" x2="180" y2="30" stroke="#e0ddd8" stroke-width="0.2"/>

  <text x="182" y="-28" font-size="2.2" fill="#aaa">30°N</text>
  <text x="182" y="-18" font-size="2.2" fill="#aaa">20°N</text>
  <text x="182" y="2" font-size="2.2" fill="#aaa">EQ</text>
  <text x="182" y="22" font-size="2.2" fill="#aaa">20°S</text>
  <text x="182" y="32" font-size="2.2" fill="#aaa">30°S</text>

  <!-- Natural Earth coastlines — context -->
''' + CONTEXT + r'''
  <!-- DESERT OVERLAYS — sandy ellipses at real latitudes -->

  <!-- Northern Hemisphere (20-30°N) -->
  <ellipse cx="10" cy="-25" rx="28" ry="6" fill="#e8d8b0" fill-opacity="0.6" stroke="#c0a060" stroke-width="0.3"/>
  <text x="2" y="-24" font-size="2.8" fill="#8a7040" font-weight="bold">SAHARA</text>
  <text x="5" y="-21" font-size="1.8" fill="#8a7040">9.2 M km²</text>

  <ellipse cx="48" cy="-24" rx="8" ry="5" fill="#e8d8b0" fill-opacity="0.6" stroke="#c0a060" stroke-width="0.3"/>
  <text x="43" y="-23" font-size="2" fill="#8a7040" font-weight="bold">ARABIAN</text>

  <ellipse cx="72" cy="-26" rx="5" ry="4" fill="#e8d8b0" fill-opacity="0.6" stroke="#c0a060" stroke-width="0.3"/>
  <text x="69" y="-25" font-size="1.8" fill="#8a7040">THAR</text>

  <ellipse cx="-112" cy="-30" rx="6" ry="4" fill="#e8d8b0" fill-opacity="0.6" stroke="#c0a060" stroke-width="0.3"/>
  <text x="-117" y="-29" font-size="1.8" fill="#8a7040">SONORAN</text>

  <ellipse cx="-104" cy="-28" rx="5" ry="3" fill="#e8d8b0" fill-opacity="0.6" stroke="#c0a060" stroke-width="0.3"/>
  <text x="-110" y="-27" font-size="1.6" fill="#8a7040">CHIHUAHUAN</text>

  <!-- Gobi exception (~42°N, rain shadow — outside this view) -->

  <!-- Southern Hemisphere (20-30°S) -->
  <ellipse cx="-70" cy="24" rx="3" ry="5" fill="#e8d8b0" fill-opacity="0.6" stroke="#c0a060" stroke-width="0.3"/>
  <text x="-78" y="22" font-size="1.8" fill="#8a7040" font-weight="bold">ATACAMA</text>
  <text x="-80" y="25" font-size="1.4" fill="#8a7040" font-style="italic">driest</text>

  <ellipse cx="14" cy="24" rx="3" ry="5" fill="#e8d8b0" fill-opacity="0.6" stroke="#c0a060" stroke-width="0.3"/>
  <text x="10" y="22" font-size="1.8" fill="#8a7040">NAMIB</text>

  <ellipse cx="24" cy="26" rx="6" ry="5" fill="#e8d8b0" fill-opacity="0.6" stroke="#c0a060" stroke-width="0.3"/>
  <text x="20" y="27" font-size="2" fill="#8a7040" font-weight="bold">KALAHARI</text>

  <ellipse cx="132" cy="25" rx="14" ry="7" fill="#e8d8b0" fill-opacity="0.6" stroke="#c0a060" stroke-width="0.3"/>
  <text x="122" y="23" font-size="1.8" fill="#8a7040">GREAT SANDY</text>
  <text x="124" y="26" font-size="1.8" fill="#8a7040">GIBSON · VICTORIA</text>

  <!-- Band labels -->
  <text x="-178" y="-38" font-size="2" fill="#c08030" font-weight="bold">← SUBTROPICAL HIGH (30°N) — Hadley Cell exhaust →</text>
  <text x="-178" y="38" font-size="2" fill="#c08030" font-weight="bold">← SUBTROPICAL HIGH (30°S) — Hadley Cell exhaust →</text>

  <!-- Scale bar -->
  <line x1="155" y1="40" x2="165" y2="40" stroke="#444" stroke-width="0.3"/>
  <line x1="155" y1="39" x2="155" y2="41" stroke="#444" stroke-width="0.2"/>
  <line x1="165" y1="39" x2="165" y2="41" stroke="#444" stroke-width="0.2"/>
  <text x="157" y="43" font-size="1.8" fill="#444">~1,100 km</text>

</svg>

**Exception**: The Gobi (~42°N) is a rain shadow desert — the Himalayas block moisture from the Indian Ocean. Continental interior, far from any moisture source. Not Hadley Cell driven.

---

## Monsoon Systems

Monsoons are seasonal wind reversals driven by differential heating of land and ocean. They deliver the majority of annual rainfall for billions of people.

```
SOUTH ASIAN MONSOON — SEASONAL REVERSAL

  WINTER (DEC-MAR): dry                SUMMER (JUN-SEP): wet
  Cold air sinks over land             Hot air rises over land
  Wind blows FROM land → sea           Wind blows FROM sea → land

  ┌─────────────────────────┐          ┌─────────────────────────┐
  │    ASIA (cold, high P)  │          │    ASIA (hot, low P)    │
  │         ↓↓↓↓↓↓↓         │          │         ↑↑↑↑↑↑↑         │
  │  HIMALAYAS ▲▲▲▲▲▲▲▲▲▲  │          │  HIMALAYAS ▲▲▲▲▲▲▲▲▲▲  │
  │         ↓↓↓↓→→→→        │          │     ←←←←↑↑↑↑↑↑         │
  │  INDIA  →→→→→→→→        │          │  INDIA ←←←←←←←←        │
  │         dry NE wind     │          │     moist SW wind       │
  │         →→→→→→→→→       │          │  ←←←←←←←←←←←           │
  │    INDIAN OCEAN         │          │    INDIAN OCEAN         │
  │    (warm, low P)        │          │    (warm, high P)       │
  └─────────────────────────┘          └─────────────────────────┘

  RESULT: dry winter          RESULT: 80% of India's annual
          (Oct-May)                    rainfall in 4 months
```

### Global Monsoon Regions

| Region | Season | Rainfall Share | Impact |
|--------|--------|---------------|--------|
| South Asian (India, Bangladesh, Myanmar) | Jun-Sep | 70-90% of annual | Failure = famine for 1.5 billion |
| East Asian (China, Korea, Japan) | Jun-Jul | 40-60% of annual | Meiyu/Baiu front |
| West African (Sahel, Guinea coast) | Jun-Sep | 80%+ of annual | ITCZ migration northward |
| North American (SW US) | Jul-Sep | 30-40% of annual | Weaker. Arizona, New Mexico |
| Australian (Northern Australia) | Dec-Mar | 80%+ of annual | "Wet season" vs "dry season" |

---

## Jet Streams

```
JET STREAM POSITIONS — TOP-DOWN VIEW (NORTHERN HEMISPHERE)

                     NORTH POLE
                        ·
                   ·  ·   ·  ·
               ·                 ·
           · ·   POLAR JET        · ·
         ·   ═══════════════════    ·     ← 50-70°N
        ·     (speed: 100-200 kt)    ·      follows polar front
       ·       meanders N↔S           ·     drives mid-lat storms
      ·          (Rossby waves)        ·
     ·                                  ·
     ·    SUBTROPICAL JET               ·  ← 25-35°N
     ·    ═══════════════════           ·    weaker, higher altitude
     ·     (speed: 50-100 kt)          ·    associated with Hadley
      ·                                ·
       ·                              ·
        ·                            ·
         ·    TROPICS               ·
           · ·                 · ·
               ·            ·
                   ·  ·  ·
                    EQUATOR

  Jets meander — when they dip south ("trough"), cold Arctic air
  plunges into mid-latitudes. When they bulge north ("ridge"),
  warm air pushes poleward. These meanders drive weather patterns
  lasting days to weeks.
```

---

## Storm Tracks

```
MAJOR STORM TRACK CORRIDORS

  TROPICAL CYCLONES (hurricanes/typhoons):
  Form over warm ocean (>26°C) between 8-20° latitude.
  Move westward with trade winds, then curve poleward.

                                                  recurve →
  ─────── track ────→─→─→─→─→─→─→─→─↗↗↗↗→→→→→→→→→→→
  FORMATION ZONE         westward drift      poleward turn

  ATLANTIC BASIN:                    W. PACIFIC BASIN:
  ╭────────────╮                     ╭──────────────╮
  │ Cape Verde │                     │  W. Pacific  │
  │  ←←←←←←←  │                     │   ←←←←←←←←   │
  │ Caribbean  │  Jun-Nov            │  Philippines │  May-Dec
  │  ←←←←←←←↗ │  peak: Aug-Oct     │   ←←←←←←←↗  │  peak: Aug-Nov
  │ Gulf/US    │  ~12/year          │  Japan/China │  ~26/year
  │  coast ↗↗  │                     │   coast ↗↗   │  (most active
  ╰────────────╯                     ╰──────────────╯   basin)

  Also: S. Indian, N. Indian, S. Pacific basins.
  NO tropical cyclones in South Atlantic (cool water, high shear).

  MID-LATITUDE STORMS (extratropical cyclones):
  Follow the polar jet stream, west to east.
     North Pacific → Alaska → Pacific NW
     North Atlantic → Iceland → UK/Scandinavia
     Southern Ocean → "Roaring Forties" (40-50°S) — relentless

  TORNADO CORRIDORS:
     US Great Plains ("Tornado Alley"): Oklahoma, Kansas, Nebraska, Texas
     Also: Bangladesh, Argentina (Pampas), South Africa
     US sees ~1,200 tornadoes/year — more than rest of world combined
```

---

## Practical Wind Table

| Latitude Band | Prevailing Wind | Direction | Characteristics | Survival Note |
|---------------|----------------|-----------|-----------------|---------------|
| 60-90° | Polar Easterlies | E→W | Cold, dry, weak | Extreme cold; wind chill kills |
| 40-60° | Westerlies | W→E | Variable, stormy | Most weather comes from the west |
| 30-40° | Horse Latitudes | Calm/variable | Light wind, dry | Becalmed sailing, clear skies |
| 10-30° | Trade Winds | E→W (NE/SE) | Steady, reliable | Best sailing wind on Earth |
| 0-10° | Doldrums (ITCZ) | Calm/variable | Hot, humid, thunderstorms | Unpredictable; heavy rain |

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Which way does weather move at mid-latitudes? | West → East (westerlies). Storm approaching? Look west. |
| Why is the Sahara dry? | Hadley Cell: air rises at equator, sinks dry at 30°N |
| When is monsoon season in India? | June-September. 80% of annual rainfall. |
| Where do hurricanes form? | Over warm ocean (>26°C), 8-20° latitude |
| Most active hurricane basin? | Western Pacific (~26/year), then Atlantic (~12/year) |
| What are the Roaring Forties? | Westerlies at 40-50°S — no land to slow them |
| What drives multi-day weather patterns? | Jet stream meanders (Rossby waves) |
| Best latitude for sailing east? | 40-50° (westerlies). For sailing west? 10-25° (trades). |
| Where do tornadoes happen most? | US Great Plains, May-June peak |

---

## Cross-References

- **Atmospheric layers** → [meteorology/](../meteorology/00-OVERVIEW.md)
- **Climate classification** → [atlas/30-CLIMATE-CLASSIFICATION.md](30-CLIMATE-CLASSIFICATION.md) *(planned)*
- **Ocean currents** → [atlas/18-OCEAN-CURRENTS.md](18-OCEAN-CURRENTS.md) *(planned)*
- **Celestial navigation** → [atlas/04-CELESTIAL-NAVIGATION.md](04-CELESTIAL-NAVIGATION.md)
- **Climate science** → [climate-science/](../climate-science/00-OVERVIEW.md)
'''

with open('../02-GLOBAL-WINDS.md', 'w', encoding='utf-8') as f:
    f.write(MAP02.lstrip('\n'))
print(f"Wrote 02-GLOBAL-WINDS.md ({len(MAP02):,} chars)")


# ────────────────────────────────────────────────────────────
# MAP 03 — World Soils
# Uses CONTEXT coastlines + breadbasket overlays
# File is too large to include inline — read existing and replace SVG block
# ────────────────────────────────────────────────────────────

# Read existing map 03
with open('../03-WORLD-SOILS.md', 'r', encoding='utf-8') as f:
    map03_content = f.read()

# Find the SVG block and replace the coastline paths inside it
# The SVG starts after "## The World's Breadbaskets" and the paragraph
import re

# Build new SVG content for map 03
MAP03_SVG = r'''<svg viewBox="-185 -90 370 180" width="960" height="480" xmlns="http://www.w3.org/2000/svg" style="background:#faf8f5; font-family: Georgia, serif;">

  <!-- Grid -->
  <line x1="-180" y1="0" x2="180" y2="0" stroke="#e0ddd8" stroke-width="0.3"/>
  <line x1="-180" y1="-30" x2="180" y2="-30" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="30" x2="180" y2="30" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="-60" x2="180" y2="-60" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="60" x2="180" y2="60" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="0" y1="-85" x2="0" y2="85" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-90" y1="-85" x2="-90" y2="85" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="90" y1="-85" x2="90" y2="85" stroke="#e0ddd8" stroke-width="0.2"/>

  <text x="182" y="2" font-size="2.5" fill="#aaa">0°</text>
  <text x="182" y="-28" font-size="2.5" fill="#aaa">30°N</text>
  <text x="182" y="32" font-size="2.5" fill="#aaa">30°S</text>
  <text x="182" y="-58" font-size="2.5" fill="#aaa">60°N</text>

  <!-- Natural Earth coastlines — context -->
''' + CONTEXT + r'''
  <!-- BREADBASKET REGIONS — green fills -->

  <!-- US Great Plains / Corn Belt (mollisol) -->
  <ellipse cx="-97" cy="-42" rx="12" ry="7" fill="#7aaa5a" fill-opacity="0.5" stroke="#4a7a3a" stroke-width="0.4"/>
  <text x="-107" y="-44" font-size="2.5" fill="#3a6a2a" font-weight="bold">US GREAT PLAINS</text>
  <text x="-104" y="-41" font-size="2" fill="#3a6a2a">Corn Belt — mollisol</text>
  <text x="-105" y="-38" font-size="1.8" fill="#4a7a3a">wheat, corn, soy</text>

  <!-- Canadian Prairies -->
  <ellipse cx="-108" cy="-52" rx="10" ry="4" fill="#7aaa5a" fill-opacity="0.35" stroke="#4a7a3a" stroke-width="0.3"/>
  <text x="-118" y="-51" font-size="2" fill="#3a6a2a">CANADIAN PRAIRIES</text>

  <!-- Ukrainian Steppe / Chernozem -->
  <ellipse cx="33" cy="-50" rx="10" ry="5" fill="#5a8a3a" fill-opacity="0.5" stroke="#3a6a2a" stroke-width="0.4"/>
  <text x="25" y="-52" font-size="2.5" fill="#2a5a1a" font-weight="bold">CHERNOZEM</text>
  <text x="26" y="-49" font-size="2" fill="#3a6a2a">Ukrainian steppe</text>
  <text x="27" y="-46.5" font-size="1.8" fill="#4a7a3a" font-style="italic">richest soil on Earth</text>

  <!-- France -->
  <ellipse cx="2" cy="-47" rx="5" ry="4" fill="#7aaa5a" fill-opacity="0.4" stroke="#4a7a3a" stroke-width="0.3"/>
  <text x="-3" y="-46" font-size="1.8" fill="#3a6a2a">FRANCE</text>

  <!-- Indo-Gangetic Plain -->
  <ellipse cx="80" cy="-28" rx="10" ry="4" fill="#7aaa5a" fill-opacity="0.5" stroke="#4a7a3a" stroke-width="0.4"/>
  <text x="72" y="-29.5" font-size="2.2" fill="#2a5a1a" font-weight="bold">INDO-GANGETIC</text>
  <text x="73" y="-26.5" font-size="1.8" fill="#3a6a2a">alluvial — feeds 1 billion</text>

  <!-- North China Plain (loess) -->
  <ellipse cx="115" cy="-35" rx="8" ry="5" fill="#7aaa5a" fill-opacity="0.5" stroke="#4a7a3a" stroke-width="0.4"/>
  <text x="109" y="-37" font-size="2.2" fill="#2a5a1a" font-weight="bold">N. CHINA PLAIN</text>
  <text x="110" y="-34" font-size="1.8" fill="#3a6a2a">loess plateau</text>

  <!-- Pampas (Argentina) -->
  <ellipse cx="-60" cy="35" rx="7" ry="5" fill="#7aaa5a" fill-opacity="0.5" stroke="#4a7a3a" stroke-width="0.4"/>
  <text x="-67" y="34" font-size="2.2" fill="#2a5a1a" font-weight="bold">PAMPAS</text>
  <text x="-66" y="37" font-size="1.8" fill="#3a6a2a">mollisol — cattle, wheat, soy</text>

  <!-- SE Brazil -->
  <ellipse cx="-45" cy="22" rx="6" ry="5" fill="#aac87a" fill-opacity="0.4" stroke="#6a8a4a" stroke-width="0.3"/>
  <text x="-51" y="21" font-size="1.8" fill="#3a6a2a">SE BRAZIL</text>
  <text x="-51" y="24" font-size="1.5" fill="#4a7a3a">oxisol + mgmt</text>

  <!-- Murray-Darling -->
  <ellipse cx="144" cy="34" rx="6" ry="4" fill="#aac87a" fill-opacity="0.3" stroke="#8aaa6a" stroke-width="0.3" stroke-dasharray="1"/>
  <text x="138" y="33" font-size="1.8" fill="#5a7a4a">MURRAY-DARLING</text>
  <text x="139" y="36" font-size="1.4" fill="#5a7a4a" font-style="italic">marginal, salinity</text>

  <!-- Mollisol belt annotation -->
  <text x="-40" y="-58" font-size="2.5" fill="#3a6a2a" font-weight="bold">MOLLISOL BELT (~35-55°N)</text>
  <text x="-35" y="-55" font-size="2" fill="#4a7a3a">world's great grain exporters</text>

  <!-- Legend -->
  <rect x="-178" y="68" width="50" height="14" fill="#faf8f5" stroke="#ddd" stroke-width="0.3" rx="1"/>
  <ellipse cx="-172" cy="72" rx="3" ry="1.5" fill="#5a8a3a" fill-opacity="0.5"/>
  <text x="-167" y="73" font-size="2" fill="#444">Mollisol / chernozem (highest fertility)</text>
  <ellipse cx="-172" cy="76" rx="3" ry="1.5" fill="#7aaa5a" fill-opacity="0.5"/>
  <text x="-167" y="77" font-size="2" fill="#444">Alfisol / alluvial (managed fertility)</text>
  <ellipse cx="-172" cy="80" rx="3" ry="1.5" fill="#aac87a" fill-opacity="0.4" stroke="#8aaa6a" stroke-width="0.2" stroke-dasharray="0.5"/>
  <text x="-167" y="81" font-size="2" fill="#444">Marginal / managed (irrigation dependent)</text>

  <!-- Scale bar -->
  <line x1="140" y1="68" x2="150" y2="68" stroke="#444" stroke-width="0.4"/>
  <line x1="140" y1="67" x2="140" y2="69" stroke="#444" stroke-width="0.3"/>
  <line x1="150" y1="67" x2="150" y2="69" stroke="#444" stroke-width="0.3"/>
  <text x="142" y="72" font-size="2.2" fill="#444">~1,100 km</text>

</svg>'''

# Replace the SVG block in map03
svg_start = map03_content.find('<svg viewBox=')
svg_end = map03_content.find('</svg>', svg_start) + len('</svg>')
map03_new = map03_content[:svg_start] + MAP03_SVG + map03_content[svg_end:]

with open('../03-WORLD-SOILS.md', 'w', encoding='utf-8') as f:
    f.write(map03_new)
print(f"Wrote 03-WORLD-SOILS.md ({len(map03_new):,} chars)")


print("\nDone. Maps 02 and 03 rebuilt with Natural Earth coastlines.")
print("Map 04 (Celestial Navigation) uses the light tier — keeping existing version")
print("since its SVG is a star visibility concept map, not a geographic map.")
