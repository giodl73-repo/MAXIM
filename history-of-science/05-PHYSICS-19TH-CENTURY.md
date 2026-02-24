# 19th-Century Physics — Thermodynamics, Electromagnetism, and the Coming Crisis

## The Big Picture

The 19th century produced two complete, successful physical theories — thermodynamics and electromagnetism — whose synthesis in Maxwell's equations predicted electromagnetic waves at the speed of light. By 1895, physics appeared nearly complete. Lord Kelvin (allegedly) said only "two small clouds" remained. Both clouds became relativity and quantum mechanics.

```
+------------------------------------------------------------------+
|         19TH-CENTURY PHYSICS -- CONCEPTUAL MAP                  |
+------------------------------------------------------------------+
|                                                                   |
|  THERMODYNAMICS (1824-1905)                                       |
|  Carnot (efficiency) --> Joule (mechanical equivalent)           |
|  --> Clausius (entropy) --> Boltzmann (statistical mechanics)    |
|  --> Planck (quantum hypothesis to fix UV catastrophe)           |
|                                                                   |
|  ELECTROMAGNETISM (1820-1887)                                     |
|  Oersted (current->field) --> Ampere (force law)                 |
|  --> Faraday (field concept, induction) --> Maxwell (equations)  |
|  --> Hertz (electromagnetic waves confirmed 1887)                |
|                                                                   |
|  SPECTROSCOPY (1814-1900)                                         |
|  Fraunhofer (dark lines) --> Kirchhoff/Bunsen (identification)   |
|  --> Balmer (empirical formula) --> Rydberg (constant)           |
|  --> waiting for quantum explanation                             |
|                                                                   |
|  THE CRISIS (1887-1905)                                           |
|  Michelson-Morley null result (1887): no ether                   |
|  Ultraviolet catastrophe: Rayleigh-Jeans diverges                |
|  Photoelectric effect: classical prediction fails                |
|  --> special relativity (1905) + quantum mechanics (1900-1926)  |
+------------------------------------------------------------------+
```

---

## Layer 1: Thermodynamics — Heat, Work, and Entropy

### Carnot (1824) — The Efficiency Limit

Sadi Carnot published *Reflections on the Motive Power of Fire* in 1824. He died of cholera in 1832 at age 36. His work was ignored for 16 years until Clausius and Kelvin resurrected it.

```
CARNOT'S QUESTION:
What is the maximum efficiency of a heat engine?

CARNOT'S ANSWER:
Efficiency depends only on the temperatures of the
hot and cold reservoirs, NOT on the working substance.

eta_max = 1 - T_cold/T_hot  (Carnot efficiency)
(T in absolute temperature, Kelvin)

CARNOT'S ENGINE (ideal cycle):
     HOT RESERVOIR (T_H)
           |
     1. Isothermal expansion: absorb Q_H at T_H
           |
     2. Adiabatic expansion: no heat transfer, temperature drops
           |
     COLD RESERVOIR (T_C)
           |
     3. Isothermal compression: reject Q_C at T_C
           |
     4. Adiabatic compression: no heat transfer, temperature rises
           |
     back to start

W = Q_H - Q_C  (conservation of energy)
eta = W/Q_H = 1 - Q_C/Q_H = 1 - T_C/T_H

IMPLICATIONS:
- No engine can be 100% efficient unless T_C = 0 (absolute zero)
- Reversible engines have maximum efficiency
- All reversible engines operating between same T have same efficiency
- This is Second Law's direct consequence
```

**What Carnot got wrong**: He used caloric theory (heat as a fluid), which was wrong. His result is correct. This is an important pattern: correct results derived from wrong theory — the mathematical structure was right; the interpretation was wrong.

### Joule and the Mechanical Equivalent of Heat

James Joule (1818-1889) measured how much mechanical work produces a given amount of heat:

```
JOULE'S PADDLE WHEEL EXPERIMENT (1845):

Known weight drops a known distance:
Potential energy lost = m * g * h

Churns water via paddle wheel.
Measures temperature rise of water.
heat gained = m_water * c * Delta_T

From multiple runs:
1 calorie = 4.186 Joules (mechanical work equivalent)

SIGNIFICANCE:
Heat is a form of energy, not a substance.
The caloric theory (heat-fluid) is wrong.
Energy can be converted between mechanical and thermal forms.
This is the First Law of Thermodynamics (conservation of energy).
```

### Clausius and Entropy (1850-1865)

Rudolf Clausius reconciled Carnot's result with the mechanical theory of heat (Joule), producing the two laws of thermodynamics in their final form:

```
FIRST LAW:
dU = dQ - dW
Change in internal energy = heat absorbed - work done
(conservation of energy, including heat)

SECOND LAW (several formulations):
Clausius: "Heat cannot spontaneously flow from cold to hot"
Kelvin: "No process exists whose sole effect is to convert heat
         entirely into work" (no 100%-efficient engine)

ENTROPY (Clausius, 1865):
dS = dQ_rev / T  (entropy change for reversible process)

For irreversible processes: dS > dQ / T

The entropy of an isolated system never decreases:
dS >= 0  (Second Law in entropic form)

NAME ETYMOLOGY:
Clausius coined "entropy" from Greek trope (transformation)
to parallel "energy" -- he wanted them to sound related.
```

### Boltzmann — Statistical Mechanics and the Atomic Reality

Ludwig Boltzmann (1844-1906) derived thermodynamic laws from atomic mechanics:

```
BOLTZMANN'S PROGRAM:
If matter consists of atoms in random motion,
thermodynamic quantities emerge statistically.

S = k_B * ln(W)
S = entropy
k_B = Boltzmann constant (bridge between atomic and macro scales)
W = number of microscopic states consistent with the macroscopic state

PHYSICAL MEANING:
High entropy = many microscopic arrangements
Low entropy = few microscopic arrangements
Second Law = system evolves toward more probable state
              (overwhelmingly likely, not logically necessary)

H-THEOREM (1872):
Boltzmann proved that his H-function (related to entropy)
always decreases or stays constant for gas of atoms.
H is essentially -S.

LOSCHMIDT'S REVERSIBILITY OBJECTION:
"All microscopic laws are time-reversible. If you reverse
all velocities, the system runs backwards. The H-function
should sometimes increase. Contradiction."

BOLTZMANN'S REPLY:
"Yes, in principle entropy can decrease -- it's just
overwhelmingly improbable. The Second Law is statistical,
not absolute. You would have to wait longer than the age
of the universe for a macroscopic decrease."

This is correct. But it was philosophically unsatisfying
to his contemporaries.
```

### Boltzmann's Suicide in Context

