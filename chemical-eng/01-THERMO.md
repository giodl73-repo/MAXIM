# 01 — Chemical Engineering Thermodynamics

## Phase Equilibria, Equations of State, Fugacity, Activity

```
CHEMICAL THERMODYNAMICS TOOLKIT

  EQUATIONS OF STATE        PHASE EQUILIBRIUM          REACTION EQUILIBRIUM
  ─────────────────         ──────────────────         ───────────────────────
  PV relationships          VLE, LLE, SLE              K_eq = exp(−ΔG°/RT)
  ideal gas → Peng-Robinson Raoult → NRTL/UNIQUAC       van't Hoff: d(lnK)/dT
  compressibility Z         fugacity = activity         Gibbs energy minimization
  fugacity coefficient φ    azeotropes
```

Chemical thermodynamics extends mechanical thermodynamics (01-THERMODYNAMICS.md) to
**mixtures**, **phase behavior**, and **chemical reactions** — the additional complexity
that distinguishes chemical engineering from mechanical engineering.

---

## Fundamental Relations

**Gibbs free energy as master potential (at constant T, P):**
```
G = H − TS

Differential:
  dG = V dP − S dT + Σ μᵢ dnᵢ

Chemical potential:
  μᵢ = (∂G/∂nᵢ)_{T,P,nⱼ≠ᵢ}   [J/mol]

Criterion for equilibrium (at const T, P): dG = 0 → G is minimized
For species i in phase equilibrium: μᵢ^α = μᵢ^β  (equality of chemical potential)
```

### Gibbs Phase Rule

```
F = C − P + 2

F = degrees of freedom (intensive variables that can be independently set)
C = number of independent chemical components
P = number of phases present (not confused with pressure)

Examples:
  Pure water, vapor-liquid: F = 1−2+2 = 1  (specify T or P → state fixed)
  Water-ethanol, vapor-liquid: F = 2−2+2 = 2  (specify T and x)
  Triple point: F = 0  (no freedom, exactly one T,P)
  Pure gas: F = 2  (specify T and P independently)
```

---

## Equations of State (EOS)

### Ideal Gas (Baseline)

```
pV = nRT    or    pv = RT  (molar volume v = V/n)
Z = pv/RT = 1
```

Fails at high pressures (intermolecular forces matter) and low temperatures (near condensation).

### van der Waals

```
(p + a/v²)(v − b) = RT

Corrections:
  a/v² = internal pressure (intermolecular attractions reduce observed p)
  b = excluded volume (molecules have finite size)

Critical constants: T_c = 8a/(27Rb),  p_c = a/(27b²),  v_c = 3b
```

### Peng-Robinson (Industry Standard)

```
p = RT/(v−b) − aα/[v(v+b) + b(v−b)]

a = 0.45724 R²T_c²/p_c
b = 0.07780 RT_c/p_c
α = [1 + κ(1 − √(T/T_c))]²    κ = 0.37464 + 1.54226ω − 0.26992ω²

ω = acentric factor (tabulated for all common compounds; 0 for noble gases, ~0.3 for alkanes)
```

**Why Peng-Robinson over van der Waals?** PR much more accurate for VLE calculations.
PR predicts liquid densities better than SRK (Soave-Redlich-Kwong), particularly for heavy hydrocarbons.

**Cubic EOS root structure:**
```
At subcritical T: cubic → 3 real roots
  Largest root: vapor (Z_V)
  Smallest root: liquid (Z_L)
  Middle root: unstable (ignore)
At supercritical T: only 1 real root
```

**Fugacity from EOS:**
```
ln φ = Z − 1 − ln(Z − B') − A'/(2√2 B') × ln[(Z+(1+√2)B')/(Z+(1−√2)B')]
(Peng-Robinson fugacity coefficient equation)

where A' = aα p/(R²T²),  B' = bp/(RT)
```

---

## Fugacity and Activity

