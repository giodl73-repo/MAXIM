# Watchmaking — 02 The Verge Escapement
## The First Mechanical Clock (~1280s): Crown Wheel, Verge, and Foliot

---

## The Big Picture

The escapement is the clock's fundamental innovation. Without it, a falling weight drives a gear train at whatever rate friction allows — not useful for counting time. The escapement converts continuous rotational energy into a controlled stepping motion, and it counts those steps against an oscillator.

The verge-and-foliot is the first mechanical escapement. It appeared in European tower clocks in the 1280s. It was good enough to ring bells at canonical hours. It was not good enough to keep accurate time. Why not: it had an escapement but no proper oscillator. The foliot (a horizontal bar) has no natural period — it simply oscillates at whatever rate the gear train drives it. Remove the driving force and it stops immediately.

```
ESCAPEMENT PROBLEM

Continuous input:                      Stepped output:
                                       (countable, controlled)
 weight falls ──► gear train ──────►   tick
 (continuous     (wants to spin         tock
  torque)         as fast as            tick
                  friction allows)      tock
                         │
                         ▼
                   ESCAPEMENT
                   - Releases gear train one tooth at a time
                   - Each release = one count
                   - Rate controlled by oscillator
                         │
                         ▼
                   OSCILLATOR
                   - Sets the tempo
                   - Verge-and-foliot: tempo depends on drive force (bad)
                   - Pendulum: tempo depends on length and gravity (good)
                   - Quartz: tempo depends on crystal physics (very good)
                   - Cesium: tempo depends on quantum physics (near-perfect)
```

---

## The Crown Wheel and Verge: Mechanism

The verge-and-foliot escapement has three main components:

```
VERGE-AND-FOLIOT ESCAPEMENT — SIDE VIEW

                    foliot bar (horizontal)
           ←────────────────────────────→
           weight                    weight
           (adjustable position)     (adjustable position)
               │                         │
               └──────────┬──────────────┘
                          │
                    verge (vertical shaft / spindle)
                          │
                    pallet A (upper)        ← fits between crown wheel teeth
                          │                   on the back side
                    pallet B (lower)        ← fits between crown wheel teeth
                          │                   on the front side
                          │
               ┌──────────┴──────────┐
               │   CROWN WHEEL       │
               │   (escape wheel)    │
               │   teeth project     │
               │   perpendicular     │
               │   to wheel plane    │
               │   (like a crown)    │
               └──────────┬──────────┘
                          │
                   going train
                          │
                   great wheel
                          │
                   mainspring or
                   falling weight
```

**Crown wheel geometry:** The crown wheel has teeth that project axially (perpendicular to the wheel face), like the battlements on a castle crown — hence the name. Typically 13 or 15 teeth (odd numbers to prevent pallets engaging on opposite sides simultaneously).

**Verge (spindle):** A vertical shaft with two flat paddles (pallets) set approximately 90–120° apart along its length. The critical angular offset: both pallets must engage the crown wheel teeth, but on opposite sides (one on the front face of the crown wheel, one on the back).

**How one beat works:**

```
BEAT SEQUENCE

Step 1: Crown wheel tooth pushes pallet A
        → verge rotates clockwise
        → foliot swings clockwise
        → pallet B enters crown wheel teeth on opposite side

Step 2: Crown wheel tooth catches pallet B
        → wheel locks (brief pause)
        → foliot inertia decelerates, reverses direction

Step 3: Foliot reverses, swings counter-clockwise
        → pallet B pushed by crown wheel tooth
        → verge rotates counter-clockwise
        → pallet A re-enters crown wheel teeth

Step 4: Crown wheel tooth catches pallet A
        → wheel locks again
        → foliot inertia decelerates, reverses

... repeat ...

Each complete cycle: crown wheel advances by 2 teeth.
Crown wheel tooth count = N → one full revolution = N/2 oscillations.
```

**The escapement "escapes":** Each beat, one tooth "escapes" past a pallet. This is where the term "escapement" comes from — the wheel's teeth escape one at a time.

---

## Why the Verge Was Inaccurate

The verge-and-foliot has no natural frequency. The foliot is a rigid bar with adjustable weights — it has **inertia** but no restoring force. Its oscillation period is not intrinsic; it depends on:

1. **Driving torque:** More force from the falling weight = faster oscillation. As the weight falls and the rope winds onto different drum diameters, torque varies.
2. **Friction:** Changes with temperature, lubricant condition, wear.
3. **Foliot mass distribution:** The weights can be moved inward/outward to adjust the rate, but this is a rate *setter*, not a natural frequency *keeper*.
4. **Impulse geometry:** The angle and shape of the pallet-tooth interaction affect how hard the crown wheel pushes the pallets — and thus how fast the foliot swings.

