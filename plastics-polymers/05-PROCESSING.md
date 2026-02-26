# Processing: Injection Molding, Extrusion, Blow Molding

## The Big Picture

```
+------------------------------------------------------------------+
|              POLYMER PROCESSING LANDSCAPE                        |
|                                                                  |
|   PELLETS/GRANULES          PROCESSES           PRODUCTS         |
|   ───────────────           ─────────           ────────         |
|   PP, PE, ABS, etc.         Injection mold  →   Parts, housings  |
|   Dried (if hygroscopic)    Extrusion       →   Film, pipe, rod  |
|   Colorant / additive       Blow molding    →   Bottles, drums   |
|   masterbatch               Thermoforming   →   Trays, cups      |
|                             Compression     →   Thermoset parts  |
|                             Transfer mold   →   Precision TS     |
|                             Rotomolding     →   Large hollow      |
|                             Foam            →   Structural / pack |
+------------------------------------------------------------------+
```

All melt-processing shares a common physics: heat the polymer to lower
viscosity, force it into a shape, cool (or cure for thermosets) to lock shape.
The difference is how the shaping step is done.

---

## Melt Rheology — The Foundation

Processing forces depend on how polymer melts flow. Polymer melts are
non-Newtonian (shear-thinning) — viscosity decreases with shear rate.

```
   VISCOSITY vs. SHEAR RATE (log-log)

   η (Pa·s)
   |
   1000 |──────\         (Newtonian plateau at low shear)
        |       \
    100 |        \____   (power-law shear thinning region)
        |              \__
     10 |                  (high shear: near-Newtonian again)
        |
        +──────────────────────────────────> γ̇ (shear rate)
        0.01              100        10,000 s⁻¹
```

Power law: η = K · γ̇^(n-1)
n < 1 for polymers (pseudoplastic). LDPE: n ~ 0.35. PP: n ~ 0.25.
HDPE: n ~ 0.5. Lower n = more shear-thinning = easier to inject.

**Melt Flow Index (MFI)**: Standard comparative measure.
ASTM D1238: 2.16 kg load, 190°C (PE) or 230°C (PP), 10-min measurement.
MFI = grams extruded per 10 min.
- Low MFI (0.1–2): high MW, stiff melt, fiber/pipe grades
- High MFI (10–50): low MW, easy flow, thin-wall injection grades

---

## Injection Molding

Single highest-volume plastic processing method by number of parts produced.

### Machine Layout

```
   HOPPER → BARREL → SCREW → NOZZLE → MOLD (clamped)
     |          |                          |
   Pellets   Heater    Reciprocating    Cavity fills,
             bands     screw melts      cools, part ejects
```

### The Injection Cycle

```
   1. FILL:    Screw advances — melt injected into cavity under pressure
               Injection pressure: 50–200 MPa (hydraulic on screw face)
               Fill time: 0.5–5 seconds (thin wall faster)

   2. PACK:    Screw holds pressure — compensates for volumetric shrinkage
               Pack pressure: 50–80% of injection pressure
               Pack time: 2–15 seconds

   3. COOLING: Mold cooling circuit extracts heat
               Part must cool below Tg (amorphous) or Tm (semi-xtal)
               before ejection
               Cooling time: 5–60+ seconds (dominant cycle fraction)

   4. EJECT:   Mold opens, ejector pins push part out
               Part removed, mold closes, screw recovers (re-melts)

   TOTAL CYCLE: 10–120 seconds depending on part thickness and material
```

### Process Parameters and Defects

```
   PARAMETER        EFFECT                  DEFECT IF WRONG
   ─────────        ──────                  ───────────────
   Melt temperature  Viscosity (↑T → ↓η)   Too low: short shots, weld lines
                                             Too high: degradation, splay marks

   Injection speed   Fill rate              Too slow: premature freeze-off
                                             Too fast: jetting, burn marks

   Pack pressure     Shrinkage compensation Too low: sink marks, warpage
                                             Too high: flash, residual stress

   Mold temperature  Crystallinity, Tg      Too low: poor surface, warpage
                                             Too high: long cycle, sticking

   Cooling time      Dimensional stability  Too short: distortion on eject
```

### Gate Types

