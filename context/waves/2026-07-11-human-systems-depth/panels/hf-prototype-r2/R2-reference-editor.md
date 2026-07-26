# R2 Reference Editor — HF Prototype Boundary Gate (`02`, `03`, `06`)

Round-2 **strict, independent** editorial and factual pass over the three prototype guides
after the R1 repairs. This reviewer neither authored nor repaired the R1 findings. Lens:
factual/quantitative correctness of the worked passes (recomputable by hand), the source
hierarchy/edition of every load-bearing figure, the completeness of the scaling-gate
Definition of Done, and record consistency (STATUS / architecture / pulse / WAVE) including the
**truthfulness of the untracked-file validation claim**. Fixes were applied by the authoring
role in the same round and are marked *disposition: repaired*; because the raiser is
independent, this pass clears the gate — see the verdict.

## Finding Summary

| # | Guide/record | Lens | Severity | Disposition |
|---|---|---|---|---|
| RE2-01 | 02 | RNLE **coupling multiplier wrong for the stated height**: `CM = 0.95` is the `V < 75 cm` value, but the task states `V = 75 cm` (>= 75) with fair coupling, which is `CM = 1.00`; and `FM = 0.90` was asserted with **no stated frequency/duration** | BLOCK | repaired |
| RE2-02 | 02 | Joint-coverage arithmetic unreproducible and wrong ("about 0.84"); no method shown | BLOCK | repaired |
| RE2-03 | 03 | "**Four families**" mis-count: raw + weighted TLX are one *subjective* family; SAGAT measures *SA*, not a workload family; and one rating vector stood in for `n = 12` | BLOCK | repaired |
| RE2-04 | 06 | Before/after alarm metrics **asserted with no derivation**, and priority row **conflated "P3 / informational"** (informational = no-action ≠ a low-priority alarm) | WARN | repaired |
| RE2-05 | 02 | Scaling-gate **Definition of Done** listed only content gates and left "residual citation-risk logged for backfill" — no closure/sign-off gates, and citation risk allowed to remain open at sign-off | WARN | repaired |
| RE2-06 | records | Records still read IN REVIEW / gate-pending; the untracked-file validation claim ("`git diff --check` clean for the touched untracked files") was **not literally true** (git diff --check inspects tracked/indexed content unless intent-to-add is used); WAVE carried stale "remaining step" wording | NOTE | repaired |

BLOCK: 3 · WARN: 2 · NOTE: 1.

## Findings

### RE2-01 — BLOCK: NIOSH coupling multiplier wrong for the stated vertical height; FM unstated
File: `02` (§Q3 lifting-index sensitivity)

