# [12] --- Magnesium

**8&#9827; The Fabricator** &middot; Technology &middot; &#9733; T1

---

> The Fabricator builds chains of components, each one transforming what the last one made. Follow the signal. Don't lose it.

---

## The Puzzle

Ten circuits. Each one takes a handful of binary inputs and routes them through logic gates. Your job is to evaluate every gate -- by hand, in order, tracing the signal through each wire -- until you have five output bits.

Five bits make a number. A number makes a letter.

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

  NOT     A ── NOT ──── Y   NOT 0 = 1
                            NOT 1 = 0

  XOR     A ──┐             0 XOR 0 = 0
              ├── XOR ── Y  0 XOR 1 = 1
          B ──┘             1 XOR 0 = 1
                            1 XOR 1 = 0
──────────────────────────────────────────────────────
```

Each circuit gives you its input values. Evaluate every gate left to right, top to bottom. Collect the five output bits b4 b3 b2 b1 b0 (most significant first). Convert each 5-bit binary number to a letter using A=1, B=2, ... Z=26.

---

### Circuit 1

```
Inputs:  A = 1,  B = 1,  C = 0

         A ──┐
             ├── AND ── G1 ─────────────────────── b4
         B ──┘

         B ──┐
             ├── AND ── G2 ─────────────────────── b3
         C ──┘

         A ──┐
             ├── XOR ── G3 ── NOT ── G4 ────────── b2
         B ──┘

         A ──┐
             ├── AND ── G5 ─────────────────────── b1
         C ──┘

         C ──┐
             ├── AND ── G6 ─────────────────────── b0
         A ──┘
```

---

### Circuit 2

```
Inputs:  A = 1,  B = 1,  C = 0,  D = 1

         A ──┐
             ├── AND ── G1 ─────────────────────── b4
         B ──┘

         C ──┐
             ├── OR ─── G2 ── NOT ── G3 ────────── b3
         D ──┘

         C ──┐
             ├── AND ── G4 ─────────────────────── b2
         D ──┘

         A ──┐
             ├── XOR ── G5 ── NOT ── G6 ────────── b1
         B ──┘

         C ──┐
             ├── AND ── G7 ─────────────────────── b0
         A ──┘
```

---

### Circuit 3

```
Inputs:  A = 1,  B = 0,  C = 1

         A ── NOT ── G1 ───────────────────────── b4

         A ──┐
             ├── AND ── G2 ─────────────────────── b3
         B ──┘

         B ──┐
             ├── AND ── G3 ─────────────────────── b2
         C ──┘

         B ──┐
             ├── OR ─── G4 ── NOT ── G5 ────────── b1
         C ──┘

         A ──┐
             ├── AND ── G6 ─────────────────────── b0
         C ──┘
```

---

### Circuit 4

```
Inputs:  A = 0,  B = 1,  C = 1,  D = 0

         A ──┐
             ├── OR ─── G1 ── NOT ── G2 ────────── b4
         B ──┘

         B ──┐
             ├── AND ── G3 ─────────────────────── b3
         C ──┘

         C ──┐
             ├── XOR ── G4 ─────────────────────── b2
         D ──┘

         D ── NOT ── G5 ───────────────────────── b1

         A ──┐
             ├── AND ── G6 ─────────────────────── b0
         D ──┘
```

---

### Circuit 5

```
Inputs:  A = 1,  B = 0,  C = 1,  D = 1

         A ──┐
             ├── AND ── G1 ─────────────────────── b4
         C ──┘

         B ──┐
             ├── OR ─── G2 ── NOT ── G3 ────────── b3
         D ──┘

         A ──┐
             ├── XOR ── G4 ─────────────────────── b2
         C ──┘

         C ──┐
             ├── AND ── G5 ─────────────────────── b1
         D ──┘

         B ── NOT ── G6 ───────────────────────── b0
```

---

### Circuit 6

```
Inputs:  A = 1,  B = 0,  C = 0,  D = 1

         A ──┐
             ├── XOR ── G1 ─────────────────────── b4
         D ──┘

         C ── NOT ── G2 ──┐
                          ├── AND ── G3 ────────── b3
         D ───────────────┘

         B ──┐
             ├── OR ─── G4 ─────────────────────── b2
         C ──┘

         A ──┐
             ├── AND ── G5 ─────────────────────── b1
         B ──┘

         A ──┐
             ├── AND ── G6 ─────────────────────── b0
         D ──┘
```

---

### Circuit 7

```
Inputs:  A = 1,  B = 1,  C = 0

         A ──┐
             ├── XOR ── G1 ─────────────────────── b4
         C ──┘

         A ── NOT ── G2 ──┐
                          ├── OR ─── G3 ────────── b3
         C ───────────────┘

         B ──┐
             ├── AND ── G4 ─────────────────────── b2
         C ──┘

         A ──┐
             ├── AND ── G5 ─────────────────────── b1
         B ──┘

         A ──┐
             ├── XOR ── G6 ── NOT ── G7 ────────── b0
         B ──┘
