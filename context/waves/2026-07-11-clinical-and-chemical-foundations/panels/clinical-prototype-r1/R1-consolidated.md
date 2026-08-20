# Clinical Prototype R1 - Consolidated

> **Status (final).** This is the **prototype-round** panel for guides `03` and `08`. Its findings
> were repaired and the prototypes received **final sign-off** (see Decision). Two point-in-time
> statements below are **superseded** by Pulse 04: (a) the `medicine/10 §11` overlap is described as
> *forward-only / reverse deferred*, but a reciprocal pointer `medicine/10 §11` → `03` was later
> added, making the boundary **bidirectional**; and (b) "sign-off pending" / "module not integrated"
> notes were resolved when Pulse 04 integrated the module and regenerated the source corpus. The
> full-module adversarial review is recorded separately under `panels/clinical-full-r1/`.

## Decision

**REPAIRED and SIGNED OFF — no unresolved BLOCK or WARN findings after two strict
passes.** The first strict pass (R1, below) repaired the worked-case threshold math and
the pervasive advice-creep; a follow-up **strict re-review (R2)** then surfaced and closed a
further set of residual findings (banner/cheat-sheet imperatives, the correlated-test
inequality overreach, the routing-vs-responsibility conflation in guide 08, an over-strong
specialty-PPV claim, and a missing alternate-system case). With R2 closed, prototypes `03`
and `08` received **final prototype sign-off** and **Pulse 03 is DONE**; the two guides are
recorded prototype-complete in `STATUS.md` and now define the ratified quality/safety pattern
for the module. At the time of this panel `medicine/` was not edited, the module was not yet
wired into nav / `TRACKER.md` / `sections/`, and source backfill was not run — all completed
subsequently in Pulse 04, which also added the reverse `medicine/10 §11` → `03` pointer that
makes the overlap **bidirectional**.

## Repair Summary

| Area | Result |
|---|---|
| Worked-case thresholds (03) | Both positive and negative branches now computed for each varied treatment threshold, with T_test/T_treat recomputed (odds(p*) = H/B). Baseline flips only on the positive branch; at H/B = 0.05 the negative branch flips and testing is not moot; at H/B = 1.0 no branch crosses. The "both directions" and "testing moot" claims are removed. |
| Non-advice voice (03) | Diagrams, thresholds, worked cases, and the Decision Cheat Sheet recast into third-person model states ("the model favors …") for a hypothetical clinician; analytic equations retained but framed as decision rules, never advice. |
| Overgeneralizations (03) | "single most common diagnostic error" → "one of the common test-interpretation errors"; low prevalence "raises the false-positive share" without guaranteeing most positives are false; "many screening pathways" (designs vary); repeat testing can measure real temporal change. |
| Transport limits (03) | Added two contrasting fictional contexts (low-prevalence screening vs. enriched referral) plus a low-resource overlay, as model states without personalized advice. |
| `medicine/10 §11` overlap (03, STATUS, architecture, pulse) | Now a forward-only cross-reference from 03; reverse wiring in `medicine/10` deferred to a later minimal reconciliation or accepted+documented duplication. No false "already bidirectional" claim; 03 states `medicine/10 §11` holds a compact treatment and this guide is the deeper standalone version. *(R1-era, superseded — the reverse pointer `medicine/10 §11` → `03` was added in Pulse 04; the boundary is now bidirectional.)* |
| Referral ownership (08) | "Sending a referral alone transfers nothing"; ownership moves only on explicit acceptance of an agreed scope by a named owner; overall-patient / referred-problem / ordering / pending-result / follow-up ownership separated. |
| Closed-loop case + topologies (08) | Added an end-to-end fictional closed-loop comanagement case (question → acceptance → scope → ordering/result owner → communication → unresolved conflict → closure) and alternate topologies (direct access, district-hospital, task-shifting/CHW, teleconsult). |
| Specialty table (08) | Marked explicitly illustrative, grouped into service families, missing top-level families added; nephrology tightened to dialysis management and access coordination. |
| Prototype status | `03`/`08` marked prototype / in review in `STATUS.md`; pulse + WAVE updated; Pulse 03 held IN REVIEW. |

## Strict Re-Review (R2) — Residual Findings Closed

A second, stricter editorial pass over the two prototypes (advice-creep + honesty
re-check) surfaced five residual findings; all are now repaired in the guides. No
`medicine/` edits, no integration, no source backfill.

| ID | Guide(s) | Residual finding | Repair |
|---|---|---|---|
| R2-01 | 03 + 08 banners; 08 cheat sheet | Reader-directed **personal/emergency imperatives** ("consult a qualified professional," "contact your local emergency services") and imperative "Ask/Treat/Assign" cheat-sheet voice remained | Banners recast to a **descriptive scope statement** ("for personal concerns, appropriate care comes from qualified local professionals; emergencies are handled through local emergency services"); guide-08 Decision Cheat Sheet recast to third-person **"What the interface model shows"** states |
| R2-02 | 03 §6 (+ cheat sheet, confusion point) | Correlated-test treatment asserted a **universal inequality** (`LR_combined < LR_A × LR_B`) | Rewritten: multiplication assumes **conditional independence given status**; **positive** dependence usually **overstates** evidence, **negative** dependence can change direction; **no universal inequality**; general solution is a **validated joint conditional model or empirically estimated combined LR** |
| R2-03 | 08 §5 (+ landscape, tables, case, cheat sheet, confusions) | **Routing mechanism** and **responsibility contract** were conflated on one axis; "acceptance" was treated as sufficient to transfer | Reworked into **two independent axes** — routing (referral / e-consult / direct access) vs contract (advice-only consultation / shared care-comanagement / explicit transfer); a **label or bare acceptance transfers nothing** — only an **explicit, locally valid agreement + acknowledgment** does; landscape, tables, worked case, cheat sheet, and confusion points aligned |
| R2-04 | 08 §1, §3, cheat sheet, reader task | Specialty-setting **PPV** claimed to rise from referral alone | Qualified: PPV rises **only when** the referred population is **demonstrably enriched** *and* test performance **transports**; **spectrum effects can change Sn/Sp** |
| R2-05 | 08 §10 (new) | No **alternate-system** end-to-end case | Added a compact **district-hospital + task-shifting + teleconsult** case with named team ownership, escalation **acceptance**, **pending-result** ownership, and **closure** |

## Validation

- Focused PROOF (MAXIM `proof.toml`) via the `tools-infra/proof` Cargo manifest,
  scoped to the two prototype guides, re-run after the R2 repairs: **2 files checked,
  0 errors, 0 warnings**.
- `git diff --check`: clean (no whitespace/conflict errors); the prototype module is
  still **untracked** (not yet integrated), so the check was run against the two edited
  guides explicitly.
- Source backfill (PROOF/MDCROP/MDPORT/FLETCH) **not** run — this is a prototype
  boundary review, per the pulse scope.
- `medicine/` untouched; module not integrated into navigation, `TRACKER.md`, or the
  section landing page.

The prototypes now satisfy the wave quality gate for the two de-risked boundaries with
no unresolved adversarial findings after two strict passes; they received **final prototype
sign-off** (Pulse 03 DONE), and Pulse 04 then authored the remaining guides, integrated the
module, added the reverse `medicine/10 §11` → `03` pointer, and regenerated the source-corpus
artifacts. The full-module adversarial review is recorded under `panels/clinical-full-r1/`.
