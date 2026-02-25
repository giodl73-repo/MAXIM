# Behavioral Ecology and Sociobiology

## The Big Picture

Behavioral ecology applies evolutionary theory to animal behavior, asking why natural selection produced the observed behavioral strategies. It emerged from the synthesis of ethology and ecology in the 1960s-70s (Hamilton, Trivers, Maynard Smith, Wilson) and treats behavior as an evolved phenotype subject to the same optimization logic as any other trait. The central concepts — kin selection, reciprocal altruism, honest signaling, ESS — form a rigorous mathematical framework.

```
BEHAVIORAL ECOLOGY CONCEPTUAL MAP
=====================================

INDIVIDUAL SELECTION:
  Maximize own fitness
  Foraging, territorial defense, predator avoidance

KIN SELECTION:
  Maximize inclusive fitness (own + relatives' fitness weighted by r)
  Hamilton's rule: rb > c
  Altruism toward relatives; explains eusociality

SEXUAL SELECTION:
  Mate choice + intrasexual competition
  Runaway selection, handicap principle, good genes

RECIPROCAL ALTRUISM:
  Cooperate with non-relatives when mutual benefit expected
  Tit-for-tat ESS in repeated games
  Reputation effects; punishment

EVOLUTIONARILY STABLE STRATEGY (ESS):
  Maynard Smith (1973): strategy stable against invasion by alternatives
  Game theory formalization of behavioral evolution
```

---

## Hamilton's Kin Selection

```
HAMILTON'S INCLUSIVE FITNESS THEORY (1964)
============================================

PROBLEM: Why do individuals help relatives at cost to themselves?
CLASSICAL ANSWER: "For good of the species" (group selection)
HAMILTON'S ANSWER: Selection acts on inclusive fitness
                   (direct + indirect components)

INCLUSIVE FITNESS:
  W_inclusive = W_direct + W_indirect
  W_direct: own reproductive success
  W_indirect: fitness effect on relatives, weighted by r

HAMILTON'S RULE:
  rb > c
  r = coefficient of relatedness (probability of sharing allele by descent)
  b = benefit to recipient (fitness units)
  c = cost to actor (fitness units)

  Gene for altruism spreads when: rb > c

  RELATEDNESS COEFFICIENTS (diploid outbred):
  Full sibling:    r = 0.5
  Half sibling:    r = 0.25
  First cousin:    r = 0.125
  Parent-child:    r = 0.5
  Identical twin:  r = 1.0

  EXAMPLE:
  A worker bee helps the queen raise 100 new workers (benefit b=100)
  At cost of not reproducing herself (cost c=50)
  r = 0.5 (full sisters in monandrous colony)
  rb = 0.5 x 100 = 50 > c = 50 -> MARGINAL (barely)
  With r = 0.75 (haplodiploidy): rb = 75 > 50 -> spread more easily

LIMITS OF KIN SELECTION:
  Polyandry: queen mates with multiple males -> r(sisters) < 0.5
    Reduces inclusive fitness advantage
  Boomsma (2009): eusociality requires lifetime monogamy at founding
    -> r maintained high enough
  Doesn't explain all social behavior (reciprocal altruism for non-kin)
```

---

## Reciprocal Altruism and Cooperation

```
RECIPROCAL ALTRUISM (Trivers 1971)
=====================================

PROBLEM: Non-related animals cooperate; kin selection doesn't explain
ANSWER: Temporal trade: help now; benefit later (when partner returns favor)

CONDITIONS FOR RECIPROCAL ALTRUISM:
  1. Repeated interactions (same partners)
  2. Benefit to receiver > cost to actor (creates surplus)
  3. Ability to recognize cheaters
  4. Punishment of cheaters (or shunning)

GAME THEORY FORMALIZATION:
  Prisoner's Dilemma:
    Two players: each can Cooperate (C) or Defect (D)
    Payoff matrix (row player):
             C            D
      C  (R,R)=3,3   (S,T)=0,5
      D  (T,S)=5,0   (P,P)=1,1
      T>R>P>S; 2R>T+S

    Single game: Defect dominates (D beats C regardless of partner)
    Repeated game: TIT-FOR-TAT (TFT) can be stable
      TFT: cooperate first; then copy partner's last move
      Axelrod tournament (1984): TFT won 200+ strategies

TIT-FOR-TAT PROPERTIES:
  Nice: cooperate first (not provocable without cause)
  Retaliatory: punish defection immediately
  Forgiving: return to cooperation after one retaliation
  Clear: easy to understand -> partner can model you

EVOLUTIONARY STABILITY:
  TFT stable in high r (repeated interaction) environments
  GRIM TRIGGER: cooperate until first defection; defect forever
    -> stable but not forgiving
  WIN-STAY-LOSE-SHIFT: better than TFT in noisy environments

VAMPIRE BAT EXAMPLE (Wilkinson 1984):
  Vampire bats (Desmodus rotundus): nightly blood meals; miss meals -> starve
  Roost mates regurgitate blood to hungry neighbors
  Analysis:
    Blood shared: preferentially to close kin + regular reciprocators
    Blood withheld: from those who didn't share previously
    -> BOTH kin selection and reciprocal altruism operating simultaneously
```

