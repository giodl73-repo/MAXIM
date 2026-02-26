# Planetary Science — Landscape and Taxonomy

## The Big Picture

Planetary science bridges astronomy, geology, atmospheric physics, and geochemistry. The central question: how do planets form, evolve, and (sometimes) become habitable?

```
PLANETARY SCIENCE: CAUSAL FLOW
+------------------------------------------------------------------+
|                                                                  |
|  NEBULAR DISK (gas + dust)                                       |
|       |                                                          |
|       v  [condensation sequence: refractory → icy beyond frost  |
|           line; N-body dynamics; core accretion / disk instab.] |
|  PLANETESIMALS → PROTOPLANETS → PLANETS                         |
|       |                                                          |
|       v  [differentiation: dense metals sink to core;           |
|           silicates form mantle; volatiles → atmosphere]        |
|  INTERNAL STRUCTURE                                              |
|  (core / mantle / crust / atmosphere)                           |
|       |                                                          |
|       +———————————→ VOLCANISM (internal heat escapes)           |
|       +———————————→ TECTONICS (lithospheric stress releases)    |
|       +———————————→ MAGNETIC DYNAMO (convecting liquid core)    |
|       |                                                          |
|       v  [surface-atmosphere coupling; solar forcing;           |
|           impact bombardment; volatile delivery/loss]           |
|  SURFACE EVOLUTION + CLIMATE                                     |
|  (impact craters; erosion; atmospheric chemistry; habitability) |
|                                                                  |
+------------------------------------------------------------------+

OBSERVATIONAL TOOLS          THEORETICAL FRAMEWORKS
Telescopes (ground/space)    N-body dynamics (orbital evolution)
Spacecraft flyby/orbit       Planetary interior models (EOS, seismology)
Landers / rovers             Radiative transfer (atmospheric T profile)
Sample return                Hydrodynamic escape (atmosphere loss)
Radar / sonar sounding       Condensation sequences (composition gradients)
Seismometry                  Geochemical box models (element cycling)
Spectroscopy (remote sensing)Giant impact simulations (SPH/AMR codes)
```

---

## The Solar System at a Glance

```
DISTANCE FROM SUN (AU, approximate)

 0.4    0.7    1.0    1.5     |2-3.5|   5.2    9.5    19     30     30-50+
  |      |      |      |      | Belt|    |      |      |       |        |
Mercury Venus Earth  Mars           Jupiter Saturn Uranus Neptune   Kuiper Belt

<----------- ROCKY ZONE ----------->  <---------- GAS / ICE GIANTS -------->

                           FROST LINE ~2.7 AU
            (water ice stable beyond this; ice-enhanced solid surface density)
```

The frost line is the architectural key. Inside: only refractory silicates and metals condensed — small, rocky planets. Outside: ices added mass rapidly, enabling runaway gas accretion — hence giant planets.

---

## Planet Type Taxonomy

```
BODY TYPE        EXAMPLES           DEFINING PROPERTIES
---------        --------           -------------------
Terrestrial      Mercury-Mars       Rock/metal bulk; <2 R_Earth; solid surface
Gas giant        Jupiter, Saturn    H/He dominated; >100 M_Earth; no solid surface
Ice giant        Uranus, Neptune    H2O/CH4/NH3 "ices" in bulk; 14-17 M_Earth
Dwarf planet     Pluto, Eris, Ceres Hydrostatic equilibrium; NOT orbit-clearing
Asteroid         Vesta, Bennu       Rock/metal; irregular; <~1000 km
Comet            Halley, 67P        Ice-rich; outgassing when near Sun
KBO/TNO          Pluto, Arrokoth    Trans-Neptunian; primitive composition
```

IAU 2006: A planet must (1) orbit the Sun, (2) be in hydrostatic equilibrium, (3) have cleared its orbital neighborhood. Pluto fails #3.

---

## Planetary Science Subdisciplines

```
+-------------------------------------------------------------------+
| SUBDISCIPLINE            | FOCUS                    | METHODS     |
|--------------------------|--------------------------|-------------|
| Comparative planetology  | Cross-planet systematics | Spacecraft  |
| Geomorphology            | Surface landforms        | Imaging/DEM |
| Planetary petrology      | Rock/mineral composition | Spectroscopy|
| Planetary interiors      | Core/mantle structure    | Seismology  |
| Atmospheric science      | Climate/dynamics         | GCMs, probes|
| Planetary magnetism      | Fields and dynamo theory | Magnetometry|
| Astrobiology             | Habitability conditions  | Multiple    |
| Cosmochemistry           | Isotopes, element distrib| Mass spec   |
| Exoplanetary science     | Planets beyond the Sun   | Transit/RV  |
+-------------------------------------------------------------------+
```

---

## Key Physical Scales

