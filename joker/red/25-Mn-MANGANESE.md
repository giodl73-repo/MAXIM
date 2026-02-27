# [25] --- Manganese

**7&#9827; The Constructor** &middot; Mechanics &middot; T2

---

> The Constructor builds chains where nothing is wasted. One motion becomes the next becomes the next. Eight stages. Eight principles. You trace the chain. You name each law. The first letters are the answer.

---

## The Puzzle

**Type:** Rube Goldberg Chain -- trace chain reaction, each stage's principle &rarr; first letter
**References:** mechanical/, structural/, energy-systems/, acoustics/

An elaborate machine sits on a workbench. A single push starts a chain of eight events. Each stage exploits a different mechanical or physical principle -- the kind documented in the Mechanics section of the encyclopedia. Your job: trace the chain from first motion to last, identify the governing principle at each stage, and take the first letter of each principle name. Eight stages. Eight principles. Eight letters. One word.

The diagram below shows the entire machine. Study it carefully. The numbered stages are described in detail after the diagram.

---

### The Machine

```
                                                      STEAM
                                                    RESERVOIR
                                                    ┌───────┐
                                                    │░░░░░░░│
                                                    │░░░░░░░│
                                                    │░STEAM░│
                                          CAM ──►   │░░░░░░░├──┐
                                          ┌───┐     └───────┘  │  VALVE
    ①                ②            ③       │ ◐ ├──────          │
    ▼                ▼            ▼       └─┬─┘     ────►──────┘     ⑧
                                            │                        ▼
 ╔═══╗    ┌───────┐   OIL TROUGH            │ PINION              ┌──────┐
 ║   ║    │~spring│   ┌────────────┐      ┌─┴──┐                 │▓▓▓▓▓▓│
 ║ W ║    │~~~~~~~│   │≈≈≈≈≈≈≈≈≈≈≈≈│     │////│                 │PISTON│
 ║   ║    │~~~~~~~│   │≈≈≈≈≈≈≈≈≈≈≈≈│     │////│    RACK ↑       │▓▓▓▓▓▓│
 ╚═══╝    └───┬───┘   └──────┬─────┘     └────┘    ┌────┴───┐   └──┬───┘
   │          │              │                      │ ┌────┐ │      │
   │          │              │   ④                   │ │FLOAT│ │      │
   ▼          │              ▼                      │ │    │ │      ▼
 ══╪══════════╧══     ═══════╪════════     ⑥       │ └────┘ │   ╔══════╗
   ●                         │           ┌────────┐ │  ↑↑↑   │   ║STAMP ║
 FULCRUM            ──cork──►│           │ WATER  │ │  WATER │   ║  ●   ║
   │                    ▼    │           │~~~~~~~~│ └────────┘   ╚══════╝
   │                  ┌──┴───┤           │~~~~~~~~│      ⑦
   │           ⑤     │ BEAM │           │~~~~~~~~│
   │           ▼      │  ◄──►│           └───┬────┘
   │       ┌────────┐ │PIVOT │               │
   │       │ STRING │ └──┬───┘           PLUG/PIN ← ⑤ shakes loose
   │       │   ↓    │    │
   │       │ ~~~~── │    │
   │       │ WIRE   │    │
   │       └────────┘    │
   │                     │
   └─────────────────────┘
         BALL FLIGHT PATH
```

---

### Stage Descriptions

Read each description. The encyclopedia's Mechanics section contains the principle that governs each stage. Some stages name the phenomenon in plain sight. Others describe the physics -- you must recognize the principle from its behavior.

---

**Stage 1 -- The First Push**

A 2 kg weight drops from a shelf onto the long arm of a rigid bar that pivots on a fixed fulcrum. The short arm is four times shorter than the long arm. The falling weight pushes the long arm down; the short arm swings up and launches a steel ball into the air.

*The principle:* a rigid bar on a pivot amplifies force at the cost of distance. Effort arm, load arm, fulcrum. The oldest machine.

**What mechanical principle governs Stage 1?**

First letter: [___]

---

**Stage 2 -- Catch and Release**

The steel ball lands in a cup mounted atop a coiled helical spring (wire diameter 4 mm, mean coil diameter 32 mm, 10 active coils, spring steel G = 79 GPa). The impact compresses the spring, storing energy as potential energy in the deformed wire. The spring rate k = Gd&#8308;/(8D&#179;N) determines how far it compresses. When the ball bounces back, the spring releases its stored energy, launching a wooden puck horizontally along a track.

*The principle:* F = kx. Energy stored in a deformed solid, returned when the deforming load is removed. Stress proportional to strain below the yield point.

**What physical property governs the spring's behavior?**

First letter: [___]

---

**Stage 3 -- The Slow Lane**

