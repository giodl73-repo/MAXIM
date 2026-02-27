# 03 — Nuclear Thermal Hydraulics

## Heat Generation, Coolant Flow, DNB, Reactivity Feedback

```
TEMPERATURE GRADIENT: FUEL CENTER → COOLANT BULK

   UO₂ Fuel          Gap    Clad         Coolant
   (ceramic)          │      │            │
                      │      │            │
   T_center ~1800°C   │      │            │ T_bulk ~300°C
       │              │      │            │
       │ parabolic     │      │ linear     │ log
       │ profile       │ jump │ profile    │ decay
       │              │      │            │
   T_surface ~400°C   │  300°C│ 330°C→350°C│ ──── T_sat (subcooled)
                      │      │            │
       ← k_fuel ~2W/mK→←k_gap→←k_clad ~15→←h·(T_clad-T_bulk)→

Total ΔT center-to-coolant: ~1400°C for typical PWR conditions
```

Nuclear thermal hydraulics links the neutronics (heat generation) to structural and safety limits.
The hierarchy: fuel temperatures → gap/clad temps → coolant conditions → DNB/CHF limit.
Exceeding limits in sequence leads to fuel damage → cladding failure → fission product release.

---

## Heat Generation in the Fuel

### Volumetric Heat Generation Rate

```
q''' = Σ_f · φ · Q_f  [W/m³]

where:
  Σ_f = macroscopic fission cross section [cm⁻¹]
  φ = neutron flux [n/(cm²·s)]
  Q_f = recoverable energy per fission ≈ 188 MeV = 3.0×10⁻¹¹ J

Typical PWR fuel rod:
  q''' ≈ (0.093 cm⁻¹)(3×10¹³ n/cm²·s)(3.0×10⁻¹¹ J) ≈ 8.4×10⁷ W/m³ = 84 MW/m³

Linear heat rate q' [W/m] = q''' · π R_fuel²
  Design limit: q' < 590 W/cm (prevents centerline melting in UO₂)
  Typical operating: q' ≈ 200–350 W/cm

Average rod power: q' ≈ 17.5 kW/m (typical PWR)
Assembly power: ~4.5 MW per 17×17 assembly
```

### Axial Flux and Power Profile

```
Axial power shape ≈ cosine (for unrodded, uniform fuel):
  q'(z) = q'₀ cos(πz/H_eff)   where H_eff = H + 2δ (extrapolation distance)
  q'₀ = peak linear heat rate at core midplane

Peak-to-average factor F_Δ (axial):
  For cosine: F_Δ = π/2 ≈ 1.57 → peak is 57% above average
  Rod insertion, xenon tilts, burnup all modify axial shape

Enthalpy rise hottest channel:
  ΔH = q' · L / (ṁ Cp)   q' = peak rod, L = channel length
```

---

## Radial Temperature Distribution in Fuel Rod

### Fuel Pellet Temperature Profile

```
For cylindrical fuel pellet with uniform heat generation q''' [W/m³]:

Heat equation: (1/r) d(r dT/dr)/dr = −q'''/k_f

Boundary conditions: T(R_fuel) = T_surface;  dT/dr|_{r=0} = 0 (symmetry)

Solution:  T(r) = T_surface + q'''(R_fuel² − r²)/(4 k_f)

At centerline (r = 0):
  T_center = T_surface + q''' R_fuel²/(4 k_f)

Or in terms of linear heat rate q' = q''' π R_fuel²:
  T_center = T_surface + q'/(4π k_f)

UO₂ thermal conductivity k_f:  strongly temperature-dependent
  At 300°C: k_f ≈ 6.1 W/m·K
  At 1000°C: k_f ≈ 3.0 W/m·K
  At 2000°C: k_f ≈ 2.2 W/m·K  (degraded at high T!)

UO₂ melting point: 2840°C (with 20% fission product depression → ~2700°C at high burnup)
Peak centerline temperature limit: ~2300°C (margin to melting)
```

### Gap Conductance

