# Codes & Symbolic Systems — Overview

## The Big Picture

Human symbolic communication layers over four physical channels. Every code in this directory lives in exactly one of these quadrants.

```
                    MEDIUM TAXONOMY
    ┌─────────────────────────────────────────────────────────┐
    │                                                         │
    │   VISUAL                         TACTILE                │
    │   ┌───────────────────┐          ┌────────────────────┐ │
    │   │ Flag semaphore    │          │ Braille (Grade 1/2)│ │
    │   │ Signal flags ICS  │          │ Deafblind manual   │ │
    │   │ Musical notation  │          │ Moon type          │ │
    │   │ Road signs/ISO    │          │ Tactile paving     │ │
    │   │ Resistor bands    │          │ Tactile graphics   │ │
    │   │ QR/barcode        │          └────────────────────┘ │
    │   │ ASL fingerspelling│                                  │
    │   └───────────────────┘                                  │
    │                                                         │
    │   AUDITORY                       ELECTRONIC/MACHINE     │
    │   ┌───────────────────┐          ┌────────────────────┐ │
    │   │ Morse code        │          │ QR / Data Matrix   │ │
    │   │ NATO phonetic     │          │ NFC/RFID           │ │
    │   │ Radio prosigns    │          │ Barcode (EAN/UPC)  │ │
    │   │ Drum telegraphy   │          │ ASCII/Unicode      │ │
    │   │ Heliograph flash  │          │ Error-correcting   │ │
    │   └───────────────────┘          │ codes (Reed-Solomon│ │
    │                                  │ in CD/QR/DVB)      │ │
    │   GESTURE/KINESTHETIC            └────────────────────┘ │
    │   ┌───────────────────┐                                  │
    │   │ ASL (full)        │                                  │
    │   │ BSL               │                                  │
    │   │ Signed Exact Eng. │                                  │
    │   │ Semaphore arms    │                                  │
    │   └───────────────────┘                                  │
    └─────────────────────────────────────────────────────────┘
```

**And then there are ciphers** — a separate axis. Ciphers transform content for secrecy; codes above transform content for accessibility, distance, or machine readability.

---

## Historical Arc — From Signal Fire to QR Code

```
~3000 BCE  Beacons, drums, smoke — broadcast, no alphabet
 776 BCE   Greek Olympic fire relay — single-bit signaling (fire/no fire)
 200 BCE   Polybius square — first matrix encoding of letters (checkerboard)
1794 CE    Chappe optical telegraph — mechanized semaphore, France
1837       Morse/Vail electric telegraph — wire-speed text transmission
1821       Braille — tactile code for blind readers (Louis Braille, age 15)
1865       International Morse standardized (ITU predecessor)
1891       Semaphore flags standardized for maritime
1850s-1900 Various flag code books → International Code of Signals
1926       NATO precursor phonetic: Able Baker alphabet (US Army)
1956       ICAO/NATO phonetic alphabet finalized (Alfa Bravo...)
1949       International Code of Signals modernized
1952       Music notation standardized (modern practice codified)
1974       EAN barcode — first laser scanner supermarket use
1994       QR code — Denso Wave, Toyota (high density + error correction)
2003       NFC standard — contactless close-range
2010s      Data Matrix, Aztec Code — industrial/ticket applications
```

The pattern: **every code emerges from a bandwidth/fidelity constraint** — telegraph wires had no alphabet, the blind could not see print, radio had no typing, cargo ships needed a lingua franca across languages.

---

## Relationship to Information Theory

Claude Shannon's 1948 paper provides the mathematical foundation for all of these:

```
Source → Encoder → Channel → Decoder → Destination
                      |
               Noise / Error
```

