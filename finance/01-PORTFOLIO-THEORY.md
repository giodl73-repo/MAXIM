# Portfolio Theory — Markowitz, CAPM, Factor Models

## The Big Picture

Portfolio theory answers: **given a set of risky assets, how should you combine them to
maximize expected return for a given risk level?** The mathematics is convex optimization
applied to a stochastic problem — Markowitz (1952) founded the field, CAPM extended it to
equilibrium, and factor models added explanatory power.

```
HISTORICAL ARC:
  1952: Markowitz — mean-variance optimization, efficient frontier
  1964: Sharpe — CAPM (single-factor model, market beta)
  1973: Merton — ICAPM (multi-factor, dynamic)
  1976: Ross — APT (Arbitrage Pricing Theory, factor model)
  1992: Fama-French — 3-factor model (Mkt + SMB + HML)
  1997: Carhart — 4-factor (+ MOM momentum)
  2015: Fama-French — 5-factor (+ RMW profitability + CMA investment)
  Today: 100s of "factors" published; factor zoo; replication crisis

MATHEMATICAL TOOLKIT:
  Mean-variance: quadratic programming
  CAPM: linear regression
  Factor models: multivariate regression + PCA
  Black-Litterman: Bayesian updating of prior = CAPM equilibrium
```

---

## Returns and Risk Basics

```
RETURN DEFINITIONS:
  Simple return:    Rt = (Pt - Pt-1 + Dt) / Pt-1
  Log return:       rt = ln(Pt/Pt-1) = ln(1 + Rt)

  Log returns are additive over time: r(0→T) = Σ rt
  Simple returns are additive across assets: R_portfolio = Σ wi·Ri
  Use log returns for time series; simple returns for cross-sectional portfolios

EXPECTED RETURN: μ = E[R]  (estimated from sample mean or factor model)

VARIANCE (risk): σ² = E[(R-μ)²]  (estimated from sample variance)

COVARIANCE: σ_ij = E[(Ri-μi)(Rj-μj)]

COVARIANCE MATRIX:
  Σ = [σ₁₁  σ₁₂  ... σ₁ₙ]
      [σ₂₁  σ₂₂  ... σ₂ₙ]
      [  :        ⋱    : ]
      [σₙ₁  σₙ₂  ... σₙₙ]
  Symmetric, positive semi-definite
  Diagonal: own variances; off-diagonal: pairwise covariances
```

---

## Markowitz Mean-Variance Optimization

### Portfolio Statistics

For n assets with weight vector **w** (Σwi = 1):

```
Portfolio expected return:   μ_p = wᵀμ  (dot product)
Portfolio variance:          σ²_p = wᵀΣw
Portfolio std deviation:     σ_p = √(wᵀΣw)

DIVERSIFICATION BENEFIT:
  If all assets have variance σ² and pairwise correlation ρ:
    σ²_p = σ²(1/n + (1-1/n)ρ)

  As n→∞: σ²_p → σ²ρ  (residual from correlation, cannot diversify away)

  Systematic risk: ρ·σ² — survives diversification
  Idiosyncratic risk: (1-ρ)σ²/n → 0 — diversified away
```

### Efficient Frontier

```
MINIMUM VARIANCE PORTFOLIO:
  min  wᵀΣw
  s.t. wᵀ1 = 1   (fully invested)

Solution: w_mv = Σ⁻¹1 / (1ᵀΣ⁻¹1)

EFFICIENT FRONTIER (with target return μ*):
  min  wᵀΣw
  s.t. wᵀ1 = 1
       wᵀμ = μ*

Solution: w* = (a·Σ⁻¹μ + b·Σ⁻¹1)  (two-fund separation!)
          where a, b are scalars solving the two constraints

TWO-FUND SEPARATION THEOREM:
  Any efficient portfolio = linear combination of ANY two efficient portfolios
  Investors only need to choose between: risk-free asset + market portfolio

GEOMETRY:
  μ_p
   |          ← efficient frontier (northeast boundary of feasible set)
   |         /
   |        /  ← Capital Market Line (with risk-free asset)
   |       /
   |    *  ← minimum variance portfolio
   |   /   ← individual assets scatter below frontier
   |  /
   | /
  Rf────────────────────→ σ_p

  Efficient frontier: achievable (μ,σ) with no wasted return for given risk
  Capital Market Line: introduces risk-free asset → straight line tangent to frontier
```

### Sharpe Ratio

```
SHARPE RATIO: SR = (μ_p - Rf) / σ_p

Measures return per unit of risk above risk-free rate.
Tangency portfolio maximizes SR → it is the Market Portfolio in CAPM.

w_tangency = Σ⁻¹(μ - Rf·1) / (1ᵀΣ⁻¹(μ - Rf·1))

Optimal allocation with risk-free asset:
  wᵢₙᵥₑₛₜₒᵣ = (1/λ) · w_tangency  where λ = risk aversion coefficient
```

