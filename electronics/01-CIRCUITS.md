# 01 — Circuit Analysis Fundamentals

```
CIRCUIT ANALYSIS LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  Sources + Elements                      Analysis builds upward:
  ────────────────────                    ────────────────────────────────────
  V/I sources (indep/dep)                 Layer 1: KVL/KCL
  R, C, L, Z(s)                              Write equations from topology
                 │                                    │
                 ▼                                    ▼
            ┌─────────────────────────────────────────────┐
            │  Layer 2: Node Voltage / Mesh Current       │
            │  Systematic approach: converts circuit into │
            │  system of linear equations Ax = b          │
            └─────────────────┬───────────────────────────┘
                              │
                              ▼
            ┌─────────────────────────────────────────────┐
            │  Layer 3: Thévenin / Norton Equivalents     │
            │  Reduce any subcircuit to V_th + R_th       │
            │  Enables interface thinking: source → load  │
            └─────────────────┬───────────────────────────┘
                              │
                              ▼
            ┌─────────────────────────────────────────────┐
            │  Layer 4: Op-Amp Analysis                   │
            │  Golden rules (V+=V−, I_in=0) from         │
            │  negative feedback + high open-loop gain    │
            │  Builds on Layers 1–3 for each topology    │
            └─────────────────────────────────────────────┘

  6.002 bridge: This is the 6.002 core. 30-year refresher for intuition,
  not re-derivation from first principles.
```

---

## 1. Kirchhoff's Laws

### KVL — Kirchhoff's Voltage Law

```
  Around any closed loop: ΣVₖ = 0

  Physical basis: Conservative electric field in lumped circuits.
    ∮ E·dl = 0  →  sum of voltage drops around loop = 0.

  Sign convention:
    Trace the loop in a chosen direction.
    + if you enter the + terminal of element
    − if you enter the − terminal

  Example — single loop:
    +Vs - V_R1 - V_R2 = 0
    Vs = IR1 + IR2 = I(R1 + R2)
    I = Vs/(R1 + R2)    ← voltage divider
```

### KCL — Kirchhoff's Current Law

```
  At any node: ΣIᵢₙ = ΣIₒᵤₜ     (charge conservation)
  Equivalently: Σ Iₖ = 0  (with sign convention on currents)

  Physical basis: Charge cannot accumulate at a node (lumped circuit model).
    ∇·J = 0  →  KCL.

  Current divider (two parallel resistors R1, R2):
    I₁ = I_total · R2/(R1+R2)
    I₂ = I_total · R1/(R1+R2)
    (current takes path inversely proportional to resistance)
```

---

## 2. Resistor Combinations

```
  Series:    R_eq = R₁ + R₂ + ... + Rₙ          (currents equal)
  Parallel:  1/R_eq = 1/R₁ + 1/R₂ + ... + 1/Rₙ  (voltages equal)

  Two in parallel: R_eq = R₁R₂/(R₁+R₂)  ← memorize this

  Y-Δ / Star-Delta conversion:
    R_Y → R_Δ: each Δ resistor = sum of adjacent Y / opposite Y
    Useful when neither series nor parallel simplification works.
```

### Voltage Divider

```
  Vs ──R1──┬──R2── GND
           │
           V_out

  V_out = Vs · R2/(R1+R2)

  Valid only when no current drawn from output (load = ∞).
  With finite load R_L: R2 is replaced by R2||R_L.
```

---

## 3. Node Voltage Method

```
  Best when: fewer nodes than meshes.

  Steps:
  1. Choose reference node (ground, V = 0)
  2. Label all other nodes V₁, V₂,...
  3. Write KCL at each non-reference node:
       ΣI leaving node = 0
       (V_n - V_neighbor)/R = 0 for each branch
  4. For voltage sources: constraint equation V_a - V_b = Vs
     (supernode if source between two non-reference nodes)
  5. Solve system of linear equations.

  Example — two-node circuit:
    V₁ is unknown.
    (V₁ - Vs)/R₁ + V₁/R₂ = 0     ← KCL at node 1
    V₁/R₂ - V₁/R₁ + Vs/R₁ = 0
    V₁(1/R₁ + 1/R₂) = Vs/R₁
    V₁ = Vs · R₂/(R₁+R₂)         ← same as voltage divider ✓
```

---

## 4. Thévenin and Norton Equivalents

