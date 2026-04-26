# Shallow Foundations: Bearing Capacity, Settlement, Mats

## The Big Picture

Shallow foundations transfer structural loads to near-surface soils — typically within 3 meters of the ground surface. The two governing criteria are: (1) the soil must not fail in shear (bearing capacity), and (2) settlements must be within acceptable limits. In practice, settlement almost always governs in soft soils; bearing capacity governs in weak fills or very soft clays.

```
+------------------------------------------------------------------+
|          SHALLOW FOUNDATION DESIGN — DECISION FLOW               |
+------------------------------------------------------------------+
|                                                                  |
|  STRUCTURAL LOADS: Column, wall, mat loads (kN, kN/m, kPa)     |
|              |                                                   |
|              v                                                   |
|  SOIL PROFILE: Depth to acceptable bearing layer?               |
|  Groundwater table position?                                     |
|  Is near-surface soil adequate?                                 |
|              |                                                   |
|  YES: Shallow foundation feasible                               |
|              |                                                   |
|              v                                                   |
|  CHECK 1: BEARING CAPACITY                                       |
|  qu = cNc + qNq + 0.5γBNγ (Terzaghi general shear)             |
|  Factor of safety: qa = qu / FS (FS = 2.5 to 3)                |
|  Applied pressure q ≤ qa?                                        |
|              |                                                   |
|  YES: OK from strength perspective                               |
|              |                                                   |
|              v                                                   |
|  CHECK 2: SETTLEMENT                                             |
|  Immediate: Si = qBIf/Es (elastic)                               |
|  Consolidation: Sc = Cc/(1+eo) × H × log(σ'f/σ'o)              |
|  Is total and differential settlement within limits?            |
|              |                                                   |
|  YES: Foundation design acceptable                               |
|              |                                                   |
|  NO (either check): Increase size, change depth, use deep fdn.  |
|                                                                  |
+------------------------------------------------------------------+
```

---

## Foundation Types

| Type | Description | Typical Use |
|------|------------|-------------|
| **Isolated spread footing** | Square or rectangular pad under single column | Most common column foundation |
| **Continuous strip footing** | Long, narrow footing under wall | Bearing walls, building perimeter |
| **Combined footing** | Two or more columns on one footing | Closely spaced columns, near property lines |
| **Mat (raft) foundation** | Single slab under entire building footprint | Soft soils, irregular loads, high loads |
| **Ring footing** | Circular ring under cylindrical structure | Tanks, silos, towers |

---

## Bearing Capacity Theory

### Terzaghi's General Bearing Capacity Equation (1943)

For a **strip footing** (L >> B) with general shear failure:

**qu = c × Nc + q × Nq + 0.5 × γ × B × Nγ**

