# Morse Code — Complete Reference

## The Big Picture

Morse code is a **variable-length prefix code** that maps each letter, digit, and symbol to a sequence of two elements: dot (·) and dash (—). Invented jointly by Samuel Morse and Alfred Vail in 1838, it dominated telegraphy for a century and remains in active use by amateur radio operators today.

```
┌──────────────────────────────────────────────────────────────────┐
│                    MORSE CODE SYSTEM MAP                          │
│                                                                  │
│  Message ──→ Encoding ──→ Transmission medium ──→ Decoding       │
│                                                                  │
│  "SOS"                                                           │
│  S=···  O=───  S=···   ("three dots, three dashes, three dots")  │
│                                                                  │
│  Transmission modes:                                             │
│  ┌─────────────┬──────────────────────────────────────────────┐ │
│  │ CW (radio)  │ Continuous Wave keying — on/off carrier      │ │
│  │ Sounder     │ Audible click/clack mechanical device         │ │
│  │ Light       │ Flash lamp or mirror (heliograph/Aldis lamp)  │ │
│  │ Buzzer      │ Audible tone keying                           │ │
│  │ Tactile     │ Vibration on skin (deafblind applications)    │ │
│  │ Visual      │ Written dots and dashes on paper/screen       │ │
│  └─────────────┴──────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

---

## Timing Rules (the Signal Grammar)

Morse is a **time-based** code. The relationships between durations are everything:

```
┌────────────────────────────────────────────────────────────┐
│                    TIMING RATIOS                            │
│                                                            │
│  Dot duration      = 1 unit  (reference unit)              │
│  Dash duration     = 3 units                               │
│  Intra-char gap    = 1 unit  (between dots/dashes in same  │
│                               letter — silence same as dot)│
│  Inter-char gap    = 3 units (between letters)             │
│  Inter-word gap    = 7 units (between words)               │
│                                                            │
│  Example: "hi" = H I                                       │
│  H = · · · ·    I = · ·                                    │
│  ·_·_·_·  ___  ·_·                                         │
│  1+1+1+1+1+1+1  3  1+1+1  (units)                          │
│         ^inter-char gap^                                    │
└────────────────────────────────────────────────────────────┘
```

At 20 WPM, one dot ≈ 60ms. At 30 WPM, one dot ≈ 40ms.

---

## Complete Alphabet — A to Z

```
┌─────────────────────────────────────────────────────────────┐
│                  MORSE ALPHABET                             │
├──────┬──────────┬──────┬──────────┬──────┬──────────────────┤
│  A   │  ·  —   │  J   │  ·———    │  S   │  ·  ·  ·         │
│  B   │  — ···  │  K   │  — · —   │  T   │  —               │
│  C   │  — · — ·│  L   │  · — ··  │  U   │  ·  · —          │
│  D   │  — ··   │  M   │  — —     │  V   │  ·  · · —        │
│  E   │  ·      │  N   │  — ·     │  W   │  ·  — —          │
│  F   │  · · — ·│  O   │  — — —   │  X   │  —  · · —        │
│  G   │  — — ·  │  P   │  · — — · │  Y   │  —  · — —        │
│  H   │  ····   │  Q   │  — — · — │  Z   │  — —  ··         │
│  I   │  ··     │  R   │  · — ·   │      │                  │
└──────┴──────────┴──────┴──────────┴──────┴──────────────────┘
```

Mnemonic/pattern notes:
- **E** = `.` and **T** = `—` are single symbols (most frequent English letters)
- **I** = `··` (2 dots), **A** = `·—` (1+1), **N** = `—·` (flip of A)
- **S** = `···` (3 dots), **O** = `———` (3 dashes)
- **R** = `·—·` (dit-dah-dit), **L** = `·—··` (dit-dah-dit-dit)
- **K** = `—·—` (the invitation prosign), **C** = `—·—·`

---

## Complete Numbers — 0 to 9

```
┌────────────────────────────────────────────────────────────┐
│                    MORSE NUMERALS                          │
│                                                            │
│  1  ·————    (one dot, four dashes)                        │
│  2  ··———    (two dots, three dashes)                      │
│  3  ···——    (three dots, two dashes)                      │
│  4  ····—    (four dots, one dash)                         │
│  5  ·····    (five dots)                                   │
│  6  —····    (one dash, four dots)                         │
│  7  ——···    (two dashes, three dots)                      │
│  8  ———··    (three dashes, two dots)                      │
│  9  ————·    (four dashes, one dot)                        │
│  0  —————    (five dashes)                                 │
│                                                            │
│  Pattern: 1-5 are "loading up" dots → dashes               │
│           6-0 are "unloading" dashes → dots                │
│           0 = all dashes (continues from 9's pattern)      │
└────────────────────────────────────────────────────────────┘
```

---

## Punctuation and Special Characters

| Symbol | Morse | Notes |
|--------|-------|-------|
| `.` Period | `·—·—·—` | AR prosign-like, but with space treatment |
| `,` Comma | `——··——` | MIM |
| `?` Question | `··——··` | IMI |
| `'` Apostrophe | `·————·` | JN |
| `!` Exclamation | `—·—·——` | MN |
| `/` Slash (Fraction bar) | `—··—·` | DN |
| `(` Open paren | `—·——·` | KN |
| `)` Close paren | `—·——·—` | KK |
| `&` Ampersand/Wait | `·—···` | AS (same as wait prosign) |
| `:` Colon | `———···` | OS |
| `;` Semicolon | `—·—·—·` | |
| `=` Equals (double dash) | `—···—` | BT (same as paragraph break) |
| `+` Plus | `·—·—·` | AR (same as end-of-message) |
| `-` Hyphen | `—····—` | |
| `_` Underscore | `··——·—` | |
| `"` Quote | `·—··—·` | AF |
| `@` At sign | `·——·—·` | AC (added to ITU standard in 2004) |
| `$` Dollar | `···—··—` | SX |

---

## Prosigns (Procedure Signals)

Prosigns are sent as single characters (no inter-element gap between letters), indicated by overlines in formal notation. Critical for radio operating procedure:

```
┌─────────────────────────────────────────────────────────────────┐
│                    PROSIGNS                                      │
├───────┬─────────┬───────────────────────────────────────────────┤
│ AR    │ ·—·—·   │ End of message — "over" (go ahead, reply)     │
│ AS    │ ·—···   │ Wait / Stand by                               │
│ BT    │ —···—   │ Break (new paragraph or section separator)    │
│ CL    │ —·—···—·│ Going off the air (closing station)           │
│ CT/KA │ —·—·—   │ Attention — start copy (beginning of message) │
│ HH    │ ········│ Error — disregard previous (8 dots)           │
│ K     │ —·—     │ Invite any station to transmit ("go")         │
│ KN    │ —·——·   │ Invite only named station to transmit         │
│ SK/VA │ ···—·—  │ End of contact (signing off completely)       │
│ SN/VE │ ···—·   │ Understood / "Roger"                          │
│ SOS   │ ···———··│ Distress (sent as one unit, no gaps)          │
└───────┴─────────┴───────────────────────────────────────────────┘
```

**SOS** `···———···` is not `S + O + S` with gaps — it's a single prosign sent continuously. The equal spacing makes it unmistakable.

---

## Q-Codes

Q-codes originated for maritime/commercial telegraphy, now heavily used in amateur radio. All begin with Q; all have a question form (interrogative) and statement form (answer/information):

### Essential Q-Codes

| Code | Question Form | Answer / Statement Form |
|------|--------------|------------------------|
| **QRL** | Are you busy? Is this frequency in use? | Yes, frequency is in use — don't call here |
| **QRM** | Are you being interfered with (man-made)? | I am being interfered with (interference from other stations) |
| **QRN** | Are you troubled by static? | I am troubled by static (atmospheric noise) |
| **QRO** | Shall I increase power? | Increase power |
| **QRP** | Shall I decrease power? | Decrease power / *also: low power ops (<5W)* |
| **QRQ** | Shall I send faster? | Send faster (___ WPM) |
| **QRS** | Shall I send more slowly? | Send more slowly (___ WPM) |
| **QRT** | Shall I stop sending? | Stop sending / I am closing my station |
| **QRU** | Have you anything for me? | I have nothing for you |
| **QRV** | Are you ready? | I am ready |
| **QRX** | When will you call me again? | Stand by / I will call at ___ hours |
| **QRZ** | Who is calling me? | You are being called by ___ |
| **QSB** | Are my signals fading? | Your signals are fading |
| **QSK** | Can you hear between signals? (break-in) | Yes, I can hear between your signals |
| **QSL** | Can you acknowledge receipt? | I acknowledge receipt / *also: QSL card* |
| **QSO** | Can you communicate with ___ direct? | I can communicate with ___ / Two-station contact |
| **QSP** | Will you relay to ___? | I will relay to ___ |
| **QST** | General call to all amateurs | (not used as statement) |
| **QSY** | Shall I change to another frequency? | Change to ___ kHz/MHz |
| **QTH** | What is your position/location? | My position/location is ___ |
| **QTR** | What is the correct time? | The correct time is ___ UTC |

---

## Anatomy of a CW Contact (QSO)

```
Station A                        Station B
─────────                        ─────────
CQ CQ CQ DE W1ABC K               (calling general)
                       W1ABC DE K1XYZ K    (replying)
K1XYZ DE W1ABC GD OM UR RST 599 BTname TOM
BT QTH BOSTON MA BT HW? AR K1XYZ DE W1ABC KN
                       W1ABC DE K1XYZ FB TOM RST 5 9 9
                       BT QTH NEW YORK NY BT HW? AR W1ABC DE K1XYZ KN
... (exchange)
K1XYZ DE W1ABC TNX QSO 73 SK W1ABC
                       73 SK K1XYZ
```

**Glossary**: CQ = general call. DE = from. OM = "old man" (friendly term). GD = good. UR = your. RST = readability/signal/tone. BT = break. HW = how (are you receiving me?). TNX = thanks. 73 = best regards. 88 = love and kisses. SK = end of contact.

---

## The Koch Method — Learning to Copy by Ear

The Koch method (Ludwig Koch, 1930s) is the modern standard for learning Morse:

```
┌──────────────────────────────────────────────────────────────┐
│                    KOCH METHOD                               │
│                                                              │
│  Step 1: Choose final target speed (20–25 WPM typical)      │
│  Step 2: Start with 2 letters only (K and M classically)     │
│  Step 3: Practice until 90% copy accuracy at full speed      │
│  Step 4: Add one new letter at a time                        │
│  Step 5: Never slow down — only add letters                  │
│                                                              │
│  Key insight: SPEED UP to learn, not slow down.             │
│  Slow Morse forces visual/counting recognition.             │
│  Fast Morse forces pattern/sound recognition (the goal).    │
│                                                              │
│  Tools: LCWO.net, G4FON Koch trainer, Morse Runner          │
└──────────────────────────────────────────────────────────────┘
```

**Farnsworth timing**: Letters sent at target speed but with longer inter-character and inter-word gaps. Lets ear learn letter sounds while giving extra time to write. Different from Koch (which uses normal gaps).

---

## Frequency of Letters — Why Morse is Nearly Huffman-Optimal

```
English letter frequency → Morse code length:

E (12.7%)  →  ·          1 unit  ←  most common = shortest
T  (9.1%)  →  —          1 unit
A  (8.2%)  →  ·—         3 units
O  (7.5%)  →  ———        5 units  ←  somewhat long
I  (7.0%)  →  ··         3 units
N  (6.7%)  →  —·         3 units
S  (6.3%)  →  ···        5 units  ←  somewhat long
H  (6.1%)  →  ····       7 units
R  (6.0%)  →  ·—·        5 units
...
Q  (0.1%)  →  ——·—       9 units  ←  rare = longest
Z  (0.1%)  →  ——··       9 units
X  (0.2%)  →  —··—       9 units
```

Not a perfect Huffman code (developed empirically, not mathematically), but closely approximates one for English. International Morse (1865) differed from American Morse (1844) precisely because international standardizers wanted better frequency optimization.

---

## International vs. American Morse

```
┌────────────────────────────────────────────────────────────┐
│  American Morse (1844, Morse/Vail)                         │
│  — Used on US land telegraph lines until mid-20th century  │
│  — Has "spaced dashes" (long vs short vs space variants)   │
│  — C, O, R, Y, Z differ from international                 │
│  — L = ·—· (not ·—··)                                      │
│                                                            │
│  International Morse (Continental, ITU 1865)               │
│  — Only two elements: dot and dash (simpler)               │
│  — Used globally for radio, maritime, amateur              │
│  — All modern Morse = International Morse                   │
└────────────────────────────────────────────────────────────┘
```

---

## Morse in Amateur Radio Context

**Bands and licensing**: In the US, CW (Morse) operation is permitted in specific sub-bands of every amateur band. The General class license (35 WPM no longer required since 2007 FCC rule change) grants CW privileges. CW is valued for narrow bandwidth and ability to dig out signals from noise.

**CW advantages**:
- Narrowest bandwidth of any voice/data mode (~100–200 Hz occupied BW vs 2.4 kHz for SSB voice)
- Readable at signal-to-noise ratios where voice communication fails completely
- No complex hardware — a straight key and a tube transmitter is enough

**Common CW frequencies (ITU Region 2, US)**:

| Band | CW Sub-band | Notes |
|------|-------------|-------|
| 80m | 3.500–3.525 MHz | CW-only segment |
| 40m | 7.000–7.025 MHz | CW-only segment |
| 20m | 14.000–14.025 MHz | Busiest CW band |
| 15m | 21.000–21.025 MHz | |
| 10m | 28.000–28.070 MHz | |

---

## Reading Morse by Sound — Rhythm Mnemonics

Memorizing the sound (not the symbol) is the goal. Common rhythm mnemonics:

| Letter | Sound | Spoken rhythm |
|--------|-------|---------------|
| A `·—` | dit-dah | "A-way" |
| B `—···` | dah-dit-dit-dit | "BIG-I-dig-it" or "BEA-ver" |
| C `—·—·` | dah-dit-dah-dit | "CA-na-DA-na" or "CA-dil-LAC-car" |
| D `—··` | dah-dit-dit | "DIG-it" or "DOG" |
| F `··—·` | dit-dit-dah-dit | "di-dit-DAH-dit" or "fi-ne-WOOD-nut" |
| K `—·—` | dah-dit-dah | "Ok-AY" |
| L `·—··` | dit-dah-dit-dit | "a-LONE-a-bit" |
| Q `——·—` | dah-dah-dit-dah | "GOD-SAVE-the-QUEEN" |
| R `·—·` | dit-dah-dit | "a-ROUND" or "a-RITH-met" |
| U `··—` | dit-dit-dah | "you-and-ME" |
| V `···—` | dit-dit-dit-dah | "Bee-tho-ven's FIFTH" (da-da-da-DAH) |
| X `—··—` | dah-dit-dit-dah | "EX-ca-va-TOR" |
| Y `—·——` | dah-dit-dah-dah | "why-NOT-I-SAID" |

---

## Decision Cheat Sheet

| Situation | What to use |
|-----------|-------------|
| General CW contact | CQ [3x] DE [call] K |
| End of over, want reply | AR, or K (any station), or KN (specific) |
| Copied, replying | DE [call] [content] AR [their call] DE [call] KN |
| Error in sending | HH (8 dots), then resend word |
| Strong QRM on frequency | QRL? before transmitting |
| Want to end contact | 73 SK |
| Acknowledge receipt | QSL |
| Signal report | RST: Readability (1-5), Strength (1-9), Tone (1-9) |
| Station at low power | QRP (conventionally < 5W) |
| General emergency | SOS (prosign, no gaps) or MAYDAY on voice |

---

## Common Confusion Points

**"SOS" is not `S` + `O` + `S`**. It is sent as a single prosign with no gaps: `···———···` as one continuous sequence. It's a prosign specifically chosen for its memorability (3+3+3) and asymmetry (detectable in any phase).

**"CQ" means "seek you"** — it's a general call, not an abbreviation. Historical origin from British Marconi: C/Q = "calling all stations" in early telegraph commercial usage.

**Morse is not encrypted**. Anyone knowing the code can decode it. This confuses people because of its use in WWII — the encryption was separate cipher systems (Enigma, SIGABA), with Morse used as the transmission medium.

**American Morse vs. International**: If you see spaced dashes or dots in old telegraph textbooks, that's American Morse. All modern use (amateur radio, ARRL, IARU) is International Morse (ITU). Don't mix them.

**Q-codes work for voice too**: On voice radio, an operator might say "QRM" out loud meaning "interference." Q-codes have migrated from their CW-only origin into general radio procedure vocabulary.

**73 vs. 88**: 73 = "best regards" (appropriate for all contacts). 88 = "love and kisses" (reserved for close personal acquaintances/family). Using 88 casually is a faux pas.
