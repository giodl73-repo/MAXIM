# Geology — Overview

**Bridge — Earth as a coupled reservoir system:** Think of Earth as a set of finite-capacity reservoirs (core, mantle, crust, hydrosphere, atmosphere, biosphere) exchanging energy and mass across well-defined interfaces. Each interface has characteristic flux rates and transfer functions: mantle convection moves heat from core-mantle boundary to crust on ~10⁸-year timescales; weathering moves mass from crust to ocean on ~10⁴-year timescales; the carbon cycle exchanges CO₂ between atmosphere and ocean on ~10²-year timescales. The system is never at equilibrium — it's a set of coupled differential equations with very different time constants per reservoir. Plate tectonics is the dominant long-period controller; the atmosphere/ocean are the fast-response layer. Every geological process is a flux between two of these reservoirs.

## The Big Picture

Earth is a heat engine wrapped in a thin rocky shell. Everything in geology — mountains, earthquakes, ore deposits, the fossil record — flows from the interplay between internal heat (radioactive decay + primordial accretion energy) and external solar energy driving weathering and erosion.

```
+------------------------------------------------------------------+
|                    EARTH AS A SYSTEM                              |
|                                                                   |
|  INTERNAL ENGINE              EXTERNAL ENGINE                     |
|  +-----------------------+    +---------------------------+       |
|  | Core heat +           |    | Solar radiation           |       |
|  | radioactive decay     |    | Water cycle               |       |
|  | +--> mantle convection|    | Atmosphere/biosphere      |       |
|  | +--> plate tectonics  |    | +--> weathering/erosion   |       |
|  | +--> volcanism        |    | +--> sediment transport   |       |
|  | +--> metamorphism     |    | +--> soil formation       |       |
|  +-----------------------+    +---------------------------+       |
|           |                              |                        |
|           v                              v                        |
|  +---------------------------------------------+                 |
|  |              ROCK CYCLE                      |                 |
|  |  Magma --> Igneous --> Weathering -->         |                 |
|  |  Sediment --> Sedimentary --> Burial -->      |                 |
|  |  Metamorphic --> Melting --> Magma           |                 |
|  +---------------------------------------------+                 |
|                                                                   |
|  OUTPUTS: Landforms / Ore deposits / Fossil record /             |
|           Soils / Petroleum / CO₂ fluxes                         |
+------------------------------------------------------------------+
```

---

## Earth Structure — The Layered Planet

```
DEPTH        LAYER              COMPOSITION              STATE
-----------  -----------------  -----------------------  ----------------
0–35 km      CRUST              Silicates                Solid, brittle
             (continental ~30,  (Si-Al-rich continents,  (seismic P+S)
              oceanic ~7 km)     Si-Mg-Fe-rich ocean)

35–2890 km   MANTLE             Peridotite               Solid but ductile
             Upper: 35–670 km   (Mg-Fe silicates:        flows on 10⁵–10⁷ yr
             Lower: 670–2890 km  olivine/pyroxene)        timescales

2890–        OUTER CORE         Iron-Nickel alloy        LIQUID
5150 km                         + light elements         Convection drives
                                 (S, O, Si)              geodynamo /
                                                         magnetic field

5150–        INNER CORE         Iron-Nickel              SOLID
6371 km                         (crystalline bcc Fe)     Pressure freezes
                                                         despite ~5000°C
                                                         Rotates slightly
                                                         faster than mantle
```

**Key seismic discontinuities:**
- **Moho** — crust/mantle boundary; P-wave velocity jumps from ~7 to ~8 km/s
- **410-km discontinuity** — olivine → wadsleyite phase transition
- **660-km discontinuity** — ringwoodite → bridgmanite (blocks some convection)
- **CMB (Core-Mantle Boundary)** — dramatic: liquid iron against solid silicate

---

## The Rock Cycle

Three rock families, connected by processes operating on vastly different timescales:

