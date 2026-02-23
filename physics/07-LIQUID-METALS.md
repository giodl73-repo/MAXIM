# Liquid Metals — Electromagnetic Properties and Behavior

## The Big Picture

Liquid metals are the experimentally accessible regime of MHD. They are
room-to-moderate-temperature conducting fluids where EM fields can be applied,
measured, and controlled in a lab. They also sit at the center of a cluster
of industrial technologies and — at the edges — fringe claims that deserve
precise evaluation.

```
+------------------------------------------------------------------------+
|                      LIQUID METALS LANDSCAPE                           |
|                                                                        |
|  THE FLUID          EM PROPERTIES         APPLICATIONS                 |
|  ────────           ─────────────         ────────────                 |
|  Mercury Hg         σ ~ 10⁶ S/m           Industrial processing        |
|  Gallium Ga         δ (skin depth)        EM pumping                   |
|  Sodium Na          Rm << 1 (lab)         Induction heating            |
|  Lead-Bismuth       η = 1/μ₀σ            EM stirring/forming          |
|  Aluminum (melt)                          Liquid metal batteries        |
|                                           Soft robotics (Ga)            |
|                                           Levitation melting            |
|                                                                        |
|  FRINGE TERRITORY (evaluated at end of this module):                  |
|  Rotating mercury + EM → anti-gravity?   What physics actually says.   |
+------------------------------------------------------------------------+
```

---

## What Makes a Liquid Metal

A liquid metal is a metal above its melting point — still metallic bonding,
still free electron gas, still high electrical conductivity, but fluid.

**Why metals conduct**: the free electron model. Valence electrons are not
bound to individual atoms — they form a delocalized electron gas that flows
freely through the ionic lattice. This remains true in the liquid phase.
The conductivity drops somewhat from solid (more lattice disorder = more
electron scattering), but remains 10⁵–10⁷ S/m — orders of magnitude above
any ionic solution or semiconductor.

**Key distinction from plasma**: in a plasma, the ions are also free (fully
ionized). In a liquid metal, only electrons are free — ions remain as
positively charged fluid. This affects the MHD at small scales (Hall effect,
two-fluid effects) but at large scales liquid metals obey single-fluid MHD.

---

## Properties of Key Liquid Metals

```
+──────────────────────────────────────────────────────────────────────────────+
│ Metal     │Melt  │Density │Viscosity│Conductivity│Skin depth │ Rm per       │
│           │ (°C) │(kg/m³) │(mPa·s)  │σ (MS/m)    │δ at 60 Hz │ m·(m/s)     │
+──────────────────────────────────────────────────────────────────────────────+
│ Mercury   │ -39  │ 13,600 │  1.5    │   1.0      │  65 mm    │  1.3×10⁻⁶   │
│ Gallium   │  30  │  6,090 │  2.0    │   3.7      │  34 mm    │  4.6×10⁻⁶   │
│ Indium    │ 157  │  7,020 │  1.9    │   3.4      │  36 mm    │  4.3×10⁻⁶   │
│ Sodium    │  98  │    930 │  0.7    │  10.0      │  21 mm    │  1.3×10⁻⁵   │
│ Lithium   │ 181  │    510 │  0.6    │   4.0      │  33 mm    │  5.0×10⁻⁶   │
│ Lead-Bi   │ 125  │ 10,500 │  1.7    │   0.9      │  69 mm    │  1.1×10⁻⁶   │
│ Al (melt) │ 660  │  2,380 │  1.3    │   4.1      │  33 mm    │  5.2×10⁻⁶   │
│ Fe (melt) │1538  │  6,980 │  5.5    │   0.7      │  76 mm    │  8.8×10⁻⁷   │
+──────────────────────────────────────────────────────────────────────────────+

  δ = √(2/ωμ₀σ) at f=60 Hz    Rm per m·(m/s) = μ₀σ  (multiply by v×L for Rm)

  Skin depth: depth at which EM field amplitude falls to 1/e
  Rm column: multiply by v (m/s) × L (m) to get magnetic Reynolds number
```

