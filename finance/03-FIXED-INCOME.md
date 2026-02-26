# Fixed Income — Bonds, Yield Curves & Interest Rate Models

## The Big Picture

```
+------------------------------------------------------------------+
|                     FIXED INCOME LANDSCAPE                        |
+------------------------------------------------------------------+
|                                                                    |
|  INSTRUMENTS           VALUATION             RISK                  |
|  ────────────          ──────────            ──────               |
|  Treasury bonds        Discounted cash flow  Duration             |
|  Corporate bonds       Yield to maturity     Convexity            |
|  Municipal bonds       Spot rates vs        DV01                  |
|  MBS, ABS              yield curves         Key rate dur.         |
|  Swaps, FRAs           OAS for callables     Spread risk          |
|  Inflation-linked      Credit spread         Credit risk          |
|  Bond futures          Z-spread              Prepayment risk       |
|                                                                    |
|  TERM STRUCTURE MODELS                                             |
|  ─────────────────────────────────────────────────────────────   |
|  Vasicek, CIR (short rate) → Ho-Lee, Hull-White                  |
|  HJM (forward rate process) → LMM (LIBOR market model)           |
+------------------------------------------------------------------+
```

Fixed income = instruments that promise **fixed or formulaic cash flows**.
Valuation is about discounting — but *which* discount rate? The yield curve
is the central object: the market's consensus on discount rates across maturities.

---

## Bond Mechanics

### Cash Flow Structure

```
ZERO-COUPON BOND:
  Pays face value F at maturity T. No intermediate cash flows.
  Price: P = F · d(0,T)  where d(0,T) = discount factor

COUPON BOND:
  Pays coupon c·F at times t₁, t₂, ..., tₙ = T, plus F at T.
  c = annual coupon rate, F = face value (par)

  Price: P = Σᵢ₌₁ⁿ c·F·d(0,tᵢ) + F·d(0,T)

  Priced at par: P = F  ↔  coupon rate = yield to maturity
  Above par (premium): coupon > YTM
  Below par (discount): coupon < YTM

ACCRUED INTEREST:
  Between coupon dates, price = clean price + accrued interest
  Quoted price = clean price (flat price)
  Settlement price = dirty price = clean + accrued

CONVENTIONS (bond math is full of day-count nuance):
  Actual/Actual (ICMA): US Treasury
  30/360: US corporate bonds
  Actual/360: money market instruments
```

### Yield to Maturity (YTM)

```
YTM = internal rate of return assuming bond held to maturity,
      coupons reinvested at same rate.

P = Σᵢ₌₁ⁿ C/(1+y/m)^(m·tᵢ) + F/(1+y/m)^(m·T)

  y = YTM (annual),  m = coupon frequency per year (m=2 for semi-annual US)

No closed form — solve numerically (Newton's method on P(y)):
  P'(y) = −Σᵢ tᵢ · CFᵢ / (1+y)^(tᵢ+1)  = −P · Modified Duration

YTM is a single summary number. Its limitations:
  Assumes flat term structure (all cash flows discounted at same rate)
  Assumes coupons reinvested at YTM (rarely true)
  Better: price from spot curve, then back out YTM as summary metric
```

---

## The Yield Curve

```
SPOT RATE (zero coupon rate) r(T):
  Yield on zero-coupon bond maturing at T.
  d(0,T) = e^{-r(T)·T}  (continuous) or  1/(1+r_semi)^T (semi-annual)
  Spot curve = r(T) as function of T.

FORWARD RATE f(T₁,T₂):
  Rate locked in today for borrowing from T₁ to T₂:
  d(0,T₁) · e^{-f(T₁,T₂)·(T₂-T₁)} = d(0,T₂)
  Instantaneous forward: f(T) = −d ln d(0,T)/dT = r(T) + T·r'(T)

PAR RATE c(T):
  Coupon rate at which a coupon bond prices at par.
  c(T) = [1 − d(0,T)] / Σᵢ d(0,tᵢ)  (annuity factor)

YIELD CURVE SHAPES:
  Normal (upward sloping): shorter rates < longer rates — typical
  Inverted (downward): short > long — recession predictor
  Flat: similar rates across maturities
  Humped: intermediate maturities highest — transition

BOOTSTRAP — extracting spot curve from coupon bonds:
  1. 3m, 6m: already zero-coupon (T-bills) → spot rates directly
  2. 2yr bond: P = c·d(0.5) + c·d(1.0) + (100+c)·d(1.5) → solve for d(1.5)
     given d(0.5), d(1.0) from step 1
  3. Continue: each new maturity uses all previously computed spot rates.
```

