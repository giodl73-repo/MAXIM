# 02 — Propulsion

## Piston Engines, Gas Turbines, Rockets, Thermodynamic Cycles

---

## Big Picture: Propulsion Landscape

```
┌──────────────────────────────────────────────────────────────────────────┐
│                      PROPULSION TAXONOMY                                 │
├──────────────────────────┬───────────────────────────────────────────────┤
│  AIR-BREATHING           │  ROCKET (self-contained oxidizer)            │
├──────────────────────────┼───────────────────────────────────────────────┤
│  Piston/reciprocating    │  Chemical (liquid/solid/hybrid)              │
│  ├── 4-stroke Otto cycle │  ├── Liquid: LOX/LH2, LOX/RP-1, N2O4/UDMH  │
│  └── 2-stroke            │  ├── Solid: HTPB + ammonium perchlorate      │
│                          │  └── Hybrid: solid fuel + liquid oxidizer    │
│  Gas turbine             │                                               │
│  ├── Turbojet            │  Non-chemical                                │
│  ├── Turbofan            │  ├── Ion thruster (electric)                 │
│  ├── Turboprop           │  └── Nuclear (theoretical)                  │
│  ├── Turboshaft          │                                               │
│  └── Ramjet / Scramjet   │                                               │
└──────────────────────────┴───────────────────────────────────────────────┘

THRUST EQUATION (fundamental):
  T = ṁ_e V_e + (p_e - p_∞)A_e − ṁ_in V_∞
  Net: T = ṁ(V_e − V_∞) for non-pressure thrust, no inlet ram drag simplification
  More precisely (air-breathing): T = ṁ_exit V_exit − ṁ_inlet V_inlet + (p_e−p∞)A_e
```

---

## 1. Reciprocating (Piston) Engines

### Otto Cycle (Ideal 4-Stroke Gasoline)

```
FOUR STROKES: Intake → Compression → Power (combustion) → Exhaust

IDEAL OTTO CYCLE (p-v diagram):
  1→2: isentropic compression (piston up; adiabatic)
  2→3: constant-volume heat addition (spark ignition; combustion)
  3→4: isentropic expansion (power stroke)
  4→1: constant-volume heat rejection (exhaust valve opens)

THERMAL EFFICIENCY:
  η_th = 1 − 1/r^(γ-1)
  r = compression ratio = V_BDC / V_TDC
  γ = 1.4 for air (diatomic)
  Higher compression → higher efficiency → knock (pre-ignition) limits r to ~8-12 for gasoline
  Diesel cycle: constant-pressure combustion; higher r (14-22); higher efficiency; no knock

REAL ENGINE LOSSES:
  Pumping losses (intake/exhaust strokes)
  Heat transfer to cylinder walls
  Incomplete combustion
  Blow-by (leakage past rings)
  Friction

AIRCRAFT PISTON ENGINES:
  Horizontally opposed (flat): Lycoming, Continental; 4-6 cylinders; 100-300 hp
  Air-cooled: weight advantage; no coolant system
  Fuel: avgas 100LL (100 octane, low lead); moving toward unleaded UL94/UL100
  Turbocharged/supercharged: maintain manifold pressure at altitude (normally aspirated engines
    lose power with altitude: power ∝ ρ ∝ p)
  Magneto ignition: redundant dual magneto system (not battery-dependent)
  Constant-speed propeller: governor adjusts pitch to maintain rpm → optimal efficiency
```

---

## 2. Gas Turbine Engines — Brayton Cycle

### Ideal Brayton Cycle

```
FOUR COMPONENTS: Compressor → Combustor → Turbine → (nozzle or output shaft)

IDEAL BRAYTON CYCLE (p-s diagram):
  1→2: isentropic compression (compressor; raises p, T, ρ)
  2→3: constant-pressure heat addition (combustion)
  3→4: isentropic expansion (turbine; some; rest in nozzle)
  4→1: constant-pressure heat rejection (exhaust to atmosphere)

TEMPERATURE RATIOS:
  T₂/T₁ = (p₂/p₁)^((γ-1)/γ) = OPR^((γ-1)/γ)  [compressor exit]
  OPR = Overall Pressure Ratio = p₂/p₁
  T₄/T₃ = (p₄/p₃)^((γ-1)/γ)  [turbine exit]
  T₃ = Turbine Inlet Temperature (TIT); limited by material → ~1800-2000 K with cooling

THERMAL EFFICIENCY:
  η_th = 1 − 1/OPR^((γ-1)/γ) = 1 − T₁/T₂
  Higher OPR → higher efficiency
  Modern turbofans: OPR = 40-60
  GE9X (B777X): OPR = 60:1; T₃ ≈ 1750°C with blade cooling

SPECIFIC WORK:
  Compressor work: w_c = cp(T₂ - T₁)
  Turbine work: w_t = cp(T₃ - T₄)
  Net work: w_net = w_t - w_c
  Turbine must power compressor + produce shaft power/thrust
  Back-work ratio: w_c/w_t ≈ 0.4-0.5 (much higher than steam turbine)
    → Compressor isentropic efficiency matters enormously; polytropic efficiency
```

