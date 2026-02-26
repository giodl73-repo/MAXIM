# Thermodynamics and Statistical Mechanics — Carnot, Clausius, Kelvin, Boltzmann, Gibbs

## The Central Questions

```
THERMODYNAMICS QUESTIONS
=========================

CARNOT'S QUESTION (1824): How efficient can a heat engine be?
  Why can't you convert all heat to work?

CLAUSIUS'S ANSWER (1850): The Second Law.
  Heat flows from hot to cold. Entropy always increases.
  There is an arrow of time built into the laws of physics.

KELVIN'S QUESTION: What is the minimum temperature?
  Absolute zero: the state of minimum thermal motion.

BOLTZMANN'S QUESTION: What IS heat, microscopically?
  Answer: Random motion of molecules.
  Statistical mechanics: thermodynamics derived from Newtonian mechanics
  applied to huge numbers of particles.

GIBBS'S SYNTHESIS: Put it all on rigorous mathematical footing.
  Free energy, chemical potential, ensembles.
  Gibbs's work is the foundation of all of physical chemistry.
```

---

## Sadi Carnot (1796–1832)

### Who He Was

French military engineer. Published one book: *Réflexions sur la puissance motrice
du feu* (1824). Died of cholera at 36. His notebook showed he was moving toward
energy conservation; it was burned with his personal effects (cholera precaution).

### The Contribution: The Carnot Engine and Thermodynamic Efficiency

**The Carnot Engine**

```
THE CARNOT ENGINE
==================

A heat engine: takes in heat Q_H from a hot reservoir at temperature T_H,
  does work W, and dumps waste heat Q_C into a cold reservoir at T_C.

CARNOT'S THEOREM:
  No heat engine operating between temperatures T_H and T_C can be
  more efficient than a reversible engine (Carnot engine) operating
  between the same temperatures.

CARNOT EFFICIENCY:
  η_Carnot = 1 - T_C/T_H = W/Q_H

  (T in KELVIN — Kelvin temperature scale is defined to make this right)

Example: Coal power plant
  Firebox: T_H ≈ 840 K (567°C)
  Condenser: T_C ≈ 300 K (27°C ambient)
  η_Carnot = 1 - 300/840 ≈ 0.64 (64%)
  Real plants: ~35–45% (irreversibilities reduce efficiency)

This HARD LIMIT comes from the Second Law, not engineering limitations.
No matter how good your engineering, you can't beat Carnot efficiency.
```

**Why Carnot Worked With Caloric Theory (And Was Still Right)**

Carnot incorrectly believed heat was a fluid (caloric). He was still right
because his argument was about TRANSFORMATIONS — the cycle structure —
not the nature of heat. The efficiency formula depends only on temperatures.
This is the beauty of thermodynamics: macroscopic laws often hold regardless
of microscopic details.

---

## Rudolf Clausius (1822–1888)

### Who He Was

German physicist. Reformulated Carnot's work in terms of energy conservation
(the correct theory, after Joule and Mayer established energy conservation in 1840s).
Introduced entropy.

### The Contribution: Entropy and the Two Laws

**The First Law (Formalized)**

```
FIRST LAW OF THERMODYNAMICS
=============================

Energy is conserved. For a system:
  dU = δQ - δW
  Change in internal energy = heat added - work done by system

  (Joule: heat and work are both forms of energy transfer)
  (Clausius: formalized for thermodynamic systems)
```

**The Second Law and Entropy**

```
CLAUSIUS'S ENTROPY (1865)
==========================

For a reversible process:
  dS = δQ_rev / T

For any process:
  dS ≥ δQ / T  (equality for reversible; strict inequality for irreversible)

CLAUSIUS'S STATEMENT OF SECOND LAW:
  Heat cannot spontaneously flow from a cold body to a hot body.

KELVIN-PLANCK STATEMENT:
  No engine operating in a cycle can convert all heat to work.

THESE ARE EQUIVALENT. Both require entropy to increase (or stay constant).

ENTROPY INCREASES:
  In an isolated system, dS ≥ 0.
  Total entropy of universe never decreases.
  This is the ARROW OF TIME: why processes are irreversible.
  Why you can't unscramble an egg. Why heat flows only one direction.
  Why memory of the past is possible but not of the future.

Clausius's famous epitome (1865):
  "Die Energie der Welt ist konstant.
   Die Entropie der Welt strebt einem Maximum zu."
  (The energy of the world is constant. The entropy of the world
   tends toward a maximum.)
```

