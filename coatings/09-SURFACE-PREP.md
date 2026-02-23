# 09 — Surface Preparation

## The Most Critical Step — Cleaning, Profiling, Why 80% of Failures Are Prep Failures

---

## The Prime Directive

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   "The coating is only as good as the surface it's applied to."            │
│                                                                             │
│   Industry data: ~80% of premature coating failures trace to surface        │
│   preparation failures — not coating failures.                              │
│                                                                             │
│   The expensive mistake: you can't see prep failure until the coating       │
│   fails, by which point the substrate damage has compounded.                │
│                                                                             │
│   Cost hierarchy:                                                           │
│   Proper prep (day 0) << Recoat (6 months) << Remediation (2 years)        │
│                        10×                   100×                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Failure Mode Map

Before discussing prep methods, understand what you're preventing:

```
  FAILURE MODE         ROOT CAUSE               PREP FAILURE
  ────────────────     ─────────────────────    ────────────────────────
  Peeling              Adhesion loss             Contamination, wrong primer,
                       at substrate              glossy surface, moisture

  Blistering           Moisture under film       Wet substrate, humidity
                                                 during application

  Alligatoring         Incompatible layers       Hard topcoat over soft
  (reptile-skin                                  undercoat (common: oil paint
  cracking)                                      over fresh latex, or new over
                                                 un-cured)

  Fisheyes             Silicone contamination    One drop of silicone in a
  (circular craters)   on substrate              gallon of product; or off a
                                                 contaminated tool; or airborne

  Flash rusting        Moisture on bare          Water on blasted steel before
                       steel before primer       primer (even condensation)

  Sagging              Film too thick or         Temperature/humidity wrong,
                       cold substrate            film built too heavy

  Tannin bleed         Inadequate sealing        Wrong primer for tannin-rich
                                                 wood

  Checking/            Brittle topcoat           Too many coats, wrong product
  checking             over flexible base        sequence, or film too thick
```

---

## 1. Contamination Removal

The first step. Coatings bond to the substrate — not to the contamination on the
substrate. No prep step matters until the surface is clean.

### Common Contaminants and Removal

```
  OIL AND GREASE
  ├── Source: machining, hands, cooking, lubricants
  ├── Detection: water beading test (water sheets off clean metal, beads on oily)
  ├── Removal: solvent wipe (SSPC SP1)
  │     Solvents: acetone (fast evap), MEK, naphtha, isopropyl alcohol
  │     Method: two-rag technique — first rag applies solvent and mobilizes oil,
  │             second clean rag wipes before solvent re-deposits
  │     Never wipe with single rag in circles — redistributes contamination
  └── Then: mechanical prep follows, never precedes chemical cleaning

  SILICONE CONTAMINATION
  ├── Source: spray lubricants (WD-40 has no silicone, but Teflon-based sprays do),
  │           silicone polishes, cured sealant adjacent to paint area, hand lotion
  ├── Detection: fisheye test — apply thin coat of finish; craters = silicone
  ├── Visual indicator: fisheyes appear as perfectly circular depressions
  │                     (silicone repels coating in circular radius from point source)
  ├── Removal: very difficult once in substrate wood grain
  │     - Wipe down with fisheye eliminator additive (silicone flow agent) in coating
  │     - Or: thorough cleaning with silicone remover, then seal with shellac primer
  │     - In automotive finishing: sand back, wipe with wax-and-grease remover,
  │       full wipedown before each coat
  └── Prevention: never use spray silicone lubricants in a spray painting environment

  MOLD AND MILDEW
  ├── Source: high humidity surfaces (exterior siding, bathroom, basement)
  ├── Detection: bleach test — apply 10% bleach; if discoloration disappears = mold
  │             If resistant = dirt (mold dies with bleach)
  ├── Removal: bleach solution (1 part bleach : 3 parts water), dwell time 15min,
  │           scrub, rinse thoroughly, neutralize with clean water
  └── Critical: must kill mold before painting — paint over mold = mold grows
                through paint within months

  EFFLORESCENCE (masonry)
  ├── Source: water carries soluble salts to surface, deposits as crystals when water
  │           evaporates; calcium carbonate, calcium sulfate, sodium/potassium salts
  ├── Detection: white crystalline deposits on brick, CMU, concrete
  ├── Removal: dry wire brush (mechanical), then dilute acid wash (10% muriatic)
  │           if stubborn; rinse thoroughly; allow to dry fully
  └── Root cause: must address water infiltration or efflorescence returns
```

