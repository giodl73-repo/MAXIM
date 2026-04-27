# Architecture Design Process

## The Big Picture

The architecture design process is not linear. It spirals: each phase revisits earlier decisions at higher resolution. But the phases impose a governance structure — major decisions made late cost exponentially more to change, so the process front-loads design intent and back-loads documentation.

```
+--------------------------------------------------------------------+
|                    AIA PHASE STRUCTURE (US)                        |
|                                                                    |
|  PRE-DESIGN        SD         DD            CDs         CA         |
|  ─────────       ──────     ──────        ──────      ──────       |
|  Programming     15%        35%            65%        construction |
|  Site analysis   design     design         design     admin        |
|  Feasibility     complete   complete       complete                |
|                                                                    |
|  ~5% of fee    ~15%       ~20%           ~40%       ~20% of fee    |
|                                                                    |
|  DECISIONS MADE vs COST TO CHANGE:                                 |
|  ────────────────────────────────────────────────────────────      |
|  SD: 15% decisions → determine 80% of project cost                 |
|      1x cost to change                                             |
|  DD: 35% decisions locked                                          |
|      10–50x cost to change                                         |
|  CDs: 65% decisions locked                                         |
|      100–200x cost to change                                       |
|  Field: 5% undecided surprises                                     |
|      500–1,000x cost to change                                     |
|                                                                    |
|  This is the Boehm curve applied to buildings.                     |
+--------------------------------------------------------------------+
```

---

## AIA Phases

### Pre-Design / Programming

Programming translates client requirements into spatial and technical criteria before any design begins. Often done by a specialist programming consultant (CRS-style); sometimes done by the architect as an early phase service.

```
  PROGRAMMING DELIVERABLES
  ==========================

  AREA SCHEDULE:           Rooms × areas × adjacencies × occupancy
  FUNCTIONAL DIAGRAM:      Organizational chart of spaces
  SITE CRITERIA:           Zoning, setbacks, FAR, height limits,
                           parking requirements, utilities
  SUSTAINABILITY GOALS:    LEED level, energy target, certifications
  BUDGET PARAMETERS:       Cost/sqft benchmarks, contingency
  SCHEDULE REQUIREMENTS:   Occupancy date, phasing constraints
  CODE REQUIREMENTS:       Occupancy classification, egress
                           requirements, accessibility
  TECHNICAL REQUIREMENTS:  For specialized programs
                           (data center tier, OR suite, lab biosafety)

  THIS PHASE OFTEN REVEALS THAT THE CLIENT'S
  PROGRAM CANNOT FIT THE BUDGET OR SITE.
  The architect's job is to say so before design starts.
```

### Schematic Design (SD)

The concept phase. Design decisions at this phase determine the vast majority of project cost.

```
  SD DELIVERABLES
  ================

  Site plan (scale: 1"=20' to 1"=50')
  Floor plans (1"=20' to 1"=10')
  Building sections (1"=20' to 1"=10')
  Exterior elevations
  Concept structural system description
  Concept MEP strategy (not sized)
  Outline specifications (major materials/systems)
  SD cost estimate (±20–30% accuracy)
  Preliminary LEED scorecard

  WHAT GETS RESOLVED IN SD:
  ─────────────────────────
  - Building massing and orientation on site
  - Structural grid and system type
  - Circulation hierarchy (primary paths, vertical cores)
  - Major program spaces located and dimensioned
  - Facade strategy (curtain wall vs masonry vs rainscreen)
  - Site access, parking, utilities entry
  - Mechanical strategy (central plant, distributed, natural ventilation)

  SD IS THE CREATIVE PHASE.
  DD and CDs are engineering and documentation phases.
  If the design is weak at SD, the project never recovers.
```

### Design Development (DD)

All design decisions resolved. By the end of DD, there should be no unresolved design questions — only documentation remaining.

