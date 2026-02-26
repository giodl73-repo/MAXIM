# Organizational Design — Mintzberg, Matrix vs Hierarchy, Conway's Law

## The Big Picture

Org design is the choice of how to divide and coordinate work. Every organizational structure is a set of tradeoffs between efficiency and flexibility, depth and breadth, control and autonomy. Mintzberg's configurations provide the best taxonomy of how organizations actually look. Conway's Law adds the essential tech-org insight: your system architecture will mirror your communication structure whether you intend it or not.

```
ORG DESIGN DECISION TREE + STRUCTURAL DIMENSIONS
==================================================

WHAT IS THE PRIMARY WORK?          HOW BIG IS THE ORG?
         |                                  |
  ───────────────────             ──────────────────────
  |        |        |             |                    |
Repet.  Knowl.  Crisis        Small/new          Large/mature
  |        |        |             |                    |
Machine  Prof.  Adhoc-        Simple           Division/functional
Bureau.  Bureau. racy         structure        choice
                                   |
                    HOW DYNAMIC IS THE ENVIRONMENT?
                             |
                    ──────────────────
                    |                |
                 Stable           Dynamic
                    |                |
                Mechanistic       Organic
                (tall, rules)     (flat, lateral)

STRUCTURAL DIMENSIONS THAT CUT ACROSS ALL CONFIGURATIONS:
─────────────────────────────────────────────────────────────────────────────
Dimension            Low                     High
─────────────────────────────────────────────────────────────────────────────
Specialization       Generalists; wide        Deep specialists;
(horizontal)         role scope               narrow role scope
Formalization        Judgment; informal        Written rules;
                     norms; discretion         documented procedures
Centralization       Distributed authority;    Decisions at apex;
                     local decision rights     approval chains
─────────────────────────────────────────────────────────────────────────────

CONFIGURATIONS MAPPED TO DIMENSIONS:
                        Specialization  Formalization   Centralization
Simple structure            Low            Low              High
Machine bureaucracy         High           High             High
Professional bureaucracy    High (skills)  Low              Low (to professionals)
Divisionalized form         Moderate       Moderate         Mixed (strategy central;
                                                            ops decentralized)
Adhocracy                   High (expert)  Low              Low (mutual adjustment)
```

---

## Mintzberg's Organizational Configurations

```
MINTZBERG'S FIVE (PLUS TWO) CONFIGURATIONS
============================================

Henry Mintzberg, "The Structuring of Organizations" (1979)

Each configuration = characteristic combination of:
 Coordinating mechanism + key part of organization

SIMPLE STRUCTURE:
 Coordination: direct supervision
 Key part: strategic apex (the leader)
 Features: flat; informal; little technostructure; centralized
 Environment: simple + dynamic (e.g., startup)
 Example: small startup, entrepreneur's company, corner store
 Strength: fast decisions; adaptable; minimal bureaucracy
 Weakness: depends entirely on one person; not scalable; no depth

MACHINE BUREAUCRACY:
 Coordination: standardization of work processes
 Key part: technostructure (analysts who design and control processes)
 Features: tall hierarchy; formal rules; specialized functions; mass production
 Environment: simple + stable
 Example: McDonald's, Boeing assembly, traditional manufacturer
 Strength: efficiency; predictability; reliability; scale
 Weakness: rigid; slow to adapt; dehumanizing for workers; obsoletion risk
 Weber's ideal: this is the Weberian rational-legal bureaucracy

PROFESSIONAL BUREAUCRACY:
 Coordination: standardization of skills (professionals trained before hire)
 Key part: operating core (the professionals)
 Features: flat; decentralized to professionals; minimal technostructure
 Environment: complex + stable
 Example: hospital, law firm, university, accounting firm
 Strength: expertise; quality; professional autonomy; complex services
 Weakness: professionals resist coordination; hard to change direction;
            dysfunctional professional politics; accountability gaps
           "Professionals eat strategy for breakfast"

DIVISIONALIZED FORM:
 Coordination: standardization of outputs (targets, performance metrics)
 Key part: middle line (division heads)
 Features: corporate headquarters gives financial targets; divisions autonomous
 Environment: diverse markets (one division per market/product)
 Example: GE, Unilever, multidivisional corporation, conglomerate
 Strength: market focus per division; accountability; risk containment
 Weakness: duplication; central intelligence diffused; divisional conflict;
            portfolio thinking vs operational thinking tension

ADHOCRACY:
 Coordination: mutual adjustment (informal communication)
 Key part: support staff + operating core (blurred)
 Features: flat; project-based; highly trained specialists; very flexible;
            limited formal procedures; sometimes called "innovative organization"
 Environment: complex + dynamic
 Example: NASA (early Apollo), R&D labs, consulting firms, film studios
 Strength: highly innovative; adaptable; expertise utilization
 Weakness: conflict-prone; inefficient; stress (ambiguity is expensive);
            hard to maintain over time; instability → often becomes machine bureaucracy

MISSIONARY (6th type):
 Coordination: standardization of norms and ideology
 Key part: ideology (culture is the control mechanism)
 Example: kibbutz, some NGOs, mission-driven orgs (Doctors Without Borders)
 Culture so strong it coordinates without formal authority

POLITICAL (7th type):
 No dominant coordination mechanism; conflict is structural
 Example: org undergoing power transition; government agency; academic dept
 Not a healthy form; diagnostic rather than aspirational
```