---

## Lord Kelvin (William Thomson) (1824–1907)

### Who He Was

Irish-Scottish physicist. Knighted as Baron Kelvin in 1892. Made contributions
to thermodynamics, electromagnetism, hydrodynamics, and practical engineering
(supervised the laying of the transatlantic telegraph cable).

### The Contribution: Absolute Temperature and Thermodynamic Insights

**Absolute Temperature (Kelvin Scale)**

```
THE KELVIN SCALE
=================

Kelvin recognized that Carnot efficiency η = 1 - T_C/T_H defines
a temperature scale independent of the thermometric substance.
  (Ordinary scales — Celsius, Fahrenheit — depend on properties of mercury.)

Absolute zero: the temperature where η = 1 (all heat converted to work)
  — which is unattainable but definable.

  0 K = -273.15°C = absolute zero

The Kelvin scale: 0 K at absolute zero, 1 K degrees same size as 1°C.

WHY THIS MATTERS FOR COMPUTATION:
  Thermal noise in electronics is kT (Boltzmann constant × temperature).
  kT at room temperature (300 K) ≈ 0.026 eV — sets the minimum energy
  per bit operation (Landauer's principle: kT ln 2 to erase one bit).
  This is why quantum computing needs extreme cooling (millikelvin) —
  to reduce thermal noise below the quantum signal.
```

**Kelvin's Big Mistake**

Kelvin calculated the age of the Earth from the cooling rate and got
~20–40 million years. Geologists needed hundreds of millions. Kelvin
was dismissive of their evidence.

He was wrong because he didn't know about radioactive decay — a heat
source inside the Earth that Curie and Rutherford discovered later.
Good lesson: wrong assumptions about mechanism produce wrong answers
even from correct physics.

---

## Ludwig Boltzmann (1844–1906)

### Who He Was

Austrian physicist. Developed statistical mechanics — the theory that
thermodynamics arises from the statistical behavior of large numbers of molecules.
Faced intense opposition from Mach and Ostwald ("energeticists" who denied
the existence of atoms). Suffered depression and took his own life in 1906.
Within two years, Einstein's 1905 paper on Brownian motion had given the
first quantitative proof of atomic existence.

### The Contribution: Statistical Mechanics and S = k ln W

**Boltzmann's S = k ln W**

```
BOLTZMANN'S ENTROPY FORMULA
=============================

S = k_B · ln W

  S = entropy
  k_B = 1.38 × 10⁻²³ J/K (Boltzmann constant)
  W = number of microscopic configurations (microstates) corresponding
      to the observed macrostate

WHAT THIS MEANS:
  Entropy = logarithm of the number of ways the system can be arranged.

  Example: A box with all gas molecules in one half.
    That's ONE configuration — almost (few ways to arrange them all there).
    W is tiny → S is low → low entropy.

  After opening partition: molecules spread to fill box.
    Now there are VASTLY more configurations.
    W is enormous → S is high → high entropy.

  This is WHY entropy increases: the universe explores microstates
  randomly; high-entropy macrostates are overwhelmingly more numerous.

RELATIONSHIP TO SHANNON ENTROPY:
  Shannon (1948): H = -Σ pᵢ log pᵢ
  Boltzmann (1877): S = k_B · ln W = -k_B · Σ pᵢ log pᵢ (Gibbs's form)

  Same formula. Shannon entropy = Boltzmann entropy / k_B.
  The connection is deep: information = negative entropy.
  (Szilard 1929: Maxwell's demon requires information processing;
   Landauer 1961: erasing one bit dissipates k_B T ln 2 energy.)

The formula is carved on Boltzmann's tombstone in Vienna.
```

