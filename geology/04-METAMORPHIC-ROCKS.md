# Metamorphic Rocks — P-T Paths, Facies, Foliation, Index Minerals

**Bridge — metamorphism as constrained optimization under changing boundary conditions:** A shale entering a subduction zone carries its original mineral assemblage (the starting data structure). As pressure and temperature increase along the P-T path, the system continuously seeks the lowest free-energy configuration given current constraints — recrystallizing into new mineral assemblages without melting, preserving bulk chemical composition throughout. This is refactoring under new performance requirements: same data, reorganized structure to satisfy the current operating constraints. The P-T path is the full constraint history of the transformation; retrograde overprinting (chlorite replacing garnet during exhumation) records constraint relaxation on the way out. Index minerals are runtime type assertions: finding kyanite in a rock is a proof that the system was once at >5 kbar (>15 km depth), regardless of what it looks like now. Eclogite (dense, garnet + omphacite) is the fully-optimized state for subduction-zone P-T conditions — bring it to the surface and it becomes metastable, a high-performance data structure running on the wrong hardware.

## The Big Picture

Metamorphism = solid-state recrystallization of existing rocks in response to changes in temperature, pressure, and/or fluid chemistry. The key word is *solid-state* — metamorphic rocks never fully melt. If they do, we're back in the igneous realm.

```
+---------------------------------------------------------------+
|                METAMORPHIC FRAMEWORK                           |
|                                                                |
|  PRESSURE (depth)                                             |
|  HIGH |                                                        |
|       |  Eclogite      Granulite                             |
|       |  (blueschist   facies (high                          |
|       |   before)      T/low P)                              |
|       |                                                        |
|       |  Amphibolite facies (peak regional metamorphism)     |
|       |                                                        |
|       |  Greenschist facies (chlorite, epidote green colors) |
|       |                                                        |
|  LOW  |  Zeolite / Sub-greenschist (diagenesis boundary)    |
|       +-------------------------------------------------->    |
|          LOW                    HIGH   TEMPERATURE           |
|                                                               |
|  CONTACT METAMORPHISM: aureole around igneous intrusion      |
|  REGIONAL METAMORPHISM: mountain-building, deep burial       |
+---------------------------------------------------------------+
```

---

## Pressure-Temperature Conditions

Temperature and pressure both increase with depth, but their ratio varies:

```
SETTING             T GRADIENT    P GRADIENT    FACIES SERIES
-----------------   -----------   -----------   ------------------
Subduction zone     Low T/depth   High P/depth  Blueschist → Eclogite
(cold, fast burial) (5–10°C/km)                 (high-P/low-T path)

Normal continent    ~25°C/km      Normal        Greenschist → Amphibolite
burial                                          → Granulite

Contact aureole     Very high T   Low P         Hornfels facies
(magma intrusion)   (hundreds     (shallow)     (non-foliated)
                     °C over km)

Collision orogen    Variable T    High P        Eclogite possible at
                                  (deep burial  depth; amphibolite
                                   of crust)    at peak T
```

**Geothermal gradient = T increase per km depth**
Normal continental: ~25°C/km (surface T ~15°C → 40 km depth ~1000°C)
Under arc: higher T due to magma flux
Subduction slab: colder (cold oceanic crust descends fast → ~10°C/km)

---

## Metamorphic Facies — Mineral Assemblage Stability Fields

A **facies** = characteristic mineral assemblage that is stable at a specific P-T range. Facies named for their indicator rock type or mineral:

```
FACIES           P RANGE     T RANGE     KEY MINERALS (basaltic protolith)
---------------  ----------  ----------  ---------------------------------
Zeolite          <2 kbar     <300°C      Zeolites (laumontite, wairakite)
Prehnite-        ~2–5 kbar   200–350°C   Prehnite, pumpellyite
 Pumpellyite
Blueschist       5–15 kbar   200–500°C   Glaucophane (blue amphibole),
                                          lawsonite, jadeite
Greenschist      2–8 kbar    300–500°C   Chlorite, epidote, actinolite
                                          (green minerals = name)
Amphibolite      3–10 kbar   450–700°C   Hornblende, plagioclase
                                          (peak of most regional)
Granulite        5–15 kbar   >700°C      Orthopyroxene, diopside, garnet
                                          (no hydrous minerals; dry)
Eclogite         >12 kbar    500–800°C   Omphacite (Na-pyroxene) + garnet
                                          (high-density; oceanic crust
                                           brought to mantle depths)
Hornfels         <3 kbar     >400°C      Fine-grained, non-foliated;
(contact)                                 random mineral orientations
```

---

## Index Minerals — Barrow's Zones

George Barrow (1893) mapped progressive metamorphism in the Scottish Highlands, defining zones by first appearance of index minerals in pelitic (shale-derived) rocks:

```
INCREASING TEMPERATURE/PRESSURE -->

Chlorite → Biotite → Garnet → Staurolite → Kyanite → Sillimanite

ZONE     MINERAL         TEMP RANGE   INDICATOR
------   -----------     ----------   ---------------------------
I        Chlorite        ~300°C       Greenschist; chlorite slate/phyllite
II       Biotite         ~400°C       Foliation; biotite schist
III      Garnet          ~450°C       Porphyroblastic garnet
IV       Staurolite      ~500°C       Cross-shaped crystals in schist
V        Kyanite         ~550°C       Blade-like blue crystals
VI       Sillimanite     ~600°C       Fibrous "fibrolite" or prismatic
         (+ melting →)   >700°C       Partial melts: migmatites
```

**Al₂SiO₅ polymorphs** — three minerals with identical composition, different structures, stable at different P-T:
- **Kyanite** — high P, moderate T (subduction/collision)
- **Andalusite** — low P, moderate T (contact metamorphism)
- **Sillimanite** — high T (both high and low P)

