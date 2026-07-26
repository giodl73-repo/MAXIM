---
wave: clinical-and-chemical-foundations
date_open: 2026-07-11
date_close: 2026-07-12
status: complete
---

# Clinical and Chemical Foundations

## Mission

Close MAXIM's two largest foundation gaps with standalone, peer-level modules:

- `chemistry/`: analytical, inorganic, organic, physical, and computational
  chemistry as a coherent first-class discipline;
- `clinical-medicine/`: clinical reasoning, differential diagnosis,
  evidence-based care, specialty boundaries, and care pathways;
- `pathology/`: mechanisms, histopathology, laboratory interpretation, and the
  bridge from disease process to diagnosis.

## Guardrails

- Existing `medicine/` remains pharmacology/diagnostics until an explicit rename
  or boundary decision is reviewed.
- No medical-advice framing; content is educational reference material.
- Follow the repo's learner profile and style contract; do not lower the bar to
  introductory textbook prose or template filling.
- Read strong local exemplars before drafting, especially deep guides rather
  than treating `computing/01-PACKAGE.md` as the content-depth ceiling.
- Each guide needs a real landscape, layered model, decision-useful tables,
  cross-domain bridges, Decision Cheat Sheet, and Common Confusion Points.
- External sources may support fact-checking, but MAXIM remains independently
  readable and no sibling repo is a runtime or publication gate.
- Every source edit regenerates MDLOOM/CROP/MDPORT/FLETCH artifacts.

## Pulses

| Pulse | Status | Outcome |
|---:|---|---|
| 01 - Chemistry architecture and exemplars | DONE | Non-duplicating scope defined against `natural-sciences/`, `biochemistry/`, `materials/`, `chemical-eng/`, `optics/`, `biophysics/`, and `statistical-mechanics/`; 12 guides + STATUS authored at full depth, integrated into section/nav/registry, and regenerated into MDLOOM/CROP/MDPORT/FLETCH source-corpus artifacts. See `pulses/01+chemistry-authoring.md`. |
| 02 - Chemistry adversarial review | DONE | Two independent adversarial reviews completed; all BLOCK/WARN findings repaired and recorded under `panels/chemistry-r1/`. |
| 03 - Clinical medicine architecture | DONE | Non-duplicating scope defined against `medicine/`, `disease/`, `pharmacology/`, `human-biology/`, and `public-health/`; reusable-reasoning-pattern (not per-organ) architecture ratified; 12-guide manifest + `STATUS.md` authored (module IN PROGRESS, not complete); two highest-risk boundary guides prototyped at full depth (`03-DIAGNOSTIC-TEST-INTERPRETATION` resolving the `medicine/10` overlap as decision-theory-vs-catalog; `08-SPECIALTY-INTERFACES` as an interface catalog). Architecture record + pulse under `artifacts/CLINICAL-MEDICINE-ARCHITECTURE.md` and `pulses/03+clinical-medicine-architecture.md`. Prototypes then re-reviewed and repaired in `panels/clinical-prototype-r1/`: `03` worked-case branch-by-branch threshold math + non-imperative recast + `medicine/10 §11` overlap honesty; `08` separates routing mechanisms from explicit, locally valid responsibility contracts and adds closed-loop cases across resourced and district/teleconsult topologies. Guides passed the strict prototype gate (`panels/clinical-prototype-r1/`), establishing the ratified quality/safety pattern for the module; focused MDLOOM clean. Full authoring, section/nav integration, source-corpus backfill, and the reverse `medicine/10 §11` → `03` wiring were carried out in Pulse 04. |
| 04 - Clinical medicine authoring and review | DONE | Authored and integrated all 12 guides at full peer-level MAXIM depth using the passed prototype pattern; added the minimal reverse `medicine/10 §11` → `clinical-medicine/03` cross-reference; regenerated and validated clinical-medicine and medicine source corpora; completed full-module adversarial and guide-specific ten-dimension/reader-task review. No unresolved BLOCK/WARN findings. Honest tier decision: all 12 guides are Silver; optional Da Vinci pinning and Gold promotion are future work, not a Pulse-04 blocker. See `pulses/04+clinical-medicine-authoring.md` and `panels/clinical-full-r1/`. |
| 05 - Pathology module completion and review | DONE — FINAL PASS | Non-duplicating mechanism/method scope, the three-way lab split, 12-guide manifest, and four-pillar safety contract are ratified under `artifacts/PATHOLOGY-ARCHITECTURE.md` (MAXIM-PATH-01 … 25). **All 12/12 guides are authored, integrated, reciprocally wired, source-backfilled, and reviewed.** Prototype guides `08`/`10` passed R1/R2; scaling guides `09`/`11` both passed Stage 2; the full-module R1 adversarial panel has no unresolved BLOCK/WARN; and `panels/pathology-full-r1/R2-gold-rubric.md` records differentiated ten-dimension and reader-task evidence. The final reviewer returned **PASS** on 2026-07-12. Honest tier: **Silver for all 12**; no Gold registry rows were added. |

## Quality Gate

1. Every file reads like a durable MAXIM reference guide, not a generated
   outline.
2. Every guide answers 3-5 concrete reader tasks without requiring another
   source.
3. Diagrams perform conceptual work and remain terminal-readable.
4. Tables compare, decide, or compress real choices.
5. Factual specifics receive a focused numbers/names/formulas check.
6. MDLOOM passes for the touched module and generated source-corpus artifacts
   are regenerated from canonical numbered guides.

## Exit Gate

Each module has a reviewed scope map, numbered guides, section/navigation
integration, source-corpus regeneration, and adversarial expert findings with
no unresolved BLOCK items.

## Closeout Summary

The wave is complete. Chemistry, clinical medicine, and pathology are first-class,
integrated 12-guide modules. Their canonical guides and generated source-corpus artifacts
validate cleanly, and all adversarial BLOCK/WARN findings are resolved. Pathology Pulse 05
received final PASS on 2026-07-12, closing the last wave gate. See `CLOSE.md`.

## Carry-Forwards

Da Vinci figure pinning, Gold promotion, and stronger external/source-custody evidence are
optional future promotion work. They are not blockers to this wave closeout.