```
The UO₂-Zircaloy gap (~0.07 mm initially) is the largest thermal resistance:

1/h_gap = d_gap/k_gas + 2σ_σ/(σ₁ + σ₂ − σ₁σ₂) (roughness terms)

Gas composition:
  Fresh fuel: He fill gas → k_He ≈ 0.25 W/m·K at 400°C
  After burnup: fission gas release (Kr, Xe) → k_mix decreases
  → ΔT across gap increases with burnup → higher fuel temperatures at end of life

Contact pressure effects:
  Pellet swells with burnup + thermal expansion → gap closes
  Contact → h_gap increases dramatically (solid conduction)
  At ~15 GWd/tU: gap closure begins; hot-spot fuel temp may DECREASE despite higher burnup
```

### Cladding Temperature

```
Cladding (Zircaloy-4 or ZIRLO):
  Thickness: ~0.57 mm
  k_clad ≈ 13–20 W/m·K (temperature dependent)

ΔT across cladding:
  ΔT_clad = q'' · δ_clad / k_clad   where q'' = surface heat flux [W/m²]
  For typical q'' = 0.6 MW/m²: ΔT_clad ≈ 0.6×10⁶ × 5.7×10⁻⁴ / 15 ≈ 23°C

Outer cladding temperature limit:
  Operational limit: T_clad,outer < ~350°C (PWR coolant at ~310–340°C → small ΔT)
  Accident limit: T_clad < 1204°C (10 CFR 50.46 peak cladding temperature — PCT)
  Above ~1000°C: Zircaloy oxidizes rapidly: Zr + 2H₂O → ZrO₂ + 2H₂ (exothermic!)
  Above 1204°C: rapid oxidation + embrittlement → rod failure → fission gas release
```

---

## Coolant Energy Balance — Single Channel Model

### Single-Phase Forced Convection

```
Energy balance on coolant channel:
  ṁ Cp (dT_b/dz) = q''(z) · P_heated   [W/m]

where:
  ṁ = mass flow rate [kg/s]
  Cp = specific heat at constant pressure
  T_b = bulk coolant temperature (mixed mean)
  P_heated = heated perimeter of channel

Integrating from inlet (z=0) to height z:
  T_b(z) = T_in + ∫₀^z q''(z') P_h/(ṁ Cp) dz'

For cosine power shape:
  T_b(H) = T_in + q'₀ H/(ṁ Cp/P_h) × (2/π) sin(πz/H)

PWR typical values:
  T_in ≈ 291°C, T_out ≈ 327°C → ΔT_coolant ≈ 36°C
  Pressure ≈ 155 bar → T_sat ≈ 345°C (stays subcooled!)
  Flow velocity ≈ 4–5 m/s
```

### Convection Coefficient

```
Dittus-Boelter: Nu = 0.023 Re^0.8 Pr^0.4   (turbulent, Pr > 0.6)

For PWR coolant (pressurized water, ~310°C):
  Re ≈ 5×10⁵  (turbulent flow in rod bundle subchannel)
  Pr ≈ 1.0
  Nu ≈ 0.023 × (5×10⁵)^0.8 × (1.0)^0.4 ≈ 700
  h = Nu × k/D_h ≈ 700 × 0.56 / 0.012 ≈ 33,000 W/m²K

Clad surface temp:  T_clad = T_bulk + q''/h ≈ 310 + 600,000/33,000 ≈ 328°C
  → well below T_sat = 345°C → no significant boiling in nominal operation
```

---

## Boiling in Nuclear Systems

### Flow Regimes in Heated Channel

```
SUBCOOLED          SATURATED BOILING         POST-CHF
REGION             (quality increases)        REGION
  │                     │                        │
  ▼                     ▼                        ▼
Forced    → Onset of → Bubbly → Slug → Annular → Film boiling /
convection  Nucleate     flow    flow    flow     dispersed flow
(liquid)    Boiling
            (ONB)
              │                    ↑                    ↑
              │                    │                    │
              │               DEPARTURE            BURNOUT
              │               from NB              (CHF)

ONB: when T_wall > T_sat locally → bubbles nucleate on surface
  Subcooled nucleate boiling: vapor bubbles condense back into subcooled liquid
  Beneficial: enhanced heat transfer (h increases dramatically)

Nucleate boiling regime:
  q'' = h_nb × (T_wall − T_sat)^n   (highly nonlinear, n ≈ 2–3)
  Heat transfer enhanced 3–10× compared to forced convection
```

