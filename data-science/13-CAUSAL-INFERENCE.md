# Causal Inference
## Beyond Correlation — DAGs, Do-Calculus, and Causal ML

```
THE CAUSAL INFERENCE HIERARCHY (Pearl's Ladder of Causation)

  Level 3: Counterfactual     "What if I had done X instead of Y?"
           Imagining worlds   PNS, attribution, blame, necessity/sufficiency
                              ↑ Requires structural causal model

  Level 2: Intervention       "What happens if I do X?"
           Doing              do-calculus, randomized trials, treatment effect
                              ↑ Observational data + identifiability conditions

  Level 1: Association        "What happens when I observe X?"
           Seeing             Correlation, regression, conditional probability
                              ← All classical statistics lives here
```

---

## 1. The Fundamental Problem of Causal Inference

For unit i, define potential outcomes:
```
  Yᵢ(1) = outcome if unit i receives treatment
  Yᵢ(0) = outcome if unit i receives control

  Observed: Yᵢ = Dᵢ Yᵢ(1) + (1-Dᵢ) Yᵢ(0)  where Dᵢ ∈ {0,1}

  Individual treatment effect: τᵢ = Yᵢ(1) - Yᵢ(0)

  FUNDAMENTAL PROBLEM: we can never observe both Yᵢ(1) and Yᵢ(0)
  for the same unit at the same time.
```

**ATE (Average Treatment Effect)**: `τ = E[Y(1) - Y(0)] = E[Y(1)] - E[Y(0)]`

**ATT (Average Treatment Effect on the Treated)**: `E[Y(1) - Y(0) | D=1]`

**Why correlation ≠ causation**:
```
  E[Y|D=1] - E[Y|D=0] = ATE + Selection bias

  Selection bias: treated and control differ on confounders
  E.g., healthier people choose to exercise → exercise seems more beneficial than it is
```

---

## 2. Directed Acyclic Graphs (DAGs)

A DAG G = (V, E) encodes causal structure:
- Nodes V = variables (observed + latent)
- Directed edges X → Y mean "X is a direct cause of Y"
- Acyclicity: no directed path from X back to X

**Structural Causal Model (SCM)**:
```
  Each variable Xᵢ has an assignment equation:
    Xᵢ = fᵢ(Pa(Xᵢ), Uᵢ)

  Pa(Xᵢ) = parents (direct causes)
  Uᵢ = exogenous noise (independent across variables)

  Joint distribution: p(x) = Π_i p(xᵢ | pa(xᵢ))  ← Markov factorization
```

**Three fundamental graph patterns (d-separation building blocks)**:
```
  Chain:     X → Z → Y     (mediation)
  Fork:      X ← Z → Y     (common cause / confounder)
  Collider:  X → Z ← Y     (common effect)

  d-separation: X ⊥ Y | C if all paths between X and Y are blocked by C

  Chain:    blocked by conditioning on Z  (mediation blocked)
  Fork:     blocked by conditioning on Z  (confounder removed)
  Collider: OPENED by conditioning on Z   (Berkson's paradox — selection bias)
```

**D-separation algorithm**: for sets X, Y, Z:
1. Find all paths (ignoring edge direction) between X and Y
2. A path is blocked by Z if it contains a non-collider in Z, OR a collider not in Z (and no descendant in Z)
3. X ⊥⊥ Y | Z iff all paths blocked

---

## 3. Interventions and the Do-Operator

**Observational**: P(Y | X=x) — what Y looks like in the world among those with X=x. Includes selection effects.

**Interventional**: P(Y | do(X=x)) — what Y looks like if we force X=x for everyone. Cuts all incoming edges to X.

```
  Graphically: do(X=x) removes all arrows into X in the DAG

  Original graph:  Z → X → Y     P(Y|X=x) ≠ P(Y|do(X=x)) if Z also affects Y
  After do(X=x):   Z   X → Y     Z no longer confounds X→Y
```

**Do-calculus** (Pearl 1995): three rules for transforming interventional quantities into observational ones:

```
  Rule 1: Insertion/deletion of observations
    P(y | do(x), z, w) = P(y | do(x), w)   if Y ⊥⊥ Z | X,W in G_{X̄}

  Rule 2: Action/observation exchange
    P(y | do(x), do(z), w) = P(y | do(x), z, w)   if Y ⊥⊥ Z | X,W in G_{X̄, Z_}

  Rule 3: Insertion/deletion of actions
    P(y | do(x), do(z), w) = P(y | do(x), w)   if Y ⊥⊥ Z | X,W in G_{X̄, Z̄(W)}

  Complete: any identifiable causal query is derivable from these 3 rules.
```

---

## 4. Identification Strategies

