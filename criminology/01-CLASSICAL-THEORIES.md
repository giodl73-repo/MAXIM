# Classical and Rational Choice Theories

## The Big Picture

**Decision-theory bridge:** Classical criminology is mechanism design in reverse — it asks what punishment parameters (certainty, severity, swiftness) push the expected-utility calculation below zero for a rational agent. The model is precisely EU(crime) = p(detection) × U(punishment) + (1-p(detection)) × U(gain), which is von Neumann-Morgenstern expected utility under uncertainty. Beccaria's insight that certainty dominates severity maps to discounted future costs: hyperbolic discounting steeply devalues distant punishments, so p(detection) — which determines whether punishment is immediate or distant — is the dominant term. The policy implication (invest in detection over sentence length) follows directly from the discounting structure of the utility function, not from intuition.

Classical criminology grounds crime explanation in economics: crime is a choice made by a rational actor weighing expected benefits against expected costs. Deterrence policy flows directly from this model -- manipulate the cost side of the ledger and behavior changes.

```
+------------------------------------------------------------------+
|              CLASSICAL CRIMINOLOGY LANDSCAPE                     |
+------------------------------------------------------------------+
|                                                                  |
|  PHILOSOPHICAL ROOTS           DECISION MODEL                    |
|  ------------------            -------------                     |
|  Enlightenment (Locke,         Expected Utility:                 |
|  Rousseau, Montesquieu)        EU = p(caught) x severity         |
|                                    - benefit of crime            |
|  Social Contract theory        If EU(crime) > EU(no crime):      |
|  -- punishment is justified    --> offend                        |
|     only to protect society                                      |
|                                                                  |
|  KEY TEXTS                     MODERN DESCENDANTS                |
|  ---------                     -----------------                 |
|  Beccaria: Dei delitti e        Routine Activity Theory          |
|   delle pene (1764)            Rational Choice Theory (Clarke)   |
|  Bentham: Panopticon (1791)    Situational Crime Prevention      |
|  Bentham: Intro to Principles  Deterrence Theory (Nagin)         |
|   of Morals & Legislation      Behavioral economics critiques    |
+------------------------------------------------------------------+
```

---

## Cesare Beccaria (1764)

*On Crimes and Punishments* is the founding text. Beccaria was 26 when he published it, drawing on Enlightenment philosophy to systematically attack the arbitrary, brutal, and corrupt criminal justice of ancien regime Europe.

### Core Propositions

```
  BECCARIA'S SYSTEM
  =================

  1. CERTAINTY > SEVERITY
     A moderate punishment swiftly applied deters more
     than a severe punishment rarely applied.

  2. PROPORTIONALITY
     Punishment must fit the crime.
     Disproportionate punishment is both unjust and
     counterproductive (destroys compliance incentive).

  3. SWIFTNESS
     Delay between crime and punishment weakens the
     association in the offender's mind.

  4. PUBLICITY
     Public knowledge of crimes AND punishments is
     prerequisite for deterrence to work.
     Secret proceedings undermine the system.

  5. NO TORTURE
     Torture to extract confessions is epistemically
     and morally bankrupt.
     Truth is not pain-indexed.

  6. RULE OF LAW
     Judges interpret law, not make it.
     Certainty requires legislative clarity.
```

### Legacy

Beccaria directly influenced Jefferson, Hamilton, and Madison. The 8th Amendment's "cruel and unusual punishment" clause is Beccarian. The entire Enlightenment reform movement in criminal law traces to this pamphlet.

---

## Jeremy Bentham (1748-1832)

Bentham operationalized Beccaria through utilitarianism and the Panopticon.

### Felicity Calculus

```
  BENTHAM'S COST-BENEFIT MODEL
  ============================

  Net Pleasure of Crime =
    (Intensity + Duration + Certainty + Propinquity
     + Fecundity + Purity + Extent of pleasure)
    MINUS
    (same dimensions of pain from punishment)

  Dimensions of pain/pleasure:
  +------------+------------------------------------------+
  | Intensity  | How strong is the sensation?             |
  | Duration   | How long does it last?                   |
  | Certainty  | How probable is it to occur?             |
  | Propinquity| How near in time? (proximity)            |
  | Fecundity  | Does it produce more pleasure/pain?      |
  | Purity     | Is it unmixed with opposite sensation?   |
  | Extent     | How many people does it affect?          |
  +------------+------------------------------------------+

  Key insight: Certainty dimension dominates.
  Distant, uncertain punishments barely register.
```

### The Panopticon

```
  +---------------------------+
  |         GUARD TOWER       |
  |         (central)         |
  |        / | | | \          |
  |       /  | | |  \         |
  |      v   v v v   v        |
  |    [C] [C] [C] [C] [C]    |  C = Cell
  |                           |
  |  Guard may or may not     |
  |  be watching any cell.    |
  |  Inmates can't tell.      |
  |  But they act as if       |
  |  always watched.          |
  +---------------------------+

  Foucault's critique: The Panopticon is the metaphor
  for all modern surveillance/discipline -- not just prison.
  Power operates through internalized surveillance.
```

