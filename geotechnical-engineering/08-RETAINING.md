# Retaining Structures: Earth Pressure, Wall Types, MSE, Seismic

## The Big Picture

Retaining structures hold back a mass of soil (or other material) against gravity and lateral loads. The driving force is lateral earth pressure from the retained soil. The resisting mechanism depends on the wall type: gravity (self-weight), cantilever (structural moment), or reinforced mass (internal reinforcement + friction).

```
+------------------------------------------------------------------+
|               LATERAL EARTH PRESSURE — MASTER CONCEPT          |
+------------------------------------------------------------------+
|                                                                  |
|  AT-REST (K0): No wall movement                                 |
|  Ko = σ'h / σ'v = 1 - sinφ' (Jaky's formula, NC)              |
|                                                                  |
|  ACTIVE (Ka): Wall moves away from soil                         |
|  → Soil expands toward wall                                     |
|  → Minimum lateral pressure for equilibrium                     |
|  Small movement needed: δ/H ≈ 0.001–0.005 for sand             |
|                                                                  |
|  PASSIVE (Kp): Wall moves into soil                             |
|  → Soil compressed by wall                                      |
|  → Maximum lateral resistance                                   |
|  Large movement needed: δ/H ≈ 0.01–0.05 for sand               |
|                                                                  |
|  PRESSURE DIAGRAM (cohesionless soil, no water):               |
|                                                                  |
|  ACTIVE:        PASSIVE:         AT REST:                       |
|  ───┐           ───┐             ───┐                          |
|     │              │  much           │  between                 |
|     │  σ'h = Ka×γz │  larger         │  active and             |
|     │              │                 │  passive                 |
|     ▼              ▼                 ▼                          |
|  Pressure          Pressure          Pressure                   |
|  triangular        triangular        triangular                 |
|  (increases        (larger)                                     |
|  with depth)                                                    |
|                                                                  |
|  Ka << Ko << Kp (typically Ka ≈ 0.3, Ko ≈ 0.5, Kp ≈ 3.0)     |
|                                                                  |
+------------------------------------------------------------------+
```

---

## Earth Pressure Theories

### Rankine Theory (1857)