| Code | Shannon Angle |
|------|--------------|
| Morse | Variable-length prefix code — short symbols for frequent letters (like Huffman) |
| Braille | Fixed 6-bit cell — 64 possible symbols, subsets assigned to grades |
| QR | Block error-correction code (Reed-Solomon) — redundancy against partial damage |
| One-time pad | Perfect secrecy — mutual information between ciphertext and plaintext = 0 |
| Resistor bands | Fixed-length numerical code — 3 sig figs + exponent |
| Musical notation | Lossless representation — pitch + duration + dynamics → score |
| NATO phonetic | Noise-robust substitution — phoneme chosen for cross-accent clarity |

**Key insight from information theory**: the more **structured** the noise channel, the more you can fight it. QR codes survive 30% data loss because they're designed knowing that damage is spatially correlated (physical tearing). Morse is robust to short bursts of noise because each symbol is time-bounded.

Shannon entropy also explains **why Morse code works**: E (.) and T (-) are the shortest symbols because `e` and `t` are the most frequent English letters. Morse approximates a Huffman code for English. Verified: Shannon entropy of English ≈ 1.0–1.5 bits/letter; Morse average length ≈ 2.5 time units/letter (not optimal Huffman but historically derived from same principle).

---

## Taxonomy by Purpose

```
┌──────────────────────────────────────────────────────────┐
│                    PURPOSE TAXONOMY                      │
├──────────────────┬───────────────────────────────────────┤
│ CHANNEL-ADAPTIVE │ Morse, semaphore, signal flags,        │
│                  │ NATO phonetic — message across a       │
│                  │ constrained channel (wire/light/radio) │
├──────────────────┼───────────────────────────────────────┤
│ ACCESSIBILITY    │ Braille, Moon type, ASL fingerspelling,│
│                  │ tactile paving — same information for │
│                  │ different sensory modalities          │
├──────────────────┼───────────────────────────────────────┤
│ MACHINE-READABLE │ Barcode, QR, Data Matrix, NFC/RFID,   │
│                  │ resistor bands — human → machine I/O  │
├──────────────────┼───────────────────────────────────────┤
│ CULTURAL/DOMAIN  │ Musical notation, road signs, wire    │
│ LINGUA FRANCA    │ color codes — expert community        │
│                  │ standard, cross-language              │
├──────────────────┼───────────────────────────────────────┤
│ SECURITY/SECRECY │ Historical ciphers (Caesar, Vigenère,  │
│                  │ Enigma), modern crypto (in computing/  │
│                  │ 25-SECURITY.md) — prevent unauthorized │
│                  │ reading                                │
└──────────────────┴───────────────────────────────────────┘
```

---

## Encoding Dimensions Comparison

| System | Alphabet Size | Fixed/Variable Length | Error Detection | Human Decodable | Machine Decodable |
|--------|--------------|----------------------|-----------------|-----------------|-------------------|
| Morse | 54+ symbols | Variable (dit/dah) | None built-in | Yes (by ear) | Yes |
| Braille Grade 1 | 64 cells | Fixed (6-bit) | None | Touch-trained | Yes |
| Braille Grade 2 | 189 contractions | Fixed cells, variable meaning | None | Touch-trained | Yes |
| Semaphore | 26 letters + nums | Fixed (2 arms) | None | Yes (trained) | Camera |
| Signal flags | 26 + numerals | 1–few flags | None | Yes | No |
| NATO phonetic | 26 letters | Variable (words) | High (phoneme) | Yes | NLP |
| ASL fingerspelling | 26 handshapes | Fixed (1 hand) | None | Trained | Vision AI |
| QR Code | Full Unicode | Variable | Reed-Solomon | No | Yes |
| EAN-13 | Digits | Fixed (13 digits) | Check digit | With training | Yes |
| Musical notation | Full domain | Mixed | None (pitch/rhythm) | Trained | Yes |

---

## The Cipher vs. Code Distinction

Historically confused, now well-defined:

```
CODE  = replaces entire words/phrases with other words/numbers
        (codebook required — "VICTOR" means "attack at dawn")

CIPHER = transforms individual letters/bits by algorithm
         (Caesar, Vigenère, AES)
```

