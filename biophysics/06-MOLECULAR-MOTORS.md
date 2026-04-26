# Molecular Motors — Brownian Ratchets, Force Generation, and Energy Transduction

## The Big Picture

```
┌──────────────────────────────────────────────────────────────────────────┐
│                 MOLECULAR MOTORS LANDSCAPE                               │
│                                                                          │
│  SHARED MECHANOCHEMICAL CYCLE (all P-loop NTPases):                      │
│  ATP bind → conformational change (power stroke) → force/torque →        │
│  ATP hydrolysis → product release (ADP, Pi) → reset                      │
│  Linear motors: conformational change → linear translation on track      │
│  Rotary motors: conformational change → rotation of c-ring or γ shaft    │
│                                                                          │
│  LINEAR MOTORS                   ROTARY MOTORS                           │
│  ─────────────                   ─────────────                           │
│  Kinesin: + end directed         ATP synthase (F₀F₁)                     │
│  Dynein: - end directed          Bacterial flagellar motor               │
│  Myosin II: muscle contraction   DNA polymerase (rotary on helical track) │
│  Myosin V: vesicle transport                                             │
│                                                                          │
│  TRACK               MOTOR           FUNCTION                            │
│  ──────────────────────────────────────────────────────────────────────  │
│  Microtubule (+ end)  Kinesin-1      Anterograde axonal transport        │
│  Microtubule (- end)  Cytoplasmic dynein  Retrograde + mitosis           │
│  Actin filament       Myosin II       Muscle contraction, cytokinesis    │
│  Actin filament       Myosin V        Vesicle/organelle transport        │
│  Actin filament       Myosin VI       Endocytosis (- end directed)       │
│  None                 ATP synthase    Proton gradient → ATP              │
│  Flagellar basal body Flagellar motor Bacterial motility                 │
│                                                                          │
│  ENERGY SCALE:                                                           │
│  Kinesin stall force × step: 7 pN × 8 nm = 56 pN·nm ≈ 14 k_BT per step   │
│  ATP hydrolysis in vivo: ~50 pN·nm ≈ 12 k_BT → efficiency ~25-50%        │
│  Stall force:  kinesin ~7 pN, myosin II ~3-5 pN per head                 │
│  ATP synthase: 120° rotation per ATP, ~25 k_BT free energy per ATP       │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Section 1 — The Brownian Ratchet Concept

### Why Thermal Noise Matters

At the scale of molecular motors (nm dimensions, pN forces), thermal fluctuations
dominate. k_BT ≈ 4.1 pN·nm at 310 K. A kinesin motor doing ~8 pN·nm of work per
step is working against energy comparable to 2 k_BT per step. The motor cannot
work without thermal fluctuations — it exploits them.

### The Ratchet Principle

A Brownian ratchet converts directed (asymmetric) thermal fluctuations into net
directed motion. The key: the asymmetry must break detailed balance.

```
  SYMMETRIC POTENTIAL:               FLASHING RATCHET:

  V(x)  /\/\/\/\/\              V(x) ON:   /\/\/\/\/\
  →  no net motion                  OFF: ___________  (flat)

  Symmetric barriers: equal          Particle diffuses freely when flat,
  probability of going left/right    then falls into asymmetric potential
  → no net drift                     → net rightward drift

  Require: asymmetric potential (different slopes on left/right)
           energy input to "flash" between states
           → breaks time-reversal symmetry
```

**Feynman's ratchet-and-pawl** (1963 Lectures): at equilibrium, a ratchet cannot
do directed work from thermal fluctuations alone (Brownian motor at equilibrium
violates 2nd law). A ratchet does useful work only when driven away from equilibrium
by an external energy input — in molecular motors, by ATP hydrolysis.

### Key Features of a Molecular Brownian Ratchet

1. **Asymmetric binding sites**: track has structural polarity (+ vs. - end)
2. **State-dependent binding**: strong vs. weak binding states driven by ATP cycle
3. **ATP hydrolysis**: provides the free energy to drive the asymmetry
4. **Thermal fluctuations**: drive the diffusive search within weak-binding state

---

## Section 2 — Kinesin

### Structure and Track

Kinesin-1 is a dimer: two ~45 kDa motor domains ("heads"), each with an ATP
binding site (P-loop) and a microtubule-binding site:

```
  KINESIN STRUCTURE:

  [Head 1] — coiled-coil stalk — [Head 2]
      |                               |
      |    neck linker (~14 aa)        |
  MT binding site                MT binding site

  Head diameter: ~5 nm
  Step size: 8 nm (= tubulin dimer repeat)
  Processivity: ~100 steps per run (processive motor)
  → Kinesin walks hand-over-hand, like a person walking

  Microtubule track:
  (+end) ----α-β-α-β-α-β-α-β---- (-end)
         ←─────── 8 nm ──────→
  Kinesin walks toward + end (anterograde, away from nucleus)
