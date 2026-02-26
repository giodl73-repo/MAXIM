# Ocean Currents — Geostrophic Flow, Gyres, Western Boundary Intensification, Ekman Transport, Upwelling

## The Big Picture

```
+===========================================================================+
|                  OCEAN CURRENT HIERARCHY                                   |
+===========================================================================+
|                                                                           |
|  WIND-DRIVEN                    THERMOHALINE                              |
|  (upper ~1000 m)                (full depth, slow)                        |
|  ───────────────                ─────────────────                         |
|  Ekman transport                Deep water formation                      |
|  Geostrophic balance            NADW/AABW spreading                       |
|  Gyres (5 major)                ~1000 yr timescale                        |
|  Western boundary currents                                                |
|  ~weeks to years                                                          |
|                                                                           |
|  MESOSCALE EDDIES               COASTAL UPWELLING                         |
|  (10–300 km, months)            (seasonal, high productivity)             |
|  ─────────────────              ──────────────────────────                |
|  Shed from WBC jets             Ekman offshore transport                  |
|  ~90% of ocean KE               Nutrient injection                        |
|  Rings, spirals                 Fisheries hotspots                        |
|                                                                           |
+===========================================================================+
```

---

## Geostrophic Balance — The Dominant Balance

Geostrophic balance is steady-state force equilibrium between the pressure gradient and Coriolis — exactly analogous to static force balance in engineering mechanics, except one of the forces is the Coriolis pseudo-force from the rotating reference frame. The Sverdrup relation (β v = curl τ / ρ) is a conservation law for potential vorticity — the same concept as Kelvin's circulation theorem in inviscid fluid dynamics: the wind imparts vorticity to the ocean, and vorticity must be conserved as fluid columns stretch and squash while moving in latitude. Western boundary intensification is a boundary layer phenomenon: the β-effect creates an asymmetry that concentrates the entire gyre return flow into a thin viscous boundary layer on the western wall, just as aerodynamic boundary layers concentrate drag at solid surfaces — the interior is nearly inviscid, the boundary layer dissipates.

In the interior of the ocean (away from boundaries, surface, bottom), the dominant momentum balance is:

```
GEOSTROPHIC BALANCE:
  Pressure gradient force  =  Coriolis force

  -∂P/∂x = -ρfv   (x-component)
  -∂P/∂y =  ρfu   (y-component)

  where f = 2Ω sin(φ) = Coriolis parameter (φ = latitude)
  f > 0 Northern Hemisphere, f < 0 Southern Hemisphere

In vector form:
  f k̂ × u_g = -(1/ρ)∇P

RESULT:
  Geostrophic flow is PARALLEL to pressure isobars (not perpendicular!)
  In N. Hemisphere: flow rotates so HIGH pressure is on the RIGHT
  (Same physics as atmospheric highs → clockwise circulation around ridges)

  Dynamic height: D = -(1/g)∫ρ'dz (deviation from reference state)
  Geostrophic current: perpendicular to D gradient

THERMAL WIND (vertical shear):
  ∂u_g/∂z = -(g/f) ∂(ρ/ρ₀)/∂y
  Horizontal density gradient → vertical velocity shear
  Gulf Stream: core at surface, weakens with depth
```

---

## Sverdrup Balance and the Wind-Driven Gyre Interior

```
WIND STRESS CURL DRIVES GYRE INTERIOR FLOW:

  Sverdrup relation: β v = (1/ρ) curl(τ)

  where:
    β = ∂f/∂y = 2Ω cos(φ)/R (variation of Coriolis with latitude)
    v = meridional (N-S) velocity
    curl(τ) = wind stress curl (positive = counterclockwise wind pattern)

  Subtropical gyres: anticyclonic wind stress (trade winds + westerlies)
    → positive curl in N. Hemisphere → equatorward Sverdrup transport in interior
    → must return poleward somewhere → western boundary currents!

  Subpolar gyres: cyclonic wind stress
    → negative curl in N. Hemisphere → poleward Sverdrup transport in interior

CIRCULATION SCHEMATIC:

  SUBTROPICAL GYRE (N. Hemisphere):

           WESTERLIES (→ eastward)
  ┌──────────────────────────────────────────┐
  │ 60°N                    Ekman convergence│
  │                                          │
  │  Slow equatorward Sverdrup return        │
  │     in broad interior (Sv balance)       │
  │                                          │
  │ 20°N  Gulf Stream/Kuroshio ←──────────── │
  └──────────────────────────────────────────┘
           TRADE WINDS (← westward)
```

