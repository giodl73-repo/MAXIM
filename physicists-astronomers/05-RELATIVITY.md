# Relativity — Einstein, Minkowski, Schwarzschild

## The Two Theories

Einstein produced two theories of relativity, separated by 10 years, each
a conceptual revolution:

```
SPECIAL RELATIVITY (1905)
==========================
Domain: Inertial frames (constant velocity), no gravity.
Insight: The speed of light is the same for ALL observers.
         There is no absolute simultaneity.
         Space and time are unified into spacetime.
Result: E = mc², time dilation, length contraction, relativity of simultaneity.
         Lorentz transformations are correct geometry, not physical contraction.

GENERAL RELATIVITY (1915)
==========================
Domain: Accelerating frames, gravity.
Insight: Gravity is not a force — it's curved spacetime.
         Matter curves spacetime; curved spacetime tells matter how to move.
Result: Einstein field equations. Predicts: gravitational lensing,
        black holes, gravitational waves, Big Bang, GPS corrections.

CONNECTION:
  SR: flat spacetime (Minkowski space) with Lorentz symmetry.
  GR: curved spacetime with general covariance.
  GR reduces to SR in the absence of gravity (locally flat spacetime).
```

---

## Albert Einstein (1879–1955)

### Who He Was

German-Swiss-American physicist. Failed to get an academic job after graduation;
worked as a patent clerk in Bern. In 1905 (his "miracle year"), published 5 papers
including special relativity, the photoelectric effect (Nobel Prize 1921), and
Brownian motion. Developed general relativity 1907–1915.

Fled Nazi Germany in 1933 to Princeton's Institute for Advanced Study.
Spent his last 25 years working unsuccessfully on a unified field theory.
His final calculation on the night before he died was on unified field theory.

### Special Relativity (1905)

**The Two Postulates**

```
EINSTEIN'S TWO POSTULATES OF SPECIAL RELATIVITY
=================================================

1. THE PRINCIPLE OF RELATIVITY:
   The laws of physics are the same in all inertial reference frames.
   (Galileo's principle, extended to ALL physics — not just mechanics.)

2. CONSTANCY OF THE SPEED OF LIGHT:
   The speed of light in vacuum is c ≈ 3 × 10⁸ m/s,
   independent of the motion of the source or observer.

THESE TOGETHER IMPLY EVERYTHING:
  - No absolute rest. No ether.
  - Simultaneity is relative: two events simultaneous in one frame
    may not be simultaneous in another.
  - Time dilation: moving clocks run slow.
  - Length contraction: moving objects are shorter.
  - Mass-energy equivalence.
```

**The Lorentz Factor and Consequences**

```
THE LORENTZ FACTOR
==================

γ = 1/√(1 - v²/c²)

  v = relative velocity between frames
  v → 0: γ → 1 (Newtonian limit)
  v → c: γ → ∞ (infinite energy required to reach c)

TIME DILATION:
  A clock moving at speed v ticks more slowly by factor γ.
  Δt' = γ Δt  (proper time t' in moving frame; coordinate time t in rest frame)

  Example: Cosmic ray muons created at 15 km altitude.
    Muon lifetime: τ = 2.2 μs (measured at rest)
    Speed: v ≈ 0.998c, γ ≈ 16
    Without dilation: they'd travel 0.998c × 2.2μs ≈ 660 m → most wouldn't reach ground
    With dilation: they travel 16 × 660 m ≈ 10 km → they reach the ground. Observed.

LENGTH CONTRACTION:
  A rod moving at speed v is shorter by factor γ.
  L = L₀/γ  (L₀ = proper length in rest frame)

RELATIVITY OF SIMULTANEITY:
  Two events at x₁ ≠ x₂ that are simultaneous (Δt = 0) in one frame
  have time separation Δt' = -γvΔx/c² in a moving frame.
  Simultaneity is not absolute.
```

**Mass-Energy Equivalence: E = mc²**

```
E = mc²
========

The full equation: E² = (pc)² + (mc²)²
  E = total energy
  p = momentum
  m = rest mass

For an object at rest (p = 0): E = mc²
For a photon (m = 0): E = pc

E = mc² says: mass is a form of energy.
  Converting mass to energy releases enormous energy density.
  1 kg of mass ↔ 9 × 10¹⁶ J = 21.5 megatons of TNT equivalent

Examples:
  Nuclear fission: ~0.1% of mass converted to energy
  Nuclear fusion: ~0.7% of mass converted to energy
  Matter-antimatter annihilation: 100% mass to energy

  The Sun converts 4 million tons of mass to energy every second
  via proton-proton fusion.

Kinetic energy in SR:
  KE = (γ-1)mc²  → (1/2)mv² when v << c  (Newtonian limit)
```

### General Relativity (1915)

**The Equivalence Principle**

