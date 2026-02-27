# [17] --- Chlorine

**10♦ The Broadcaster** · Language & Communication · T2

---

> The Broadcaster sends a signal through noise and distance and time. Some signals arrive clean. Some do not. This one has been waiting for you.

---

## The Puzzle

**Type:** Cipher Strip Decoder -- align two printed alphabets, discover the key, decode a message
**References:** codes/00-OVERVIEW.md, codes/08-HISTORICAL-CIPHERS.md

A message, forty letters long. Eight words. Encrypted with a polyalphabetic cipher -- the kind that uses a repeating keyword to shift each letter by a different amount.

```
    FZS  XYKME  NFRKNZIPT  XYXG  CLMPVW  QT  FOFIXIKLCPV
```

To decrypt it, you need two things: a tool and a key.

**The tool** is printed below. Two alphabet strips, one above the other. Lay a bookmark, a straightedge, or the edge of a sheet of paper vertically across both strips. Slide it until the **key letter** on the top strip aligns with **A** on the bottom strip. Now read down from each ciphertext letter on the top strip to find the plaintext letter on the bottom strip. Repeat for each letter of the message, advancing through the key.

If you have worked a Vigenere tableau before, the strips do the same job -- they are the tableau, one row at a time.

**The key.** The strips below are a poor man's version of a tool that was first built in Florence. The original was not a pair of strips but a pair of concentric discs -- one fixed, one rotating. The inventor called it *formula.* It was the first device in history to defeat frequency analysis, because it used not one shifted alphabet but many.

The first such disc was built more than three centuries before the telegraph. The encyclopedia names its inventor. His surname -- seven letters -- is your key.

---

## The Cipher Strips

Place a straight edge vertically across both strips. To set up for a key letter, slide until that key letter on the **outer strip** sits directly above **A** on the **inner strip**. Then for each ciphertext letter, find it on the outer strip and read the plaintext letter directly below it on the inner strip.

**Outer strip (ciphertext):**
```
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ A │ B │ C │ D │ E │ F │ G │ H │ I │ J │ K │ L │ M │ N │ O │ P │ Q │ R │ S │ T │ U │ V │ W │ X │ Y │ Z │
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
```

**Inner strip (plaintext) -- slide this one:**
```
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ A │ B │ C │ D │ E │ F │ G │ H │ I │ J │ K │ L │ M │ N │ O │ P │ Q │ R │ S │ T │ U │ V │ W │ X │ Y │ Z │
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
```

*Alternatively, use the full Vigenere tableau in `codes/08-HISTORICAL-CIPHERS.md`. Find the key letter's row, scan that row for the ciphertext letter, and read the column header.*

---

## Worksheet

### Step 1 -- Find the key

The puzzle text names the city, the century, and the device. The encyclopedia names the inventor.

```
Key (7 letters):  ___  ___  ___  ___  ___  ___  ___
```

### Step 2 -- Align key beneath ciphertext

The key repeats cyclically. Spaces in the ciphertext are not encrypted -- the key advances only on letters.

```
Cipher:  F   Z   S       X   Y   K   M   E       N   F   R   K   N   Z   I   P   T
Key:     __  __  __      __  __  __  __  __      __  __  __  __  __  __  __  __  __
Plain:   __  __  __      __  __  __  __  __      __  __  __  __  __  __  __  __  __

Cipher:  X   Y   X   G       C   L   M   P   V   W       Q   T
Key:     __  __  __  __      __  __  __  __  __  __      __  __
Plain:   __  __  __  __      __  __  __  __  __  __      __  __

Cipher:  F   O   F   I   X   I   K   L   C   P   V
Key:     __  __  __  __  __  __  __  __  __  __  __
Plain:   __  __  __  __  __  __  __  __  __  __  __
```

### Step 3 -- Decrypt each letter

For each position: set the strips so the key letter on the outer strip aligns with A on the inner strip. Find the ciphertext letter on the outer strip. Read the plaintext letter below it on the inner strip.

**Worked example** (position 1):

- Key letter: (first letter of your key)
- Set strips: slide inner strip until your key letter on outer aligns with A on inner
- Ciphertext letter: **F**
- Find **F** on the outer strip. Read what sits below it on the inner strip.
- Write the plaintext letter.

```
Pos   Cipher   Key    Plain
───   ──────   ───    ─────
 1      F       __      __
 2      Z       __      __
 3      S       __      __
         ── space ──
 4      X       __      __
 5      Y       __      __
 6      K       __      __
 7      M       __      __
 8      E       __      __
         ── space ──
 9      N       __      __
10      F       __      __
11      R       __      __
12      K       __      __
13      N       __      __
14      Z       __      __
15      I       __      __
16      P       __      __
17      T       __      __
         ── space ──
18      X       __      __
19      Y       __      __
20      X       __      __
21      G       __      __
         ── space ──
22      C       __      __
23      L       __      __
24      M       __      __
25      P       __      __
26      V       __      __
27      W       __      __
         ── space ──
28      Q       __      __
29      T       __      __
         ── space ──
30      F       __      __
31      O       __      __
32      F       __      __
33      I       __      __
34      X       __      __
35      I       __      __
36      K       __      __
37      L       __      __
38      C       __      __
39      P       __      __
40      V       __      __
```

### Step 4 -- Read the plaintext

```
___  ___  ___     ___  ___  ___  ___  ___     ___  ___  ___  ___  ___  ___  ___  ___  ___

___  ___  ___  ___     ___  ___  ___  ___  ___  ___     ___  ___

___  ___  ___  ___  ___  ___  ___  ___  ___  ___  ___
```

### Step 5 -- Extract the answer

The plaintext is an English sentence. The last word is your answer.

```
Answer:   ___  ___  ___  ___  ___  ___  ___  ___  ___  ___  ___
```

**Checkpoint:** The sentence describes a reputation that lasted three hundred years. If your plaintext reads as coherent English and the last word names that reputation, you have the right key.

---

**Your answer** (11 letters): _ _ _ _ _ _ _ _ _ _ _

*You may find the Language & Communication section helpful.*