```

### Mechanochemical Cycle

The key coupling: ATP hydrolysis conformational changes are mechanically linked
to track detachment and forward translocation.

```
  STATE 1: Both heads bound, lead head (apo/ADP state)
  ↓
  ATP binds to trailing head
  ↓
  STATE 2: ATP binding → neck linker docks (power stroke)
    → swings unbound head forward ~16 nm
    → unbound head finds new binding site 8 nm ahead
  ↓
  STATE 3: New lead head binds MT, releases ADP
    → tight-binding ADP-free state
  ↓
  STATE 4: Trailing head: Pi released → weak binding
    → trailing head detaches (ATP already hydrolyzed → ADP bound)
  ↓
  Back to STATE 1: one step completed, 8 nm advance

  Net: 1 ATP per step, 8 nm advance, ~8 pN·nm work
```

### Force-Velocity Relationship and Stall Force

Under load F opposing forward motion:

```
  Stall force: kinesin stall ≈ 7 pN

  Force-velocity relationship (approximately linear near stall):
    v(F) ≈ v_max × (1 - F/F_stall)

  v_max (no load) ≈ 800 nm/s ≈ 100 steps/s
  v at F_stall ≈ 0

  Efficiency: W_mech / ΔG_ATP = (7 pN × 8 nm) / (50 pN·nm)
            = 56 pN·nm / 50 pN·nm ≈ 1.1? → apparent >100%?

  Resolution: stall force is maximum against a constant load.
  In vivo, step size can vary; true efficiency ≈ 25-50% for kinesin.
  (At maximum power output, efficiency < thermodynamic maximum.)
```

---

## Section 3 — Dynein

### Structure

Cytoplasmic dynein is the largest motor protein (~1.4 MDa dimer):

```
  DYNEIN STRUCTURE:

  Ring of 6 AAA+ domains (AAA1-AAA6) per head
  ATP hydrolysis: primarily AAA1, AAA3
  Stalk: projects from AAA4/5 → MT binding domain at tip
  Linker: AAA1-N terminus — major mechanical element

  Direction: minus-end directed (toward nucleus, centrosome)
  Step size: variable, 8-32 nm (not tightly coupled to ATP)
  Processivity: intrinsically low; requires dynactin cofactor for processive cargo

  Dynein is far more complex than kinesin:
  kinesin: simple dimer, well-characterized mechanism
  dynein: ring motor, sidesteps possible, mechanism still debated
```

### Dynein vs. Kinesin

```
  ┌──────────────────────────────────────────────────────────────────┐
  │  PROPERTY         │  KINESIN-1          │  DYNEIN (cytoplasmic)  │
  │  ─────────────── │  ─────────────────  │  ────────────────────   │
  │  Direction        │  + end              │  - end                 │
  │  Step size        │  8 nm (constant)    │  8-32 nm (variable)    │
  │  Stall force      │  ~7 pN              │  ~1 pN (solo)          │
  │                   │                     │  ~7 pN (with dynactin) │
  │  Processivity     │  ~100 steps/run     │  ~10 steps; needs      │
  │                   │                     │  dynactin/BICD2        │
  │  ATP coupling     │  Tight (1:1)        │  Loose, uncoupled      │
  │  Structural family│  Kinesin superfamily│  AAA+ ATPase           │
  │  Major function   │  ER, Golgi, mito    │  Endosomes, nucleus,   │
  │                   │  anterograde        │  retrograde, mitosis   │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Section 4 — Myosin

### Myosin II: Muscle Contraction

Myosin II is a non-processive motor (single detachment per ATP) that works in
large ensembles in muscle fibers:

```
  MYOSIN II HEAD (lever arm model):

  Structure: motor domain + lever arm (3-4 IQ motifs) + tail (dimerization)
  Lever arm length: ~10 nm
  Power stroke: lever arm swings ~45-60° → ~5 nm displacement

  CROSSBRIDGE CYCLE (Lymn-Taylor, 1971):

  Step 1: Myosin-ADP-Pi (cocked state) binds actin (strong binding)
  ↓
  Step 2: Pi release → power stroke (lever arm swings from "up" to "down")
          → generates ~3-5 pN force, ~5 nm displacement
  ↓
  Step 3: ADP released → rigor state (strong binding, no ATP)
  ↓
  Step 4: ATP binds → rapid detachment from actin
  ↓
  Step 5: ATP hydrolysis → myosin returns to cocked state (reprimes)
```

### Sliding Filament Model: Muscle

In sarcomeres, thick (myosin) and thin (actin) filaments interdigitate:

```
  Sarcomere (2.2 μm at rest):

  Z──────────────────────────────────Z
  |  thin (actin)                     |
  |  ─────────────     ───────────── |
  |              thick (myosin)       |
  |         ─────────────────────── │
  |  ─────────────     ───────────── │
  Z──────────────────────────────────Z

  Contraction: myosin heads on thick filament pull thin filament inward
  → Z-lines approach → sarcomere shortens

  Whole muscle:
    Force: ~0.5-1 N/mm² (specific force)
    Shortening velocity: up to 10 lengths/s (velocity ∝ g_detachment)
    P-V curve: v = v_max × (P₀-P)/(P₀+P/a)  (Hill equation)
```

### Myosin V: Processive Transport

Myosin V carries vesicles on actin in non-muscle cells:

```
  Lever arm: 6 IQ motifs → ~24 nm → step size ≈ 36 nm (actin helical repeat)
  Processive: hand-over-hand walking, ~100 steps per run
  Speed: ~400-600 nm/s (slower than kinesin, longer step)
  Stall force: ~2-3 pN

  Structural symmetry between kinesin (MT) and myosin V (actin):
    Both: hand-over-hand, processive, dimeric, one head bound at a time
    Convergent evolution of the walking mechanism
```

---

## Section 5 — ATP Synthase: Rotary Motor

### F₀F₁-ATP Synthase

ATP synthase (F₀F₁ or Complex V in mitochondria) is a rotary molecular motor.
It can run in both directions: synthesis (using proton gradient) or hydrolysis
(pumping protons using ATP — when membrane potential collapses).

```
  STRUCTURE:

                         ┌─────────────────────────────┐
  Matrix                 │  F₁: soluble, catalytic head │
                         │  α₃β₃γδε: γ subunit rotates │
                         │  inside α₃β₃ hexamer        │
                         └──────────────┬──────────────┘
                                        │  central stalk (γε)
  Inner                  ┌─────────────┴──────────────┐
  membrane               │  F₀: membrane sector        │
                         │  a + b₂: stator (static)    │
                         │  c-ring: 10-15 c subunits    │
                         │          rotates with γ      │
                         └─────────────────────────────┘
  Intermembrane
  space (high [H⁺])
```

### Mechanism: Binding Change Mechanism (Paul Boyer, Nobel 1997)

```
  Each β subunit cycles through three states:
    L (loose): ADP + Pi bound
    T (tight): ATP forms spontaneously (binding energy drives synthesis!)
    O (open):  ATP released

  The γ subunit rotation interconverts states:
    120° rotation → all three β subunits advance one state

  Proton flow drives γ rotation:
    c-ring + γ rotate together
    H⁺ enters from periplasm → binds c subunit → ring rotates
    H⁺ exits to matrix after traversing c-ring

  Stoichiometry:
    c-ring has 8-15 c subunits (species-dependent)
    Each H⁺ rotates ring by 360°/c
    Three β subunits → 3 ATPs per full 360° rotation
    H⁺/ATP = c/3 subunits

    For c = 10 (E. coli): 10/3 = 3.3 H⁺ per ATP
    For c = 8 (bovine): 8/3 = 2.7 H⁺ per ATP

  Torque: ~40 pN·nm per step (largest torque of any molecular motor)
  Rotation speed: ~100 rev/s = 6000 RPM under physiological load
```

