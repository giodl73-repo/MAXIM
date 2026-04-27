# Groundwater — Aquifer Types, Darcy's Law, Hydraulic Conductivity, Well Hydraulics

## The Big Picture

```
+===========================================================================+
|                  GROUNDWATER SYSTEM STRUCTURE                             |
|       Darcy's law: flux proportional to head gradient — same as Ohm's law |
+===========================================================================+
|                                                                           |
|  VADOSE ZONE (unsaturated):         SATURATED ZONE:                      |
|  ─────────────────────────          ─────────────                        |
|  Soil → Capillary fringe            Water table (unconfined aquifer)     |
|  Tension > atmospheric              Water table at atmospheric pressure  |
|  Water held by capillarity          Pore pressure > atmospheric          |
|                                     Phreatic surface = water table       |
|                                                                           |
|  CONFINED AQUIFER:                  AQUITARD (low K):                    |
|  ─────────────────                  ────────────────                     |
|  Bounded above by aquitard          Confining layer                      |
|  Pressure head > water table        Silt, clay, unfractured rock         |
|  Artesian if head > land surface    Separates aquifer systems            |
|                                                                           |
+===========================================================================+
```

---

## Darcy's Law — The Fundamental Equation

### The Ohm's Law Analog

```
OHM'S LAW:           I = V/R = (ΔV/L) × (A/R_L)   current ∝ voltage gradient

DARCY'S LAW:         Q = K × (Δh/L) × A            flow ∝ head gradient
                     q = Q/A = K × dh/dL            specific discharge (flux)

  Where:
    Q = volumetric flow rate (m³/s)
    K = hydraulic conductivity (m/s) ← analogous to electrical conductivity 1/R_L
    dh/dL = hydraulic gradient (dimensionless) ← analogous to ΔV/L
    A = cross-sectional area (m²)
    q = specific discharge (Darcy flux, m/s) — NOT pore velocity!

  Pore velocity (actual water velocity):
    v = q / n
    n = porosity (fraction of void space)
    If n = 0.3 and q = 10⁻⁵ m/s → v = 3.3×10⁻⁵ m/s ≈ 3 m/day

THE FULL ANALOGY:
  Hydrology                    Electrical
  ─────────────────────────    ─────────────────────────
  Hydraulic head h (m)         Voltage V (V)
  Specific discharge q (m/s)   Current density J (A/m²)
  Hydraulic conductivity K     Electrical conductivity σ
  Storage coefficient S        Capacitance C
  Darcy's law q = K dh/dl      Ohm's law J = σ E = σ (-dV/dl)
  Storage eq: S ∂h/∂t = ...   RC circuit: C dV/dt = ...
  Transmissivity T = Kb        Sheet conductance (σ × thickness)
```

### Hydraulic Head

```
HYDRAULIC HEAD:
  h = z + P/(ρg)

  z   = elevation above datum (potential energy component)
  P/(ρg) = pressure head (pressure energy component)
  ρ   = water density
  g   = gravitational acceleration

  For a well: hydraulic head = level where water stabilizes in the well
  (standpipe head = pressure head + elevation = total energy per unit weight)

  WATER TABLE: surface where P = atmospheric → pressure head = 0 → h = z
  Piezometric surface: locus of hydraulic heads in a confined aquifer
    (can be above land surface → artesian conditions → well flows without pumping)

HYDRAULIC GRADIENT:
  i = -dh/dl = -(Δh/L)
  Negative sign: flow is from high head to low head (down the gradient)
  Typical values: 1:1000 (0.001) in flat terrain to 1:100 in hilly areas
```

---

## Hydraulic Conductivity