### Backdoor Criterion
A set Z satisfies the backdoor criterion for (X,Y) if:
1. Z blocks all backdoor paths from X to Y (paths into X)
2. Z contains no descendant of X on the path to Y

```
  If Z satisfies backdoor criterion:
  P(Y | do(X=x)) = Σ_z P(Y | X=x, Z=z) P(Z=z)

  ← Adjustment formula: control for Z to identify causal effect

  Example:
    Confounder Z → X and Z → Y:
    Backdoor: control for Z
    ATE = E_Z[E[Y | X=1, Z]] - E_Z[E[Y | X=0, Z]]
```

### Frontdoor Criterion
When X → Y is confounded by unmeasured U, but there's a measured mediator M:
```
  U → X → M → Y,  U → Y (but U unmeasured)

  Frontdoor adjustment:
  P(Y|do(X=x)) = Σ_m P(M=m|X=x) Σ_{x'} P(Y|X=x', M=m) P(X=x')

  Works because:
    X → M is unconfounded (U doesn't affect M directly)
    M → Y conditional on X is unconfounded
```

---

## 5. Randomized Controlled Trials (RCTs)

**Gold standard**: assign treatment randomly, so:
```
  D ⊥⊥ (Y(0), Y(1))   ← treatment independent of potential outcomes

  → E[Y|D=1] - E[Y|D=0] = E[Y(1) - Y(0)] = ATE
  No confounding possible.
```

**Randomization eliminates selection bias** by making treated/control groups comparable on all measured and unmeasured confounders in expectation.

**ITT vs LATE**:
- Intent-to-Treat (ITT): ATE of assignment (ignore compliance)
- Local Average Treatment Effect (LATE): ATE for compliers only (use IV)

**External validity / generalization**: RCT gives ATE for the trial population. Generalizing to other populations requires assumptions (transportability).

---

## 6. Observational Methods

### Propensity Score Matching (PSM)
```
  Propensity score: e(x) = P(D=1 | X=x)
  Rosenbaum-Rubin: D ⊥⊥ (Y(0),Y(1)) | X  ↔  D ⊥⊥ (Y(0),Y(1)) | e(X)

  Dimensionality reduction: balance on scalar e(X) instead of all X

  Methods:
    1. Match treated units to control units with similar e(X)
    2. Inverse propensity weighting (IPW): weight by 1/e(X) or 1/(1-e(X))
    3. Doubly robust estimation: combine outcome model + propensity model
```

**IPW estimator**:
```
  τ̂_{IPW} = (1/n) Σ [ Dᵢ Yᵢ / ê(Xᵢ)  -  (1-Dᵢ) Yᵢ / (1-ê(Xᵢ)) ]
```

**Doubly robust** (AIPW): consistent if either outcome model or propensity model is correctly specified.

### Difference-in-Differences (DiD)
```
  Parallel trends assumption: E[Y(0)_{t=1} - Y(0)_{t=0} | D=1]
                             = E[Y(0)_{t=1} - Y(0)_{t=0} | D=0]

  Treated group and control group would have had the same time trend absent treatment.

  DiD estimator:
  τ̂ = (Ȳ_{treated,post} - Ȳ_{treated,pre}) - (Ȳ_{control,post} - Ȳ_{control,pre})

  Regression form:
  Yᵢₜ = α + βDᵢ + γPostₜ + τ(Dᵢ × Postₜ) + εᵢₜ
  τ is the DiD coefficient.
```

**Synthetic control**: when only one unit treated, construct a weighted combination of control units that matches the pre-treatment trajectory.

### Instrumental Variables (IV)
```
  Setting: X → Y but X ← U → Y  (unmeasured confounder U)

  Instrument Z: affects X but not Y directly, unrelated to U

  Validity assumptions:
    Relevance: Cov(Z, X) ≠ 0  (Z predicts treatment)
    Exclusion restriction: Z → Y only through X (Z has no direct effect on Y)
    Independence: Z ⊥⊥ U  (Z is exogenous)

  2SLS (Two Stage Least Squares):
    Stage 1: X̂ = α + βZ + ... (project X onto Z)
    Stage 2: Y = γ X̂ + δ + ...

  IV estimate: τ_IV = Cov(Y,Z) / Cov(X,Z)  ← ratio of reduced forms
```

**LATE interpretation**: IV identifies treatment effect for compliers (those whose treatment status is changed by Z), not all units.

### Regression Discontinuity (RD)
```
  Assignment: D = 1{score ≥ cutoff c}
  Near the cutoff: treated ≈ control (local RCT)

  Sharp RD estimator:
  τ̂ = lim_{x↓c} E[Y|X=x] - lim_{x↑c} E[Y|X=x]

  Local polynomial regression near the cutoff.
  Bandwidth selection is critical.
```

