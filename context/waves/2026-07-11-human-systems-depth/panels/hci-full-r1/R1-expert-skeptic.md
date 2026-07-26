# HCI Full-Module R1 — Expert-Skeptic

> **Historical R1 lens; superseded final disposition: PASS — Pulse 02 DONE.** At this
> review stage the `expert-skeptic` status was REPAIRED and awaited an independent final
> re-review. The final reviewer subsequently passed all content and record repairs. This is the
> preserved conservative, whole-module
> adversarial pass over all **twelve** `human-computer-interaction/` guides (`00`–`11`) plus the
> two reciprocal-pointer siblings (`cognitive-science/09-APPLIED-BRIDGE`,
> `industrial-design/06-INTERACTION-DESIGN`) and the source-corpus custody surface, run after
> authoring, integration, and backfill. The expert-skeptic lens owns **overclaim, model honesty,
> statistical/derivation rigor, the safety/ethics floor, and boundary accuracy**. Findings below are
> a conservative superset; each is **repaired** in the guides. This record is **review-only** and
> does not clear the gate — see the verdict. No commit/push.

## Scope reviewed

All twelve guides at peer depth; the `02`↔`09` unit-of-analysis seam and the `08`↔`10`↔`11`
safety/ethics seams; the four honesty invariants the module asserts (heuristics ≠ laws; conformance
is a floor; discovery ≠ measurement; named laws/standards attributed, dated, bounded); and the two
reciprocal pointers HCI added into `cognitive-science/09` and `industrial-design/06`.

## Findings

**ES-01 — BLOCK — Guide 01: QWERTY presented as *demonstrably* sub-optimal (a clean verdict on a
contested case).** The path-dependence bullet and a Common Confusion Point asserted QWERTY is
"demonstrably not optimal for speed," universal only by coordination — a one-sided verdict stated as
settled fact, and un-sourced, in a guide whose own banner says history is judged by **sourcing and
dating**. *Repaired:* the argument is now **sourced and dated** to Paul David, "Clio and the
Economics of QWERTY" (*American Economic Review*, **1985**), the founding path-dependence account,
and its premise is **explicitly contested** with Liebowitz & Margolis, "The Fable of the Keys"
(*Journal of Law and Economics*, **1990**), who argue the Dvorak-superiority evidence is weak. The
guide now keeps only the **durable mechanism** — standards persist through coordination, installed
base, and relearning cost *whether or not* the incumbent is optimal — and drops the clean
"demonstrably not optimal" claim in the bullet, the confusion point, and (aligned) `03`'s text.

**ES-02 — BLOCK — Guides 02 & 05: the interaction-model admission test did not match the model's unit
of analysis.** Guide `02`'s per-guide banner admitted a model *only* if it "localizes a breakdown to
a specific step and a specific gulf (execution vs evaluation) a think-aloud could confirm" — but the
guide itself **owns distributed cognition and activity theory**, which are **system-level** lenses
whose claims are about coordination across people/artifacts/time and are confirmed by **field study**
(`06`) with `09`'s group outcomes, not by mapping one gulf in a think-aloud. The banner therefore
contradicted §5 and the guide's own WEIRD caveat. `05`'s `02` scaling contract carried the same
single-gulf rule. *Repaired:* the `02` banner and the `05` scaling contract now **split by unit of
analysis** — individual-level models (Norman's stages/gulfs, modes, instrumental interaction, mental
models; GOMS/KLM as applied) localize to a step+gulf a think-aloud can test; **system-level lenses
predict a findable coordination/system breakdown, confirmed by a field study, and need not map one
gulf** — and both name the **mismatched-evidence error** (a think-aloud for a system claim, or a
field study for a single-user gulf) as a failure. §5's distributed-cognition prediction was reworded
from "a failure at the perceive/interpret stages" to a **system-level** hand-off breakdown, and a new
reader task exercises matching the model class to the evidence.

**ES-03 — BLOCK — `cognitive-science/09` reciprocal pointer: an unsupported voice extension and an
overstated Shannon derivation the pointer *certified*.** The Fitts section claimed the law "applies
to … voice command selection latency (distance = phonetic distance)" — an invented metric,
**self-contradicted** by the same guide's "Where these laws break" note that the Fitts motor
component *drops out* for voice. Separately, "The deeper point" asserted Fitts' Law **is** Shannon's
Theorem 17 and that the index of difficulty **is literally the channel capacity**, with both systems
"operating near their information-theoretic capacity limits" — a contested interpretation stated as
fact, and the reciprocal-pointer box promised the derivations "stay here," i.e. certified them.
*Repaired:* the **phonetic-distance** extension is removed (voice selection is a Hick-style *choice*
problem, not a Fitts motor one); "The deeper point" is bounded — Fitts **motivated** his index by
**analogy** to Shannon (MacKenzie's Shannon formulation is standard), but the literal-channel reading
is contested and alternative optimized-submovement/signal-dependent-noise derivations reproduce the
log form *without* channel capacity, while Hick's information-theoretic framing (which Hick himself
used, citing Shannon) is kept on its firmer historical footing; and the pointer box now **certifies
only the well-established forms, not their strongest interpretations**.