Boltzmann died by suicide in 1906 while on vacation in Duino, Italy. The conventional story attributes his death partly to the hostility of the scientific establishment (especially Mach's positivism) to atomic theory.

```
THE MACH-BOLTZMANN BATTLE:

ERNST MACH'S POSITIVISM:
Only sensory observations are real.
Atoms are not observable -- they are metaphysical fictions.
Science should describe observable relations, not posit
unobservable entities.
"I don't believe that atoms exist" -- Mach's position.

BOLTZMANN'S RESPONSE:
Atoms explain thermodynamic properties quantitatively.
They predict Avogadro's number, Brownian motion, etc.
(Perrin's Brownian motion experiments confirmed atoms 1905-1908)
Positivism would eliminate the most fruitful part of physics.

INSTITUTIONAL CONTEXT:
Mach had enormous institutional influence in German-speaking
physics. Attacking atomism was not a fringe position in 1890-1905.
Boltzmann suffered repeated public criticism.

IRONY:
Einstein's 1905 Brownian motion paper provided conclusive
experimental confirmation of atoms. Perrin's 1908 experiments
settled the question. Mach eventually accepted atoms.
Boltzmann did not live to see his vindication.
```

### Kelvin's Age-of-Earth Calculation

William Thomson (Lord Kelvin, 1824-1907) applied thermodynamics to geology:

```
KELVIN'S CALCULATION:
Earth started molten. It is now cooler.
Given thermal conductivity and current temperature gradient:
how long has Earth been cooling?

Result: 20-100 million years (varying estimates over his career)

PROBLEM FOR DARWIN:
Natural selection requires enormous time.
Darwin estimated hundreds of millions of years minimum.
Kelvin's thermodynamics said this was impossible.

DARWIN'S RESPONSE:
"I am greatly troubled... I cannot explain heat production."
He had no answer. Kelvin's physics was seemingly correct.

RESOLUTION (1904-1905):
Radioactivity (Becquerel 1896, Curie 1898, Rutherford 1904).
Earth has internal heat SOURCES (radioactive decay).
Kelvin's calculation assumed no heat sources.
Rutherford reportedly told Kelvin this at a 1904 lecture.
Earth's age: ~4.5 billion years.

LESSON: Kelvin's physics was correct given his assumptions.
His assumptions were wrong because he didn't know about
radioactivity. Correct physics + wrong physical model = wrong result.
```

---

## Layer 2: Electromagnetism — Fields and the Unification of Light

### Faraday — The Field Concept

Michael Faraday (1791-1867) had no formal mathematical education but developed the **field concept** — perhaps the most important conceptual advance in 19th-century physics.

```
FARADAY'S EXPERIMENTS:

1. ELECTROMAGNETIC INDUCTION (1831):
   Moving a magnet near a coil induces current.
   The RATE OF CHANGE of magnetic flux through a circuit
   determines the induced EMF.
   (Later formalized as Faraday's Law of Induction)

2. LINES OF FORCE:
   Iron filings around a magnet trace curved lines.
   Faraday took these literally: the lines ARE the physical
   reality of the magnetic field.
   They mediate force -- no action at distance.
   This is what Maxwell later formalized mathematically.

ACTION AT DISTANCE (Newtonian view):
+--+    force propagates instantaneously    +--+
|N |  ================================>     |S |
+--+    across empty space                  +--+

FIELD CONCEPT (Faraday's view):
+--+    field pervades space, exerts        +--+
|N |-->-->-->-->-->-->-->-->-->-->-->-->-->  |S |
+--+    local force on local charge/magnet  +--+

The field is a physical entity, not just a mathematical tool.
This is why electromagnetic waves are possible:
a changing E-field creates a B-field, which creates an E-field...
the disturbance propagates through the field itself.
```

### Maxwell's Equations (1865)

James Clerk Maxwell (1831-1879) translated Faraday's qualitative field concepts into mathematical form, and added the **displacement current** — a crucial term that no experiment had directly observed but which was required for mathematical consistency.

```
MAXWELL'S EQUATIONS (differential form):

nabla . E = rho/epsilon_0            (Gauss's law: charges make E-fields)

nabla . B = 0                        (no magnetic monopoles)

nabla x E = -dB/dt                   (Faraday: changing B makes E)

nabla x B = mu_0*J + mu_0*epsilon_0*dE/dt
                          ^
                          Displacement current -- Maxwell's addition
                          (changing E-field acts like a current)

THE DISPLACEMENT CURRENT:
Ampere's original law: nabla x B = mu_0*J
Problem: In a capacitor charging circuit, no current flows
between the plates, but B-field is observed there.
Maxwell's fix: changing E-field also creates B-field.
This seems ad hoc but:
1. Makes the equations mathematically consistent (divergence of J = 0)
2. Predicts electromagnetic waves
```

### Prediction of Electromagnetic Waves

Maxwell derived electromagnetic wave equations from his four equations. The wave speed:

```
c = 1 / sqrt(mu_0 * epsilon_0)

mu_0 = magnetic permeability of free space (measured)
epsilon_0 = electric permittivity of free space (measured)

Plugging in measured values:
c = 1/sqrt(4pi x 10^-7 * 8.85 x 10^-12)
  = 2.998 x 10^8 m/s

Speed of light (Fizeau, 1849): 3.13 x 10^8 m/s
(modern: 2.998 x 10^8 m/s)

MAXWELL'S CONCLUSION (1865):
"This velocity is so nearly that of light, that it seems
we have strong reason to conclude that light itself
(including radiant heat and other radiations if any)
is an electromagnetic disturbance in the form of waves
propagated through the electromagnetic field."

This was: theory predicting a previously unknown connection
between two seemingly unrelated phenomena (electricity/magnetism
and light). Confirmed by Hertz 1887.
```

### Hertz Confirmation (1887)

Heinrich Hertz (1857-1894) generated and detected radio waves in his laboratory, confirming Maxwell's prediction:

```
HERTZ'S EXPERIMENT:

Transmitter:               Receiver:
+--------+                +----------+
|Spark   |  EM waves  --> | Wire loop|
|gap     |  ~600 MHz      | with gap |
+--------+                +----------+

Observed: Spark in receiver when transmitter fires.
Measured wavelength: consistent with Maxwell's equations.
Showed: reflection, refraction, polarization -- same as light.

HERTZ'S COMMENT:
"It's of no use whatsoever. This is just an experiment
that proves Maxwell was right."
(Asked what wireless telegraphy applications were possible.)

Within 10 years, Marconi was transmitting radio signals
across the Atlantic.
```

---

## Layer 3: Spectroscopy — Elements' Fingerprints

### Fraunhofer Lines (1814)

Joseph Fraunhofer systematically mapped the dark lines in the solar spectrum — 574 lines by 1821. He labeled the prominent ones A through K. He had no explanation for them.

```
SOLAR SPECTRUM:

Continuous rainbow spectrum + dark absorption lines:

Red    Orange  Yellow  Green   Blue   Violet
|      |       |       |       |       |
|      |      D|      b|      F|      H|
|      |   D1,D2      g|     H&K       |
|      |   (sodium)    (magnesium)     |
                                (calcium)

The D-lines correspond exactly to sodium's emission spectrum.
Fraunhofer saw this but couldn't explain it.
```

### Kirchhoff and Bunsen (1859-1860)

Gustav Kirchhoff and Robert Bunsen established the **spectroscopic identification of elements**:

```
KIRCHHOFF'S LAWS OF SPECTROSCOPY:

1. A hot dense gas (or solid) produces a continuous spectrum.

2. A hot, low-density gas produces an emission spectrum:
   bright lines at specific wavelengths characteristic of the element.

3. A cool gas in front of a hot continuum source produces
   an absorption spectrum: dark lines at the same wavelengths
   as the emission lines.

APPLICATION TO THE SUN:
The Sun's hot interior produces continuous spectrum.
The cooler outer atmosphere absorbs at specific wavelengths.
Dark Fraunhofer lines = elements in solar atmosphere absorbing.

D-lines = sodium in solar atmosphere.
This is chemistry at 150 million km distance.
```

**Helium discovery via spectroscopy (1868)**: Janssen and Lockyer observed a yellow spectral line in the solar chromosphere during an eclipse that matched no known element. Named helium (from Helios, the Sun). Found on Earth only in 1895 by Ramsay. This is the only element discovered in space before Earth.

### The Balmer Series — Waiting for Theory

Johann Balmer (1825-1898) in 1885 noticed that the visible hydrogen spectral lines followed a formula:

```
BALMER'S FORMULA (empirical):

lambda = B * n^2/(n^2 - 4)   where n = 3, 4, 5, 6...
B = 364.6 nm (Balmer constant)

Or equivalently:
1/lambda = R_H * (1/2^2 - 1/n^2)

R_H = Rydberg constant = 1.097 x 10^7 m^-1

This perfectly predicted hydrogen's visible spectral lines.
Nobody knew WHY.

BALMER SERIES: n=3->2, n=4->2, n=5->2, n=6->2
LYMAN SERIES (UV, discovered 1906): n->1
PASCHEN SERIES (IR, discovered 1908): n->3

The formula was purely empirical. Explanation had to wait for
Bohr's model (1913) -- and Bohr's explanation was itself
provisional, replaced by quantum mechanics in 1925-26.

THE RYDBERG CONSTANT was measured to extraordinary precision.
It remains the most precisely measured fundamental constant.
```

---

## Layer 4: The Ether Problem

### What the Ether Was

Maxwell's equations describe waves propagating through... what? Newton's mechanical philosophy said waves require a medium. Light is a wave (Young's double slit, 1801, proved this). Therefore light requires a medium: the **luminiferous ether**.

```
PROPERTIES REQUIRED OF THE ETHER:

1. Fills all of space (light propagates everywhere)
2. Extremely rigid (light speed is enormous; wave speed in
   medium proportional to sqrt(rigidity/density))
3. Has near-zero density (planets move through it unimpeded)
4. Perfectly transparent
5. Provides absolute reference frame for Maxwell's equations

Properties 2 and 3 are contradictory.
A medium that is rigid enough to transmit light at 3x10^8 m/s
should be detectable by planetary orbital perturbations.
```

### Michelson-Morley Experiment (1887)

Albert Michelson and Edward Morley designed an interferometer to measure Earth's velocity through the ether. If the ether exists and Earth moves through it, the speed of light should be slightly different in the direction of Earth's motion vs perpendicular to it.

```
MICHELSON INTERFEROMETER:

Light source --> half-silvered mirror
                    |           |
                    v           v
                Mirror 1    Mirror 2
                    |           |
                    |           |
                    +-----+-----+
                          |
                        Detector

Arm 1: along Earth's orbital velocity
Arm 2: perpendicular to Earth's orbital velocity

EXPECTED (if ether exists):
Earth moves at ~30 km/s through ether
Light going with ether: faster
Light going against ether: slower
Interference fringe pattern should shift as apparatus rotates.

Expected fringe shift: ~0.4 fringe
Measurement sensitivity: 0.01 fringe
Observed shift: ~0.02 fringe (consistent with zero, within error)

RESULT: No ether wind detected.
The speed of light is the same in all directions.

INITIAL REACTIONS:
Michelson himself was disappointed -- he expected to measure
the ether.
Most physicists assumed instrumental error.
Lorentz and FitzGerald proposed that lengths contract along
direction of motion (true, but as ad hoc fix for ether).
Einstein (1905) eliminated the ether entirely.
```

---

## Layer 5: The Two Clouds — Ultraviolet Catastrophe and Photoelectric Effect

### The Ultraviolet Catastrophe

Classical thermodynamics + Maxwell's electromagnetic theory made a prediction for **blackbody radiation** (the spectrum emitted by a hot object) that was spectacularly wrong:

```
RAYLEIGH-JEANS LAW (classical):
Energy density per unit frequency: u(v) = 8*pi*v^2/c^3 * k_B*T

As v --> infinity (ultraviolet, X-ray): u(v) --> infinity
A hot object should radiate INFINITE energy at high frequencies.
This is the "ultraviolet catastrophe."

EXPERIMENTALLY:
Blackbody spectrum peaks at a finite frequency and decreases
at high frequencies. No catastrophe.

PLANCK'S FIX (1900):
Assume energy is emitted in discrete chunks: E = hv
(h = Planck's constant, v = frequency)

This means high-frequency modes are suppressed because they
require large energy quanta -- exponentially less probable.

Planck's law:
u(v) = 8*pi*h*v^3/c^3 * 1/(exp(hv/k_BT) - 1)

Matches experiment perfectly across all frequencies.

PLANCK'S OWN VIEW:
He called it "an act of desperation" -- a mathematical trick.
He did not believe energy quantization was physically real.
It took Einstein (1905) and later quantum mechanics to show
that it is.
```

### The Photoelectric Effect

Light shining on a metal surface ejects electrons. Classical predictions:
- Intensity (brightness) should determine ejection energy
- Any frequency should work given sufficient intensity
- Time delay expected while electrons accumulate energy

Observations (Hertz 1887, Lenard 1902):
- **Frequency** determines maximum electron energy, not intensity
- Below a threshold frequency, no electrons ejected regardless of intensity
- No time delay — instantaneous ejection

```
CLASSICAL PREDICTION vs OBSERVATION:

                Predicted (classical)    Observed
Max electron    proportional to          proportional to
kinetic energy  intensity                FREQUENCY

Below threshold no threshold exists      no electrons ejected
frequency                                at any intensity

Time delay      yes, for low intensity   no, instantaneous

Einstein's explanation (1905):
Light consists of discrete quanta (photons), each with energy E = hv.
One photon interacts with one electron.
If hv < work function phi: electron not ejected.
If hv >= phi: electron ejected with KE = hv - phi.
Intensity = number of photons, not energy per photon.

This required treating light as PARTICLES -- contradicting
Maxwell's wave theory.
Wave-particle duality: one of the central puzzles of quantum mechanics.

Einstein won the Nobel Prize (1921) for this, not relativity.
```

---

## Fin de Siecle Physics — The False Confidence

```
THE PREVAILING MOOD (~1895):

Lord Kelvin's "Two Clouds" speech (1900 actually):
"The beauty and clearness of the dynamical theory [of heat
and light] is at present obscured by two clouds."
  Cloud 1: Michelson-Morley (ether problem)
  Cloud 2: Equipartition theorem and blackbody radiation

Phillips (apocryphal): "Physics is essentially complete."
Incoming students reportedly advised to do biology instead.
Michelson himself (1894): "The more important fundamental laws
and facts of physical science have all been discovered."

IRONY:
Both "small clouds" required revolutionary new physics:
  Cloud 1 (ether) --> Special Relativity (1905)
  Cloud 2 (radiation) --> Quantum Mechanics (1900-1926)

Both demolished Newtonian mechanics as a fundamental framework.
Physics in 1905 was not nearly complete -- it was on the verge
of its deepest transformation since Newton.
```

---

## Decision Cheat Sheet

| You want to understand... | Key figure/event | Key point |
|---------------------------|-----------------|-----------|
| Why Carnot's result is fundamental | Carnot efficiency limit | Only depends on temperatures, not working substance |
| Why Boltzmann's atomism was controversial | Mach's positivism | Atoms unobservable; Second Law statistical not absolute |
| What was genuinely new in Faraday | Field concept | Fields as physical entities, not mathematical conveniences |
| Why Maxwell's equations are a unification | Speed of light falls out of EM constants | Light is an electromagnetic phenomenon |
| Why Michelson-Morley was a crisis | Expected ether wind, found nothing | Light speed same in all directions -- no absolute frame |
| Why Planck's quantum was "an act of desperation" | UV catastrophe | Classical physics predicted infinite radiation; Planck's fix worked but he didn't believe it |

---

## Common Confusion Points

**Carnot used the wrong theory (caloric) but got the right answer.** The mathematical structure of the Carnot efficiency is independent of whether heat is a fluid or kinetic energy. Carnot's law is correct.

**Boltzmann's suicide was not solely caused by physics disputes.** He had lifelong depression. The professional hostility was real and was a factor, but attributing his death entirely to Mach vs atoms is oversimplified.

**Maxwell's displacement current was not just a mathematical fix.** It was motivated by the physical requirement that charge be conserved (divergence of current must equal zero). Consistency requirement --> novel prediction (EM waves).

**The Michelson-Morley experiment did not prove there is no ether.** It showed no ether wind. Lorentz's length-contraction hypothesis could also explain it while retaining the ether. Einstein's move was to treat the constancy of c as a postulate and eliminate the ether as unnecessary.

**Planck did not propose that light consists of photons.** He proposed that energy exchange between matter and radiation is quantized. Einstein (1905) extended this to say light itself consists of discrete quanta. Planck resisted this interpretation for years.
