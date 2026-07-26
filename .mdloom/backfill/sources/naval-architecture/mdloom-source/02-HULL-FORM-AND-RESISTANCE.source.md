---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "02-HULL-FORM-AND-RESISTANCE.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:naval-architecture:hull-form-and-resistance
kind: guide
module: naval-architecture
section: naval-architecture
title: Hull Form and Resistance
status: source-custody
source_custody: partial
current_path: naval-architecture/02-HULL-FORM-AND-RESISTANCE.md
canonical_path: naval-architecture/02-HULL-FORM-AND-RESISTANCE.md
backsource_ids: [mdloom-backfill:naval-architecture:02-hull-form-and-resistance, git-history:naval-architecture:02-hull-form-and-resistance]
concepts: [hull form, block coefficient, resistance, froude number, wave-making, model testing]
root_concepts: [hull form, ship resistance]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Hull Form and Resistance

## The Big Picture

The water resists every metre a ship moves. That resistance — and the engine power
needed to overcome it — is the single biggest driver of fuel cost, emissions, and the
choice of hull shape. The crucial discovery, due to William Froude in the 1860s-70s,
is that ship resistance is not one thing but a *sum of separable components* that obey
*different scaling laws*. Splitting them is what lets us test a 5-metre model in a tank
and confidently predict the drag of a 300-metre ship.

```
SHIP RESISTANCE — THE DECOMPOSITION
===============================================================================

   TOTAL RESISTANCE  R_total
        |
        +----------------------------+----------------------------+
        |                            |                            |
        v                            v                            v
  FRICTIONAL  R_f              RESIDUARY  R_r               AIR / APPENDAGE
  (skin friction)             (everything left)            (above water + rudder)
        |                            |                       usually small
  scales with REYNOLDS         +-----+-----+
  (viscosity)                  |           |
  ~70-90% at slow speed        v           v
                          WAVE-MAKING   FORM (viscous
                            R_w          pressure) R_form
                            |               |
                       scales with     scales (mostly)
                       FROUDE (gravity) with Reynolds
                       grows steeply        small-ish
                       near hull speed

   THE TRICK: R_f scales by Reynolds, R_w by Froude. You can't match both
   at model scale -> split them (Froude's method, detailed below).
```

The whole guide hangs off this one diagram. Frictional resistance scales by Reynolds
number; wave-making by Froude number; they cannot be matched simultaneously in a model,
so Froude *separated* them. (For the general physics of skin friction and wave drag, see
`fluid-dynamics/04-BOUNDARY-LAYERS.md` and `fluid-dynamics/08-HYDRODYNAMICS.md`; this
guide specializes that physics to the hull-and-free-surface problem.)

---

## Layer 1: Describing the Hull Shape

Before resistance, you need a vocabulary for hull geometry. A hull is described by a
handful of dimensionless **form coefficients**, each comparing the actual hull to a
simple enclosing box or prism. They are the compressed DNA of a hull form.

```
THE BLOCK COEFFICIENT Cb (fullness)
===============================================================================

   Cb = (hull underwater volume) / (L x B x T)
      = how much of the enclosing box the hull actually fills

   Cb -> 1.0 : BOX-LIKE              Cb -> 0.4 : FINE / SLENDER
   .-------------------.             .-------------------.
   |###################|  full       |        ###        |  fine
   |###################|  bulk       |     #########      |  fast
   |###################|  carrier    |  ###############   |  warship
   '-------------------'             '-------------------'
   slow, lots of cargo               fast, little cargo

   A supertanker:  Cb ~ 0.80-0.85   (a brick — maximize volume)
   A bulk carrier: Cb ~ 0.80
   A container ship: Cb ~ 0.60-0.70
   A frigate:      Cb ~ 0.45-0.50   (a knife — minimize wave drag)
```

The full family of coefficients, each a ratio of the real hull to an idealized solid:

| Coefficient | Symbol | Definition | What it captures |
|-------------|--------|------------|------------------|
| Block | Cb | V ÷ (L·B·T) | Overall fullness of the underwater body |
| Prismatic | Cp | V ÷ (Am·L) | Fore-aft distribution of volume |
| Midship | Cm | Am ÷ (B·T) | Fullness of the midship cross-section |
| Waterplane | Cw | Aw ÷ (L·B) | Fullness of the waterline slice |
| Length/beam | L/B | — | Slenderness (drag vs. manoeuvrability trade) |
| Beam/draft | B/T | — | Stability vs. resistance trade |

These are linked: **Cb = Cp · Cm** (block fullness = how volume is distributed along the
length × how full the midship section is). Cp is the resistance-relevant one — it tells
you whether volume is concentrated amidships (low Cp, good for waves) or pushed toward
the ends (high Cp, full ships). A reader comfortable with moments will recognize these
as normalized integrals of the hull offsets; the lines plan is just the level-set
description of the hull surface, and the coefficients are its low-order summary.

