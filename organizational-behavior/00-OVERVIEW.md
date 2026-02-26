# Organizational Behavior — Field Map, Theory History, Evidence Base

## The Big Picture

Organizational behavior (OB) is the systematic study of how individuals, groups, and organizations behave. It's interdisciplinary — drawing from psychology, sociology, economics, and anthropology — and it has a mixed evidence base. Some core findings are rock-solid (goal-setting works, psychological safety matters); others are replication-crisis casualties (many "studies show" claims from the 1970s-90s don't hold up).

```
OB LEVELS OF ANALYSIS
======================

ENVIRONMENT
(economy, industry, institutions, culture)
         |
ORGANIZATION
(structure, culture, strategy, resources)
         |
GROUPS / TEAMS
(norms, cohesion, leadership, dynamics)
         |
INDIVIDUAL
(personality, motivation, perception, attitudes)

KEY INSIGHT: Effects operate in both directions.
 Individual behavior shapes group norms → group norms shape individuals.
 Org culture shapes individual behavior → individual leaders shape culture.
 Most OB models are multi-level; the error is treating individual-level
 findings as if they explain org-level outcomes and vice versa.

ADJACENT DISCIPLINES:
 Industrial-Organizational (I-O) Psychology: individual/group focus;
  rigorous psychometric tradition; selection, training, performance
 Organizational Sociology: macro-level; institutions, fields, legitimacy
 Strategic Management: org + environment; competitive dynamics
 Behavioral Economics: decision-making under uncertainty; cognition
 Management Accounting: incentive design; principal-agent problems
```

---

## From Engineering Org Experience to OB as a Discipline

If you run engineering organizations, you are already practicing applied OB — the academic field is the systematic formalization of what you observe empirically. The value of the formal study is not novelty but precision: it names the mechanisms, identifies which interventions have replicable effects vs. which are organizational mythology, and provides a framework for diagnosing failure modes rather than attributing them to individual character.

**The org you manage is a complex adaptive system.** Individual behavior is shaped by incentive structures, social norms, information flows, and role constraints in ways that make individual-level explanations systematically misleading. When a team's velocity drops, the explanation is rarely "people stopped caring" — it is more likely a coordination overhead increase, an unclear priority signal, a loss of psychological safety after a high-profile failure, or a change in task interdependence structure. OB provides the vocabulary to reason about those system-level causes rather than defaulting to person-level attribution.

**The replication crisis is not an abstraction — it is a budget allocation problem.** A significant fraction of management interventions you might consider (MBTI for team composition, Maslow-based motivation programs, Situational Leadership training) have weak or failed empirical support. Other interventions (goal-setting structured as OKRs, psychological safety investment, structured behavioral interviews for hiring) have strong meta-analytic evidence. OB's evidence hierarchy tells you where to put engineering management investment.

**The OB-economics interface is where your formal training is most applicable.** Principal-agent theory, tournament theory, efficiency wages, and transaction cost economics are the formal economic models underlying the management accounting intuitions you work with daily. SDT and equity theory are the behavioral corrections to those models: people are not narrow self-interest maximizers, and the behavioral departures are systematic and predictable. The interaction between economic incentive structures and intrinsic motivation crowding-out is the central design question for engineering performance management.

## History of Management Thought

