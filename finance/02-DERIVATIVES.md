# Derivatives — Options, Black-Scholes, Greeks, Risk-Neutral Pricing

## The Big Picture

Derivatives are contracts whose value derives from an underlying asset (stock, bond,
commodity, interest rate, index). The mathematics is stochastic calculus — Brownian
motion, Itô's lemma, and the risk-neutral pricing measure.

<!-- @editor[diagram/P2]: Diagram lists derivative categories in stacked boxes but doesn't show relationships — e.g., how forwards underpin futures, how swaps decompose into forward contracts, how exotics build on vanilla options -->
```
DERIVATIVE LANDSCAPE:
  ┌───────────────────────────────────────────────────────────────┐
  │  FORWARDS/FUTURES: obligation to buy/sell at future price     │
  │  LINEAR payoff: V = S_T - K  (long forward on S at strike K) │
  ├───────────────────────────────────────────────────────────────┤
  │  OPTIONS: right (not obligation) to buy/sell                  │
  │  NONLINEAR payoff: V = max(S_T - K, 0)  (call option)        │
  ├───────────────────────────────────────────────────────────────┤
  │  SWAPS: exchange of cashflow streams (fixed ↔ floating rate)  │
  │  OTC bilateral; notional can be huge                          │
  ├───────────────────────────────────────────────────────────────┤
  │  EXOTICS: path-dependent, barrier, Asian, lookback, digital   │
  │  Structured products: CLOs, CDOs, synthetic CDOs              │
  └───────────────────────────────────────────────────────────────┘
```

---

## Options Fundamentals

```
CALL OPTION: right to BUY S at strike K at/before expiry T
  Payoff at expiry: max(S_T - K, 0) = (S_T - K)⁺
  In-the-money (ITM): S > K
  At-the-money (ATM): S ≈ K
  Out-of-the-money (OTM): S < K

PUT OPTION: right to SELL S at strike K at/before expiry T
  Payoff at expiry: max(K - S_T, 0) = (K - S_T)⁺
  In-the-money (ITM): S < K
  Out-of-the-money (OTM): S > K

EUROPEAN: exercisable only at expiry T
AMERICAN: exercisable at any time up to T (early exercise premium)

PAYOFF DIAGRAMS:
           Long Call         Long Put         Short Call
           ↑                 ↑                ↑
    profit │      /          │\               │───────\
           │     /           │  \             │        \
    ───────│────/────→ S_T   │   \────→ S_T  │         \──→ S_T
           │   K             │  K             K
    loss   │ (premium)       │(premium)       │ unlimited downside

PUT-CALL PARITY (European, no dividends):
  C - P = S - K·e^{-rT}
  (arbitrage relationship between call, put, stock, zero-coupon bond)

  PROOF (no-arbitrage):
    Portfolio A: Long call + K·e^{-rT} in cash
    Portfolio B: Long put + long stock
    At T: both pay max(S_T, K) → must have equal price today
```

---

## Stochastic Calculus Foundation

### Geometric Brownian Motion

```
STOCK PRICE MODEL (Black-Scholes assumption):
  dS = μS dt + σS dW_t

  S = stock price
  μ = drift (expected return under real-world measure ℙ)
  σ = volatility (constant, Black-Scholes assumption)
  W_t = Wiener process (Brownian motion) under ℙ
  dW_t ~ N(0, dt)   (infinitesimal increment)

SOLUTION (Itô's lemma on log S):
  S(t) = S(0) · exp((μ - σ²/2)t + σW_t)

  Log-normal distribution: ln(S_T/S_0) ~ N((μ-σ²/2)T, σ²T)
  S_T has mean: S_0 e^{μT}  (geometric average growth)

KEY PARAMETER: σ (volatility) is the critical unknown.
  μ (drift) cancels in derivative pricing under risk-neutral measure!
  σ does not — it fully determines option prices.
```

### Itô's Lemma

The fundamental calculus rule for stochastic functions — no chain rule naively:

