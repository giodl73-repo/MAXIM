---
wave: maxim-quality-control-spine
pulse: 06
date: 2026-05-14
status: done
depends_on: [02, 03, 04]
governing_roles: [reference-editor, ascii-cartographer, expert-skeptic, bridge-builder]
---

# Pulse 06 - Pilot Gold Audit

## Mission

Apply the raised rubric to a small cross-section before scaling it to the whole
library.

## Candidate Sample

| Guide | Why |
|---|---|
| `computing/01-PACKAGE.md` | Existing gold-standard style contract |
| `distributed-systems/03-CONSENSUS.md` | Peer-level technical guide with algorithm diagrams |
| `periodic-table/01-HYDROGEN.md` | Cross-domain science guide with strong density |
| `music-theory/01-PITCH-SCALES.md` | Mathematical arts guide; tests tone and notation |
| `atlas/02-GLOBAL-WINDS.md` | Hybrid SVG/ASCII atlas precedent |

## Deliverables

- [x] Score each guide against Gold Rubric v2.
- [x] Record findings in a wave panel, not inline tags, unless the user asks for
      remediation.
- [x] Identify proof false positives and false negatives.
- [x] Produce a revised rollout plan for the next wave.

## Evidence

- `panels/pilot-gold-audit/R1-consolidated.md`

## Validation

```powershell
git diff --check
```

## Non-Goals

- Do not rewrite sampled guides during the audit.
- Do not generalize from one weak file without checking at least one strong file.
