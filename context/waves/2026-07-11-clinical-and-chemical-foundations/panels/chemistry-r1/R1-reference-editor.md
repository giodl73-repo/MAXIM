# Chemistry R1 - Reference Editor

## Initial Decision

The first review found three Gold blockers despite strong module-wide structure:

1. incomplete statistical-thermodynamics conventions and a non-executable reader
   task in `09-PHYSICAL-CHEMISTRY-DEPTH.md`;
2. a false protecting-group orthogonality claim and insufficient multistep route
   reasoning in `03-ORGANIC-SYNTHESIS.md`;
3. insufficient end-to-end workflow depth in `10-COMPUTATIONAL-CHEMISTRY.md`.

Warnings also covered Ni/Pd/Pt kinetics, ICH Q2 currency, Randles-Sevcik units,
chromatographic selectivity, NMR inference, crystallographic certainty, GUM
definitions, and PPE selection.

## Repair Decision

All blockers were repaired:

- `Q=q^N/N!`, the Stirling `+1` term, standard-state conventions, and a complete
  numerical equilibrium example now anchor physical chemistry.
- Organic synthesis now compares competing disconnections, rejects invalid
  routes, treats protecting-group compatibility as condition-dependent, and
  makes substrate-specific selectivity explicit.
- Computational chemistry now carries an end-to-end state/conformer/method/
  solvent/diagnostics/validation/archive workflow and distinguishes benchmark
  expectations from pinned computed results.

The remaining localized warnings from R2 were repaired before closeout.