```
ITO'S LEMMA: if dX = a dt + b dW,  and f = f(X, t), then:
  df = (∂f/∂t + a·∂f/∂X + ½b²·∂²f/∂X²) dt + b·∂f/∂X dW

The extra term ½b²·∂²f/∂X² arises because (dW)² = dt ≠ 0 in Itô calculus.
In classical calculus, (dx)² = 0.

APPLIED TO log S (derive Black-Scholes lognormal distribution):
  f = ln S, dS = μS dt + σS dW
  a = μS, b = σS, ∂f/∂S = 1/S, ∂²f/∂S² = -1/S², ∂f/∂t = 0

  d(ln S) = (μS · 1/S + ½σ²S² · (-1/S²)) dt + σS · (1/S) dW
           = (μ - σ²/2) dt + σ dW   ← drift correction term σ²/2 !
```

---

## Black-Scholes-Merton Model

### PDE Derivation

```
KEY INSIGHT (Black-Scholes, 1973): Δ-hedging eliminates randomness.

Portfolio: Long 1 call option C(S,t), short Δ shares of S.
  Π = C - Δ·S

  dΠ = dC - Δ·dS   (Itô + dS formula)
     = [∂C/∂t + ½σ²S²∂²C/∂S²] dt + (∂C/∂S - Δ)dW

  Choose Δ = ∂C/∂S  → dW term vanishes (Δ-hedging!)

  Risk-free portfolio must earn r: dΠ = r·Π·dt = r(C - Δ·S) dt

  Substituting:
  ∂C/∂t + ½σ²S²∂²C/∂S² = r(C - S·∂C/∂S)

  BLACK-SCHOLES PDE:
  ∂C/∂t + rS·∂C/∂S + ½σ²S²·∂²C/∂S² - rC = 0

  Same form as heat equation (change of variables x = ln S, τ = T-t)!
  Boundary condition (call): C(S,T) = max(S-K, 0)
```

### Black-Scholes Formula

```
EUROPEAN CALL:
  C = S·N(d₁) - K·e^{-rT}·N(d₂)

EUROPEAN PUT:
  P = K·e^{-rT}·N(-d₂) - S·N(-d₁)

where:
  d₁ = [ln(S/K) + (r + σ²/2)T] / (σ√T)
  d₂ = d₁ - σ√T

  N(·) = standard normal CDF
  S = current stock price
  K = strike price
  r = risk-free rate (continuously compounded)
  T = time to expiry
  σ = annualized volatility

INTUITION:
  N(d₂) = risk-neutral probability that option expires in-the-money
  N(d₁) = delta (shares to hold in replicating portfolio)
  S·N(d₁) = expected benefit (stock component)
  K·e^{-rT}·N(d₂) = expected cost (strike payment)
```

---

## Risk-Neutral Pricing

The deep insight: derivative pricing uses a special probability measure where ALL
assets grow at the risk-free rate.

```
REAL-WORLD MEASURE ℙ:
  dS = μS dt + σS dW^ℙ       (μ = actual expected return)
  Investors demand risk premium: μ > r

RISK-NEUTRAL MEASURE ℚ (Girsanov theorem):
  dS = rS dt + σS dW^ℚ       (drift replaced by r)
  dW^ℚ = dW^ℙ + (μ-r)/σ · dt  (changed measure)

  Under ℚ: every asset earns the risk-free rate r.
  "As if" investors are risk-neutral.

RISK-NEUTRAL PRICING FORMULA:
  V(S,t) = e^{-r(T-t)} · E^ℚ[payoff(S_T)]

  Call: C = e^{-rT} E^ℚ[max(S_T - K, 0)]
            = e^{-rT} ∫₀^∞ max(s-K,0) · f^ℚ(s) ds
            = S·N(d₁) - K·e^{-rT}·N(d₂)  ← Black-Scholes formula ✓

WHY THIS WORKS:
  Fundamental theorem of asset pricing (Harrison-Pliska 1979):
  No arbitrage ⟺ ∃ equivalent martingale measure ℚ
  Unique ℚ ⟺ complete market (every payoff replicable)
  Black-Scholes: unique ℚ (complete market by Δ-hedging)

THE DRIFT μ CANCELS OUT:
  S_T/S_0 under ℚ is lognormal with drift r, variance σ²T.
  The actual drift μ irrelevant for pricing (but not for hedging P&L)!
```