```
  DD DELIVERABLES
  ================

  All drawings at 1"=8' or 1"=4' (larger scale than SD)
  Architectural: all rooms dimensioned, materials specified,
                 key details resolved
  Structural: foundation type, all member sizes, connection types
  Mechanical: equipment selected, duct layout coordinated,
              terminal units sized
  Electrical: panel locations, riser diagram, lighting strategy
  Plumbing: fixture count, riser locations, equipment rooms
  BIM coordination: first round clash detection complete
  DD cost estimate (±15–20% accuracy)
  Updated LEED scorecard

  THE CLASH DETECTION IMPERATIVE:
  ─────────────────────────────────
  BIM coordination must happen in DD, not CDs.
  If ducts fight beams in DD → resolve in design (cheap).
  If ducts fight beams in CDs → resolve by RFI (expensive).
  If ducts fight beams in field → crisis (very expensive).
```

### Construction Documents (CDs)

CDs are the legal contract document — the specification against which contractors bid and build. They are NOT the design phase. Design is done.

```
  CD DELIVERABLES
  ================

  DRAWINGS:
  Site plan, grading, utilities (civil)
  Floor plans (1"=8' and 1"=4' scale)
  Reflected ceiling plans
  Elevations (all four sides)
  Building sections
  Wall sections (1"=1' scale)
  Details (1"=1' to full scale)
  Door, window, hardware schedules
  Finish schedule (every room, every surface)
  Equipment schedules
  Structural: all plan / section / detail / schedule drawings
  Mechanical: equipment, duct, pipe, equipment schedules
  Electrical: power, lighting, fire alarm plans + schedules
  Plumbing: plans, riser diagrams, fixture schedules
  Fire protection: sprinkler layout, hydraulic calcs

  TYPICAL DRAWING COUNT:
  ────────────────────────────────────────────────────────────────
  Small commercial (5,000 sqft):        20–50 sheets
  Medium commercial (50,000 sqft):      100–300 sheets
  Large hospital (500,000 sqft):        1,000–3,000 sheets
  Major data center campus:             500–2,000 sheets
```

### Specifications

The specifications are the written half of the construction documents. Drawings show WHERE and WHAT SHAPE; specifications show WHAT MATERIAL, WHAT STANDARD, WHAT QUALITY.

```
  CSI MASTERFORMAT — THE ORGANIZING SYSTEM
  ==========================================

  MasterFormat (CSI — Construction Specifications Institute)
  organizes all construction information into Divisions.
  The "OmniClass" of the built environment.

  DIVISION 00    Procurement and Contracting Requirements
  DIVISION 01    General Requirements
  DIVISION 02    Existing Conditions
  DIVISION 03    Concrete
  DIVISION 04    Masonry
  DIVISION 05    Metals
  DIVISION 06    Wood, Plastics, and Composites
  DIVISION 07    Thermal and Moisture Protection
  DIVISION 08    Openings (doors, windows, hardware)
  DIVISION 09    Finishes
  DIVISION 10    Specialties
  DIVISION 11    Equipment
  DIVISION 12    Furnishings
  DIVISION 13    Special Construction
  DIVISION 14    Conveying Equipment (elevators)
  DIVISION 21    Fire Suppression
  DIVISION 22    Plumbing
  DIVISION 23    HVAC
  DIVISION 25    Integrated Automation (BAS)
  DIVISION 26    Electrical
  DIVISION 27    Communications
  DIVISION 28    Electronic Safety and Security
  DIVISION 31    Earthwork
  DIVISION 32    Exterior Improvements
  DIVISION 33    Utilities

  EACH SECTION: Three parts
  Part 1 – General (administrative, submittals, quality control)
  Part 2 – Products (materials, manufacturers, properties)
  Part 3 – Execution (installation procedures, tolerances)

  SPEC BRIDGE TO SOFTWARE:
  The specification is the contract. Like a functional spec or
  API contract — it defines what the contractor must provide,
  to what standard, verified how. The architect reviews
  submittals (shop drawings, material samples) just as a PM
  reviews engineering designs for conformance to spec.
```

### Construction Administration (CA)

