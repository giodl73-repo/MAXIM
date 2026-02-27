# Puzzle Test: 26-Fe-IRON

**Puzzle:** [26] Iron -- Engineering Calculation (Mechanics)
**Card:** 7 of Spades -- The Instrumentalist
**Testers:** Kenny Young, Thomas Snyder, Peter Sarrett
**Date:** 2026-02-27

---

## Sanitized Puzzle (as presented to testers)

> The Instrumentalist measures before making. Lever, pulley, gear, incline, wheel, press. Six machines. Six numbers. The numbers are not decoration. They are the answer.

**Type:** Engineering Calculation -- forces in 6 simple machines, numbers &rarr; A1Z26 &rarr; letters

Six machines sit on a workbench. Each has labeled dimensions and a single applied force. Calculate the output of each machine -- a force, a torque, or a mechanical advantage. The numerical result is your key: convert each number to a letter using A1Z26 (1=A, 2=B, ... 26=Z). Six machines. Six numbers. Six letters.

---

### Machine 1 -- The Lever

A rigid bar pivots on a fulcrum. A load hangs from one side. You push on the other.

```
                        effort arm                load arm
                    |<--- 4 m --->|<--- 1 m --->|

                    E              ^              L
                    |              |              |
                    v              |              v
            push ===[==============]===============[===
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

    Output force = MA x effort = _____ x 5 N = _____ N
```

**Machine 1 answer:** ________

---

### Machine 2 -- The Compound Pulley

Three pulleys are rigged so that three rope segments support the load. You pull on the free end.

```
                [============]  ceiling
                |            |
               [A]          [B]          fixed pulleys
                |            |
                |   [----]   |
                |   |    |   |
                +---| C  |---+
                    |    |
                    +--+-+           movable pulley
                       |
                      [=]
                      | |  load
                      [=]

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
    Output force = number of supporting ropes x effort
                 = _____ x 5 N = _____ N
```

**Machine 2 answer:** ________

---

### Machine 3 -- The Gear Train

A small driving gear meshes with a larger driven gear. You apply torque to the input shaft.

```
        input shaft                output shaft
            |                          |
            v                          v
         [-----]                [===========]
         |     |                |           |
         |  A  |================|     B     |
         |     |  teeth mesh    |           |
         | 12T |                |    36T    |
         [-----]                [===========]
         driving                   driven
         gear                      gear

    Input torque: 6 N-m applied to gear A
```

**Given:**
- Driving gear (A) = 12 teeth
- Driven gear (B) = 36 teeth
- Input torque = 6 N-m

In meshed gears, the torque ratio equals the tooth ratio: T_out / T_in = N_driven / N_driving. (The driven gear turns slower but with more torque -- power is conserved.)

**Calculate:** What is the output torque at gear B (in N-m)?

```
    Gear ratio = N_driven / N_driving = _____ / _____ = _____

    Output torque = input torque x gear ratio
                  = 6 N-m x _____ = _____ N-m
```

**Machine 3 answer:** ________

---

### Machine 4 -- The Inclined Plane

A crate is pushed up a long, shallow ramp instead of being lifted straight up.

```
                                                      /|
                                                    /  |
                                                  /    |
                                                /      |
                                              /        |
                                            /          |
                                          /            |  height
                                        /              |  1 m
                                      /                |
                                    /                  |
                                  /                    |
                                /                      |
                              /                        |
                            /                          |
                          /                            |
                        /==============================|
                       <--------- 17 m -------------->
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
              [==========================]
              |                          |
              |                          |
              |         [----]           |
              |         |axle|           |
         ---- | --------| .  |---------- | ----
              |    R=21  |    | r=1      |
              |         [----]           |
              |          axle            |
              |                          |
              |                          |
              [==========================]
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
         |
         v
    [---------]                     [=========================]
    |         |                     |                         |
    |  small  |                     |         large           |
    | piston  |                     |        piston           |
    |  2 cm2  |                     |        10 cm2           |
    |         |                     |                         |
    [----+----]                     [------------+------------]
         |          fluid line                   |
         +=======================================+
                  (incompressible fluid)
```

**Given:**
- Small piston area (A1) = 2 cm2
- Large piston area (A2) = 10 cm2
- Force applied to small piston = 1 N

Pascal's principle: pressure is transmitted equally. The force multiplier equals the area ratio.

**Calculate:** What force (in newtons) does the large piston exert?

```
    Force ratio = A2 / A1 = _____ / _____ = _____

    Output force = input force x (A2 / A1)
                 = 1 N x _____ = _____ N
```

**Machine 6 answer:** ________

---

## Worksheet

### Extraction Table

Copy each machine's numerical answer, then convert to a letter using A1Z26 (1=A, 2=B, ... 26=Z).

```
Machine       Calculation result       A1Z26 letter
----------    ------------------       ------------
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
Machine 1 -> Machine 2 -> Machine 3 -> Machine 4 -> Machine 5 -> Machine 6

  [___]      [___]      [___]      [___]      [___]      [___]
```

**Your answer:** _______________

*You may find the Mechanics section helpful.*

---

## Intended Solution

