# Content Strategy: Audit, Taxonomy, Governance, Voice and Tone

## The Big Picture

```
CONTENT STRATEGY SCOPE
=======================

+------------------------------------------------------------------+
|                    CONTENT STRATEGY                              |
|                                                                  |
|  "Content strategy plans for the creation,                       |
|   publication, and governance of useful,                         |
|   usable content." — Kristina Halvorson (2008)                  |
|                                                                  |
|  SUBSTANCE           STRUCTURE            WORKFLOW              |
|  (what content)      (how organized)      (how created)         |
|  Content types       Taxonomy             Roles                  |
|  Key messages        Metadata             Process               |
|  User needs          IA / navigation      Tools                 |
|  Gaps / redundancy   Labeling             Governance            |
|                                                                  |
|  VOICE & TONE        EDITORIAL STANDARDS  GOVERNANCE            |
|  (how it sounds)     (writing rules)      (who decides)         |
|  Brand voice         Style guide          Ownership             |
|  Tone variations     Grammar/usage        Approval chain        |
|  Consistency         Formatting rules     Maintenance           |
+------------------------------------------------------------------+
```

**The core problem content strategy addresses**: organizations accumulate content over time without systematic planning. The result is redundancy (three versions of the same FAQ), orphaned pages (no navigation path to them), outdated information (still saying "new product" for a 5-year-old feature), and inconsistent voice (each team writes their own way). Content strategy is the discipline that prevents and cleans up this entropy.

---

## Halvorson's Content Strategy Framework

Kristina Halvorson's *Content Strategy for the Web* (2008, 2nd ed. 2012) is the foundational text of the discipline:

```
HALVORSON'S FOUR QUESTIONS
============================

1. WHY are we making this content?
   What problem does it solve?
   For whom?
   What business goal does it serve?
   -> Content without a "why" is clutter

2. WHAT content do we need?
   What does the user need to accomplish their goal?
   What information gaps exist?
   What content types serve this need? (article? video? FAQ?)
   -> Content audits answer this question

3. HOW does it get created, maintained, and deleted?
   Who writes it? Who reviews it? Who approves it?
   What tools are used (CMS, DAM)?
   What is the workflow?
   -> Governance models answer this question

4. WHO is responsible?
   Clear ownership prevents orphaned content
   Accountability for accuracy and freshness
   -> Roles and responsibilities chart
```

---

## Content Audit Methodology

A content audit is the inventory + analysis of all existing content:

```
CONTENT AUDIT PROCESS
======================

PHASE 1: INVENTORY
  Goal: complete list of all content that exists

  Full quantitative audit:
    Crawl the site/repository with a tool (Screaming Frog, Sitebulb)
    Output: URL, page title, word count, last modified date,
            inbound links, meta description, status code
    This is the "content inventory" -- it tells you WHAT exists

  Sample qualitative audit:
    Random or purposive sample (say, 20% of URLs)
    Manual evaluation of each: quality, accuracy, relevance
    This is too slow for full sites; sampling is acceptable

PHASE 2: ANALYSIS
  For each piece of content, evaluate:
  - Is it accurate? (When was it last verified?)
  - Is it relevant? (Does anyone need this?)
  - Is it findable? (Can users navigate to it?)
  - Is it consistent? (Does it match standards?)
  - Is it complete? (Does it answer the user's question?)

  Assessment categories:
  KEEP: accurate, relevant, well-trafficked
  UPDATE: useful but needs refreshing
  REVISE: good purpose, poor execution
  REDIRECT: content moved or merged elsewhere
  DELETE: outdated, irrelevant, or redundant

PHASE 3: RECOMMENDATIONS
  Content gap report: what needed content is missing?
  Content bloat report: what can be removed?
  Priority matrix: effort vs. value (impact/effort 2x2)
  Migration plan: if moving to new CMS/structure
```

---

## Taxonomy Design

Taxonomy in information architecture: a controlled vocabulary and classification scheme for organizing content.

```
TAXONOMY CONCEPTS
==================

CONTROLLED VOCABULARY:
  Authorized terms for categorizing content
  vs. "free tagging" (folksonomy): users apply their own tags
  Controlled: consistent, findable, searchable
  Folksonomy: flexible, reflects user language, messy

  Tradeoffs:
    Controlled vocab: requires governance; resists obsolescence
    Folksonomy: requires cleanup; captures emergent terms

HIERARCHICAL TAXONOMY:
  Parent -> child categories
  Example: Products > Software > Cloud Services > Azure
  Navigation use: breadcrumbs follow the hierarchy
  Challenge: items belong to multiple categories (polyhierarchy)

FACETED CLASSIFICATION:
  Multiple independent dimensions (facets) applied to content
  Example: product classified by:
    Category: Software
    Platform: Cloud
    Audience: Enterprise
    Feature: AI
  User can filter by any combination of facets
  E-commerce: standard (filter by color + size + brand)
  Enterprise: powerful for document management

FLAT TAGGING:
  No hierarchy; items receive tags from flat list
  Simple to implement; discovery via tag clouds / tag pages
  Problem: synonyms proliferate ("machine learning" + "ML" + "AI")
  Solution: tag normalization (synonym rules)

METADATA SCHEMA:
  The attributes defined for each content item
  Minimum: title, author, date, category, tags
  Extended: audience, product, geography, lifecycle status
  Dublin Core: standard metadata vocabulary (15 core elements)
  Schema.org: machine-readable metadata standard
```

---

## Voice and Tone

**Voice** is consistent across all content. **Tone** varies by context.

