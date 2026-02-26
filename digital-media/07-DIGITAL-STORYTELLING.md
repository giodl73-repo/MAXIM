# Digital Storytelling: Interactive Narrative, Data Visualization, Scrollytelling

## The Big Picture

```
DIGITAL STORYTELLING FORMS
============================

+------------------------------------------------------------------+
|  FORM              INTERACTION     EXAMPLE                       |
|  ----              -----------     -------                       |
|  Branching story   High (choices)  Twine, interactive fiction    |
|  Scrollytelling    Low (scroll)    NYT Snow Fall, Pudding.cool   |
|  Data narrative    Variable        Dear Data, narrative charts   |
|  Podcast narrative None (audio)    Serial, Radiolab              |
|  VR documentary    Presence        Nonny de la Peña works        |
|  Longform web      Low (read)      Atavist, Epic Magazine         |
|  Video essay       None (watch)    YouTube video essays           |
|  Game narrative    High (all)      AAA storytelling games         |
+------------------------------------------------------------------+

KEY TENSION IN ALL FORMS:
  CONTROL (author's narrative arc)
  vs.
  AGENCY (reader/viewer/player's choices)

More interactivity = more author control surrendered
Less interactivity = more authorial control, less engagement
The art is calibrating where the control/agency axis sits
for each story's purpose
```

---

## Scrollytelling: Scroll-Triggered Narrative

### NYT "Snow Fall" as Origin Point

```
SNOW FALL (NYT, December 2012)
================================

"Snow Fall: The Avalanche at Tunnel Creek"
  John Branch, multimedia team
  Six-part immersive longform piece
  13,000 words + video + photo + audio + animation
  Read by 3.5 million people in 6 days (unprecedented for long-form)
  Won 2013 Pulitzer Prize for Feature Writing

TECHNICAL INNOVATION:
  Scroll-triggered animations (parallax effects)
  Video autoplay on scroll
  Photo galleries embedded in text
  Interactive mountain terrain model
  Sidebar profiles that expand on click

WHY IT WORKED:
  The interactivity served the story (avalanche unfolds as you scroll)
  Not decoration -- the scroll = the narrative pace
  The reader's progression through the piece = the mountain run

SUBSEQUENT INFLUENCE:
  Every major news organization built "Snow Fall clones"
  New genre: "immersive longform" or "scrollytelling"
  Technical infrastructure: Vox's "Chorus", NYT's "Scoop" (now "Oak")
  Third-party tools: Shorthand, Atavist, Exposure
```

### Scrollytelling Mechanics

```
SCROLLYTELLING ARCHITECTURE
=============================

BASIC SCROLLYTELLING PATTERN:
  User scrolls -> position on page detected via JS
  -> CSS transitions / JS animations triggered
  -> Text, images, charts animate into view or transform
  -> Creates "story unfolding" experience

TYPES:
  PARALLAX: background moves slower than foreground
    Creates depth/immersion effect
    Used for: scene-setting, location, atmosphere

  STICKY SCROLL: element stays fixed while page scrolls
    Interactive chart that updates as user scrolls through context
    Example: chart shows 1900 data; user scrolls past 1950;
             chart updates to 1950 while text discusses that era

  ANIMATION TRIGGER: element animates when scrolled into view
    Fade-in, slide-in, draw-on effects
    Charts: bars animate up as user reaches the chart

  VIDEO SCROLL CONTROL: video frame tied to scroll position
    User "controls" the video by scrolling
    Used for: process demonstrations, before/after

TOOLS (2025):
  Scrollama (JS library): open source, lightweight
    Designed for sticky-scroll journalism
  ScrollMagic: feature-rich; heavier
  GSAP ScrollTrigger: powerful animation library
  Shorthand: no-code journalist tool
  Atavist: full publishing platform with scrollytelling
```

---

## Data Visualization Storytelling

### Narrative vs. Exploratory Visualization

```
VISUALIZATION SPECTRUM (Segel & Heer, 2010)
=============================================

AUTHOR-DRIVEN                      VIEWER-DRIVEN
(narrative charts)                 (exploratory dashboards)

  Specific message ->                Multiple questions ->
  Linear path through data           Non-linear exploration
  Author controls sequence           Viewer controls sequence
  Minimal interactivity              High interactivity
  Examples:                          Examples:
    Newspaper chart                    Tableau dashboard
    NYT visual story                   Power BI report
    Dear Data postcards                D3.js exploratory vis

HYBRID FORMS:
  "Martini glass" structure (Segel & Heer):
    Narrow stem = guided narrative section
    Open glass = free exploration section
  Example: start with author-driven story, then "explore your own"
```

