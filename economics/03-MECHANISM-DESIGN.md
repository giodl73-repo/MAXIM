# Mechanism Design — Designing the Rules of the Game

---

## Big Picture

```
GAME THEORY: given the rules, what will rational players do?
MECHANISM DESIGN: design the rules to achieve desired outcome

SETTING:
  Social planner wants outcome f(θ₁,...,θₙ)
  But types θᵢ are PRIVATE to each agent
  Planner must elicit types and implement outcome

CHALLENGE: Agents have incentives to lie about their types
  if lying leads to better outcomes for them

SOLUTION: Incentive-Compatible (IC) mechanisms
  Design rules such that telling the truth is optimal for every agent

REVELATION PRINCIPLE:
  For any mechanism, there exists a direct mechanism (just report type)
  that implements the same outcomes and is incentive-compatible.
  → Only need to consider direct, truthful mechanisms.
```

---

## Revelation Principle

```
DIRECT MECHANISM: agents report their types; mechanism implements outcome
  (mechanism = game form + outcome function)

DOMINANT STRATEGY IC (DSIC): truth-telling dominant strategy regardless of others' types
  For all i, all θᵢ, θᵢ', θ₋ᵢ:
  uᵢ(f(θᵢ, θ₋ᵢ), θᵢ) ≥ uᵢ(f(θᵢ', θ₋ᵢ), θᵢ)

BAYESIAN IC (BIC): truth-telling optimal in expectation over others' types
  For all i, all θᵢ, θᵢ':
  E_{θ₋ᵢ}[uᵢ(f(θᵢ, θ₋ᵢ), θᵢ)] ≥ E_{θ₋ᵢ}[uᵢ(f(θᵢ', θ₋ᵢ), θᵢ)]

REVELATION PRINCIPLE: If mechanism M implements outcome f,
  ∃ direct DSIC (or BIC) mechanism implementing same f.
  → Search over direct mechanisms sufficient (enormously simplifies design)
```

---

## Auctions

### Second-Price (Vickrey) Auction

```
RULE: Highest bidder wins; pays SECOND-highest bid.

TRUTH-TELLING IS DOMINANT STRATEGY:

Case 1: Your valuation v = $100, highest other bid b₂.

  If you win (bid > b₂): pay b₂ (not your bid)
  → Bidding v ensures you win whenever v > b₂ → no reason to bid higher
  → If v < b₂, you want to lose → bidding v correctly makes you lose

  Case b₂ < v: Win no matter what (as long as bid > b₂)
    Bidding v: win, profit = v - b₂ > 0 ✓
    Bidding lower (say b₂ - 1): lose, profit = 0 < v - b₂ ✗

  Case b₂ > v: Lose no matter what (as long as bid < b₂)
    Bidding v: lose, profit = 0 ✓
    Bidding higher (say b₂ + 1): win, profit = v - b₂ < 0 ✗

  Case b₂ = v: tie → indifferent

  In ALL cases: bidding true valuation v is weakly dominant strategy ✓

REVENUE EQUIVALENCE THEOREM:
  In symmetric IPV auctions with increasing equilibrium strategies,
  all auction formats yield same expected revenue (under risk-neutrality):
  E[Revenue(Second-price)] = E[Revenue(First-price)] = E[second-highest valuation]
```

### First-Price (Sealed-Bid) Auction

```
RULE: Highest bidder wins; pays their own bid.

TRUTH-TELLING IS NOT OPTIMAL:
  If you bid v, profit = 0 (pay exactly what it's worth)
  → Shade bid below valuation to get positive profit

SYMMETRIC BAYESIAN NE: vᵢ ~ F(v) on [0,1], N bidders
  Optimal bid: b*(v) = E[second-highest | all others below v]
             = v - ∫₀ᵛ F(t)^{N-1}/F(v)^{N-1} dt
  For Uniform[0,1]: b*(v) = v × (N-1)/N

  Example: N=2, v=0.8 → bid 0.4; v=1.0 → bid 0.5
  Higher N → bids closer to value (competition forces honest bidding)
```

### VCG Mechanism (Vickrey-Clarke-Groves)

The general social choice mechanism that achieves efficiency truthfully.

