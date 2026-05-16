# ASCII Perfection Spec

## Thesis

ASCII diagrams in MAXIM are not decoration. They are executable mental models:
the reader should be able to understand structure, flow, hierarchy, or decision
logic faster from the diagram than from prose.

Perfect ASCII means three things:

1. **Mechanical correctness**: monospace alignment, no broken borders, no
   dangling arrows.
2. **Semantic correctness**: the diagram's geometry matches the concept.
3. **Reader usefulness**: the diagram reduces cognitive load instead of adding
   ornamental noise.

## Diagram Classes

| Class | Use When | Mechanical Checks | Semantic Checks |
|---|---|---|---|
| **Box** | components, categories, bounded concepts | border widths align; labels fit; no uneven corners | boxes represent real conceptual boundaries |
| **Pipeline** | ordered transformations | every arrow has source/target; direction consistent | stages are causally or temporally ordered |
| **Layer cake** | stack, abstraction, dependency, substrate | layer widths deliberate; vertical order clear | lower layers support upper layers |
| **Matrix / grid** | comparisons, coordinates, state spaces | columns align; row labels stable | axes are independent and meaningful |
| **Timeline** | chronology, process phases, evolution | ticks ordered; labels do not collide | time direction and scale are clear |
| **Map / topology** | spatial relation without exact geography | labels legible; crossings intentional | distance/topology claims are not misleading |
| **State machine** | modes, transitions, protocols | every transition connects states | labels name events or guards |
| **Axis / band chart** | latitude, frequency, pressure, spectrum | axis labels ordered; bands do not overlap | intervals and thresholds are meaningful |
| **Decision tree** | choice logic | all branches terminate or continue visibly | branch predicates are mutually intelligible |
| **Mechanism cross-section** | physical/biological/engineering mechanisms | arrows and labels align to parts | diagram explains why, not only where |

## Gold Diagram Checklist

A Gold guide diagram should pass this checklist:

| Check | Pass Standard |
|---|---|
| Purpose named | Reader can say what question the diagram answers |
| Geometry meaningful | Position, nesting, arrows, or layers encode real relationships |
| Terminal-safe | Renders cleanly in plain monospace, not only in a rich preview |
| No fake precision | Spatial diagrams do not imply exact scale unless scale is provided |
| No orphan labels | Every label attaches to a visible object, layer, arrow, or band |
| No decorative frames | Borders exist to group meaning, not to make a poster |
| Prose handshake | Paragraph before or after tells the reader how to read it |
| Maintenance-safe | Future editor can change one label without redrawing the world |

## When SVG Is Better Than ASCII

Use SVG or another visual medium when:

| Need | Why ASCII Fails |
|---|---|
| real geographic coordinates | monospace cells distort aspect ratio |
| dense labels on a map | collisions become unavoidable |
| curved paths or coastlines | block approximations imply false shapes |
| proportional scale | character cells are not square |
| color/legend carries data | ASCII symbol vocabulary becomes overloaded |

Atlas precedent: SVG for geography, ASCII for mechanisms, Markdown tables for
dense reference data.

## Da Vinci Invariant Candidates

Protect canonical diagrams by requiring their key concepts to remain present.

| Candidate | File | Required Invariants |
|---|---|---|
| Package manager stack | `computing/01-PACKAGE.md` | system layer, runtime layer, language PM, libraries |
| Consensus landscape | `distributed-systems/03-CONSENSUS.md` | FLP, partial synchrony, Paxos, Raft, quorum |
| Hydrogen identity crisis | `periodic-table/01-HYDROGEN.md` | Group 1, Group 17, unique hydrogen properties |
| 12-TET pitch mapping | `music-theory/01-PITCH-SCALES.md` | frequency, pitch class, 12-TET, octave |
| Global wind cells | `atlas/02-GLOBAL-WINDS.md` | Hadley, Ferrel, Polar, ITCZ, subtropical high |

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Topic poster | lists nouns in boxes but no relation | add arrows, layers, or axes |
| Subway-map lie | implies topology that is not true | use table or prose if relation is weak |
| Border theater | heavy frames around ordinary text | remove frame or turn into table |
| Arrow soup | arrows cross without named meaning | split into smaller diagrams |
| Nested impossibility | boxes inside boxes require fragile spacing | use layer cake or bullet hierarchy |
| Side-by-side squeeze | two diagrams crammed into 80 columns | stack vertically |
| Code block as proof | code sample satisfies "has diagram" check | require conceptual diagram marker |

## Review Procedure

1. Classify the diagram.
2. Run mechanical checks for that class.
3. Ask what relationship the geometry encodes.
4. Ask whether prose explains how to read it.
5. If geography or proportional spatial data is involved, consider SVG.
6. Record findings as `diagram/P1` when broken, `diagram/P2` when decorative or
   weak, and `diagram/P3` when polish would improve an otherwise good diagram.

## Implementation Guidance For Proof

Proof should eventually support diagram-class metadata, but do not require it
globally yet. Start with pilot annotations in wave reviews:

```markdown
<!-- diagram-class: layer-cake -->
```

or panel records:

```markdown
Diagram: Big Picture
Class: pipeline
Mechanical: pass
Semantic: warn - arrow direction unclear between resolver and lockfile
```

Only promote class metadata into source files if the pilot demonstrates clear
value without visual clutter.
