# Gauge Theory and the Standard Model

## The Big Picture

Gauge theory is the framework in which the Standard Model is formulated. The central idea: the
laws of physics should be invariant under local (position-dependent) symmetry transformations.
Requiring this invariance forces the existence of force-mediating fields. The symmetry group is
a Lie group; the forces are the curvature of a connection on a principal bundle.

```
+----------------------------------------------------------------------+
|           THE STANDARD MODEL GAUGE GROUP                             |
+----------------------------------------------------------------------+
|                                                                      |
|   G_SM = SU(3) x SU(2) x U(1)                                       |
|            |       |       |                                         |
|           QCD    Weak   Hypercharge                                  |
|          (color) (isospin)                                           |
|            |       |       |                                         |
|          gluons  W+,W-,Z  photon (after symmetry breaking)          |
|          8 gen.  3 gen.   1 gen.                                     |
|         dim=8   dim=3    dim=1                                       |
|                                                                      |
|  Matter fields (fermions) live in REPRESENTATIONS of G_SM:          |
|  Quarks:   (3, 2, 1/6)   [color x isospin x hypercharge]            |
|  Leptons:  (1, 2, -1/2)                                             |
|  ...                                                                 |
|                                                                      |
|  The Higgs: (1, 2, 1/2)  -- breaks SU(2)xU(1) -> U(1)_EM          |
|                                                                      |
+----------------------------------------------------------------------+
```

---

## U(1) Gauge Theory: Electromagnetism

**Global U(1) symmetry:** A free charged particle with field psi(x) is invariant under
psi(x) -> e^{i alpha} psi(x) for constant alpha. This is a global U(1) symmetry.

**Making it local:** Demand invariance under psi(x) -> e^{i alpha(x)} psi(x) for
position-dependent alpha(x). The kinetic term d_mu psi doesn't transform well:
```
d_mu psi -> e^{i alpha} (d_mu + i d_mu alpha) psi
```
The extra i d_mu alpha spoils invariance.

**Fix — introduce a gauge field:** Replace d_mu with the covariant derivative:
```
D_mu psi = (d_mu - i e A_mu) psi
```
where A_mu(x) is a new gauge field (the photon). Under gauge transformation:
```
psi -> e^{i alpha} psi
A_mu -> A_mu + (1/e) d_mu alpha
```
Then D_mu psi -> e^{i alpha} D_mu psi (covariant), so the kinetic term |(D_mu psi)|^2 is invariant.

**The curvature of A:** The field strength tensor:
```
F_mu nu = d_mu A_nu - d_nu A_mu = [D_mu, D_nu] / (-ie)
```
F_mu nu is the electromagnetic field tensor: F_{01}=E_x, F_{12}=B_z, etc.

**Lagrangian:**
```
L_EM = -(1/4) F^{mu nu} F_{mu nu} + psi_bar (i D_slash - m) psi
```
The first term is the photon kinetic/self-interaction term. The second is the matter term.
Local U(1) invariance uniquely (up to coupling constants) determines this Lagrangian.
This is the essence of gauge theory: symmetry requirement -> dynamics.

---

## Non-Abelian Gauge Theory: Yang-Mills (1954)

Yang and Mills generalized electromagnetism to non-abelian gauge groups. The key difference:
the gauge fields don't commute, so the field strength has a nonlinear term.

**Non-abelian gauge field:** Take G = SU(2) (or any Lie group). The gauge field A_mu is a
Lie-algebra-valued 1-form:
```
A_mu(x) in su(2)   (a traceless skew-Hermitian 2x2 matrix at each point x)
A_mu = A_mu^a T_a  (T_a are the generators, a = 1,2,3 for SU(2))
```

**Covariant derivative:** For a field psi in a representation rho of G:
```
D_mu psi = d_mu psi - g A_mu^a rho(T_a) psi
```
(g is the coupling constant; rho(T_a) is the generator matrix in the representation psi lives in)

**Gauge transformation:** For U(x) in G (locally):
```
psi(x)   ->  U(x) psi(x)
A_mu(x)  ->  U A_mu U^{-1} + (1/g) (d_mu U) U^{-1}
```

**Field strength (curvature):**
```
F_mu nu = d_mu A_nu - d_nu A_mu + g [A_mu, A_nu]   (non-abelian curvature)
F_mu nu = F^a_{mu nu} T_a
F^a_{mu nu} = d_mu A^a_nu - d_nu A^a_mu + g f^{abc} A^b_mu A^c_nu
```
where f^{abc} are the structure constants: [T_a, T_b] = f^{abc} T_c.

