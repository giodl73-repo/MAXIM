# The Relativity and Quantum Revolution — 1905-1935

## The Big Picture

The 30 years from Einstein's annus mirabilis (1905) to the stabilization of quantum field theory produced the two frameworks that replaced Newtonian mechanics. Neither was anticipated from within the prior framework. Both required abandoning commonsense assumptions about space, time, and measurement.

```
+------------------------------------------------------------------+
|         RELATIVITY AND QUANTUM -- CONCEPTUAL MAP                 |
+------------------------------------------------------------------+
|                                                                   |
|  RELATIVITY (Einstein)                                            |
|  Special (1905): no absolute space/time, c is constant           |
|  General (1915): gravity = spacetime curvature                    |
|  Confirmed: Eddington eclipse 1919, GPS requires GR corrections  |
|                                                                   |
|  QUANTUM MECHANICS                                                |
|  Planck 1900: E = hv (energy quantized, reluctantly)             |
|  Einstein 1905: photons (light as particles)                      |
|  Bohr 1913: quantized orbits (why? no theory yet)                |
|  de Broglie 1924: matter has wave properties                      |
|  Heisenberg 1925: matrix mechanics (observables as matrices)      |
|  Schrodinger 1926: wave mechanics (psi as wave equation)          |
|  Born 1926: psi^2 as probability density                          |
|  Dirac 1928: relativistic QM, predicts antimatter                |
|  EPR 1935: Einstein's challenge to completeness                   |
|                                                                   |
|  THE DEBATE:                                                       |
|  Bohr vs Einstein: what is physics FOR?                           |
|  Copenhagen vs realism: complete description or not?             |
|  Bell 1964, Aspect 1982: nonlocality is real                      |
+------------------------------------------------------------------+
```

---

## Layer 1: Einstein's Special Relativity (1905)

### The Annus Mirabilis

In 1905, Albert Einstein (26 years old, Patent Office clerk in Bern) published four papers that each would have been sufficient to establish a major physicist's reputation:

| Paper | Content |
|-------|---------|
| Photoelectric effect | Light as photons, Einstein wins Nobel for this |
| Brownian motion | Mathematical proof that atoms exist |
| Special relativity | Space, time, simultaneity |
| E = mc^2 | Mass-energy equivalence (follow-up to SR) |

### The Two Postulates

```
SPECIAL RELATIVITY DERIVES FROM TWO POSTULATES:

1. PRINCIPLE OF RELATIVITY:
   Physical laws take the same form in all inertial
   (non-accelerating) reference frames.
   (Galileo already had this for mechanics; Einstein
   extended it to electromagnetism)

2. CONSTANCY OF LIGHT SPEED:
   The speed of light in vacuum is c = 3x10^8 m/s
   in ALL inertial frames, regardless of the motion
   of the source or observer.

   This is what Michelson-Morley showed.
   This contradicts "common sense" velocity addition.
   (If I run at 10 m/s and throw a ball at 20 m/s,
   the ball moves at 30 m/s relative to ground.)
   For light: no matter how fast the source moves,
   light always moves at c relative to any observer.
```

### What Changes

```
CONSEQUENCES OF SPECIAL RELATIVITY:

RELATIVITY OF SIMULTANEITY:
Two events simultaneous in one frame are NOT simultaneous
in another frame moving relative to it.
There is no absolute "now."

TIME DILATION:
Moving clocks run slower.
Delta_t' = Delta_t * gamma,  gamma = 1/sqrt(1 - v^2/c^2)
Verified: muons from cosmic rays reach Earth's surface
because their lifetime is dilated (time runs slower for
fast-moving muons relative to Earth)
GPS satellites: ~45 microseconds/day time dilation
correction required (without it, GPS would drift ~10 km/day)

LENGTH CONTRACTION:
Objects are shorter in the direction of motion.
L' = L/gamma

RELATIVISTIC MASS-ENERGY:
E = gamma * mc^2
At rest (v=0, gamma=1): E = mc^2
Rest mass and energy are interconvertible.
1 kg of matter = 9x10^16 joules
(Hiroshima bomb: ~1 gram of mass converted)

VELOCITY ADDITION:
u' = (u + v) / (1 + u*v/c^2)
For v << c: reduces to u' = u + v (Galilean)
For u = c: u' = c (light always c)
```