```
MANAGEMENT THEORY GENEALOGY
==============================

SCIENTIFIC MANAGEMENT (Frederick Taylor, ~1900-1920):
 Core idea: work can be studied scientifically to find "one best way"
 Methods: time-and-motion study; task decomposition; piece-rate pay
 Assumptions: workers are lazy; respond only to economic incentives;
              management knows best; workers' job is to execute, not think
 Legacy: production efficiency; operations management; job design theory
 Problem: dehumanizing; ignores motivation, social dynamics, knowledge work
 Permanent contribution: systematic observation of work is valuable
 Henry Ford: Taylorism + mass production → vertically integrated factory

ADMINISTRATIVE MANAGEMENT (Henri Fayol, ~1916):
 Core idea: management functions and principles applicable universally
 14 Principles: division of labor, authority, discipline, unity of command,
  unity of direction, subordination, remuneration, centralization,
  scalar chain, order, equity, stability, initiative, esprit de corps
 Criticism: prescriptive; no empirical grounding; culturally bound
 Legacy: the language of management (span of control, chain of command)
  still largely Fayolian

BUREAUCRACY (Max Weber, ~1910-1920):
 Core idea: rational-legal authority as the efficient form of organization
 Features: written rules; specialized roles; hierarchy; impersonal
           application of rules; career advancement by merit
 Compared to: traditional authority (inherited), charismatic authority (person)
 Legacy: modern organizations ARE Weber's bureaucracy
 Problem: Weber described and praised it; he also feared it becoming an
  "iron cage" — the pathology of rules replacing judgment

HUMAN RELATIONS MOVEMENT (Elton Mayo, Hawthorne studies, ~1927-1932):
 Experiment: Western Electric Hawthorne plant, Cicero, IL
 Finding: manipulating physical working conditions (lighting) → changes
  in productivity didn't track physical changes
 Interpretation: social dynamics + being observed → workers perform better
 THE HAWTHORNE EFFECT: being studied changes behavior (now a methodological
  concern in all OB research, not just the original claim)
 Key insight: workers are social beings; relationships matter; management
  attention matters beyond pay and physical conditions
 Legacy: launched "human relations" school; management should consider
  worker attitudes, not just task efficiency
 Methodological critique: the studies were not well-controlled;
  the "Hawthorne effect" as originally claimed may be weaker than claimed

SYSTEMS THEORY (Katz & Kahn, ~1966):
 Core idea: organizations are open systems (input → transformation → output)
  interacting with their environment; not closed mechanical systems
 Key concepts: equifinality (multiple paths to same goal),
               homeostasis (tendency toward equilibrium),
               entropy (tendency toward disorder if not maintained)
 Legacy: contingency theory; sociotechnical systems; complexity theory

CONTINGENCY THEORY (~1960s-1970s, Joan Woodward; Burns & Stalker; Lawrence & Lorsch):
 Core idea: there is no "one best way"; effectiveness depends on fit
  between organization and its environment
 Key findings:
  Production technology → structure (Woodward: unit/mass/process production)
  Environmental uncertainty → org form (Burns/Stalker: mechanistic/organic)
  Differentiation vs integration (Lawrence/Lorsch: specialized units need
   coordination mechanisms that match their interdependence)
 Legacy: undermined universal prescriptions; encouraged situational thinking
```

---

## What Has Evidence — The Meta-Analytic View

```
EVIDENCE HIERARCHY IN OB
===========================

LEVELS OF EVIDENCE:
 Strong:   Meta-analysis of multiple RCTs or high-quality longitudinal studies
 Moderate: Multiple well-designed studies with replication
 Weak:     Single studies; self-report only; correlational; small samples
 Unreliable: Failed to replicate; p-hacking suspected; file drawer problem

REPLICATION CRISIS IN MANAGEMENT RESEARCH:
 ~2010+: Open Science movement exposed problems in social psychology
 Management research: similar issues; less visible but present
 Common problems:
  Researcher degrees of freedom: many analytical choices → cherry-picked
  Small samples: typical OB study N=200; low power for subtle effects
  Self-report bias: most OB measures = surveys; demand characteristics
  Publication bias: positive results published; nulls in file drawer
  Construct proliferation: too many similar constructs with different names

WHAT HAS STRONG EVIDENCE:
 Goal-setting works (Locke & Latham): specific + challenging goals
  → better performance than vague goals; meta-analytic effect size d≈0.68
 Psychometric predictors: cognitive ability (GMA) is the strongest single
  predictor of job performance (Schmidt & Hunter meta-analysis, 1998)
 Transformational leadership: positive correlation with performance outcomes
  (though effect sizes vary by context; meta-analysis: r≈0.44)
 Psychological safety (Edmondson): well-replicated; Google Project Aristotle
  confirmed it as key team effectiveness predictor
 Feedback and performance management: structured feedback → performance
  improvement (though 1/3 of feedback interventions → performance decrease)

WHAT IS CONTESTED OR WEAK:
 Myers-Briggs (MBTI): poor test-retest reliability; low predictive validity;
  psychologists largely reject it; management widely uses it anyway
 Maslow's hierarchy: virtually no empirical support for the hierarchy
  (needs don't activate in order); useful as a general list of needs,
  not as a developmental model
 Learning styles (visual/auditory/kinesthetic): no evidence that
  matching teaching to "style" improves learning
 Emotional intelligence as a leadership predictor: constructs overlap
  with personality; incremental validity over Big Five is limited
 Herzberg two-factor: methodological issues (attribution bias in design);
  motivators vs hygiene distinction = interesting framework, not reliable theory

WHAT IS SIMPLY OVERUSED:
 SWOT analysis: too general; no proven link to strategy quality
 7-S framework (McKinsey): useful checklist; not a predictive theory
 Most 2×2 matrices: useful communication; not empirical findings
```

