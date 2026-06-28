---
maxim_schema: maxim.frontmatter.v1
id: maxim:dynamical-systems:fractals
kind: guide
module: dynamical-systems
section: dynamical-systems
title: Fractals
status: source-custody
source_custody: partial
current_path: dynamical-systems/07-FRACTALS.md
canonical_path: dynamical-systems/07-FRACTALS.md
backsource_ids: [proof-backfill:dynamical-systems:07-fractals, git-history:dynamical-systems:07-fractals]
concepts: [fractals]
root_concepts: [fractals]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Fractals

A fractal is a set with **detail at every scale** and a **non-integer dimension**. The two ideas are
one: self-similarity across scales is *why* the dimension is fractional. Fractals are the geometry of
chaos — strange attractors (Ch. 06) are fractal, basin boundaries are fractal, and the parameter-space
boundary of chaos (the Mandelbrot set) is fractal. This chapter makes "dimension" precise (box-counting,
Hausdorff), builds fractals as **fixed points of contraction maps** (IFS), and connects the Mandelbrot/Julia
sets back to the iterated-map dynamics of Chapter 08.

```
                     WHAT NON-INTEGER DIMENSION MEANS
                     ================================
   Scale a shape by factor s; count how many copies N tile the original:

     LINE (1D):     halve length -> 2 copies.   N = s^1,  D = 1
     SQUARE (2D):   halve side   -> 4 copies.   N = s^2,  D = 2
     CUBE (3D):     halve edge   -> 8 copies.   N = s^3,  D = 3

     CANTOR SET:    third length -> 2 copies.   N = s^D
                    2 = 3^D  ->  D = ln2/ln3 ~ 0.6309   (BETWEEN 0 and 1)

     KOCH CURVE:    third length -> 4 copies.   D = ln4/ln3 ~ 1.2619 (>1, <2)
     SIERPINSKI:    half  side   -> 3 copies.   D = ln3/ln2 ~ 1.585

                    log N(s)                     "How does the amount of
   DIMENSION  D = ----------     in general.      stuff scale when you
                    log s                         zoom in?" -- a number,
                                                  possibly fractional.
```

---

## Defining Dimension Rigorously

```
   BOX-COUNTING (capacity) DIMENSION  D0  -- the workhorse:
        Cover the set with boxes of side eps. Let N(eps) = minimum number
        of boxes needed.  As eps -> 0:   N(eps) ~ eps^{-D0}.

                        ln N(eps)
        D0 = lim       -----------       (slope of log-log plot)
             eps->0    ln(1/eps)

   HAUSDORFF DIMENSION  D_H  -- the mathematically fundamental one:
        Built from coverings weighted by (diameter)^s; D_H is the unique
        s where the s-dimensional Hausdorff measure jumps from inf to 0.
        For "nice" self-similar sets D_H = D0; in general D_H <= D0.

   INFORMATION (D1) and CORRELATION (D2) dimensions weight boxes by how
   OFTEN the orbit visits them (the natural measure):
        D2 <= D1 <= D0   (generalized "Renyi" dimension spectrum D_q).
        Equality for uniform sets; STRICT inequality for MULTIFRACTALS.
```

For exactly self-similar fractals built from `N` copies each scaled by `r`, the **similarity
dimension** gives the answer in closed form:

```
   N r^D = 1   =>   D = ln N / ln(1/r).

   Cantor:     N=2, r=1/3 -> D = ln2/ln3 ~ 0.631
   Koch:       N=4, r=1/3 -> D = ln4/ln3 ~ 1.262
   Sierpinski: N=3, r=1/2 -> D = ln3/ln2 ~ 1.585
   Menger:     N=20,r=1/3 -> D = ln20/ln3 ~ 2.727 (a "sponge", < 3)
```

### Old world → new world bridges

| You already know | Fractal framing |
|---|---|
| Recursion / self-reference in code | A fractal is the geometric fixed point of a recursive (contraction) rule |
| Big-O log-log scaling plots | Dimension *is* the slope of `log N` vs `log(1/ε)` — same diagnostic |
| Space-filling curves (Hilbert) | A curve (`D_topological=1`) with fractal dimension `2` — fills the plane |
| Compression / minimum description length | IFS fractal compression: store the *rules*, not the pixels |
| Self-similar network / load distributions | Heavy-tail, scale-free structure ⇒ fractal/power-law geometry |

---

## Iterated Function Systems: Fractals as Fixed Points

