# Mechanism Design — Engineering Games for Desired Outcomes

## The Big Picture

Standard game theory takes the rules as given and asks: what will rational agents do?
Mechanism design (the "engineering" branch of game theory) inverts this: given a desired
social outcome, what rules should we impose so that rational agents produce that outcome?

```
+------------------------------------------------------------------+
|                  MECHANISM DESIGN FRAMEWORK                       |
|                                                                  |
|  STANDARD GAME THEORY         MECHANISM DESIGN                   |
|  --------------------         ----------------                   |
|  Rules given → find           Desired outcome → design rules     |
|  equilibrium                  whose equilibrium achieves it      |
|                                                                  |
|  WHAT WE'RE DESIGNING:                                           |
|  ┌─────────────────────────────────────────────────────────┐    |
|  │  A social choice function f: Θ → X                      │    |
|  │  Θ = type profiles (private info)                       │    |
|  │  X = outcome space (allocations, prices, decisions)     │    |
|  │                                                         │    |
|  │  A mechanism M = (M₁×...×Mₙ, g)                       │    |
|  │  Mᵢ = message space for agent i                        │    |
|  │  g: M₁×...×Mₙ → X = outcome function                  │    |
|  │                                                         │    |
|  │  M implements f if the equilibrium of the game         │    |
|  │  induced by M achieves f(θ) for all θ.                 │    |
|  └─────────────────────────────────────────────────────────┘    |
|                                                                  |
|  KEY RESULTS:                                                    |
|  Revelation Principle → WLOG study direct mechanisms            |
|  Gibbard-Satterthwaite → DSIC efficiency impossible (general)   |
|  VCG → DSIC + efficiency (with transfers)                       |
|  Myerson → revenue-maximizing auction                           |
|  Gale-Shapley → stable matching without transfers               |
+------------------------------------------------------------------+
```

---

## The Revelation Principle

This is the foundational simplification theorem of mechanism design.

**Direct revelation mechanism**: Mᵢ = Θᵢ (agents report their types directly) with
outcome function g: Θ → X.

**Incentive compatibility (IC)**: Truthful reporting is a (Bayesian or dominant strategy)
equilibrium.

**Theorem (Revelation Principle)**: For any mechanism M and any equilibrium σ* of the
game induced by M, there exists a direct revelation mechanism M' = (Θ, g∘σ*) where:
1. M' is incentive compatible (truth-telling is an equilibrium)
2. M' achieves the same outcome as M under equilibrium play

```
  REVELATION PRINCIPLE PICTURE

  Original mechanism M:          Equivalent direct mechanism M':
  ─────────────────────          ─────────────────────────────
  Agent i has type θᵢ            Agent i has type θᵢ
  Sends message mᵢ = σᵢ*(θᵢ)   Reports θᵢ truthfully
          │                              │
          ↓                              ↓
  Mechanism g(m₁,...,mₙ)         Mechanism g(σ₁*(θ₁),...,σₙ*(θₙ))
          │                              │
          ↓                              ↓
  Outcome x ∈ X                  Same outcome x ∈ X

  Incentive to lie in M'? If agent i reports θ'ᵢ ≠ θᵢ:
  M' plays σᵢ*(θ'ᵢ) on their behalf. But σᵢ*(θᵢ) was optimal
  in M — so mimicking another type's strategy doesn't help.
```

**Implication**: Without loss of generality, restrict attention to direct revelation
mechanisms where truth-telling is an equilibrium. This collapses an infinite design space
into a tractable constraint satisfaction problem.

**Variants**:
- **Dominant Strategy IC (DSIC)**: truth is dominant strategy (best regardless of others)
- **Bayesian IC (BIC)**: truth is best response in expectation over others' types

