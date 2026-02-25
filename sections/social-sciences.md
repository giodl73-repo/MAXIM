# Social Sciences

12 directories · from individual decision-making and market structure through political institutions, social organization, and population dynamics

---

## Landscape

```
╔═══════════════════════════════════════════════════════════════════════════════════════════╗
║  ECONOMIC LAYER  (how resources are allocated and agents make decisions)                  ║
║                                                                                           ║
║  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐  ┌───────────────┐   ║
║  │  economics/      │  │  finance/        │  │  behavioral-econ/│  │  game-theory/ │   ║
║  │  micro/macro     │  │  asset pricing   │  │  prospect theory │  │  normal form  │   ║
║  │  market structure│  │  portfolio theory│  │  heuristics/bias │  │  Nash equilib.│   ║
║  │  welfare theory  │  │  derivatives     │  │  nudges          │  │  mechanism    │   ║
║  │  behavioral excp.│  │  corp. finance   │  │  mechanism design│  │  design       │   ║
║  │                  │  │  financial crises│  │  experimental    │  │  auctions     │   ║
║  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘  └───────┬───────┘   ║
║           │                     │                      │                    │            ║
║           └─────────────────────┴──────────────────────┴────────────────────┘            ║
║                            all four share: rational-agent baseline and its limits        ║
╠═══════════════════════════════════════════════════════════════════════════════════════════╣
║  POLITICAL / LEGAL LAYER  (how collective decisions get made and enforced)               ║
║                                                                                           ║
║  ┌──────────────────────────────────────┐   ┌──────────────────────────────────────┐   ║
║  │  political-science/                  │   │  law/                                │   ║
║  │  IR theory (realism/liberalism/      │──▶│  common vs. civil law tradition      │   ║
║  │   constructivism)                    │   │  contract · IP · privacy             │   ║
║  │  nuclear deterrence                  │   │  antitrust · corporate               │   ║
║  │  geopolitics                         │   │  employment · international          │   ║
║  │  comparative politics & institutions │   │                                      │   ║
║  └──────────────────────────────────────┘   └──────────────────────────────────────┘   ║
╠═══════════════════════════════════════════════════════════════════════════════════════════╣
║  BEHAVIORAL / INDIVIDUAL LAYER  (psychology of the agents inside the institutions)      ║
║                                                                                           ║
║  ┌────────────────────────────────────────────┐   ┌──────────────────────────────────┐  ║
║  │  psychology/                               │   │  organizational-behavior/        │  ║
║  │  social · personality · clinical          │──▶│  motivation · leadership         │  ║
║  │  organizational · persuasion              │   │  team design (Team Topologies)   │  ║
║  │  health psychology                         │   │  Conway's Law · org design       │  ║
║  └────────────────────────────────────────────┘   │  strategy · change management   │  ║
║                                                   └──────────────────────────────────┘  ║
╠═══════════════════════════════════════════════════════════════════════════════════════════╣
║  SOCIAL / STRUCTURAL LAYER  (aggregate patterns above the individual)                    ║
║                                                                                           ║
║  ┌──────────────────────────┐   ┌───────────────────────────────────────────────────┐  ║
║  │  sociology/              │   │  demography/                                      │  ║
║  │  social structure        │──▶│  demographic transition model                    │  ║
║  │  stratification          │   │  migration · fertility · mortality                │  ║
║  │  institutions & networks │   │  population aging · labor supply                 │  ║
║  │  culture · collective beh│   │  projections (UN variants)                       │  ║
║  └──────────────────────────┘   └───────────────────────────────────────────────────┘  ║
╠═══════════════════════════════════════════════════════════════════════════════════════════╣
║  METHODS & APPLIED  (cross-cutting analytical and policy layers)                         ║
║                                                                                           ║
║  ┌─────────────────────────────────────────────┐   ┌──────────────────────────────────┐ ║
║  │  statistics-applied/                        │   │  public-health/                  │ ║
║  │  experimental design · A/B testing          │   │  epidemiology (incidence/        │ ║
║  │  quasi-experimental methods (DiD, RDD, IV)  │   │   prevalence/RR/OR/NNT)          │ ║
║  │  Bayesian practice                          │   │  disease prevention              │ ║
║  │  reliability · SPC                          │   │  health systems & financing      │ ║
║  └─────────────────────────────────────────────┘   │  global health · health policy   │ ║
║         ↑                                          └──────────────────────────────────┘ ║
║         feeds all empirical work above                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════════════╝
```

---

## Directories

