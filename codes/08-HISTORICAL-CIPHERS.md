# Historical Ciphers — From Caesar to Enigma

## The Big Picture

Classical cryptography is the prehistory of modern cryptographic theory. The arc runs from simple monoalphabetic substitution (Caesar, ~100 BCE) through polyalphabetic ciphers (Vigenère, 1553), mechanical devices (Enigma, 1920s), to Shannon's 1949 mathematical framework that birthed modern cryptography. For modern crypto (AES, RSA, ECC, TLS), see `computing/25-SECURITY.md`.

```
┌──────────────────────────────────────────────────────────────────┐
│           CLASSICAL CIPHER EVOLUTION                              │
│                                                                  │
│  ~100 BCE  Caesar cipher         monoalphabetic substitution     │
│  ~600 BCE  Atbash               Hebrew mirror alphabet           │
│  1467      Alberti cipher        first polyalphabetic (disc)     │
│  1553      Vigenère              keyword polyalphabetic          │
│  1854      Playfair              digraph substitution            │
│  1918      ADFGVX                WWI German field cipher         │
│  1917      Vernam (OTP)          one-time pad (provably secure)  │
│  1918      Enigma concept        first mechanical cipher machine  │
│  1920s     Enigma production     electromechanical, naval/army   │
│  1941–45   Bletchley Park breaks Enigma, Lorenz                  │
│  1949      Shannon: "Communication Theory of Secrecy Systems"    │
│            → mathematical proof OTP is perfectly secure          │
│            → framework for all modern cryptography               │
│  1977      DES (first public standard cipher)                    │
│  2001      AES (current standard) → see computing/25-SECURITY.md│
└──────────────────────────────────────────────────────────────────┘
```

---

## Caesar Cipher (Monoalphabetic Shift)

The simplest cipher: shift every letter by a fixed amount.

```
┌──────────────────────────────────────────────────────────────────┐
│                    CAESAR CIPHER (ROT-N)                          │
│                                                                  │
│  ROT-3 (Caesar's alleged preference):                            │
│  Plaintext:   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z│
│  Ciphertext:  D E F G H I J K L M N O P Q R S T U V W X Y Z A B C│
│                                                                  │
│  Mathematical form:                                              │
│  E(x) = (x + n) mod 26    (encryption, shift right by n)         │
│  D(y) = (y - n) mod 26    (decryption, shift left by n)          │
│                                                                  │
│  Example (ROT-3): "HELLO" → "KHOOR"                              │
│  H(7)+3=10=K, E(4)+3=7=H, L(11)+3=14=O, O(14)+3=17=R           │
│                                                                  │
│  ROT-13: special case n=13; applying twice decodes (symmetric)   │
│  Still used: USENET spoiler hiding, obfuscated puzzle hints      │
└──────────────────────────────────────────────────────────────────┘
```

**Breaking Caesar**: 25 possible keys. Try all 25 (brute force). Done.

```
Security analysis:
  Key space: 25 (excluding no-op ROT-0)
  Brute force: trivial by hand, microseconds by computer
  Frequency analysis: single most frequent ciphertext letter → 'E'
  Use: education, childproofing, puzzle games only
```

---

## Atbash Cipher (Reverse Alphabet)

Hebrew cipher from ~600 BCE, used in the Bible (Book of Jeremiah):

```
Plaintext:   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Ciphertext:  Z Y X W V U T S R Q P O N M L K J I H G F E D C B A

Atbash = reverse mapping: A↔Z, B↔Y, C↔X, etc.
Function: E(x) = 25 - x (in 0-indexed alphabet)
Self-inverse: encrypt = decrypt (like ROT-13)

Original Hebrew: aleph (א) ↔ tav (ת), bet (ב) ↔ shin (ש) → "Atbash"
Biblical use: "Sheshach" in Jeremiah 25:26 = Atbash encoding of "Babel"
```

---

## Vigenère Cipher (Polyalphabetic)

The breakthrough: using multiple alphabets (shifts) in rotation, keyed by a keyword. Defeats simple frequency analysis.