---

## Deterrence Theory: Formal Structure

Deterrence is the behavioral mechanism through which punishment reduces crime.

### Types of Deterrence

```
  +---------------------------+-----------------------------+
  |   SPECIFIC DETERRENCE     |   GENERAL DETERRENCE        |
  +---------------------------+-----------------------------+
  |  Target: offender who     |  Target: general population |
  |  was caught and punished  |  who observes punishment    |
  |                           |                             |
  |  Mechanism: "I don't      |  Mechanism: "I won't risk   |
  |  want that again"         |  what happened to them"     |
  |                           |                             |
  |  Empirical evidence:      |  Empirical evidence:        |
  |  WEAK -- recidivism       |  WEAK for severity;         |
  |  rates high               |  MODERATE for certainty     |
  +---------------------------+-----------------------------+

  MARGINAL DETERRENCE:
  Does an additional unit of punishment deter an additional
  unit of crime? This is the policy-relevant question.
  Evidence: marginal deterrence of certainty is positive;
            marginal deterrence of severity is near-zero.
```

### Daniel Nagin's Synthesis (modern consensus)

```
  DETERRENCE EVIDENCE BASE (Nagin, 2013)
  =======================================

  Certainty of punishment:
    Effect on crime: SUBSTANTIAL
    Evidence quality: HIGH
    Mechanism: Immediate apprehension risk changes decisions

  Severity of punishment:
    Effect on crime: WEAK
    Evidence quality: MODERATE
    Mechanism: Distant, discounted -- hyperbolic discounting
               means future punishments are steeply devalued

  Swiftness of punishment:
    Effect on crime: MODERATE
    Evidence quality: LOWER
    Mechanism: Temporal proximity strengthens association

  Key equation:
    Deterrence = f(certainty) >> f(severity)
```

---

## Rational Choice Theory (Clarke & Cornish)

The 1985 formalization by Clarke and Cornish extended classical deterrence into a full decision-theory model.

### The Choice Model

```
  INVOLVEMENT DECISIONS (big picture choices)
  ============================================

  Background factors:
  - Needs (money, status, excitement)
  - Previous learning
  - Values, attitudes

  Readiness to offend
  (standing willingness to commit crime type X)
            |
            v
  EVENT DECISIONS (in-the-moment choices)
  ========================================

  Situational factors:
  - Perceived effort
  - Perceived risk
  - Perceived rewards
  - Perceived excuses/justifications

         |         |         |
         v         v         v
      Commit    Abort    Displace
     the crime  attack   to easier
                          target
```

### Crime-Specific Decision Scripts

A key insight: decision scripts are crime-specific. A residential burglar uses different decision criteria than a bank robber. "Rational choice" doesn't mean identical calculation -- it means purpose-specific cost/benefit logic.

```
  Residential Burglary Decision Script:
  - Is there a car in the driveway? (occupancy signal)
  - Are there neighbors visible?
  - Is there an alarm system?
  - How quickly can I exit?
  - What is the likely yield?

  vs.

  Fraud/Embezzlement Decision Script:
  - Will auditors notice?
  - How long before detection?
  - Can I blame a system error?
  - What is my exit strategy?
```

---

## Routine Activity Theory (Cohen & Felson, 1979)

Crime = motivated offender + suitable target + absence of capable guardian, converging in time and space.

```
+--------------------------------------------------------------+
|              ROUTINE ACTIVITY TRIANGLE                       |
+--------------------------------------------------------------+
|                                                              |
|            MOTIVATED OFFENDER                                |
|                   /\                                         |
|                  /  \                                        |
|                 /    \                                       |
|                / CRIME \                                     |
|               /  OCCURS  \                                   |
|              /____________\                                  |
|    SUITABLE                ABSENCE OF                        |
|    TARGET                  GUARDIAN                          |
|                                                              |
|  Remove any one vertex --> crime prevented                   |
|                                                              |
|  Guardians: police, bystanders, neighbors, cameras,          |
|             door locks, alarm systems                        |
|                                                              |
|  Suitable target: VIVA model                                 |
|    Value       -- is it worth taking?                        |
|    Inertia     -- how heavy/portable?                        |
|    Visibility  -- can offender see it?                       |
|    Access      -- how easy to reach/escape?                  |
+--------------------------------------------------------------+
```

### Post-WWII Crime Rise: The Paradox

Cohen and Felson used their model to explain why crime rose after WWII despite rising prosperity -- exactly opposite to what strain theory would predict. Answer: rising prosperity created more suitable targets (more cars, TVs, portable goods) and disrupted routine guardianship (women entering workforce, changed household routines). Opportunity expanded faster than affluence reduced motivation.

---

## Situational Crime Prevention (Clarke)

The policy application of rational choice and routine activity: reduce crime by manipulating situations, not by changing people.