---

## The Five Major Subtropical Gyres

```
OCEAN            GYRE        WESTERN BOUNDARY CURRENT   TYPICAL SPEED
─────────────────────────────────────────────────────────────────────
N. Atlantic      Subtropical  Gulf Stream               1–2 m/s
N. Pacific       Subtropical  Kuroshio Current          0.5–1.5 m/s
S. Atlantic      Subtropical  Brazil Current            0.5–1 m/s
S. Pacific       Subtropical  East Australian Current   0.3–0.8 m/s
Indian Ocean     Subtropical  Agulhas Current           0.5–2 m/s (fastest)

Subpolar gyres:
N. Atlantic      Subpolar     Labrador Current          0.2–0.5 m/s
N. Pacific       Subpolar     Oyashio Current           0.2–0.5 m/s
S. hemisphere    ACC          Antarctic Circumpolar (not a gyre) 0.1–0.3 m/s

SUBTROPICAL GYRE CENTER (Sargasso Sea, etc.):
  Ekman convergence → downwelling → warm, nutrient-depleted, clear blue water
  Often called "ocean deserts" despite beauty
  Flotsam accumulates → garbage patches (Great Pacific Garbage Patch in N. Pacific gyre center)
```

---

## Western Boundary Intensification — Why the Gulf Stream is Fast

```
The western boundary current is narrow and fast; the eastern boundary is broad and slow.
This is NOT intuitively obvious from symmetry. Mechanism:

STOMMEL (1948) THEORY:
  The β effect (f increasing northward) breaks symmetry.

  Interior flow (Sverdrup): equatorward, broad
  Return must be poleward somewhere.

  In a frictionless ocean, return can be anywhere.
  With bottom friction, β creates the asymmetry:
    East boundary: β reinforces, current stable
    West boundary: β demands narrow, strong jet to close vorticity budget

  Physically: a northward-moving parcel at the western boundary gains
  planetary vorticity as it moves poleward (β effect).
  To conserve potential vorticity, it stretches, speeds up.
  This creates the narrow, fast western boundary jet.

RESULT:
  Gulf Stream: width ~100 km, depth ~1000 m, speed 1–2 m/s, transport ~30 Sv
  Eastern return: width ~3000 km, depth ~500 m, speed ~0.01 m/s, transport ~30 Sv
  Same mass flux, vastly different velocities and widths (continuity satisfied)
```

---

## Gulf Stream and Kuroshio — The Dominant WBCs

```
GULF STREAM:
  Florida Straits: 30 Sv northward (Florida Current + Antilles Current)
  Cape Hatteras: separates from coast, becomes free jet at ~35°N
  Transport increases to 150 Sv by 40°N (including recirculation eddies)
  Extension: crosses Atlantic, bifurcates
    → Norwegian Current → Arctic
    → Canary Current → returns equatorward (completing subtropical gyre)

KUROSHIO:
  Japanese "black current" (kuro = black; dark blue from low nutrients/sediment)
  ~42 Sv transport, similar to Gulf Stream
  Bifurcates north of Japan into Tsugaru Current (Sea of Japan) and
  North Pacific Current (crossing Pacific)
  Extension: highly variable, eddy-rich

AGULHAS CURRENT:
  Strongest boundary current by volume flux per unit width
  Flows south around Africa; retroflects at ~40°S
  Agulhas Retroflection sheds large warm-core rings into S. Atlantic
  "Agulhas leakage" — ~1.5 Sv leaks into South Atlantic, affecting AMOC salt budget
```

---

## Ekman Transport and Layer

### Surface Ekman Layer

```
EKMAN SPIRAL:
  Wind stress at surface → stress transmitted downward by turbulent viscosity
  Coriolis deflects each layer to the right (N. Hemisphere)
  Result: velocity vector rotates clockwise with depth, spiraling in

                        WIND DIRECTION
                              ↑ τ
  Surface: current at 45° to right of wind (theory)
           (actual: typically 20–45° deflection; turbulence matters)
  Deeper: current weakens and rotates further right
  Ekman depth (D_E): where current ~4% of surface, rotated 180°

  D_E = π√(2A_z/f)

  where A_z = eddy viscosity (10⁻²–10⁰ m²/s), f = Coriolis
  Typical: D_E ~ 20–100 m

NET EKMAN TRANSPORT:
  Integral of Ekman layer velocity:

  M_x = τ_y / (ρf)    (eastward transport from northward wind stress)
  M_y = -τ_x / (ρf)   (northward transport from eastward wind stress)

  NET TRANSPORT IS 90° TO THE RIGHT OF WIND (N. Hemisphere)
  (not in wind direction — this is the key result)
```