**Maxwell-Boltzmann Distribution**

```
MAXWELL-BOLTZMANN VELOCITY DISTRIBUTION
=========================================

For a gas in thermal equilibrium at temperature T:
  f(v) = 4π (m/2πk_BT)^(3/2) · v² · exp(-mv²/2k_BT)

  f(v)dv = probability of having speed in [v, v+dv]

Properties:
  Most probable speed: v_mp = √(2k_BT/m)
  Mean speed: v̄ = √(8k_BT/πm)
  RMS speed: v_rms = √(3k_BT/m)

At room temperature for air (N₂, m ≈ 28 amu):
  v_rms ≈ 515 m/s ≈ 1,150 mph

Applications:
  - Chemical reaction rates (Arrhenius equation)
  - Atmospheric escape (why light planets lose light gases)
  - Neutron moderation in nuclear reactors
  - Effusion through small holes (separation of isotopes)
```

**The H-Theorem and Irreversibility**

Boltzmann's H-theorem: entropy increases in a gas undergoing molecular collisions.
This led to the "reversibility paradox" (Loschmidt): Newton's laws are time-symmetric,
yet entropy only increases. How?

Boltzmann's answer: it's about PROBABILITY, not necessity. A low-entropy state
is extremely improbable but not forbidden. The Second Law is a statistical law.
In a universe with 10²⁴ molecules, "overwhelmingly improbable" = "never observed."

---

## Josiah Willard Gibbs (1839–1903)

### Who He Was

American physicist and mathematician, Yale. Worked in almost complete intellectual
isolation but produced work of extraordinary depth and originality. His papers
on chemical thermodynamics and statistical mechanics (published in the proceedings
of the Connecticut Academy) were largely ignored in America but recognized by
Maxwell and Clausius in Europe.

### The Contribution: Free Energy, Phase Diagrams, and Vector Analysis

**Gibbs Free Energy**

```
GIBBS FREE ENERGY
==================

G = H - TS = U + PV - TS

  H = enthalpy (heat content at constant pressure)
  T = temperature, S = entropy
  U = internal energy, P = pressure, V = volume

AT CONSTANT TEMPERATURE AND PRESSURE:
  A process is SPONTANEOUS if ΔG < 0.
  A process is at EQUILIBRIUM if ΔG = 0.
  A process is NON-SPONTANEOUS if ΔG > 0.

  ΔG = ΔH - TΔS
  Spontaneity depends on competition between enthalpy change (ΔH)
  and entropy change (TΔS).

Examples:
  Dissolution of NaCl: ΔH > 0 (endothermic), TΔS > 0 (entropy increase)
    → Spontaneous only when TΔS > ΔH: needs warm enough temperature.
  Combustion: ΔH << 0 (very exothermic), TΔS > 0
    → Spontaneous at essentially all temperatures.

CHEMICAL POTENTIAL:
  μᵢ = ∂G/∂nᵢ  (how G changes with number of moles of species i)
  At equilibrium: Σ μᵢ νᵢ = 0 (for each reaction with stoichiometry ν)
  This governs all chemical equilibria.
```

**Phase Diagrams and Gibbs Phase Rule**

```
GIBBS PHASE RULE
=================

F = C - P + 2

  F = degrees of freedom (variables you can change while maintaining equilibrium)
  C = number of chemical components
  P = number of phases in equilibrium (solid, liquid, gas, etc.)

For pure water (C=1):
  Single phase (e.g., just liquid): P=1, F = 1-1+2 = 2 (vary T and P freely)
  Two phases (liquid-vapor): P=2, F = 1-2+2 = 1 (only one degree of freedom)
  Triple point: P=3, F = 1-3+2 = 0 (fixed point: T=273.16K, P=611.7 Pa)

This rule governs all phase diagrams in metallurgy, geology,
materials science, and chemistry.
```

**Gibbs Ensembles**

Gibbs reformulated statistical mechanics using "ensembles":