```
  CA SERVICES
  ============

  SUBMITTALS:
  Contractor submits shop drawings, product data, samples.
  Architect reviews for conformance to contract documents.
  NOT designing — verifying compliance.
  Typically 1,000–10,000 submittals on a large project.

  RFIs (Requests for Information):
  Contractor asks questions about unclear CDs.
  Architect provides clarification in writing.
  Typically 200–2,000 RFIs on a major project.
  RFI volume is a quality proxy for CDs.

  CHANGE ORDERS:
  Modifications to the contract scope, price, or schedule.
  Owner must approve all change orders.
  Change orders are the source of most construction disputes.
  The budget line for "owner contingency" exists because of this.

  SITE OBSERVATIONS:
  Architect visits site periodically (not full-time inspection).
  Documents conditions, notes non-conformances.
  Issues Architect's Supplemental Instructions (ASIs) for
  minor clarifications without cost impact.

  SUBSTANTIAL COMPLETION:
  Architect issues Certificate of Substantial Completion.
  Building is usable for intended purpose.
  Punch list: remaining items to complete (cosmetic, minor).

  FINAL COMPLETION:
  All punch list items closed.
  Architect issues final Application for Payment certificate.
  Owner receives as-built drawings (record drawings).
```

---

## RIBA Plan of Work (UK)

```
  RIBA PLAN OF WORK 2020 (UK standard)
  ======================================

  Stage 0    Strategic Definition
  Stage 1    Preparation and Briefing      (≈ AIA Pre-design / Programming)
  Stage 2    Concept Design               (≈ AIA Schematic Design)
  Stage 3    Spatial Coordination         (≈ AIA Design Development early)
  Stage 4    Technical Design             (≈ AIA Design Development + CDs)
  Stage 5    Manufacturing and Construction (≈ AIA CDs + CA)
  Stage 6    Handover                     (≈ AIA Substantial Completion)
  Stage 7    Use                          (Post-Occupancy Evaluation)

  KEY UK DIFFERENCE: "Technical Design" in Stage 4 integrates
  specialist contractor design earlier than US practice —
  cladding contractors, steel fabricators, etc. are brought
  in during design to provide fabrication-ready geometry.
  This is closer to design-build in philosophy.
```

---

## BIM (Building Information Modeling)

### What BIM Is

BIM is a database of building objects with properties, not just geometry. A wall in BIM has: geometry, fire rating, acoustic rating, thermal value, material, cost, maintainability notes, and a unique ID.

```
  BIM vs CAD
  ===========

  CAD                            BIM
  ───────                        ─────
  Lines, arcs, circles           Objects with properties
  No meaning                     Wall = fire rating + U-value + cost
  No coordination                Model coordinates automatically
  Drawings are the product       Drawings extracted from model
  2D primary                     3D primary
  No clash detection             Hard + soft clash detection
  No quantity take-off           Automatic QTO
  No lifecycle data              COBie data handoff to FM

  ANALOGY TO SOFTWARE:
  CAD = plain text files
  BIM = typed object model with a schema
  BIM coordination = static type checking applied to geometry
  BIM clash detection = runtime assertion on spatial conflicts
```

### BIM Maturity Levels

```
  BIM MATURITY LEVELS (PAS 1192 / BS EN 19650 — UK framework)
  =============================================================

  LEVEL 0    2D CAD. Unmanaged.
             Paper drawings or PDFs.

  LEVEL 1    3D modeling but no collaboration.
             Models not shared between disciplines.
             "BIM" in name only.

  LEVEL 2    Collaborative BIM.
             Each discipline has its own federated model.
             Models shared, coordinated via common data environment (CDE).
             UK Government mandate since 2016 for public projects.
             This is current standard for major projects.

  LEVEL 3    Integrated (OpenBIM / "iBIM").
             Single integrated model, all disciplines.
             IFC as the shared format.
             Real-time coordination.
             Contractually challenging (who owns the model?).
             Aspirational standard; limited real-world implementation.

  CURRENT REALITY (2024):
  Large commercial projects: Level 2 (federated BIM, clash detection)
  Most commercial work: Level 1–2
  Residential: often still Level 0–1
```

### Revit and IFC

