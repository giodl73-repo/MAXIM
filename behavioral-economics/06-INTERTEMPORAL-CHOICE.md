# Intertemporal Choice

## The Discounting Problem

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    INTERTEMPORAL CHOICE FRAMEWORK                           │
│                                                                             │
│  STANDARD MODEL (DU — Discounted Utility, Samuelson 1937):                  │
│  V = Σ_t U(c_t) × δ^t   where δ = discount factor = 1/(1+r)                 │
│  Constant discount rate r per period. Exponential discounting.              │
│  Preferences are DYNAMICALLY CONSISTENT.                                    │
│                                                                             │
│  BEHAVIORAL REALITY:                                                        │
│  People discount the near future MUCH more steeply than the far future.     │
│  Hyperbolic discounting: D(t) = 1/(1+kt) for parameter k                    │
│  Present bias: immediate rewards get disproportionate weight.               │
│  Dynamic inconsistency: plans made for the future are abandoned             │
│  when the future arrives and becomes the present.                           │
│                                                                             │
│  APPLICATIONS:                                                              │
│  Retirement savings, dieting, exercise, debt management                     │
│  Technical debt in software (delayed pain → discounted)                     │
│  Organizational change (future benefit discounted; immediate disruption not) │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Exponential vs. Hyperbolic Discounting

```
EXPONENTIAL DISCOUNTING (standard economics):
  D(t) = δ^t = e^{-rt}
  Discount factor at time t is exponential in t.
  Constant instantaneous discount rate r.

  Property: DYNAMICALLY CONSISTENT.
  If I prefer $100 in year 2 to $110 in year 1 today,
  I will still prefer $100 in year 2 when I'm sitting in year 1.
  My preference order between future options doesn't change as time passes.

HYPERBOLIC DISCOUNTING (empirical):
  D(t) = 1/(1 + k×t)
  Discount factor falls slowly at first but rapidly near t=0.
  Instantaneous discount rate = dD/dt / D(t) = k / (1+kt) → falls with t.

  Property: HIGH IMMEDIATE DISCOUNT RATE, LOW LONG-RUN DISCOUNT RATE.
  Near-term: discount rate very high (sacrifice a lot to get it NOW)
  Far-future: discount rate lower (patient about far-future tradeoffs)

GRAPHICAL COMPARISON:

  D(t) │
  1.0  │●
  0.9  │ ●
  0.8  │  ●         Exponential
  0.7  │   ●● ───────────────────────── (straight on log scale)
  0.6  │    ●●●
  0.5  │    ●●●●    Hyperbolic
  0.4  │       ●●●●●
  0.3  │           ●●●●●●●●
  0.2  │                   ●●●●●●●●
  0.1  │                           ●●●●●
       └─────────────────────────────────── t
         0   1   2   3   4   5   6   7   8

  KEY DIFFERENCE: Near t=0, hyperbolic falls much faster than exponential.
  The "immediacy effect": the present moment has a qualitatively special status.
```

## Quasi-Hyperbolic Discounting (β-δ Model)

```
β-δ MODEL (Laibson 1994, O'Donoghue & Rabin 1999):
  A tractable approximation to hyperbolic discounting.

  V(c₀, c₁, c₂, ...) = U(c₀) + β × Σ_{t=1}^∞ δ^t × U(cₜ)

  β = present bias parameter (0 < β < 1)
  δ = standard exponential discount factor (0 < δ < 1)
  Both β and δ apply to ALL future periods; only β creates the discontinuity at t=0.

  WHEN β = 1: reduces to standard exponential (δU₁ + δ²U₂ + ...)
  WHEN β < 1: extra discount on all future periods relative to present.
    Present gets U₀ (no discounting).
    Period 1 gets β×δ×U₁ (double-discounted).
    Period 2 gets β×δ²×U₂.
    Period t gets β×δ^t×U_t.

  INTERPRETATION:
  δ captures long-run patience (how much people value the future generally).
  β captures present bias (how much more they favor the present over the future).

  Empirical estimates:
  β ≈ 0.7-0.9 (most estimates; varies by context)
  δ ≈ 0.95-0.99 per year

  EXAMPLE:
  β = 0.8, δ = 0.95/year
  Trade $100 now for $x in 1 year: x such that 100 = 0.8 × 0.95 × x
  x = 100 / 0.76 ≈ $131.6 (requires 31.6% premium for 1-year delay)
  Trade $100 in 10 years for $y in 11 years: 0.8×0.95^10 × 100 = 0.8×0.95^11 × y
  0.95^10 × 100 = 0.95^11 × y → y = 100/0.95 ≈ $105.3 (only 5.3% for same delay)
  DRAMATIC DIFFERENCE: 31.6% for NOW→1yr vs. 5.3% for 10yr→11yr.
```