### Dear Data: The Canonical Data Storytelling Example

```
DEAR DATA (Giorgia Lupi + Stefanie Posavec, 2015-2016)
=========================================================

Project: 52-week postcard exchange between NYC and London
  Each week: a theme (complaints, laughter, worry, time)
  Each person: collected personal data for that theme
  Each person: hand-drew a visualization on a postcard
  Each person: sent it to the other person across the Atlantic

Output: 104 postcards; collected in book (Princeton Arch Press 2016)
Key principles demonstrated:
  Data collection IS a form of attention (what you track changes you)
  Visualization can be personal, handmade, imperfect
  The "legend" (how to read the chart) is part of the artifact
  Small personal data can be more revealing than big data

INFLUENCE:
  "Humanistic data visualization" movement
  Data journalism aesthetic: hand-drawn, sketch-quality, personal
  Giorgia Lupi's subsequent work: "Data Humanism" manifesto

GIORGIA LUPI (b. 1981):
  Partner at Pentagram
  Most influential data visualization designer currently working
  TED Talk: "How We Can Find Ourselves in Data"
  Key claim: the goal of data visualization is not efficiency
    but human connection -- the data should reveal the human story
```

---

## Podcast Narrative Structure: Serial as Model

```
SERIAL (NPR/WBEZ, Sarah Koenig, 2014)
=======================================

"Serial" Season 1: investigation of the 1999 murder
  of Hae Min Lee and conviction of Adnan Syed
  12 episodes; first podcast to hit 5 million downloads
  Defined "narrative podcast" as a cultural form

NARRATIVE STRUCTURE:
  COLD CASE STRUCTURE:
    Open question sustained across episodes
    Each episode: reveals new information that reframes
    what was established in previous episode
    The listener's certainty oscillates with each episode:
      "He's guilty" -> "maybe not" -> "definitely innocent" -> "unclear"
    Uncertainty is the engine; resolution would end the series

  NARRATOR-AS-INVESTIGATOR:
    Koenig is the narrator AND the protagonist (investigating)
    Listener follows the investigation in real time
    This is subjective journalism: narrator's uncertainty
    is shared with the listener (vs. objective omniscient narrator)

  EPISODIC vs. SERIAL:
    Each episode ends without resolution
    Listener must return for the next installment
    This is the TV cliffhanger structure applied to journalism

SUBSEQUENT INFLUENCE:
  "S-Town" (2017): 7-part series; most downloaded podcast ever at launch
  "In the Dark": investigative serial journalism
  "Dr. Death": crime narrative + healthcare system critique
  The narrative podcast is now a major content category
```

---

## Interactive Narrative: Twine and Branching Story

```
BRANCHING STORY STRUCTURE
===========================

BASIC BRANCHING:
  Linear story with decision points
  Each decision -> different branch
  Multiple endings possible

PROBLEMS WITH FULL BRANCHING:
  "Combinatorial explosion":
    10 decisions with 2 options each = 2^10 = 1,024 possible paths
    Writing and testing 1,024 paths is not feasible
    Most branches dead-end (nothing happens differently)
    The player feels the illusion of choice, not real choice

SOLUTIONS:
  FUNNEL STRUCTURE: branches merge back to main story
    Choices have local effects; global story converges
    Illusion of choice with author control

  CONSEQUENCE WEIGHTING: choices affect character stats
    Not immediate narrative branch but accumulating variables
    Game examples: Baldur's Gate, Mass Effect moral system
    Variables then gate later options ("your reputation is high")

  TEMPORAL BRANCHES: choices have delayed consequences
    "This choice will have consequences later" (Telltale model)
    Player makes choice without knowing impact
    Impact revealed much later -> creates anxiety and investment

TWINE (tool):
  Free, open-source interactive narrative tool
  Text-based hyperlinks as choices
  No coding required for basic stories
  Published to HTML (browser-native)
  Used for: IF (interactive fiction), experimental narrative,
            educational scenarios, parser games
  Annual IF competitions: IFComp (1995-present)
```

