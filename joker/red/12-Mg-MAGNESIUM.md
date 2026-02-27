# [12] --- Magnesium

**8&#9827; The Fabricator** &middot; Technology &middot; &#9733; T1

---

> The Fabricator builds chains of components, each one transforming what the last one made. But some parts fell off the bench. Figure out what they were. Follow the signal. Don't lose it.

---

## The Puzzle

Ten circuits. Each one takes binary inputs, routes them through logic gates, and produces five output bits. Five bits make a number. A number makes a letter.

But the Fabricator's parts bin is incomplete. Some gates are missing their labels -- shown as **?** marks. You must deduce which gate type belongs at each **?** by reasoning about what output the circuit needs to produce a valid letter (A--Z, decimal 1--26).

Four of the missing gates are **shared parts** -- marked with symbols (**&#9651;**, **&#9671;**, **&#9633;**, **&#9734;**). Each symbol represents the same gate type everywhere it appears. Solving a shared part in one circuit tells you what it is in every other circuit that uses it.

Here are the gates you will encounter:

```
GATE REFERENCE
──────────────────────────────────────────────────────
  AND     A ──┐             0 AND 0 = 0
              ├── AND ── Y  0 AND 1 = 0
          B ──┘             1 AND 0 = 0
                            1 AND 1 = 1

  OR      A ──┐             0 OR 0 = 0
              ├── OR ─── Y  0 OR 1 = 1
          B ──┘             1 OR 0 = 1
                            1 OR 1 = 1

  XOR     A ──┐             0 XOR 0 = 0
              ├── XOR ── Y  0 XOR 1 = 1
          B ──┘             1 XOR 0 = 1
                            1 XOR 1 = 0

  NOT     A ── NOT ──── Y   NOT 0 = 1
                            NOT 1 = 0
──────────────────────────────────────────────────────

Every ? is one of: AND, OR, or XOR.
(NOT gates are always labeled. They are never missing.)
```

Collect the five output bits b4 b3 b2 b1 b0 (most significant first). Convert each 5-bit binary number to a letter: A=1, B=2, ... Z=26.

---

### Circuit 1

```
Inputs:  A = 1,  B = 0,  C = 1

         A ──┐
             ├── AND ── G1 ─────────────────────── b4
         C ──┘

         A ──┐
             ├── (△) ── G2 ──┐
         B ──┘               ├── AND ── G3 ─────── b3
         B ──────────────────┘

         B ── NOT ── G4 ──────────────────────────── b2

         B ──┐
             ├── AND ── G5 ─────────────────────── b1
         C ──┘

         A ──┐
             ├── AND ── G6 ─────────────────────── b0
         B ──┘
```

---

### Circuit 2

```
Inputs:  A = 1,  B = 1,  C = 0,  D = 1

         A ──┐
             ├── AND ── G1 ─────────────────────── b4
         D ──┘

         C ──┐
             ├── (◇) ── G2 ──┐
         D ──┘               ├── AND ── G3 ─────── b3
         C ──────────────────┘

         A ──┐
             ├── AND ── G4 ─────────────────────── b2
         C ──┘

         C ── NOT ── G5 ──────────────────────────── b1

         B ──┐
             ├── AND ── G6 ─────────────────────── b0
         C ──┘
```

---

### Circuit 3

```
Inputs:  A = 1,  B = 0,  C = 1

         A ── NOT ── G1 ──────────────────────────── b4

         A ──┐
             ├── AND ── G2 ─────────────────────── b3
         B ──┘

         B ──┐
             ├── AND ── G3 ─────────────────────── b2
         C ──┘

         B ──┐
             ├── (?) ── G4 ─────────────────────── b1
         C ──┘

         A ──┐
             ├── AND ── G5 ─────────────────────── b0
         C ──┘
```

---

### Circuit 4

```
Inputs:  A = 0,  B = 1,  C = 1,  D = 0

         A ──┐
             ├── AND ── G1 ─────────────────────── b4
         B ──┘

         D ── NOT ── G2 ──────────────────────────── b3

         B ──┐
             ├── (☐) ── G3 ──┐
         C ──┘               ├── OR ─── G4 ─────── b2
         B ──────────────────┘

         B ──┐
             ├── AND ── G5 ─────────────────────── b1
         C ──┘

         A ──┐
             ├── AND ── G6 ─────────────────────── b0
         D ──┘
```

---

### Circuit 5

```
Inputs:  A = 1,  B = 0,  C = 1,  D = 1

         C ──┐
             ├── AND ── G1 ─────────────────────── b4
         D ──┘

         A ──┐
             ├── (☆) ── G2 ──┐
         B ──┘               ├── AND ── G3 ─────── b3
         B ──────────────────┘

         A ──┐
             ├── XOR ── G4 ─────────────────────── b2
         C ──┘

         B ── NOT ── G5 ──────────────────────────── b1

         A ──┐
             ├── AND ── G6 ─────────────────────── b0
         D ──┘
```

---

### Circuit 6

```
Inputs:  A = 1,  B = 0,  C = 1,  D = 1

         A ──┐
             ├── AND ── G1 ─────────────────────── b4
         B ──┘

         B ── NOT ── G2 ──────────────────────────── b3

         A ──┐
             ├── (△) ── G3 ─────────────────────── b2
         C ──┘

         B ──┐
             ├── AND ── G4 ─────────────────────── b1
         D ──┘

         C ──┐
             ├── AND ── G5 ─────────────────────── b0
         D ──┘
```

---

### Circuit 7

```
Inputs:  A = 1,  B = 1,  C = 0

         A ──┐
             ├── XOR ── G1 ─────────────────────── b4
         C ──┘

         B ──┐
             ├── (◇) ── G2 ─────────────────────── b3
         C ──┘

         A ──┐
             ├── AND ── G3 ─────────────────────── b2
         C ──┘

         A ──┐
             ├── AND ── G4 ─────────────────────── b1
         B ──┘

         C ── NOT ── G5 ──────────────────────────── b0
```

---

### Circuit 8

```
Inputs:  A = 1,  B = 1,  C = 0,  D = 1

         A ──┐
             ├── AND ── G1 ─────────────────────── b4
         D ──┘

         A ──┐
             ├── (☐) ── G2 ─────────────────────── b3
         B ──┘

         C ── NOT ── G3 ──────────────────────────── b2

         B ──┐
             ├── AND ── G4 ─────────────────────── b1
         C ──┘

         C ──┐
             ├── AND ── G5 ─────────────────────── b0
         D ──┘
```

---

### Circuit 9

```
Inputs:  A = 1,  B = 1,  C = 0,  D = 1

         A ──┐
             ├── (?) ── G1 ─────────────────────── b4
         B ──┘

         A ──┐
             ├── AND ── G2 ─────────────────────── b3
         D ──┘

         C ── NOT ── G3 ──────────────────────────── b2

         B ──┐
             ├── AND ── G4 ─────────────────────── b1
         D ──┘

         A ──┐
             ├── OR ─── G5 ─────────────────────── b0
         C ──┘
```

---

### Circuit 10

```
Inputs:  A = 1,  B = 0,  C = 1

         A ──┐
             ├── AND ── G1 ─────────────────────── b4
         C ──┘

         B ──┐
             ├── (☆) ── G2 ─────────────────────── b3
         A ──┘

         A ──┐
             ├── XOR ── G3 ─────────────────────── b2
         C ──┘

         B ── NOT ── G4 ──────────────────────────── b1

         B ──┐
             ├── AND ── G5 ─────────────────────── b0
         C ──┘
```

---

### Parts Bin

```
SHARED PARTS — same gate type wherever the symbol appears
──────────────────────────────────────────────────────
  △  triangle    appears in Circuits 1 and 6
  ◇  diamond     appears in Circuits 2 and 7
  ☐  square      appears in Circuits 4 and 8
  ☆  star        appears in Circuits 5 and 10
──────────────────────────────────────────────────────

LOCAL UNKNOWNS — appear in only one circuit
──────────────────────────────────────────────────────
  ?  Circuit 3   (one unknown gate)
  ?  Circuit 9   (one unknown gate)
──────────────────────────────────────────────────────
```

---

### Binary-to-Letter Conversion

```
A=1    B=2    C=3    D=4    E=5    F=6    G=7    H=8    I=9
J=10   K=11   L=12   M=13   N=14   O=15   P=16   Q=17   R=18
S=19   T=20   U=21   V=22   W=23   X=24   Y=25   Z=26

Binary quick reference:
00001=1   00010=2   00011=3   00100=4   00101=5
00110=6   00111=7   01000=8   01001=9   01010=10
01011=11  01100=12  01101=13  01110=14  01111=15
10000=16  10001=17  10010=18  10011=19  10100=20
10101=21  10110=22  10111=23  11000=24  11001=25
11010=26
```

---

### Extraction

```
PART DEDUCTIONS
──────────────────────────────────────────────────────
  △  triangle  =  ___________
  ◇  diamond   =  ___________
  ☐  square    =  ___________
  ☆  star      =  ___________
  ?  Circuit 3 =  ___________
  ?  Circuit 9 =  ___________
──────────────────────────────────────────────────────

Circuit:    1     2     3     4     5     6     7     8     9     10

Binary:   _____  _____  _____  _____  _____  _____  _____  _____  _____  _____

Decimal:  ___    ___    ___    ___    ___    ___    ___    ___    ___    ___

Letter:   ___    ___    ___    ___    ___    ___    ___    ___    ___    ___
```

---

**Your answer** (10 letters): _ _ _ _ _ _ _ _ _ _

*You may find the Technology section helpful.*