```
QUANTITY            EARTH (BENCHMARK)     COMPARISON
---------           -----------------     ----------
Radius              6,371 km              Jupiter: 71,492 km (11.2×)
Mass                5.97 × 10²⁴ kg        Jupiter: 318×; Mars: 0.107×
Surface gravity     9.81 m/s²             Moon: 1.62; Jupiter: 24.8; Mars: 3.72
Escape velocity     11.2 km/s             Mars: 5.0; Jupiter: 59.5; Moon: 2.4
Mean surface temp   288 K (15°C)          Venus: 737 K; Mars: 210 K
Magnetic dipole     8 × 10²² A·m²         Jupiter: 1.6 × 10²⁷; Mars: none (global)
Orbital period      365.25 days           Mercury: 88 d; Neptune: 165 yr
```

---

## Module Map

```
00-OVERVIEW  (this file) — taxonomy, scales, subdisciplines
    |
    +-- 01-SOLAR-SYSTEM-FORMATION   Nebular disk → Nice model → Grand Tack
    |                               Late Heavy Bombardment, volatile delivery
    |
    +-- 02-TERRESTRIAL-PLANETS      Mercury, Venus, Earth, Mars comparison
    |                               Internal structure, surfaces, atmospheres
    |
    +-- 03-VENUS                    Runaway greenhouse deep dive
    |                               Surface geology, DAVINCI/VERITAS missions
    |
    +-- 04-MARS                     Geology epochs, water history, current climate
    |                               Habitability assessment, exploration status
    |
    +-- 05-GAS-GIANT-ICE-GIANT      Jupiter/Saturn/Uranus/Neptune interiors
    |                               Atmospheres, ring systems, major moons
    |
    +-- 06-SMALL-BODIES             Asteroid populations and compositions
    |                               Comet nuclei, KBOs, delivery of volatiles
    |
    +-- 07-EXOPLANETS               Transit, RV, direct imaging, astrometry
    |                               Demographics, radius gap, occurrence rates
    |
    +-- 08-HABITABILITY             Habitable zone definition and limits
    |                               Water, energy, chemistry requirements
    |
    +-- 09-PLANETARY-INTERIORS      Seismology, differentiation, dynamo theory
                                    P/S waves, moment of inertia constraints
```

---

## The Central Questions

```
+---------------------------------------------------+
| FORMATION   | How did planets acquire mass and    |
|             | composition from a disk of gas/dust?|
+---------------------------------------------------+
| EVOLUTION   | How have surfaces, interiors, and   |
|             | atmospheres changed over 4.6 Gyr?   |
+---------------------------------------------------+
| COMPARISON  | Why are Earth, Venus, Mars so        |
|             | different from similar starting       |
|             | materials and distances?             |
+---------------------------------------------------+
| HABITABILITY| What physical/chemical conditions    |
|             | enable life, and how common are      |
|             | they in exoplanet populations?       |
+---------------------------------------------------+
```

---

## Decision Cheat Sheet

| Question | Key Answer |
|---|---|
| Why are giant planets beyond the frost line? | Only there did solid cores reach ~10 M_Earth before the gas disk dispersed, triggering runaway gas accretion |
| Why does Earth have plate tectonics but Venus doesn't? | Leading hypotheses: Venus lacks water (lubricates subduction) and may have undergone a global resurfacing ~500–800 Mya that reset the lithosphere |
| Why did Mars lose its atmosphere? | Dynamo cessation ~4 Ga → no magnetic shield → solar wind stripping; small mass → low escape velocity; CO₂ sequestration in carbonates |
| What is the frost line? | ~2.7 AU from the Sun, the condensation boundary for water ice; compositions of solar system bodies differ markedly across it |
| What is the Nice model? | Late instability of giant planets (originally in compact configuration) that scattered Kuiper Belt Objects inward → Late Heavy Bombardment ~3.9 Ga |
| Best age proxy for surfaces? | Impact crater density (relative); radiometric dating of returned samples (absolute) |
| What is the Grand Tack? | Jupiter migrated inward to ~1.5 AU then reversed — depleting the asteroid belt and setting Mars's small size |

---

## Common Confusion Points

**Planet vs dwarf planet vs moon**: IAU definition requires orbit-clearing. Moons orbit planets; dwarf planets orbit the Sun without clearing. The distinction is gravitational dominance in the orbital zone, not size alone.

**Albedo types**: Geometric albedo (brightness vs Lambertian disk) is used for photometry. Bond albedo (total reflected / total incident) governs energy balance. Venus has Bond albedo ≈ 0.77 yet is hotter than Mercury because of the greenhouse effect.

**Ice giants vs gas giants**: "Ice" refers to composition (H₂O, CH₄, NH₃ in the bulk), not temperature state. Uranus and Neptune's interiors are hot dense fluids, not cold ice.

**Tidal locking**: Not just the Moon — Mercury is in a 3:2 spin-orbit resonance (not locked 1:1) due to its orbital eccentricity. True 1:1 locking requires near-circular orbit.

**Habitable zone edge cases**: The HZ is computed for a rocky planet with a CO₂-H₂O greenhouse atmosphere. It doesn't apply to subsurface oceans (Europa, Enceladus), which are inside the HZ yet potentially habitable through tidal heating.
