# Clinical Prototype R1 - Reference Editor

> **Historical (Pulse-03 prototype round) — partially superseded.** This is the reference-editor
> lens report for the two boundary prototypes (`03`, `08`). Its repairs stand, but finding **RE-01**
> is **superseded**: it recorded the `medicine/10` overlap as **forward-only** with the reverse
> pointer *deferred* (correct under the Pulse-03 guardrail against editing `medicine/`). Pulse 04
> later added the reciprocal pointer `medicine/10 §11` → `clinical-medicine/03`, so the boundary is
> now **bidirectional**. The prototypes received final sign-off (see `R1-consolidated.md`); the
> full-module review is in `panels/clinical-full-r1/`.

## Initial Decision

The prototypes are structurally strong (landscape diagram, layered formalism,
decision-useful tables, reader tasks, cheat sheet, confusions), but the first pass
carried two **Gold blockers** at the exact boundaries the prototypes exist to de-risk:
a dishonest description of the `medicine/10` overlap, and an incorrect universal claim
that a referral transfers ownership. Both are repaired, along with structural gaps in
guide 08 and the prototype status markers.

## Findings

### RE-01 - BLOCK: `medicine/10` overlap described as already bidirectional

Files: `clinical-medicine/03-DIAGNOSTIC-TEST-INTERPRETATION.md`,
`clinical-medicine/STATUS.md`, `context/waves/.../artifacts/CLINICAL-MEDICINE-ARCHITECTURE.md`,
`context/waves/.../pulses/03+clinical-medicine-architecture.md`

Finding: The architecture, pulse, and STATUS claimed the overlap with `medicine/10`'s
diagnostic-reasoning section was "resolved" via "**bidirectional** cross-references,"
while the wave guardrail forbids editing `medicine/`. A reverse pointer inside
`medicine/10` cannot exist without editing it, so the claim was false.

Fix: All four artifacts now state a **forward-only** cross-reference from
`clinical-medicine/03`; the reciprocal pointer in `medicine/10` is **deferred** to a
later minimal reconciliation, and publication/integration must either add it or accept
and document the duplication. Guide 03 additionally states plainly that `medicine/10 §11`
("Diagnostic Reasoning", ~lines 467–561) currently holds a **compact** diagnostic-
reasoning treatment and that this guide is the **deeper standalone decision-theory
version** — no promise that the references are already bidirectional.

*Superseded (Pulse 04): the reverse pointer `medicine/10 §11` → `03` was subsequently added,
so the boundary is now legitimately **bidirectional** — the R1 concern (a false bidirectional
claim with no reverse pointer) no longer applies because the reverse pointer now exists.*

### RE-02 - BLOCK: Guide 08 claimed referral itself transfers ownership

File: `clinical-medicine/08-SPECIALTY-INTERFACES.md`

Finding: The ownership diagram and table stated, universally, that a referral MOVES
ownership of a defined problem to the specialist. This mis-models real accountability
and is the root of the "I thought you had it" failure the guide warns about.

Fix: Recast ownership as gated by **explicit acceptance of an agreed scope by a named
owner**. "Sending a referral alone transfers nothing." The five ownerships are now
separated — **overall-patient, referred-problem, ordering, pending-result, follow-up** —
each with a default holder until reassigned by acceptance. The model table, load-bearing
rule, systems bridge, and the "referral vs consultation" confusion point are aligned.

### RE-03 - WARN: Guide 08 missing closed-loop case, topologies, and an honest table

File: `clinical-medicine/08-SPECIALTY-INTERFACES.md`

Finding: The guide asserted closed-loop and comanagement principles without an
end-to-end worked case; presented only the gatekept funnel; read as if the specialty
table were exhaustive while omitting whole top-level families; and used loose
nephrology wording.

Fix: Added an end-to-end fictional closed-loop comanagement case (§9) tracing question
→ acceptance → scope → ordering/result owner → communication → unresolved conflict →
closure, with an ownership trace. Added alternate topologies (direct access,
district-hospital, task-shifting / community-health-worker, teleconsult / hub-and-spoke)
with their invariants. Marked the specialty table **illustrative, not exhaustive**,
grouped it into coherent service families, and added missing top-level families
(general pediatrics, critical care, pulmonology, rheumatology, hematology, allergy/
immunology, dermatology, obstetrics & gynecology, clinical genetics). Tightened
nephrology to **dialysis management and access coordination**.

### RE-04 - NOTE: Prototype status not reflected in the manifest/tracking

Files: `clinical-medicine/STATUS.md`, `context/waves/.../pulses/03+...md`,
`context/waves/.../WAVE.md`

Finding: STATUS marked `03`/`08` as complete while they were still under boundary
review.

Fix: STATUS now marks both **prototype / in review** (with an in-review header); the
pulse records the R1 panel and repairs and stays **IN REVIEW** (not done); the WAVE
pulse row references this panel and the deferred reverse wiring.
