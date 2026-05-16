---
wave: atlas-map-invariants
date_open: 2026-05-14
date_close: 2026-05-14
status: complete
source_wave: pilot-gold-rescore
---

# Atlas Map Invariants

## Mission

Close the remaining pilot carry-forward by proving that Da Vinci invariants can
protect SVG-backed atlas content, not only fenced ASCII figures.

## Pulse Status

| Pulse | Status | Evidence |
|---|---|---|
| 01 - Desert latitude map invariant | DONE | `proof.toml` pins `atlas/02-GLOBAL-WINDS.md#the-worlds-deserts-positioned-by-latitude:0` |
| 02 - Map semantic anchors | DONE | Invariants require 30°N, 30°S, Sahara, Atacama, and Hadley Cell exhaust |

## Validation

```powershell
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail atlas\02-GLOBAL-WINDS.md proof.toml
```

## Closeout

This establishes an atlas-specific invariant pattern: protect SVG maps by
pinning their semantic anchors and coordinate-band labels, while leaving exact
geometry and cartographic rendering for `/atlas-review`.