```
   EDGE GATE         — simplest, manual trim
   SUBMARINE GATE    — auto-degates on ejection (clip-off)
   HOT RUNNER        — no cold runner, no waste, better process control
   FAN GATE          — distributes flow for thin flat parts
   FILM GATE         — ultra-thin parts, flat distribution
   DIRECT SPRUE      — large single cavity, direct injection
```

### Mold Temperature: Critical for Crystallinity

```
   PP Mold Temperature Effect:
   ────────────────────────────
   Cold mold (25°C):   fast quench → small crystallites, lower χ_c
                        → lower modulus, hazy, dimensional issues later
   Hot mold (80–100°C): slow cooling → large crystallites, higher χ_c
                          → higher modulus, higher shrinkage (must be
                            accounted for in tool dimensions)

   For PEEK: mold at 160–190°C mandatory for crystallization
   Amorphous PEEK at cold mold: low Tg (~143°C) — unacceptable
   Crystallized PEEK: continuous use to 250°C
```

---

## Extrusion

Continuous process — screw melts and pumps polymer through a shaped die.

### Screw Design

```
   FEED ZONE → COMPRESSION ZONE → METERING ZONE
   ──────────   ─────────────────   ─────────────
   Deep channel  Decreasing depth   Shallow, constant
   Takes solid   Melts and          Pumps at controlled
   pellets       compresses         rate and pressure

   L/D ratio: 20:1 to 30:1 (length to diameter)
   Compression ratio: 2:1 to 4:1 (feed depth / metering depth)
```

### Die Shapes and Products

```
   FLAT DIE (sheet / film)          ANNULAR DIE (blown film)
   ───────────────────────          ────────────────────────
   ┌──────────────────────┐         Tube of melt rises vertically
   │   manifold           │         Internal air pressure inflates
   │   choker bar         │         bubble (2–5× die diameter)
   │   lip gap             │         Frost line: where melt solidifies
   └──────────────────────┘         Take-up nips flatten bubble
   → Sheet (>0.5mm)                 → LDPE/LLDPE film for bags, wrap
   → Film (<0.5mm biaxially later)

   PIPE/TUBE DIE                    PROFILE EXTRUSION
   ─────────────                    ─────────────────
   Mandrel inside die               Window profiles, deck boards
   Calibration sleeve sizes OD      Complex cross-sections
   Water cooling                    PVC, HDPE, WPC
```

### Blown Film Bubble Stability

```
   Key parameters:
   BUR (Blow-up ratio) = bubble diameter / die diameter
      Typical: 2:1 to 4:1
   TUR (Take-up ratio) = line speed / extrusion rate
      Controls machine-direction orientation

   LDPE: stable bubble, lower crystallization point (low MFI LCB grades)
   LLDPE: higher melt strength needed (blend with LDPE 20–30% for bubble)
   mLLDPE: narrow PDI → poor bubble stability → typically blended
```

---

## Blow Molding

### Extrusion Blow Molding (EBM)

Parison (hollow tube) extruded vertically → mold closes around it →
compressed air (0.3–0.7 MPa) inflates parison to mold walls.

```
   DIE HEAD
      │
      │ parison drops (100–300 mm/s)
      ↓
   [==parison==]
      │
      ↓ MOLD CLOSES (pinch bottom, seal top)
   ┌──────────┐
   │ air →    │   Air inflates parison to mold shape
   │ [bottle] │   Mold cooling water sets shape
   └──────────┘
      │
      ↓ MOLD OPENS — part ejected
```

Used for: HDPE milk jugs, detergent bottles, fuel tanks, large drums.
Parison programming: swell ratio varied along parison length to control wall
thickness uniformity in complex shapes.

### Injection Stretch Blow Molding (ISBM) — PET Bottles

Two-stage: injection mold preform → reheat → stretch + blow.

```
   STAGE 1: INJECTION MOLDING PREFORM
   Melt PET → inject into preform mold → cool to solid "test tube"
   Stored or immediately transferred.

   STAGE 2: BLOW MOLDING
   Reheat preform to Tg + 30–50°C (110–130°C for PET)
   Insert stretch rod → extends axially (×2.5)
   Air (1.5–4 MPa) → expands radially (×3.5)
   Biaxial orientation: aligns chains → χ_c 20–30% → barrier + strength
   Total stretch: (axial) × (hoop) ~ 8–10× area ratio
```

ISBM gives the CO2 barrier and pressure containment that PET CSD bottles need.
Same machine processes water, juice, sports drink, and beer bottles.