```
┌──────────────────────────────────────────────────────────────────┐
│                    VIGENÈRE CIPHER                                │
│                                                                  │
│  Key: LEMON   (repeated for length of message)                   │
│  Plaintext:   A  T  T  A  C  K  A  T  D  A  W  N               │
│  Key:         L  E  M  O  N  L  E  M  O  N  L  E               │
│  Key (0-idx): 11  4 12 14 13 11  4 12 14 13 11  4               │
│  Ciphertext:  L  X  F  O  P  V  E  F  R  N  H  R               │
│                                                                  │
│  Rule: C_i = (P_i + K_i) mod 26                                  │
│  Decryption: P_i = (C_i - K_i) mod 26                           │
│                                                                  │
│  TABULA RECTA: 26×26 table of Caesar shifts                      │
│  Row label = key letter, Column label = plaintext letter         │
│  Cell = ciphertext letter                                        │
└──────────────────────────────────────────────────────────────────┘
```

### Tabula Recta (partial)

```
     A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
  A: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
  B: B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
  C: C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
  ...
  L: L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
  ...
  Z: Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
```

### Autokey Variant

```
Instead of repeating the keyword, append the plaintext itself as key:
  Key:         LEMON ATTACKATDAWN...
  Plaintext:   ATTACKATDAWN
  → Key = L E M O N A T T A C K A (starts with keyword, extends with plaintext)

Stronger than repeating keyword because no periodic pattern.
Still breakable with sufficient ciphertext.
```

### Breaking Vigenère — Kasiski Attack (1863)

```
┌──────────────────────────────────────────────────────────────┐
│               KASISKI / FRIEDMAN ATTACK                       │
│                                                              │
│  KASISKI (1863):                                             │
│  1. Scan ciphertext for repeated trigrams                    │
│  2. Distance between repeats is likely a multiple of key len │
│     (because same plaintext + same key position = same cipher)│
│  3. GCD of all repeat-distances ≈ key length                 │
│  4. Once key length known: divide into key-length columns    │
│  5. Each column is a simple Caesar cipher → frequency-analyze│
│                                                              │
│  FRIEDMAN (1922) — Index of Coincidence method:             │
│  IC = Σ(f_i × (f_i-1)) / (N × (N-1))                        │
│  For English random text: IC ≈ 0.065                         │
│  For random uniform: IC ≈ 0.038                              │
│  Vigenère with key length k → IC ≈ 0.038 + (0.027/k)        │
│  → IC tells you the key length                               │
│  → Then Kasiski columns + frequency analysis = broken        │
│                                                              │
│  KEY INSIGHT: polyalphabetic != immune to statistics         │
│  Long-enough ciphertext always reveals key-length periodicity│
└──────────────────────────────────────────────────────────────┘
```

---

## Playfair Cipher (Digraph Substitution, 1854)

Charles Wheatstone invented it; Lord Playfair popularized it. Encrypts **pairs** of letters (digraphs), not single letters, using a 5×5 key grid.

```
┌──────────────────────────────────────────────────────────────┐
│                PLAYFAIR CIPHER                                │
│                                                              │
│  5×5 grid: fill with keyword (no duplicate letters),        │
│  then remaining alphabet (I and J share a cell)              │
│                                                              │
│  Example key: MONARCH                                        │
│  M O N A R                                                   │
│  C H Y B D                                                   │
│  E F G I K                                                   │
│  L P Q S T                                                   │
│  U V W X Z                                                   │
│                                                              │
│  RULES for encrypting letter pair (X, Y):                    │
│  1. Same row: each slides right one (wrap)                   │
│     (M,O) → (O,N)                                            │
│  2. Same column: each slides down one (wrap)                 │
│     (M,C) → (C,E)                                            │
│  3. Rectangle: each takes the other's column in same row     │
│     (E,R) → E in row 3 col 1, R in row 1 col 5              │
│           → take row 3 col 5, row 1 col 1 = (K,M)           │
│                                                              │
│  PREPROCESSING:                                              │
│  — J → I (or Q → K, depends on variant)                     │
│  — Double letters in a pair: insert X between (HELLO → HE LX LO)│
│  — Odd-length plaintext: add X at end                        │
│                                                              │
│  Security: breaks frequency analysis of single letters,      │
│  but digraph frequency analysis (25² = 625 combinations)     │
│  is still feasible with moderate ciphertext length.          │
│  British military used it in WWI and WWII.                   │
└──────────────────────────────────────────────────────────────┘
```

