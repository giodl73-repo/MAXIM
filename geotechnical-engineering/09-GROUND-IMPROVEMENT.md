# Ground Improvement: Preloading, Stone Columns, Grouting, Deep Soil Mixing

## The Big Picture

When the natural ground is inadequate for the proposed structure, you can either: (a) avoid it (deep foundations), (b) improve it in place, or (c) replace it. Ground improvement covers option (b) — densifying, strengthening, or modifying the in-situ soil to make it suitable for shallow foundations, embankments, or other uses.

```
+------------------------------------------------------------------+
|              GROUND IMPROVEMENT — SELECTION MAP                 |
+------------------------------------------------------------------+
|                                                                  |
|  PROBLEM: SOFT/WEAK SOIL         GROUND IMPROVEMENT OPTIONS:   |
|                                                                  |
|  Compressible (high e, soft clay)  → Preloading + PVDs          |
|                                    → Surcharge + time           |
|                                                                  |
|  Loose granular (sand, gravel)     → Dynamic compaction         |
|                                    → Vibro-compaction           |
|                                    → Compaction grouting        |
|                                                                  |
|  Soft clay needing quick strength → Stone columns (composite)   |
|                                    → Lime/cement columns (DSM)  |
|                                                                  |
|  Permeable (needs waterproofing)  → Permeation grouting         |
|                                    → Jet grouting               |
|                                    → Ground freezing            |
|                                                                  |
|  Liquefiable sand                 → Vibro-densification         |
|                                    → Stone columns (drainage)   |
|                                    → DSM (containment)          |
|                                                                  |
|  SELECTION CRITERIA:                                             |
|  Soil type + grain size + permeability + accessibility +        |
|  load requirement + settlement tolerance + cost + time          |
|                                                                  |
+------------------------------------------------------------------+
```

---

## Preloading with Prefabricated Vertical Drains (PVDs)

### Concept

Apply fill (surcharge) load to accelerate consolidation of a soft clay layer. Simultaneously install PVDs to dramatically shorten drainage paths and thus reduce the time required.

```
PRELOADING SEQUENCE:

  TIME ──────────────────────────────────────────────────→

  Phase 1: Install PVDs (install through soft layer)
            ↓
  Phase 2: Stage fill placement (to avoid slope failure!)
            ↓↓
  Phase 3: Monitor piezometers and settlement plates
            ↓↓↓
  Phase 4: Add surcharge beyond design load if needed
            ↓↓↓↓
  Phase 5: When target consolidation achieved: remove surcharge
            ↓↓↓ (settlement stops / greatly reduced)
  Phase 6: Build structure on improved ground

  Without PVDs: years to decades for thick clay
  With PVDs:    months to a year (drainage path = 1-2m vs. 5-15m)
```

### PVD Design

Barron's theory for radial consolidation:
- Effective diameter of drainage cylinder: de = 1.13s (square) or 1.05s (triangular pattern)
- Time factor for radial: Tr = Cv-radial × t / de²
- Average degree of consolidation from radial drainage: Ur

Combined vertical + radial consolidation:
(1 - U) = (1 - Uv) × (1 - Ur)

**Installation effects**:
- **Mandrel-induced smear zone**: disturbed, remolded zone around PVD (diameter = 2–5 × mandrel)
- Smear reduces permeability in smear zone → reduces PVD effectiveness
- Design must account for smear using reduced permeability ratio kh/ks ≈ 2–10

### Surcharge Design

Total surcharge height = design load + surcharge increment
- Design fill height hf → structural load on completed embankment
- Surcharge hs = additional fill to push consolidation into NC range and achieve faster completion

**Removal timing**: Remove surcharge when:
Settlement rate < threshold (typically < 10–20 mm/month)
OR: consolidation monitoring shows target degree of consolidation achieved (typically 90–95%)

---

## Dynamic Compaction

Large (typically 10–40 tonne) steel or concrete tampers dropped from heights of 15–40 m using cranes. The impact energy compacts loose granular soils.

**Effective depth of improvement**:
D (m) ≈ 0.5 to 0.7 × √(W × H)

where W = tamper weight (tonnes), H = drop height (m)

For W = 20 tonnes, H = 20 m: D ≈ 0.6√400 = 12 m improvement depth.

**Energy per blow**: E = W × H (tonne-m)
**Total energy per area**: sum of all passes × E / grid spacing²

**Grid pattern**: Primary grid (large spacing, penetrate deep), secondary grid (infill between primary), ironing pass (closely spaced, low drops to improve upper zone).

**Effectiveness**:
- Best for: clean sands and gravels (SP, GP), artificial fills, MSW (municipal solid waste)
- Marginal for: silty sands (SM, SC) — drainage insufficient for rapid pore pressure dissipation
- Not effective for: saturated soft clays — energy dissipates in pore water, minimal improvement