In modern usage "code" is often used loosely. The files in this directory use both but the historical ciphers section (`08-HISTORICAL-CIPHERS.md`) covers the encryption-specific track. For modern cryptography, see `computing/25-SECURITY.md`.

---

## Index of All Files

| File | System | What You'll Find |
|------|--------|-----------------|
| `01-MORSE.md` | Morse code | Full A–Z + 0–9 + punctuation, dot/dash visual charts, Koch method, Q-codes, prosigns |
| `02-BRAILLE.md` | Braille | 6-dot cell, Grade 1/2, UEB contractions, Nemeth Code, computer Braille |
| `03-SEMAPHORE.md` | Semaphore | Flag alphabet with ASCII arm diagrams, Chappe telegraph, railway semaphore |
| `04-SIGNAL-FLAGS.md` | ICS/NATO signal flags | A–Z single-letter meanings, numeral pendants, urgent signals |
| `05-NATO-PHONETIC.md` | NATO/ICAO phonetic | Alfa–Zulu + pronunciation, history (Able Baker), radio procedure words |
| `06-FINGERSPELLING-SIGN.md` | ASL | 26 handshapes, BSL comparison, ASL grammar intro |
| `07-MUSICAL-NOTATION.md` | Western music notation | Staff, clefs, note values, keys, dynamics, tempo, chord symbols |
| `08-HISTORICAL-CIPHERS.md` | Classical ciphers | Caesar, Vigenère, Playfair, ADFGVX, OTP, Enigma, frequency analysis |
| `09-MODERN-CODES.md` | Machine-readable codes | EAN-13, QR, Data Matrix, NFC, resistor bands, wire colors, road signs |

---

## Common Confusion Points

**Morse "code" vs. cipher**: Morse is a public encoding — anyone who knows the table can decode it. It provides no secrecy; it's a channel-adaptive encoding like Base64.

**Braille Grade 1 vs. 2**: Grade 1 is letter-for-letter (literary Braille). Grade 2 adds contractions (186 in UEB) — "the" is a single cell, "and" is a single cell, etc. Most Braille in the real world is Grade 2. Nemeth is a separate system for mathematics.

**NATO phonetic vs. spelling alphabet**: "NATO phonetic" is a slight misnomer — it's a spelling alphabet (each word stands for one letter), not a phonetic transcription system like IPA.

**Musical notation is language-agnostic**: A score written in Milan is readable by a musician in Tokyo without translation. The notation is a domain lingua franca, not encoding in the information-theory sense (it has no compression or error correction).

**QR vs. barcode**: 1D barcode = linear, encodes ~20 chars. 2D QR = matrix, encodes up to 3000 chars with error correction. QR is a superset in capability.

**Signal flag "code" vs. phonetic**: Signal flags have two modes — (1) single-letter procedural meaning (A = "diver below, keep clear"), (2) multi-flag combinations from the International Code of Signals (ICS) codebook with thousands of entries.

---

## Decision Cheat Sheet — Which Code for Which Need?

| Situation | Best System |
|-----------|-------------|
| Long-distance, minimal equipment | Morse (light/sound) |
| Maritime ship-to-ship signaling | Signal flags (ICS) |
| Voice radio, call sign clarity | NATO phonetic |
| Blind reader, literary text | Braille Grade 2 (UEB) |
| Blind reader, math/science | Nemeth Code |
| Deaf/HoH communication, fingerspelling | ASL manual alphabet |
| Musical performance instructions | Standard notation (treble/bass clef) |
| Product tracking, retail | EAN-13 barcode |
| URL, text, dense data on label | QR code |
| Electronic component marking | Resistor color bands |
| Secret message, pen and paper | Vigenère (educational); AES-256 (real) |
| Secret message, absolute secrecy | One-time pad (if key distribution solved) |
