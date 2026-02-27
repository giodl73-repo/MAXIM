"""
Assemble Section II maps (05-08) with Natural Earth coastlines + PhyloPic silhouettes.
"""

import re
import os

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_path_d(svg_file):
    """Extract first <path> d attribute from a PhyloPic SVG."""
    content = read_file(svg_file)
    match = re.search(r'<path[^>]*\bd="([^"]*)"', content)
    return match.group(1) if match else ""

def extract_viewbox(svg_file):
    content = read_file(svg_file)
    match = re.search(r'viewBox="([^"]*)"', content)
    return match.group(1) if match else "0 0 100 100"

def make_symbol(svg_file, symbol_id):
    vb = extract_viewbox(svg_file)
    d = extract_path_d(svg_file)
    return f'    <symbol id="{symbol_id}" viewBox="{vb}"><path d="{d}"/></symbol>'

SIL = 'silhouettes'
CONTEXT = read_file('world_context_int.svg')

# Build silhouette symbol blocks for each map
def biome_symbols():
    syms = []
    for name in ['conifer', 'cactus', 'palm', 'fern', 'moss', 'oak', 'eucalyptus']:
        f = f'{SIL}/{name}.svg'
        if os.path.exists(f):
            syms.append(make_symbol(f, name))
    return '\n'.join(syms)

def river_symbols():
    syms = []
    for name in ['salmon', 'fish', 'crocodile']:
        f = f'{SIL}/{name}.svg'
        if os.path.exists(f):
            syms.append(make_symbol(f, name))
    return '\n'.join(syms)

def grain_symbols():
    syms = []
    for name in ['wheat', 'rice', 'maize', 'barley', 'coffee']:
        f = f'{SIL}/{name}.svg'
        if os.path.exists(f):
            syms.append(make_symbol(f, name))
    return '\n'.join(syms)

def flyway_symbols():
    syms = []
    for name in ['barnacle_goose', 'humpback_whale', 'monarch_butterfly',
                  'black_tern', 'bar-tailed_godwit', 'flamingo', 'penguin',
                  'albatross', 'caribou', 'wildebeest', 'sea_turtle', 'salmon']:
        f = f'{SIL}/{name}.svg'
        if os.path.exists(f):
            sid = name.replace('-', '_').replace(' ', '_')
            syms.append(make_symbol(f, sid))
    return '\n'.join(syms)


# ════════════════════════════════════════════════════════════════
# MAP 05 — GLOBAL BIOMES
# ════════════════════════════════════════════════════════════════