---

## Evolutionary Stable Strategies (ESS)

```
EVOLUTIONARILY STABLE STRATEGY (ESS)
=======================================

DEFINITION (Maynard Smith + Price 1973):
  A strategy S is ESS if, when adopted by most of the population,
  no rare alternative strategy can invade.

FORMALLY: S is ESS if for all T ≠ S:
  E(S,S) > E(T,S)    [S does better than T in population of S]
  OR E(S,S) = E(T,S) and E(S,T) > E(T,T)  [S does better when T rare]

HAWK-DOVE GAME:
  Two strategies: HAWK (always escalate) and DOVE (display; retreat if escalated)
  Resource value: V; Injury cost: C (assume V < C)
  Payoffs:
    H vs H: (V-C)/2 = -2 (if V=2, C=6)
    H vs D: H gets V = 2; D gets 0
    D vs H: D gets 0; H gets 2
    D vs D: V/2 = 1

  PURE ESS: none (Hawk beats Dove but Hawks get hurt by other Hawks)
  MIXED ESS: proportion p of Hawks at which E(H,mix) = E(D,mix)
    p = V/C (e.g., p = 2/6 = 1/3)
    ESS: 1/3 Hawks, 2/3 Doves (or each individual plays H 1/3 of time)

  APPLIED TO: sexual conflict, territorial behavior, foraging strategy,
              antibiotic resistance evolution (same mathematics)
```

---

## Optimal Foraging Theory

```
OPTIMAL FORAGING THEORY (OFT)
================================

PREY MODEL (Charnov 1976 formalization):
  Ranking prey types by PROFITABILITY: E_i / h_i
    E_i = energy from prey type i
    h_i = handling time for prey type i
  Decision: include prey type if:
    E_1/(h_1 + s_1) < E_i/h_i
    Where s_1 = search time for type 1 (best prey)
  When best prey abundant (s_1 small): exclude lower-ranked prey
  When best prey scarce (s_1 large): include lower-ranked prey
  PREDICTION: specialization when prey abundant; generalism when scarce

MARGINAL VALUE THEOREM (Charnov 1976):
  Question: When should animal leave a food patch?
  Prediction: Leave when instantaneous capture rate = average capture rate
    in the environment
  Graphical: gain function (cumulative food vs time in patch)
    Optimal departure = tangent from origin touches curve
  PREDICTIONS:
    Stay longer when: travel time between patches is long
    Stay longer when: poor habitat (low average rate)
    Leave earlier when: good patch (when marginal rate drops quickly)

  TESTED: Great tits (Lechebruck); starlings (Kacelnik);
          oystercatchers; shore crabs; all roughly confirm

RISK-SENSITIVE FORAGING:
  Energy budget rule (Stephens 1981):
    Below budget: prefer variance (gamble for large payoff)
    Above budget: avoid variance (take certain smaller reward)
  Starvation risk changes optimal strategy
  Yellow-eyed juncos: switch from low-variance to high-variance diet
    as temperature drops (energy budget more precarious)
```

---

## Mating Systems and Sexual Conflict

```
MATING SYSTEM ECOLOGY
=======================

PARENTAL INVESTMENT THEORY (Trivers 1972):
  The sex that invests MORE in offspring will be choosier
  The sex that invests LESS will compete for mates
  Usually: females invest more (eggs > sperm; often gestation/incubation)
  -> Females: choosy; Males: competitive

  BUT: paternal care can flip this
    In species with male-only care (some fish, many birds partially):
      Male investment > female -> male more choosy; female more competitive
  Pipefish (Syngnathus): males pregnant; females compete
  Jacanas: females defend territories; males incubate

RESOURCE DEFENSE POLYGYNY:
  Males control resources (territories) females need
  Female choice: choose male with best resource (not best genes per se)
  -> Male quality = quality of territory
  Red-winged blackbird (Agelaius phoeniceus):
    Polygynous; 1 male: 3-8 females on territory
    Female choice: marsh territory quality, not male ornamentation alone

SEXUAL CONFLICT:
  Male and female fitness optima can diverge
  Classic example: polyandry vs monogamy
    Male: prefers to maximize matings (polyandry)
    Female: prefers male parental investment (monogamy)
  Conflict resolution: coercive mating; harassment; counter-resistance
  Waterfowl: forced copulation -> arms race (female genital morphology
    counter-adapts: corkscrew vagina; dead-end pouches)
  Male seminal fluid proteins (Drosophila): toxic to female (extends
    time before female re-mates; also shortens female lifespan)
```

---

## Altruism: The Hard Problem

