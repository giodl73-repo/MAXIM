# [26] --- Iron

**7&#9824; The Instrumentalist** &middot; Mechanics &middot; &#9733; T1

---

> The Instrumentalist measures before making. Lever, pulley, gear, incline, wheel, press. Six machines. Six numbers. The numbers are not decoration. They are the answer.

---

## The Puzzle

**Type:** Engineering Calculation -- forces in 6 simple machines, numbers &rarr; A1Z26 &rarr; letters
**References:** mechanical/, structural/

Six machines sit on a workbench. Each has labeled dimensions and a single applied force. Calculate the output of each machine -- a force, a torque, or a mechanical advantage. The numerical result is your key: convert each number to a letter using A1Z26 (1=A, 2=B, ... 26=Z). Six machines. Six numbers. Six letters.

---

### Machine 1 -- The Lever

A rigid bar pivots on a fulcrum. A load hangs from one side. You push on the other.

```
                        effort arm                load arm
                    |<--- 4 m --->|<--- 1 m --->|

                    E              ▲              L
                    │              │              │
                    ▼              │              ▼
            push ═══╪══════════════╪══════════════╪═══
                  effort         fulcrum         load
                   (?)                          (5 N)
```

**Given:**
- Effort arm = 4 m
- Load arm = 1 m
- Load = 5 N

For a balanced lever, effort x effort arm = load x load arm. But that gives you the effort -- the force you apply. The question is different.

**Calculate:** What is the output force the lever exerts on the load side? That is: what maximum load (in newtons) can this lever lift with 5 N of effort?

```
    Mechanical advantage = effort arm / load arm = _____ / _____ = _____

    Output force = MA × effort = _____ × 5 N = _____ N
```

**Machine 1 answer:** ________

---

### Machine 2 -- The Compound Pulley

Three pulleys are rigged so that three rope segments support the load. You pull on the free end.

```
                ┌────────────┐  ceiling
                │            │
               ┌┴┐          ┌┴┐
               │A│          │B│          fixed pulleys
               └┬┘          └┬┘
                │            │
                │   ┌────┐   │
                │   │    │   │
                └───┤ C  ├───┘
                    │    │
                    └──┬─┘           movable pulley
                       │
                      ╔╧╗
                      ║ ║  load
                      ╚═╝

    rope segments supporting the load: 3
    (one from A down to C, one from B down to C, one free end you pull)

    You pull with 5 N of effort on the free end.
```

**Given:**
- Number of supporting rope segments = 3
- Effort applied = 5 N

In an ideal compound pulley, the load is shared equally among all supporting rope segments.

**Calculate:** What load (in newtons) can this system lift?

```
    Output force = number of supporting ropes × effort
                 = _____ × 5 N = _____ N
```

**Machine 2 answer:** ________

---

### Machine 3 -- The Gear Train

A small driving gear meshes with a larger driven gear. You apply torque to the input shaft.

```
        input shaft                output shaft
            │                          │
            ▼                          ▼
         ┌─────┐                ┌───────────┐
         │     │                │           │
         │  A  │────────────────│     B     │
         │     │  teeth mesh    │           │
         │ 12T │                │    36T    │
         └─────┘                └───────────┘
         driving                   driven
         gear                      gear

    Input torque: 6 N·m applied to gear A
```

**Given:**
- Driving gear (A) = 12 teeth
- Driven gear (B) = 36 teeth
- Input torque = 6 N&middot;m

In meshed gears, the torque ratio equals the tooth ratio: T_out / T_in = N_driven / N_driving. (The driven gear turns slower but with more torque -- power is conserved.)

**Calculate:** What is the output torque at gear B (in N&middot;m)?

```
    Gear ratio = N_driven / N_driving = _____ / _____ = _____

    Output torque = input torque × gear ratio
                  = 6 N·m × _____ = _____ N·m
```

**Machine 3 answer:** ________

---

### Machine 4 -- The Inclined Plane

A crate is pushed up a long, shallow ramp instead of being lifted straight up.