The deepest unifying idea: a fractal is the **unique fixed point of a contraction on the space of
compact sets**. This is the Banach fixed-point theorem applied to *shapes*.

```
   An IFS is a finite set of CONTRACTION maps {w1, ..., wk} on R^n
   (each shrinks distances: |wi(x) - wi(y)| <= s|x-y|, s < 1).

   Define the HUTCHINSON OPERATOR on sets:
        W(S) = w1(S) U w2(S) U ... U wk(S)    (apply all, union the images)

   THEOREM (Hutchinson): W is a contraction in the Hausdorff metric on
   compact sets. By Banach's fixed-point theorem it has a UNIQUE fixed set
   A* (the ATTRACTOR of the IFS) with W(A*) = A*, and W^n(S0) -> A* from
   ANY starting set S0.

   SIERPINSKI TRIANGLE as an IFS (3 maps, each scale 1/2 to a corner):
        w1: shrink toward bottom-left    Start with ANY S0:
        w2: shrink toward bottom-right        []  ->   /\  ->  /\/\  -> ...
        w3: shrink toward top                          --      ----
                                          converges to the Sierpinski gasket
                                          regardless of S0.
```

This is profound: the fractal *is* the solution of `W(A) = A`, exactly as a fixed point `x* = F(x*)`
solves a dynamical map — the same Banach contraction logic used for Picard existence (Ch. 00) and
for convergence of iterative solvers in `numerical-methods/02`. The **Chaos Game** (pick a random
map each step and plot the orbit) renders the same attractor because the orbit's ω-limit set *is*
`A*`. Fractal image compression stores the `wᵢ` and regenerates the image by iteration — recursion as
data structure.

---

## The Mandelbrot and Julia Sets

The bridge between fractals and *dynamics*: these sets are catalogs of the behavior of a single
iterated map `z → z² + c` on the complex plane.

```
   ITERATE:  z_{n+1} = z_n^2 + c,   z_0 = 0  (or z_0 = z for Julia).

   JULIA SET J_c (fix c, vary starting z): boundary between starting
     points whose orbits stay bounded vs escape to infinity. Connected for
     c inside M; a "Cantor dust" (totally disconnected) for c outside M.

   MANDELBROT SET M (fix z_0=0, vary c): the set of c for which the orbit
     of 0 stays BOUNDED.  M = "the index of all connected Julia sets."

        Im(c)
          |          .-"""""-.            The cardioid body = c values where
          |        .'  bulbs   '.         z->z^2+c has an attracting FIXED pt.
          |   __  ( M  .---.     )        Each circular "bulb" = an attracting
          |  (  )-(    | * | main )       PERIODIC orbit of some period p.
          |   --  ( '. '---'  .'  )       The bulb periods around the cardioid
          |        '.       .'            follow Farey/period-doubling order;
          |          '-...-'              the boundary dD(M) is fractal with
          +------------------------> Re(c)   Hausdorff dimension = 2 (Shishikura).
```

The Mandelbrot set is a **dynamical atlas**: each region of `c` is colored by the *attractor* of the
map `z→z²+c` — fixed point (main cardioid), period-2 (the big disk), period-3, etc. — and the
**period-doubling cascade** along the real axis (`c` from `−0.75` to `−1.401...`) is *literally* the
logistic map's cascade (Ch. 05) in complex disguise. The bulbs' periods exhibit Feigenbaum scaling.
Its boundary has Hausdorff dimension exactly 2 (Shishikura) — maximally rough — yet zero area. This
is the densest link between fractal geometry (this chapter) and iterated-map dynamics (Ch. 08).

---

## Multifractals: When One Dimension Isn't Enough

Real strange attractors are not uniformly dense — orbits visit some regions far more than others. A
*single* dimension `D₀` (which only counts occupied boxes) misses this; you need a **spectrum**.

```
   GENERALIZED (RENYI) DIMENSIONS D_q weight boxes by visitation
   probability p_i raised to the q:

                1        ln SUM p_i^q
        D_q = ----- lim  ------------         D_q is NON-INCREASING in q.
              q-1  eps->0   ln eps

        D_0 = box-counting (geometry only; ignores p_i)
        D_1 = information dimension (entropy scaling; L'Hopital limit)
        D_2 = correlation dimension (pair counting; Ch. 06)

   MONOFRACTAL:  D_q = const for all q (uniform measure).
   MULTIFRACTAL: D_q strictly decreasing -> a whole SPECTRUM f(alpha) of
                 interwoven fractal subsets of differing local density.
```