```
                         MAGMA
                        /     \
               Cooling /       \ Melting (burial
          (intrusive)  /         \ + heat ~700–1200°C)
                      v           ^
               IGNEOUS            |
               ROCKS          METAMORPHIC
               |    \         ROCKS
  Weathering + |     \            ^
  Erosion      |      \_________  |
               v      Burial +    | Heat + Pressure
          SEDIMENT    compaction  | (no melting)
               |                  |
               | Lithification    |
               v                  |
          SEDIMENTARY ----------->+
          ROCKS      (deep burial)
```

| Rock Family | Formation Process | Key Examples |
|-------------|------------------|--------------|
| **Igneous** | Cooling of magma/lava | Granite (slow, coarse), Basalt (fast, fine), Obsidian (quenched) |
| **Sedimentary** | Weathering → transport → deposition → lithification | Sandstone, Shale, Limestone, Coal |
| **Metamorphic** | Existing rock recrystallized by T+P (no melting) | Marble←Limestone, Quartzite←Sandstone, Schist, Gneiss |

---

## Geologic Time — Deep Time Intuition

```
EON           ERA          PERIOD           START (Ma)   KEY EVENT
-----------   ----------   --------------   ----------   ----------------------------
PHANEROZOIC   CENOZOIC     Quaternary       2.6          Ice ages; Homo ~0.3 Ma
(541–now)                  Neogene          23           Grasses; C4 expansion
                           Paleogene        66           K-Pg extinction; mammal radiation
              MESOZOIC     Cretaceous       145          Angiosperms; chalk seas
                           Jurassic         200          Dinosaur peak; Pangea breakup
                           Triassic         252          Recovery from P-T extinction
              PALEOZOIC    Permian          299          P-T extinction (96% marine spp)
                           Carboniferous    359          Coal swamps; first reptiles
                           Devonian         419          First forests; fish diversify
                           Silurian         444          Land plants; O-S recovery
                           Ordovician       485          Marine invertebrate diversity peak
                           Cambrian         541          Cambrian explosion — body plans

PROTEROZOIC                                 2500         Eukaryotes; snowball Earth
ARCHEAN                                     4000         First life ~3.8 Ga
HADEAN                                      4600         Earth forms; Moon-forming impact
```

**Ma = million years ago; Ga = billion years ago**

The Big 5 mass extinctions (% marine genera lost):
1. **Ordovician-Silurian** 444 Ma — 57%
2. **Late Devonian** 375 Ma — 35%
3. **Permian-Triassic** 252 Ma — 96% ← worst ever
4. **Triassic-Jurassic** 200 Ma — 47%
5. **Cretaceous-Paleogene (K-Pg)** 66 Ma — 75% (Chicxulub impact)

---

## Plate Tectonics — The Unifying Framework

```
RIDGE                 SUBDUCTION ZONE            COLLISION
(divergent)           (convergent)               (continent-continent)

  ^   ^               Ocean  |  Continent        +---------+  +---------+
  |   |              Trench  |  arc               |         |  |         |
~~+~~~+~~    ~~~~~~~~~vvvvvvvv|~~~~~~~~~           |   Cont  |  |   Cont  |
   \ /         \___________  |  /\                +---------+  +---------+
    v     ~~~~~\  Oceanic  \ | /  \                   |          |
  Magma          \  slab   \|/    Melting → arc       +---/\/\---+
  upwells          \sink    v     volcanoes          Himalayan-type
  (mid-ocean        \  into mantle                   orogeny
   ridge)            \
```

| Boundary Type | Motion | Example | Products |
|---------------|--------|---------|---------|
| Divergent | Away from each other | Mid-Atlantic Ridge | Ocean crust, rift valleys |
| Convergent (ocean-ocean) | Together | Mariana Trench + Japan arc | Subduction, arc volcanoes |
| Convergent (ocean-continent) | Together | Cascades, Andes | Subduction, mountain chains |
| Convergent (cont-cont) | Together | Himalayas | Mountain belts, no subduction |
| Transform | Side by side | San Andreas Fault | Earthquakes, no volcanism |