### What Does NOT Change

SR is fundamentally about **invariants**:

```
SPACETIME INTERVAL (invariant):
ds^2 = c^2*dt^2 - dx^2 - dy^2 - dz^2

This quantity is the same in all inertial frames.
Different observers disagree on dt and dx separately,
but agree on ds^2.

ds^2 > 0: timelike interval (events connected by < c)
ds^2 = 0: lightlike interval (photon worldline)
ds^2 < 0: spacelike interval (no causal connection)
```

---

## Layer 2: General Relativity (1915)

### The Equivalence Principle

Einstein's starting point (1907): a person in a closed room cannot distinguish between:
- Resting in a gravitational field (gravity pulling them down)
- Accelerating upward at g

```
EQUIVALENCE PRINCIPLE:

GRAVITATIONAL FIELD:              ACCELERATING ROCKET:
+------------------+              +------------------+
|     Person       |              |     Person       |
|  feels 1g down   |              |  feels 1g down   |
|                  |              |                  |
|  Earth below     |              |  Rocket engine   |
+------------------+              +------------------+

These are locally indistinguishable.

CONSEQUENCE:
If you can't distinguish them, gravity IS acceleration.
A "gravitational field" is equivalent to a non-inertial frame.
Inertial motion in curved spacetime = free fall.
```

### Gravity as Spacetime Curvature

```
NEWTONIAN GRAVITY:              EINSTEIN'S GRAVITY:
Force F = Gm1m2/r^2             Spacetime curvature
Instantaneous action             Mass curves spacetime
at distance                      Objects follow geodesics
                                 (straightest paths in
                                 curved spacetime)

ANALOGY (imperfect but useful):
Place a bowling ball on a rubber sheet --> depression
A marble rolled near it follows a curved path.
The "force" is the geometry of the sheet.

FIELD EQUATIONS:
G_mu_nu + Lambda*g_mu_nu = (8*pi*G/c^4) * T_mu_nu

G_mu_nu: Einstein tensor (describes spacetime curvature)
T_mu_nu: stress-energy tensor (describes matter/energy distribution)
Lambda: cosmological constant (Einstein added it to get static
        universe; later called "my greatest blunder")

"Matter tells spacetime how to curve;
spacetime tells matter how to move." -- Wheeler's summary
```

### Predictions and Tests

```
GENERAL RELATIVITY PREDICTIONS:

1. LIGHT BENDING (1916 prediction, tested 1919):
   Light follows geodesics in curved spacetime.
   Light near massive body is deflected.
   GR predicts 1.75 arcseconds for light grazing Sun.
   (Newtonian calculation: 0.87 arcseconds -- exactly half)

   EDDINGTON EXPEDITION (May 29, 1919 solar eclipse):
   Stars near Sun photographed during totality.
   Positions compared to nighttime positions.
   Deflection: 1.61 +/- 0.30 arcsec (Sobral)
              1.98 +/- 0.16 arcsec (Principe)
   GR prediction: 1.75 arcsec
   Within experimental error: confirmed.

   MEDIA REACTION: Front page worldwide.
   "Revolution in Science -- New Theory of the Universe"
   (London Times, November 7, 1919)
   Einstein became globally famous overnight.

2. MERCURY PERIHELION PRECESSION:
   Mercury's closest approach to Sun rotates 43 arcsec/century
   unexplained by Newtonian mechanics.
   GR predicts exactly 43 arcsec/century.
   This is not a new prediction -- it explained a known anomaly.

3. GRAVITATIONAL REDSHIFT:
   Light climbing out of a gravitational well loses energy.
   Its frequency decreases (redshifts).
   Confirmed by Pound-Rebka experiment (1959) in a 22m building.

4. GRAVITATIONAL WAVES:
   Ripples in spacetime propagating at c.
   Predicted 1916. Confirmed by LIGO 2015 (two black holes merging).
   GW150914: ~1.3 billion light-years away, signal lasted 0.2 seconds.
   Peak power output: ~3.6x10^49 watts (more than all stars combined)
```

