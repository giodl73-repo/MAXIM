# Semaphore — Visual Distance Signaling

## The Big Picture

Semaphore encodes the alphabet into **spatial positions** of arms, flags, or mechanical shutters. Unlike Morse (which encodes in time), semaphore encodes in space — the configuration visible at a single moment. Multiple distinct semaphore systems exist:

```
┌──────────────────────────────────────────────────────────────────┐
│                    SEMAPHORE SYSTEM MAP                          │
│                                                                  │
│  FLAG SEMAPHORE (most familiar)                                  │
│  Two handheld flags, arm positions encode letters                │
│  Range: ~3 km with flags; ~10 km with Aldis lamp                 │
│  Speed: ~20–30 characters/min (trained operator)                 │
│  Context: maritime, military, emergency signaling                │
│                                                                  │
│  CHAPPE OPTICAL TELEGRAPH (historical, 1793)                     │
│  Mechanical semaphore towers, 556 km network across France       │
│  Forerunner of all telecommunications                            │
│                                                                  │
│  RAILWAY SEMAPHORE (operational, 1830s–present)                  │
│  Fixed mechanical arm signals; 2 or 3 positions                  │
│  Controls train movement on single-track lines                   │
│                                                                  │
│  HELIOGRAPH (optical, 1870s–1944)                                │
│  Reflected sunlight using mirror and shutter                     │
│  Encodes Morse, not semaphore positions                          │
│  Range: 50–100+ km in clear conditions                           │
└──────────────────────────────────────────────────────────────────┘
```

---

## Flag Semaphore — Position System

The operator holds one flag in each hand and extends arms to one of **8 positions**, 45° apart. With two independent arms, the theoretical capacity is 8 × 8 = 64 combinations (minus same-position for both arms = 56 usable). The 26 letters + digits + procedural signals use a subset.

### Position Reference Grid

```
                        EIGHT ARM POSITIONS
                     (from receiver's perspective)

                            UP (8)
                           /
              UL (7)      |        UR (1)
             /            |         \
            /             |          \
LEFT (6) ──────────── CENTER (body) ──────── RIGHT (2)
            \             |          /
             \            |         /
              LL (5)      |        LR (3)
                           \
                            DOWN (4)

  Number key: 1=upper-right, 2=right, 3=lower-right, 4=down,
              5=lower-left, 6=left, 7=upper-left, 8=up

  Each arm can be in any of these 8 positions.
  "Down" (4) is the rest/neutral position.
```

### ASCII Stick Figure Notation

For each letter below, positions shown as: `[L-arm]/[R-arm]` using:
`8`=up, `7`=upper-left, `6`=left, `5`=lower-left, `4`=down, `3`=lower-right, `2`=right, `1`=upper-right

```
  Example — Letter A: Left arm DOWN (4), Right arm UPPER-RIGHT (1)

         ↗ (right arm upper-right)
    o
    |
  ↓ |    (left arm down)

  Stick figure: body center, arms at described angles
```

---

## The Complete Flag Semaphore Alphabet

Standard International Semaphore (most widely used; variations exist):

