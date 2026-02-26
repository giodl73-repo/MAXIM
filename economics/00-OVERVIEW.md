# Economics & Game Theory — Overview

---

## Big Picture

<!-- @editor[diagram/P2]: Diagram lists items in a hierarchy but doesn't show how micro, game theory, mechanism design, and macro relate to each other — rework as layered system view showing information economics feeding into mechanism design, game theory underpinning market equilibria, etc. -->
```
ECONOMICS
  │
  ├── MICROECONOMICS — individual agents, markets
  │     Consumers (utility maximization)
  │     Firms (profit maximization)
  │     Markets (supply, demand, equilibrium, efficiency)
  │     Market failures (externalities, public goods, asymmetric info)
  │
  ├── GAME THEORY — strategic interaction
  │     Normal form games (Nash equilibrium)
  │     Extensive form games (backward induction)
  │     Cooperative games (coalitions, Shapley value)
  │     Repeated games (folk theorem, cooperation)
  │
  ├── MECHANISM DESIGN — "inverse game theory"
  │     Design rules of the game to achieve desired outcome
  │     Auctions, voting, matching, incentive compatibility
  │     Nobel 2007 (Hurwicz, Maskin, Myerson)
  │
  └── MACROECONOMICS — aggregate phenomena
        GDP, inflation, interest rates, business cycles
        Monetary/fiscal policy, growth theory
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

<!-- @editor[diagram/P2]: Field Map repeats the hierarchy pattern — three separate trees with no cross-links showing how game theory feeds mechanism design, how information economics bridges micro and mechanism design, etc. -->
```
MICROECONOMICS TREE:
  Consumer theory → demand curves
  Producer theory → supply curves, cost minimization
  Competitive equilibrium → first welfare theorem (Pareto efficiency)
  Monopoly, oligopoly → market power, deadweight loss
  Information economics → adverse selection, moral hazard, signaling
  Externalities → Pigouvian tax, Coase theorem
  Public goods → free rider problem, mechanism design needed

GAME THEORY TREE:
  Static games → Nash equilibrium, iterated dominance
  Dynamic games → backward induction, subgame perfect equilibrium
  Bayesian games → incomplete information, Bayesian Nash equilibrium
  Evolutionary games → evolutionary stable strategy (ESS)
  Cooperative games → core, Shapley value

MECHANISM DESIGN TREE:
  Social choice → Arrow impossibility, voting rules
  Revelation principle → truthful mechanisms
  VCG mechanism → efficient mechanism (public goods, combinatorial auctions)
  Myerson optimal auction → revenue maximization
  Matching theory → stable matching (Gale-Shapley)
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

## Historical Arc

```
<!-- @editor[structure/P1]: Missing Decision Cheat Sheet section — guide needs a "what do I use when" table (e.g., "need to model strategic agents → game theory", "need to design incentive-compatible rules → mechanism design") -->
<!-- @editor[structure/P2]: Missing Common Confusion Points section — natural gotchas include game theory vs decision theory, mechanism design vs market design, micro vs macro boundaries, Nash equilibrium misconceptions -->
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
