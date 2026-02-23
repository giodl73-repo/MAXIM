# Experimental Design — RCTs, Power Analysis, Factorial, Blocking

## The Big Picture

```
+------------------------------------------------------------------+
|              EXPERIMENTAL DESIGN DECISION TREE                  |
|                                                                  |
|  ONE FACTOR, TWO LEVELS → two-sample t-test; power formula       |
|  ONE FACTOR, 3+ LEVELS → one-way ANOVA; post-hoc comparison     |
|  MULTIPLE FACTORS → factorial design (full or fractional)        |
|  NUISANCE FACTORS KNOWN → block them (RCBD, Latin square)        |
|  SUBJECT IS OWN CONTROL → within-subjects / crossover            |
|  WANT TO OPTIMIZE → response surface methodology (RSM)           |
|  INTERIM LOOKS NEEDED → group sequential / adaptive design       |
|                                                                  |
|  BEFORE ANY DESIGN: specify the estimand + primary endpoint      |
|  BEFORE DATA COLLECTION: power analysis + pre-registration       |
|  DURING: randomization + blinding + protocol adherence           |
|  AFTER: intention-to-treat analysis + pre-specified secondary    |
+------------------------------------------------------------------+
```

---

## Why Randomization Enables Causal Inference

```
THE FUNDAMENTAL PROBLEM OF CAUSAL INFERENCE:
  For unit i, we observe EITHER Y_i(1) [under treatment] OR Y_i(0) [under control]
  NEVER both simultaneously
  → Individual causal effect Y_i(1) - Y_i(0) is fundamentally unobservable
  → Average treatment effect (ATE) = E[Y(1) - Y(0)] requires assumptions

WHAT RANDOMIZATION DOES:
  Random assignment: T_i ⊥⊥ (Y_i(0), Y_i(1))
  Treatment assignment is INDEPENDENT of potential outcomes

  IMPLICATION:
  E[Y | T=1] - E[Y | T=0]
  = E[Y(1) | T=1] - E[Y(0) | T=0]    (by definition of observed outcomes)
  = E[Y(1)] - E[Y(0)]                  (by independence T ⊥⊥ Y(0), Y(1))
  = ATE                                 (average treatment effect)

  → Observed difference in means = causal average treatment effect
  → Valid because randomization balances ALL confounders (observed AND unobserved)
    in expectation

WITHOUT RANDOMIZATION:
  E[Y|T=1] - E[Y|T=0] = ATE + SELECTION BIAS
  Selection bias = E[Y(0)|T=1] - E[Y(0)|T=0]
  (Difference in untreated potential outcomes between treatment groups)
  → If healthier patients choose treatment: selection bias inflates treatment effect
  → Observational methods try to eliminate selection bias; never guaranteed

STABLE UNIT TREATMENT VALUE ASSUMPTION (SUTVA):
  1. No interference between units: treatment of unit i doesn't affect unit j
  2. No hidden variations of treatment: one version of "treated"
  → Violated in: social networks (interference), marketplace (two-sided),
    geographic rollouts (spillover), epidemics (herd immunity)
  → Network experiments, switchback designs, cluster randomization address this
```

---

## Power Analysis

```
THE FOUR QUANTITIES (fix any three → determines the fourth):

α = Type I error rate (false positive probability)
  → P(reject H₀ | H₀ is true)
  → Convention: α = 0.05 (two-sided); justify any deviation
  → One-sided tests: use only with strong directional prior + pre-specified

β = Type II error rate (false negative probability)
  → P(fail to reject H₀ | H₀ is false with effect δ)
  → 1 - β = power; convention: 80% or 90%
  → 80% power = 20% chance of missing a real effect of size δ

δ = MDE (Minimum Detectable Effect)
  → The smallest effect size worth detecting
  → NOT "the effect we expect" — smaller than true effect = underpowered
  → NOT "the effect that would be statistically significant"
  → The business/scientific minimum worth acting on

n = sample size per group (for two-group comparison)

SAMPLE SIZE FORMULA (two-sample t-test, two-sided):
  n = (z_{α/2} + z_β)² × 2σ² / δ²

  z_{α/2}: critical value for significance level (α=0.05: z = 1.96)
  z_β: critical value for power (80%: z = 0.84; 90%: z = 1.28)
  σ²: outcome variance (estimate from pilot/historical data)
  δ: MDE

  Numerically:
  α=0.05, 80% power: n = (1.96 + 0.84)² × 2σ² / δ² = 15.7 × σ²/δ²
  α=0.05, 90% power: n = (1.96 + 1.28)² × 2σ² / δ² = 21.0 × σ²/δ²

STANDARDIZED FORM (using Cohen's d = δ/σ):
  n ≈ 2 × (z_{α/2} + z_β)² / d²
  d = 0.2 (small): n ≈ 394 per group (at 80% power, α=0.05)
  d = 0.5 (medium): n ≈ 64 per group
  d = 0.8 (large): n ≈ 26 per group

EFFECT SIZE CONVENTIONS (Cohen, 1988):
  d = |μ₁ - μ₂| / σ_pooled
  +-------+--------+-------------------------------------------+
  | d     | Label  | Example                                   |
  +-------+--------+-------------------------------------------+
  | 0.2   | Small  | 1 IQ point diff, 2cm height diff          |
  | 0.5   | Medium | Visible in interview                      |
  | 0.8   | Large  | Obvious in everyday observation           |
  +-------+--------+-------------------------------------------+
  Most "real" effects in A/B testing: 0.1-0.3 standardized
  → Most online experiments need hundreds of thousands of users

OTHER MEASURES:
  Relative risk / odds ratio: use for binary outcomes
  NNT (Number Needed to Treat): 1/ARR; clinically interpretable
  Eta-squared (η²): variance explained in ANOVA
  Partial η²: variance of factor / (variance of factor + error variance)

TOOLS:
  R: pwr package (pwr.t.test, pwr.2p.test, pwr.anova.test)
  G*Power: free GUI application; comprehensive
  Python: statsmodels.stats.power
  Effect size calculator: embedded in most platforms (Amplitude, Optimizely)
```