---

## ADFGVX Cipher (WWI German, 1918)

Used by the Imperial German Army in the final months of WWI. Combines substitution with transposition.

```
┌──────────────────────────────────────────────────────────────┐
│                ADFGVX CIPHER                                  │
│                                                              │
│  Step 1: Polybius square with alphabet + digits (36 chars)   │
│  Uses the 6 letters A, D, F, G, V, X as coordinates         │
│  (chosen because these letters are distinct in Morse code)   │
│                                                              │
│  Example ADFGVX grid (key "CAFE"):                           │
│      A  D  F  G  V  X                                        │
│  A [ C  A  F  E  B  D ]                                      │
│  D [ G  H  I  J  K  L ]                                      │
│  F [ M  N  0  1  2  3 ]                                      │
│  G [ 4  5  6  7  8  9 ]                                      │
│  V [ O  P  Q  R  S  T ]                                      │
│  X [ U  V  W  X  Y  Z ]                                      │
│                                                              │
│  Each plaintext letter → 2-letter coordinate                 │
│  "ATTACK" → AA DD GG AA AC VA AX                             │
│              A   T  T  A  C  K                               │
│                                                              │
│  Step 2: Columnar transposition                              │
│  Write output rows under a numeric keyword                   │
│  Read columns in keyword-number order                        │
│                                                              │
│  Security: combined substitution + transposition was        │
│  difficult for 1918 cryptanalysts. Broken by Georges Painvin │
│  (French) in June 1918 during the Spring Offensive — one    │
│  of the most important cryptanalytic feats of WWI.          │
└──────────────────────────────────────────────────────────────┘
```

---

## One-Time Pad / Vernam Cipher (1917)

The **only provably secure cipher**. Gilbert Vernam's 1917 patent; Claude Shannon proved its perfect secrecy in 1949.

```
┌──────────────────────────────────────────────────────────────┐
│                ONE-TIME PAD (OTP)                             │
│                                                              │
│  Requirements for perfect secrecy:                          │
│  1. Key must be as long as the message                       │
│  2. Key must be truly random (not pseudorandom)              │
│  3. Key must never be reused (hence "one-time")              │
│  4. Key must be kept secret                                  │
│                                                              │
│  Encryption: C_i = (P_i + K_i) mod 26 (or XOR for binary)  │
│  Decryption: P_i = (C_i - K_i) mod 26                       │
│  (Same formula as Vigenère, but key length = message length  │
│   and key is random — this is what makes it unbreakable)     │
│                                                              │
│  Shannon's proof (1949):                                     │
│  I(P; C) = 0  (mutual information between plaintext and      │
│                 ciphertext is zero)                          │
│  For every possible plaintext p and ciphertext c:            │
│  P(P=p | C=c) = P(P=p)                                       │
│  → Observing ciphertext gives NO information about plaintext │
│  → Breaking the cipher requires the key, period.            │
│                                                              │
│  Historical use:                                             │
│  — USSR/US hotline (Moscow-Washington) used OTP              │
│  — "Number stations" broadcast OTP key consumption            │
│  — Diplomatic traffic for highest-security messages          │
│                                                              │
│  Why not universally used:                                   │
│  KEY DISTRIBUTION PROBLEM — how do you securely share a      │
│  key as long as all future messages you'll ever send?        │
│  This is the central problem of pre-public-key cryptography. │
└──────────────────────────────────────────────────────────────┘
```

---

## Enigma Machine (1918–1945)

Electromechanical rotor machine; the most sophisticated cipher device of its era.

