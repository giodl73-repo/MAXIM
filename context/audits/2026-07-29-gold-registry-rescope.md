# MAXIM Gold Registry Rescope — 2026-07-29

## Decision

Re-scope public Gold claims to match evidence. Do **not** delete provenance
tables; relabel and count honestly.

## Measured ground truth

| Metric | Value |
|---|---:|
| Batch table raw rows | 818 |
| Batch unique guides | ~801 |
| Historical register raw rows | 893 |
| Historical unique guides | ~876 |
| Deduped candidate universe (approx.) | ~875 |
| Rows with score exactly 4.6 | nearly all candidates |
| Differentiated pilot-rescore Certified Gold | **2** |

The two Certified Gold guides:

1. `computing/01-PACKAGE.md` (4.8) — pilot gold rescore
2. `distributed-systems/03-CONSENSUS.md` (4.7) — pilot gold rescore

## Changes

1. `context/gold/REGISTRY.md`
   - Honesty Dashboard with unique-guide counts
   - Explicit **Current Certified Gold** section (2 guides only)
   - Batch table retitled as Candidate-Hardened provenance
   - Reset Audit Summary uses unique counts
   - Promotion protocol forbids bulk wave promotion
2. `README.md` / `CLAUDE.md`
   - Softened "reviewed and clean / complete" to authored + style-clean
   - Point to registry for Gold honesty

## What we did not do

- Did not delete the large provenance tables (still useful for invariants/waves)
- Did not auto-promote differentiated 4.7 cohort rows without reset-era panels
- Did not regenerate source-corpus (PROOF toolchain still unwired here)

## Allowed public claims after this rescope

| Claim | OK? |
|---|---|
| 2 Certified Gold guides | Yes |
| ~875 Candidate-Hardened guides | Yes |
| ~1,700 Certified Gold | **No** |
| Full library fact-certified | **No** |
| Style/`@editor` largely clean | Yes |

## Next

1. Optional: dedupe batch/historical tables in a later mechanical cleanup
2. Promote candidates only via per-guide reset-era panels
3. Prefer numbers/names fact-check waves over Gold factory stamping