```
SETUP: N agents, outcome space X, type θᵢ privately known
  Social welfare: W(x, θ) = Σᵢ vᵢ(x, θᵢ)   (sum of agent values)

VCG RULE:
  1. Ask agents to report types θ̂
  2. Choose outcome: x*(θ̂) = argmax_x Σᵢ vᵢ(x, θ̂ᵢ)   (social welfare maximizing)
  3. Transfer to agent i: tᵢ(θ̂) = Σ_{j≠i} vⱼ(x*(θ̂), θ̂ⱼ) + hᵢ(θ̂₋ᵢ)
     where hᵢ is any function of other agents' reports (not agent i's)
     Clarke pivot rule: hᵢ = -max_{x} Σ_{j≠i} vⱼ(x, θ̂ⱼ)  (without i's contribution)

AGENT i's PAYMENT:
  Pays nothing extra; receives: tᵢ = (welfare of others with i) - (welfare of others without i)
  = externality agent i imposes on others (negative → i pays; positive → i receives)

INCENTIVE COMPATIBILITY: Truth-telling is dominant strategy
  Agent i reports θ̂ᵢ to maximize vᵢ(x*(θ̂), θᵢ) + tᵢ(θ̂)
  With VCG, this equals vᵢ + Σ_{j≠i} vⱼ = total social welfare → maximizing truth maximizes welfare

EXAMPLE (public project, N=2):
  Project costs $10. Values: v₁=7, v₂=4 → build (11>10).
  VCG: if θ̂₁=7, θ̂₂=4: build.
  Payment for agent 1: welfare of agent 2 with project = 4; without 1 (build only if 4>10) = 0
    t₁ = 4 - 0 = 4 (agent 1 pays 4)
    But agent 1 gets project worth 7: net = 7-4 = 3
  Payment for agent 2: welfare of agent 1 with project = 7; without 2 (build if 7>10) = 0
    t₂ = 7 - 0 = 7 but... agent 2 only gets value 4 → net = 4-7 = -3 (agent 2 is paid?)
  Wait: "pays" means Clarke rule: agent i pays the externality they impose
    Interpretation: agent i's payment = how much their presence changes the world for others
    Agent 1 causes project to happen (without 1, wouldn't build): externality = 4 - 0 = 4 → pay 4
    Agent 2's presence doesn't change decision (would build with 7>10): externality = 0 → pay 0

LIMITATIONS:
  Budget balance: transfers don't sum to zero in general (money may need to be destroyed)
  Computationally hard: finding optimal x* is NP-hard in combinatorial auctions
  Strategic: with budget constraints, bidders may collude to manipulate
```

### Sponsored Search Auctions (Google/Bing)

```
Setting: K ad slots with click-through rates α₁ ≥ α₂ ≥ ... ≥ αK
  Bidders have private values per click vᵢ, bid bᵢ
  Allocation: assign bidders to slots (highest bid gets best slot)
  Payment: Generalized Second Price (GSP) — each bidder pays next-highest bid

GSP IS NOT TRUTHFUL in one-shot game:
  → Not a dominant strategy to bid truthfully (strategic shading)
  BUT: under "locally envy-free" equilibrium concept, GSP ≈ VCG revenues
  VCG for search: each bidder pays the externality on lower bidders
  → Google actually uses a modified GSP that approximates VCG

QUALITY SCORE: Google multiplies bid by quality score (expected CTR × ad quality)
  → "Expected value bid" = bid × quality
  → Rewards relevant ads over irrelevant high-bids → better user experience
  → Can win top slot with lower bid if quality is higher
```

---

## Optimal Auction Design (Myerson 1981)

```
REVENUE MAXIMIZING AUCTION:
  N bidders, values vᵢ ~ Fᵢ (possibly different distributions)
  Goal: maximize expected revenue

VIRTUAL VALUATION: ψᵢ(v) = v - (1 - Fᵢ(v))/fᵢ(v)
  For regular distributions (ψ monotone increasing):
  Optimal mechanism: allocate to bidder with highest positive virtual valuation;
  charge each bidder the threshold at which their virtual valuation = 0

RESERVE PRICE:
  Single bidder: optimal to set reserve r* where ψ(r*) = 0
  i.e., r* - (1-F(r*))/f(r*) = 0
  For Uniform[0,1]: ψ(v) = 2v-1 = 0 → r* = 1/2
  → Seller sets $50 floor even if it risks no sale
  → Extracts surplus from high-type buyers

REVENUE vs EFFICIENCY:
  Vickrey (2nd price) = efficient (allocates to highest value) but not revenue-optimal
  Myerson optimal auction = revenue-optimal but may not allocate to highest-value buyer
  (may not sell at all if everyone has low virtual value)
```

---

## Matching Theory

### Stable Matching (Gale-Shapley 1962, Nobel 2012)