```
┌─────────────────────────────────────────────────────────────────┐
│        FLAG SEMAPHORE ALPHABET — LEFT/RIGHT ARM POSITIONS       │
│        Position key: 8=up, 7=UL, 6=L, 5=LL, 4=down,             │
│                      3=LR, 2=R, 1=UR                            │
├─────┬───────┬──────────────────────────────────────────────────┤
│  A  │ L:4   │ R:1    "L down, R upper-right"                   │
│  B  │ L:4   │ R:2    "L down, R right"                         │
│  C  │ L:4   │ R:3    "L down, R lower-right"                   │
│  D  │ L:4   │ R:5    "L down, R lower-left" (crossing)         │
│  E  │ L:4   │ R:6    "L down, R left"                          │
│  F  │ L:4   │ R:7    "L down, R upper-left"                    │
│  G  │ L:4   │ R:8    "L down, R up"                            │
├─────┼───────┼──────────────────────────────────────────────────┤
│  H  │ L:1   │ R:2    "L upper-right, R right"                  │
│  I  │ L:1   │ R:3    "L upper-right, R lower-right"            │
│  J  │ L:6   │ R:8    "L left, R up"   [special – J]            │
│  K  │ L:1   │ R:5    "L upper-right, R lower-left"             │
│  L  │ L:1   │ R:6    "L upper-right, R left"                   │
│  M  │ L:1   │ R:7    "L upper-right, R upper-left"             │
│  N  │ L:1   │ R:8    "L upper-right, R up"                     │
├─────┼───────┼──────────────────────────────────────────────────┤
│  O  │ L:2   │ R:3    "L right, R lower-right"                  │
│  P  │ L:2   │ R:5    "L right, R lower-left"                   │
│  Q  │ L:2   │ R:6    "L right, R left"                         │
│  R  │ L:2   │ R:7    "L right, R upper-left"                   │
│  S  │ L:2   │ R:8    "L right, R up"                           │
├─────┼───────┼──────────────────────────────────────────────────┤
│  T  │ L:3   │ R:5    "L lower-right, R lower-left"             │
│  U  │ L:3   │ R:6    "L lower-right, R left"                   │
│  V  │ L:5   │ R:8    "L lower-left, R up"                      │
│  W  │ L:6   │ R:7    "L left, R upper-left"                    │
│  X  │ L:3   │ R:7    "L lower-right, R upper-left"             │
│  Y  │ L:3   │ R:8    "L lower-right, R up"  [variant: 3/1]     │
│  Z  │ L:5   │ R:6    "L lower-left, R left"                    │
├─────┴───────┴──────────────────────────────────────────────────┤
│  Numbers: signal NUMERALS flag first (L:6/R:7 = W = nums on),  │
│  then:  1=A, 2=B, 3=C, 4=D, 5=E, 6=F, 7=G, 8=H, 9=I, 0=K     │
│  (The J position stays the "numerals" indicator for digits 10=J)│
│                                                                 │
│  Attention/Ready: Both arms down (L:4, R:4)                    │
│  Error/Cancel:    Both arms overhead waving side to side        │
│  Numerals cancel: J position (L:6, R:8) again to exit nums mode │
└─────────────────────────────────────────────────────────────────┘
```

### ASCII Alphabet Gallery (selected letters)

```
A: right arm up-right     B: right arm right        G: right arm up
     /                         ─ ─                       |
  o/                         o                          o|
  |                           |                          |
  ↓                           ↓                          ↓

K: arms mirror diagonal    M: arms spread upper      Q: arms horizontal
    \  /                        \ /                    ─ o ─
      o                          o                       |
      |                          |                       |
      ↓                          ↓                       ↓
```

---

## Procedural Signals

```
Signal         Description
────────────   ────────────────────────────────────────────────
Attention      Both arms down at sides (ready position)
Ready/OK       L:4, R:4 then receiver raises flag to confirm
Error          Both arms waved overhead repeatedly
Numerals on    W position (L:6, R:7) — signals following are digits
Numerals off   J position again
Interval       Receiver unable to copy — resend last group
End of word    Small pause
End of message Both arms crossed overhead
```

---

## Chappe Optical Telegraph (1793)

Claude Chappe built the first telecommunications network in history — not electric, but mechanical:

```
┌──────────────────────────────────────────────────────────────┐
│              CHAPPE OPTICAL TELEGRAPH SYSTEM                 │
│                                                              │
│  Tower structure:                                            │
│                                                              │
│         R  (regulator arm, 3 positions: /, |, \)             │
│        /|                                                    │
│  ──────┤├─────  (horizontal beam = regulator)                │
│        \|                                                    │
│         R                                                    │
│         |                                                    │
│     ════╬════  (mast)                                        │
│         |                                                    │
│  Indicator arms on each end of horizontal beam:              │
│  Each has 7 positions (45° increments, 0°–270°)              │
│                                                              │
│  Capacity: 196 distinct configurations                       │
│  Codebook: 92 pages × 92 signals = 8,464 vocabulary entries  │
│  Speed: Paris to Lille (225 km, 15 towers): ~10 min          │
│  Paris to Toulon (765 km, 50+ towers): ~20 min               │
│  Paris to Strasbourg (556 km): ~7 min (demonstrated 1798)    │
│                                                              │
│  Operation:                                                  │
│  Relay operator reads predecessor tower through telescope,   │
│  reproduces configuration, successor reads and continues.    │
│  Network: ~556 towers across France by 1820                  │
└──────────────────────────────────────────────────────────────┘
```