---

## Layer 3: The Old Quantum Theory (1900-1925)

### Bohr's Atom (1913)

Niels Bohr (1885-1962) proposed a planetary model of the atom with **quantized orbits** — electrons can only occupy certain allowed circular orbits.

```
BOHR'S MODEL:

Rules:
1. Electrons orbit in circular orbits with angular momentum
   L = n * hbar  (n = 1, 2, 3...)
2. Electrons in allowed orbits don't radiate.
3. Radiation emitted/absorbed when electron changes orbit.
   E = hv  where v = |E_final - E_initial| / h

Energy levels for hydrogen:
E_n = -13.6 eV / n^2

BALMER SERIES:
Transitions from n_upper to n=2:
1/lambda = R_H * (1/4 - 1/n^2)
Matches the empirical Balmer formula EXACTLY.

THIS WAS A TRIUMPH.
Bohr derived the empirical Rydberg constant from first principles:
R_H = m_e * e^4 / (8 * epsilon_0^2 * h^3 * c)
All measured constants -- no free parameters.
```

**But why?** Bohr had no physical reason for quantized orbits. He just assumed them and got the right answer. His own retrospective: "I know this is not right, but we must find out why."

The Bohr model fails for multi-electron atoms, cannot explain spectral line intensities or splitting in magnetic fields (Zeeman effect details). It is a calculation recipe, not a theory.

---

## Layer 4: Quantum Mechanics (1925-1926)

### Two Routes to the Same Theory

```
HEISENBERG'S MATRIX MECHANICS (1925):              SCHRODINGER'S WAVE MECHANICS (1926):

Starting point: observable quantities              Starting point: de Broglie's matter waves
(positions, momenta) as non-commuting matrices     Wave equation for psi (wave function)

Key postulate:                                     Key equation:
pq - qp = i*hbar * I                               i*hbar * d(psi)/dt = H*psi
(position and momentum don't commute)              (Schrodinger equation, time-dependent)

This alone implies uncertainty principle.          Stationary states: H*psi = E*psi

Heisenberg, Born, Jordan develop formalism         de Broglie, Schrodinger develop formalism
(Gottingen school)                                 (Austrian-Swiss school)

SCHRODINGER SHOWED THESE ARE MATHEMATICALLY EQUIVALENT (1926):
Matrix mechanics <--> Wave mechanics
Different representations of same mathematical structure.
```

### The Uncertainty Principle

Heisenberg derived from the non-commutativity of operators:

```
HEISENBERG UNCERTAINTY PRINCIPLE:

Delta_x * Delta_p >= hbar/2

(uncertainty in position) * (uncertainty in momentum) >= hbar/2

This is NOT about measurement disturbance (though Heisenberg
initially presented it that way -- Robertson proved the
algebraic form in 1929).

IT IS: a fundamental property of quantum states. A state
cannot simultaneously have definite position AND definite
momentum. These are complementary observables.

ENERGY-TIME VERSION:
Delta_E * Delta_t >= hbar/2

NOT a conservation law violation -- it says a quantum state
of duration Delta_t has an energy uncertainty Delta_E.
(This is why virtual particles are "allowed" for short times.)
```

### The Measurement Problem and Copenhagen Interpretation

```
THE MEASUREMENT PROBLEM:

Before measurement: quantum system in superposition
|psi> = alpha|up> + beta|down>

After measurement: definite outcome (up OR down)

What happens between?

COPENHAGEN INTERPRETATION (Bohr, Heisenberg, Born, 1926-1930):

1. The wavefunction psi is a complete description of
   the quantum state. Nothing more exists to know.

2. |psi|^2 gives probability of each outcome.
   (Born rule -- this was NOT in Schrodinger's original paper;
   Schrodinger thought psi was a physical wave, not a probability)

3. Upon measurement, the wavefunction "collapses" to
   the observed eigenstate. The collapse is not described
   by the Schrodinger equation.

4. "Unobserved" quantities don't have definite values.
   The question "which slit did the electron go through?"
   has no answer if unobserved.

5. Classical physics required for measurement apparatus.
   "There is no quantum world -- only an abstract description."
   (Bohr)

DELIBERATE ANTI-REALISM:
Bohr explicitly rejected the idea that QM describes
a reality independent of observation. "Physics is not
about nature; it is about what we can say about nature."
```