### Gas Turbine Variants

```
TURBOJET:
  All air through compressor → combustor → turbine → nozzle → high-velocity jet
  Turbine extracts only enough work to drive compressor
  Exhaust jet: high velocity, small mass flow → good thrust at high speed
  Propulsive efficiency η_p = 2V∞/(V_e + V∞) → low for V_e >> V∞ (most turbojets)
  Best at M > 2 (concorde: M 2.02; J-79: F-104/F-4 engines)

TURBOFAN:
  Additional large fan in front driven by extra turbine stages
  Bypass ratio (BPR): ṁ_bypass / ṁ_core
  Low BPR (0.1-2): military fighters (F-35: BPR 0.57; F-22: BPR 0.30)
  High BPR (4-10): early airliners (JT9D on 747: BPR 4.9; CFM56: BPR 5-6)
  Ultra-high BPR (10-20): modern airliners
    GE9X: BPR ~10; CFM LEAP: BPR ~9; PW GTF: BPR ~12-15

  Fan generates ~70-75% of thrust (high BPR) at subsonic conditions
  Why high BPR is efficient:
    η_p = 2V∞/(V_e + V∞) → want V_e close to V∞ (but V_e > V∞ for positive thrust)
    Fan accelerates large mass flow a little → better than small mass flow a lot
    Fan pressure ratio ~1.3-1.8; core pressure ratio very high (OPR = total)

  Trade-off: large fan → large nacelle → more nacelle drag + weight; cannot fit under wing
    A320neo: engine moved forward and up to fit LEAP/PW1100 under wing

TURBOPROP:
  Turbine extracts almost all expansion energy → drives propeller through gearbox
  Propeller: much larger mass flow than jet; very efficient at M < 0.65
  Residual jet thrust: ~10-15% total thrust
  Propeller efficiency: η_prop ≈ 0.85-0.90 at design point
  Gearbox: huge challenge; propeller ≈ 1000-1500 rpm; turbine ≈ 15,000-30,000 rpm
  Examples: PW100 (ATR-72, Dash-8); PT6A (Beechcraft, Pilatus); TP400 (A400M)

TURBOSHAFT:
  Extracts ALL power as shaft power; no jet thrust
  Helicopters, APUs, tanks (AGT-1500 in Abrams), ships
  GE T700: Black Hawk/Apache helicopter; 1,890 shp
  Rolls-Royce Gem: Lynx helicopter
  Power turbine: free turbine stage; mechanically decoupled from gas generator
```

---

## 3. Component Analysis

### Compressor

```
AXIAL COMPRESSOR:
  Alternating rotor (moving blades) + stator (stationary vanes) stages
  Each stage: small pressure ratio (≈1.1-1.3 per stage); 10-20+ stages in series
  Rotor: imparts velocity (kinetic energy) to air
  Stator: diffuses velocity to pressure rise (diffusion in passages)
  Work input per stage: Δh₀ = U × ΔVθ = U × (c_θ2 - c_θ1)  [Euler turbomachinery equation]
    U = blade speed; ΔVθ = change in tangential velocity

STALL/SURGE:
  Compressor stall: blade stall at high angle of attack (high pressure ratio or low mass flow)
    → individual stages stall; loss of pressure rise; noise
  Compressor surge: global flow reversal through compressor
    → violent oscillations; catastrophic if not corrected; blow-out or engine damage
  Surge line on compressor map: operating point must stay below/right of surge line
  Variable stator vanes (VSV): adjust stator angles during engine startup + off-design operation
    → move operating point away from surge line

CENTRIFUGAL COMPRESSOR:
  Impeller: throws air radially outward; diffuser converts velocity to pressure
  Single stage: high pressure ratio (3-8:1); simple; robust
  Used in: small engines, APUs, turboprops/turboshafts (PT6A), some helicopter engines
  Disadvantage: larger frontal area than axial for same mass flow

ISENTROPIC EFFICIENCY:
  η_c = (h₂s - h₁) / (h₂ - h₁) = ideal work / actual work
  Polytropic efficiency: η_c,poly = (γ-1)/γ × ln(p₂/p₁) / ln(T₂/T₁)
  For multistage compressor, use polytropic (small stage efficiency compounds)
  Typical: η_c,poly ≈ 0.88-0.92 for modern compressors
```