---

## Structural Dimensions

```
STRUCTURAL DIMENSIONS
======================

SPECIALIZATION (division of labor):
 Horizontal: how many different tasks per job role
  Low horizontal: each person does many different tasks (simple structure)
  High horizontal: narrow specialization (machine bureaucracy; craft guild)
 Vertical: how much control over one's work
  Low vertical: worker controls method, pace, quality (professional bureaucracy)
  High vertical: worker executes; others plan, control, evaluate (Taylor model)

FORMALIZATION: extent to which behavior is governed by rules/procedures
 High: detailed job descriptions; documented procedures; formal communication
  Predictability; control; fairness (same rules for everyone)
  Cost: rigidity; judgment suppressed; slow to respond to unusual situations
 Low: discretion; judgment; informal norms
  Speed; adaptability
  Cost: inconsistency; coordination requires more communication

CENTRALIZATION vs DECENTRALIZATION:
 Decision-making authority: concentrated at top vs dispersed
 Centralization benefits: coordination; consistency; strategic control;
  avoiding duplicate decisions; knowledge concentration
 Decentralization benefits: speed; local information; learning; motivation;
  risk distribution; scalability
 Modern tendency: selective decentralization
  (centralize strategy + financial control; decentralize execution decisions)

UNIT GROUPING (primary basis for departmentalization):
 Function: all similar skills together (engineering dept, finance dept)
  → depth of expertise; economies of scale; career paths
  → silo problem: coordination between functions costly
 Product/Service: all capabilities for one product/customer together
  → customer focus; integration; P&L clarity
  → duplication of functions; fragmentation of expertise
 Geography: regional groupings
  → local market knowledge; time zone logistics
  → regional fragmentation; scale loss
 Matrix: dual reporting (functional + product/project)
  → attempt to get both functional depth AND product/project coordination
  → coordination cost; conflict; ambiguity (see below)
```

---

## Matrix Organizations

