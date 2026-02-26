# Philosophy of Science — Landscape

## The Big Picture

Philosophy of science sits at the intersection of epistemology, metaphysics, and the actual practice of science. It asks the normative and descriptive questions that scientists themselves rarely pause to examine.

```
+------------------------------------------------------------------+
|               PHILOSOPHY OF SCIENCE — PROBLEM MAP               |
+------------------------------------------------------------------+
|                                                                  |
|  DEMARCATION              STRUCTURE              CONFIRMATION    |
|  What is science?         How do theories        When does       |
|  What isn't?              work internally?       evidence        |
|  Popper: falsifiable      Laws, models,          support a       |
|  Kuhn: paradigm-bound     mechanisms,            theory?         |
|  Lakatos: program         idealizations          Hempel, Bayes   |
|                                                                  |
+------------------------------------------------------------------+
|                                                                  |
|  EXPLANATION              REALISM                SOCIAL DIM.     |
|  What counts as           Do theoretical         How does        |
|  explanation?             entities really        community       |
|  DN-model, causal         exist? Electrons,      shape science?  |
|  mechanical, causal       fields, quarks.        Kuhn, SSK,      |
|  Bayes nets, IBE          van Fraassen vs.       Latour, ANT     |
|                           Putnam, Worrall                        |
|                                                                  |
+------------------------------------------------------------------+
|                                                                  |
|  FIELD-SPECIFIC QUESTIONS                                        |
|  QM interpretations · Arrow of time · Species concept           |
|  Causation in economics · Functionalism in psychology            |
|  Computational theory of mind · Church-Turing as metaphysics    |
|                                                                  |
+------------------------------------------------------------------+
```

---

## Major Traditions

The field developed in roughly three phases:

```
+-----------------------------+------------------------------------+
|  PERIOD                     |  DOMINANT PROGRAM                  |
+-----------------------------+------------------------------------+
|  1920s–1950s                |  Logical Positivism / Empiricism   |
|  Vienna Circle              |  Verificationism, Carnap's         |
|  Schlick, Carnap, Neurath   |  logical syntax, Hempel's DN model |
+-----------------------------+------------------------------------+
|  1950s–1970s                |  Critical Rationalism + Historicism|
|  Popper, Kuhn, Lakatos,     |  Falsificationism, paradigm theory |
|  Feyerabend                 |  Research programs, "anything goes"|
+-----------------------------+------------------------------------+
|  1970s–present              |  Post-positivist pluralism         |
|  van Fraassen, Boyd,        |  Anti-realism, structural realism, |
|  Latour, Longino, Pearl     |  SSK, causal Bayes nets, feminist  |
|                             |  epistemology, social constructivism|
+-----------------------------+------------------------------------+
```

---

## Major Figures and Their Core Moves

| Figure | Era | Core Claim | Problem Left Open |
|--------|-----|-----------|-------------------|
| **Mach** | 1883 | Science describes sensations, not hidden causes | Anti-atomism: Boltzmann's despair |
| **Schlick** | 1918 | Logical structure of empirical knowledge | How to ground protocol sentences |
| **Carnap** | 1928 | Aufbau: reduce world to logical structure | Analyticity collapses (Quine 1951) |
| **Hempel** | 1948 | DN model of scientific explanation | Raven paradox, flagpole asymmetry |
| **Popper** | 1934/59 | Falsifiability as demarcation criterion | Duhem-Quine: what exactly is falsified? |
| **Kuhn** | 1962 | Science proceeds through paradigm shifts | Incommensurability too strong? |
| **Lakatos** | 1970 | Research programs (hard core + belt) | When is a program genuinely degenerating? |
| **Feyerabend** | 1975 | Against Method: "anything goes" | Abandons normative epistemology entirely |
| **Quine** | 1951 | Holism; no analytic/synthetic distinction | Web of belief underdetermines theory choice |
| **van Fraassen** | 1980 | Constructive empiricism: adequacy, not truth | Observable/unobservable boundary is vague |
| **Putnam** | 1975 | No-miracles argument for realism | Pessimistic meta-induction (Laudan 1981) |
| **Worrall** | 1989 | Structural realism retains structure | What is "structure" without content? |
| **Latour** | 1987 | Science in Action: facts socially constructed | Science Wars backlash, Sokal affair |
| **Pearl** | 2000 | do-calculus for causal inference | Identifiability, model selection |