```

---

### Circuit 8

```
Inputs:  A = 0,  B = 1,  C = 1,  D = 0

         A ── NOT ── G1 ──┐
                          ├── AND ── G2 ────────── b4
         C ───────────────┘

         A ──┐
             ├── AND ── G3 ─────────────────────── b3
         D ──┘

         B ──┐
             ├── XOR ── G4 ─────────────────────── b2
         D ──┘

         A ──┐
             ├── OR ─── G5 ─────────────────────── b1
         D ──┘

         C ──┐
             ├── AND ── G6 ─────────────────────── b0
         D ──┘
```

---

### Circuit 9

```
Inputs:  A = 1,  B = 1,  C = 0,  D = 1

         A ── NOT ── G1 ──┐
                          ├── OR ─── G2 ────────── b4
         C ───────────────┘

         A ──┐
             ├── AND ── G3 ─────────────────────── b3
         B ──┘

         B ──┐
             ├── XOR ── G4 ─────────────────────── b2
         C ──┘

         A ──┐
             ├── OR ─── G5 ─────────────────────── b1
         D ──┘

         C ── NOT ── G6 ───────────────────────── b0
```

---

### Circuit 10

```
Inputs:  A = 1,  B = 0,  C = 1

         A ──┐
             ├── OR ─── G1 ──┐
         B ──┘               ├── AND ── G2 ─────── b4
         C ──────────────────┘

         A ── NOT ── G3 ──┐
                          ├── OR ─── G4 ────────── b3
         B ───────────────┘

         A ──┐
             ├── XOR ── G5 ─────────────────────── b2
         C ──┘

         B ── NOT ── G6 ───────────────────────── b1

         B ──┐
             ├── AND ── G7 ─────────────────────── b0
         C ──┘
```

---

## Worksheet

Evaluate each gate. Write the result in the blank. Then collect the five output bits.

### Circuit 1 &ensp; (A=1, B=1, C=0)

```
  G1 = A AND B  = ___ AND ___ = ___   → b4 = ___
  G2 = B AND C  = ___ AND ___ = ___   → b3 = ___
  G3 = A XOR B  = ___ XOR ___ = ___
  G4 = NOT G3   = NOT ___     = ___   → b2 = ___
  G5 = A AND C  = ___ AND ___ = ___   → b1 = ___
  G6 = C AND A  = ___ AND ___ = ___   → b0 = ___

  Binary:  b4 b3 b2 b1 b0 = ___ ___ ___ ___ ___
  Decimal: ___    Letter: ___
```

### Circuit 2 &ensp; (A=1, B=1, C=0, D=1)

```
  G1 = A AND B  = ___ AND ___ = ___   → b4 = ___
  G2 = C OR D   = ___ OR  ___ = ___
  G3 = NOT G2   = NOT ___     = ___   → b3 = ___
  G4 = C AND D  = ___ AND ___ = ___   → b2 = ___
  G5 = A XOR B  = ___ XOR ___ = ___
  G6 = NOT G5   = NOT ___     = ___   → b1 = ___
  G7 = C AND A  = ___ AND ___ = ___   → b0 = ___

  Binary:  b4 b3 b2 b1 b0 = ___ ___ ___ ___ ___
  Decimal: ___    Letter: ___
```

### Circuit 3 &ensp; (A=1, B=0, C=1)

```
  G1 = NOT A    = NOT ___     = ___   → b4 = ___
  G2 = A AND B  = ___ AND ___ = ___   → b3 = ___
  G3 = B AND C  = ___ AND ___ = ___   → b2 = ___
  G4 = B OR C   = ___ OR  ___ = ___
  G5 = NOT G4   = NOT ___     = ___   → b1 = ___
  G6 = A AND C  = ___ AND ___ = ___   → b0 = ___

  Binary:  b4 b3 b2 b1 b0 = ___ ___ ___ ___ ___
  Decimal: ___    Letter: ___
```

### Circuit 4 &ensp; (A=0, B=1, C=1, D=0)

```
  G1 = A OR B   = ___ OR  ___ = ___
  G2 = NOT G1   = NOT ___     = ___   → b4 = ___
  G3 = B AND C  = ___ AND ___ = ___   → b3 = ___
  G4 = C XOR D  = ___ XOR ___ = ___   → b2 = ___
  G5 = NOT D    = NOT ___     = ___   → b1 = ___
  G6 = A AND D  = ___ AND ___ = ___   → b0 = ___

  Binary:  b4 b3 b2 b1 b0 = ___ ___ ___ ___ ___
  Decimal: ___    Letter: ___