These are critical P-T indicators: if you find kyanite in a rock, you know it reached high pressures (>5 kbar = >15 km depth).

---

## Foliation — Planar Fabric in Metamorphic Rocks

Foliation develops when directional stress (not just confining pressure) recrystallizes minerals perpendicular to the maximum principal stress:

```
FOLIATION TYPE    HOW IT FORMS          GRADE    EXAMPLE ROCK
---------------   --------------------   -------  -----------------
Slaty cleavage    Phyllosilicates align  Low      Slate
                  perpendicular to σ₁            (splitting planes)

Phyllitic         Coarser; sheen from   Low-Med  Phyllite
 texture          sericite/chlorite

Schistosity       Large mica/amphibole  Medium   Schist
                  crystals define                ("schistose fabric")
                  foliation planes

Gneissic          Alternating light/    High     Gneiss
 banding          dark mineral bands             (segregation bands)
 (gneissosity)    (no one dominant
                   mineral)

Mylonite          Ductile shear zone    Any      Mylonite (fine-
 foliation        fabric; stretched               grained, ribbony)
                  minerals
```

**Porphyroblasts** — large metamorphic crystals (garnet, staurolite) that grew within a finer foliated matrix. Growth can pre-date, syn-date, or post-date deformation (determined by inclusion trails in the crystal).

---

## Contact vs Regional Metamorphism

```
+---------------------------+    +---------------------------+
|  CONTACT METAMORPHISM     |    |  REGIONAL METAMORPHISM    |
|                           |    |                           |
|  Cause: magma intrusion   |    |  Cause: mountain building |
|  Scale: m to km aureole   |    |  Scale: 100s of km belt   |
|  P: low (shallow)         |    |  P: high (deep burial)    |
|  T: very high (contact)   |    |  T: moderate to high      |
|  Result: HORNFELS          |    |  Result: SCHIST, GNEISS   |
|  (non-foliated; no        |    |  (foliated; directed       |
|   directed stress)        |    |   stress from tectonics)  |
|  Zoning: spotted →        |    |  Zoning: Barrow zones     |
|  hornfels near contact    |    |  mapped over hundreds km  |
+---------------------------+    +---------------------------+
```

---

## Common Metamorphic Rocks

| Original Rock | Low Grade | Medium Grade | High Grade |
|--------------|-----------|--------------|------------|
| Shale/Mudstone | Slate, Phyllite | Schist | Gneiss |
| Sandstone | Quartzite | Quartzite | Quartzite (metaquartzite) |
| Limestone | Marble | Marble | Marble (recrystallized) |
| Basalt/Gabbro | Greenstone (greenschist) | Amphibolite | Granulite, Eclogite |
| Granite | (less common metamorphism) | Orthogneiss | Orthogneiss |
| Peridotite | Serpentinite | — | — |

---

## P-T Paths — Reading Tectonic History

A single metamorphic rock records its entire P-T journey, not just peak conditions:

```
PRESSURE
  ^
  |         /\ Peak P-T
  |        /  \
  |       /    \  Retrograde
  |      /      \  (exhumation)
  |     / Prograde\
  |    /  burial   \_______
  |   /                    ---> surface
  +--/--------------------------------> TEMPERATURE
     Burial (subduction or          Cooling during
     continental collision)         tectonic uplift
```

**Clockwise P-T path** = typical for continental collision (Himalayas): burial increases P while T lags; then exhumation (P drops while T maintained briefly)

**Counterclockwise P-T path** = crustal thickening followed by deep melting (granulite terrain), or some rifting scenarios

Preserved retrograde minerals (e.g., chlorite replacing garnet) record the cooling/decompression history.

---

## Decision Cheat Sheet

| Sample | Identification |
|--------|----------------|
| Fine-grained, cleaves into thin flat sheets | Slate |
| Fine-grained, silky sheen, crinkled cleavage | Phyllite |
| Platy, medium-grained mica-rich, foliated | Schist |
| Coarse-grained, alternating light/dark bands | Gneiss |
| Very hard, white/grey, no foliation, quartzose | Quartzite |
| White/grey, calcitic, no foliation, fizzes HCl | Marble |
| Dark green, serpentine minerals, slippery feel | Serpentinite |
| Fine-grained, non-foliated, hornlike | Hornfels (contact metamorphic) |
| Dense, red garnet + green omphacite | Eclogite (high-P subduction) |
| Blue amphibole present | Blueschist (subduction high-P/low-T) |

---

## Common Confusion Points

**Slate vs shale** — Both are fine-grained and dark, but shale is sedimentary (clay minerals, bedding planes, possibly fossils). Slate is metamorphic (phyllosilicates aligned by stress, slaty cleavage often at angle to original bedding). Slate doesn't fizz with HCl (shale might if calcareous).

**Schist vs gneiss** — Both are medium/high-grade; gneiss is higher grade with segregated bands rather than one dominant mineral defining fabric. A rough rule: if mica sheets define the fabric → schist; if alternating light (felsic) and dark (mafic) bands define structure → gneiss.

**Metamorphic grade vs metamorphic facies** — "Grade" is a relative term (low to high). "Facies" is a specific P-T field defined by mineral assemblages. Both describe the same P-T space but from different angles.

**Eclogite density** — Eclogite (~3.5 g/cm³) is much denser than continental crust (~2.7–2.8). When subducted oceanic crust transforms to eclogite at depth, this is a key driver of slab pull — the high-density slab pulls the rest of the plate down. Eclogite brought to surface in outcrops records former deep (>50 km) subduction.
