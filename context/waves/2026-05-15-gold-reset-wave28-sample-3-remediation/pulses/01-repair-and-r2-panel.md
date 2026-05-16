---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `ai-engineering/00-OVERVIEW.md`
- `animal-phylogeny/00-OVERVIEW.md`
- `anthropology/00-OVERVIEW.md`
- `anthropology/02-PALEOANTHROPOLOGY.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
model selectors, phylum routers, framework selectors, or key-evidence lookup
tables without enough diagnostic caveats for Current Certified Gold.

## Changes

| Guide | Repair |
|---|---|
| `ai-engineering/00-OVERVIEW.md` | Rebuilt the cheat sheet around reasoning, high-volume tasks, RAG, coding, multimodal documents, air-gapped deployment, long context, media generation, fine-tuning, and embeddings. |
| `animal-phylogeny/00-OVERVIEW.md` | Rebuilt the phylum decision tree into diagnostics for animal identity, sponges, non-bilaterians, bilaterians, protostomes/deuterostomes, ecdysozoans, lophotrochozoans, and deuterostome candidates. |
| `anthropology/00-OVERVIEW.md` | Rebuilt the cheat sheet around biological variation, cooperation, ethnography, WEIRD sampling, tools, gift obligation, organizational culture, language, ethics, and situated action. |
| `anthropology/02-PALEOANTHROPOLOGY.md` | Rebuilt the cheat sheet around bipedalism, stone tools, fire, Africa dispersal, interbreeding, Denisovans, early Homo sapiens, symbolic behavior, Out-of-Africa timing, and behavioral modernity. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- ai-engineering\00-OVERVIEW.md animal-phylogeny\00-OVERVIEW.md anthropology\00-OVERVIEW.md anthropology\02-PALEOANTHROPOLOGY.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml ai-engineering\00-OVERVIEW.md animal-phylogeny\00-OVERVIEW.md anthropology\00-OVERVIEW.md anthropology\02-PALEOANTHROPOLOGY.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

