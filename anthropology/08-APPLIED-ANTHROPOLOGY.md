# Applied Anthropology

## The Big Picture

```
+------------------------------------------------------------------+
|                    APPLIED ANTHROPOLOGY                          |
|                                                                  |
|  "Anthropological methods and theory put to work on real         |
|   problems — in health, development, design, justice, and        |
|   heritage — outside the academic literature"                    |
+------------------------------------------------------------------+
         |              |              |              |
         v              v              v              v
  +-----------+ +-----------+ +-----------+ +-----------+
  | MEDICAL   | | DEVELOP-  | | DESIGN    | | FORENSIC  |
  | ANTHRO    | | MENT      | | ETHNOGR-  | | & LEGAL   |
  |           | | ANTHRO    | | APHY      | |           |
  +-----------+ +-----------+ +-----------+ +-----------+
  | Kleinman  | | Scott     | | IDEO/PARC | | Mass grave|
  | Illness   | | Chambers  | | Suchman   | | ICMP/FAFG |
  | models    | | FPIC      | | Contextual| | Daubert   |
  | Farmer    | | Mosse     | | inquiry   | |           |
  +-----------+ +-----------+ +-----------+ +-----------+

         +-----------------------------------+
         |  HERITAGE & DECOLONIZATION        |
         |  NAGPRA  /  CARE principles       |
         |  Linda Tuhiwai Smith              |
         |  Digital repatriation            |
         +-----------------------------------+
```

Applied anthropology is anthropology doing something other than describing.
The practitioner bridges ethnographic insight and institutional action —
which requires navigating institutional constraints, ethics, power, and
the gap between what research shows and what organizations can implement.

---

## Section 1: Medical Anthropology

### Kleinman's Explanatory Model Framework

```
  PROBLEM: Doctors and patients have different models of what
  is happening in illness. This causes non-compliance, failed
  treatment relationships, and worse outcomes.

  Arthur Kleinman (Harvard Medical Anthropology):
  EXPLANATORY MODEL = the ideas any individual has about an
  episode of illness: etiology, timing/onset, pathophysiology,
  severity, expected course, appropriate treatment.

  PATIENT'S EXPLANATORY MODEL:  often culturally embedded,
  may involve spirit possession, punishment, imbalance, or
  food taboo violation — not biomedical causation.

  CLINICIAN'S EXPLANATORY MODEL: biomedical, germ theory,
  organ-based, chemically addressed.

  WHEN THEY CONFLICT:
  Patient nods, receives prescription, does not fill it.
  Or fills it, does not take it correctly.
  Or takes biomedical treatment PLUS traditional treatment
  that may interact.
  Or does not return for follow-up (the "non-compliant patient").

  KLEINMAN'S 8-QUESTION ELICITATION:
  ┌────────────────────────────────────────────────────────┐
  │ 1. What do you call the problem?                       │
  │ 2. What do you think has caused it?                    │
  │ 3. Why do you think it started when it did?            │
  │ 4. What do you think the sickness does to you?         │
  │ 5. How severe is it?                                   │
  │ 6. What kind of treatment do you think you need?       │
  │ 7. What are the main results you hope to get?          │
  │ 8. What are the chief problems caused by this illness? │
  └────────────────────────────────────────────────────────┘

  Clinical use: elicit BEFORE prescribing. Negotiate between
  models. Don't assume non-compliance is ignorance; it's
  usually different model + different priorities.

  TECHNOLOGY PARALLEL:
  Users have explanatory models of software behavior.
  When the user's model (the "toaster mental model" of email)
  differs from the system model (the actual SMTP/IMAP
  architecture), the "non-compliant user" does the "wrong"
  thing from the developer's perspective.
  The solution is not better documentation — it is designing
  the system model to match the mental model, OR actively
  eliciting and negotiating models.
```

### Disease, Illness, and Sickness — The Tripartite Distinction

```
  THREE LEVELS (Kleinman, Young, Eisenberg):

  DISEASE: The biomedical/pathophysiological process.
  "What the doctor treats."
  Exists as an objective phenomenon (the bacteria, the tumor).

  ILLNESS: The patient's lived experience of being unwell.
  "What the patient experiences."
  Culturally shaped: what counts as sick, how sick one "should"
  feel, which symptoms are salient, what it means to be ill.
  Pain experience varies cross-culturally. "Low back pain"
  as a category does not exist in all languages.

  SICKNESS: The social role of being ill.
  "What society does with sick people."
  Sick role (Parsons): exempted from normal duties, expected
  to seek treatment. Sickness status is negotiated (who gets
  to claim sick role, for how long, with what obligations).
  Mental illness stigma: sickness status denied or over-applied.

  APPLICATION:
  A patient with chronic pain has a disease (possibly), an
  illness (definitely — they suffer), and a contested sickness
  status (employer/insurer may deny the sick role).
  Effective care addresses all three levels.
```