The [A_mu, A_nu] term is new compared to electromagnetism. It causes gluons to interact with
each other — unlike photons, which do not interact directly (since [A_mu, A_nu] = 0 for U(1)).

**Yang-Mills Lagrangian:**
```
L_YM = -(1/4g^2) tr(F^{mu nu} F_{mu nu}) = -(1/4) F^{a mu nu} F^a_{mu nu}
```
(The trace uses the invariant inner product on the Lie algebra.)

---

## SU(2) Weak Force

**Weak isospin group G = SU(2)_L.** The "L" means it acts only on left-handed fermion fields.

**The electroweak gauge group** is SU(2)_L x U(1)_Y (before symmetry breaking).
Generators: T_1, T_2, T_3 for SU(2); Y for U(1).

**Gauge bosons (before breaking):** W_mu^1, W_mu^2, W_mu^3 from SU(2) (3 generators);
B_mu from U(1)_Y (1 generator). Total: 4 gauge bosons.

**Higgs mechanism (SSB):** The Higgs doublet H = [[phi+],[phi0]] in representation (1,2,1/2)
of G_SM acquires a vacuum expectation value: <H> = [[0],[v/sqrt(2)]].

This breaks SU(2)_L x U(1)_Y -> U(1)_EM:
```
Before SSB:  4 massless gauge bosons: W^1, W^2, W^3, B
After SSB:   3 massive bosons: W+ = (W^1 - iW^2)/sqrt(2)  mass = gv/2
                                W- = (W^1 + iW^2)/sqrt(2)  mass = gv/2
                                Z  = cos_W W^3 - sin_W B   mass = gv/(2cos_W)
             1 massless boson:  gamma = sin_W W^3 + cos_W B  (photon)
```
where Weinberg angle theta_W satisfies tan(theta_W) = g'/g (ratio of U(1) and SU(2) couplings).

**Fermion masses:** Also come from the Higgs VEV through Yukawa couplings. The mass matrix for
quarks is a 3x3 complex matrix — its singular value decomposition gives the quark masses and
the CKM matrix (the quark mixing matrix).

---

## SU(3) Strong Force: Quantum Chromodynamics

**Color gauge group G = SU(3).** "Color" is the SU(3) charge; quarks carry color.

**Generators:** 8 linearly independent traceless skew-Hermitian 3x3 matrices.
The conventional basis (Gell-Mann matrices lambda_a, a=1,...,8) is the physicist's convention;
the Lie algebra generators are T_a = lambda_a / 2.

**Structure constants:** f^{abc} defined by [T_a, T_b] = i f^{abc} T_c.
Key values: f^{123}=1, f^{147}=f^{246}=f^{257}=f^{345}=1/2, f^{156}=f^{367}=-1/2, etc.

**Matter representations:**
- Quarks: fundamental 3-dim representation (one quark = a 3-component color vector)
- Antiquarks: anti-fundamental (conjugate) 3*-dim representation
- Gluons: adjoint 8-dim representation

**Color confinement (non-perturbative):** In QCD, isolated quarks cannot exist. Only
"color-neutral" (singlet) combinations appear as hadrons:
```
Mesons (qq-bar):   3 tensor 3* = 8 + 1  (the 1 = singlet = meson)
Baryons (qqq):     3 tensor 3 tensor 3 = 10 + 8 + 8 + 1  (the 1 = baryon)
```
This decomposition is a Clebsch-Gordan computation for SU(3).

**Asymptotic freedom:** The running coupling constant g_s(mu) decreases at high energy for
non-abelian gauge theories with few matter fields. For SU(N) with N_f flavors:
```
beta(g) = -g^3/(16pi^2) * (11/3 N - 2/3 N_f) + O(g^5)
```
Asymptotic freedom (beta < 0) requires 11N/3 > 2N_f/3. For SU(3), N=3: 11 > 2N_f/3, so N_f < 16.5.
QCD has 6 flavors, well within the asymptotically free range. This was discovered by Gross-Wilczek
and Politzer in 1973 (Nobel Prize 2004).

---

## The Full Standard Model

**Gauge group:** G_SM = SU(3)_c x SU(2)_L x U(1)_Y

**Matter content (one generation of fermions):**

