# Tissue Culture and Micropropagation

## The Big Picture

Tissue culture allows any piece of plant tissue — a leaf disc, a shoot tip, an embryo — to regenerate into a complete plant under sterile laboratory conditions. This capability, called totipotency, is the biological foundation for a technology that produces hundreds of millions of plants annually.

```
THE MICROPROPAGATION PIPELINE:

  EXPLANT SELECTION
  (piece of donor plant)
        |
        v
  SURFACE STERILIZATION
  (eliminate microorganisms)
        |
        v
  Stage I: ESTABLISHMENT        Culture initiated in sterile medium
  (weeks to months)              Explant establishes; contamination eliminated
        |
        v
  Stage II: MULTIPLICATION       Shoot proliferation stimulated by cytokinin
  (continuous, months)            Each cycle: 3–10× multiplication of shoots
        |
        v
  Stage III: ROOTING             Auxin applied; roots induced
  (weeks)                         Plants become self-sufficient
        |
        v
  ACCLIMATIZATION                Transition from controlled lab to nursery
  (weeks)                         The critical bottleneck
        |
        v
  TRANSPLANT-READY PLANTLET
```

---

## Totipotency

The concept that any plant cell retains the complete genome and, in principle, can develop into a complete plant:

```
HISTORICAL DEVELOPMENT:
  1902: Gottlieb Haberlandt (Austrian botanist) hypothesized that
        isolated plant cells could be grown in culture media
        ("totipotency" — from Latin totus = all).
        His experiments failed (technical limitations).

  1950s: Folke Skoog (University of Wisconsin) developed MS medium
         and discovered cytokinins while studying tobacco cultures.
  1958: F.C. Steward demonstrated whole carrot plants regenerated
         from single cells suspended in coconut milk culture.
         First experimental confirmation of Haberlandt's hypothesis.

WHY PLANTS (BUT NOT ANIMALS):
  Animal cells differentiate and lose pluripotency (mostly).
  Plant cells retain totipotency because:
  1. Plant development is post-embryonic and modular — meristems
     produce new organs throughout life.
  2. Wounding response requires dedifferentiation (callus).
     The wound response mechanism can be hijacked in culture.
  3. Plant growth regulators (auxin, cytokinin) control the
     differentiation pathway; changing their ratio redirects fate.

  NOTE: Animal cells DO retain totipotency — demonstrated by
  Dolly the sheep (1996) somatic cell nuclear transfer.
  But in situ plant cells are more readily reprogrammed
  without nuclear transfer.
```

---

## Murashige-Skoog (MS) Medium

Toshio Murashige and Folke Skoog (1962) developed the medium that became the standard formulation for plant tissue culture:

```
MS MEDIUM COMPONENTS:
  ┌─────────────────────────────────────────────────────────────────┐
  │ MACRONUTRIENTS (mM range):                                       │
  │   NH₄NO₃ (ammonium nitrate)    1650 mg/L — nitrogen source      │
  │   KNO₃ (potassium nitrate)      1900 mg/L — nitrogen + potassium │
  │   CaCl₂·2H₂O                    440 mg/L  — calcium              │
  │   MgSO₄·7H₂O                    370 mg/L  — magnesium + sulfur   │
  │   KH₂PO₄                        170 mg/L  — phosphorus           │
  ├─────────────────────────────────────────────────────────────────┤
  │ MICRONUTRIENTS (μM range):                                       │
  │   MnSO₄, ZnSO₄, H₃BO₃, KI,                                     │
  │   Na₂MoO₄, CuSO₄, CoCl₂, FeSO₄/Na₂EDTA                        │
  │   (exact concentrations vary by species and purpose)             │
  ├─────────────────────────────────────────────────────────────────┤
  │ VITAMINS:                                                        │
  │   Myo-inositol (100 mg/L) — cell wall synthesis                 │
  │   Thiamine (B1), Pyridoxine (B6), Nicotinic acid                │
  ├─────────────────────────────────────────────────────────────────┤
  │ CARBON SOURCE:                                                   │
  │   Sucrose (30 g/L) — plants in culture are heterotrophic;       │
  │   they do photosynthesize but not enough for growth;            │
  │   external carbon required                                       │
  ├─────────────────────────────────────────────────────────────────┤
  │ GELLING AGENT (for solid media):                                │
  │   Agar (6–8 g/L) — seaweed polysaccharide; gels at 40°C        │
  │   Alternative: Gelrite (gellan gum) — clearer, more defined     │
  ├─────────────────────────────────────────────────────────────────┤
  │ PLANT GROWTH REGULATORS (variable):                             │
  │   Auxin (IAA, IBA, 2,4-D, NAA) — concentration varies          │
  │   Cytokinin (BAP, kinetin, zeatin) — concentration varies       │
  │   See Skoog-Miller ratio below                                  │
  └─────────────────────────────────────────────────────────────────┘
  Final pH: 5.7–5.8 (before autoclaving; drops slightly after)
  Autoclave: 121°C, 15 PSI, 15–20 minutes → sterilized
```

