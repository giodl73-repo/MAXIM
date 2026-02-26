# 03-THERMOCHEM — Thermochemistry & Chemical Thermodynamics

> From heat of combustion to Gibbs free energy to phase diagrams.
> The laws that govern what reactions can happen, how much energy they release,
> and when equilibrium is reached.

---

<!-- @editor[diagram/P2]: The Four Laws section is an excellent text summary but not a landscape diagram — it lists laws sequentially without showing how they connect to the rest of the guide (equilibrium, phase diagrams, Gibbs, Hess, colligative properties). A visual map showing these relationships would anchor the layered drill-down. -->
## The Four Laws — Quick Map

```
Zeroth Law:  Temperature is transitive.
             A = B (thermal), B = C (thermal) → A = C.
             Defines temperature as a state function.

First Law:   Energy is conserved.
             ΔU = q + w   (internal energy = heat + work)
             At constant pressure: q = ΔH (enthalpy)

Second Law:  Entropy of an isolated system never decreases.
             ΔS_universe = ΔS_system + ΔS_surroundings ≥ 0
             Spontaneous processes increase total entropy.

Third Law:   Entropy of a perfect crystal at 0 K is zero.
             Absolute entropy S° is measurable.
             All tabulated S° values are referenced to this.
```

---

## Enthalpy (ΔH)

### Definition

```
H = U + PV      (enthalpy = internal energy + pressure-volume work)

At constant pressure (most chemistry):
  ΔH = ΔU + PΔV

For ideal gas reactions:
  ΔH = ΔU + Δn_gas · RT     (Δn_gas = moles product gas − moles reactant gas)
```

**Sign convention:**
- ΔH < 0: exothermic (heat released to surroundings)
- ΔH > 0: endothermic (heat absorbed from surroundings)

### Hess's Law

Enthalpy is a **state function** — path-independent.
ΔH for any reaction = sum of ΔH for any set of steps that add to give the target reaction.

```
Target:   C(s) + ½O₂(g) → CO(g)              ΔH = ?

Known:    C(s) + O₂(g) → CO₂(g)             ΔH₁ = −393.5 kJ/mol
          CO(g) + ½O₂(g) → CO₂(g)           ΔH₂ = −283.0 kJ/mol

Reverse reaction 2 and add:
          C(s) + O₂(g) → CO₂(g)             ΔH₁ = −393.5
          CO₂(g) → CO(g) + ½O₂(g)           −ΔH₂ = +283.0
          ─────────────────────────────────────────────────────
          C(s) + ½O₂(g) → CO(g)             ΔH = −110.5 kJ/mol
```

### Standard Enthalpy of Formation (ΔHf°)

ΔHf° = enthalpy change to form 1 mol of compound from elements in standard states.
By definition: ΔHf°(element in standard state) = 0.

```
ΔH°rxn = Σ n·ΔHf°(products) − Σ m·ΔHf°(reactants)

Example: CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(l)
  ΔHf°: CH₄ = −74.8,  O₂ = 0,  CO₂ = −393.5,  H₂O(l) = −285.8  (kJ/mol)
  ΔH° = [−393.5 + 2(−285.8)] − [−74.8 + 0] = −890.3 kJ/mol
```

### Bond Enthalpy Method (Approximate)

```
ΔH ≈ Σ(bonds broken) − Σ(bonds formed)
     [energy in]       [energy out]

Bond enthalpies (kJ/mol, avg):
  C–H: 413    C=C: 614    C≡C: 839
  C–C: 347    C=O: 799    O–H: 463
  N–N: 163    N=N: 418    N≡N: 945
  Cl–Cl: 243  H–H: 436    H–Cl: 431

Less accurate than Hess's law (uses averages, not actual bond energies).
Useful for quick estimates and understanding trends.
```

### Kirchhoff's Law — Temperature Dependence

```
ΔH°(T₂) = ΔH°(T₁) + ∫[T₁ to T₂] ΔCp dT

where ΔCp = Σ Cp(products) − Σ Cp(reactants)

For moderate temperature ranges (ΔCp approximately constant):
  ΔH°(T₂) ≈ ΔH°(T₁) + ΔCp · (T₂ − T₁)
```