> Old world -> new world bridge. The coefficients are a lossy *feature vector* for the
> hull — a handful of scalars that summarize a complex 3-D surface well enough to predict
> behavior and to look up empirical resistance data. The lines plan is the full model;
> the coefficients are the embedding you actually compute and compare against.

---

## Layer 2: Frictional Resistance — Skin on the Hull

The hull drags an entire boundary layer of water with it. At normal merchant speeds this
viscous skin friction is the *largest* component — often 70-90% of total resistance for
a slow, full ship. It scales with Reynolds number, and naval architects estimate it from
the equivalent flat plate of the same wetted area.

```
   R_f  =  C_f x (1/2) x rho x S x V^2

   C_f = frictional coefficient (a function of Reynolds number only)
   S   = wetted surface area of the hull
   V   = ship speed
   rho = water density

   The standard correlation line (ITTC 1957):
        C_f = 0.075 / (log10(Re) - 2)^2          with  Re = V L / nu
```

The ITTC-1957 line is the agreed flat-plate friction law the whole industry tows models
against. Two consequences:

- **Wetted surface S is the enemy of friction.** Anti-fouling coatings, hull polishing,
  and air-lubrication systems all attack R_f by reducing effective S or wall shear.
- **Re for a real ship is enormous (~10^9).** The boundary layer is fully turbulent over
  almost the entire hull — there is no laminar reprieve at ship scale (contrast with the
  partly-laminar wing of `fluid-dynamics/07-AERODYNAMICS.md`).

---

## Layer 3: Wave-Making Resistance — The Hull's Own Wake

A moving ship continuously builds a system of waves — the **Kelvin wake** — and radiating
those waves costs energy that shows up as drag. This is wave-making resistance R_w. It is
small at low speed and rises *steeply* as the ship approaches its "hull speed." It scales
with **Froude number**, not Reynolds.

```
THE KELVIN WAKE AND HULL SPEED
===============================================================================

   A displacement hull makes a bow wave and a stern wave. As speed rises,
   the wavelength of the ship's own wave grows (lambda = 2 pi V^2 / g).
   When that wavelength ~ the ship length, the ship sits in a trough of its
   own making and "climbs its own bow wave" -- R_w shoots up.

        bow wave              stern wave
          /\                     /\
   ~~~~~~/  \~~~~~~~~~~~~~~~~~~~~/  \~~~~~~ free surface
       _/    \__________________/    \_
      / SHIP                          \
     /________________________________\
     |<---------- L_ship ------------->|

   "Hull speed" ~ when wave length = ship length, near Fn ~ 0.4:
        V_hull (knots) ~ 1.34 x sqrt(L_waterline in feet)
   Pushing a displacement hull past this needs sharply more power
   (or you must plane / go semi-displacement -- different regime).
```

The governing dimensionless group is the **Froude number**:

```
        Fn  =  V / sqrt(g x L)

   Fn < 0.2   : friction-dominated, wave drag tiny (tankers, bulkers cruise here)
   Fn ~ 0.25-0.30 : container ships, where wave drag starts to bite
   Fn ~ 0.4   : "hull speed" hump; brutal power penalty for displacement hulls
   Fn > 1.0   : planing regime (the boat rides on top of the water, not through it)
```

Two physical levers reduce R_w without changing speed:

- **Slenderness.** A finer hull (lower Cp, higher L/B) makes smaller waves. This is why
  fast ships are long and thin and slow bulk carriers are short and fat.
- **The bulbous bow.** A bulb at the waterline below the stem launches its *own* wave
  system 180° out of phase with the hull's bow wave; the two partially cancel by
  destructive interference, cutting wave drag at the design speed by several percent.

```
THE BULBOUS BOW (wave interference, applied)
===============================================================================

   hull bow wave:    /\          /\          /\
                    /  \        /  \        /  \
   bulb wave:        \  /  +     \  /  +     \  /     (180 deg out of phase)
                      \/          \/          \/
   ------------------------------------------------------------------
   sum (partial cancellation):  ~~~~~~~~ smaller residual wave ~~~~~~~

   Tuned for ONE design speed. Off-design (slow steaming) a bulb can
   make things WORSE -- which is why slow-steamed ships sometimes get
   re-bulbed. It is a narrowband interference filter, not free lunch.
```

The bulbous bow is destructive interference engineered into steel — a concept any
signal-processing or wave-physics reader recognizes instantly. It is tuned to one
frequency (one speed), so off-design it can backfire, exactly like a narrowband filter
driven outside its passband.

---

## Layer 4: Froude's Method — Why Model Testing Works

