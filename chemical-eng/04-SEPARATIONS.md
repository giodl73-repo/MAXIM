# 04 — Separation Processes

## Distillation, Absorption, Extraction, Membranes, Adsorption

<!-- @editor[diagram/P2]: The "Separation Selection Framework" is a text list, not a landscape diagram. The file needs an ASCII diagram showing the separation process hierarchy — feed composition → driving force selection → equipment type → column/stage design. The current text block lists items but doesn't show how they relate to one another (e.g., which driving forces work for which feed phases, how equilibrium stages vs differential contact differ architecturally). Rework as a layered selection tree or process flow. -->
```
SEPARATION SELECTION FRAMEWORK

Driving force:
  Volatility difference → DISTILLATION (most common)
  Solubility difference → LIQUID-LIQUID EXTRACTION
  Size/charge difference → MEMBRANES, CHROMATOGRAPHY
  Adsorption affinity → ADSORPTION, PSA
  Crystallization → CRYSTALLIZATION (solid-liquid)

Phase contacting method:
  Equilibrium stages (trays, mixer-settlers) vs
  Differential contact (packed columns, membranes)
```

Separations typically account for 40–80% of capital and operating cost in chemical plants.
Choosing the right separation method is as important as the reaction.

---

## Vapor-Liquid Equilibrium Fundamentals for Separations

**Relative volatility:**
```
α_AB = (y_A/x_A) / (y_B/x_B) = K_A/K_B

y_A = α x_A / (1 + (α−1) x_A)    (binary, for constant α)

α = 1:   no separation possible
α = 1.1: difficult (many stages needed)
α = 1.5: moderate
α > 2:   easy separation
```

---

## Distillation

<!-- @editor[bridge/P1]: Distillation is the canonical separation algorithm — exploiting a property difference (volatility) to partition a mixture using a staged cascade. The bridge to software: merge sort and radix sort are also staged separation algorithms that exploit a property (key ordering) to partition data. The reflux ratio is analogous to re-examination passes in sorting. The McCabe-Thiele step-off method is a graphical fixed-point iteration — the learner knows fixed-point iteration. This bridge should appear before the graphical method explanation. -->
The workhorse of chemical engineering separations. Based on volatility differences.

### McCabe-Thiele Graphical Method (Binary Distillation)

```
Assumptions: constant molar overflow (CMO), negligible heat effects

Rectifying section operating line:
  y = (R/(R+1)) x + x_D/(R+1)
  [slope = L/V = R/(R+1), passes through (x_D, x_D)]

Stripping section operating line:
  y = ((L+F_q)/(V−F(1−q))) x − (B x_B)/(V−F(1−q))
  [passes through (x_B, x_B)]

q-line (feed condition):
  y = q/(q−1) × x − z_F/(q−1)
  q = fraction of feed that is liquid
  q = 1: saturated liquid feed  → vertical q-line at x = z_F
  q = 0: saturated vapor feed   → horizontal q-line at y = z_F
```

**Step off plates:**
1. Start at (x_D, y_D) on equilibrium curve
2. Step horizontally to operating line → advance one stage
3. Step vertically to equilibrium curve → end of stage
4. Count stages until x ≤ x_B

### Minimum Reflux and Minimum Stages

```
Minimum reflux (infinite stages):
  At minimum reflux, operating line passes through a pinch point
  Underwood equation for minimum reflux:
    Σ (α_i z_Fi)/(α_i − θ) = 1 − q   (find θ between α's of key components)
    R_min = Σ (α_i z_Fi)/(α_i − θ) − 1  (then compute from rectifying line)

Minimum stages (total reflux, infinite reflux rate):
  Fenske equation:
    N_min = log[(x_D/(1−x_D)) × ((1−x_B)/x_B)] / log(α_avg)

Gilliland correlation (actual stages vs N_min, R):
  (N − N_min)/(N + 1) = f((R − R_min)/(R + 1))
  Design rule: R ≈ 1.2–1.5 R_min (economic optimum)
```

### Column Design — Height and Diameter

**Number of Transfer Units (NTU) for packed column:**
```
N_OG = ∫ dy/(y* − y)    (based on overall gas-phase driving force)
        (y_B to y_T)

Height of a Transfer Unit (HTU):
  H_OG = G / (K_ya a S)   [G = molar gas flow, K_ya = overall coefficient, S = area]

Packed height: Z = N_OG × H_OG

Equivalent: HETP (Height Equivalent to Theoretical Plate)
  Z = HETP × N_stages
  HETP relates packed performance to equilibrium stage performance
```