---

## 7. Causal ML

### Double Machine Learning (DML) — Chernozhukov et al. 2018
```
  Semi-parametric setup: Y = τD + g(X) + ε,  D = m(X) + v

  Naive ML: fit Y~D+X directly → regularization biases τ̂

  DML (Orthogonalization):
    1. Fit Ỹ = Y - Ê[Y|X] (residualize outcome on controls)
    2. Fit D̃ = D - Ê[D|X] (residualize treatment on controls)
    3. τ̂ = Cov(Ỹ, D̃) / Var(D̃)

    → √n-consistent and asymptotically normal under mild ML assumptions
    → Any ML method can be used in steps 1-2 (neural net, forest, etc.)
    → Cross-fitting required (train on one half, predict on other) to avoid overfitting bias
```

### Causal Forests (Wager & Athey 2018)
```
  Goal: estimate heterogeneous treatment effects τ(x) = E[Y(1)-Y(0)|X=x]

  Causal forest: random forest variant where splits maximize variance of τ̂(x)

  Local CATE: for test point x₀, weight training obs by proximity:
  τ̂(x₀) = Σᵢ αᵢ(x₀) Ỹᵢ / Σᵢ αᵢ(x₀) D̃ᵢ

  Properties:
    Asymptotically normal → confidence intervals
    Honest (uses sample splitting for inference)
    Variable importance: which X explain heterogeneity
```

### Counterfactual Evaluation (Off-Policy Evaluation)
```
  RL/bandit setting: evaluate policy π without deploying it
  Using historical data collected under π₀

  IPS (Inverse Propensity Scoring):
  V̂(π) = (1/n) Σᵢ (π(aᵢ|xᵢ) / π₀(aᵢ|xᵢ)) rᵢ

  Doubly robust OPE: combine direct method + IPS
```

---

## 8. Identifiability — What Can Be Identified?

Not all causal queries are identifiable from observational data, even with a known graph.

```
  Identifiable: P(Y|do(X)) can be computed from P(V) = observational distribution

  Non-identifiable: hidden confounders that can't be blocked

  Example (non-identifiable):
    U → X, U → Y, X → Y  (U unmeasured)
    Cannot identify X→Y effect from observational data alone.
    Need an instrument or RCT.

  Completeness of do-calculus: an effect is identifiable iff derivable via do-calculus.
  ID algorithm (Shpitser & Pearl): systematic procedure for identifiability.
```

---

## 9. Decision Cheat Sheet

| Method | When applicable | Identifies |
|--------|----------------|-----------|
| RCT | Can randomize | ATE (population) |
| Backdoor adjustment | Observed confounders sufficient | ATE via adjustment |
| Frontdoor | Measured mediator, unmeasured confounder | ATE via mediation |
| IV (2SLS) | Valid instrument exists | LATE (compliers) |
| DiD | Parallel trends plausible, panel data | ATT (post-pre) |
| RD | Assignment by threshold | LATE near cutoff |
| PSM / IPW | Conditional independence plausible | ATE / ATT |
| DML | Semi-parametric, ML nuisance | ATE (efficient) |
| Causal forest | Heterogeneous effects wanted | CATE(x) |

---

## 10. Common Confusion Points

1. **"Controlling for more variables is always better"** — Controlling for a collider (or its descendant) opens a spurious path and introduces bias. You can make things worse by controlling for the wrong variables.

2. **"No unmeasured confounders = ignorability"** — The ignorability assumption D ⊥ (Y(0),Y(1)) | X requires no unmeasured variables that affect both treatment and outcome. This is untestable from observational data.

3. **"A significant IV F-statistic means the instrument is valid"** — F > 10 indicates relevance (Z predicts D). It says nothing about the exclusion restriction (Z doesn't affect Y directly). Validity is untestable and requires subject-matter knowledge.

4. **"DiD requires the groups to have the same pre-treatment levels"** — Parallel trends requires the same *trend*, not level. Groups can have different baseline outcomes as long as they would have evolved in parallel absent treatment.

5. **"Causal inference only works for binary treatments"** — These methods extend to continuous (dose-response), multi-valued, and dynamic treatments. The math is messier but the principles hold.

6. **"Machine learning can solve causal inference with enough data"** — No. More data doesn't resolve confounding. You can estimate correlations precisely with infinite data, but without causal assumptions (RCT or structure), you can't identify causal effects.

7. **"Mediation analysis gives you direct and indirect effects"** — Only under sequential ignorability assumptions. If the mediator is also confounded, natural direct/indirect effects are not identified from data alone.
