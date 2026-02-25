# Joining: Welding, Brazing, and Adhesives

## The Big Picture

Joining processes create permanent or semi-permanent connections between separately manufactured parts. The tradeoff axes: joint strength, distortion, heat input, material compatibility, cost, and reversibility.

```
JOINING PROCESS MAP
──────────────────────────────────────────────────────────────────
                              JOINING
                               │
           ┌───────────────────┼───────────────────┐
           │                   │                   │
     MECHANICAL           CHEMICAL/THERMAL       COHESIVE
     FASTENING            JOINING               MATERIAL
     ─────────            ──────────            ─────────
     Bolts/screws         Fusion welding        Adhesive bonding
     Rivets               Solid-state weld      Brazing/soldering
     Press fit            Brazing/soldering
     Snap fit             Diffusion bonding
     Clinching

     Reversible?          Heat input:           Bond quality:
     Usually yes          High → Low            Adhesive = surface
     (bolts/rivets)       Fusion welding most   Brazing = capillary
     Interference fit     Soldering least       Welding = metallurgical
     = semi-permanent     FSW = intermediate    (strongest)
```

---

## Fusion Welding Processes

### MIG Welding (GMAW — Gas Metal Arc Welding)

```
MIG WELDING SETUP
──────────────────────────────────────────────────────────────────
Wire electrode feeds through torch continuously.
Arc between wire and workpiece → melts both → forms weld pool.
Shielding gas protects molten metal from atmosphere.

        Wire spool → wire conduit → welding gun
                                       │
                              Wire electrode (0.030"–0.045")
                                       │
                              ┌────────▼────────┐
                              │   Arc / Pool    │ ← Shielding gas
                              └─────────────────┘
                                   │
                               Solidified weld bead

Shielding gas choices:
  75% Ar + 25% CO₂  →  mild steel (C25), general purpose
  100% CO₂           →  cheaper, more spatter, deeper penetration
  98% Ar + 2% O₂     →  stainless steel
  100% Ar            →  aluminum
  Tri-mix (Ar+He+CO₂) →  stainless, thick section

Transfer modes:
  Short circuit:   low current, low heat, thin material (< 3mm)
  Globular:        high spatter, inefficient, avoid
  Spray transfer:  high current, high deposition, thick material
  Pulse MIG:       alternates high/low, better control, less distortion
```

### TIG Welding (GTAW — Gas Tungsten Arc Welding)

```
TIG WELDING
──────────────────────────────────────────────────────────────────
Non-consumable tungsten electrode creates arc.
Filler rod added separately (or autogenous — no filler).
Higher operator skill. Much better control and quality.

         Tungsten electrode
              │
         ┌────▼────┐
         │  Arc    │ ← 100% Argon shielding
         └────┬────┘
              │                  Filler rod (optional)
          Weld pool ◄────────────────────────
              │
           Weld bead

Applications: aerospace, stainless, titanium, aluminum (AC),
              thin sheet, pipe welds (root pass), critical joints

AC TIG for aluminum: alternating current provides "cleaning action"
  → breaks up oxide layer (Al₂O₃) on oxide film
  → DCEN (direct current electrode negative) for steel/Ti

Pulse TIG:
  Alternates peak and background current
  → excellent control of heat input
  → thin sheet, heat-sensitive materials, root passes
```

### SAW (Submerged Arc Welding)

Consumable wire electrode, arc submerged under granular flux. No UV flash, very high deposition rates. Used for heavy plate (pressure vessels, structural beams, ship hulls). Requires flat/horizontal position — flux falls off vertical surfaces.

### FCAW (Flux-Cored Arc Welding)

Hollow wire with flux inside. High deposition rate, all positions. Self-shielded (no external gas) or gas-shielded. Between MIG and SAW in quality. Common for structural steel fabrication, field erection.

### PAW (Plasma Arc Welding)

Constricted arc through a water-cooled copper nozzle → plasma jet. Higher energy density than TIG. Used for keyhole welding (single pass on thick material), precision micro-welding.

### Laser and Electron Beam Welding