**Mercury** (-39°C melt): the only liquid metal at room temperature.
Dense, low viscosity, moderate conductivity. Historical use in switches,
thermometers, instruments. Toxic — use largely phased out.

**Gallium** (30°C melt): melts in your hand. Non-toxic. Alloys (GaInSn =
galinstan) are liquid at -19°C. The modern substitute for mercury in many
applications. Wets most surfaces (difficult to contain). Recent revolution
in soft robotics.

**Sodium** (98°C melt): lightweight, very high conductivity, excellent heat
transfer. Used as coolant in fast breeder nuclear reactors (BN-800, Superphénix).
Violent reaction with water — handling requires inert atmosphere. Rm for
reactor-scale flows can reach 10-100 (interesting MHD regime).

**Lead-bismuth eutectic** (125°C melt): dense, moderately conducting, no
sodium-water reaction hazard. Used in some submarine reactors (Russian Alfa-class)
and new reactor designs. Polonium-210 buildup from neutron activation of bismuth
is a radiological concern.

---

## Electromagnetic Properties in Detail

### Skin Depth and Field Penetration

From module 04: δ = √(2/ωμσ)

For liquid metals, the key question is whether the applied EM field penetrates
throughout the bulk or is confined to the surface. This determines whether
you can pump/stir/heat the whole volume or only the surface layer.

```
  PENETRATION REGIMES:

  δ >> L (device size):   field penetrates fully — bulk coupling
  δ ~ L:                  partial penetration — complex profiles
  δ << L:                 surface coupling only — skin effect dominates
```

At power-line frequency (50/60 Hz), all liquid metals have δ in the range
20-80 mm — so lab-scale devices (10-100 mm) are in the full-penetration to
partial-penetration regime. This is why industrial MHD devices operate at
low frequency.

At higher frequencies (kHz-MHz), δ shrinks to millimeters or less — the field
is confined to a surface skin and the coupling changes character entirely.

### Magnetic Reynolds Number in the Lab

For liquid metals in laboratory conditions (v ~ 0.1-1 m/s, L ~ 0.01-0.1 m):

```
  Rm = μ₀σvL ~ 10⁻⁶ × 1 × 0.1 = 10⁻⁷  to  10⁻⁵  (mercury)
       μ₀σvL ~ 10⁻⁵ × 10 × 1   = 10⁻⁴  to  10⁻²  (sodium, large-scale)
```

Laboratory liquid metals are firmly in the **low-Rm regime**: the flow barely
perturbs the externally applied B field. This greatly simplifies the analysis —
the EM problem decouples from the fluid problem. You compute J and F from the
applied B and the flow, without needing to solve for the modified B.

Only at reactor scale (sodium, L ~ 1 m, v ~ 1 m/s) does Rm approach 1 and the
full coupled MHD system become necessary.

---

## Industrial Applications

### Electromagnetic Pumping

No moving parts, no seals, no contact with the fluid. Three main types:

```
  DC CONDUCTION PUMP:
  Apply DC current across the duct + static external B
  J×B force drives flow
  Requires electrical contacts in the liquid metal
  Simple, reliable, used in sodium reactor loops

  AC INDUCTION PUMP (linear induction motor):
  AC coils outside the duct create traveling magnetic field
  Traveling field induces eddy currents in liquid metal
  Eddy currents + traveling field → J×B force pushes metal
  No electrical contacts with fluid
  Higher frequency → more induced current but shallower penetration

  ROTATING FIELD PUMP:
  Three-phase coils create rotating B field
  Rotating field drives azimuthal flow → centrifugal pumping
  Used for large-volume aluminum stirring
```

**Performance**: EM pumps can achieve flow rates of hundreds of liters/second
in nuclear applications. Efficiency 30-60% — lower than mechanical pumps, chosen
for reliability in hostile environments (radioactive sodium at 500°C).