| Machine | Given | Calculation | Result | Letter |
|---|---|---|---|---|
| 1 Lever | effort arm = 4 m, load arm = 1 m, effort = 5 N | MA = 4/1 = 4; output = 4 x 5 | 20 N | **T** |
| 2 Pulley | 3 supporting ropes, effort = 5 N | output = 3 x 5 | 15 N | **O** |
| 3 Gears | 12T driving, 36T driven, input = 6 N-m | ratio = 36/12 = 3; output = 6 x 3 | 18 N-m | **R** |
| 4 Ramp | length = 17 m, height = 1 m | MA = 17/1 | 17 | **Q** |
| 5 Wheel | R = 21 cm, r = 1 cm | MA = 21/1 | 21 | **U** |
| 6 Press | A1 = 2 cm2, A2 = 10 cm2, force = 1 N | ratio = 10/2 = 5; output = 1 x 5 | 5 N | **E** |

**Extraction:** T-O-R-Q-U-E = **TORQUE**

---

# Test: Iron -- Kenny Young

## Solve Attempt

Kenny reads the Instrumentalist's flavor text. "Six machines. Six numbers. The numbers are not decoration. They are the answer." He counts: lever, pulley, gear, incline, wheel, press. Six classic simple machines. Six numbers that map to letters via A1Z26.

He identifies the seed: "Simple machine calculations as letter-encoding. The Instrumentalist -- the card is about measurement and precision. The conceit is that you are an engineer at a workbench, computing outputs of physical devices. The numbers are the point."

**Seed assessment before solving:**

Kenny pauses. "I know this seed. I have seen it before -- many times. The puzzle gives you six labeled diagrams with all inputs specified, asks you to apply one formula per diagram, and converts the results to letters. This is the Magnesium pattern: given inputs, given rules, compute outputs. The only question is whether the six calculations are clean and whether there is anything to figure out beyond the formulas."

He reads through all six machines before computing anything.

**Machine 1 -- The Lever:**

```
MA = effort arm / load arm = 4 / 1 = 4
Output force = MA x effort = 4 x 5 = 20 N
```

"20. That is T. The formula is printed in the worksheet. The calculation is one division and one multiplication. There is no ambiguity about which formula to use -- the puzzle tells you MA = effort arm / load arm and output force = MA x effort. I am filling in blanks."

**Machine 2 -- The Compound Pulley:**

```
Output force = 3 x 5 = 15 N
```

"15. That is O. One multiplication. The formula is printed. The number of supporting ropes is stated. This is not a puzzle -- it is a labeled multiplication."

**Machine 3 -- The Gear Train:**

```
Gear ratio = 36 / 12 = 3
Output torque = 6 x 3 = 18 N-m
```

"18. That is R. The formula is printed: T_out / T_in = N_driven / N_driving. One division and one multiplication. Same pattern."

**Machine 4 -- The Inclined Plane:**

```
MA = 17 / 1 = 17
```

"17. That is Q. One division. The divisor is 1, so it is barely even division."

**Machine 5 -- The Wheel and Axle:**

```
MA = 21 / 1 = 21
```

"21. That is U. Same as Machine 4 -- ratio with a denominator of 1. The numbers 17 and 21 are prime and just happen to be within A1Z26 range because the dimensions were chosen to produce those values."

**Machine 6 -- The Hydraulic Press:**

```
Force ratio = 10 / 2 = 5
Output force = 1 x 5 = 5 N
```

"5. That is E. One division and one trivial multiplication (by 1)."

**Extraction:** T-O-R-Q-U-E.

"TORQUE. That is a good answer word -- perfectly thematic for a puzzle about simple machines. Six machines produce six forces or mechanical advantages; the word that names the rotational force measure is TORQUE. The self-reference is clean."

**Buildability assessment:**

Kenny shifts to constructor mode. "Could I build this as a PuzzleJS interactive? Yes -- easily. Each machine gets an animated diagram. You drag a slider to apply the effort force, and the output number appears. The visual feedback would be nice. But the interactive version would make the puzzle FASTER, not MORE INTERESTING. The problem is not presentation -- it is that there is nothing to figure out."

"In a brainstorming session, if someone pitched 'six simple machines, compute the output, the numbers spell a word,' the group would ask: 'What is the twist?' The answer here is: there is no twist. The dimensions are chosen to produce integers in the 1-26 range, and the formulas are printed on the page. The solver's job is to not make arithmetic errors."

"This is the same issue we flagged on Magnesium. Given inputs + given formula + compute = no puzzle. The Magnesium puzzle had ten circuits with four gate types. This puzzle has six machines with six formulas. Both are computation exercises with no deductive layer."

## Answer

**TORQUE**

## Scores