### Structural Violence — Paul Farmer

```
  "STRUCTURAL VIOLENCE" (Farmer, "Infections and Inequalities"):
  Harm caused by social structures (economic systems,
  political arrangements, institutions) rather than direct
  individual action. Not a person's fault; not random.

  TB in Haiti:
  - TB is a curable bacterial infection
  - Most TB deaths occur in poor countries, among poor people
  - Farmer's work in central Haiti: TB is not spreading
    "because Haitians don't understand germ theory"
  - It is spreading because: malnutrition (compromised
    immunity), crowded housing (transmission), no access
    to treatment, inability to take drugs on empty stomach

  The social structure produces disease.
  The solution is not education campaigns — it is reducing
  the structural conditions (poverty, access to food,
  access to care) that make populations vulnerable.

  Partners in Health (PIH) model:
  Community health workers + direct care + social support
  (food, transportation, incentives to complete treatment).
  Dramatically improves treatment completion.
  Later: proven in Boston with homeless population.

  APPLICATION TO TECH:
  The "digital divide" is structural violence in Farmer's
  sense. The populations most impacted by poor digital
  infrastructure (rural US, developing world) are not
  experiencing failure because of individual choices — they
  are experiencing a structural condition that systematically
  denies access to tools others take for granted.
```

---

## Section 2: Development Anthropology

### James Scott — Seeing Like a State (1998)

```
  THE PROBLEM: Why do major development projects backed by
  technical expertise, funding, and political will so
  consistently fail to achieve their goals?

  Scott's analysis of high-modernist disasters:
  - Soviet collectivization
  - Ujamaa villages (Tanzania forced resettlement)
  - High-modernist urban planning (Le Corbusier, Pruitt-Igoe)
  - Green Revolution side effects

  THREE NECESSARY CONDITIONS FOR DISASTER:
  ┌────────────────────────────────────────────────────────┐
  │ 1. LEGIBILITY PROJECTS: making local systems legible   │
  │    to the state (cadastral mapping, standardized       │
  │    measurements, surnames, census categories)          │
  │    Simplification enables intervention but destroys    │
  │    local complexity.                                   │
  │                                                        │
  │ 2. HIGH-MODERNIST IDEOLOGY: faith in scientific        │
  │    planning and rational redesign of social/natural    │
  │    order. "We know better." The pretense that          │
  │    knowledge can be complete.                          │
  │                                                        │
  │ 3. AUTHORITARIAN STATE: ability to impose the plan     │
  │    regardless of local resistance.                     │
  │                                                        │
  │ (+ weak civil society unable to resist or modify)      │
  └────────────────────────────────────────────────────────┘

  METIS vs. TECHNE:
  Techne: formal, systematic knowledge. The blueprint.
  Metis: practical, local, adaptive knowledge. The farmer
  who knows this field. Cannot be codified. Destroyed by
  abstraction.

  The plan fails because it replaces metis (local knowledge)
  with techne (standardized knowledge), and the residue of
  local complexity that the plan cannot model is precisely
  what made the local system work.

  VP-LEVEL RELEVANCE:
  Platform migrations, org redesigns, and process mandates
  that ignore local team culture and work practices
  are Scott's scenario at corporate scale.
  The "agile transformation" that imposes a single process
  template on 50 teams with different domains, customers,
  and technical constraints — and then wonders why teams
  are doing "agile theater" — is legibility + high-modernism
  + authority without feedback.
```

### Participatory Development and FPIC

