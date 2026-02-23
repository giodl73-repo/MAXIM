# Session 18 — Economics & Game Theory

**Date:** 2026-02-22
**Track:** Social Sciences — Decision Theory & Strategic Interaction

---

## What This Session Covers

Economics is the study of how agents with competing interests and limited information make decisions and how markets aggregate those decisions. Game theory is the mathematical framework for strategic interaction. Mechanism design inverts the problem: given a desired outcome, design the rules that achieve it. This is directly relevant to anyone building systems where rational (or near-rational) agents interact.

---

## Module Index

| File | Topic | Status |
|------|-------|--------|
| `economics/00-OVERVIEW.md` | Field map, why engineers care, historical arc | ✅ |
| `economics/01-MICROECONOMICS.md` | Consumer/producer theory, equilibrium, welfare, market failures, information economics | ✅ |
| `economics/02-GAME-THEORY.md` | Nash equilibrium, Prisoner's Dilemma, backward induction, SPE, repeated games, evolutionary GT | ✅ |
| `economics/03-MECHANISM-DESIGN.md` | Revelation principle, VCG, auctions, Myerson optimal auction, stable matching, Shapley value | ✅ |
| `economics/04-MACROECONOMICS.md` | GDP accounting, IS-LM, AS-AD, monetary policy, Taylor rule, Solow growth, endogenous growth | ✅ |

---

## Learning Arc

```
Individual agents (utility max, profit max) (01)
  │
  └─→ Strategic interaction (game theory) (02)
          │
          └─→ Design rules for strategic agents (mechanism design) (03)
                    │
                    └─→ Aggregate market outcomes (macroeconomics) (04)
```

---

## Key Mental Models

**Incentive compatibility is the fundamental constraint.** Any system where agents have private information and self-interested behavior must be designed so that truthful behavior is optimal (DSIC) or approximately optimal. Revelation principle: restrict to direct, truthful mechanisms without loss of generality.

**Nash equilibrium is not necessarily efficient.** Prisoner's Dilemma: individual rationality → collective irrationality. Market failures (externalities, public goods, information asymmetry) mean competitive equilibrium ≠ optimum. Mechanism design bridges the gap.

**Price = marginal cost at optimum.** In competitive markets this is achieved automatically. Any departure (monopoly, tax, externality) creates deadweight loss. Policy instruments: taxes (Pigouvian), subsidies, quotas, property rights (Coase), public provision.

---

## MIT / Math Connections

- **Fixed-point theorems:** Nash existence uses Kakutani fixed-point (generalization of Brouwer). Social choice theory (Arrow's theorem) is combinatorial math
- **Optimization under constraints:** Lagrangian duality in consumer theory; KKT conditions for firm problems
- **Information theory:** Adverse selection = information asymmetry. Mechanism design = optimal information revelation. MDL criterion ≈ model selection in economics
- **Probability:** Bayesian games require posterior updating; Harsanyi types are formal probability spaces
- **Linear algebra:** IS-LM is a linear system. Solow model is a nonlinear ODE. Input-output models use matrix inversion

---

## Bridges to Software / Systems

| Economics concept | Systems / tech application |
|------------------|---------------------------|
| Vickrey (2nd price) | eBay auctions, early internet ad auctions |
| VCG mechanism | Google Ads backbone (approximate GSP); 5G spectrum auctions |
| Gale-Shapley stable matching | AWS EC2 spot instance markets, medical residency NRMP |
| Shapley value | SHAP ML interpretability; cost-sharing in distributed systems |
| Two-sided markets | Airbnb, Uber, App Store (platform pricing) |
| Network effects | WhatsApp, LinkedIn, Bitcoin (DAU × active connections = value) |
| Mechanism design / IC | Blockchain consensus incentives (Ethereum MEV, validator rewards) |
| Moral hazard | SaaS billing models; unlimited vs metered plans |
| Adverse selection | Crypto: anonymous transactions; insurance products; API terms |
| Taylor rule | How Fed sets interest rates → VC discount rates → startup valuations |