```
VOICE vs. TONE
===============

VOICE (invariant):
  The personality of the brand/organization expressed through content
  "We are [these three adjectives]" always
  Example: Mailchimp voice = "funny, direct, genuine"
  This voice appears in every piece of Mailchimp content
  -> in error messages, in marketing, in documentation

TONE (context-variable):
  How you express the voice changes with the emotional context
  Same organization; different emotion register

  Mailchimp example:
  Success confirmation tone: celebratory, enthusiastic
  Error message tone: calm, direct, not humorous
    (user is frustrated; jokes make it worse)
  Marketing tone: playful, confident
  Legal/privacy tone: clear, direct, less personality

TONE AXES:
  Formal <-----> Casual
  Serious <-----> Funny
  Irreverent <-----> Respectful
  Enthusiastic <-----> Matter-of-fact
  Different contexts call for different positions on each axis

VOICE CHART (Mailchimp canonical model):
  | Voice characteristic | NOT this        | But THIS        |
  |---------------------|-----------------|-----------------|
  | Funny, not childish | Immature jokes  | Wit and levity  |
  | Confident, not bossy| "You must..."   | "You can..."    |
  | Smart, not academic | Jargon          | Clear expertise |
  | Expert, not elitist | Exclusionary    | Accessible      |
```

---

## Governance Models

How organizations manage who controls content decisions:

```
CONTENT GOVERNANCE MODELS
===========================

CENTRALIZED:
  Single team controls all content creation and publishing
  Advantage: consistency, quality control
  Disadvantage: bottleneck; slow; disconnected from subject matter

  Typical: small organizations; brand-critical content
  Structure: Central Content Team owns all web content
             All requests go through this team

DISTRIBUTED:
  Each team/department creates and publishes their own content
  Advantage: speed, subject matter expertise, autonomy
  Disadvantage: inconsistency, duplication, orphans

  Typical: large organizations where centralized is impossible
  Structure: Each team has a "content owner" who publishes
             A style guide exists but adherence varies

FEDERATED (Hub-and-Spoke):
  Central team sets standards, guidelines, shared components
  Individual teams create content within those standards
  Central team audits and advises; does not control

  Typical: large organizations that want consistency + autonomy
  Structure:
    Hub: Content strategy team + CMS governance + Style guide
    Spokes: Product teams, Marketing, Support, each with content owners
  This is the most common enterprise model

EDITORIAL BOARD:
  Cross-functional group makes decisions collectively
  Advantage: buy-in, multiple perspectives
  Disadvantage: slow, committee decisions
  Typical: media organizations, content-heavy institutions
```

---

## Content Operations

The systems and processes that make content work at scale:

```
CONTENT OPERATIONS (ContentOps)
=================================

CMS (Content Management System):
  Platform for creating, storing, publishing content
  Headless CMS: separates content from presentation
    Content API -> multiple frontends (web, mobile, kiosk)
    Examples: Contentful, Sanity, Strapi
  Traditional CMS: tightly coupled to one display layer
    Examples: WordPress, Drupal, Sitecore

DAM (Digital Asset Management):
  Repository for images, videos, PDFs, branded assets
  Metadata, rights management, version control for assets
  Examples: Bynder, Canto, Brandfolder

WORKFLOW:
  Brief -> Draft -> Review -> Approval -> Publish -> Maintain
  Each stage: who does it, what tool, what criteria
  Bottlenecks: typically in review/approval (legal, compliance)

ROLES:
  Content Strategist: plans, audits, governs
  Content Designer: UX-oriented, product content
  Copywriter: marketing and campaign content
  Technical Writer: documentation, product guides
  Editor: quality, consistency, style enforcement
  Content Operations Manager: systems, tools, process

METRICS FOR CONTENT OPERATIONS:
  Time from brief to publish (efficiency)
  Content accuracy audit score (quality)
  % content reviewed within X months (freshness)
  Traffic / engagement (effectiveness)
  Duplicate content rate (redundancy)
```

---

## Decision Cheat Sheet

| Question | Content strategy answer |
|----------|------------------------|
| We have too much content; what to keep? | Content audit: inventory + analyze + prioritize keep/update/delete |
| Our content is inconsistent across teams | Federated governance + shared style guide |
| Users can't find our content | Taxonomy/IA review; faceted classification if complex |
| Brand sounds different in each channel | Defined voice + tone guide with examples |
| Content becomes outdated quickly | Assign owners; set review cadence; build into workflow |
| We don't know who owns each content item | Governance model clarification + RACI matrix |

---

## Common Confusion Points

**Content strategy is not content marketing.** Content marketing is a promotional technique (produce valuable content to attract buyers). Content strategy is an organizational discipline applied to all content, including product UX copy, support documentation, and internal knowledge bases. Content marketing is a subset.

**Voice and tone are not the same.** Voice is invariant brand personality. Tone is how you express that voice in a specific context. Getting this wrong produces either robotic consistency (same tone for legal disclaimers and product celebrations) or incoherent inconsistency (different personality in each channel).

**Content audits require tools.** Doing a manual inventory of a 10,000-page site is not viable. Crawlers (Screaming Frog: free up to 500 URLs; paid for more) automate the inventory phase. The analysis still requires human judgment.

**Taxonomy is not navigation.** Taxonomy is the classification system. Navigation is how users move through the content. They are related but distinct. Good taxonomy supports multiple navigation paths; navigation forces users down one path.

**"Just use AI to write the content" does not solve a content strategy problem.** AI can accelerate writing, but content produced at AI speed without strategy still becomes a pile of inconsistent, orphaned, duplicated content. The strategy problem is upstream of the writing problem.
