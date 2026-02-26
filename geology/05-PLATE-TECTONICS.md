# Plate Tectonics — Seafloor Spreading, Wilson Cycle, Mantle Plumes

**Bridge — plate tectonics as the grand unified theory of geology:** Before the 1960s, geology was a collection of disconnected empirical observations: mountain ranges appeared for unclear reasons, earthquakes and volcanoes had unexplained distributions, identical fossils appeared on separate continents, and the ocean floor had mysterious linear magnetic striping. Plate tectonics unified these the way Maxwell's equations unified electricity, magnetism, and light — all disparate phenomena became instances of one mechanism. The parallel to software: it is the architectural refactoring that revealed every legacy module (earthquake seismology, stratigraphy, paleontology, volcanology) was implementing the same underlying abstraction. Once the framework clicked, each formerly ad-hoc observation became a predictable consequence. Continental drift without a mechanism (Wegener, 1912) was a correct observation without a theory — like identifying a performance regression without understanding the cause. Seafloor spreading (Hess, 1960) + magnetic striping (Vine & Matthews, 1963) provided the mechanism; GPS today measures it directly to millimeter precision.

## The Big Picture

Plate tectonics is geology's grand unified theory, explaining the distribution of mountains, earthquakes, volcanoes, ore deposits, and the assembly/dispersal of continents. The plates are rigid lithospheric slabs moving on the ductile asthenosphere, driven primarily by slab pull and ridge push.

```
+------------------------------------------------------------------+
|                  GLOBAL PLATE SYSTEM                              |
|                                                                   |
|  PLATE BOUNDARIES                                                 |
|  ┌─────────────────────┬─────────────────────┬─────────────┐     |
|  │ DIVERGENT           │ CONVERGENT          │ TRANSFORM   │     |
|  │ (rifting apart)     │ (colliding)         │ (sliding)   │     |
|  │                     │                     │             │     |
|  │ Mid-ocean ridges    │ Subduction zones    │ Strike-slip │     |
|  │ Continental rifts   │ Collision belts     │ fault zones │     |
|  │ Ophiolites          │ Island arcs         │             │     |
|  └─────────────────────┴─────────────────────┴─────────────┘     |
|                                                                   |
|  INTRAPLATE: Hotspot tracks, Large Igneous Provinces (LIPs)      |
|                                                                   |
|  DRIVING FORCES:                                                  |
|  Slab pull (~dominant) > Ridge push > Mantle drag                |
+------------------------------------------------------------------+
```

---

## Seafloor Spreading — The Key Evidence (1960s)

Harry Hess (1960): ocean ridges are spreading centers where new ocean crust is continuously generated. Vine & Matthews (1963): magnetic stripes flanking ridges confirmed this.

```
MAGNETIC REVERSAL RECORD:
(Earth's magnetic field reverses every ~200,000–1,000,000 years)

              RIDGE AXIS
                  |
    Normal  Rev   |   Rev  Normal
    ++++++  ---   |   ---  ++++++   ← Symmetric magnetic anomaly stripes
    ++++++  ---   |   ---  ++++++
    ++++++  ---   |   ---  ++++++
                  |
           <---   |   --->  Spreading direction

SEAFLOOR AGE: 0 at ridge → oldest (~180 Ma) at subduction zone margins
SEAFLOOR DESTRUCTION: equal to creation (ocean floor recycled in ~180 Ma)
```

**Critical observations that established plate tectonics:**
1. Magnetic stripes symmetric about mid-ocean ridges
2. Seafloor age increases away from ridges
3. Heat flow highest at ridges
4. Earthquakes shallow at ridges, deep at subduction zones (Wadati-Benioff zones)
5. Continental fit (Wegener) + matching fossils + geologic structures
6. GPS today directly measures plate motion (1–15 cm/yr)

---

## Subduction — Consuming Oceanic Crust

