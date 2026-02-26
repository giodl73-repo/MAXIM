# Microeconomics — Markets, Equilibrium, Welfare

---

## Big Picture

```
AGENTS:

CONSUMERS                      FIRMS
maximize U(x₁,x₂)             maximize π = Revenue - Cost
subject to p₁x₁+p₂x₂ ≤ W     choose Q to maximize profit

      │                              │
      ▼                              ▼
  DEMAND CURVE                 SUPPLY CURVE
  x*(p₁,p₂,W)                 Q*(p, costs)

                  ↘       ↙
                MARKET EQUILIBRIUM
                Supply = Demand
                    │
                    ▼
              PRICES AND QUANTITIES
              Resource allocation
```

---

## Consumer Theory

### Preferences and Utility

```
PREFERENCE RELATION ≻ on bundle space X:
  x ≻ y: x strictly preferred to y
  x ~ y: indifferent
  x ≽ y: at least as good

AXIOMS (for "rational" preferences):
  Completeness: x ≽ y OR y ≽ x (can always compare)
  Transitivity: x ≽ y, y ≽ z → x ≽ z
  Continuity: {x: x ≽ y} is closed (technical)
  Monotonicity: more is better (≥ x component-wise → ≽)
  Convexity: mixtures preferred to extremes (convex indifference curves)

UTILITY FUNCTION: u: X → R representing ≽
  u(x) ≥ u(y) iff x ≽ y
  Exists under completeness + transitivity + continuity

ORDINAL: only ordering matters, not magnitude
  u and f(u) for any strictly increasing f represent same preferences
  → Cannot compare utility across people (interpersonal comparisons require cardinal utility)
```

### Utility Maximization

```
MAX u(x₁, x₂)   subject to: p₁x₁ + p₂x₂ = W   (budget constraint)

Lagrangian: L = u(x₁,x₂) - λ(p₁x₁ + p₂x₂ - W)

FOC: ∂u/∂x₁ = λp₁   →   MU₁/p₁ = MU₂/p₂ = λ
     ∂u/∂x₂ = λp₂

TANGENCY: MRS = p₁/p₂
  MRS (marginal rate of substitution) = |∂u/∂x₁| / |∂u/∂x₂|
  Slope of indifference curve = slope of budget line
  λ = marginal utility of income (Lagrange multiplier interpretation)

SOLUTIONS → Marshallian demand: x*(p₁, p₂, W)
  Demand curve: x₁*(p₁, p₂, W) as function of p₁
  Income expansion path: x*(p, W) as W increases
```

### Common Utility Functions

```
COBB-DOUGLAS: u = x₁^α x₂^β  (α+β=1 WLOG)
  MRS = (αx₂)/(βx₁)
  Demand: x₁* = αW/p₁,  x₂* = βW/p₂
  Spends fixed fractions α, β of income on each good
  Price elasticity: -1 (unit elastic)

PERFECT SUBSTITUTES: u = x₁ + x₂
  MRS = 1 → buy only cheaper good

PERFECT COMPLEMENTS: u = min(x₁, x₂)
  Always consume in fixed ratio → L-shaped indifference curves
  Demand: x₁* = x₂* = W/(p₁+p₂)

QUASI-LINEAR: u = v(x₁) + x₂ (x₂ = numeraire)
  No income effect on x₁: x₁*(p₁) doesn't depend on W
  Useful in theory: allows welfare analysis without distributional concerns

CES (Constant Elasticity of Substitution):
  u = [x₁^ρ + x₂^ρ]^{1/ρ}
  Elasticity of substitution: σ = 1/(1-ρ)
  ρ→1: perfect substitutes; ρ→-∞: perfect complements; ρ→0: Cobb-Douglas
```

### Demand and Elasticity

```
OWN-PRICE ELASTICITY:
  ε = (∂x/∂p) × (p/x)   (always ≤ 0 for normal goods)
  |ε| > 1: elastic (demand very responsive to price)
  |ε| < 1: inelastic (demand not responsive)
  |ε| = 1: unit elastic

INCOME ELASTICITY:
  η = (∂x/∂W) × (W/x)
  η > 0: normal good (demand increases with income)
  η > 1: luxury good
  η < 0: inferior good (demand decreases with income; e.g., cheap food)

CROSS-PRICE ELASTICITY:
  ε₁₂ = (∂x₁/∂p₂) × (p₂/x₁)
  ε₁₂ > 0: substitutes (higher p₂ → more x₁)
  ε₁₂ < 0: complements (higher p₂ → less x₁)

SLUTSKY EQUATION:
  ∂x/∂p = (∂h/∂p)|_{utility} - x × ∂x/∂W
  Total price effect = Substitution effect (move along IC) + Income effect

GIFFEN GOOD: ε > 0 (demand increases with price!)
  Requires strongly inferior good (income effect > substitution effect)
  Irish potato famine example: potatoes so inferior that price rise → eat more potatoes
```