```
EINSTEIN'S EQUIVALENCE PRINCIPLE
==================================

Einstein's "happiest thought" (1907):
  A person in a closed elevator with no windows cannot tell whether
  they are standing on Earth (gravity g) or accelerating in space at g.

  Gravity and acceleration are LOCALLY INDISTINGUISHABLE.

Consequence: In a small enough region of spacetime, you can always
  find a freely-falling frame where gravity disappears.
  (In a falling elevator: objects float weightlessly.)

This means: General relativity must be formulated so that the
  equations look the same in all frames — including accelerating ones.
  The mathematics for this: differential geometry (Riemann's geometry!).
```

**The Einstein Field Equations**

```
EINSTEIN FIELD EQUATIONS
=========================

G_μν = (8πG/c⁴) T_μν

Or equivalently: R_μν - ½Rg_μν = (8πG/c⁴) T_μν

  G_μν = Einstein tensor (describes spacetime curvature)
  T_μν = stress-energy tensor (describes matter + energy distribution)
  g_μν = metric tensor (encodes spacetime geometry)
  R_μν = Ricci curvature tensor
  R = Ricci scalar
  G = Newton's gravitational constant
  c = speed of light

IN WORDS: "Spacetime curvature = 8πG/c⁴ × energy-momentum content"
  Or Wheeler's summary: "Matter tells spacetime how to curve.
  Curved spacetime tells matter how to move."

These are 10 coupled nonlinear PDEs (the metric has 10 independent components).
Exact solutions are rare and prized.
```

**Predictions and Confirmations**

```
GENERAL RELATIVITY PREDICTIONS — STATUS
=========================================

1. Perihelion precession of Mercury:
   43 arcseconds/century (unexplained by Newton). GR predicts exactly this.
   Confirmed 1915 (explained existing data).

2. Gravitational light deflection:
   Light bends near massive objects.
   Einstein: 1.75 arcseconds near the Sun's limb.
   Confirmed 1919 (Eddington's eclipse expedition — made Einstein world-famous).

3. Gravitational redshift:
   Photons climbing out of a gravity well lose energy → shift to lower frequency.
   Confirmed 1959 (Pound-Rebka experiment, Harvard tower).
   GPS satellites run fast by ~45 μs/day due to weaker gravity (compensated).

4. Gravitational waves:
   Predicted 1916. First detected September 14, 2015 (LIGO).
   Two black holes, 1.3 billion light-years away, 36 + 29 solar masses, merged.
   Nobel Prize 2017 (Weiss, Barish, Thorne).

5. Black holes:
   Predicted by Schwarzschild (1916 — see below).
   First image: 2019 (Event Horizon Telescope — M87* black hole).
   Milky Way center: 2022 (Sagittarius A*).

6. Expanding universe:
   GR allows (requires) a non-static universe. Einstein added a
   "cosmological constant" Λ to make it static. When Hubble showed
   the universe is expanding (1929), Einstein called Λ "my greatest blunder."
   Λ is now back — it's dark energy (discovered 1998).
```

---

## Hermann Minkowski (1864–1909)

### Who He Was

German mathematician, Einstein's former professor (Einstein reportedly skipped
his classes). Minkowski took Einstein's special relativity (1905) and gave
it the correct geometric interpretation in 1907–1908. Died of appendicitis at 44.

### The Contribution: Spacetime Geometry

**Minkowski Spacetime**

```
MINKOWSKI SPACETIME
====================

Einstein's 1905 paper was algebraic: Lorentz transformations as equations.
Minkowski's 1907 paper: Special relativity is GEOMETRY in 4D spacetime.

The spacetime interval:
  ds² = -c²dt² + dx² + dy² + dz²    (Minkowski metric, signature -+++)

  This is the 4D "distance" between events.
  It is INVARIANT — all observers agree on ds²,
  even though they disagree on Δt, Δx, Δy, Δz individually.

Three types of separation:
  ds² < 0: TIMELIKE — events that can be causally connected
           |Δr| < c|Δt|: the separation is inside the light cone
  ds² > 0: SPACELIKE — events too far apart for any signal to connect them
           |Δr| > c|Δt|: outside the light cone
  ds² = 0: LIGHTLIKE (null) — only light can connect them
           |Δr| = c|Δt|: on the light cone

THE LIGHT CONE:
  ┌─────────────────────────────┐
  │         FUTURE LIGHT CONE   │
  │              /\             │
  │             /  \            │
  │            / ds²=0           │
  │           /      \          │
  │      ────/────────\────── t │
  │         /    NOW   \        │
  │        /            \       │
  │       /              \      │
  │      / PAST LIGHT CONE\     │
  └─────────────────────────────┘

  Only events in the past light cone can have caused NOW.
  Only events in the future light cone can be affected by NOW.
```

Minkowski's famous quote: "Henceforth space by itself, and time by itself,
are doomed to fade away into mere shadows, and only a kind of union of the
two will preserve an independent reality."

---

