# Economics & Game Theory — Overview

---

## Big Picture

```
LAYERED STRUCTURE OF ECONOMICS:

MICROECONOMICS — atomic building blocks
  Individual optimization: max U(x) s.t. budget; max π = pQ − C(Q)
  Market equilibrium: supply = demand → price vector clears all markets
  Efficiency: First Welfare Theorem — competitive equilibrium is Pareto optimal
         ↓ extends to
INFORMATION ECONOMICS — micro with private types
  Adverse selection, moral hazard, signaling
  When agents have asymmetric info, competitive equilibrium can collapse
  (Akerlof lemons; Spence signaling; Mirrlees optimal taxation)
         ↓ private types + strategic agents =
GAME THEORY — strategic interaction (multiple optimizing agents)
  Each agent's optimal action depends on others' strategies
  Solution concepts: Nash equilibrium, SPE, PBE, BNE
  Game theory does NOT design the rules; it analyzes given rules
         ↓ flip the question: design rules to achieve target outcome
MECHANISM DESIGN — "inverse game theory" / algorithmic incentive engineering
  Social planner chooses rules given agents will play Nash/Bayes-Nash
  Revelation principle: restricts search to direct truthful mechanisms
  VCG (efficient outcomes), Myerson (revenue-optimal), DA (stable matching)
  Connects directly to: distributed systems incentive design, auction platforms
         ↓ zoom out from individual markets to economy-wide dynamics
MACROECONOMICS — aggregate phenomena
  Not just "big micro" — emergent dynamics from coordination failures,
  sticky prices, monetary/fiscal policy, capital accumulation
  IS-LM, AS-AD, Solow, DSGE models

CROSS-LINKS:
  Information economics → mechanism design (private types are the input)
  Game theory ↔ mechanism design (same math, opposite direction)
  Macro uses micro foundations (DSGE = game theory + optimization + equilibrium)
  Information economics ↔ macro (credit markets, bank runs, asymmetric info cycles)
```

---

## Why an Engineer/CS Person Cares

1. **Pricing and markets in tech:** How does Uber surge pricing work? How does Google Ads auction operate? Why do two-sided platforms (eBay, Airbnb) face a chicken-and-egg problem? These are economics questions.

2. **Mechanism design = systems design for rational agents:** When agents have private information and self-interested behavior, how do you design a system that still achieves good outcomes? This is exactly what distributed systems engineers face when incentives matter.

3. **Auction theory:** Google's AdWords, Vickrey-Clarke-Groves (VCG) mechanisms, spectrum auctions. Nobel 2020 (Milgrom, Wilson) directly from spectrum auction design.

4. **Game theory in AI:** Multi-agent RL, strategic behavior in AI systems, Nash equilibria as fixed points of best-response dynamics.

5. **Shapley values in ML:** SHAP (SHapley Additive exPlanations) for ML interpretability is directly from cooperative game theory.

6. **Matching markets:** Stable matching (Gale-Shapley algorithm) used in medical residency matching, school choice, kidney exchange. Nobel 2012 (Roth, Shapley).

7. **Information economics:** Adverse selection (used car market), moral hazard (insurance), signaling (education as credential, not skill). Explains many market failures.

---

## Field Map

```
FIELD MAP WITH CROSS-LINKS:

MICROECONOMICS                         GAME THEORY
─────────────────────────────          ─────────────────────────────
Consumer theory → demand curves        Static: Nash equilibrium
Producer theory → supply curves        Dynamic: SPE, backward induction
Competitive equilibrium                Bayesian: BNE (incomplete info)
  └→ First Welfare Theorem             Evolutionary: ESS, replicator dyn.
Monopoly, oligopoly → market power     Cooperative: core, Shapley value
Information economics:                       │
  Adverse selection (Akerlof)               │ "given rules → predict play"
  Moral hazard (principal-agent)            ▼
  Signaling (Spence)              ←── feeds types/strategies into ───→
Externalities → Pigouvian tax
Public goods → free rider                MECHANISM DESIGN
  └→ needs mechanism design ──────→  ──────────────────────────────
                                       "design rules to achieve outcome"
         ▲                             Revelation principle (DSIC / BIC)
         │                             VCG: efficient allocation
  micro foundation                     Myerson: revenue-optimal auction
         │                             DA / TTC: stable/Pareto matching
MACROECONOMICS                         Arrow impossibility: social choice
─────────────────────────────
IS-LM → AD-AS short run                INFORMATION ECONOMICS bridges:
Solow → long-run growth                Micro ──→ private types as inputs
DSGE → NK business cycles              Game theory: Bayesian games
Taylor rule, ZLB, QE                   Mechanism design: revelation principle
Exchange rates, trilemma               Macro: credit market failures
```

---

## Module Map