The wooden puck slides off the track and into a shallow trough filled with heavy oil (SAE 90, dynamic viscosity &mu; &asymp; 0.3 Pa&middot;s at 40&deg;C). The puck decelerates as the fluid resists its motion -- the shear stress in the oil is proportional to the velocity gradient (Newton's law: &tau; = &mu; du/dy). The thick oil slows the puck to a crawl. At the end of the trough, the barely-moving puck nudges a small cork off a ledge and onto a balance beam below.

*The principle:* a fluid property measured in Pa&middot;s that determines resistance to shear deformation. The thicker the fluid, the greater the drag. Newton's law of fluid resistance.

**What fluid property governs the puck's deceleration?**

First letter: [___]

---

**Stage 4 -- The Tipping Point**

A beam rests on a knife-edge pivot, perfectly balanced: &Sigma;F = 0 and &Sigma;M = 0. Equal weights hang from equal arms. The cork from Stage 3 lands on one side. The symmetry breaks -- the sum of moments about the pivot is no longer zero. The heavy side sinks. A string tied to the descending arm pulls taut.

*The principle:* the condition where all forces and all moments sum to zero. The beam was in this state; the cork destroyed it. The entire field of statics begins with this condition and the free-body diagram.

**What condition did the cork destroy?**

First letter: [___]

---

**Stage 5 -- The Singing Wire**

The string from Stage 4 plucks a taut steel wire stretched between two posts. The wire vibrates -- but not at just any frequency. It vibrates at its natural frequency &omega;&#8345; = &radic;(k/m), the eigenvalue of the mass-stiffness system. At this frequency, even small periodic inputs produce large-amplitude oscillations. The wire's vibrations grow until a pin balanced on the wire shakes loose and falls.

*The principle:* the condition where a system's driving frequency matches its natural frequency, producing maximum amplitude response. The SDOF eigenvalue. The Campbell diagram's crossing point. The reason soldiers break step on bridges.

**What phenomenon causes the wire's amplitude to grow?**

First letter: [___]

---

**Stage 6 -- The Rising Float**

The falling pin was a plug in the bottom of a water reservoir. Water floods into a sealed chamber below. Inside the chamber, a hollow sealed cylinder sits on the floor. As water rises around it, the cylinder experiences an upward force equal to the weight of the water it displaces (F&#7522; = &rho;&#7525;gV&#8347;). The cylinder is less dense than water. It rises, pushing a toothed rack upward with it.

*The principle:* the upward force on a submerged body equals the weight of displaced fluid. The eureka principle. The reason ships float and hot-air balloons rise. Stated in Syracuse in the third century BC.

**Whose principle governs the float's rise?**

First letter: [___]

---

**Stage 7 -- The Torque Transform**

The rising rack meshes with a small pinion gear (12 teeth). The pinion is fixed to a shaft that also carries a larger gear (48 teeth) on the other end. That larger gear meshes with a 12-tooth gear connected to a cam. The tooth ratio i = N&#8322;/N&#8321; sets the torque and speed transformation at each mesh -- torque multiplied, speed divided, power conserved (minus friction). The rack's linear motion becomes rotational; the gear train amplifies torque to turn the cam.

*The principle:* toothed wheels that transmit and transform rotational motion. Speed/torque converters with defined ratio. The module m = d/N sets the tooth geometry. The most common power transmission element in mechanical engineering.

**What machine elements transform the motion in Stage 7?**

First letter: [___]

---

**Stage 8 -- The Final Conversion**

The rotating cam pushes open a valve on a pressurized steam reservoir (T&#8345; = 400 K). Steam rushes through and expands against a piston. But not all the steam's thermal energy becomes mechanical work -- the second law sets a ceiling: &eta;&#8344; = 1 &minus; T&#8320;/T&#8345;. Some energy is always rejected as waste heat to the surroundings. The piston drives a stamp that prints the final mark. Energy entered the machine as gravitational potential in Stage 1; here, it exits as work done on the stamp -- less than what entered, because every conversion step destroyed some of the original energy's capacity to do work.

*The principle:* the measure of energy's capacity to do useful work, destroyed at every irreversible conversion step. Not energy (which is conserved) but the useful portion of energy (which is not). The second law's accounting system. The Alchemist's question: where does availability die?

**What thermodynamic quantity was destroyed at every stage?**

First letter: [___]

---

## Worksheet

### Chain Verification

Before extracting, verify the chain is connected. Each stage's output should be the next stage's input.

```
Stage    Output                          Feeds into
─────    ──────                          ──────────
  1      ball launched upward        →   2 (ball lands on spring)
  2      puck launched horizontally  →   3 (puck enters oil trough)
  3      cork nudged off ledge       →   4 (cork lands on beam)
  4      string pulled taut          →   5 (string plucks wire)
  5      pin shaken loose            →   6 (pin/plug falls, water flows)
  6      rack pushed upward          →   7 (rack meshes with pinion)
  7      cam rotates                 →   8 (cam opens steam valve)
  8      stamp prints                     END
```

Does each output cause the next input? If any link is broken, re-read that stage.

---

### Principle Identification

For each stage, name the governing principle. The Mechanics section files contain every principle used in this machine. If you are unsure, the stage descriptions contain clues that point to specific equations, laws, or concepts in the encyclopedia.

```
Stage    Principle name                First letter
─────    ──────────────                ────────────
  1      _________________________     [___]
  2      _________________________     [___]
  3      _________________________     [___]
  4      _________________________     [___]
  5      _________________________     [___]
  6      _________________________     [___]
  7      _________________________     [___]
  8      _________________________     [___]
```

### Extraction

Read the first letters top to bottom.

```
Stage 1 → Stage 2 → Stage 3 → Stage 4 → Stage 5 → Stage 6 → Stage 7 → Stage 8

 [___]     [___]     [___]     [___]     [___]     [___]     [___]     [___]
```

---

**Your answer** (8 letters): _ _ _ _ _ _ _ _

*You may find the Mechanics section helpful -- particularly the machine design, fluid mechanics, thermodynamics, and statics guides.*