```
HYDRAULIC CONDUCTIVITY K (m/s):
  Measure of ease of water flow through porous medium
  Depends on: pore geometry (rock/soil) + fluid viscosity

  K = k × ρg/μ
    k = intrinsic permeability (m²) — depends only on porous medium geometry
    μ = dynamic viscosity of water (~1×10⁻³ Pa·s at 20°C)
    → For oil (higher viscosity) in same rock: lower K

  VALUES ACROSS MATERIALS (K in m/s):

  Gravel:           10⁻² – 10⁻¹     (fastest, used for drains)
  Coarse sand:      10⁻⁴ – 10⁻²
  Medium sand:      10⁻⁵ – 10⁻³
  Fine sand:        10⁻⁶ – 10⁻⁴
  Silt:             10⁻⁸ – 10⁻⁵
  Clay:             10⁻¹⁰ – 10⁻⁸    (practically impermeable)
  Limestone (karst):10⁻⁶ – 10⁻²    (highly variable, secondary porosity)
  Fractured rock:   10⁻⁷ – 10⁻⁴    (depends on fracture density)
  Unfractured rock: 10⁻¹³ – 10⁻¹⁰

  8 orders of magnitude variation in common earth materials!

PERMEABILITY FIELD:
  K varies spatially (heterogeneous aquifer)
  Layered systems: effective K_horizontal >> K_vertical
  Fractures: extremely high local K, create preferential flow paths
  Representative elementary volume (REV): scale above which
    average K is meaningful (~10–100 × grain diameter)
```

---

## Aquifer Types

```
UNCONFINED AQUIFER (water-table aquifer):
  Top boundary: free water surface (water table) — at atmospheric pressure
  Bottom: bedrock or low-K aquitard
  Water table rises/falls with recharge/pumping
  Storage: water released by draining pores = specific yield Sy
  Typical Sy = 0.1–0.3 (fraction drained)

  WATER TABLE FLUCTUATION:
    Pumping: water table FALLS locally around well
    Recharge: water table RISES
    Mounding under recharge basins
    Seasonal fluctuation: typically 1–5 m in humid regions

CONFINED AQUIFER (artesian aquifer):
  Bounded above AND below by low-K aquitard
  Pressure head > elevation of top of aquifer → artesian conditions
  ARTESIAN WELL: water rises in well to piezometric surface level
                 FLOWING artesian well: piezometric surface above land surface

  Storage: water released by elastic compression/expansion of water and aquifer
  Storativity (storage coefficient) S = S_s × b
    S_s = specific storage (m⁻¹) = ρw g (α + n β)
      α = aquifer compressibility, β = water compressibility
    b = aquifer thickness
  Typical S = 10⁻⁵ – 10⁻³ (much smaller than unconfined Sy = 0.1–0.3)
  → Confined aquifers deliver water via compression, not draining

LEAKY AQUIFER (semi-confined):
  Top or bottom is low-K (but not zero) layer — leakance
  Pumping → head drops → leakage from adjacent aquifer
  Most aquifers in reality are "leaky" — pure confinement rare
  Leakance coefficient B: B = √(Tb') where T = transmissivity, b' = aquitard T
```

---

## Groundwater Flow Equations

### Governing PDE

```
LAPLACE EQUATION (steady, homogeneous, isotropic):
  ∇²h = 0
  → Same as electrostatics (Laplace for electric potential), heat conduction at steady state

DIFFUSION EQUATION (transient):
  S ∂h/∂t = T ∇²h      (confined aquifer)
  Sy ∂h/∂t = K ∇²h     (unconfined, Boussinesq approximation)

  S = storativity, T = transmissivity = K × b
  This is the HEAT EQUATION — identical mathematical form
  → All solutions from heat conduction apply to groundwater flow!
  → Theis solution = point source solution to the heat equation

  The mathematical equivalence:
    Temperature T ↔ Hydraulic head h
    Thermal diffusivity α ↔ Hydraulic diffusivity D = T/S
    Heat flux q = -k ∇T ↔ Darcy flux q = -K ∇h

ANISOTROPY:
  Natural aquifers: K_horizontal >> K_vertical
  Layered sediment: K_h / K_v ≈ 10–1000 (horizontal conducts much better)
  Aligned fractures: K in fracture orientation >> K perpendicular
  → Full form: q_i = K_ij ∂h/∂x_j (K becomes a tensor)
```

---

## Well Hydraulics — Theis Solution