### TSP (Trisodium Phosphate) for General Cleaning

Alkaline cleaner — cuts grease, removes chalky paint residue, cleans surfaces before
painting. Available as powder (mix with water) or substitute formulas.

- Interior walls before repainting: TSP or equivalent wipe-down removes years of
  accumulated dust, grease, hand oils, cooking residue
- After water damage: TSP wash before any coating
- Wood prior to staining: removes mill glaze from factory lumber
- Caution: PPE (gloves, eye protection) — alkaline, irritant; rinse thoroughly

---

## 2. Mechanical Surface Preparation for Metal

The SSPC (Society for Protective Coatings) and NACE (now AMPP) standards define
preparation quality for metal substrates. These are the language of industrial
coating specs — you'll see "SSPC SP10" in coating specifications.

```
  ┌────────────────────────────────────────────────────────────────────────┐
  │ SSPC STANDARDS — Metal Surface Preparation (ascending quality)        │
  ├──────────┬────────────────────────────────┬───────────────────────────┤
  │ Standard │ Name                           │ Description               │
  ├──────────┼────────────────────────────────┼───────────────────────────┤
  │ SP1      │ Solvent Cleaning               │ Remove oil/grease; not    │
  │          │                                │ a surface prep standard   │
  │          │                                │ per se, always the first  │
  │          │                                │ step before any other     │
  ├──────────┼────────────────────────────────┼───────────────────────────┤
  │ SP2      │ Hand Tool Cleaning             │ Wire brush, scraper,      │
  │          │                                │ chipping hammer           │
  │          │                                │ Removes loose rust/scale  │
  │          │                                │ Lowest acceptable         │
  │          │                                │ Tight rust may remain     │
  ├──────────┼────────────────────────────────┼───────────────────────────┤
  │ SP3      │ Power Tool Cleaning            │ Angle grinder, needle gun,│
  │          │                                │ cup brush (power)         │
  │          │                                │ Better than SP2, same     │
  │          │                                │ limitation: tight scale   │
  ├──────────┼────────────────────────────────┼───────────────────────────┤
  │ SP6/     │ Commercial Blast Cleaning      │ Blast cleans 66%+ of      │
  │ NACE 3   │                                │ each unit area            │
  │          │                                │ Minimum for most          │
  │          │                                │ industrial primer specs   │
  ├──────────┼────────────────────────────────┼───────────────────────────┤
  │ SP10/    │ Near-White Metal Blast         │ 95%+ of each unit area    │
  │ NACE 2   │                                │ free of all contamination │
  │          │                                │ Required for aggressive   │
  │          │                                │ environments, immersion   │
  ├──────────┼────────────────────────────────┼───────────────────────────┤
  │ SP5/     │ White Metal Blast              │ 100% bare metal           │
  │ NACE 1   │                                │ No contamination visible  │
  │          │                                │ Immersion service,        │
  │          │                                │ critical structures       │
  └──────────┴────────────────────────────────┴───────────────────────────┘

  Also used:
  SP11 — Power Tool Clean to Bare Metal (angle grinder with right discs)
  SP15 — Commercial Grade Power Tool (meets SP6 equivalent with power tools)
  WPC — Wet Abrasive Blast (with water; reduces dust/flash rust risk)
```

### Surface Profile (Anchor Pattern)

Blasted metal is not smooth — it has microscopic peaks and valleys. This roughness
is the mechanical anchor for the primer.

```
  BEFORE BLAST:           AFTER BLAST:

  ─────────────────        ∧ ∧ ∧ ∧ ∧ ∧ ∧
                          ╱╲╱╲╱╲╱╲╱╲╱╲╱╲
                           microscopic peaks/valleys

  Primer must:
  1. Fill the valleys (wet-out)
  2. Build enough film to cover the peaks
  3. Have enough dry film thickness above peaks for protection

  Peak-to-valley height = "surface profile" or "anchor pattern"
  Measured in mils (thousandths of inch): 1.5-4 mil typical for commercial blast

  If profile too low: primer adhesion poor — like trying to park on glass
  If profile too high: peaks read through the coating, require more film build,
                       and can appear as "rogue peaks" = early corrosion starting points
```