---

## CAPM — Capital Asset Pricing Model

CAPM (Sharpe 1964, Lintner 1965) is a market equilibrium model:

```
E[Ri] - Rf = βi · (E[Rm] - Rf)

where:
  Ri    = return on asset i
  Rf    = risk-free rate
  Rm    = market return (e.g., S&P 500)
  βi    = Cov(Ri, Rm) / Var(Rm)  ← systematic risk loading
  E[Rm] - Rf = equity risk premium (ERP) ≈ 5-7% historically
```

### Beta Interpretation

```
BETA    MEANING                      EXAMPLE
──────  ────────────────────────────  ─────────────────────────────────────
β = 0   No co-movement with market    Cash (Rf), gold (roughly)
β = 0.5 Half the market volatility   Utility stocks, staples
β = 1   Moves with market            Index fund by definition
β = 1.5 50% more than market         Tech stocks, cyclicals
β < 0   Moves opposite to market     Long volatility instruments (VIX-linked)
```

### Security Market Line

```
Expected Return
   |                    *  (above SML = underpriced, buy)
   |                /
   |              /  ← Security Market Line
   |         *  /
E[Rm] ──── / ──────────────────
   |      /   * (below SML = overpriced, sell)
   Rf ──/────────────────────────→ Beta
       0  1
```

**Alpha (α) = actual return − CAPM expected return**. Positive alpha → manager added
value beyond systematic exposure. CAPM predicts α = 0 in equilibrium.

### CAPM Assumptions and Failures

```
ASSUMPTIONS (all violated in practice):
  ─ Single period
  ─ Mean-variance preferences (quadratic utility or normal returns)
  ─ Homogeneous expectations
  ─ Frictionless markets (no taxes, costs, short-sale constraints)
  ─ All investors hold the same tangency portfolio (= market)

EMPIRICAL FAILURES:
  ─ Small stocks outperform (size effect, SMB) — CAPM β doesn't explain
  ─ Value stocks outperform (B/M ratio, HML) — CAPM β doesn't explain
  ─ Momentum: past winners beat past losers
  ─ Low-volatility anomaly: low-β stocks earn high risk-adjusted returns
  ─ Market β alone explains <10% of cross-sectional return variation
```

---

## Fama-French Factor Models

```
3-FACTOR MODEL (1992):
  Ri - Rf = αi + βi,mkt(Rm-Rf) + βi,smb·SMB + βi,hml·HML + εi

  SMB = "Small Minus Big"   = return of small stocks − return of large stocks
  HML = "High Minus Low"    = return of high B/M (value) − low B/M (growth)

  Average annual premiums (US, 1963-2023):
    Mkt-Rf ≈ 5.5%
    SMB    ≈ 2.4%
    HML    ≈ 3.1%

4-FACTOR (Carhart 1997):
  Adds: MOM = Momentum = return of 12-2 month past winners − past losers
  MOM ≈ 7-9% historically (but crashes badly in specific years)

5-FACTOR (Fama-French 2015):
  Adds:
    RMW = "Robust Minus Weak"  = profitable − unprofitable firms
    CMA = "Conservative Minus Aggressive" = low − high investment firms
  Note: HML becomes redundant when RMW and CMA included (empirically)

FACTOR ZOO PROBLEM (Cochrane 2011 presidential address):
  400+ factors published that "predict" returns
  Most are data-mined / multiple hypothesis testing artifacts
  Out-of-sample performance much weaker (Harvey et al. 2016)
  Need t-stat > 3.0 (not 2.0) for factor to be credible
```

---

## Black-Litterman Model

Practical Markowitz: solves estimation sensitivity problem.

```
PROBLEM WITH RAW MARKOWITZ:
  μ is estimated with huge uncertainty from historical returns
  Small estimation errors → extreme, unstable portfolio weights
  "Error maximization" critique: optimizer amplifies estimation errors

BLACK-LITTERMAN APPROACH (Goldman Sachs, 1990):
  Start with CAPM equilibrium as prior for returns:
    Π = λ·Σ·w_mkt   (implied equilibrium returns)

  Incorporate investor "views" as likelihood:
    P·μ = Q + ε   where ε ~ N(0, Ω)
    P = view matrix (which assets)
    Q = expected return for each view
    Ω = uncertainty in views (diagonal)

  Bayesian posterior for expected returns:
    μ_BL = [(τΣ)⁻¹ + PᵀΩ⁻¹P]⁻¹ · [(τΣ)⁻¹Π + PᵀΩ⁻¹Q]

    τ ≈ 1/T (usually small, scaling factor)

  Resulting portfolio is tilted from market cap weights by views.

INTUITION:
  Without views: portfolio = market cap weights (CAPM equilibrium)
  With views: portfolio tilts proportional to view conviction and precision
  Uncertainty (large Ω) → small tilt; strong conviction (small Ω) → large tilt
```

---