| File | Topic |
|------|-------|
| `01-MICROECONOMICS.md` | Consumer/producer theory, markets, equilibrium, welfare, market failures |
| `02-GAME-THEORY.md` | Normal/extensive form games, Nash equilibria, backward induction, repeated games |
| `03-MECHANISM-DESIGN.md` | Revelation principle, VCG, auctions, matching, Shapley value |
| `04-MACROECONOMICS.md` | GDP, monetary/fiscal policy, growth models, business cycles |

---

---

## Decision Cheat Sheet

| Goal | Tool | Where covered |
|------|------|---------------|
| Model a single agent's optimal choice | Utility/profit maximization (micro) | 01-MICROECONOMICS |
| Model several agents choosing simultaneously | Normal-form game, Nash equilibrium | 02-GAME-THEORY |
| Model sequential strategic decisions | Extensive-form game, SPE, backward induction | 02-GAME-THEORY |
| Model agents with private information (types) | Bayesian game, BNE | 02-GAME-THEORY |
| Design rules to achieve a social objective | Mechanism design, revelation principle | 03-MECHANISM-DESIGN |
| Maximize seller revenue from an auction | Myerson optimal auction (virtual valuations) | 03-MECHANISM-DESIGN |
| Allocate objects stably/efficiently | Gale-Shapley DA, Top Trading Cycles | 03-MECHANISM-DESIGN |
| Attribute value fairly to coalition members | Shapley value | 03-MECHANISM-DESIGN |
| Model market failure from information gaps | Adverse selection, signaling, moral hazard | 01-MICROECONOMICS |
| Explain aggregate output, inflation, cycles | IS-LM, AS-AD, Solow, Taylor rule | 04-MACROECONOMICS |
| Correct externalities | Pigouvian tax, Coase theorem | 01-MICROECONOMICS |

---

## Common Confusion Points

**Game theory vs decision theory**: Decision theory is single-agent optimization under uncertainty (no strategic opponent). Game theory models multiple agents whose payoffs depend on each other's choices. When you have one optimizing agent and nature draws states: decision theory. When outcomes depend on other rational agents' strategies: game theory.

**Mechanism design vs market design**: Mechanism design is the theoretical framework (revelation principle, DSIC, VCG). Market design is the applied discipline — using mechanism design tools for real markets (kidney exchange, spectrum auctions, school choice). Roth (Nobel 2012) built market design from mechanism design theory.

**Micro vs macro boundaries**: Macroeconomics is not simply "aggregated microeconomics." Aggregation creates emergent properties: coordination failures, liquidity traps, self-fulfilling expectations, nominal rigidities. DSGE models try to provide micro foundations for macro but require additional assumptions (sticky prices, financial frictions) that don't flow from standard micro.

**Nash equilibrium is not unique, optimal, or stable in general**: Most games have multiple Nash equilibria. NE says nothing about which equilibrium is reached (focal points, refinements needed). NE is not Pareto optimal (Prisoner's Dilemma: unique NE is Pareto dominated). NE is not a stable attractor in general (finding NE is PPAD-complete; best-response dynamics need not converge).

**Mechanism design vs regulation**: Mechanism design assumes the planner can commit to rules and agents respond rationally. Real-world regulation faces non-commitment, bounded rationality, political constraints. VCG is theoretically optimal but rarely deployed as written because of budget imbalance and computational complexity.

---

## Historical Arc

```
1776: Adam Smith — Wealth of Nations (invisible hand, specialization)
1890: Marshall — Principles of Economics (supply and demand diagrams)
1938: Hicks, Allen — formal consumer theory (ordinal utility)
1944: von Neumann & Morgenstern — Theory of Games and Economic Behavior
1950: Nash — Nash equilibrium (dissertation, 21 years old)
1951: Arrow — impossibility theorem (no perfect voting system)
1954: Arrow-Debreu — general equilibrium existence (fixed-point theorem)
1957: Samuelson — revealed preference, foundations of economic analysis
1960: Coase — externalities and property rights (Coase theorem)
1963: Akerlof (1970 paper published) — market for lemons (adverse selection)
1970: Harsanyi — Bayesian games, incomplete information
1973: Spence — signaling (education as signal)
1974: Myerson — mechanism design, revelation principle
1979: Vickrey-Clarke-Groves — VCG mechanism
1994: Nash, Harsanyi, Selten — Nobel (game theory)
1996: Vickrey, Mirrlees — Nobel (mechanism design in taxation)
2001: Akerlof, Spence, Stiglitz — Nobel (information asymmetry)
2002: Kahneman — Nobel (behavioral economics, prospect theory)
2007: Hurwicz, Maskin, Myerson — Nobel (mechanism design)
2012: Roth, Shapley — Nobel (stable matching, market design)
2014: Tirole — Nobel (market power, regulation)
2016: Hart, Holmström — Nobel (contract theory)
2020: Milgrom, Wilson — Nobel (auction theory, spectrum auction design)
```