---

## Entropy (ΔS)

### Statistical Definition

```
S = k_B · ln(W)      (Boltzmann, 1877)

W = number of microstates consistent with the macrostate
k_B = 1.38 × 10⁻²³ J/K

More microstates → higher entropy.
```

### Thermodynamic Definition (Clausius)

```
dS = δq_rev / T      (reversible heat transfer at temperature T)

For phase transition at constant T:
  ΔS_transition = ΔH_transition / T

Example: H₂O(l) → H₂O(g) at 100°C (373 K)
  ΔS_vap = 40,700 J/mol ÷ 373 K = 109 J/(mol·K)
```

### What Increases Entropy

```
HIGH entropy                         LOW entropy
─────────────────────────────────────────────────
Gas > liquid > solid                 Ordered crystal
More moles of gas                    Fewer moles of gas
Higher temperature                   Lower temperature
Mixing (solutions, gases)            Separation
Larger molecules (more conformations) Rigid structures
Disordered sequences                 Regular patterns
```

**Trouton's Rule:** ΔS_vap ≈ 88 J/(mol·K) for most non-hydrogen-bonding liquids.
Water is an exception (~109 J/(mol·K)) — H-bond network in liquid reduces entropy vs expectation.

---

## Gibbs Free Energy (ΔG)

The master function for chemistry at constant T and P (which is almost all chemistry).

```
G = H − TS          (Gibbs function)
ΔG = ΔH − TΔS

Criterion for spontaneity (constant T, P):
  ΔG < 0:  spontaneous (exergonic)
  ΔG = 0:  equilibrium
  ΔG > 0:  non-spontaneous (endergonic); reverse is spontaneous
```

### The Four Cases

```
ΔH    ΔS    ΔG = ΔH − TΔS      Spontaneity
──────────────────────────────────────────────────────────
−     +     Always negative     Always spontaneous
+     −     Always positive     Never spontaneous
−     −     Negative at low T   Spontaneous at low T
+     +     Negative at high T  Spontaneous at high T
```

**Crossover temperature** (where ΔG changes sign):
```
T_crossover = ΔH / ΔS     (set ΔG = 0, solve for T)

Example: CaCO₃(s) → CaO(s) + CO₂(g)
  ΔH = +178 kJ/mol,  ΔS = +165 J/(mol·K)
  T_crossover = 178,000 / 165 = 1079 K (≈ 806°C)
  → Spontaneous above 806°C. Below: ΔG > 0, calcite stable.
```

### Standard Gibbs Energy of Formation

```
ΔG°rxn = Σ n·ΔGf°(products) − Σ m·ΔGf°(reactants)

Also:  ΔG° = ΔH° − TΔS°     (using standard values at 298 K)

Link to equilibrium:
  ΔG° = −RT ln K
  K = e^(−ΔG°/RT)

ΔG° < 0  → K > 1  (products favored at equilibrium)
ΔG° > 0  → K < 1  (reactants favored at equilibrium)
```

### ΔG vs ΔG° — Critical Distinction

```
ΔG° = standard free energy change (all species at 1 M, 1 atm, 298 K)
ΔG  = free energy change at actual conditions

ΔG = ΔG° + RT ln Q

where Q = reaction quotient (same form as K, but current concentrations/pressures)

At equilibrium: ΔG = 0 and Q = K → 0 = ΔG° + RT ln K ✓
```

---

## Chemical Equilibrium

### Equilibrium Constants

```
For:  aA + bB ⇌ cC + dD

Kc = [C]^c[D]^d / [A]^a[B]^b     (concentrations, mol/L)
Kp = P_C^c · P_D^d / P_A^a · P_B^b   (partial pressures, atm or bar)

Relationship:
  Kp = Kc · (RT)^Δn_gas

Pure solids and liquids: omitted from K (activity = 1)
Water as solvent: omitted from K (activity ≈ 1)
```

### Solubility Products (Ksp)