### Ekman Pumping

```
CONVERGENCE/DIVERGENCE OF EKMAN TRANSPORT:

  ∂M_x/∂x + ∂M_y/∂y = w_E (Ekman pumping velocity)

  w_E = (1/ρ) curl(τ/f) ≈ (1/ρf) curl(τ)

  Anticyclonic wind stress curl (subtropical high) → convergence → downwelling
  Cyclonic wind stress curl (subpolar low) → divergence → upwelling

SUBTROPICAL GYRE:
  Trade winds (westward) + Westerlies (eastward) → convergent Ekman transport
  → Ekman downwelling at gyre center
  → Warm, deep thermocline (200+ m)
  → Low nutrients → clear, blue, unproductive water (ocean deserts)

SUBPOLAR GYRE:
  Westerlies (poleward edge) + Polar Easterlies → divergent Ekman transport
  → Ekman upwelling → shallow thermocline
  → Nutrient-rich surface → productive fisheries (North Sea, Bering Sea)
```

---

## Coastal Upwelling

```
EKMAN OFFSHORE TRANSPORT → UPWELLING:

  CALIFORNIA CURRENT (N. Hemisphere example):
    Prevailing northerly/northwesterly winds along Pacific coast
    Ekman transport: 90° to right → OFFSHORE (westward)
    Surface water displaced offshore → replaced by deeper water rising
    → UPWELLING

  Cold, nutrient-rich water from ~100–300 m depth:
    T drops from 18°C to 12°C at surface
    NO₃⁻ rises from ~0 to ~25 μM
    → Phytoplankton bloom → zooplankton → sardines/anchovies → tuna/marine mammals

EASTERN BOUNDARY UPWELLING SYSTEMS:
  California Current (E. Pacific, N. Hemi): ~200 Sv Ekman transport
  Humboldt/Peru Current (E. Pacific, S. Hemi): largest upwelling system
  Canary Current (E. Atlantic, N. Hemi)
  Benguela Current (E. Atlantic, S. Hemi)
  Somali Current (W. Indian Ocean, seasonal — monsoon-driven)

PRODUCTIVITY PARADOX:
  These eastern boundary systems are adjacent to the world's driest deserts
  (California coast, Atacama, Sahara, Namib) yet support the richest fisheries.
  Cold upwelled water appears as "cold tongue" in SST satellite imagery.

EL NIÑO DISRUPTION:
  Anomalous eastward warm water surge suppresses upwelling off Peru
  → thermocline deepens → nutrient supply cut off
  → fisheries collapse (Peru anchovy industry destroyed in strong El Niño years)
```

---

## Mesoscale Eddies

