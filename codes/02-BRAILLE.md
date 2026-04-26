# Braille — Complete Reference

## The Big Picture

Braille is a **6-dot tactile writing system** that encodes text and specialized notation (mathematics, music, computer data) into raised dot patterns on paper or embossed surfaces. Invented in 1824 by Louis Braille (age 15, French), it is the primary literacy system for blind and visually impaired people worldwide.

```
┌──────────────────────────────────────────────────────────────────┐
│                      BRAILLE SYSTEM MAP                          │
│                                                                  │
│  Grade 1 (Uncontracted)     Grade 2 (Contracted/UEB)             │
│  ┌──────────────────┐       ┌─────────────────────┐              │
│  │ 26 letters       │       │ Grade 1 +            │             │
│  │ 10 digits        │  ──→  │ 189 contractions     │             │
│  │ Punctuation      │       │ Short forms          │             │
│  │ Basic indicators │       │ More efficient        │             │
│  └──────────────────┘       └─────────────────────┘             │
│                                                                  │
│  Nemeth Code            Computer Braille (8-dot)                │
│  ┌──────────────┐       ┌──────────────────────┐               │
│  │ Mathematics  │       │ Full ASCII (256 chars)│              │
│  │ Science      │       │ Programming code     │               │
│  │ Technical    │       │ Braille display output│              │
│  └──────────────┘       └──────────────────────┘               │
│                                                                  │
│  Music Braille          Braille versions exist for:             │
│  ┌──────────────┐       Chess, Shorthand, Korean, Japanese      │
│  │ Pitch, rhythm│       Arabic, Hebrew, Chinese, Thai...        │
│  │ Dynamics     │       (each script has a Braille mapping)     │
│  └──────────────┘                                               │
└──────────────────────────────────────────────────────────────────┘
```

---

## The 6-Dot Cell

The fundamental unit of Braille is a 6-dot cell. Dots are numbered 1–6 in a fixed layout:

```
┌──────────────────────────────────────────────────────────┐
│                  BRAILLE CELL LAYOUT                     │
│                                                          │
│    Left column    Right column                           │
│                                                          │
│       ● ●         Dot 1  Dot 4                           │
│       ● ●         Dot 2  Dot 5                           │
│       ● ●         Dot 3  Dot 6                           │
│                                                          │
│    Dots are named by number:                             │
│    ·  ·  = no dots (space)                               │
│    ●  ·  = dot 1 only → letter 'a'                       │
│    ●  ●  = dots 1,4 → letter 'c'                         │
│    ● ● ● = dots 1,2,3 (left column full) → 'l'           │
│                                                          │
│  Physical specs (BANA standard):                         │
│  Cell width:  6.35mm    Cell height:  10.16mm            │
│  Dot spacing: 2.34mm (center-to-center within cell)      │
│  Inter-cell:  6.35mm (center-to-center horizontally)     │
│  Dot height:  0.48mm above paper surface                 │
│  Paper:       120–160 lb index stock (holds embossing)   │
└──────────────────────────────────────────────────────────┘
```

With 6 binary positions, 2⁶ = **64 possible cell configurations**. Grade 1 uses 63 of them (excluding the blank). Grade 2 reuses cells with meaning determined by context and indicator cells.

---

## Grade 1: The Full Alphabet

Cells are described by dot numbers (e.g., "1" = only dot 1 raised, "12" = dots 1 and 2 raised):

```
┌──────────────────────────────────────────────────────────────┐
│               GRADE 1 ALPHABET — DOT NUMBERS                 │
│                                                              │
│  a=1       b=12      c=14      d=145     e=15                │
│  f=124     g=1245    h=125     i=24      j=245               │
│                                                              │
│  k=13      l=123     m=134     n=1345    o=135               │
│  p=1234    q=12345   r=1235    s=234     t=2345              │
│                                                              │
│  u=136     v=1236    w=2456    x=1346    y=13456   z=1356    │
│                                                              │
│  PATTERN: letters a–j use only dots 1,2,4,5 (top 4 dots)   │
│           letters k–t = corresponding a–j + dot 3            │
│           letters u–z = corresponding k–t + dot 6            │
│           (w is irregular: j+6 would be 2456, which IS w)    │
│           (w was added for English; French Braille had no w) │
└──────────────────────────────────────────────────────────────┘
```