---

## Layer 5: The Bohr-Einstein Debates

### Einstein's Objections

Einstein had three distinct objections to quantum mechanics:

```
OBJECTION 1: INCOMPLETENESS
QM is not a complete description of reality.
"God does not play dice" -- probability reflects our
ignorance, not fundamental indeterminism.
There must be "hidden variables" completing the description.

OBJECTION 2: NONLOCALITY (EPR, 1935)
Einstein, Podolsky, Rosen paper: if QM is complete,
measuring one particle instantly affects the state of
a correlated distant particle.
This violates locality (no faster-than-light influences).
Either QM is incomplete (hidden variables exist) OR
QM implies spooky action at distance.
Einstein preferred: QM is incomplete.

OBJECTION 3: MACROSCOPIC SUPERPOSITION
Schrodinger's Cat (Schrodinger 1935): quantum rules applied
to macroscopic system give absurd results.
Cat is "alive and dead" simultaneously until observed?
Something must prevent this. What?
```

### The EPR Argument

```
EPR SETUP:
Create two particles with correlated spin (total = 0).
Particle 1 goes to Alice, Particle 2 to Bob.
They are far apart.

Alice measures particle 1: spin up.
Instantly, particle 2 is "spin down" (to conserve spin).
Bob will always measure spin down if Alice measured up.

EPR'S ARGUMENT:
1. If Alice's measurement instantly determines Bob's result:
   either FTL influence exists (violates relativity)
   OR the result was predetermined (Bob's particle was "always"
   spin down, just unknown)

2. Since FTL is unacceptable: the result was predetermined.

3. But QM says no predetermined values -- QM is INCOMPLETE.
   The hidden variables that predetermine results are not
   in the QM description.

BOHR'S REPLY:
"The completeness of the quantum-mechanical description
cannot be taken for granted." (Notoriously obscure response)
Bohr argued that Alice's measurement changes the "experimental
arrangement" for Bob -- no unambiguous properties can be
attributed to either particle alone.
```

### Bell's Theorem (1964) and Aspect's Experiments (1982)

```
BELL'S INSIGHT:
If hidden variables exist (Einstein's view), they make
QUANTITATIVE predictions for correlation experiments
that DIFFER from quantum mechanical predictions.

BELL INEQUALITY:
|C(a,b) - C(a,c)| <= 1 + C(b,c)

C(a,b) = correlation of measurements along axes a and b

If local hidden variables: Bell inequality holds.
If quantum mechanics: Bell inequality can be violated.

ASPECT EXPERIMENTS (1982):
Measured photon correlations.
Result: Bell inequality VIOLATED. QM predictions confirmed.

IMPLICATION:
Local hidden variables cannot explain quantum correlations.
The world is NONLOCAL -- correlated particles are not
independent, no matter how far apart.

HOWEVER:
Nonlocality does not allow FTL communication.
You cannot use correlations to send signals faster than light
because you cannot control which measurement outcome you get.
The correlations are random individually; the pattern
emerges only when you compare notes (at <= c speed).
```

### Path Integral Formulation (Feynman)

Richard Feynman (1948) reformulated quantum mechanics as a sum over all possible paths:

```
FEYNMAN PATH INTEGRALS:

Classical mechanics: one path (principle of least action)
Quantum mechanics: sum over ALL paths

<x_f, t_f | x_i, t_i> = integral over all paths of exp(iS/hbar)

S = action (time integral of Lagrangian)

For each path, compute e^(iS/hbar) and sum all contributions.
Paths near the classical path add constructively.
Paths far from classical path cancel (rapidly oscillating phase).
In classical limit (hbar -> 0): only classical path survives.

PRACTICAL VALUE:
Provides computational algorithm for QED (quantum electrodynamics).
Feynman diagrams are visual representations of terms in the
perturbation expansion of the path integral.
QED: most precisely tested theory in physics (g-factor of electron
measured to 12 decimal places, theory matches to 10).
```