---

## Duration and Convexity

Duration measures interest rate sensitivity — the "delta" of a bond:

### Modified Duration

```
MACAULAY DURATION (weighted avg time to cash flows):
  D_Mac = (1/P) · Σᵢ tᵢ · PV(CFᵢ)
        = Σᵢ tᵢ · [CFᵢ/(1+y)^tᵢ] / P   (semi-annual: adjust for frequency)

  INTERPRETATION: bond with D_Mac = 5 years has same price sensitivity as
  a 5-year zero-coupon bond.

MODIFIED DURATION:
  D_mod = D_Mac / (1 + y/m)   (adjusts for yield convention)

  ΔP/P ≈ −D_mod · Δy           (first-order price sensitivity)
  ΔP ≈ −D_mod · P · Δy

DOLLAR DURATION (DV01 — dollar value of 1bp = 0.0001):
  DV01 = D_mod · P / 10,000
  ΔP ≈ −DV01 · (Δy in bps)

PROPERTIES:
  Zero coupon bond: D_Mac = T exactly (one cash flow)
  Coupon bond: D_Mac < T (coupons paid earlier)
  Higher coupon → shorter duration
  Higher yield → shorter duration (higher PV weight on nearer CFs)

PORTFOLIO DURATION:
  D_port = Σᵢ wᵢ · Dᵢ  where wᵢ = market value weight
```

### Convexity

Duration is first-order. Convexity is the second-order correction:

```
Taylor expansion of bond price vs yield:
  ΔP/P ≈ −D_mod · Δy + ½ · Conv · (Δy)²

CONVEXITY:
  Conv = (1/P) · d²P/dy²
       = (1/P) · Σᵢ tᵢ(tᵢ+1) · PV(CFᵢ) / (1+y)²    (annual compounding)

  Always positive for non-callable bonds — convexity is good!
  For same duration, higher convexity → better price performance in both directions.

CALLABLE BOND: negative convexity when rates fall
  (issuer calls → cap on price appreciation)
  Effective duration = duration accounting for optionality
  OAS (Option-Adjusted Spread) = spread after removing optionality

IMMUNIZATION:
  Match asset duration to liability duration → portfolio insensitive to yield shifts.
  Requires periodic rebalancing (duration drifts over time).
  Full immunization: also match convexity (protects against large moves).
```

---

## Term Structure Models

### Short Rate Models

Model the instantaneous short rate r(t) as a stochastic process:

```
VASICEK (1977):
  dr = κ(θ − r)dt + σ dW   (Ornstein-Uhlenbeck process)

  κ = mean reversion speed, θ = long-run mean, σ = volatility
  Bond price: P(t,T) = A(t,T) e^{-B(t,T)r(t)}   (affine model)
  B(t,T) = (1 − e^{-κ(T-t)})/κ
  A(t,T) = exp[(θ − σ²/2κ²)(B − (T-t)) − σ²B²/4κ]

  Problem: r can go negative (OK for some currencies; problematic for others)

COX-INGERSOLL-ROSS (CIR, 1985):
  dr = κ(θ − r)dt + σ√r dW  (square-root diffusion)

  r stays positive if 2κθ > σ² (Feller condition)
  Bond price: still affine P(t,T) = A(t,T) e^{-B(t,T)r(t)}
  Closed-form cap/floor pricing.

HO-LEE (1986):
  dr = θ(t)dt + σ dW          (no mean reversion, time-varying drift)
  θ(t) calibrated to match initial yield curve exactly.
  First arbitrage-free model — can fit observed term structure.

HULL-WHITE (1990):
  dr = [θ(t) − κr]dt + σ dW   (generalization of Vasicek + Ho-Lee)
  θ(t) calibrated to initial forward curve.
  Most widely used for derivatives pricing.
  Trinomial tree or Monte Carlo implementation.
```

