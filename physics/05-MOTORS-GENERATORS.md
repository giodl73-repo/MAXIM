# Motors, Generators, and Transformers — Maxwell Made Mechanical

## The Big Picture

Two laws from Maxwell. Two machines from those laws. One chain from fire to light.

```
+------------------------------------------------------------------------+
|                  THE ELECTROMECHANICAL LANDSCAPE                       |
|                                                                        |
|   FARADAY'S LAW              LORENTZ FORCE LAW                        |
|   ∮ E·dl = -dΦ_B/dt          F = IL × B                               |
|   ─────────────────          ────────────────                         |
|   changing flux → EMF        current in B field → force               |
|         ↓                              ↓                              |
|     GENERATOR                        MOTOR                            |
|   (mechanical → electric)      (electric → mechanical)                |
|         ↑                              ↑                              |
|         └──────── same machine ────────┘                              |
|                                                                        |
|   TRANSFORMER: Faraday's law between two coils (no moving parts)      |
|                                                                        |
|   THE CHAIN:                                                           |
|   HEAT → STEAM → TURBINE → SHAFT → GENERATOR → ELECTRICITY            |
+------------------------------------------------------------------------+
```

Everything in this module is Faraday's law and the Lorentz force. The machines
are just those two laws arranged into useful geometry.

---

## EMF and Faraday's Law — The Generator Principle

**EMF** (electromotive force) is not a force — it is voltage induced around a
closed loop by a changing magnetic flux. Units: Volts.

```
  EMF = -dΦ_B/dt = -d/dt ∫∫_S B·dA
```

The negative sign is Lenz's law: the induced EMF drives a current whose
magnetic field opposes the change in flux. Nature resists change.

**Three ways to change Φ_B = ∫∫ B·dA:**

```
  1. Change |B|        — vary the field strength (electromagnet with varying current)
  2. Change area       — expand/contract the loop (motional EMF, sliding bar)
  3. Change angle      — rotate the loop in a fixed field ← how generators work
```

**The rotating coil**:

A coil of N turns, area A, rotating at angular velocity ω in a uniform field B:

```
  Φ_B(t) = NBA cos(ωt)       (flux varies as coil rotates)

  EMF(t) = -dΦ_B/dt = NBAω sin(ωt)
```

This is a **sinusoidal voltage** — AC comes naturally from rotation.
Peak EMF: ε₀ = NBAω. To increase output: more turns N, bigger area A,
stronger field B, faster rotation ω. Every AC generator ever built.

---

## DC Motor — Anatomy and Operation

A DC motor converts electrical energy to mechanical rotation using the
Lorentz force on current-carrying conductors in a magnetic field.

```
  DC MOTOR CROSS SECTION (simplified):

         N pole
          ║
     ┌────║────┐
     │    ║    │
     │  ──┼──  │   ← armature coil (current-carrying)
     │    ║    │
     └────║────┘
          ║
         S pole

  Current in armature: I
  Force on each side of coil: F = BIL
  These forces are in opposite directions → torque → rotation
```

**Torque on a current loop**:

```
  τ = NIAB sin θ

  N = turns, I = current, A = loop area, B = field, θ = angle between B and loop plane
  Maximum torque: θ = 90° (coil parallel to B)
  Zero torque: θ = 0° (coil perpendicular to B)
```

**The commutator problem**: as the coil rotates, the torque direction would
reverse every half turn without intervention. The commutator fixes this.

```
  COMMUTATOR:

  Split ring attached to coil shaft.
  Brushes (stationary contacts) press against split ring.

  First half turn:   brush A contacts segment 1 → current flows right in coil
  Second half turn:  brush A now contacts segment 2 → current reverses in coil
                     but coil has also flipped → net force still same direction

  Result: torque always in same rotational direction.
```

Real motors use multiple coil segments to smooth out the torque (less "cogging").

### Back-EMF — The Self-Regulating Mechanism

A spinning motor is also a generator — its rotating coil in a magnetic field
generates an EMF opposing the applied voltage (Faraday's law, Lenz's law).

```
  V_supply = EMF_back + I × R_armature

  At rest (ω = 0):      EMF_back = 0,   I = V_supply / R   ← SURGE CURRENT
  At full speed:        EMF_back ≈ V_supply,  I is small    ← normal operation
```

**Surge current on startup** can be 5-10× the running current. Large motors
use soft starters (resistors in series, gradually removed) or variable
frequency drives to limit startup current.

**Load behavior**: Add mechanical load → motor slows → less back-EMF →
more current drawn → more torque until new equilibrium. The motor
self-regulates current to match load. This is a natural control loop.

```
  BACK-EMF CONTROL LOOP:

  Load increases
       ↓
  Motor slows
       ↓
  Back-EMF decreases
       ↓
  More current drawn (V_back < V_supply)
       ↓
  More torque produced (τ = NIAB)
       ↓
  Motor speeds back up
       ↓
  New equilibrium
```