### Induction Heating

High-frequency AC coil surrounding a conducting liquid metal container:
eddy currents induced in the metal → I²R Joule heating.

```
  INDUCTION FURNACE:

  AC coil (kHz-MHz)
       │
  ─────┼─────
  │ ~~~│~~~ │   ← Eddy currents (circles in liquid metal)
  │    │    │   ← Joule heating → temperature rise
  ─────┼─────
       │
  Frequency chosen so δ ~ R (container radius)
  for efficient coupling
```

At MHz frequencies, the eddy currents also create an outward magnetic
pressure (the J×B force is outward), which can **levitate** the liquid metal
away from the container walls — levitation melting. Used for ultra-pure
alloy preparation (no crucible contamination).

The stirring effect of induction furnaces is actually unwanted in some
applications (crystal growth) — electromagnetic braking coils are added to
suppress it.

### Electromagnetic Stirring

In continuous casting of steel, the solidifying metal must be stirred to
avoid segregation and improve grain structure. Rotating magnetic fields
create rotating flow in the liquid metal pool — electromagnetic stirring.

```
  CONTINUOUS CASTING:

  Liquid steel → mold → solidification front
                    ↕
  External rotating B field → induced currents → rotating flow
  → breaks up dendrites → uniform grain structure → better steel
```

Used in essentially all modern continuous steel casting. The field parameters
(frequency, strength, position) are tuned to the metallurgy of each alloy.

### Electromagnetic Forming and Shaping

Pulsed high-current coils near molten metal create transient J×B forces
that shape the free surface without contact.

**Electromagnetic levitation** (not anti-gravity — electromagnetic pressure):
A conducting sphere (or liquid metal droplet) placed above a coil carrying
high-frequency AC. The induced eddy currents interact with the coil field —
net upward J×B force supports the metal against gravity.

```
  LEVITATION PRINCIPLE:

  AC coil (RF, ~ 100 kHz-MHz)
       │     B field concentrated above coil
  ─────────────────
  ~~~~~~~~~~~~~~~~~~~~   ← induced eddy currents in metal
  ─────────────────
  metal droplet floats    Force = B²/2μ₀ × area > mg
```

This is **real electromagnetic levitation** — used for:
- Processing reactive metals without crucible contamination
- Measuring surface tension of liquid metals
- Demonstrating MHD (the levitron principle)

It is emphatically not anti-gravity — gravity is unchanged, the metal is
pushed up by EM pressure from below, exactly as a ping-pong ball is held up
by an air jet.

---

## Liquid Metal Batteries

Sadoway group (MIT), commercialized by Ambri.

Three liquid layers at operating temperature (450-700°C), separated by
density and immiscibility:

```
  LIQUID METAL BATTERY:

  ─────────────────────────────
  Negative electrode (top):    Mg, Li, Na  (low density, electropositive)
  ─────────────────────────────
  Electrolyte (middle):        Molten salt (MgCl₂, LiCl, etc.)
  ─────────────────────────────
  Positive electrode (bottom): Sb, Bi, Pb  (high density, electronegative)
  ─────────────────────────────
```

The density gradient maintains the layering — no separators, no membranes,
all self-assembling. On discharge: metal at top dissolves into electrolyte,
deposits on bottom. On charge: reverse.

**Advantages**: very low cost (earth-abundant materials), long cycle life
(no solid-state degradation), simple manufacturing.
**Challenges**: high operating temperature, self-discharge at temperature,
efficiency ~80%.

Target: grid-scale storage at <$100/kWh to enable 24/7 renewable power.

---

## Gallium-Based Soft Robotics

Gallium and its alloys (galinstan: Ga-In-Sn, liquid at -19°C) have enabled
a new class of deformable electronics and actuators.

**Key properties for soft robotics**:
- Liquid at room temperature — deformable, stretchable
- Metallic conductivity — can carry signals and power
- Non-toxic (unlike mercury)
- Surface tension keeps it contained in elastomer channels
- Can be shaped, injected, printed