DSIC ⊆ BIC. DSIC is more robust (doesn't require common prior); BIC allows more revenue.

---

## Incentive Compatibility and Individual Rationality

### Formal Constraints

**Quasilinear utility**: uᵢ(x, tᵢ, θᵢ) = vᵢ(x, θᵢ) - tᵢ

where x is the allocation, tᵢ is the payment made by agent i (can be negative = subsidy),
vᵢ(x, θᵢ) is agent i's value for allocation x given type θᵢ.

**DSIC constraint** for direct mechanism (x̂, t̂):

    vᵢ(x̂(θᵢ, θ₋ᵢ), θᵢ) - t̂ᵢ(θᵢ, θ₋ᵢ) ≥ vᵢ(x̂(θ'ᵢ, θ₋ᵢ), θᵢ) - t̂ᵢ(θ'ᵢ, θ₋ᵢ)

for all i, θᵢ, θ'ᵢ, θ₋ᵢ. (Reporting truthfully weakly dominates any lie.)

**Individual Rationality (IR / participation constraint)**:

    vᵢ(x̂(θᵢ, θ₋ᵢ), θᵢ) - t̂ᵢ(θᵢ, θ₋ᵢ) ≥ 0

Agents must weakly prefer participating to their outside option (normalized to 0).

---

## Gibbard-Satterthwaite Theorem

**Context**: What if there are no transfers (no money)? Can we design efficient DSIC
mechanisms for social choice over ≥ 3 alternatives?

**Theorem (Gibbard 1973, Satterthwaite 1975)**: Suppose:
1. There are at least 3 possible outcomes
2. All preference orderings over outcomes are possible types
3. The mechanism f: Θ → X is surjective (every outcome is achievable)

Then: f is DSIC iff f is **dictatorial** (there exists a fixed agent i* such that
f(θ) is always i*'s top-ranked alternative).

**Proof connection to Arrow**: Arrow's Impossibility Theorem (1951) states that no social
welfare function satisfies unrestricted domain, Pareto efficiency, independence of
irrelevant alternatives, and non-dictatorship. Gibbard-Satterthwaite follows by showing
DSIC for social choice functions implies the conditions of Arrow's theorem.

```
  IMPLICATION DIAGRAM

  Want: DSIC + Efficient + Non-dictatorial
        over general preferences, ≥ 3 alternatives, no transfers
                        |
                        v
  IMPOSSIBLE (Gibbard-Satterthwaite)

  Escape routes:
  ┌─────────────────────────────────────────────────────┐
  │ 1. Add monetary transfers → Groves/VCG mechanisms   │
  │ 2. Restrict domain (single-peaked preferences)      │
  │    → Median voter rule is DSIC + efficient          │
  │ 3. Weaken IC to Bayesian IC (BIC)                  │
  │    → Myerson-Satterthwaite impossibility theorem    │
  │      (bilateral trade has another impossibility)    │
  │ 4. Allow randomization (Gibbard 1977: random dicts) │
  └─────────────────────────────────────────────────────┘
```

---

## Groves Mechanisms and VCG

### Groves Mechanisms

**Setting**: Allocate an object (or make a decision) x ∈ X to maximize social welfare.
Agents have quasilinear utility. Agent i's value for outcome x is vᵢ(x, θᵢ) — private.

**Efficient allocation**: x*(θ) = argmax_x Σᵢ vᵢ(x, θᵢ)

**Groves mechanism**:
- Allocate x*(θ) (socially efficient given reports)
- Pay agent i:  tᵢ(θ) = Σⱼ≠ᵢ vⱼ(x*(θ), θⱼ) + hᵢ(θ₋ᵢ)

where hᵢ(θ₋ᵢ) is any function of others' types (not i's).

**Why is Groves DSIC?** Agent i's payoff:

    vᵢ(x*(θ), θᵢ) - tᵢ(θ) = vᵢ(x*(θ), θᵢ) + Σⱼ≠ᵢ vⱼ(x*(θ), θⱼ) + hᵢ(θ₋ᵢ)
                             = Σⱼ vⱼ(x*(θ), θⱼ) + hᵢ(θ₋ᵢ)

Agent i's payoff equals **total social welfare + a term independent of their report**.
So maximizing their payoff = maximizing social welfare = reporting truthfully. □

**Green-Laffont Theorem**: Groves mechanisms are essentially the *only* DSIC mechanisms
that always implement the socially efficient allocation (in the quasilinear, full-range
setting). Efficiency + DSIC pins down the mechanism up to hᵢ.

### VCG: Vickrey-Clarke-Groves

**VCG payment** (Clarke's pivot rule):

    tᵢᵛᶜᴳ(θ) = Σⱼ≠ᵢ vⱼ(x*(θ), θⱼ) - Σⱼ≠ᵢ vⱼ(x*₋ᵢ(θ₋ᵢ), θⱼ)

where x*₋ᵢ(θ₋ᵢ) = argmax_{x} Σⱼ≠ᵢ vⱼ(x, θⱼ) is the efficient outcome without agent i.

Agent i **pays their externality on others**: the difference in others' welfare caused by
including agent i in the mechanism.

```
  VCG INTUITION: "you internalize the harm you impose"

  Without you: others get Σⱼ≠ᵢ vⱼ(x*₋ᵢ)  (their best possible world)
  With you:    others get Σⱼ≠ᵢ vⱼ(x*(θ))  (world distorted by your presence)

  You pay: (what others would get without you) - (what they get with you)
         = your externality

  If you have no externality (your presence doesn't change others' welfare):
  tᵢ = 0. Fair.
```

**Key properties of VCG**:
- DSIC (inherits from Groves)
- Efficient allocation
- IR (with appropriate hᵢ choices)
- Not budget-balanced in general (the mechanism may need external subsidy)

---

## Auction Theory

### Vickrey Second-Price Auction

**Setup**: Single indivisible object. n bidders with private valuations vᵢ ~ independent
distributions. Highest bidder wins; pays the second-highest bid.

**Theorem**: Truthful bidding (bᵢ = vᵢ) is a dominant strategy in the second-price auction.

**Proof**:

```
  Fix any bids b₋ᵢ by others. Let m = max_{j≠i} bⱼ (the price if you win).

  Case 1: vᵢ > m (your value exceeds the price)
    Bid vᵢ: you win, pay m, profit vᵢ - m > 0  ✓
    Bid b < m: you lose, profit 0. Worse if vᵢ > m.
    Bid b > vᵢ: you win if b > m, but so does bidding vᵢ.
    → Bidding vᵢ is at least as good.

  Case 2: vᵢ < m (price exceeds your value)
    Bid vᵢ: you lose, profit 0  ✓
    Bid b > m: you win, pay m, profit vᵢ - m < 0. Worse.
    → Bidding vᵢ is at least as good.

  Case 3: vᵢ = m
    Outcome same whether you win or lose (zero profit either way).

  In all cases, bidding vᵢ weakly dominates any other bid.  □
```

**Connection to VCG**: Second-price auction is VCG for a single-item allocation.
The VCG payment = (value to others if you win) - (value to others if you don't) = m.

### First-Price Sealed-Bid Auction

Highest bidder wins; pays their own bid. No dominant strategy. BNE: bid-shading.

For n bidders with valuations iid U[0, 1]:

    bᵢ*(vᵢ) = (n-1)/n · vᵢ

Each bidder bids a fraction (n-1)/n of their value. Expected revenue = (n-1)/(n+1).

### Revenue Equivalence Theorem

**Theorem (Myerson 1981, Riley-Samuelson 1981)**: Consider any two auction formats that:
1. Award the object to the bidder with the highest value (efficiency)
2. Give a bidder with value 0 an expected payment of 0

Then both auctions yield the **same expected revenue to the seller** and the **same
expected payment by each bidder**.

**Implication**: First-price and second-price auctions (and many others) yield the same
expected revenue when bidders have independent private values.

```
  The theorem works because: in both formats, a bidder with value v
  wins with probability F(v)^{n-1} (same — must beat all n-1 others).
  The envelope theorem pins down payments given the allocation rule.

  Envelope condition: d/dvᵢ [Uᵢ(vᵢ)] = P(win | vᵢ) = F(vᵢ)^{n-1}

  Integrating: Uᵢ(vᵢ) = ∫₀^{vᵢ} F(t)^{n-1} dt

  Expected payment = vᵢ · F(vᵢ)^{n-1} - Uᵢ(vᵢ) — same in both formats.
```

**Failures of revenue equivalence**: risk-averse bidders, correlated values, asymmetric
distributions, budget constraints, common values — all break RET.

### Myerson Optimal Auction

**Goal**: Maximize expected revenue, not efficiency. May sacrifice efficiency.

**Virtual value** for bidder i with distribution Fᵢ and density fᵢ:

    φᵢ(vᵢ) = vᵢ - (1 - Fᵢ(vᵢ)) / fᵢ(vᵢ)

```
  Interpretation: "virtual value" is value minus information rent.
  The seller must give buyers information rent to elicit truthful reporting.
  Virtual value = true value minus the rent.

  For uniform on [0,1]: φ(v) = v - (1-v)/1 = 2v - 1.
  So φ(v) < 0 for v < 1/2: even a willing buyer may not be served if their
  virtual value is negative.
```

**Myerson's Optimal Auction**:
- Allocate the object to the bidder with the highest **positive** virtual value
- If all virtual values are negative: don't sell (set a reserve price)
- For symmetric bidders: reserve price r* solves φ(r*) = 0

**Regular distributions**: Fᵢ is regular if φᵢ is non-decreasing. For regular distributions,
Myerson's auction is implementable. For irregular distributions: "ironing" (averaging virtual
values over intervals where they decrease).

```
  Optimal reserve price (symmetric, regular):
  φ(r*) = 0  →  r* - (1-F(r*))/f(r*) = 0

  For U[0,1]: 2r* - 1 = 0  →  r* = 1/2

  With n=1 bidder: post price r* = 1/2. Sell iff bidder's value ≥ 1/2.
  Expected revenue = ∫_{1/2}^1 v · dF + r* · (1-F(r*))
                   = 1/4 + 1/4 = 1/2.  (vs 0 with no reserve)
```

---

## Combinatorial Auctions

**Setting**: Multiple heterogeneous items; bidders have valuations for packages (bundles).

**Winner Determination Problem**: Given bids, find the revenue-maximizing assignment.

    max Σᵢ bᵢ(Sᵢ)  subject to: {Sᵢ} are disjoint subsets of items

This is equivalent to **weighted set packing** — NP-hard. Exact solution requires
exponential-time algorithms (branch-and-bound, IP solvers).

**VCG for combinatorial auctions**: compute the efficient allocation (NP-hard), then
compute VCG payments. The allocation problem intractability makes this impractical for
large instances.

**FCC Spectrum Auctions**: Milgrom and Wilson designed the **Simultaneous Multi-Round
Ascending (SMRA)** auction used for FCC spectrum licenses since 1994. More recently,
the **Combinatorial Clock Auction (CCA)** and **Incentive Auction** (2017) involved
sophisticated mechanism design (buy back broadcast spectrum, repurpose for mobile).
Milgrom/Wilson received 2020 Nobel for this work.

---

## Two-Sided Matching: Gale-Shapley

### The Setup

**Stable matching problem**: Two disjoint sets M (students) and S (schools). Each student
has a strict preference ordering over schools; each school has a strict preference over
students. Find a matching (one-to-one correspondence) such that no student-school pair
both prefer each other to their assigned match.

### Deferred Acceptance Algorithm (Gale-Shapley 1962)

```
  STUDENT-PROPOSING DEFERRED ACCEPTANCE
  ======================================

  Round 1:
    Each student proposes to their top-choice school.
    Each school tentatively accepts their most preferred applicant
    from those proposing; rejects all others.

  Round 2:
    Each rejected student proposes to their next-choice school.
    Each school considers new proposals + current tentative accept;
    keeps the best one; rejects all others.

  ...

  Continue until no student is rejected.
  All tentative acceptances become final.

  RUNTIME: At most |M| × |S| rounds.
```

**Theorem (Gale-Shapley)**: Deferred acceptance produces a **stable matching** — no
student-school pair both prefer each other to their assigned match.

**Proof sketch**: Suppose student m and school s form a blocking pair (both prefer each
other). Since m prefers s to their match, m must have proposed to s at some round. School
s either rejected m (in favor of someone s prefers) or accepted someone later. Either way,
s ended up with someone s prefers over m. Contradiction. □

**Optimality**:
- Student-proposing DA is **student-optimal**: every student is matched to their best
  possible partner in any stable matching.
- Student-proposing DA is **school-pessimal**: every school is matched to their worst
  acceptable partner in any stable matching.
- School-proposing DA reverses these.

**Strategy-proofness**: Student-proposing DA is **strategy-proof for students** — no
student can benefit by misreporting their preferences. Schools, however, can sometimes
benefit by strategic misreporting (this is unavoidable for one side).

```
  APPLICATIONS:
  - NRMP (National Residency Matching Program): residency placement in US medicine.
    Roth redesigned NRMP in 1998 using DA. 2012 Nobel.
  - NYC High School admissions (Roth/Abdulkadiroglu 2003)
  - Boston school choice (Abdulkadiroglu/Sonmez 2003)
  - Kidney exchange (Roth/Sonmez/Unver 2004)
```

### Kidney Exchange (Roth)

```
  Problem: Incompatible donor-patient pairs who wish to exchange.
  Patient A has donor incompatible with B's need; vice versa.
  → Direct exchange (2-way cycle)
  → Or: longer cycles and chains
  → Chains starting from altruistic donors (no reciprocal need)

  Mechanism: Top Trading Cycles (Shapley-Scarf)
  Each patient points to their most preferred donor;
  each donor points to their patient. Find cycles; execute.
  Repeat on remaining agents.

  TTC is: Pareto efficient, DSIC, individually rational.
```

---

## Myerson-Satterthwaite Impossibility

**Setting**: Bilateral trade — one seller with value cₛ ~ Fₛ, one buyer with value vᵦ ~ Fᵦ,
both private. Gains from trade exist when vᵦ > cₛ.

**Theorem (Myerson-Satterthwaite 1983)**: There is **no mechanism** that is simultaneously:
- **Bayesian IC** (truth-telling is BNE)
- **Ex post efficient** (trade occurs whenever vᵦ > cₛ)
- **Budget balanced** (no external subsidy needed)
- **Individually rational** (both agents willing to participate)

This is the double auction impossibility. Even the best possible mechanism must sacrifice
at least one of these properties. In practice: mechanisms sacrifice some efficiency
(not all mutually beneficial trades happen) or require budget subsidies.

---

## Decision Cheat Sheet

| Goal | Mechanism | Notes |
|------|-----------|-------|
| Efficient allocation, dominant strategy IC | VCG / Groves | May need external budget |
| Single item, maximize revenue | Myerson optimal auction | Reserve price = φ⁻¹(0) |
| Single item, standard format | Second-price (Vickrey) | Truthful, no revenue max |
| Multiple items (packages) | Combinatorial auction + VCG | Allocation is NP-hard |
| Two-sided matching, stability | Gale-Shapley DA | Proposing side gets optimum |
| Match + strategy-proof for one side | Student-proposing DA | Students: truthful dominant |
| Social choice, no transfers | Dictatorial (G-S theorem) | Or restrict domain |
| Maximize revenue with correlated types | Cremer-McLean extraction | Requires common knowledge |
| Trade with private costs/values | Double auction | Efficiency ↔ budget (M-S theorem) |

---

## CS and Systems Bridges

| Mechanism design concept | Formal / systems analogue |
|---|---|
| Incentive compatibility (IC) | Type safety / compiler enforcement: IC is a constraint that makes truth-telling a dominant strategy — the mechanism statically rules out profitable lying, analogous to a type system ruling out invalid operations |
| Revelation principle | Abstraction layer: any indirect mechanism (sealed-bid auction, ascending auction, negotiation protocol) can be compiled down to an equivalent direct mechanism (ask types, run algorithm) — you don't lose generality by working at the direct level |
| VCG mechanism | Externality internalization: each agent pays the negative externality they impose on others — aligns private incentives with social welfare; exact analogue of Pigouvian taxation in public economics |
| Arrow's Impossibility Theorem | No protocol satisfies all three "obvious" desiderata simultaneously (Pareto + IIA + non-dictatorship); in distributed systems: CAP theorem has the same flavor — no system satisfies all three of Consistency, Availability, Partition tolerance |
| Myerson optimal auction | Revenue-maximizing mechanism design = constrained optimization over allocation/payment rules subject to IC + IR; Myerson's ironing is a convexification step analogous to LP relaxation in integer programs |
| Myerson-Satterthwaite theorem | Impossibility result: efficiency + budget balance + individual rationality are jointly infeasible for bilateral trade — no market mechanism satisfies all three; trade-off must be made |
| Two-sided matching (Gale-Shapley) | Stable matchings as a fixed point of a deferred acceptance algorithm; runs in O(n²) and is used in NRMP (medical residency), FCC spectrum auctions, school assignment — a polynomial-time algorithm for a problem with no NE computation difficulty |
| Combinatorial auction (VCG) | Winner determination is NP-hard — the computational complexity of mechanism design for package bidding; practical systems use MIP solvers or approximation algorithms with bounded PoA |
| Scoring rules / forecast elicitation | Proper scoring rules (Brier, log loss) are incentive-compatible mechanisms for eliciting probabilistic forecasts — paying log(p(true outcome)) makes truth-telling dominant; bridges to information-theory/ (log loss = cross-entropy) |

## Common Confusion Points

**"Revelation principle says direct mechanisms are optimal"**: Revelation principle says
every equilibrium of any mechanism can be replicated by an IC direct mechanism. It doesn't
say direct mechanisms are uniquely best — it says you don't lose generality by restricting
to them. The class of implementable outcomes is the same.

**"VCG always works"**: VCG requires the allocation problem to be solvable. For combinatorial
auctions, the winner determination problem is NP-hard. VCG also fails budget balance (may
require external subsidy). In practice: approximation mechanisms, ascending auctions.

**"Revenue equivalence means all auctions are the same"**: Revenue equivalence is an
expected revenue statement over distributions. It requires: same allocation rule, same
expected payment for lowest type, independent private values, risk-neutral bidders. Violate
any of these and revenues diverge. First-price and second-price have the same *expected*
revenue but different distributions of outcomes and different strategic properties.

**"Gale-Shapley is strategy-proof"**: DA is strategy-proof for the *proposing* side only.
Schools (the receiving side) can benefit from misreporting. No matching mechanism that
always produces a stable matching is strategy-proof for both sides (Roth 1982).

**"Myerson optimal auction maximizes efficiency"**: No — it maximizes the seller's expected
revenue, which may mean not selling to some positive-value buyers (when their virtual value
is negative). Efficiency (total welfare maximization) = VCG / Groves. Revenue maximization
= Myerson. These are different objectives.

**"IC and IR are weak constraints"**: In mechanism design, IC and IR together can be very
restrictive. The Myerson-Satterthwaite theorem shows that IC + IR + efficiency + budget
balance are mutually inconsistent for bilateral trade. The information rents required to
elicit truth-telling from buyers eat into the gains from trade.