### Critical Heat Flux (CHF) and DNB

```
Critical Heat Flux (CHF): the heat flux above which film boiling occurs
  → vapor film blankets surface → sudden temperature excursion → fuel damage

CHF mechanisms:
  Subcooled/low-quality: departure from nucleate boiling (DNB) — Leidenfrost-like crisis
  High-quality: dryout — liquid film on annular flow walls evaporates

W-3 Correlation (PWR DNB):
  q''_CHF = {(2.022 − 0.0004302 P) + (0.1722 − 0.0000984 P) exp(18.177 − 0.004129 P)x}
           × [(0.1484 − 1.596x + 0.1729 x|x|) G/10⁶ + 1.037]
           × (1.157 − 0.869x) × [0.2664 + 0.8357 exp(−3.151 D_e)]
           × [0.8258 + 0.000794(H_f − H_in)]

  (P = pressure, x = quality, G = mass flux, D_e = hydraulic diameter, H = enthalpy)

<!-- @editor[bridge/P2]: DNBR is the thermal-hydraulic equivalent of a rate limiter with a hard threshold: the system operates safely within the nucleate boiling regime (analogous to sustainable queue depth), and DNB onset is the phase transition where the heat transfer mechanism collapses catastrophically — the thermal analog of a queue overflow or connection pool exhaustion. The DNBR ≥ 1.3 design margin is deliberately kept well above 1.0 for the same reason circuit breakers open before the actual failure threshold: you want the safety system to trigger before the physical limit is reached. The minimum DNBR occurring at the axial point of maximum heat flux maps exactly to a hot-spot analysis: find the worst-case node in the distribution, not the average. -->
Departure from Nucleate Boiling Ratio:
  DNBR = q''_CHF / q''_actual ≥ 1.3 (NRC design limit for PWR)
  Typical design: DNBR ≈ 1.7–2.0 at rated power
  Minimum DNBR (MDNBR) occurs at axial point of maximum heat flux

Safety significance: if DNBR < 1, fuel clad temperature spikes to ~700°C+
  → cladding fails → fission product release → loss of first barrier
```

---

## Hot Channel Factors

```
F_Q (total power peaking factor) = max local power / average power
  F_Q = F_N_Q × F_E_Q × uncertainty factors

  F_N_Q = nuclear factor (flux peaking from enrichment + rod patterns + burnup)
  F_E_Q = engineering factor (fuel pellet mass variations, clad eccentricity)

  F_Q ≤ 2.5 (typical PWR technical specification limit)
  → limits total peaking: no single location more than 2.5× average power

F_ΔH (enthalpy rise hot channel factor):
  = ratio of max-to-average enthalpy rise across the core
  F_ΔH = F_N_ΔH × engineering uncertainty
  F_ΔH ≤ 1.65 (typical limit)
  → limits DNBR exceedance in highest-enthalpy channel

Relationship:  F_Q = F_ΔH × F_Z (axial factor)
  F_Z depends on axial peaking — typically F_Z ≈ 1.5 for cosine distribution
```

---

## Two-Phase Flow

### Quality and Void Fraction

```
Quality x = steam mass flow / total mass flow = ṁ_vapor / (ṁ_vapor + ṁ_liquid)
  x = 0: saturated liquid;  x = 1: saturated vapor

Void fraction α = volumetric steam fraction = volume of vapor / total volume
  α ≠ x because vapor has much lower density

Slip ratio S = v_vapor / v_liquid  (velocities differ due to buoyancy)
  S > 1 (vapor moves faster than liquid)
  Homogeneous model: S = 1 (simplest)

Relationship: α = x / [x + S(1−x)(ρ_g/ρ_f)]

BWR coolant: x ≈ 12–15% quality at core exit
PWR coolant: x ≈ 0 (subcooled, no bulk boiling under normal conditions)
```

