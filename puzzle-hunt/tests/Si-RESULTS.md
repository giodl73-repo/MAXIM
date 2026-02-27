# Puzzle Test: 14-Si-SILICON

**Puzzle:** [14] Silicon -- Vigenere Cipher Decryption (Computing / Cryptography)
**Card:** K of Spades -- The Sentinel
**Testers:** Wei-Hwa Huang, Jonathan Blow, Thomas Snyder
**Date:** 2026-02-27

---

## Sanitized Puzzle (as presented to testers)

The following was stripped before presenting to testers:
- Line 3: Removed `T1` tier marker and star rating
- Line 14: Removed `**References:**` line referencing cryptography/ files
- Lines containing `<!-- comments -->`: None found in original
- Line 150: Changed answer line to `**Your answer:** _______________`
- No "ALGORITHM" answer text, letter counts, "Panel votes", or tier markers present in puzzle body (clean)

---

> The Sentinel stands at the gate. Not every message is meant for every reader. This one is meant for you -- but you will have to earn it.

## The Puzzle

**Type:** Cipher Decryption -- decrypt a message using an algorithm from the encyclopedia

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
  +-------------------------------------------------------------------------------------
A |  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
B |  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A
C |  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B
...
S |  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R
...
Z |  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y
```

[Full 26x26 tableau provided as in original]

---

## Worksheet

### Step 1 -- Identify the key

The card at the top of this page names an archetype. That archetype is the key.

```
Key (8 letters):  ___  ___  ___  ___  ___  ___  ___  ___
```

### Step 2 -- Write out the ciphertext and align the key

```
Ciphertext:   L   L   R       T   V   F   A   P   J       M   F       T   T   T   S   C   A   X   U   F

Key:          __  __  __      __  __  __  __  __  __      __  __      __  __  __  __  __  __  __  __  __

