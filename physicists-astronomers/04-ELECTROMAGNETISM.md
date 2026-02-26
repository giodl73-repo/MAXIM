# Electromagnetism — Faraday, Maxwell, Hertz, Lorentz, Tesla

## The Central Achievement: Unifying Electricity, Magnetism, and Light

```
THE ELECTROMAGNETIC STORY
==========================

FARADAY (1820–1851): Experiments show electricity and magnetism are connected.
  - A moving magnet creates a current (induction).
  - A current creates a magnetic field.
  - Introduced the concept of "field."
  - No mathematics — pure experimental genius.

MAXWELL (1865): Unifies everything in 4 equations.
  - Electric and magnetic fields obey coupled wave equations.
  - The wave speed = 1/√(ε₀μ₀) ≈ 3 × 10⁸ m/s = speed of light.
  - Light IS an electromagnetic wave.
  - Predicts radio waves (and all electromagnetic radiation).

HERTZ (1887): Experimentally confirms Maxwell's prediction.
  - Creates and detects radio waves in the lab.
  - Dead at 36 from bone disease.

LORENTZ (1892–1904): Shows Maxwell's equations are invariant under what
  we now call Lorentz transformations. Length contraction, time dilation.
  Einstein (1905) gives the correct physical interpretation.

TESLA (1880s–1890s): Engineers AC power, making electrical grids practical.
  More engineer than physicist, but transformative.
```

---

## Michael Faraday (1791–1867)

### Who He Was

English physicist and chemist. Son of a blacksmith. Started as a bookbinder's
apprentice, attended public lectures by Humphry Davy, wrote up notes and
sent them to Davy — hired as laboratory assistant. Eventually Faraday surpassed
Davy entirely. Never mastered mathematics; did all his physics through experiment
and geometric reasoning about field lines.

### The Contribution: The Field Concept and Electromagnetic Induction

**Electromagnetic Induction (1831)**

```
FARADAY'S LAW OF INDUCTION
============================

A changing magnetic flux through a loop induces an EMF (voltage).

  EMF = -dΦ_B/dt

  Φ_B = ∫∫ B⃗ · dA⃗  (magnetic flux through a surface)
  EMF = -dΦ_B/dt    (Faraday's law — the minus sign is Lenz's law)

Lenz's law: The induced current flows in a direction to OPPOSE the change
  in flux. (Conservation of energy — the induced current does negative work
  against the change causing it.)

APPLICATIONS:
  Generator: rotate a coil in a magnetic field → changing flux → EMF.
    Every power plant in the world generates electricity this way.

  Transformer: changing current in primary coil → changing B field →
    changing flux through secondary coil → induced EMF.
    The entire AC power grid depends on transformers (step up/down voltage).

  Induction motor: rotating magnetic field induces current in rotor,
    which then feels force in the field → rotation.
    (Tesla's induction motor, File 04.)
```

**The Field Concept**

Before Faraday, action-at-a-distance was accepted: charges and magnets
reached across empty space to attract or repel. Faraday rejected this.
He visualized "field lines" — real entities filling space, carrying the
electromagnetic interaction.

```
FARADAY'S FIELD LINES
======================

Electric field lines: point from + charges to - charges.
  The field E⃗ at a point = force per unit charge placed there.
  E⃗ is a vector field filling all space.

Magnetic field lines: form closed loops around current-carrying wires.
  B⃗ = magnetic field.
  Field lines never start or end (no magnetic monopoles).

The field stores energy:
  Energy density in electric field: u_E = ε₀E²/2
  Energy density in magnetic field: u_B = B²/(2μ₀)

Maxwell formalized Faraday's intuitive field picture into mathematical equations.
```

**Faraday's Other Contributions**

- Benzene discovery (1825)
- Electrolysis laws: the mass of substance deposited is proportional to charge
  (Q = nF·m/M, where F = Faraday constant = 96,485 C/mol)
- Faraday cage: a conductor shields its interior from external electric fields
  (the charge redistributes to cancel the field inside)
- Faraday effect: a magnetic field rotates the polarization of light in a medium

---

## James Clerk Maxwell (1831–1879)

### Who He Was