**Electromagnetic actuation of liquid metal**:

Lorentz force on current-carrying liquid metal in a B field can deform
the metal, move it through channels, or change circuit topology:

```
  RECONFIGURABLE ANTENNA:
  Gallium in elastomer channel → apply pressure → metal flows → antenna
  changes shape → resonant frequency changes
  No moving mechanical parts — fluid reconfiguration
```

**EGaIn (gallium-indium)**: forms an oxide skin on contact with air that
provides structural support while remaining deformable. Used for:
- Stretchable circuit interconnects
- Self-healing conductors
- Microfluidic logic
- Variable stiffness structures

The electromagnetic behavior follows from standard MHD at the microscale —
the same induction and Lorentz force physics, just in microchannel geometry.

---

## The Fringe Claims — Evaluated

This section examines specific claims about liquid metals and E&M that appear
in non-mainstream sources. For each: what is claimed, what the physics says.

### The Mercury Vortex Engine (Vimana Propulsion)

**Claim**: Ancient Sanskrit texts (Vaimanika Shastra) describe aircraft
propelled by rapidly rotating mercury in a container, creating lift and thrust.

**What physics says**:
- Rotating liquid mercury in a container: the MHD forces are completely
  described by the equations in module 06. No anomalous effects.
- Rotating charged fluid does create a magnetic field (it's a current loop).
  For a small mercury drum, this field is tiny (~nT range).
- The gravitomagnetic (frame-dragging) effect of a rotating mass also exists —
  this is real GR physics. For a lab-scale mercury drum, it is ~10⁻²³ T
  equivalent — unmeasurably, unreachably small.
- **Verdict**: rotating mercury can drive a pump, create small magnetic fields,
  and theoretically produce ion thrust if ionized. None of these mechanisms
  produce significant lift against gravity. The Vaimanika Shastra was likely
  written ~1900 CE, not ancient.

### The Nazi Bell (Die Glocke)

**Claim**: Late-WWII German experimental device, two counter-rotating drums
of mercury (or mercury compound), claimed to cause anomalous gravitational,
biological, or spacetime effects.

**What physics says**:
- Primary source is one postwar account (Witkowski, 2000) — no wartime
  documentation verified.
- Counter-rotating conducting fluids: creates complex MHD flows, possibly
  interesting instabilities. No known mechanism for gravitational modification.
- Strong rotating EM fields CAN affect biological tissue (induced currents,
  magnetic field effects on free radicals). This is documented and plausible
  for any high-field device.
- **Verdict**: probably either a centrifuge, a uranium enrichment device (both
  use spinning cylinders), or fabricated entirely. The "antigravity" framing
  is inconsistent with any known or theoretically plausible physics.

### Podkletnov Effect

**Claim**: Evgeny Podkletnov (1992): a rotating superconducting disc above
a superconducting magnet reduces the weight of objects above it by ~2%.

**What physics says**:
- The effect, if real, would be extraordinary — gravity modification by an
  EM device would overturn GR and open enormous engineering possibilities.
- Multiple serious replication attempts: NASA Marshall Space Flight Center
  (2001-2006), Boeing Phantom Works, Canterbury University — none confirmed
  the effect.
- The Meissner effect in superconductors creates strong EM fields above the
  disc. Any acceleration sensor in this field has large EM systematic errors
  that could mimic a gravity reduction.
- GR permits no mechanism: EM energy density does curve spacetime via the
  stress-energy tensor, but a lab-scale superconductor's EM field contributes
  ~10⁻³⁰ g of gravitational effect. Not 2%.
- **Verdict**: most likely experimental artifact (EM interference with sensor,
  vibration coupling). Effect not reproducible under controlled conditions.

### What Physics Actually Permits

Legitimate EM effects that sound dramatic but are real:

```
  ELECTROMAGNETIC LEVITATION:   Real. EM pressure supports conducting objects.
  Not antigravity — gravity unchanged, EM force opposes it.

  MEISSNER LEVITATION:          Real. Superconductors expel B fields.
  Magnet floats above superconductor. Used in maglev trains.
  Not antigravity — magnetic pressure supports the magnet.

  GRAVITOELECTROMAGNETISM (GEM): Real. Weak-field GR analog of Maxwell.
  Frame-dragging confirmed by Gravity Probe B (2011).
  Effect is ~10⁻¹⁴ of EM forces at equivalent scales.
  Cannot be harnessed for propulsion at any conceivable power level.

  RADIATION PRESSURE:           Real. EM waves push on objects (solar sail).
  Not antigravity — an actual force, but tiny.
  ~9 μN/m² at 1 AU from Sun.

  BIEFELD-BROWN EFFECT:         Real thrust from asymmetric capacitors.
  Mechanism: electrohydrodynamic ion wind — NOT gravity modification.
  Works in air, not in vacuum — confirms ion wind mechanism.
```

**The fundamental barrier**: gravity couples to mass-energy with coupling
constant G/c² ~ 10⁻²⁷ m/J. Electromagnetism couples to charge with coupling
constant 1/4πε₀ ~ 10¹⁰ N·m²/C². The ratio is ~10³⁶. No known physics allows
an EM device to produce gravitational effects comparable to its EM effects.
Any claimed effect requires either extraordinary evidence or an error in
measurement.

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Best liquid metal for room-temp work | Galinstan (Ga-In-Sn), -19°C melt, non-toxic |
| Best conductivity | Sodium (~10 MS/m) but 98°C melt, reactive |
| Skin depth for 60 Hz, mercury | ~65 mm |
| Full field penetration condition | δ >> device size L |
| Lab MHD: Rm regime | Rm << 1 — external B barely perturbed |
| EM pump mechanism | J×B Lorentz force on current in B field |
| EM levitation mechanism | Eddy current J×B upward force, not gravity change |
| Rotating liquid metal in B field | Standard MHD — no anomalous effects |
| Podkletnov effect status | Not replicated, likely artifact |
| Real EM "levitation" | Meissner effect, EM pressure — gravity unchanged |

---

## Common Confusion Points

**Electromagnetic levitation is not anti-gravity.**
When a liquid metal is levitated by an RF coil, gravity is unchanged.
The EM force pushes the metal up; gravity pulls it down; equilibrium.
Remove the coil, gravity wins immediately. Nothing has changed about the
gravitational field — a nearby mass is not affected at all.

**High conductivity does not mean high Rm in the lab.**
Rm = μ₀σvL. Even sodium (highest conductivity liquid metal) gives Rm ~ 10⁻⁴
at lab scale (v=0.1 m/s, L=0.01 m). You need large scale AND high velocity
to get interesting Rm. This is why MHD dynamo experiments require large
tanks of sodium.

**Mercury is not special for EM effects — it's historically convenient.**
Mercury was used in early EM experiments because it's liquid at room temperature.
Any liquid metal with comparable conductivity gives the same physics.
Gallium is now preferred in laboratories (non-toxic, similar properties).
The "special" status of mercury in fringe literature has no physical basis.

**Skin depth is not a sharp boundary.**
The field doesn't stop at z = δ — it decays exponentially. At z = δ, it's
at 37%; at z = 2δ, it's at 14%; at z = 3δ, 5%. For "full penetration"
in practice, you want δ ≥ 3-5× the device half-thickness.

**Low Rm doesn't mean EM effects are weak.**
Even at Rm << 1, J×B forces can strongly modify the flow (large Hartmann
number). Rm measures whether the flow modifies B; Ha measures whether B
modifies the flow. These are independent. A liquid metal pump can have
Rm = 0.001 (B barely perturbed by flow) and Ha = 100 (flow strongly
controlled by B). That's exactly the useful operating regime.