```
                                                      ╱│
                                                    ╱  │
                                                  ╱    │
                                                ╱      │
                                              ╱        │
                                            ╱          │
                                          ╱            │  height
                                        ╱              │  1 m
                                      ╱                │
                                    ╱                  │
                                  ╱                    │
                                ╱                      │
                              ╱                        │
                            ╱                          │
                          ╱                            │
                        ╱──────────────────────────────│
                       ◄───────── 17 m ──────────────►
                              ramp length
```

**Given:**
- Ramp length (along the slope) = 17 m
- Ramp height (vertical rise) = 1 m
- Assume frictionless

The inclined plane trades distance for force. The mechanical advantage equals the ratio of the distance you push to the distance the load rises.

**Calculate:** What is the mechanical advantage of this ramp?

```
    MA = ramp length / height = _____ / _____ = _____
```

**Machine 4 answer:** ________

---

### Machine 5 -- The Wheel and Axle

A large wheel is fixed to a small axle. You turn the wheel; the axle lifts the load.

```
              ┌──────────────────────────┐
              │                          │
              │                          │
              │         ┌────┐           │
              │         │axle│           │
         ──── │ ────────┤ ●  ├────────── │ ────
              │    R=21 │    │ r=1       │
              │         └────┘           │
              │          axle            │
              │                          │
              │                          │
              └──────────────────────────┘
                    wheel (R = 21 cm)       axle (r = 1 cm)

    You apply force at the wheel rim. The axle winds a rope that lifts the load.
```

**Given:**
- Wheel radius (R) = 21 cm
- Axle radius (r) = 1 cm

The wheel and axle is a continuous lever: the wheel radius is the effort arm, the axle radius is the load arm.

**Calculate:** What is the mechanical advantage?

```
    MA = R / r = _____ / _____ = _____
```

**Machine 5 answer:** ________

---

### Machine 6 -- The Hydraulic Press

A small piston pushes fluid into a large piston. Pascal's principle does the rest.

```
    force applied
        1 N
         │
         ▼
    ┌─────────┐                     ┌─────────────────────────┐
    │         │                     │                         │
    │  small  │                     │         large           │
    │ piston  │                     │        piston           │
    │  2 cm²  │                     │        10 cm²           │
    │         │                     │                         │
    └────┬────┘                     └────────────┬────────────┘
         │          fluid line                   │
         └───────────────────────────────────────┘
                  (incompressible fluid)
```

**Given:**
- Small piston area (A&#8321;) = 2 cm&sup2;
- Large piston area (A&#8322;) = 10 cm&sup2;
- Force applied to small piston = 1 N

Pascal's principle: pressure is transmitted equally. The force multiplier equals the area ratio.

**Calculate:** What force (in newtons) does the large piston exert?

```
    Force ratio = A₂ / A₁ = _____ / _____ = _____

    Output force = input force × (A₂ / A₁)
                 = 1 N × _____ = _____ N
```

**Machine 6 answer:** ________

---

## Worksheet

### Extraction Table

Copy each machine's numerical answer, then convert to a letter using A1Z26 (1=A, 2=B, ... 26=Z).

```
Machine       Calculation result       A1Z26 letter
──────────    ──────────────────       ────────────
1  Lever      ________                 [___]
2  Pulley     ________                 [___]
3  Gears      ________                 [___]
4  Ramp       ________                 [___]
5  Wheel      ________                 [___]
6  Press      ________                 [___]
```

### A1Z26 Reference

```
 A= 1   B= 2   C= 3   D= 4   E= 5   F= 6   G= 7   H= 8   I= 9
 J=10   K=11   L=12   M=13   N=14   O=15   P=16   Q=17   R=18   S=19
 T=20   U=21   V=22   W=23   X=24   Y=25   Z=26
```

### Read the answer

```
Machine 1 → Machine 2 → Machine 3 → Machine 4 → Machine 5 → Machine 6

  [___]      [___]      [___]      [___]      [___]      [___]
```

---

**Your answer** (6 letters): _ _ _ _ _ _

*You may find the Mechanics section helpful.*