```
  PARTICIPATORY DEVELOPMENT: communities are not
  beneficiaries of development interventions — they are
  co-designers and co-implementers.

  Robert Chambers' "Putting the Last First" (1983):
  - Reverse learning: professionals learning from
    community members rather than teaching
  - Participatory Rural Appraisal (PRA): methods that
    make local knowledge visible and usable
    (community mapping, seasonal calendars, wealth ranking
    done by community members, not external consultants)

  CRITIQUE OF PARTICIPATION (Mosse 2005):
  "Imposing Aid" and later critiques: participatory
  processes can become performance. Communities tell
  development workers what they want to hear. Power
  differentials persist. "Participation" becomes a
  legitimating ritual rather than genuine co-design.

  The insight: participation is institutionally productive
  even when substantively hollow — it produces the
  narrative of community buy-in that donors and agencies
  need. Cynical but analytically important.

  FREE, PRIOR, AND INFORMED CONSENT (FPIC):
  UN Declaration on the Rights of Indigenous Peoples (2007):
  Indigenous communities have the right to give or withhold
  consent to projects affecting their lands and resources —
  BEFORE those projects begin, with full information,
  without coercion.

  This is not just ethics — it is law in many jurisdictions.
  Mining, pipeline, and infrastructure projects that ignore
  FPIC face injunctions, protests, and legal liability.
```

---

## Section 3: Design Ethnography and Corporate Applications

### IDEO and the Human-Centered Design Methodology

```
  IDEO (founded 1991, David Kelley) popularized:
  Human-centered design = design informed by ethnographic
  observation of actual users in actual contexts.

  THE PROCESS:
  ┌────────────────────────────────────────────────────────┐
  │ 1. EMPATHIZE: ethnographic observation                 │
  │    - "Follow the user home" — observe in natural context│
  │    - Shadowing, contextual interviews                  │
  │    - NOT: focus groups, surveys, stated preferences    │
  │    Why: people say what they think they should do;     │
  │    observation reveals what they actually do.          │
  │                                                        │
  │ 2. DEFINE: synthesize observations into insight        │
  │    - "How might we..." problem reframing               │
  │    - Identify unmet needs, workarounds, frustrations   │
  │                                                        │
  │ 3. IDEATE: generate options                            │
  │ 4. PROTOTYPE: make it tangible quickly                 │
  │ 5. TEST: with actual users, iterate                    │
  └────────────────────────────────────────────────────────┘

  KEY INSIGHT — OBSERVATION VS. STATED PREFERENCE:
  The classic IDEO example: observed that hospital workers
  in EMERGENCY DEPARTMENTS NEVER USE CRASH CARTS CORRECTLY
  because cart drawers were consistently in wrong positions
  for their actual workflow (not the designed workflow).
  Surveys showed: "carts work fine." Observation showed:
  workarounds everywhere.

  This is Suchman's "plans vs. situated action" in product form.
```

### Contextual Inquiry — Holtzblatt and Jones

```
  CONTEXTUAL DESIGN (Karen Holtzblatt, Hugh Beyer):
  A formalized version of ethnographic fieldwork for
  software and product design contexts.

  THE CONTEXTUAL INQUIRY INTERVIEW:
  Not: "How do you do your job?"
  Instead: "Show me how you're doing it right now. I'll
  watch and ask questions as you go."

  Four principles:
  ┌────────────────────────────────────────────────────────┐
  │ 1. CONTEXT: observe in the actual work environment,    │
  │    not a usability lab                                 │
  │ 2. PARTNERSHIP: researcher and user as partners        │
  │    exploring the work together                         │
  │ 3. INTERPRETATION: share interpretations in real time  │
  │    ("It looks like you're doing X because Y — is       │
  │    that right?") Get corrections immediately.          │
  │ 4. FOCUS: guided by a research agenda, not a rigid     │
  │    script. Follow interesting threads.                 │
  └────────────────────────────────────────────────────────┘

  WORK MODELS (Holtzblatt's five models):
  ┌────────────────────────────────────────────────────────┐
  │ Flow model: communication and coordination between     │
  │   people. Who talks to whom, when, about what.         │
  │ Cultural model: policies, values, influencers — the    │
  │   invisible rules governing work.                      │
  │ Artifact model: documents, tools, objects used in      │
  │   work — their structure and meaning.                  │
  │ Physical model: physical environment and how it        │
  │   shapes work (desk arrangement, interruptions, etc.)  │
  │ Sequence model: steps taken to accomplish key tasks    │
  │   (often reveals actual vs. designed workflow gap).    │
  └────────────────────────────────────────────────────────┘

  These are directly the "thick description" tools of
  ethnography applied to product design contexts.
```

### Corporate Ethnography in Tech — The Applied Anthropology Tradition