| Dimension | Score (1-5) | Notes |
|---|---|---|
| Clarity | 5 | Each machine is clearly diagrammed with labeled dimensions. The formulas are explicit. The A1Z26 reference is provided. The worksheet is well-structured. A solver with zero physics background can follow every step -- the puzzle is entirely self-contained. The diagrams are actually quite good as ASCII engineering drawings. |
| Solvability | 5 | Completely deterministic. Every input is given. Every formula is stated. Every calculation produces a clean integer in the 1-26 range. No ambiguity, no unit conversion traps, no rounding. Each machine is independently solvable. |
| Elegance | 2 | Six independent computations with no interlock. No machine's answer constrains or informs any other. The numbers were reverse-engineered from the target word TORQUE -- the dimensions (4/1, 3x5, 36/12, 17/1, 21/1, 10/2) exist solely to produce the integers 20, 15, 18, 17, 21, 5. There is no deeper reason for the specific dimensions beyond hitting the right A1Z26 values. The elegance of the answer word (TORQUE for simple machines) is undermined by the mechanical solving path. |
| Reading Reward | 2 | The puzzle explains each machine's operating principle inline -- you learn what a lever ratio is, how pulleys share load, how gear ratios work, what Pascal's principle does. This is genuinely educational content. But the solver does not need the encyclopedia (mechanical/, structural/) at all. Every formula is printed in the puzzle. The "You may find the Mechanics section helpful" hint is vestigial -- you do not need it. The puzzle is entirely self-contained. A solver who never opens the encyclopedia solves this identically to one who does. |
| Fun | 2 | The first machine (lever) is mildly engaging as you set up the ratio. By Machine 3 (gears), the pattern is clear: divide two numbers, multiply by the input. Machines 4-6 are repetitive. Machine 4 and Machine 5 both have a denominator of 1, making them trivial divisions. Machine 6 has a trivial input force of 1, making the multiplication pointless. The fun is front-loaded (novel format) and back-loaded (seeing TORQUE emerge), with a valley of arithmetic in between. |
| Confirmation | 4 | TORQUE is thematically perfect for a simple-machines puzzle. The word is 6 letters matching 6 machines exactly. After 3 machines you have TOR, which begins to suggest TORQUE. The Mechanics section hint aligns. Strong confirmation. |
| **Total** | **20/30** | |

## Issues

1. **No seed beyond "compute outputs."** The puzzle's mechanism is: apply the printed formula to the printed inputs. There is no twist, no discovery, no moment where the solver realizes something unexpected. In Kenny's brainstorming framework, this seed would be sent back for a hook in the first five minutes. "What if one of the machines is broken and the solver has to figure out which one?" "What if the formulas are NOT given and the solver must determine them from the encyclopedia?" "What if two machines are connected in series?" Any of these would add a genuine puzzle layer.

2. **The formulas are printed on the page.** This is the critical over-scaffolding problem. Each machine states its operating formula explicitly: "MA = effort arm / load arm," "Output force = number of supporting ropes x effort," "T_out / T_in = N_driven / N_driving." The solver does not need to know or discover anything -- the puzzle hands them the complete method. Compare to a version where the solver must determine the correct formula by consulting the encyclopedia: that would create a genuine Reading Reward.

3. **Trivial arithmetic.** Four of the six calculations involve dividing by 1 or multiplying by 1. Machine 4: 17/1. Machine 5: 21/1. Machine 6: 1 x 5. Machine 2: 3 x 5. The only calculations requiring actual division are Machine 1 (4/1 = 4, then 4 x 5 = 20) and Machine 3 (36/12 = 3, then 6 x 3 = 18). The arithmetic is so simple that a solver cannot meaningfully make an error -- the difficulty floor is basic multiplication.

4. **No encyclopedia engagement required.** The puzzle references mechanical/ and structural/ but provides every formula inline. A solver who ignores the encyclopedia entirely will arrive at the same answer in the same time. This violates the Reading Reward >= 4 principle.

## Suggested Fixes

1. **Remove the formulas.** Present the six machines with their dimensions and inputs but do NOT state the operating principle. The solver must consult the mechanical/ encyclopedia to learn how a lever ratio works, how pulleys share load, how gear ratios function. This transforms the puzzle from "compute" to "research and compute" -- the Reading Reward jumps from 2 to 4+.

2. **Add a deductive wrinkle.** For example: withhold one dimension per machine and give the solver a constraint (e.g., "the answer is a 6-letter word related to mechanics"). The solver must work backward from plausible letter values to determine the missing dimension. This creates genuine problem-solving.

3. **Connect the machines.** What if Machine 1's output force becomes Machine 2's input? Now the solver must get Machine 1 right before they can compute Machine 2. Error propagation creates real stakes. The machines become a system, not six isolated problems.

4. **Vary the cognitive task.** Not every machine should be a forward calculation. Machine 1: compute output (forward). Machine 2: given the output, compute the missing number of ropes (backward). Machine 3: given two possible gear ratios, determine which produces a valid A1Z26 letter (deductive). This creates variety in the solving experience.

---

# Test: Iron -- Thomas Snyder

## Solve Attempt

Thomas reads the puzzle and immediately applies his craftsmanship filter: "Is this hand-crafted with an intentional solving path, or is this a worksheet?"

He scans all six machines before computing anything. He notes:

- Every machine has a complete ASCII diagram with labeled dimensions.
- Every machine states its operating formula.
- Every machine provides all input values.
- Every worksheet has fill-in-the-blank spaces that mirror the formula exactly.

"This is a worksheet. The solver fills in blanks. There is no puzzle here -- there is a calculation exercise with an encoding step at the end."