---

## Organizational Culture

```
ORGANIZATIONAL CULTURE
========================

SCHEIN'S THREE LEVELS:
 Artifacts: visible structures and processes (behaviors, architecture,
  dress, language, stories — observable, surface)
 Espoused Values: stated strategies, goals, philosophies
  (what the organization SAYS it believes)
 Basic Assumptions: unconscious, taken-for-granted beliefs and values
  (the real culture; hard to surface; governs actual behavior)
 THE GAP: artifacts + espoused values often contradict basic assumptions
  "We value innovation" (espoused) vs. "innovation proposals are buried
   in process" (artifact) → basic assumption: safety over risk

HOFSTEDE DIMENSIONS (National Culture):
 Power Distance (PDI): acceptance of unequal power distribution
  High: Malaysia, Philippines, China; Low: Scandinavia, Austria
 Individualism-Collectivism (IDV): individual vs group orientation
  High IDV: US, UK; High collectivism: China, Japan, Latin America
 Uncertainty Avoidance (UAI): tolerance of ambiguity
  High: Greece, Japan, France; Low: Singapore, Jamaica, Denmark
 Masculinity-Femininity (MAS): achievement vs care orientation
  High MAS: Japan, Hungary; High FEM: Sweden, Norway
 Long-Term Orientation (LTO): future vs present/past orientation
  High: East Asian countries; Low: Pakistan, many African nations
 Indulgence vs Restraint (IVR): added later

CULTURE CHANGE:
 Schein: culture changes via:
  (1) Incremental: evolution via primary embedding mechanisms
      (what leaders pay attention to; how they react to crises;
       what they model; what they reward; criteria for selection/promotion)
  (2) Transformation: only occurs via founder/leadership replacement,
      organizational trauma, or merger/acquisition
 "Culture eats strategy for breakfast" (attributed to Drucker):
  overstated but captures: strategy implementation requires cultural alignment
  The complete version: culture eats strategy AND structure AND incentives
  if they are misaligned with the basic assumptions
```

---

## Evidence Strength Summary

| Theory / Construct | Evidence | Notes |
|---|---|---|
| Goal-setting (Locke & Latham) | Strong | d≈0.68; most replicated motivation finding |
| Psychological safety (Edmondson) | Strong | Large-scale replication; Google Project Aristotle |
| Cognitive ability (GMA) as job predictor | Strong | Best single predictor; often underused |
| Structured behavioral interview | Strong | r≈.51; far outperforms unstructured |
| Transformational leadership → performance | Moderate | r≈.44; inflated by common-method bias |
| Equity theory (underpayment effects) | Moderate | Underpayment robust; overpayment weaker |
| SDT / intrinsic motivation crowding-out | Moderate | Cross-cultural replication; some moderators disputed |
| Big Five personality → leadership | Moderate | Useful combined; modest individual effects |
| LMX differentiation effects | Moderate | Team-level effects well-documented |
| Expectancy theory (VIE) | Moderate | Strong theoretical logic; field replication mixed |
| Herzberg two-factor | Weak | Methodological artifact; useful heuristic only |
| Maslow hierarchy | Weak | No empirical support for activation sequence |
| Situational Leadership (D1-S4 matching) | Weak | Widely used; meta-analytic support absent |
| Myers-Briggs (MBTI) | Rejected | Poor test-retest; low predictive validity |
| Learning styles (VAK) | Rejected | No evidence that matching style improves learning |
| Emotional intelligence as leadership predictor | Contested | Construct validity problems; overlap with Big Five |

## The OB-Economics Interface

