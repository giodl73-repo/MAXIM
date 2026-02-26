# Quantitative Finance — Field Map & Orientation

## The Big Picture

Finance is applied mathematics: stochastic calculus, optimization, statistics, and
probability theory deployed on market data. As an MIT Math + TCS person, you already have
the machinery — this maps it onto the financial domain and shows where the interesting
mathematical problems live.

```
+------------------------------------------------------------------+
|                 QUANTITATIVE FINANCE LANDSCAPE                    |
+------------------------------------------------------------------+
|                                                                   |
|  ASSET PRICING      PORTFOLIO MGMT    RISK MGMT    DERIVATIVES   |
|  ┌─────────────┐   ┌─────────────┐   ┌─────────┐  ┌─────────┐  |
|  │ CAPM        │   │ Markowitz   │   │ VaR     │  │ B-S-M   │  |
|  │ Fama-French │   │ Efficient   │   │ CVaR    │  │ Options │  |
|  │ APT         │   │ frontier    │   │ Stress  │  │ Greeks  │  |
|  │ SDF/pricing │   │ Black-Litt. │   │ testing │  │ Exotics │  |
|  │ kernel      │   │ Factor mdls │   │ Copulas │  │ Hedging │  |
|  └─────────────┘   └─────────────┘   └─────────┘  └─────────┘  |
|                                                                   |
|  FIXED INCOME       MARKET MICRO     COMPUTATIONAL  ML IN FIN   |
|  ┌─────────────┐   ┌─────────────┐   ┌──────────┐  ┌────────┐  |
|  │ Bond math   │   │ Order book  │   │ Monte    │  │Factor  │  |
|  │ Duration    │   │ Bid-ask     │   │ Carlo    │  │models  │  |
|  │ Yield curve │   │ Price disc. │   │ MCMC     │  │Alt data│  |
|  │ Vasicek/CIR │   │ HFT         │   │ PDE      │  │NLP/LLM │  |
|  │ Term struct │   │ Adverse sel │   │ solvers  │  │RL      │  |
|  └─────────────┘   └─────────────┘   └──────────┘  └────────┘  |
+------------------------------------------------------------------+
```

---

## Asset Classes

```
ASSET CLASS         DESCRIPTION                      EXAMPLES
──────────────────  ───────────────────────────────  ──────────────────────────
Equities (stocks)   Ownership claim on firm cashflows AAPL, SPY, emerging markets

Fixed income        Debt instruments with coupon      T-bills, corporate bonds,
                    and maturity                      MBS, CDS, CDOs

Derivatives         Contracts deriving value from     Options, futures, swaps,
                    underlying asset                  swaptions, exotics

Commodities         Physical goods or futures         Oil (WTI/Brent), gold,
                    contracts on them                 agricultural, energy

FX (currencies)     Exchange rate between currencies  EUR/USD, yen carry trade

Alternatives        Non-traditional investments       Private equity, hedge funds,
                                                      real estate, infrastructure

Crypto              Digital bearer assets             BTC (digital gold narrative),
                                                      ETH (smart contract platform)
```

---

## Market Microstructure

Before talking about models, understand how prices actually get formed:

```
ORDER BOOK (Level 2 data)
──────────────────────────────────────────────────────────────
  ASK (sells)                BID (buys)
  ┌──────────────┐          ┌──────────────┐
  │ $100.05  10  │          │ $100.00  25  │ ← Best bid
  │ $100.04  30  │          │  $99.99  100 │
  │ $100.03  15  │ ← Ask    │  $99.98  50  │
  │ $100.02  50  │          │  $99.97  200 │
  └──────────────┘          └──────────────┘
       Spread = $100.02 - $100.00 = $0.02 (2 cents)

Market order: executes immediately at best available price
Limit order: sits in book until match found or cancelled
Market maker: provides liquidity both sides; profit = spread × volume
Market taker: demands liquidity; pays spread

Price discovery: the continuous mechanism converting information
               into prices (Grossman-Stiglitz paradox: if prices
               are perfectly informative, no one would pay to get
               information to trade on)
```

**Adverse selection:** Market makers face traders with private information (informed
traders). The bid-ask spread compensates for the risk of trading against someone who
knows the stock is worth $110 when you're selling at $100.05. This is the Kyle (1985)
and Glosten-Milgrom (1985) framework.

---

## Efficient Market Hypothesis (EMH)

```
FORM            CLAIM                           IMPLICATION
─────────────── ──────────────────────────────  ──────────────────────────────────
Weak form       Prices reflect all past prices  Technical analysis cannot work
                (historical return data)         (excess return over buy-and-hold)

Semi-strong     Prices reflect all public info  Fundamental analysis cannot work
                (earnings, macro data, news)     (no alpha from public research)

Strong form     Prices reflect ALL info,         Even insider information is priced
                including private                in (empirically false — insider
                                                 trading laws exist because it works)
```

