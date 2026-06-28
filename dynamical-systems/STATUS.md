# dynamical-systems/ — Status

## Files

| File | Topic | Status |
|------|-------|--------|
| 00-OVERVIEW.md | Landscape: flows vs maps, state space, linear → nonlinear → chaos; existence/uniqueness; the central questions | ✅ |
| 01-FLOWS-AND-FIXED-POINTS.md | Vector fields, flows, fixed points, 1D phase lines, conservative vs dissipative, nullclines, invariant sets | ✅ |
| 02-STABILITY-AND-LINEARIZATION.md | Jacobian, eigenvalue stability, 2D fixed-point classification, Hartman-Grobman, Lyapunov functions, LaSalle | ✅ |
| 03-BIFURCATIONS.md | Saddle-node / transcritical / pitchfork / Hopf, normal forms, bifurcation diagrams, codimension, hysteresis | ✅ |
| 04-LIMIT-CYCLES.md | Periodic orbits, Poincaré-Bendixson, van der Pol, relaxation oscillations, Liénard, index theory | ✅ |
| 05-CHAOS.md | Logistic map, period-doubling cascade, Feigenbaum δ ≈ 4.669, Lyapunov exponents, SDIC, routes to chaos | ✅ |
| 06-STRANGE-ATTRACTORS.md | Lorenz, Rössler, fractal/correlation dimension, Poincaré sections, attractor reconstruction (Takens) | ✅ |
| 07-FRACTALS.md | Self-similarity, box-counting & Hausdorff dimension, Mandelbrot/Julia sets, IFS, multifractals | ✅ |
| 08-DISCRETE-MAPS.md | Iterated maps, cobwebbing, symbolic dynamics, shift map, Hénon, Smale horseshoe, Sharkovskii | ✅ |
| 09-APPLICATIONS.md | Synchronization (Kuramoto), network dynamics, gradient flows (ML), control of chaos (OGY/Pyragas) | ✅ |

## Completed

2026-06-27 — All 10 files written. Full coverage: continuous flows and fixed points through
chaos, strange attractors, fractal geometry, discrete maps, and applications to synchronization,
networks, machine-learning gradient flows, and chaos control.

## Coverage Notes

The qualitative and quantitative theory of how systems evolve in time — both continuous flows
(ODEs) and discrete maps. Distinct from `numerical-methods/` (which covers the *algorithms* that
integrate ODEs) and from `mathematics/` differential-equations material (which covers closed-form
solution techniques): this directory covers the *geometric* and *asymptotic* theory — what
trajectories do without solving them. Strong bridges to `control-theory/` (Lyapunov stability,
feedback as bifurcation control, Hopf and limit cycles), `numerical-methods/` (RK integrators,
stiffness, shadowing), `statistical-mechanics/` (ergodicity, mixing, SRB measures, phase
transitions as bifurcations), `fluid-dynamics/` (Lorenz from Rayleigh-Bénard convection,
transition to turbulence), and machine learning (gradient descent as a discretized gradient flow,
training instability as eigenvalue/Hopf phenomena). The MIT TCS learner will recognize symbolic
dynamics as a bridge to formal languages and the shift map as a full-shift automaton.