### Physical Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                    ENIGMA ARCHITECTURE                            │
│                                                                  │
│  KEYBOARD ──→ PLUGBOARD ──→ ROTORS (3 or 4) ──→ REFLECTOR       │
│               (Steckerbrett)   (Scrambler)      (Umkehrwalze)   │
│                    ↑                                ↓            │
│                    └───────── return path ──────────┘            │
│                                                                  │
│  Each key press:                                                 │
│  1. Signal enters plugboard (swaps pairs of letters)            │
│  2. Passes through 3 (or 4 Navy) rotors left-to-right          │
│  3. Hits reflector — routes signal back through rotors          │
│  4. Returns through plugboard                                   │
│  5. Lights up a lamp on the lampboard                           │
│  6. Rightmost rotor advances one step (others cascade)          │
│                                                                  │
│  ROTORS (Walzen):                                                │
│  Each rotor: 26-letter substitution + notch for advancement     │
│  Wehrmacht had 5 standard rotors (I–V), each with unique wiring │
│  Kriegsmarine (Navy Enigma M4): 4 rotors (added Enigma M4 1942) │
│  Right rotor steps every keypress                               │
│  Middle rotor steps when right passes notch (odometer-like)     │
│  Left rotor steps when middle passes notch                      │
│                                                                  │
│  REFLECTOR (Umkehrwalze):                                        │
│  Fixed rotor — pairs letters (A↔Y, B↔S, etc.)                  │
│  Key property: reflector ensures E(E(x)) = x                   │
│  → Enigma is self-reciprocal (same machine settings decrypt)    │
│  → ALSO: a letter can never encrypt to itself                   │
│     (This was a critical cryptanalytic exploit)                 │
│                                                                  │
│  PLUGBOARD (Steckerbrett):                                       │
│  Swaps up to 13 letter pairs before/after rotors                │
│  Wehrmacht: 10 pairs typically; Luftwaffe: same                  │
│  Adds enormous key space: C(26,2)×C(24,2)×...÷10! combinations  │
└──────────────────────────────────────────────────────────────────┘
```

### Enigma Key Space

```
Rotor selection (from 5, choose 3, arrange): 5×4×3 = 60
Rotor starting positions: 26³ = 17,576
Ring settings (Ringstellung): 26² = 676 (for 3-rotor)
Plugboard (10 cable pairs): ≈ 150,738,274,937,250

Total daily key combinations ≈ 1.07 × 10²³

