# Precipitation and Clouds — Bergeron-Findeisen, Cloud Classification

## The Big Picture

Clouds form when air cools to its dewpoint. But cloud droplets are too small (~10 μm) to fall as precipitation — they must grow. Two mechanisms dominate: the Bergeron-Findeisen process (ice crystal growth in mixed-phase clouds, dominant in mid-latitudes) and collision-coalescence (droplet collection in warm clouds, dominant in tropics).

```
+---------------------------------------------------------------+
|           PRECIPITATION FORMATION PATHWAYS                    |
|                                                               |
|  Cloud forms (cooling → condensation on CCN)                  |
|          |                                                    |
|          v                                                    |
|   DROPLETS ~10 μm (too small to fall)                         |
|          |                                                    |
|    [T > 0°C]           [T < 0°C mixed phase]                  |
|          |                      |                             |
|          v                      v                             |
|   COLLISION-            BERGERON-FINDEISEN                    |
|   COALESCENCE           (ice crystal process)                 |
|   (warm cloud)          (mixed-phase cloud)                   |
|          |                      |                             |
|          v                      v                             |
|   Large droplets         Ice crystals grow                    |
|   (tropical rain)        → aggregate → melt                   |
|          |               → fall as rain or snow               |
|          v                                                    |
|   PRECIPITATION (rain, snow, hail, sleet, freezing rain)      |
+---------------------------------------------------------------+
```

---

## Bergeron-Findeisen Process — Ice Crystal Growth

The fundamental insight: at sub-zero temperatures, the saturation vapor pressure over **liquid water** is higher than over **ice**. In a mixed-phase cloud (both supercooled droplets and ice crystals coexist):

```
SATURATION VAPOR PRESSURE:
  e_liquid > e_ice   (at same sub-zero temperature)

  Therefore in a mixed-phase cloud:
    - Air is supersaturated with respect to ICE
    - Air is at saturation or slightly unsaturated with respect to LIQUID

  Result:
    - Ice crystals grow (depositional growth; vapor deposits on them)
    - Liquid droplets evaporate (they're in slightly subsaturated air)
    - Net transfer: mass moves from liquid droplets to ice crystals
    - Ice crystals grow rapidly → aggregate → eventually fall
```

**Why this matters for mid-latitude precipitation:**
- Most precipitation that reaches the surface originates as ice
- Even summer rain showers in mid-latitudes often start as snow aloft
- Seeding a cloud with ice nuclei (silver iodide) can trigger precipitation

**Ice nuclei** — needed to initiate ice formation (homogeneous nucleation requires ~-40°C). Heterogeneous nucleation occurs at warmer temperatures (-5° to -20°C) on ice nuclei:
- Dust (kaolinite, quartz)
- Biological particles (bacteria, fungi — active at only -4 to -5°C!)
- Silver iodide (artificial; cloud seeding)

---

## Collision-Coalescence — Warm Cloud Process

In tropical clouds where cloud tops stay above 0°C (all-liquid clouds):

```
SIZE SPECTRUM:
  Cloud condensation nuclei (CCN): 0.01–1 μm
  Cloud droplets: 5–100 μm (too small to fall)
  Drizzle drops: 100–500 μm
  Rain drops: 500–5000 μm (0.5–5 mm)

COLLECTION MECHANISM:
  Large droplets fall faster than small droplets
  Large drops collide with small drops → merge (coalescence)
  Drop grows exponentially if collection efficiency is high

COLLISION EFFICIENCY:
  Very small drops curve around larger drops (streamlines)
  Very large drops may splash apart
  Optimal size match: medium "collector" + smaller droplets
```

**Salt particles (marine CCN)** — sea spray produces large CCN. In maritime tropical air, CCN are relatively few but large → fewer but larger drops → more efficient collision-coalescence → heavier tropical rain. Continental air has many small CCN → lots of tiny droplets → less efficient coalescence → need Bergeron process for precipitation.

---

## Cloud Classification — Luke Howard's System (1803)

```
VERTICAL EXTENT AND ALTITUDE (mid-latitudes):

HIGH CLOUDS (above 6 km; all ice or ice+water):
  Cirrus (Ci)          Fibrous, wispy, "mare's tails"; ice crystals
  Cirrocumulus (Cc)    Small rounded white puffs; "mackerel sky"
  Cirrostratus (Cs)    Thin sheet; causes halos around Sun/Moon
                       (classic warm front approach indicator)

MIDDLE CLOUDS (2–6 km; often mixed phase):
  Altocumulus (Ac)     Grey/white patches or rolls; can produce virga
  Altostratus (As)     Grey/blue sheet; sun seen as "through ground glass"
                       (no halo); precedes warm front precipitation

LOW CLOUDS (below 2 km; liquid or mixed):
  Stratus (St)         Grey, featureless sheet; drizzle; fog-lifted
  Stratocumulus (Sc)   Lumpy grey/white layer; most common cloud worldwide
  Nimbostratus (Ns)    Dark grey; continuous rain/snow; thick; no bottom

VERTICAL DEVELOPMENT (all altitudes):
  Cumulus (Cu)         Flat bottom (LCL), cauliflower top; fair weather Cu
                       (shallow) or towering Cu (Tcu, growing)
  Cumulonimbus (Cb)    Full storm cloud; extends from near surface to
                       tropopause; ice anvil top; all precipitation types
```

**Vertical extent abbreviations and special forms:**