---

## The Central Problems

### 1. Demarcation
What distinguishes science from non-science? Logical positivism: verifiability. Popper: falsifiability. Kuhn: having a paradigm. Lakatos: belonging to a progressive research program. No consensus — the question matters because courts, funding agencies, and practitioners all need answers.

### 2. Theory Structure
Early positivism (Carnap/Hempel): theories = axioms + correspondence rules connecting theoretical terms to observables. The "received view." Collapsed under criticism: most theories don't have this form. Semantic view (van Fraassen, Giere): theories = families of models, not linguistic entities. This matters for how you count "the same theory" across time.

### 3. Confirmation and Evidence
When does evidence E confirm hypothesis H? Hypothetico-deductive: if H entails E, and E is observed, H is confirmed. Problem: any evidence confirms infinitely many hypotheses. Bayesian: confirmation means raising prior probability. Hempel's satisfaction criterion generates the raven paradox. No clean universal solution.

### 4. Scientific Explanation
Hempel's DN model: explain by showing the phenomenon follows deductively from laws plus antecedent conditions. Fails on asymmetry (flagpole shadow), on irrelevance, and on statistical laws. Causal and mechanistic models replace it in most current work. Woodward's interventionism provides a precise alternative.

### 5. Scientific Realism
Do electrons exist? The realist says yes — inference to best explanation forces it. Van Fraassen says: maybe — we only need empirical adequacy, not truth. Structural realist (Worrall): the mathematical structure exists, the underlying "nature" need not. Pessimistic meta-induction (Laudan): every past successful theory was eventually abandoned as false — caloric, phlogiston, ether.

### 6. The Social Dimension
Kuhn opened this. SSK (Edinburgh school) went further: even true and false beliefs are explained by social causes symmetrically. Latour/Woolgar: facts are produced in labs through inscription devices and negotiation. Constructivism in various forms. Reconciling this with science's evident success is the "science wars" problem.

---

## Connection to MIT Math + TCS Background

```
+------------------------------+----------------------------------+
|  TCS / MATH CONCEPT          |  PHILOSOPHY OF SCIENCE ECHO      |
+------------------------------+----------------------------------+
|  Decidability (Turing)       |  Empirical undecidability:       |
|  Some problems have no       |  some questions lie beyond any   |
|  algorithmic solution        |  possible evidence (modal claims,|
|                              |  unobservable realm)             |
+------------------------------+----------------------------------+
|  Godel incompleteness        |  Neurath's boat: no system can   |
|  No consistent system proves |  fully self-justify from inside  |
|  its own consistency         |  (Vienna Circle self-refutation) |
+------------------------------+----------------------------------+
|  No Free Lunch theorem       |  Underdetermination: no prior-   |
|  All algorithms equal over   |  free theory-selection procedure |
|  all problems uniformly      |  works across all possible worlds|
+------------------------------+----------------------------------+
|  PAC learning bounds         |  Hempel's confirmation theory:   |
|  Sample complexity and what  |  how much evidence licenses      |
|  evidence licenses inference |  inference? Bayesian analog.     |
+------------------------------+----------------------------------+
|  Formal specification        |  Theory structure question:      |
|  (Hoare logic, Z, TLA+)      |  can science be axiomatized?     |
|  Model vs. specification     |  Semantic view: theory = family  |
|                              |  of models, not axiom set        |
+------------------------------+----------------------------------+
|  Halting problem asymmetry   |  Popper's asymmetry: a false     |
|  We can detect non-halting   |  theory can be falsified in      |
|  in finite steps if wrong    |  finite steps; never confirmed   |
+------------------------------+----------------------------------+
|  Type systems                |  Carnap's logical syntax:        |
|  Well-typedness determines   |  syntactic well-formedness       |
|  meaningfulness              |  determines cognitive meaning    |
+------------------------------+----------------------------------+
```

---

## Connection to Scientific Practice

The reproducibility crisis makes this concrete:

