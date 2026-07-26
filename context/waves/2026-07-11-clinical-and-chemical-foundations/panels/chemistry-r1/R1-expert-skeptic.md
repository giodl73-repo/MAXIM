# Chemistry R1 - Expert Skeptic

## Judgment

The module clears a strong upper-undergraduate / early-graduate reference bar.
The first pass found one incorrect NMR coupling table entry and several bounded
precision issues; no unsafe procedural guidance was found.

## Findings

### F-01 - WARN: Geminal coupling values were reversed

File: `chemistry/06-NMR-SPECTROSCOPY.md`

Finding: The original table assigned the small geminal coupling to sp3
methylenes and the large value to terminal-alkene methylenes.

Fix: The table now records approximately 12-18 Hz magnitude for sp3 CH2 and
approximately 0-3 Hz for terminal sp2 =CH2.

### F-02 - NOTE: GUM Type A/B language needed correction

File: `chemistry/11-MEASUREMENT-AND-SAFETY.md`

Finding: Type A/B describe evaluation methods, not random/systematic effect
types.

Fix: The guide now uses the GUM definition and qualifies coverage factors and
tolerance-to-standard-uncertainty conversion.

### F-03 - NOTE: Several claims needed narrower boundaries

Files: `chemistry/08-CRYSTALLOGRAPHY.md`,
`chemistry/10-COMPUTATIONAL-CHEMISTRY.md`,
`chemistry/11-MEASUREMENT-AND-SAFETY.md`

Finding: XRD certainty, aspirin RDKit logP, inversion-twin interpretation,
Grignard classification, and glove-selection language needed tighter wording.

Fix: Claims are bounded to the method, substrate, and available evidence.