Scottish physicist. Cambridge-educated. Published the Maxwell equations in 1865
at age 34. Died of abdominal cancer at 48. Had he lived to 60, he might well
have developed special relativity — everything he needed was in his equations.

### The Contribution: Maxwell's Equations

**The Four Equations**

```
MAXWELL'S EQUATIONS (in differential form)
============================================

In SI units:

∇ · E⃗ = ρ/ε₀              (Gauss's Law for E)
∇ · B⃗ = 0                  (Gauss's Law for B — no magnetic monopoles)
∇ × E⃗ = -∂B⃗/∂t            (Faraday's Law)
∇ × B⃗ = μ₀J⃗ + μ₀ε₀∂E⃗/∂t  (Ampère-Maxwell Law)

READING THEM:
  1. Electric charges create diverging electric field.
  2. Magnetic field lines form closed loops (no sources/sinks).
  3. Changing magnetic field creates circulating electric field.
  4. Electric currents AND changing electric fields create
     circulating magnetic field.

THE KEY ADDITION — Maxwell's "displacement current" (μ₀ε₀∂E⃗/∂t):
  Without this term, the equations were Faraday/Ampère's laws.
  Maxwell added it for consistency (required by charge conservation).
  This addition changes everything.
```

**The Light Equation**

```
ELECTROMAGNETIC WAVES FROM MAXWELL'S EQUATIONS
================================================

In free space (no charges or currents: ρ = 0, J⃗ = 0):

Take the curl of Faraday's law:
  ∇ × (∇ × E⃗) = -∂(∇ × B⃗)/∂t

Use Ampère-Maxwell with J⃗ = 0:
  ∇ × B⃗ = μ₀ε₀ ∂E⃗/∂t

Combine (using ∇ × ∇ × E⃗ = ∇(∇·E⃗) - ∇²E⃗ and ∇·E⃗ = 0):
  ∇²E⃗ = μ₀ε₀ ∂²E⃗/∂t²

This is a WAVE EQUATION: ∇²f = (1/v²) ∂²f/∂t²
  with wave speed v = 1/√(μ₀ε₀)

  μ₀ = 4π × 10⁻⁷ T·m/A (permeability of free space)
  ε₀ = 8.854 × 10⁻¹² F/m (permittivity of free space)

  v = 1/√(μ₀ε₀) = 2.998 × 10⁸ m/s = c (speed of light!)

MAXWELL'S CONCLUSION (1865): Light is an electromagnetic wave.
  The colors of visible light are different frequencies of the same wave.
  X-rays, UV, IR, radio — all the same phenomenon at different frequencies.
```

**The Electromagnetic Spectrum**

```
ELECTROMAGNETIC SPECTRUM (All Maxwell waves)
=============================================

Frequency      Wavelength     Name            Applications
-----------    ----------     ----            -----------
10³ Hz         300 km         Radio (LF)      AM radio, navigation
10⁶ Hz         300 m          AM radio        Amplitude modulation
10⁸ Hz         3 m            FM/TV           FM radio, television
10⁹ Hz         30 cm          Microwave       WiFi, radar, microwave oven
10¹⁰ Hz        3 cm           Microwave       Satellite, 5G
10¹² Hz        300 μm         Infrared        Thermal imaging, remote control
3.9–7.5×10¹⁴   400–770 nm     Visible light   Human vision
10¹⁵ Hz        300 nm         UV              Sunburn, sterilization
10¹⁶ Hz        30 nm          Soft X-ray      Microscopy
10¹⁸ Hz        0.3 nm         X-ray           Medical imaging
10²⁰ Hz        3 pm           Gamma ray       Nuclear processes, cancer treatment

WiFi (2.4/5/6 GHz) is Maxwell waves.
Bluetooth (2.4 GHz) is Maxwell waves.
Your cellphone (700 MHz – 60 GHz for 5G) is Maxwell waves.
```

**Maxwell's Statistical Mechanics — The Maxwell-Boltzmann Distribution**

Maxwell independently derived the velocity distribution of gas molecules
(the Maxwell-Boltzmann distribution, 1860) before Boltzmann. He also
introduced the statistical concept of "degrees of freedom" and the
equipartition theorem.