### Single-Molecule Rotation Experiments

Noji et al. (1997): attached actin filament to γ subunit, observed rotation
under epifluorescence. Confirmed:
- Counterclockwise rotation (viewed from F₁) during ATP hydrolysis
- Steps of 120° (one per ATP)
- Sub-steps: 80° then 40° within each 120° (fast and slow sub-steps)
- Torque measured by angular drag of actin filament

---

## Section 6 — Flagellar Motor

The bacterial flagellar motor is a molecular turbine driven by proton gradient:

```
  STRUCTURE:

  External filament: hollow helical propeller
  Hook: flexible joint
  Basal body: 20+ proteins, MS ring, C ring, stators

  MECHANISM:
    Stator units (MotAB): fixed to cell wall, span membrane
    H⁺ enters through stator → electrochemical force on C-ring
    C-ring + M/S-ring rotate → hook + filament rotate
    Switch protein (FliM in C-ring) switches CW ↔ CCW rotation

  PERFORMANCE:
    Speed: up to 1000 RPM (E. coli); some species >100,000 RPM
    Torque: ~1000-4000 pN·nm per motor
    Stall force: ~600 pN (measured with optical tweezers)
    H⁺ per revolution: ~1200 H⁺
    Efficiency: near-100% near stall (thermodynamic limit)

  CHEMOTAXIS:
    CW rotation: flagellar bundle unbundles → "tumble"
    CCW rotation: flagellar bundle → "run" (swimming)
    CheA/CheY cascade: [attractant] → less tumbling → runs toward gradient
```

---

## Section 7 — Single-Molecule Force Measurements

Force-velocity curves and stall forces measured with optical tweezers (see also
07-SINGLE-MOLECULE.md):

```
  ┌──────────────────────────────────────────────────────────────────┐
  │  MOTOR         │  STALL FORCE  │  SPEED (no load) │  STEP SIZE   │
  │  ─────────────  │  ───────────  │  ────────────────  │  ─────────  │
  │  Kinesin-1      │  ~7 pN        │  800 nm/s         │  8 nm      │
  │  Cytoplasmic    │  ~1 pN solo   │  variably          │  8-32 nm  │
  │  dynein         │  ~7 pN w/dyn  │  variable         │  variable  │
  │  Myosin II      │  ~3-5 pN/head │  ~800 nm/s (max)  │  5 nm      │
  │  Myosin V       │  ~2-3 pN      │  400-600 nm/s     │  36 nm     │
  │  RNA polymerase │  ~25-30 pN    │  ~10-50 nt/s      │  0.34 nm   │
  │  DNA polymerase │  ~34 pN       │  ~200-500 bp/s    │  0.34 nm   │
  └──────────────────────────────────────────────────────────────────┘
```

---

## CS, Mechanics, and Thermodynamics Bridges

Molecular motors are physical machines whose behavior can be understood entirely through state machines, thermodynamic engine theory, and stochastic dynamics.

```
  MOLECULAR MOTORS              CS / ENGINEERING PARALLEL
  ──────────────────────────────────────────────────────────────────────
  Mechanochemical cycle         Finite state machine / Markov chain:
  (ATP bind → hydrolyze →       each biochemical state (ATP-bound,
  release → reset)              ADP·Pi-bound, apo) is a graph node.
                                Transition rates are edge weights.
                                The cycle drives a probability flux
                                around the loop — detailed balance
                                violation is the signal that the motor
                                is doing work, not just diffusing.

  Brownian ratchet              Feynman's ratchet revisited: at equilibrium,
  (asymmetric potential         a classical ratchet does zero net work
  + energy input)               (thermal fluctuations drive it both ways).
                                Directed motion requires a nonequilibrium
                                drive — ATP hydrolysis breaks detailed
                                balance, creating a rectified random walk.
                                Exactly analogous to a stochastic resonance
                                rectifier.

  Force-velocity curve          P-V operating curve of a heat engine:
  v(F) ≈ v_max·(1 - F/F_stall) maximum power at F_stall/2 (same as
                                matching load to source impedance for
                                maximum power transfer). At stall:
                                maximum force, zero velocity, zero power.

  Kinesin processivity          Coordinated two-thread execution:
  (hand-over-hand, 100 steps)   one head always bound (mutex held) before
                                the other releases. Mechanical coordination
                                prevents simultaneous detachment — analogous
                                to two-phase commit with one lock always held.

  ATP synthase γ rotation       Torque-generating motor with state machine:
  120° per ATP, 3-fold symmetry the three β subunits cycle L→T→O in phase,
                                like a 3-cylinder engine with offset timing.
                                Boyer's binding change mechanism: synthesis
                                requires no ATP energy directly — binding
                                energy at the T site IS the synthetic
                                mechanism.

  Flagellar motor chemotaxis    Feedback control loop with hysteresis:
  (CheA/CheY → CW/CCW switch)  attractant → phosphorylation cascade →
                                switch probability change → run/tumble ratio.
                                The bistable CW/CCW switch is a Schmitt
                                trigger with noise-driven transitions.
  ──────────────────────────────────────────────────────────────────────
```