```
THE EVOLUTION OF ALTRUISM
===========================

PROBLEM: Altruistic behavior (costly to actor; beneficial to recipient)
         should be eliminated by selection (selfish alternatives do better)

THREE SOLUTIONS:
1. KIN SELECTION: indirect fitness via relatives (Hamilton 1964)
2. RECIPROCAL ALTRUISM: temporal trade with non-kin (Trivers 1971)
3. DIRECT FITNESS: "altruism" benefits the actor directly
   Alarm calls: bring predator attention to callers? OR reduces predation
                via dilution + warning own kin? (usually kin selection)

GROUP SELECTION (now rarely accepted in strong form):
  Classic: altruism for good of group
  Problem: within-group selection eliminates altruists
  Modern multi-level selection: not a separate mechanism;
    mathematically equivalent to inclusive fitness under most conditions

APPARENT ALTRUISM IN NATURE:
  Sterile castes (ants, bees): kin selection (r=3/4 in haplodiploid)
  Vampire bat regurgitation: kin selection + reciprocal altruism
  Sentinel behavior (meerkats): kin selection; sentry calls benefit relatives
    AND sentry reduces own risk (predator sees it exposed -> flee faster?)
  Helpers at the nest (see ornithology/06): kin selection + direct benefits

ALTRUISM vs MUTUALISM:
  Mutualism: both parties benefit (not altruism)
  Altruism: one party bears net cost
  Many "altruistic" behaviors reanalyzed as mutualism once hidden benefits found
```

---

## Social Organization

```
ANIMAL SOCIAL ORGANIZATION
============================

SOLITARY:
  Most animals; benefits of sociality < costs of competition/disease

AGGREGATION:
  Passive: food/habitat concentration (not social bond)
  Active: dilution effect (each individual safer in larger group)

GROUP LIVING: kin groups, mating pairs, cooperative groups
  COSTS:
    Resource competition (food, territory, mates)
    Disease transmission
    Conspicuousness to predators
    Increased competition for reproduction
  BENEFITS:
    Predator dilution (Hamilton's selfish herd)
    Collective vigilance (each individual can scan less)
    Cooperative foraging (some predators)
    Cooperative defense (mobbing, group antipredator)
    Information center (colony nesters; track food patches)

EUSOCIALITY (see entomology/04):
  Extreme social organization with reproductive division of labor
  Only 15+ independent origins; most in Hymenoptera

FISSION-FUSION DYNAMICS:
  Group size varies with context; individuals move between groups
  Examples: dolphins, elephants, chimpanzees, wolves
  Cognitive demand: recognize many individuals + their relationships
  Suggested link: fission-fusion -> social complexity -> brain size
    (Social Brain Hypothesis: Dunbar 1998)
```

---

## Decision Cheat Sheet

| Concept | Mathematical core | Classic example |
|---------|------------------|-----------------|
| Hamilton's rule | rb > c | Worker bee altruism |
| Reciprocal altruism | Repeated Prisoner's Dilemma; TFT ESS | Vampire bat blood sharing |
| ESS | No alternative strategy can invade | Hawk-Dove mixed equilibrium |
| Optimal foraging (prey model) | Include prey if E_i/h_i > E_best/(h_best+s_best) | Great tit prey selection |
| Marginal value theorem | Leave patch when marginal rate = average rate | Oystercatcher mussel handling |
| Sexual selection | Parental investment asymmetry -> sex roles | Red-winged blackbird polygyny |

---

## Common Confusion Points

**Inclusive fitness ≠ total fitness**: Inclusive fitness is the sum of direct fitness (own reproduction) and indirect fitness (fitness of relatives weighted by r). It is a property of an individual's gene for a behavior, not of the individual. Hamilton's rule says: spread of a gene for altruism requires rb > c, where both r and b are the gene's effects on the lineage.

**Group selection is not wrong, just rarely important**: Group selection (higher-level selection favoring traits good for the group but not the individual) can occur in principle and mathematically. It is usually weak compared to within-group selection. Modern "multi-level selection theory" (Wilson, Sober) attempts to rehabilitate it, but the inclusive fitness framework (Price equation) is usually simpler and equivalent.

**ESS is not the same as optimal strategy**: An ESS is stable against invasion, not necessarily the strategy that maximizes individual fitness. The Hawk-Dove mixed ESS is stable but both Hawks and Doves get lower fitness than they would if they could coordinate to be all-Doves. ESS describes what selection produces in frequency-dependent contexts.

**Reciprocal altruism requires repeated interaction**: TFT is not stable in one-shot encounters (Defect is dominant). The whole framework requires repeated interactions with the same partner + partner recognition. In anonymous populations with no repeated encounters, reciprocal altruism cannot evolve.

**"Sociobiology" as a term**: Wilson's (1975) book "Sociobiology" applied evolutionary theory to human social behavior, causing political controversy. The science (applying evolution to behavior) is now called "behavioral ecology" or "evolutionary psychology" for humans. The mathematics and principles are valid; the political controversy was about specific applications to humans.