```
LASER WELDING (LBW)
  High-power laser focused to small spot
  Deep narrow welds ("keyhole" mode)
  Very low heat input, minimal distortion
  Fast (1–15 m/min for thin sheet)
  Fiber laser (Nd:YAG, diode pump) → most common
  CO₂ laser → thick material, large spot
  Applications: automotive body panels, battery packs, medical

ELECTRON BEAM WELDING (EBW)
  Focused electron beam in vacuum
  Extremely deep narrow welds (depth:width up to 30:1)
  Near-zero atmospheric contamination
  Applications: aerospace (jet engine discs), titanium, refractory metals
  Limitation: requires vacuum chamber → large parts impractical
```

---

## Solid-State Welding

### Friction Stir Welding (FSW)

```
FSW PROCESS
──────────────────────────────────────────────────────────────────
Rotating pin tool plunges into workpiece.
Friction heats metal to plasticized state (below melt).
Tool traverses joint, mechanically stirs material.
Metals forge together behind tool.

     Shoulder (heats and forges surface)
         │
    ┌────▼────┐
    │  Tool   │ → rotates + translates
    └────┬────┘
         │
         Pin (plasticizes and stirs)
         │
    ┌────▼──────────────────────────────────┐
    │  Workpiece 1    │    Workpiece 2       │
    └─────────────────┴─────────────────────┘
              Joint line (zero gap tolerance)

Properties:
  - No melt → no solidification defects
  - Fine equiaxed grain at joint → excellent properties
  - Al-Al joints: 80–90% of parent strength (vs 60–70% for MIG)
  - No fumes, minimal distortion
  - Can join 2024-T3 and 7075-T6 (unweldable by fusion)

Limitations:
  - Tool wear on hard materials (steel FSW is difficult)
  - Keyhole at end of weld (run-off tab or backfill required)
  - Joint must be rigidly clamped (high axial force)
  - Speed: 200–1000 mm/min (slower than laser)
```

### Other Solid-State Methods

```
DIFFUSION BONDING
  Parts held under pressure at elevated temperature (~0.5–0.7 Tm)
  Atomic diffusion across interface → metallurgical bond
  No melt, no deformation
  Very flat surfaces required (Ra < 0.4 µm)
  Applications: titanium aerospace, multilayer metal structures
  Batch process, slow

ULTRASONIC WELDING
  Vibration at 20–70 kHz creates friction at interface
  → local heating → pressure → bond
  Plastics (most common), thin metals, dissimilar materials
  Fast (0.1–2 seconds), no filler, no heat affected zone
  Automotive: instrument panels, fuel tanks, door trim

EXPLOSIVE WELDING
  Controlled detonation of explosive layer accelerates one plate
  into another → wavy interface → metallurgical bond
  Joins highly dissimilar metals (aluminum-steel clad, titanium-steel)
  Pressure vessel cladding, bimetallic transition pieces
```

---

## Brazing and Soldering

### Brazing Principles

```
BRAZING vs SOLDERING vs WELDING
──────────────────────────────────────────────────────────────────
           Temperature     Filler        Base metal
           at joint        melts?        melts?
Welding    >T_liquidus     No (or same)  Yes
Brazing    450°C–1150°C    Yes           No
Soldering  <450°C          Yes           No

Brazing mechanics:
  1. Base metal heated above filler melting point
  2. Filler (braze alloy) wets and flows by capillary action
     into tight joint gap (0.001"–0.010" / 25–250 µm)
  3. Filler solidifies → brazed joint
```

### Common Brazing Alloys

| Alloy Type | Temp Range (°C) | Base Metals Joined | Notes |
|------------|----------------|-------------------|-------|
| Silver (BAg) | 620–900 | Most metals | Most common, general purpose |
| Copper-Phosphorus (BCuP) | 700–900 | Copper + alloys | Self-fluxing on copper |
| Nickel (BNi) | 900–1200 | SS, Ni alloys, steel | High-temp service |
| Aluminum-Silicon (BAISi) | 590–620 | Aluminum | CAB process for heat exchangers |
| Gold (BAu) | 900–1100 | Electronics, medical | Precious, bio-compatible |