## Dynamic Inconsistency

```
DYNAMIC INCONSISTENCY:
  Today I plan to do X in the future.
  When the future arrives, I don't do X.
  Not because circumstances changed — my preferences changed.

EXAMPLE:
  January: "I will exercise every day starting February."
  February arrives: "I'll start properly in March."
  This isn't updating beliefs; it's preference reversal when future becomes present.

FORMAL DEFINITION:
  Agent is dynamically inconsistent if:
  Plan made from perspective of time t for action at t' > t
  differs from the plan made from perspective of time t' for action at t'.

NAÏVE vs. SOPHISTICATED AGENTS:
  NAÏVE: Doesn't anticipate their own present bias.
    Believes they will follow their current plan ("I'll definitely start diet Monday").
    Repeatedly makes plans that future self abandons.
    Procrastinates indefinitely on costly tasks.
    Over-borrows expecting to pay off quickly (doesn't).
    Gym membership: buy, rarely go, don't cancel because "I'll start next week."

  SOPHISTICATED: Anticipates their present bias.
    Knows future self will succumb to immediate temptation.
    Takes commitment actions to constrain future self.
    Ulysses strategy: lash yourself to the mast before the sirens.
    Examples: put savings in illiquid account (avoid future self spending it),
      schedule meetings to create deadlines, meal prep to avoid future food choices.

  PARTIAL NAÏVETÉ: Most realistic. People are partially aware of bias.
    O'Donoghue & Rabin (2001): partial naïveté creates systematic procrastination
    patterns. The model predicts: tasks are done at last moment, or never.
```

## Commitment Devices

```
COMMITMENT DEVICE:
  Action taken in advance that constrains future choice to align with
  long-run preferences.
  "Binding the future self."

EXAMPLES:
  Personal:
    Illiquid savings accounts (Christmas clubs, 401k early withdrawal penalty)
    Pre-commitment to social/public declarations ("I'm quitting smoking today")
    Automatic savings transfers on payday (before discretionary spending)
    Meal prep (remove future decision about healthy eating)
    Removing junk food from home (make temptation unavailable)
    Gym enrollment with non-refundable fee (sunk cost as commitment device!)

  Medical:
    Disulfiram (Antabuse) for alcoholism: take drug that makes alcohol toxic
    → commitment device against future drinking
    Naltrexone implant: blocks opioid receptors → commitment against relapse

  Financial:
    Annuities: commit future self to spend down wealth slowly
    Defined contribution with vesting schedule: golden handcuffs = commitment
    Target date funds: removes future asset allocation decisions (good for naïve)

  Organizational:
    Sprint commitments: commit team to deliverable in fixed period
    Milestone-triggered funding: next tranche only on hitting objective
    Public roadmaps: visible commitment to external stakeholders
    Pre-mortems: imagine project failed → reduce planning fallacy bias
    Killswitch criteria: pre-commit to cancel if X happens (removes sunk cost)

  Policy:
    Automatic enrollment in retirement savings (default commitment; see 07-NUDGE)
    Save More Tomorrow (SMarT, Thaler & Benartzi 1999):
      Employees commit in advance to increase savings rate with each future raise.
      Key insight: commitment is in the future (present bias doesn't resist it);
        increases are framed as foregone gains, not losses.
      Outcome: savings rates increased dramatically vs. control groups.
```

## Technical Debt as Hyperbolic Discounting

```
TECHNICAL DEBT AND PRESENT BIAS:

  The decision to take on technical debt is a discounted intertemporal choice:
  Option A: Spend extra time now doing it right → cost = developer time now,
             benefit = future maintainability / avoided refactoring
  Option B: Quick fix now → immediate shipping, future refactoring cost

  Under exponential discounting: if future cost > present cost, choose A.
  Under hyperbolic discounting: future cost is heavily discounted → choose B more often.

  β < 1: future refactoring cost is discounted by β relative to present shipping goal.
  δ: future is discounted per period.
  Combined: future debt payment feels small relative to immediate shipping gain.

  MANIFESTATION:
  "We'll refactor after the launch."
  "We'll add tests next sprint."
  "We'll clean this up in Q4."
  → These are naïve plans that future-self (pressured by new deadlines) abandons.
  → Technical debt compounds (interest accrues) while present bias recurs.

  COMMITMENT DEVICE SOLUTIONS:
  1. Definition of Done: include code quality standards in DoD (pre-commitment)
  2. Tech debt sprints: scheduled regular debt reduction (structural commitment)
  3. 20% time for quality: committed allocation (not optional after-thought)
  4. Visible debt metrics: tech debt dashboard makes future costs salient NOW
     (reduce psychological distance; make future cost feel present)
  5. Architecture review boards: external constraint on future-self's decisions

  MEASUREMENT MAKES FUTURE COSTS SALIENT:
  "This module has a maintainability index of 12 and 8% test coverage.
   The expected refactoring cost if not addressed: 200 engineer-hours."
  Making future costs explicit and specific reduces their psychological discounting.
```

