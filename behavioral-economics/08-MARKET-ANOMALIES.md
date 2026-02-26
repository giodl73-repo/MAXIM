# Market Anomalies

## Behavioral Finance Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    BEHAVIORAL FINANCE LANDSCAPE                              │
│                                                                               │
│  EFFICIENT MARKET HYPOTHESIS (Fama 1970):                                   │
│  Prices reflect all available information.                                   │
│  No systematic profitable trading strategy exists.                          │
│  Price changes = unpredictable (random walk).                               │
│                                                                               │
│  BEHAVIORAL CHALLENGE:                                                       │
│  Systematic, predictable pricing errors exist.                              │
│  These anomalies are inconsistent with rational risk-based explanations.    │
│  They are consistent with psychological mechanisms (prospect theory,        │
│  overconfidence, representativeness, loss aversion).                        │
│                                                                               │
│  KEY TENSION: If anomalies are real, why don't arbitrageurs eliminate them? │
│  ANSWER: Limits to arbitrage (Shleifer & Vishny 1997):                      │
│  - Risk: arbitrage is never riskless (noise trader risk)                    │
│  - Horizon: arbitrageurs may not survive until prices converge              │
│  - Short-selling constraints: hard to short; costly                        │
│  - Tracking error: fund managers fired before anomaly corrects             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## The Equity Premium Puzzle

```
EQUITY PREMIUM PUZZLE (Mehra & Prescott 1985):
  Historical US equity premium: ~6-8% per year above risk-free rate.
  Stocks have returned ~10-12% annually; T-bills ~1-4%.
  Premium: ~6-8% per year, on average, for 100+ years.

  RATIONAL RISK-BASED EXPLANATION:
  Stocks are riskier than bonds → rational investors demand a premium.
  Lucas (1978) consumption-based CAPM: calibrated to consumption volatility.
  To explain 6-8% premium with standard utility model (CRRA):
  Requires coefficient of relative risk aversion γ ≈ 30-100.
  But: at γ = 30, investors would refuse a 50/50 gamble between doubling and
  losing 1.4% of wealth. No calibration of reasonable risk aversion reproduces
  the observed premium without implausible parameters.

  BEHAVIORAL EXPLANATIONS:

  1. MYOPIC LOSS AVERSION (Benartzi & Thaler 1995):
     Combines loss aversion (λ ≈ 2.25) with narrow framing (evaluate portfolio
     performance frequently — myopically).
     If investors evaluate losses annually: stocks look scary (20% chance of loss
     in any given year → loss aversion pain).
     If evaluated over 10-year horizon: much less often a loss year.
     Calibrated model with λ = 2.25 and annual evaluation:
     Exactly reproduces the historical ~6% equity premium!
     This is among the most successful quantitative behavioral predictions.

  2. HABIT FORMATION (Campbell & Cochrane 1999):
     Risk premium depends on local risk aversion, which varies with wealth
     relative to habit level. When wealth falls near habit: extreme aversion.
     Captures time variation in risk premium.

  3. AMBIGUITY AVERSION:
     Equity returns involve Knightian uncertainty (unknown probability distribution).
     Ambiguity aversion → additional premium demanded over and above risk premium.

  CONNECTION TO FINANCE/:
  Equity premium is the central puzzle in quantitative finance.
  The behavioral explanation (myopic loss aversion) is elegant:
  λ from laboratory experiments (Kahneman-Tversky) × observed evaluation frequency
  → observed market premium. Cross-disciplinary validation.
```

## Disposition Effect