---

## DC Generator — Same Machine, Reversed

Run the motor with mechanical input instead of electrical input.
Spin the shaft → rotating coil in B field → changing flux → EMF → current out.

```
  MOTOR:      electrical in  →  mechanical out
  GENERATOR:  mechanical in  →  electrical out

  Same machine. Same equations. Direction of energy flow reversed.
```

A DC generator with a commutator produces pulsating DC (full-wave rectified sine).
Multiple coil segments smooth this to near-constant DC.

**Motional EMF** — the microscopic picture:
As the conductor moves through B with velocity v, the free electrons experience
Lorentz force F = qv×B, which drives them along the conductor — that's the EMF.
No magic, just charges being pushed by the magnetic force on them as they move.

```
  Conductor moving with velocity v in field B:

  Free electrons feel:  F = q(v×B)  — pushed along the conductor
  This charge separation → potential difference → EMF
  Connect a circuit → current flows
```

---

## AC Generator (Alternator)

Without a commutator — just slip rings that maintain continuous contact
without reversing the current. Output is pure sinusoidal AC.

```
  EMF(t) = NBAω sin(ωt)    ← directly the AC voltage waveform

  Peak voltage: V₀ = NBAω
  RMS voltage:  V_rms = V₀/√2  ← what your wall outlet voltage means

  US: 120 V_rms, 60 Hz  →  V₀ = 170 V peak
  EU: 230 V_rms, 50 Hz  →  V₀ = 325 V peak
```

The shaft is the prime mover input. Spin it with steam turbine, water
turbine, diesel engine, gas turbine — same electrical output.

---

## Transformer — Faraday Coupling, No Moving Parts

Two coils wound on a shared iron core. No electrical connection between them —
coupled purely through changing magnetic flux.

```
  PRIMARY COIL (N₁ turns, voltage V₁)
       │
  ─────┼──────────────────────────────
  │    │  IRON CORE (high μ)          │
  │    │  concentrates and guides flux│
  │    │                              │
  ─────┼──────────────────────────────
       │
  SECONDARY COIL (N₂ turns, voltage V₂)
```

**How it works**: AC in primary → changing current → changing Φ in core →
Faraday's law induces EMF in secondary.

```
  EMF₁ = -N₁ dΦ/dt
  EMF₂ = -N₂ dΦ/dt

  Same dΦ/dt (shared core), so:

  V₂/V₁ = N₂/N₁    ← TURNS RATIO

  Power conservation (ideal transformer):
  P_in = P_out  →  V₁I₁ = V₂I₂  →  I₂/I₁ = N₁/N₂
```

Step-up transformer (N₂ > N₁): higher voltage, lower current.
Step-down transformer (N₂ < N₁): lower voltage, higher current.

**Why transformers only work with AC**:
DC has constant current → constant flux → dΦ/dt = 0 → zero induced EMF.
The moment you plug DC into a transformer primary you have a short circuit
through the primary resistance (no back-EMF to limit current) → transformer
burns. Transformers require changing flux. This is why Edison (DC advocate)
lost the Current Wars to Tesla/Westinghouse (AC). AC transforms; DC doesn't.

### Power Transmission — Why High Voltage

Transmit power P over a line with resistance R:

```
  P = VI    →    I = P/V

  Line loss = I²R = P²R/V²

  Double the voltage → quarter the transmission losses
  10× the voltage → 100× less losses
```

```
  POWER GRID CHAIN:

  Generator       Step-up           Transmission      Step-down
  (10-25 kV)  → transformer  →  (115-765 kV)   →   transformer → Home (120/240 V)
                 N₂ >> N₁                              N₂ << N₁

  Long distance at ultra-high voltage (UHV): very low I, very low I²R loss.
  Dangerous to work with, not safe for homes → step down at substations.
```

Modern HVDC (high-voltage DC) transmission uses power electronics to convert
back to DC for long-distance runs — DC has no reactive losses, no skin effect.
But you still need AC transformers at the ends.

---

## AC Induction Motor — No Brushes, No Commutator

The workhorse of industry. Invented by Tesla. No mechanical contact between
stator and rotor.

**Principle**: A rotating magnetic field in the stator induces currents in
the rotor. Those induced currents in the external rotating field produce torque.

**Creating the rotating field** (three-phase):

```
  Three coils 120° apart, fed by three-phase AC (120° phase offset):

  V_a = V₀ cos(ωt)
  V_b = V₀ cos(ωt - 120°)
  V_c = V₀ cos(ωt - 240°)

  The net magnetic field from all three coils rotates at ω.
  No mechanically rotating parts in the stator.
```