---

## Plant Growth Regulators in Culture

### The Skoog-Miller Ratio

Skoog and Miller (1957) discovered that the ratio of auxin to cytokinin determines the developmental fate of plant tissue:

```
SKOOG-MILLER PRINCIPLE:

  HIGH CYTOKININ : LOW AUXIN → Shoot proliferation
    Culture conditions for Stage II multiplication
    Many shoot buds form; shoots elongate

  HIGH AUXIN : LOW CYTOKININ → Root formation
    Culture conditions for Stage III rooting
    Roots form at base of shoots

  BALANCED AUXIN : CYTOKININ → Callus formation (undifferentiated)
    Used when callus is the intermediate (somatic embryogenesis)

  LOW BOTH → Shoot elongation (minimal callus, minimal branching)
    Sometimes used for Stage I establishment

AUXIN TYPES (ordered by activity/stability):
  IAA (indole-3-acetic acid): natural; unstable in light and heat
  IBA (indole-3-butyric acid): stable; widely used
  NAA (naphthaleneacetic acid): synthetic; strong; not natural
  2,4-D (2,4-dichlorophenoxyacetic acid): strong; induces callus;
    used in somatic embryogenesis, not shoot culture

CYTOKININ TYPES:
  BAP/6-BAP (benzylaminopurine): most widely used; cheap; effective
  Kinetin: weaker than BAP; used for sensitive species
  Zeatin: natural cytokinin; most physiologically natural; expensive
  TDZ (thidiazuron): synthetic; extremely potent; used for woody plants
```

---

## The Three Stages

### Stage I: Establishment

```
STAGE I GOALS:
  1. Establish viable, contamination-free culture.
  2. Confirm the explant is growing (not dying).
  3. For virus-free programs: confirm pathogen freedom.

EXPLANT CHOICE:
  Shoot tips / meristems: lowest contamination; fastest establishment;
    best for virus elimination (meristems are ahead of vascular tissue
    where viruses travel — tips may be virus-free even if parent is infected).
  Axillary buds: reliable establishment; good for ornamentals.
  Leaf discs: common for tobacco, potato, Arabidopsis; variable for others.
  Embryos (zygotic): reliable; used for difficult-to-germinate seeds.

SURFACE STERILIZATION:
  Purpose: eliminate epiphytic fungi, bacteria on plant surface.
  Method:
    1. Wash in water with few drops detergent.
    2. Immerse in 70% ethanol, 30–60 seconds.
    3. Immerse in sodium hypochlorite (10–30% commercial bleach = 0.5–1.5% NaOCl)
       + few drops Tween-20 surfactant, 10–20 minutes.
    4. Rinse 3× in sterile distilled water.
    5. Transfer to medium under laminar flow hood.
  Balance: kill surface microbes without killing plant cells.
    Too long = plant damage. Too short = contamination.
    Each species requires optimization.

LAMINAR FLOW HOOD:
  Provides sterile working environment.
  HEPA filter (0.3μm) captures bacteria and spores.
  Air flows away from operator (horizontal) or down (vertical).
  Not a chemical fume hood — provides no protection from chemicals.
  All manipulations done inside the hood.
```