---

## Producer Theory

### Production Function

```
f(K, L) = output (given capital K and labor L)

RETURNS TO SCALE:
  f(tK, tL) = t·f(K,L): constant returns (CRTS)
  f(tK, tL) > t·f(K,L): increasing returns (IRS) → natural monopoly
  f(tK, tL) < t·f(K,L): decreasing returns (DRS) → diseconomies of scale

MARGINAL PRODUCT: MP_K = ∂f/∂K, MP_L = ∂f/∂L
MARGINAL RATE OF TECHNICAL SUBSTITUTION: MRTS = MP_L/MP_K
  = slope of isoquant = rate at which K substitutes for L to keep output constant

COBB-DOUGLAS: f = K^α L^{1-α}
  MP_K = αK^{α-1}L^{1-α} = α(f/K)   (∝ average product)
  MRTS = [(1-α)/α] × (K/L)
  Returns: α+(1-α) = 1 → CRTS
```

### Cost Minimization

```
MIN w_K K + w_L L   subject to f(K,L) = Q

FOC: MP_L/w_L = MP_K/w_K   (MRTS = factor price ratio)

COST FUNCTION: C(Q, w_K, w_L) = min cost to produce Q

MARGINAL COST: MC = ∂C/∂Q
AVERAGE COST: AC = C/Q
AVERAGE VARIABLE COST: AVC = VC/Q (exclude fixed cost)

COST CURVES:
  U-shaped AC: Initially falls (fixed cost spread over Q), then rises (diminishing MP)
  MC intersects AC at AC minimum
  Short run: capital fixed → diminishing returns → MC rises
  Long run: all inputs variable → constant or decreasing AC possible
```

### Profit Maximization

```
MAX π = p·Q - C(Q)

FOC: p = MC   (price = marginal cost)
  Marginal revenue of last unit = marginal cost of producing it

COMPETITIVE FIRM: price-taker → MR = p
  Profit-maximizing: produce at Q* where MC(Q*) = p
  Supply curve = MC curve above AVC (shutdown if p < AVC)

LONG-RUN COMPETITIVE EQUILIBRIUM:
  Entry/exit until π = 0 (zero profit condition)
  P = MC = AC (minimum efficient scale)
  All firms earn normal return; no excess profit
```

---

## Market Equilibrium

### Competitive Equilibrium

```
SUPPLY: Q_S = S(p)  (upward sloping: higher p → more production)
DEMAND: Q_D = D(p)  (downward sloping: higher p → less consumption)
EQUILIBRIUM: Q_S = Q_D at price p*

FIRST WELFARE THEOREM:
  Competitive equilibrium is Pareto efficient
  (cannot make anyone better off without making someone worse off)
  Conditions needed: no externalities, no market power, complete markets, full information

SECOND WELFARE THEOREM:
  Any Pareto efficient allocation can be achieved by competitive equilibrium
  with appropriate lump-sum transfers (redistribute endowments, let market allocate)
  → Efficiency and distribution can be separated in principle (not in practice)
```

### Welfare Measures

```
CONSUMER SURPLUS: CS = ∫₀^{Q*} [D(Q) - p*] dQ = area under demand, above price

PRODUCER SURPLUS: PS = ∫₀^{Q*} [p* - S(Q)] dQ = area above supply, below price

TOTAL SURPLUS (SOCIAL WELFARE): W = CS + PS

DEADWEIGHT LOSS: W_max - W(policy) = efficiency loss from distortions

TAX INCIDENCE:
  Per-unit tax t → shifts supply up by t → new equilibrium
  Price buyers pay: p_b = p* + t × E_S/(E_S + |E_D|)
  Price sellers receive: p_s = p* - t × |E_D|/(E_S + |E_D|)
  Incidence borne by side with less elastic demand/supply
  (Inelastic side cannot avoid the tax by changing quantity)
```

---

## Market Power

### Monopoly