### Two-Phase Pressure Drop

```
Lockhart-Martinelli correlation:
  ΔP_TP = ΔP_liquid × Φ²_L   (two-phase multiplier)

  Φ²_L = 1 + C/X + 1/X²   (Martinelli parameter X)
  X² = (ΔP/dz)_liquid / (ΔP/dz)_gas

  For turbulent-turbulent:  X = [(1−x)/x]^0.9 × (ρ_g/ρ_f)^0.5 × (μ_f/μ_g)^0.1

Two-phase pressure drop matters for:
  → BWR stability analysis (density-wave oscillations)
  → LOCA blowdown calculation
  → Natural circulation loop driving head calculation
```

---

## Natural Circulation

### Driving Head

```
Natural circulation driving force = buoyancy due to density difference:

  ΔP_drive = (ρ_cold − ρ_hot) g H   [Pa]

  ρ_cold = density at cold leg entry (after steam generator cooling)
  ρ_hot = density at core exit (after fuel heating)
  H = elevation difference between core centerline and steam generator centerline

For PWR at 155 bar:
  ρ_cold ≈ 720 kg/m³,  ρ_hot ≈ 680 kg/m³  (after ~36°C heating)
  H ≈ 12 m (typical 4-loop PWR steam generator height above core)
  ΔP_drive ≈ (720−680) × 9.81 × 12 ≈ 4700 Pa

  This drives natural circulation after loss of RCP power
  AP1000 and passive designs amplify this by increasing H and eliminating flow resistance
```

### Decay Heat and Natural Circulation Capacity

```
Decay heat after shutdown (way-et al. correlation):
  P_decay(t) ≈ 0.066 P₀ [(t−t_s)^−0.2 − t^−0.2]  (seconds after shutdown at t_s)

  At t = 1 s after shutdown: P_decay ≈ 6–7% of full power
  At t = 1 hr: P_decay ≈ 1.5%
  At t = 1 day: P_decay ≈ 0.5%
  At t = 1 week: P_decay ≈ 0.1%

  → Must remove decay heat even with no coolant pumps
  Natural circulation typically provides 5–7% of forced flow rate
  → adequate for decay heat removal (need ~1–3% of rated flow)

Fukushima lesson: natural circulation and RCIC worked initially; failure of ECCS/AC power
  ultimately prevented adequate long-term decay heat removal
```

---

## Loss of Coolant Accident (LOCA) Thermal Response

### LOCA Phases

```
LARGE-BREAK LOCA (double-ended guillotine break of large-diameter pipe):

  Phase 1: BLOWDOWN (0 – ~30 s)
    → primary pressure drops from ~155 bar to saturation
    → bulk flashing → rapid void formation → flow reversal
    → core uncovery begins → decay heat with no cooling
    → peak cladding temperature starts to rise

  Phase 2: REFILL (~30 – ~200 s)
    → ECCS injection begins (accumulators ~10 bar)
    → lower plenum fills with ECCS water
    → core still uncovered → continued heatup
    → Peak Cladding Temperature (PCT) occurs during this phase

  Phase 3: REFLOOD (~200 s onward)
    → water front moves up through core → quenching
    → steam binding can slow reflood (steam must vent upward through core)
    → eventually core fully covered → normal decay heat removal resumes

  PCT LIMIT: ≤ 1204°C (10 CFR 50.46)
  Max oxidation: ≤ 17% of cladding thickness as ZrO₂ (embrittlement limit)
  Coolable geometry: core must remain coolable (no rod swelling/blockage)
```

### SMALL-BREAK LOCA (SB-LOCA)

```
Small pipe break (2-6" diameter): slower depressurization
  Pressurizer heaters keep primary subcooled initially
  Break flow rate < MFP (makeup pump) capacity → slow level decrease

  Challenge: Loss of natural circulation (loop seal clearing)
    Steam accumulates in u-tube bends of steam generators
    → flow stagnates → hotter core temperatures
    IMPORTANT: Three Mile Island was an SB-LOCA (stuck-open PORV)

  SB-LOCA mitigated by:
    High-pressure injection
    Pressurizer pressure control (PORV blocking, pressurizer heaters)
    Operator action to depressurize if HPIS inadequate
```