For comparison:
56-bit DES: 7.2 × 10¹⁶ possible keys (less than Enigma!)
Yet Enigma was broken; DES was considered secure by brute force.
The difference: Enigma had structural weaknesses; DES did not.
```

### Breaking Enigma

```
┌──────────────────────────────────────────────────────────────┐
│              HOW ENIGMA WAS BROKEN                            │
│                                                              │
│  STRUCTURAL WEAKNESS: no letter can encrypt to itself        │
│  (because reflector returns signal through rotors)           │
│  This gave cryptanalysts a "crib" test: if proposed key       │
│  produces a ciphertext letter that equals the plaintext,     │
│  that key setting is IMPOSSIBLE.                             │
│                                                              │
│  CRIBS: known/guessed plaintext snippets                     │
│  — "Keine besonderen Ereignisse" (nothing to report)         │
│  — Weather reports with predictable format/phrases           │
│  — "An die Gruppe" (to the group) in message headers         │
│  — Operators lazy: AAAAAAA, or "Hitler" in known position    │
│                                                              │
│  BOMBE (Turing/Welchman machine):                            │
│  Electromechanical analog computer                           │
│  Tests crib hypothesis against all rotor/ring combinations   │
│  Uses "menu" of crib letter chains to eliminate settings     │
│  Thousands of Bombe machines by 1944 at Bletchley Park       │
│                                                              │
│  ADDITIONAL ATTACKS:                                         │
│  — Polish mathematicians (Rejewski, Różycki, Zygalski):     │
│    broke early Enigma using algebraic group theory (1932)   │
│    — Before WWII, before the bombe!                          │
│  — Captured key sheets from U-boats (pinch operations)       │
│  — Indicators repeated → provided known plaintext           │
│  — Operator errors: messages enciphered with same key        │
│                                                              │
│  LORENZ CIPHER (Tunny): German high command teleprinter      │
│  Even more complex; broken by Bill Tutte analyzing structure  │
│  without ever seeing the machine.                            │
│  → Led to Colossus (first programmable electronic computer)  │
└──────────────────────────────────────────────────────────────┘
```

---

## Frequency Analysis

The fundamental attack on monoalphabetic substitution, developed by Arab scholar Al-Kindi (~850 CE):

```
┌──────────────────────────────────────────────────────────────┐
│              ENGLISH LETTER FREQUENCIES                       │
│                                                              │
│  E  12.7%   T   9.1%   A   8.2%   O   7.5%                  │
│  I   7.0%   N   6.7%   S   6.3%   H   6.1%                  │
│  R   6.0%   D   4.3%   L   4.0%   C   2.8%                  │
│  U   2.8%   M   2.4%   W   2.4%   F   2.2%                  │
│  G   2.0%   Y   2.0%   P   1.9%   B   1.5%                  │
│  V   1.0%   K   0.8%   J   0.15%  X   0.15%                 │
│  Q   0.10%  Z   0.07%                                        │
│                                                              │
│  DIGRAPH FREQUENCIES (most common):                          │
│  TH  HE  IN  ER  AN  RE  ON  EN  AT  ES  ST  NT             │
│                                                              │
│  TRIGRAPH FREQUENCIES:                                       │
│  THE  AND  ING  ION  ENT  ION  FOR  HER  HAT  THA           │
│                                                              │
│  ATTACK STRATEGY for monoalphabetic ciphertext:              │
│  1. Count ciphertext letter frequencies                      │
│  2. Most frequent → E (especially if clearly dominant)       │
│  3. Second → T; also look for single-letter words (A, I)     │
│  4. Look for two-letter words: he, is, it, of, to, do...     │
│  5. Look for "THE" pattern: most common trigraph             │
│  6. Each identification constrains remaining letters         │
│  7. Pattern-match against common English words               │
│  8. Complete by context inference                            │
└──────────────────────────────────────────────────────────────┘
```

### Index of Coincidence

```
IC = Σ(n_i × (n_i - 1)) / (N × (N-1))

Where n_i = count of letter i in the ciphertext, N = total letters

English text:   IC ≈ 0.065
Random cipher:  IC ≈ 0.038 (1/26)
Vigenère key-2: IC ≈ 0.052
Vigenère key-5: IC ≈ 0.044

Interpretation:
  IC near 0.065 → monoalphabetic (substituted English-like)
  IC near 0.038 → uniform distribution (OTP or long polyalphabetic)
  Intermediate → polyalphabetic with short key
  Key length estimate: k ≈ (0.027 × N) / ((N-1)×IC - 0.038×N + 0.065)
```

---

## Cipher vs. Code vs. Steganography

```
┌──────────────────────────────────────────────────────────────┐
│              SECRECY TECHNIQUE TAXONOMY                       │
│                                                              │
│  CIPHER: transforms plaintext algorithmically                │
│  — Security comes from key secrecy, not algorithm secrecy    │
│  — Kerckhoffs's principle: assume attacker knows the cipher  │
│  — Example: AES, RSA, Caesar                                 │
│                                                              │
│  CODE: replaces words/phrases from a codebook                │
│  — "VICTOR" means "attack at dawn"                           │
│  — Security from codebook secrecy                            │
│  — WWII Japan Naval Code JN-25 = codebook cipher             │
│  — One-time codebooks + super-encryption (encipher the code) │
│                                                              │
│  STEGANOGRAPHY: hides existence of message                   │
│  — Invisible ink, microdots, least-significant bit in image  │
│  — "The spy's message is in the 2nd letter of each sentence" │
│  — Security from not knowing a message exists                │
│  — Modern: watermarking, stego in image files                │
│                                                              │
│  Real-world systems combine all three:                       │
│  Enigma = cipher (rotor algorithm) + codebook (Schlüssel)   │
│  + operational security protocols                            │
└──────────────────────────────────────────────────────────────┘
```

---

## Bridge to Modern Cryptography

The conceptual gap between classical and modern cryptography:

```
Classical crypto problem:                Modern crypto solution:
─────────────────────────────────────────────────────────────────
"How do two parties communicate         Public-key cryptography (1976)
 securely without meeting first          Diffie-Hellman key exchange
 to exchange a key?"                     RSA key exchange/encryption
                                         → No pre-shared secret needed