```
GIBBS ENSEMBLES
================

Instead of following one system in time, consider an ENSEMBLE:
  a mental collection of all possible systems with the same macroscopic
  constraints.

Microcanonical ensemble: fixed E, V, N (isolated system)
  All microstates with given energy equally probable.

Canonical ensemble: fixed T, V, N (thermostat at temperature T)
  Boltzmann distribution: Pᵢ ∝ exp(-Eᵢ/k_BT)
  Partition function: Z = Σᵢ exp(-Eᵢ/k_BT)
  All thermodynamic quantities from Z: F = -k_BT ln Z, S = -∂F/∂T, etc.

Grand canonical: fixed T, V, μ (particle exchange allowed)
  For quantum statistics: Fermi-Dirac, Bose-Einstein distributions.

The partition function Z is the central object — the rest of statistical
mechanics is extracting thermodynamic quantities from Z.
```

---

## Comparison Table

| Figure | Dates | Core Contribution | Key Formula | Legacy |
|--------|-------|-------------------|-------------|--------|
| **Carnot** | 1796–1832 | Carnot efficiency | η = 1 - T_C/T_H | Hard limit on heat engines |
| **Clausius** | 1822–1888 | Entropy, 2nd Law | dS ≥ δQ/T | Arrow of time, irreversibility |
| **Kelvin** | 1824–1907 | Absolute temperature, 2nd Law | T = 0 K = absolute zero | Temperature scale |
| **Boltzmann** | 1844–1906 | Statistical mechanics, entropy | S = k_B ln W | Atomic reality, information theory |
| **Gibbs** | 1839–1903 | Free energy, ensembles, phase rule | G = H - TS | All of chemistry, materials science |

---

## Who to Cite for What

| Concept | Cite | Notes |
|---------|------|-------|
| Carnot efficiency limit | Carnot | 1824, before energy conservation known |
| Second Law (heat flow direction) | Clausius | 1850 |
| Entropy (macroscopic definition) | Clausius | 1865 |
| Absolute temperature / Kelvin scale | Kelvin | ~1848 |
| S = k ln W (entropy = log of microstates) | Boltzmann | 1877 |
| Maxwell-Boltzmann distribution | Maxwell + Boltzmann | 1860–1871 |
| Statistical mechanics (ensemble approach) | Gibbs (+ Boltzmann) | Gibbs more rigorous |
| Gibbs free energy ΔG | Gibbs | |
| Phase rule F = C - P + 2 | Gibbs | |
| Partition function | Gibbs | Z = Σ exp(-E/kT) |

---

## Common Confusion Points

**"The Second Law is absolute"** — It's probabilistic (Boltzmann). In a system of
N molecules, you could observe a spontaneous decrease in entropy — with probability
~exp(-N). For N ~ 10²⁴ (Avogadro's number), this probability is effectively zero.
Poincaré recurrence theorem: every closed classical system will return to any state
given enough time — but "enough time" is 10^(10^23) years for a mole of gas.

**"Entropy is disorder"** — This is imprecise. Entropy = logarithm of the number
of microstates. "Disorder" is an intuitive gloss. Counter-example: polymer chains
have more entropy when disordered (many configurations), but some polymer ordering
increases entropy through other degrees of freedom. Use "microstates" not "disorder."

**"Boltzmann proved atoms exist"** — He argued for atomic theory from thermodynamics.
Mach and Ostwald rejected atoms as metaphysical. Actual proof came from Einstein's
1905 Brownian motion paper: the diffusion coefficient of pollen grains matched
predictions from atomic theory. Perrin measured Avogadro's number from Brownian
motion in 1908–1909, settling the debate definitively.

**"The Carnot engine is a real engine"** — The Carnot cycle is a theoretical ideal:
isothermal expansion, adiabatic expansion, isothermal compression, adiabatic compression,
operating infinitely slowly (quasi-static). No real engine operates this way.
It's the theoretical maximum for efficiency. Real engines use different cycles
(Otto cycle for gasoline engines, Rankine cycle for steam turbines).
