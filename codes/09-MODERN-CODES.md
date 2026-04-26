# Modern Machine-Readable Codes & Marking Systems

## The Big Picture

Modern codes are optimized for **machine reading**, not human reading. The shift from human-decoded systems (Morse, semaphore) to machine-decoded systems (barcodes, QR) happened in the 1970s with laser scanners and CCD cameras. The defining requirement: encode enough redundancy that physical damage, printing imperfections, or partial obstruction don't cause decoding failures.

```
┌──────────────────────────────────────────────────────────────────┐
│              MODERN CODE TAXONOMY                                │
│                                                                  │
│  1D LINEAR BARCODES                                              │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ UPC-A, UPC-E, EAN-13, EAN-8 — retail products            │   │
│  │ Code 128, Code 39 — industrial/logistics                  │   │
│  │ ITF-14 — outer cartons and pallets                        │   │
│  │ ISBN barcode — books (EAN-13 + price EAN-5 supplement)    │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  2D MATRIX CODES                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ QR Code — URLs, contact cards, payments                  │   │
│  │ Data Matrix — manufacturing, small parts, pharmaceuticals│   │
│  │ Aztec Code — transport tickets (Eurostar, Amtrak)        │   │
│  │ PDF417 — ID documents, shipping labels                   │   │
│  │ MaxiCode — UPS sorting system                            │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  PROXIMITY/WIRELESS                                              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ NFC (ISO 18092) — payments, access, tags                 │   │
│  │ RFID (ISO 15693) — passive tags, supply chain            │   │
│  │ Bluetooth LE — proximity sensing                         │   │
│  │ iBeacon / Eddystone — location beacons                   │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  COMPONENT MARKING                                               │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ Resistor color bands — resistance + tolerance            │   │
│  │ Capacitor markings — capacitance + voltage rating        │   │
│  │ Wire color codes — circuit function identification       │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  REGULATORY/SAFETY                                               │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ ISO 7010 — safety pictograms                             │   │
│  │ MUTCD — US road sign system                              │   │
│  │ Vienna Convention — international road sign system       │   │
│  │ Tactile paving — pedestrian navigation                   │   │
│  └──────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────┘
```

---

## EAN-13 Barcode

The global standard for retail product identification, managed by GS1.

```
┌──────────────────────────────────────────────────────────────────┐
│                    EAN-13 STRUCTURE                              │
│                                                                  │
│  13 digits total: [GS1 Prefix][Company Code][Item Ref][Check]    │
│                   ─────────────────────────────────────────────  │
│                   D1 D2 D3 D4 D5 D6 D7 D8 D9 D10 D11 D12 | D13   │
│                                                                  │
│  GS1 prefix (2–3 digits): country/organization of GS1 member     │
│  — 0xx = USA/Canada                                              │
│  — 3xx = France                                                  │
│  — 400–440 = Germany                                             │
│  — 45x/49x = Japan                                               │
│  — 690–699 = China                                               │
│  — 978/979 = Books (ISBN)                                        │
│  — 977 = Periodicals (ISSN)                                      │
│                                                                  │
│  Company code + Item reference: variable split based on          │
│  GS1 membership tier                                             │
│                                                                  │
│  Check digit (D13): calculated by algorithm:                     │
│  1. Multiply alternate digits by 1 and 3                         │
│     (positions 1,3,5,7,9,11 × 1; positions 2,4,6,8,10,12 × 3)    │
│  2. Sum all 12 weighted values                                   │
│  3. Find what makes sum + check_digit divisible by 10            │
│     check = (10 - (sum mod 10)) mod 10                           │
│                                                                  │
│  Example: 978-0-306-40615-? (a book ISBN → EAN-13)               │
│  9×1 + 7×3 + 8×1 + 0×3 + 3×1 + 0×3 + 6×1 + 4×3 + 0×1 + 6×3       │
│  + 1×1 + 5×3 = 9+21+8+0+3+0+6+12+0+18+1+15 = 93                  │
│  Check = (10 - (93 mod 10)) mod 10 = (10-3) mod 10 = 7           │
│  → 9780306406157                                                 │
└──────────────────────────────────────────────────────────────────┘
```