### HJM Framework

Model the entire forward curve:

```
HEATH-JARROW-MORTON (1992):
  df(t,T) = α(t,T)dt + σ(t,T)dW(t)
  f(t,T) = instantaneous forward rate at time t for maturity T

  No-arbitrage: α(t,T) = σ(t,T) ∫ₜᵀ σ(t,s)ds   (HJM drift condition)
  → drift is determined by volatility structure (drift restriction)

  Special cases:
    Constant σ → Ho-Lee
    σ e^{-κ(T-t)} → Hull-White
    HJM allows non-Markovian dynamics (path-dependent)

LIBOR MARKET MODEL (LMM / BGM):
  Model LIBOR rates L(t, Tᵢ, Tᵢ₊₁) directly (market-observable)
  dL(t,Tᵢ,Tᵢ₊₁) = μᵢ(t)L dt + σᵢ(t)L dWᵢ

  Log-normal → Black formula for caps/floors exact (industry standard)
  Swaption pricing: approximate (Rebonato formula for swap vol)
  Monte Carlo friendly; used for complex interest rate derivatives
```

---

## Credit Spreads and Default Risk

```
CREDIT SPREAD:
  Yield spread over risk-free rate: s = y_bond − y_treasury
  Decomposition: s ≈ default spread + liquidity spread + convexity adj.

INTENSITY MODEL (reduced-form):
  Default arrives as Poisson process with hazard rate λ (t):
  P(survive to T) = e^{−∫₀ᵀ λ(t)dt}
  Risky bond price: P = Σ CFᵢ · e^{−∫₀^{tᵢ}(r(t)+λ(t))dt}
  For constant λ: spread ≈ λ (approximately)

  CDS (Credit Default Swap):
    Protection buyer pays spread s each period until default or maturity
    Protection seller pays (1−R)·F at default (R = recovery rate, typical 40%)
    Equilibrium: PV(premium leg) = PV(protection leg)
    CDS spread ≈ λ(1−R)  (for constant hazard rate)

  Z-SPREAD: flat spread added to Treasury spot curve to price risky bond
  OAS: option-adjusted spread = Z-spread net of embedded option value

STRUCTURAL MODEL (Merton 1974):
  Firm equity = call option on firm assets A with strike = debt D:
  E = A·N(d₁) − D·e^{-rT}·N(d₂)
  Default at maturity if A < D.
  Allows inferring default probability from equity prices + leverage.
```

---

## Interest Rate Risk Management

```
HEDGING A BOND POSITION:
  Hedge DV01 exposure using:
  - Treasury futures (most liquid)
  - Interest rate swaps
  - Key rate duration matching (hedge each maturity bucket)

INTEREST RATE SWAP:
  Fixed-for-floating: pay fixed K, receive LIBOR (now SOFR)
  Value to fixed-payer: V = P_float − P_fixed
  Duration: D_swap ≈ D_float − D_fixed  (approximately −D_fixed for at-market swap)
  Swap rate S = coupon making V = 0 = par rate for that maturity

YIELD CURVE RISK:
  Parallel shift: DV01, duration — captures most risk
  Steepening/flattening: key rate durations at 2yr, 5yr, 10yr, 30yr
  Curvature: butterfly risk (short position on intermediate vs wings)

KEY RATE DURATION (KRD):
  Sensitivity to shift in one specific maturity (e.g., 10yr) holding others fixed.
  Σ KRDᵢ = Total Duration (approximately)
  Used to hedge non-parallel yield curve moves.

PRINCIPAL COMPONENTS (PCA on yield curve):
  PC1: parallel shift (~90% of variance)
  PC2: slope change (~8%)
  PC3: curvature (~2%)
  Hedge using PC1 and PC2 captures most yield curve risk.
```