Visual representation of the alphabet using the cell grid:

```
a    b    c    d    e    f    g    h    i    j
●·   ●·   ●·   ●·   ●·   ●·   ●·   ●·   ··   ··
··   ●·   ··   ·●   ·●   ●·   ●·   ●·   ●·   ●·
··   ··   ··   ··   ··   ··   ·●   ··   ··   ·●

k    l    m    n    o    p    q    r    s    t
●·   ●·   ●·   ●·   ●·   ●·   ●·   ●·   ··   ··
··   ●·   ··   ·●   ·●   ●·   ●·   ●·   ●·   ●·
●·   ●·   ●·   ●·   ●·   ●·   ●●   ●·   ●·   ●·

u    v    w    x    y    z
●·   ●·   ··   ●·   ●·   ●·
··   ●·   ●·   ··   ·●   ·●
●●   ●●   ●●   ●●   ●●   ●●
```
*(● = raised dot, · = flat. Left col = dots 1,2,3 top-to-bottom; right col = dots 4,5,6)*

---

## Digits, Punctuation, and Indicators

### Number Indicator

Numbers use the **number indicator** cell (dots 3456) followed by letters a–j for digits 1–9, 0:

```
Number indicator: dots 3,4,5,6 = ··  (top-right empty, bottom full)
                                  ●●
                                  ●●

#1 = [3456][1]     (a cell = dot 1)
#2 = [3456][12]
#3 = [3456][14]
#4 = [3456][145]
#5 = [3456][15]
#6 = [3456][124]
#7 = [3456][1245]
#8 = [3456][125]
#9 = [3456][24]
#0 = [3456][245]   (j cell = dots 2,4,5)
```

### Capital Indicator

Single capital letter: dot 6 before the letter.
Multiple capitals: dots 6,6 (two capital indicators) before a sequence.
All-caps word: dots 6,6,6 (three capital indicators) — rarely used.

### Key Punctuation Cells

| Symbol | Dot numbers | Notes |
|--------|-------------|-------|
| `.` Period | 256 | |
| `,` Comma | 2 | Single dot-2 |
| `?` Question | 236 | |
| `!` Exclamation | 235 | |
| `:` Colon | 25 | |
| `;` Semicolon | 23 | |
| `"` Opening quote | 236 | Context-dependent |
| `"` Closing quote | 356 | |
| `(` Open paren | 2356 | |
| `)` Close paren | 2356 | (same as open — context determines) |
| `-` Hyphen | 36 | |
| `'` Apostrophe | 3 | Single dot-3 |

---

## Grade 2: Contracted Braille (UEB)

Grade 2 is **not a separate code** — it is Grade 1 with 189 additional contractions layered on top, standardized in **Unified English Braille (UEB)** adopted by most English-speaking countries since 2004–2016.

### Whole-Word Contractions (selected)

These single cells stand for complete common words when surrounded by spaces:

| Word | Cell (dot numbers) | Visual |
|------|-------------------|--------|
| `and` | 12346 | 5 dots |
| `for` | 123456 | all 6 dots |
| `of` | 12356 | |
| `the` | 2346 | |
| `with` | 23456 | |
| `a` | 1 | (same as letter a) |
| `but` | 12 | (same as b) |
| `can` | 14 | (same as c) |
| `do` | 145 | (same as d) |
| `every` | 15 | (same as e) |
| `from` | 124 | (same as f) |
| `go` | 1245 | (same as g) |
| `have` | 125 | (same as h) |
| `just` | 245 | (same as j) |
| `knowledge` | 13 | (same as k) |
| `like` | 123 | (same as l) |
| `more` | 134 | (same as m) |
| `not` | 1345 | (same as n) |
| `people` | 1234 | (same as p) |
| `quite` | 12345 | (same as q) |
| `rather` | 1235 | (same as r) |
| `so` | 234 | (same as s) |
| `that` | 2345 | (same as t) |
| `us` | 136 | (same as u) |
| `very` | 1236 | (same as v) |
| `will` | 2456 | (same as w) |
| `it` | 1346 | (same as x) |
| `you` | 13456 | (same as y) |
| `as` | 1356 | (same as z) |

### Partial-Word Contractions (letter group abbreviations)