MAP05 = f'''# 05 — Global Biomes & Ecoregions

*2♣ The Taxonomist — the living skin of the planet.*

---

## Biome Map

Earth's land surface divides into ~14 major biomes, distributed primarily by latitude and precipitation. Temperature sets the bands; moisture fills them in.

<svg viewBox="-185 -90 370 180" width="960" height="480" xmlns="http://www.w3.org/2000/svg" style="background:#faf8f5; font-family: Georgia, serif;">

  <defs>
{biome_symbols()}
  </defs>

  <!-- Grid -->
  <line x1="-180" y1="0" x2="180" y2="0" stroke="#e0ddd8" stroke-width="0.3"/>
  <line x1="-180" y1="-30" x2="180" y2="-30" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="30" x2="180" y2="30" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="-60" x2="180" y2="-60" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="60" x2="180" y2="60" stroke="#e0ddd8" stroke-width="0.2"/>

  <text x="182" y="2" font-size="2.5" fill="#aaa">0°</text>
  <text x="182" y="-28" font-size="2.5" fill="#aaa">30°N</text>
  <text x="182" y="32" font-size="2.5" fill="#aaa">30°S</text>
  <text x="182" y="-58" font-size="2.5" fill="#aaa">60°N</text>

  <!-- Natural Earth coastlines -->
{CONTEXT}

  <!-- BIOME BANDS — transparent color overlays at latitude zones -->

  <!-- Tundra (>60°N/S) — pale blue -->
  <rect x="-180" y="-90" width="360" height="23" fill="#c0d8e8" fill-opacity="0.25"/>
  <rect x="-180" y="67" width="360" height="23" fill="#c0d8e8" fill-opacity="0.25"/>
  <text x="-178" y="-72" font-size="2.5" fill="#5080a0" font-weight="bold">TUNDRA</text>

  <!-- Boreal/Taiga (50-67°N) — dark green -->
  <rect x="-180" y="-67" width="360" height="17" fill="#406040" fill-opacity="0.15"/>
  <text x="-178" y="-55" font-size="2.5" fill="#406040" font-weight="bold">BOREAL FOREST / TAIGA</text>

  <!-- Temperate (30-50°N and 30-50°S) — medium green -->
  <rect x="-180" y="-50" width="360" height="20" fill="#60a060" fill-opacity="0.12"/>
  <rect x="-180" y="30" width="360" height="20" fill="#60a060" fill-opacity="0.12"/>
  <text x="50" y="-42" font-size="2.5" fill="#408040" font-weight="bold">TEMPERATE FOREST / GRASSLAND</text>

  <!-- Desert (20-30°N and 20-30°S) — tan -->
  <rect x="-180" y="-30" width="360" height="10" fill="#e0d0a0" fill-opacity="0.20"/>
  <rect x="-180" y="20" width="360" height="10" fill="#e0d0a0" fill-opacity="0.20"/>
  <text x="50" y="-23" font-size="2.2" fill="#a08040">DESERT / ARID SCRUB</text>

  <!-- Tropical (0-20°N/S) — bright green -->
  <rect x="-180" y="-20" width="360" height="40" fill="#40a040" fill-opacity="0.12"/>
  <text x="-40" y="2" font-size="2.8" fill="#307030" font-weight="bold">TROPICAL FOREST / SAVANNA</text>

  <!-- Silhouette markers — positioned at representative biome locations -->
  <use href="#conifer" x="30" y="-65" width="5" height="5" fill="#406040" opacity="0.6"/>
  <use href="#conifer" x="-100" y="-58" width="5" height="5" fill="#406040" opacity="0.6"/>
  <use href="#cactus" x="-110" y="-28" width="4" height="4" fill="#a08040" opacity="0.6"/>
  <use href="#cactus" x="10" y="-26" width="4" height="4" fill="#a08040" opacity="0.6"/>
  <use href="#palm" x="-65" y="2" width="5" height="5" fill="#307030" opacity="0.6"/>
  <use href="#palm" x="105" y="-5" width="5" height="5" fill="#307030" opacity="0.6"/>
  <use href="#fern" x="170" y="30" width="4" height="4" fill="#408040" opacity="0.5"/>
  <use href="#oak" x="-80" y="-42" width="5" height="5" fill="#408040" opacity="0.5"/>
  <use href="#oak" x="5" y="-46" width="5" height="5" fill="#408040" opacity="0.5"/>
  <use href="#eucalyptus" x="140" y="30" width="4" height="4" fill="#608040" opacity="0.5"/>
  <use href="#moss" x="-30" y="-78" width="4" height="4" fill="#5080a0" opacity="0.5"/>

  <!-- Scale bar -->
  <line x1="140" y1="72" x2="150" y2="72" stroke="#444" stroke-width="0.4"/>
  <line x1="140" y1="71" x2="140" y2="73" stroke="#444" stroke-width="0.3"/>
  <line x1="150" y1="71" x2="150" y2="73" stroke="#444" stroke-width="0.3"/>
  <text x="142" y="76" font-size="2.2" fill="#444">~1,100 km</text>

  <!-- Attribution -->
  <text x="-178" y="88" font-size="1.5" fill="#bbb">Silhouettes: PhyloPic (CC0). Coastlines: Natural Earth (public domain).</text>

</svg>

---

## Biome Latitude Bands

```
BIOME DISTRIBUTION BY LATITUDE — CROSS-SECTION

  90N ┌──────────────────────────────────────────────┐
      │  ICE CAP                                      │  permanent ice
      │  (Greenland, Antarctica)                      │
  70N ├──────────────────────────────────────────────┤
      │  TUNDRA                                       │  permafrost, lichens
      │  No trees. Growing season <60 days.          │  mosses, sedges
  60N ├──────────────────────────────────────────────┤
      │  BOREAL FOREST (TAIGA)                        │  spruce, fir, pine
      │  World's largest biome by area.              │  long winters, short
      │  Spans Russia, Canada, Scandinavia.          │  growing season
  50N ├──────────────────────────────────────────────┤
      │  TEMPERATE DECIDUOUS FOREST                   │  oak, maple, beech
      │  4 distinct seasons. Rich soil (alfisols).   │  high biodiversity
  40N ├──────────────────────────────────────────────┤
      │  TEMPERATE GRASSLAND                          │  prairie, steppe, pampas
      │  Mollisols — world's best farming soil.      │  wheat, corn belt
  30N ├──────────────────────────────────────────────┤
      │  DESERT / ARID SCRUB                          │  cactus, succulents
      │  <250 mm rain/yr. Hadley Cell exhaust.       │  Sahara, Arabian, Sonoran
  20N ├──────────────────────────────────────────────┤
      │  TROPICAL SAVANNA                             │  grassland + scattered trees
      │  Wet/dry seasons. Fire-maintained.           │  Serengeti, Cerrado
  10N ├──────────────────────────────────────────────┤
      │  TROPICAL RAINFOREST                          │  >2000 mm rain/yr
      │  Most biodiversity on Earth.                 │  Amazon, Congo, SE Asia
      │  Tall canopy, epiphytes, no seasons.         │  nutrient-poor oxisol
   EQ ├──────────────────────────────────────────────┤
      │  (Mirror image south of equator)              │
  30S ├──────────────────────────────────────────────┤
      │  TEMPERATE RAINFOREST (fragments)             │  Chile, NZ, Tasmania
      │  Wet, mild, ferns and mosses.                │  small but unique
  45S └──────────────────────────────────────────────┘
```

---

## Biome Comparison

| Biome | Latitude | Precip (mm/yr) | Temp Range | Soil | Key Species |
|-------|----------|---------------|------------|------|-------------|
| Tundra | >60° | 150-250 | -40 to 10°C | Gelisol (permafrost) | Lichens, mosses, sedges |
| Boreal/Taiga | 50-67° | 300-900 | -30 to 20°C | Spodosol (acidic) | Spruce, fir, pine, wolf, moose |
| Temperate deciduous | 35-50° | 750-1500 | -10 to 30°C | Alfisol | Oak, maple, deer, songbirds |
| Temperate grassland | 30-50° | 250-750 | -20 to 35°C | Mollisol | Prairie grass, bison, prairie dog |
| Mediterranean | 30-45° | 300-900 | 5 to 40°C | Alfisol/aridisol | Olive, cork oak, chaparral |
| Desert | 15-35° | <250 | -5 to 50°C | Aridisol | Cactus, scorpion, camel |
| Tropical savanna | 5-20° | 500-1500 | 20 to 35°C | Oxisol/ultisol | Acacia, elephant, lion |
| Tropical rainforest | 0-10° | >2000 | 24 to 30°C | Oxisol (nutrient-poor) | Canopy trees, primates, parrots |
| Temperate rainforest | 40-55° | >1500 | 5 to 20°C | Inceptisol | Ferns, mosses, old-growth conifers |
| Montane | Any (altitude) | Varies | Drops ~6°C/1000m | Varies | Alpine meadow, pikas, raptors |

---

## Why Biomes Follow Latitude

```
SOLAR ENERGY → TEMPERATURE → BIOME

  At the equator, sunlight hits the surface nearly vertically.
  At the poles, it arrives at a steep angle, spreading over
  more area and passing through more atmosphere.

  Sun angle
    ↓
  ┌────────┐          ┌────────────────────┐
  │ ██████ │ Equator  │ ████               │ 60°N
  │ ██████ │ direct   │ ████               │ oblique
  │ ██████ │ intense  │ ████               │ weak
  └────────┘          └────────────────────┘
  same beam, same beam,
  small area  spread over 2x the area

  Result: equator gets ~2.4x more solar energy per m² than 60°N.
  This drives the entire biome gradient.

  MOISTURE adds the second axis:
  same latitude + wet = forest
  same latitude + dry = grassland or desert
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Largest biome by area? | Boreal forest (taiga) — Russia + Canada + Scandinavia |
| Most biodiverse biome? | Tropical rainforest — >50% of all species on ~7% of land |
| Best soil for farming? | Temperate grassland (mollisols) — US Great Plains, Ukraine steppe |
| Why are there deserts at 30°? | Hadley Cell: air rises at equator, sinks dry at 30° |
| Why no trees in tundra? | Permafrost + wind + <60 day growing season |
| What controls biome boundaries? | Temperature (latitude/altitude) + precipitation |
| What's savanna vs. grassland? | Savanna = tropical (wet/dry, scattered trees). Grassland = temperate (no trees). |
| Most threatened biome? | Temperate grassland — 70%+ converted to agriculture |

---

## Cross-References

- **Soil types** → [atlas/03-WORLD-SOILS.md](03-WORLD-SOILS.md)
- **Climate classification** → [atlas/30-CLIMATE-CLASSIFICATION.md](30-CLIMATE-CLASSIFICATION.md) *(planned)*
- **Ecology** → [ecology/](../ecology/00-OVERVIEW.md)
- **Botany** → [botany/](../botany/00-OVERVIEW.md)
- **Wind patterns** → [atlas/02-GLOBAL-WINDS.md](02-GLOBAL-WINDS.md)
- **Watersheds** → [atlas/06-WATERSHEDS-RIVERS.md](06-WATERSHEDS-RIVERS.md)
'''