```
+------------------------------------------------------------------+
|          PHILOSOPHY PROBLEM → PRACTICE MANIFESTATION            |
+------------------------------------------------------------------+
|                                                                  |
|  POPPER FALSIFICATIONISM                                         |
|  Pre-register hypotheses before seeing data. Otherwise HARKing  |
|  (Hypothesizing After Results Known) makes results unfalsifiable.|
|  Pre-registration = operationalizing Popper.                    |
|                                                                  |
|  BAYESIAN CONFIRMATION                                           |
|  p < 0.05 does NOT equal high posterior probability of H.       |
|  Low base-rate hypothesis + p = 0.05 = weak evidence.           |
|  Replication failures often trace to unexamined priors.         |
|                                                                  |
|  DUHEM-QUINE HOLISM                                             |
|  A failed experiment doesn't unambiguously target the theory.   |
|  Could be instrumentation, sample quality, auxiliary assumptions.|
|  "Failed replication" often means changed auxiliaries.          |
|                                                                  |
|  KUHN NORMAL SCIENCE                                             |
|  Peer review enforces paradigm. Revolutionary work gets rejected.|
|  Kuhnian structure predicts publication bias and anomaly hoarding|
|                                                                  |
|  SSK / SOCIAL DIMENSION                                          |
|  Funding structures, career incentives, replication rewards:    |
|  social forces shape which programs get resources to survive.   |
|                                                                  |
+------------------------------------------------------------------+
```

---

## Module Map

```
00-OVERVIEW (this file) — landscape, problems, figures
     |
     +-- 01-LOGICAL-POSITIVISM — Vienna Circle, verificationism, Carnap Aufbau
     |
     +-- 02-POPPER — falsificationism, demarcation, corroboration, Duhem-Quine problem
     |
     +-- 03-KUHN-PARADIGMS — normal science, crisis, revolution, incommensurability
     |
     +-- 04-LAKATOS — research programs, hard core, progressive vs. degenerating
     |
     +-- 05-UNDERDETERMINATION — Duhem thesis, Quine holism, web of belief
     |
     +-- 06-SCIENTIFIC-REALISM — IBE, no-miracles, van Fraassen, structural realism
     |
     +-- 07-CAUSATION — DN model, mechanisms, interventionism, causal Bayes nets
     |
     +-- 08-SOCIAL-STUDIES — SSK, laboratory studies, ANT, feminist epistemology
     |
     +-- 09-BY-FIELD — QM interpretations, species, economic models, computational mind
```

---

## Decision Cheat Sheet

| You want to understand... | Go to... |
|--------------------------|---------|
| What makes science distinct from non-science | 02-POPPER (demarcation) |
| Why logical positivism collapsed | 01-LOGICAL-POSITIVISM |
| How paradigm shifts actually work | 03-KUHN-PARADIGMS |
| Lakatos as synthesis of Popper and Kuhn | 04-LAKATOS |
| Why evidence never uniquely pins down theory | 05-UNDERDETERMINATION |
| Whether unobservable entities really exist | 06-SCIENTIFIC-REALISM |
| How to think about causation precisely | 07-CAUSATION |
| How social factors enter scientific knowledge | 08-SOCIAL-STUDIES |
| QM interpretations, species concept, computational mind | 09-BY-FIELD |

---

## Common Confusion Points

**Epistemology vs. philosophy of science**: Epistemology is about knowledge generally. Philosophy of science is about the specific epistemic practices of science — theory testing, evidence, explanation. Large overlap but not the same.

**Descriptive vs. normative**: Kuhn is largely descriptive ("this is how science historically works"). Popper is normative ("this is how science ought to work"). Most practicing scientists think Popper describes them; historians think Kuhn does. Both are partially right.

**"Social construction" does not mean "made up"**: Latour's point is that facts emerge from a social process of inscription and negotiation, not that gravity doesn't exist when unobserved. Stronger constructivists lose this nuance and invite justified ridicule.

**Underdetermination has degrees**: Weak underdetermination (evidence never uniquely pins theory) is uncontroversial — everyone agrees. Strong underdetermination (multiple permanently inequivalent theories always remain) is contested and is where the real action is.

**The reproducibility crisis is philosophy made practical**: p-hacking, HARKing, publication bias — these are confirmation theory and demarcation problems expressed as measurement and incentive problems in actual laboratory practice.