```
MATRIX STRUCTURE — BENEFITS AND PATHOLOGY
==========================================

WHAT IT IS:
 Dual reporting relationships: each employee reports to both:
  1. A functional manager (for expertise, career, resources)
  2. A product/project/business manager (for work direction, priorities)

WHY IT EXISTS:
 Functional (silo) structure → poor cross-functional coordination
 Divisional structure → duplication; loss of expertise depth
 Matrix → attempt to get both: functional expertise + product/project integration

THREE TYPES:
 Functional matrix (weak matrix):
  Functional managers have authority; project managers are coordinators
  → functional depth preserved; coordination improved marginally
 Balanced matrix:
  Equal power between functional and project dimensions
  → coordination improved; political conflict chronic
 Project matrix (strong matrix):
  Project manager has authority; functional manager manages resource pool
  → project coordination good; functional expertise development harder

BENEFITS (in theory):
 Flexible resource allocation across projects
 Expertise shared across projects (not duplicated in silos)
 Broader perspectives on decisions (two-manager inputs)
 Career development via functional depth + project breadth

MATRIX PATHOLOGIES (in practice):
 Ambiguity of authority: "who's my boss?" → paralysis; both say yes; or conflict
 Priority conflicts: functional manager says train; project manager says ship
 Two bosses = two annual reviews = gaming behavior (play them against each other)
 Overhead: every decision requires consultation with two managers
  → velocity drops
 "Matrix madness": coordination costs > benefit from coordination
 WHO WINS when they conflict? Research and practice: the one who controls salary
  usually wins. Makes the other dimension de facto advisory.

BOEING 737 MAX AS MATRIX FAILURE (partially):
 Consolidation of design and operations into shared matrix-managed programs
 created ambiguity between schedule-focused program management and
 engineering judgment authority → a structural failure with fatal consequences
 (oversimplified, but org design contributed to the failure mode)

MICROSOFT'S REORG (Satya Nadella, 2014+):
 From functional silos (Windows, Office as separate empires)
 to matrixed product + functional collaboration
 The One Microsoft strategy required cross-org coordination
 Azure + Microsoft 365 integration required breaking vertical silos
 This required changes to incentive structures (not just org chart)
```

---

## Span of Control

```
SPAN OF CONTROL
================

Number of direct reports a manager supervises.
Wide span = flat hierarchy; narrow span = tall hierarchy.

GRAICUNAS' FORMULA (1933):
 For n subordinates, potential relationships = n(2^(n-1) + n - 1)
 At n=5: 100 relationships; n=10: 5,210; n=12: 24,580
 This is why classical management theorists recommended 5-8 spans
 (Graicunas' formula overstates the problem but captures the exponential)

MODERN EVIDENCE:
 No universal optimal span (contingency: depends on task, subordinate skills,
  manager capacity, geographic distribution, interdependence)
 Research suggests: wider spans work when:
  Work is routine and well-defined (low coordination demand)
  Subordinates are experienced and autonomous
  Tasks are similar (not diverse roles requiring different management)
  Physical proximity (same location)
 Narrower spans work when:
  Complex, ambiguous, or creative work
  New or developing subordinates
  Geographic dispersion
  Manager has non-management work to do also

FLATTENING TREND:
 1980s-2000s: massive organizational delayering
 Average management layers: Fortune 500 went from ~9 layers (1980s) to ~5-6
 Reasons: IT enabling information flow without intermediaries;
          knowledge work requiring more autonomy; cost pressure
 Costs of flattening: information overload for few senior managers;
  promotion ladder compressed (fewer rungs → career development problem)
  → many organizations "flattened" without adjusting coordination mechanisms
  → managers with 20+ direct reports who can't actually manage them
```

---

## Conway's Law and Team Topologies