**Measurement:** Testex Press-O-Film tape (Coarse or X-Coarse) pressed onto blast
profile, measured with micrometer. The tape conforms to the profile; tape thickness
− base tape thickness = peak-to-valley height.

**Abrasive selection:**
```
  Steel grit:   angular, cuts aggressively, high profile
  Steel shot:   round, peens surface, lower profile, good for thin metal
  Coal slag:    cheap, one-pass, lower reuse capability
  Garnet:       hard, lower metallic contamination risk (food/pharma)
  Aluminum oxide: very hard, high profile, suitable for hard metals
```

---

## 3. Wood Surface Preparation

```
  BARE WOOD PREP SEQUENCE:

  1. Mill glaze removal (if factory/S4S lumber):
     │  Factory-surfaced lumber has burnished surface — planer blades
     │  compress and seal wood fibers, reducing penetration
     └─ Light sand with 80-100 grit, or TSP wash

  2. Sanding sequence (for a smooth finish):
     80 grit (remove old finish, major stock removal)
      → 120 grit (remove 80-grit scratches)
       → 150 grit (remove 120-grit scratches)
        → 180 grit (ready for stain/oil finish)
         → 220 grit (fine furniture, ready for clear topcoat)

     Rule: never skip more than one grit step — each grit only removes
     scratches from the previous grit, not from two grits back

  3. Grain raising (water-based products only):
     Water-based primers and finishes raise the grain — wet wood
     fibers swell, creating a rough "fuzzy" surface.

     Prevention:
     └─ Wipe with damp sponge, let dry, resand with final grit
        before applying water-based product → pre-raises grain
        → subsequent water-based product doesn't raise it again

  4. Tack cloth:
     Fine cheesecloth with sticky residue — removes sanding dust
     without contaminating surface
     Caution: don't use before water-based products (waxy residue may
     interfere) — use slightly damp rag instead

  5. Knot treatment:
     Pine knots and sap pockets: shellac-based sealer (2 coats BIN)
     Oozing resin knots: use shellac, allow to cure, sand, then proceed
     Even after sealing: check after first topcoat coat for resin bleed

  6. Between coats (recoat adhesion):
     Scuff sand with 320 grit or fine scotch-brite pad
     Creates mechanical key for subsequent coat
     Remove dust before recoating
     Wipe with tack cloth or dry cloth
```

### Deglossing Existing Finishes

Before painting over existing glossy surfaces:
- **Mechanical:** 120-150 grit sand entire surface — creates profile
- **Chemical deglosser (liquid sandpaper):** Wash-on chemical that dulls gloss
  without sanding; less labor but less reliable than mechanical
- For glossy old oil-based trim: mechanical degloss is required, or use bonding primer

---

## 4. Masonry Preparation

```
  NEW CONCRETE:
  ┌───────────────────────────────────────────────────────────────────┐
  │ 28-day cure minimum before applying non-breathable coatings       │
  │ (concrete gains ~90% strength by 28 days, continues to gain)     │
  │                                                                   │
  │ Moisture test: tape 18"×18" plastic sheet, seal edges, 24h       │
  │ If condensation on back of plastic → too wet for coating         │
  │                                                                   │
  │ pH test: pH strips on wetted surface; pH>9 → alkali-resistant    │
  │          primer required; pH<9 → standard masonry primer OK      │
  └───────────────────────────────────────────────────────────────────┘

  GARAGE FLOOR EPOXY PREP (critical sequence — skip any step = failure):
  1. Degrease with concrete cleaner/degreaser (dish soap is inadequate)
  2. Acid etch: 10% muriatic acid (HCl) solution, brush on, watch fizz
     - Fizzing = acid reacting with carbonates in concrete = surface opening
     - No fizzing = either too clean or surface has sealer (must remove sealer first)
  3. Rinse thoroughly (multiple passes)
  4. Neutralize: baking soda solution rinse
  5. pH test: should be 6-8 before epoxy
  6. Moisture test (24h plastic sheet) — see above
  7. Profile check: should feel like 120-grit sandpaper
  8. Apply epoxy within specified window (within hours of prep)

  EXISTING MASONRY WITH PAINT:
  - Peeling/flaking: remove all loose material (scraper, wire brush)
  - Stable painted masonry: check adhesion (cross-hatch test, tape),
    prime and paint over if intact
  - Efflorescence: remove as described above; address water source
```

