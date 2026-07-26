# Clinical Prototype R1 - Expert Skeptic

> **Historical (Pulse-03 prototype round).** This is the expert-skeptic lens report for the two
> boundary prototypes (`03`, `08`); its repairs stand and established the module's advice-creep and
> quantitative-honesty pattern. The prototypes received final sign-off (see `R1-consolidated.md`);
> the full-module advice-creep review across all 12 guides is recorded in `panels/clinical-full-r1/`.

## Judgment

The two boundary prototypes (`clinical-medicine/03`, `clinical-medicine/08`) hit the
intended quantitative and architectural depth, but the first pass carried two blocking
defects: a **worked-case threshold error** that overstated what the test decision does,
and pervasive **advice-creep** (imperative, second-person voice) that made an
educational reference read like instructions to the reader. Both are repaired. Several
overgeneralizations were hedged. No unsafe procedural or dosing guidance was present.

## Findings

### ES-01 - BLOCK: Worked-case threshold sensitivity was mis-stated

File: `clinical-medicine/03-DIAGNOSTIC-TEST-INTERPRETATION.md`

Finding: The central worked case claimed a single result "flips the decision in BOTH
directions" at the 10% baseline, and the sensitivity table asserted that at H/B = 0.05
"testing may be moot." Branch-by-branch math contradicts both. At baseline (p* = 20%)
only the **positive** branch crosses p* (10% → 40%); the negative branch (→ 1.3%)
merely confirms "no treat." At H/B = 0.05 the treatment threshold recomputes to
p* = 4.76%, the baseline flips to "treat," and the **negative** posterior (1.3%) falls
*below* p*, so a negative result changes management — testing is **not** moot.

Fix: Both branches are now computed for every varied threshold, with T_test/T_treat
recomputed per threshold (odds(p*) = H/B; T_test = odds(p*)/LR+, T_treat = odds(p*)/LR−):
H/B = 0.05 → zone 0.83%–29.8% (negative branch flips); 0.25 → 4.0%–68.0% (positive
branch flips); 1.0 → 14.3%–89.5% (10% is below T_test, no branch crosses). The
"both directions" and "moot" claims are removed and replaced with the asymmetric,
branch-by-branch reading.

### ES-02 - BLOCK: Advice-creep (imperative / second-person voice)

File: `clinical-medicine/03-DIAGNOSTIC-TEST-INTERPRETATION.md`

Finding: Diagrams, thresholds, the worked case, and the Decision Cheat Sheet used
prescriptive imperatives and second person ("do not test," "act (treat)," "you demand
near-certainty," "you will treat," "You have a positive result," "Ask…", "Demand…",
"Use…", "at your threshold"). For a non-advice reference this reads as guidance to the
reader and violates the module's third-person contract.

Fix: Recast into abstract **model states** for a hypothetical clinician — "the model
favors no test / testing / action in the vignette," "below the test threshold →
observation/no test," "above the treatment threshold → action." Analytic equations are
retained but framed as the model's decision rule ("favor Rx if …"), never as advice.
The Decision Cheat Sheet is rewritten as "What the model does."

### ES-03 - WARN: Overgeneralizations needed hedging

File: `clinical-medicine/03-DIAGNOSTIC-TEST-INTERPRETATION.md`

Finding: Four universal claims overreached: "the single most common diagnostic error";
low-prevalence testing "means most positives are false"; serial testing is "behind all
screening"; a repeat test "mostly probes analytic noise, not new biology."

Fix: Hedged respectively to "one of the common test-interpretation errors"; "low
prevalence raises the false-positive share but does not by itself guarantee most
positives are false" (depends jointly on prevalence and LR+); "behind many screening
pathways" with an explicit "screening designs vary"; and a repeat can measure "real
temporal change" when the underlying state can change, distinct from re-confirming a
static value.

### ES-04 - NOTE: Transport limits were asserted, not shown

File: `clinical-medicine/03-DIAGNOSTIC-TEST-INTERPRETATION.md`

Finding: The guide stated that test decisions do not transport across settings but did
not demonstrate it.

Fix: Added two contrasting fictional contexts (low-prevalence asymptomatic screening
vs. an enriched symptomatic referral clinic) plus a low-resource overlay, showing the
same marker changing PPV, test-zone placement, and which branch carries the decision —
all as model states, without personalized advice.