```
CONWAY'S LAW (Melvin Conway, 1967)
=====================================

"Organizations which design systems are constrained to produce
 designs which are copies of the communication structures of those organizations."

WHAT THIS MEANS:
 Your software architecture will mirror your organizational communication patterns
 Not because of technical reasons — because of how coordination actually works
 Teams design interfaces at their own boundaries
 → if team A and team B can't easily talk → A-B interface will be awkward
 → if team A and team B are fully integrated → A-B interface will be seamless

EXAMPLES:
 Microsoft (Windows, then): separate teams for UI, kernel, network
  → Windows APIs were organized around team boundaries, not user needs
 Amazon: service boundaries map closely to team boundaries (intended Conway)
  "You build it, you run it" → team owns its entire service
 Microservices: often Conway's law operating; every team = one service
  whether or not that's the right decomposition

INVERSE CONWAY MANEUVER:
 Don't accept Conway's Law as fate — design the org to get the architecture you want
 If you want tight API coupling → co-locate the teams
 If you want loose coupling + fast independent deployment → separate the teams
 Jeff Bezos: "Two-pizza teams" with mandatory API ownership → forced service separation
 Satya Nadella Microsoft reorg: forced cross-organizational collaboration → forced
  integration of Azure + M365 products that had been separate

TEAM TOPOLOGIES (Matthew Skelton & Manuel Pais, 2019):
 Four team types for software organizations:

 STREAM-ALIGNED TEAMS:
  Own a product stream from user need to production
  Small; autonomous; end-to-end ownership
  The primary team type; all other types exist to serve them
  Minimal cognitive load; clear value stream

 PLATFORM TEAMS:
  Provide internal services/capabilities to stream-aligned teams
  Reduce cognitive load on stream-aligned teams
  Example: infrastructure platform; developer tools; data platform
  Risk: platform becomes a bottleneck if it requires too much handshake

 ENABLING TEAMS:
  Specialist teams that help stream-aligned teams grow capability
  Temporary; consultative; capacity-building role
  Example: security champions; accessibility specialists; ML experts

 COMPLICATED-SUBSYSTEM TEAMS:
  Own a component requiring specialist expertise
  Stream-aligned teams use it; don't understand internals
  Example: search engine component; recommendation algorithm; encryption

INTERACTION MODES:
 COLLABORATION: close working; high bandwidth; temporary
  (used to discover; not sustainable long-term)
 X-AS-A-SERVICE: consume an API; low bandwidth; steady-state
  (platform teams; complicated-subsystem teams)
 FACILITATING: enabling team helps and leaves; temporary
  (enabling teams)
```

---

## Platform Organization as a Structural Form

Mintzberg's taxonomy was developed before platform businesses existed at scale. Platform organizations require an additional structural lens.

```
PLATFORM ORGANIZATION — STRUCTURAL CHARACTERISTICS
====================================================

A platform org has two structural layers operating simultaneously:

LAYER 1: INTERNAL PLATFORM (infrastructure for producers)
  Team Topologies model:
  Platform teams → Stream-aligned teams → Complicated-subsystem teams
  The platform team provides capabilities-as-a-service; stream-aligned teams
  are the "customers" of the internal platform

  Structural form: Professional bureaucracy for the platform teams
    (coordination by standardization of skills; high autonomy)
  + Machine bureaucracy elements for reliability and SLA guarantees
    (standardized processes for deployment, incident response, SLAs)
  → The tension: professional autonomy vs machine bureaucracy reliability
     is the core engineering org design problem for platform teams

LAYER 2: EXTERNAL ECOSYSTEM (coordination of external producers + consumers)
  Platform governance: the policies, APIs, and contracts that govern
    external developer relations and ecosystem health
  This layer has no Mintzberg analog — it is governance of a
    multi-sided market, not management of employees

PLATFORM GOVERNANCE DIMENSIONS:
  API contract stability: how much notice before breaking changes?
    Strict: enterprise trust; slow evolution; technical debt accumulation
    Loose: fast innovation; ecosystem fragmentation; developer attrition
  Developer relations: onboarding friction; documentation investment;
    support model (community / tiered / partner)
  Revenue model alignment: does the platform's revenue model create
    incentive alignment with ecosystem participants, or does it extract
    from them? (app store 30% take rate vs. metered consumption pricing)
  Governance legitimacy: how are rule changes decided?
    Unilateral (Apple App Store) vs consultative (W3C-style) vs market
    (fees signal policy via pricing)

INTERNAL PLATFORM ANTIPATTERNS (Team Topologies / Skelton & Pais):
  Platform as gatekeeper: platform team controls too much; stream teams blocked
    → Symptom: pull request queues measured in weeks; "we're waiting for platform"
    → Fix: X-as-a-service model with clear SLAs; self-service APIs
  Platform team as service desk: stream teams treat platform as on-call support
    → Symptom: platform team reactive; no investment in platform capabilities
    → Fix: product mindset; platform team has roadmap; stream teams consume APIs
  Cognitive load overload on stream teams: platform surface area too large
    → Symptom: stream engineers spend >30% on infrastructure concerns
    → Fix: platform abstraction layer; internal developer experience investment
```

## Bureaucracy Paradox and Greiner Growth