He applies his computer test: "Could a computer generate and solve this puzzle?" The answer is trivially yes. Given a target word (TORQUE = 20, 15, 18, 17, 21, 5), assign each number to a machine type, then choose dimensions that produce that number via the machine's formula. The dimensions are reverse-engineered:

- Machine 1: Need 20. Lever MA = effort arm / load arm. Choose effort arm = 4, load arm = 1, effort = 5. Output = (4/1) x 5 = 20. Done.
- Machine 2: Need 15. Pulley output = ropes x effort. Choose ropes = 3, effort = 5. Output = 15. Done.
- Machine 3: Need 18. Gear output = input x (N_driven / N_driving). Choose 12T / 36T, input = 6. Output = 6 x 3 = 18. Done.
- Machine 4: Need 17. Ramp MA = length / height. Choose length = 17, height = 1. Done.
- Machine 5: Need 21. Wheel MA = R / r. Choose R = 21, r = 1. Done.
- Machine 6: Need 5. Press output = input x (A2 / A1). Choose input = 1, A1 = 2, A2 = 10. Output = 5. Done.

"A ten-line script could generate this puzzle for any 6-letter target word. Choose six machine types, pick dimensions that produce the target integers, generate diagrams. The dimensions are arbitrary -- there is no reason the lever has a 4:1 ratio except that 4 x 5 = 20 = T. There is no reason the ramp is 17 meters long except that 17 = Q. The puzzle was manufactured backward from the answer, and the manufacturing process is transparent."

He now evaluates each machine:

**Machine 1:** MA = 4/1 = 4. Output = 4 x 5 = 20. Letter T.

Thomas notes: "The question wording is the one interesting element in this puzzle. It says 'the question is different' -- the lever formula gives you the effort, but the puzzle asks for the output force. The solver must recognize that MA = effort arm / load arm, and output = MA x effort. This is a minor misdirection -- the word 'different' signals that the obvious calculation (balance equation) is not what is asked. But the worksheet immediately clarifies by printing the correct formula. The misdirection is introduced and resolved within the same paragraph. Net effect: zero."

**Machine 2:** Output = 3 x 5 = 15. Letter O.

"One multiplication. The ideal pulley formula is the simplest relationship in mechanics: force times advantage. The puzzle states 'the load is shared equally among all supporting rope segments.' This is the formula. There is nothing to figure out."

**Machine 3:** Ratio = 36/12 = 3. Output = 6 x 3 = 18. Letter R.

"The gear ratio formula is stated in the puzzle: 'T_out / T_in = N_driven / N_driving.' The solver plugs in numbers. The parenthetical note about power conservation is educational but irrelevant to the computation."

**Machine 4:** MA = 17/1 = 17. Letter Q.

"Dividing by 1. This is not a calculation; it is reading a number off the diagram."

**Machine 5:** MA = 21/1 = 21. Letter U.

"Same as Machine 4. Dividing by 1. The puzzle calls it 'a continuous lever' -- that is a nice conceptual bridge. But the computation is trivial."

**Machine 6:** Ratio = 10/2 = 5. Output = 1 x 5 = 5. Letter E.

"Dividing 10 by 2 and multiplying by 1. The multiplication by 1 is especially telling -- the input force is 1 N because the puzzle needs the output to be exactly 5 and the simplest way to achieve that is to make the force multiplier do all the work. This is a construction artifact, not a design choice."

**Extraction:** T-O-R-Q-U-E = TORQUE.

Thomas sits back. "TORQUE is an excellent answer word. It is precisely the right word for a simple-machines puzzle -- torque is the rotational force concept that unifies lever arms, gear ratios, and wheel-axle systems. Three of the six machines (lever, gears, wheel-and-axle) are fundamentally torque systems. The answer has thematic depth."

"But the answer's quality does not redeem the solving experience's quality. These are two separate evaluations. TORQUE is a 5/5 answer embedded in a 1/5 solving experience."

## Answer

**TORQUE**

## Scores

| Dimension | Score (1-5) | Notes |
|---|---|---|
| Clarity | 5 | Impeccable presentation. The ASCII diagrams are clear and well-labeled. Every formula is explicit. The worksheet structure is logical. A solver with no physics background can follow every step. The A1Z26 reference is provided. No ambiguity in any dimension or formula. |
| Solvability | 5 | Completely deterministic. All inputs given. All formulas stated. All calculations produce clean integers in the 1-26 range. No unit conversion required (forces in N, distances in consistent units per machine). No rounding. |
| Elegance | 1 | This is where the puzzle fails Thomas's standards entirely. Six independent forward calculations with no structural relationship. No interlock. No constraint propagation. No pattern across machines. The dimensions are transparently reverse-engineered from target values. Machines 4 and 5 both use denominators of 1. Machine 6 uses an input force of 1. These choices exist solely to hit target numbers -- they have no engineering rationale and no puzzle-design elegance. A hand-crafted puzzle reveals the constructor's intent at every step; these machines reveal only arithmetic convenience. |
| Reading Reward | 2 | Each machine description is a competent explanation of the operating principle. The lever/fulcrum diagram, the pulley rigging, the gear mesh, Pascal's principle -- these are well-written technical descriptions. A reader learns something from each one. But the solving process does not require the encyclopedia. The puzzle is entirely self-contained. The hint "You may find the Mechanics section helpful" is misleading -- you do not need it. Reading Reward measures whether solving requires engaging with the encyclopedia; here it does not. |
| Fun | 1 | Six arithmetic problems. Four of them involve dividing by 1 or multiplying by 1. The cognitive demand peaks at Machine 3 (36 / 12 = 3, then 6 x 3 = 18) and never exceeds single-digit mental math. There is no discovery, no surprise, no moment of delight during the solving process. The TORQUE reveal at the end is satisfying, but the path to it is tedious. The fun-per-minute ratio is very low. |
| Confirmation | 4 | TORQUE is thematically perfect. Six letters for six machines. The word describes the central force concept in classical mechanics. The Mechanics section hint aligns. After TOR (3 machines), the solver can anticipate TORQUE. Solid confirmation. |
| **Total** | **18/30** | |

