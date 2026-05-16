---
wave: pilot-r3-gold-promotion
date_open: 2026-05-14
date_close: 2026-05-14
status: complete
source_wave: gold-registry
---

# Pilot R3 Gold Promotion

## Mission

Re-run the three remaining pilot candidates after their follow-up polish and
promote only those that now satisfy the Gold Registry entry criteria.

## Mechanical Gate

```powershell
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail music-theory\01-PITCH-SCALES.md atlas\02-GLOBAL-WINDS.md periodic-table\01-HYDROGEN.md proof.toml
```

Result: pass.

## Candidate-Specific Review

### `atlas/02-GLOBAL-WINDS.md`

Atlas-specific checks:

| Criterion | Result | Notes |
|---|---|---|
| Coordinate convention | pass | World map uses `x = longitude`, `y = -latitude`; desert labels match hemispheres |
| Feature placement | pass | Sahara, Arabian, Thar, Sonoran, Atacama, Namib, Kalahari, Australian deserts land in plausible bands |
| Grid and band labels | pass | 30°N/30°S subtropical high bands explicitly labeled |
| Scale bar | pass | World-scale approximate bar present; adequate for overview map |
| Palette | pass | Light/warm atlas palette preserved |
| Label collision | pass | Dense but readable at intended width |
| ASCII mechanism diagrams | pass | Three-cell, wind-belt, desert, monsoon, jet-stream, and storm-track diagrams explain why, not just where |

Decision: **Gold**. The map now has SVG semantic anchors plus atlas review.

### `periodic-table/01-HYDROGEN.md`

Follow-up checks:

| Criterion | Result | Notes |
|---|---|---|
| Mechanism visual | pass | PEMFC selective-transport diagram clarifies proton/electron/gas separation |
| Bridge integration | pass | Nafion/ion-channel bridge sits inside fuel-cell section |
| Decision utility | pass | Fuel/storage/economy decisions are direct and practical |
| Factual confidence | pass | Strong claims are bounded; engineering caveats are named |

Decision: **Gold**.

### `music-theory/01-PITCH-SCALES.md`

Follow-up checks:

| Criterion | Result | Notes |
|---|---|---|
| Notation review | pass | Guide now defines enharmonic spelling, octave numbering, pitch class, `f0`, `n`, and interval quality notation |
| Cross-reference value | pass | Onward paths now connect to overview, modes, harmony, voice-leading, and jazz extensions |
| Reader tasks | pass | Frequency calculation, interval inversion, major/minor construction, and ambiguity handling are self-contained |
| Factual confidence | pass | 12-TET, cents, intervals, and scale formulas are bounded and mathematically coherent |

Decision: **Gold**.

## R3 Score Table

| Guide | Tier | Average | Decision |
|---|---:|---:|---|
| `atlas/02-GLOBAL-WINDS.md` | Gold | 4.6 | atlas review + SVG invariants complete |
| `periodic-table/01-HYDROGEN.md` | Gold | 4.6 | PEMFC mechanism polish resolves final visual gap |
| `music-theory/01-PITCH-SCALES.md` | Gold | 4.5 | notation and cross-reference gaps resolved |

## Dimension Scores

| Dimension | Winds | Hydrogen | Pitch |
|---|---:|---:|---:|
| Landscape power | 5 | 5 | 4 |
| Layering integrity | 5 | 5 | 4 |
| ASCII precision | 5 | 5 | 4 |
| Explanatory compression | 4 | 4 | 4 |
| Decision utility | 5 | 4 | 5 |
| Confusion handling | 4 | 5 | 4 |
| Bridge quality | 4 | 5 | 4 |
| Cross-reference value | 4 | 4 | 5 |
| Voice | 5 | 5 | 5 |
| Factual confidence | 5 | 4 | 5 |

## Closeout

All five pilot guides are now certified Gold: Package, Consensus, Global Winds,
Hydrogen, and Pitch. This closes the original pilot loop and gives future waves
a concrete pattern for evidence-backed promotion.