---

## 5. Temperature and Humidity Conditions

Most coating failures from environmental conditions are completely avoidable.
Check the product TDS for specific limits — these are minimums:

```
  UNIVERSAL RULES:

  ┌─────────────────────────────────────────────────────────────────────┐
  │ Substrate temperature:   ≥ 40-50°F (some products require ≥ 50°F) │
  │ Air temperature:         ≥ 50°F                                    │
  │ Relative humidity:       ≤ 85%                                     │
  │ Substrate temperature:   ≥ 5°F above dew point                    │
  └─────────────────────────────────────────────────────────────────────┘

  DEW POINT RULE EXPLAINED:
  If air temp = 60°F at 70% RH → dew point ≈ 49°F
  If substrate = 51°F → substrate is only 2°F above dew point (not safe)
  If substrate = 45°F → substrate is BELOW dew point = condensation forming
                         = invisible moisture layer = coating failure

  WHY METAL IS ESPECIALLY CRITICAL:
  - Metal substrates thermally equalize to ambient temperature quickly
  - In morning, air warms faster than metal mass
  - Metal surface can be at dew point even when air feels dry
  - Rule: apply 2-3 hours after sunrise minimum; stop 2 hours before sunset

  HOT WEATHER PROBLEMS:
  - Very hot substrate (direct sun on metal > 130°F) causes solvent to
    flash before film can flow out properly
  - Bubbles, blistering, poor film formation
  - Solutions: apply in shade, early morning, use "hot weather" thinner,
               reduce coat thickness

  COLD WEATHER PROBLEMS:
  - Latex paint: below 50°F, coalescence fails (polymer particles don't fuse)
  - Film forms but is brittle, poor adhesion, poor water resistance
  - Oil/alkyd: slow cure, tackiness issues, may never fully harden
  - Solutions: heat the space (not the surface with a torch), use
               low-temp formulations, wait for temperature
```

---

## 6. Intercoat Adhesion

The interface between existing coat and new coat is a potential failure plane.

```
  RECOAT WINDOW — from product TDS:

  Too soon (wet):
  - Solvent from new coat re-lifts previous coat
  - Wrinkling, lifting, intercoat contamination
  - For lacquers: extremely tight window (re-dissolves)

  Too late (hard/glossy):
  - Previous coat has hardened and oxidized surface
  - New coat has nothing to mechanically key to
  - Adhesion failure along intercoat plane

  Correct window: per TDS (varies widely — 2h to 24h to "indefinitely with
  scuff sanding")

  SCUFF SANDING between coats:
  ├── Required when: hard clear coats (polyurethane, conversion varnish),
  │                  waiting longer than recoat window, glossy intermediate
  ├── Grit: 320-400 for fine finishes; 150-220 for build coats
  ├── Goal: visible haze (no bare spots, no through-sanding)
  └── After sanding: remove all dust before recoating
```

---

## 7. Intercoat Compatibility

Not all products work over all other products. The general compatibility matrix:

```
  OVER EXISTING COATING:          CAN APPLY:

  Fully cured latex paint         Latex ✓, oil ✓, alkyd ✓

  Fully cured oil/alkyd paint     Latex ✓ (if scuffed), oil ✓, alkyd ✓
  Glossy oil paint (unscuffed)    Nothing directly — will peel

  Shellac (dewaxed)               Latex ✓, oil ✓, lacquer ✓ = universal bridge

  Lacquer (nitrocellulose)        Lacquer ✓, shellac ✓ (as intermediate)
                                   NEVER: polyurethane directly

  Conversion varnish (catalyzed)  Same chemistry or nothing (check TDS)
                                   Do NOT apply new coats after 72h without scuff

  Unknown existing finish         Shellac first → universal platform above

  SOFT OVER HARD RULE:
  Hard, brittle topcoat over flexible, soft undercoat = alligatoring
  The hard coat doesn't flex when the soft coat moves beneath it → cracking

  Example failure: alkyd enamel (hard) over fresh latex (soft/flexible)
  Common failure: multiple thick coats of polyurethane without sanding between
                  = exterior coat in tension as interior flexes
```

