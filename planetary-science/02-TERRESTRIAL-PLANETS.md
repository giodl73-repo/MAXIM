---
maxim_schema: maxim.frontmatter.v1
id: maxim:planetary-science:terrestrial-planets
kind: guide
module: planetary-science
section: planetary-science
title: Terrestrial Planets: Comparative Planetology
status: source-custody
source_custody: partial
current_path: planetary-science/02-TERRESTRIAL-PLANETS.md
canonical_path: planetary-science/02-TERRESTRIAL-PLANETS.md
backsource_ids: [proof-backfill:planetary-science:02-terrestrial-planets, git-history:planetary-science:02-terrestrial-planets]
concepts: [terrestrial, planets]
root_concepts: [terrestrial, planets]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Terrestrial Planets: Comparative Planetology

## The Big Picture

Four rocky planets, one star, similar building blocks — wildly different outcomes. Comparative planetology treats them as natural experiments.

```
COMPARATIVE PLANETOLOGY: SAME STARTING MATERIALS, DIVERGENT OUTCOMES
+------------------------------------------------------------------+
|                                                                  |
|  DISTANCE    0.38 AU    0.72 AU    1.00 AU    1.52 AU            |
|              Mercury    Venus      Earth      Mars               |
|                                                                  |
|  MASS        0.055 M⊕  0.815 M⊕  1.000 M⊕   0.107 M⊕             |
|  (outcome)   lost mantle?  twin?  reference  too small           |
|                                                                  |
|  ATMOSPHERE  none       92 bar    1 bar       0.006 bar          |
|  (outcome)   stripped   runaway   stable      lost (no dynamo)   |
|                                                                  |
|  SURFACE T   ~167°C avg  464°C    15°C mean   -63°C mean         |
|  (outcome)   solar-driven GH+500K  GH+33K     GH+5K              |
|                                                                  |
|  DYNAMO      none       none      active      extinct ~3.9 Ga    |
|  (outcome)   too small? slow rot? plate tecton.→ core convects   |
|                                                                  |
|  WATER       ice (poles) trace D/H oceans     ancient; now ice   |
|  (outcome)   cold trap   lost     retained    lost w/ dynamo     |
|                                                                  |
+------------------------------------------------------------------+

The central question comparative planetology asks: which parameters at t=0
(distance, mass, composition, spin) determine which of these divergent
outcomes? Mass and distance explain a lot; the residual variance drives
the field — Venus's lack of magnetic field, Mars's dynamo extinction,
Earth's plate tectonics are all poorly understood from first principles.
```

---

## Internal Structure

All terrestrial planets differentiated: heavy metals sank to form an iron core; silicate mantle surrounds it; thin crust on top.

```
INTERNAL STRUCTURE COMPARISON
==============================

  MERCURY              EARTH                MARS
  -------              -----                ----
  +--------+           +--------+           +--------+
  | Crust  |           | Crust  |           | Crust  |
  | ~100km |           | 5-70km |           | 30-60km|
  +--------+           +--------+           +--------+
  | Mantle |           | Mantle |           | Mantle |
  | thin   |           | 2890km |           | ~1800km|
  +--------+           +--------+           +--------+
  |  Core  |           |  Core  |           |  Core  |
  |  HUGE  |           | 3480km |           | ~1800km|
  +--------+           | liquid |           | liquid?|
                       | outer  |           +--------+
                       | solid  |
                       | inner  |
                       +--------+

Mercury: largest core fraction (~85% by radius) — why?
  Early giant impact stripped much of the original mantle
  Alternatively: solar wind ablated silicates (not favored now)
  BepiColombo mission (arrives 2025-26) will constrain this

Earth: only terrestrial planet with confirmed active outer liquid core
  → sustains the geodynamo → global magnetic field

Mars: InSight (2018-2022) seismology found:
  Core radius ~1830 km (larger than expected)
  Core is liquid Fe-S (no inner solid core confirmed)
  Crust is thick: 20-37 km (northern) to 55-70 km (southern highlands)
```

---

## Moment of Inertia Factor

The moment of inertia factor C/(MR²) constrains internal mass distribution without a spacecraft needing to land.

```
C/MR² VALUES AND INTERPRETATION
=================================

  Uniform sphere:  0.4  (all mass at same radius)
  Earth:           0.331 (concentrated core — heavier inside)
  Moon:            0.393 (small iron core)
  Mars:            0.365 (intermediate)
  Mercury:         0.346 (large dense core)

  The MORE the planet is concentrated toward center →
  LOWER the C/MR² value

  Determined from: spacecraft tracking (J₂ gravity term) +
  precession rate + tidal response
```

---

## Surface Processes