where:
- q = overburden pressure at foundation level = γ × Df (Df = depth of embedment)
- B = footing width
- γ = unit weight of soil below footing
- Nc, Nq, Nγ = dimensionless bearing capacity factors (function of φ')

```
BEARING CAPACITY FACTORS (selected values):

  φ'    Nc      Nq      Nγ
  0     5.14    1.00    0.00   ← undrained clay: qu = 5.14 × Su
  10    8.35    2.47    1.22
  20    14.8    6.40    5.39
  25    20.7    10.7    10.9
  30    30.1    18.4    22.4
  35    46.1    33.3    48.0
  40    75.3    64.2    109

  Undrained clay (φ = 0): qu = 5.14 × Su + γDf
  (first term from Nc = 5.14; second term = overburden)
```

### Three Failure Modes

```
THREE FAILURE MODES:

  GENERAL SHEAR                LOCAL SHEAR               PUNCHING
  (dense sand, stiff clay)     (medium density)           (loose sand, soft clay)

  Sharp peak then rapid        Gradual peak,              No defined peak;
  drop in load-displacement    less defined               continuous compression
  curve. Full mobilization     failure surface            below footing
  of failure surface.

  Use General: relative        Use Local: intermediate    Use Punching: ID < 35%
  density ID > 67%             density                    (Vesic's recommendation)
```

### Meyerhof/Hansen/Vesic Modifications

Terzaghi's formula is for strip footings. Real footings are square, circular, or rectangular, embedded at depth, and may be loaded at an angle:

**qu = c × Nc × Fcs × Fcd × Fci + q × Nq × Fqs × Fqd × Fqi + 0.5 × γ × B × Nγ × Fγs × Fγd × Fγi**

where F = correction factors:
- **s** = shape (square/circular footings have different Nc/Nq distribution)
- **d** = depth (deeper footings get shear resistance from soil on sides)
- **i** = inclination (inclined load reduces capacity)

Shape factors (Hansen):
- Square: Fcs = 1 + (Nq/Nc)(B/L), Fqs = 1 + (B/L)tanφ'
- Circle: same as square with B/L = 1

---

## Allowable Bearing Capacity

**qa = qu / FS**

Standard factors of safety:
- FS = 3.0 for permanent loads on shallow foundations (ASD)
- FS = 2.5 when settlement is checked separately and limited
- Lower FS may be acceptable with LRFD methods (resistance factors φ applied to qu)

**Typical allowable bearing capacities** (rough reference):
| Soil Type | qa (kPa) |
|-----------|---------|
| Soft clay (Su = 25 kPa) | ~40–60 |
| Stiff clay (Su = 100 kPa) | ~150–200 |
| Loose sand (N ≈ 10) | ~100–150 |
| Medium dense sand (N ≈ 25) | ~200–300 |
| Dense sand (N ≈ 40) | ~300–500 |
| Rock (RQD > 50%) | > 1000 |

---

## Settlement Analysis

### Immediate (Elastic) Settlement

Occurs as load is applied; in sands, essentially instantaneous:

**Si = qnet × B × (1 - ν²) / Es × If**

where:
- qnet = net applied bearing pressure
- Es = elastic (Young's) modulus of soil
- ν = Poisson's ratio (0.3 for sand, 0.5 for undrained clay)
- If = influence factor (depends on shape, rigidity, depth)

Elastic modulus correlations:
- Sand: Es ≈ (2 to 4) × N60 × 100 kPa (rough)
- Clay: Es ≈ (200 to 500) × Su (very rough)

Plate load test gives Es directly (but only for upper 1–2 plate widths).

### Consolidation Settlement

In clay, the primary settlement from consolidation (see 03-CONSOLIDATION.md):
Sc = Cc/(1+eo) × H × log(σ'f/σ'o)

where σ'f = initial effective stress + Boussinesq stress increase

### Total and Differential Settlement

Differential settlement (δ_diff = difference between two adjacent settlement points) governs structural damage:

| L/δ ratio | Condition | Impact |
|-----------|-----------|--------|
| > 1/150 | Structural distortion | Possible frame damage |
| > 1/300 | Serviceability limit | Cracking in cladding/partitions |
| > 1/500 | Sensitive structures | Damage to sensitive equipment, glass facades |

Typical allowable total settlements:
- Isolated footings on clay: 25–50 mm total, 20 mm differential
- Isolated footings on sand: 25 mm total, 18 mm differential
- Raft foundations: 50 mm total, 25 mm differential

---

## Mat (Raft) Foundations

A mat foundation distributes load over the entire building footprint. Use mats when:
- Soil is weak and individual footings would be too large
- Many column loads, irregular spacing, need distribution
- High column loads and tight differential settlement requirements
- Reduce bearing pressure to reduce consolidation settlement
- Basement slab serves as mat (buoyancy from water table helps)

### Rigid vs. Flexible Mat

**Rigid mat** (conventional analysis): Assumes mat is infinitely stiff; contact pressure distribution is linear (varies from one edge to other under eccentric load). Simple hand calculation.

**Flexible mat** (beam on elastic foundation / winkler model):
- Soil reaction modeled as series of springs: p = ks × w (contact pressure = subgrade modulus × settlement)
- Subgrade modulus ks (kN/m³): ks ≈ qa/Δ (from plate load test)
- Mat is flexible member; analyzed as beam/plate on spring supports
- More accurate than rigid analysis for large mats

**FEM analysis**: Full 2D/3D finite element analysis for important projects.

### Net Bearing Pressure and Compensated Foundations

For deep basements, the excavation relieves stress equal to the weight of excavated soil. The **net bearing pressure** = applied load - overburden removed:

qnet = Q/A - γ × Df

For a fully compensated foundation: qnet = 0 (load equals excavation weight). No net settlement. Common for deep basements in Mexico City and other soft ground cities.

---

## Eccentricity and Overturning

For footings with moments (from eccentric column loads or lateral forces), the effective footing dimensions are reduced:

**Effective width**: B' = B - 2e_B
**Effective length**: L' = L - 2e_L

where eccentricities: e_B = M_B/P, e_L = M_L/P

Requirement: eccentricity ≤ B/6 (kern of footing) to avoid tension at footing base (soil can't take tension).

---

## Decision Cheat Sheet

| Condition | Use | Notes |
|-----------|-----|-------|
| Single column, adequate soil | Isolated spread footing | Size for bearing + settlement |
| Bearing wall | Strip/continuous footing | Width from bearing capacity |
| Soft/weak soil, large loads | Mat foundation | Reduces bearing pressure |
| Deep basement | Net bearing / compensated | qnet = Q/A - γDf |
| Sand, short-term loading | Immediate settlement governs | Check elastic settlement |
| Clay, long-term | Consolidation settlement governs | Terzaghi time-rate analysis |
| Eccentric loads | Reduce to effective B', L' | Check e < B/6 for no tension |

---

## Common Confusion Points

**Bearing capacity failure is rare in modern design**: Most foundations are designed to have F ≥ 3 against bearing capacity failure. What actually controls most designs is settlement — the allowable bearing pressure is often set by settlement limits, not by qu/3.

**Terzaghi's equation assumes general shear failure**: For loose sands or soft clays, local or punching shear controls. Applying the general shear equation gives unconservative results. Use the local shear modification (Terzaghi: reduce c' by 2/3 and tanφ' by 2/3 for local shear) or the Vesic failure mode criterion.

**Immediate settlement is not total settlement**: Immediate elastic settlement occurs during construction. Consolidation settlement in clay occurs over years. Total settlement = Si + Sc + Ss. In soft clay, Sc >> Si.

**Subgrade modulus ks depends on footing size**: ks from a plate load test (small diameter plate) must be corrected for the actual footing size. ks decreases with footing size. Using the plate test value directly for a large mat overestimates spring stiffness.