```
DISPOSITION EFFECT (Shefrin & Statman 1985):
  Investors tend to:
  SELL winners too early  (realize gains quickly)
  HOLD losers too long    (avoid realizing losses)

  MECHANISM: Prospect Theory prediction.
  Reference point = purchase price.
  When price > purchase price: gain domain. Concave utility → risk averse → sell
    to lock in gain (avoid chance of going back down).
  When price < purchase price: loss domain. Convex utility → risk seeking → hold
    to avoid locking in the loss (gamble on recovery).

EMPIRICAL EVIDENCE:
  Odean (1998): analysis of 10,000 individual brokerage accounts (1987-1993).
  "Proportion of gains realized" / "Proportion of losses realized":
  PGR = 0.148 (sell ~15% of winning positions)
  PLR = 0.098 (sell ~10% of losing positions)
  Disposition ratio = PGR/PLR = 1.51 (50% more likely to sell winners than losers)
  Robust: persists after controlling for transaction costs, taxes, portfolio rebalancing.

  TAX IMPLICATION: The rational strategy is exactly OPPOSITE.
  For taxable accounts: sell losers at year-end (realize capital losses → tax benefit).
  Hold winners (defer capital gains → delay tax payment).
  Investors are doing the wrong thing for tax purposes, consistent with loss aversion.

AGGREGATE MARKET IMPLICATIONS:
  If many investors hold losers and sell winners:
  Past winners → selling pressure → underperform going forward
  Past losers → holding (limited selling pressure) → underperform due to continued drift
  This partially explains the MOMENTUM anomaly (below).

PROFESSIONAL INVESTORS:
  Disposition effect present but weaker among institutional traders.
  Seru, Shumway & Stoffman (2010): disposition effect strongest for inexperienced investors;
  partially eliminated through learning.
  But: never fully eliminated even in experienced traders.
```

## Momentum

```
MOMENTUM ANOMALY (Jegadeesh & Titman 1993):
  Past winners continue to outperform past losers over 3-12 month horizons.
  Strategy: buy stocks in top quintile of past 6-12 month returns;
            sell stocks in bottom quintile.
  Annual alpha: historically ~10-12% (before transaction costs).

  This violates weak-form EMH: past prices should not predict future returns.

BEHAVIORAL EXPLANATIONS:
  1. UNDERREACTION to information (Barberis, Shleifer & Vishny 1998):
     Investors update beliefs insufficiently when news arrives (anchoring).
     → Price adjustment is gradual → continuing drift in direction of initial move.

  2. INVESTOR INERTIA: Slow diffusion of information across investor population.
     Some investors react fast; most react slow → serial autocorrelation in returns.

  3. OVERCONFIDENCE (Daniel, Hirshleifer & Subrahmanyam 1998):
     Overconfident investors overreact to private information → prices overshoot.
     But also underreact to public information.
     Long-run reversal: overreaction eventually corrects → momentum eventually
     reverses at 3-5 year horizon (consistent with evidence).

MOMENTUM CRASHES:
  Momentum can crash suddenly and severely (e.g., 2009 recovery).
  When market recovers sharply after a crash: past losers (beaten-down stocks)
  bounce hardest → momentum strategy (short losers) catastrophically short-squeezed.
  Daniel & Moskowitz (2016): momentum crashes driven by high market beta of loser portfolio.

LIMITS TO ARBITRAGE:
  Momentum is profitable after transaction costs for large institutional investors.
  Why does it persist? Benchmark constraints (tracking error), short-selling costs,
  crashes, and career risk prevent full arbitrage.
```

## Overconfidence in Markets

```
OVERCONFIDENCE → EXCESS TRADING:
  De Bondt & Thaler (1985): "Does the stock market overreact?"
  Portfolios of past 3-5 year losers outperform past winners over next 3-5 years.
  Over-reaction to news → over-pricing winners, under-pricing losers.
  Contrarian strategy: profitable over long horizon.

EXCESS TRADING AND OVERCONFIDENCE (Odean 1999):
  Hypothesis: overconfident traders trade too much.
  Mechanism: overconfidence → perceived informational edge → excessive trading.
  Finding: the more investors trade, the worse their net returns.
  "Men trade more than women; men's returns worse than women's" (Barber & Odean 2001).
  Active trader returns ≈ market − ~3-4% (after transaction costs).

ANALYST FORECAST BIAS (De Bondt & Thaler 1990):
  Analysts' earnings forecasts are systematically optimistic:
  Long-term earnings growth forecasts average ~15-17% per year.
  Actual long-run earnings growth: ~6-7% per year.
  Persistent, large overestimation.
  Causes: overconfidence, career incentives (maintain relationships with management),
  anchoring to recent growth rates (representativeness).

  HERDING AMONG ANALYSTS:
  Analysts' forecasts cluster (Welch 2000).
  Career risk: "it is safer to fail conventionally than to succeed unconventionally."
  Deviating from consensus → personal reputation risk if wrong.
  Following consensus → blame shared if wrong.
  → Systematic under-dispersion of analyst forecasts relative to rational disagreement.
```