---

## Randomization Types

```
SIMPLE RANDOMIZATION:
  Each unit: P(T=1) = 0.5 independently
  Problem: by chance, imbalance in small samples
  (20 people: might get 14 treatment / 6 control by chance)

BLOCK RANDOMIZATION:
  Fix block size (e.g., 4 or 6)
  Within each block: exact balance (half treatment, half control)
  Ensures balance at each interim point; protects against temporal trends
  Trades some flexibility for guaranteed allocation balance

STRATIFIED RANDOMIZATION:
  Within each stratum (e.g., age groups, disease severity):
  apply separate randomization
  Guarantees stratum balance; enables subgroup analysis with power
  Requires stratification variables known at enrollment

CLUSTER RANDOMIZATION:
  Unit = group (hospital, school, village), not individual
  Required when: intervention is group-level (can't randomize within group)
    OR contamination risk if individuals within group could interact
  Cost: lose power (within-cluster correlation reduces effective N)
    Design effect = 1 + (m-1)ρ  (m = cluster size, ρ = ICC)
    → ICC=0.05, m=50: design effect = 3.45 → need 3.45× more total units
  Analysis: must account for clustering (GEE, mixed models, cluster-robust SE)

ADAPTIVE RANDOMIZATION:
  Assignment probability changes based on accumulating data
  Response-adaptive: assign more to better-performing arm (ethical appeal)
  Risk: introduces selection bias (later patients differ from earlier)
  Biostatistical consensus: use sparingly; frequentist calibration complex
```

---

## CONSORT Framework and Intent-to-Treat

```
CONSORT (Consolidated Standards of Reporting Trials):
  25-item checklist + flow diagram for RCT reporting
  Required by major medical journals
  Core: eligibility, randomization, allocation concealment, blinding,
    follow-up, primary analysis, adverse events

ALLOCATION CONCEALMENT vs BLINDING:
  Allocation concealment: investigators cannot predict future assignments
    → Prevents systematic selection before enrollment
    → ESSENTIAL even when blinding is impossible
    → Implemented by: central randomization, sequentially-numbered sealed envelopes

  Blinding: participants/assessors don't know treatment assignment
    → Prevents post-randomization measurement bias
    → Double blind: participant + assessor blinded
    → Triple blind: + statistician blinded (before analysis)
    → Not always feasible (surgery vs sham surgery); use as much as possible

INTENTION-TO-TREAT (ITT) ANALYSIS:
  Analyze all randomized participants in their assigned group
  REGARDLESS of whether they received assigned treatment, complied, or dropped out
  → Preserves the causal benefits of randomization (preserves balance)
  → Estimates the "treatment policy effect" (effect of assignment, not receipt)

  MODIFIED ITT (mITT): exclude specific pre-specified patients
    (e.g., received no study treatment at all; enrolled before protocol amendment)
    Must be pre-specified; not "clean up failures"

  PER-PROTOCOL (PP): analyze only protocol-compliant patients
  → BIASED: selects on post-randomization behavior (compliance is endogenous)
  → Use as sensitivity analysis only; never primary

  AS-TREATED (AT): analyze by treatment actually received
  → Estimates LATE (local average treatment effect for compliers) via IV
  → For biologic plausibility only; not primary unless IV used

NON-COMPLIANCE:
  Two-stage analysis: instrument = randomization assignment
  Exclusion restriction: assignment affects outcome ONLY through treatment receipt
  LATE / CACE (Complier Average Causal Effect):
    Effect among units who comply with assignment
    Bounded above/below using Manski bounds (without IV assumptions)
```