```

### Circuit 5 &ensp; (A=1, B=0, C=1, D=1)

```
  G1 = A AND C  = ___ AND ___ = ___   → b4 = ___
  G2 = B OR D   = ___ OR  ___ = ___
  G3 = NOT G2   = NOT ___     = ___   → b3 = ___
  G4 = A XOR C  = ___ XOR ___ = ___   → b2 = ___
  G5 = C AND D  = ___ AND ___ = ___   → b1 = ___
  G6 = NOT B    = NOT ___     = ___   → b0 = ___

  Binary:  b4 b3 b2 b1 b0 = ___ ___ ___ ___ ___
  Decimal: ___    Letter: ___
```

### Circuit 6 &ensp; (A=1, B=0, C=0, D=1)

```
  G1 = A XOR D  = ___ XOR ___ = ___   → b4 = ___
  G2 = NOT C    = NOT ___     = ___
  G3 = G2 AND D = ___ AND ___ = ___   → b3 = ___
  G4 = B OR C   = ___ OR  ___ = ___   → b2 = ___
  G5 = A AND B  = ___ AND ___ = ___   → b1 = ___
  G6 = A AND D  = ___ AND ___ = ___   → b0 = ___

  Binary:  b4 b3 b2 b1 b0 = ___ ___ ___ ___ ___
  Decimal: ___    Letter: ___
```

### Circuit 7 &ensp; (A=1, B=1, C=0)

```
  G1 = A XOR C  = ___ XOR ___ = ___   → b4 = ___
  G2 = NOT A    = NOT ___     = ___
  G3 = G2 OR C  = ___ OR  ___ = ___   → b3 = ___
  G4 = B AND C  = ___ AND ___ = ___   → b2 = ___
  G5 = A AND B  = ___ AND ___ = ___   → b1 = ___
  G6 = A XOR B  = ___ XOR ___ = ___
  G7 = NOT G6   = NOT ___     = ___   → b0 = ___

  Binary:  b4 b3 b2 b1 b0 = ___ ___ ___ ___ ___
  Decimal: ___    Letter: ___
```

### Circuit 8 &ensp; (A=0, B=1, C=1, D=0)

```
  G1 = NOT A    = NOT ___     = ___
  G2 = G1 AND C = ___ AND ___ = ___   → b4 = ___
  G3 = A AND D  = ___ AND ___ = ___   → b3 = ___
  G4 = B XOR D  = ___ XOR ___ = ___   → b2 = ___
  G5 = A OR D   = ___ OR  ___ = ___   → b1 = ___
  G6 = C AND D  = ___ AND ___ = ___   → b0 = ___

  Binary:  b4 b3 b2 b1 b0 = ___ ___ ___ ___ ___
  Decimal: ___    Letter: ___
```

### Circuit 9 &ensp; (A=1, B=1, C=0, D=1)

```
  G1 = NOT A    = NOT ___     = ___
  G2 = G1 OR C  = ___ OR  ___ = ___   → b4 = ___
  G3 = A AND B  = ___ AND ___ = ___   → b3 = ___
  G4 = B XOR C  = ___ XOR ___ = ___   → b2 = ___
  G5 = A OR D   = ___ OR  ___ = ___   → b1 = ___
  G6 = NOT C    = NOT ___     = ___   → b0 = ___

  Binary:  b4 b3 b2 b1 b0 = ___ ___ ___ ___ ___
  Decimal: ___    Letter: ___
```

### Circuit 10 &ensp; (A=1, B=0, C=1)

```
  G1 = A OR B   = ___ OR  ___ = ___
  G2 = G1 AND C = ___ AND ___ = ___   → b4 = ___
  G3 = NOT A    = NOT ___     = ___
  G4 = G3 OR B  = ___ OR  ___ = ___   → b3 = ___
  G5 = A XOR C  = ___ XOR ___ = ___   → b2 = ___
  G6 = NOT B    = NOT ___     = ___   → b1 = ___
  G7 = B AND C  = ___ AND ___ = ___   → b0 = ___

  Binary:  b4 b3 b2 b1 b0 = ___ ___ ___ ___ ___
  Decimal: ___    Letter: ___
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
Circuit:    1     2     3     4     5     6     7     8     9     10

Binary:   _____  _____  _____  _____  _____  _____  _____  _____  _____  _____

Decimal:  ___    ___    ___    ___    ___    ___    ___    ___    ___    ___

Letter:   ___    ___    ___    ___    ___    ___    ___    ___    ___    ___
```

---

**Your answer** (10 letters): _ _ _ _ _ _ _ _ _ _

*You may find the Technology section helpful.*
