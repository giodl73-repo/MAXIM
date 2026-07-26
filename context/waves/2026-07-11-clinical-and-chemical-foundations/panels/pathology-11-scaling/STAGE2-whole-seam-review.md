# Pathology Scaling-Gate — Guide 11 Laboratory as a Quality System (STAGE-2 COMPLETE — PASS)

> **Status: STAGE-2 COMPLETE — PASS (clean re-review recorded 2026-07-12).**
> The completed-guide whole-seam `expert-skeptic` review that governs `pathology/11-QUALITY-ERROR-
> AND-THE-DIAGNOSTIC-LABORATORY-AS-SYSTEM.md` under MAXIM-PATH-24 and the architecture record's
> *Scaling Mini-Contracts* section was **executed over the whole `08`↔`11` seam and the
> governance/error/QC surface**. Its initial run returned a set of accuracy/seam findings (below),
> all of which were **repaired in the guide**; the **clean re-review has since been run — folded
> into the full-module `pathology-full-r1` pass — and guide `11` PASSES** with no residual
> seam/governance/accuracy findings. Guide `11` therefore **clears its Stage-2 scaling gate**.
> This is a *per-guide* clearance: both `09` and `11` have now cleared Stage 2; full-module
> R1 and R2 tier evidence are complete, and the final reviewer returned **PASS** on
> 2026-07-12. **Pulse 05 is DONE.** (Guide `09` cleared its Stage-2 review — see
> `../pathology-09-scaling/`.)

## Two-stage gate

| Stage | What it checks | Status |
|---|---|---|
| Stage 1 — representative high-risk sections | Pass on the **governance/accreditation** section and the **total-testing-process error-taxonomy/QC section that carries the `08`↔`11` seam**: (a) no `08` duplication/contradiction, (b) governance kept conceptual, dated, and non-prescriptive (no accreditation how-to or jurisdiction-specific compliance steps), (c) clean forward/back cross-reference with `08` | **Satisfied in-guide** |
| Stage 2 — completed-guide whole-seam review | A final `expert-skeptic` pass over the **entire `08`↔`11` seam and the whole governance/error/QC surface**, confirming the ownership split and non-prescriptive governance hold across the whole guide | **PASS (clean re-review 2026-07-12, folded into `pathology-full-r1`)** |

## Stage-2 findings and repairs (2026-07-12)

The whole-seam review returned the following findings; each has been repaired in the guide (guide
sections in parentheses). The repairs are content-accuracy and seam-ownership corrections, not
scope expansion.

1. **`08`↔`11` EQA/PT seam over-claimed.** The guide re-derived `08 §6` EQA/PT mechanics and
   asserted internal QC "can only agree with itself." **Repaired** (§Big Picture, §2): mechanics
   deferred to `08 §6`; IQC can detect *some* bias via assayed/independent controls, reference
   materials, calibration verification, and method comparison; EQA framed as an external
   *comparison* (not ground truth) and **broader than PT** (EQA ⊋ PT); `11` owns program
   governance, longitudinal review, limitations, corrective response, and alternatives when PT is
   unavailable.
2. **QC chart semantics wrong.** Levey–Jennings limits were said to come from the method's
   imprecision. **Repaired** (§2): limits come from the **control material's own mean/SD** measured
   locally; `1_2s` is a **warning**, rejection needs `1_3s`/multirule; bias/TEa/sigma inform **QC
   planning**, not chart-limit construction; added qualitative/microbiology/molecular/anatomic-IHC
   and pre-/post-analytic controls beyond quantitative chemistry.
3. **CAPA over-simplified.** The "corrective fixes the instance, preventive removes the class"
   bucket. **Repaired** (§6): correction/containment fixes the instance → impact assessment → cause
   analysis → **corrective action removes/controls the cause to prevent recurrence** →
   effectiveness verification; **preventive action / prospective risk control** treated as a
   separate, proactive activity.
4. **Accreditation mis-framed as conformance/certification.** **Repaired** (§7): accreditation =
   **ISO 15189:2022** scope-specific formal demonstration of **competence, impartiality, and
   consistent operation**, explicitly distinguished from **certification** (QMS conformance, e.g.
   ISO 9001); QC/EQA/audit/accreditation distinguished; **none attests an individual result**.