Here is the methodological heart. We want the full-scale ship's resistance but can only
afford to tow a small model. The problem: R_f scales by Reynolds (need to match V·L/ν)
while R_w scales by Froude (need to match V/√(gL)). **You cannot satisfy both at once**
in a smaller model — they demand contradictory model speeds.

```
THE INCOMPATIBILITY (and Froude's escape from it)
===============================================================================

   To match FROUDE:    V_model = V_ship / sqrt(scale)   (slow the model down)
   To match REYNOLDS:  V_model = V_ship x scale          (speed it WAY up)
                       -- these disagree by scale^1.5. Impossible together.

   FROUDE'S HYPOTHESIS: total resistance splits into
        R_total = R_friction(Reynolds) + R_residuary(Froude)
   and the two are INDEPENDENT. So:

   +------------------------------------------------------------------+
   | 1. Tow the model at the FROUDE-matched speed.                    |
   |    -> R_residuary (mostly wave-making) scales correctly by       |
   |       Froude: same residuary COEFFICIENT model and full scale.   |
   |                                                                  |
   | 2. SUBTRACT a computed friction (flat plate, ITTC line) at       |
   |    MODEL Reynolds to isolate R_residuary of the model.           |
   |                                                                  |
   | 3. SCALE residuary up by displacement ratio; ADD BACK a computed |
   |    friction at FULL-SCALE Reynolds.                              |
   |                                                                  |
   | 4. R_ship = R_friction(full) + R_residuary(scaled).              |
   +------------------------------------------------------------------+
```

Stated as the procedure used in every towing tank since:

```
   Froude scaling of speed:   V_ship = V_model x sqrt(L_ship / L_model)

   Step-by-step:
     measure  R_total,model   in the tank
     compute  R_f,model       from ITTC line at model Reynolds
     R_residuary,model = R_total,model - R_f,model
     C_r = R_residuary,model / (0.5 rho S_m V_m^2)   <- same at both scales
     R_residuary,ship = C_r x 0.5 x rho x S_ship x V_ship^2
     compute R_f,ship from ITTC line at FULL-scale Reynolds
     R_total,ship = R_f,ship + R_residuary,ship + correlation allowance
```

> Old world -> new world bridge. Froude's method is *superposition on a decomposed
> system*: split the response into a part that obeys one scaling law and a part that
> obeys another, transform each independently, then recombine. It is exactly the move
> you make when you separate a signal into components that transform differently — solve
> each in its own domain, sum back. The "correlation allowance" added at the end is the
> empirical fudge term covering roughness and model-ship effects the clean theory drops.

The modern complement is **CFD** (`fluid-dynamics/09-CFD.md`): solve the free-surface
Navier-Stokes problem numerically at full scale and skip the Reynolds mismatch entirely.
In practice CFD and the towing tank are used together — CFD for shape optimization across
hundreds of variants, the tank for the final validated number.

---

## Layer 5: From Resistance to Power

Resistance is a force; what the owner pays for is *power*. The chain from hull drag to
fuel burned passes through several efficiencies, each of which the designer fights for.

```
THE POWER CHAIN
===============================================================================

   R_total  --x speed-->  EFFECTIVE POWER (PE = R x V)   <- power to tow the bare hull
        |
        | / quasi-propulsive coefficient (hull-propeller interaction, ~0.65-0.75)
        v
   DELIVERED POWER (PD)  <- power the propeller must put into the water
        |
        | / shaft & bearing losses (~0.98)
        v
   SHAFT POWER (PS)  <- power at the shaft out of the gearbox
        |
        | / transmission / gearbox (~0.97)
        v
   BRAKE POWER (PB)  <- power the engine produces  -> this sets engine size & fuel
```

The defining identity is **effective power PE = R_total × V**: the power needed just to
tow the bare hull at speed V. Everything to the right of it is loss recovery, handed off
to guide [03] Propulsion, which covers how the propeller converts engine power into
thrust and where the propulsive efficiency goes.

A consequence worth stating plainly: because R_w climbs steeply with speed and PE = R·V,
**power required rises faster than the cube of speed** in the wave-making regime. Wanting
10% more speed can cost 35-40% more power. This cube-ish law is why "slow steaming" saves
so much fuel and is the central economic fact of ship operation.

---

## Worked Example: Predicting Full-Scale Resistance

A 6 m model of a 150 m ship (scale λ = 25). Model towed at 1.5 m/s; measured total
model resistance 30 N. Predict the ship's resistance and effective power at the
corresponding speed. (Seawater ρ = 1025 kg/m³, ν = 1.19×10⁻⁶ m²/s.)

