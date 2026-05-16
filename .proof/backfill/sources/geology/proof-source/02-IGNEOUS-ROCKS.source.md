---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "02-IGNEOUS-ROCKS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:geology:igneous-rocks
kind: guide
module: geology
section: geology
title: Igneous Rocks - Magma, Differentiation, Bowen's Series
status: source-custody
source_custody: partial
current_path: geology/02-IGNEOUS-ROCKS.md
canonical_path: geology/02-IGNEOUS-ROCKS.md
backsource_ids: [proof-backfill:geology:02-igneous-rocks, git-history:geology:02-igneous-rocks]
concepts: [igneous, rocks]
root_concepts: [igneous, rocks]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Igneous Rocks — Magma, Differentiation, Bowen's Series

**Bridge — phase diagrams and multi-component solidification:** Any thermodynamics course covers binary phase diagrams: a melt of two components solidifies along a liquidus curve, with one phase crystallizing first, enriching the remaining liquid in the other component. Bowen's reaction series is the multi-component version of this applied to silicate melts: as a basaltic magma cools, olivine crystallizes first (highest liquidus temperature), removing Mg and Fe from the melt and enriching the residual liquid in Si, Al, K, and Na. Each crystallization step shifts the melt composition along a differentiation path toward more felsic compositions. Fractional crystallization (physically removing early-formed crystals) is the analog of distillation — repeated fractional removal drives the system toward an end-member composition far from the starting point. Porphyritic textures record two-phase cooling: slow (deep, phenocrysts form) followed by fast (surface, fine groundmass quenches). The same logic as a thermally arrested phase transition with two distinct cooling regimes.

## The Big Picture

Igneous rocks record the cooling history of melts. The entire compositional range from basalt (mafic, ~50% SiO₂) to rhyolite (felsic, ~75% SiO₂) reflects magma differentiation — the process by which a single basaltic parent melt generates a spectrum of daughter magmas.

```
+---------------------------------------------------------------+
|                  IGNEOUS ROCK FRAMEWORK                       |
|                                                               |
|  COMPOSITION (SiO₂ content)                                   |
|  Mafic         Intermediate      Felsic                       |
|  ~50% SiO₂     ~57-63%           ~70-75% SiO₂                 |
|  (Mg/Fe-rich)  (mixed)           (Si/Al-rich)                 |
|                                                               |
|  EXTRUSIVE (volcanic, fast cooling, fine-grained):            |
|  Basalt    -- Andesite        -- Rhyolite                     |
|  Pillow lava   Stratovolcano     Rhyolite domes               |
|                                                               |
|  INTRUSIVE (plutonic, slow cooling, coarse-grained):          |
|  Gabbro    -- Diorite         -- Granite                      |
|  Oceanic crust  Batholiths       Continental crust            |
|                                                               |
|  TEXTURES: grain size = cooling rate                          |
|  Pegmatite (cm) > Phaneritic (mm) > Aphanitic (invisible)     |
|  > Glassy (quenched) = Obsidian/Pumice                        |
+---------------------------------------------------------------+
```

---

## Magma Composition — The Felsic-Mafic Spectrum

"Mafic" = Magnesium + Ferric (iron-rich). "Felsic" = Feldspar + Silica.

| Property | Mafic (Basaltic) | Intermediate | Felsic (Granitic) |
|----------|-----------------|--------------|-------------------|
| SiO₂ | ~45–52% | ~52–66% | ~66–75% |
| Temperature | 1100–1200°C | 900–1100°C | 650–900°C |
| Viscosity | Low (runny) | Medium | High (sticky) |
| Volatile content | Low | Medium | Higher |
| Eruption style | Effusive flows | Mixed | Explosive |
| Density | ~2.9 g/cm³ | ~2.7 | ~2.6 g/cm³ |
| Example intrusive | Gabbro | Diorite | Granite |
| Example extrusive | Basalt | Andesite | Rhyolite |

**Why does viscosity matter so much?** High-silica magma has polymerized [SiO₄] chains that resist flow. Dissolved gases (H₂O, CO₂) can't escape easily → explosive decompression = pyroclastic eruptions. Low-silica basalt is runny → gases bubble out gently → lava flows.

---

## Bowen's Reaction Series — Crystallization Order

N.L. Bowen (1922) experimentally determined the order minerals crystallize as basaltic magma cools:

