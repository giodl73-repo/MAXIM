"""Assemble map 01 (Tectonic Plates) with Natural Earth coastlines."""

def read_svg_fragment(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

COASTLINES = read_svg_fragment('world_full_int.svg')

MAP01 = r'''# 01 — Tectonic Plates & Geological Provinces

*3♣ The Timekeeper — deep time written in stone.*

---

## World Plate Boundaries

Earth's lithosphere is broken into ~15 major plates and dozens of microplates, all riding on the asthenosphere (~100-300 km deep, partially molten, convecting). The plates move 1-15 cm/year — imperceptible until they don't, and then catastrophic.

<svg viewBox="-185 -90 370 180" width="960" height="480" xmlns="http://www.w3.org/2000/svg" style="background:#faf8f5; font-family: Georgia, serif;">

  <!-- Grid lines -->
  <line x1="-180" y1="0" x2="180" y2="0" stroke="#e0ddd8" stroke-width="0.3"/>
  <line x1="-180" y1="-30" x2="180" y2="-30" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="30" x2="180" y2="30" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="-60" x2="180" y2="-60" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-180" y1="60" x2="180" y2="60" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="0" y1="-90" x2="0" y2="90" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="-90" y1="-90" x2="-90" y2="90" stroke="#e0ddd8" stroke-width="0.2"/>
  <line x1="90" y1="-90" x2="90" y2="90" stroke="#e0ddd8" stroke-width="0.2"/>

  <!-- Lat/lon labels -->
  <text x="182" y="1.5" font-size="2.5" fill="#aaa">0°</text>
  <text x="182" y="-28.5" font-size="2.5" fill="#aaa">30°N</text>
  <text x="182" y="31.5" font-size="2.5" fill="#aaa">30°S</text>
  <text x="182" y="-58.5" font-size="2.5" fill="#aaa">60°N</text>
  <text x="182" y="61.5" font-size="2.5" fill="#aaa">60°S</text>
  <text x="-1" y="-82" font-size="2.5" fill="#aaa">0°</text>
  <text x="-91" y="-82" font-size="2.5" fill="#aaa">90°W</text>
  <text x="89" y="-82" font-size="2.5" fill="#aaa">90°E</text>

  <!-- CONTINENT OUTLINES — Natural Earth 110m public domain data -->
''' + COASTLINES + r'''
  <!-- PLATE BOUNDARIES -->

  <!-- Mid-Atlantic Ridge (divergent) — red dashed -->
  <path d="M-18,-68 L-20,-60 L-22,-50 L-25,-40 L-28,-30 L-30,-20
           L-28,-10 L-25,0 L-20,10 L-15,20 L-10,30 L-5,40 L0,50 L5,58"
        fill="none" stroke="#c04040" stroke-width="1.0" stroke-dasharray="2,1"/>

  <!-- East Pacific Rise (divergent) -->
  <path d="M-115,55 L-110,45 L-108,35 L-105,25 L-103,15 L-105,5 L-110,-5 L-115,-15"
        fill="none" stroke="#c04040" stroke-width="1.0" stroke-dasharray="2,1"/>

  <!-- Indian Ocean Ridge system -->
  <path d="M5,58 L20,50 L35,42 L50,35 L65,30 L75,20 L80,10 L90,5"
        fill="none" stroke="#c04040" stroke-width="0.8" stroke-dasharray="2,1"/>
  <path d="M65,30 L55,20 L45,10 L40,0 L38,-10"
        fill="none" stroke="#c04040" stroke-width="0.8" stroke-dasharray="2,1"/>

  <!-- East African Rift (divergent) -->
  <path d="M38,-15 L36,-8 L35,0 L33,8 L32,15 L34,22"
        fill="none" stroke="#c04040" stroke-width="0.7" stroke-dasharray="1.5,1"/>

  <!-- Ring of Fire subduction zones (convergent) — blue solid -->
  <path d="M-74,55 L-72,48 L-75,40 L-78,30 L-80,20 L-82,10 L-85,0
           L-90,-5 L-95,-15 L-105,-20 L-115,-28 L-125,-35 L-130,-42
           L-135,-48 L-148,-55 L-160,-58 L-170,-60"
        fill="none" stroke="#4060c0" stroke-width="0.9"/>
  <path d="M-170,-60 L-175,-55 L-180,-52"
        fill="none" stroke="#4060c0" stroke-width="0.9"/>
  <path d="M180,-52 L170,-50 L163,-55 L158,-52"
        fill="none" stroke="#4060c0" stroke-width="0.9"/>
  <path d="M158,-52 L150,-45 L142,-38 L138,-32 L132,-25 L125,-18 L118,-10
           L112,-4 L108,0 L104,4"
        fill="none" stroke="#4060c0" stroke-width="0.9"/>
  <path d="M180,18 L176,22 L174,28 L172,35 L170,42"
        fill="none" stroke="#4060c0" stroke-width="0.7"/>

  <!-- Alpine-Himalayan collision belt — orange -->
  <path d="M-10,-38 L0,-37 L10,-38 L20,-40 L30,-42 L40,-38
           L50,-33 L60,-30 L70,-28 L80,-28 L90,-30 L100,-28"
        fill="none" stroke="#c08030" stroke-width="0.9"/>

  <!-- San Andreas Transform — green -->
  <path d="M-125,-35 L-122,-38 L-118,-42"
        fill="none" stroke="#408040" stroke-width="0.8"/>

  <!-- PLATE LABELS -->
  <text x="-160" y="5" font-size="3.5" fill="#555" font-weight="bold">PACIFIC</text>
  <text x="-160" y="9" font-size="2.5" fill="#777">103.3 M km²</text>
  <text x="-110" y="-50" font-size="3" fill="#555" font-weight="bold">NORTH</text>
  <text x="-110" y="-47" font-size="3" fill="#555" font-weight="bold">AMERICAN</text>
  <text x="-55" y="25" font-size="3" fill="#555" font-weight="bold">SOUTH</text>
  <text x="-55" y="28" font-size="3" fill="#555" font-weight="bold">AMERICAN</text>
  <text x="5" y="-55" font-size="3" fill="#555" font-weight="bold">EURASIAN</text>
  <text x="5" y="8" font-size="3" fill="#555" font-weight="bold">AFRICAN</text>
  <text x="90" y="-50" font-size="2.5" fill="#555" font-weight="bold">EURASIAN</text>
  <text x="90" y="-47" font-size="2.0" fill="#777">(cont.)</text>
  <text x="72" y="-12" font-size="2.5" fill="#555" font-weight="bold">INDIAN</text>
  <text x="125" y="25" font-size="2.5" fill="#555" font-weight="bold">AUSTRALIAN</text>
  <text x="-105" y="5" font-size="2.2" fill="#555">NAZCA</text>
  <text x="-95" y="-8" font-size="2.2" fill="#555">COCOS</text>
  <text x="-90" y="-25" font-size="2" fill="#555">CARIBBEAN</text>
  <text x="42" y="-18" font-size="1.8" fill="#555" font-style="italic">ARABIAN</text>
  <text x="145" y="-40" font-size="2" fill="#555">PHILIPPINE</text>
  <text x="145" y="-37" font-size="2" fill="#555">SEA</text>
  <text x="-20" y="78" font-size="3" fill="#555" font-weight="bold">ANTARCTIC</text>

  <!-- Water labels -->
  <text x="-165" y="-30" font-size="3" fill="#a0b0c0" font-style="italic">Pacific</text>
  <text x="-165" y="-27" font-size="3" fill="#a0b0c0" font-style="italic">Ocean</text>
  <text x="-35" y="-12" font-size="2.8" fill="#a0b0c0" font-style="italic">Atlantic</text>
  <text x="60" y="18" font-size="2.8" fill="#a0b0c0" font-style="italic">Indian Ocean</text>

  <!-- Legend -->
  <rect x="-178" y="62" width="50" height="18" fill="#faf8f5" stroke="#ddd" stroke-width="0.3" rx="1"/>
  <line x1="-175" y1="66" x2="-165" y2="66" stroke="#c04040" stroke-width="1.0" stroke-dasharray="2,1"/>
  <text x="-163" y="67" font-size="2.2" fill="#444">Divergent (spreading)</text>
  <line x1="-175" y1="71" x2="-165" y2="71" stroke="#4060c0" stroke-width="0.9"/>
  <text x="-163" y="72" font-size="2.2" fill="#444">Convergent (subduction)</text>
  <line x1="-175" y1="76" x2="-165" y2="76" stroke="#c08030" stroke-width="0.9"/>
  <text x="-163" y="77" font-size="2.2" fill="#444">Collision (continental)</text>

  <!-- Scale bar -->
  <line x1="140" y1="62" x2="150" y2="62" stroke="#444" stroke-width="0.4"/>
  <line x1="140" y1="61" x2="140" y2="63" stroke="#444" stroke-width="0.3"/>
  <line x1="150" y1="61" x2="150" y2="63" stroke="#444" stroke-width="0.3"/>
  <text x="142" y="65" font-size="2.2" fill="#444">~1,100 km</text>
  <text x="142" y="67.5" font-size="1.8" fill="#777">(at equator)</text>

</svg>

---

## Plate Inventory

| Plate | Area (M km²) | Type | Speed (cm/yr) | Notable boundary |
|-------|-------------|------|---------------|-----------------|
| Pacific | 103.3 | Oceanic | 5-10 | Ring of Fire (subduction on all sides) |
| North American | 75.9 | Continental+oceanic | 2-3 | San Andreas transform, Cascadia subduction |
| Eurasian | 67.8 | Continental+oceanic | 1-2 | Alpine-Himalayan collision |
| African | 61.3 | Continental+oceanic | 2-3 | East African Rift (divergent) |
| Antarctic | 60.9 | Continental+oceanic | 1-2 | Surrounded by ridges |
| Indo-Australian | 58.9 | Continental+oceanic | 6-7 | Himalayas (India-Eurasia collision) |
| South American | 43.6 | Continental+oceanic | 3-4 | Andes subduction |
| Nazca | 15.6 | Oceanic | 7-8 | Subducts under S. America → Andes |
| Philippine Sea | 5.5 | Oceanic | 6-8 | Subduction on all sides |
| Arabian | 5.0 | Continental | 3-5 | Red Sea opening, Zagros collision |
| Caribbean | 3.3 | Oceanic | 1-2 | Arc volcanism |
| Cocos | 2.9 | Oceanic | 7-9 | Subducts under Central America |
| Scotia | 1.6 | Oceanic | 2-3 | Antarctic-South America bridge |
| Juan de Fuca | 0.3 | Oceanic | 4-5 | Cascadia subduction zone |

---

## Three Types of Plate Boundary

```
BOUNDARY TYPES — CROSS-SECTION VIEWS

  1. DIVERGENT (plates move apart — new crust forms)
  ─────────────────────────────────────────────────
     Mid-Atlantic Ridge, East African Rift, Iceland

              ↑ magma rises
     ←──plate │ plate──→          sea floor
     ═════════╪═════════          spreading
              │ mantle

     Result: new oceanic crust, shallow earthquakes
     Hazard: volcanic fissures, not usually catastrophic

  2. CONVERGENT (plates collide — crust destroyed or crumpled)
  ────────────────────────────────────────────────────────────
     a) OCEANIC-CONTINENTAL: Andes, Cascades, Japan

        ocean plate     continent
        ──────────╲     ──────────
                   ╲    volcanoes ▲▲▲
                    ╲   mountains ████
                     ╲  ──────────────
                      ╲ melting → magma rises
                       ╲ deep earthquakes

     b) CONTINENTAL-CONTINENTAL: Himalayas, Alps

        India plate →→→  Eurasian plate
        ═══════════════╗  ═══════════════
                  crush╠══╣crumple
                       ╠══╣ mountains grow
                       ╠══╣ no subduction (both too buoyant)
                       ╚══╝ shallow earthquakes, very large

     c) OCEANIC-OCEANIC: Mariana Trench, Tonga Trench

        older plate     younger plate
        ──────────╲     ──────────
                   ╲    volcanic arc (island chain)
                    ╲   ──────────────
                     ╲  deep trench + deep earthquakes

  3. TRANSFORM (plates slide past — crust conserved)
  ──────────────────────────────────────────────────
     San Andreas, Alpine Fault (NZ), Dead Sea Transform

     ════════════→
     ←════════════        lateral grinding
                          shallow earthquakes, no volcanism
                          very destructive (near surface)
```

---

## Stable Cratons — The Safe Ground

Cratons are the ancient cores of continents: 1-4 billion years old, thick lithosphere, no significant seismic activity. If the question is "where won't the ground shake?", the answer is a craton.

| Craton | Location | Age (Ga) | Area (M km²) | Notes |
|--------|----------|----------|-------------|-------|
| Canadian Shield | Central/E Canada | 2.5-4.0 | 8.0 | Largest exposed craton, rich in minerals |
| Baltic Shield | Scandinavia, Finland | 1.8-3.5 | 1.5 | Extremely stable, low seismicity |
| Siberian Craton | Central Siberia | 2.0-3.5 | 4.0 | Overlain by Siberian Traps (basalt) |
| West African Craton | Sahara, W. Africa | 2.0-3.0 | 4.5 | Mostly buried under desert |
| Congo Craton | Central Africa | 2.5-3.5 | 3.5 | Rainforest-covered |
| Kalahari Craton | Southern Africa | 2.5-3.6 | 2.0 | Gold, diamonds (Kaapvaal) |
| Indian Craton | Peninsular India | 2.5-3.5 | 3.0 | Deccan Traps overlay |
| Australian Craton | Western Australia | 2.5-3.7 | 5.0 | Pilbara: oldest known rocks |
| Sao Francisco | Eastern Brazil | 2.0-3.4 | 0.6 | Iron ore deposits |
| East Antarctic | Under ice sheet | 2.5-4.0 | ~10.0 | Largest, entirely ice-covered |

---

## Seismic Hazard Zones

```
GLOBAL SEISMIC RISK — BY ZONE

  VERY HIGH (magnitude 7+ expected, frequent activity):
     Pacific Ring of Fire — entire rim
     Alpine-Himalayan Belt — Turkey through Nepal
     Indonesian archipelago
     Japan, Philippines, Taiwan
     Western South America (Chile, Peru, Ecuador)
     Cascadia (Pacific NW — overdue M9+)
     Eastern Mediterranean

  HIGH (magnitude 6-7 expected):
     San Andreas corridor (California)
     New Madrid zone (central US — last M7+ in 1812)
     Iran (multiple active faults)
     Central Asia (Tien Shan, Pamir)
     East African Rift

  MODERATE (magnitude 5-6, infrequent):
     Southeast US, Northeast US (rare but possible)
     Northern Europe (post-glacial rebound)
     Central/West Africa
     Eastern Australia

  LOW (cratons, stable continental interiors):
     Canadian Shield, Baltic Shield
     Central Siberia, Western Australia
     Sahara, interior Brazil
```

---

## Tsunami Risk

Tsunamis are generated by undersea earthquakes (usually M7.5+) at subduction zones. Travel time across ocean basins: 6-22 hours. Wave speed in deep water: ~800 km/h. Coastal run-up: 10-40 meters in worst cases.

| Source Zone | Threatens | Last Major Event |
|-------------|-----------|-----------------|
| Cascadia | Pacific NW coast, Hawaii | 1700 (M9.0) — overdue |
| Chile-Peru trench | West S. America, Pacific basin | 2010 Chile (M8.8) |
| Japan Trench | Japanese coast, Pacific | 2011 Tohoku (M9.1) |
| Sumatra-Andaman | Indian Ocean rim | 2004 (M9.1, 230,000 dead) |
| Aleutian Trench | Alaska, Hawaii, Pacific | 1964 Alaska (M9.2) |
| Caribbean | Gulf, E. Caribbean islands | 1755 Lisbon (tsunami crossed Atlantic) |
| Mediterranean | S. Europe, N. Africa | 365 AD Crete (M8.0+) |

**Survival rule**: After strong ground shaking near a coast, move to high ground (30+ meters) immediately. Do not wait for a warning. The wave may arrive in minutes.

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Where is ground most stable? | Cratons: Canadian Shield, Baltic, W. Australia, Siberia |
| Where are the worst earthquake zones? | Ring of Fire, Alpine-Himalayan belt, Cascadia |
| Why do the Andes exist? | Nazca plate subducting under South America |
| Why do the Himalayas exist? | India colliding with Eurasia (still rising ~5mm/yr) |
| Where is Africa splitting? | East African Rift — Red Sea to Mozambique |
| Where is new ocean floor forming? | Mid-Atlantic Ridge, East Pacific Rise |
| What causes tsunamis? | Subduction zone earthquakes (M7.5+), undersea landslides |
| Most dangerous overlooked zone? | Cascadia (Pacific NW) — last M9 in 1700, ~300-500 yr cycle |

---

## Cross-References

- **Geology detail** → [geology/](../geology/00-OVERVIEW.md)
- **Volcanic features** → [atlas/14-VOLCANIC-GEOTHERMAL.md](14-VOLCANIC-GEOTHERMAL.md) *(planned)*
- **Mountain passes** → [atlas/17-MOUNTAIN-PASSES.md](17-MOUNTAIN-PASSES.md) *(planned)*
- **Mineral deposits** → [atlas/13-MINERAL-ORE-DEPOSITS.md](13-MINERAL-ORE-DEPOSITS.md) *(planned)*
- **Deep time context** → [paleontology/](../paleontology/00-OVERVIEW.md)
'''

with open('../01-TECTONIC-PLATES.md', 'w', encoding='utf-8') as f:
    f.write(MAP01.lstrip('\n'))

print(f"Wrote 01-TECTONIC-PLATES.md ({len(MAP01):,} chars)")
