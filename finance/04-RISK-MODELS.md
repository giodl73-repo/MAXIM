# Risk Models — VaR, CVaR, Stress Testing & Systemic Risk

## The Big Picture

```
+------------------------------------------------------------------+
|                      FINANCIAL RISK LANDSCAPE                     |
+------------------------------------------------------------------+
|                                                                    |
|  RISK TYPES                  MEASUREMENT               MANAGEMENT |
|  ──────────                  ───────────               ────────── |
|  Market risk                 Value at Risk (VaR)       Hedging    |
|  Credit risk                 Expected Shortfall (CVaR) Limits     |
|  Liquidity risk              Stress testing            Diversif.  |
|  Operational risk            Scenario analysis         Collateral |
|  Systemic risk               Greeks (options)          Capital    |
|                              Copula models             req.       |
|                                                                    |
|  REGULATORY FRAMEWORKS                                             |
|  ────────────────────────────────────────────────────────────    |
|  Basel III/IV: banking capital requirements                       |
|  FRTB: Fundamental Review of Trading Book (2025 implementation)   |
|  Solvency II: insurance capital requirements (EU)                 |
+------------------------------------------------------------------+
```

Risk management = quantifying uncertainty in financial outcomes and
ensuring sufficient capital to survive adverse scenarios. The 2008
financial crisis exposed massive failures in every layer of this framework.

---

## Value at Risk (VaR)

The most widely used single risk metric (and widely criticized):

```
DEFINITION:
  VaR_{α}(X) = minimum loss such that P(loss > VaR) = 1 − α

  Equivalently: the α-quantile of the loss distribution.
  "We are α% confident our loss will not exceed VaR over horizon T."

  Common: α = 99%, T = 1 day (trading book)
          α = 99.9%, T = 10 days (regulatory capital, Basel II)

EXAMPLE:
  Daily VaR₉₉% = $10M means:
  On any given day, there is 1% probability of losing more than $10M.
  Equivalently: losses exceed $10M roughly 2-3 times per year.
```

### Parametric VaR (Variance-Covariance Method)

```
Assume P&L ~ N(μ, σ²):
  VaR_{α} = μ − σ · z_{1-α}   (z_{0.99} = 2.326, z_{0.95} = 1.645)
  Often μ ≈ 0 for daily, so: VaR ≈ σ · z_{α}

PORTFOLIO VaR (Δ-Normal):
  Portfolio positions: w ∈ ℝⁿ, asset P&L covariance: Σ
  Portfolio variance: σ_p² = wᵀΣw
  VaR = z_{α} · σ_p = z_{α} · √(wᵀΣw)

COMPONENT VaR:
  CVaRᵢ = ρᵢ · VaRᵢ   where ρᵢ = correlation of asset i with portfolio
  Component VaR sums to total VaR: Σᵢ CVaRᵢ = VaR_portfolio

MARGINAL VaR:
  ∂VaR/∂wᵢ = z_{α} · (Σw)ᵢ / σ_p
  Position contribution to portfolio risk.
```

### Historical Simulation VaR

```
PROCEDURE:
  1. Collect N days of historical returns (e.g., N = 250 or 500)
  2. Apply today's portfolio weights to each historical day
  3. Generate N hypothetical P&L scenarios
  4. VaR = (1−α) percentile of the distribution

ADVANTAGES:
  Nonparametric — no Gaussian assumption
  Captures fat tails from historical data
  Easy to explain to regulators

DISADVANTAGES:
  Only captures risks in the historical window
  Equal weight to all history (recency bias)
  Can't model crises we haven't seen (Knightian uncertainty)

IMPROVEMENTS:
  Age-weighted (exponential decay of older scenarios)
  Filtered historical simulation: standardize by current volatility (GARCH)
```

### Monte Carlo VaR

```
PROCEDURE:
  1. Specify risk factor model (GBM, jump-diffusion, copula)
  2. Simulate K scenarios (K = 10,000–1,000,000)
  3. For each scenario: price all instruments
  4. VaR = (1−α) percentile of simulated P&L

ADVANTAGES:
  Handles complex nonlinear instruments (options, MBS)
  Can incorporate full term structure dynamics
  Flexible risk factor models

DISADVANTAGES:
  Computationally expensive (full repricing each scenario)
  Model risk: results depend heavily on assumptions
  Greeks-based approximation sometimes used to speed up
```