```
TEMPERATURE  CRYSTALLIZATION ORDER        SERIES TYPE
-----------  ---------------------------  -------------------
HIGHEST      Olivine (Mg end)             DISCONTINUOUS
~1200°C      |                            (each mineral is a
             v                             different structure)
             Pyroxene (Ca,Mg)
             |
             v
             Amphibole (Ca,Mg,Fe)
             |
             v
~800°C       Biotite mica
             |
LOWEST       Potassium feldspar           }
~650°C       Muscovite mica               } CONTINUOUS
             |                            } (plagioclase
             v                            } reacts with melt
             Quartz                       } continuously as
                                          } Ca→Na solid sol.)
```

**The Continuous Series (plagioclase)** runs alongside the discontinuous series:
```
HIGH T:  Anorthite (Ca-rich plagioclase, CaAl₂Si₂O₈)
             v  (reacts with melt, Ca replaced by Na)
LOW T:   Albite (Na-rich plagioclase, NaAlSi₃O₈)
```

**Magmatic differentiation** = early-crystallizing minerals (olivine, Ca-plagioclase) separate from the melt by settling, filter pressing, wall crystallization, or chamber replenishment/mixing. The remaining liquid becomes progressively more silica/alkali-rich and can move toward intermediate or felsic compositions. Basalt can differentiate toward granitic melts, but continents are not "made from basalt" by this route alone: crustal melting, assimilation, subduction fluids, and repeated recycling all matter.

---

## Intrusive Bodies — Plutons and Their Geometry

```
PLUTON TYPE    SHAPE                   SIZE         EXAMPLE
-------------  ----------------------  -----------  -----------------
Batholith      Large, irregular mass   >100 km²     Sierra Nevada,
               at depth               (often       Coast Range
                                       1000s km²)
Stock          Smaller irregular mass  <100 km²     Many Cascade peaks
Laccolith      Mushroom-shaped,        km scale     Henry Mountains,
               concordant floor,                    Utah
               domed roof
Sill           Horizontal sheet,       m to km      Palisades Sill, NJ
               concordant with         thick
               country rock
Dike           Tabular, discordant     cm to tens   Everywhere; often
               (cuts across bedding)   of meters    fill fractures
               vertical or angled
Ring dike      Annular (circular       —            Above magma
               plan view)                           chamber collapse
```

---

## Volcanic Features and Eruption Styles

```
ERUPTION STYLE       MAGMA TYPE    VEI RANGE   PRODUCTS
-------------------  ------------  ----------  --------------------------
Hawaiian             Mafic         0-1         Lava fountains, lava flows,
                                               aa vs pahoehoe textures
Strombolian          Mafic-Interm  1-3         Rhythmic blasts, scoria
                                               cones, bombs
Vulcanian            Intermediate  2-5         Short explosive bursts,
                                               ash, blocks
Plinian              Felsic        4-8         Sustained column (10s km),
                                               ignimbrites, caldera
                                               collapse (Pinatubo 1991=VEI6)
Ultravulcanian       Any           varies      Phreatic (steam) explosions
(phreatomagmatic)                              when magma contacts water
```

**Lava types (basaltic):**
- **Pahoehoe** — smooth, ropy surface; low viscosity, slow flow
- **Aa** — rough, clinkery; same composition but faster flow → crust breaks up
- **Pillow basalt** — submarine; rapid quenching produces pillow shapes
- **Block lava** — more viscous, angular blocks (andesite/rhyolite)

**Pyroclastic materials:**
- **Ash** — <2 mm, can travel globally (Pinatubo aerosols cooled Earth 0.5°C for 1 yr)
- **Lapilli** — 2–64 mm
- **Bombs/blocks** — >64 mm (bombs are aerodynamically shaped in flight)
- **Ignimbrite** — welded tuff from pyroclastic flow

---

## Igneous Textures — Reading Cooling History

```
TEXTURE       GRAIN SIZE     FORMATION                  EXAMPLE
-----------   ------------   ------------------------   ------------------
Pegmatitic    >1 cm          Very slow cooling in       Pegmatite dikes
              (some >1 m)    volatile-rich fluid;       (gem crystals!)
                             giant crystals form

Phaneritic    1–10 mm        Slow cooling deep          Granite, Gabbro,
(coarse)      visible grains pluton → years to          Diorite
                             millions of years

Aphanitic     <0.1 mm        Fast cooling at/near       Basalt, Andesite,
(fine)        invisible to   surface → days to          Rhyolite
              naked eye      years

Porphyritic   Two sizes:     Two-stage cooling:         Common in
              phenocrysts    slow at depth (large       andesites
              in fine matrix crystals) then fast
                             (fine groundmass)

Glassy        No crystals    Quenched (minutes)         Obsidian (silicic),
                                                        Tachylite (mafic)

Vesicular     Bubbles        Gas escaping before        Scoria, Pumice
                             solidification             (pumice floats!)
```