### Physical Barcode Encoding

```
EAN-13 visual structure:
  ║║ (left guard = 101)
  [6 digits left half, encoded in set A or B based on 1st digit]
  ║  ║ (center guard = 01010)
  [6 digits right half, encoded in set C = inverted A]
  ║║ (right guard = 101)

Each digit = 7 modules (black or white bars)
3 encoding sets exist (A, B, C) — the pattern of which sets are
used in the left half encodes the 1st digit of the 13.

Total width: 95 modules + 2×11 quiet zone = 117 modules minimum
Standard width: 37.29mm at magnification 1.0 (80% to 200% acceptable)
```

### UPC-A vs. EAN-13

```
UPC-A: 12 digits (used in US/Canada)
EAN-13: 13 digits (global) = UPC-A with a leading 0 prepended
Scanners at checkout typically read both identically.
EAN-8: short version for small products (8 digits)
```

---

## QR Code

Invented 1994 by Masahiro Hara at Denso Wave (Toyota supplier) for tracking automotive parts. "QR" = Quick Response.

### Structure

```
┌──────────────────────────────────────────────────────────────────┐
│                    QR CODE ANATOMY                               │
│                                                                  │
│  ┌─────┐  . . . . . .  ┌─────┐                                   │
│  │■■■■■│  . . . . . .  │■■■■■│   FINDER PATTERNS (3 corners)    │
│  │■   ■│  . . . . . .  │■   ■│   7×7 squares with white border  │
│  │■ ■ ■│  . . . . . .  │■ ■ ■│   Unique pattern; tells scanner  │
│  │■   ■│  . . . . . .  │■   ■│   orientation and scale          │
│  │■■■■■│  . . . . . .  │■■■■■│                                  │
│  └─────┘  . . . . . .  └─────┘                                  │
│  . . . . . FORMAT INFO . . . . .   FORMAT INFORMATION STRIP      │
│  . ■■■■■ . ─────────── . ■■■■■ .  (error level + mask pattern)  │
│  . . . . . . . . . . . . . . . .                                 │
│  . . . . . . . . . . . . . . . .  DATA AREA (variable)          │
│  . . . . . . . . . . . . . . . .                                 │
│  . . . . ■ . . . . . . . . . . .  ALIGNMENT PATTERN             │
│  . . . . . . . . . . . . . . . .  (larger QR codes have more)   │
│  ┌─────┐  . . . . . . . . . . .                                  │
│  │■■■■■│  . . . . . . . . . . .  TIMING PATTERNS                │
│  │■   ■│  (alternating ■·■·■ strips for coordinate reference)   │
│  │■ ■ ■│                                                        │
│  │■   ■│  ── QUIET ZONE: 4-module white border on all sides     │
│  │■■■■■│                                                        │
│  └─────┘                                                        │
└──────────────────────────────────────────────────────────────────┘
```

### Versions and Capacity

```
Version = size, from 1 (21×21 modules) to 40 (177×177 modules)

┌──────────────────────────────────────────────────────────────┐
│         QR CODE CAPACITY vs. VERSION                         │
├─────────┬──────────────┬────────────────────────────────────┤
│ Version │  Size        │  Max numeric / alphanumeric / byte  │
├─────────┼──────────────┼────────────────────────────────────┤
│    1    │  21×21       │  41 / 25 / 17                      │
│    3    │  29×29       │  127 / 77 / 53                     │
│    5    │  37×37       │  277 / 167 / 115                   │
│   10    │  57×57       │  652 / 395 / 271                   │
│   20    │  97×97       │  1817 / 1096 / 754                 │
│   30    │  137×137     │  3057 / 1985 / 1367                │
│   40    │  177×177     │  7089 / 4296 / 2953                │
└─────────┴──────────────┴────────────────────────────────────┘
```

### Error Correction Levels

