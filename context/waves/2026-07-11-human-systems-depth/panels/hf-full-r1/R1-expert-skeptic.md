# Human-Factors Full-Module R1 — Expert-Skeptic

> **Disposition: REPAIRED IN THIS PASS — wave remains IN REVIEW pending an independent final
> re-review.** This is the conservative, whole-module adversarial pass over all **twelve**
> `human-factors/` guides (`00`–`11`), run after authoring, integration, and source-corpus
> backfill — the full-module panel that Pulse 04's Definition-of-Done closure gate 12 named as its
> outstanding requirement. The expert-skeptic lens owns **overclaim, quantitative/model rigor,
> safety-floor honesty, and boundary accuracy**. Every finding below is a conservative
> superset and is **repaired in the guides**. Because this lens both raised and repaired the
> findings, it **cannot self-ratify**; the wave stays **IN REVIEW** until an independent reviewer
> re-derives the passes. No commit/push. No Gold/Da Vinci; the tier decision lives in
> `R2-gold-rubric.md` (**Silver**, no registry).

## Scope reviewed

All twelve guides at peer depth; the quantitative worked passes in `05` (HRA/HEP), `07`
(automation trade), `08` (bow-tie/common-cause), `09` (cross-domain alarm), `10` (coverage), and
`11` (safety metrics); the module's honesty invariants (every number is a bounded, dated,
method-relative estimate; the module supplies methods/evidence, not acceptance; accessibility is a
≥2-channel safety requirement); and the cross-guide numerical consistency of the shared HEP value
between `05` and `08`.

## Findings

**ES-01 — BLOCK — Guide `05` (HRA): the error-factor uncertainty convention was mis-stated, the
bounded-probability ceiling was ignored, and the SPAR-H adjustment was applied outside its
documented ≥3-negative-PSF trigger.** The "report a RANGE" box asserted a central HEP ~0.29 with a
lognormal error factor EF ~5 "spans ~0.06 to ~0.9" — but the standard NUREG error-factor convention
is `EF = sqrt(P95/P05)`, so `P95 = median×EF = 0.29×5 = 1.45`, **not a probability**; the "0.9"
upper bound was asserted with **no stated method**, and the box never acknowledged that a HEP lives
in `(0,1]`. Separately, the PSF-sensitivity sweep applied the SPAR-H adjustment formula
`HEP_adj = NHEP·P / (NHEP·(P−1)+1)` at time ×1 and ×0.1 — where only **two** PSFs are negative — even
though the guide's own excerpt correctly states the adjustment applies **only at ≥3 negative PSFs**,
and it even evaluated the formula with a nonsensical negative `(P−1)` term. *Repaired:* the box now
**defines the EF convention** (`EF = sqrt(P95/P05)`; band `[median/EF, median×EF]`), shows
`P05 = 0.06` is valid but `P95 = 1.45` is inadmissible (a lognormal with median 0.29 and EF 5 puts
~10% of its mass above 1), and requires an explicit **bounded-probability treatment** — truncate and
renormalize at HEP = 1, or a logit-normal/Beta — which gives a 90% band of **~[0.06, 0.8]**, the 0.8
being a property of the bounded model, **not** read off EF. The sweep now honors the **≥3-negative-PSF
trigger** (adjust at ×10 → 0.288; plain product at ×1 → 0.04 and ×0.1 → 0.004), the worked-case step,
the honest-output line, and reader tasks 1–3 are aligned.

**ES-01a — BLOCK (cross-guide consistency) — Guide `08` carried the same unmethoded "0.06–0.9"
human-term range.** The bow-tie worked pass and reader task 2 propagated the operator HEP as
"0.06–0.9 (guide 05)". *Repaired:* both now read the corrected bounded range **~0.06–0.8**, and the
human-term-alone top-event propagation reads **~6e-5 to ~8e-4 /yr**, consistent with `05`.

**ES-02 — BLOCK — Guide `07` (automation): the expected-cost model charged L1 a takeover failure it
cannot have, used a single global takeover multiplier instead of a common off-normal probability
with level-specific conditional costs, and the sweep was read as crowning a winner.** The model
`E(L) = (1−p)·W(L) + p·K·F(L)` applied the same `p·K·F(L)` failure term to **L1 (human decides)** —
but at L1 there is no automation to hit a limit and no takeover, so L1 cannot carry a
takeover-failure cost. It also folded all level dependence into one `F(L)×K` term rather than
separating the **common** off-normal-scenario probability from the **level-specific** conditional
cost, and the reading implied L2 was the answer. *Repaired:* the model is redesigned as
`E(L) = (1−p)·W(L) + p·C(L)` with `p` an explicit **common off-normal-scenario probability** (a
property of the world, identical across levels) and `C(L)` a **level-specific conditional cost given
an off-normal**; **`C(L1)` carries no takeover/OOTL term** (the human never left the loop). With
`W = [8,5,3,1]`, `C = [3,12,30,60]`, the sweep recomputes cleanly and the optimum **slides L4 → L3 →
L2 → L1** as off-normals grow more common (p = 0.01 → L4 = 1.59; p = 0.08 → L3 = 5.16; p = 0.15 →
L2 = 6.05; p = 0.30 → L1 = 6.50) — **every level is optimal for some p, so the model crowns no
winner**; it prices the trade only. Reader task 2, the fictional-case step, the uncertainty note,
and the cheat sheet are aligned.