---

## Thermoforming

Sheet (typically 0.25–6 mm) heated above Tg → formed over mold → trimmed.

```
   VACUUM FORMING           PRESSURE FORMING
   ──────────────           ────────────────
   Sheet + vacuum           Sheet + air pressure (up to 4 bar)
   Simple, one-sided        Better detail, sharper corners
   Thin sheet only          Thicker sheet, better draw

   PLUG-ASSISTED: mechanical plug pre-stretches sheet before vacuum
   → more uniform wall thickness in deep draws

   MATERIALS: ABS, PS, PET, HDPE, PP, PMMA, PC
   PRODUCTS: Trays, blister packs, cups, auto door panels, spa baths
```

Wall thickness thinning is the key challenge. At corners and deep draws,
material thins. Draw ratio = depth / width. Ratio > 1 requires plug assist.

---

<!-- @editor[structure/P2]: Rotational molding referenced in landscape diagram and Decision Cheat Sheet but has no drill-down section — layering broken -->

## Compression and Transfer Molding (Thermosets)

```
   COMPRESSION MOLDING (thermosets / rubber)
   ──────────────────────────────────────────
   Charge (preform or powder) placed in open mold
   Mold closes under press (10–50 MPa)
   Heat from mold (150–200°C) cures material
   Open — demold

   Suitable: rubber compounds, phenolic, BMC, SMC
   Cycle: 1–10 minutes (cure-limited, not cool-limited)

   TRANSFER MOLDING
   ─────────────────
   Material in pot → ram forces through runners into closed cavities
   Better dimensional control than compression
   Used: precision electronic encapsulation, connectors
```

---

## Shrinkage, Warpage, and Dimensional Control

```
   VOLUMETRIC SHRINKAGE by material:

   Material      Mold shrinkage (%/mm)
   ──────────    ──────────────────────
   LDPE          1.5–4.0
   HDPE          1.5–3.5
   PP            1.0–2.5
   PVC rigid     0.2–0.6   (low – amorphous)
   PS            0.2–0.6   (low – amorphous)
   ABS           0.3–0.8   (low – amorphous)
   PC            0.5–0.7   (low – amorphous)
   Nylon 66      1.5–2.0   (higher – semi-xtal)
   POM           2.0–3.5   (highest – high xtal)
   PEEK          1.2–1.5

   Amorphous polymers: shrink ~0.5–1% (no density change from crystallization)
   Semi-crystalline:   shrink 1.5–4% (crystallization = densification)
```

Warpage = differential shrinkage. Gate location, cooling uniformity, and
fiber orientation all cause asymmetric shrinkage → flat parts warp.

---

## Decision Cheat Sheet

| Need | Process |
|------|---------|
| Complex 3D parts, medium–large volumes | Injection molding |
| Long continuous product (pipe, rod, profile) | Extrusion |
| Thin packaging film | Blown film extrusion |
| PET bottles | ISBM (2-stage) |
| HDPE/PP bottles, fuel tanks | Extrusion blow molding |
| Packaging trays, thermoformed cups | Thermoforming |
| Large hollow parts (kayaks, tanks) | Rotational molding |
| Thermoset precision parts / rubber seals | Compression / transfer molding |
| Structural foam (automotive, furniture) | Structural foam injection |

---

## Common Confusion Points

**MFI is not directly the processing viscosity**: MFI is measured at one shear
rate (low). Injection molding runs at 100–10,000 s⁻¹. A high-MFI polymer may
still behave differently at high shear. Always look at the full viscosity curve
for process simulation.

**Cooling time dominates cycle, not fill time**: Fill is 0.5–5 seconds. Pack is
2–15 seconds. Cooling is 5–60+ seconds. Cutting cooling time by conformal
cooling (3D-printed mold channels) can reduce cycle by 30–50%.

**Shrinkage must be built into the tool**: Mold dimensions = part dimensions /
(1 – shrinkage). For PP at 2% shrinkage, a 100 mm dimension requires 102.04 mm
mold feature. If this is wrong, all parts are wrong and the tool must be
modified (expensive).

**ISBM preforms are designed for specific bottles**: A 28g PET preform for a
0.5L bottle is engineered with specific wall thickness distribution. Use the
wrong preform and you get uneven walls, wall failure, or poor carbonation hold.
