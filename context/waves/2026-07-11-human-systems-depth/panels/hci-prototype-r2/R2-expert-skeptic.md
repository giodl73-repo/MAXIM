# R2 Expert Skeptic — HCI Prototype Boundary Gate, Strict Re-Review (`05`, `08`)

Independent strict re-review of the two prototype guides after the R1 repairs. This is the
**R2** round R1 required: R1 raised and fixed its own findings and therefore could not
ratify. R2 re-derives the numbers from the stated inputs, re-reads the honesty language end
to end, and clears a residual set of strict-editor findings. Review-only record; the fixes
it calls for were applied in this repair-and-R2 pass and are marked *disposition: repaired*.

## Independent re-derivations (R1 checklist items 1–3)

| Quantity | Stated inputs | R2 recomputation | Guide value | Match |
|---|---|---|---|---|
| Completion CI, 4/5 | Wilson score, 95%, p̂=0.8, n=5 | center 0.670, half-width 0.294 → **[0.38, 0.96]**, ±29 pts | [0.38, 0.96], ±29 | yes |
| Completion CI, 88% | Wilson score, 95%, p̂=0.88, n=40 | **[0.74, 0.95]** | [74%, 95%] | yes |
| SUS mean CI | *t*-interval, mean 77, SD 16, n=40 | SE 2.53, t(39,.975) 2.02, margin 5.1 → **[72, 82]** | [72, 82] | yes |
| SUS one-sided .05 bound | 95% one-sided lower, same inputs | 77 − 1.645·2.53 = **72.8 (≈73)** < 75 | "≈73 … below 75" | yes |

Every headline number in `05` reproduces from its stated method and inputs. The Wilson
interval and the SUS *t*-interval are both correct and internally consistent (no residual
adjusted-Wald / ±30 / [0.44, 0.96] discrepancy from R1's ES-01).

## Findings

### ES2-01 — WARN: target-rule α-equivalence was misstated
File: `05` (worked case pass rule; "Reading against targets"; §9 / cheat sheet)

Finding: The pre-committed pass rule ("the entire 95% CI at or beyond target") was annotated
as *"equivalently, a one-sided test clears it at α = .05."* That equivalence is wrong. A
**two-sided 95%** interval lying wholly beyond the target corresponds to a one-sided test at
**α = .025** (2.5% in the relevant tail). A one-sided **α = .05** decision uses the **95%
one-sided lower bound** — equivalently the lower limit of a **90% two-sided CI** — not the
two-sided 95% interval.

Consequence: A reader would under-state the stringency of the precommitted rule by a factor
of two in α, and could mislabel a borderline result.

Fix: State the precommitted rule exactly — *whole two-sided 95% CI at/beyond target = the
conservative α = .025 rule* — and give the α = .05 alternative (95% one-sided lower bound =
90% two-sided CI limit). Align the worked case, reader task 3, and the cheat sheet (new
"Claiming a fixed target is met" row). Worked-case check added: even the less-strict α = .05
bound (≈73) is below the 75 target, so the SUS target is not demonstrated under *either*
rule. *Disposition: repaired.*

### ES2-02 — WARN: "ground-truthier" overclaims empirical methods
File: `05` (Big Picture, consequence 2)

Finding: Empirical methods were called *"expensive and ground-truthier."* "Ground-truthier"
smuggles back the ground-truth framing the module elsewhere rejects: user testing is
**directly observed** behavior, but it is still bounded by the sample, tasks, and context —
not a truth oracle.

Fix: Replace "ground-truthier" with **directly observe behavior — evidence that is still
sample-, task-, and context-bounded, never ground truth.** The remaining "ground truth"
mentions in `05` / `08` are all *negations* ("no single method is ground truth," "verbal ≠
ground truth," "never ground truth") and are correct honesty statements; left intact.
*Disposition: repaired.*

### ES2-03 — WARN: the automated-recall fraction is stated too precisely for its evidence
File: `08` (§6 recall note; confusions)

Finding: The automated-accessibility **recall** figure was given as *"about a third"* (and
"~30–40%"). No **named primary comparison and denominator** is cited; the guide itself
concedes the number varies with tool, ruleset, page, and how a barrier is counted. A precise
fraction with no fixed denominator is exactly the over-precision this lens exists to catch.

Fix: Remove the precise fraction. State recall qualitatively — **a minority / limited
recall, well below 100%** — and say explicitly that, absent a named primary comparison and
its denominator, no single figure is defensible. The attributed WebAIM Million 2024 (~96% of
home pages have detectable errors) is a *different* quantity (prevalence of detectable
failures, named source) and is retained. *Disposition: repaired.*

## Model-honesty re-read (R1 checklist item 3)

| Claim under test | R2 read | Result |
|---|---|---|
| `05` axes are a *starting filter*, not a decision procedure | six fit factors intact; "narrow, not decide" holds | PASS |
| `05` discovery ≠ measurement | Wilson / `t` split, λ-caveats, "unresolved not refuted" all present | PASS |
| `08` five independent axes (no nesting, no "binary-ish floor") | axes read as independent end to end; no residual nesting | PASS |
| `08` distinct AT mechanisms (not "it's all the keyboard") | keyboard / a11y-API-tree / touch-pointer-voice-switch kept separate | PASS |
| `08` conformance is a floor; testing is bounded, not ground truth | intact after ES2-02 / ES2-03 wording fixes | PASS |

## Verdict

The prototypes reproduce their own statistics, state the target rule with the correct α
semantics, and carry no residual ground-truth or over-precise-recall overclaim. On this
lens the two guides now hold under strict re-derivation. Combined with the reference-editor
lens and the R1-repair verification, this round **ratifies** the prototype pattern — see
`R2-consolidated.md`.
