# Deep Foundations: Driven Piles, Drilled Shafts, Capacity, Lateral Loads

## The Big Picture

Deep foundations transfer load to soil or rock at depth, bypassing near-surface soils that are too weak, compressible, or unstable to support the structure. The mechanism is either end bearing (load transferred to strong material at pile tip) or skin friction (load transferred along the pile shaft through interface shear) or — usually — both.

```
+------------------------------------------------------------------+
|               DEEP FOUNDATION SELECTION                         |
+------------------------------------------------------------------+
|                                                                  |
|  WHY DEEP FOUNDATIONS?                                           |
|  Near-surface soils too weak/compressible                       |
|  Need to bypass scour zone (bridges, piers)                     |
|  Uplift (tension) forces from wind/hydrostatic/earthquake       |
|  Settlement control (transfer to stiffer material)              |
|  Lateral loads requiring deeper fixity                          |
|                                                                  |
|  DRIVEN PILES                    DRILLED SHAFTS (bored piles)  |
|  +-------------------+          +-------------------+           |
|  |  Steel H-pile     |          |  Dry method       |           |
|  |  Closed-end pipe  |          |  Casing method    |           |
|  |  Open-end pipe    |          |  Slurry method    |           |
|  |  Precast concrete |          |  (bentonite or    |           |
|  |  Timber           |          |   polymer)        |           |
|  +-------------------+          +-------------------+           |
|                                                                  |
|  CRITERIA FOR CHOICE:           CAPACITY METHODS:              |
|  • Soil type / rock depth        α method (total stress)        |
|  • Load magnitude                β method (effective stress)    |
|  • Vibration/noise limits        CPT-based methods              |
|  • Construction access           Static load test               |
|  • Water table / contamination   Dynamic testing (PDA/CAPWAP)   |
|                                                                  |
+------------------------------------------------------------------+
```

---

## Driven Piles

### Pile Types

| Type | Description | Advantages | Disadvantages |
|------|------------|-----------|---------------|
| **Steel H-pile** | Standard H-section steel (HP shapes) | Easy installation, high end bearing, can splice | Corrosion in aggressive soils |
| **Closed-end pipe pile** | Steel pipe with end plate | Inspectable interior, plug forms at tip | Higher cost |
| **Open-end pipe pile** | Steel pipe, soil enters | Can advance through harder layers | Must check plugging behavior |
| **Precast concrete** | Cast offsite, driven | Durable, no steel corrosion issue | Heavy, hard to splice, can crack during driving |
| **Timber** | Treated softwood | Low cost, excellent for marine | Decay if exposed to air, limited load |
| **Monotube/Tapered** | Thin-walled tapered steel | Good skin friction, displacement pile | Limited sizes |

### Installation — Driving Mechanics

**Hammers**:
- Drop hammer: simple, inefficient, causes shock
- Single-acting diesel: most common; fuel ignition drives ram down
- Double-acting: air/steam or hydraulic drives ram both ways; higher blow rate
- Hydraulic: controlled energy; reduces noise; better energy measurement

**Driving formula (ENR — Engineering News Record)**:
qu_formula = Wh × H / (s + C)

where Wh = hammer weight, H = drop height, s = set per blow (mm), C = empirical constant (25 for drop, 2.5 for steam).

**Problem**: ENR formula is unreliable — errors of 2–3× common. Use only for preliminary estimates.

### Wave Equation Analysis (WEAP)

Better: model the pile as a rod with wave propagation:
- Hammer + cushion + pile + soil resistance = system
- WEAP (Wave Equation Analysis Program) solves the 1D wave equation
- Input: hammer model, pile stiffness, soil damping and quake (Smith parameters)
- Output: blow count vs. capacity curve; driving stress
- Used to: select appropriate hammer, predict capacity from final blow count, check pile integrity

### Dynamic Load Testing (PDA/CAPWAP)

During driving or as restrike:
- Accelerometer + strain gauge mounted near pile head
- Record Force (from strain × EA) and Velocity (from acceleration integration)
- CAPWAP signal matching: model soil resistance to match measured response
- Result: capacity estimate comparable to static load test