```
PROCESS          MERCURY   VENUS     EARTH    MARS
---------        -------   -----     -----    ----
Plate tectonics  None      None?     Active   None (stagnant lid)
Volcanism        Ancient   Possible  Active   Ancient (+ recent?)
Erosion (water)  None      None      Strong   Ancient only
Erosion (wind)   None      Strong    Moderate Strong (dust storms)
Impact craters   Many      Few       Few      Many (S hemisphere)
                 (old surf) (young)  (erased) (ancient crust)

KEY DIAGNOSTIC: Crater density → relative surface age
  High crater density = old surface (Mercury, Mars highlands)
  Low crater density  = young surface (Venus, Earth, Mars lowlands)
```

---

## Mercury: Extreme Density and Exosphere

```
MERCURY FACTS
=============

  Bulk density: 5.43 g/cm³ (second-highest; Earth = 5.51)
  Core fraction: ~85% by radius (largest of any planet)
  Surface: heavily cratered + smooth volcanic plains (Caloris Basin)
  Magnetic field: 1% of Earth's, dipole offset toward north pole

  EXOSPHERE (not a real atmosphere):
  Composition: Na, K, O, Ca, Mg, H, He (sputtered from surface)
  Pressure: ~10⁻¹⁰ bar (essentially vacuum)
  Source: solar wind sputtering + meteorite vaporization + sublimation

  ORBITAL ODDITIES:
  - 3:2 spin-orbit resonance (not 1:1)
  - Highly eccentric orbit (e = 0.206)
  - Perihelion precession: 43 arcsec/century confirmed by GR

  WHY NO ATMOSPHERE?
    Mass: too small to retain volatiles
    Temperature swings: 430°C day, -180°C night side
    Solar wind: no magnetopause prevents stripping
    Volatiles: Water ice confirmed in permanently shadowed craters at poles
```

---

## Venus: Sister Planet Gone Wrong

Covered separately in 03-VENUS.md. Key contrasts here:

```
EARTH vs VENUS CONTRAST TABLE
==============================

                    EARTH              VENUS
  ----------------  ------             -----
  Mass              1.000 M⊕           0.815 M⊕
  Radius            6,371 km           6,052 km
  Density           5.51 g/cm³         5.24 g/cm³
  Atm. pressure     1 bar              92 bar
  Atm. composition  N₂/O₂             CO₂/N₂
  Mean surface T    288 K (15°C)       737 K (464°C)
  Rotation period   24 hrs             243 days (retrograde)
  Magnetic field    Yes (active dynamo) None
  Plate tectonics   Yes                No (stagnant lid?)
  Surface age       Mixed (0-3.8 Ga)   Young (~500-800 Ma)
  Water             Abundant (oceans)  Trace (ppm in atm.)
```

The ~500-800 Ma surface age of Venus (from crater statistics) suggests a global resurfacing event — either a catastrophic overturn of a stagnant lid or continuous volcanism that erased craters uniformly.

---

## Mars: The Red Planet

Covered separately in 04-MARS.md. Key structure here:

```
MARS GEOLOGICAL EPOCHS (absolute ages estimated from cratering + radiometry)
===========================================

  Noachian    4.1 – 3.7 Ga   Heavy bombardment; valley networks; liquid water
  Hesperian   3.7 – 3.0 Ga   Widespread volcanism; catastrophic floods
  Amazonian   3.0 Ga – now   Cold, dry, icy; thin atmosphere; dust storms

  DICHOTOMY:
  Northern hemisphere  Low elevation; thin crust; smoother
  Southern hemisphere  High elevation; thick crust; heavily cratered

  Cause of dichotomy: debated
    Single giant impact ~4 Ga (Wilhelms & Squyres 1984 revisited)
    Different internal processes
    Tidal heating from large early Moon (not Mars's moons)
```

---

## Comparative Atmosphere Summary

```
ATMOSPHERE COMPARISON
======================

            Mercury   Venus     Earth     Mars
            -------   -----     -----     ----
  P (bar)   ~0        92        1.013     0.006
  T_eff(K)  442       231*      255       210
  T_surf(K) 100-700   737       288       160-300
  GH effect  ~0       +506 K   +33 K     +5 K
  Main gas   (none)   CO₂ 96%  N₂ 78%   CO₂ 95%
  Scale ht.  N/A      15 km    8.5 km    11 km

  *Venus T_eff is low despite high T_surf because its high albedo
   reflects most sunlight — the massive greenhouse does the heating

SCALE HEIGHT: H = kT/(mg)
  Larger H → atmosphere extends higher → more gradual with altitude
  Mars: larger H than Earth despite lower T because g is much lower
```

