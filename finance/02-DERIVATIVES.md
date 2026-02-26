# Derivatives — Options, Black-Scholes, Greeks, Risk-Neutral Pricing

## The Big Picture

Derivatives are contracts whose value derives from an underlying asset (stock, bond,
commodity, interest rate, index). The mathematics is stochastic calculus — Brownian
motion, Itô's lemma, and the risk-neutral pricing measure.

```
DERIVATIVE LANDSCAPE — STRUCTURAL RELATIONSHIPS:

FORWARDS (atomic building block):
  Agreement to exchange S for K at T. Linear payoff: V = S_T − K.
  Value today: V_0 = (F − K)e^{-rT}   where F = S_0 e^{(r-q)T}
        │
        ├─→ FUTURES: standardized forward + daily mark-to-market (margin)
        │    Economically identical if rates non-stochastic
        │
        └─→ SWAPS: portfolio of forwards at successive dates
               Interest rate swap = series of forward rate agreements (FRAs)
               Currency swap = series of FX forwards
               CDS = forward on default event

OPTIONS (adds optionality to the linear payoff):
  Payoff: max(S_T − K, 0)  (call) or max(K − S_T, 0)  (put)
  Black-Scholes prices European options in closed form
        │
        ├─→ AMERICAN OPTIONS: European + early exercise premium
        │    No closed form; priced by binomial tree or LSM Monte Carlo
        │
        ├─→ VANILLA PORTFOLIO: straddles, strangles, spreads, collars
        │    All built from puts + calls; model-free relationships (put-call parity)
        │
        └─→ EXOTICS (build additional structure on vanilla options):
               Path-dependent: Asian (avg price), Lookback (max/min), Barrier (knock-in/out)
               Digital/binary: cash-or-nothing, asset-or-nothing
               Compound options: option on an option
               Quanto: payoff in different currency from underlying
               Volatility products: variance swaps, VIX futures

STRUCTURED PRODUCTS (combine multiple instruments):
  CLO = securitization of leveraged loans; tranching redistributes credit risk
  CDO = securitization of bonds/CDS; tranches ranked by seniority
  Synthetic CDO = CDO referencing CDS instead of bonds (no actual loans needed)
  MBS = securitization of mortgage pool (see 03-FIXED-INCOME)
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
  Works well for 1-2 underlying assets; scales poorly to higher dimensions.

LONGSTAFF-SCHWARTZ (LSM) MONTE CARLO — industry standard for high-dimensional:
  Prices American/Bermudan options with multiple underlyings by Monte Carlo.
  Key insight: continuation value = E^ℚ[future cash flows | S_t, in-the-money]
  is estimated by cross-sectional regression on simulated paths at each exercise date.

  ALGORITHM:
  1. Simulate N paths of S_1,...,S_T under ℚ (all exercise dates)
  2. At final exercise date T: set value = intrinsic value max(S_T − K, 0)
  3. Work backward from T-1 to 0:
     At each date t:
       a. Select paths where option is in-the-money
       b. Regress discounted future cash flows on basis functions of S_t
          (polynomials: a₀ + a₁S_t + a₂S_t² + ... )
       c. Estimated continuation value Ĉ(S_t) = fitted value from regression
       d. Exercise if intrinsic value > Ĉ(S_t); otherwise continue
  4. Option price = discounted average of optimal exercise cash flows

  WHY IT WORKS:
  Least-squares regression estimates the conditional expectation E^ℚ[CV | S_t]
  This is the key quantity needed for optimal stopping (exercise when IV > E[CV])
  Convergence: O(N^{-1/2}) in paths; need N ≥ 10,000 for accuracy

  EXTENSIONS:
  Bermudan swaptions: same algorithm, S_t = swap rate, payoff = swap value
  Multi-asset basket options: basis functions include cross-terms S_i × S_j
  Callable bonds / MBS: standard tool for OAS computation

  COMPARISON:
  Binomial tree:  O(n³) in steps; scales poorly to d > 2 assets
  LSM Monte Carlo: O(N × T × d²) — handles d = 10-100 assets easily
  PDE (finite difference): O(n^d) in grid points — impractical for d > 3
```

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