**ES-04 — WARN — Guide 09: the collaboration worked case coupled a coordination measure to a
patient-safety outcome.** The clinical shift-handoff case measured "coordination breakdowns (**missed
medications** flagged at handoff)" — an omission/coordination signal, but phrased as a patient-safety
outcome the seam elsewhere defers to `human-factors/`/clinical. *Repaired:* the measure is neutralized
to **handoff items dropped or left unacknowledged** (an omission/coordination measure), with an
explicit line that **HCI owns the coordination/omission measurement; whether a dropped item became a
patient-safety event is a `human-factors/`/clinical question**, not this guide's to score.

**ES-05 — WARN — Guide 10: BCI capability claims were undated and unanchored.** §5 asserted EEG BCIs
have "low information transfer rates" and "invasive BCIs achieve more" with no source or date — the
exact hype-vs-evidence looseness the guide exists to police. *Repaired:* the claims are **dated and
anchored** — the low-ITR characterization to the foundational review (Wolpaw et al., *Clinical
Neurophysiology*, **2002**) and the invasive high-water mark to recent single-participant intracortical
demonstrations (~90 chars/min handwriting, Willett et al., *Nature* **2021**; ~60–78 words/min
attempted-speech decoding, Willett et al. **2023**; Metzger et al. **2023**) — and **bounded** as
small-N research demonstrations carrying surgical risk, **not** a shipped/consumer capability.

**ES-06 — WARN — Guide 07: dual-axis charts framed as inherently deceptive.** The honesty section, the
worked case, a reader task, and the cheat sheet listed "dual axes" flatly among "deceptive encodings
to refuse" and said they "manufacture a correlation." A secondary axis is a **legitimate but
high-risk / manipulable** encoding, not automatically a lie. *Repaired:* dual axes are reframed as
**high-risk / manipulable — the second, independent scale can be set to manufacture an apparent trend,
so scrutinize, don't assume** — distinguished from the by-construction distortions (truncated baseline,
area-for-1D); the worked case, reader task 4, and the cheat sheet are aligned.

**ES-07 — WARN — Guide 05: two distinct detection-rate figures were conflated, and the discovery curve
was mis-rounded.** The heuristic-evaluation text computed "five evaluators find 75–85% … one finds
~35%" from "an average per-evaluator detection rate around **0.31**" — mixing the **discovery-model λ
≈ 0.31** (Nielsen & Landauer 1993) with the separately reported **~35% single-evaluator
heuristic-evaluation** average (Nielsen 1994); at λ = 0.31 one evaluator finds ~31%, not 35%.
Separately, the Poisson discovery curve rounded **n = 8 → 94%** where 1 − 0.69⁸ = 94.9% → **95%**.
*Repaired:* the two figures are held apart (0.31 is the discovery-model rate; ~35% is the distinct
heuristic-evaluation average, a different study lineage), one evaluator at λ = 0.31 is stated as
**~31%**, and the curve reads **n = 8 → 95%**.

## Safety / honesty invariant checks (whole module)

- **No manipulation playbook.** Holds — `07`'s deceptive-encoding reframe and `11`'s dark-pattern
  taxonomy remain recognize-and-refuse; ES-06 did not soften the refusal, only corrected the category.
- **Conformance is a floor; heuristics ≠ laws.** Holds — `05` heuristic caveats intact after ES-07;
  `08` overlay/conformance language intact.
- **Discovery ≠ measurement.** Holds and strengthened — `05`/`07` discovery-vs-measurement discipline
  intact; ES-07 corrects the figures it rests on.
- **Named laws/standards attributed, dated, bounded.** ES-01 (David/Liebowitz-Margolis), ES-03
  (Fitts/Hick/Shannon), ES-05 (BCI reviews), and the `03` ISO-9241-411 effective-throughput fix bring
  the remaining loose citations into line.
- **Boundary/deferral honesty.** ES-02 (unit of analysis → `06`/`09`), ES-04 (safety → `human-factors/`)
  keep the seams clean; the two reciprocal pointers no longer over-certify (ES-03).

## Decision

**Historical R1 decision: REPAIRED — no unresolved BLOCK or WARN after this pass.** The module
holds the peer-depth bar and the honesty invariants; the conservative pass surfaced one contested-case
overclaim (`01`), one unit-of-analysis mismatch across `02`/`05`, one over-certified sibling pointer
(`cognitive-science/09`), and four bounded honesty/precision defects (`09`, `10`, `07`, `05`). All are
repaired in the guides and validated by focused module-scope MDLOOM (0 errors, 0 warnings). Because
every fix was made in this same pass, this lens did not itself ratify. **Superseding final
disposition:** the final reviewer returned **PASS**; Pulse 02 is **DONE**. **No Da Vinci figure
invariants and no Gold eligibility** are claimed; the reference-editor lens and
`R2-gold-rubric.md` carry the tier decision (**Silver**, no registry).