Plaintext:    __  __  __      __  __  __  __  __  __      __  __      __  __  __  __  __  __  __  __  __
```

### Step 3 -- Decrypt each letter

[Position table with 20 rows as in original]

### Step 4 -- Read the plaintext

```
___  ___  ___     ___  ___  ___  ___  ___  ___     ___  ___     ___  ___  ___  ___  ___  ___  ___  ___  ___
```

### Step 5 -- Extract the answer

The plaintext is an English sentence. The final word is your answer.

**Your answer:** _______________

*You may find the Computing and Cryptography sections helpful.*

---

## Intended Solution

**Key identification:** The card header reads "The Sentinel." SENTINEL is 8 letters.

**Key alignment (cycling SENTINEL over 20 ciphertext letters):**

```
Ciphertext:  L   L   R   |   T   V   F   A   P   J   |   M   F   |   T   T   T   S   C   A   X   U   F
Key:         S   E   N   |   T   I   N   E   L   S   |   E   N   |   T   I   N   E   L   S   E   N   T
Plaintext:   T   H   E   |   A   N   S   W   E   R   |   I   S   |   A   L   G   O   R   I   T   H   M
```

**Decryption verification (letter by letter):**

| Pos | Cipher | Key | Key val | Cipher val | (C - K) mod 26 | Plain |
|-----|--------|-----|---------|------------|-----------------|-------|
| 1 | L | S | 18 | 11 | (11-18+26) mod 26 = 19 | T |
| 2 | L | E | 4 | 11 | (11-4) mod 26 = 7 | H |
| 3 | R | N | 13 | 17 | (17-13) mod 26 = 4 | E |
| 4 | T | T | 19 | 19 | (19-19) mod 26 = 0 | A |
| 5 | V | I | 8 | 21 | (21-8) mod 26 = 13 | N |
| 6 | F | N | 13 | 5 | (5-13+26) mod 26 = 18 | S |
| 7 | A | E | 4 | 0 | (0-4+26) mod 26 = 22 | W |
| 8 | P | L | 11 | 15 | (15-11) mod 26 = 4 | E |
| 9 | J | S | 18 | 9 | (9-18+26) mod 26 = 17 | R |
| 10 | M | E | 4 | 12 | (12-4) mod 26 = 8 | I |
| 11 | F | N | 13 | 5 | (5-13+26) mod 26 = 18 | S |
| 12 | T | T | 19 | 19 | (19-19) mod 26 = 0 | A |
| 13 | T | I | 8 | 19 | (19-8) mod 26 = 11 | L |
| 14 | T | N | 13 | 19 | (19-13) mod 26 = 6 | G |
| 15 | S | E | 4 | 18 | (18-4) mod 26 = 14 | O |
| 16 | C | L | 11 | 2 | (2-11+26) mod 26 = 17 | R |
| 17 | A | S | 18 | 0 | (0-18+26) mod 26 = 8 | I |
| 18 | X | E | 4 | 23 | (23-4) mod 26 = 19 | T |
| 19 | U | N | 13 | 20 | (20-13) mod 26 = 7 | H |
| 20 | F | T | 19 | 5 | (5-19+26) mod 26 = 12 | M |

**Plaintext:** THE ANSWER IS ALGORITHM

**Answer:** ALGORITHM (9 letters)

---

# Test: Silicon -- Wei-Hwa Huang

**Lens:** Deductive rigor -- is the key discovery clean?

## Solve Attempt

Wei-Hwa reads the puzzle text carefully. He immediately identifies the cipher type from the description: "polyalphabetic substitution... Blaise de Vigenere... Giovan Battista Bellaso." Standard Vigenere. The algorithm is explicitly given: the tableau is provided, the decryption instructions are spelled out. No mystery about what to do. The only question is the key.

**Key identification:**

"The card at the top of this page names an archetype. That archetype is the key."

He reads the header: "The Sentinel." The key is 8 letters long. SENTINEL is 8 letters.

Wei-Hwa pauses. "This is not a puzzle. This is an instruction. The key is SENTINEL. It says so at the top of the page. The clue says 'read the top of this page again.' I read it. The archetype is The Sentinel. The key is SENTINEL. There is no deduction here -- there is only reading comprehension."

He briefly considers whether the key might be something else: GUARDIAN? (8 letters, and the flavor text says "the one who guards the gate.") He checks: GUARDIAN is also 8 letters. Two candidates.

He tries SENTINEL first (the archetype name stated on the card). He works through the first three letters:

- L with S: find row S, scan for L. Column header = T.
- L with E: find row E, scan for L. Column header = H.
- R with N: find row N, scan for R. Column header = E.

"THE..." -- English word start. He continues through position 9: "THE ANSWER" -- this confirms SENTINEL is correct. GUARDIAN would produce gibberish at position 1 (L with G = F, not a promising start for a 3-letter English word).

He completes the decryption mechanically:

```
THE ANSWER IS ALGORITHM
```

"ALGORITHM. The answer is literally 'the answer is ALGORITHM.' The plaintext tells you which word to extract. That is clean -- no ambiguity about the extraction step. But the solving process was: read the page, notice the word SENTINEL, apply a known algorithm for 20 letters. Every step was mechanical."

**Total time:** ~8 minutes. Mostly tableau lookups.

## Answer

**ALGORITHM**

## Scores

| Dimension | Score (1-5) | Notes |
|-----------|-------------|-------|
| Clarity | 5 | The instructions are explicit. The algorithm is named, the tableau is provided, the decryption procedure is explained with a worked example for the first letter. The key clue is unambiguous: "the card names an archetype" and "the key is eight letters long." No parsing difficulty whatsoever. |
| Solvability | 5 | Uniquely solvable. The key is stated on the page. The algorithm is provided. The tableau is provided. The decryption is mechanical. There is exactly one path: identify key, apply cipher, read plaintext. A solver who follows the instructions cannot fail. |
| Elegance | 2 | The puzzle has one step: identify the key (read the page header) and one execution: apply Vigenere decryption 20 times. There is no structural depth, no interlock, no constraint propagation. The cipher is a lookup table operation repeated 20 times. The thematic wrapper (Sentinel guards the message, the key is the Sentinel's name) is clean but does not create puzzle logic. It is a decryption exercise, not a deduction puzzle. |
| Reading Reward | 3 | The solver learns what a Vigenere cipher is, if they did not know. The encyclopedia's cryptography section covers the arc from Caesar to polyalphabetic substitution to modern symmetric cryptography. The puzzle orients the solver in the history of cryptography -- pre-computational, pre-Turing, pre-Shannon. But the encyclopedia access is optional: the tableau and instructions are self-contained. A solver never needs to open cryptography/00-OVERVIEW.md or 01-SYMMETRIC.md. The reference to "perfect secrecy" and "computational security" is flavor, not functional. |
| Fun | 3 | There is a modest satisfaction in working a Vigenere cipher by hand. The tableau lookup is tactile -- find the row, scan for the letter, read the header. The moment when "THE ANSWER IS" emerges from gibberish has a mild decryption thrill. But twenty lookups is mechanical. After the third or fourth letter, the solver is executing a procedure, not solving a puzzle. The answer ALGORITHM has a nice self-referential quality: you used an algorithm to find the word ALGORITHM. |
| Confirmation | 5 | THE ANSWER IS ALGORITHM is an English sentence. The plaintext explicitly labels the answer word. There is zero ambiguity about extraction. The 9-letter blank matches ALGORITHM. The sentence structure confirms the decryption is correct long before position 20. By position 12 ("THE ANSWER IS A..."), the solver can guess ALGORITHM and verify the remaining 8 letters as confirmation. |

| **Total** | **23/30** | |

## Issues

1. **The key discovery is trivially easy.** The puzzle says "the card names an archetype" and the card says "The Sentinel." The key is SENTINEL. This is not deduction -- it is reading. A genuine puzzle would require the solver to derive the key from indirect evidence: a pattern, a constraint, a hidden message. Here the key is stated in plain text. The puzzle fails my core test: "Does the intended solution stand out from unintended shortcuts?" There are no shortcuts because there is no deduction to shortcut. The intended path IS the shortcut.

2. **GUARDIAN is a plausible alternative key.** The flavor text says "the one who guards the gate also guards the message." GUARDIAN (8 letters) is a natural interpretation. The puzzle resolves this by fitting the archetype name from the card header, not the flavor text -- but a solver who tries GUARDIAN first will waste time on 3-4 letters of gibberish before switching. The ambiguity is low (trying SENTINEL second takes ~30 seconds) but it exists, and it is gratuitous. The puzzle should either eliminate GUARDIAN (make the key 7 letters, not 8 -- but GUARDIAN is also 8) or strengthen the archetype clue to be unmistakable.

3. **No deduction layer.** The puzzle has zero logic gates. Compare to Sodium (logic grid with 11 interlocking clues) or Oxygen (30 object identifications + coordinate plotting + letter recognition). Silicon is: read key, apply algorithm, read plaintext. The worksheet provides all the structure. The solver fills in blanks.

## Principle Checks

| Principle | Pass/Fail | Notes |
|-----------|-----------|-------|
| The Riven Standard | PARTIAL | The puzzle IS cryptography -- you are decrypting a cipher. But the relationship is shallow: you are executing a historical cipher, not understanding modern cryptographic principles. The encyclopedia's content on IND-CPA, security games, reduction proofs, AES internals -- none of it is needed. The Vigenere cipher is pre-modern; the encyclopedia is modern. |
| Solving = Proving Understanding | FAIL | Solving proves you can follow a lookup table. It does not prove understanding of cryptography. A solver who has never read the cryptography section can solve this puzzle identically to one who has read every page. |
| The Book Test | PASS | Pencil, book, no other tools. The tableau is provided. |
| Blame the Player | PASS | Every element is fair. The key is stated. The algorithm is given. If the solver fails, they misread the page. |
| No Over-Scaffolding | FAIL | The worksheet does ALL the work. Step 1: identify key. Step 2: align key. Step 3: decrypt each letter (with worked example). Step 4: read plaintext. Step 5: extract answer. The solver is never asked to figure out what to do -- only to execute what is spelled out. Remove the worksheet and the solver would still know what to do (the algorithm description is clear), so the worksheet is redundant scaffolding. |
| Surprise the Answer | PARTIAL | ALGORITHM is not the most predictable answer for a cryptography puzzle (ENCRYPTION, CIPHER, or CRYPTOGRAPHY would be more obvious). But it is not surprising either -- the puzzle is about applying an algorithm, and the answer is ALGORITHM. Self-referential, not surprising. |
| One Aha | FAIL | Zero ahas. The key is given. The algorithm is given. The extraction is spelled out. There is no moment of insight. |
| Reading Reward >= 4 | FAIL | Score: 3. The solver does not need the encyclopedia. The puzzle is self-contained. The cryptography references are flavor text. |
| Snyder's Computer Test | FAIL | A 10-line Python script solves this puzzle: `key = "SENTINEL"; cipher = "LLRTVFAPJMFTTTSCAXUF"; print("".join(chr((ord(c)-ord(k))%26+65) for c,k in zip(cipher, itertools.cycle(key))))`. No deduction layer. |

## Suggested Fixes

1. **Hide the key.** Do not state the archetype name on the card header. Instead, embed the key in a secondary puzzle: an acrostic, a pattern in the flavor text, a sequence derived from the encyclopedia. The key discovery should BE the aha moment. For example: the Sentinel's eight qualities (described in flavor text) each start with S-E-N-T-I-N-E-L. The solver must notice the acrostic. Now the key is discovered, not read.

2. **Require encyclopedia engagement.** Instead of providing the tableau, tell the solver to find the algorithm in the cryptography section. The overview describes "polyalphabetic substitution" and the historical arc. The solver must read the encyclopedia to understand the Vigenere mechanism. This converts a self-contained exercise into an encyclopedia-driven puzzle.

3. **Add a deduction layer.** Instead of giving the key length, give the solver a clue that requires deduction. "The key length equals the number of cards in a suit minus the number of face cards minus the number of aces." (13 - 3 - 1 = 9... that does not work for 8.) Better: embed the key length in the ciphertext structure or the card's periodic table position (Si = 14 -- could relate to the key somehow).

---

# Test: Silicon -- Jonathan Blow

**Lens:** Epiphany -- is the "archetype name IS the key" aha genuine?

## Solve Attempt

Blow reads the Sentinel's flavor text first: "Not every message is meant for every reader. This one is meant for you -- but you will have to earn it." He finds the voice appropriate -- quiet, serious, gatekeeping. The atmosphere is right for a cipher puzzle.

He reads the puzzle description. Polyalphabetic substitution. Vigenere. The algorithm is named and explained. The tableau is provided.

"So the algorithm is given. The cipher type is given. The tableau is given. The decryption procedure is explained. There is even a worked example for the first letter. What, exactly, does the solver have to figure out?"

He reads the key clue: "Read the top of this page again. The one who guards the gate also guards the message. The key is eight letters long."

He looks at the top of the page: "The Sentinel." He counts: S-E-N-T-I-N-E-L. Eight letters.

"That is the key. SENTINEL. And I know this because the puzzle told me to read the top of the page, and the key length confirms it. There is no epiphany here. There is no moment where I see something I was not supposed to see, no moment where my understanding of the system shifts. The puzzle TOLD me where the key was and how long it was. I just had to look."

He pauses. "Compare this to The Witness. In The Witness, you encounter a panel with unfamiliar symbols. You do not know the rules. You try things. You fail. You notice a pattern. You form a hypothesis. You test it. It works. THAT is epiphany -- the rules were there all along, but you had to discover them through interaction. Here, the rules are stated, the key is pointed at, the tableau is provided, the procedure is described. There is nothing to discover."

**Decryption:**

Blow works through the cipher quickly using the arithmetic method rather than the tableau (he is a programmer; modular arithmetic is faster than table lookup):

```
L(11) - S(18) = -7 mod 26 = 19 = T
L(11) - E(4) = 7 = H
R(17) - N(13) = 4 = E
```

"THE. Already confirmed."

He finishes: THE ANSWER IS ALGORITHM.

"ALGORITHM. The answer is the word for a step-by-step procedure. I just followed a step-by-step procedure to find it. Is that self-referential irony? Or is it confirming that the puzzle is, in fact, just an algorithm execution?"

**The information content question:**

"Surprise is the same thing as information content. If you send someone a message and it says exactly what they expected, there is no information. By position 12, the plaintext reads 'THE ANSWER IS A...' and I am already guessing ALGORITHM. The remaining 8 letters confirm my guess. The surprise content of those 8 letters is near zero because the sentence structure + topic constrain the answer almost completely. The only information in this puzzle is: (1) the key is SENTINEL, which took 5 seconds to discover, and (2) the answer is ALGORITHM rather than, say, ANTIQUITY or ANONYMOUS. The total information content is very low."

## Answer

**ALGORITHM**

## Scores

| Dimension | Score (1-5) | Notes |
|-----------|-------------|-------|
| Clarity | 5 | Crystal clear. The instructions leave nothing to interpretation. Algorithm named, tableau provided, key location described, decryption procedure explained with worked example. A solver cannot be confused about what to do. |
| Solvability | 5 | Uniquely and trivially solvable. The key is on the page. The cipher is standard. The tableau handles all computation. The sentence structure of the plaintext provides early confirmation. |
| Elegance | 2 | The thematic wrapper is apt: the Sentinel guards a message, the key is the Sentinel's name, you must decrypt to pass the gate. But the wrapper is all there is. The mechanism (Vigenere decryption) is a single operation repeated 20 times with no variation, no constraint, no discovery. A Vigenere cipher is elegant as a historical invention; it is not elegant as a puzzle mechanism in 2026. The solver is doing arithmetic, not thinking. |
| Reading Reward | 2 | The puzzle references the cryptography encyclopedia ("the cryptography overview describes the arc from perfect secrecy to computational security") but does not require reading it. The Vigenere cipher is fully explained within the puzzle itself. The cryptography section covers AES internals, IND-CPA, AEAD, reduction proofs -- none of which is relevant. The solver learns what a Vigenere cipher is, which is a 16th-century technique. The encyclopedia covers 21st-century cryptography. The gap is vast. |
| Fun | 3 | Working a cipher by hand has a small, real pleasure. The moment when gibberish becomes English ("T...H...E...") is satisfying the way any decryption is satisfying. But the satisfaction peaks at position 3 and the remaining 17 lookups are duty. The self-referential answer (ALGORITHM from an algorithm) produces a wry smile, not a gasp. |
| Confirmation | 5 | "THE ANSWER IS ALGORITHM" is maximally self-confirming. The sentence literally labels the answer. The 9-letter blank matches. The solver cannot be uncertain. |

| **Total** | **22/30** | |

## Issues

1. **Zero epiphany.** The puzzle has no moment of genuine insight. Every element is given: algorithm, key location, tableau, procedure, worked example. The solver's job is execution, not discovery. In Witness terms, this is a panel where the rules are written on the wall in plain text. There is nothing to learn by solving it -- only time to spend.

2. **The puzzle makes you FEEL smart, not BE smart.** Completing a Vigenere decryption by hand feels like cryptographic work. But it is not. It is looking up values in a table 20 times. The solver who finishes thinks "I decrypted a cipher" but has not engaged with any idea that matters -- not the distinction between polyalphabetic and monoalphabetic substitution (which is mentioned but not tested), not the concept of key periodicity (which is the Vigenere cipher's actual weakness), not the relationship between historical and modern cryptography. The puzzle flatters rather than teaches.

3. **The plaintext structure spoils the answer early.** "THE ANSWER IS ..." by position 12, the solver knows the sentence structure. The remaining 8 letters carry almost no information because ALGORITHM is highly constrained by context (a cryptography puzzle where you applied an algorithm). A plaintext like "ALL GATES YIELD TO THE ALGORITHM" would delay the answer word and add thematic texture. Or better: a plaintext that is itself a clue to something deeper, not a self-labeling sentence.

4. **No connection to the encyclopedia's actual content.** The cryptography section covers AES, GCM, ChaCha20, IND-CPA, reduction proofs, post-quantum migration. The puzzle uses a 16th-century cipher that the section does not even describe (it is too primitive for the encyclopedia's scope). The puzzle is set IN cryptography but does not engage WITH cryptography. The Riven standard asks: would a cryptographer recognize their work? A cryptographer would recognize Vigenere as a historical curiosity, not as their discipline.

## Principle Checks

| Principle | Pass/Fail | Notes |
|-----------|-----------|-------|
| The Riven Standard | FAIL | A cryptographer would recognize Vigenere but would not consider this puzzle "what cryptography does." Modern cryptography is about security definitions, hardness assumptions, and protocol composition. Vigenere is a museum piece -- interesting historically but not representative of the field. |
| Solving = Proving Understanding | FAIL | Solving proves the solver can execute a lookup table operation. It does not prove understanding of any cryptographic concept. The solver learns nothing about why Vigenere is broken (key periodicity, Kasiski examination, Friedman test) or how modern ciphers address its weaknesses. |
| No Over-Scaffolding | FAIL | The worksheet is a paint-by-numbers guide. Every step is spelled out. The worked example removes any remaining friction. This is a tutorial, not a puzzle. |
| Surprise the Answer | PARTIAL | ALGORITHM is not the most predictable word (CIPHER, ENCRYPTION would be worse). But the sentence "THE ANSWER IS ALGORITHM" eliminates surprise by position 12. The solver is not surprised by the answer; they are confirming what they already expect. |
| One Aha | FAIL | Zero ahas. The key is read, not discovered. The algorithm is given, not deduced. |
| The Dinner Party Test | FAIL | "I decrypted a Vigenere cipher where the key was written at the top of the page" is not a story anyone tells at dinner. |

## Suggested Fixes

1. **Make the key discovery the epiphany.** The key should not be readable on the page. It should be discoverable through a pattern that requires understanding the encyclopedia. Example: "The key is the name of the operation that makes AES resist linear cryptanalysis" -- the answer is SUBBYTES (8 letters). Now the solver must read the cryptography section, understand AES round operations, identify SubBytes as the nonlinear layer, and use it as the key. The encyclopedia engagement becomes functional, not decorative.

2. **Make the plaintext teach something.** Instead of "THE ANSWER IS ALGORITHM," use a plaintext that itself requires cryptographic knowledge to interpret: "THE SBOX GUARDS AGAINST LINEAR PATHS" with SBOX as the answer (or a variant). Now the solver learns what an S-box does by decrypting a sentence about it.

3. **Remove the tableau.** Tell the solver the algorithm exists in the encyclopedia. Let them find the Vigenere mechanism by reading about polyalphabetic substitution in context. The discovery of HOW to decrypt becomes part of the puzzle, not a given.

---

# Test: Silicon -- Thomas Snyder

**Lens:** Craftsmanship -- is the Vigenere decryption hand-solvable and elegant?

## Solve Attempt

Thomas assesses the puzzle's construction before solving. He reads the full page, counts the elements, evaluates the structure.

**Structural inventory:**

- One ciphertext (20 letters, 4 words)
- One key clue (archetype name, 8 letters)
- One provided tableau (26x26)
- One worksheet (5 steps, fully scaffolded)
- One worked example
- One extraction rule (final word of plaintext)

"Every element is provided. The puzzle is: identify key, execute decryption, extract answer. There is no ambiguity at any step. The worksheet guides the solver through every micro-operation. This is construction designed to guarantee completion, not to challenge."

**Key identification:**

The card says "The Sentinel." The clue says "The card names an archetype. That archetype is the key." Thomas writes SENTINEL immediately.

"The key is handed to the solver. In a well-crafted cipher puzzle, the key should be the reward of a deduction. Here it is the label on the card. The construction equivalent: imagine a Sudoku puzzle where the first row is pre-filled with 1-2-3-4-5-6-7-8-9. You can still solve it, but the constructor did all the interesting work for you."

**Decryption:**

Thomas works the tableau by hand, using the prescribed method: find key letter row, scan for ciphertext letter, read column header.

Position 1: Row S. Scan for L. Column header: T.
Position 2: Row E. Scan for L. Column header: H.
Position 3: Row N. Scan for R. Column header: E.

"THE. Three letters and I have a common English word. This is going to be a sentence."

He works efficiently through all 20 positions:

```
T-H-E  A-N-S-W-E-R  I-S  A-L-G-O-R-I-T-H-M
```

"THE ANSWER IS ALGORITHM. The plaintext is a meta-sentence that labels its own answer. Clean extraction, but it means the puzzle has no extraction puzzle -- the plaintext tells you what to write."

**Craftsmanship evaluation:**

Thomas examines the construction quality of the cipher itself:

"The ciphertext LLR TVFAPJ MF TTTSCAXUF has 20 letters in a 3-6-2-9 pattern. The key SENTINEL has 8 letters. The key cycles 2.5 times over 20 letters. This means some key letters encrypt more plaintext letters than others, but since the plaintext is a natural English sentence (not a constructed pattern), there is no exploitable structure in the ciphertext.

"However -- the ciphertext contains TTT at positions 12-13-14, which decrypt to ALG. The three consecutive identical ciphertext letters arise because A(0)+T(19)=T, L(11)+I(8)=T, G(6)+N(13)=T. This is a coincidence, not a construction flaw -- three different plaintext-key pairs happen to produce the same ciphertext letter. But a solver who notices TTT might wonder if it encodes AAA or III (common repeated letters), which could give them a foothold. This is actually a minor unintended shortcut: TTT with key T-I-N gives A-L-G, and a solver who guesses the key locally could crack this segment independently.

"More importantly: the puzzle does not USE the cipher in any interesting way. A good cipher puzzle would exploit properties of the Vigenere mechanism -- key periodicity, letter frequency, known-plaintext attacks -- as part of the solving process. Here, the solver is given everything and asked to execute. The cipher is a black box: input key + ciphertext, output plaintext. The mechanism is opaque -- the solver does not need to understand WHY Vigenere works, only HOW to operate the tableau."

**Hand-solvability assessment:**

"Is this hand-solvable? Yes, completely. The tableau is provided. The arithmetic is modular subtraction mod 26, which the tableau performs visually. A careful solver can complete all 20 lookups in 10-15 minutes. There are no traps, no ambiguous letters, no tricky modular arithmetic edge cases. The construction is clean in the sense that it produces no errors -- but clean is not the same as elegant."

## Answer

**ALGORITHM**

## Scores

| Dimension | Score (1-5) | Notes |
|-----------|-------------|-------|
| Clarity | 5 | Unimprovable. Every instruction is explicit. The key is identified. The algorithm is named. The tableau is provided. The worked example demonstrates the first step. The extraction rule is a natural English sentence. |
| Solvability | 5 | A solver who reads the page and follows the instructions will arrive at the answer with certainty. There is no step that requires guessing, inference, or creativity. The puzzle is an exercise, and exercises are always solvable. |
| Elegance | 1 | This is the puzzle's fundamental weakness. There is no hand-crafted solving path. There is no intentional difficulty curve. There is no moment where the solver must make a choice that requires insight. The puzzle is: read the key from the page, look up 20 values in a table, read the English sentence that results. A computer generates this puzzle trivially: pick a key, pick a plaintext, encrypt. The construction shows no constructor's hand. Compare to a hand-crafted Sudoku where the opening deductions are choreographed, where the constructor placed each given to create a specific solving experience. This puzzle has no choreography. |
| Reading Reward | 2 | The solver learns about the Vigenere cipher -- a historical curiosity from the 16th century. The puzzle mentions the arc from perfect secrecy to computational security but does not engage with it. The encyclopedia's cryptography section covers AES, GCM, security games, lattice cryptography -- material that is orders of magnitude more relevant to the learner profile than a Vigenere cipher. The reading reward is: "I now know how a Vigenere cipher works." This is mildly interesting but not connected to the encyclopedia's actual curriculum. |
| Fun | 3 | Hand-decryption has a tactile, almost meditative quality. The row-scan-column procedure is satisfying in the way that any systematic table operation is satisfying. The emergence of English from gibberish provides a small thrill. But the fun plateaus after position 3 and the remaining 17 positions are rote. The self-referential answer (ALGORITHM from an algorithm) is a mild wink, not a reward. |
| Confirmation | 5 | "THE ANSWER IS ALGORITHM" is the strongest possible confirmation. The sentence is unambiguous. The word length matches the blank. The solver cannot doubt the answer. |

| **Total** | **21/30** | |

## Issues

1. **A computer generates this puzzle.** Pick any 8-letter word as a key. Pick any English sentence as plaintext. Encrypt with Vigenere. Done. This is a 5-line script. There is no hand-crafted element in the cipher construction. The ciphertext LLR TVFAPJ MF TTTSCAXUF was not designed by a human who thought about the solving experience -- it was produced by mechanical encryption of a plaintext. The constructor's choices were: (a) use SENTINEL as the key (dictated by the card name), (b) use "THE ANSWER IS ALGORITHM" as the plaintext (a meta-sentence). Neither choice reflects craftsmanship in the puzzle-mechanical sense.

2. **No intentional solving path.** In a crafted cipher puzzle, the constructor might: use a known-plaintext crib ("the" appears in nearly all English), exploit key periodicity to create a secondary deduction, embed a pattern in the ciphertext that hints at the key length, or structure the plaintext so that partial decryption reveals meaningful fragments that guide further solving. None of this happens here. The solving path is: start at position 1, proceed to position 20.

3. **The worksheet is over-scaffolded.** Step 1: identify key. Step 2: align key. Step 3: decrypt (with worked example). Step 4: read plaintext. Step 5: extract. Every cognitive step is pre-chewed. Remove the worksheet and the puzzle improves -- the solver must figure out the procedure themselves, which is at least a small challenge.

4. **Thematic mismatch between puzzle and encyclopedia.** The Sentinel guards the Computing section. The cryptography subsection covers AES, GCM, SHA-3, Argon2id, post-quantum migration. The puzzle uses a 16th-century cipher that the encyclopedia implicitly dismisses -- the overview describes the historical arc from monoalphabetic to polyalphabetic substitution in two sentences before moving to the real content. The puzzle is set in the wrong century for its section.

## Principle Checks

| Principle | Pass/Fail | Notes |
|-----------|-----------|-------|
| The Riven Standard | FAIL | Vigenere is to modern cryptography what an abacus is to computing. The section covers AES-GCM, IND-CPA, reduction proofs, post-quantum lattice assumptions. The puzzle uses a cipher that was broken in the 19th century. A cryptographer would not recognize this as their field. |
| No Over-Scaffolding | FAIL | The worksheet is a paint-by-numbers kit. The worked example removes the last shred of discovery. |
| One Aha | FAIL | Zero ahas. Everything is given. |
| Snyder's Computer Test | FAIL | `from itertools import cycle; key="SENTINEL"; ct="LLRTVFAPJMFTTTSCAXUF"; print("".join(chr((ord(c)-ord(k))%26+65) for c,k in zip(ct,cycle(key))))` -- 2 lines of Python. |
| Interlock, Not Independence | N/A | Single-mechanism puzzle; no clues to interlock. |
| The Dinner Party Test | FAIL | "I looked up 20 letters in a table" is not a dinner story. |

## Suggested Fixes

1. **Make the key the puzzle.** Hide SENTINEL across eight separate clues or constraints that each require encyclopedia knowledge to resolve. The solver assembles the key letter by letter from deductions about the cryptography section. Example: "The first letter of the key is the initial of the function that AES applies to each byte for confusion" (SubBytes -> S). Now the key construction IS the puzzle, and the Vigenere decryption is the payoff.

2. **Use the cipher's historical vulnerability as a puzzle mechanic.** Give the solver a longer ciphertext (40+ letters) with NO key. Tell them the cipher is Vigenere and the key is 8 letters. The solver must use Kasiski examination (finding repeated trigrams to determine key length) and frequency analysis within each key position to recover the key. THIS is what a cryptographer does. The encyclopedia's discussion of breaking classical ciphers becomes functional.

3. **Remove the worksheet.** Let the solver figure out the procedure from the algorithm description and the tableau alone. The worksheet adds convenience but removes the last potential challenge.

4. **Connect the plaintext to the encyclopedia.** Instead of the meta-sentence "THE ANSWER IS ALGORITHM," use a plaintext that teaches a real cryptographic concept: "CONFUSION AND DIFFUSION GUARD EVERY BLOCK" with BLOCK as the answer. Now the solver encounters Shannon's two principles (covered in the encyclopedia) through the act of decryption.

---

# Synthesis

## Score Summary

| Dimension | Huang | Blow | Snyder | Average |
|-----------|-------|------|--------|---------|
| Clarity | 5 | 5 | 5 | **5.0** |
| Solvability | 5 | 5 | 5 | **5.0** |
| Elegance | 2 | 2 | 1 | **1.7** |
| Reading Reward | 3 | 2 | 2 | **2.3** |
| Fun | 3 | 3 | 3 | **3.0** |
| Confirmation | 5 | 5 | 5 | **5.0** |
| **Total** | **23** | **22** | **21** | **22.0/30** |

## Consensus Issues

1. **Zero ahas (all three, unanimous).** The key is stated on the page. The algorithm is provided. The tableau is provided. The worksheet guides every step. There is no moment of discovery, insight, or epiphany. All three testers identify this as the fundamental problem: the puzzle is an exercise, not a puzzle.

2. **No engagement with the encyclopedia (all three).** The cryptography section covers AES internals, security games, reduction proofs, post-quantum migration -- sophisticated modern content for a reader with an MIT TCS background. The puzzle uses a 16th-century cipher that the encyclopedia barely mentions. The solver never needs to open any encyclopedia file. Reading Reward scores: 3, 2, 2 (average 2.3 -- below the >= 4 threshold).

3. **Over-scaffolded (all three).** The worksheet provides step-by-step instructions, a worked example, and pre-formatted blanks for every position. The solver fills in a form rather than solving a puzzle. All three flag the No Over-Scaffolding principle as violated.

4. **Snyder's Computer Test fails (Huang, Snyder explicit; Blow implicit).** The puzzle is solvable in 2 lines of Python. There is no deduction layer, no judgment call, no insight required. The cipher is a mechanical transformation.

5. **Thematic mismatch (Blow, Snyder).** Vigenere is a museum piece. The Sentinel guards the Computing section, which covers modern cryptographic engineering. The puzzle operates in the wrong century. A practitioner of the field (Riven Standard) would not recognize their discipline.

## Consensus Strengths

1. **Perfect clarity (all three, unanimous 5/5).** The puzzle is impeccably clear. Instructions are explicit, the algorithm is named, the tableau is provided, the extraction is labeled. No solver will be confused about what to do.

2. **Perfect confirmation (all three, unanimous 5/5).** "THE ANSWER IS ALGORITHM" is the strongest possible confirmation mechanism. The sentence labels the answer. The word length matches. The English grammar confirms the decryption long before it is complete.

3. **Thematic wrapper is apt.** The Sentinel guards a message. The key is the Sentinel's name. The solver must "earn" access by decrypting. The flavor text creates appropriate atmosphere. The card identity system is working -- the archetype name IS functional (it is the key). This is a strength of the card system, even though the puzzle underuses it.

4. **Correct and fair.** No errors in the ciphertext. The key produces valid English. The encryption is standard Vigenere. The Bellaso/Vigenere attribution is historically accurate. Every factual claim is verifiable.

## Verdict

### REVISE

**Score: 22.0/30 -- below passing threshold.**

The puzzle is mechanically correct, perfectly clear, and completely fair. But it is not a puzzle in any meaningful sense. It is a cipher exercise with the key written on the page. The solver executes 20 tableau lookups and reads an English sentence. There is no aha moment, no encyclopedia engagement, no deduction, no discovery.

The core idea -- "the archetype name is the Vigenere key" -- is elegant as a card-identity-system concept. The Sentinel guards a message; the Sentinel's name unlocks it. This is a good structural idea trapped in a bad puzzle implementation. The fix is not to change the concept but to make the solver EARN the key through deduction that engages the cryptography encyclopedia.

### Required Fixes (before publication)

1. **Make the key discovery non-trivial.** The key SENTINEL should not be readable from the card header. Either: (a) remove the archetype name from the visible page and let the solver deduce it from properties described in the flavor text + encyclopedia, or (b) keep the archetype name visible but use a DIFFERENT key that must be derived from cryptographic content (e.g., the key is a concept from the encyclopedia that the flavor text hints at).

2. **Require encyclopedia engagement.** The solver must read the cryptography section to solve the puzzle. Options: hide the algorithm (let them find Vigenere in the encyclopedia), hide the key (derivable from cryptographic concepts), or use a plaintext that requires cryptographic knowledge to interpret.

3. **Remove or reduce the worksheet.** The current worksheet is a tutorial. At minimum: remove the worked example, remove the step-by-step instructions, keep only the blank alignment grid. Let the solver figure out the procedure from the algorithm description.

### Recommended Fixes (polish)

4. **Change the plaintext.** "THE ANSWER IS ALGORITHM" is meta and self-labeling. Use a plaintext that teaches a cryptographic concept, creating reading reward even in the decryption output. The sentence should not label the answer -- the solver should extract it from context.

5. **Add a secondary deduction layer.** After decryption, require the solver to connect the plaintext to a specific concept in the encyclopedia. The extraction should involve understanding, not just reading the last word of a sentence.

6. **Consider the GUARDIAN ambiguity.** Either make the key unambiguously SENTINEL (not derivable from "guards the gate") or use a mechanism where GUARDIAN demonstrably fails within 1-2 letters.