### Furnace Brazing

```
FURNACE (CONTROLLED ATMOSPHERE) BRAZING
──────────────────────────────────────────────────────────────────
Parts fixtured with braze foil/paste pre-placed at joints.
Loaded into furnace (vacuum, hydrogen, or nitrogen atmosphere).
Cycle:
  1. Heat to pre-braze temperature (450°C) → burn off organics
  2. Ramp to braze temperature → filler melts, flows
  3. Hold (soak) → complete capillary flow and diffusion
  4. Controlled cool (avoid thermal shock to ceramics or thin joints)

Advantages over torch brazing:
  - All joints in assembly heated simultaneously
  - No oxidation → no flux needed (vacuum or reducing atmosphere)
  - Reproducible: time-temperature controlled
  - Better joint quality
  - Scale production: batch furnaces, mesh belt continuous furnaces

Applications: automotive heat exchangers (Al-brazing), aerospace
  assemblies, carbide tool inserts brazed to steel shanks
```

### Soldering

```
SOLDERING ALLOYS
──────────────────────────────────────────────────────────────────
Sn-Pb (60/40, 63/37 eutectic):
  Eutectic: 183°C, classic electronics solder
  BANNED in EU (RoHS) for consumer electronics since 2006
  Still used: military, aerospace, medical (exemptions)

Lead-free SAC (Sn-Ag-Cu):
  SAC305: Sn-3.0Ag-0.5Cu, liquidus 217°C (most common)
  Higher process temp → more board and component stress
  More brittle than Sn-Pb under thermal cycling
  RoHS compliant

Low-temp alternatives:
  Bi-Sn: 138°C eutectic → sensitive components, rework
  In-Sn: 118°C → cryogenic, flexible electronics

Soldering methods: iron, hot air, reflow oven (SMD), wave (THT)
```

---

## Adhesive Bonding

### Adhesive Mechanics

```
ADHESIVE JOINT MECHANICS
──────────────────────────────────────────────────────────────────
Strength depends on:
  Adhesion (surface chemistry): adhesive bonded to substrate
  Cohesion (adhesive strength): adhesive bonded to itself

Failure modes:
  Adhesive failure:  failure at interface (preparation problem)
  Cohesive failure:  failure within adhesive (strength OK, design issue)
  Mixed mode:        combination (typical in well-designed joints)

Goal: cohesive failure (adhesive is load-limiting, not surface prep)

Loading in adhesive joints:
  Shear:    Strongest (adhesive designed for this)
  Tension:  Moderate (peel and tension separations)
  Peel:     WEAKEST → avoid peel loading in joint design
  Cleavage: Similar to peel, one side rigid
```

### Major Adhesive Types

| Type | Chemistry | Strength | Temperature | Notes |
|------|-----------|----------|------------|-------|
| Epoxy | Two-part or heat-cure | Very High | −55 to 200°C | Structural standard |
| Acrylic / MA | Two-part, rapid cure | High | −40 to 150°C | Oily surfaces OK |
| Cyanoacrylate | One-part, humidity cure | Medium-High | −55 to 120°C | Fast, gaps fill poorly |
| Polyurethane | One or two-part | Medium | −40 to 80°C | Flexible, impact absorb |
| Silicone | RTV or heat-cure | Low-Med | −65 to 300°C | High temp, flexible |
| Anaerobic | Metal-activated, no O₂ | High | −55 to 150°C | Threadlock, retaining |
| Film adhesive | Prepreg film, heat-cure | Very High | −55 to 180°C | Aerospace composites |

### Surface Preparation (Critical)

