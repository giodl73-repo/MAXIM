# numerical-methods/ — Status

## Files

| File | Topic | Status |
|------|-------|--------|
| 00-OVERVIEW.md | Landscape: the four problems (solve Ax=b, find eigenvalues, integrate, solve ODEs/PDEs); error taxonomy | 🔜 |
| 01-FLOATING-POINT.md | IEEE 754, rounding modes, cancellation, conditioning vs. stability, interval arithmetic | 🔜 |
| 02-LINEAR-SYSTEMS.md | Gaussian elimination, LU/QR/Cholesky factorization, iterative methods (CG/GMRES/multigrid) | 🔜 |
| 03-EIGENVALUE-METHODS.md | Power iteration, QR algorithm, Lanczos, SVD computation, randomized algorithms | 🔜 |
| 04-INTERPOLATION.md | Polynomial interpolation (Lagrange/Newton), splines (cubic/B-spline), scattered data (RBF) | 🔜 |
| 05-NUMERICAL-INTEGRATION.md | Newton-Cotes, Gaussian quadrature, adaptive integration, Monte Carlo methods | 🔜 |
| 06-ODES.md | Euler, Runge-Kutta families, stiff systems (BDF/Rosenbrock), boundary value problems (shooting/collocation) | 🔜 |
| 07-PDES.md | Finite differences, finite element method, spectral methods, finite volume, stability (CFL condition) | 🔜 |
| 08-OPTIMIZATION.md | Gradient descent, Newton/quasi-Newton, convex optimization (interior point), global methods (SA/GA) | 🔜 |
| 09-SCIENTIFIC-COMPUTING.md | BLAS/LAPACK/ScaLAPACK, sparse matrices, GPU computing, NumPy/SciPy/Julia/MATLAB ecosystem | 🔜 |

## Coverage Notes

The computational layer below all applied science and engineering. Distinct from computing/ (which covers software engineering stack) and mathematics/ (which covers theory) — this directory covers algorithms for numerical computation. Bridges mathematics/, physics/, and engineering/ via computational simulation. The MIT TCS learner will recognize connections to algorithm complexity, but this is the applied/numerical side rather than the combinatorial/symbolic side. Strong connections to data-science/ (matrix operations underlie all of ML) and differential-geometry/ (geodesic computation, manifold optimization).