---

## Fuel Performance Limits

### Pellet-Cladding Interaction (PCI)

```
PCI: rapid power increase → pellet expands faster than cladding → mechanical + chemical attack

Mechanism: fission products (I, Cs) stress-corrosion cracking of Zircaloy
  Critical: rapid ramp rates (> 0.5 kW/m·hr for some conditions)

Prevention:
  Conditioning: ramp up slowly → pellet and clad creep together
  Liner cladding: Zr or Cu liner on inner surface
  Technical specification limits: limited power ramp rates during startup/reload
```

### Fission Gas Release

```
Kr, Xe generated by fission → initially trapped in UO₂ grains
At high temp (> ~1100°C): diffuse to grain boundaries → collected in pores → plenum

Fuel rod internal pressure limit: rod pressure ≤ primary coolant pressure
  (to prevent gap opening → gap conductance decrease → higher fuel temps → more gas)

At high burnup (>45 GWd/tU): significant gas accumulation → pressure buildup
  Design: rod plenum sized for expected gas release over lifetime
  Thermal cycling: gas can pressurize beyond design if fuel runs hot

Significance: fission gas release:
  → Indicator of fuel damage (detected in coolant activity monitors)
  → Increases rod pressure
  → Increases thermal resistance across gap (Xe is poor conductor)
```

---

## Common Confusion Points

**Centerline melting vs cladding failure:** Two separate limits. Centerline melting
(UO₂ → liquid) at ~2840°C destroys fuel pellet geometry but does not immediately
release fission products (cladding still intact). Cladding failure at >1204°C (PCT limit
during accidents) releases fission gas. Both must be prevented; PCT is the binding
accident limit under 10 CFR 50.46.

**DNBR < 1 doesn't mean immediate fuel failure:** It means film boiling onset, which
causes a dramatic temperature spike in the cladding. Cladding fails when PCT > ~1200°C
or when Zircaloy oxidation exceeds 17% of wall thickness. DNB initiates the transient;
whether fuel fails depends on how long it persists.

**Decay heat cannot be turned off:** Even with control rods fully inserted, fission product
β/γ decay continues. At 1 second post-shutdown it's ~6% of full power. This is why
you need ECCS and decay heat removal systems — not just control rods — to keep a reactor
safe after shutdown. Fukushima: rods inserted (fission stopped), decay heat was the problem.

**Two-phase pressure drop creates instability in BWRs:** Density-wave oscillations
occur when flow rate and two-phase pressure drop couple. This can cause power oscillations
at low-flow/high-power conditions. BWRs have stability maps (operating limits) to avoid.
PWRs are subcooled — no two-phase instability concern in normal operation.

---

## Decision Cheat Sheet

| Thermal-hydraulic question | Approach | Key formula/limit |
|---------------------------|----------|------------------|
| Centerline fuel temperature | Parabolic profile | T_c = T_s + q'/(4π k_f) |
| Clad surface temperature | Forced convection | T_clad = T_bulk + q''/h |
| Will DNB occur? | DNBR check | DNBR = q''_CHF/q''_actual ≥ 1.3 |
| Coolant exit temperature | Energy balance | ΔT = q'_avg × L/(ṁ Cp/P_h) |
| Natural circulation feasible? | Driving head | ΔP = (ρ_cold − ρ_hot) g H |
| Decay heat magnitude | Way-et al. | ~6% at 1s, ~1.5% at 1hr, ~0.5% at 1day |
| LOCA PCT compliance | 10 CFR 50.46 | PCT ≤ 1204°C, oxidation ≤ 17% |
| Two-phase flow pressure drop | Lockhart-Martinelli | Φ²_L = 1 + C/X + 1/X² |
| Gap conductance at burnup | Gas composition | He→Xe/Kr degradation at high burnup |
| Power peaking limit | F_Q | F_Q ≤ 2.5 typical PWR |