```
Level L (Low):       ~7% data modules can be lost/damaged
Level M (Medium):   ~15% recoverable
Level Q (Quartile): ~25% recoverable
Level H (High):     ~30% recoverable

Higher error correction = more redundant data = lower payload capacity

Reed-Solomon error correction is used (same algorithm as:
— CD audio data correction
— DVB digital TV broadcasting
— Spacecraft telemetry (Voyager, Cassini)
— Blu-ray disc data recovery)

This is why QR codes with logos or partial damage still scan:
the logo replaces data modules, but Reed-Solomon rebuilds them.
Maximum logo area ≈ 30% (at Level H) without failure.
```

### Data Encoding Modes

```
Numeric: digits 0–9 only → 3.3 bits/char (most efficient)
  Encodes 3 digits per 10 bits (1000 combinations in 10 bits)

Alphanumeric: 0–9, A–Z, space, $%*+-./: → 5.5 bits/char
  Encodes 2 chars per 11 bits

Byte: full ISO 8859-1 / UTF-8 → 8 bits/char
  Any character but least efficient

Kanji: Shift-JIS Japanese characters → 13 bits/char
  Optimized for Japanese content

Mixed: QR can switch modes within one code for efficiency
```

---

## Data Matrix

2D code alternative to QR; dominant in manufacturing, pharma, and aerospace:

```
┌──────────────────────────────────────────────────────────────┐
│                DATA MATRIX OVERVIEW                          │
│                                                              │
│  Structure:                                                  │
│  ┌─────────────────────┐                                     │
│  │■■■■■■■■■■■■■■       │  Solid "L" border (finder)         │
│  │■                ·   │  Alternating border (clock)        │
│  │■   DATA AREA    ·   │  Data in interior cells            │
│  │■                ·   │                                    │
│  │■■■■■■■■■■■■■■       │                                    │
│  └─────────────────────┘                                     │
│                                                              │
│  Shape: typically square but rectangular also supported      │
│  Range: 10×10 to 144×144 cells                              │
│  Capacity (max): 2335 alphanumeric / 3116 numeric chars     │
│  Error correction: Reed-Solomon (up to 25% damage recovery)  │
│                                                              │
│  Advantages over QR:                                         │
│  — Smaller physical size for same data capacity              │
│  — Can be laser-etched or dot-peened directly on metal parts │
│  — ISO 16022 standard                                        │
│  — GS1 Data Matrix: standard for pharma unit-of-sale codes  │
│                                                              │
│  Common uses:                                                │
│  — Direct part marking on aerospace/medical/defense parts    │
│  — FDA UDI (Unique Device Identification) on medical devices │
│  — Pharmaceutical serialization (track-and-trace)           │
│  — US DOD MIL-STD-130 component marking                     │
└──────────────────────────────────────────────────────────────┘
```

---

## NFC (Near Field Communication)

NFC is a short-range (≤4 cm) wireless communication standard derived from RFID. Based on ISO 18092 / ISO 14443.

```
┌──────────────────────────────────────────────────────────────────┐
│                    NFC SYSTEM MAP                                │
│                                                                  │
│  Frequency: 13.56 MHz (ISM band, globally available)             │
│  Range: 1–4 cm (security through proximity)                      │
│  Data rate: 106, 212, 424, or 848 kbps                           │
│  Standard: ISO/IEC 18092, ISO/IEC 14443                          │
│                                                                  │
│  THREE OPERATING MODES:                                          │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │ Card Emulation Mode:                                      │  │
│  │ Device behaves like a passive NFC tag                    │  │
│  │ Use case: contactless payment (Apple Pay, Google Pay)    │  │
│  │ Secure Element stores payment credentials                │  │
│  ├───────────────────────────────────────────────────────────┤  │
│  │ Reader/Writer Mode:                                       │  │
│  │ Device powers and reads passive NFC tags                  │  │
│  │ Use case: scanning product tags, transit cards, posters   │  │
│  │ Android/iOS apps can read NDEF-formatted tags             │  │
│  ├───────────────────────────────────────────────────────────┤  │
│  │ Peer-to-Peer Mode:                                        │  │
│  │ Two powered devices exchange data                        │  │
│  │ Use case: Android Beam (deprecated), contact sharing     │  │
│  │ Less common; Bluetooth used instead for larger transfers │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
│  NDEF (NFC Data Exchange Format):                                │
│  Standard record format for NFC content                         │
│  Record types: URL, text, vCard, MIME type, launch app          │
│  Max tag capacity: depends on tag type (NTAG215 = 504 bytes)    │
└──────────────────────────────────────────────────────────────────┘
```