## Issues

1. **Fails Snyder's Computer Test completely.** A trivial script generates this puzzle: pick a 6-letter target word, assign each letter's A1Z26 value to a machine type, choose dimensions that produce that value. The dimensions are arbitrary -- there is no constraint on them beyond producing the right integer. The solving script is equally trivial: read dimensions, apply formula, output letter. Ten lines of code, both directions. This is the definition of a computer-generatable puzzle.

2. **No intentional solving path.** The solver's experience is identical regardless of which machine they start with, how they approach each calculation, or what they know about physics. There is one path: plug numbers into formulas. Thomas's core question -- "Is there a choreographed solving journey?" -- yields a definitive no. The constructor cannot guide the solver's experience because every step is predetermined.

3. **Over-scaffolding at maximum.** The worksheet provides the formula, the blank spaces for intermediate values, and the structure for the final answer. If you removed the worksheet, the solver would still need to compute the same formulas -- but at least they would need to IDENTIFY which formula to use. The worksheet eliminates even that minimal cognitive task. This violates the No Over-Scaffolding principle directly.

4. **Dimensions expose the construction process.** A ramp 17 meters long and 1 meter high. A wheel with R = 21 cm and r = 1 cm. These are not realistic engineering dimensions -- they are numbers chosen to produce the letters Q and U. A solver who notices this will realize the dimensions are reverse-engineered, which breaks immersion. A well-crafted puzzle hides its construction; this puzzle advertises it.

## Suggested Fixes

1. **Remove all formulas.** Force the solver to discover the operating principle of each machine from the encyclopedia. The lever diagram shows dimensions but does not explain what a lever ratio is. The solver must consult mechanical/04-MACHINE-DESIGN.md or structural/01-STATICS.md to learn the formula. This creates a genuine reading requirement and transforms the puzzle from computation into research-driven computation.

2. **Add reverse-engineering steps.** For some machines, give the output and withhold an input dimension. "This lever lifts a 20 N load with 5 N of effort. What is the effort arm length?" The solver must work the formula backward. For others, give two possible configurations and ask which produces a valid A1Z26 letter. This creates deductive variety.

3. **Make the dimensions plausible.** Instead of R = 21 cm / r = 1 cm (transparently designed to produce 21), use R = 63 cm / r = 3 cm (same ratio, more realistic). Instead of ramp length = 17 m / height = 1 m, use length = 8.5 m / height = 0.5 m (same ratio, less conspicuous). The calculations become slightly more complex (fractional intermediates that simplify to the same integer) and the construction is less transparent.

4. **Introduce a broken machine.** One of the six machines has a deliberate error in its given dimensions -- the calculation produces a number outside 1-26 or a letter that breaks the word. The solver must identify which machine is broken and determine the correct dimension from context. This adds a deductive layer that pure computation lacks.

---

# Test: Iron -- Peter Sarrett

## Solve Attempt

Peter approaches this from his experience-design perspective. His first question is not "can I solve it?" but "what is the experience of solving it?"

He reads the Instrumentalist's flavor text: "Lever, pulley, gear, incline, wheel, press. Six machines. Six numbers." The voice is clean and measured. He opens the puzzle.

"Okay, six machines with diagrams. Each one has labeled dimensions, a formula printed right there, and blank spaces to fill in. This is a physics worksheet. I did these in high school."

**Solving experience, narrated:**

**Machine 1 -- Lever:**

Peter reads the diagram. "Nice ASCII art. The lever looks good. Effort arm 4 m, load arm 1 m, load 5 N." He reads the text: "For a balanced lever, effort x effort arm = load x load arm. But that gives you the effort -- the force you apply. The question is different."

"Okay, that is a tiny moment of misdirection. The puzzle says 'the question is different' and redirects me to compute output force via mechanical advantage. But then it prints the formula: MA = effort arm / load arm. So the misdirection lasts about three seconds before the puzzle solves its own misdirection for me."

```
MA = 4 / 1 = 4
Output = 4 x 5 = 20
```

"20 = T."

**Machine 2 -- Pulley:**

"Three ropes, 5 N. Output = 3 x 5 = 15. That is O."

