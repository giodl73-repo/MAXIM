# R1 - expert-skeptic

## Findings

### F-07 - WARN: Plate tectonics needs tighter caveats around debated mechanisms
File: `geology/05-PLATE-TECTONICS.md`
Finding: The guide correctly notes plume debate and gives modern plate drivers,
but its opening statement says plates are driven "primarily by slab pull and
ridge push" without immediately separating evidence strength, regime variation,
and ongoing mantle-flow debates.
Consequence: The claim is not egregious, but Gold should bound the mechanism
more carefully for a strong geology reader.
Fix: Add a short caveat near the opening driver sentence: slab pull dominates
many fast subducting systems, ridge push contributes, basal drag/mantle flow is
regime-dependent, and plume interpretation remains contested.

### F-08 - WARN: Effective Stress should distinguish conceptual formula from field uncertainty
File: `geotechnical-engineering/02-EFFECTIVE-STRESS.md`
Finding: The equation and examples are sound, but the guide could better surface
field uncertainty: stratigraphic variability, anisotropic permeability,
partially saturated behavior, and construction-stage pore-pressure measurement.
Consequence: A reader might over-trust clean calculations without enough field
instrumentation context.
Fix: Add a Gold-level caveat block connecting piezometers, lab parameters, field
permeability, and staged construction monitoring.

### F-09 - WARN: Float Glass has strong facts but needs product-risk caveats
File: `glassmaking/04-FLOAT-GLASS.md`
Finding: The guide is fact-dense, but safety and energy-performance decisions
are mostly downstream facts. It should more explicitly warn that annealed float
glass is not acceptable in hazardous locations and that Low-E/IGU choices depend
on code, climate, orientation, and processing sequence.
Consequence: The guide is high-value but not yet adversarially complete for
building-product decisions.
Fix: Add a caveat/selection block before the cheat sheet tying product choice to
safety code, thermal target, coating durability, tempering order, and climate.

## Summary

No sampled guide has a factual BLOCK. All three have WARN-level caveat or
field-decision gaps that justify Candidate-Hardened status rather than Certified
Gold.

