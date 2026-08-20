# R2 Expert Skeptic — HF Prototype Boundary Gate (`02`, `03`, `06`)

Round-2 **strict, independent** adversarial pass over the three `human-factors/` prototype
guides after the R1 repairs. This reviewer **neither authored nor repaired** the R1 findings,
so — unlike R1 — this pass may ratify. Lens: advice-creep into operational instruction,
over-claim beyond a model's validity domain, construct/threshold reification, point-estimate
over-precision, participant/aggregation honesty, and **fictitious authority** at the
HCI↔HF↔domain seam (a reference module cannot sign off or veto a real system). Findings the
strict pass raised were repaired by the authoring role in the same round and are marked
*disposition: repaired*; because the raiser (this panel) is independent of the repairs, the
gate **is** cleared — see the verdict.

## Finding Summary

| # | Guide/record | Risk | Severity | Disposition |
|---|---|---|---|---|
| ES2-01 | 02 | Worked case implied the NIOSH RNLE **models heat** ("hot case dominating in the model") — heat is **outside** the equation's validity domain (§6.1), so the claim over-extends the model | BLOCK | repaired |
| ES2-02 | 02 | Residual **actionable workplace phrases** survived R1: "more frequent short rests," "make it adjustable / place the cart," and the non-WEIRD imperative triple "cut the horizontal distance, raise the origin, remove the twist" | BLOCK | repaired |
| ES2-03 | 02 / 06 / STATUS / arch | HCI↔HF↔domain seam granted the **reference modules sign-off / veto authority** ("all three sign off," "HF veto," "HCI veto," "final acceptance" by a module) — fictitious authority over a real system | BLOCK | repaired |
| ES2-04 | 02 | `rho = 0.5` joint coverage given as a **point estimate** ("about 0.84"), and `rho` treated as a constant, hiding its own uncertainty | WARN | repaired |
| ES2-05 | 03 | Worked pass computed **one rating vector** but narrated `n = 12`, blurring participant-level vs group-level and using inconsistent (condition-specific) weighting | WARN | repaired |

BLOCK: 3 · WARN: 2.

## Findings

### ES2-01 — BLOCK: the lifting model was made to "model" heat, outside its domain
File: `02` (Fully Worked Case, step 5)

Finding: Step 5 said summer heat "in the model, effectively increases the load, so a modeled
comparison of the **hot** case against the nominal one shows the hot case dominating." The
revised NIOSH equation has **no thermal term**; §6.1 explicitly places *extreme heat* outside
its validity domain (the model assumes a moderate thermal environment). Presenting a "hot vs
nominal" RNLE comparison implies the equation quantifies heat — an over-claim, and internally
contradictory with the guide's own validity-domain section.

Consequence: A reader could believe the Lifting Index captures thermal strain; the "sensitivity
variable" swept is one the model does not contain.

Fix: Recast step 5 so environment is an explicit **out-of-model modifier**: extreme heat sits
outside the RNLE domain (§6.1), the equation does **not** quantify it, and **no "hot RWL" is
computed**; heat's cardiovascular effect is handled qualitatively (§7) or by tools that model
thermal strain. The legitimate in-model sensitivity is over a variable the equation *contains*
— the horizontal-distance sweep of §Q3 — not temperature. *Disposition: repaired.*

### ES2-02 — BLOCK: residual actionable workplace phrases
File: `02` (§7 work–rest; Fully Worked Case step 2; non-WEIRD contrasting case)

Finding: Three imperative/workplace-directive phrases survived R1's main-case repair:
(1) §7 "more frequent short rests generally clear fatigue better than one long break";
(2) worked-case step 2 "make it *adjustable* … place the cart so the 5th-percentile reach
succeeds"; (3) the non-WEIRD case's conceptual-lens gloss "cut the horizontal distance, raise
the origin, remove the twist." Each reads as an instruction to change a real workplace.

Consequence: The safety/ethics contract forbids operational instruction; these are exactly that.