# ════════════════════════════════════════════════════════════════
# MAP 06 — WATERSHEDS & RIVERS
# ════════════════════════════════════════════════════════════════

MAP06 = f'''# 06 — Watersheds & Major Rivers

*2♠ The Ecologist — water finds a way.*

---

## World River Basins

Every drop of rain that falls on land drains to a river, and every river drains to a sea. Drainage divides — often inconspicuous ridgelines — determine which ocean gets the water. These invisible lines shape civilizations.

<svg viewBox="-185 -90 370 180" width="960" height="480" xmlns="http://www.w3.org/2000/svg" style="background:#faf8f5; font-family: Georgia, serif;">

  <defs>
{river_symbols()}
  </defs>

  <!-- Grid -->
  <line x1="-180" y1="0" x2="180" y2="0" stroke="#e0ddd8" stroke-width="0.3"/>
  <line x1="-180" y1="-30" x2="180" y2="-30" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="30" x2="180" y2="30" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="-60" x2="180" y2="-60" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="60" x2="180" y2="60" stroke="#e0ddd8" stroke-width="0.2"/>

  <text x="182" y="2" font-size="2.5" fill="#aaa">0°</text>
  <text x="182" y="-28" font-size="2.5" fill="#aaa">30°N</text>
  <text x="182" y="32" font-size="2.5" fill="#aaa">30°S</text>
  <text x="182" y="-58" font-size="2.5" fill="#aaa">60°N</text>

  <!-- Natural Earth coastlines -->
{CONTEXT}

  <!-- MAJOR RIVERS — blue curves at real coordinates -->

  <!-- Amazon (-73W to -50W, ~0°) — thickest: highest discharge on Earth -->
  <path d="M-73,0 L-70,-2 L-65,-2 L-60,-1 L-55,0 L-52,1 L-50,2"
        fill="none" stroke="#4080c0" stroke-width="1.8" stroke-linecap="round"/>
  <text x="-65" y="-5" font-size="2.5" fill="#3060a0" font-weight="bold">Amazon</text>
  <text x="-65" y="-2" font-size="1.8" fill="#5080b0">209,000 m³/s</text>

  <!-- Nile (31E, 0°N to 31E, 31°N) -->
  <path d="M33,2 L32,-2 L33,-8 L32,-15 L31,-20 L31,-25 L30,-30"
        fill="none" stroke="#4080c0" stroke-width="0.8" stroke-linecap="round"/>
  <text x="34" y="-20" font-size="2" fill="#3060a0">Nile</text>
  <text x="34" y="-17" font-size="1.5" fill="#5080b0">6,650 km</text>

  <!-- Mississippi (-90W, 47°N to -90W, 29°N) -->
  <path d="M-93,-47 L-92,-42 L-90,-38 L-91,-33 L-90,-29"
        fill="none" stroke="#4080c0" stroke-width="1.0" stroke-linecap="round"/>
  <text x="-100" y="-38" font-size="2" fill="#3060a0">Mississippi</text>

  <!-- Congo -->
  <path d="M18,2 L20,-1 L22,-2 L25,0 L27,2 L28,4 L24,5 L20,4 L15,6"
        fill="none" stroke="#4080c0" stroke-width="1.2" stroke-linecap="round"/>
  <text x="22" y="-5" font-size="2" fill="#3060a0">Congo</text>
  <text x="22" y="-2.5" font-size="1.5" fill="#5080b0">41,000 m³/s</text>

  <!-- Yangtze -->
  <path d="M92,-30 L98,-30 L104,-30 L110,-30 L116,-31 L120,-31 L122,-31"
        fill="none" stroke="#4080c0" stroke-width="1.0" stroke-linecap="round"/>
  <text x="100" y="-33" font-size="2" fill="#3060a0">Yangtze</text>

  <!-- Ganges -->
  <path d="M78,-28 L80,-25 L82,-23 L85,-23 L88,-22 L90,-22"
        fill="none" stroke="#4080c0" stroke-width="1.0" stroke-linecap="round"/>
  <text x="82" y="-18" font-size="2" fill="#3060a0">Ganges</text>
  <text x="82" y="-15.5" font-size="1.5" fill="#5080b0">38,129 m³/s</text>

  <!-- Ob -->
  <path d="M68,-55 L70,-58 L72,-62 L73,-66 L73,-70"
        fill="none" stroke="#4080c0" stroke-width="0.8" stroke-linecap="round"/>
  <text x="74" y="-62" font-size="1.8" fill="#3060a0">Ob</text>

  <!-- Yenisei -->
  <path d="M88,-52 L90,-56 L92,-62 L92,-68 L90,-72"
        fill="none" stroke="#4080c0" stroke-width="0.8" stroke-linecap="round"/>
  <text x="93" y="-60" font-size="1.8" fill="#3060a0">Yenisei</text>

  <!-- Lena -->
  <path d="M120,-55 L122,-60 L125,-65 L127,-70 L129,-73"
        fill="none" stroke="#4080c0" stroke-width="0.8" stroke-linecap="round"/>
  <text x="130" y="-65" font-size="1.8" fill="#3060a0">Lena</text>

  <!-- Murray-Darling -->
  <path d="M145,33 L142,34 L139,35 L136,35"
        fill="none" stroke="#4080c0" stroke-width="0.5" stroke-linecap="round"/>
  <text x="136" y="38" font-size="1.5" fill="#3060a0">Murray</text>

  <!-- Rhine-Danube -->
  <path d="M6,-47 L8,-48 L12,-48 L16,-47 L20,-46 L24,-45 L28,-44"
        fill="none" stroke="#4080c0" stroke-width="0.6" stroke-linecap="round"/>
  <text x="12" y="-50" font-size="1.5" fill="#3060a0">Danube</text>

  <!-- Mekong -->
  <path d="M100,-28 L102,-22 L104,-16 L105,-10 L106,-5"
        fill="none" stroke="#4080c0" stroke-width="0.7" stroke-linecap="round"/>
  <text x="106" y="-15" font-size="1.5" fill="#3060a0">Mekong</text>

  <!-- Silhouette markers -->
  <use href="#salmon" x="-128" y="-50" width="5" height="5" fill="#4080c0" opacity="0.5"/>
  <use href="#crocodile" x="25" y="0" width="6" height="6" fill="#607050" opacity="0.4"/>
  <use href="#fish" x="-58" y="-2" width="4" height="4" fill="#4080c0" opacity="0.5"/>

  <!-- Scale bar -->
  <line x1="140" y1="72" x2="150" y2="72" stroke="#444" stroke-width="0.4"/>
  <line x1="140" y1="71" x2="140" y2="73" stroke="#444" stroke-width="0.3"/>
  <line x1="150" y1="71" x2="150" y2="73" stroke="#444" stroke-width="0.3"/>
  <text x="142" y="76" font-size="2.2" fill="#444">~1,100 km</text>

  <text x="-178" y="88" font-size="1.5" fill="#bbb">Silhouettes: PhyloPic. Coastlines: Natural Earth. Both public domain.</text>

</svg>

---

## The Hydrological Cycle

```
WATER CYCLE — CROSS-SECTION

     ┌──── SOLAR ENERGY ────────────────────────────────────────┐
     │                                                           │
     ↓                                                           │
  EVAPORATION ──→ water vapor rises ──→ CONDENSATION (clouds)   │
  from oceans        ↑                      │                    │
  (86% of total)     │                      ↓                    │
                     │               PRECIPITATION               │
  EVAPOTRANSPIRATION │               (rain, snow)                │
  from land (14%)    │                      │                    │
     ↑               │                      ↓                    │
     │               │              ┌───────────────┐            │
  ┌──┴───┐           │              │   LAND        │            │
  │PLANTS│           │              │   ┌────────┐  │            │
  │ pull │           │              │   │INFILTR-│  │            │
  │water │           │              │   │ATION   │  │            │
  │ up   │           │              │   │→ ground│  │            │
  └──────┘           │              │   │  water │  │            │
                     │              │   └───┬────┘  │            │
                     │              │       │       │            │
                     │              │  RUNOFF│  → RIVERS → OCEAN │
                     │              └───────┘───────┘            │
                     │                                           │
                     └───────────── REPEAT ──────────────────────┘

  Key numbers:
    Total water on Earth:     1,386,000,000 km³
    In oceans:                97.5%
    Freshwater:               2.5%  (35,000,000 km³)
    In glaciers/ice:          68.7% of freshwater
    Groundwater:              30.1% of freshwater
    Surface water (rivers,    1.2%  of freshwater
     lakes, wetlands):        (~105,000 km³)

    Annual precipitation:     505,000 km³
    Annual evaporation:       505,000 km³  (balanced)
```

---

## Top 20 Rivers by Discharge

Discharge — not length — determines a river's importance for water supply, navigation, and ecology.

| # | River | Discharge (m³/s) | Length (km) | Basin (M km²) | Drains to |
|---|-------|-----------------|------------|----------------|-----------|
| 1 | **Amazon** | **209,000** | 6,400 | 7.05 | Atlantic |
| 2 | Congo | 41,000 | 4,700 | 3.68 | Atlantic |
| 3 | Ganges | 38,129 | 2,525 | 1.02 | Bay of Bengal |
| 4 | Orinoco | 30,000 | 2,250 | 0.88 | Atlantic |
| 5 | Yangtze | 30,166 | 6,300 | 1.81 | East China Sea |
| 6 | Yenisei | 19,600 | 5,539 | 2.58 | Arctic |
| 7 | Mississippi | 16,800 | 6,275 | 2.98 | Gulf of Mexico |
| 8 | Parana | 17,290 | 4,880 | 2.58 | Atlantic |
| 9 | Lena | 17,100 | 4,400 | 2.49 | Arctic |
| 10 | Mekong | 16,000 | 4,350 | 0.81 | South China Sea |
| 11 | Brahmaputra | 19,200 | 2,900 | 0.71 | Bay of Bengal |
| 12 | Ob | 12,475 | 5,410 | 2.97 | Arctic |
| 13 | Irrawaddy | 13,000 | 2,170 | 0.41 | Andaman Sea |
| 14 | St. Lawrence | 10,900 | 3,058 | 1.03 | Atlantic |
| 15 | Mackenzie | 10,300 | 4,241 | 1.81 | Arctic |
| 16 | Amur | 10,900 | 4,444 | 1.86 | Sea of Okhotsk |
| 17 | Niger | 5,589 | 4,200 | 2.12 | Gulf of Guinea |
| 18 | Danube | 6,500 | 2,860 | 0.82 | Black Sea |
| 19 | Nile | 2,830 | 6,650 | 3.35 | Mediterranean |
| 20 | Murray-Darling | 767 | 3,672 | 1.06 | Southern Ocean |

**The Amazon discharges more water than the next 7 rivers combined.** The Nile — the longest river — has less discharge than some tributaries of the Amazon.

---

## Drainage Divides

```
CONTINENTAL DRAINAGE — WHERE WATER GOES

  Every point on land drains to one of five destinations:

  ATLANTIC OCEAN receives:
     Amazon, Congo, Mississippi, Parana, Niger, St. Lawrence,
     Orinoco, Rhine, Danube, Nile (via Mediterranean)
     → Most of the world's largest rivers drain to the Atlantic

  PACIFIC OCEAN receives:
     Yangtze, Mekong, Amur, Columbia, Colorado
     → Fewer large rivers (narrow Pacific-side basins)

  ARCTIC OCEAN receives:
     Ob, Yenisei, Lena, Mackenzie
     → All frozen 6+ months/year — seasonal flood pulse

  INDIAN OCEAN receives:
     Ganges, Brahmaputra, Irrawaddy, Zambezi, Indus
     → Monsoon-fed — extreme seasonal variation

  ENDORHEIC (internal, no ocean outlet):
     Volga → Caspian Sea, Amu Darya → Aral Sea,
     Jordan → Dead Sea, interior Australia
     → Water evaporates, concentrates salts

  The CONTINENTAL DIVIDE is the ridgeline separating basins.
  In the Americas: the Rockies/Andes spine.
  In Africa: the Great Rift Valley highlands.
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| River with most water? | Amazon — 209,000 m³/s (20% of all river discharge to oceans) |
| Longest river? | Nile (6,650 km) but Amazon is close (6,400 km) and debated |
| Why is the Nile's discharge so low? | Passes through Sahara — extreme evaporation, no tributaries in desert |
| Where does Arctic water come from? | Ob, Yenisei, Lena — Siberian rivers draining south-to-north |
| What's an endorheic basin? | No ocean outlet. Water evaporates. Examples: Caspian, Dead Sea, Aral |
| Why does the Atlantic get the most rivers? | Continental divides (Rockies, Andes, African Rift) create huge eastward-draining basins |
| Best freshwater source? | Groundwater (30% of freshwater vs. 1.2% in rivers/lakes) |
| Most threatened river system? | Aral Sea basin (90% gone), Colorado (rarely reaches the sea) |

---

## Cross-References

- **Hydrology detail** → [hydrology/](../hydrology/00-OVERVIEW.md)
- **Ocean currents** → [atlas/18-OCEAN-CURRENTS.md](18-OCEAN-CURRENTS.md) *(planned)*
- **Biomes** → [atlas/05-GLOBAL-BIOMES.md](05-GLOBAL-BIOMES.md)
- **Soils** → [atlas/03-WORLD-SOILS.md](03-WORLD-SOILS.md)
- **Water infrastructure** → [atlas/20-WATER-INFRASTRUCTURE.md](20-WATER-INFRASTRUCTURE.md) *(planned)*
'''

