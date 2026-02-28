# /hunt props — Physical Asset Logistics

Manages all physical items distributed to teams during the hunt. Covers puzzle components, flavor items, unlock deliveries, and team kits. Produces inventory, distribution plans, and day-of checklists.

## Usage

```
/hunt props add <item>          — register a new physical prop
/hunt props inventory           — full inventory with quantities and status
/hunt props kit                 — design team starter kits
/hunt props distribute          — generate distribution plan (who gets what, when)
/hunt props labels              — generate label content for all props (feeds /hunt print props)
/hunt props checklist           — day-of event checklist
/hunt props status              — what's prepared, what's outstanding
```

---

## Prop Types

| Type | Description | Examples |
|------|-------------|---------|
| `component` | A puzzle piece teams manipulate to solve | Cipher wheel, transparency overlay, punch card, rotating disk |
| `flavor` | An item that IS the puzzle or carries a clue | Brownies with hidden flavor patterns, tagged objects to arrange |
| `unlock` | Delivered when a team solves a specific puzzle | Envelope with next clue, physical key, small gift |
| `kit_item` | Included in every team's starter kit | Pen, notepad, hunt booklet, ID badge |
| `location` | An item placed at a physical location in the venue | Sign, object at a station, hidden cache |
| `consumable` | Single-use or food item | Labeled candy, flavored items with clue significance |

---

## PROPS.md Registry

All props tracked in `delivery/props/PROPS.md`:

```markdown
# Props Registry — [Hunt Name]

| ID | Name | Type | Linked puzzle | Teams | Qty/team | Total | Distributed | Notes |
|----|------|------|---------------|-------|----------|-------|-------------|-------|
| PR01 | Cipher Wheel | component | P03 | all | 1 | 8 | at start | Print double-sided, score+fold |
| PR02 | Brownie Box | consumable | P07 | all | 1 box (6 flavors) | 8 boxes | at start | Label each brownie with flavor tag |
| PR03 | Unlock Envelope A | unlock | after P04 | all | 1 | 8 | on solve | Contains map fragment |
| PR04 | Mystery Object | component | P09 | all | 1 | 8 | at start | See P09 brief for rotation instructions |
| PR05 | Welcome Kit | kit_item | — | all | 1 | 8 | at start | Pen, notepad, hunt ID |
```

---

## /hunt props add <item>

Interactive registration. Asks:
1. What is this item? (name, brief description)
2. What type? (component / flavor / unlock / kit_item / location / consumable)
3. Which puzzle does it support? (or "none" for kit items)
4. When is it distributed? (at start / on solve of puzzle X / at location Y / other)
5. How many teams? What quantity per team?
6. Any special preparation needed? (printing, folding, labeling, baking, etc.)
7. Any special instructions for the team when they receive it?

Adds row to `delivery/props/PROPS.md`.

---

## /hunt props kit

Designs the team starter kit. Asks what every team receives at the beginning regardless of puzzle progress.

Output: `delivery/props/TEAM-KIT.md`

```markdown
# Team Starter Kit — [Hunt Name]

Every team receives at check-in:

| Item | Purpose | Qty | Notes |
|------|---------|-----|-------|
| Hunt booklet | Puzzle pages for Act I | 1 | Stapled, 20pp |
| Cipher wheel | Used in P03 | 1 | Printed double-sided |
| Team ID card | Team name + hunt info | 1 per solver | Laminated if possible |
| Pen | Solving | 1 per solver | |
| Brownie box | Used in P07 | 1 | 6 brownies, individually labeled |
| Welcome letter | Flavor / rules | 1 | In-universe voice |

Kit assembly: 30 min for N teams. Prep space needed: [table size].
```

---

## /hunt props distribute

Generates the full distribution plan: what each team gets, when, and how.

Output: `delivery/props/DISTRIBUTION-PLAN.md`