The EMH debate is really about **market efficiency vs. market predictability at different
timescales**. Most practitioners believe: weak form ≈ true at short horizons (hard to
beat HFT); semi-strong ≈ mostly true; strong form ≈ false.

---

## The Mathematical Toolkit

```
MATH AREA           HOW IT APPEARS IN FINANCE
────────────────    ──────────────────────────────────────────────────────────
Probability         Asset return distributions, risk-neutral pricing measure
Stochastic calc.    Itô's lemma, SDEs, Black-Scholes PDE, diffusion models
Optimization        Markowitz frontier, LQR in execution, convex portfolio opt.
Linear algebra      Factor models, PCA on returns, covariance matrix estimation
Statistics          Regression for factor loadings, hypothesis testing returns
PDEs                Black-Scholes PDE, heat equation ← same PDE after transform
Monte Carlo         Option pricing (path-dependent), VaR, stress scenarios
Time series         ARIMA/GARCH for volatility modeling, cointegration for pairs
Graph theory        Systemic risk network models, contagion
Information theory  Entropy in portfolio construction, Kelly criterion
Game theory         Market microstructure (Cournot-Nash in oligopolies)
```

---

## Quant vs. Fundamental vs. Systematic

```
STYLE           WHAT THEY DO                        MATH INTENSITY
─────────────── ────────────────────────────────────────────────────────────
Fundamental     DCF models, qualitative business    Medium — statistics,
                analysis, sector expertise           basic valuation math

Quantitative    Factor models, stat-arb, alpha       High — regression,
                research on historical data          ML, time series

High-frequency  Microstructure, latency arbitrage,   Extreme — stochastic
(HFT)           market making, order flow analysis   control, optimization

Systematic      Rule-based execution of signals,     High — signal processing,
macro           macro factors (momentum, carry)      econometrics

Risk / quant    VaR, stress testing, CVA/DVA         Very high — stochastic
(banks)         pricing, regulatory capital           calculus, copulas
```

---

<!-- @editor[content/P2]: ML in Finance box appears in landscape diagram but has no drill-down section — significant gap given current industry relevance -->
<!-- @editor[content/P2]: No mention of data infrastructure (Bloomberg, CRSP, WRDS, Quandl) — practitioners need to know where to get data -->
<!-- @editor[bridge/P2]: No bridge from classical optimization tools (scipy, cvxpy, MATLAB) to financial optimization — learner knows optimization theory from MIT but not the finance-specific toolchain -->

## Session Arc for This Directory

```
00-OVERVIEW.md        ← You are here (asset classes, microstructure, EMH, math toolkit)
01-PORTFOLIO-THEORY   ← Markowitz, CAPM, factor models, efficient frontier
02-DERIVATIVES        ← Options, Black-Scholes, Itô calculus, Greeks, risk-neutral
03-FIXED-INCOME       ← Bonds, duration, yield curves, short-rate models
04-RISK-MODELS        ← VaR, CVaR, copulas, stress testing, systemic risk
```

---

## Decision Cheat Sheet

| You want to...                            | Relevant tool/concept        |
|-------------------------------------------|------------------------------|
| Build an optimized portfolio              | Markowitz mean-variance      |
| Understand expected returns               | CAPM / Fama-French factors   |
| Price a European call option              | Black-Scholes formula        |
| Hedge option delta                        | Delta/Gamma hedging          |
| Measure portfolio risk                    | VaR or CVaR (ES)             |
| Model interest rate dynamics              | Vasicek / CIR / Hull-White   |
| Analyze bond price sensitivity            | Duration + convexity         |
| Understand risk correlation in a crisis   | Copulas (Gaussian vs t)      |
| Model volatility clustering               | GARCH(1,1) or Heston model   |
| Find the risk-free arbitrage relationship | Put-call parity / APT        |

## Common Confusion Points

**Risk ≠ volatility alone.** Volatility (σ) is the standard risk proxy, but tail risk,
liquidity risk, and correlation risk can dominate in crises. Volatility is symmetric;
real losses are asymmetric (fat tails, skew).

**The risk-neutral measure ℚ ≠ real-world measure ℙ.** Option pricing uses ℚ (drift
replaced by risk-free rate); factor models for expected returns use ℙ (actual risk
premia). Confusing these leads to pricing vs. prediction mistakes.

**Alpha vs. beta.** Beta is systematic (market) risk — cheap, available via index funds.
Alpha is excess return above beta — what active managers claim to generate. Most fail
net of fees (Fama-French evidence).

**Duration measures linear sensitivity; convexity is the second-order correction.**
For large yield moves, the bond price–yield relationship is convex, and ignoring
convexity leads to hedging errors.

**Historical VaR does not predict future VaR.** In crises, correlations go to 1,
volatility spikes, and historical VaR dramatically understates true tail risk. CVaR
(Expected Shortfall) is a coherent risk measure that captures tail behavior better.