# ════════════════════════════════════════════════════════════════
# MAP 07 — GRAIN & FERMENTATION BELTS
# ════════════════════════════════════════════════════════════════

MAP07 = f'''# 07 — Grain & Fermentation Belts

*2♦ The Brewer — what the land gives, and what people make of it.*

---

## Grain Growing Zones

Five grains feed the world: wheat, rice, maize, barley, and sorghum. Their ranges are set by temperature and moisture — each grain occupies a distinct latitude-climate band.

<svg viewBox="-185 -90 370 180" width="960" height="480" xmlns="http://www.w3.org/2000/svg" style="background:#faf8f5; font-family: Georgia, serif;">

  <defs>
{grain_symbols()}
  </defs>

  <!-- Grid -->
  <line x1="-180" y1="0" x2="180" y2="0" stroke="#e0ddd8" stroke-width="0.3"/>
  <line x1="-180" y1="-30" x2="180" y2="-30" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="30" x2="180" y2="30" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="-60" x2="180" y2="-60" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="60" x2="180" y2="60" stroke="#e0ddd8" stroke-width="0.2"/>

  <text x="182" y="2" font-size="2.5" fill="#aaa">0°</text>
  <text x="182" y="-28" font-size="2.5" fill="#aaa">30°N</text>
  <text x="182" y="32" font-size="2.5" fill="#aaa">30°S</text>
  <text x="182" y="-58" font-size="2.5" fill="#aaa">60°N</text>

  <!-- Natural Earth coastlines -->
{CONTEXT}

  <!-- GRAIN ZONES — colored ellipses at production centers -->

  <!-- WHEAT — golden (35-55°N band: US Plains, Ukraine, France, N China, Argentina, Australia) -->
  <ellipse cx="-100" cy="-42" rx="12" ry="5" fill="#d4a840" fill-opacity="0.4" stroke="#b08820" stroke-width="0.3"/>
  <ellipse cx="35" cy="-50" rx="10" ry="4" fill="#d4a840" fill-opacity="0.4" stroke="#b08820" stroke-width="0.3"/>
  <ellipse cx="2" cy="-48" rx="5" ry="3" fill="#d4a840" fill-opacity="0.35" stroke="#b08820" stroke-width="0.3"/>
  <ellipse cx="76" cy="-32" rx="6" ry="3" fill="#d4a840" fill-opacity="0.35" stroke="#b08820" stroke-width="0.3"/>
  <ellipse cx="-62" cy="35" rx="5" ry="3" fill="#d4a840" fill-opacity="0.35" stroke="#b08820" stroke-width="0.3"/>
  <ellipse cx="138" cy="33" rx="5" ry="3" fill="#d4a840" fill-opacity="0.3" stroke="#b08820" stroke-width="0.3"/>

  <!-- RICE — green (tropical/subtropical: SE Asia, India, China, W Africa) -->
  <ellipse cx="105" cy="-25" rx="15" ry="8" fill="#70b050" fill-opacity="0.3" stroke="#508030" stroke-width="0.3"/>
  <ellipse cx="80" cy="-22" rx="8" ry="5" fill="#70b050" fill-opacity="0.3" stroke="#508030" stroke-width="0.3"/>
  <ellipse cx="120" cy="-10" rx="10" ry="6" fill="#70b050" fill-opacity="0.25" stroke="#508030" stroke-width="0.3"/>
  <ellipse cx="-5" cy="-8" rx="6" ry="4" fill="#70b050" fill-opacity="0.2" stroke="#508030" stroke-width="0.3"/>

  <!-- MAIZE — orange (Americas + scattered: US Corn Belt, Brazil, Argentina, E Africa) -->
  <ellipse cx="-92" cy="-40" rx="8" ry="4" fill="#e08830" fill-opacity="0.35" stroke="#c06820" stroke-width="0.3"/>
  <ellipse cx="-50" cy="20" rx="6" ry="5" fill="#e08830" fill-opacity="0.3" stroke="#c06820" stroke-width="0.3"/>
  <ellipse cx="32" cy="5" rx="5" ry="4" fill="#e08830" fill-opacity="0.2" stroke="#c06820" stroke-width="0.3"/>

  <!-- Silhouette markers at major production centers -->
  <use href="#wheat" x="-105" y="-48" width="5" height="5" fill="#b08820" opacity="0.6"/>
  <use href="#wheat" x="30" y="-55" width="5" height="5" fill="#b08820" opacity="0.6"/>
  <use href="#rice" x="100" y="-30" width="5" height="5" fill="#508030" opacity="0.6"/>
  <use href="#rice" x="76" y="-28" width="5" height="5" fill="#508030" opacity="0.5"/>
  <use href="#maize" x="-96" y="-44" width="5" height="5" fill="#c06820" opacity="0.6"/>
  <use href="#barley" x="-112" y="-52" width="4" height="4" fill="#a07020" opacity="0.5"/>
  <use href="#coffee" x="-48" y="5" width="4" height="4" fill="#604020" opacity="0.5"/>
  <use href="#coffee" x="36" y="-2" width="4" height="4" fill="#604020" opacity="0.5"/>

  <!-- Labels -->
  <text x="-98" y="-36" font-size="2" fill="#b08820" font-weight="bold">Wheat Belt</text>
  <text x="90" y="-16" font-size="2" fill="#508030" font-weight="bold">Rice Paddy Zone</text>
  <text x="-88" y="-34" font-size="2" fill="#c06820" font-weight="bold">Corn Belt</text>

  <!-- Fermentation traditions — small text annotations -->
  <text x="-5" y="-42" font-size="1.8" fill="#804060" font-style="italic">Wine (grape)</text>
  <text x="133" y="-38" font-size="1.5" fill="#804060" font-style="italic">Sake (rice)</text>
  <text x="-100" y="-32" font-size="1.5" fill="#804060" font-style="italic">Bourbon (maize)</text>
  <text x="48" y="-48" font-size="1.5" fill="#804060" font-style="italic">Beer (barley)</text>
  <text x="-48" y="10" font-size="1.5" fill="#604020" font-style="italic">Coffee Belt</text>
  <text x="36" y="3" font-size="1.5" fill="#604020" font-style="italic">Coffee</text>

  <!-- Legend -->
  <rect x="-178" y="65" width="48" height="18" fill="#faf8f5" stroke="#ddd" stroke-width="0.3" rx="1"/>
  <ellipse cx="-172" cy="69" rx="3" ry="1.5" fill="#d4a840" fill-opacity="0.4"/>
  <text x="-167" y="70" font-size="2" fill="#444">Wheat (35-55° temperate)</text>
  <ellipse cx="-172" cy="73" rx="3" ry="1.5" fill="#70b050" fill-opacity="0.3"/>
  <text x="-167" y="74" font-size="2" fill="#444">Rice (tropical/subtropical)</text>
  <ellipse cx="-172" cy="77" rx="3" ry="1.5" fill="#e08830" fill-opacity="0.35"/>
  <text x="-167" y="78" font-size="2" fill="#444">Maize (Americas + scattered)</text>
  <text x="-172" y="82" font-size="1.8" fill="#804060" font-style="italic">italic = fermentation tradition</text>

  <!-- Scale bar -->
  <line x1="140" y1="68" x2="150" y2="68" stroke="#444" stroke-width="0.4"/>
  <line x1="140" y1="67" x2="140" y2="69" stroke="#444" stroke-width="0.3"/>
  <line x1="150" y1="67" x2="150" y2="69" stroke="#444" stroke-width="0.3"/>
  <text x="142" y="72" font-size="2.2" fill="#444">~1,100 km</text>

  <text x="-178" y="88" font-size="1.5" fill="#bbb">Silhouettes: PhyloPic. Coastlines: Natural Earth. Both public domain.</text>

</svg>

---

## Grain-Climate Matrix

```
WHICH GRAIN GROWS WHERE — LATITUDE × MOISTURE

  Latitude       Dry ←────────────────────→ Wet
  ─────────────────────────────────────────────────────
  55-65°N        barley (hardy,            rye
                  short season)

  35-55°N        WHEAT                     WHEAT
                  (world's #1 grain         (winter wheat
                   by area harvested)        in wetter zones)

  25-40°N/S      sorghum, millet          MAIZE (corn)
                  (drought-tolerant)        (needs 500+ mm)

  15-30°          sorghum                  sugarcane
                                            (>1500 mm)

  0-20°          millet                    RICE
                  (Sahel, W. Africa)       (needs standing water
                                            or >1200 mm rain)

  ALTITUDE OVERRIDE:
  Coffee: 1000-2000m in tropics (highland only)
  Barley: grows at highest altitude of any grain (up to 4500m in Tibet)
  Quinoa: Andean highlands 3000-4000m
```

---

## Fermentation Geography

What you drink depends on what grows where you live.

| Grain/Crop | Latitude | Fermented Product | Region |
|-----------|----------|------------------|--------|
| Barley | 45-60°N | **Beer** | N. Europe (Germany, Belgium, UK, Czech) |
| Grape | 30-50°N/S | **Wine** | Mediterranean, California, Chile, S. Africa, Australia |
| Rice | 15-35°N | **Sake** / rice wine | Japan, China, SE Asia |
| Agave | 20-25°N | **Tequila / mezcal** | Mexico (Jalisco) |
| Sugarcane | 0-25°N/S | **Rum** | Caribbean, Brazil |
| Maize | 30-45°N | **Bourbon / whiskey** | US Southeast (Kentucky, Tennessee) |
| Potato | 50-60°N | **Vodka** | Poland, Russia, Scandinavia |
| Honey | Any | **Mead** | Universal (oldest fermented drink) |
| Milk | 30-60°N | **Kumiss / kefir** | Central Asian steppe |
| Apple | 40-55°N | **Cider** | Normandy, SW England, Basque Country |

**The Coffee Belt**: 23.5°N to 23.5°S (between the tropics), 1000-2000m altitude. Ethiopia (origin), Colombia, Brazil, Vietnam, Indonesia.

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Most widely grown grain by area? | Wheat (~220M hectares) |
| Most produced grain by weight? | Maize (~1.2B tonnes/yr), then wheat, then rice |
| Why is rice tropical? | Needs standing water or >1200 mm rain + warm temps year-round |
| What grows in the coldest climates? | Barley and rye — shortest season, cold-tolerant |
| Where does coffee grow? | Tropics only, 1000-2000m altitude. The "Coffee Belt." |
| Why wine in Mediterranean? | Grapes need warm dry summers + cool winters. Mediterranean climate. |
| Oldest fermented drink? | Mead (honey wine) — Neolithic, ~7000 BCE |
| Why bourbon in Kentucky? | Maize + limestone-filtered water + white oak barrels |

---

## Cross-References

- **Spread of agriculture** → [atlas/22-SPREAD-OF-AGRICULTURE.md](22-SPREAD-OF-AGRICULTURE.md) *(planned)*
- **Soils** → [atlas/03-WORLD-SOILS.md](03-WORLD-SOILS.md)
- **Biomes** → [atlas/05-GLOBAL-BIOMES.md](05-GLOBAL-BIOMES.md)
- **Agriculture** → [agriculture/](../agriculture/00-OVERVIEW.md)
- **Fermentation** → [fermentation-spirits/](../fermentation-spirits/00-OVERVIEW.md)
- **Culinary history** → [culinary-history/](../culinary-history/00-OVERVIEW.md)
'''