```
OCEAN                        CONTINENT (or ocean arc)
                     TRENCH
~~~~~~~~~~~~~~~~~~~~~~~vvvvvvv~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         OCEANIC CRUST  \
         (dense, ~7 km)  \    FOREARC     VOLCANIC ARC
         LITHOSPHERE      \   BASIN       (Mt. Rainier,
                           \              Mt. St. Helens)
                            \   Melting of mantle wedge
                             \  (flux melting by slab H₂O)
                              \         /\
                         Slab  \       /  \
                         (Wadati-Benioff zone:
                          earthquakes to 700 km depth)

PRODUCTS:
- Volcanic arcs (stratovolcanoes, andesite)
- Accretionary wedge (scraped-off sediment)
- Forearc/backarc basins (trapped sediment)
- Ore deposits (porphyry Cu-Mo in arc)
- Blueschist/eclogite at depth (high P)
```

**Subduction erosion** — in some margins, subducting plate removes material from overlying plate instead of accreting. Japan, Chile, Tonga are erosive margins.

**Flat slab subduction** — if subducting slab is young (warm, buoyant) or has high bathymetric ridges, it can subduct at very shallow angle, spreading magmatism far inland. Laramide orogeny (~70 Ma) in North America attributed to flat-slab subduction.

---

## Continental Collision — Building Mountain Ranges

When oceanic crust between two continents is completely consumed, the continents collide:

```
STAGE 1: Ocean closes (subduction)
STAGE 2: Ophiolite obduction (slivers of ocean floor emplaced on continent)
STAGE 3: Continental collision — neither plate subducts easily (low density)
STAGE 4: Crustal shortening — thickening, folding, thrusting, mountain building
STAGE 5: Isostatic uplift + erosion → deep metamorphic rocks exhumed

EXAMPLES:
Alpine-Himalayan belt: Africa-Eurasia, India-Eurasia collisions
Appalachians: Iapetus Ocean closure (Caledonian orogeny)
Urals: Laurussia-Siberia collision
```

**Isostasy and mountain roots** — Mountains float on the mantle like icebergs. High mountains have deep crustal roots (Moho at 50–70 km under Himalayas vs ~35 km average). Erosion removes mass → root rebounds upward (isostatic rebound). This is why old, eroded mountains (Appalachians) have shallow roots now.

---

## Transform Faults — Lateral Motion

```
Ridge 1          Ridge 2
  |                  |
  |   TRANSFORM      |
  |   FAULT ZONE     |
~~+------------------+~~   (earthquake zone BETWEEN ridges,
     Active seismic       not along ridge extensions)
     segment
```

**San Andreas Fault** — Pacific Plate sliding NW past North American Plate at ~5 cm/yr. Not a subduction zone (no trench). Produces large (M7–8) but not megathrust earthquakes. The Big Bend is a compressional restraining bend → Transverse Ranges.

**Oceanic transform faults** (fracture zones) — offset ridge segments. The fracture zone beyond the active transform is a fossil scar, seismically quiet. Transforms connect segments of offset ridges; they connect two constructive margins, not destructive.

---

## Wilson Cycle — Ocean Opening and Closing

J. Tuzo Wilson (1966) recognized a systematic lifecycle for ocean basins:

```
STAGE            DESCRIPTION                    EXAMPLE TODAY
--------------   ----------------------------   -------------------
EMBRYONIC        Continental rift begins        East African Rift
                 (crust extends, normal faults,
                  limited volcanism)

YOUNG            Narrow ocean forms             Red Sea, Gulf of Aden
                 (seafloor spreading starts;
                  thin ocean floor)

MATURE           Wide ocean with mid-ocean      Atlantic Ocean
                 ridge; full spreading

DECLINING        Subduction initiates on one    Pacific Ocean
                 margin; ocean shrinks           (Ring of Fire)

TERMINAL         Ocean nearly consumed;          Mediterranean
                 continental collision           (closing, remnant of
                 approaching                     Tethys Ocean)

SUTURE           Collision complete;             Himalayas, Alps,
                 ocean gone; mountains           Appalachians (old)
```