Common letter groups contract to a single cell when used within words or standing alone:

| Letters | Dot numbers | Example |
|---------|-------------|---------|
| `ch` | 16 | "child" → [ch]ild |
| `gh` | 126 | "night" → ni[gh]t |
| `sh` | 146 | "she" → [sh]e |
| `th` | 1456 | "the" → [th]e |
| `wh` | 156 | "what" → [wh]at |
| `ed` | 1246 | "moved" → mov[ed] |
| `er` | 12456 | "paper" → pap[er] |
| `ou` | 1256 | "our" → [ou]r |
| `ow` | 246 | "below" → bel[ow] |
| `ing` | 346 | "reading" → read[ing] |
| `ar` | 345 | "art" → [ar]t |
| `ble` | 3456 | Wait — 3456 is number indicator; context-sensitive |
| `com` | 23 | "complete" → [com]plete |
| `con` | 25 | "condition" |
| `dis` | 256 | "discuss" |
| `en` | 26 | "end" |
| `in` | 35 | "into" |
| `ness` | 234 | "sadness" |
| `tion` | 2345 | "nation" |

Grade 2 ambiguities are resolved by position in word and surrounding context. Skilled Braille readers disambiguate at reading speed (200+ WPM) without conscious effort — the same way skilled readers of abbreviated text infer meaning from context.

---

## Nemeth Code

Developed by Abraham Nemeth (1965), Nemeth Code is the Braille standard for **mathematics and scientific notation**. It uses the same 6-dot cell but assigns completely different meanings to most cells in "Nemeth mode":

```
Nemeth mode is entered/exited with specific indicator cells:
  Enter Nemeth:  ⠀⠸⠩⠀  (dots 456 then 146, surrounded by spaces)
  Exit Nemeth:   ⠀⠸⠱⠀  (dots 456 then 1245 6)
```

### Nemeth Digits

Nemeth uses **lower-cell digits** (dots in the bottom two rows):

| Digit | Dots | Grade 1 letter equivalent |
|-------|------|--------------------------|
| 0 | 356 | none |
| 1 | 2 | (comma) |
| 2 | 23 | (semicolon) |
| 3 | 25 | colon / `con` shortform |
| 4 | 256 | |
| 5 | 26 | |
| 6 | 235 | |
| 7 | 2356 | |
| 8 | 236 | |
| 9 | 35 | |

### Nemeth Operators

```
+  =  dots 346
-  =  dots 36 (same as hyphen, but context is Nemeth mode)
×  =  dots 16
÷  =  dots 12346
=  =  dots 2356
<  =  dots 126
>  =  dots 345
√  =  dots 345 then 146 (multi-cell)
∫  =  two-cell sequence
```

Nemeth handles: fractions, exponents, subscripts, Greek letters (α, β, γ…), matrices, chemical formulas. It's complex — trained transcribers specialize in it. Key insight: Nemeth is to mathematics what LaTeX is to sighted typesetting — a complete symbolic representation system for technical content.

---

## Computer Braille (8-Dot)

Computer Braille (also called Braille ASCII, Grade 0, or BRF — Braille Ready Format) adds dots **7 and 8** below the standard 6:

```
Standard 6-dot cell:  ● ●    Computer 8-dot cell:  ● ●
                      ● ●                           ● ●
                      ● ●                           ● ●
                                                    ● ●  ← dots 7 and 8
```

With 8 binary positions, 2⁸ = **256 possible cells**, mapping directly to 7-bit ASCII (128 chars) or extended character sets. Dot 7 typically represents lowercase shift; dots 7+8 represent uppercase. Computer Braille appears on refreshable Braille displays (electronic devices with 40–80 cells of piezoelectric pins that rise/fall in real-time).

**Refreshable Braille displays** connect to computers/smartphones via USB or Bluetooth and render screen content. They're used by screen reader users (JAWS, NVDA on Windows; VoiceOver on macOS/iOS) who prefer tactile reading to text-to-speech.

---

## Reading and Embossing

### Braille Reading Speed

- Average sighted person learning Braille: 50–80 WPM after 1–2 years
- Average blind reader (Grade 2): 125–200 WPM
- Expert blind reader: 400+ WPM (faster than most sighted reading)
- Profoundly deaf-blind readers (tactile signing): 100–130 WPM

