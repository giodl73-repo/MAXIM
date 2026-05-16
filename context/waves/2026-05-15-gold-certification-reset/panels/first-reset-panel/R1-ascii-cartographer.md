# R1 - ascii-cartographer

## Findings

### F-04 - WARN: Plate tectonics figure is a category panel, not a system diagram
File: `geology/05-PLATE-TECTONICS.md`
Finding: The `GLOBAL PLATE SYSTEM` diagram is terminal-readable and valid, but
it functions mainly as a category table. It does not show the cycle of crust
creation, transport, subduction, collision, plume exceptions, and observational
evidence.
Consequence: The diagram protects a real anchor, but the anchor is not yet the
best visual explanation of the field.
Fix: Promote the diagram from "boundary taxonomy" to "global plate engine" with
arrows for creation, motion, destruction, recycling, and intraplate exceptions.

### F-05 - NOTE: Effective Stress opening figure earns the invariant
File: `geotechnical-engineering/02-EFFECTIVE-STRESS.md`
Finding: The master-concept box directly encodes total stress, pore pressure,
effective stress, and the groundwater-settlement consequence. It performs real
conceptual work and is a good Da Vinci candidate.
Consequence: No diagram blocker; the Gold blocker is the downstream decision
surface, not the protected figure.
Fix: Keep the opening figure stable while improving later diagnostic tables.

### F-06 - WARN: Float Glass process map is linear but not layered
File: `glassmaking/04-FLOAT-GLASS.md`
Finding: The process diagram is readable and detailed, but it is a single
manufacturing line. It does not visually distinguish physics, control levers,
economics, coating/IGU value-add, and failure constraints.
Consequence: The figure supports Candidate-Hardened status; Gold would benefit
from a layered value-chain view or a second diagram tied to product decisions.
Fix: Add a compact downstream map from float ribbon -> annealed sheet ->
tempered/laminated/coated/IGU product choices.

## Summary

No sampled guide has an ASCII failure. Two have WARN-level diagram-depth issues;
one has a strong protected figure. None should be restored to Gold solely from
Da Vinci coverage.