```
MONOPOLIST: price-setter → MR < p (must lower price on all units to sell more)

MR = p + Q × (dp/dQ) = p[1 + 1/ε]   (ε = own-price elasticity, negative)

Profit max: MR = MC → p[1 + 1/ε] = MC

LERNER INDEX: (p - MC)/p = -1/ε = 1/|ε|
  Measures markup over marginal cost
  L = 0: competitive; L > 0: market power

DEADWEIGHT LOSS: Monopolist restricts output below competitive Q*
  → Rectangle of lost surplus (buyer's willingness > MC but no trade)

PRICE DISCRIMINATION:
  1st degree: charge each customer their WTP → zero CS, no DWL (perfect info required)
  2nd degree: quantity discounts, versioning → partial discrimination (self-selection)
  3rd degree: different prices for different groups (students, seniors, geography)
              → increases output to low-value groups, reduces to high-value; may increase welfare
```

### Network Effects and Platforms

```
TWO-SIDED MARKETS (Rochet-Tirole):
  Platform serves two groups (buyers and sellers, drivers and riders)
  Externality: each side benefits from size of other side
  Pricing: may subsidize one side heavily (charge the other side)
  Chicken-and-egg: need both sides simultaneously → first-mover advantage

NETWORK EFFECTS:
  Direct: more users of same product = more valuable (fax machines, phones)
  Indirect: more sellers → cheaper → more buyers → more sellers (platforms)

WINNER-TAKE-ALL: Network effects + economies of scale → concentrated markets
  Switching costs: multi-homing reduces lock-in
  Antitrust tension: scale necessary for efficiency but creates monopoly power
```

---

## Information Economics

### Adverse Selection

```
AKERLOF "MARKET FOR LEMONS" (1970, Nobel 2001):

Setup: Used cars of quality q ~ Uniform[0,1]
  Seller knows q; buyer doesn't → buyer pays expected value
  Seller only sells if price ≥ q (opportunity cost)

At price p: only cars with q ≤ p sell → E[q|sell] = p/2 < p
Buyer's WTP: E[q|sell] × 1.5 = 0.75p (assume buyer values at 1.5× seller)
Equilibrium: p = 0.75p → p = 0 (market collapses!)

GENERAL: Information asymmetry can destroy mutually beneficial trade
  Bad quality drives out good (adverse selection by informed party)

SOLUTIONS:
  Screening: uninformed party designs contract menu (insurance: deductibles)
  Signaling: informed party credibly signals type (education, warranties)
  Certification: third party verifies quality (CARFAX, doctors board certification)
  Government mandate: make everyone participate (health insurance mandate → ACA)
```

### Moral Hazard

```
SETUP: After contract, agent takes hidden action that affects outcome
  Principal (employer/insurer) cannot observe agent's effort
  Agent's effort is costly → may shirk under full insurance

PRINCIPAL-AGENT PROBLEM:
  Agent: max U(w) - c(e)   (utility of wage - cost of effort e)
  Principal: max E[y(e)] - E[w]  (expected output - expected wage)
  Optimal contract: balance risk-sharing vs incentive provision

  First-best (observable effort): risk-neutral agent bears all risk, max effort
  Second-best (unobservable effort): partial insurance + incentive pay
  → Higher-powered incentives (bonuses, equity) → more effort, more agent risk
  → Tension: risk-averse agent dislikes variance, so pure performance pay is inefficient

EXAMPLES:
  Health insurance: fully insured patients consume more care (moral hazard)
  Flat-fee software consulting: developer may deliver minimum viable
  Manager equity: stock options align incentives (but volatility also borne by mgr)
  Banking: "too big to fail" guarantee → excessive risk-taking (systemic moral hazard)
```

### Signaling (Spence)

```
SETUP: Workers have ability θ ∈ {H, L}; firms can't observe θ
  Education e: costly for all, more costly for low types (c(e,H) < c(e,L))

SEPARATING EQUILIBRIUM:
  High type chooses e* such that low type would not mimic:
  w(H) - c(e*,H) ≥ w(L)    (high type benefits from education)
  w(H) - c(e*,L) < w(L)    (low type would not mimic)

  → Education as pure signal (content irrelevant, just costly)
  → Separating equilibrium if e* ∈ [(w(H)-w(L))/c_L, (w(H)-w(L))/c_H]

POOLING EQUILIBRIUM: All types choose same education
  → Cannot distinguish types; wage = E[θ]

HUMAN CAPITAL vs PURE SIGNAL debate:
  Pure signal (Spence): education has zero productivity value, just sorts
  Human capital (Mincer): education genuinely raises productivity
  Reality: probably both (credential + skill formation)
  Policy implication: if pure signal, subsidizing education is wasteful
```

