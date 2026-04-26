# Comparative Politics

## The Big Picture

Comparative politics asks: why do political systems look different, and with what
consequences? Electoral systems, regime types, state capacity, and institutional
design all produce systematically different political and policy outcomes.

**Formal bridge:** Institutional design choices in political systems are structurally
identical to distributed system architecture choices. Veto player count directly
controls the commit threshold: a US-style system with 3+ effective veto players is
like a distributed consensus protocol requiring near-unanimity — high consistency,
low availability for change, maximum safety. A Westminster single-party majority is
like a single-node system: fast commits, no blocking, maximum policy throughput but
no redundancy against error. Duverger's Law (FPTP produces two parties) is an
equilibrium result from the same strategic voting logic as plurality-wins tournaments
in any ranked-choice system. Electoral thresholds (Germany's 5% barrier) are the
minimum quorum required for a partition to enter the decision process. The Tsebelis
veto players framework is the clearest example: it is literally a formal model
predicting policy change as a function of the number of consent-required actors and
the spread of their ideal points in policy space.

```
+----------------------------------------------------------------------+
|                    COMPARATIVE POLITICS FRAMEWORK                    |
|                                                                      |
|  INSTITUTIONAL DESIGN            OUTCOMES                            |
|  ─────────────────────           ────────                            |
|  Electoral system                Party system (# of parties)         |
|  Executive structure             Policy output (stability/change)    |
|  Federal/unitary               → Democratic quality                  |
|  Veto players                    Economic performance                |
|  State capacity                  Redistribution                      |
|                                  Democratic durability               |
|                                                                      |
|  VARIETIES OF CAPITALISM         DEMOCRATIC TRAJECTORIES             |
|  ─────────────────────           ─────────────────────               |
|  LME: US, UK                     Consolidation (most OECD)           |
|  CME: Germany, Japan             Backsliding (Hungary, Turkey)       |
|  Mixed/Mediterranean             Breakdown (Venezuela)               |
|  Hierarchical (LatAm)            Emergence (new democracies)         |
+----------------------------------------------------------------------+
```

---

## Section 1: Electoral Systems

Electoral systems translate votes into seats — and the choice of system shapes
the entire party system and policy outcomes.

### First Past The Post (FPTP)

```
  MECHANISM: Single-member districts; candidate with most votes wins
             (plurality, not majority required)

  DUVERGER'S LAW: FPTP tends to produce two-party systems
  Why: Wasted votes → strategic voting → third parties marginalized
       Parties have incentive to merge to be viable

  EFFECTS:
  ┌────────────────────────────────────────────────────────────────┐
  │ + Manufactured majorities: minority of votes → majority of seats│
  │   → Single-party government → decisive policy action           │
  │ + Clear accountability: voters know who governs                │
  │ + Geographic representation: each district has own MP          │
  │                                                                │
  │ - Unrepresentative: 40% of votes → 60% of seats                │
  │ - Wasted votes: large parties win big margins; small parties   │
  │   get nothing                                                  │
  │ - Tactical voting: vote for lesser evil, not preference        │
  │ - Two-party lock: third parties face structural disadvantage   │
  └────────────────────────────────────────────────────────────────┘

  EXAMPLES: US House, UK Commons, Canada, India
```

### Proportional Representation (PR)

```
  MECHANISM: Party list systems; seats proportional to vote share

  VARIANTS:
  ┌────────────────────┬──────────────────────────────────────────────┐
  │ Closed list PR     │ Party controls ranking; voters choose party  │
  │                    │ Israel, Spain, Netherlands                   │
  ├────────────────────┼──────────────────────────────────────────────┤
  │ Open list PR       │ Voters influence individual candidate rank   │
  │                    │ Finland, Sweden, Brazil                      │
  ├────────────────────┼──────────────────────────────────────────────┤
  │ STV (Single        │ Ranked choice in multi-member districts      │
  │ Transferable Vote) │ Ireland, Australian Senate                   │
  └────────────────────┴──────────────────────────────────────────────┘

  EFFECTS:
  ┌────────────────────────────────────────────────────────────────┐
  │ + More representative: vote share ≈ seat share                 │
  │ + More parties: ideological diversity represented              │
  │ + Higher voter participation (every vote counts)               │
  │                                                                │
  │ - Coalition governments: slower policy-making, compromise      │
  │ - Harder accountability: multiple parties share blame/credit   │
  │ - Small parties can have outsized leverage in coalition        │
  │ - Threshold requirement needed to prevent fragmentation        │
  └────────────────────────────────────────────────────────────────┘

  THRESHOLD: Germany 5%; Netherlands 1/150; Israel 3.25%
```

### Mixed-Member Proportional (MMP)

```
  Germany's system — often considered the gold standard:
  Each voter has TWO votes:
  Vote 1: Candidate in local district (FPTP)
  Vote 2: Party list (proportional)

  Overhang seats + leveling seats → final result is proportional to party vote
  Preserves local representation + overall proportionality

  Also: New Zealand (since 1996), Scotland, Wales
```

---

## Section 2: Presidential vs. Parliamentary Systems

```
  PRESIDENTIALISM:                PARLIAMENTARISM:
  ──────────────                  ───────────────
  Fixed electoral term            Executive from legislature
  Separate elections for          Prime minister + cabinet can be
  legislature + executive         removed by parliament (no confidence)
  Veto + separation of powers     Dissolution of parliament possible
  Gridlock risk (divided govt)    Strong single-party or coalition govt
  High personalization            Lower personalization (party focus)
  US, Brazil, Mexico, Indonesia   UK, Germany, Japan, Australia

  LINZ THESIS (1990s): Presidentialism is less stable than parliamentarism
  Why: dual legitimacy (president + legislature both elected); no mechanism
  for resolving deadlock except coup or presidential decree
  Evidence: Latin American presidential democracies failed at higher rates

  Counter-argument: US presidentialism has been stable; other factors matter
  (political culture, economic development, federalism)

  SEMI-PRESIDENTIALISM (France):
  Directly elected president + prime minister accountable to parliament
  COHABITATION: president and PM from different parties (1986-88, 1993-95, 1997-2002)
  → Power-sharing between rivals; foreign vs domestic policy division
```

---

## Section 3: Veto Players

Tsebelis's framework: the most powerful analytical tool in comparative politics.

```
  TSEBELIS: Veto Players (2002)

  VETO PLAYER: Any actor whose agreement is required for policy change
  (status quo can only change if all veto players agree)

  TWO TYPES:
  Institutional veto players: defined by constitution
  - US: President + House + Senate (+ filibuster effectively)
  - Germany: Bundestag + Bundesrat (on many issues)
  - EU: Commission + Council + Parliament

  Partisan veto players: defined by coalition politics
  - German grand coalition: CDU/CSU + SPD → two partisan VPs
  - Israeli coalition: multiple parties = multiple VPs per partner

  PREDICTIONS:
  More veto players → less policy change → more policy stability (gridlock)
  Fewer veto players → more policy change → less stability (potentially)

  VETO PLAYER INDEX:
  Low (Westminster UK): 1-2 veto players → rapid policy change
  High (US, EU): 3+ effective veto players → gridlock common

  APPLICATION:
  Why does US have no VAT, national health insurance, gun regulations?
  → Not because of public opinion
  → Because of veto player architecture (Senate, filibuster, committee chairs)
  US has systematically more veto players than any other democracy
```

---

## Section 4: Democratic Backsliding

The phenomenon that has dominated comparative politics since ~2010:

```
  LEVITSKY & ZIBLATT: How Democracies Die (2018)

  INSIGHT: Modern democracies die through elections, not coups
  The new authoritarianism uses democratic procedures to dismantle democracy

  FOUR KEY BEHAVIORS OF AUTHORITARIANS-IN-DEMOCRACY:
  1. Rejection of democratic rules of the game
  2. Denial of legitimacy of political opponents
  3. Toleration/encouragement of violence
  4. Readiness to curtail civil liberties of opponents

  TWO INSTITUTIONAL GUARDRAILS:
  MUTUAL TOLERATION: Accept opponent as legitimate (not existential enemy)
  INSTITUTIONAL FORBEARANCE: Don't use every legal power available
    (e.g., Senate could fill 9 Supreme Court seats per term — they don't)

  CASE STUDIES:
  ┌───────────────┬────────────────────────────────────────────────────┐
  │ Hungary       │ Fidesz 2010+: electoral reforms, media capture,    │
  │               │ judiciary packing, constitutional changes          │
  │               │ Still has elections — competitive authoritarianism │
  ├───────────────┼────────────────────────────────────────────────────┤
  │ Turkey        │ AKP/Erdogan: July 2016 coup attempt → purges →    │
  │               │ presidential referendum 2017 → quasi-presidential  │
  │               │ system with weakened institutional checks         │
  ├───────────────┼────────────────────────────────────────────────────┤
  │ Venezuela     │ Chavez → Maduro: economic crisis + institutional   │
  │               │ capture → authoritarian consolidation              │
  │               │ Electoral fraud from 2018 onward                   │
  └───────────────┴────────────────────────────────────────────────────┘

  V-DEM BACKSLIDING INDEX:
  25+ countries showing autocratization trends (2019-2025)
  Brazil under Bolsonaro: temporary; reversed 2022
  India: V-Dem electoral democracy index declining
  US 2017-2021: declined but recovered
```

---

## Section 5: Varieties of Capitalism

Hall and Soskice's framework — institutional complementarities in political economy:

```
  HALL & SOSKICE: Varieties of Capitalism (2001)

  LIBERAL MARKET ECONOMIES (LME):
  US, UK, Canada, Australia, Ireland

  Coordination mechanism: MARKET (arm's-length competitive markets)
  ┌────────────────────────────────────────────────────────────────┐
  │ Labor market: fluid (hire/fire easy, spot market wages)        │
  │ Finance: equity markets (short-term return focus)              │
  │ Skills: general (portable, company-funded training risky)      │
  │ Corporate governance: shareholder primacy                      │
  │ Innovation: radical (disruptive, Schumpeterian)                │
  │ Comparative advantage: high-tech, finance, bio                 │
  └────────────────────────────────────────────────────────────────┘

  COORDINATED MARKET ECONOMIES (CME):
  Germany, Japan, Scandinavia, Netherlands, Austria

  Coordination mechanism: NON-MARKET (collaborative institutions)
  ┌────────────────────────────────────────────────────────────────┐
  │ Labor market: patient (unions, works councils, long tenure)    │
  │ Finance: banks (patient capital, relationship lending)         │
  │ Skills: specific (company-specific, apprenticeship programs)   │
  │ Corporate governance: stakeholder orientation                  │
  │ Innovation: incremental (quality, reliability, process)        │
  │ Comparative advantage: machine tools, autos, chemicals         │
  └────────────────────────────────────────────────────────────────┘

  INSTITUTIONAL COMPLEMENTARITIES:
  Each element reinforces others in the same variety
  LME: fluid labor + equity markets + general skills all fit together
  CME: patient capital + works councils + specific skills all fit together
  → Mixing creates friction; cross-variety transplants often fail

  CRITIQUE: World becoming more similar (convergence thesis)?
  Evidence: Some convergence in finance; but core VoC differences persist
  German co-determination still structurally different from US shareholder primacy
```

---

## Section 6: Authoritarian Durability

Why do some authoritarian regimes last for decades?

```
  SELECTORATE THEORY (Bueno de Mesquita et al.):

  ALL LEADERS need a WINNING COALITION (W) to stay in power
  All leaders have access to a SELECTORATE (S) = those who could be in W

  Small W (autocracy): ruler distributes private goods to small group
  → Coalition members get high per-capita benefits → loyal
  → Selectorates outside W know: if they lose position, get nothing
  → Strong loyalty incentive in small-W systems

  Large W (democracy): ruler must distribute public goods to large coalition
  → Can't afford private goods for everyone → rely on policy performance
  → Members easily replaced → each member's loyalty less valuable
  → Accountability mechanism emerges from W size

  TYPES OF AUTHORITARIAN REGIMES:
  ┌────────────────────────┬─────────────────────────────────────────┐
  │ Personalist            │ Single leader dominates; Stalin, Saddam │
  │                        │ Weakest institutionally; most brutal    │
  │                        │ Succession = most dangerous moment      │
  ├────────────────────────┼─────────────────────────────────────────┤
  │ Party-based            │ Party apparatus rules; CCP, CPVN       │
  │                        │ More institutionalized; succession rules│
  │                        │ Most durable; adapt over time          │
  ├────────────────────────┼─────────────────────────────────────────┤
  │ Military               │ Junta; usually shorter-lived; domestic  │
  │                        │ legitimacy problems; exit harder        │
  │                        │ Myanmar, Egypt, Thailand                │
  └────────────────────────┴─────────────────────────────────────────┘
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| Why does US have two parties? | Duverger's Law; FPTP structure discourages third parties |
| Why does German policy change slowly? | Multiple veto players (Bundestag + Bundesrat + coalition partners) |
| Why does Hungary look democratic but isn't? | Competitive authoritarianism: uses elections to legitimate capture |
| Why doesn't Germany have Silicon Valley? | CME structure: patient capital + incremental innovation; LME needed for radical innovation |
| How do autocracies stay in power? | Small winning coalition + private goods distribution (selectorate theory) |
| What predicts democratic backsliding? | Rejection of democratic norms by leaders + erosion of institutional guardrails |
| Presidential vs parliamentary which is more stable? | Parliamentary (Linz thesis) but evidence mixed; context matters |

---

## Common Confusion Points

**Veto players ≠ political opposition**: veto players are defined institutionally or by
coalition necessity. In a Westminster system, the opposition has no veto power —
a majority government can pass anything. In the US, a single senator can filibuster.

**Competitive authoritarianism is not just a "flawed democracy"**: regimes like Hungary
under Fidesz still hold elections, but the playing field is systematically tilted —
media capture, gerrymandering, NGO restrictions, judiciary packing. Elections occur
but cannot produce meaningful accountability. This is categorically different from
a democracy with weaknesses.

**LME ≠ better: CME ≠ better**: each variety performs better at different things.
LMEs produce more disruptive innovation; CMEs produce higher manufacturing quality
and lower inequality. The VoC framework is analytical, not normative.

**Comparative advantage in politics**: the comparison of systems must control for
many variables. Germany's low inequality isn't just because of its electoral system —
it's because of the full institutional complementarities of the CME (unions, works
councils, training system). Transplanting one element doesn't replicate the outcome.