---

## Immersive Journalism: VR Documentary

```
NONNY DE LA PENA AND IMMERSIVE JOURNALISM
==========================================

Nonny de la Pena (b. 1960):
  Documentary filmmaker; "Godmother of Virtual Reality"
  Created first VR journalism pieces before consumer VR existed

"Hunger in Los Angeles" (2012):
  Reconstructed audio of a real incident at a food bank
  User: present in the scene as events unfold
  Person collapsed from diabetic shock; crowd reaction
  Significance: first widely shown VR journalism piece
    at Sundance 2012

"Project Syria" (2014):
  Placed users in Aleppo during shelling
  Immersive sound design + 3D environment
  Award-winning at Davos

The "presence" thesis:
  VR creates sense of physical presence at events
  This presence triggers empathy more strongly than video
  "Presence" research: Mel Slater's lab, Stanford VHIL
  De la Pena's argument: presence = better journalism tool
    for stories that are hard to understand from text/video

CURRENT STATE (2025):
  Consumer VR adoption: ~10% penetration; niche
  360-degree video: more accessible than full VR
    (watch on YouTube in mobile with cardboard)
  Most VR journalism: festival exhibition, not mass distribution
  The distribution problem limits VR journalism's reach
```

---

## Longform Web Narrative: The Atavist Model

```
ATAVIST MAGAZINE (2011-2018)
=============================

Founded: Evan Ratliff, Jefferson Rabb
Model: single-story digital issues
  Each issue: one longform story (10,000-20,000+ words)
  Built native digital reader (iOS app, web)
  Subscriptions + single-issue purchase

Significance:
  Proved readers would pay for digital single-story purchases
  Demonstrated that digital-native storytelling forms
  could be editorially serious
  "The Mastermind" (Evan Ratliff, 2016): 40,000-word
    investigation of Paul Le Roux -- subsequently became a book

The platform problem:
  Atavist the magazine stopped in 2018 (platform survived)
  Distribution is the challenge: longform digital needs
    a committed reader relationship
  The newsletter/subscription model (Substack) is the
  current iteration of this: paid direct relationship
  bypasses algorithm dependency
```

---

## Decision Cheat Sheet

| Form | Use when | Key tool |
|------|---------|---------|
| Scrollytelling | Story unfolds geographically or temporally; scroll maps to narrative | Scrollama, Shorthand |
| Interactive data vis | User has multiple questions; data supports exploration | D3.js, Flourish, Datawrapper |
| Narrative data vis | You have one specific message from data | Datawrapper, Illustrator, Flourish |
| Branching story | Multiple equally valid paths; finite decisions | Twine, Ink, Yarn Spinner |
| VR/immersive | Physical presence at scene is essential; niche distribution OK | Unity, Unreal, 360 video |
| Podcast narrative | Audio-primary story; serial audience commitment desired | Interview + scripted hybrid |
| Longform web | 2,000-20,000 words; committed reader | Atavist, Shorthand, own CMS |

---

## Common Confusion Points

**Interactivity does not improve stories.** More interaction choices do not automatically produce better engagement. Poorly motivated interactivity is distracting. The principle: interactivity should serve the story's purpose. Snow Fall worked because the scroll was the avalanche. Many "interactive" pieces use interaction as decoration.

**Branching stories have the combinatorial explosion problem.** Full branching is not feasible at scale. All major narrative games use funneling, consequence weighting, or temporal delay to create the feeling of choice without exponential authoring cost.

**Scrollytelling is a production-heavy format.** Snow Fall required an entire multimedia team for months. Tools like Shorthand reduce this, but the production investment is still higher than text. Use it for flagship pieces, not routine coverage.

**"Presence" in VR does not guarantee empathy.** Mel Slater's research shows that presence (feeling of being there) is measurable and achievable. Empathy is separate. VR can produce presence without producing changed behavior or durable empathy. The "empathy machine" claim for VR is overstated.

**Narrative podcasts are serialized journalism, not radio.** Serial was built for on-demand listening, not broadcast scheduling. The listener controls pace; episodes can be released all at once (binge model) or weekly. The serialized structure is a deliberate design choice for listener commitment, not a broadcast necessity.