```
  LUCY SUCHMAN at XEROX PARC (1987):
  "Plans and Situated Actions" — the foundational text for
  design ethnography in tech. (See 07-COGNITIVE-CULTURAL.md)

  MICROSOFT'S ANTHROPOLOGICAL TRADITION:
  ┌────────────────────────────────────────────────────────┐
  │ Microsoft Research: CHI (Computer-Human Interaction)   │
  │ and CSCW (Computer Supported Cooperative Work) are     │
  │ the conferences where social science meets computing.  │
  │                                                        │
  │ EPIC conference (Ethnographic Praxis in Industry):     │
  │ Corporate ethnographers from Microsoft, Google,        │
  │ Intel, IDEO sharing methodology and findings.          │
  │                                                        │
  │ Intel's People and Practices Research group:           │
  │ Pioneered deployment of professional ethnographers in  │
  │ product teams (Genevieve Bell).                        │
  │                                                        │
  │ danah boyd (MSR): Technology and society research —    │
  │ ethnography of teen social media use; privacy norms;   │
  │ algorithmic accountability. Applied anthropological    │
  │ methods to digital contexts.                           │
  └────────────────────────────────────────────────────────┘

  THE GAP THE VP MANAGES:
  Research team delivers insights. Product team has sprints.
  The organizational gap between "we observed X about users"
  and "feature Y ships in 3 weeks" is where anthropological
  insight most often fails to influence product.

  Structure that works:
  - Embedded researchers in product teams (not central labs)
  - Synthesis artifacts that map to product decisions
    (personas, opportunity maps — not just reports)
  - Research findings that match decision-making cadence
  - Translation layer between research language and
    engineering language (this is a practice design problem)
```

---

## Section 4: Forensic Anthropology in Human Rights Contexts

### Mass Grave Investigation

```
  DEPLOYMENT CONTEXTS:
  - International Criminal Tribunal (ICTY — Yugoslavia)
  - ICMP (International Commission on Missing Persons —
    Bosnia/Herzegovina): 8,100+ Srebrenica victims
  - AAAS Science and Human Rights Program
  - EAAF (Argentine Forensic Anthropology Team) — model
    for all later efforts; pioneered aDNA for victim ID
  - FAFG (Guatemalan Forensic Anthropology Foundation)
  - INFORCE (UK forensic team deployed to Iraq, Kosovo, etc.)

  THE METHODOLOGY:
  ┌────────────────────────────────────────────────────────┐
  │ 1. SITE LOCATION:                                      │
  │    - Witness testimony + satellite imagery + LiDAR     │
  │    - Ground-penetrating radar to confirm disturbed     │
  │      ground without excavation                         │
  │                                                        │
  │ 2. ARCHAEOLOGICAL EXCAVATION:                          │
  │    - Full forensic context documentation               │
  │    - Secondary graves (moved to hide evidence): most   │
  │      complex; bodies scattered, commingled             │
  │    - Chain of custody for all evidence                 │
  │                                                        │
  │ 3. MORTUARY ANALYSIS:                                  │
  │    - Individual inventory (count, articulation)        │
  │    - Biological profile each individual                │
  │    - Cause of death documentation (gunshot location,   │
  │      trajectory, perimortem injury pattern)            │
  │    - Personal effects (clothing, documents, artifacts) │
  │                                                        │
  │ 4. IDENTIFICATION:                                     │
  │    - Ante-mortem data collection from families         │
  │    - DNA: blood reference from families; aDNA from     │
  │      remains; STR profile matching                     │
  │    - Dental/medical record comparison                  │
  │    - ICMP DNA database: >8,000 IDs in Bosnia           │
  │                                                        │
  │ 5. REPATRIATION: death certificate issued;             │
  │    family receives remains for burial                  │
  └────────────────────────────────────────────────────────┘

  DAUBERT STANDARD (US federal courts, 1993):
  Expert scientific testimony must be:
  1. Based on a testable theory or technique
  2. Peer-reviewed and published
  3. With known or knowable error rates
  4. Using generally accepted standards in the field

  Forensic anthropologists testify under this standard.
  The biological profile and trauma analysis must be
  reproducible, not "expert opinion" in the subjective sense.
```

---

## Section 5: Heritage Management

### UNESCO World Heritage and the Conservation Tension