---

## Externalities and Market Failures

```
EXTERNALITY: cost or benefit to third party not in the transaction
  Negative: carbon emissions, noise, congestion, overuse of antibiotics
  Positive: vaccination, research spillovers, infrastructure

PIGOUVIAN CORRECTION:
  Tax negative externalities by the social cost: t = MEC (marginal external cost)
  Subsidy positive externalities by the social benefit
  → Forces private decisions to internalize social cost
  Carbon tax: t = social cost of carbon (~$50-200/tonne CO₂)

COASE THEOREM (1960):
  If property rights are well-defined and transactions are costless,
  private bargaining leads to efficient outcome regardless of initial assignment.
  → No need for regulation if bargaining is possible
  REAL WORLD: transaction costs exist, property rights often unclear
  Coase = useful theoretical baseline, not always practical prescription

PUBLIC GOODS: non-rival + non-excludable
  Non-rival: consumption by one doesn't reduce availability to others (broadcast TV)
  Non-excludable: cannot prevent non-payers from consuming
  FREE RIDER PROBLEM: everyone waits for others to provide public good
  → Government provision, Lindahl prices, assurance contracts (mechanism design solutions)

COMMON POOL RESOURCES (TRAGEDY OF THE COMMONS):
  Non-excludable, rival (fisheries, groundwater, highway congestion)
  Overuse without governance → Hardin (1968)
  Solutions: Privatize (assign property rights), Regulate (quotas), Ostrom institutions
  Ostrom (Nobel 2009): community governance can solve commons without privatization
```

---

## Decision Cheat Sheet

| Situation | Model | Key Result |
|-----------|-------|------------|
| Competitive market | Supply = Demand | P = MC, Pareto efficient |
| Monopoly | MR = MC | P > MC, deadweight loss |
| Asymmetric info (quality) | Lemons model (Akerlof) | Market may collapse; certification helps |
| Hidden effort | Principal-agent | Incentive pay trades off risk and effort |
| Costly signal | Spence signaling | Separating equilibrium; education may be pure signal |
| Externality | Pigouvian tax | Set t = marginal external cost |
| Public good | Free rider problem | Government provision or mechanism design |
| Common pool | Tragedy of commons | Quotas, property rights, or Ostrom institutions |
| Price discrimination | 1st/2nd/3rd degree | 1st = efficient, eliminates CS; 3rd = market segmentation |

---

## Common Confusion Points

**Giffen good vs inferior good**: All Giffen goods are inferior, but not all inferior goods are Giffen. An inferior good has negative income elasticity (η < 0): demand falls as income rises. A Giffen good additionally requires the income effect to swamp the substitution effect so strongly that demand *rises* when price rises (ε > 0). Requires: good is strongly inferior, large budget share, no close substitutes. Empirically rare; Irish potato famine is the canonical near-example.

**Normal profit vs zero profit**: "Zero economic profit" in long-run competitive equilibrium means firms earn exactly their opportunity cost — they are covering all costs including the normal return on capital. This is not zero accounting profit. Normal profit = the return the firm's owners could earn in their next-best use of capital. Economic profit = accounting profit − opportunity cost. Long-run competitive equilibrium drives economic profit → 0, not accounting profit.

**MRS vs MRTS**: MRS (marginal rate of substitution) = |∂u/∂x₁| / |∂u/∂x₂| — slope of indifference curve in consumption space; how much of good 2 a consumer gives up for one more unit of good 1. MRTS (marginal rate of technical substitution) = MP_L/MP_K — slope of isoquant in production space; how much capital a firm gives up for one more unit of labor holding output fixed. Same mathematical structure, different economic context.

**Short-run vs long-run supply**: Short run: at least one input (typically capital) is fixed. Supply curve = MC curve above AVC (shutdown point). Long run: all inputs variable; entry/exit drives economic profit to zero. The long-run supply curve in a competitive industry with constant input costs is *horizontal* at minimum AC — not upward sloping. Upward sloping long-run supply requires rising input prices as industry expands (increasing-cost industry).

**Consumer surplus vs utility**: Consumer surplus = area under demand curve above price = willingness to pay minus price actually paid. This is a monetary measure of welfare gain. Utility is an ordinal preference index — only differences in ordinal ranking matter, not the magnitude. CS approximates the compensating variation in welfare under quasi-linear preferences; otherwise there are income effects to worry about. CS and utility are related but not the same object.