The speed advantage of Grade 2 over Grade 1 is ~35% (mirroring dictionary compression ratios).

### Physical Production

```
┌──────────────────────────────────────────────────────────────┐
│            BRAILLE EMBOSSING METHODS                         │
│                                                              │
│  Personal embosser (home/office):                            │
│  — Interpoint embosser: dots on both sides, interlaced       │
│  — Single-sided: less efficient, easier to produce           │
│  — Speed: 10–50 pages/minute                                 │
│  — Cost: $1,000–$5,000                                       │
│                                                              │
│  Industrial embosser:                                        │
│  — High-volume: textbook production                          │
│  — Speed: 800+ pages/hour                                    │
│                                                              │
│  Braille paper:                                              │
│  — Weight: 90–160 gsm (heavier than copier paper)            │
│  — Dots last ~2 years with heavy use before flattening       │
│  — Wet conditions collapse dots faster                       │
│                                                              │
│  Braille slate and stylus (manual):                          │
│  — Metal or plastic template with 6-dot wells                │
│  — Punch from right to left (mirror image)                   │
│  — Turn over to read left-to-right                           │
│  — The pencil-and-paper equivalent for Braille               │
└──────────────────────────────────────────────────────────────┘
```

---

## Braille Around the World

Braille was created for French and is adapted for virtually every language. Key facts:

| Script | Braille system | Notes |
|--------|---------------|-------|
| English | UEB (Unified English Braille) | Replaced multiple conflicting systems in 2016 |
| French | French Braille | Origin system; closely related to English |
| German | German Braille | |
| Japanese | Japanese Braille | Based on phonetic kana, not kanji |
| Korean | Korean Braille | Based on hangul syllable structure |
| Arabic | Arabic Braille | Right-to-left script mapped to standard cells |
| Chinese (Mandarin) | Two systems: Mandarin Braille (phonetic) | Uses pinyin sounds |
| Hebrew | Hebrew Braille | |
| Greek | Greek Braille | |

Braille is script-agnostic at the cell level — any culture can define its own cell-to-phoneme mapping. The physical cell, dot numbering, and reading direction (left-to-right, regardless of source script) are universal.

---

## UEB vs. Earlier Systems

Before UEB, English Braille had three competing systems (US, UK, and others), creating a translation problem — a book embossed in American Grade 2 wasn't identical to the same book in British Grade 2. UEB resolved this and was adopted:
- Australia, New Zealand, UK: 2004
- US, Canada: 2016
- Still in transition in some institutions

Old grade 2 is called **English Braille, American Edition (EBAE)** in the US. Most pre-2016 textbooks use EBAE. Both are readable by competent Grade 2 readers.

---

## Decision Cheat Sheet

| Use Case | Braille Grade/Type |
|----------|--------------------|
| Literary text, general reading | Grade 2 / UEB |
| Letter-by-letter transcription learning | Grade 1 |
| Mathematics, science, technical | Nemeth Code (US) or UEB Math |
| Computer output, screen reader | Computer Braille (8-dot) / BRF |
| Music score | Music Braille (separate standard) |
| Non-English language | Language-specific Braille standard |
| Tactile graphics | Braille line drawings + Grade 1/2 labels |

---

## Common Confusion Points

**Braille is not universal across languages**. Each language has its own Braille system. The 6-dot physical format is universal; the cell meanings are not.

**Grade 2 is not shorthand** — it's fully unambiguous in context. The same cell means different things in different positions (standalone word vs. within a word), but a trained reader has no ambiguity, just as English readers interpret "lead" differently as noun vs. verb from context.

**Braille displays don't replace screen readers**. They work in tandem. The screen reader (JAWS, VoiceOver) interprets the UI and feeds text to the Braille display (and/or speech). Braille display users often turn off speech and use the display alone for silent reading.

**Dot 6 alone is NOT a letter**. Dot 6 is the capital indicator. This is why capital letters take 2 cells each in Grade 1: indicator + letter. Names, start-of-sentences, etc., always take more space than lowercase.

**Nemeth Code is a distinct mode, not a superset**. When you enter Nemeth mode, the Grade 2 contraction rules no longer apply. You can't mix Grade 2 contractions inside a Nemeth expression. The indicator cells switch modes explicitly.