Assumes smooth wall (no wall friction), horizontal backfill, and that the failure surface forms at angle (45 + φ'/2) to horizontal.

**Active earth pressure coefficient**:
**Ka = tan²(45° - φ'/2) = (1 - sinφ')/(1 + sinφ')**

**Passive earth pressure coefficient**:
**Kp = tan²(45° + φ'/2) = (1 + sinφ')/(1 - sinφ') = 1/Ka**

Active pressure distribution (cohesionless backfill):
σ'a = Ka × σ'v = Ka × γz

Active pressure distribution (c-φ soil):
σ'a = Ka × γz - 2c√Ka

Note: Tension crack zone at surface to depth: zt = 2c / (γ√Ka). Don't include tension zone in design (fill with water in worst case).

### Coulomb Theory (1776)

More general: includes wall friction (δ), sloped backfill (β), and inclined wall back (α):

**Ka = sin²(α + φ') / {sin²α × sin(α - δ) × [1 + √(sin(φ'+δ)sin(φ'-β) / sin(α-δ)sin(α+β))]²}**

Coulomb gives higher Ka than Rankine when wall friction is present, but passive Ka by Coulomb can be dangerously unconservative for curved failure surfaces.

Use Rankine for active pressure (conservative, simpler). Use log-spiral solutions or tables for passive (Coulomb Kp is too high for high δ).

---

## Wall Types

### Gravity Walls

Depend entirely on self-weight for stability. No tension in the wall body.

Types: rubble masonry, unreinforced concrete, gabion baskets.

**Design checks**:
1. **Overturning**: Mo/Mr ≥ factor of safety (moments about toe)
   FS_OT ≥ 1.5 (seismic), ≥ 2.0 (static)
2. **Sliding**: FS_sliding = Fresist / Fdrive ≥ 1.5
   Fresist = (ΣV) × tanδb + Passove + Cohesion on base
3. **Bearing capacity**: max contact pressure ≤ allowable
   e_eccentricity = B/2 - ΣM/ΣV ≤ B/6 (no tension on base)

### Cantilever Walls (T-Wall, L-Wall)

Thin stem + base slab. Reinforced concrete. Stem acts as vertical cantilever from base. Base slab mobilizes weight of soil above base as surcharge:

```
CANTILEVER WALL GEOMETRY:

  ───────────────
  ↑              ↓ stem thickness
  H  ← stem     ← footing extends into backfill
  ↓              (heel side) and toward face (toe side)
  ──────────────────────────────────
  ← toe →       ← heel →

  Critical section: bending moment at base of stem
  M = Ka × γ × H³ / 6  (active pressure triangle, no surcharge)

  Footing design:
  Heel: moment from soil weight above vs. upward soil reaction
  Toe: moment from soil reaction vs. weight of concrete above
```

Shear key under footing: increases sliding resistance by developing passive resistance in front of key.

### Sheet Pile Walls

Interlocking sections (steel, vinyl, precast concrete) driven or vibrated into ground.

**Cantilevered sheet pile**: No support at top. Depends on passive resistance in front of embedded section for stability. Limited to heights ≤ 3–5 m.

```
CANTILEVERED SHEET PILE — NET PRESSURE DIAGRAM:

  Above dredge line:   Active pressure from back (→)
  Below dredge line:   Net effect of active (back) and passive (front)
                       Initially: passive > active (resists wall)
                       At some depth: reversal point

  Active behind: pa = Ka × γ × z
  Passive front (below dredge): pp = Kp × γ × (z - zdredge)
  Net horizontal pressure reverses at depth "d"

  Free earth method: simple approach, conservative
  Fixed earth method: assumes wall embedded enough to "fix" at base
```

**Anchored sheet pile**: Tie-rod or strand anchor connected to deadman anchor or ground anchor at top (or intermediate level). Greatly reduces required embedment depth and wall moments.

**Wales and tie-rods**: Wales (horizontal W-sections) distribute anchor forces along wall. Tie-rods extend to anchors at 45° angle to avoid active zone. Ground anchors (drilled and grouted) used where deadman isn't feasible.

### Soldier Pile and Lagging

Driven or drilled H-piles at regular spacing (1.5–3.0 m); timber lagging between piles retains soil.

Used in: urban excavations; where vibration from sheet pile driving is prohibited.

Advantage: flexible, can be installed in rock; lagging inspectable.
Disadvantage: lagging joints leak groundwater; not water-tight.

Tiebacks (prestressed ground anchors): drill through wall, grout in competent soil/rock behind, prestress to limit wall deflection.

---

## Mechanically Stabilized Earth (MSE) Walls

MSE walls use **geosynthetics** (geotextiles, geogrids) or metallic strips embedded in compacted granular fill to create a reinforced soil mass that acts together as a gravity structure.

### Mechanism

Reinforcement mobilizes soil friction to develop tensile resistance:
- **Geogrid**: stiff polymer grid; soil interlocks through apertures
- **Geotextile**: woven or nonwoven fabric; friction with soil
- **Metallic strips**: galvanized steel ribbed strips; friction and passive bearing

```
MSE WALL CROSS-SECTION:

  Concrete face panels (precast, modular)
  or modular block system
  │
  │  ←── Geogrid layers at regular vertical spacing (0.3–0.6 m)
  │←──── Geogrid extends into fill (L = 0.7H minimum)
  │
  │  Compacted granular fill (SW or GW preferred)
  │
  ──────────────────────────────────── Foundation

  INTERNAL STABILITY: Reinf. must not rupture or pullout
  EXTERNAL STABILITY: Reinforced mass = gravity wall
    Check overturning, sliding, bearing, global stability
```

### External Stability Checks (same as gravity wall)

The entire reinforced zone acts as a gravity wall. Check:
- Overturning about toe
- Sliding on base
- Bearing capacity of foundation

### Internal Stability

For each reinforcement layer at depth z:
1. **Tensile force per unit width**: T = Ka × (γz + q) × Sv (Sv = vertical reinforcement spacing)
2. **Pullout resistance**: F* × α × σ'v × 2Le (F* = pullout friction, Le = embedment behind failure surface)
3. **Rupture capacity**: TULT / FS ≥ T (use long-term tensile strength after creep reduction)

MSE walls are commonly 15% cheaper than cast-in-place cantilever walls for walls > 4m height.

---

## Drainage

All retaining walls must have adequate drainage. Hydrostatic pressure can easily double or triple total wall load:

```
EFFECT OF WATER ON WALL LOAD:

  WITHOUT WATER:           WITH SATURATED BACKFILL:
  Active pressure          Active pressure
  = Ka × γ × H²/2         = Ka × γ' × H²/2   (buoyant γ')
  (total horizontal force) + γw × H²/2         (hydrostatic)

  For H = 6m, Ka = 0.33, γ = 20, γ' = 10, γw = 10:
  Dry:  0.33 × 20 × 36/2 = 120 kN/m
  Wet:  0.33 × 10 × 36/2 + 10 × 36/2 = 60 + 180 = 240 kN/m
  → 2× increase in force!
```

Drainage solutions:
- **Weep holes**: 100–150 mm diameter holes at bottom of wall, with filter aggregate
- **Geocomposite drainage board** (Mirafi Geodrain, etc.): prefabricated drain mat at back of wall face, connected to collector drain at base
- **Filter criteria** (Terzaghi): grain sizes must prevent piping while allowing water through

---

## Seismic Earth Pressure: Mononobe-Okabe (MO)

During earthquake, additional dynamic earth pressure increment must be added:

**Mononobe-Okabe active earth pressure coefficient**:

KAE = sin²(α + φ' - θ) / {sinα × sin(α - δ - θ) × [1 + √(sin(φ'+δ)sin(φ'-β-θ)/sin(α-δ-θ)sin(α+β))]²}

where θ = arctan(kh / (1 - kv)), kh = horizontal seismic coefficient, kv = vertical.

**Total active force**: PAE = 0.5 × KAE × γ × H²

Approximately: PAE ≈ PA + ΔPAE (static active + dynamic increment)

ΔPAE ≈ 0.375 × kh × γ × H² (Seed and Whitman simplification)

Applied at 0.6H from base (dynamic increment concentrates higher than static).

---

## Decision Cheat Sheet

| Wall Height | Situation | Preferred Wall Type |
|------------|-----------|-------------------|
| < 2 m | Low wall, good soil | Gravity (concrete or masonry) |
| 2–5 m | General purpose | Cantilever T-wall (CIP) or MSE |
| 3–8 m | Budget-conscious, granular backfill | MSE wall |
| 4–10 m | Tight footprint, urban, braced | Sheet pile (cantilevered or anchored) |
| > 6 m | Any, phased construction | MSE or tieback soldier pile/sheet pile |
| Vibration-sensitive area | Urban excavation | Soldier pile and lagging |
| Seismic zone, H > 5 m | Bridge abutment | MSE or CIP with MO seismic check |

---

## Common Confusion Points

**Active failure requires wall movement**: Active earth pressure (Ka) develops only when the wall moves away from the soil by a small amount (0.1–0.5% of H for dense sand). For rigid structures (massive dams, basements with restrained floor slabs), use Ko not Ka — the soil never fully mobilizes active failure.

**Passive resistance requires large movement**: Mobilizing full passive Kp requires 5–10× more displacement than mobilizing Ka. Don't rely on passive resistance in design unless you can ensure the required deformation is acceptable.

**Water doubles wall load**: Many wall failures are drainage failures. Properly designed and maintained drainage is not optional — it is as critical as the structural design.

**MSE walls need granular fill**: Cohesive backfill in MSE walls causes long-term creep, loss of reinforcement pullout, and poor drainage. FHWA specifications require low-plasticity fill (PI < 20, ideally < 6) for metallic strips, and PI < 20 for geogrids/geotextiles.