### NFC Tag Types

```
┌──────────────────────────────────────────────────────┐
│  NFC TAG TYPES (ISO/IEC standards)                   │
├───────────┬──────────────┬────────────────────────── ┤
│ Type 1    │ ISO 14443A   │ 96B–2kB; read/write; low cost│
│ Type 2    │ ISO 14443A   │ 48B–2kB; NXP MIFARE Ultra  │
│ Type 3    │ JIS X 6319-4 │ FeliCa (Sony); transit in  │
│           │              │ Japan (Suica, Pasmo)        │
│ Type 4    │ ISO 14443A/B │ 32kB; Java Card; high sec  │
│ Type 5    │ ISO 15693    │ 1m range (actually RFID)   │
│           │              │ Inventory, library tags     │
└───────────┴──────────────┴────────────────────────── ┘
```

### NFC vs. RFID

```
┌──────────────────────────────────────────────────────────────┐
│  NFC vs. RFID — COMPARISON                                   │
├─────────────────────┬────────────────────────────────────────┤
│  NFC                │ RFID                                   │
├─────────────────────┼────────────────────────────────────────┤
│ 13.56 MHz only      │ LF (125kHz), HF (13.56MHz), UHF        │
│                     │ (860–960MHz), microwave (2.45GHz)      │
│ ≤4 cm range         │ LF: 10cm; HF: 1m; UHF: 1–12m           │
│ Bidirectional (P2P) │ Unidirectional (reader → tag)          │
│ Peer-to-peer mode   │ No peer-to-peer                        │
│ Smart devices built-│ Requires dedicated reader hardware     │
│ in (phones/watches) │                                        │
│ ISO 18092           │ ISO 15693 (HF); ISO 18000-6 (UHF)      │
│ Payment, transit,   │ Supply chain, inventory, animal tag,   │
│ access control      │ vehicle tracking (EZPass/FastTrack)    │
└─────────────────────┴────────────────────────────────────────┘
```

---

## Resistor Color Code

4-band and 5-band resistor color codes encode resistance value and tolerance:

```
┌──────────────────────────────────────────────────────────────────┐
│                RESISTOR COLOR CODE                               │
│                                                                  │
│  COLOR BAND TABLE:                                               │
│                                                                  │
│  Color      Digit  Multiplier      Tolerance (5th band)          │
│  ─────────  ─────  ────────────    ────────────────────          │
│  Black        0      ×1 (10⁰)      —                             │
│  Brown        1      ×10 (10¹)     ±1%  (F)                      │
│  Red          2      ×100 (10²)    ±2%  (G)                      │
│  Orange       3      ×1k (10³)     ±0.05% (rare)                 │
│  Yellow       4      ×10k (10⁴)   ±0.02% (rare)                  │
│  Green        5      ×100k (10⁵)  ±0.5% (D)                      │
│  Blue         6      ×1M (10⁶)    ±0.25% (C)                     │
│  Violet       7      ×10M (10⁷)   ±0.1% (B)                      │
│  Gray         8      ×100M (10⁸)  ±0.05% (A)                     │
│  White        9      ×1G (10⁹)    —                              │
│  Gold         —      ×0.1          ±5%  (J)                      │
│  Silver       —      ×0.01         ±10% (K)                      │
│  (no band)   —      —              ±20% (M)                      │
│                                                                  │
│  4-BAND RESISTOR: [Band1][Band2][Multiplier][Tolerance]          │
│  Example: Red-Red-Brown-Gold = 2,2,×10, ±5% = 220Ω ±5%           │
│                                                                  │
│  5-BAND RESISTOR: [Band1][Band2][Band3][Multiplier][Tolerance]   │
│  Example: Brown-Black-Black-Brown-Brown = 1,0,0,×10,±1%          │
│           = 1000Ω = 1kΩ ±1%                                      │
│                                                                  │
│  6-BAND RESISTOR: adds temperature coefficient                   │
│  (6th band, usually on precision resistors)                      │
└──────────────────────────────────────────────────────────────────┘
```