"How do you prove identity              Digital signatures (RSA/ECDSA)
 over an insecure channel?"             Zero-knowledge proofs

"How do you authenticate a             HMAC / AES-GCM authenticated
 message without encrypting it?"        encryption

"One-time pad is perfect but           Pseudo-random key streams from
 key distribution is impossible"        PRF/PRG + computationally secure
                                         assumptions (AES-CTR mode)

"Enigma's key space was huge           Structural attacks matter more
 but it was still broken"               than key space; algorithm design
                                         determines security
```

**Kerckhoffs's Principle** (1883): A cipher system should be secure even if everything about the system except the key is public knowledge. Modern cryptography embodies this — AES is completely public; security rests entirely on key secrecy. Classical systems often violated this.

**Shannon's maxims** (1949):
1. Perfect secrecy requires key ≥ message length (→ impractical)
2. Computational security is the practical goal
3. Confusion + Diffusion are the two design principles
   - Confusion: each ciphertext bit depends on many key bits (substitution)
   - Diffusion: each plaintext bit affects many ciphertext bits (transposition/mixing)
   → Still the design principles behind modern block ciphers (AES's SubBytes = confusion, ShiftRows/MixColumns = diffusion)

---

## Decision Cheat Sheet

| Cipher Type | Example | Security | Broken by |
|-------------|---------|----------|-----------|
| Monoalphabetic shift | Caesar | None | Frequency analysis |
| Monoalphabetic substitution | Atbash | None | Frequency analysis |
| Polyalphabetic | Vigenère | Weak | Kasiski/Friedman + frequency |
| Digraph substitution | Playfair | Moderate | Digraph frequency analysis |
| Combined sub+transpose | ADFGVX | Moderate-strong | Painvin (1918) |
| One-time pad | Vernam | Perfect | Cannot be broken (key needed) |
| Electromechanical | Enigma | Strong (structurally flawed) | Bombe + cribs + operator errors |
| Modern symmetric | AES-256 | Very high | Not practically broken |
| Modern asymmetric | RSA-2048 | High | Not practically broken (yet) |

---

## Common Confusion Points

**Vigenère was called "le chiffre indéchiffrable"** (the unbreakable cipher) for 300 years until Kasiski (1863) broke it. The reputation survived despite the vulnerability because the attack wasn't published or widely known. This is a classic example of security by obscurity failing eventually.

**Enigma was a cipher machine, not a cipher algorithm**: The algorithm was publicly known (it was sold commercially in the 1920s). The security came from the daily key settings (rotor selection, positions, ring settings, plugboard). This correctly embodies Kerckhoffs's principle — but the key management and operator procedures were the vulnerabilities.

**No letter encrypting to itself was the critical flaw**: This was an inherent consequence of the reflector design that enabled the bombe to work. A cipher with this property can never encrypt A→A, so if you have a crib, you can eliminate any key setting where any ciphertext letter matches the crib plaintext letter. This dramatically reduces the search space.

**Polish mathematicians broke Enigma first**: The British success at Bletchley Park built on foundational work by Marian Rejewski, Jerzy Różycki, and Henryk Zygalski who broke the Wehrmacht Enigma in 1932 using algebraic methods. They passed their work to the British and French just before the German invasion of Poland in September 1939.

**OTP security requires true randomness**: PRNG-generated "random" key is NOT a one-time pad. If the attacker can predict the keystream (or compromise the PRNG), the OTP guarantee breaks immediately. Historical failures in "OTP" systems typically involved reuse or poor randomness, not algorithmic weaknesses.