## Risk Parity

Alternative to Markowitz that targets equal risk contribution:

```
EQUAL RISK CONTRIBUTION PORTFOLIO:
  Risk contribution of asset i: RCi = wi · (Σw)i / (wᵀΣw)

  Constraint: RCi = 1/n for all i

  Implies: overweight low-volatility/low-correlation assets
           underweight high-volatility assets

LEVERAGE ISSUE:
  Low-vol assets (bonds) get high weight → often leveraged to match equity target
  Risk parity strategies borrow to fund bond allocation
  Worked well 1980-2020 (falling rates); underperformed in 2022 rising-rate environment

BRIDGEWATER ALL WEATHER:
  Conceptually similar — balance "risk" across economic environments
  Asset classes: stocks, bonds, gold, commodities × (risk on/off) = 4 buckets
```

---

## Portfolio Optimization in Practice

```
ESTIMATION CHALLENGES:
  Covariance matrix: n(n+1)/2 parameters for n assets
    n=500 stocks: 125,250 parameters
    Historical estimate very noisy; needs regularization

  LEDOIT-WOLF SHRINKAGE:
    Σ_shrunk = (1-α)·Σ_sample + α·Σ_target
    Target: structured matrix (diagonal, identity, single-factor)
    α chosen to minimize expected estimation error

PRACTICAL CONSTRAINTS:
  Long-only: wi ≥ 0 (can't short)
  Max position size: wi ≤ w_max (risk management)
  Tracking error: ||w - w_benchmark|| ≤ TE_budget
  Turnover: Σ|wi_new - wi_old| ≤ turnover_budget

QUADRATIC PROGRAM FORM:
  min  wᵀΣw − λ·wᵀμ      (mean-variance with λ = risk aversion)
  s.t. Aw = b              (equality constraints: budget, sector, ...)
       lb ≤ w ≤ ub         (bounds: long-only, max position)

  Solved by standard QP solvers (cvxpy, Gurobi, scipy.optimize)
```

---

## Factor Model Implementation

```python
# Fama-French 3-factor regression (conceptual)
import numpy as np

# Data: T × n returns matrix R, T × 3 factor returns F
# R: stock returns (excess)
# F: [Mkt-Rf, SMB, HML]

# OLS regression for each stock:
# r_i = α_i + β_i,mkt·F_mkt + β_i,smb·F_smb + β_i,hml·F_hml + ε_i

X = np.column_stack([np.ones(T), F])  # T × 4 (intercept + 3 factors)
# Beta = (X'X)⁻¹X'R   (n × 4 matrix of coefficients for all stocks)
Beta = np.linalg.lstsq(X, R, rcond=None)[0]  # 4 × n

alphas = Beta[0, :]       # intercepts (alpha)
factor_loadings = Beta[1:, :]   # 3 × n factor betas

# Factor model covariance matrix decomposition:
# Σ = B·F_cov·Bᵀ + D   (systematic + idiosyncratic)
# B: n × k factor loading matrix
# F_cov: k × k factor covariance matrix
# D: n × n diagonal idiosyncratic variance matrix
```

---

## Decision Cheat Sheet

| Task | Method |
|------|--------|
| Optimal portfolio given μ and Σ | Markowitz QP (minimize wᵀΣw for target return) |
| One-number portfolio quality | Sharpe ratio |
| Tangency portfolio | Maximize Sharpe = Σ⁻¹(μ-Rf) normalized |
| Understand systematic risk | CAPM beta |
| Explain cross-sectional return variation | Fama-French 3- or 5-factor model |
| Robust portfolios with views | Black-Litterman |
| Balance risk across assets | Risk parity / equal risk contribution |
| Handle estimation error | Ledoit-Wolf shrinkage, robust optimization |
| Decompose portfolio variance | Factor model: systematic + idiosyncratic |
| Test if a manager adds alpha | Fama-French regression, check α significance |

## Common Confusion Points

**Markowitz optimizes in-sample but often fails out-of-sample.** The optimizer treats
estimated μ and Σ as exact — but estimation error is large, especially for expected
returns (1-2% standard error per year). Use shrinkage, Black-Litterman, or minimum-variance
(ignore μ entirely) for practical robustness.

**Beta is context-dependent.** A stock's beta changes with the estimation window, frequency
(daily vs monthly), and benchmark choice. "The" beta of a stock is not a stable physical constant.

**Diversification reduces idiosyncratic risk, not systematic.** You can add 1000 stocks
to a portfolio and still have full market beta. Correlation to the market does not go away.

**The market portfolio in CAPM theory ≠ S&P 500 in practice.** CAPM's market portfolio
includes ALL risky assets: international stocks, private equity, real estate, human capital.
The S&P 500 is a proxy for a component of this.

**High Sharpe ratio in-sample often means overfitting.** Adding constraints and using
robust estimation routinely halves the in-sample Sharpe ratio but doubles out-of-sample.