```
+------------------------------------------------------------------+
|         25 TECHNIQUES OF SITUATIONAL CRIME PREVENTION            |
|                    (Clarke & Eck, 2003)                          |
+------------------------------------------------------------------+
|                                                                  |
| INCREASE EFFORT     INCREASE RISK      REDUCE REWARDS           |
| ---------------     -------------      --------------           |
| Target harden       Extend guardianship Remove targets          |
| Control access      Natural surveillance Identify property      |
| Screen exits        Reduce anonymity    Remove inducements      |
| Deflect offenders   Utilize place mgrs  Disrupt markets         |
| Control tools/      Strengthen formal   Deny benefits           |
|   weapons           surveillance                                |
|                                                                  |
| REDUCE PROVOCATIONS   REMOVE EXCUSES                            |
| --------------------  ---------------                           |
| Reduce frustrations   Set rules                                 |
| Avoid disputes        Post instructions                         |
| Reduce arousal        Alert conscience                          |
| Neutralize peer       Assist compliance                         |
|   pressure            Control drugs/alcohol                     |
+------------------------------------------------------------------+
```

**Key principle**: Situational crime prevention targets specific crime types in specific places. A technique that prevents car theft at parking garages may not prevent domestic violence. No general panacea.

---

## Behavioral Economics Critiques

Classical rational choice assumes full rationality (utility maximization with stable preferences, accurate probability estimation). Behavioral economics erodes each assumption.

```
  CLASSICAL ASSUMPTION        BEHAVIORAL REALITY
  ====================        ==================

  Accurate probability        Probability weighting:
  estimation                  People overweight small probs
                              (lottery), underweight moderate
                              probs (typical crime detection)

  Stable time preferences     Hyperbolic discounting:
                              Immediate rewards valued
                              disproportionately over future
                              punishments -- "present bias"

  Consequentialist            Dual-process:
  deliberation                System 1 (fast/emotional) often
                              overrides System 2 (deliberative)
                              Most crime is impulsive

  Perfect information         Hot/cold empathy gap:
  about consequences          Decisions made while "hot"
                              (anger, intoxication, excitement)
                              do not reflect "cold" state
                              preferences
```

**Dual-process bridge:** The behavioral economics critique maps directly onto Kahneman's System 1 / System 2 distinction. Classical rational choice assumes System 2 (slow, deliberative, consequentialist) governs criminal decisions. The behavioral evidence shows System 1 (fast, emotional, present-biased) dominates in most street crime — especially under intoxication, anger, or peer pressure. This is not merely a psychological curiosity: it has architectural implications for intervention. If crime is System 1-driven, then deterrence via expected-penalty calculation (a System 2 mechanism) is largely inert, while environmental friction (removing opportunities before System 1 can act) and hot-state triggers (alcohol policy, de-escalation) are the effective levers. The Routine Activity and Situational Prevention frameworks are implicitly System 1-targeted; classical deterrence theory is implicitly System 2-targeted.

**Implication**: If most crime is impulsive rather than calculated, certainty of swift apprehension matters even more than deterrence theory already suggests -- but so do interventions that reduce hot-state triggers (alcohol policy, conflict de-escalation).

---

## Decision Cheat Sheet

| Concept | Key Insight | Policy Application |
|---------|-------------|-------------------|
| Beccaria's first principle | Certainty > severity | Invest in detection, not sentence length |
| Bentham's calculus | Pain must exceed pleasure | Proportional punishment |
| Specific deterrence | Punishment of offenders | Rehabilitation also works |
| General deterrence | Punishment of examples | High visible police presence |
| Routine activity | Opportunity = crime | Target hardening, CCTV |
| Situational prevention | Fix places, not people | CPTED, hot spots policing |
| Rational choice scripts | Crime-specific decisions | Crime-specific interventions |
| Hyperbolic discounting | Future punishment discounted | Swift, certain, moderate |

---

## Common Confusion Points

**Deterrence vs. Incapacitation**
Deterrence changes behavior through anticipated cost. Incapacitation prevents crime by physically removing the offender (incarceration). They are distinct mechanisms. Incapacitation works (the incarcerated don't offend in society) but is expensive and has no deterrent spillover to others.

**General vs. Absolute Deterrence**
General deterrence asks whether any punishment is better than none. Absolute deterrence asks whether the current level of punishment is optimal. Most evidence supports absolute deterrence (some deterrence exists) but not marginal deterrence (more severity beyond a threshold doesn't help).

**"Rational" Does Not Mean "Smart"**
Rational in the technical sense means purposive -- pursuing perceived goals. A heroin addict robbing a convenience store is "rational" in this sense (pursuing drug money) despite the high apprehension risk. The key variable is subjective perception of risk, which addicts systemically underestimate.

**Displacement vs. Diffusion**
Situational prevention may displace crime (move it elsewhere) rather than reduce it. But evidence also shows "diffusion of benefits" -- preventive effects spread beyond targeted areas/times. Both occur; net effect is usually positive.