---

## Layer 6: What the Quantum Revolution Means

### The Philosophical Stakes

```
THE QUESTION AT STAKE (Bohr vs Einstein):

Einstein's position:
"Does the Moon exist when nobody looks at it?"
Yes, obviously. Physics should describe objective reality.
QM is incomplete because it doesn't describe the Moon
(or electron) when unobserved.

Bohr's position:
"What does it even mean to say the Moon exists when
unobserved?" The question presupposes classical categories.
QM doesn't describe "the electron" -- it describes what
we can say when we interact with the electron.

BELL'S RESOLUTION (partial):
Local realism (Einstein's position) is ruled out by
Bell + Aspect experiments. You cannot have:
- Local causes (no FTL)
- Realism (definite values even when unobserved)
- QM predictions (which are confirmed)

All three together are inconsistent.
Pick any two: drop one.

SURVIVING INTERPRETATIONS:
- Copenhagen: drop realism (no definite values unobserved)
- Many-worlds (Everett): all outcomes happen, no collapse
- Pilot wave (de Broglie-Bohm): nonlocal hidden variables
- QBism: wavefunction is agent's belief state, not reality
- Relational QM: quantum states are relational, not absolute

None of these is empirically distinguishable from each other.
This is a philosophical dispute, not a scientific one
(in Popper's sense -- no experiment discriminates them).
```

---

## Decision Cheat Sheet

| You want to understand... | Key figure/result | Key point |
|---------------------------|------------------|-----------|
| Why SR is forced on us | Michelson-Morley + Maxwell | c is constant in all frames; no ether |
| What E=mc^2 actually means | SR mass-energy equivalence | Mass is a form of energy; 1kg = 9x10^16 J |
| Why GR was needed after SR | SR is for inertial frames; gravity involves acceleration | Equivalence principle --> gravity = curvature |
| Why Bohr's atom worked | Quantized orbits match Balmer series | Nobody knew why; it was a recipe, not a theory |
| Why Copenhagen is anti-realist | Bohr's philosophy | QM describes knowledge, not reality |
| What EPR + Bell proved | Nonlocality | Local hidden variables are ruled out |

---

<!-- @editor[bridge/P2]: No old-world bridge section — natural parallels for the learner: SR's invariant spacetime interval as the concept that what's conserved matters more than what's relative (like an API contract — implementations vary, interface is invariant); Heisenberg's matrix mechanics vs Schrodinger's wave mechanics as two isomorphic representations of the same system (like SQL vs LINQ — different syntax, same semantics, proven equivalent); the Copenhagen interpretation debate maps to software's "what does the abstraction represent" question -->

## Common Confusion Points

**Special relativity does not say "everything is relative."** The invariant spacetime interval is the same in all frames. What is relative: simultaneity, time intervals, lengths. What is invariant: speed of light, spacetime intervals, proper time.

**E=mc^2 does not explain atomic bombs by converting mass entirely to energy.** A fission bomb converts ~0.1% of its mass to energy. E=mc^2 says mass and energy are the same thing; nuclear reactions that decrease total rest mass release that mass difference as kinetic energy.

**Schrodinger's equation is deterministic.** The wavefunction evolves perfectly deterministically under Schrodinger's equation. Indeterminism enters only during **measurement** (wavefunction collapse). In many-worlds, there is no collapse and everything is deterministic.

**Heisenberg uncertainty is not about the experimenter being clumsy.** It is not about disturbing the electron with photons during measurement. It is about the fundamental impossibility of a quantum state having simultaneously definite position and momentum. Robertson's algebraic proof doesn't involve measurement disturbance.

**Bell's theorem does not prove no hidden variables exist.** It proves no **local** hidden variables exist. Nonlocal hidden variable theories (Bohmian mechanics) are consistent with Bell's results and with all QM predictions.