```
  REVIT ECOSYSTEM
  ================

  Autodesk Revit: dominant authoring tool (~70% market share)
  Revit Architecture: walls, floors, roofs, casework
  Revit Structure: beams, columns, foundations
  Revit MEP: ducts, pipes, conduit, equipment

  REVIT FEATURES:
  - Families: parametric objects (a window with adjustable width)
  - Schedules: automatic from model (door schedule, room schedule)
  - Phases: construction phases, demolition, new work
  - Worksets: collaborative editing by team on same model
  - Dynamo: visual programming / automation plugin

  IFC (Industry Foundation Classes):
  ─────────────────────────────────────
  Open standard (buildingSMART International)
  Format: .ifc (text-based STEP format) or .ifcZIP
  Analogy: IFC is to BIM what STEP is to mechanical CAD
  Purpose: vendor-neutral exchange between Revit, ArchiCAD,
           CATIA, Tekla, etc.

  IFC LIMITATIONS:
  Round-trip fidelity: poor
  Export to IFC → import to another tool → data loss
  Proprietary tools retain their native formats for
  production; IFC is used for handoff, not authoring.

  COBie (Construction Operations Building Information Exchange):
  ──────────────────────────────────────────────────────────────
  Spreadsheet (Excel/CSV) containing asset data:
  Space names, equipment list, manufacturer data,
  warranty data, maintenance schedules, spare parts.
  Delivered to FM (facilities management) at handover.
  UK Government requires COBie on public projects.
  Analogy: COBie is the API documentation for the building's
  maintenance interface. The FM team inherits the building
  and needs to know what everything is and how to maintain it.
```

---

## Parametric and Computational Design

### Grasshopper + Rhino

```
  PARAMETRIC DESIGN WORKFLOW
  ============================

  RHINO (McNeel):
  - NURBS-based 3D geometry
  - Industry standard for complex freeform geometry
  - Used by: Zaha Hadid, Gehry, BIG, Snøhetta
  - Grasshopper: visual programming plugin

  GRASSHOPPER MENTAL MODEL:
  Input Parameters → Algorithm → Geometry Output

  [slider: column count]    →  [divide curve]
  [number: height]          →  [extrude]
  [material: glass/metal]   →  [evaluate geometry]
                               [export to fabrication]

  This is visual programming. The "code" is a network
  of connected nodes (components), not text.
  Analogy: Azure Data Factory pipeline = Grasshopper canvas.
  Both are dataflow programming environments.

  USES:
  - Facade panel rationalization (optimize complex curves to
    flat / developable / ruled surfaces for fabrication)
  - Structural form-finding (optimize geometry for stress)
  - Parametric planning (vary unit mix, density, setbacks)
  - Acoustic geometry (optimize concert hall shape for RT60)

  DYNAMO (Autodesk):
  - Visual programming plugin for Revit (like Grasshopper for Revit)
  - Python / C# scripting in Revit
  - Used for: automated model checking, parameter population,
    schedule processing, geometry generation
```

---

## Delivery Methods

```
  PROJECT DELIVERY COMPARISON
  =============================

  DESIGN-BID-BUILD (DBB)          DESIGN-BUILD (DB)
  ────────────────────────        ──────────────────
  Owner → Architect → CDs         Owner → DB Entity
                ↓                         │
           Competitive bid          ┌─────┴─────┐
                ↓                   │ Architect │ Contractor │
           GC selected              └─────┬─────┘
                ↓                         │
           Construction                   Build
                                          │
  Owner controls design.          Owner surrenders
  Architect is owner's rep.       design authority.
  Competitive pricing.            Single accountability.
  GC cannot influence design.     Speed to market.
  Most adversarial model.         Less architect independence.
  Disputes: GC claims not in CDs  Used in: data centers,
                                  warehouses, hospitals,
                                  fast-track commercial

  CONSTRUCTION MANAGER AT RISK (CMAR):  INTEGRATED PROJECT DELIVERY (IPD)
  ─────────────────────────────────     ─────────────────────────────────
  CM brought in at SD/DD.               Multi-party agreement:
  CM provides pre-construction          Owner + Architect + GC.
  services (pricing, schedule).         Shared risk and reward.
  CM holds all subcontracts.            Target cost contract.
  Architect retains design authority.   BIM-intensive.
  GMP (Guaranteed Maximum Price)        Early contractor involvement.
  provided at GMP milestone.            Collaborative culture required.
  Very common for complex               Rare; requires trust and
  institutional projects.               cultural alignment.

  DATA CENTER DELIVERY (typical):
  Owner/developer → Design-Build entity
  (usually major data center contractor: Turner, Whiting-Turner)
  Architect works for contractor.
  Speed is the primary driver (time to power = revenue).
  Standard prototypical designs repeated across campuses.
```