### Combustor and Turbine

```
COMBUSTOR:
  Diffuse air to ≈50 m/s (prevents flame blowout); primary zone at stoichiometric;
  dilution zone mixes to reduce TIT; liner cooling
  Emission constraints: NOx forms at high T; CO/HC from incomplete combustion
  ICAO NOx standards progressively tighter; lean burn combustors (GE TAPS, CFM TECT)
  TIT limits: single crystal Ni superalloys (~1000°C without cooling + TBC + air cooling → ~1750°C)

TURBINE:
  Highly loaded; air-cooled blades + TBC (thermal barrier coating: 7-8% yttria-stabilized zirconia)
  High-pressure turbine (HPT): 1-2 stages; drives compressor; highest pressure/temperature
  Low-pressure turbine (LPT): 4-7 stages; drives fan
  Blade materials: single crystal Ni superalloy (Rene N6, CMSX-4)
    Isotropic crystal orientation eliminates grain boundaries → removes creep paths
    Directionally solidified DS → single crystal SC → turbine blade evolution
  Turbine efficiency η_t ≈ 0.88-0.92 (polytropic)
```

---

## 4. Rocket Propulsion

### Fundamentals

```
SPECIFIC IMPULSE (Isp):
  Isp = thrust / weight flow rate of propellant = T / (ṁ_p × g₀)  [seconds]
  Higher Isp → more thrust per unit propellant weight
  Compare propellants:
    LOX/LH2: Isp ≈ 450 s vacuum (best chemical); cold, low density (large tanks)
    LOX/RP-1: Isp ≈ 370 s vacuum; dense, easy to handle (Falcon 9, Saturn V first stage)
    N2O4/UDMH: Isp ≈ 330 s; hypergolic (self-igniting); storable (no cryogenics)
    Solid APCP: Isp ≈ 260-280 s; simple; cannot throttle; SRBs, missiles
    Ion thruster (Xe): Isp ≈ 3000-10,000 s; tiny thrust; deep space (Dawn, Starlink)
    Nuclear thermal: Isp ≈ 900 s (theoretical); never flight-tested

TSIOLKOVSKY ROCKET EQUATION:
  Δv = Isp × g₀ × ln(m₀/m_f)
  Δv = mission velocity change (orbit insertion, Δv budget)
  m₀ = initial mass (full tanks); m_f = final mass (empty tanks)
  Mass ratio: m₀/m_f = exp(Δv / (Isp × g₀))
  Example: LEO Δv ≈ 9.4 km/s; Isp = 360 s
    m₀/m_f = exp(9400 / (360 × 9.81)) = exp(2.66) ≈ 14.3
    → 92% of liftoff mass must be propellant! → why rockets are hard

STAGING:
  Each stage: separate structure + engines; discarded when propellant exhausted
  Multi-stage allows each stage optimized for its conditions
  Stage N mass ratio: only that stage's propellant / that stage's (dry + upper stages)
  SpaceX Falcon 9: 2 stages; Stage 1 landing (recovery) critical to economics
  GLOW (Gross Liftoff Weight) of Falcon 9: 549,054 kg → payload to LEO: 22,800 kg (4.1%)
```

### Rocket Nozzle Design

```
DE LAVAL NOZZLE (convergent-divergent):
  Converging section: subsonic → sonic (M = 1 at throat)
  Diverging section: supersonic expansion
  Throat: minimum area; M = 1; choked flow (mass flow cannot increase with decreased back pressure)

IDEAL NOZZLE EXIT CONDITIONS:
  Perfectly expanded: p_e = p_∞ (maximum thrust; no pressure term)
  Over-expanded (p_e < p∞): outside air "squeezes" exhaust → thrust penalty; oblique shocks
    At extreme: flow separation inside nozzle
  Under-expanded (p_e > p∞): exhaust expands further after exit → pressure thrust + poor efficiency
    Seen: rocket exhaust plume expanding into large bell shape (SLS, Falcon 9 in vacuum)

AREA RATIO: A_e/A_t determines exit Mach and expansion ratio
  Higher area ratio → higher M_e → higher Isp in vacuum (Merlin vacuum: ε = 165:1)
  Sea-level nozzle limited by separation: ε typically 15-30:1
  Altitude-compensating nozzles: aerospike (expands against atmosphere; works at all altitudes)

PRESSURE-FED vs PUMP-FED:
  Pressure-fed: pressurant gas (He, N2) forces propellants into combustion chamber
    Simple; no turbopump; lower chamber pressure → lower Isp
    Used: small thrusters, RCS systems, some upper stages (Electron stage 1 is pump-fed)
  Pump-fed: turbopump pressurizes propellants to high chamber pressure → higher Isp
    Turbopump driven by tap-off from combustion gases:
      Open cycle (gas generator): exhaust turbopump drive gases overboard; less efficient
      Staged combustion: preburner burns some propellant to drive pump; all gas enters main chamber
        → higher chamber pressure → higher Isp; more complex
      Full-flow staged combustion: both oxidizer-rich and fuel-rich preburners
        SpaceX Raptor (Starship): first full-flow SC engine; Pc ≈ 330 bar; Isp ≈ 380 s SL
```

