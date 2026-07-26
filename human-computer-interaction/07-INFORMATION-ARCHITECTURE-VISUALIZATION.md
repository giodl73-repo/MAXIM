---
maxim_schema: maxim.frontmatter.v1
id: maxim:human-computer-interaction:information-architecture-visualization
kind: guide
module: human-computer-interaction
section: human-computer-interaction
title: Information Architecture and Visualization - Structuring and Showing Information
status: source-custody
source_custody: partial
current_path: human-computer-interaction/07-INFORMATION-ARCHITECTURE-VISUALIZATION.md
canonical_path: human-computer-interaction/07-INFORMATION-ARCHITECTURE-VISUALIZATION.md
backsource_ids: [proof-backfill:human-computer-interaction:07-information-architecture-visualization]
concepts: [information-architecture, navigation, findability, search-ux, data-visualization, visual-encoding, dashboards]
root_concepts: [information-architecture-visualization]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Information Architecture and Visualization — Structuring and Showing Information

**This guide owns** two joined problems: **structuring** information so people can find and
understand it (information architecture, navigation, findability, search UX) and **showing** it so
they can read it (the visual-encoding grammar, interaction in visualization, dashboards as
interfaces). **It builds on** `02` (interaction models), `03` (the display substrate), and shares
instruments with `05` (its objects are *evaluated* with `05`'s methods, pointed at comprehension).
**It explicitly defers**: *statistical-graphics theory* (estimator/inference behind a chart, when a
plot is a statistical claim) to `data-science/`; *rendering and pipeline internals* to
`computer-graphics/`; *color science* to `colors/`; *information-retrieval theory* behind search to
`data-science/`/`query-languages/`; the *graphical-perception mechanism* (why some encodings read
faster) to `cognitive-science/`; and the *evaluation statistics* to `05` + `statistics-applied/`.

> **This module is an educational reference. This guide includes how charts and navigation can
> *mislead* — described so you can **recognize and refuse** deceptive encodings, never as a recipe
> for building them. A misleading chart or a dark-pattern navigation is a `11` violation. Named
> results and rankings are attributed, dated, and treated as bounded.**

*Per-guide banner: IA and visualization are judged by **comprehension and task success**, and those
are measured with `05`'s instruments under `05`'s discipline. A tree-test or first-click success on a
handful of users is **discovery**, not a measured rate; reading a comprehension score off a discovery
sample as if it were a measurement — or comparing two designs without a difference test — is the
error this guide guards against. Encoding-effectiveness rankings are **cited, dated, bounded** applied
results, not laws.*

---

## The Big Picture: Structure First, Then Encoding — Both Judged by Comprehension

Two halves, one goal: get the right information to a person in a form they can act on. The first
half **structures** (where does it live, how do I get to it, how do I search it); the second half
**encodes** (how is it drawn so I can read it). Neither is judged by taste — both are judged by
whether people **find** and **understand**, which is a `05` measurement problem.

```
  THE TWO HALVES (both judged by comprehension + task success)
  ==================================================================
   STRUCTURE (information architecture)     ENCODING (visualization)
   ------------------------------------     ------------------------------
   organization: how content is grouped     marks: point / line / area
   labeling: what things are called         channels: position, length,
   navigation: how you move through it        angle, area, color, shape
   search: how you query for it             interaction: overview -> zoom/
   findability: can you GET there?            filter -> details on demand
        |                                          |
        +---------------- EVALUATED BY ------------+
                     COMPREHENSION + TASK SUCCESS
              (card sort, tree test, first-click, encoding-
               comprehension tasks) -- guide 05's instruments,
               under guide 05's discovery-vs-measurement rule.
  ==================================================================
```

**Bridge (software).** IA is the **API surface and routing table** for content: organization is your
**schema/namespace**, labeling is your **naming conventions**, navigation is the **routes**, search is
the **query interface**, and findability is whether a caller can **resolve** what they need. A
visualization is a **serialization of data into perceptual channels** — and like any serialization it
can be lossy or misleading, so you validate it against what the reader must **decode**, exactly as you
validate a wire format against what the client must parse.

---

## 1. Information Architecture — Organizing, Labeling, Navigating, Searching

The classic decomposition (Rosenfeld, Morville & Arango, *Information Architecture*, "the polar bear
book," 4th ed. **2015**; orig. 1998) is four interlocking systems:

```
  THE FOUR IA SYSTEMS
  ------------------------------------------------------------------
   ORGANIZATION .. how content is grouped and structured
      EXACT schemes:      alphabetical / chronological / geographic
                          (unambiguous; good when you KNOW the item)
      AMBIGUOUS schemes:  topic / task / audience / metaphor
                          (subjective; good for BROWSING/discovery, harder to
                           maintain -- one item, many plausible homes)
   LABELING ...... what things are CALLED (the vocabulary users must match)
   NAVIGATION .... global / local / contextual paths through the structure
   SEARCH ........ query -> results, for when browsing the structure fails
  ------------------------------------------------------------------
   The hard part is AMBIGUOUS organization + LABELING: users and authors carve
   the world differently, so the "obvious" category is obvious to the author,
   not the user. This is a comprehension question -> test it (section 4).
```

The load-bearing IA problem is **the vocabulary gap**: authors label by their model, users search by
theirs, and the two rarely match (the classic finding that different people name the same thing
differently far more often than intuition suggests). IA is the discipline of **closing that gap by
testing**, not by arguing about the "right" category in a meeting.

---

## 2. Findability, Navigation, and Information Scent

Getting *to* the content is **findability**, and users navigate largely by **information scent** —
following cues (labels, links, snippets) that seem to lead toward the goal (information foraging
theory; Pirolli & Card, **1999** — *cited and applied here*; the cognitive mechanism of foraging is
`cognitive-science/`'s). Strong scent means each step visibly reduces the distance to the goal; weak
or misleading scent means users backtrack, thrash, or give up.

Applied consequences (each a comprehension hypothesis to test, §4):

- **Labels are wayfinding signs, not decoration.** A menu item is a *scent cue*; a clever or internal-
  jargon label lowers scent and predicts navigation failure.
- **Depth vs breadth is a scent-and-choice trade-off.** Deeper hierarchies mean more decisions with
  less information each; broader ones mean bigger choices with more scent per step. Neither is
  universally better — it's an empirical question for the content and users (and the Hick–Hyman bound
  from `03` cautions against treating "fewer options" as automatically faster).
- **Search is the safety net for when structure fails** (§3), not a substitute for good structure.

---

## 3. Search UX — Query, Results, and the Zero-Result Cliff

When browsing the structure fails, users **search**. The interaction responsibilities (the IR theory
— indexing, ranking, recall/precision math — is `data-science/`'s):

- **Query support.** Forgive typos and synonyms (the vocabulary gap again), suggest as they type,
  and scope the search to what's relevant.
- **Results legibility.** Snippets that carry **scent** (why did this match?), sensible ranking, and
  clear result types.
- **Faceted navigation.** Let users refine by attributes (filters/facets) — the highest-leverage
  pattern for large, structured collections, because it combines browsing and searching.
- **The zero-results cliff.** "No results" is a dead end and a scent collapse; good search offers
  suggestions, relaxed queries, or a path back. *Recall/precision* are useful **concepts** to reason
  about "did we miss relevant items vs return junk," but the estimator math is deferred.

**Browse vs search vs facet — the decision.** These are not competitors but a **layered** answer to
"how do I get to the right item?", and the choice turns on what the user can express:

```
  GETTING TO THE ITEM -- pick by what the user can express
  ------------------------------------------------------------------
   BROWSE (navigate the structure) .. user knows the CATEGORY, not the words
                                       -> strong scent + shallow, wide hierarchy
   SEARCH (type a query) ............ user knows the WORDS (a name, an error)
                                       -> query support, ranked results w/ scent
   FACET (refine by attribute) ...... user knows CONSTRAINTS, not one answer
                                       -> combine browse+search over a large,
                                          structured set (price<X, in-stock, 2023)
  ------------------------------------------------------------------
   Large structured collections want ALL THREE: land by search or browse,
   then FACET down. Faceted navigation is the highest-leverage pattern because
   it lets the user express PARTIAL knowledge and watch the result set shrink.
```

---

## 4. Evaluating IA — `05`'s Methods, Pointed at Comprehension

This is the guide's spine: IA and encodings are **evaluated with `05`'s instruments**, aimed at
comprehension and task success, **under `05`'s discovery-vs-measurement discipline.**

```
  IA / COMPREHENSION EVALUATION METHODS (all are guide-05 instruments)
  ------------------------------------------------------------------
   CARD SORTING (open/closed) . how DO/SHOULD users group & name items?
                                (generative: informs the structure)
   TREE TESTING ............... can users FIND items in a given structure,
                                text-only (isolates IA from visual design)?
   FIRST-CLICK TESTING ........ is the first move toward a task correct?
                                (first-click correctness tracks task success;
                                 Bailey et al. 2006 -- bounded to their tasks,
                                 a strong signal, not a law)
   ENCODING-COMPREHENSION ..... can users read the value/trend off the chart?
                                (task: "which is larger?", "what's the trend?")
  ------------------------------------------------------------------
   THE DISCIPLINE (from guide 05): a tree-test "81% success" on 8 users is a
   DISCOVERY signal, NOT a measured rate. To MEASURE a success rate you need a
   sized sample and a Wilson-score CI; to COMPARE two IAs you need a DIFFERENCE
   test (paired if same users, two-sample if independent) -- guide 05, section 6.
```

The failing test (from the scaling contract): reading a comprehension/first-click/tree-test score off
a **discovery-sized** sample as if it were a **measurement**, or claiming "IA-B beat IA-A" without a
difference test on the change. Discovery finds the confusing labels and the mis-filed items;
*measuring* how findable the structure is, or *proving* one structure beats another, needs a sized,
powered study whose statistics are `statistics-applied/`'s.

---

## 5. The Visual Encoding Grammar — Marks, Channels, and a Bounded Ranking

A visualization maps data to **marks** (points, lines, areas) and **visual channels** (position,
length, angle, area, color, shape). Two dated, bounded results anchor the grammar:

- **Marks and visual variables** (Jacques Bertin, *Semiology of Graphics*, **1967**) — the systematic
  vocabulary of what can be varied to encode data.
- **Graphical-perception effectiveness ranking** (Cleveland & McGill, **1984**; formalized for
  automated design by Mackinlay, **1986**): people decode some channels more accurately than others.

```
  ENCODING EFFECTIVENESS FOR QUANTITATIVE DATA (Cleveland & McGill 1984)
  ------------------------------------------------------------------
   MORE ACCURATE  position on a common scale
        ^         position on non-aligned scales
        |         length / direction / angle
        |         area
        |         volume / curvature
   LESS ACCURATE  color hue / shading / saturation
  ------------------------------------------------------------------
   APPLIED, DATED, BOUNDED: this is a ranking of DECODING ACCURACY for
   QUANTITATIVE comparison, not a universal law. Color is weak for MAGNITUDE
   but excellent for CATEGORY; the ranking depends on the task. Cite it; don't
   universalize it. The perception MECHANISM is cognitive-science's.
```

The two governing principles (Mackinlay 1986): **expressiveness** (the encoding shows all and only
the facts in the data — e.g., don't put unordered categories on a position axis that implies order)
and **effectiveness** (prefer channels the reader decodes accurately for the task). Together they turn
"which chart?" from taste into a **decodability** argument you can test (§4).

*Deferral.* When a chart is a **statistical claim** (a fitted line, a confidence band, a distribution
estimate), the estimator and its uncertainty are `data-science/`/`statistics-applied/`'s; this guide
owns the *encoding and interaction*, not the inference.

---

## 6. Interaction in Visualization — The Visual-Seeking Mantra

Static charts show; **interactive** visualization lets users *explore*. The organizing pattern is
Shneiderman's **visual information-seeking mantra** ("The Eyes Have It," **1996**):

```
  OVERVIEW FIRST -> ZOOM AND FILTER -> DETAILS ON DEMAND (Shneiderman 1996)
  ------------------------------------------------------------------
   OVERVIEW ........ show the whole, so users get the gestalt and the outliers
   ZOOM & FILTER ... let them narrow to a region / subset of interest
   DETAILS ON DEMAND reveal specifics only when asked (avoid overload)
   + RELATE / HISTORY / EXTRACT (the fuller taxonomy)
  ------------------------------------------------------------------
   BRUSHING & LINKING: select in one view, see the selection highlight in all
   linked views -> lets users see multivariate relationships by interaction.
```

**Dashboards are interfaces, not posters.** A dashboard is a *coordinated multi-view interface* whose
job is to answer questions at a glance and support drill-down — so it is subject to the same
comprehension evaluation (§4) as any interface. The common failure is a wall of gauges with weak
encodings and no interaction: it decorates data instead of answering a question.

---

## 7. Honesty in Encoding — Recognize and Refuse Deception

Charts can mislead while being "technically accurate," and a professional must **recognize and
refuse** the patterns (Tufte, *The Visual Display of Quantitative Information*, **1983**: the *lie
factor*, data-ink, chartjunk):

```
  DECEPTIVE ENCODINGS TO RECOGNIZE AND REFUSE (never a how-to)
  ------------------------------------------------------------------
   truncated / non-zero bar baseline .. exaggerates differences
   dual y-axes, independently scaled .. HIGH-RISK: CAN manufacture a trend
   area/bubble/3D for a 1-D quantity .. distorts magnitude (area != value)
   inconsistent bins / cherry-picked ranges .. hides the real pattern
   color that encodes nothing but bias attention .. misdirects the eye
  ------------------------------------------------------------------
   Truncated baselines and area-for-1D DISTORT by construction. DUAL AXES are
   NOT inherently a lie -- they are HIGH-RISK / manipulable: the second,
   independent scale can be set to manufacture an apparent trend, so SCRUTINIZE
   them, don't assume. Used to deceive, any of these is a dark pattern in chart
   form (guide 11); this guide names them so you can catch and reject them.
```

The honest rule: an encoding's job is to let the reader **decode the true relationship with least
distortion**. A chart that inflates a difference or fabricates a correlation is not a style choice —
it is a comprehension failure engineered *against* the reader, and it is out of scope to build.

---

## A Worked IA + Dashboard Case (illustrative, fictional)

*Fictional, to show comprehension evaluation under the discovery-vs-measurement rule. No real
product.*

**System.** *Grove*, a fictional city open-data portal. Two problems: residents can't find "how to
report a pothole," and the budget dashboard is "unreadable."

- **IA (find the task).** An **open card sort** (`05`/§4) with residents shows people file "pothole"
  under *Streets/Roads*, not the site's *Public Works → Assets* label — a **vocabulary gap**. A
  **tree test** on a revised structure raises first-find success in an 8-person round. **Honest
  reporting:** that 8-person tree-test result is **discovery** — it says the new labels are better and
  surfaces remaining confusions; it is **not** a measured findability rate. Claiming "structure B is
  92% findable" or "B beats A" would need a **sized sample + Wilson CI** and a **difference test**
  (`05` §6; stats → `statistics-applied/`).
- **Search + facets (find the dataset).** Beyond the pothole task, residents also hunt for *datasets*
  in a ~400-item catalog. Browsing the category tree alone fails (they don't know which department owns
  "bus on-time data"), so the portal adds **search** (typo/synonym-tolerant, snippets that show *why* a
  dataset matched) landing in a **faceted** result set — refine by **department**, **year**, and
  **format** (CSV / API / PDF). The **zero-results cliff** is handled: a mis-typed query relaxes and
  suggests rather than dead-ending. A **first-click / findability** round on the search+facet flow is
  again **discovery** — it surfaces missing facets and bad synonyms — not a measured find-rate.
- **Dashboard (read the budget).** The original used **3D pie wedges** and **dual axes** — an
  effectiveness failure (area/angle decode poorly) plus a **high-risk / manipulable** encoding (a
  second, independently scaled axis can manufacture an apparent trend, §7). The redesign uses
  **position/length** encodings (bars on a common zero baseline),
  **overview → filter → details** interaction, and brushing across a "by-department" and "over-time"
  view. An **encoding-comprehension task** ("which department grew fastest?") in a discovery round
  shows readers now answer correctly and fast — again a **discovery** signal, not a measured accuracy
  rate.
- **Accessibility (a carried invariant).** The dashboard is not "read" by color alone (a `08`/§4
  requirement); every chart has a text/table alternative and accessible names in the accessibility
  tree, and the flow is keyboard-operable — because a chart that only a sighted mouse user can decode
  has failed part of its population.

**Reading.** IA and encoding problems were turned into **comprehension hypotheses** and tested with
`05`'s instruments; every small-sample result was reported as **discovery, not measurement**; the
deceptive encodings were **refused**, not tuned; and accessibility rode along as a first-class
constraint. That is the discipline this guide enforces.

---

## Reader Tasks (answerable from this guide)

1. **Diagnose a findability failure and pick the method.** Given "users can't find returns policy,"
   name the likely cause (vocabulary gap / weak scent) and the method to test a fix (card sort →
   tree test / first-click), and state why an 8-person result is discovery, not a findability rate.
2. **Choose an encoding from the effectiveness ranking.** Given a task "compare quarterly revenue
   across five regions," pick position/length over pie/area and justify from Cleveland & McGill
   (1984), noting the ranking is task-bounded (color is fine for category, weak for magnitude).
3. **Apply the visual-seeking mantra to a dashboard.** Redesign a wall-of-gauges dashboard using
   overview → zoom/filter → details on demand plus brushing/linking, and say what question each view
   answers.
4. **Scrutinize a high-risk chart.** Given a bar chart with a non-zero baseline and a dual axis, name
   the truncated-baseline **distortion** (exaggerated difference) and why the dual axis is
   **high-risk / manipulable** (a second, independent scale can manufacture an apparent correlation —
   not automatically a lie, but scrutinize it), give the honest redesign, and say why *building it to
   deceive* is out of scope (`11`).
5. **Design and evaluate the get-to-the-item path.** Given a ~400-dataset open-data catalog where users "can't find
   anything," combine **browse**, **search** (typo/synonym-tolerant, scent-bearing snippets), and
   **facets** (department / year / format) for the three knowledge states (category / words /
   constraints), and handle the **zero-results cliff**. Then hold the discovery-vs-measurement
   line: an 8-person first-click round is discovery, not a find-rate; measuring success needs a
   sized sample + CI, and proving improvement over the old navigation needs a difference test
   (`statistics-applied/`).

---

## Decision Cheat Sheet

| Situation | Do | Because (this guide) |
|-----------|----|--------------------|
| deciding categories/labels | **card sort** with real users | close the author↔user vocabulary gap (§1) |
| "can users find X?" | **tree test** (text-only) | isolates IA from visual design (§4) |
| "is the first move right?" | **first-click test** | first-click correctness tracks task success (Bailey et al. 2006, bounded) (§4) |
| user knows the category, not the words | **browse** a shallow, wide structure with strong scent | match the path to what the user can express (§3) |
| user knows the words (a name/error) | **search**: typo/synonym-tolerant, scent-bearing snippets | close the vocabulary gap at query time (§3) |
| a large, structured collection | add **facets** (refine by attribute) over browse+search | facets let users express partial knowledge (§3) |
| "no results" returned | never dead-end: **relax + suggest + a path back** | the zero-results cliff is a scent collapse (§3) |
| choosing a chart type | rank by **effectiveness** for the task | position/length decode best for magnitude (§5) |
| unordered categories | never on an ordered position axis | expressiveness: don't imply order (§5) |
| building a dashboard | **overview → zoom/filter → details**; brush & link | it's an interface, not a poster (§6) |
| a chart that "looks more dramatic" | check for **truncated baseline** / **area-for-1D** (distortions) and a **dual axis** (high-risk — scrutinize) | refuse deception; scrutinize, don't assume, dual axes (§7) |
| any small-sample comprehension score | report as **discovery**, not a rate | discovery ≠ measurement (§4, `05`) |
| a chart that is a statistical claim | defer estimator to **`data-science/`** | HCI owns encoding, not inference (§5) |

---

## Common Confusion Points

**"There's a right category; we just have to think harder."** No. Users and authors carve the world
differently and name things differently; the "obvious" category is obvious to the author. IA is closed
by **testing** (card sort, tree test), not by argument (§1, §4).

**"A pie chart is fine; it's a standard chart."** For comparing magnitudes, pies (angle/area) decode
worse than bars (position/length) — Cleveland & McGill (1984). Pies are tolerable for a couple of
part-to-whole slices; for comparison, prefer position/length (§5).

**"Our first-click test proved the navigation works."** A discovery-sized test **found problems and
suggested the new nav is better** — it did not **measure** a success rate or **prove** it beat the old
one. Those need a sized sample, a CI, and a difference test (§4, `05`).

**"More data on the dashboard is more informative."** Usually the opposite — a dense grid of weak
encodings with no interaction overloads and hides the answer. A dashboard's job is to answer a
question at a glance and support drill-down (§6).

**"The chart is accurate, so it's honest."** Accuracy of numbers doesn't prevent a misleading
**encoding** (truncated axis, dual scales, area-for-1-D). Honesty is about what the reader **decodes**;
a technically-accurate but distorting chart is out of scope to build (§7).

---

## Global, WEIRD, and Resource Caveats

- **Reading order, icons, and color semantics are cultural.** Left-to-right layout, "up/green =
  good," and many icons are learned conventions (`01`, `02`); RTL scripts, different color meanings,
  and unfamiliar iconography can flip an "obvious" IA or encoding into a confusing one. Test IA and
  encodings **with the target population**, not by studio intuition.
- **Literacy, numeracy, and language gate comprehension.** Dense text IA and chart-heavy dashboards
  assume literacy and graph-literacy that not all users have; plain language, labeled values, and
  text/table alternatives serve low-literacy, low-numeracy, non-native, and cognitively-diverse users
  at once (the curb-cut effect, `08`).
- **Heavy visualization is a bandwidth and device barrier.** Rich interactive dashboards can be
  unusable on low-end devices or metered connections; provide lightweight, text/table fallbacks
  (`08` §8). The carried invariants ride here: encodings must not rely on **color alone** and must be
  reachable through the **accessibility tree** and the keyboard (`08`), and deceptive encodings are a
  safety/ethics-floor violation (`11`) regardless of how good the numbers are.