## Behavioral Explanations for Additional Anomalies

```
VOLATILITY PUZZLE (Shiller 1981 — variance bounds test):

  SETUP: Under rational expectations, stock price = PV of future dividends.
    P_t = E_t[Σ_{k=1}^∞ d_{t+k} / (1+r)^k]   (present value formula)
    If r is constant, define P* = ex-post rational price = actual PV of realized dividends

  VARIANCE BOUNDS TEST:
    P* is the "correct" price a rational agent would set if they knew future dividends.
    By the law of iterated expectations: Var(P*) ≥ Var(P_t)
    (P* has more information than P_t; variance should be at least as large)

    Shiller's finding: empirically, Var(P_t) >> Var(P*) — prices are MORE volatile
    than the ex-post rational benchmark that knows the actual dividend stream.
    Prices are ~5-13× more volatile than justified by dividends alone.

    This is a direct violation of the rational expectations PV model.
    Not a failure at the margin — a factor of 5-10× discrepancy.

  QUANTITATIVE CALIBRATION:
    S&P 500 dividend yield std dev: ~0.5-1% per year
    S&P 500 price std dev: ~15-20% per year (annualized)
    Rational model with constant discount rate predicts price std dev ≈ divided by r^2
    At r = 5%: implies price std dev ≈ 20× dividend std dev (comparable to observed)
    But: LeRoy & Porter (1981), Shiller (1981) test more carefully using realized dividends
    → Prices still "too volatile" even accounting for plausible discount rate variation.

  CRITICISMS AND REFINEMENTS:
    West (1988): test requires dividend stationarity; unit root in dividends complicates it
    Marsh & Merton (1986): dividends are smoothed → dividend volatility understates
    Campbell & Shiller (1988): log-linearized return decomposition:
      log return = dividend yield + capital gain
      Variance decomposition: most of price variance = discount rate variation, not dividend news
      Time-varying risk premium explains much of excess price volatility

  BEHAVIORAL EXPLANATIONS:
    Investor sentiment (DeLong, Shleifer, Summers, Waldmann 1990 — noise trader model):
      Noise traders have stochastic misperceptions of asset value
      Rational arbitrageurs can't fully correct because noise trader risk is systematic
      (arbitrage requires a risky short position; noise traders can push price further wrong)
      Sentiment risk is priced → persistent excess volatility even with rational arbitrageurs

    Excess extrapolation (Barberis, Greenwood, Jin, Shleifer 2015):
      Investors extrapolate recent returns into future expectations
      Rising prices → bullish expectations → more buying → further price rise
      Falling prices → bearish → more selling → further fall
      Creates momentum + mean-reversion at different horizons; amplifies fundamental volatility

    Overconfidence (Odean 1998, DeBondt-Thaler 1985):
      Investors overestimate precision of private signals
      Trade excessively; disagree more than rational agents would → inflated volume and volatility

  PRACTICAL IMPLICATION:
    Market prices fluctuate for reasons beyond dividend news — shifts in risk appetite,
    sentiment, and discount rates drive most short- to medium-run variance.
    This is the empirical basis for the Shiller CAPE ratio as a valuation tool:
    CAPE smooths 10-year earnings to filter out cyclical noise; high CAPE historically
    predicts low subsequent 10-year returns (r ≈ −0.6 over 1880-2020 in US data).

CALENDAR ANOMALIES:
  January effect: small-cap stocks abnormally high returns in January.
  Tax-loss selling in December → price depression → recovery in January.
  Partially behavioral (tax-loss harvesting creating systematic seasonality).
  Weaker post-documentation (anomaly partially arbitraged away after Keim 1983).

SIZE AND VALUE PREMIUMS:
  Small-cap stocks historically outperform large-cap (size premium).
  Value stocks (low P/B) outperform growth stocks (value premium).
  Fama-French: risk-based explanation (small and value are riskier).
  Behavioral interpretation: overreaction → growth stocks overpriced, value underpriced.
  Both explanations have some support; not definitively resolved.

IPO UNDERPERFORMANCE (Ritter 1991):
  IPOs underperform matched firms over 3-5 years post-IPO.
  Short-run: IPO underpricing (first-day pop).
  Long-run: investor overoptimism → overpricing at IPO.
  Behavioral: representativeness (recent growth extrapolated indefinitely).
  Firms go public when investors are most enthusiastic (market timing).
```