| Field | Representation | SU(3) | SU(2) | U(1)_Y |
|-------|---------------|-------|-------|--------|
| Q_L (left quark doublet) | (3,2,1/6) | fundamental | fundamental | 1/6 |
| u_R (right up quark) | (3,1,2/3) | fundamental | singlet | 2/3 |
| d_R (right down quark) | (3,1,-1/3) | fundamental | singlet | -1/3 |
| L_L (left lepton doublet) | (1,2,-1/2) | singlet | fundamental | -1/2 |
| e_R (right electron) | (1,1,-1) | singlet | singlet | -1 |

Three generations of this pattern, plus the Higgs (1,2,1/2). That's the entire Standard Model
matter content. The gauge bosons are in the adjoint representations:
- 8 gluons: adjoint of SU(3)
- 3 W bosons: adjoint of SU(2)
- 1 B boson: adjoint of U(1)

**Anomaly cancellation:** For quantum consistency, the theory must be free of gauge anomalies.
This is a constraint on the fermion representations. The Standard Model fermion content is
precisely anomaly-free — this is a non-trivial constraint that the above assignment satisfies.
The cancellation involves the specific hypercharge assignments (the 1/6, 2/3, -1/3, etc.) and
is why the quark and lepton charges are related.

---

## Yang-Mills Equations and Instantons

**Yang-Mills equations** (analogues of Maxwell's equations in curved Lie-algebra-valued form):
```
D_mu F^{mu nu} = J^nu      (equations of motion for gauge field)
D_[mu F_{nu rho]] = 0      (Bianchi identity, automatic)
```

**Self-dual and anti-self-dual connections:** Define the dual field strength:
```
*F_{mu nu} = (1/2) epsilon_{mu nu rho sigma} F^{rho sigma}
```
Self-dual connections (F = *F) automatically satisfy the Yang-Mills equations (instantons).
Anti-self-dual (F = -*F) also automatic (anti-instantons).

**Instantons:** Classical solutions of the Euclidean Yang-Mills equations that are localized
in Euclidean spacetime (finite action, F -> 0 at infinity). They contribute to path integrals
via tunneling between topologically distinct vacua. The topological charge:
```
k = (g^2/16pi^2) integral tr(F wedge F) in Z
```
classifies instantons by an integer (the instanton number).

**BPST instanton (SU(2), k=1):**
```
A_mu = (2/g) * Im(q_bar d_mu q) / (|x|^2 + rho^2)
```
where q is a unit quaternion and rho is the instanton size. Instantons drive chiral symmetry
breaking in QCD and contribute to the theta-vacuum structure.

---

## Decision Cheat Sheet

| Physical effect | Gauge group | Mathematical structure |
|-----------------|-------------|----------------------|
| Electromagnetism | U(1) | Abelian gauge field = 1-form on R^{3,1} |
| Weak force | SU(2)_L | Non-abelian; chiral (left-handed only) |
| Electroweak unification | SU(2)_L x U(1)_Y | Spontaneously broken by Higgs |
| Strong force / QCD | SU(3)_c | 8 gluons = adjoint representation |
| Standard Model | SU(3)xSU(2)xU(1) | Product of three gauge theories |
| Requiring local symmetry | Any group G | Forces gauge boson to cancel non-covariance |
| Topological charge | Any non-abelian | pi_3(G) for instantons (= Z for SU(2)) |

---

## Common Confusion Points

**"SU(2) is the weak force":** More precisely, SU(2)_L x U(1)_Y is the electroweak gauge group,
spontaneously broken to U(1)_EM by the Higgs. The unbroken SU(2) would give 3 massless W bosons;
the breaking gives 2 massive W's, 1 massive Z, and 1 massless photon.

**"The gauge group acts on spacetime":** No. The gauge group G acts on the *fibers* of a vector
bundle over spacetime. At each spacetime point x, there is a copy of G acting on the local
representation space. This is the principal bundle picture (08-DIFFERENTIAL-GEOMETRY.md).

**"Gluons carry color charge":** Yes. Unlike photons (which are U(1) gauge bosons and neutral),
gluons are SU(3) adjoint reps and carry color-anticolor charge. This is because SU(3) is
non-abelian: the [A,A] term in F means gluons interact with themselves. Three-gluon and
four-gluon vertices exist in QCD.

**"Anomaly cancellation is automatic":** Not at all. An arbitrary assignment of fermion
representations to a gauge group is generically anomalous (quantum consistency fails). The
Standard Model representation content is special: the anomalies cancel precisely because
quarks come in 3 colors and the hypercharges satisfy specific sum rules. This is sometimes
called the "miracle" of the Standard Model.