```
   STEP 1 -- corresponding ship speed (Froude scaling):
     V_ship = V_model x sqrt(L_ship/L_model) = 1.5 x sqrt(150/6)
            = 1.5 x sqrt(25) = 1.5 x 5 = 7.5 m/s  (~14.6 knots)
     Check Froude: Fn = 1.5/sqrt(9.81 x 6) = 0.195 (model)
                      = 7.5/sqrt(9.81 x 150) = 0.196 (ship)  -> matched, good.

   STEP 2 -- model frictional resistance (ITTC line):
     Re_model = V_m L_m / nu = 1.5 x 6 / 1.19e-6 = 7.56e6
     C_f,model = 0.075 / (log10(7.56e6) - 2)^2
               = 0.075 / (6.879 - 2)^2 = 0.075/23.80 = 3.15e-3
     S_model (assume from lines) = 9.0 m^2
     R_f,model = 3.15e-3 x 0.5 x 1025 x 9.0 x 1.5^2 = 32.7 N
     (note: friction here EXCEEDS measured 30 N at this low Fn -- normal;
      it just means residuary is small. We keep signs honest below.)

   For a clean illustration take measured R_total,model = 40 N instead:
     R_residuary,model = 40 - 32.7 = 7.3 N
     C_r = 7.3 / (0.5 x 1025 x 9.0 x 1.5^2) = 7.3/9234 = 7.9e-4 (same both scales)

   STEP 3 -- scale residuary to ship:
     S_ship = S_model x lambda^2 = 9.0 x 625 = 5625 m^2
     R_residuary,ship = C_r x 0.5 x rho x S_ship x V_ship^2
                      = 7.9e-4 x 0.5 x 1025 x 5625 x 7.5^2 = 128,100 N

   STEP 4 -- ship friction (full-scale Reynolds):
     Re_ship = 7.5 x 150 / 1.19e-6 = 9.45e8
     C_f,ship = 0.075 / (log10(9.45e8) - 2)^2 = 0.075/(8.976-2)^2 = 1.54e-3
     R_f,ship = 1.54e-3 x 0.5 x 1025 x 5625 x 7.5^2 = 249,700 N

   STEP 5 -- total ship resistance (+ ~5% correlation allowance):
     R_ship ~ (249,700 + 128,100) x 1.05 = 396,700 N ~ 397 kN

   STEP 6 -- effective power:
     PE = R_ship x V_ship = 396,700 x 7.5 = 2.98 x 10^6 W = ~3.0 MW
```

Note the structural result: at this low Froude number friction (250 kN) dominates wave
drag (128 kN) — exactly what the decomposition predicts for a slow ship. The 3 MW is the
*effective* power; divide by the propulsive coefficient (~0.7, guide [03]) to get the ~4.3
MW the engine must actually deliver.

---

## Common Confusion Points

### "Friction or waves — which dominates?"

It depends entirely on Froude number, i.e. on speed-length ratio.

```
   SLOW & FULL (tanker, Fn<0.2)   |  FAST & FINE (frigate, Fn~0.4)
   ----------------------------   |  ----------------------------
   friction = 80-90% of total     |  wave-making can be 50%+ of total
   -> fight wetted surface,       |  -> fight wave-making: slenderness,
      coatings, fouling           |     bulbous bow, length
```

There is no universal answer; the speed regime selects the villain, which is why hull
shape is so different across ship types.

### Hull speed is not a hard wall

"Hull speed" (≈1.34√L in knots) is where the power penalty steepens, not a physical
limit. Planing craft and semi-displacement hulls routinely exceed it by lifting out of
the water and changing regime entirely. For a *displacement* hull, though, exceeding it
is brutally expensive in power.

### A bigger bulbous bow is not always better

The bulb is tuned to one design speed. Slow-steam a ship below that speed and the bulb's
wave can add to the hull's instead of cancelling it, *increasing* drag. Several operators
literally replaced bulbous bows after the industry shifted to permanent slow steaming.

### Cb (fullness) is not Cm (midship fullness)

A ship can have a full midship section (high Cm, square bilges) yet fine ends (low Cp),
giving a moderate overall Cb. The resistance lives mostly in Cp — how the volume tapers
toward bow and stern — not in Cb alone. Always ask *where* the volume is, not just how
much.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Describe how full a hull is | Block coefficient Cb = V/(L·B·T) |
| Predict drag scaling at model scale | Froude number Fn = V/√(gL) |
| Predict skin-friction scaling | Reynolds number Re = VL/ν |
| Estimate friction resistance | R_f = C_f·½ρSV², ITTC line for C_f |
| Reduce skin friction | Less wetted area, coatings, air lubrication |
| Reduce wave-making | Slender hull, length, bulbous bow |
| Predict full-scale R from a model | Froude's method (split, scale, recombine) |
| Get power from resistance | PE = R·V, then divide by propulsive coeff. |
| Optimize a hull across many variants | CFD (`fluid-dynamics/09-CFD.md`) |
| Understand boundary layers / wave drag generally | `fluid-dynamics/` [04],[08] |
| Convert thrust to engine power | guide [03] Propulsion |
