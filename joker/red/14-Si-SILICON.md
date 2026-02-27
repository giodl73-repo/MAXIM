# [14] --- Silicon

**K&#9824; The Sentinel** &middot; Computing &middot; &#9733; T1

---

> The Sentinel stands at the gate. Not every message is meant for every reader. This one is meant for you -- but you will have to earn it.

---

## The Puzzle

**Type:** Cipher Decryption -- decrypt a message using an algorithm from cryptography/
**References:** cryptography/00-OVERVIEW.md, cryptography/01-SYMMETRIC.md

An intercepted ciphertext. Twenty letters. Four words.

```
    LLR  TVFAPJ  MF  TTTSCAXUF
```

The encryption is older than AES, older than RSA, older than Turing. It is a polyalphabetic substitution cipher -- the kind that broke the monopoly of frequency analysis. The cryptography overview describes the arc from perfect secrecy to computational security, but this cipher predates both formalisms. It is the one Blaise de Vigenere's name is on, though Giovan Battista Bellaso invented it first.

To decrypt it, you need two things: the algorithm and the key.

**The algorithm.** A polyalphabetic substitution repeats a keyword beneath the plaintext. Each letter is shifted by the value of the key letter above it. To decrypt, reverse the shift. If you have never worked one by hand, the tableau below will get you there.

**The key.** Read the top of this page again. The one who guards the gate also guards the message. The key is eight letters long.

---

## The Vigenere Tableau

To encrypt: find the plaintext letter in the top row and the key letter in the left column. The intersection is the ciphertext letter.

To decrypt: find the key letter in the left column. Scan that row until you find the ciphertext letter. The column header is the plaintext letter.

```
     A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
  ┌────────────────────────────────────────────────────────────────────────────────────
A │  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
B │  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A
C │  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B
D │  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C
E │  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D
F │  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E
G │  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F
H │  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G
I │  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H
J │  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I
K │  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J
L │  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K
M │  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L
N │  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M
O │  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N
P │  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O
Q │  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P
R │  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q
S │  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R
T │  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S
U │  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T
V │  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U
W │  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V
X │  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W
Y │  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X
Z │  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y
```

---

## Worksheet

### Step 1 -- Identify the key

The card at the top of this page names an archetype. That archetype is the key.

```
Key (8 letters):  ___  ___  ___  ___  ___  ___  ___  ___
```

### Step 2 -- Write out the ciphertext and align the key

The key repeats cyclically beneath the ciphertext. Spaces are not encrypted -- the key advances only on letters.

```
Ciphertext:   L   L   R       T   V   F   A   P   J       M   F       T   T   T   S   C   A   X   U   F

Key:          __  __  __      __  __  __  __  __  __      __  __      __  __  __  __  __  __  __  __  __

Plaintext:    __  __  __      __  __  __  __  __  __      __  __      __  __  __  __  __  __  __  __  __
```

### Step 3 -- Decrypt each letter

For each position, find the key letter's row in the tableau. Scan that row until you find the ciphertext letter. Read the column header -- that is the plaintext letter.

**Worked example** (first letter):

- Ciphertext letter: **L**
- Key letter: (your first key letter -- go to that row in the tableau)
- Find **L** in that row. Read the column header above it.
- Write the plaintext letter.

Repeat for all 20 letters.

```
Position   Cipher   Key   Plaintext
────────   ──────   ───   ─────────
  1          L       __      __
  2          L       __      __
  3          R       __      __
             ─ space ─
  4          T       __      __
  5          V       __      __
  6          F       __      __
  7          A       __      __
  8          P       __      __
  9          J       __      __
             ─ space ─
 10          M       __      __
 11          F       __      __
             ─ space ─
 12          T       __      __
 13          T       __      __
 14          T       __      __
 15          S       __      __
 16          C       __      __
 17          A       __      __
 18          X       __      __
 19          U       __      __
 20          F       __      __
```

### Step 4 -- Read the plaintext

```
___  ___  ___     ___  ___  ___  ___  ___  ___     ___  ___     ___  ___  ___  ___  ___  ___  ___  ___  ___
```

### Step 5 -- Extract the answer

The plaintext is an English sentence. The final word is your answer.

```
Answer:   ___  ___  ___  ___  ___  ___  ___  ___  ___
```

---

**Your answer** (9 letters): _ _ _ _ _ _ _ _ _

*You may find the Computing and Cryptography sections helpful.*