# ════════════════════════════════════════════════════════════════
# MAP 08 — FLYWAYS & MIGRATION
# ════════════════════════════════════════════════════════════════

MAP08 = f'''# 08 — Flyways & Migration Routes

*2♥ The Collector — paths of the living world.*

---

## Major Bird Flyways

Eight major flyways funnel billions of birds between breeding and wintering grounds each year. The routes follow coastlines, river valleys, and mountain passes — the same corridors humans use.

<svg viewBox="-185 -90 370 180" width="960" height="480" xmlns="http://www.w3.org/2000/svg" style="background:#faf8f5; font-family: Georgia, serif;">

  <defs>
{flyway_symbols()}
  </defs>

  <!-- Grid -->
  <line x1="-180" y1="0" x2="180" y2="0" stroke="#e0ddd8" stroke-width="0.3"/>
  <line x1="-180" y1="-30" x2="180" y2="-30" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="30" x2="180" y2="30" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="-60" x2="180" y2="-60" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="60" x2="180" y2="60" stroke="#e0ddd8" stroke-width="0.2"/>

  <text x="182" y="2" font-size="2.5" fill="#aaa">0°</text>
  <text x="182" y="-28" font-size="2.5" fill="#aaa">30°N</text>
  <text x="182" y="32" font-size="2.5" fill="#aaa">30°S</text>
  <text x="182" y="-58" font-size="2.5" fill="#aaa">60°N</text>

  <!-- Natural Earth coastlines -->
{CONTEXT}

  <!-- FLYWAY ROUTES -->

  <!-- 1. Atlantic Americas (Arctic → Tierra del Fuego) — blue -->
  <path d="M-75,-70 L-72,-60 L-68,-50 L-70,-40 L-75,-30 L-78,-20
           L-75,-10 L-70,0 L-65,10 L-60,20 L-55,30 L-58,40 L-65,50"
        fill="none" stroke="#3070b0" stroke-width="1.2" stroke-dasharray="3,1.5"/>
  <text x="-62" y="-45" font-size="2.5" fill="#3070b0" font-weight="bold">Atlantic</text>
  <text x="-62" y="-42" font-size="2.5" fill="#3070b0" font-weight="bold">Americas</text>

  <!-- 2. Mississippi Flyway -->
  <path d="M-90,-60 L-92,-50 L-93,-40 L-92,-30 L-88,-25 L-85,-20"
        fill="none" stroke="#3070b0" stroke-width="1.0" stroke-dasharray="2,1"/>
  <text x="-98" y="-35" font-size="2" fill="#3070b0">Mississippi</text>

  <!-- 3. Pacific Americas -->
  <path d="M-155,-62 L-140,-55 L-128,-45 L-122,-35 L-118,-25
           L-110,-15 L-105,-5 L-95,5 L-85,15 L-78,25 L-72,35"
        fill="none" stroke="#308080" stroke-width="1.0" stroke-dasharray="2,1"/>
  <text x="-140" y="-48" font-size="2" fill="#308080">Pacific Americas</text>

  <!-- 4. East Atlantic (Scandinavia → W Africa) — green -->
  <path d="M10,-70 L5,-60 L0,-50 L-5,-40 L-8,-30 L-10,-20
           L-12,-10 L-10,0 L-5,10 L0,20 L5,30"
        fill="none" stroke="#408040" stroke-width="1.2" stroke-dasharray="3,1.5"/>
  <text x="12" y="-50" font-size="2.5" fill="#408040" font-weight="bold">East</text>
  <text x="12" y="-47" font-size="2.5" fill="#408040" font-weight="bold">Atlantic</text>

  <!-- 5. Central Asian (Siberia → India) — orange -->
  <path d="M70,-65 L68,-55 L65,-45 L62,-35 L65,-28 L70,-22
           L75,-15 L78,-10 L80,-5 L82,0"
        fill="none" stroke="#c07030" stroke-width="1.2" stroke-dasharray="3,1.5"/>
  <text x="55" y="-50" font-size="2.5" fill="#c07030" font-weight="bold">Central</text>
  <text x="55" y="-47" font-size="2.5" fill="#c07030" font-weight="bold">Asian</text>

  <!-- 6. East Asian-Australasian (Siberia → Australia/NZ) — red -->
  <path d="M120,-65 L125,-55 L128,-45 L130,-35 L128,-25
           L125,-15 L120,-5 L115,5 L118,15 L125,25 L135,35"
        fill="none" stroke="#b04040" stroke-width="1.2" stroke-dasharray="3,1.5"/>
  <text x="132" y="-40" font-size="2.5" fill="#b04040" font-weight="bold">East Asian-</text>
  <text x="132" y="-37" font-size="2.5" fill="#b04040" font-weight="bold">Australasian</text>

  <!-- 7. African-Eurasian -->
  <path d="M25,-60 L28,-50 L30,-40 L32,-30 L35,-20
           L36,-10 L35,0 L33,10 L30,20"
        fill="none" stroke="#408040" stroke-width="1.0" stroke-dasharray="2,1"/>
  <text x="36" y="-35" font-size="2" fill="#408040">African-Eurasian</text>

  <!-- WHALE MIGRATION -->
  <path d="M-70,58 L-72,45 L-75,30 L-70,18 L-62,10 L-55,5"
        fill="none" stroke="#607090" stroke-width="1.0" stroke-dasharray="4,2"/>
  <text x="-80" y="50" font-size="2" fill="#607090" font-style="italic">Humpback whale</text>

  <!-- Gray whale -->
  <path d="M-165,-58 L-145,-50 L-130,-42 L-120,-35 L-115,-28"
        fill="none" stroke="#607090" stroke-width="0.8" stroke-dasharray="3,2"/>
  <text x="-152" y="-42" font-size="1.8" fill="#607090" font-style="italic">Gray whale</text>

  <!-- MONARCH BUTTERFLY -->
  <path d="M-100,-45 L-98,-38 L-97,-30 L-100,-22 L-103,-18"
        fill="none" stroke="#d08020" stroke-width="0.8" stroke-dasharray="1,1"/>
  <text x="-105" y="-40" font-size="1.8" fill="#d08020">Monarch butterfly</text>

  <!-- LAND MIGRATION -->
  <!-- Caribou (N. Canada) -->
  <path d="M-110,-65 L-105,-62 L-100,-60 L-95,-62 L-90,-65"
        fill="none" stroke="#806040" stroke-width="0.7" stroke-dasharray="1.5,1"/>
  <text x="-108" y="-67" font-size="1.5" fill="#806040">Caribou</text>

  <!-- Wildebeest (Serengeti) -->
  <path d="M34,2 L35,5 L33,8 L30,5 L32,2 L34,2"
        fill="none" stroke="#806040" stroke-width="0.7" stroke-dasharray="1.5,1"/>
  <text x="36" y="5" font-size="1.5" fill="#806040">Wildebeest</text>

  <!-- SILHOUETTE MARKERS -->
  <use href="#barnacle_goose" x="-2" y="-42" width="6" height="6" fill="#408040" opacity="0.6"/>
  <use href="#black_tern" x="-72" y="-30" width="5" height="5" fill="#3070b0" opacity="0.6"/>
  <use href="#bar_tailed_godwit" x="122" y="-20" width="5" height="5" fill="#b04040" opacity="0.6"/>
  <use href="#humpback_whale" x="-67" y="28" width="7" height="7" fill="#607090" opacity="0.5"/>
  <use href="#monarch_butterfly" x="-104" y="-25" width="4" height="4" fill="#d08020" opacity="0.6"/>
  <use href="#flamingo" x="30" y="-8" width="5" height="5" fill="#c07080" opacity="0.5"/>
  <use href="#penguin" x="-5" y="60" width="5" height="5" fill="#333" opacity="0.4"/>
  <use href="#albatross" x="-40" y="55" width="6" height="6" fill="#555" opacity="0.4"/>
  <use href="#caribou" x="-105" y="-62" width="5" height="5" fill="#806040" opacity="0.5"/>
  <use href="#sea_turtle" x="-78" y="10" width="5" height="5" fill="#408060" opacity="0.4"/>

  <!-- Legend -->
  <rect x="-178" y="62" width="55" height="22" fill="#faf8f5" stroke="#ddd" stroke-width="0.3" rx="1"/>
  <line x1="-175" y1="66" x2="-165" y2="66" stroke="#3070b0" stroke-width="1.0" stroke-dasharray="3,1.5"/>
  <text x="-163" y="67" font-size="2" fill="#444">Bird flyway (Americas)</text>
  <line x1="-175" y1="70" x2="-165" y2="70" stroke="#408040" stroke-width="1.0" stroke-dasharray="3,1.5"/>
  <text x="-163" y="71" font-size="2" fill="#444">Bird flyway (Africa-Eurasia)</text>
  <line x1="-175" y1="74" x2="-165" y2="74" stroke="#c07030" stroke-width="1.0" stroke-dasharray="3,1.5"/>
  <text x="-163" y="75" font-size="2" fill="#444">Bird flyway (Central Asian)</text>
  <line x1="-175" y1="78" x2="-165" y2="78" stroke="#b04040" stroke-width="1.0" stroke-dasharray="3,1.5"/>
  <text x="-163" y="79" font-size="2" fill="#444">Bird flyway (E. Asian-Australasian)</text>
  <line x1="-175" y1="82" x2="-165" y2="82" stroke="#607090" stroke-width="1.0" stroke-dasharray="4,2"/>
  <text x="-163" y="83" font-size="2" fill="#444">Whale migration</text>

  <!-- Scale bar -->
  <line x1="140" y1="68" x2="150" y2="68" stroke="#444" stroke-width="0.4"/>
  <line x1="140" y1="67" x2="140" y2="69" stroke="#444" stroke-width="0.3"/>
  <line x1="150" y1="67" x2="150" y2="69" stroke="#444" stroke-width="0.3"/>
  <text x="142" y="72" font-size="2.2" fill="#444">~1,100 km</text>

  <text x="-178" y="88" font-size="1.5" fill="#bbb">Silhouettes: PhyloPic (CC0/CC-BY). Coastlines: Natural Earth (public domain).</text>

</svg>

---

## Why Birds Migrate

```
MIGRATION MECHANICS — WHAT DRIVES THE JOURNEY

  TRIGGER: day length (photoperiod)
  ─────────────────────────────────
  As days shorten in autumn, hormonal changes trigger
  restlessness (Zugunruhe) and fat deposition. The bird's
  body prepares for a flight it has never taken before.

  NAVIGATION: four compass systems
  ─────────────────────────────────
  1. SUN COMPASS    — time-compensated azimuth
                      (knows sun's arc changes with season)
  2. STAR COMPASS   — calibrated to celestial rotation
                      (learned by watching sky rotate as a juvenile)
  3. MAGNETIC SENSE — detects Earth's magnetic field
                      (cryptochrome proteins in retina — quantum biology)
  4. LANDMARKS      — coastlines, rivers, mountain ranges
                      (learned on first migration with parents)

  ENERGY: fuel and range
  ─────────────────────
  Pre-migration fat loading: 50-100% body weight increase.
  Flight speed: 30-80 km/h depending on species.
  Bar-tailed godwit: 11,000 km nonstop (Alaska → New Zealand)
  — longest nonstop flight of any bird, 8-9 days without rest.

  WHY NOT STAY?
  ───────────────
  Arctic summer: 24-hour daylight → massive insect bloom
  → virtually unlimited food for 3 months.
  Arctic winter: no food. The energy cost of migration is
  less than the energy cost of surviving winter at high latitude.
```

---

## Migration Distance Records

| Species | Route | Distance | Duration | Notes |
|---------|-------|----------|----------|-------|
| **Arctic tern** | Arctic → Antarctic → Arctic | 71,000 km/yr | Year-round | Longest migration of any animal |
| **Bar-tailed godwit** | Alaska → New Zealand | 11,000 km nonstop | 8-9 days | Longest nonstop flight |
| **Humpback whale** | Antarctic → tropics | 16,000 km round trip | 6 months | Breeds in warm water, feeds in cold |
| **Gray whale** | Alaska → Baja California | 20,000 km round trip | 4 months | Longest mammal migration |
| **Monarch butterfly** | Canada → Mexico | 4,000 km | 2 months | Multi-generational return trip |
| **Wildebeest** | Serengeti circuit | 1,500 km | Year-round | 1.5 million animals in loop |
| **Caribou** | Canadian tundra → boreal | 5,000 km round trip | Seasonal | Largest land migration by biomass |
| **Leatherback turtle** | Tropics → subarctic | 16,000 km round trip | Year-round | Deepest-diving migrant |
| **Salmon** | Ocean → birth river | 1,000-3,000 km | 2-4 weeks | One-way trip; die after spawning |

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Longest migration? | Arctic tern — 71,000 km/yr, pole to pole |
| Longest nonstop flight? | Bar-tailed godwit — 11,000 km, Alaska to NZ, no landing |
| What triggers migration? | Day length (photoperiod) → hormonal cascade |
| How do birds navigate? | 4 systems: sun compass, star compass, magnetic sense, landmarks |
| Why migrate at all? | Arctic summer food bonanza > energy cost of flight |
| Largest land migration? | Wildebeest — 1.5 million animals circling the Serengeti |
| Which flyway has most birds? | East Asian-Australasian — ~50 million shorebirds |
| Most threatened flyway? | East Asian-Australasian — Yellow Sea stopover sites being lost to development |

---

## Cross-References

- **Ornithology** → [ornithology/](../ornithology/00-OVERVIEW.md)
- **Marine biology** → [marine-biology/](../marine-biology/00-OVERVIEW.md)
- **Biomes** → [atlas/05-GLOBAL-BIOMES.md](05-GLOBAL-BIOMES.md)
- **Ocean currents** → [atlas/18-OCEAN-CURRENTS.md](18-OCEAN-CURRENTS.md) *(planned)*
- **Exploration routes** → [atlas/41-EXPLORATION-ROUTES.md](41-EXPLORATION-ROUTES.md) *(planned)*
'''


# ════════════════════════════════════════════════════════════════
# WRITE ALL FILES
# ════════════════════════════════════════════════════════════════

for num, content in [(5, MAP05), (6, MAP06), (7, MAP07), (8, MAP08)]:
    names = {
        5: "05-GLOBAL-BIOMES.md",
        6: "06-WATERSHEDS-RIVERS.md",
        7: "07-GRAIN-FERMENTATION-BELTS.md",
        8: "08-FLYWAYS-MIGRATION.md",
    }
    path = f"../{names[num]}"
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.lstrip('\n'))
    print(f"Wrote {names[num]} ({len(content):,} chars)")

print("\nSection II complete — 4 maps with Natural Earth coastlines + PhyloPic silhouettes.")