| Name | Special Form | Description |
|------|-------------|-------------|
| Cumulonimbus incus | Anvil | Top spreads horizontally at tropopause (Cb with anvil) |
| Lenticular (Ac len) | Lens-shaped | Orographic standing wave; smooth, often mistaken for UFOs |
| Mammatus | Pouches | Hanging from Cb anvil; turbulent air |
| Pileus | Cap cloud | Thin smooth cap above growing Cu |
| Virga | Precipitation shafts | Precipitation falling but evaporating before hitting ground |
| Banner cloud | Flag | Permanent cloud on lee side of peak |

---

## Precipitation Types

```
TEMPERATURE PROFILE → PRECIPITATION TYPE:

TYPE 1: ALL ABOVE 0°C
  Liquid from cloud top to surface → RAIN

TYPE 2: COLD SURFACE LAYER (surface < 0°C, warm aloft)
  Snow/ice → melts in warm layer → refreezes near surface
  → FREEZING RAIN / ICE STORM (most destructive winter precip)
  (surface coated with clear ice; powerlines, trees collapse)

TYPE 3: THIN WARM LAYER (snow aloft → brief warm layer → cold)
  Snow → partially melts → refreezes
  → SLEET (ice pellets; rattles on windows)
  (crunchy, bounces)

TYPE 4: ALL BELOW 0°C
  Ice crystals never melt
  → SNOW (fluffy if T very cold; wet/heavy if near 0°C)

TYPE 5: SEVERE THUNDERSTORM
  Updraft carries ice up multiple times
  → HAIL (growth layers like onion rings)
  Hailstone size: pea (~6mm) to softball (~100mm+)
  Largest recorded: ~20 cm (South Dakota, 2010)
```

**Snow density** — New fluffy snow: 50–100 kg/m³. Settled older snow: 200–400 kg/m³. Ice: 900 kg/m³. "10:1 ratio" is a rough rule (10 inches snow = 1 inch liquid water equivalent) but varies from 4:1 (heavy wet snow) to 30:1 (powder snow).

---

## Fog Types

Fog = stratus cloud at the surface (visibility < 1 km). Multiple formation mechanisms:

```
TYPE            MECHANISM                           WHERE/WHEN
--------------  ---------------------------------   -------------------------
Radiation fog   Clear night, calm winds;            Valley bottoms, inland;
                surface cools by radiation;         autumn nights; "tule fog"
                air above chilled → fog forms       (Central Valley, CA)

Advection fog   Warm moist air advects over         West Coast marine layer;
                cold surface (cold ocean/land)      sea smoke; Great Lakes
                Air cools → fog

Upslope fog     Moist air lifted orographically     Appalachians, east slopes
                → cools adiabatically → fog         of Rockies

Precipitation/  Evaporation from rain adds          Ahead of warm front
Frontal fog     moisture near saturation surface

Valley fog      Cold air drains into valleys at     Mountain terrain;
                night; high humidity → fog          autumn/winter nights
```

---

## Radar Reflectivity and Precipitation Rate

Doppler weather radar (WSR-88D, NEXRAD) measures reflectivity Z (dBZ):

```
dBZ    PRECIPITATION RATE    DESCRIPTION
-----  --------------------  -----------------------------------
< 20   None/light drizzle    Ground clutter, clear air return
20–30  Light rain            Light showers, possible snow
30–40  Moderate rain         Moderate showers; scattered T-storms
40–50  Heavy rain            Heavy rain; strong thunderstorms
50–60  Very heavy/hail       Severe thunderstorms; possible hail
> 60   Extreme; hail likely  Supercells; large hail definite
> 70   Giant hail            Extreme supercell; baseball+ hail
```

**Z-R relationship:** R = (Z/300)^(1/1.4) [mm/hr; empirical, highly variable by storm type]

---

## Decision Cheat Sheet

| Cloud type seen | Forecast implication |
|----------------|---------------------|
| Cirrus thickening to cirrostratus | Warm front approaching 12–36 hrs |
| Rapid growth of cumulus towers | Convective initiation; T-storms possible |
| Cumulonimbus with anvil spreading upwind | Severe storm; hail/tornado risk |
| Stratocumulus layer, persistent | Stable; little precipitation |
| Dark nimbostratus; prolonged steady rain | Frontal system (warm front) |
| Mammatus under Cb anvil | Severe turbulence possible; storm mature/dissipating |
| Virga but no rain reaching ground | Dry mid-levels; evaporation; downburst risk |

---

## Common Confusion Points

**Sleet vs freezing rain** — Sleet (ice pellets) has a complete refreeze before landing → bounces/crunches. Freezing rain is liquid when it lands, then freezes on contact with surfaces → clear ice coating. Both require a warm layer aloft overlying a cold surface layer, but the surface cold layer is thicker for sleet.

**Why doesn't it snow when it's "too cold"?** — Extreme cold means very low moisture (air holds less water vapor) → low snowfall rates even during storms. The heaviest snowfalls occur near 0°C (maximum moisture) not at -20°C. "Too cold to snow" is somewhat valid — but there's no absolute floor, just reduced intensity.

**Radar reflectivity and hail** — High reflectivity (>60 dBZ) in summer storms often indicates hail, not just heavy rain. Hail particles are large, dense, and highly reflective. Dual-polarization radar can distinguish hail from rain by examining the differential reflectivity (Zdr) — hail has low Zdr (tumbling → not oblate like raindrops).

**Cloud classification by altitude** — Cloud names encode altitude: Alto- = middle level, Cirr- = high level. Cumulo- = heaped (vertical development). Nimbo- = rain-bearing. So nimbostratus = layered (stratus) rain cloud. Altostratus = mid-level layered cloud. Cumulonimbus = the big vertical storm cloud.