---

## Credit Derivatives

### Credit Default Swap (CDS)

```
CDS = insurance contract on a reference entity's default.

STRUCTURE:
  Protection buyer:  pays periodic spread s (basis points × notional × time)
  Protection seller: pays (1 − R) × Notional at default if it occurs before T
  R = recovery rate (typically assumed 40% for investment grade)

PRICING (flat hazard rate λ, constant R):
  Survival probability to time t: Q(t) = e^{-λt}
  PV(premium leg) = s × N × Σᵢ Δtᵢ × e^{-(r+λ)tᵢ}
  PV(protection leg) = (1-R) × N × ∫₀ᵀ λ e^{-(r+λ)t} dt = (1-R)N × λ/(r+λ) × (1-e^{-(r+λ)T})

  At initiation: PV(premium) = PV(protection)
  CDS spread ≈ λ(1-R)   (approximate rule of thumb for short maturities)

INFORMATION CONTENT:
  CDS spread = market's risk-neutral expected loss rate
  Backed out λ: market-implied hazard rate from CDS price
  CDS vs bond spread: CDS is cleaner measure (no accrued interest, no liquidity premium)
  CDS-bond basis: CDS spread − bond Z-spread; should ≈ 0; deviations = relative value trade

USES:
  Hedge credit exposure (buy protection on counterparty)
  Speculate on credit quality (sell protection to earn carry)
  Index CDS (CDX IG, CDX HY, iTraxx): basket CDS on 125 names
```

### CDO Tranching and Correlation Trading

```
CDO (Collateralized Debt Obligation):
  Pool of risky assets (bonds, loans, or CDS) → tranched into notes by seniority

  WATERFALL:
  Senior (AAA):  first to be paid; last to absorb losses; low spread (~20-50bps)
  Mezzanine (BBB-A): absorbs losses after equity exhausted; medium spread (~200-400bps)
  Equity (0-3%): first-loss tranche; absorbs losses first; residual upside

  ATTACHMENT AND DETACHMENT:
  [0%, 3%)   Equity tranche:    loses first; typically retained by CDO manager
  [3%, 7%)   Junior mezz tranche
  [7%, 15%)  Senior mezz tranche
  [15%, 30%) Senior tranche
  [30%, 100%) Super-senior:     historically considered near-risk-free

GAUSSIAN COPULA MODEL (Li 2000, the infamous model):
  Default times: τᵢ ~ F_i (marginal default time for obligor i)
  Joint defaults modeled by Gaussian copula with correlation ρ:
    τᵢ = F_i^{-1}(Φ(√ρ M + √(1-ρ) Zᵢ))
    M = common factor; Zᵢ = idiosyncratic; both ~ N(0,1)

  Single-factor model → loss distribution computed analytically (or by recursion)
  Tranche price = E[tranche loss | correlation ρ]

  CORRELATION TRADING:
  Different tranches have different sensitivity to ρ:
    Equity tranche: SHORT correlation (more ρ → more joint defaults → equity wiped out)
    Senior tranche: LONG correlation (more ρ → joint defaults cluster; either all survive or all fail)
  "Correlation trader" = buy equity + sell senior → delta-neutral in ρ

  WHAT WENT WRONG (2008):
  Gaussian copula assumes Gaussian tails — zero tail dependence
  Housing defaults turned out to be highly correlated (common macro factor)
  The ρ implied by prices pre-crisis (~15-30%) was far below realized (~70-80%)
  Senior tranches priced as near-riskless turned out to be highly vulnerable
  Super-senior CDO tranches lost 30-80% of value
  Model was used to misprice trillions of dollars of structured credit

SYNTHETIC CDO:
  References basket of CDS instead of actual bonds
  No actual asset pool; pure credit risk transfer
  Allows leverage: sell protection on CDX index tranches
  2003-2007: explosive growth; enabled rapid credit exposure accumulation
```

---

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