### Mnemonics

```
Standard mnemonic for 0–9:
"Bad Boys Race Our Young Girls But Violet Goes West"
B  B   R   O   Y   G   B   V   G   W
0  1   2   3   4   5   6   7   8   9

Alternative: "Big Beautiful Roses Often Yield Great Bright Violets Generally Win"
Many variants exist; pick one and stick to it.
```

---

## Wire Color Standards

Wire color coding is NOT globally standardized — it varies significantly by country and application:

```
┌──────────────────────────────────────────────────────────────────┐
│           WIRE COLOR CODES BY CONTEXT                            │
│                                                                  │
│  AC MAINS POWER (IEC 60446 — EU standard, adopted 2003+):        │
│  Phase (Live):    Brown                                          │
│  Neutral:         Blue                                           │
│  Earth (Ground):  Green/Yellow stripe                            │
│                                                                  │
│  AC MAINS POWER (Pre-2004 UK / old British standard):            │
│  Phase:    Red                                                   │
│  Neutral:  Black                                                 │
│  Earth:    Green (no stripe)                                     │
│                                                                  │
│  AC MAINS POWER (US/Canada, NEC):                                │
│  Hot (Line 1):     Black                                         │
│  Hot (Line 2):     Red (in 240V circuits)                        │
│  Neutral:          White or Gray                                 │
│  Ground:           Green or Bare                                 │
│  * Single-phase: Black(hot), White(neutral), Green/Bare(ground)  │
│  * 3-phase: Black, Red, Blue (L1, L2, L3) + White(N) + Green(G)  │
│                                                                  │
│  DC AUTOMOTIVE (12V/24V vehicle systems):                        │
│  Positive (+):     Red                                           │
│  Negative (─):     Black                                         │
│  Ground:           Black (same as negative in single-ground)     │
│  (Additional colors vary by vehicle manufacturer)                │
│                                                                  │
│  DC ELECTRONICS (typical PCB/breadboard convention):             │
│  Positive:         Red                                           │
│  Negative/Ground:  Black                                         │
│  Signal:           Other colors (application-specific)           │
│                                                                  │
│  ETHERNET (TIA/EIA-568):                                         │
│  568A: W-Green/Green, W-Orange/Blue, W-Blue/Orange, W-Brown/Brown│
│  568B: W-Orange/Orange, W-Green/Blue, W-Blue/Green, W-Brown/Brown│
│  (T568B more common in US commercial installations)              │
└──────────────────────────────────────────────────────────────────┘
```

---

## Road Sign Systems

Two major competing standards for road sign design:

```
┌──────────────────────────────────────────────────────────────────┐
│              ROAD SIGN SYSTEMS COMPARISON                        │
├─────────────────────────────┬────────────────────────────────────┤
│  MUTCD (USA/Canada)         │  Vienna Convention (150+ countries) │
├─────────────────────────────┼────────────────────────────────────┤
│  Text-based primarily       │  Symbol-based primarily            │
│  Sign shapes carry meaning  │  Sign shapes + colors carry meaning│
│  Specific fonts mandated    │  No specific font standard         │
│  (Highway Gothic, Clearview)│                                    │
├─────────────────────────────┼────────────────────────────────────┤
│  SHAPES:                    │  SHAPES:                           │
│  Octagon = STOP             │  Red inverted triangle = YIELD      │
│  Triangle (US) = YIELD      │  Red circle + bar = prohibition    │
│  Diamond = WARNING           │  Triangle = warning (yellow/white) │
│  Rectangle = regulatory info│  Rectangle = information           │
│  Pentagon = school zone     │  Circular blue = positive command  │
│  Pennant = no passing zone  │                                    │
├─────────────────────────────┼────────────────────────────────────┤
│  COLORS:                    │  COLORS:                           │
│  Red = STOP/PROHIBITION     │  Red = STOP/PROHIBITION            │
│  Yellow = WARNING           │  Yellow/Orange = WARNING           │
│  Orange = construction      │  Blue = mandatory instruction      │
│  Green = guide/direction    │  Green = direction/guide           │
│  Blue = services/info       │  Brown = tourist/cultural          │
│  Brown = recreational/cultural│                                  │
│  White = regulatory         │                                    │
└─────────────────────────────┴────────────────────────────────────┘
```