```
CaF₂(s) ⇌ Ca²⁺(aq) + 2F⁻(aq)
Ksp = [Ca²⁺][F⁻]²

Molar solubility s: [Ca²⁺] = s,  [F⁻] = 2s
Ksp = s · (2s)² = 4s³  →  s = (Ksp/4)^(1/3)

Common ion effect: adding F⁻ (from NaF) suppresses CaF₂ dissolution
  → Q > Ksp → precipitation until Q = Ksp
```

### Le Chatelier's Principle

System at equilibrium shifts to oppose any imposed stress:

```
Stress                    Direction of shift
─────────────────────────────────────────────────────────
Add reactant              → products (forward)
Add product               → reactants (reverse)
Remove reactant           → reactants (reverse)
Increase pressure         → fewer moles of gas side
Decrease pressure         → more moles of gas side
Increase temperature      → endothermic direction
Decrease temperature      → exothermic direction
Add inert gas (const. V)  no shift (partial pressures unchanged)
Add catalyst              no shift (both rates increase equally)
```

### Van't Hoff Equation — K vs Temperature

```
d(ln K)/dT = ΔH° / RT²

Integrated (constant ΔH°):
  ln(K₂/K₁) = −(ΔH°/R) · (1/T₂ − 1/T₁)

Plot ln K vs 1/T → slope = −ΔH°/R  (Van't Hoff plot)

Exothermic reaction (ΔH° < 0): K decreases as T rises
Endothermic reaction (ΔH° > 0): K increases as T rises
```

---

## Phase Equilibria

### Phase Diagrams

```
WATER (anomalous)                  CO₂ (typical)

    P                               P
    │        Liquid                 │         Liquid
    │  ┌─────────────── Critical    │   ┌───────────────── Critical
    │  │                point       │   │                  point
    │  │   Solid                    │   │   Solid
    │  │ /                          │   │  /
1atm│──┼────────────→ Gas          │   │ /
    │  │ Triple pt                  │   │/ Triple pt (5.1 atm)
    │  └──────────→ T               │   └──────────────→ T
    │  0°C 100°C                    │   −78.5°C
    │                               │
    │ Water solid/liquid line has   │ CO₂ solid/liquid line has
    │ NEGATIVE slope (anomalous):   │ POSITIVE slope (normal):
    │ ice melts under pressure      │ pressure raises melting point
```

**Triple point:** unique T, P where all three phases coexist.
Water: 273.16 K, 611.7 Pa (0.006 atm)
CO₂: 216.8 K, 5.18 atm (→ CO₂ never liquid at 1 atm — sublimes)

**Critical point:** above this T and P, gas/liquid distinction disappears.
Water: 374°C, 218 atm.

### Clausius-Clapeyron Equation

```
Slope of any phase boundary:
  dP/dT = ΔH_transition / (T · ΔV)

For liquid-gas (ΔV ≈ RT/P for ideal gas):
  d(ln P)/dT = ΔH_vap / RT²

Integrated (vapor pressure vs T):
  ln(P₂/P₁) = −(ΔH_vap/R) · (1/T₂ − 1/T₁)

Plot ln P vs 1/T → slope = −ΔH_vap/R
```

### Colligative Properties

Depend only on solute particle count, not identity:

```
Property           Formula                   Notes
──────────────────────────────────────────────────────────────────
Boiling point rise  ΔTb = Kb · m · i         Kb = ebullioscopic const.
Freezing pt. dep.   ΔTf = Kf · m · i         Kf = cryoscopic const.
Osmotic pressure    Π = iMRT                  M = molarity, R = 0.08206
Vapor pressure dep. P = x_solvent · P°        Raoult's law

m = molality (mol solute/kg solvent)
i = van't Hoff factor (1 for non-electrolyte, ~2 for NaCl, ~3 for CaCl₂)
```

Water: Kb = 0.512 °C·kg/mol, Kf = 1.86 °C·kg/mol
NaCl in water: i ≈ 1.9 (not exactly 2 due to ion pairing at real concentrations)

---

## Thermodynamic Cycles

### Carnot Cycle — The Efficiency Limit