```
SURFACE PREP HIERARCHY
──────────────────────────────────────────────────────────────────
Steel:
  1. Degrease (MEK, acetone, IPA)
  2. Abrade (80–120 grit) or grit blast
  3. Wipe clean again
  4. Apply primer if long open time or corrosion risk

Aluminum:
  1. Degrease
  2. Chemical etch (chromic acid = best, phosphoric acid = green)
  3. Anodize (sulfuric acid or phosphoric) + prime
  → Necessary for durable bonding (oxide layer otherwise)

CFRP (carbon fiber):
  1. Peel-ply removal (exposes fresh surface) → immediate bonding
  2. Abrade lightly with 120 grit
  3. Solvent wipe

Contamination kills bond strength:
  Oil, mold release, dust, fingerprints → adhesive failure
  Rule: bond within 4 hours of surface prep
```

---

## Joint Design Principles

### Welding Joint Types

```
BASIC WELD JOINTS (AWS nomenclature)
──────────────────────────────────────────────────────────────────
Butt joint:      ─┤├─   Flat plates aligned, groove fill
Corner joint:    □       Two plates at 90° corners
T-joint:         ┴       One plate perpendicular to another
Lap joint:       ══      Plates overlapping, fillet weld
Edge joint:      ∥       Edges parallel (thin sheet)

Groove types for butt joints:
  Square butt:   clean edges, thin material (< 6mm)
  V-groove:      beveled edges, thicker material, single V
  Double V:      bevel both sides, thick plate, less distortion
  U-groove:      radiused root, less fill, tight spaces
  J-groove:      one-sided U, limited access joints
```

### Weld Symbol on Drawing

```
WELD SYMBOL ANATOMY
──────────────────────────────────────────────────────────────────
        Tail (specification/                Weld symbol
        process note)                       (on arrow side)
           ╲                               /
Reference ──╲──────────────────────────────── Arrow (points to joint)
   line       ╲
               Note above = other side
               Note below = arrow side

Common symbols:
  △  Fillet weld (size = leg length, e.g., 5△)
  |→ Groove weld (with depth of bevel indicated)
  O  Weld all around
  (circle at reference line intersection)
  Field weld flag (filled triangle at reference line)
```

---

## Decision Cheat Sheet

| Need | Process |
|------|---------|
| General fabrication, steel | MIG (GMAW) |
| High-quality, thin, SS/Ti/Al | TIG (GTAW) |
| Heavy plate production | SAW (Submerged Arc) |
| Aluminum panels, aerospace | Friction Stir Welding |
| Titanium assemblies | TIG or EBW (vacuum) |
| Automotive body panels | Laser welding or RSW |
| All joints in an assembly simultaneously | Furnace brazing |
| Carbide inserts on tooling | Furnace or torch brazing (silver) |
| Aluminum heat exchangers | Controlled atmosphere (CAB) brazing |
| Electronic solder (RoHS) | SAC305 reflow |
| CFRP structural bond | Film adhesive (epoxy) |
| Fast-cure structural bond | Two-part acrylic or epoxy |
| Vibrating fastener lock | Anaerobic (Loctite) |

---

## Common Confusion Points

**Brazing vs welding strength**: Brazing joints can be stronger than the base metal in shear — the filler distributes stress across a large area. But tension (peel) loading on a brazed joint is much weaker. The design must route loads into shear.

**Flux in brazing vs soldering**: Flux removes oxides that prevent wetting. Insufficient flux → dewetting, voids. Excess flux → corrosion if not removed (especially for aluminum). Vacuum and controlled-atmosphere brazing eliminate flux entirely — better quality, no post-cleaning.

**FSW keyhole**: At end of weld, pin withdraws leaving a hole. For structural applications, run weld off the part (tab piece) and cut tab away. Retractable-pin tools eliminate this. NASA has used FSW for cryogenic fuel tank structures (Space Shuttle external tank replacement).

**Solder joint reliability under thermal cycling**: Pb-free SAC joints crack under thermal fatigue more readily than Sn-Pb. JEDEC standards specify thermal cycling profiles for reliability testing. Military/aerospace exemptions for Sn-Pb remain because the reliability data for Pb-free in high-cycle environments is still accumulating.

**Adhesive creep under sustained load**: Most structural adhesives exhibit viscoelastic creep under sustained load, especially above 60°C. Aerospace film adhesives are tested for creep specifically. Do not design lap-shear joints with constant tensile loads in warm environments without creep data.