**Column diameter (flooding criterion):**
```
Flooding = excessive liquid hold-up blocks vapor → column fails
Design at 65–80% of flooding velocity

F_factor = v_s √ρ_G   (flooding parameter)
Use generalized pressure drop correlation (Eckert chart) or GPDC
```

### Azeotropic and Extractive Distillation

```
Minimum-boiling azeotrope (e.g., ethanol-water at 95.6%):
  Cannot pass azeotrope by ordinary distillation

Approaches:
  1. Pressure-swing: azeotrope composition changes with P → two-column system
     (ethanol-water: limited shift → not practical)
  2. Extractive distillation: add heavy solvent (e.g., ethylene glycol) that changes γ
     → shifts relative volatility → can separate past azeotrope → recover solvent
  3. Azeotropic distillation: add entrainer (e.g., benzene for ethanol dehydration)
     → forms heterogeneous azeotrope → decant → two columns
  4. Molecular sieves (adsorption): for dehydration (ethanol-water, last bit)
```

---

## Absorption and Stripping

**Purpose:** Transfer a component from gas to liquid (absorption) or liquid to gas (stripping).
Examples: CO₂ capture (gas → amine liquid), solvent recovery (liquid → stripping steam).

### Kremser Equation (Dilute Systems, Straight Equilibrium)

```
For absorption:  y*= m x  (Henry's law, m = slope)
Absorption factor: A = L/(mG)  where L = liquid rate, G = gas rate

Number of ideal stages:
  N = ln[(y_in − mx_in)/(y_out − mx_in) × (1 − 1/A) + 1/A] / ln(A)

For stripping: use stripping factor S = mG/L = 1/A

Design guidelines:
  A = 1.25–1.5 (absorption) — economic optimum
  Too low A → many stages; too high A → excessive solvent
```

---

## Liquid-Liquid Extraction (LLE)

**Concept:** Distribute solute between immiscible phases using difference in solubility.

```
Distribution coefficient: K_D = C_A^(extract)  / C_A^(raffinate)
Extraction factor: E = K_D × B/A   (B = extract phase, A = raffinate phase)

Single-stage extraction: fraction extracted = E/(E+1)
N stages (countercurrent, E constant):
  Kremser equation: N = ln[(x_in−y_in/K_D)/(x_out−y_in/K_D) × (1−1/E) + 1/E] / ln(E)

McCabe-Thiele for LLE: same graphical method as absorption, on x-y diagram
```

**Equipment:**
- Mixer-settler stages: high contact, clean phase separation, high capital
- Pulsed columns / extraction columns: differential contact, smaller footprint
- Centrifugal extractors: fast separation, compact, good for emulsifying systems

---

## Membrane Separations

### Reverse Osmosis (RO) and Pressure-Driven Membranes

```
Osmotic pressure: π = i c R T   (van't Hoff for dilute solutions)
  Seawater: π ≈ 27 bar

RO driving force: ΔP − Δπ  (net transmembrane pressure)
Flux: J_w = A_w (ΔP − Δπ)   [A_w = water permeability]
Salt flux: J_s = B_s Δc_s   [B_s = solute permeability, independent of pressure]

Concentration polarization: solute builds up at membrane → increases Δπ → reduces flux
```

**Membrane categories (by size cutoff):**
```
Process         MWCO / pore size    Removes
─────────────────────────────────────────────────────────────────
Microfiltration  0.1–10 μm          Particles, bacteria, cells
Ultrafiltration  1–100 kDa          Colloids, proteins, viruses
Nanofiltration   200–1000 Da        Small organics, divalent ions
Reverse osmosis  < 200 Da           All ions, small molecules
```

### Gas Separation Membranes

```
Solution-diffusion model:
  J_i = P_i (p_feed - p_permeate)
  P_i = permeability [Barrer = 10⁻¹⁰ cm³(STP)·cm/(cm²·s·cmHg)]

Selectivity: α_ij = P_i/P_j

Robeson upper bound: trade-off between permeability and selectivity
  Above upper bound: "super-glassy" or mixed-matrix membranes required

Gas pairs: O₂/N₂ (air separation), CO₂/CH₄ (natural gas upgrading), H₂/CO (syngas)
```

---