Multifractals appear wherever a measure is spread unevenly across a fractal support: turbulent energy
dissipation (`fluid-dynamics/`), the harmonic measure on DLA clusters, financial-return roughness,
and the invariant (SRB) measure on strange attractors. The `f(α)` spectrum is the fractal analogue of
a thermodynamic free energy — another deep tie to `statistical-mechanics/` (the `D_q` ↔ Rényi
entropies, the multifractal formalism ↔ Legendre transform of a partition function).

---

## Worked Example: Dimension of a Strange-Attractor Cross-Section

```
   The Lorenz attractor's Poincare section (Ch. 06) is, transverse to the
   sheets, a Cantor-like set. Suppose successive returns split each layer
   into 2 sub-layers at scale ratio r ~ 0.5 (idealized). Then the
   cross-section dimension is:
        D_cross = ln 2 / ln(1/0.5) ... but the true ratio is ~0.06 thin,
   giving a near-zero transverse (Cantor) dimension. Add the 2 "flowing"
   surface dimensions:
        D_attractor ~ 2 + (tiny Cantor dimension) ~ 2.06,
   matching the Kaplan-Yorke value from the Lyapunov spectrum (Ch. 06).

   The point: the fractal "2.06" is 2 smooth directions PLUS a thin
   Cantor dust transverse to the sheets. Geometry (this chapter) and
   dynamics (Lyapunov exponents, Ch. 06) give the SAME number.
```

---

## Decision Cheat Sheet

| Goal | Tool |
|---|---|
| Dimension of an exactly self-similar set | Similarity dimension `D = ln N / ln(1/r)` |
| Dimension of an arbitrary set/data | Box-counting `D₀` (slope of `log N` vs `log 1/ε`) |
| Dimension from a measured time series | Correlation dimension `D₂` (Grassberger–Procaccia) |
| Construct a fractal from rules | Iterated Function System + Hutchinson operator |
| Render an IFS fractal cheaply | Chaos Game (random-map orbit) |
| Catalog a complex map's attractors | Mandelbrot set (parameter plane) + Julia sets (state plane) |
| Capture non-uniform density on a fractal | Multifractal spectrum `D_q` / `f(α)` |
| Relate fractal dim to dynamics | Kaplan–Yorke from Lyapunov spectrum (Ch. 06) |
| Compress self-similar imagery | Fractal (IFS) compression — store the maps |

---

## Common Confusion Points

### "Fractal = infinitely detailed picture"

Detail at all scales is the *visual* symptom; the *definition* is non-integer dimension (or, for
strict self-similar sets, `D_Hausdorff > D_topological`). A space-filling Hilbert curve has
topological dimension 1 but fractal dimension 2 — it is a fractal despite being a "simple" curve. A
smooth curve with wiggles at one scale but not all scales is *not* fractal. The scaling law, not the
prettiness, is the test.

### "Box-counting vs Hausdorff dimension — does it matter which?"

For well-behaved self-similar fractals they agree. In general `D_Hausdorff ≤ D_box`, and they can
differ (e.g. the rationals in [0,1] have `D_Hausdorff = 0` but `D_box = 1`). Hausdorff is the
theoretically canonical definition; box-counting is what you can actually *compute* from data or
images. Report which one you used.

### "The Mandelbrot set is just a pretty picture"

It is a complete **bifurcation atlas** of the family `z → z² + c`: every bulb encodes the *period of
an attracting cycle*, the cardioid is the fixed-point region, and the real-axis cascade *is* the
logistic period-doubling route to chaos (Ch. 05), Feigenbaum constant and all. The Julia set for each
`c` is the corresponding *state-space* boundary. It is dynamics, drawn.

### "More zoom always reveals new structure, forever"

For the mathematical (idealized) fractal, yes — true scale invariance. For *physical* fractals
(coastlines, blood vessels, attractors reconstructed from finite data) self-similarity holds only
across a **finite range** of scales, bounded below by molecular/measurement scales and above by
system size. Always report the scaling range over which a measured dimension was fit; a power law
outside its range is meaningless.

### "A single dimension number describes my attractor"

Only if the invariant measure is uniform (monofractal). Real strange attractors are **multifractal**:
orbits crowd some regions and avoid others, so `D₀ > D₁ > D₂`. A lone "the dimension is 2.06" hides
this. If `D_q` varies with `q`, you have a spectrum, not a number — and the variation itself carries
physical information (e.g. intermittency strength).