---

## Heinrich Hertz (1857–1894)

### Who He Was

German physicist. Studied under Helmholtz. Died at 36 of granulomatosis
(an autoimmune condition). In his short career, he experimentally confirmed
Maxwell's theory and discovered the photoelectric effect.

### The Contribution: Radio Waves (Experimental Confirmation of Maxwell)

**Hertz's Experiment (1887)**

```
HERTZ'S SETUP
==============

Transmitter: A Leyden jar (capacitor) connected to a spark gap.
  When charged enough, a spark jumps → oscillating current →
  radiates electromagnetic waves (radio waves).

Receiver: A loop of wire with a small gap.
  The induced EM wave drives oscillating current in the loop →
  spark jumps across the gap (detectable).

Hertz could:
  - Detect radio waves across the room (they propagate through space)
  - Measure wavelength by creating standing waves
  - Show they reflect and refract like light
  - Show they travel at the speed of light (c)

CONFIRMATION: Maxwell's prediction was correct.
  Light = radio waves = the same thing at different frequencies.

When asked about the practical applications: "None. I suppose not."
  Marconi (1890s) invented wireless telegraphy.
  Radio, TV, WiFi, cell phones followed.
```

**The Photoelectric Effect (1887)**

Hertz noticed that UV light hitting a metal surface helped spark gaps discharge.
He reported the observation without understanding it. Einstein explained it in
1905: the photoelectric effect shows light is quantized (photons). For this
explanation, Einstein won the 1921 Nobel Prize.

---

## Hendrik Lorentz (1853–1928)

### Who He Was

Dutch physicist. Nobel Prize 1902 (with Zeeman) for discovering how magnetic
fields affect spectral lines (Zeeman effect). Developed the Lorentz transformation
equations that Einstein would later interpret as consequences of special relativity.

### The Contribution: The Lorentz Transformation

**The Problem: Maxwell's Equations and the Ether**

In the 1880s, Maxwell's equations predicted electromagnetic waves travel at
speed c. But: c relative to WHAT? Classical mechanics required an absolute
medium — the "luminiferous ether." Michelson-Morley experiment (1887) tried
to detect Earth's motion through the ether. Found: nothing. No ether.

```
LORENTZ'S SOLUTION (1892–1904)
================================

Lorentz (and independently Fitzgerald) proposed:
  Moving objects physically CONTRACT in the direction of motion by factor:
    L = L₀ √(1 - v²/c²)

  And time DILATES:
    t' = γ(t - vx/c²)  where γ = 1/√(1 - v²/c²)

The LORENTZ TRANSFORMATION:
  x' = γ(x - vt)
  y' = y
  z' = z
  t' = γ(t - vx/c²)

Lorentz's interpretation: Physical shrinkage due to ether.
  Objects physically contract because they push through the ether.

Einstein's interpretation (1905):
  No ether. Space and time are relative.
  Lorentz transformation is a CHANGE OF REFERENCE FRAME,
  not a physical effect. "Length contraction" and "time dilation"
  are relational — they depend on which frame you measure in.

Same mathematics; profoundly different physics.
Einstein got it right. Lorentz's ether picture is wrong.
But the Lorentz transformation is named for Lorentz because he
found the equations first.
```

---

## Nikola Tesla (1856–1943)

### Who He Was

Serbian-American inventor and electrical engineer. Worked briefly for Edison
(who paid him poorly and cheated him). Partnered with Westinghouse to deploy
AC power. The "War of Currents" (AC vs DC) between Tesla/Westinghouse and Edison
was won by AC — because AC transformers can step voltage up/down efficiently,
allowing long-distance power transmission at high voltage (low current, low losses).

Tesla was an extraordinary engineering genius and a poor businessman who died
nearly penniless.

### The Contribution: AC Power Systems

**Why AC Won Over DC**