---

## Mantle Plumes and Hotspots

Some intraplate volcanism can't be explained by plate boundary processes. Mantle plumes = columns of anomalously hot mantle rising from deep (possibly CMB):

```
HOTSPOT TRACK (Hawaii-Emperor chain):
Hawaii today    <--- NW direction of plate motion
 |
 | 5 cm/yr plate motion
 v
Midway Atoll (28 Ma)
 |
 v
Emperor Seamounts (>50 Ma)
 |
 v
Detroit Seamount (~76 Ma)
(bend at ~47 Ma reflects plate motion change)
```

**Large Igneous Provinces (LIPs)** — rapid, massive flood basalt eruptions from plume heads:
- Siberian Traps (~252 Ma) — coincides with P-T mass extinction
- Deccan Traps (~66 Ma) — coincides with K-Pg event
- Columbia River Basalts (~16 Ma)
- Ontong Java Plateau — largest LIP, ~125 Ma, Pacific

**Plume debate** — Whether all hotspots involve deep plumes is contested. Iceland (on mid-Atlantic Ridge), Hawaii (far from any boundary), and Yellowstone (overriding hotspot) show different characteristics.

---

## Plate Velocities and Major Plates

| Plate | Type | Speed (cm/yr) | Notable Boundary |
|-------|------|---------------|-----------------|
| Pacific | Oceanic | 5–10 (fast) | Ring of Fire subduction |
| North American | Mixed | 2–3 (SW motion) | San Andreas, Mid-Atlantic Ridge |
| Eurasian | Mixed | 1–3 (east) | Himalayas, Mediterranean |
| African | Mixed | 2–3 (north) | Mid-Atlantic + E Africa Rift |
| Australian | Mixed | 5–7 (NNE, fast) | Colliding with SE Asia |
| Antarctic | Mixed | ~2 | Mid-Atlantic + Indian-Antarctic Ridge |
| Pacific (subducting) | Oceanic | 8–10 | Fastest major plate |
| Juan de Fuca | Oceanic | 3–4 | Cascadia subduction |

**Fastest:** Some segments of the East Pacific Rise spread at >15 cm/yr total (symmetric).

---

## Decision Cheat Sheet

| Observation | Tectonic Interpretation |
|-------------|------------------------|
| Parallel linear mountains + trench | Active subduction margin |
| Symmetric magnetic stripes | Active or fossil spreading center |
| Ophiolite sequence on continent | Obducted oceanic crust (ancient subduction) |
| Back-arc basin behind volcanic arc | Extensional tectonics behind subduction |
| Flood basalts + continental rifting | Plume head / LIP |
| Straight coast with no trench | Passive margin (rifted continental edge) |
| Blue-schist belt | Ancient subduction zone (high-P/low-T) |
| Paired metamorphic belts | Ancient subduction: high-P side + arc high-T side |

---

## Common Confusion Points

**Plate vs crust** — A plate = crust + uppermost mantle (lithosphere, ~100 km). The boundary between plates isn't just the Moho; it's the base of the mechanical lithosphere (rheological boundary).

**Transform fault vs fracture zone** — The active transform fault (between two ridge segments) has strike-slip earthquakes. The fracture zone continues beyond the ridges as an aseismic scar. Only the segment between the two offset ridges is active and seismogenic.

**Subduction direction** — The denser (older, colder) plate subducts. Oceanic crust subducts under continental OR oceanic crust. Old oceanic crust (cold, dense) subducts readily; young oceanic crust (warm, buoyant) resists. Continental crust rarely subducts deeply (too buoyant) — hence collisions produce mountains, not deep trenches.

**Plume vs rift volcanism** — Hot spot/plume produces alkalic basalts enriched in incompatible elements (OIB chemistry). Rift/ridge produces tholeiitic MORB (depleted mantle source). The chemistry is diagnostic.