```
BUREAUCRACY PARADOX
====================

Weber's Weberian paradox:
 Rational-legal authority and formal rules → efficiency + fairness
 Over time → rules become ends in themselves → "iron cage"
 "Bureaucracy is like a machine: efficient for routine; useless for exceptions"

OB research on bureaucratic pathology:
 Goal displacement: rules become goals; original purpose forgotten
  Example: "complete the form" becomes the goal, not "serve the customer"
 Trained incapacity (Robert Merton): rules create experts in rule-following
  → expertise in following rules makes you worse at handling exceptions
 Inertia: bureaucracy resists change because change requires rule revision
  → change agents must navigate the bureaucracy to change the bureaucracy

ADHOCRACY AS OVERCORRECTION:
 Reaction: flat, flexible, no hierarchy → adhocracy
 Problem: coordination failure; ambiguity; political conflict fill the vacuum
  "If no one has authority, everyone fights for it"
 Real startups: often adhocracy that works until ~50 people;
  then: either formalize or fail to scale

GREINER GROWTH MODEL (Larry Greiner, 1972):
 Organizations pass through predictable crises as they grow:

 Phase 1 (Creativity) → CRISIS OF LEADERSHIP:
  Startup; informal; founder-led; fast; but:
  → too big for one person to handle → need professional management

 Phase 2 (Direction) → CRISIS OF AUTONOMY:
  Professional management; formal procedures; hierarchy; but:
  → managers below top need more autonomy; top becomes bottleneck

 Phase 3 (Delegation) → CRISIS OF CONTROL:
  Decentralized divisions; P&L responsibility; but:
  → divisions go in different directions; integration lost

 Phase 4 (Coordination) → CRISIS OF RED TAPE:
  Corporate staff; formal planning; systems and standards; but:
  → overhead; bureaucracy; coordination costs exceed value

 Phase 5 (Collaboration) → CRISIS OF GROWTH:
  Matrix; project teams; cultural alignment; task forces; but:
  → political exhaustion; saturation of the collaboration mechanisms

 Modern additions (Phase 6+): network organizations; platform ecosystems;
  post-bureaucratic forms

 The insight: no organizational form is permanent; each carries the seeds
 of its own crisis; leadership's job is recognizing which phase you're in
 and designing the transition intentionally.
```

---

## Common Confusion Points

**Flat hierarchy ≠ no hierarchy**:
"Flattening" reduces layers but doesn't eliminate authority. Many "flat" organizations have unclear decision rights (which is worse than a clear hierarchy). Holacracy and other no-hierarchy models are very rare in practice and often revert because coordination fails without explicit authority.

**Matrix = dual accountability, not dual authority**:
In theory, both managers have equal authority. In practice, the one who controls compensation and promotion has real authority. The other has influence only. Calling something a matrix doesn't create genuine coordination.

**Conway's Law is descriptive, not prescriptive**:
Conway described what happens when organizations design systems. He wasn't saying you should mirror your org in your architecture. The inverse Conway maneuver is deliberately using his observation: shape the org to get the architecture you want, not the other way around.

**Mintzberg's types rarely appear pure**:
Real organizations are hybrid configurations. A hospital is mostly professional bureaucracy with elements of machine bureaucracy (billing, administration) and perhaps some adhocracy (research projects). Using the types as analytical lenses, not rigid categories, is how they're most useful.

---

## Decision Cheat Sheet

| Org Design Question | Answer |
|--------------------|--------|
| Best structure for routine mass production | Machine bureaucracy |
| Best structure for expert knowledge delivery | Professional bureaucracy |
| Best structure for innovation/R&D | Adhocracy |
| When to use matrix | Dual resource optimization; use with clear authority resolution |
| Why matrix often fails | Priority conflicts; ambiguity about real authority |
| Conway's Law implication | Design teams before architecture, or accept architectural mirrors |
| Team Topologies primary team type | Stream-aligned |
| What "span of control" 20 means | 20 direct reports = almost certainly not actually managed |
| Greiner Phase 2 → Phase 3 crisis | Crisis of Autonomy → Delegation phase |
| Org design before or after strategy | Design follows strategy; then evaluate the reverse (inverse Conway) |