---

## Mortgage-Backed Securities

```
MBS = POOL OF MORTGAGES (example: FNMA pass-through)
  Cash flows: principal + interest from pool of mortgages
  Prepayment risk: borrowers refinance when rates fall → extension/contraction risk

PREPAYMENT MODELS:
  PSA (Public Securities Association): benchmark speeds
  CPR (Conditional Prepayment Rate): annualized prepayment rate
  100 PSA = 6% CPR in month 30+, ramps from 0% to 6% in months 1–30

NEGATIVE CONVEXITY:
  When rates fall: prepayments increase → bonds shorten (worse for longs)
  When rates rise: prepayments decrease → bonds lengthen (worse for longs)
  MBS has negative convexity unlike agency bullet bonds

CMO (COLLATERALIZED MORTGAGE OBLIGATION):
  Tranches with different prepayment priority:
  PAC (Planned Amortization Class): stable cash flows over range of prepayment speeds
  TAC: protected against prepayment in one direction
  Z-bond: zero coupon; receives cash last (long duration, highest convexity)

OAS PRICING:
  Model option-adjusted spread via Monte Carlo of rate paths + prepayment model.
  OAS removes optionality → compare fair value across MBS.
```

---

<!-- @editor[content/P2]: Inflation-linked bonds (TIPS) appear in landscape diagram ("Inflation-linked") but have no drill-down — real yield vs nominal yield, breakeven inflation rate missing -->
<!-- @editor[content/P2]: Repo markets absent — repurchase agreements are fundamental to fixed-income funding, short selling, and the plumbing of bond markets -->
<!-- @editor[bridge/P2]: No old-world bridge — e.g., DCF from corporate finance maps directly to bond pricing; bootstrap is iterative dependency resolution (familiar pattern from build systems or topological sort) -->

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why do bond prices fall when yields rise? | P = Σ CF/(1+y)^t — higher denominator → lower price |
| What's the most important risk metric for bond? | DV01 (dollar value of 1 basis point) |
| How do I hedge interest rate risk? | Match DV01 with Treasury futures or swaps |
| What's duration of a zero coupon bond? | Exactly T years (Macaulay duration = maturity) |
| Why does convexity matter? | Second-order effect; positive convexity = gains more/loses less |
| What model for interest rate derivatives? | Hull-White (simple, widely used) or LMM (caps/swaptions) |
| How to extract spot rates? | Bootstrap from Treasury prices |
| What's OAS vs Z-spread? | OAS removes embedded option value; Z-spread doesn't |
| What's CDS spread approximately? | ≈ λ(1−R) where λ = hazard rate, R = recovery |

---

## Common Confusion Points

**"Yield curve is a graph of bond yields"** — technically yes, but *which*
yields? The par curve (coupon bond yields), spot curve (zero-coupon yields),
and forward curve all look different. Discount to spot rate always; the
others are derived quantities.

**"Duration = time to maturity"** — only for zero-coupon bonds. Coupon
bonds have duration less than maturity because coupon payments arrive earlier.
High-coupon bonds have shorter duration than low-coupon bonds of same maturity.

**"Negative convexity is rare"** — MBS, callable bonds, and many structured
products exhibit negative convexity. Mortgage portfolios held by banks are
full of it.

**"LIBOR is still used"** — LIBOR was discontinued June 2023. Replaced by
SOFR (Secured Overnight Financing Rate) in the US. LMM models are being
updated to SOFR market models (risk-free rate models).

**"Higher duration = always worse"** — depends on directional view. If
rates will fall, high duration bonds gain more. Duration is risk and opportunity.