### Stage II: Multiplication

```
STAGE II GOALS:
  Maximize shoot number while maintaining genetic fidelity.
  Typical multiplication rate: 3–10× per subculture cycle.
  Typical cycle length: 3–6 weeks.

ORGANOGENESIS:
  Axillary shoots are stimulated by high cytokinin.
  Each axillary bud in the leaf axils activates.
  Result: dense cluster of small shoots ("bunched" appearance).
  Each shoot is a potential new plant.
  Subculture: subdivide the cluster; each section transferred
  to fresh medium → begins next multiplication cycle.

GENETIC FIDELITY:
  Organogenesis from axillary buds = high fidelity.
  Each axillary bud represents a single mitotic lineage.
  Very low somaclonal variation (spontaneous mutations in culture).

  SOMATIC EMBRYOGENESIS:
  Callus route: higher multiplication potential but
  HIGHER SOMACLONAL VARIATION.
  Cells in callus are genetically unstable; chromosome abnormalities accumulate.
  Not suitable for variety propagation.
  Suitable for: transformation studies, breeding applications.

COMMERCIAL SCALE:
  Automated liquid culture systems: bioreactors with temporary
  immersion (RITA, TIS systems) — shoots immersed in medium for
  brief periods, then drained. Higher growth rate than agar.
  Used for: banana, sugarcane, potato, strawberry at large scale.
```

### Stage III: Rooting

```
STAGE III GOALS:
  Produce roots on individual shoots.
  Roots must be functional (able to absorb water and nutrients).

METHOD 1 (IN VITRO ROOTING):
  Transfer individual shoot to medium with:
    High auxin (IBA or NAA): 0.5–5 mg/L
    Low or zero cytokinin
    Half-strength MS (lower salt stimulates rooting)
  Roots form in 2–4 weeks.
  Transfer to acclimatization.

METHOD 2 (EX VITRO ROOTING):
  Treat shoot base with IBA solution or gel.
  Stick directly into rooting medium (perlite, or propagation mix).
  Place in mist bench or high-humidity tent.
  Roots form in normal propagation environment.
  Often faster and cheaper than in vitro rooting.
  Used for: many ornamentals, strawberry, some fruit rootstocks.
```

---

## Acclimatization

The most critical bottleneck in micropropagation. In vitro plants have:

```
IN VITRO PLANT LIMITATIONS:
  1. STOMATA DYSFUNCTION:
     Stomata fail to close normally. Reason: no ABA signaling in
     humid culture; stomata remain constitutively open.
     Result in low humidity: immediate wilting from uncontrolled
     water loss.

  2. THIN CUTICLE:
     Waxy cuticle not formed properly (no wind, vapor-saturated
     atmosphere in culture). Water loss directly through leaf surface
     is 5–20× higher than a hardened plant.

  3. PHOTOAUTOTROPHIC INCOMPETENCE:
     Plants in culture are partially or fully heterotrophic (fed sucrose).
     Photosynthetic enzymes may be at low levels.
     Transition to full photoautotrophy requires time.

  4. EPIDERMIS STRUCTURE:
     Cell arrangement and wall composition adapted to in vitro conditions;
     not optimal for open air.

ACCLIMATIZATION PROTOCOL:
  Week 1: High humidity (95%+) in closed plastic tent.
           Keep in low light initially.
  Week 2: Begin opening tent slightly; reduce humidity to ~85%.
  Week 3: Progressively reduce humidity to ~70%.
  Week 4–6: Move to normal nursery conditions.
  Mist frequency reduced as plants harden.

  MORTALITY: 10–40% acclimatization losses are normal.
  Elite commercial operations with optimized protocols: <10%.
  Poor protocols: 50–70% losses — entirely wasted Stage I–III work.
```