---

## Limitations of VaR

```
WHAT VaR DOES NOT TELL YOU:
  1. Nothing about the SEVERITY of losses beyond VaR
     (tail of the distribution is ignored)
  2. Not subadditive in general:
     VaR(A+B) ≤ VaR(A) + VaR(B) is FALSE for non-Gaussian
     → VaR can encourage concentration, penalize diversification!
  3. Smooth P&L history → low VaR, but hidden tail risk

SUBADDITIVITY FAILURE EXAMPLE:
  Bond A: 0 with prob 98%, −100 with prob 2%
  Bond B: same distribution, independent of A
  VaR₉₉(A) = 0,  VaR₉₉(B) = 0
  VaR₉₉(A+B) = 100  (portfolio of "safe" bonds has VaR > each individually!)

This led to regulatory shift from VaR to Expected Shortfall.
```

---

## Expected Shortfall (CVaR / ES)

Fixes VaR's tail-blindness:

```
DEFINITION:
  ES_α = E[Loss | Loss > VaR_α]   (expected loss given we're in the tail)
        = (1/(1-α)) ∫_{VaR_α}^∞ x f(x) dx   (integral of tail distribution)

  ES₉₇.₅% ≈ VaR₉₉%  (rough equivalence often used in regulatory comparisons)

PROPERTIES:
  Coherent risk measure (Artzner et al. 1999):
    ✓ Subadditive: ES(A+B) ≤ ES(A) + ES(B)
    ✓ Monotone: if A ≥ B always, then ES(A) ≥ ES(B)
    ✓ Positive homogeneous: ES(λA) = λES(A)
    ✓ Translation invariant: ES(A+c) = ES(A) + c

  VaR fails subadditivity → not coherent.
  ES is coherent → preferred by regulators and academics.

BASEL FRTB (2025):
  Replaces VaR₉₉% with ES₉₇.₅% for regulatory capital
  Reason: ES captures tail severity; more stable under volatility clustering
  10-day ES = sqrt(10) × 1-day ES  (for normal distribution only)

ESTIMATION:
  Parametric: ES_α = μ + σ · φ(z_α)/(1-α)   where φ = standard normal PDF
  Historical: average of worst (1-α)·N losses in sample
  Monte Carlo: average of worst (1-α)·K simulated losses
```

---

## Extreme Value Theory

For modeling deep tail risk beyond historical data:

```
GENERALIZED EXTREME VALUE DISTRIBUTION (GEV):
  Block maxima theorem (Fisher-Tippett-Gnedenko):
  Maxima of i.i.d. variables converge (after scaling) to GEV:
  F(x; μ,σ,ξ) = exp(−(1 + ξ(x-μ)/σ)^{-1/ξ})

  ξ = shape parameter:
    ξ > 0: Fréchet — heavy tail (power law): financial returns, insurance
    ξ = 0: Gumbel — light exponential tail: normal, log-normal
    ξ < 0: Weibull — bounded tail: unusual in finance

GENERALIZED PARETO DISTRIBUTION (GPD):
  Peaks over threshold (POT) method — preferred for VaR/ES:
  P(X > u + y | X > u) → GPD as threshold u → ∞

  Fit GPD to tail observations beyond threshold u:
  F_tail(x) ≈ 1 − (Nu/N)(1 + ξ(x-u)/σ)^{-1/ξ}  for x > u

  Then:
  VaR_α = u + (σ/ξ)[(N/Nu (1-α))^{-ξ} − 1]
  ES_α = VaR_α / (1-ξ) + (σ-ξu)/(1-ξ)

  Tail index ξ ≈ 0.3 for equity returns (power law tail exponent α_tail ≈ 3)
```

---

## Copula Models

Separate marginal distributions from dependence structure:

