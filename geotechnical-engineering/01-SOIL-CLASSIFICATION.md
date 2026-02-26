# Soil Classification: USCS, Atterberg Limits, Sieve Analysis

## The Big Picture

Classifying soil is the first step in predicting its engineering behavior. Two systems dominate: the **Unified Soil Classification System (USCS)**, used for most geotechnical work, and the **AASHTO** system, used for road subgrade design. Classification tells you: how strong is this material likely to be? How much will it settle? Will it shrink and swell? Is it susceptible to frost heave?

```
+------------------------------------------------------------------+
|              SOIL CLASSIFICATION — DECISION FLOW                 |
+------------------------------------------------------------------+
|                                                                  |
|  START: Collect soil sample                                      |
|                    |                                             |
|                    v                                             |
|         Is soil highly organic? (dark, fibrous, odor)           |
|         YES → Pt (Peat) — special treatment required            |
|         NO  ↓                                                    |
|                    v                                             |
|         What fraction passes #200 sieve?                        |
|         < 50% fines → COARSE-GRAINED SOIL                       |
|         > 50% fines → FINE-GRAINED SOIL                         |
|                    |                     |                       |
|                    v                     v                       |
|          COARSE: gravel or sand  FINE: silt or clay             |
|          based on > #4 sieve?    based on Atterberg limits       |
|          G vs. S based on >50%   and position on A-line         |
|          retained on #4          (Casagrande plasticity chart)  |
|                    |                     |                       |
|                    v                     v                       |
|          Quality modifier: W, P, M, C   Descriptor: M, C, O     |
|          based on gradation (Cu, Cc)     H vs. L from LL=50      |
|          or Atterberg limits                                     |
|                                                                  |
+------------------------------------------------------------------+
```

---

## Sieve Analysis

### The Sieve Stack

Particle size distribution is determined by passing dry soil through a stack of progressively finer sieves:

```
STANDARD SIEVE STACK (coarse to fine):
  3"   (75 mm)   — cobbles vs. coarse gravel
  ¾"   (19 mm)
  #4   (4.75 mm) — gravel vs. sand boundary
  #10  (2.00 mm)
  #20  (0.85 mm)
  #40  (0.425 mm)
  #60  (0.250 mm)
  #100 (0.150 mm)
  #200 (0.075 mm) — sand vs. fines (silt/clay) boundary

  Particles passing #200: silt and clay
  (too fine for sieve — use hydrometer analysis)
```

### Gradation Parameters

From the particle-size distribution curve (% passing vs. log grain size):

**D10, D30, D60**: particle sizes at 10%, 30%, 60% passing

**Coefficient of Uniformity** (Cu = D60/D10):
- Cu < 4: uniform (gap-graded or poorly graded)
- Cu ≥ 4 (gravel) or ≥ 6 (sand): well-graded

**Coefficient of Curvature** (Cc = D30² / (D10 × D60)):
- 1 ≤ Cc ≤ 3: well-graded

Well-graded = wide range of particle sizes, good interlocking, low void ratio, good bearing.
Poorly graded = narrow range, looser packing, higher void ratio.

---

## Atterberg Limits

Fine-grained soils (silts and clays) change behavior dramatically with water content. The Atterberg limits define the water content boundaries between behavioral states.

```
+------------------------------------------------------------------+
|                    ATTERBERG LIMITS                              |
+------------------------------------------------------------------+
|                                                                  |
|  SL (shrinkage limit)    PL (plastic limit)    LL (liquid limit) |
|        |                       |                       |         |
|        v                       v                       v         |
|  ------+--------+--------------+-------+--------------+------  |
|  SOLID |  SEMI- |   SEMI-SOLID |       |   PLASTIC    |LIQUID  |
|        | SOLID  |              |       |   STATE      |STATE   |
|  Soil  |        |              |       |              |        |
|  rigid,|        |Soil deforms  |       |Soil deforms  |Soil    |
|  non-  |        |but doesn't   |       |like plasticine|flows  |
|  plastic        |spring back   |       |              |        |
|  ------+--------+--------------+-------+--------------+------  |
|                                                                  |
|  Increasing water content →                                     |
|                                                                  |
+------------------------------------------------------------------+
```

### Liquid Limit (LL)

The LL is the water content at which soil transitions from plastic to liquid behavior. Two test methods:

**Casagrande cup method** (ASTM D4318): Soil is placed in a brass cup; a groove is cut through the center. The cup is dropped from 1 cm height. LL = water content at which 25 blows close the groove by 13 mm.

**Fall cone method** (BS 1377): A cone of defined weight is released onto the soil surface. LL = water content at which 80g cone penetrates exactly 20mm.

### Plastic Limit (PL)

PL = water content at which soil can no longer be rolled into a 3 mm thread without crumbling. Below PL, soil is semi-solid. Tested by hand-rolling technique — subjective but reproducible with practice.

### Plasticity Index (PI)

**PI = LL - PL**

PI quantifies the range of water content over which the soil is plastic. PI is the most important single number for engineering prediction:

| PI | Description | Typical Behavior |
|----|-------------|-----------------|
| 0 | Non-plastic | Sand or non-plastic silt |
| 1–5 | Slightly plastic | Low-plasticity silt |
| 5–15 | Medium plasticity | ML, CL soils |
| 15–35 | High plasticity | CH clay |
| > 35 | Very high | Expansive clays, montmorillonite |

---

## USCS Classification (ASTM D2487)

### Coarse-Grained Soils (< 50% passing #200)

```
COARSE-GRAINED CLASSIFICATION TREE:

  < 50% passing #200 → COARSE
              |
              v
  > 50% retained on #4 → GRAVEL (G_)
  < 50% retained on #4 → SAND (S_)
              |
              +--- Fines < 5%:
              |    Cu and Cc determine W (well-graded) vs. P (poorly-graded)
              |    GW: Cu≥4, 1≤Cc≤3   SW: Cu≥6, 1≤Cc≤3
              |    GP: doesn't meet W criteria  SP: doesn't meet W criteria
              |
              +--- Fines > 12%:
              |    Run Atterberg limits on fines
              |    Fines plot below A-line (low plasticity): GM or SM
              |    Fines plot above A-line (high plasticity): GC or SC
              |
              +--- Fines 5-12%: dual symbol (e.g., GW-GM)
```

### Fine-Grained Soils (> 50% passing #200)

The **Casagrande Plasticity Chart** plots PI vs. LL:

```
CASAGRANDE PLASTICITY CHART:

  PI
  60 |                                          /
     |                                         / CH
  50 |                              A-line    /
     |                           PI=0.73(LL-20)
  40 |                                    /
     |                               /   / CL
  30 |                          /       /
     |      ML/OL          /         /
  20 |      region    /           /
     |           /             /
  10 |       /  MH/OH region /
     |   CL-ML               /
   4 |_U-line____________/________________
     0   10  20  30  40  50  60  70  80  LL

  A-line (Casagrande): PI = 0.73(LL - 20)
  ABOVE A-line: Clay character (C)
  BELOW A-line: Silt/organic character (M or O)

  LL < 50: Low plasticity (L) — CL, ML, OL
  LL ≥ 50: High plasticity (H) — CH, MH, OH
```

### Full USCS Symbols

| Symbol | Name | Key Properties |
|--------|------|---------------|
| **GW** | Well-graded gravel | Good structural fill, high strength |
| **GP** | Poorly-graded gravel | Free-draining, lower strength |
| **GM** | Silty gravel | Reduced strength and drainage with fines |
| **GC** | Clayey gravel | Plastic fines, shrink-swell possible |
| **SW** | Well-graded sand | Excellent foundation material |
| **SP** | Poorly-graded sand | Susceptible to liquefaction |
| **SM** | Silty sand | Susceptible to piping, moderate strength |
| **SC** | Clayey sand | Plastic, lower permeability |
| **ML** | Low-plasticity silt | Susceptible to frost heave, low strength |
| **CL** | Low-plasticity clay | Moderate swelling, moderate strength |
| **OL** | Organic silt/clay | Low strength, high compressibility |
| **MH** | High-plasticity silt | Very frost susceptible, elastic silt |
| **CH** | High-plasticity clay | High swelling/shrinkage, low strength |
| **OH** | Organic clay | Very compressible, avoid as fill |
| **Pt** | Peat | Extremely compressible, avoid as bearing |

---

## Hydrometer Analysis

Particles finer than #200 sieve (< 0.075 mm) cannot be sieved. Hydrometer analysis uses Stokes' law: settling velocity = f(particle diameter, fluid viscosity, specific gravity difference).

