# Consolidation: Primary Settlement, Terzaghi 1D Theory, Time Rates, PVDs

## The Big Picture

When a saturated, low-permeability soil (clay, silt) is loaded, it cannot immediately expel its pore water. The load is temporarily carried by increased pore pressure. Over time, the excess pore pressure dissipates, the effective stress increases, and the soil skeleton compresses — this is consolidation. The settlement can be large (meters for soft clay) and slow (years to decades). Understanding both magnitude and time rate is essential for foundation design.

```
+------------------------------------------------------------------+
|               CONSOLIDATION — TWO DISTINCT PROBLEMS              |
+------------------------------------------------------------------+
|                                                                  |
|  PROBLEM 1: HOW MUCH will it settle?                            |
|  = consolidation magnitude                                       |
|  = governed by compressibility parameters (Cc, Cs)              |
|  = determined from oedometer (consolidation) test               |
|                                                                  |
|  PROBLEM 2: HOW LONG until it settles?                          |
|  = rate of consolidation                                         |
|  = governed by drainage length and permeability (Cv)            |
|  = Terzaghi's diffusion equation solution                        |
|                                                                  |
|  BOTH PROBLEMS needed for:                                       |
|  - Predicting total settlement (structural design)               |
|  - Predicting differential settlement (structural damage)        |
|  - Designing preloading schedules                                |
|  - Sizing prefabricated vertical drains                          |
|                                                                  |
+------------------------------------------------------------------+
```

---

## The Oedometer Test

The fundamental lab test for consolidation behavior: a thin (2–3 cm) sample confined laterally in a rigid ring, drained at top and bottom. Load applied in increments (typically doubled: 25, 50, 100, 200, 400 kPa...).

For each load increment, dial gauge records settlement vs. time (Terzaghi curve for each increment).

**Output from oedometer**:
- e vs. log σ'v curve (compression curve)
- Cv (coefficient of consolidation) from each load increment
- Preconsolidation pressure σ'p (Casagrande construction)

---

## The e - log σ' Curve

```
e (void ratio)
|
|  Virgin compression line (VCL)
|  (slope = Cc — compression index)
| *
|   *
|     *  ← Preconsolidation pressure σ'p (peak past stress)
|       *                                   ↓
|       |*  Recompression range            ---
|       |  * (slope = Cs — swelling index)  |
|       |    *                              Cc = Δe / Δ(log σ'v)
|       |      *                            typically 0.1–0.8
|       |    ↑  * ← Current stress σ'vo
|       | Cs/Cc ≈ 1/5 to 1/10
|       |
+─────────────────────────────── log σ'v
        σ'p  σ'vo

  OCR = σ'p / σ'vo
  OCR = 1: normally consolidated (NC)
  OCR > 1: overconsolidated (OC) — soil has experienced higher stress in past
```

**Overconsolidation causes**: Glacial loading, erosion of overlying material, past drying/desiccation, chemical cementation.

**OC soils are stiffer**: They have already been compressed; recompression uses Cs (much smaller than Cc). Major practical difference:
- NC clay: uses Cc (large settlement)
- OC clay, OC region: uses Cs (small settlement)
- If new stress exceeds σ'p: uses Cs to σ'p, then Cc beyond

---

## Settlement Magnitude Calculation

### Normally Consolidated Clay (σ'f > σ'p = σ'vo)

**Δe = Cc × log(σ'f / σ'vo)**

**Settlement**: Sc = (Cc / (1 + eo)) × H × log(σ'f / σ'vo)

### Overconsolidated Clay — Two Cases

**Case 1**: Stress remains in OC range (σ'f < σ'p):
Sc = (Cs / (1 + eo)) × H × log(σ'f / σ'vo)

**Case 2**: Stress crosses preconsolidation pressure (σ'f > σ'p):
Sc = (Cs / (1 + eo)) × H × log(σ'p / σ'vo) + (Cc / (1 + eo)) × H × log(σ'f / σ'p)

### Stress Increase with Depth

The applied stress σ'f at depth z below a loaded area decreases with depth. Two methods:
- **2:1 method** (simplified): stress spreads at 2V:1H → Δσ'v = Q / (B+z)(L+z)
- **Boussinesq elastic solution**: more accurate for flexible loads, uses influence charts

---

## Terzaghi's 1D Consolidation Theory

### The Governing Equation

For a saturated clay layer of thickness 2H (drained top and bottom), loaded at time t=0 by a uniform stress increase Δσ, Terzaghi derived the consolidation equation:

**∂u/∂t = Cv × (∂²u/∂z²)**

where:
- u = excess pore pressure (above hydrostatic) at depth z, time t
- Cv = coefficient of consolidation = k / (γw × mv)
- mv = volume compressibility = Δεv / Δσ'v = 1 / (1 + eo) × (Δe / Δσ'v)

This is the **diffusion equation** — mathematically identical to heat conduction. The excess pore pressure diffuses from the clay (undrained interior) to the drainage boundaries (where u = 0).

### Solution: Time Factor and Degree of Consolidation

**Time Factor**: Tv = Cv × t / Hdr²

where Hdr = drainage length:
- Single drainage (one boundary): Hdr = H (full layer thickness)
- Double drainage (two boundaries): Hdr = H/2

**Average Degree of Consolidation** U vs. Tv:

```
Tv        U (%)    Approximate formula
0         0
0.008     10%
0.031     20%      For U < 60%:   Tv = (π/4)(U/100)²
0.071     30%      For U ≥ 60%:   Tv = 1.781 - 0.933 × log(100-U%)
0.126     40%
0.196     50%
0.287     60%
0.403     70%
0.567     80%
0.848     90%
∞        100%
```