"The pulley diagram is actually well-drawn -- I can trace the rope from A down to C, from B down to C, and the free end. If the puzzle asked me to COUNT the supporting ropes from the diagram, that would be a small puzzle. But it tells me: 'rope segments supporting the load: 3.' So there is nothing to figure out."

**Machine 3 -- Gears:**

"12 teeth and 36 teeth, 6 N-m. Ratio = 36/12 = 3. Output = 18. That is R."

"I now have T-O-R. I suspect this spells TORQUE. Let me check: if the answer is TORQUE, the remaining letters are Q=17, U=21, E=5. Let me see if the remaining machines produce those numbers."

He glances ahead:

- Machine 4: Ramp 17 m long, 1 m high. MA = 17/1 = 17. Q. Yes.
- Machine 5: Wheel R=21, axle r=1. MA = 21/1 = 21. U. Yes.
- Machine 6: Press areas 2 and 10, force 1 N. Output = 10/2 x 1 = 5. E. Yes.

"TORQUE. I solved the puzzle at Machine 3 by guessing the word and verifying forward. Machines 4-6 are confirmation, not solving."

**This is the critical experience-design observation.** Peter notes: "A solver who recognizes the pattern -- simple machines, forces, thematic word -- can shortcut the puzzle after 3 of 6 calculations. The puzzle does not prevent this. The last three machines are redundant once the solver guesses TORQUE. In a well-designed puzzle, guessing ahead should be possible but should not eliminate the need to engage with the remaining content. Here, it eliminates everything."

"Compare to a crossword: if you guess a long Across answer, you still need the Down crossings to confirm individual letters. Here, there are no crossings. Once you have the word, the remaining machines are just checking arithmetic you already know the answer to."

**Reading Reward assessment:**

Peter now asks his signature question: "Does the puzzle make you a better reader of the encyclopedia?"

"No. The puzzle explains each machine's operating principle inline. I did not open the mechanical/ or structural/ directories. I did not need to. Every formula was printed on the page. The diagrams were self-contained tutorials. I learned what a compound pulley does and how Pascal's principle works -- but I learned it from the PUZZLE, not from the ENCYCLOPEDIA. The encyclopedia is irrelevant to the solving experience."

"This means the puzzle violates the fundamental conceit of the project: that the puzzles are embedded in an encyclopedia and require engaging with it. This puzzle could exist in any context -- a physics textbook, a children's activity book, a standardized test. The encyclopedia adds nothing."

**The "Chicago Fire" test:**

Peter applies his own standard: "Is there a moment where the medium does something unexpected? Where the solver interacts with the book in a way they did not anticipate?"

"No. The solver reads a description, applies a formula, writes a number, converts to a letter. This is the most predictable possible interaction with a page. There is no 'pour water on it' moment. There is no 'look at it from a different angle' moment. There is no surprise in the medium."

## Answer

**TORQUE**

## Scores

| Dimension | Score (1-5) | Notes |
|---|---|---|
| Clarity | 5 | The diagrams are well-drawn. The formulas are explicit. The worksheet is structured. A solver with no physics background can follow every step. The ASCII engineering drawings are actually one of the puzzle's genuine strengths -- they are clean and readable. |
| Solvability | 5 | Deterministic. All inputs given. All formulas stated. Clean integers throughout. No ambiguity. The puzzle cannot produce a wrong answer unless the solver makes an arithmetic error. |
| Elegance | 1 | Six independent calculations with no interlock. The dimensions are transparently chosen to produce target values (17/1, 21/1, 1 N input). No machine's answer constrains any other. The puzzle is guessable after 3 of 6 machines, rendering the second half redundant. There is no structural relationship between the machines -- they are six standalone problems sharing a worksheet. |
| Reading Reward | 1 | This is the puzzle's most serious failure. The encyclopedia is not needed. Every formula is printed inline. Every operating principle is explained in the puzzle text. A solver who never opens the mechanical/ or structural/ directories solves the puzzle identically to one who memorizes them. The hint "You may find the Mechanics section helpful" is false -- you will not find it helpful because you do not need it. The puzzle teaches physics, but it teaches it INSTEAD of the encyclopedia, not THROUGH it. Reading Reward must measure engagement with the encyclopedia, not engagement with the puzzle's own text. |
| Fun | 2 | The first machine is mildly interesting (lever with a small misdirection about which force to compute). The TORQUE reveal is satisfying. Everything between is arithmetic. The puzzle is guessable at Machine 3, eliminating the fun of machines 4-6. The experience is: compute, compute, compute, guess the word, verify. Not: discover, connect, realize. |
| Confirmation | 4 | TORQUE is an excellent answer word for a simple-machines puzzle. Six letters for six machines. Thematically resonant. Partially confirmable at Machine 3 (TOR -> TORQUE). The Mechanics hint aligns. |
| **Total** | **18/30** | |

## Issues

1. **Zero encyclopedia engagement.** The puzzle is entirely self-contained. Every formula is printed. Every principle is explained. The solver never needs to open the encyclopedia. This violates the Reading Reward >= 4 principle and the Riven Standard ("the puzzle IS what the section does, not an obstacle overlaid on it"). The puzzle is overlaid on mechanics; it does not arise from the encyclopedia's content.