A hydrometer measures specific gravity of the soil-water suspension at a given depth at regular time intervals. From the reading: % finer than a given particle diameter at that time.

**Stokes' law**: v = γw(Gs - 1) × D² / (18η)

where D = particle diameter, η = viscosity of water, Gs = specific gravity of solids.

Practical output: distribution curve extended below 0.075 mm into silt (0.002–0.075 mm) and clay (< 0.002 mm) fractions.

---

## AASHTO Classification (M-145)

Used for highway and roadway subgrade design. Groups soils A-1 through A-8 based on sieve analysis and Atterberg limits:

```
AASHTO CLASSIFICATION SUMMARY:

  A-1: Coarse granular (gravel/sand, ≤10% fines, PI≤6) — excellent
  A-2: Granular with fines — good to fair
  A-3: Fine sand (coastal dune sand) — fair to good
  A-4: Silty soil (≤LL, low plasticity) — fair to poor
  A-5: Silty soil (high LL, elastic silt) — poor
  A-6: Clayey soil (PI≥11) — poor
  A-7: Plastic clay (high LL + PI) — very poor
  A-8: Peat/muck — not suitable as subgrade

  Group Index (GI): 0 (best) to 20+ (worst)
  GI = f(% passing #200, LL, PI) — quantifies subgrade quality

  AASHTO focuses on subgrade performance.
  USCS focuses on material behavior for broader applications.
```

---

## Correlations: What Classification Predicts

```
ENGINEERING PROPERTIES FROM CLASSIFICATION:

  PI → Shrink/swell potential:
  PI < 10:  Low expansion
  PI 10-20: Medium
  PI 20-40: High
  PI > 40:  Very high (montmorillonite clays)

  PI → Undrained shear strength (rough):
  Su/σ'v ≈ 0.11 + 0.0037 × PI (Skempton, normally consolidated)

  LL → Compressibility:
  Cc ≈ 0.009(LL - 10)  (Terzaghi/Peck correlation for remolded)
  Higher LL → more compressible

  Classification → Permeability (order of magnitude):
  GW: 10^-1 to 10^-2 cm/s
  SW: 10^-2 to 10^-3 cm/s
  ML: 10^-4 to 10^-5 cm/s
  CL: 10^-6 to 10^-8 cm/s
  CH: 10^-7 to 10^-9 cm/s

  SP: susceptible to liquefaction (D10 < 0.5 mm, FC < 15%)
  ML: susceptible to frost heave
  CH: high swelling, low allowable bearing
```

---

## Decision Cheat Sheet

| You have... | Run test... | Why |
|------------|------------|-----|
| Soil with large particles | Sieve analysis (Cu, Cc) | USCS coarse group W vs. P |
| Fine-grained soil | Atterberg limits (LL, PL, PI) | USCS fine group C vs. M; H vs. L |
| Need to check for fines character | Atterberg limits on -#40 fraction | Above/below A-line determines M vs. C suffix |
| Highway subgrade design | AASHTO classification | Group Index directly used in pavement design |
| Suspect organic content | Visual, Casagrande cup → oven dry | LL drops > 30% after oven drying → organic (O) |
| Need compressibility estimate | LL → Cc = 0.009(LL-10) | Settlement calculation from classification |

---

## Common Confusion Points

**USCS vs. AASHTO**: USCS is the general-purpose geotechnical system. AASHTO focuses specifically on road subgrade performance. The same soil can get different ratings in each. Use USCS for foundations, slopes, retaining walls; AASHTO for pavement design.

**Silt vs. clay by behavior, not particle size**: In USCS, the boundary between M (silt) and C (clay) is determined by the **Atterberg limits and position on the plasticity chart**, not by particle size. A soil can have clay-sized particles but behave like silt (plot below A-line) — it's still classified M. What matters for engineering is plasticity behavior, not grain size alone.

**Poorly graded ≠ bad soil**: "Poorly graded" means uniform particle size, not poor quality. A clean SP (poorly graded sand) can be excellent foundation material — it's free-draining and densifies well. "Well-graded" means wide size distribution, which usually means better interlocking and lower void ratio.

**LL testing requires standardized equipment**: Casagrande cup results are sensitive to cup drop height, groove-cutting tool, and operator technique. Routine tests should use the fall cone method (less operator-dependent) or ensure equipment calibration. Interlaboratory variability for LL is ±3–5%.