```
  Any linear two-terminal circuit can be replaced by:

  Thévenin:               Norton:
    ┌──────Vth──────┐       ┌────────────────┐
    │              │        │                │
   Rth            Load     Isc   Rth(=Vth/Isc)   Load
    │              │        │                │
    └──────────────┘        └────────────────┘

  Finding Thévenin equivalent:
    Vth = V_oc   (open-circuit voltage at terminals)
    Rth = V_oc / I_sc   (open circuit / short circuit)
    OR: Rth = resistance seen at terminals with all independent sources killed
              (voltage sources → short, current sources → open)

  Norton equivalent:
    Isc = I_sc  (short-circuit current)
    Rth same as Thévenin

  Max power transfer: Load receives max power when R_load = R_th
    P_max = Vth² / (4·Rth)
```

### Why Thévenin Matters

```
  Real-world use:
    - Amplifier output impedance = Thévenin Rth seen at output
    - Source driving a load: effective voltage source + series impedance
    - Signal chain: each stage has Thévenin output, next stage is load
    - Interface design: want low Rth_out, high Rin (for voltage)

  Impedance matching:
    Power transfer: R_source = R_load (conjugate match in AC)
    Signal voltage: R_source << R_load (voltage divider doesn't divide)
    Signal current: R_source >> R_load
```

---

## 5. Superposition

```
  In linear circuits, the response to multiple sources = sum of responses
  with each source active individually (others killed).

  Kill: voltage source → short circuit
        current source → open circuit

  Not applicable to nonlinear elements (diodes, transistors in general).

  When to use: circuit with multiple sources, need contribution of each.
  When NOT: dependent sources stay active (only kill independent sources).
```

---

## 6. Op-Amp Analysis

### Ideal Op-Amp Model

```
  ┌───────────────────────────────────────────────────────┐
  │  Op-amp golden rules (for negative feedback circuits): │
  │                                                         │
  │  Rule 1: V+ = V−   (virtual short — inputs equalize)   │
  │  Rule 2: Iin = 0   (no current into inputs)            │
  │                                                         │
  │  Open-loop gain A → ∞, Rin → ∞, Rout → 0              │
  └───────────────────────────────────────────────────────┘

  These rules are consequences of large open-loop gain + negative feedback.
  Without feedback: output saturates to ±Vs. Rules require feedback.
```

### Inverting Amplifier

```
         R_f
    ┌────┤├────┐
    │          │
  Vin ──R_in──(−)──── Vout
               (+)──GND

  Apply golden rules:
    V- = V+ = 0   (virtual ground at − input)
    I_in = Vin/R_in flows through R_f (KCL: no current into op-amp)
    Vout = -I_in · R_f = -Vin · R_f/R_in

  Gain: A_v = Vout/Vin = -R_f/R_in    (inverting, magnitude = R_f/R_in)
```

### Non-Inverting Amplifier

```
  Vin ──────(+)────── Vout
             (−)──┤├──GND
                 R₁   R₂

  V- = Vout · R₁/(R₁+R₂)   (voltage divider from Vout to GND)
  V+ = Vin
  Golden rule: V+ = V-
    Vin = Vout · R₁/(R₁+R₂)
  Gain: A_v = 1 + R₂/R₁    (non-inverting, gain ≥ 1)
```

### Voltage Follower (Buffer)

```
  Vin ──(+)──── Vout
         (−)──── Vout  (direct feedback)

  V- = Vout,  V+ = Vin → Vout = Vin
  Gain = 1, but: Rin = ∞, Rout = 0  ← the valuable property
  Use: impedance buffer. Drive a low-impedance load from high-impedance source.
```

### Summing Amplifier

```
      R_f
  ┌───┤├────────┐
  │             │
  V₁ ──R₁──(−)──── Vout
  V₂ ──R₂──
  V₃ ──R₃──
            (+)──GND

  Virtual ground at − input.
  Currents: I₁=V₁/R₁, I₂=V₂/R₂, I₃=V₃/R₃ all flow into feedback R_f.
  Vout = -R_f(V₁/R₁ + V₂/R₂ + V₃/R₃)
  If all R equal: Vout = -(V₁+V₂+V₃) · R_f/R
```

### Difference Amplifier

```
  Vout = (R_f/R_in)(V₂ - V₁)  when all resistors matched R_in/R_f
  CMR: rejects signals common to both inputs — key for sensor interfaces.
```

### Integrator