Verification: CPT/SPT before and after; require N60 increase of specified amount at specified depths.

---

## Vibro-Compaction

A vibrating torpedo-shaped probe (vibroflot) is inserted into granular soil. The vibration causes particles to rearrange into denser packing.

```
VIBRO-COMPACTION PROCESS:

  1. Vibroflot lowered into granular soil under vibration + water jet
     (water loosens soil and carries cuttings to surface)
  2. Vibroflot reaches target depth
  3. Slow withdrawal with vibration at specified withdrawal rate
  4. Additional granular material (quartz sand or gravel) fed into annular space
  5. Vibroflot works back down in lifts to densify each zone

  Spacing: 2.0–3.5 m triangular or square pattern
  Effective radius from each probe: 1.5–2.5 m (depends on soil and energy)

  AFTER TREATMENT:
  SPT N-value and CPT qc increase significantly
  Settlement potential reduced 50–70%
  Liquefaction resistance improved
```

**Effectiveness**: Only for granular soils with limited fines (< 15% passing #200). When fines increase, drainage is impeded, vibration energy cannot densify, and vibro-replacement (stone columns) is needed instead.

---

## Stone Columns (Vibro-Replacement)

In soft clayey soils, vibro-compaction doesn't work. Instead, a vibroflot creates a hole that is backfilled with crushed stone or gravel. The stone is compacted radially by the vibrating probe to form a stiff column.

### Mechanism

Stone columns work by **composite action**: the stiff stone column and surrounding soft clay share the applied load. The column carries load in end bearing and skin friction; the clay carries a reduced share.

The column can also serve as a **drainage path** for the clay, accelerating consolidation (PVD function).

### Priebe Design Method

The area replacement ratio: Ac/A = πDc²/(4s²) (for triangular grid: A = 0.866s²)

Improvement factor n (ratio of improved settlement to unimproved):
n is a function of area ratio and stiffness ratio (E_column/E_clay)

Typical improvement: settlement reduced to 30–50% of unimproved value.

**Settlement of composite:** S_improved ≈ S_unimproved / n_Priebe

**Stability of embankment on stone columns**: check unit cell stability; provide granular load transfer platform (LTP) above columns to distribute load and prevent punching.

---

## Grouting Methods

### Permeation Grouting

Inject low-viscosity grout (cement slurry, sodium silicate, or acrylamide) into soil pores without disrupting the soil structure.

Requires: clean, coarse-grained soil (gravel, coarse to medium sand)
Criterion: groutability N = D15 soil / D85 grout > 24 (Marsh criterion for particulate grouts)

**Portland cement grout**: effective for gravels and coarse sands; permanent; strong
**Sodium silicate grout**: finer soils; reacts with calcium chloride or hardener; moderate strength
**Chemical grouts** (acrylamide, acrylate): very fine soils; high capital cost; health concerns

Application: pre-treatment for tunnels, temporary or permanent cutoff walls, foundation underpinning.

### Compaction Grouting

Low-mobility, stiff mortar-consistency grout (slump < 75 mm) injected under pressure. Grout does not penetrate pores — it displaces and densifies surrounding soil.

```
COMPACTION GROUTING:

  Grout pipe installed in injection zone
  Thick grout pumped at high pressure
  Grout forms a bulb that expands radially
  → Displaces and densifies surrounding soil
  → Void ratio decreases
  → Settlement reduced; bearing capacity increases

  Uses:
  - Sinkholes and karst areas (fill and compact)
  - Settlement remediation under existing structures
  - Near-surface densification where dynamic compaction
    would cause unacceptable vibration
  - Correction of differential settlement
```

### Jet Grouting

High-velocity cement grout jets (300–700 bar) erode and mix in-situ soil. Creates cemented soil columns of 0.3–2+ meters diameter depending on system.

**Systems**:
- **Single fluid** (S): grout jet only; small column (0.3–0.6 m); stiffest product
- **Double fluid** (D): grout jet + air shroud; medium column (0.6–1.0 m); less grout
- **Triple fluid** (T): water jet erodes, air shroud, then grout injection; large column (1.0–2.0 m); weakest, most consistent

**Applications**:
- Underpinning existing foundations (columns below existing footing)
- Excavation support (columns + tie-rods = secant or tangent wall)
- Cutoff walls (overlapping columns, any soil)
- Foundation improvement where access limits driven piles

Quality control: core samples for UCS testing; typical strength 1–10 MPa; coefficient of variation high.

---

## Deep Soil Mixing (DSM)

Cement slurry is injected and mechanically mixed in-situ using hollow-stem augers with mixing paddles. Creates columns or panels of cemented soil.

```
DSM APPLICATIONS:

  Columns: individual cemented columns
  at specified grid spacing
  └─ Embankment support
  └─ Liquefaction mitigation (reduce seismically-induced settlement)
  └─ Support for lightly loaded structures

  Panels: rows of columns forming wall elements
  └─ Excavation support
  └─ Containment of contaminated soils
  └─ Seismic mitigation walls (reduce lateral spreading)

  Mass treatment: columns overlap everywhere
  └─ Bridge approach fill support
  └─ Settlement reduction under fills
```

**Strength**: Unconfined compressive strength of mixed soil:
- Sandy soils: qu = 0.5–5.0 MPa
- Soft clays: qu = 0.1–1.5 MPa (variable; depends on organic content)
- High organic content: poor cementation (< 50 kPa possible for peat)

**Design**: Column group acts as composite material; overall stiffness used for settlement calculation; check individual column bearing capacity.

---

## Ground Freezing

Temporary ground stabilization by circulating refrigerant (brine) or liquid nitrogen through freeze pipes installed in the ground. Water in voids freezes → frozen soil is strong and impermeable.

**Uses**:
- Tunnel excavation through water-bearing ground
- Shaft sinking
- Access to contaminated soils
- Emergency repair of leaks in existing tunnels

**Systems**:
- **Brine circulation** (-20 to -35°C): slower (weeks to develop), energy efficient for long operations
- **Liquid nitrogen** (-196°C): rapid freeze (hours to days), expensive, short duration

**Design considerations**:
- Frost heave: freezing expands water → uplift forces on structures
- Thaw settlement: on thawing, improved ground may be weaker than original
- Geometry: freeze pipes must be closely enough spaced to ensure closure (overlap of freeze zones)

---

## Liquefaction Mitigation

Saturated, loose sands under cyclic loading (earthquake) can liquefy — pore pressure equals total stress, effective stress → 0, soil behaves like liquid.

Mitigation strategies:

| Strategy | Mechanism | Methods |
|---------|-----------|---------|
| **Densification** | Increase relative density Dr | Vibro-compaction, dynamic compaction |
| **Drainage** | Prevent pore pressure buildup | Stone columns, gravel drains |
| **Solidification** | Bind particles together | Deep soil mixing, grouting |
| **Containment** | Limit lateral spreading | DSM walls at perimeter of critical area |

**Evaluation**: Simplified Liquefaction Triggering Procedure (Seed-Idriss-Youd):
- CSR (Cyclic Stress Ratio) = 0.65 × (σv/σ'v) × amax/g × rd (demand)
- CRR (Cyclic Resistance Ratio) from (N1)60 or qc1N (capacity)
- FS = CRR/CSR → target FS ≥ 1.2–1.3 post-improvement

**Post-improvement verification**: CPT before and after; require (N1)60 or qc1N to exceed threshold value.

---

## Decision Cheat Sheet

| Problem | Soil Type | Best Method | Alternative |
|---------|-----------|------------|------------|
| Soft clay, large area, time available | Saturated clay | Preloading + PVDs | DSM columns |
| Loose sand, large area, vibration OK | Clean sand/gravel | Vibro-compaction | Dynamic compaction |
| Soft clay, immediate strength needed | Soft clay | Stone columns + LTP | DSM columns |
| Underpinning existing structure | Any | Compaction grouting or jet grouting | Micropiles |
| Excavation support in any soil | Any | Jet grouting or DSM panels | Sheet pile |
| Liquefiable sand, earthquake zone | Loose sand | Vibro-densification | Stone columns + drainage |
| Contaminated zone, no excavation | Any | Ground freezing (temporary) | DSM containment |
| Deep access tunnel (waterlogged) | Sandy/gravelly | Ground freezing | Jet grouting cutoff |

---

## Common Confusion Points

**Preloading without PVDs is very slow**: Doubling the drainage path quadruples the time required (Terzaghi time-rate). A 10 m thick clay layer with no drainage from below: Hdr = 10 m. With PVDs at 1.5 m spacing (de ≈ 1.7 m): Hdr ≈ 0.85 m. Time ratio: (10/0.85)² ≈ 140× faster. PVDs are almost always worth the cost for thick soft clay.

**Stone columns in soft clay do not densify the clay**: Stone columns work by load sharing (stiff column carries most load) and drainage acceleration. The clay itself is not densified. The column provides stiffness; the clay consolidates over time. Settlement is reduced and time to settlement is shortened, but the clay still consolidates.

**Jet grouting quality is highly variable**: The same injection pressure and withdrawal rate will produce very different column diameters in different soils. Core sampling and pre-production trials are essential. Design strengths must use lower-bound values from production testing, not idealized values.

**DSM is poor in highly organic soils**: Organic content (peat, organic clay) reacts with and consumes cement. High cement factors are required but results are still variable and often low-strength. Alternative: displacement columns or surcharge on geosynthetic platform.