**ES-03 — BLOCK — Guide `10` (methods): the coverage frame used overlapping, non-orthogonal
"strata."** The sampling frame merged **experience** (novice/experienced) and **sensory/
anthropometric tail** into a single 3-way "operator stratum," then multiplied `3 (S) × 2 (T) ×
2 (C) = 12` cells — but an experienced operator can *also* be in the sensory tail, so the "tail"
level overlaps the experience levels and the percentage double-counts. *Repaired:* the frame now
uses **orthogonal, fully crossed factors** — **Experience × Profile × Task × Shift = 2×2×2×2 = 16
cells** — with an explicit note that experience and sensory/anthropometric profile are distinct axes
that must be crossed, not merged, and an alternative **requirements-coverage matrix** is offered.
The convenience sample recomputes to **1/16 ≈ 6%**, the coverage-designed sample to **16/16 = 100%**,
and the "signature failure" text, the fictional case, and reader task 2 are aligned.

**ES-04 — BLOCK — Guide `09` (domain applications): the guide issued prescriptive interventions
instead of candidate mechanisms and evidence questions.** The cross-domain alarm pass concluded
"so the **FIX is the same** (rationalize: demote no-action alarms to notifications…)"; the healthcare
section framed a "structured handover" as "a communication defense"; and the low-resource example
prescribed "a **paper checklist and a structured verbal handoff**" and "the cheapest reduction (a
**second check** at the highest-severity step)." For a guide whose whole thesis is *apply-and-defer*,
naming specific interventions crosses from evidence into recommendation and pre-empts the domain
owner. *Repaired:* every prescription is reframed as a **candidate mechanism / evidence question**
with **selection and acceptance deferred to the domain owner** under its own hazard-review/change
process — the alarm pass now raises the actionable-fraction *question* and defers the fix; the
handoff bullet is a "candidate mechanism the domain must select and verify"; and the low-resource
example names candidate mechanisms and routes *which* affordable form (if any) to the hospital's own
review and local testing (`10`), removing the "second check" prescription.

**ES-05 — WARN — Guide `08` (hazard): the barrier taxonomy was presented as a universal strength
ranking, and the combustible-dust example gave actionable barrier advice.** The "BARRIER STRENGTH"
box ordered Hollnagel's four types "strongest → weakest," reading reliability off the category; and
the low-resource dust example "favors one strong physical/functional barrier the cooperative *can*
build (venting, housekeeping…, mechanical isolation)" — actionable barrier advice for a specialized,
standards-governed combustible-dust hazard. *Repaired:* the box is retitled **BARRIER TYPES — a
classification by nature, not a universal strength ranking**, and states that a specific barrier's
reliability depends on design, maintenance, demand rate, and context and must be **assessed**, not
read off the category (a corroded relief valve can be worse than a well-drilled procedure). The dust
example is reframed to apply the **reasoning pattern without issuing barrier advice** — barrier type
vs count is a concept and a set of *questions*; **which** barriers suit a dust-explosion hazard
belongs in a **domain hazard review / Management of Change (MoC)** owned by the cooperative and the
competent authority under combustible-dust standards. Separately, the **common-cause decomposition**
is made explicit (each barrier's failure split into a shared-instrument part that defeats both and an
independent residual part), addressing the same finding's dependency clause.

## Safety / honesty invariant checks (whole module)

- **Every number is a bounded, method-relative estimate.** Holds and is strengthened — ES-01 fixes
  the HEP bounded-probability treatment, ES-02 makes the automation model illustrative (no winner),
  ES-03 fixes the coverage arithmetic, and `08`/`09`/`11` worked passes remain explicitly synthetic.
- **Methods/evidence, not acceptance.** Holds — ES-04 removes the domain prescriptions and ES-05
  removes the dust barrier advice, keeping acceptance and intervention selection with the domain
  owner and its regulator.
- **Accessibility as a ≥2-channel safety requirement.** Now honest module-wide after the
  reference-editor's RE-04 added the explicit note to `01`,`03`,`05`,`09`,`10`.
- **Named models/standards attributed, dated, bounded.** ES-01 (SPAR-H/NUREG-CR-6883, EF
  convention), plus the reference-editor's Leveson-2011 and RNLE-1993/1994 fixes, bring the loose
  citations into line.

## Decision

**REPAIRED — no unresolved BLOCK or WARN after this pass, but the lens does not itself ratify.** The
module holds the peer-depth bar and the honesty invariants; the conservative pass surfaced four
quantitative/model BLOCKs (`05` EF/ceiling/trigger, `07` L1-takeover/model, `10` overlapping strata,
`09` prescriptions) and one WARN (`08` barrier ranking + dust advice), all repaired in the guides and
validated by focused module-scope MDLOOM (**12 files, 0 errors, 0 warnings**). Because every fix was
made in this same pass, an **independent final re-review is still required**, so the wave stays **IN
REVIEW**. The reference-editor lens and `R2-gold-rubric.md` carry the tier decision (**Silver**, no
registry).