---

## The Greeks

Sensitivities of option value to its parameters:

```
GREEK    SYMBOL  DEFINITION                INTERPRETATION            SIGN
───────  ──────  ─────────────────────     ──────────────────────    ──────
Delta    Δ       ∂V/∂S                     Shares to hold in hedge   Call: 0<Δ<1
                                                                      Put: -1<Δ<0
Gamma    Γ       ∂²V/∂S²                   Rate of change of Δ       Always > 0
                 = ∂Δ/∂S                   (option nonlinearity)     (long option)

Theta    Θ       ∂V/∂t                     Time decay (per day)      Usually < 0
                                           Long option loses time      (long option)
                                           value as T decreases

Vega     ν       ∂V/∂σ                     Sensitivity to volatility Always > 0
                 (not a Greek letter!)     Long option = long vega    (long option)

Rho      ρ       ∂V/∂r                     Sensitivity to rate       Call > 0
                                                                      Put < 0

Vanna    ∂Δ/∂σ  Cross-sensitivity         Delta hedge changes with σ
Volga    ∂ν/∂σ  Convexity in volatility
```

### BSM Greek Formulas

```
For a European call with d₁, d₂ as defined above, n = N'(d) = standard normal PDF:

  Δ_call = N(d₁)
  Γ = n(d₁) / (Sσ√T)    (same for call and put by put-call parity)
  Θ_call = -Sn(d₁)σ/(2√T) - rKe^{-rT}N(d₂)
  ν = S√T · n(d₁)         (same for call and put)

P&L DECOMPOSITION (Δ-hedged position):
  P&L ≈ ½Γ(ΔS)² + Θ·Δt + ν·Δσ + ...

  Gamma P&L:  ½Γ(ΔS)² > 0  (always positive for long option!)
  Theta P&L:  Θ·Δt < 0     (cost of holding long option)
  Tradeoff: buying gamma costs theta — core options trading dynamic
```

---

## Implied Volatility and the Vol Surface

```
IMPLIED VOLATILITY:
  V_BS(S, K, T, r, σ_impl) = V_market
  Solve for σ_impl numerically (no closed form)

  σ_impl ≠ historical volatility (realized vol)
  σ_impl > realized vol on average (vol risk premium)
  VIX index ≈ 30-day implied vol on S&P 500

VOLATILITY SMILE / SKEW:
  Black-Scholes assumes constant σ — empirically false!

  Equity vol skew: OTM puts > ATM > OTM calls
    (fear of crashes → put demand → high put IV)

  FX vol smile: OTM options more expensive on both sides
    (tail risk symmetric → both tails expensive)

VOL SURFACE: σ_impl(K, T)
  Strike axis:    moneyness K/S or log-moneyness
  Maturity axis:  calendar time T

  TERM STRUCTURE of vol: usually upward sloping (uncertainty grows with T)
  SKEW: slope across strikes (typically negative for equity)

STOCHASTIC VOL MODELS (beyond BSM):
  Heston (1993): σ follows CIR process (mean-reverting, correlated with S)
  SABR:          Widely used for rates; σ follows GBM correlated with S
  Local vol:     σ = σ(S,t) — Dupire's formula; no-arbitrage consistent surface
```

---

## American Options and Early Exercise