Finding: The RNLE table used `CM = 0.95` for "fair coupling," but `CM` depends on **both**
coupling quality **and** vertical height: for **fair** coupling, `CM = 0.95` only when
`V < 75 cm`; at `V >= 75 cm` (the case's stated `V = 75 cm`), fair coupling gives `CM = 1.00`.
The guide therefore applied the wrong-height value. Separately, `FM = 0.90` was labelled a
"table lookup" with **no frequency or duration stated**, so it was neither reproducible nor a
real cell of the frequency table.

Fix: Set **`CM = 1.00`** (fair coupling, `V >= 75 cm`), and state an explicit frequency/duration
— `F = 3 lifts/min`, duration `<= 1 h`, `V >= 75 cm` → **`FM = 0.88`** — reading both from a
**bounded excerpt of the public-domain NIOSH 94-110** applications manual (reproduced so the
values are traceable, and so the coupling term matches the *stated* height). Recompute:
`RWL = 23 · 0.833 · 1.000 · 0.910 · 0.904 · 0.88 · 1.00 ≈ 13.88 kg`; for a 15 kg load
`LI ≈ 1.08`; the H-sweep becomes `H = 25 → LI 0.90`, `30 → 1.08`, `35 → 1.26`, `40 → 1.44`. All
recomputed and internally consistent. *Disposition: repaired.*

### RE2-02 — BLOCK: joint-coverage value wrong and unreproducible
File: `02` (§Q2)

Finding: The `rho = 0.5` central-90%×90% coverage was written "0.81 < P < 0.90 (about 0.84)"
— the actual mass is **~0.8245**, and no method was shown, so the reader could not reproduce it.

Fix: Give the exact value **~0.8245** with the **method + inputs**: the probability mass of the
standard bivariate normal inside `[-1.645, +1.645] × [-1.645, +1.645]`, from the bivariate-normal
CDF `F2` by inclusion–exclusion `P = F2(z,z) - F2(-z,z) - F2(z,-z) + F2(-z,-z)`, `z = 1.645`;
keep the independent `0.90^k` (0.8100 / 0.729 / 0.656) for contrast, and bound it over a
plausible `rho ∈ [0.3, 0.7]` (~0.815–0.839). *Disposition: repaired.*

### RE2-03 — BLOCK: "four families" mis-count and single-vector-as-study
File: `03` (Worked Quantitative Pass)

Finding: The pass said "**four instrument families**." Raw TLX and weighted TLX are two scorings
of **one** family (subjective); primary and secondary task are **performance**; SAGAT measures
**situation awareness**, a different construct, not a workload family. The count is wrong on two
counts, and a single rating vector represented an `n = 12` study.

Fix: Recast to **five instruments spanning two workload families** (subjective TLX raw+weighted;
performance primary+secondary) **plus** an SA probe (SAGAT); relabel the section "the five
instruments … (participant P)"; frame the whole pass as **one representative participant** with
**common weighting** across A and B; recompute the Old-console weighted TLX (58.8 → **53.9**)
consistent with the common weights. *Disposition: repaired.*

### RE2-04 — WARN: alarm metrics not derived; P3/informational conflated
File: `06` (Worked Quantitative Pass — before/after alarm metrics)

Finding: Every before/after figure (62 → 9 /hr, 220 → 14 /10 min, etc.) was asserted with no
derivation, and the priority row read "~75% **P3/informational**." An **alarm** — at any
priority P1/P2/P3 — requires an operator action by definition; an **informational** message
requires none and is **not** an alarm. Fusing "P3" with "informational" mis-defines both.

Fix: Add a **traceable fictional event inventory + explicit aggregation rules** that yield each
metric (a quiet-hour class breakdown — chattering 21, standing 8, informational 8, actionable 25
= 62, so 40% actionable; the after projection consolidates cascade duplicates and moves the
informational messages out). **Separate alarms from informational notifications**: P1/P2/P3 are
three **urgency bands of action-requiring alarms**; the ~8/hr no-action messages are
**reclassified to a separate notification channel** (a new metric row), not counted as P3. The
"~75% P3" is relabelled "lowest-urgency but **still action-requiring**." *Disposition: repaired.*

### RE2-05 — WARN: Definition of Done lacked closure/sign-off gates
File: `02` (Testable Definition of Done)

Finding: The DoD listed eight **content** gates but left source verification as "residual
citation-risk **logged for backfill**," i.e. citation risk could remain open at sign-off, and it
named no process gates for MDLOOM, metadata/custody, independent review, or records/integration.

Fix: Strengthen gate 4 to **edition verification** and add **five closure gates** every
remaining guide must also pass: (9) ordinary MDLOOM with no BLOCK/WARN; (10) truthful metadata &
**source-custody transition** (prototype→real custody only after backfill artifacts exist);
(11) **source-hierarchy/edition & citation-risk closure** — *citation risk cannot remain
unresolved at sign-off*; (12) **independent adversarial closure** (the R2 pattern; no
self-ratification); (13) **records & integration closure**. *Disposition: repaired.*

### RE2-06 — NOTE: records advanced to DONE; untracked-file validation made truthful
File: `STATUS.md`, `HUMAN-FACTORS-ARCHITECTURE.md`, the pulse record, `WAVE.md`

Finding: With the gate now independently cleared, the records needed to move from IN REVIEW /
gate-pending to **DONE / ratified**, and two truthfulness items needed fixing: (a) the pulse's
"`git diff --check` clean for the touched untracked files" is not literally true, because
`git diff --check` inspects **tracked/indexed** content unless the files are staged with
**intent-to-add**; (b) WAVE still said the "adversarial boundary-gate panel is the remaining
step," stale now that R1 ran and R2 has signed off.

Fix: STATUS, architecture, pulse, and WAVE updated to **DONE / ratified (R1 + independent R2)**;
the pulse Validation now states MDLOOM checks the guides **explicitly by path** (module untracked;
STATUS/00/`context` MDLOOM-excluded) and that `git diff --check` was run **after `git add -N`
(intent-to-add)** and then unstaged, so the whitespace/conflict check genuinely covers the
untracked guides. Scope was kept **human factors** (no Westgard/lab-QC drift), and **no sibling
module was edited**. *Disposition: repaired.*

## Style / structure check (all three guides)

| Lens | Assessment |
|---|---|
| Landscape-first + layered; single H1; Decision Cheat Sheet present | PASS |
| Diagrams do conceptual work (joint-distribution, RNLE excerpt, TLX table, EID, evidence/acceptance) | PASS after edits |
| Worked passes recomputable by hand | PASS: joint 0.8245; RWL 13.88 / LI 1.08 / sweep 0.90–1.44; RTLX A 49.2 B 48.8, weighted A 53.9 B 60.3; alarm inventory sums to 62 (40% actionable) |
| Dates/standards attributed & at the correct edition | PASS: NIOSH 1993/1994 + 94-110 lookup; EEMUA 191 4th ed. 2024; ANSI/ISA-18.2-2016; IEC 62682:2022 |
| Reader tasks answerable, computation/boundary-focused | PASS (5 each) |
| Focused MDLOOM | PASS — 3 files checked, 0 errors, 0 warnings |

## Verdict

Factual, quantitative, DoD, and record defects in this lens are corrected and reproducible, and
focused MDLOOM is green. As the raiser is independent of the repairs, this pass **clears** the
gate. **Recommend: ratify; Pulse 03 → DONE.**