**Solving for time**:
Given Sc (total settlement), want U = Sc_current / Sc_total → find Tv → solve t = Tv × Hdr² / Cv

### Example Calculation

10 m thick NC clay, double drainage, Cv = 2 m²/yr, total settlement = 300 mm.
Q: How long to achieve 150 mm settlement (U = 50%)?

Hdr = 10/2 = 5 m
Tv at U = 50% = 0.196
t = 0.196 × 5² / 2 = 0.196 × 25 / 2 = **2.45 years**

---

## Measuring Cv from Oedometer Test

Two methods from the settlement vs. time curve for each load increment:

### Taylor's Method (√t fitting)
1. Plot settlement vs. √t
2. Early part is linear → draw line through origin
3. A line with 15% greater slope intersects the curve at t90
4. Tv at 90% consolidation = 0.848
5. Cv = 0.848 × Hdr² / t90

### Casagrande's Method (log t fitting)
1. Plot settlement vs. log t
2. Find t50 at the inflection point (intersection of two tangents)
3. Tv at 50% = 0.197
4. Cv = 0.197 × Hdr² / t50

Cv typically ranges from 0.1 to 100 m²/yr for soft to stiff clays.

---

## Piezometers and Field Monitoring

In the field, consolidation is tracked by:
- **Piezometers** (Casagrande, vibrating wire): measure pore pressure at specific depths
- **Settlement plates**: measure surface settlement vs. time
- **Settlement monuments**: survey points on fill surface

Comparing theoretical Terzaghi curves to measured pore pressure dissipation:
- Faster dissipation than predicted: better drainage than assumed (sand layers, fissures)
- Slower dissipation: smear from driving, lower k than assumed

---

## Secondary Consolidation (Creep)

After primary consolidation (excess pore pressure fully dissipated), soil continues to compress under constant effective stress — this is secondary consolidation or creep.

**Cα** = secondary compression index = Δe / Δ(log t)

Settlement rate: Ss = Cα / (1 + ep) × H × log(t2/t1)

where ep = void ratio at end of primary consolidation.

Cα/Cc ≈ 0.04 ± 0.01 for inorganic clays
Cα/Cc ≈ 0.05 ± 0.01 for organic clays
Cα/Cc ≈ 0.075 ± 0.01 for peats

Secondary consolidation is significant for:
- Organic soils (Cα/Cc can reach 0.1)
- Long-term settlements in soft clay (decades)
- Buildings on reclaimed land

---

## Accelerating Consolidation

### Surcharge Loading

Apply a temporary surcharge (extra fill) beyond the final design load:
- Creates higher Δσ'v → faster consolidation
- Primary consolidation completes sooner
- Secondary consolidation time "credit" can be used
- Remove surcharge when required degree of consolidation achieved

### Prefabricated Vertical Drains (PVDs)

PVDs (band drains, wick drains) installed in a grid pattern to add radial drainage paths, dramatically reducing drainage path length.

```
PVD INSTALLATION PATTERN:

  Plan view (square or triangular pattern):

  ○  ○  ○  ○  ○     ← each ○ = PVD (typically at 1-2m spacing)
  ○  ○  ○  ○  ○
  ○  ○  ○  ○  ○
  ○  ○  ○  ○  ○

  PVD typically: 100mm wide × 3-5mm thick band drain
  Depth: 10-30m depending on weak layer thickness

  Barron's radial consolidation theory:
  Tr = Cv-radial × t / de²
  where de = 1.13s (square pattern) or 1.05s (triangular)
              s = drain spacing

  With PVDs: drainage path = half drain spacing (1-2m)
  vs. without PVDs: drainage path = half clay layer (5-15m)
  Time to 90% consolidation reduced by factor of (Hdr/re)²
  → From years to months
```

---

## Decision Cheat Sheet

| Problem | Formula | Key Parameters |
|---------|---------|---------------|
| NC clay settlement | Sc = Cc/(1+eo) × H × log(σ'f/σ'vo) | Cc from oedometer; check stress range |
| OC clay (OC range) | Sc = Cs/(1+eo) × H × log(σ'f/σ'vo) | Use Cs not Cc; confirm σ'f < σ'p |
| OC crossing σ'p | Two-part formula (OC range + NC range) | σ'p from Casagrande construction |
| Time to achieve U% | t = Tv × Hdr² / Cv | Tv from chart; Hdr depends on drainage |
| Is primary or secondary important? | Compare tp (primary) to structure life | Secondary matters for organic soils, long service life |
| Reduce time by PVDs | Radial consolidation theory | Barron; spacing controls Hdr and time |

---

## Common Confusion Points

**Cc is a line, not a constant**: Cc is the slope of the e-log σ' curve in the NC region. For most clays, Cc is reasonably constant over the stress range of interest. For very soft clays and organic soils, Cc can change with stress level.

**Hdr squared in time formula**: The time to achieve a given U is proportional to Hdr². Doubling the drainage length → 4× longer. This is why PVDs are so effective: reducing Hdr from 10m to 1m reduces time by factor 100.

**Cv from oedometer may not equal field Cv**: Lab Cv is measured on small, remolded samples. Field Cv can be 2–10× higher due to macrofabric (thin sand seams, fissures) that aren't captured in lab samples. Use piezometer-backfitted Cv for important projects.

**Primary vs. secondary consolidation boundary**: Primary consolidation ends when excess pore pressure reaches zero. Secondary consolidation begins at that point. In practice, for thick layers, primary consolidation may take so long that secondary is negligible during the structure's design life.