```
SKLAR'S THEOREM:
  Any joint distribution F(x₁,...,xₙ) = C(F₁(x₁),...,Fₙ(xₙ))
  C = copula (joint distribution on uniform margins)
  Marginals Fᵢ and copula C can be chosen independently.

COMMON COPULAS:

  Gaussian copula: C = Φₙ(Φ⁻¹(u₁),...,Φ⁻¹(uₙ); ρ)
    Correlation matrix ρ captures dependence.
    Zero tail dependence — underestimates joint extremes!
    Infamous: used for CDO pricing (Li 2000); blamed for 2008 crisis.

  t-copula: uses multivariate t distribution with ν degrees of freedom
    Tail dependence coefficient: λ = 2t_{ν+1}(-√((ν+1)(1-ρ)/(1+ρ)))
    λ > 0 for any ν < ∞ — correctly captures joint tail risk.
    Preferred for credit portfolios.

  Clayton copula: C(u,v) = (u^{-θ} + v^{-θ} − 1)^{-1/θ}
    Lower tail dependence: λ_L = 2^{-1/θ} > 0
    Left-tail dependent — captures joint crashes.
    No upper tail dependence.

  Gumbel copula: upper tail dependent — captures joint booms.
  Frank copula: symmetric, no tail dependence — intermediate.

COPULA MODEL BUILDING:
  1. Estimate marginal distributions (empirical or parametric) for each asset
  2. Map each observation to uniform via probability integral transform uᵢ = Fᵢ(xᵢ)
  3. Fit copula to uniform margins {uᵢ} using MLE or rank-correlation matching
  4. Simulate from joint model: simulate copula → inverse transform marginals
```

---

## Stress Testing and Scenario Analysis

```
HISTORICAL SCENARIOS:
  Apply historical stress periods to current portfolio:

  Event                  S&P 500  IG Spread  Vol (VIX)
  ────────────────────   ───────  ─────────  ─────────
  Black Monday 1987      -22.6%   +50 bps    spike to 100
  LTCM 1998              -20%     +200 bps   spike to 45
  Dot-com bust 2000-02   -50%     +150 bps   30-40
  9/11 2001              -14%     +50 bps    spike to 43
  GFC 2008               -57%     +600 bps   spike to 80
  COVID crash 2020       -34%     +300 bps   spike to 66

HYPOTHETICAL SCENARIOS:
  "What if rates rise 200bp instantaneously?"
  "What if credit spreads widen 300bp while equities fall 30%?"
  "What if USD/EUR drops 20% overnight?"

  Key: correlation structure during stress ≠ normal times.
  "Correlation goes to 1 in a crisis" — diversification fails when needed most.

REVERSE STRESS TESTING:
  Work backward: what scenario causes a specific loss (e.g., insolvency)?
  Useful for identifying hidden vulnerabilities.
  Required by regulators for systemically important institutions.

BASEL STRESS TESTING (CCAR/DFAST in US):
  Fed publishes hypothetical adverse scenario annually.
  Banks must demonstrate sufficient capital to absorb losses.
  "Severely adverse scenario" typically -50% equities, +5% unemployment, deep recession.
```

---

## Systemic Risk

Risk of financial system failure — not just individual firm failure:

```
SOURCES:
  Fire sales: forced selling by stressed institutions → prices fall → more stress
  Contagion: counterparty failures cascade (AIG → multiple banks in 2008)
  Bank runs: self-fulfilling panic (Bagehot: lend freely at penalty rate)
  Pro-cyclicality: regulations that amplify cycles (mark-to-market + VaR limits)
  Too-big-to-fail: implicit government guarantee → excessive risk-taking

MEASUREMENT:

  SRISK (Brownlees-Engle): Capital shortage in crisis scenario
    SRISK = E[Capital Deficit | crisis]
          = E[max(0, d·Debt − (1-d)·Equity·(1+crisis_return))]
    Aggregated across all banks: systemic risk index

  ΔCoVaR (Adrian-Brunnermeier): Marginal contribution to system VaR
    CoVaR_{system|i} = VaR(system | institution i at its VaR)
    ΔCoVaR = CoVaR_{system|stress_i} − CoVaR_{system|normal_i}

  CoVaR estimated by quantile regression: easy + interpretable

  MES (Marginal Expected Shortfall): Expected equity loss in market crash
    MES_i = E[rᵢ | r_m < VaR_{m,α}]
    Used in systemic risk rankings (V-Lab at NYU Stern)

NETWORK MODELS:
  Banks linked by interbank loans, derivatives exposures, common asset holdings.
  Contagion modeled as cascading defaults on exposure network.
  Eisenberg-Noe model: clearing vector in multilateral netting.
  DebtRank: weighted network measure of financial distress propagation.
```

---

## Portfolio-Level Risk Framework