## Adsorption

**Isotherm types:**
```
Langmuir (favorable):
  q = q_max K C / (1 + K C)
  q = loading [mol/kg], C = fluid concentration, K = affinity constant

Freundlich (empirical):
  q = K_F C^(1/n)   (n > 1: favorable; n = 1: linear; n < 1: unfavorable)

BET (multilayer, for gas/solid):
  p/(p°−p) × 1/(C×q_m) + (C−1)/(C×q_m) × p/p°
  Used for surface area measurement
```

### Pressure Swing Adsorption (PSA)

```
Cycle:
  1. Adsorption at high pressure: feed passes through bed, impurity adsorbs
  2. Depressurization + purge: regenerate bed at low pressure (impurity desorbs)
  3. Repressurization: return to high pressure for next cycle

Applications:
  Air separation: O₂ production (zeolite adsorbs N₂ preferentially) → 90–95% O₂
  H₂ purification: activated carbon adsorbs CO, CO₂, CH₄ → >99.9% H₂
  CO₂ capture from flue gas (post-combustion, emerging technology)
```

---

## Crystallization

**Supersaturation drives nucleation and growth:**
```
Supersaturation: S = C/C* or σ = (C−C*)/C*  (C* = saturation concentration)

Nucleation:
  Homogeneous: J = A exp(−B/σ²)  (classical nucleation theory)
  Heterogeneous: lower energy barrier → occurs at lower σ → faster

Crystal growth:
  G = k_g σ^g   (growth rate, g ≈ 1–3)

Crystal size distribution (CSD):
  Population balance: dn/dL + Gn/τ = 0  (MSMPR model)
  n = n₀ exp(−L/(Gτ))  → exponential distribution
  Dominant size: L_dom = 3Gτ
```

**Solubility curves:** plot solubility vs T.
- Cooling crystallization: most salts less soluble at low T → cool solution
- Evaporative crystallization: remove solvent → supersaturate at constant T
- Anti-solvent crystallization: add a solvent where compound is insoluble

---

## Chromatography

**Plate theory:**
```
N = theoretical plates = (t_R/σ)²   (t_R = retention time, σ = peak std dev)
HETP = L/N   (height equivalent to theoretical plate)

van Deemter equation:
  HETP = A + B/u + C×u
  A = Eddy diffusion (packing geometry)
  B/u = longitudinal diffusion (B = 2γD_m)
  C×u = mass transfer resistance (C = R/D_s)
  Minimum HETP at u_opt = √(B/C)
```

**Resolution:** R_s = 2(t_R2 − t_R1)/(w_1 + w_2) ≥ 1.5 for baseline separation.

---

## Common Confusion Points

**Reflux ratio R vs internal flows:** R = L/D (external, measurable). Internal liquid flow L = R × D; internal vapor flow V = (R+1)D. Operating line slope = L/V = R/(R+1).

**NTU ≠ number of stages:** NTU is for packed (differential) columns. Number of equilibrium stages is for tray columns. HETP bridges them: N_stages = Z/HETP.

**Stripping vs absorption:** Absorption: gas → liquid. Stripping: liquid → gas. Same equations, different direction. Key check: what's the driving force (y − y*) or (x* − x)?

**K_D and extraction factor:** K_D is a thermodynamic property (ratio of concentrations at equilibrium). E = K_D × B/A includes flow rates. E > 1 needed for effective extraction.

**Reverse osmosis energy:** RO operates above osmotic pressure. Energy ~0.3–1 kWh/m³ for brackish water, 3–4 kWh/m³ for seawater. Better than evaporation (distillation) by 10–30×.

---

## Decision Cheat Sheet

| Separation need | Method | Key condition |
|----------------|--------|-------------|
| Separate two volatility-different liquids | Distillation | α > 1.05; both condensable |
| Pass through azeotrope | Extractive/azeotropic distillation | Add solvent or entrainer |
| Remove gas from liquid | Absorption (gas → liquid) | High L/G or high K_H |
| Strip dissolved component | Steam stripping | High Henry's constant |
| Separate with solvent | LLE | High K_D in desired phase |
| Remove salts from water | Reverse osmosis | ΔP > Δπ |
| Purify H₂ | PSA | H₂ doesn't adsorb on activated C |
| Separate proteins/biologics | Chromatography / UF | Size or affinity differences |
| Separate crystalizable compound | Crystallization | Clear solubility curve |