Fix: Recast all three as **hypothetical variable comparisons / design hypotheses** requiring
**qualified assessment and local validation**: work–rest becomes "how recovery is distributed
is a design variable … a hypothesis to model and validate locally, not a schedule this guide
sets"; step 2 becomes fixed-vs-adjustable and nearer-vs-farther **variant comparisons** whose
adoption "is a matter for qualified assessment and local validation"; the non-WEIRD gloss
becomes "comparing variants — nearer vs farther changes the horizontal term, higher vs lower
origin the vertical term, twist-free vs twisting the asymmetry term — not a directive to alter
any real task." *Disposition: repaired.*

### ES2-03 — BLOCK: reference modules given sign-off / veto authority (fictitious authority)
File: `06` (§9 seam box + text; prototype seam contract), `02` (§8; reader task 5; DoD common
contract), `STATUS.md`, `HUMAN-FACTORS-ARCHITECTURE.md`

Finding: The seam was drawn as "joint acceptance — all three **sign off**," with "HF veto" and
"HCI veto," and the **domain module** owning "final acceptance." MAXIM modules are educational
references; they own **methods and evidence**, not authority to accept, sign off, or veto a
real deployment. Assigning them acceptance/veto is fictitious authority — the same class of
over-reach as certification, which the contract forbids.

Consequence: Readers could infer a knowledge module (or its authors) can accept or block a real
safety-critical system.

Fix: Recast the seam everywhere to **evidence vs acceptance**: HCI supplies
interaction/visualization/accessibility **methods/evidence**; HF supplies workload/error and
**performance-under-stress evidence**; **acceptance and implementation are owned by the
accountable domain organization and its regulator** (legal obligation to `law/`). Explicit new
rule: "a reference module supplies evidence; it does not sign off or veto." Aligned in `06`
(§9 box retitled *Evidence + Acceptance*, RULE reworded), `02` (§8, task 5, DoD contract),
`STATUS.md`, and the architecture seam. *Disposition: repaired.*

### ES2-04 — WARN: `rho = 0.5` joint coverage as an over-precise point estimate
File: `02` (§Q2 joint accommodation)

Finding: The bivariate box coverage was written "0.81 < P(both central) < 0.90 (about 0.84)"
— both **wrong** (the true value is ~0.8245) and framed as a single point, with `rho` treated
as a fixed constant despite being a sampled, dataset-dependent quantity.

Fix: State the exact value **~0.8245** with the **method and inputs** (mass of the standard
bivariate normal inside `[-1.645, +1.645]^2` via the bivariate-normal CDF by inclusion–
exclusion) and, because `rho` is itself uncertain, give a **bounded range**: over a plausible
`rho` in `[0.3, 0.7]` the joint fraction moves only within ~0.815–0.839, so the conclusion
(~0.82, below 0.90, above 0.81) is robust to the exact `rho`. *Disposition: repaired.*

### ES2-05 — WARN: participant-vs-group ambiguity in the TLX worked pass
File: `03` (Worked Quantitative Pass)

Finding: The pass narrated `n = 12` operators but computed a **single** six-subscale vector and
presented condition-specific weights, so the reader cannot tell whether the numbers are one
person's or a group's, and the weighting was not held common across conditions.

Fix: Explicitly **follow one representative participant (P)**, with weights elicited **once**
and applied to **both** consoles (common weighting), showing A **and** B ratings and computing
both composites; state that aggregating the twelve and testing for significance is
`statistics-applied/`'s job. *Disposition: repaired.*

## Safety / authority check

No operational instruction, certification, accident/legal determination, or individual fitness
assessment survives in any of the three guides; every model/standard/stereotype stays dated,
attributed, and bounded; and — after ES2-03 — **no reference module claims acceptance, sign-off,
or veto** over a real system. Scope stayed **human factors** throughout: no drift into
lab-QC/Westgard or other sibling territory, and no sibling module was edited.

## Verdict

The strict pass finds the prototypes now hold the advice-creep, model-domain, reification,
point-estimate, participant-honesty, and fictitious-authority lines, and focused PROOF stays
green. Because this reviewer is **independent of the authoring/repair role**, the findings it
raised and saw repaired **do** clear this lens. **Recommend: ratify the prototype pattern/gate;
Pulse 03 → DONE.**