## Karl Schwarzschild (1873–1916)

### Who He Was

German physicist and astronomer. Director of the Astrophysical Observatory
in Potsdam. When Einstein published his general relativity in November 1915,
Schwarzschild — serving in the German army on the Russian front — found the
first exact solution. He sent the paper to Einstein in December 1915 from the trenches.
He died in May 1916 from an autoimmune disease (pemphigus) contracted on the front.

### The Contribution: The Schwarzschild Solution and Black Holes

**The Schwarzschild Metric**

```
SCHWARZSCHILD SOLUTION (1916)
==============================

The exact spacetime metric outside a non-rotating spherical mass M:

ds² = -(1 - r_s/r)c²dt² + dr²/(1 - r_s/r) + r²(dθ² + sin²θ dφ²)

Schwarzschild radius:
  r_s = 2GM/c²

For the Sun: r_s ≈ 3 km (compared to actual radius 700,000 km)
For Earth:  r_s ≈ 9 mm

WHAT HAPPENS AS r → r_s:
  The metric component g_tt = -(1 - r_s/r) → 0
  Time effectively stops for an outside observer.
  A clock at r_s runs infinitely slow (gravitational time dilation → ∞).

  A falling observer crosses r_s in finite proper time and notices nothing special.
  An outside observer sees the falling object slow to a stop and redshift to infinity.

THE EVENT HORIZON at r = r_s:
  A surface from which nothing (not even light) can escape.
  Not a physical surface — the Schwarzschild coordinates break down here.
  (Kruskal-Szekeres coordinates extend smoothly through it.)

BLACK HOLES:
  If mass is compressed inside r_s, you get a black hole.
  The singularity at r = 0 is where current physics breaks down
  (quantum gravity needed).
```

**The Singularity — What Schwarzschild's Solution Implies**

Inside the event horizon, the roles of r and t switch: r becomes timelike
(future-directed), t becomes spacelike. This means: inside the horizon,
the singularity at r = 0 is not a point in space but a moment in time
— an inevitable future for anything that falls in.

---

## Comparison Table

| Figure | Dates | Core Contribution | Technical Requirement | Legacy |
|--------|-------|-------------------|-----------------------|--------|
| **Einstein (SR)** | 1905 | Time dilation, E=mc², relativity of simultaneity | Algebra, physical insight | All high-energy physics |
| **Einstein (GR)** | 1915 | Gravity = spacetime curvature, field equations | Riemannian geometry | Cosmology, GPS, gravitational waves |
| **Minkowski** | 1907 | Geometric formulation of SR, spacetime | Differential geometry | GR mathematical language |
| **Schwarzschild** | 1916 | First GR exact solution, black hole metric | Solving PDEs | Black hole physics, tests of GR |

---

## Who to Cite for What

| Concept | Cite | Notes |
|---------|------|-------|
| Special relativity | Einstein | 1905 |
| Two postulates of SR | Einstein | Foundation |
| E = mc² | Einstein | 1905 (derived same year) |
| Time dilation, length contraction | Einstein (derived) + Lorentz (equations) | |
| General relativity | Einstein | 1915 |
| Einstein field equations | Einstein | |
| Equivalence principle | Einstein | Key insight of GR |
| Spacetime as 4D geometric object | Minkowski | 1907–1908 |
| Spacetime interval / metric signature | Minkowski | |
| Schwarzschild metric / event horizon | Schwarzschild | 1916 |
| Schwarzschild radius r_s = 2GM/c² | Schwarzschild | |

---

## Common Confusion Points

**"E = mc² means you can convert mass to energy"** — It means mass IS energy.
The total energy of a system is E² = (pc)² + (mc²)². At rest (p=0), E = mc².
Nuclear reactions don't "convert mass to energy" in the sense of destroying mass —
they convert rest mass energy into kinetic energy of products. The mass defect
(binding energy) is what gets released as kinetic energy.

**"Light slows down in GR gravity"** — Locally, light always travels at c. The
apparent slowing (Shapiro delay) is because the spacetime metric means the coordinate
speed of light changes, but the locally-measured speed is always c. The distinction
between coordinate speed and locally measured speed is crucial in GR.

**"Black holes suck things in"** — At large distances, a black hole has the same
gravitational pull as any other mass of the same value. The Earth would not be
affected if the Sun somehow became a black hole (except for the loss of light).
Black holes are "dangerous" only if you get very close (within a few Schwarzschild
radii).

**"Einstein didn't like quantum mechanics because he was old"** — Einstein's objections
were specific and technical. EPR (Einstein-Podolsky-Rosen) paper (1935) was a
carefully constructed argument that QM is incomplete. Bell's theorem (1964) and
Bell test experiments (Aspect 1982, conclusive experiments 2015) showed that QM's
"spooky action at a distance" is real — the correlations cannot be explained by
hidden variables. Einstein was wrong on QM, but not for lack of rigor.