```
THEIS (1935) SOLUTION FOR A PUMPING WELL (confined aquifer):

  s(r,t) = Q/(4πT) × W(u)

  Where:
    s = drawdown = h₀ - h (initial head minus current head) [m]
    Q = pumping rate [m³/s]
    T = transmissivity [m²/s]
    W(u) = well function = -Ei(-u) = -γ - ln(u) + u - u²/2! + ...
    u = r²S / (4Tt)
    r = distance from well [m]
    S = storativity [-]
    t = time since pumping began [s]

  PHYSICAL INTERPRETATION:
    Drawdown cone spreads radially from pumping well
    Rate of cone expansion ~ √(Tt/S)
    Peak drawdown at well, decreasing with r

  SMALL u APPROXIMATION (Cooper-Jacob, 1946):
    W(u) ≈ -0.5772 - ln(u)    valid for u < 0.01

    s ≈ Q/(4πT) × [-0.5772 - ln(r²S/4Tt)]
    s ≈ (2.303Q)/(4πT) × log(2.25Tt / r²S)

    This is LINEAR in log(t) — the basis for time-drawdown analysis!
    Plot s vs. log(t) on straight line → slope = 2.303Q/(4πT) → solve for T
    Extrapolate to s=0 → t₀ → solve for S

THEIS WELL FUNCTION TABLE:
  u        W(u)
  0.001    6.33
  0.01     4.04
  0.1      1.82
  1.0      0.219
  10.0     0.000
```

---

## Aquifer Testing

```
PUMPING TEST PROCEDURE:
  1. Measure initial water levels in pumping well + observation wells
  2. Pump at constant rate Q (measure with flowmeter)
  3. Record water level (head) vs. time in observation wells
  4. Analyze: plot s vs. t on log scale → type curve matching or Cooper-Jacob

  THEIS TYPE CURVE METHOD:
    Plot s vs. t on log-log paper → scale-shift to match Theis W(u) vs. 1/u curve
    Match point: read off (s, t, W(u), 1/u) simultaneously
    T = Q × W(u) / (4π × s)
    S = 4Tu × t / r²

  COOPER-JACOB STRAIGHT LINE METHOD:
    Plot s vs. log(t) → straight line portion (after u < 0.01)
    Slope Δs per log-cycle → T = 2.303Q / (4π × Δs)
    Extrapolate to s=0, t₀: S = 2.25T t₀ / r²

  RECOVERY TEST:
    Stop pumping → water levels recover
    Theis residual drawdown method: s' = Q/(4πT) × log(t/t')
    t = time since pumping started, t' = time since pumping stopped
    Same straight-line method → T (don't need exact S)
    Advantage: simpler, Q uncertainty less important

SLUG TEST (for low-K formations):
  Instantaneous removal or addition of water volume to well
  → head change vs. time analyzed (Hvorslev, Cooper-Bredehoeft-Papadopulos methods)
  Used where pumping tests not feasible (low K, small wells)
  Limitation: tests only immediate vicinity of well (1–5 m radius)
```

---

## Well Design and Protection

```
WELL CONSTRUCTION (top to bottom):

  Ground surface
  ┌───────────────────┐
  │   Grout seal      │
  │                   │
  │   Casing (steel   │
  │   or PVC pipe)    │
  │                   │
  │   Well screen     │
  │   (slotted pipe)  │
  │                   │
  │                   │
  │   Filter pack     │
  │   (gravel)        │
  └───────────────────┘
    Grout seal:   prevents contamination from surface.
    Casing:       structural support, keeps hole open.
    Well screen:  allows water in, keeps sand out;
                  pump intake typically in middle.
    Filter pack:  graded gravel around screen.
    Bottom plug:  closes the casing at the base.

WELL DESIGN PARAMETERS:
  Screen slot size: retain 90% of filter pack material
  Filter pack grain size: retain 90% of aquifer material × 4–6 factor
  Well radius: larger radius → larger Q for same drawdown
    BUT: Q ∝ 1/log(R/r_w) — logarithmic → diminishing returns above ~30 cm

WELLHEAD PROTECTION:
  WHPA (Wellhead Protection Area): zone around well
    1-day travel time: immediate protection zone (bacteria, protozoa)
    10-year travel time: pesticide, volatile contaminant zone
    Calculate: elliptical capture zone using Darcy velocity and porosity
  Groundwater travel time: t = L × n / q (porosity × distance / Darcy flux)
```

---

## Groundwater Contamination Basics