| Directory | Focus | Entry Point | Bridges to |
|-----------|-------|-------------|------------|
| `economics/` | Consumer and producer theory, supply/demand to general equilibrium, market structures (perfect competition through oligopoly), welfare economics (Pareto, Kaldor-Hicks), externalities and public goods, behavioral exceptions to the rational-agent model | `01-MICROECONOMICS.md` — micro before macro; the welfare framework is prerequisite for policy analysis | `finance/` (asset pricing needs macro; micro welfare informs corporate decisions), `behavioral-economics/` (the deviations from rational-agent that economics increasingly incorporates), `game-theory/` (oligopoly analysis requires Nash equilibria), `economic-history/` (where the models came from) |
| `finance/` | No-arbitrage asset pricing (CAPM, APT, risk-neutral measure), portfolio theory (Markowitz, factor models), derivatives (Black-Scholes, Greeks, replication argument), corporate finance (WACC, capital structure, M&A), financial crises (leverage cycles, liquidity spirals, systemic risk) | `01-ASSET-PRICING.md` — the no-arbitrage principle is the conceptual spine | `economics/` (macro drives yield curves, credit cycles), `game-theory/` (strategic behavior in markets, auctions), `behavioral-economics/` (anomalies: momentum, value premium, volatility puzzle) |
| `behavioral-economics/` | Prospect theory (loss aversion, probability weighting, reference dependence), judgment heuristics and their systematic biases (Kahneman/Tversky program), nudge architecture (libertarian paternalism, choice architecture), mechanism design with non-standard preferences, experimental methods (lab, field, natural experiments) | `01-PROSPECT-THEORY.md` — the formal model before the heuristics catalog | `economics/` (BE is the empirical critique of rational-agent theory), `psychology/` (cognitive biases have psychological underpinnings), `game-theory/` (mechanism design is the normative counterpart), `statistics-applied/` (experimental methods are shared) |
| `political-science/` | International relations theory (structural realism, liberal institutionalism, constructivism), nuclear deterrence theory (MAD, extended deterrence, proliferation dynamics), geopolitical analysis (power transition, hegemonic stability), comparative political institutions (presidential vs. parliamentary, electoral systems, federalism) | `01-IR-THEORY.md` — the systemic level before domestic institutions | `law/` (international law is IR in legal form; constitutional design is comparative politics applied), `economic-history/` (institutions as economic determinants — North/Acemoglu), `military-history/` (deterrence theory has deep historical grounding) |
| `law/` | Common law vs. civil law traditions and their practical consequences, contract formation and enforcement, intellectual property (copyright, patent, trade secret), privacy law (GDPR architecture, US sectoral approach), antitrust (market definition, dominance, merger review), corporate law (fiduciary duties, Delaware doctrine), employment law, international law and treaty mechanics | `01-LEGAL-SYSTEMS.md` — common/civil distinction frames everything that follows | `political-science/` (law is institutionalized politics; constitutional law ↔ regime type), `economics/` (antitrust is applied industrial organization; IP law affects innovation incentives), `philosophy/` (jurisprudence is applied moral and political philosophy) |
| `psychology/` | Social psychology (conformity, obedience, attribution error, group dynamics), personality theory (Big Five and its limits), clinical psychology (DSM taxonomy, cognitive-behavioral models), organizational psychology (job design, motivation, leadership), persuasion and influence (Cialdini's principles, dual-process theory), health psychology | `01-SOCIAL-PSYCHOLOGY.md` — social effects are the most immediate application; personality and clinical follow | `neuroscience/` (neural substrates of social behavior and cognition), `cognitive-science/` (perception, attention, memory underlie all psychological phenomena), `organizational-behavior/` (organizational psychology is psychology applied to the firm) |
| `sociology/` | Social structure and stratification (class, race, gender as sociological constructs), social institutions (family, education, religion, polity as systemic objects), social networks (structural holes, weak ties, diffusion), culture and collective behavior (moral panics, social movements, tipping points), interaction ritual chains | `01-SOCIAL-STRUCTURE.md` — structural framing before network or cultural analysis | `demography/` (population dynamics are sociology's quantitative layer), `economics/` (stratification ↔ inequality research; labor markets are embedded social institutions), `political-science/` (collective action, social movements, civil society) |
| `organizational-behavior/` | Motivation theory (Maslow→Herzberg→Deci/Ryan SDT; Vroom expectancy), leadership models (transformational, servant, situational), team dynamics (Tuckman, psychological safety, Lencioni), org structure and Conway's Law (how communication structure constrains system architecture), Team Topologies (stream-aligned, platform, enabling, complicated-subsystem), strategy and organizational change | `01-MOTIVATION.md` — individual before group before structure | `psychology/` (OB is applied psychology at the workplace level), `sociology/` (organizations as social structures), `computing/` (Conway's Law is directly applicable to software architecture decisions — especially relevant for a VP engineering audience) |
| `game-theory/` | Normal form and extensive form games, dominant strategies and Nash equilibrium (existence, uniqueness, refinements), repeated games and cooperation (folk theorems), mechanism design (revelation principle, incentive compatibility, VCG auctions), auction theory (first/second price, optimal auction design), evolutionary game theory (ESS, replicator dynamics) | `01-NORMAL-FORM.md` — static games before dynamic; Nash before mechanism design | `economics/` (oligopoly, public goods, externalities all use game-theoretic models), `behavioral-economics/` (mechanism design with non-standard agents), `political-science/` (deterrence, arms control, coalition formation), `computing/` (mechanism design ↔ platform incentive design, AI alignment) |
| `statistics-applied/` | Experimental design principles (randomization, blinding, power, multiple testing), A/B testing in production systems (sequential testing, always-valid inference, CUPED variance reduction), quasi-experimental methods (difference-in-differences, regression discontinuity, instrumental variables), Bayesian practice (prior elicitation, posterior computation, decision theory), reliability engineering and SPC (control charts, FMEA, reliability block diagrams) | `01-EXPERIMENTAL-DESIGN.md` — design before analysis; valid identification before any estimation | `behavioral-economics/` (experimental methods are shared), `public-health/` (RCTs, observational epidemiology), `computing/` (A/B testing infrastructure, experimentation platforms — directly applicable to platform engineering) |
| `public-health/` | Epidemiological measures (incidence, prevalence, RR, OR, NNT, attributable fraction), study design hierarchy (RCT → cohort → case-control → ecological), disease prevention (primary/secondary/tertiary; vaccination strategy), health systems architecture (Beveridge, Bismarck, out-of-pocket models), global health (DALY/QALY burden, DAH, vertical vs. horizontal programs), health policy | `01-EPIDEMIOLOGY.md` — measurement and study design underlie all evidence in the field | `medicine/` (clinical to population scale), `disease/` (burden of disease framing), `demography/` (mortality and life expectancy as shared metrics), `statistics-applied/` (causal inference methods are foundational to epidemiology) |
| `demography/` | Population dynamics (cohort-component model, Leslie matrices, stable population theory), demographic transition model (stages I–V, low-fertility trap), fertility determinants (Bongaarts proximate determinants framework), mortality transition, international migration (push-pull, remittances, diaspora effects), population aging (dependency ratios, pension systems, healthcare demand), UN projection methodology and variants | `01-POPULATION-DYNAMICS.md` — stable population theory gives the mathematical backbone before transition narratives | `sociology/` (demography is sociology's quantitative substrate), `economics/` (labor supply, savings rates, and growth depend on demographic structure), `public-health/` (mortality and morbidity measurement are shared), `geography/` (spatial demography, urban-rural dynamics) |

---

## Paths

### The Policy Analysis Stack
`economics/` → `statistics-applied/` → `behavioral-economics/` → `public-health/`
*Welfare economics defines what "better" means; causal inference methods are how you measure whether a policy achieves it; behavioral economics explains why rational-agent predictions fail in practice; public health applies all three at population scale — the complete toolkit for evidence-based policy.*

### The Platform and Incentive Path
`game-theory/` → `behavioral-economics/` → `economics/`
*Mechanism design specifies the game structure; behavioral economics tells you which theoretical predictions will hold when agents are human; microeconomics provides the welfare framework for evaluating outcomes — directly applicable to marketplace design, auction systems, and AI alignment problems.*

### The Organization Path
`psychology/` → `organizational-behavior/` → `sociology/`
*Individual cognition and motivation are the micro-foundation; OB scales up to teams and firm structure (including Conway's Law, which is directly relevant to software architecture); sociology provides the macro-frame of institutions, networks, and cultural dynamics that OB sits inside — the full stack from individual to organization to society.*

---

## Adjacent Sections

| Section | The bridge |
|---------|------------|
| History & Ideas | `economics/` ↔ `economic-history/` — the models need their historical grounding to be used well; `political-science/` ↔ `military-history/` (deterrence theory has deep historical instantiations); `philosophy/` → `law/` (jurisprudence is normative philosophy applied to institutions) |
| Life Sciences | `public-health/` ↔ `disease/` and `medicine/` — population epidemiology bridges individual pathophysiology to policy; `psychology/` ↔ `neuroscience/` and `cognitive-science/` — the behavioral layer rests on neural substrates |
| Computing & Software | `game-theory/` (mechanism design ↔ platform economics, incentive-compatible protocol design, AI alignment); `statistics-applied/` (A/B testing infrastructure, experimentation platforms); `organizational-behavior/` (Conway's Law as architecture constraint — the VP engineering audience will use this constantly) |
| Earth & Space | `demography/` ↔ `climate-science/` (population growth drives emissions trajectories; climate change displaces populations); `economics/` ↔ `agriculture/` and `hydrology/` (food and water security as economic goods) |