```
AC vs DC — THE PHYSICS
=======================

DC (Direct Current — Edison's choice):
  Current flows in one direction constantly.
  Cannot easily step voltage up/down.
  Power loss in wires: P_loss = I²R
  At low voltage (110V), need high current for high power → high I²R losses.
  Practical for ~1 mile distribution radius from power plant.

AC (Alternating Current — Tesla/Westinghouse):
  Current oscillates (60 Hz in the US, 50 Hz in Europe).
  Transformer: step up voltage → step down current → I²R losses minimized.
    V₁/V₂ = N₁/N₂ (voltage ratio = turns ratio)
    I₁N₁ = I₂N₂ (power conservation — ignoring losses)
  Practical for cross-country power transmission.

MODERN POWER GRID:
  Generation: ~10–25 kV at the generator
  Step up to: 115–765 kV for long-distance transmission
  Step down to: 4–35 kV for distribution
  Step down to: 120/240 V for consumers

  High-voltage DC (HVDC) is now used for very long lines and undersea cables
  (DC has lower losses than AC for very long distances), but AC remains
  standard for most of the grid.
```

**Tesla's Inventions**

- AC induction motor: uses rotating magnetic field to drive rotor; no brushes
  needed (Faraday's induction principle)
- Alternator (AC generator)
- Tesla coil: resonant transformer for very high voltages (still used in
  radio transmitters, neon signs, plasma globes)
- Polyphase (3-phase) AC systems: the standard for power transmission

The SI unit of magnetic flux density is the **tesla** (T).

---

## Comparison Table

| Figure | Dates | Core Contribution | Mathematical Depth | Legacy |
|--------|-------|-------------------|--------------------|--------|
| **Faraday** | 1791–1867 | Induction, field concept | Minimal (geometric) | Generators, transformers, field theory |
| **Maxwell** | 1831–1879 | Maxwell's equations, light = EM | High (PDEs, vectors) | All EM technology, special relativity |
| **Hertz** | 1857–1894 | Radio waves (Maxwell confirmed) | Experimental | Radio, wireless technology |
| **Lorentz** | 1853–1928 | Lorentz transformation | High | Special relativity (math) |
| **Tesla** | 1856–1943 | AC power systems, induction motor | Engineering | Electric power grid |

---

## Who to Cite for What

| Concept | Cite | Notes |
|---------|------|-------|
| Electromagnetic induction | Faraday | 1831 |
| Field concept (E⃗, B⃗ as real) | Faraday | Conceptual; Maxwell formalized |
| Faraday's law: EMF = -dΦ/dt | Faraday (formalized by Maxwell) | |
| Faraday cage | Faraday | Shielding |
| Maxwell's equations (4 equations) | Maxwell | 1865 |
| Light as electromagnetic wave | Maxwell | Predicted 1865 |
| Maxwell-Boltzmann distribution | Maxwell + Boltzmann | Velocity distribution in gases |
| Radio waves (experimental) | Hertz | 1887 |
| Photoelectric effect (observation) | Hertz | Explained by Einstein 1905 |
| Lorentz transformation | Lorentz | 1904 |
| AC power system | Tesla + Westinghouse | 1880s–1890s |
| Induction motor | Tesla | 1887 |

---

## Common Confusion Points

**"Maxwell added the displacement current for mathematical elegance"** — He added
it because the equations without it violate charge conservation. The displacement
current ε₀ ∂E/∂t is required for ∇ · J + ∂ρ/∂t = 0 (continuity equation)
to hold. The electromagnetic wave prediction was a consequence, not the motivation.

**"Einstein proved Lorentz wrong"** — Lorentz and Einstein agreed on the
mathematical equations (Lorentz transformations). They disagreed on interpretation:
Lorentz thought physical ether caused contraction; Einstein showed no ether exists,
the transformations express the relativity of simultaneity. The physics is
Einstein's; the math is Lorentz's.

**"Tesla invented radio"** — It's disputed. Tesla, Marconi, Popov, and Lodge
all contributed. The US Supreme Court overturned Marconi's patent in 1943 (the year
Tesla died) in favor of Tesla. But Marconi made radio commercially successful.
Tesla filed his radio patents in 1897; Marconi began transatlantic transmission 1901.

**"DC is obsolete"** — High-voltage DC (HVDC) is increasingly used for long-distance
and offshore transmission because it has lower losses and no reactive power issues.
Many modern data center connections use DC internally. The "AC always wins" story
is not quite right — AC is standard, but DC has specific advantages at scale.