```
ADVECTION-DISPERSION EQUATION (ADE):
  ∂C/∂t + v ∂C/∂x = D ∂²C/∂x² - R_d(C)

  C = contaminant concentration
  v = pore velocity (= q/n)
  D = dispersion coefficient (mechanical + molecular diffusion)
  R_d = reactions (decay, sorption)

  This is: Convection-diffusion equation — same as heat equation + convection term

LONGITUDINAL DISPERSION:
  D_L = α_L × v + D_e
  α_L = longitudinal dispersivity (scale-dependent: 0.01 m to 100 m)
  D_e = effective diffusion coefficient
  → Plumes spread in travel direction; concentration front is smeared

RETARDATION (sorption to aquifer material):
  R = 1 + (ρ_b/n) × K_d
  R = retardation factor
  K_d = distribution coefficient (soil-water partition coefficient, mL/g)
  Actual contaminant speed = v/R
  Benzene (low K_d): R≈1 → travels fast
  DDT (high K_d): R>>1 → travels very slowly (barely moves)

PUMP-AND-TREAT LIMITATIONS:
  Theoretical: pump groundwater → treat → dispose
  Reality: residual contamination in low-K zones slowly leaches for decades
  DNAPL (Dense Non-Aqueous Phase Liquids: PCE, TCE): sink to bottom of aquifer
    Very difficult to remove → "DNAPL problem"
  Monitored Natural Attenuation (MNA): allow natural biodegradation + dilution
    Works for BTEX (benzene, toluene, ethylbenzene, xylene) in many cases
    Not for PCBs, heavy metals, fluorinated compounds (PFAS)
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Darcy's law in plain terms? | Groundwater flux = K × hydraulic gradient; identical form to Ohm's law (I = V/R) |
| What is transmissivity? | T = K × b; transmissivity = conductivity × saturated thickness (m²/s) |
| What is storativity? | S = volume of water released per unit head decline per unit area; S_confined << S_unconfined |
| What is an artesian well? | Confined aquifer with piezometric surface above ground → water flows without pumping |
| Theis solution for? | Drawdown in a confined aquifer as function of distance r and time t from a pumping well |
| Cooper-Jacob shortcut? | When u < 0.01: s vs. log(t) is linear → easy T and S calculation from slope |
| What does K depend on? | Pore geometry (intrinsic permeability) + fluid viscosity (temperature-dependent) |
| What is a slug test? | Instantaneous water level change → monitors recovery; estimates K near well only |

---

## Common Confusion Points

**Darcy velocity ≠ pore (seepage) velocity**: q (Darcy flux, specific discharge) is flow per unit total cross-sectional area — it's the bulk velocity. Actual water in pores moves faster by factor 1/n (porosity). If n=0.3, pore velocity = q/0.3 = 3.3× the Darcy velocity. Darcy velocity is useful for flow calculations; pore velocity is what contaminants actually travel at.

**Hydraulic conductivity K is NOT porosity**: High porosity doesn't mean high K. Clay has high porosity (40–60%) but low K (10⁻¹⁰ m/s) because pores are tiny and highly tortuous. Gravel has similar porosity (~35%) but K = 10⁻² m/s because pores are large. What matters for flow is pore SIZE and CONNECTIVITY, not just fraction of void space.

**Theis solution assumes infinite aquifer**: The key assumption is a laterally infinite, homogeneous, isotropic, fully penetrating well in a confined aquifer. Real conditions violate this. Boundary effects: recharge boundary (stream nearby) → drawdown less than Theis; barrier boundary (impermeable wall) → drawdown more than Theis. Image well method handles these with superposition.

**Pumping one well affects neighboring wells**: Because drawdown cones overlap. Pumping two wells close together → each well "sees" the other's drawdown → more total drawdown than one well alone. This is the multiple-well interference problem — superposition of Theis solutions gives total drawdown from multiple wells.

**"Fossil water" is not renewable on human timescales**: Deep confined aquifers (Ogallala, Arabian, Nubian) were recharged during wetter past climates (Pleistocene). Modern recharge is negligible. Pumping them is mining a finite resource. Ogallala Aquifer: average depletion 1–3 m/yr in some areas; natural recharge ~6 mm/yr. Net balance: massively unsustainable.