```
VERGE ACCURACY — ERROR TREE

±15 min/day typical error

├── No natural frequency (≈ 50% of total error)
│   - Rate set by operator adjusting foliot weights
│   - No automatic correction of perturbations
│
├── Drive torque variation (≈ 30%)
│   - Weight-driven: torque varies as rope geometry changes
│   - Mainspring-driven (pocket watches): torque drops as spring unwinds
│   - No constant-force mechanism (fusee not yet invented for early clocks)
│
├── Friction variability (≈ 15%)
│   - Temperature changes viscosity of any lubricant
│   - Wear changes pivot geometry over time
│   - No jewel bearings (plain iron-on-iron)
│
└── Impulse inconsistency (≈ 5%)
    - Crown wheel tooth geometry not optimized
    - Contact angles vary through the beat cycle
```

**Comparison to a pendulum (previewing 03):** A pendulum has a restoring force (gravity acting on the displaced mass), which creates a natural frequency: T = 2π√(L/g). This period is independent of driving force and amplitude (for small amplitudes). The verge-and-foliot has no restoring force — the foliot just has inertia. Remove the drive force and it stops immediately; push it harder and it oscillates faster. This is the fundamental reason it's inaccurate.

---

## The Foliot: Design Details

```
FOLIOT VARIANTS

Standard foliot (horizontal bar):
          ●─────────────────────●
           weight              weight
               |
           verge

Balance wheel (later development):
          ╭────────────────────╮
         /                      \
        /   ╭────────────────╮   \
       │    │     hub        │    │
        \   ╰────────────────╯   /
         \                      /
          ╰────────────────────╯
           |
          verge

The balance wheel is a foliot bent into a circle — same physics,
more compact, enables pocket watches, still no natural frequency.
```

**Foliot vs balance wheel:**
- Foliot: used in large tower clocks; horizontal bar, adjustable weights
- Balance wheel: used in smaller table clocks and pocket watches; more compact; same accuracy limitation as foliot until the balance spring was added (17th century)

**Rate adjustment by foliot weight position:**
- Moving weights outward: increases moment of inertia → longer period → clock runs slow
- Moving weights inward: decreases moment of inertia → shorter period → clock runs fast
- This is the first "regulation" mechanism — the horological ancestor of the modern regulator index

---

## The Mainspring: Enabling Portability

Tower clocks were driven by hanging weights — a mass on a rope, with the rope wound around a drum (the "great wheel" arbor). As the weight descended, the rope unwound, driving the gear train. To rewind, a verger pulled a rope to raise the weight again (daily winding).