## Present Bias in Organizational Dynamics

```
ORGANIZATIONAL MANIFESTATIONS:

1. INVESTMENT IN FUTURE CAPABILITIES:
   Training programs → benefits arrive in 1-2 years.
   Platform investments → benefits in 2-5 years.
   Under present bias: short-term project wins crowd out these investments.
   "We'll invest in skills when we have bandwidth" → bandwidth never appears.

2. CULTURE AND NORMS:
   Building culture takes years; its effects are compounded and delayed.
   Present bias: management time goes to immediate deliverables.
   Culture investment is perpetually deferred.

3. SUCCESSION PLANNING:
   Benefits arrive after executive departs. Immediate cost = time and risk.
   Present bias: minimal succession planning until crisis forces it.

4. SECURITY AND RELIABILITY INVESTMENT:
   Security debt: skip security reviews now, face breach later.
   Reliability debt: cut corners on testing, face outage later.
   Present bias: security/reliability costs are real today; benefits are prevention
   of hypothetical future events → heavily discounted → systematically underfunded.

   CONNECTION: This is a financial version of present bias, not just behavioral.
   Organizations have β < 1 in their effective discount rates:
   quarterly earnings pressure creates institutional present bias even if
   individual managers are fully sophisticated about intertemporal choice.

5. PERFORMANCE REVIEW CYCLES:
   Annual cycles create an institutional β with period = 1 year.
   Anything that pays off in > 1 year is discounted by the review cycle.
   VP managing 3-year cycle (own promotion timeline) thinks longer-term
   than IC evaluated quarterly.
   Organizational present bias tracks the review cycle length.
```

## Decision Cheat Sheet

| Intertemporal question | Mechanism | Intervention |
|---|---|---|
| Why won't employees start saving for retirement? | Present bias: future > present sacrifice | Auto-enrollment + SMarT (see 07, 09) |
| Why does technical debt keep accumulating? | Present bias: future refactoring cost is discounted | Tech debt sprints; Definition of Done standards |
| Why is my diet plan never started? | Dynamic inconsistency: naïve agent's plan fails | Commitment device: remove food from home, prepay |
| How can I get my team to invest in platform work? | Make future costs salient (reduce psychological distance) | Visible debt metrics; structured time allocation |
| Why do layoff plans get deferred until crisis? | Present bias: delay painful action (cost is immediate) | Pre-commit to workforce planning reviews at fixed schedule |
| What's the β-δ model? | β = present bias; δ = long-run discount factor | Separate the two; β corrections via commitment devices |
| When should I use commitment devices? | When sophisticated about your own present bias | Irreversibility + upfront commitment + pre-specified triggers |

## Common Confusion Points

**Hyperbolic discounting ≠ impatience**: An exponentially discounting person with a high discount rate is impatient but dynamically consistent. A hyperbolically discounting person may be patient overall (high δ) but still present-biased (low β). These are distinct. Someone can be long-run patient AND short-run impulsive simultaneously.

**Procrastination is not laziness**: Present bias predicts systematic procrastination even for motivated, sophisticated people. A task that should be done now has future benefits (discounted by β×δ^t) and present cost (immediate effort). If β < 1, even small present costs can outweigh large future benefits. This is structural, not a character flaw.

**Commitment devices have commitment costs**: Tying your hands reduces flexibility. If the future state differs from what was planned (new information, changed circumstances), a commitment device prevents beneficial adaptation. Optimal commitment leaves some flexibility while constraining specific known failure modes. Ulysses told sailors to ignore his future self screaming to be released — but also told them to still change course if the ship needed it.

**β-δ model is an approximation**: The β-δ model is tractable but implies a discontinuity at t=0 (present is qualitatively different from all future periods, even t=1). True hyperbolic discounting is smoother. The quasi-hyperbolic form is used because it's mathematically tractable and captures the key features. Don't over-interpret the precise form.