2. **Guessable at the halfway point.** After T-O-R from machines 1-3, a solver familiar with mechanics will guess TORQUE. Machines 4-6 become redundant verification. A well-designed puzzle should make guessing ahead rewarding (you can verify) but not trivializing (you still need to engage with the remaining content). Here, guessing TORQUE eliminates all further engagement.

3. **Computation, not deduction.** Every step is: read the given values, apply the given formula, write the result. There is no step where the solver must figure something out. No missing information to infer. No ambiguous formula to resolve. No connection between machines to exploit. The cognitive task is identical to filling in a worksheet.

4. **The diagrams are wasted potential.** The ASCII machine diagrams are actually well-crafted. A pulley system with traceable ropes, a gear mesh with labeled teeth, a hydraulic press with connected pistons. These diagrams could be the basis of real puzzles -- "count the supporting ropes," "trace the force path," "identify which piston is the input." Instead, the puzzle labels every relevant quantity on the diagram AND states it in the "Given" section AND prints the formula. The diagrams become illustrations, not puzzles.

## Suggested Fixes

1. **Remove all formulas and "Given" callouts.** Present only the diagrams with labeled dimensions. The solver must (a) understand what each machine does by consulting the encyclopedia, (b) identify the relevant dimensions from the diagram, (c) determine the correct formula, and (d) compute the answer. This creates a 4-step solving process where only step (d) is computation. Currently the puzzle pre-solves steps (a), (b), and (c).

2. **Make the diagrams the puzzle.** Hide the critical dimension within the diagram rather than stating it separately. For the pulley: draw the rope routing and make the solver count supporting segments. For the gears: show the teeth but do not state the count -- the solver must count teeth on the diagram. For the ramp: draw it to scale and make the solver measure the ratio. The diagram becomes something to analyze, not just something to look at.

3. **Create cross-machine dependencies.** The output of Machine 1 (20 N) becomes the effort input for Machine 2. The gear ratio from Machine 3 constrains the wheel ratio in Machine 5. These connections create a solving chain where early errors propagate and early successes compound. The six machines become a system.

4. **Add one machine with a twist.** Five of six machines are straightforward forward calculations. The sixth requires the solver to work backward: "This press exerts __ N of output force. The large piston area is 10 cm2. What must the small piston area be, if the input force is 1 N?" The solver must reason in reverse. One different cognitive task among five similar ones prevents the grinding feeling.

---

# Synthesis

## Score Summary

| Dimension | Young | Snyder | Sarrett | Average |
|---|---|---|---|---|
| Clarity | 5 | 5 | 5 | **5.0** |
| Solvability | 5 | 5 | 5 | **5.0** |
| Elegance | 2 | 1 | 1 | **1.3** |
| Reading Reward | 2 | 2 | 1 | **1.7** |
| Fun | 2 | 1 | 2 | **1.7** |
| Confirmation | 4 | 4 | 4 | **4.0** |
| **Total** | **20** | **18** | **18** | **18.7/30** |

## Principle Checks

| Principle | Pass/Fail | Notes |
|---|---|---|
| The Riven Standard | **FAIL** | The puzzle is overlaid on mechanics; it does not arise from the encyclopedia. Removing the encyclopedia changes nothing about the solving experience. The formulas are self-contained. |
| Solving = Proving Understanding | **FAIL** | The solver proves they can do arithmetic, not that they understand simple machines. The formulas are given; the solver does not need to understand WHY a lever multiplies force, only that the ratio is printed on the page. |
| The Dinner Party Test | **FAIL** | "I did six physics calculations and the numbers spelled TORQUE" is not a dinner-party story. |
| The Book Test | Pass | Pencil and book. No tools needed beyond arithmetic. |
| Blame the Player | Pass | The puzzle is fair. All information is given. No trick questions. |
| The 80% Rule | N/A | Single puzzle, not a meta. |
| Reading Reward >= 4 | **FAIL** | All three testers scored this 1-2. The encyclopedia is not needed. |
| No Over-Scaffolding | **FAIL** | The worksheet provides formulas, intermediate blanks, and structure. The puzzle does all the work; the solver just computes. |
| Surprise the Answer | **Marginal** | TORQUE is thematically perfect and somewhat predictable for a mechanics puzzle. Not the most obvious word (ENERGY, FORCES would be more predictable), but a solver who thinks "rotational force in 6 letters" lands on TORQUE quickly. |
| One Aha, Not Zero | **FAIL** | Zero ahas. No discovery moment. The "aha" of seeing TORQUE emerge is a reward, not a puzzle-solving insight. |
| Snyder's Computer Test | **FAIL** | A ten-line script generates and solves this puzzle. The dimensions are reverse-engineered from target A1Z26 values. The solving process is pure computation. |
| Interlock, Not Independence | **FAIL** | Six completely independent calculations. No cross-referencing. No chain dependencies. |
| No Deliberate Errors | Pass | All formulas are correct. All dimensions produce correct results. |
| The Voice Rules | Pass | The Instrumentalist's flavor text follows voice rules. |

**Principles passed:** 4 of 14 applicable
**Principles failed:** 8 of 14 applicable

## Consensus Issues

