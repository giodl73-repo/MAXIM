# Succession and Stability — Succession Models, Resilience, Regime Shifts

## The Big Picture

Ecosystems change over time in predictable ways after disturbance — this is ecological succession. But "predictable" doesn't mean deterministic toward a single endpoint. Modern understanding: succession pathways are contingent on initial conditions, stochastic events, and ongoing disturbances. The stability concepts — resilience and resistance — have become central to managing ecosystems near tipping points.

```
+---------------------------------------------------------------+
|           SUCCESSION AND STABILITY FRAMEWORK                   |
|                                                                |
|  SUCCESSION:                                                   |
|  Bare rock → Pioneer species → Early community →             |
|  Middle community → Late-successional state                   |
|  (primary succession: rock → soil → full vegetation)          |
|  (secondary succession: soil present → vegetation regrowth)   |
|                                                                |
|  STABILITY CONCEPTS:                                          |
|  Resistance: ability to withstand perturbation               |
|  Resilience: rate of recovery after perturbation             |
|  Engineering resilience vs Ecological resilience             |
|                                                                |
|  REGIME SHIFTS:                                               |
|  Threshold → alternative stable state → hysteresis           |
|  (difficult to reverse; ecosystem reorganizes)               |
+---------------------------------------------------------------+
```

---

## Primary Succession — Building Ecosystem from Nothing

```
CLASSIC SEQUENCE (Rocky substrate):

BARE ROCK
    ↓ (pioneer organisms: lichen, cyanobacteria)
    |  Lichen secretes acids, accumulates organic matter
    ↓
LICHEN/MOSS STAGE
    ↓ (thin soil forms; moisture retained)
    |  Annual plants can colonize
    ↓
ANNUAL/HERBACEOUS STAGE
    ↓ (soil deepens; nutrients accumulate)
    |  Perennial plants, grasses
    ↓
SHRUB STAGE
    ↓ (shrubs modify environment: shade, litter)
    |  Early successional trees (birch, aspen, poplar) colonize
    ↓
EARLY FOREST
    ↓ (canopy trees shade out pioneer trees)
    |  Shade-tolerant trees establish in understory
    ↓
LATE-SUCCESSIONAL FOREST (climax?)

TIMESCALE: Hundreds to thousands of years
EXAMPLE: Glacial retreat (Glacier Bay, Alaska — studied since 1800s)
         Volcanic surfaces (Krakatoa, Mt. St. Helens posteruption)
```

**Soil development drives succession** — Without soil formation (pedogenesis), succession is bottlenecked. Nitrogen-fixing pioneers (alder in post-glacial; legumes in old fields) accelerate succession by adding N to nutrient-poor substrates.

---

## Secondary Succession — Rebuilding from Disruption

When soil remains but vegetation is removed (fire, farming, logging, flood):

```
AGRICULTURAL FIELD (eastern US):
Year 0:     Bare soil (abandoned after farming)
Year 1–5:   Annual weeds → perennial grasses + forbs
Year 5–15:  Shrubs, briar, early woody species
Year 15–50: Fast-growing trees: tulip poplar, cherry, sassafras
Year 50–100: Oak, hickory (canopy)
Year 150+:  Mature mixed hardwood forest

FASTER than primary succession because:
- Soil intact (nutrients, seed bank, mycelium)
- Seed rain from adjacent vegetation
- Microbial community preserved
```

**Oldfield succession** — extensively studied. The sequence is reasonably predictable in a given region/climate, though not deterministic in species composition.

---

## Mechanisms of Succession — Three Models

Connell and Slatyer (1977) proposed three non-exclusive mechanisms:

```
FACILITATION MODEL (Clements' classical view):
  Early species modify environment, making it MORE suitable for later species
  Early species "pave the way" for later succession
  → Obligate sequence: A facilitates B, B facilitates C...
  Example: lichen weathering rock → soil for mosses
           alder fixing N₂ → nitrogen for conifers

TOLERANCE MODEL:
  Species can establish at any stage, but grow at different rates
  Later species just outlive earlier ones (competitive hierarchy)
  → No obligate facilitation; co-establishment of many species
  → Later community determined by who grows tallest/survives longest
  Example: Most temperate forest succession

INHIBITION MODEL:
  Early colonizers inhibit later succession
  Change only when early species die or are disturbed
  → Succession is NOT progressive improvement
  Example: Kelp forest (existing kelp inhibit urchin → juvenile kelp)
           Old-field grass (inhibits shrub establishment for years)
```