**The squirrel cage rotor**: conducting bars embedded in iron, shorted at both ends.
The rotating field induces currents in these bars (Faraday's law).
The induced currents in the external rotating B field feel Lorentz force → torque.

**Slip**: the rotor must run slightly slower than the rotating field. If it
matched exactly, no relative motion → no changing flux → no induced current
→ no torque. The difference in speed (slip) is what drives the current and torque.

```
  Synchronous speed:  n_s = 120f/p    (rpm, f in Hz, p = number of poles)
  Rotor speed:        n_r = n_s(1-s)  where s = slip (typically 2-5%)
```

**Advantages over DC motor**: no brushes (wear), no commutator (sparks),
robust, cheap, easy to maintain. Virtually every industrial motor is AC induction.
Variable frequency drives (VFDs) control speed by varying the frequency f.

<!-- @editor[content/P2]: VFDs are mentioned but the guide stops at "varying frequency f." A reader doing modern motor control needs to know that VFDs are inverters: DC bus (rectified AC) → PWM switching of IGBTs at ~10 kHz → synthesized variable-frequency AC. Field-oriented control (FOC) / vector control decouples torque and flux control in induction motors, making them behave like DC motors in the control loop. Permanent magnet synchronous motors (PMSM / brushless DC) have replaced induction motors in EVs and precision drives. These are significant omissions for a reader connecting physics to modern engineering. -->

---

## Three-Phase Power

Three sinusoidal voltages, 120° apart in phase, on three wires:

```
  V_a = V₀ cos(ωt)          0°
  V_b = V₀ cos(ωt - 120°)   120° lag
  V_c = V₀ cos(ωt - 240°)   240° lag

  Sum at any instant: V_a + V_b + V_c = 0
```

**Why three-phase**:
- Constant total instantaneous power (no pulsation — single phase power pulses at 2f)
- Naturally creates rotating field for induction motors — no phase shifters needed
- More efficient wire utilization (three wires carry 3× the power of one)
- Neutral wire carries zero current in balanced load

**Delta and Wye configurations**:
- Wye (Y): one terminal from each phase connected at neutral point
  Line voltage = √3 × phase voltage (US: 120 V phase → 208 V line)
- Delta (Δ): phases connected in a triangle
  Line voltage = phase voltage

---

## Power Factor

In AC systems with reactive elements (inductors, capacitors — i.e., motors),
current and voltage are out of phase:

```
  V(t) = V₀ cos(ωt)
  I(t) = I₀ cos(ωt - φ)    φ = phase lag (inductive load: current lags voltage)

  REAL POWER:      P = V_rms × I_rms × cos φ    (W)  — what does useful work
  REACTIVE POWER:  Q = V_rms × I_rms × sin φ    (VAR) — stored/returned by L/C
  APPARENT POWER:  S = V_rms × I_rms            (VA)  — what generator must supply

  POWER FACTOR:  PF = cos φ = P/S
```

```
  PF = 1.0   Pure resistor: current and voltage in phase. All real power.
  PF = 0.8   Typical induction motor at partial load.
  PF = 0.0   Pure inductor: current 90° behind voltage. No real power.
```

**Why utilities care**: the generator and transmission lines must handle |S|
(apparent power), but you only pay for P (real power). Low PF means the utility
is supplying reactive current that does no useful work but heats the wires.
Industrial customers are charged penalties for low power factor.

**Correction**: add capacitors in parallel with inductive loads. Capacitor
current leads voltage; inductor current lags — they cancel.

---

## The Prime Mover Chain — Steam to Grid

All thermal power plants (coal, gas, nuclear) follow the same chain:

```
+──────────────────────────────────────────────────────────────────────+
│                       THERMAL POWER CHAIN                            │
+──────────────────────────────────────────────────────────────────────+
│                                                                      │
│  HEAT SOURCE                                                         │
│  Coal/gas combustion, nuclear fission, geothermal                   │
│       ↓  heat                                                        │
│  BOILER                                                              │
│  Water → high pressure steam (typically 500-600°C, 200+ bar)        │
│       ↓  steam                                                       │
│  STEAM TURBINE                                                       │
│  Steam expands, pushes turbine blades → shaft rotation              │
│  Multi-stage: high pressure → intermediate → low pressure           │
│       ↓  mechanical rotation (3000 rpm at 50 Hz, 3600 at 60 Hz)    │
│  GENERATOR (synchronous alternator)                                  │
│  Rotating shaft spins rotor with electromagnets in stator coils     │
│  → three-phase AC at grid frequency                                  │
│       ↓  electrical power                                            │
│  STEP-UP TRANSFORMER                                                 │
│  Generator voltage (typically 10-25 kV) → transmission (100-750 kV) │
│       ↓  high voltage AC                                             │
│  TRANSMISSION GRID                                                   │
│  Hundreds to thousands of km, very low losses                       │
│       ↓                                                              │
│  STEP-DOWN TRANSFORMERS (substations → distribution → homes)        │
│                                                                      │
│  EFFICIENCY AT EACH STAGE:                                           │
│  Boiler: 90%  ×  Turbine: 40%  ×  Generator: 98%  ×  Transform: 99%│
│  Overall thermal efficiency: ~35-40% (limited by Carnot)            │
│                                                                      │
│  Nuclear = same chain. Heat source is fission, not combustion.      │
│  The reactor just boils water. Everything downstream is identical.  │
+──────────────────────────────────────────────────────────────────────+
```

**Why 40% efficiency?** The steam turbine is a heat engine. Maximum efficiency
is given by the Carnot limit: η = 1 - T_cold/T_hot. With steam at 600°C
(873 K) and cooling water at 30°C (303 K): η_max = 1 - 303/873 = 65%.
Real turbines achieve ~40% due to irreversibilities. This is a thermodynamics
limit, not an engineering failure. The remaining 60% is waste heat.

---

## Losses and Efficiency

```
  COPPER LOSSES (I²R):
  Current flowing through winding resistance → heat
  Proportional to I² — double the current, quadruple the heat
  Reduce by using lower resistance wire (thicker, better material)

  IRON LOSSES (core losses):
  Two components:
  ├── Eddy currents: changing B induces circulating currents in core
  │   Power ∝ f² B² (worse at high frequency — why transformers use 50/60 Hz
  │   not higher)
  │   Reduce: laminate core (thin insulated layers break up eddy paths)
  └── Hysteresis: energy lost each time B-H curve is cycled
      Power ∝ f B_max^n (n ≈ 1.6-2)
      Reduce: use grain-oriented silicon steel (low hysteresis loss)

  MECHANICAL LOSSES (motors only):
  Friction in bearings, windage (air resistance on rotor)

  STRAY LOSSES:
  Leakage flux, non-uniform current distribution (skin effect in windings)
```

---

<!-- @editor[bridge/P2]: No bridge to control theory — the back-EMF feedback loop diagram is the best piece of this guide, but it's presented as a physics curiosity rather than connected to formal control theory. The back-EMF loop is a first-order lag with integrating action; it exhibits the same transfer function structure as a PI controller. A reader who knows Laplace transforms (from 6.003 / signals) will recognize the motor as a control plant — speed = integral of torque, back-EMF is a tachometer feedback, and the mechanical load is a disturbance. The connection to the control systems module (if it exists in this reference) or at minimum to block diagram notation belongs here. -->
## Decision Cheat Sheet

| Device | Principle | Key equation |
|--------|-----------|-------------|
| Generator | Faraday — rotating coil in B | EMF = NBAω sin(ωt) |
| Motor torque | Lorentz — current in B | τ = NIAB sin θ |
| Back-EMF | Lenz's law | V = EMF_back + IR |
| Transformer voltage | Faraday — shared flux | V₂/V₁ = N₂/N₁ |
| Transformer current | Power conservation | I₁/I₂ = N₂/N₁ |
| Why high V transmission | Reduce I²R loss | Loss = P²R/V² |
| Induction motor speed | Rotating field | n_s = 120f/p |
| Power factor | Phase angle | PF = cos φ = P/S |
| Thermal efficiency limit | Carnot | η < 1 - T_cold/T_hot |
| Eddy current reduction | Lamination | breaks current loops |

---

## Common Confusion Points

**Generators and motors are the same machine — only energy flow differs.**
A motor that is braked mechanically becomes a generator. An AC generator
run backwards (electrical input → mechanical output) is a synchronous motor.
Electric vehicles use the same motor for driving and regenerative braking.

**Back-EMF is not wasted energy — it's what limits current.**
Without back-EMF, a running motor would draw infinite current (limited only by
wire resistance). Back-EMF is the healthy sign that the motor is doing work.
A stalled motor (back-EMF = 0) draws maximum current and burns out.

**Transformers do not create power.**
V₂ > V₁ (step-up) means I₂ < I₁. The same power flows, just at different
V/I combination. A step-up transformer is not a free lunch.

**Why transformers fail with DC**.
AC: changing flux → back-EMF in primary = applied voltage (approximately).
Current = (V - back-EMF)/R = small.
DC: no changing flux → no back-EMF → current = V/R_wire ≈ very large → heat → fire.

**Three-phase neutral current is zero only for balanced loads.**
Single-phase loads (lights, outlets) drawn from three-phase systems unbalance
the phases, causing neutral current. Large commercial buildings balance loads
across phases to minimize neutral current.

**Slip is not waste — it's the torque mechanism.**
A zero-slip induction motor produces zero torque. Slip creates the relative
motion between rotor and field that induces rotor current that produces torque.
More load → more slip → more torque, up to the breakdown torque beyond which
slip increases but torque decreases (motor stalls).