```
EDDY FORMATION:
  Western boundary currents (Gulf Stream, Kuroshio) are baroclinically unstable:
  Strong velocity shear + horizontal density gradient → instability
  → Meanders grow → cut off → eddies

  Gulf Stream rings:
    Warm-core ring: meander encloses a bubble of warm Sargasso Sea water
                    within cold slope water → anticyclone (N. Hemi)
    Cold-core ring: cold slope water enclosed within Sargasso → cyclone

  Diameter: 100–300 km
  Depth: 1000–3000 m
  Lifespan: months to years
  Speed: 0.1–0.3 m/s (propagate west and equatorward)

MESOSCALE EDDY STATISTICS:
  ~90% of total oceanic kinetic energy is in mesoscale eddies (not mean flow!)
  Rossby radius: length scale where Coriolis = buoyancy = ~30–100 km
  Eddies are to ocean what weather systems are to atmosphere

SUBMESOSCALE (<10 km):
  Intense fronts, filaments, spirals in surface ocean
  Strong vertical velocities (up to 100 m/day)
  Critical for nutrient injection into euphotic zone
  Increasingly resolved in modern ocean models (0.01°–0.1° resolution)
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is geostrophic balance? | Coriolis = pressure gradient; current flows parallel to isobars |
| Why is the Gulf Stream so narrow and fast? | Western boundary intensification (Stommel/β-effect); vorticity budget demands narrow return flow |
| Where does Ekman transport go? | 90° to RIGHT of wind (N. Hemisphere), regardless of wind direction |
| What is Ekman pumping? | Curl of Ekman transport drives vertical motion (convergence→downwelling, divergence→upwelling) |
| Why are subtropical gyres unproductive? | Ekman convergence → downwelling → nutrients buried below photic zone |
| Why are eastern boundary currents productive? | Upwelling brings cold, nutrient-rich deep water to surface |
| What drives gyre interior flow? | Sverdrup balance: β × v = wind stress curl |
| How big are ocean eddies? | 10–300 km (mesoscale); contain ~90% of ocean KE |
| What is the Agulhas retroflection? | Agulhas Current turns sharply back on itself at ~40°S; sheds warm rings into S. Atlantic |

---

## Common Confusion Points

**Geostrophic balance is NOT the same as atmospheric geostrophic wind**: The math is identical, but the ocean current goes parallel to isobars of dynamic height (not sea level directly). Also, the ocean has baroclinic shear (thermal wind), so geostrophic velocity varies with depth.

**Ekman transport is 90° to the wind, not in the direction of wind**: This surprises everyone at first. A northward wind in the Northern Hemisphere drives net Ekman transport to the EAST (90° to the right). Only the very surface (first mm) moves roughly in the wind direction; the integral of the entire Ekman layer is always 90° perpendicular.

**Trade winds blow westward, but Ekman transport drives convergence, not simple westward drift**: The subtropical gyre converges because the trade winds (westward south) and westerlies (eastward north) have their Ekman transports pointing TOWARD each other (both toward the gyre center).

**Western boundary current transport increases downstream**: The Gulf Stream carries 30 Sv at Florida Straits, but 150 Sv by the time it separates from the coast. The additional transport comes from recirculation eddies — not the Sverdrup circulation adding mass. The Sverdrup balance gives ~35 Sv; the rest is eddy recirculation.

**The Gulf Stream does not heat Europe by itself**: While AMOC transports heat, so do the mid-latitude westerly winds over warm SST, the land distribution, and the general circulation. "The Gulf Stream keeps Europe warm" is correct in direction but overstated in magnitude. Some studies suggest atmospheric circulation differences (land vs. ocean at the same latitude) account for most of the N. Atlantic–N. Pacific temperature asymmetry.

## Antarctic Circumpolar Current (ACC)

The ACC is the largest current on Earth by volume transport (~130–150 Sv) and the only current that circles the globe unobstructed by continents. It connects all three major ocean basins and is the primary distributor of NADW and AABW to the Indian and Pacific oceans.

```
ACC STRUCTURE:
  Driven by: strong westerly winds in the "Roaring Forties" (40–60°S)
  No continental barriers between Cape Horn and Antarctic Peninsula
  → unobstructed zonal flow

  Transport: ~130–150 Sv at Drake Passage (measured by DRAKE array)
    Compare: Gulf Stream ~30 Sv; AMOC ~17 Sv thermohaline component

  Frontal system (from north to south):
    Subtropical Front       SST ~12–15°C; northern edge
    Subantarctic Front      SST ~8–10°C; boundary of AAIW subduction
    Polar Front (Antarctic Convergence)  SST ~5°C; Antarctic Intermediate Water
    Southern ACC Front      SST ~2°C; deepest winter mixing
    Southern Boundary ACC   contact with Antarctic slope

  Each front: ~0.5–1 m/s core velocity, ~100–300 km wide
  Between fronts: broad, slower background flow

KEY ROLES:
  1. CONNECTS OCEAN BASINS:
     NADW (from N. Atlantic) → enters Southern Ocean → upwells here
     → mixed with Antarctic waters → redistributed to Indian + Pacific

  2. BUOYANCY BUDGET:
     Wind stress drives surface divergence (Ekman) south of Drake Passage
     → upwelling of deep water → exchange with atmosphere
     Southern Ocean takes up ~40% of anthropogenic CO₂ + ~50% of excess heat

  3. EDDY FLUX CRITICAL:
     Unlike mid-latitude gyres, ACC cannot balance wind stress with
     sea-level tilt (no boundaries) → mesoscale eddies carry the
     northward heat + momentum flux ("eddy saturation" regime)
     This is why ACC models require resolving eddies (<10 km grid)

DRAKE PASSAGE EFFECT:
  Opening of Drake Passage ~30 Ma (Antarctica–S. America separation)
  → ACC established → thermal isolation of Antarctica → glaciation
  Closing Drake would redirect warm water to Antarctica → deglaciation
```