**Fugacity** = "thermodynamic pressure" — corrected for non-ideality:
```
For real gas:   fᵢ = φᵢ yᵢ p    (φᵢ from EOS; φᵢ → 1 for ideal gas)
For liquid:     fᵢ = γᵢ xᵢ fᵢ°  (γᵢ = activity coefficient; fᵢ° = reference fugacity)

VLE equilibrium: fᵢ^V = fᵢ^L
  → φᵢ yᵢ p = γᵢ xᵢ φᵢ^sat pᵢ^sat   (modified Raoult's law, complete form)
  → yᵢ p = γᵢ xᵢ pᵢ^sat              (simplified: assume vapor ideal, Poynting negligible)
```

**Activity coefficient γᵢ:**
- γᵢ = 1: ideal solution (no excess Gibbs energy)
- γᵢ > 1: positive deviation (weaker unlike interactions → tendency to separate)
- γᵢ < 1: negative deviation (stronger unlike interactions → negative excess enthalpy)

---

## Activity Coefficient Models (for VLE)

| Model | Parameters | Range | Notes |
|-------|-----------|-------|-------|
| Margules (1-suffix) | 1 per binary | Simple | Educational |
| van Laar | 2 per binary | Some | Early model |
| Wilson | 2 per binary | Good | Not for LLE |
| NRTL | 3 per binary | Excellent | Works for LLE too |
| UNIQUAC | 2 per binary + structure | Very good | Group contribution variant: UNIFAC |

**Wilson model:**
```
ln γ₁ = −ln(x₁ + Λ₁₂ x₂) + x₂(Λ₁₂/(x₁+Λ₁₂x₂) − Λ₂₁/(x₂+Λ₂₁x₁))
Λ₁₂ = (V₂/V₁) exp(−(λ₁₂−λ₁₁)/RT)    (fitting parameters: λᵢⱼ)
Cannot predict LLE (always predicts miscibility).
```

**NRTL (Non-Random Two-Liquid):**
```
Adds non-randomness parameter α₁₂ (= 0.3 for many systems)
Can predict LLE and strongly non-ideal VLE
Most widely used in practice
```

---

## Vapor-Liquid Equilibrium (VLE)

### Raoult's Law (Ideal Solution)

```
yᵢ p = xᵢ pᵢ^sat(T)

pᵢ^sat from Antoine equation: log₁₀(pᵢ^sat) = A − B/(C+T)

Bubble point calculation:
  Given liquid x, find T (or p) where Σ yᵢ = 1
  Σ xᵢ pᵢ^sat = p   (solve for T or p)

Dew point calculation:
  Given vapor y, find T (or p) where Σ xᵢ = 1
  p = 1/Σ(yᵢ/pᵢ^sat)   (solve for T or p)
```

### Relative Volatility

```
αᵢⱼ = (yᵢ/xᵢ) / (yⱼ/xⱼ) = Kᵢ/Kⱼ = pᵢ^sat/pⱼ^sat  (ideal solution)

α > 1: component i more volatile than j
α ≈ 1: separation by distillation very difficult/impossible
α > 1.05: distillation feasible (more stages needed as α → 1)
```

#<!-- @editor[bridge/P3]: Rachford-Rice is explicitly a root-finding problem — worth noting that this is the same bisection/Brent method class they know from numerical methods context, not because they need the explanation, but because the domain framing ("flash drums are just root-finders") is a useful mental anchor for the engineer building intuition across fields. -->
## Flash Calculation (Rachford-Rice Equation)

Given z_i (feed), T, p — find V (vapor fraction) and y_i, x_i:

```
Rachford-Rice:
  Σᵢ zᵢ(Kᵢ − 1)/(1 + V(Kᵢ − 1)) = 0

Where Kᵢ = yᵢ/xᵢ (K-values from EOS or modified Raoult's law)
Solve for V ∈ [0,1], then: xᵢ = zᵢ/(1 + V(Kᵢ−1)),  yᵢ = Kᵢ xᵢ
```

### Azeotropes

```
At azeotrope: yᵢ = xᵢ for all i  → Kᵢ = 1 for all i → separation by ordinary distillation fails

Positive deviation (γᵢ > 1): minimum-boiling azeotrope (ethanol-water at 95.6 mol% ethanol)
Negative deviation (γᵢ < 1): maximum-boiling azeotrope (HCl-water at ~20 wt% HCl)

Remedies:
  Pressure-swing distillation: azeotrope composition shifts with pressure → two columns
  Extractive distillation: add solvent to change relative volatility
  Azeotropic distillation: add entrainer (forms heteroazeotrope)
  Membrane separation: bypass thermodynamic limitations
```