**Chappe vs. electric telegraph comparison**:
- Chappe: line-of-sight dependent, fails in fog/night, ~35 chars/min at peak
- Electric (Morse, 1844): weather-independent, faster, cheaper to operate
- Chappe network: abandoned by 1855 as electric telegraph spread

**Security**: Chappe messages used a codebook for secrecy — the tower operators only relayed the mechanical configurations without knowing their meaning. This is an early example of **separation of transmission and interpretation**.

---

## Murray/Shutter Telegraph (British, 1795)

Lord George Murray's competing British system used **6 shutters** in a 2×3 grid:

```
┌────────────────────────────────────────────┐
│  MURRAY SHUTTER TELEGRAPH                  │
│                                            │
│  ┌──┬──┬──┐                                │
│  │  │  │  │  Each shutter: OPEN or CLOSED  │
│  ├──┼──┼──┤  6 shutters → 2⁶ = 64 codes   │
│  │  │  │  │                                │
│  └──┴──┴──┘                               │
│                                            │
│  Operated 1796–1847 across Britain         │
│  Chains: London–Deal, London–Portsmouth,  │
│  London–Yarmouth                           │
│  Replaced by electric telegraph 1847       │
└────────────────────────────────────────────┘
```

**Information theory note**: Murray shutter used a 6-bit binary code — conceptually equivalent to a 6-bit character code (predating ASCII by 165 years). The 64 possible configurations map directly to 64 possible symbols.

---

## Railway Semaphore (1830s–Present)

Fixed-arm trackside signals that control train movements:

```
┌──────────────────────────────────────────────────────────────┐
│                RAILWAY SEMAPHORE SIGNALS                     │
│                                                              │
│  Two-position (lower quadrant, UK classic):                  │
│                                                              │
│  HORIZONTAL arm (90°):  STOP / Danger (red light at night)   │
│         ──────                                               │
│         |                                                    │
│                                                              │
│  INCLINED arm (45° down):  CLEAR / Proceed (green at night)  │
│           \                                                  │
│            \                                                 │
│            |                                                 │
│                                                              │
│  Three-position (upper quadrant, US common):                 │
│  Horizontal: STOP                                            │
│  45° up:     CAUTION (approach next signal at reduced speed) │
│  Vertical:   CLEAR                                           │
│                                                              │
│  Color lights eventually replaced physical semaphore arms    │
│  in most countries (UK kept semaphore on heritage lines)     │
│  UK national network: mostly color light since 1970s         │
│  US: color light dominant; some semaphores remain on         │
│      Class 1 railroad systems                                │
└──────────────────────────────────────────────────────────────┘
```

Railway semaphore is **not** the same code as flag semaphore. Railway semaphore has 2–3 positions and encodes train proceed/stop instructions only.

---

## Heliograph (1870s–1944)

The heliograph reflected sunlight to transmit Morse code over extreme distances:

```
┌──────────────────────────────────────────────────────────────┐
│                HELIOGRAPH PRINCIPLE                          │
│                                                              │
│  Sunlight → Mirror (aimed at receiver)                       │
│             Shutter/wink mechanism opens/closes beam         │
│             Long flash = dash, Short flash = dot             │
│             Receiver reads Morse by eye or telescope         │
│                                                              │
│  Equipment: British Mance heliograph (1869 Henry Christopher │
│             Mance, British Army India)                       │
│             Weight: ~5 lbs field instrument                  │
│                                                              │
│  Range: 50–100 km in good conditions (clear sky, no dust)    │
│         Record: 288 km (Rocky Mountain US Army survey)       │
│                                                              │
│  Used in:                                                    │
│  — British Army, India and Afghanistan (1880s–1900s)         │
│  — US Army, Southwest (Apache Wars 1880s)                    │
│  — Boer War (1899–1902)                                      │
│  — WWI (still in use for field communications)               │
│  — WWII: Last known military use, Burma campaign 1944        │
│                                                              │
│  Limitation: Requires direct sunlight. Useless at night,     │
│  in overcast weather, or in dense forest/terrain.            │
└──────────────────────────────────────────────────────────────┘
```