---

## 8. Failure Analysis

Systematic approach when a coating fails:

```
  SYMPTOM              DIAGNOSTIC QUESTIONS               LIKELY CAUSE
  ──────────────────   ──────────────────────────────     ────────────────────
  Peeling at           Is paint pulling the primer?        Inadequate primer
  substrate            Is primer pulling the substrate?    Contamination or
  (full peel)          Was there moisture?                 moisture at bond time

  Peeling              Did intercoat adhesion fail?        Recoated too late,
  between coats        Was surface glossy?                 no scuffing, soft-
                       Were products compatible?           over-hard sequence

  Blistering           Are blisters water-filled?          Moisture under film
  (bubbles)            Are blisters solvent-filled?        Applied too thick or
                                                           too fast (solvent trap)

  Alligatoring         How many layers?                    Too many coats, hard
  (reptile cracks)     What was sequence?                  topcoat over soft base

  Fisheyes             Any silicone used nearby?           Silicone contamination
  (craters)            Any spray lubricants?

  Tannin bleed         Wood species? (cedar/pine/redwood)  Wrong primer for
  (brown stains)       Was primer shellac-based?           tannin substrate

  Flash rust           Steel substrate? Time to prime?     Moisture on blasted
  (orange on new       Humidity during application?        steel before priming
   metal primer)
```

---

## Decision Cheat Sheet

| Surface / Situation | Prep Required |
|--------------------|---------------|
| New drywall, interior | TSP wash, fill holes, PVA primer |
| Previously painted wall, clean | Wash with TSP solution |
| Previously painted wall, stained | TSP wash + stain identification + correct primer |
| Bare wood, smooth (furniture) | 80-120-150-180-220 sanding progression |
| Bare wood, exterior | Sand to 120, remove resin/mill glaze, oil primer |
| Knotty pine | Shellac BIN over knots, 2 coats |
| Bare steel, shop/industrial | SP1 solvent clean → SP6 blast (minimum) |
| Steel in aggressive environment | SP1 → SP10 blast → zinc-rich primer |
| Galvanized steel | Acid etch primer or SSPC SP16 (sweep blast) |
| Aluminum | Scotch-brite + solvent wipe, or etch primer |
| Concrete floor (epoxy) | Degreaser → acid etch → rinse → neutralize → moisture test |
| New concrete (any coating) | 28-day cure, pH test, moisture test |
| Old glossy paint | Degloss sand (120-150) or bonding primer |
| Tile/slick surface | Bonding primer + scuff sand |
| Smoke-damaged drywall | TSP wash → 2 coats shellac BIN |

---

## Common Confusion Points

**"Pressure washing = adequate prep for painting"**
Pressure washing removes loose debris and biological growth. It does not replace
mechanical prep for failing surfaces, does not remove oil/grease, and (most critically)
leaves the surface wet. Pressure washing followed by immediate painting is a recipe
for failure. Allow adequate drying time (24-48 hours minimum for wood; longer for
masonry).

**"More prep = more surface roughness = better adhesion"**
Up to a point. Surface profile that exceeds the primer's ability to fill the valleys
leaves exposed peaks — these become early corrosion initiation sites. The spec for
industrial coatings specifies a profile range (e.g., 1.5-3.0 mils) not just a minimum.
For wood: over-sanding can burnish the surface — high grits on softwood compress fibers,
reducing penetration of stain/oil finishes.

**"I wiped it down — it's clean"**
Depends entirely on what you wiped it with. A dry cloth redistributes contamination.
A solvent-saturated cloth picks up and holds. The two-rag solvent cleaning technique
(SSPC SP1 methodology) exists because single-rag wiping just moves oil around.

**"The paint can says 'no primer needed'"**
Some paints marketed as "paint + primer in one" do legitimately have improved adhesion.
They're adequate for going over clean, previously painted surfaces in good condition.
They are not adequate for bare wood, bare metal, stained surfaces, or surfaces with
any prep issue. "Self-priming paint" is a marketing shortcut, not an engineering substitute.

**"It looked fine after priming — must be good"**
You cannot visually detect: silicone contamination below the primer, moisture trapped
under the primer, inadequate surface profile, wrong primer for substrate chemistry.
These become apparent when the topcoat goes on, or months later when failure begins.