```
Maximum efficiency of any heat engine operating between T_H and T_C:

η_Carnot = 1 − T_C/T_H      (T in Kelvin)

Four steps:
  1. Isothermal expansion at T_H      (absorb q_H)
  2. Adiabatic expansion T_H → T_C    (ΔS = 0)
  3. Isothermal compression at T_C    (release q_C)
  4. Adiabatic compression T_C → T_H  (ΔS = 0)

Net: w = q_H − q_C,   η = w/q_H = 1 − q_C/q_H = 1 − T_C/T_H

Why no real engine reaches η_Carnot:
  Irreversibilities: friction, heat transfer across finite ΔT, turbulence
```

### Hess's Law as Matrix Algebra

Hess's law is exactly the statement that ΔH forms a linear functional on the
reaction vector space. Given a matrix A of stoichiometric coefficients (rows =
species, cols = reactions), any target reaction in the column space of A can
be synthesized by linear combination. This is linear algebra — the same reason
why balanced equations form the null space of the stoichiometric matrix
(used explicitly in flux balance analysis of metabolism — see 08-METABOLISM.md).

---

## Decision Cheat Sheet

| Question | Concept | Key relation |
|----------|---------|-------------|
| Will this reaction release heat? | ΔH < 0 | Exothermic — look up ΔHf° values |
| Will this reaction occur spontaneously? | ΔG < 0 | Check ΔG = ΔH − TΔS |
| At what temperature does spontaneity flip? | Crossover | T = ΔH/ΔS (both same sign) |
| Where is equilibrium at 500 K? | K = e^(−ΔG°/RT) | Calculate ΔG°, then K |
| How does K change if I heat the reaction? | Van't Hoff | Exothermic → K decreases with T |
| Why does salt lower freezing point? | Colligative | ΔTf = Kf·m·i |
| Can CO₂ be liquid at atmospheric pressure? | Phase diagram | No — triple point at 5.18 atm |
| Why does ice melt under pressure? | Negative dP/dT slope | Water density anomaly |
| What does adding product do to equilibrium? | Le Chatelier | Shifts reverse, Q > K until re-equilibration |
| Is a reaction at standard state at equilibrium? | ΔG° vs ΔG | No — equilibrium is ΔG = 0, not ΔG° = 0 |

---

## Common Confusion Points

**ΔG° ≠ ΔG — the most common thermodynamics error**
ΔG° is the free energy change under *standard conditions* (1 M, 1 atm, 298 K).
Real reactions operate under non-standard conditions.
ΔG = ΔG° + RT ln Q. At equilibrium, ΔG = 0, Q = K — NOT ΔG° = 0.
A reaction can have ΔG° > 0 (disfavored at standard state) and still proceed
spontaneously if Q < K (concentrations far from equilibrium).

**Spontaneous ≠ fast**
ΔG < 0 means the reaction can proceed (thermodynamically favorable).
It says nothing about the rate. Diamond → graphite: ΔG = −2.9 kJ/mol (spontaneous).
Rate ≈ 0 at room temperature. Thermodynamics and kinetics are independent.

**Entropy always increases — for the universe, not the system**
A reaction where ΔS_system < 0 can be spontaneous if ΔS_surroundings > |ΔS_system|.
Protein folding: ΔS_protein < 0 (order increases), but ΔS_water > 0 (hydrophobic
effect releases ordered water) → net ΔS_universe > 0 → spontaneous.

**"Equilibrium" ≠ equal concentrations**
K = [products]/[reactants] at equilibrium.
K = 1 means equal concentrations. K = 10⁶ means almost all products.
The system finds the state that minimizes G, which need not be 50:50.

**Enthalpy is not the same as internal energy**
ΔU = q + w (all work). ΔH = ΔU + PΔV = qₚ (heat at constant pressure).
For reactions involving no gases (ΔV ≈ 0): ΔH ≈ ΔU.
For gas-phase reactions: ΔH − ΔU = Δn_gas · RT (can be significant).

**Le Chatelier and catalysts**
A catalyst does not shift equilibrium. It speeds up both forward and reverse
reactions equally (lowers the same ΔG‡ for both). The equilibrium position
(K) is unchanged. The system reaches equilibrium faster, not at a different K.