5. **Validation vs verification too shallow.** **Repaired** (§4): **objective-evidence** framing;
   **reference-interval verification** distinguished from method verification; **modified methods
   may require validation** when the intended-use boundary changes.
6. **Nonconforming-work / amendments shallow.** **Repaired** (§6): nonconforming work now covers
   affected-result assessment, communication, document/training impact, risk assessment,
   implementation monitoring, and effectiveness review; amendment metrics **stratified** —
   corrections/retractions are defects, **addenda are not automatically defects**.
7. **Audit instruments conflated; traceability over-claimed.** **Repaired** (§8, §9): internal
   audit, EQA/PT, M&M, and clinicopathologic autopsy distinguished; **routine traceability
   qualified against legal chain of custody** (the latter a stricter forensic regime, out of scope,
   pillar 3).
8. **No resource-constrained worked treatment.** **Repaired** (§11 Case D, Reader Task 6): manual
   paper records, split-sample/rechecking, and tiered referral / alternative EQA arrangement when
   PT is unavailable — no accreditation, digital-system, or backup-platform assumption.
9. **Reader tasks / cheat sheet / confusion points misaligned.** **Repaired**: Tasks 2–4 rewritten,
   Task 6 added, Decision Cheat Sheet, Common Confusion Points, and caveats realigned to all of the
   above.
10. **Records.** The `08`↔`11` ownership matrix rows are corrected in-guide; `STATUS.md`, the
    Pulse-05 record, and the architecture record's guide-11 scaling mini-contract carry a Stage-2
    repair note; guide `09` Stage-2 **PASS** recorded; guide `11` Stage-2 **PASS** recorded
    after the clean review.

## Stage-2 checklist (confirmed clean at re-review 2026-07-12)

Each gate criterion was re-confirmed clean at the re-review (folded into `pathology-full-r1`);
the formal PASS is granted:

- **`08`↔`11` ownership seam holds.** `08` owns per-result generation and the local QC needed
  to bound one result; `11` owns the cross-process program and **re-derives none of `08`'s
  metrology** (no re-derivation of imprecision/bias/TEcalc/TEa/MU/sigma/RCV/LoB). Any
  metrology re-derivation or contradiction of `08` = **BLOCK**.
- **Governance stays conceptual (highest scope risk).** No accreditation "how-to," no
  jurisdiction-specific compliance steps, no standard's clauses presented as instructions;
  standards named as dated/attributed concepts (e.g., ISO 15189, editions confirmed against
  the issuing body, not asserted from the guide).
- **Pillar 3 (no forensic/legal).** The autopsy appears **only** as a conceptual
  quality-audit boundary; cause-/manner-of-death and legal determination are out of scope.
- **Defer clinical system-safety to `clinical-medicine/11`.** Swiss-cheese/latent-error, just
  culture, RCA, HRO, Donabedian, PDSA are named by reference and applied to the laboratory,
  not re-taught; no creep into the clinical care-system scope.
- **Pillars 1 & 4.** No self-diagnosis/personal-result interpretation; third-person voice,
  `0` you/your; figures illustrative and setting-dependent (no universal error-share constant).
- **Depth bar.** Landscape, layered formalism (the TTP control loop, phase-indexed error
  taxonomy, the seam), worked fictional cases, decision tables, systems bridges, reader tasks,
  Decision Cheat Sheet, Common Confusion Points, resource/bias caveats all present.

## Decision

**PASS (clean re-review recorded 2026-07-12).** The Stage-2 whole-seam review returned the findings
above; all were **repaired** in `pathology/11-QUALITY-ERROR-AND-THE-DIAGNOSTIC-LABORATORY-AS-SYSTEM.md`,
and the **clean re-review has since been run (folded into the full-module `pathology-full-r1` pass)
with no residual seam/governance/accuracy findings**. The guide passes focused Cargo PROOF
(**0 errors, 0 warnings**, part of the module-scope run over all twelve pathology guides that
reports 0 errors), carries the four-pillar banner, holds **0** `you/your` (pillar-4 voice), keeps
governance conceptual/dated, and re-derives none of `08`'s metrology. Guide `11` **clears its
Stage-2 scaling gate**. Both `09` and `11` have now cleared Stage 2; final Pulse-05 sign-off is
**PASS** and Pulse 05 is **DONE**. Full-module R1 and R2 tier evidence are complete.
Integration, reciprocal wiring, and source backfill were completed in the module round rather
than this per-guide panel.