```
AMERICAN vs EUROPEAN:
  American call on non-dividend-paying stock = European call (Merton 1973)
    No incentive to exercise early (interest earned on K + lost upside)

  American put: early exercise can be optimal
    Exercise when S ≤ S* (free boundary) → exercise to get K immediately
    American put > European put always

BINOMIAL TREE (CRR model, Cox-Ross-Rubinstein 1979):
  Discretize: at each step, S → Su (up) or Sd (down)
  u = e^{σ√Δt},  d = 1/u
  Risk-neutral prob: p = (e^{rΔt} - d)/(u-d)

  Price recursively: at expiry, set payoff
                     backward: V[i] = max(early exercise, e^{-rΔt}(p·V_up + (1-p)·V_down))

  American option: compare continuation value vs intrinsic value at each node
```
<!-- @editor[content/P2]: American options section is thin — missing Longstaff-Schwartz (LSM) Monte Carlo method, which is the industry standard for pricing American/Bermudan options in multiple dimensions -->

---

## Forwards, Futures, and Swaps

```
FORWARD:
  Agreement to buy/sell S at price F = S·e^{(r-q)T} at time T
  q = dividend yield (or convenience yield for commodities)
  No premium at initiation; value drifts as S changes
  Forward value: V = (F - K)e^{-rT}  where K = contracted price

FUTURES:
  Exchange-traded forward with daily mark-to-market (margining)
  F_futures ≈ F_forward for deterministic rates (identical if r non-stochastic)
  Basis risk: futures vs spot spread

INTEREST RATE SWAP:
  Exchange fixed rate (coupon) for floating rate (SOFR)
  Notional N, fixed rate c, floating rate L[i], payment dates {t_i}

  Fixed leg PV: c·N·Σ e^{-r_i·t_i}·(t_i - t_{i-1})
  Float leg PV: N(1 - e^{-r_T·T})  (= par minus discounted notional)

  At initiation: fixed rate c set so PV(fixed) = PV(floating)
    → c = swap rate = par yield for that maturity

  Used to: convert fixed rate debt to floating (or vice versa), hedge rate risk
```

---

<!-- @editor[content/P2]: Credit derivatives (CDS, CDO tranching, correlation trading) only mentioned in passing — deserves its own subsection given 2008 crisis relevance and mathematical depth -->

## Decision Cheat Sheet

| Task | Method |
|------|--------|
| Price European call/put | Black-Scholes formula |
| Get delta hedge ratio | Δ = N(d₁) for call |
| Check if option is mispriced | Compare implied vol vs expected realized vol |
| Price American put | Binomial tree with early exercise check |
| Account for discrete dividends | Adjust F: S₀ - PV(dividends) |
| Price exotic (barrier, Asian) | Monte Carlo or PDE (finite difference) |
| Get all sensitivities at once | Greeks (Δ, Γ, Θ, ν) from BSM formulas |
| Model volatility skew | Heston, SABR, or local vol |
| Hedge against volatility moves | Vega hedging (trade options to neutralize ν) |
| Price an interest rate swap | Discount fixed and floating legs, set c at swap rate |

## Common Confusion Points

**The drift μ cancels in option pricing, but not in P&L.** Under ℚ, μ doesn't matter
for pricing. Under ℙ (real world), μ determines whether a delta-hedged position makes
money. A Δ-hedged call earns positive P&L when realized vol > implied vol.

**Implied vol ≠ forecast of future realized vol.** Implied vol includes a volatility
risk premium (~1-2 vol points) because sellers of volatility demand compensation for
bearing the risk. Trading vol means trading the gap between implied and realized.

**Black-Scholes is wrong but useful.** Constant vol, no jumps, no transaction costs —
all violated. But it gives a consistent quoting convention (everyone quotes in implied
vol) and a hedging framework. Extensions handle the violations.

**Gamma is always positive for long options; theta always negative.** Buying an option
means paying theta (daily time decay) to own positive gamma (convexity benefit from
large moves). This tradeoff is the core of options trading intuition.

**Put-call parity is a no-arbitrage constraint, not a model.** It holds regardless of
model (log-normal, jumps, stochastic vol). Violations in market prices indicate
transaction costs or dividends not modeled, not a "free lunch."