Modern view: All three mechanisms operate; their relative importance varies by ecosystem, disturbance type, and species traits.

---

## The Climax Concept and Its Critique

Frederic Clements (1916): All succession in a region converges to a single stable "climax community" determined by climate. The climax was viewed as the natural endpoint.

Henry Gleason (1926): The "individualistic concept" — species respond independently to environment; communities are not superorganisms. No deterministic climax.

Modern synthesis:
- **No single climax** in most regions — multiple potential stable states exist
- **Polyclimax**: Different substrates, soils, and microclimates → different stable communities even in one region
- **Disturbance regime** shapes the "climax" — fire-adapted grasslands persist where fire prevents forest; not forest-climax
- **Climate determines the envelope** of possible states; disturbance + history determine which state within that envelope

---

## Resilience and Stability

C.S. Holling (1973) distinguished two stability concepts:

```
ENGINEERING RESILIENCE:
  How fast a system returns to equilibrium after disturbance
  (speed of recovery)
  → Assumes single equilibrium; small disturbances
  → Directly maps to control theory: return time ≈ 1/Re(dominant eigenvalue)
     of the linearized system at equilibrium
  → Applicable to highly stable, simplified systems near a single fixed point

ECOLOGICAL (HOLLING) RESILIENCE:
  How large a disturbance can be absorbed before the system
  reorganizes into a different state
  → Multiple equilibria possible (nonlinear dynamics)
  → Each stable state has a basin of attraction in state space
     (set of initial conditions that converge to that equilibrium)
  → High Holling resilience = large basin of attraction
  → Low resilience = system near a basin boundary → small perturbation
     → state jumps to different attractor
  → The KEY concept for managing ecosystems near tipping points

CONTROL THEORY CONNECTION:
  Engineering resilience = stability margin of a single-equilibrium linear system
  Holling resilience = volume of basin of attraction in nonlinear state space
  A system can have high engineering resilience (fast return from small kicks)
  but low Holling resilience (a large kick crosses the basin boundary → new state)
  Real management implication: measuring return time from small disturbances
  does NOT tell you how close the system is to a regime shift threshold
```

```
STABILITY LANDSCAPE (ball-in-cup metaphor):

RESILIENT SYSTEM:      LOW RESILIENCE:        COLLAPSED:
     ball                  ball                 ●
    ( ● )                 ( ● )              ___|___
   /      \              /    |              (alt state)
__/        \__        __/     |__
                              ↑
                         near tipping point;
                         ball rolls into other cup easily
```

**Resistance vs resilience trade-off** — A highly resistant system may have lower resilience when finally perturbed (and vice versa). Old-growth forests resist most fires but take centuries to recover from catastrophic fire. Early-successional grasslands burn readily but recover in years.

---

## Regime Shifts and Hysteresis

A regime shift = transition between alternative stable states; typically triggered when a slow variable (nutrient loading, temperature, grazing pressure) crosses a threshold.

**Physics analog:** The bifurcation diagram for a regime shift (fold bifurcation) is structurally identical to a magnetic hysteresis loop or the charge/discharge curve of a system with a switching threshold. In all three cases: (1) the state depends on history, not just the current input; (2) the forward transition occurs at a different threshold than the reverse transition; (3) the system has two stable states and one unstable state in the bistable region; (4) to return to the prior state requires driving the control variable well past the original transition point. The ecological "slow variable" (nutrient loading) maps to the magnetic field H; the ecosystem state (clear/turbid) maps to magnetization M. Same fold bifurcation, same hysteresis, same mathematical structure.