---

## Post-Occupancy Evaluation

```
  POE (POST-OCCUPANCY EVALUATION)
  ==================================

  The feedback loop that architecture rarely closes.

  WHAT IT IS:
  Systematic assessment of a building after occupation
  (typically 12 months post-occupancy).
  Measures: energy use, occupant satisfaction, spatial
  utilization, acoustic complaints, HVAC issues.

  WHY IT MATTERS:
  LEED modeling predicted energy → actual is 20–50% higher.
  Programmed spaces not used as designed.
  HVAC consistently complained about.
  Acoustic conditions not meeting design intent.

  TOOLS:
  Post-occupancy surveys (BUS Method — Building Use Studies)
  Energy meter readings vs EnergyPlus model
  Occupancy sensor data (badge access, IoT)
  Acoustic measurements vs design targets
  Indoor air quality monitoring

  THE PROBLEM:
  Architecture has no systematic feedback loop.
  Software teams have monitoring, logging, incident review.
  Architectural failures are often attributed to "users" or
  "facilities management" rather than design.

  Evidence-based design (healthcare architecture) is the
  exception — healthcare has mandated POE for some time.
  The "2030 Challenge" requires measured performance reporting.
```

---

## Decision Cheat Sheet

| Design situation | Process response | Phase |
|------------------|------------------|-------|
| Client wants to change the structural grid at 50% CDs | Hard stop — this is a SD decision. Show cost: redesign fees + schedule delay | SD must be locked before DD starts |
| RFIs are excessive during construction | Root cause: incomplete or ambiguous CDs. Fix the spec process. | CD quality review before issue |
| Contractor's price is 40% over budget | VE (Value Engineering) in DD, not CDs. If at CDs, expect scope reductions | SD cost estimate must validate against program |
| BIM clash count is very high in DD | Run clash detection at SD. Find the structural-MEP conflict early. | Coordination should start at DD, catch at SD |
| Client wants design-build to save time | Architect works for contractor. Set design standards upfront in RFP. | Before contract: get owner-controlled design criteria |
| Post-occupancy: energy use 30% over model | Audit occupant behavior, HVAC controls, envelope airtightness | POE 12 months after occupancy |
| Specification too tight, limits bidders | Specify performance, not manufacturer. "Equal substitution" clauses. | CDs |

---

## Common Confusion Points

**Schematic Design vs Conceptual Design**: Some firms add a "Concept Design" phase before SD (purely exploratory, no commitment). In AIA contracts, SD is the first billable design phase. The difference matters for contract scope.

**CDs vs shop drawings**: CDs are the architect's documents — they show what is required. Shop drawings are the contractor's documents — they show how the contractor proposes to build it. The architect reviews shop drawings for conformance to CDs, not to redesign. The difference: the contractor takes responsibility for their means and methods; the architect takes responsibility for design intent.

**BIM level confusion**: Saying "we use BIM" is like saying "we use version control." The question is: Level 2 federated with clash detection, or just 3D Revit models with no coordination? Level 2 with actual clash detection is the current industry standard. Most teams claiming BIM are operating at Level 1–1.5.

**Revit is not BIM**: Revit is one BIM authoring tool. BIM is the process and the data standard. A project using Revit without a common data environment, without coordination meetings, without clash detection is using Revit as fancy CAD — not BIM.

**Integrated Project Delivery hype vs reality**: IPD sounds optimal — owner, architect, and contractor aligned with shared risk/reward, BIM-intensive, collaborative. In practice, IPD requires deep mutual trust, and the legal framework (multi-party agreement) is unfamiliar to most construction lawyers. It works where organizations have built the relationship over multiple projects. It fails when procurement departments insist on traditional competitive bidding and then call it IPD.