```
  UNESCO WORLD HERITAGE CONVENTION (1972):
  Sites of "outstanding universal value" designated and
  protected. As of 2024: ~1,200 sites across 168 countries.

  THE FUNDAMENTAL TENSION:
  ┌────────────────────────────────────────────────────────┐
  │ CONSERVATION:               USE:                       │
  │ Preserve the site for       The community living       │
  │ future generations.         with the site needs it     │
  │ Minimize alteration.        for daily life.            │
  │                                                        │
  │ Often: conservation         Stone Town Zanzibar:       │
  │ benefits tourists,          WH inscription raised      │
  │ not residents.              rents, displaced           │
  │ UNESCO designation          residents, benefited       │
  │ raises land values.         tourism operators.         │
  └────────────────────────────────────────────────────────┘

  INTANGIBLE CULTURAL HERITAGE (2003 Convention):
  Recognizes that important heritage is not always material:
  - Traditional performing arts
  - Oral traditions
  - Ritual practices
  - Traditional craftsmanship
  - Social practices and knowledge

  Japan uses this well: Living National Treasures
  (practitioners of traditional crafts designated and
  supported to transmit their knowledge to apprentices).
```

### NAGPRA — Extended Analysis

```
  NATIVE AMERICAN GRAVES PROTECTION AND REPATRIATION ACT (1990):

  WHY IT EXISTS:
  In the 19th-20th centuries, thousands of Native American
  remains entered US museum collections:
  - Battlefield dead collected by US Army surgeons
    (Surgeon General's Order 1868: collect Native American
    crania for "racial science" studies)
  - Graves opened by archaeologists without tribal consent
  - Objects acquired under coercion or during disruption

  Samuel Morton (19th c.): measured ~1,000 skulls to "prove"
  racial hierarchy (Native Americans = inferior). Gould's
  "Mismeasure of Man" exposed the data fabrication.

  WHAT NAGPRA REQUIRES:
  Federal agencies and federally funded institutions:
  1. Inventory human remains and cultural items
  2. Consult with affiliated tribes
  3. Respond to repatriation requests (90-day clock)
  4. Transfer items (or explain why culturally unaffiliated)

  KENNEWICK MAN / THE ANCIENT ONE:
  ┌────────────────────────────────────────────────────────┐
  │ 1996: Complete skeleton found on Columbia River bank,  │
  │ Washington state. 9,000 years old.                     │
  │                                                        │
  │ Scientists (Chatters et al.): claimed "Caucasoid"      │
  │ morphology -> not Native American -> no NAGPRA claim   │
  │ (incorrect racial typology)                            │
  │                                                        │
  │ Tribes (Umatilla, Colville, Yakama, Nez Perce,         │
  │ Wanapum): oral tradition + geographic continuity;      │
  │ this is "The Ancient One" — a relative                 │
  │                                                        │
  │ 9-year legal battle (Bonnichsen v. United States).     │
  │ Scientists studied the remains during litigation.      │
  │                                                        │
  │ 2015: Ancient DNA (Reich lab) showed: closest living   │
  │ relatives are Indigenous Americans, specifically       │
  │ Colville tribe. The "Caucasoid" claim was false.       │
  │                                                        │
  │ 2017: Reburied by tribes.                              │
  └────────────────────────────────────────────────────────┘

  LESSON: The "science vs. tribes" framing was false.
  The science supported the tribes. The initial "Caucasoid"
  claim used discredited 19th-century racial typology.
```

---

## Section 6: Decolonizing Research — CARE and FAIR

### Linda Tuhiwai Smith — Decolonizing Methodologies

```
  "Decolonizing Methodologies" (Tuhiwai Smith 1999):

  Central argument: research methodology is not neutral.
  The frameworks, questions, data categories, and
  publication norms of Western academic research encode
  colonial power relations and continue colonial extraction.

  EXTRACTION MODEL OF RESEARCH:
  Researcher enters community -> gathers data ->
  leaves -> publishes in external journals ->
  community never sees results -> results may be used
  against community's interests -> researcher gets promoted.

  The community is an object of study; the academic
  institution captures the value.

  ALTERNATIVE: Community-based participatory research (CBPR)
  ┌────────────────────────────────────────────────────────┐
  │ Community identifies research questions                │
  │ Community members are co-investigators                 │
  │ Research design is co-developed                        │
  │ Data stays with community (or jointly held)            │
  │ Publications require community review and co-authorship│
  │ Results returned to community in usable form           │
  │ Researcher is accountable to community, not just       │
  │ to funders and journals                                │
  └────────────────────────────────────────────────────────┘
```

### CARE vs. FAIR — Data Sovereignty in Tension