## Limits to Arbitrage

```
WHY ANOMALIES PERSIST:
  If prices are wrong, why don't rational arbitrageurs correct them?

SHLEIFER & VISHNY (1997) LIMITS TO ARBITRAGE:
  1. FUNDAMENTAL RISK: No perfect substitute → can't fully hedge.
     Arbitrage against Ford requires shorting GM; but GM ≠ Ford perfectly.
     Residual risk even in "arbitrage."

  2. NOISE TRADER RISK (De Long et al. 1990):
     Irrational investors (noise traders) can move prices further wrong before
     they correct. Rational arbitrageur may be forced to close position at a loss
     before the price corrects.
     "Markets can remain irrational longer than you can remain solvent." (Keynes)

  3. IMPLEMENTATION CONSTRAINTS:
     Short-selling: expensive, hard, restricted for many investors.
     Institutional mandates: not allowed to short, long-only constraint.
     Concentration limits: can't hold >x% of portfolio in single short.

  4. AGENCY COSTS:
     Fund managers: career risk if underperform benchmark while waiting for
     anomaly to correct. Fired before the arbitrage pays off.
     "Arbitrage" requires patient capital → but capital providers are impatient.

  CONSEQUENCE:
  Mispricing can persist indefinitely if the limits to arbitrage are strong enough.
  This is not consistent with strict EMH but is consistent with market that is
  efficient in the long run but with systematic, exploitable deviations.
```

## Decision Cheat Sheet

| Market anomaly | Behavioral mechanism | Investment implication |
|---|---|---|
| Equity premium puzzle | Myopic loss aversion (λ=2.25 × annual evaluation) | Long-horizon investors should hold more equity than market implies |
| Disposition effect | Prospect theory: sell winners (gain domain risk aversion), hold losers (loss domain risk seeking) | Tax-loss harvesting; challenge your own selling decisions |
| Momentum (3-12 months) | Underreaction to news; investor inertia | Momentum factor in diversified portfolio |
| Long-run reversal (3-5 years) | Overreaction to earnings; correction | Value/contrarian strategy |
| Excess trading | Overconfidence in informational edge | Index funds beat active trading for most investors |
| Analyst optimism | Overconfidence + career incentives | Discount long-term analyst growth projections substantially |
| IPO underperformance | Investor overoptimism at listing | Be skeptical of hot IPOs; wait for post-lockup rationalization |

## Common Confusion Points

**Anomalies can be risk-based or behavioral**: Many market anomalies have both risk-based and behavioral explanations. The size premium might reflect illiquidity risk (risk-based) or overreaction (behavioral). The academic debate is ongoing and may never be fully resolved because risk and mispricing are hard to separate. Practical implication: the premium exists; whether it's risk or behavior matters for predicting persistence.

**Many anomalies weakened after publication**: McLean & Pontiff (2016): 97 anomalies studied — returns decay by ~35% post-publication. Partly because arbitrageurs trade on the published patterns. But many persist — limits to arbitrage are real. Documented anomaly ≠ free money; but documented anomaly ≠ eliminated.

**Myopic loss aversion explains equity premium quantitatively**: This is one of the most impressive predictions in behavioral economics — using independently estimated parameters (λ from K-T lab experiments, observed evaluation frequency) to explain a long-standing market puzzle. The quantitative fit is remarkable.

**Individual investor findings don't generalize to institutional**: Disposition effect, excess trading, overconfidence are strongest for retail investors. Professional traders and institutions are not immune but show these effects more weakly. Institutional markets are more efficient than retail markets. But: institutions face their own behavioral distortions (herding, career risk, tournament effects).