```
CLASSIC EXAMPLE: Clear lake → Turbid lake (eutrophication)

FORWARD SHIFT: Adding nutrients → algal bloom → turbidity
  Passes threshold (feedback: turbidity suppresses macrophytes;
  macrophytes gone → less nutrient uptake → more turbidity)

HYSTERESIS:
  Nutrient Loading (slow variable)
        ↑
        |         ← ← ← CLEAR LAKE (upper state)
Clear   |  /‾‾‾‾‾‾‾‾‾‾‾\
lake    | /             \  FOLD/BIFURCATION POINT
        |/               \
        |    bistable      \
Turbid  |    region         \___
lake    |                   ← ← ← TURBID LAKE (lower state)
        +-----------------------------→ Nutrient loading

RECOVERY REQUIRES:
  Reducing nutrients FAR BELOW the level that caused the shift
  (hysteresis: same input → different output depending on history)
  Often requires active restoration (dredging, biomanipulation)
```

**Other ecological regime shifts:**

| System | State 1 | State 2 | Transition driver |
|--------|---------|---------|------------------|
| Lake | Clear water, macrophytes | Turbid, algae-dominated | Phosphorus loading |
| Coral reef | Coral-dominated | Algae-dominated | Temperature + nutrients + grazing pressure |
| Savanna | Grassland | Dense bush/woodland | Fire suppression + CO₂ rise |
| Semi-arid vegetation | Grassy/shrubby | Desert/bare | Overgrazing + drought |
| North Atlantic circulation | AMOC strong | AMOC weak | Freshwater influx (ice melt) |
| Kelp forest | Kelp | Urchin barren | Otter loss + sea urchin eruption |

---

## Panarchy — Adaptive Cycles

Holling's panarchy theory describes ecosystems as cycling through phases:

```
r (Growth/Exploitation):
  Rapid accumulation of resources
  Pioneer species; fast growth
  Low connectivity; low stored capital
  ↓
K (Conservation):
  Mature, stable; high biomass
  High connectivity; high stored capital
  Increasing rigidity
  ↓
Ω (Release/Collapse — Creative Destruction):
  Disturbance (fire, storm, disease) disrupts K phase
  Releases stored capital
  ↓
α (Reorganization):
  Chaotic, unpredictable; conditions set for next r phase
  Seeds and propagules from smaller/larger scales

Cycles occur at MULTIPLE SCALES simultaneously:
  Small (leaf litter, gap dynamics): fast cycles
  Medium (forest stand): medium cycles
  Large (landscape, watershed): slow cycles
  → "Revolt" and "remember" connections between scales
```

---

## Decision Cheat Sheet

| Management situation | Ecological implication |
|---------------------|----------------------|
| Forest burned; want fastest recovery | Secondary succession; preserve seed bank and soil |
| Lake becomes turbid despite nutrient reduction | Hysteresis; need to reduce nutrients well below threshold |
| Ecosystem recovering slowly from human impact | Low ecological resilience; may be near alternative state |
| Suppressing fire in fire-adapted ecosystem | Increases fuel load → eventual catastrophic fire |
| Wanting to restore old-field to forest | Let secondary succession proceed; may need 50–150 years |
| Coral reef declining despite reduced stressors | Regime shift occurred; may need active intervention |

---

## Common Confusion Points

**Succession is not always linear or progressive** — Systems can be deflected, reversed, or arrested at any stage by disturbance, human intervention, climate, or invasive species. The classic textbook sequence is an idealized average, not a rule.

**Climax ≠ best or most stable** — The climax concept implies old-growth forest is the endpoint and "best" state. But grasslands, savannas, and shrublands are maintained by disturbance regimes and are just as "natural" and ecologically valuable as late-successional forests.

**Resilience is not simply "recovers quickly"** — Engineering resilience = recovery speed. Ecological resilience = magnitude of disturbance absorbed before state change. A forest with high Holling resilience may actually recover slowly from small disturbances but absorbs large ones without reorganizing.

**Hysteresis means you can't just reverse the driver** — If a lake shifted to turbid state at nutrient level X, reducing nutrients back to X won't restore clarity. You need to go far below X because the system is now in a different basin of attraction with self-reinforcing feedbacks. This is why prevention is far easier than restoration.