```markdown
# Distribution Plan — [Hunt Name]

## At Start (check-in table)
Every team: starter kit (see TEAM-KIT.md)
Staff needed: 1 person at check-in table

## On Solve — Triggered Deliveries
These are handed to teams when they submit the correct answer to a puzzle.

| Trigger | Item | Instructions to staff |
|---------|------|----------------------|
| P04 solved | Unlock Envelope A | Hand to team immediately. Don't open it for them. |
| P08 solved | Map fragment | Tell them: "You found something in the archive." |

Staff needed: 1 runner available throughout hunt

## Fixed-Location Items
These are pre-placed before the hunt starts.

| Item | Location | Set up by | Notes |
|------|----------|-----------|-------|
| Station 6 object | Room B, table 3 | Setup crew | Lock to table with cable tie |

## End-of-Hunt
[ ] Collect unreturned components (cipher wheels, physical objects)
[ ] Distribute any closing gifts
```

---

## /hunt props labels

Generates label content for every prop in `PROPS.md`. Output passed to `/hunt print props` for formatting.

For each prop, produces:
- **Item label**: prop name, team name (if team-specific), hunt-themed decoration
- **Instruction card**: if the prop has team-facing instructions ("Rotate this until...")
- **Staff label**: internal-facing note ("Give to team only after they solve P04")

---

## /hunt props checklist

Day-of event checklist. Reads PROPS.md and generates:

```
DAY-OF CHECKLIST — [Hunt Name]
[Date] — [Venue]

SETUP (1 hour before start)
  [ ] Print all puzzle pages (N copies × M teams) — see PRINT-CHECKLIST.md
  [ ] Assemble N team kits
  [ ] Label all brownie boxes (PR02) — 6 labels per box × 8 teams = 48 labels
  [ ] Prepare unlock envelopes (PR03) — 8 envelopes, seal, label with team names
  [ ] Place Station 6 object (PR04) — Room B, table 3, cable tie to table
  [ ] Set up check-in table

DURING HUNT
  [ ] Staff runner available for triggered deliveries
  [ ] P04 solve → Unlock Envelope A (1 per team, 8 total — in box marked "P04")
  [ ] P08 solve → Map fragment (1 per team, 8 total — in box marked "P08")

BREAKDOWN
  [ ] Collect cipher wheels (8 total)
  [ ] Collect any reusable components
  [ ] Debrief / answer reveal

EMERGENCY SPARES
  Keep 2 extra copies of every printed component. Location: [green bag at admin table].
```

---

## /hunt props status

Quick dashboard of prep state:

```
PROPS STATUS — [Hunt Name]

ID    Name                  Type         Qty    Prep status
────  ────────────────────  ───────────  ─────  ───────────
PR01  Cipher Wheel          component    8      [ ] Not prepared
PR02  Brownie Box           consumable   8      [ ] Not prepared
PR03  Unlock Envelope A     unlock       8      [ ] Not prepared
PR04  Mystery Object        component    8      [ ] Not prepared
PR05  Welcome Kit           kit_item     8      [ ] Not prepared

0/5 props ready. Event in [X days].
```

Update prep status by editing PROPS.md — add ✓ to the Notes column when prepared.

---

## Flavor Item Design

For consumable/flavor props (like brownies), Claude helps design the clue system:

```
/hunt props flavor-design <item>
```

Asks:
1. What is the item? (e.g., brownies, labeled jars, tagged candies)
2. How many variants? (e.g., 6 brownie flavors)
3. What does each variant need to communicate? (a letter, a number, a color, an order)
4. How will teams discover the pattern? (taste, label text, visual marking)

Output: a design doc for how the flavor item encodes its clue, plus label text for each variant.

Example — 6 brownies encoding a 6-letter extraction:
```
Brownie 1: "Classic Chocolate"     → extract first letter: C
Brownie 2: "Raspberry Ripple"      → extract first letter: R
Brownie 3: "Orange Zest"           → extract first letter: O
Brownie 4: "Walnut Swirl"          → extract first letter: W
Brownie 5: "Nougat Crunch"         → extract first letter: N
Brownie 6: "Espresso Dark"         → extract first letter: E
Answer: CROWNE
```