```
  FAIR PRINCIPLES (scientific data sharing, Wilkinson 2016):
  Findable, Accessible, Interoperable, Reusable.
  Goal: maximize scientific value by making data openly
  available for re-use and meta-analysis.

  CARE PRINCIPLES (Indigenous data governance, 2020):
  Collective Benefit, Authority to Control,
  Responsibility, Ethics.
  Goal: Indigenous communities govern how data about them,
  collected from them, or describing their territories
  and cultural heritage is used.

  THE TENSION:
  ┌────────────────────────────────────────────────────────┐
  │ FAIR says: genomic data should be in open repositories │
  │           for other scientists to use.                 │
  │                                                        │
  │ CARE says: Indigenous genomic data may be subject to   │
  │           tribal governance. The tribe decides who     │
  │           can access it, for what purposes.            │
  │                                                        │
  │ Example: A study collects DNA from an Indigenous       │
  │ community to study disease risk. FAIR: put it in       │
  │ dbGaP (public genomic repository). CARE: does the      │
  │ tribe want their genetic information accessible to     │
  │ pharmaceutical companies? Ancestry.com? Government?    │
  │ The tribe should decide.                               │
  └────────────────────────────────────────────────────────┘

  RESOLUTION (emerging practice):
  FAIR for non-sensitive, consented data.
  CARE governing access controls for sensitive heritage
  and biological data.
  Tribal data sovereignty clauses in research agreements.
  The Global Indigenous Data Alliance develops governance
  frameworks for this intersection.

  TECH INDUSTRY RELEVANCE:
  This tension mirrors data governance debates in enterprise:
  "Open data" maximizes reuse and analytics value;
  "Data sovereignty" (GDPR, CCPA) maximizes privacy/control.
  The resolution pattern is similar: technical access controls
  + governance frameworks + consent architecture.
  The CARE/FAIR tension is the indigenous data version of
  the same underlying conflict between data utility and
  data sovereignty.
```

---

## Decision Cheat Sheet

| I want to do... | Anthropological tool |
|----------------|---------------------|
| Understand why users don't follow the manual | Kleinman's explanatory model elicitation |
| Understand actual vs. designed workflow | Contextual inquiry (Holtzblatt) + sequence model |
| Understand why top-down org redesign fails | Scott "Seeing Like a State" — metis vs. techne |
| Build genuine community participation in design | CBPR + FPIC principles |
| Understand why "collaboration" programs produce compliance | Mosse's "participation as performance" |
| Conduct user research that captures real behavior | Follow-home ethnography, not surveys/focus groups |
| Handle indigenous data in research/products | CARE principles + tribal consultation |
| Identify human remains in legal or humanitarian context | Forensic anthropology biological profile + Daubert |
| Return cultural property to source communities | NAGPRA process + international repatriation frameworks |
| Bridge research insights to product decisions | Embedded researchers + synthesis artifacts (personas, opportunity maps) |

---

## Common Confusion Points

**"User research = usability testing."**
Usability testing evaluates a prototype. User research in the ethnographic
tradition precedes the prototype — it discovers what the problem is, what
users actually do, what mental models they bring. Usability testing tells you
whether your solution works; ethnographic research tells you whether your
solution solves the right problem.

**"FPIC is just a checkbox."**
In many industry implementations, yes — consent forms signed before a
meeting occurs. Genuine FPIC requires ongoing consultation, the realistic
possibility of refusal, and community capacity to evaluate the proposal.
Communities that routinely say yes to everything are demonstrating
that the "prior" and "informed" components failed. Anthropologists
distinguish formal compliance from substantive FPIC.

**"Structural violence is a political opinion, not an analysis."**
Farmer's structural violence framework makes empirical predictions:
disease distribution will track economic marginalization, not random
variation; interventions targeting individual behavior (education campaigns)
will fail while structural interventions (food security, access to care) will
succeed. These are testable claims. The data from Partners in Health programs
in Haiti, Rwanda, and Boston supports the structural analysis.

**"NAGPRA vs. science is a zero-sum trade-off."**
The Kennewick Man case showed the opposite: the science supported the tribal
claim. The "scientific access" argument relied on 19th-century racial typology.
Modern aDNA and population genetics has generally aligned with tribal claims
about ancestry and continuity. NAGPRA consultation often produces research
partnerships; it does not inherently preclude science.

**"Organizational culture is soft — HR handles it."**
Bourdieu on habitus in institutional contexts: organizational culture is a
structured field in which participants deploy different forms of capital,
pursue strategies shaped by internalized dispositions, and resist changes
that threaten their field position. "HR handles it" is the legibility problem
Scott identifies — reducing complex practice dynamics to a manageable
category. Cultural change requires changing the structural conditions
(incentives, resource allocation, promotion criteria, who holds power)
that generate the habitus, not running culture programs.