**Porphyritic texture as a two-phase recorder** — The large crystals (phenocrysts) record the deep slow-cooling phase; the fine groundmass records the fast surface phase. Intrusive equivalent: a porphyritic granite means the magma spent time deep, then was intruded rapidly.

---

## Magma Generation — Where Does Melt Come From?

Three mechanisms:
1. **Decompression melting** — hot mantle upwells at divergent ridges; pressure drops; same temperature → melting point decreases → melt forms without adding heat (produces basalt)
2. **Flux melting (subduction)** — subducting slab releases H₂O into overlying mantle wedge; water lowers melting point → wet melting of mantle → basaltic/andesitic arc magmas
3. **Heat melting** — direct heat from mantle plume (hotspot) or crustal thickening → granitic melts from partial melting of lower crust

```
SETTING         MECHANISM          TYPICAL MAGMA     EXAMPLE
--------------  -----------------  ----------------  -----------------
Mid-ocean ridge Decompression      Tholeiitic basalt  MORB
Subduction arc  Flux melting       Basalt→Andesite   Cascade volcanoes
Hotspot         Decompression      OIB basalt         Hawaii, Iceland
                (plume) + partial  (enriched mantle)
Continent       Crustal partial    Rhyolitic/         Yellowstone,
                melting            granitic           S-type granites
```

---

## Decision Cheat Sheet

| Field / Lab Question | Use This Diagnostic | Likely Interpretation |
|---|---|---|
| Is the rock intrusive or extrusive? | Grain size | Coarse phaneritic = slow plutonic cooling; fine/glassy = volcanic or shallow cooling |
| Is the composition mafic or felsic? | Color index + mineral assemblage + SiO2 if available | Dark pyroxene/olivine/plagioclase -> basalt/gabbro; quartz/K-feldspar -> rhyolite/granite |
| Why are there big crystals in a fine matrix? | Two-stage cooling | Porphyritic texture: phenocrysts grew at depth, groundmass quenched later |
| Why is it full of holes? | Vesicles and density | Gas escape before solidification; pumice is felsic enough to float, scoria is mafic and denser |
| What tectonic setting generated it? | Magma chemistry + setting | MORB at ridges, OIB at hotspots, andesite/rhyolite common in arcs and continental systems |
| Is this granite, granodiorite, or tonalite? | Quartz + K-feldspar/plagioclase proportions | "Granite" in casual use often hides real plutonic classification |
| Why is the texture glassy? | Quench rate | Obsidian/tachylite cooled too fast for crystals; not a mineral |
| Why are crystals giant? | Pegmatitic volatile-rich residual melt | Water/fluxes allow large crystals and concentrate rare elements |
| Why are there columns? | Cooling contraction joints | Common in basaltic flows/sills; geometry records thermal contraction, not crystal shape |

---

## Cross-References

- [Minerals](01-MINERALS.md) supplies the crystal and silicate vocabulary used in igneous classification.
- [Plate Tectonics](05-PLATE-TECTONICS.md) explains the tectonic settings that generate magma.
- [Earthquakes and Volcanoes](06-EARTHQUAKES-VOLCANOES.md) follows igneous processes into volcanic hazards.

## Common Confusion Points

**Granite vs granodiorite vs tonalite** — These are compositional subdivisions. True granite has >20% quartz and K-feldspar > plagioclase. Most "granite" in batholiths is actually granodiorite or tonalite. Commercial "granite" countertops are often gabbro or anorthosite.

**Basalt is the same composition as gabbro** — Texture differs, not composition. Basalt = fast-cooled gabbro. Similarly, rhyolite = volcanic equivalent of granite. The intrusive/extrusive pairs: Gabbro/Basalt, Diorite/Andesite, Granite/Rhyolite.

**Crystal settling in differentiation** — Fractional crystallization works by physically removing early-crystallized minerals from the melt. If they don't sink (or if the magma chamber is well-stirred), the differentiation trend is less pronounced.

**"Obsidian is a mineral"** — No. Obsidian is a rock (volcanic glass) with no crystalline structure, therefore no minerals. It's amorphous SiO₂-rich glass. Not to be confused with quartz (crystalline SiO₂).

**Bowen's series is predictive of weathering resistance** — Minerals that crystallize late in Bowen's series (quartz, K-feldspar, muscovite) are most stable at Earth's surface because they formed at conditions closest to surface temperature/pressure. Olivine (forms first, highest T) weathers fastest.