ASTM D4945 governs; PDA tests are standard for most driven pile projects.

---

## Load Transfer — Axial Capacity

### Capacity Components

**Qult = Qs + Qp - W**

where:
- Qs = skin (shaft) friction capacity
- Qp = tip (end bearing) capacity
- W = pile weight (often neglected or small relative to capacity)

### Alpha Method (Soft Clay — Total Stress)

**fs = α × Su**

α = empirical adhesion factor (function of Su and pile type):

| Su (kPa) | α |
|---------|---|
| < 25 | 1.0 |
| 25–75 | 0.9 to 0.75 (interpolate) |
| 75–150 | 0.75 to 0.5 |
| > 150 | 0.5 to 0.35 |

**Qs = Σ(α × Su × πD × L_segment)**

### Beta Method (Sand or OC Clay — Effective Stress)

**fs = β × σ'v_avg**

β = K × tan δ
where K = lateral earth pressure coefficient (≈ 0.5–1.5 depending on installation), δ = interface friction angle

For driven piles in sand:
β typically ranges from 0.2 to 0.4 (compression) for most sands.

### CPT-Based Methods

Most reliable direct correlation. Several methods (Bustamante/Gianeselli, Eslami-Fellenius, UWA, ICP-05):

**ICP-05 (Imperial College) for sand**:
qf = 0.8 × qc × (σ'v/pa)^0.05 (end bearing at CPT tip resistance)
fs = δf = f(qc, σ'v, pile material, installation)

CPT-based methods are preferred when CPT data is available.

### Tip Resistance

**In clay**: Qp = Nc × Su × At (Nc = 9 for deep pile)
**In sand**: Qp = qc × At (from CPT); limit qp ≈ 10–15 MPa for most sands
**In rock**: Qp = qu × Nc × At (qu = uniaxial rock strength; Nc = 3 to 9)

---

## Drilled Shafts (Bored Piles)

### Construction Methods

**Dry method**: Drill, clean, place reinforcement, pour concrete. Only in stable soils above water table with no running ground.

**Casing method**: Advance temporary steel casing ahead of excavation. Used for running sands, cave-prone soils, or when drilling near existing structures.

**Slurry method**: Drill using bentonite (mineral slurry) or polymer slurry to maintain borehole stability against groundwater pressure. Slurry density slightly exceeds groundwater pressure at each depth.

```
SLURRY-SUPPORTED SHAFT:

  Ground surface
  ─────────────────────────────
  Slurry level  ←  must be > groundwater level
  ─────────────────────────────
  Groundwater   ←  hydrostatic pressure pushes in
  ─────────────────────────────
  Slurry pressure > GW pressure → borehole stable

  After drilling:
  1. Clean bottom with air lift or cleanout bucket
  2. Lower reinforcing cage
  3. Tremie concrete from bottom up (displaces slurry)
  4. Pull casing (if used) while concreting
```

### Drilled Shaft Capacity

Similar methods to driven piles. Key differences:
- Skin friction on drilled shafts in sand: lower β than driven (installation disturbs sand at interface)
- Tip resistance: requires clean bottom (no debris); reduced by construction disturbance
- Instrumented load tests: O-cell (bi-directional) test places jack at shaft bottom or mid-height → separates skin friction from tip

### O-Cell (Osterberg Cell) Load Test

Replaces expensive conventional top-load test for large shafts:
- Hydraulic jack embedded in shaft at tip or intermediate level
- Pushes up (mobilizes upper shaft friction) and down (mobilizes tip + lower skin friction) simultaneously
- Separately measures upper and lower resistances
- Equivalent top-load capacity derived by adding components with correction
- No reaction system needed — shaft itself provides reaction

---

## Lateral Load Capacity

### p-y Curve Method

Piles under lateral loads (wind, seismic, crane braking, vessel impact) are analyzed using p-y curves:

**p** = soil resistance per unit length of pile (kN/m)
**y** = lateral pile deflection at that depth

The pile is modeled as a beam on nonlinear Winkler springs. The governing differential equation:

EI × d⁴y/dz⁴ + p(y) = 0

p-y curves are empirically derived for specific soil types:
- **Soft clay**: Matlock (1970) hyperbolic curves based on Su, ε50
- **Stiff clay**: Reese et al. (1975); bilinear with softening
- **Sand**: O'Neill and Murchison (1983); hyperbolic functions of φ', unit weight, depth

```
p-y CURVES (schematic):

  p (soil resistance)
  |          ______________________________ pu (ultimate resistance)
  |         /
  |        /   Deep location (high pu)
  |       /
  |  ____/________________________________ pu (shallow)
  | /
  |/
  +──────────────────────────── y (deflection)

  Key parameters:
  pu = ultimate soil resistance (increases with depth)
  k = initial slope of p-y curve (py initial modulus)
```

**Software**: LPile, FB-MultiPier (for bridge piers + pile groups)

### Broms Method (Simple Estimate)

For preliminary design:
- Clay (undrained): Lateral capacity = 9Su × D at depth 1.5D below rotation point
- Sand: Lateral capacity from Kp × γ × z × D diagram

---

## Pile Groups

Individual pile capacities cannot be summed directly — group interaction reduces efficiency:

**Group efficiency**: η = Qgroup / (n × Qsingle)

For friction piles in clay, efficiency may be < 1 (block failure can govern):

**Block failure capacity** = 2(B + L) × Su × D + Su × N × c × B × L

Use lesser of:
1. n × Qsingle × η (individual piles)
2. Block failure (entire group with soil acting as one mass)

For end-bearing piles on rock: group efficiency ≈ 1.0 (tip loads independent).

**Group settlement**: Pile groups settle more than single piles. Model group as equivalent raft at 2/3 depth of piles. Apply consolidation theory to equivalent raft load.

---

## Design Codes and LRFD

Modern design: AASHTO LRFD Bridge Design Specification (structural/bridge piles):
- Resistance factors φ applied to calculated capacity
- φ depends on method: static analysis (φ = 0.35–0.65), dynamic PDA (φ = 0.65–0.75), static load test (φ = 0.75)
- Lower φ for less reliable capacity estimation
- Dead + live load factored: Qu ≥ φ × Rn

---

## Decision Cheat Sheet

| Situation | Foundation Type | Capacity Method |
|-----------|----------------|-----------------|
| Soft clay, no hard layer | Friction piles (driven or drilled) | Alpha method (total stress) |
| Dense sand, silt overlying | End-bearing piles to sand | Beta or CPT method |
| Bedrock at moderate depth | Drilled shaft socketed in rock | Rock socket in shear |
| Noise/vibration sensitive area | Drilled shafts (no driving) | CPT or load test |
| Scour zone (bridge pier) | Deep driven piles below scour | Capacity from below scour zone only |
| Lateral loads dominant | Drilled shaft (large diameter, stiff) | p-y analysis (LPile) |
| Verify capacity on-site | Static load test (ASTM D1143) | Direct measurement |

---

## Common Confusion Points

**Skin friction is not like sliding friction**: Skin friction in clay depends on adhesion (α × Su), which is not a friction angle. In sand, it's interface friction (β × σ'v). Don't confuse α method (clay, total stress) with β method (sand/OC clay, effective stress).

**End bearing is not the same as footing bearing capacity**: Deep pile tip bearing uses Nc = 9 for clay (deep failure, not Terzaghi's surface failure). In sand, qp is directly from CPT qc with a correction — it is not Terzaghi's formula applied at depth.

**Group settlement ≠ single pile settlement**: Group settlement from consolidation can be orders of magnitude larger than single pile settlement. The equivalent raft method at depth gives the stress increase; apply consolidation theory. For important projects this is the critical calculation.

**WEAP is not a substitute for load testing**: WEAP and PDA predict capacity based on wave mechanics and assumed soil model. For important structures (bridges, high-rises), a static compression test (ASTM D1143) is required to confirm design capacity.