```
OB MEETS ECONOMICS — KEY BRIDGES
===================================

PRINCIPAL-AGENT THEORY:
 Principal: person who delegates work (shareholder, manager, employer)
 Agent: person who does work (CEO, employee, contractor)
 Problem: agent has private information; agent's interests ≠ principal's
 Solutions: monitoring (costly); incentives (align interests);
            screening (select agents with aligned interests)
 OB relevance: performance management, executive pay, franchise design,
               bonus structure — all are principal-agent problems
 Limitation: assumes narrow self-interest and external motivation;
             OB evidence: intrinsic motivation + social preferences matter

TRANSACTION COST ECONOMICS (Coase, Williamson):
 Question: why do firms exist? Why not all market transactions?
 Answer: transaction costs (search, negotiation, monitoring, enforcement)
 Firm boundary: bring activities in-house when market transaction costs
  exceed internal coordination costs
 OB relevance: org boundaries, outsourcing decisions, make-vs-buy
 Behavioral addition: bounded rationality (Herbert Simon) + opportunism
  explain why contracts are incomplete → hierarchy emerges

EFFICIENCY WAGE THEORY:
 Pay workers above market wage → reduces shirking (job worth keeping);
  attracts higher-ability workers; reduces turnover costs
 Evidence: large firms pay more; correlates with monitoring cost
 OB link: motivation ≠ purely effort; also selection and retention effects

TOURNAMENT THEORY:
 Large pay gaps between levels → high-effort competition for promotion
 Works when: performance is measurable; agents are risk-neutral; competitive
 Problem: sabotage of competitors (when promotion = relative performance);
           cooperation destroyed; risk-aversion by risk-averse employees
 Executive pay gaps in corporations have tournament theory support
 AND: executive pay often exceeds tournament incentive predictions → agency problem
```

---

## Common Confusion Points

**OB ≠ HR**:
HR (Human Resources) is an organizational function. OB is an academic field. HR departments use OB research and frameworks, but OB is broader — it includes organization design, strategy, culture, macro-organizational theory, all of which extend well beyond HR's functional remit.

**Hawthorne Effect ≠ "people work harder when watched"**:
The Hawthorne studies had multiple confounds. The "effect" has been re-analyzed multiple times. The strongest surviving claim is: being included in an experiment and receiving attention influences behavior. The simple "watched = harder" claim is overstated.

**Correlation ≠ causation — especially in OB**:
Most OB research is correlational. "Transformational leaders have better-performing teams" could mean: transformational leadership causes performance, OR high-performing teams are easier to lead transformationally, OR some third variable (org slack, talent density) causes both.

**Meta-analysis ≠ the final word**:
Meta-analyses aggregate multiple studies. If the input studies all have the same bias (self-report; selection bias; etc.), the meta-analysis inherits those biases. "Meta-analytic evidence" is better than a single study, but not a guarantee of truth.

---

## Decision Cheat Sheet

| You want to | Go to |
|---|---|
| Understand why engineers aren't performing | `01-MOTIVATION.md` — expectancy theory (E×I×V) diagnostic |
| Design a goal system that actually works | `01-MOTIVATION.md` — goal-setting theory; OKR failure modes |
| Understand why generous pay doesn't motivate | `01-MOTIVATION.md` — Herzberg hygiene factors; SDT crowding-out |
| Select the best leader for a role | `02-LEADERSHIP.md` — psychometric predictors; structured interview design |
| Understand why a charismatic leader is causing damage | `02-LEADERSHIP.md` — dark triad in executives |
| Diagnose why a team isn't performing | `03-TEAMS-GROUPS.md` — Hackman conditions; psychological safety assessment |
| Prevent groupthink on a high-stakes decision | `03-TEAMS-GROUPS.md` — Janis antecedents; premortem technique |
| Choose an org structure for a new program | `04-ORG-DESIGN.md` — Mintzberg configurations; Conway's Law |
| Analyze whether a product market is attractive | `05-STRATEGY.md` — Porter Five Forces |
| Evaluate why a capability is hard to copy | `05-STRATEGY.md` — VRIN analysis |
| Plan an organizational transformation | `06-CHANGE.md` — Kotter; Lewin; sensemaking |
| Understand why the Agile transformation stalled | `06-CHANGE.md` — cargo cult Agile; middle management threat pattern |

## Module Index

| Module | Coverage |
|--------|----------|
| 01-MOTIVATION.md | SDT, Herzberg, expectancy, goal-setting, intrinsic/extrinsic |
| 02-LEADERSHIP.md | Transformational, LMX, dark triad, psychometric predictors |
| 03-TEAMS-GROUPS.md | Groupthink, psychological safety, Hackman, social loafing |
| 04-ORG-DESIGN.md | Mintzberg, matrix/hierarchy, Conway's Law, coordination mechanisms |
| 05-STRATEGY.md | Porter, RBV, OKRs, balanced scorecard, platform strategy |
| 06-CHANGE.md | Kotter, Lewin, ADKAR, sensemaking, Argyris, learning org |