1. **Computation, not deduction (all three -- unanimous).** This is the same failure mode as Magnesium. The solver applies given formulas to given inputs six times. There is no discovery, no inference, no moment where the solver must figure something out. Young calls it "the Magnesium pattern." Snyder calls it "a worksheet." Sarrett calls it "a physics textbook problem set." The consensus is absolute: applying a printed formula to printed numbers is not a puzzle.

2. **Zero encyclopedia engagement (all three -- unanimous).** The puzzle is entirely self-contained. Every formula is printed inline. Every operating principle is explained in the puzzle text. The mechanical/ and structural/ directories are never needed. Sarrett scores Reading Reward at 1 -- the lowest possible -- because the encyclopedia is not just unnecessary but irrelevant. Young and Snyder score it at 2, giving credit for the educational content within the puzzle text itself. But all three agree: the encyclopedia connection is broken.

3. **Transparent reverse-engineering of dimensions (Snyder, Sarrett).** The dimensions (17/1, 21/1, R=21/r=1, force=1N) are obviously chosen to produce specific A1Z26 values. A ramp that is 17 meters long and 1 meter high is not a plausible engineering scenario -- it is a number chosen to produce the letter Q. This breaks immersion and reveals the construction process.

4. **Guessable at halfway (Sarrett).** After T-O-R from the first three machines, the word TORQUE is strongly suggested. Machines 4-6 become redundant verification, not genuine solving. The puzzle provides no mechanism to prevent or complicate this shortcut.

5. **Over-scaffolded worksheets (all three).** The worksheets provide formulas, intermediate blank spaces, and step-by-step structure. The solver fills in blanks rather than determining what to calculate. Even the minimal cognitive task of identifying the correct formula is pre-solved.

## Consensus Strengths

1. **Excellent clarity and presentation (all three, unanimous 5/5).** The ASCII machine diagrams are well-crafted. The lever, pulley, gears, ramp, wheel-and-axle, and hydraulic press are all clearly drawn with labeled dimensions. The formulas are unambiguous. The worksheet structure is logical. The puzzle communicates its rules with zero friction.

2. **Perfect answer word (all three, 4/5 on Confirmation).** TORQUE is thematically ideal for a simple-machines puzzle. It describes the central force concept that unifies lever arms, gear ratios, and wheel-and-axle systems. Six letters for six machines. Partially confirmable at the halfway point. The Instrumentalist card -- measuring before making -- aligns perfectly.

3. **Educational machine descriptions.** Each machine's operating principle is competently explained. The lever-fulcrum relationship, pulley rope sharing, gear power conservation, Pascal's principle -- these are real physics concepts presented clearly. The content is good; the problem is that the content lives inside the puzzle rather than inside the encyclopedia.

4. **Deterministic and error-resistant.** All six calculations produce clean integers with no rounding, no unit conversion traps, and no ambiguity. A solver who follows the printed formulas cannot arrive at a wrong answer. This is a strength for clarity but a weakness for puzzle-design.

## Verdict: REVISE

**Score: 18.7/30** -- below passing threshold. Lowest score in the test suite to date.

This is a pure computation exercise with no puzzle layer. It shares the same fundamental failure as Magnesium (20.7/30) but scores lower because: (a) the formulas are printed on the page (Magnesium at least required the solver to know truth tables, even though they were provided), (b) four of six calculations involve trivially dividing or multiplying by 1, and (c) the encyclopedia is completely irrelevant to the solve (Magnesium's gate reference at least taught the solver something new during the first few circuits).

The answer TORQUE and the Instrumentalist thematic wrapper are strong. The diagrams are well-crafted. The puzzle is beautifully presented. But presentation does not compensate for the absence of a puzzle.

### Required Revisions

1. **Remove all inline formulas.** This is the single most impactful change. The solver must consult the encyclopedia (mechanical/04-MACHINE-DESIGN.md, structural/01-STATICS.md) to learn how each machine works. The puzzle provides diagrams and dimensions; the encyclopedia provides the physics. This immediately transforms Reading Reward from 1-2 to 4-5 and creates a genuine research-driven solving experience. The encyclopedia becomes essential, not decorative.

2. **Add a deductive layer.** At least two of the six machines should require the solver to DETERMINE something rather than just compute. Options:
   - A machine with a missing dimension that the solver infers from the constraint that the answer must be a valid A1Z26 letter (1-26).
   - A machine where two possible configurations are given and the solver must determine which one produces a letter consistent with the emerging word.
   - A machine where the diagram contains the critical information (e.g., count the gear teeth from the drawing) rather than stating it in text.

3. **Fix the trivial arithmetic.** Eliminate denominators and multipliers of 1. Use dimensions that require actual calculation: ramp length 51 m / height 3 m (MA = 17). Wheel R = 63 cm / r = 3 cm (MA = 21). Press areas 4 cm2 and 20 cm2 with force 1 N (ratio = 5). The calculations become real multi-step problems instead of reading numbers off the page.

4. **Create at least one cross-machine dependency.** The output of one machine should feed into another. This creates interlock, prevents the solver from skipping ahead via word-guessing, and makes the six machines feel like a connected system rather than six isolated worksheets.