---

## Factorial Designs

```
2ᵏ FULL FACTORIAL:
  k factors, each at 2 levels (−1, +1; or low/high)
  All 2ᵏ combinations tested
  Estimates: k main effects + k(k-1)/2 two-way interactions + higher-order

  2² (two factors): 4 runs
  A B | Y
  - - | y₁
  + - | y₂
  - + | y₃
  + + | y₄
  Main effect A = [(y₂+y₄) - (y₁+y₃)]/2
  Interaction AB = [(y₁+y₄) - (y₂+y₃)]/2

  2³: 8 runs → 3 mains + 3 two-ways + 1 three-way
  2⁴: 16 runs; 2⁵: 32 runs → quickly expensive

2ᵏ⁻ᵖ FRACTIONAL FACTORIAL:
  Run only 2ᵏ⁻ᵖ of the 2ᵏ required runs
  Save cost; lose ability to distinguish some effects (aliasing)

  RESOLUTION:
  III: main effects aliased with 2-way interactions (bad; fine for screening only)
  IV: main effects clear; 2-ways aliased with other 2-ways (better)
  V: main effects and 2-ways both estimable (best)

  EXAMPLE: 2⁶⁻² resolution IV design: 16 runs to study 6 factors
  → Can estimate all main effects + selected interactions
  → Much cheaper than full factorial (64 runs)

PLACKETT-BURMAN DESIGNS:
  Screening: N runs for N-1 factors (where N is multiple of 4)
  12-run PB: screen 11 factors; 20-run: screen 19 factors
  Resolution III: all main effects estimable, but heavily confounded with 2-ways
  Use when: early screening, dozens of factors, interactions less important

RESPONSE SURFACE METHODOLOGY (RSM):
  GOAL: find optimal settings of continuous factors
  Step 1: Screening (2ᵏ⁻ᵖ or PB) to identify important factors
  Step 2: Steepest ascent to move toward optimum region
  Step 3: Central composite or Box-Behnken design for quadratic model
  Step 4: Fit response surface; find maximum/minimum

  Central Composite Design (CCD): 2ᵏ factorial + star points + center
  Box-Behnken: 3-level design without corners (avoids extreme combos)
  Used in: drug formulation, process engineering, chemical optimization
```

---

## Blocking

```
WHY BLOCK:
  Nuisance factors cause variation you can't eliminate but CAN control
  Block on the nuisance → remove its variance from error
  → Smaller error variance → more power for treatment effects

RANDOMIZED COMPLETE BLOCK DESIGN (RCBD):
  k treatments, b blocks
  Within each block: all k treatments applied in random order
  Block × Treatment: no interaction assumed
  Analysis: remove block sum of squares from error

  Example: test 4 drug doses across 5 days (day = block)
  Within each day: all 4 doses given in random order
  → Day-to-day variation removed from treatment comparison
  → Requires: block × treatment interaction absent
    (interaction = treatment effect different in different blocks)
    → If interaction present: must include in model or results misleading

LATIN SQUARE:
  Two blocking factors (rows and columns)
  Each treatment appears exactly once in each row AND each column
  → Controls two nuisance factors simultaneously
  Example: 4×4 Latin square — rows = operators, columns = machines
  Constraint: n = k (square design) → only one error DF per obs; very restrictive
  More useful: replicated Latin squares

SPLIT-PLOT DESIGN:
  Some factors are "hard to change" (whole-plot factors): change between plots
  Others are "easy to change" (sub-plot factors): change within plots
  Result: two error terms (between-plot error for whole-plot, within-plot for sub-plot)
  CRITICAL: using wrong error term for whole-plot factor is INCORRECT
  Common mistake: analyze split-plot as if CRD → inflated significance for hard-to-change factor

  Example: temperature (hard to change in oven) × time + recipe (easy to change)
  → Temperature is whole-plot factor; recipe is sub-plot
  → Temperature effect tested against between-oven variation; recipe against within-oven
```

---

## Within-Subjects and Crossover Designs

```
WITHIN-SUBJECTS / REPEATED MEASURES:
  Same subject receives multiple treatments (sequentially or all)
  Subject serves as own control
  → Within-subject variance MUCH lower than between-subject variance
  → Gain power by eliminating between-subject heterogeneity from error

  EFFICIENCY:
  Between-subject design: error = σ²_within + σ²_between
  Within-subject design: error = σ²_within
  If ICC (within-subject correlation) = ρ:
  Efficiency gain = 1/(1-ρ)
  ρ = 0.7 → within-subjects is 3.3× more efficient

CROSSOVER DESIGN:
  Each subject receives ALL treatments in random sequence
  Common: 2×2 crossover (AB|BA) — two treatments, two periods
  Washout period between treatments to eliminate carryover
  Period effects: remove period effect in analysis
  Sequence effects: test for sequence × treatment interaction

  ASSUMPTIONS:
  1. Carryover effect = 0 (washout is sufficient)
  2. No treatment × period interaction
  3. No permanent treatment effects (e.g., surgery: never use crossover)

  2×2 CROSSOVER MODEL:
  Y_ijk = μ + T_j + P_k + S_i + ε_ijk
  T_j = treatment effect (what we want)
  P_k = period effect (first vs second)
  S_i = subject random effect (eliminated in within-subject comparison)
  ε_ijk = within-subject residual

CARRYOVER:
  Biological washout: ≥5 half-lives of drug
  Psychological: learning/fatigue may not wash out
  Disease-modifying treatments: carryover cannot be eliminated (use parallel)
```