Heliograph encodes **Morse**, not semaphore arm positions. It's a transmission medium for the Morse code, not a separate encoding system.

---

## Aldis Lamp (Optical Morse, Navy)

The Aldis lamp is the modern naval equivalent:

```
┌──────────────────────────────────────────────────────────────┐
│  ALDIS LAMP                                                  │
│                                                              │
│  Focused directional spotlight with a shutter/key            │
│  Short flash = dot, Long flash = dash (Morse encoding)       │
│                                                              │
│  Range: ~6–10 km ship-to-ship (day)                          │
│         Longer at night (up to 15+ km)                       │
│                                                              │
│  Advantages over radio:                                      │
│  — Directional: intercept requires being in line-of-sight    │
│  — No radio frequency to allocate or detect passively        │
│  — Useful under radio silence conditions                     │
│                                                              │
│  Speed: trained naval signaller: 8–10 WPM (receiving);       │
│         ~5–6 WPM transmitting with lamp key                  │
│                                                              │
│  Still in active use: NATO navies train on Aldis lamp as     │
│  backup to radio communications                              │
└──────────────────────────────────────────────────────────────┘
```

---

## Comparison Table

| System | Encoding | Range | Speed | Medium | Era |
|--------|----------|-------|-------|--------|-----|
| Flag semaphore | Arm positions (spatial) | 3 km | 25 char/min | Visible light | 1800s–present |
| Chappe telegraph | Arm angles (spatial) | 556 km network | 35 char/min | Visible light | 1793–1855 |
| Murray shutter | 6-bit binary | ~80 km chains | ~30 char/min | Visible light | 1796–1847 |
| Railway semaphore | 2–3 positions | Track block length | N/A | Visible light | 1830s–present |
| Heliograph | Morse (temporal) | 50–100+ km | 20 WPM | Sunlight | 1870–1944 |
| Aldis lamp | Morse (temporal) | 6–15 km | 8–10 WPM | Directed light | 1900–present |

---

## Decision Cheat Sheet

| Situation | System |
|-----------|--------|
| Ship-to-ship, no radio | Flag semaphore or Aldis lamp (Morse) |
| Emergency visual signal, line of sight | Flag semaphore |
| Historical French state telegraphy | Chappe optical telegraph |
| Railway block working | Fixed semaphore arm signals |
| Desert/mountain communication, sunlight available | Heliograph (Morse) |
| Naval radio silence condition | Aldis lamp |

---

## Common Confusion Points

**Flag semaphore is not Morse**. Semaphore encodes in position (what you see at one instant). Morse encodes in time (sequence of short/long signals). Different systems, different operators, different gear.

**"Semaphore" in computing** (OS semaphores, mutex primitives) comes from the railway metaphor: a signal that tells a thread "proceed" or "stop." The connection to arm-position semaphore is purely etymological.

**The Chappe telegraph was not electric**. It transmitted information at speed by human relay — each tower operator manually reproduced what they saw at the previous tower. Despite being mechanical, it achieved Paris→Strasbourg transmission in ~7 minutes in 1798.

**Heliograph uses Morse, not arm positions**. The heliograph's flashing mirror encodes dot/dash Morse timing. Some people confuse it with flag semaphore because both involve light and hand operation — but the encoding is completely different.

**J in semaphore**: The letter J uses the same position as the "numerals indicator" in some teaching materials, which causes confusion. In the standard alphabet, J = left:6/right:8 (left horizontal, right up). The numerals mode uses a separate agreed indicator sequence. Different manuals handle this slightly differently.