Hanging weights require:
- Vertical orientation (can't tilt the clock)
- Sufficient height for the weight to descend (tower clocks have high ceilings; table clocks, obviously, don't)
- Regular winding (typically once or twice daily)

**The coiled mainspring (~1430–1510):** A strip of hardened steel coiled in a barrel. When wound, elastic energy is stored; as it uncoils, it drives the gear train. This eliminated the need for a hanging weight.

```
MAINSPRING FORCE CURVE

Torque
  ↑
  │▓▓▓▓
  │    ▓▓▓
  │       ▓▓▓▓
  │           ▓▓▓▓▓▓
  │                 ▓▓▓▓▓▓▓▓▓▓
  └──────────────────────────────→ Winding state
     fully wound              nearly run down

A fully wound mainspring exerts 2–3× more torque than a nearly run-down one.
This torque variation directly causes rate variation in a verge watch.
```

**The fusee (~1430s, Jacob the Czech is credited; widespread by 1500s):** A conical pulley attached to the great wheel. As the mainspring unwinds, a chain or gut line transfers torque through the fusee. The cone's geometry compensates for the mainspring's decreasing torque:

```
FUSEE MECHANISM

Mainspring barrel          Fusee (conical pulley)
┌──────────────┐          ╱╲
│   mainspring │ ─chain─ /  \  ← large radius (spring fully wound)
│   (provides  │        /    \
│   decreasing │       /      \ ← medium radius (mid-winding)
│   torque as  │      /        \
│   it unwinds)│     /          \ ← small radius (spring nearly run down)
└──────────────┘    ╲____________╱
                           │
                      great wheel
                      (constant torque)
```

Chain wraps from bottom of fusee (small radius) when spring is fully wound → maximum mechanical advantage compensates for maximum spring torque. As spring unwinds, chain moves to larger radius → less mechanical advantage, but spring is also weaker → approximately constant torque delivered to going train.

The fusee is elegant constant-force engineering. It's also why early mechanical pocket watches have a very different internal layout from modern ones — the fusee takes up significant space.

Peter Henlein of Nuremberg (c. 1485–1542) is often credited with the first pocket watch ("Nuremberg egg"), approximately 1510. The attribution is disputed — other contemporaries also built early portable clocks — but Nuremberg was definitively the center of early portable clock production.

---

## Notable Early Clocks

### Salisbury Cathedral (1386)
- Oldest surviving mechanical clock still running in its original location
- Wrought iron frame construction (no brass)
- Verge-and-foliot (original escapement; replaced with anchor escapement ~1790, then restored to verge ~1956 after historical research)
- Two trains: going train + striking train
- No original dial — the clock's output was sound

### Wells Cathedral (1386–1392)
- Contemporary with Salisbury
- Has an astronomical dial (later addition, ~1390)
- Famous for the jousting knights that circle on the quarter-hour — among the world's earliest surviving clock automata
- A copy of the movement mechanism is in the Science Museum, London

### Prague Astronomical Clock (Orloj, 1410)
- Still functioning (with many repairs and restorations)
- One dial shows four time systems simultaneously: Central European Time, Old Bohemian Time (hours counted from sunset), Babylonian Hours (unequal hours), and Sidereal Time
- Shows lunar phase, position of sun and moon in the zodiac
- Moving figures (Death pulling a cord, the 12 Apostles appearing in windows) added 1490, restored repeatedly
- The astronomical display predates the mechanical accuracy to make it fully precise — it was an aspirational display as much as a functional one

---

## The Transition: Verge → Pendulum

The verge-and-foliot remained the dominant escapement for approximately 370 years (c.1280–c.1660). This is a remarkably long run for an inaccurate technology. Why?

1. **No better alternative existed** — until Galileo's isochronism insight and Huygens' implementation, there was no stable oscillator to replace the foliot
2. **The task didn't demand accuracy** — ringing bells at approximately the right canonical hour was good enough; a ±15 min/day clock was more accurate than anything else available
3. **The technology improved incrementally** — better materials, better geometry, the fusee for torque compensation, better pivot work

The transition happened rapidly once the pendulum arrived. Huygens published in 1658; by 1670, pendulum clocks had largely replaced verge movements in precision applications. The verge survived in portable watches (where a pendulum is impractical) until the lever escapement replaced it there too — but that took until approximately 1800.

---

## Decision Cheat Sheet: Verge Era Technology

```
PROBLEM                        | SOLUTION                      | LIMITATION
───────────────────────────────┼───────────────────────────────┼─────────────────────
Need to ring bells hourly,     | Verge tower clock, weight     | ±15 min/day accuracy
    stationary location        | driven, verge-and-foliot      | needs daily correction

Need portable clock            | Verge pocket watch,           | Even less accurate
    (travel, personal use)     | mainspring driven             | than tower clock;
                               |                               | no temperature comp

Need constant driving torque   | Add fusee mechanism           | Adds complexity, size
    for portable clock         |                               | requires more winding

Need portable, more accurate   | Must wait for 1759 and        | Lever escapement
    (±1 sec/day class)         | the lever escapement          | doesn't exist yet

Need extreme precision,        | Precision pendulum clock;     | Not portable; affected
    stationary use             | anchor or deadbeat escapement | by vibration
```

---

## Common Confusion Points

**"The escapement controls the rate of the clock."**
The escapement controls the *stepping* — it couples energy from the power source to the oscillator one beat at a time. The oscillator controls the rate. In a verge clock, the foliot is the (poor) oscillator. In a pendulum clock, the pendulum is the oscillator. The escapement's job is to: (1) lock the gear train between beats, and (2) give the oscillator a small push each beat to keep it going. The oscillator's natural frequency sets the rate.

**"More teeth on the crown wheel = more accurate."**
Not directly. More teeth means finer steps, but the fundamental accuracy limit is the lack of a natural frequency in the foliot. More teeth just divides the same inaccurate period into smaller steps.

**"Pocket watches came after tower clocks by many centuries."**
Only about 250 years — tower clocks ~1280, portable watches ~1510. The key enabling technology was the coiled mainspring replacing the hanging weight. The verge escapement itself was used in both; it was the power source that prevented portability, not the escapement.

**"The fusee was invented to keep the clock running longer."**
No — the fusee was invented to deliver constant torque to the gear train regardless of mainspring wind state. It doesn't change how long the clock runs; it changes the uniformity of the driving force throughout the running cycle. Uniform torque → more uniform rate → better accuracy. This is the same goal as modern "constant force" remontoire mechanisms in high-end movements.