---

## Decision Cheat Sheet — Which Guide First?

| If you want to understand... | Start here |
|------------------------------|-----------|
| Why earthquakes and volcanoes are where they are | `05-PLATE-TECTONICS.md` → `06-EARTHQUAKES-VOLCANOES.md` |
| How to date a rock or event | `07-GEOLOGIC-TIME.md` |
| What a rock sample is made of | `01-MINERALS.md` → rock type guide (02, 03, or 04) |
| Why a mineral deposit exists where it does | `08-ECONOMIC-GEOLOGY.md` |
| How a landscape formed (valley, glacier, cave) | `09-SURFICIAL-GEOLOGY.md` |
| Why Mars and Moon look so different from Earth | `10-PLANETARY-GEOLOGY.md` |
| How mountains form and erode | `05-PLATE-TECTONICS.md` → `04-METAMORPHIC-ROCKS.md` |
| The full sequence of Earth history | `07-GEOLOGIC-TIME.md` → `00-OVERVIEW.md` time table |
| How oil and gas form | `03-SEDIMENTARY-ROCKS.md` → `08-ECONOMIC-GEOLOGY.md` |

## Directory Map

| File | Core Concept |
|------|-------------|
| `01-MINERALS.md` | Crystal systems, silicate tetrahedra, identification |
| `02-IGNEOUS-ROCKS.md` | Magma differentiation, Bowen's reaction series |
| `03-SEDIMENTARY-ROCKS.md` | Earth's archive — stratigraphy, Steno |
| `04-METAMORPHIC-ROCKS.md` | P-T paths, facies diagram, foliation |
| `05-PLATE-TECTONICS.md` | Seafloor spreading, Wilson cycle, mantle plumes |
| `06-EARTHQUAKES-VOLCANOES.md` | Seismic waves, Mw scale, eruption types |
| `07-GEOLOGIC-TIME.md` | Radiometric dating, stratigraphic principles |
| `08-ECONOMIC-GEOLOGY.md` | Ore deposits, petroleum systems, critical minerals |
| `09-SURFICIAL-GEOLOGY.md` | Glacial/fluvial/karst — sculpting the surface |
| `10-PLANETARY-GEOLOGY.md` | Moon, Mars, Venus — comparative geology |

---

## Key Measurement Systems

| Quantity | Unit / Scale | Notes |
|----------|-------------|-------|
| Time | Ma (million yr), Ga (billion yr) | Ma = mega-annum |
| Earthquake size | Moment magnitude Mw | Log scale; each unit = 32× energy |
| Volcanic explosivity | VEI 0–8 | Log scale; VEI 8 = supervolcano |
| Mineral hardness | Mohs 1–10 | Ordinal, not linear |
| Geothermal gradient | ~25–30°C/km (continental) | Higher near ridges, hotspots |
| Seismic velocity | km/s (P-waves ~6–14 km/s) | Used to image Earth's interior |

---

## Common Confusion Points

**"Continental drift" vs plate tectonics** — Wegener (1912) proposed drift based on coastline fit + fossil correlations. The mechanism (seafloor spreading, slab pull) wasn't established until the 1960s. Plate tectonics is the complete theory; continental drift was just the observational puzzle.

**Crust vs lithosphere** — The lithosphere = crust + uppermost brittle mantle (~100 km total). Plates are lithospheric plates, not just crustal plates. The ductile asthenosphere below is where flow happens on million-year timescales.

**Rock vs mineral** — A mineral is a naturally occurring crystalline solid with defined chemical composition. A rock is an aggregate of minerals. Granite contains quartz + feldspar + mica/hornblende. Rock salt is the mineral halite.

**Geologic time intuition** — Earth: 4.6 Ga. Multi-celled animals: ~600 Ma. Dinosaur extinction: 66 Ma. Homo sapiens: ~0.3 Ma = 0.007% of Earth history. All of written human civilization: last 5,000 years = 0.0001%.