### ISO 7010 Safety Pictograms

ISO 7010 is the international standard for safety signs in workplaces and public buildings. All pictograms follow strict rules:

```
┌──────────────────────────────────────────────────────────────┐
│              ISO 7010 SIGN CATEGORIES                        │
│                                                              │
│  PROHIBITION (circular, red border, red diagonal bar):       │
│  P001 = No smoking                                           │
│  P003 = No open flame                                        │
│  P002 = No naked flame; fire, open ignition source           │
│                                                              │
│  WARNING (triangular, yellow/amber, black symbol):           │
│  W001 = Flammable material                                   │
│  W004 = Corrosive substance                                  │
│  W011 = High voltage                                         │
│  W027 = Radiation hazard                                     │
│                                                              │
│  MANDATORY (circular, blue, white symbol):                   │
│  M001 = Eye protection must be worn                          │
│  M003 = Safety helmet must be worn                           │
│  M010 = Wear safety footwear                                 │
│                                                              │
│  SAFE CONDITION (rectangular/square, green, white symbol):   │
│  E001 = Emergency exit left/right                            │
│  E003 = First aid                                            │
│  E004 = Stretcher                                            │
│                                                              │
│  FIRE EQUIPMENT (rectangular, red background):               │
│  F001 = Fire extinguisher                                    │
│  F002 = Fire hose reel                                       │
│  F003 = Fire ladder                                          │
└──────────────────────────────────────────────────────────────┘
```

---

## Tactile Paving

Ground surface indicators for visually impaired pedestrians. Internationally standardized but implementation varies by country:

```
┌──────────────────────────────────────────────────────────────────┐
│                TACTILE PAVING PATTERNS                           │
│                                                                  │
│  HAZARD WARNING (Blister/Truncated dome pattern):                │
│  ○ ○ ○ ○ ○ ○    Small round bumps (domes)                        │
│  ○ ○ ○ ○ ○ ○    Grid pattern                                     │
│  ○ ○ ○ ○ ○ ○                                                     │
│                                                                  │
│  Meaning: STOP — hazard ahead                                    │
│  Used at: curb ramps, road crossings, platform edges, stairs,    │
│           escalator approaches, hazardous level changes          │
│                                                                  │
│  DIRECTIONAL (Bar/Corduroy pattern):                             │
│  ─────────────────────────────────                               │
│  ─────────────────────────────────    Parallel bars/ribs         │
│  ─────────────────────────────────    perpendicular to walk dir  │
│  ─────────────────────────────────                               │
│                                                                  │
│  Meaning: SAFE — walkable direction, follow bars                 │
│  Used at: transit platforms, pedestrian paths, shopping areas    │
│                                                                  │
│  COLOR:                                                          │
│  Yellow preferred (contrast against most ground surfaces)        │
│  Some countries: brick red or high-contrast to surrounding floor │
│                                                                  │
│  Standards:                                                      │
│  ISO 23599 — general standard                                    │
│  ADA (US): dome dimensions, placement at curb ramps              │
│  JASSO (Japan): pioneered tactile paving (Seiichi Miyake 1965)   │
│  BS 8300 (UK), DIN 32984 (Germany)                               │
└──────────────────────────────────────────────────────────────────┘
```

---

## Hazmat Placards (DOT/UN/GHS)

Hazardous material coding is regulated internationally through three parallel systems:

```
┌──────────────────────────────────────────────────────────────┐
│          HAZMAT CODING SYSTEMS                               │
├─────────────────────────────────────────────────────────────┤
│  DOT (US Department of Transportation):                     │
│  — Orange diamond placard on vehicles                       │
│  — UN number (4-digit, 1001–3520+) identifies substance     │
│  — Hazard class (1–9) on top half of placard                │
│  — 9 hazard classes: Explosives(1), Gases(2), Flammable     │
│    liquids(3), Flammable solids(4), Oxidizers(5), Toxics(6),│
│    Radioactive(7), Corrosives(8), Misc(9)                   │
│                                                             │
│  GHS (Globally Harmonized System, UN/OSHA):                 │
│  — 9 physical, 10 health, 2 environmental hazard pictograms │
│  — Used on chemical SDS (Safety Data Sheets) and labels     │
│  — Flame symbol, skull, exclamation, health hazard, etc.   │
│                                                             │
│  NFPA 704 "Fire Diamond" (US):                              │
│  — Square rotated 45° (diamond shape)                       │
│  — 4 quadrants: Blue=Health, Red=Flammability,              │
│                  Yellow=Instability/Reactivity, White=Special│
│  — 0–4 severity scale for each quadrant                    │
│  — Special codes: W (water reactive), OX (oxidizer),        │
│                   SA (simple asphyxiant)                    │
└──────────────────────────────────────────────────────────────┘
```

---

## Decision Cheat Sheet

| Situation | Code to use |
|-----------|-------------|
| Retail product identification | EAN-13 (global) / UPC-A (US) |
| Book identification | ISBN-13 (= EAN-13 with 978/979 prefix) |
| URL/text for smartphone scan | QR Code (high density, universal) |
| Industrial part marking, small area | Data Matrix |
| Transport tickets | Aztec Code or PDF417 |
| NFC payment | ISO 14443 Type A/B (Visa/MC/Amex contactless) |
| Inventory tracking, longer range | UHF RFID (ISO 18000-6) |
| Electronic component value | Resistor color bands (4/5-band) |
| US residential AC wiring | NEC: Black=hot, White=neutral, Green/bare=ground |
| EU AC mains wiring | IEC 60446: Brown=live, Blue=neutral, Green-yellow=earth |
| Workplace safety sign | ISO 7010 pictogram |
| Road sign (US) | MUTCD standard |
| Navigation aid for blind users | Tactile paving (ISO 23599) |
| Chemical hazard label | GHS/SDS pictogram |

---

## Common Confusion Points

**QR codes are region-free**: A QR code scanned in Tokyo reads the same as scanned in Toronto. The data format is global. URLs embedded in QR codes may redirect region-specifically, but that's the web server, not the QR code.

**EAN-13 prefix ≠ product country of origin**: The GS1 prefix identifies the GS1 member country (where the brand registered), not where the product was manufactured. A "400–440" (Germany) prefix could be on goods manufactured anywhere.

**NFC is NOT Bluetooth**: NFC (13.56 MHz, ≤4cm, passive) and Bluetooth (2.4 GHz, up to 100m, both devices must be powered) are completely different radio technologies. NFC payment works because the point-of-sale terminal powers the passive tag in your phone/card via inductive coupling.

**Wire color codes are not globally standardized**: The EU switched to IEC 60446 (Brown=live, Blue=neutral) in 2004. Old UK wiring (Red=live, Black=neutral) still exists in older buildings. US wiring (Black=hot, White=neutral) differs from both. Working on electrical systems abroad: ALWAYS measure before assuming color conventions.

**Resistor color-code orientation**: Reading direction matters. The tolerance band (gold/silver/brown) is always on the right end. Hold the resistor with tolerance band on the right and read left-to-right. On 5-band resistors, tolerance bands are sometimes ambiguous — check the resistor's markings or measure with a multimeter when uncertain.

**QR logo damage and error correction**: Adding a logo to a QR code deliberately damages data modules. This works if the error correction level (L/M/Q/H) provides enough redundancy. At Level H (30% recoverable), logos up to ~25–28% of the data area are generally safe. QR generators that add logos should automatically select Level H — verify this if creating branded QR codes.