---

## Liquid-Liquid Equilibrium (LLE)

When two liquid phases coexist. Driven by large positive deviations from ideality.

```
Ternary LLE phase diagram:
  Two partially miscible binaries + solvent
  Tie lines connect compositions of two phases in equilibrium
  Plait point: tip of two-phase region (phases become identical)

Extraction applications:
  Use LLE to extract a solute from one liquid into another (see 04-SEPARATIONS)
```

**Distribution coefficient:** K_D = c_A^(organic phase) / c_A^(aqueous phase)
High K_D → good extraction (solute prefers organic phase).

---

## Chemical Reaction Equilibrium

**Equilibrium constant:**
```
For reaction: aA + bB ⇌ cC + dD

K_eq = exp(−ΔG°_rxn / RT)

ΔG°_rxn = ΔG°_f(products) − ΔG°_f(reactants)  (standard Gibbs energies of formation)

K_eq in terms of activities:
  K_eq = (a_C^c a_D^d) / (a_A^a a_B^b)

For ideal gas: aᵢ = pᵢ/p°  where p° = 1 bar reference
  K_p = Π pᵢ^νᵢ  (equilibrium constant in terms of partial pressures)
```

**van't Hoff equation (temperature dependence):**
```
d(ln K_eq)/dT = ΔH°_rxn / RT²

ΔH°_rxn > 0 (endothermic): K increases with T → higher T favors products
ΔH°_rxn < 0 (exothermic): K decreases with T → lower T favors products

Integrated: ln(K₂/K₁) = ΔH°_rxn/R × (1/T₁ − 1/T₂)
```

**Equilibrium conversion vs. T:**
```
Exothermic reactions (e.g., NH₃ synthesis, SO₃ formation):
  Low T: high equilibrium conversion but slow kinetics
  High T: fast kinetics but low equilibrium conversion
  Optimal T profile: start high (fast), cool as equilibrium is approached

Endothermic reactions (e.g., steam reforming CH₄ + H₂O → CO + 3H₂):
  High T always better for equilibrium → favor high T
```

---

## Common Confusion Points

**Fugacity vs pressure:** Fugacity has units of pressure but corrects for non-ideal behavior.
For an ideal gas in a mixture, fᵢ = yᵢp (just partial pressure). For liquids, fugacity is
related to saturation pressure and activity coefficient.

**Modified Raoult's law:** yᵢp = γᵢxᵢpᵢ^sat. This has both γᵢ (liquid non-ideality) and pᵢ^sat (pure component property). Standard Raoult's law sets γᵢ = 1 for ideal solutions.

**Bubble vs dew point:** Bubble point = conditions where first bubble of vapor forms from liquid (start of vaporization). Dew point = conditions where first drop of liquid forms from vapor (start of condensation). They bound the two-phase region on a P-x-y or T-x-y diagram.

**EOS selection:** For hydrocarbons and gases → Peng-Robinson or SRK. For polar molecules → need activity coefficient model (NRTL, UNIQUAC) or electrolyte thermodynamics. Wrong EOS selection is a common cause of process simulation failure.

**K_eq ≠ rate:** Equilibrium constant tells you where the system ends up, not how fast. You need kinetics (reaction engineering) for rates. High K_eq just means reactions goes far to completion; doesn't mean it's fast.

---

## Decision Cheat Sheet

| Need | Tool | Notes |
|------|------|-------|
| Gas phase P-V-T | Peng-Robinson EOS | Standard for hydrocarbons |
| VLE, non-ideal mixture | Modified Raoult's + NRTL | Need γᵢ model |
| Azeotrope check | Compute γᵢ at all compositions | Where γᵢxᵢ/yᵢ = 1 |
| Flash drum design | Rachford-Rice equation | Iterative root finding |
| Reaction equilibrium | K_eq = exp(−ΔG°/RT) | From thermodynamic tables |
| T effect on equilibrium | van't Hoff equation | Exothermic ↔ endothermic |
| Number of phases possible | Gibbs phase rule | F = C − P + 2 |
| LLE / extraction | Activity model with LLE capability | NRTL or UNIQUAC |