---

## Adaptive and Sequential Designs

```
GROUP SEQUENTIAL DESIGN:
  Plan K equally-spaced interim looks during trial
  At each look: test against spending function boundary
  If significance achieved: stop and declare success (early stopping)
  If futility boundary crossed: stop for futility (early stopping)
  Final α is preserved overall via spending function

  SPENDING FUNCTIONS:
  O'Brien-Fleming: conservative early, liberal late
    → Requires very strong early evidence to stop; saves for late
    → Widely used in clinical trials
  Pocock: equal boundaries at each look
    → Easier to understand; reduces power for final analysis
  Lan-DeMets: generalizes both via alpha-spending function α*(t)
    → Allows unplanned interim analyses
    → α spent at each fraction t of total information

  BETA SPENDING (futility):
  Stop if treatment effect is clearly too small to achieve power
  Conditional power monitoring: P(significant at end | current data) < 20% → stop

  SAMPLE SIZE RE-ESTIMATION:
  Adaptive: observe nuisance parameter (σ²) at interim → adjust planned n
  Blinded SSR: re-estimate σ² from pooled data (no unblinding) → preserve type I error
  Unblinded SSR: see treatment difference → more complex alpha adjustment required

ALPHA-SPENDING FOR ONLINE A/B TESTS:
  Sequential tests / always-valid inference:
  Classical: can't peek at p-value and stop early → type I error inflation
  mSPRT (mixture sequential probability ratio test): p-value valid at ANY stopping time
  Anytime-valid confidence sequences: CS grows with n; valid whenever you check
  Implementation: Johari et al. (2017), Spotify/LinkedIn/Microsoft use in production
  → Allows continuous monitoring + stops when confident enough
  → No alpha spending across looks; mathematically different framework
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What sample size for d=0.3, α=0.05, 80% power? | n ≈ 2 × (1.96+0.84)² / 0.3² ≈ 175 per group. Or use pwr.t.test(d=0.3, sig=0.05, power=0.80) |
| What is allocation concealment? | Preventing investigators from knowing future assignments before enrollment. Distinct from blinding (post-randomization). Essential for all trials, even unblinded ones. |
| What is ITT analysis and why? | Analyze all randomized units in assigned group regardless of compliance. Preserves causal validity of randomization. Per-protocol analysis introduces selection bias. |
| What is the design effect in cluster RCT? | 1 + (cluster_size - 1) × ICC. ICC=0.05, m=50 → design effect ≈ 3.45 → need 3.45× more total observations. |
| What is a resolution V factorial design? | 2ᵏ⁻ᵖ fractional factorial where all main effects AND all two-factor interactions are estimable without aliasing with each other. |
| When is crossover design inappropriate? | When treatment effect is permanent (surgery, gene therapy), when adequate washout is not possible, or when sequence effects are likely confounded with treatment. |
| What is α-spending? | Mechanism to allocate type I error budget across multiple interim looks. O'Brien-Fleming spending: conservative early (saves α for late looks). Total α preserved at planned level. |

---

## Common Confusion Points

**Power analysis uses MDE, not expected effect:** Power analysis should specify the MINIMUM effect worth detecting (business/scientific threshold), not the expected or likely effect. Using the expected effect produces underpowered studies — most effects are smaller than expected.

**Block randomization ≠ blocking in ANOVA:** Block randomization is the allocation procedure (ensuring balance within blocks of recruits). Blocking in ANOVA is an analysis strategy (removing block effects from error). Related concepts, but at different stages of the study.

**SUTVA is often violated online:** The assumption "my treatment doesn't affect you" breaks in: social platforms (your feed content affects mine through social interaction), two-sided marketplaces (more buyers → changes seller behavior → affects control buyers), recommendation systems (model updates affect all). Cluster randomization or holdout design needed.

**p<0.05 at interim = inflate type I error:** If you test at any time p<0.05 crosses threshold, your actual α is much higher than 0.05. Sequential testing methods (O'Brien-Fleming, mSPRT, anytime-valid sequences) are the correct solution. "We stopped early because we saw significance" with no pre-specified plan is invalid.