---

## Applications

### Orchid Production

```
ORCHID MERISTEM CULTURE:
  Cymbidium orchids: commercial production transformed by Morel (1960)
  demonstrating that shoot tip meristem culture produced
  "protocorm-like bodies" (PLBs) — multiply vegetatively in liquid culture.
  Each PLB can be subdivided → exponential multiplication.
  A single meristem can produce millions of plants.

  VIRUS ELIMINATION:
  Orchids carry systemic viruses (ORSV, CymMV) that reduce vigor and
  cause flower breaks (color streaking — historically desirable in tulips,
  now usually undesirable in orchids).
  Meristem tips are virus-free because viruses travel through
  vascular tissue but meristems are vascular tissue-free.
  Meristem culture → virus-tested → virus-free clones.
  These are registered as "meristem lines" and are the basis for
  all commercial orchid production.
```

### Potato Virus-Free Stock

```
THE POTATO SEED SYSTEM:
  Certified seed potatoes must be virus-free (or low virus).
  Viruses (PVY, PLRV, PVX) reduce yield 20–80%.

  PIPELINE:
  1. Tissue culture: meristem tip culture → virus-free plantlets.
  2. Virus testing: ELISA or PCR on all regenerated plants.
  3. Virus-free mother plants maintained in insect-proof greenhouse.
  4. Minitubers produced: small potato tubers from tissue culture
     plantlets grown in greenhouse (1 season).
  5. Foundation seed: grow out minitubers under strict isolation
     (certified field, aphid management).
  6. Certified seed: 1–2 generations from foundation seed.
  7. Commercial crop.

  The tissue culture "clean" base propagates through 2–3 generations
  before virus recontamination pressure requires returning to TC base.
```

### Transformation via Agrobacterium

```
AGROBACTERIUM TUMEFACIENS:
  Soil bacterium that causes crown gall disease.
  Mechanism: Ti (tumor-inducing) plasmid carries T-DNA.
  During infection: T-DNA inserts into plant nuclear genome.
  The bacterium evolved this to make the plant produce compounds
  (opines) that only the bacterium can metabolize.

GENETIC TRANSFORMATION EXPLOITATION:
  Replace T-DNA oncogenes with gene of interest (GOI).
  GOI inserts into plant genome stably.
  Selection marker (antibiotic resistance) identifies
  transformed cells.

  PROTOCOL:
  1. Leaf discs infected with engineered Agrobacterium.
  2. Infected tissue on medium with:
     Selection antibiotic (kills non-transformed cells)
     Cytokinin (induces shoot regeneration)
  3. Only transformed cells survive → regenerate shoots.
  4. Root shoots → acclimatize → verify transgene expression.

  CROPS WITH AGROBACTERIUM TRANSFORMATION:
  Tobacco (first, 1983), tomato, soybean, cotton, potato, rice,
  most major crops. Not all crops are susceptible to Agrobacterium —
  monocots (grasses) required biolistics (gene gun) instead.
```

---

## Contamination Control

```
CONTAMINATION SOURCES:
  Surface contamination: eliminated by sterilization (above).
  Internal contamination: bacteria/fungi inside plant tissue.
    Not accessible to surface sterilization.
    Source: infected donor plants.
    Solution: start with visually healthy plants; use meristem tips
    (less internal infection than leaf discs).

BACTERIA IN CULTURE:
  Slowly growing bacteria may not cause turbidity or colony
  growth on agar initially. They reveal themselves later.
  "Escaped contamination": looks clean initially, fails later.
  Testing: inoculate a portion of medium + transfer onto
  bacterial growth medium (R2A agar) — detects slow growers.

ANTIBIOTICS IN MEDIUM:
  Cefotaxime, ampicillin, timentin: used to eliminate residual
  Agrobacterium after transformation, or to reduce bacterial
  contamination in difficult explants.
  Use sparingly: antibiotics affect plant growth; induce stress;
  mask rather than eliminate contamination.

LAMINAR FLOW HOOD MAINTENANCE:
  HEPA filter checked annually; replaced as needed.
  UV light run between sessions (not a guarantee; supplement with technique).
  70% ethanol wiped before each session.
  Flame sterilize tools in alcohol burner; cool before touching tissue.
```