**Scale note**: kinesin at stall does 56 pN·nm ≈ 14 k_BT of work per step, consuming ~50 pN·nm per ATP hydrolyzed. Efficiency depends on operating conditions; near stall (thermodynamic limit) efficiency approaches ~100%; at maximum velocity efficiency drops to ~25-50%. This parallels the fundamental efficiency vs. power tradeoff in any engine.

---

## Decision Cheat Sheet

| Question | Answer | Motor |
|----------|--------|-------|
| Which motor carries cargo toward cell periphery? | Kinesin (+end) | Kinesin-1/2/3 |
| Which motor brings cargo to nucleus/centrosome? | Dynein (-end) | Cytoplasmic dynein |
| How many nm does kinesin move per ATP? | 8 nm | Kinesin-1 |
| How does ATP synthase synthesize ATP? | Proton gradient drives γ rotation | F₀F₁ binding change mechanism |
| What drives bacterial flagellar motor? | Proton motive force (not ATP) | Flagellar motor |
| Why is kinesin processive but myosin II not? | Kinesin: hand-over-hand; head stays bound during detachment | Duty ratio differences |
| What is stall force of kinesin? | ~7 pN | Measured by optical tweezers |
| What did single-molecule rotation confirm about ATP synthase? | 120° steps, one per ATP | Noji et al. 1997 |

---

## Common Confusion Points

**Brownian ratchet ≠ violating thermodynamics.** The Brownian ratchet metaphor
sometimes implies free energy from thermal fluctuations. Feynman demonstrated
that a classical ratchet at equilibrium does no net work — thermal fluctuations
drive the pawl over the tooth equally in both directions. Molecular motors get
directed motion from ATP hydrolysis breaking detailed balance, not from "extracting"
thermal energy.

**Stall force ≠ working force.** Stall force is the maximum static load a motor
can hold (velocity = 0). Under normal cellular conditions, kinesin works against
much smaller loads (cargo viscous drag, ~0.001-1 pN). Near stall, a motor is
thermodynamically efficient but slow. Maximum power output occurs at intermediate
loads (~F_stall/2), not at stall.

**Processivity requires coordinated gating.** Kinesin is processive because the
two heads are mechanically and chemically coordinated: the lead head cannot release
ADP (and thus cannot hydrolyze ATP) until the rear head binds ATP and releases.
This prevents both heads from detaching simultaneously. Myosin II lacks this
coordination (no processive mechanism) — it is designed for ensemble use in
sarcomeres, where many motors work together.

**ATP synthase efficiency depends on H⁺/ATP ratio.** The "efficiency" depends on
thermodynamic conditions. Near thermodynamic equilibrium (v ≈ 0), efficiency →
100%. At full-speed synthesis, efficiency is lower because the motor must "slip"
somewhat. The H⁺/ATP stoichiometry (c/3) sets the maximum free energy harvested
per ATP. For c = 10 and ΔμH⁺ = 200 meV: maximum ΔG ≈ 3.3 × 200 meV ≈ 14.2 kcal/mol.

**Flagellar motor runs on H⁺, not ATP.** The flagellar basal body is directly
coupled to the proton motive force. ATP is not hydrolyzed for rotation (unlike
kinesin/myosin). The flagellar filament itself is assembled by a separate
export machinery that does use ATP (flagellar type III secretion).