The greenhouse effect size (surface T – effective T) is the key number. Venus's +506 K greenhouse is a cautionary data point for Earth's climate trajectory.

---

## Surface Geology Tools

```
HOW WE READ TERRESTRIAL PLANET GEOLOGY
========================================

  CRATER COUNTING    → Relative surface age
                       (more craters = older)

  SPECTROSCOPY       → Mineral identification
  (visible-IR)         Olivine, pyroxene, carbonates, clays, sulfates
                       Can detect from orbit

  RADAR              → Penetrate clouds (Venus) or dust
                       Subsurface structure
                       Magellan mapped Venus at ~100m resolution

  TOPOGRAPHY         → MOLA (Mars), MESSENGER (Mercury)
                       Digital elevation models
                       Drainage patterns (ancient Mars)

  SEISMOMETRY        → InSight on Mars (2018-2022)
                       Revealed core radius, mantle structure

  SAMPLE RETURN      → Apollo (Moon), Hayabusa (Bennu, Ryugu)
                       ABSOLUTE ages via radiometry
                       No Mars samples yet (MSR planned ~2033)
```

---

## The Water Question

```
WATER HISTORY ON TERRESTRIAL PLANETS
======================================

  VENUS:    Likely had liquid water early (before runaway greenhouse)
            Current: trace H₂O vapor in atmosphere (~30 ppm)
            D/H ratio in Venus atm.: 150× Earth → massive water loss
            (heavier D left behind as H escaped; implies ~1 ocean lost)

  EARTH:    Persistent liquid water since ~4.4 Ga (Hadean zircons)
            Hydrological cycle active; silicate weathering feedback
            CO₂ drawdown into carbonates stabilizes temperature

  MARS:     Definitive evidence for ancient liquid water
            Valley networks (Noachian) → precipitation? groundwater?
            Paleolake deposits: Jezero crater (Perseverance site)
            Chloride salts, perchlorates, sulfates = evaporites
            Current: water ice at poles; ground ice at mid-latitudes
            Liquid water: unlikely at surface; possible deep brine

  MERCURY:  Water ice in permanently shadowed polar craters
            Confirmed by MESSENGER neutron spectroscopy
            Delivered by comets/asteroids; cold trap preserved it
```

---

## Cross-References

- `planetary-science/01-SOLAR-SYSTEM-FORMATION.md` — accretion and differentiation origins.
- `planetary-science/03-VENUS.md` — runaway greenhouse endmember.
- `planetary-science/04-MARS.md` — small terrestrial-planet evolution endmember.

## Decision Cheat Sheet

| If you need to diagnose... | Start With | Key Caveat |
|---|---|---|
| Mercury's high density | Large iron core and mantle-loss hypothesis | Giant impact is plausible, not uniquely proven. |
| Venus dynamo absence | Slow rotation and core-state uncertainty | Dynamo failure can have multiple causes. |
| Mars hemispheric dichotomy | Ancient northern lowlands and impact hypothesis | Tectonic/convective alternatives remain discussed. |
| Interior concentration | Moment-of-inertia factor | Inference depends on gravity/topography models. |
| Venus water loss | High atmospheric D/H ratio | D/H records cumulative escape, not exact initial ocean volume. |
| Venus crater scarcity | Young resurfaced surface plus atmospheric filtering | Resurfacing may be episodic, not necessarily global instant reset. |
| Stagnant-lid tectonics | Single-plate heat loss by volcanism | No subduction does not mean geologically dead. |
| Mars versus Earth interior | Higher Mars moment-of-inertia factor | Smaller core fraction is an interpretation, not direct view. |

---

## Common Confusion Points

**Venus hotter than Mercury despite being farther from the Sun**: Venus's Bond albedo (0.77) reflects 77% of incoming sunlight; effective temperature is only 231 K. The CO₂ greenhouse then heats the surface to 737 K. Mercury's surface can reach 430°C but only on the day side; Mercury has no greenhouse.

**Mars's "rivers" are ancient**: The valley networks are 3.7-4.1 Ga old. Mars today is cold and dry — liquid water is not stable at the surface under 0.006 bar. The features look like riverbeds because erosion rates on Mars are so low that 4-billion-year-old features are preserved.

**Plate tectonics is not the only way to lose heat**: Stagnant lid planets (Venus, Mars, Mercury) release internal heat primarily through volcanism and conduction through the thick lithosphere. They can be geologically active without subduction.

**The Martian moons are not captured asteroids (probably)**: Phobos and Deimos have been considered captured C-type asteroids, but their orbits (nearly circular, equatorial) are inconsistent with capture from heliocentric orbit. Current leading hypothesis: impact-generated debris disk, similar to the Moon-forming impact.