```
RISK FACTOR DECOMPOSITION:

  Portfolio P&L = Σᵢ wᵢ rᵢ,  rᵢ = exposure i return
  Factor model: rᵢ = Σₖ βᵢₖ Fₖ + εᵢ

  Risk decomposition:
    Systematic risk: exposure to factors Fₖ
    Idiosyncratic risk: εᵢ (firm-specific, diversifies away)

RISK ATTRIBUTION:
  Total portfolio variance: σ_p² = wᵀΣw
  Contribution of asset i: CTVᵢ = wᵢ (Σw)ᵢ / σ_p²  → Σ CTVᵢ = 1
  Marginal contribution: MCVᵢ = (Σw)ᵢ / σ_p

  Risk-parity: equal risk contribution from each asset
    wᵢ MCVᵢ = σ_p / n  for all i
    Solve numerically; results in low-vol assets getting higher weights.

GREEK AGGREGATION:
  Delta-neutral book: Σ Δᵢ = 0  (total delta)
  Gamma risk: Σ Γᵢ · σᵢ² (non-linear risk)
  Vega risk: sensitivity to vol changes
  Rho: interest rate sensitivity
  All tracked at portfolio level, hedged to limits.
```

---

## Regulatory Capital Frameworks

```
BASEL III KEY REQUIREMENTS (simplified):
  CET1 ratio = CET1 capital / RWA ≥ 4.5%  (+ 2.5% buffer = 7% effective)
  Tier 1 ratio = Tier 1 capital / RWA ≥ 6%
  Total capital ratio = Total capital / RWA ≥ 8%
  Leverage ratio = Tier 1 / total exposure ≥ 3%
  Liquidity: LCR ≥ 100%, NSFR ≥ 100%

  RWA = Risk-Weighted Assets (credit risk + market risk + operational risk)
  CET1 = Common Equity Tier 1 (tangible equity, retained earnings)

MARKET RISK CAPITAL (FRTB, 2025):
  Internal Models Approach (IMA): ES₉₇.₅% × multiplier + stress capital add-on
  Standardized Approach (SA): sensitivity-based method with prescribed risk weights

STRESS VaR (SVaR):
  VaR using 12-month stressed period (e.g., 2008 crisis data)
  Capital = max(VaR_t, multiplier × avg(60d VaR)) + max(SVaR_t, multiplier × avg(60d SVaR))
  Multiplier k ≥ 3; increases if backtesting exceptions (regulatory scrutiny)
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What does VaR₉₉% = $10M mean? | 1% chance of losing more than $10M tomorrow |
| Why was VaR blamed for 2008? | Underestimated tail risk; not subadditive; pro-cyclical |
| What replaced VaR in regulations? | Expected Shortfall (ES₉₇.₅%) under Basel FRTB |
| Is VaR still used? | Yes — widely used internally; ES required for regulatory capital |
| How do I model fat tails? | EVT (GPD for peaks over threshold); t-copula for joint tails |
| What's wrong with Gaussian copula? | Zero tail dependence — underestimates joint crashes |
| What's the difference between VaR and CVaR? | VaR = threshold; CVaR = average loss beyond that threshold |
| How to stress test a portfolio? | Historical scenarios (1987, 2008, COVID) + hypothetical scenarios |

---

## Common Confusion Points

**"VaR tells you the worst loss"** — VaR tells you a loss threshold not
exceeded with probability α. It says nothing about how bad it gets beyond
that. A bond portfolio and an option portfolio could have identical VaR but
completely different tail behavior.

**"Diversification always reduces risk"** — in normal times yes. During
crises, correlations spike toward 1, diversification fails exactly when
needed most. Copulas with tail dependence (t-copula, Clayton) model this.

**"Model risk is secondary"** — the 2008 crisis was partly a model risk
event. Gaussian copula underestimated joint default probabilities by orders
of magnitude. VaR models that had never seen a mortgage crisis gave
false confidence.

**"CVaR = Conditional VaR = Expected Shortfall = all the same"** — yes,
CVaR (conditional value at risk) and ES (expected shortfall) are the same
thing: E[Loss | Loss > VaR]. Different textbooks use different notation.
CVaR and CVaR₀ (centered) occasionally differ; always clarify definition.

**"Higher risk → higher return is always true"** — only for systematic,
priced risk factors. Idiosyncratic risk is not compensated (diversify away).
The equity risk premium, term premium, credit spread are compensated risks.
Lottery-like payoffs (positive skewness) often have negative excess returns.