```
SETUP: N men, N women, each with strict preferences over the other side
  Matching: assignment M ↔ W
  STABLE matching: no blocking pair (man M and woman W who prefer each other to current match)

DEFERRED ACCEPTANCE ALGORITHM (DA):
  Round 1: Each man proposes to his 1st choice woman
           Each woman tentatively holds her best proposal, rejects others
  Round 2: Rejected men propose to their 2nd choice
           Each woman reconsiders all proposals (including held), keeps best, rejects rest
  ...
  Continue until no more proposals → all held become matches

THEOREM: DA produces a stable matching; it terminates in ≤ N² rounds.

MAN-OPTIMAL DA (men propose): gives each man his best possible stable match
WOMAN-OPTIMAL DA (women propose): gives each woman her best possible stable match
RURAL HOSPITALS THEOREM: every hospital fills same number of positions in every stable matching

STRATEGIC BEHAVIOR:
  Man-optimal DA: truth-telling is dominant strategy for MEN (proposing side)
  Women may benefit from strategic misreporting (non-proposing side)
  → DA is not universally strategyproof

APPLICATIONS:
  NRMP (National Resident Matching Program): medical residency since 1952
  School choice (Boston mechanism had strategic manipulation → replaced by DA in many cities)
  Kidney exchange: multi-way cycles in kidney donation chains (Roth)
  College admissions, job markets
```

### Top Trading Cycles (TTC)

```
SETUP: N agents, N objects, each agent owns one object and has preferences
  (or housing market: agents in existing houses, some "vacant")

TTC ALGORITHM:
  Build directed graph: each agent points to their top-choice owner
  Find cycles, execute all trades in each cycle simultaneously
  Remove traded agents/objects, repeat

THEOREM: TTC is Pareto efficient, individually rational, and strategyproof!
  (Every agent gets weakly better than their initial endowment)
  Uniquely satisfying all three properties (Roth-Postlewaite)

APPLICATION: Kidney exchange (directed graph of compatible pairs)
  k-cycles and chains (with deceased donor = "free" source)
```

---

## Shapley Value (Cooperative Game Theory)

```
SETUP: N players, characteristic function v: 2^N → R
  v(S) = total value achievable by coalition S acting alone

SHAPLEY VALUE φᵢ: fair allocation of total value among players
  Formula: φᵢ(v) = Σ_{S⊆N\{i}} [|S|!(N-|S|-1)!/N!] [v(S∪{i}) - v(S)]

  = average marginal contribution of player i across all orderings of players

AXIOMS (uniquely characterized):
  Efficiency: Σᵢ φᵢ = v(N)   (total value distributed)
  Symmetry: interchangeable players get equal value
  Dummy: player adding zero marginal contribution gets zero
  Additivity: φᵢ(v+w) = φᵢ(v) + φᵢ(w)

SHAP (SHapley Additive exPlanations) in ML:
  Features = players; prediction = value
  φᵢ = average marginal contribution of feature i to prediction
  Satisfies same axioms → "fair" attribution of prediction to features
  Exact SHAP: O(2^N) → TreeSHAP: O(N log N) for tree models (polynomial!)
  Kernel SHAP: model-agnostic approximation

NUCLEOLUS, CORE: other cooperative game theory solution concepts
  Core: set of allocations no coalition wants to block
  May be empty (needs strong conditions on v for non-empty core)
```

---

## Arrow's Impossibility Theorem

```
SOCIAL CHOICE FUNCTION: F(≻₁, ..., ≻ₙ) → social ordering ≻*

DESIRABLE AXIOMS:
  Unanimity (Pareto): if all prefer x ≻ y → x ≻* y
  Independence of Irrelevant Alternatives (IIA): social ranking x vs y depends only on
    individual rankings of x vs y (not on other options)
  Non-dictatorship: no single agent whose preferences always equal social preferences

ARROW'S THEOREM (1951): For 3+ alternatives and 2+ people,
  NO social choice function satisfies all three axioms simultaneously.

PROOF SKETCH: IIA + Unanimity → some agent is a "pivotal" agent
  → Pivotal agent's preference determines social ranking → dictatorship.

IMPLICATIONS:
  No perfect voting system (plurality, Borda count, Condorcet all violate some axiom)
  Condorcet cycles: A beats B, B beats C, C beats A → no social ordering!
  → Why dictatorships are tempting, why democratic systems use procedural rules + compromise

  BYPASSES:
  Cardinal utility (not just ordinal): score voting, quadratic voting
  Probabilistic social choice: randomize over outcomes
  Restrict domain: single-peaked preferences → median voter theorem works
```

---

## Decision Cheat Sheet

| Mechanism | Goal | IC? | Efficient? | Notes |
|-----------|------|-----|-----------|-------|
| Second-price auction | Allocate one object | DSIC | Yes | Truth-dominant, revenue < optimal |
| First-price auction | Allocate one object | BIC | Yes | Shade bids, revenue = 2nd price (Rev. Equiv.) |
| VCG | Allocate any efficiently | DSIC | Yes | Budget imbalance, computationally hard |
| Myerson optimal | Max revenue | BIC | No | Uses virtual valuations, may not sell |
| Gale-Shapley DA | Stable matching | DSIC (proposers) | Stable | Not eff., woman-optimal DA for proposers |
| Top Trading Cycles | Reassignment | DSIC | Pareto optimal | All three: unique property |
| Shapley value | Fair value allocation | — | Efficient | Used in ML (SHAP), cost-sharing |