---

## 5. Ramjet and Scramjet

```
RAMJET:
  No compressor or turbine (moving parts); compression by ram effect of incoming air
  Requires M > ~0.5 to generate sufficient ram pressure; no static thrust
  Subsonic combustion; Mach 2-6 range
  Used: missiles (AIM-54, Talos), research aircraft (X-7)

SCRAMJET (Supersonic Combustion Ramjet):
  Supersonic combustion: incoming air remains supersonic through combustor
  Fuel injection and mixing in supersonic flow (residence time ~1 ms!) is extremely challenging
  M > ~5 required; Mach 5-25 target range
  Hyshot, X-51A Waverider: demonstrated sustained scramjet combustion
  No current operational aircraft; active research
  Combined cycle: TBCC (turbine-based combined cycle) or RBCC for Mach 0 → orbit transition
```

---

## Decision Cheat Sheet

| Engine Type | Speed Range | Efficiency Feature | Application |
|------------|------------|-------------------|-------------|
| Piston/Otto | M < 0.35 | Mechanical simplicity | GA, UAVs |
| Turboprop | M 0.3-0.65 | Propulsive efficiency | Regional/commuter |
| Turbofan BPR 5-10 | M 0.75-0.90 | High OPR + moderate BPR | Short-medium range |
| Turbofan BPR 10-15 | M 0.82-0.89 | Ultra-high BPR (GTF) | Long range wide body |
| Turbojet | M 1.5-3.0 | Compact; supersonic | Concorde, fighters |
| Ramjet | M 2.0-6.0 | No compressor moving parts | Missiles, experimental |
| Scramjet | M 5-25 | Supersonic combustion | Hypersonic concept |
| LOX/LH2 rocket | All (no air) | Highest Isp chemical | Upper stages, SLS core |
| LOX/RP-1 rocket | All | Dense; moderate Isp | First stages (Falcon 9) |
| Ion thruster | Deep space | Isp 3000-10,000 s | Satellites, deep space |

---

## Common Confusion Points

**Bypass ratio and total pressure ratio are not the same:** Bypass ratio is the ratio of fan flow to core flow (mass flows). Overall pressure ratio (OPR) is the total compression ratio through the core (fan × compressor stages). Both affect efficiency differently. GTF (Pratt & Whitney) high-BPR engines also need high OPR cores.

**Isp is measured in seconds because of g₀:** Isp = thrust / weight flow rate = N / (kg/s × 9.81) = seconds. Some use "effective exhaust velocity" c* = Isp × g₀ in m/s, which is more physically transparent. Isp in seconds is the standard.

**The Tsiolkovsky equation is brutal:** Doubling Δv requires squaring the mass ratio. Going to Mars requires Δv ≈ 5.7 km/s for trans-Mars injection, then you need to slow down at Mars... The mass ratio stacking is why multi-stage rockets are necessary and why SpaceX focuses on reusability.

**Staged combustion vs open cycle:** Staged combustion engines (SpaceX Merlin for turbopump, Raptor for everything) recycle the turbopump drive gases back into the main chamber — no wastage. Open cycle (gas generator) vents turbopump drive gases, wasting propellant but much simpler. Raptor's full-flow staged combustion is the most efficient rocket engine architecture yet operational.

**Thrust doesn't depend only on exhaust velocity:** T = ṁV_e + (p_e - p_∞)A_e. The pressure term matters at sea level. Over-expanded nozzles (p_e < p_∞) actually lose thrust from the pressure term. Under-expanded (p_e > p_∞) have additional thrust. Perfectly expanded nozzles have no pressure term, but require enormous area ratios in vacuum (RL-10 upper stage: area ratio = 250:1).