The op-amp integrator is where circuit analysis directly meets control theory: H(s) = -1/(sRC) is a pure integrator in the Laplace domain — the same transfer function that appears in the "I" term of a PID controller. Analog PID controllers were historically built from exactly these op-amp blocks (integrator for I, differentiator for D, summing amplifier to combine). See 05-SIGNALS-SYSTEMS for the full s-domain framework and control-theory/01-PID-CLASSICAL for the control perspective.

```
       C
  ┌────┤├────┐
  │          │
  Vin ──R──(−)──── Vout
            (+)──GND

  I = Vin/R flows through C.
  Vout = -(1/RC)∫Vin dt
  In s-domain: H(s) = -1/(sRC)
  Pole at s=0 → integrates; DC input → output ramps → saturation risk.
```

### Differentiator

```
       R_f
  ┌────┤├────┐
  │          │
  Vin ──C──(−)──── Vout
           (+)──GND

  Vout = -R_f·C · dVin/dt
  In s-domain: H(s) = -sR_fC
  Zero at s=0. Amplifies high-frequency noise → practical differentiators
  add small R in series with C to limit high-freq gain.
```

---

## 7. Common Op-Amp Configurations Summary

| Configuration | Gain | Key Feature |
|---|---|---|
| Inverting | -R_f/R_in | Virtual ground at input |
| Non-inverting | 1+R_f/R_in | High input impedance |
| Voltage follower | 1 | Impedance buffer |
| Summing | -R_f·Σ(Vᵢ/Rᵢ) | Weighted sum |
| Difference | R_f/R_in · (V₂-V₁) | Common-mode rejection |
| Integrator | -1/(sRC) | Integrates over time |
| Differentiator | -sR_fC | Differentiates (noisy) |
| Instrumentation amp | (1+2R/R_g)·diff | Very high CMR |
| Comparator | ±Vsat (open loop) | No negative feedback |
| Schmitt trigger | Hysteresis ΔV = ±β·Vsat | Noisy signal → clean switch |

---

## 8. Decision Cheat Sheet

| Situation | Method |
|---|---|
| Find current in simple series/parallel | Ohm's law + series/parallel combination |
| Multiple voltage/current sources | Superposition or node voltage |
| Find voltage at multiple nodes | Node voltage method |
| Find current in multiple loops | Mesh current method |
| Replace complex subcircuit with simple equivalent | Thévenin/Norton |
| Amplify with controlled gain | Op-amp inverting or non-inverting |
| Buffer (high-Z source → low-Z load) | Voltage follower |
| Add weighted signals | Summing amplifier |
| Measure differential signal, reject common mode | Difference or instrumentation amp |
| Integrate control error | Op-amp integrator |

---

## 9. Common Confusion Points

**1. Virtual ground ≠ real ground**
In inverting amplifier, V- = 0 (virtual ground) because negative feedback holds it there. But current still flows through R_in into the node and through R_f out. The current path goes Vin → R_in → virtual ground → R_f → Vout. If you break the feedback, virtual ground disappears and output saturates.

**2. KCL counts current directions, not magnitudes**
Assign all unknown currents directions arbitrarily. If an answer comes out negative, the current actually flows opposite to your assumed direction. The algebra handles it — never flip signs mid-calculation.

**3. Thévenin resistance calculation — kill sources correctly**
Dependent sources are NOT killed (they depend on circuit variables which would change if killed). Only independent sources are killed. For circuits with dependent sources, find Rth via Voc/Isc, not by killing and looking.

**4. Op-amp golden rules require negative feedback**
Without negative feedback (or with positive feedback), the output swings to the rail — golden rules do not apply. Comparators, Schmitt triggers, and oscillators all involve positive feedback or open-loop operation where the golden rules are explicitly violated.

**5. Node voltage method: supernode for voltage sources**
If a voltage source connects two non-reference nodes, you have a supernode. Write one KCL equation for the combined supernode (sum of currents entering both nodes from outside) plus the constraint V_a - V_b = Vs. Don't try to write separate KCL for each node — you'd need a branch current through the ideal voltage source which is indeterminate.

**6. Max power transfer ≠ maximum efficiency**
At R_load = R_Thévenin, exactly half the available voltage drops across R_th and half across R_load. Power to load = Vth²/(4Rth), but efficiency = 50% — half is wasted in R_th. Power transmission (grid) uses R_load >> R_source for efficiency. Audio amplifiers use conjugate impedance matching for max power. These are different design objectives.
