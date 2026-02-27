# Aspect Ratio Bakeoff

## The Problem

Monospace characters are ~2× taller than wide. A typical char cell is 8px wide × 16-18px tall. Without correcting for this, maps stretch north-south and Florida becomes a needle.

```
THE DISTORTION

  What 5° × 5° SHOULD look like:        What it looks like uncorrected:
  (slightly taller than wide at 40°N)    (way too tall)

  ┌──────────┐                            ┌──────────┐
  │          │                            │          │
  │          │                            │          │
  │          │                            │          │
  └──────────┘                            │          │
                                          │          │
                                          │          │
                                          │          │
                                          │          │
                                          └──────────┘
```

## The Formula

```
rows_per_degree_lat = chars_per_degree_lon × (char_width / char_height) × (1 / cos(center_lat))
```

At 200 chars for 60° longitude = 3.33 chars/degree, centered on 37°N:

| Font ratio (w/h) | Rows/degree | Total rows (24° lat) | Example fonts |
|-------------------|-------------|---------------------|---------------|
| 0.45 | 1.88 | 45 | Narrow: Iosevka, Fira Code |
| 0.50 | 2.09 | 50 | Typical: Consolas, Menlo, Monaco |
| 0.55 | 2.30 | 55 | Medium: Courier New, JetBrains Mono |
| 0.60 | 2.51 | 60 | Wide: Ubuntu Mono, Source Code Pro |

Previous map used **3.125 rows/degree = 75 rows**. That's 50% too tall for any font.

---

## Bakeoff: Southeast US at 4 Aspect Ratios

Same geography, same width (50 chars for 15° longitude). The test: **does Florida look like Florida?**

Region: 90W-75W, 35N-25N. col = round((90 - lon) × 3.33).

### Option A: 1.9 rows/degree (narrow fonts — Iosevka, Fira Code) — WINNER

```
                ·  ··APPALACHIAN TAIL·····Cape
 ····Atlanta·····  ··▲▲▲▲▲▲▲▲▲▲▲▲▲··· Hatteras                                                  35N
 ·····························▲▲▲▲▲▲▲·····╱╱╱╱
 ··································▲▲··╱╱╱╱╱╱╱
New Orleans··FL PANHANDLE···Jacksonville                                                          30N
                          ╭─··········─╮
                          │············│
                    Tampa──┤··FLORIDA··│                                                           27N
                          │············│
                          │··········Miami
                          ╰──·Keys·──╯                                                            25N
 90W       85W       80W       75W
```

### Option B: 2.3 rows/degree (typical fonts — Consolas, Menlo)

```
                ·  ··APPALACHIAN TAIL·····Cape
 ····Atlanta·····  ··▲▲▲▲▲▲▲▲▲▲▲▲▲··· Hatteras                                                  35N
 ····························▲▲▲▲▲▲▲▲·····╱╱╱╱
 ···································▲▲··╱╱╱╱╱╱╱
 ·····································╱╱╱╱╱╱╱╱╱
 ····································╱╱╱╱╱╱╱╱╱╱
New Orleans··FL PANHANDLE··Jacksonville··╱╱╱╱╱                                                    30N
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····│·····╱╱╱╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····│···╱╱╱╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····│··╱╱╱╱
 ≈≈≈ GULF OF MEXICO ≈≈≈··Tampa·│·╱╱╱╱                                                            27N
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····│╱╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│··Miami
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···╰·Keys                                                                 25N
 90W       85W       80W       75W
```

### Option C: 2.8 rows/degree (wide fonts — Ubuntu Mono, Source Code Pro)

```
                ·  ··APPALACHIAN TAIL·····Cape
 ····Atlanta·····  ··▲▲▲▲▲▲▲▲▲▲▲▲▲··· Hatteras                                                  35N
 ·····························▲▲▲▲▲▲▲·····╱╱╱╱
 ···································▲▲▲··╱╱╱╱╱╱
 ·····································▲╱╱╱╱╱╱╱╱
 ······································╱╱╱╱╱╱╱╱
 ·····································╱╱╱╱╱╱╱╱╱
 ····································╱╱╱╱╱╱╱╱╱╱
New Orleans··FL PANHANDLE··Jacksonville··╱╱╱╱╱                                                    30N
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····│·····╱╱╱╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····│····╱╱╱╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····│···╱╱╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····│··╱╱╱╱
 ≈≈≈≈ GULF OF MEXICO ≈≈··Tampa·│·╱╱╱╱                                                            27N
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····│╱╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│···╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│··Miami
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···╰·Keys                                                                 25N
 90W       85W       80W       75W
```

### Option D: 3.3 rows/degree (CURRENT — what we had before)

```
                ·  ··APPALACHIAN TAIL·····Cape
 ····Atlanta·····  ··▲▲▲▲▲▲▲▲▲▲▲▲▲··· Hatteras                                                  35N
 ·····························▲▲▲▲▲▲▲·····╱╱╱╱
 ···································▲▲▲··╱╱╱╱╱╱
 ·····································▲╱╱╱╱╱╱╱╱
 ······································╱╱╱╱╱╱╱╱
 ·····································╱╱╱╱╱╱╱╱╱
 ····································╱╱╱╱╱╱╱╱╱╱
 ···································╱╱╱╱╱╱╱╱╱╱╱
New Orleans··FL PANHANDLE··Jacksonville··╱╱╱╱╱                                                    30N
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····│·····╱╱╱╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····│····╱╱╱╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····│···╱╱╱╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····│···╱╱╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····│··╱╱╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····│··╱╱╱                                                            27N
 ≈≈≈≈≈ GULF OF MEXICO ≈··Tampa·│·╱╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····│╱╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····│╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│····╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│···╱╱
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···│··Miami
 ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈···╰·Keys                                                                 25N
 90W       85W       80W       75W
```

---

## Quick Diagnostic: Which Circle Looks Round?

One of these should look like a circle on your screen. That's your font's aspect ratio.

```
Option A (0.45):     Option B (0.50):     Option C (0.55):     Option D (0.60):

    ·····                ·····                ·····                ·····
  ·········            ·········            ·········            ·········
 ···········          ···········          ···········          ···········
 ···········          ···········          ···········          ···········
  ·········           ···········          ···········          ···········
    ·····             ···········          ···········          ···········
                       ·········            ·········           ···········
                         ·····              ···········          ·········
                                             ·········           ·········
                                               ·····             ·········
                                                                   ·····
```

**Pick the one that looks most like a circle. That tells us your font ratio and the correct rows/degree for your maps.**

---

## Summary: What Each Option Means for the Full US Map

| Option | Font ratio | Rows for 24° | Total map size | Florida shape |
|--------|-----------|-------------|---------------|---------------|
| A | 0.45 | 45 rows | 200 × 45 | Recognizable peninsula |
| B | 0.50 | 50 rows | 200 × 50 | Good peninsula |
| C | 0.55 | 55 rows | 200 × 55 | Slightly tall peninsula |
| D (current) | — | 75 rows | 200 × 75 | Needle (wrong) |

Once you pick which circle looks round, I'll redraw the full lower 48 at that ratio.
