# MAXIM — K♠ deep dive + honest-gap closeout (2026-07-29)

## Scope

- Inventory live `@editor` tags
- Close remaining honest-gap fact leftovers (2026-06-27)
- Deep-dive K♠ (C·IV The Sentinel) vs SCORECARD grade C
- Spot-check K♠ for additional high-confidence errors

## Findings

### `@editor` tags

Zero live `<!-- @editor ... -->` tags in content guides. Grep hits are docs/meta
describing the review system (`CLAUDE.md`, `HISTORY.md`, `README.md`, etc.).

### Fact fixes (source guides)

| File | Fix |
|---|---|
| `biology/01-MOLECULAR-MACHINERY.md` | Okazaki: bacterial 1–2 kb vs euk 100–200 nt |
| `cryptography/02-ASYMMETRIC.md` | OAEP = RFC 8017 encode path; KEM-DEM fence |
| `distributed-systems/03-CONSENSUS.md` | Raft terms timeline (split vote = empty term) |
| `genomics/01-SEQUENCING-TECH.md` | Sanger throughput ~50–100 kb/run |
| `disease/02-VIRAL.md` | 1918 toll wording (not absolute history max) |
| `cloud-architecture/00-OVERVIEW.md` | Azure Savings Plan for Compute branding |
| `cloud-architecture/02-COMPUTE-PATTERNS.md` | same |
| `cloud-architecture/08-COST-OPTIMIZATION.md` | same |
| `cloud-architecture/09-MULTI-CLOUD.md` | Outposts service link ≠ Direct Connect-only |
| `distributed-systems/10-CONSENSUS-THEORY.md` | ◇W ≡ Ω weakest FD wording |

### K♠ deep dive

SCORECARD (2026-02-26) graded K♠ **C (19)** for missing overview, thin depth,
weak archetype. **No longer accurate:**

- `computing/00-SENTINEL-THESIS.md` unifies the triad with constraint stack,
  decision cheat sheet, confusion points, reading order
- Each of `distributed-systems/`, `security-engineering/`, `cloud-architecture/`
  opens with Sentinel Context + cross-links
- Deep theory files present (`10-CONSENSUS-THEORY`, `10-THREAT-MODELS`)
- ~10.3k content lines ≈ **198 pages** (was ~186)

**Rescore:** Len 3 · Suit 5 · Coh 5 · Style 4 · Depth 4 · Arch 4 → **25 A**

## Residual

1. Source-corpus regeneration for touched modules (PROOF/PROOF path not wired
   in this checkout — `module_source_backfill.py` present, PROOF binary missing).
2. Gold registry rubber-stamp issue from 2026-06-27 still open (owner decision).
3. Library-wide numbers/proper-nouns fact-check remains highest long-term value.
4. Next volume polish targets: Q♠, 10♠, 7♦, A♠ (B-tier).

## Validation

- Targeted re-read of all edited sections
- Pattern scan confirms old bad strings gone for closed leftovers
- No bulk transforms; surgical edits only (CLAUDE.md safety rules)