---

## Decision Cheat Sheet

| Use tissue culture when... | Approach | Critical watch point |
|---------------------------|----------|---------------------|
| You need thousands of genetically identical plants fast | Stage II rapid multiplication: high cytokinin, 4-week subculture cycles | Use axillary bud proliferation, not callus — callus accumulates somaclonal variation |
| You need certified virus-free stock | Stage I: meristem tip culture (0.1–0.5mm tip only) | PCR/ELISA test each line before bulk Stage II — meristem culture reduces but doesn't guarantee virus elimination |
| You want to insert foreign genes or select mutants | Stage II: Agrobacterium co-cultivation + antibiotic selection or biolistics | Transformation efficiency and regeneration rate trade off — high-efficiency lines often regenerate poorly |
| Plants will not root in vitro or in vitro rooting is slow | Stage III: transfer to ex vitro with IBA drench + humidity tent | Ex vitro rooting is often faster and cheaper than in vitro for many woody species |
| Transitioning plants from lab to greenhouse | Acclimatization phase: progressive humidity reduction over 4–6 weeks | Stomata must learn to close; cuticle must thicken — rushing kills plants that survived all in vitro stages |

---

## Common Confusion Points

**Tissue culture is not cloning in the sci-fi sense**: plant tissue culture produces clones of the donor plant — genetically identical. But it's not the "resurrection" of extinct organisms or the production of identical plants with identical phenotypes (environment affects phenotype). It's standard horticulture technology, routine and commercial.

**MS medium must be autoclaved but growth regulators are usually filter-sterilized**: the hormones (auxin, cytokinin) degrade at autoclave temperature. They are made as stock solutions, filter-sterilized through 0.22μm membranes, and added aseptically to medium cooled to ~45°C before pouring. This is a common protocol error — autoclaving the complete medium with hormones destroys the hormones.

**Somaclonal variation is real and proportional to callus time**: the longer plant tissue spends as undifferentiated callus, the more chromosomal rearrangements accumulate. Propagation via axillary buds (no callus phase) has very low somaclonal variation. Propagation via callus has high variation. This is why orchid production via PLBs (which are structurally similar to meristems) is preferred over callus-based systems for variety fidelity.

**Acclimatization failure is not a Stage I–III problem**: many tissue culture programs produce beautiful plants in vitro and then lose them in the first week outside. Acclimatization is not a "handoff" — it requires as much attention as the in vitro phases. Stomata need to learn to close; cuticle needs time to thicken. Rushing this transition is the most common commercial error.

**In vitro = sandbox; acclimatization = hardening deployment**: plants grown in vitro are running in a fully controlled environment — sterile medium, constant humidity at saturation, stable temperature, no pathogens, no wind, no UV stress. Their stomata are non-functional (permanently open — no need to close in saturated air), cuticle is thin (no cuticular wax synthesis needed), and they are partially heterotrophic (sucrose in the medium bypasses photosynthetic demand). Moving them directly to ambient conditions is equivalent to deploying a sandbox service directly to production with no hardening — the environment assumptions are violated all at once. Acclimatization is the deployment pipeline: progressively increase vapor pressure deficit over 4–6 weeks, allowing stomata to recover function and cuticle to thicken before full exposure.

**In vitro plants are not ready to survive outside**: they look like plants but behave differently. Their stomata are dysfunctional, cuticle is thin, and they are adapted to heterotrophic carbon nutrition. Treat them as neonates requiring intensive support, not as mature plants that have been shrunk.
