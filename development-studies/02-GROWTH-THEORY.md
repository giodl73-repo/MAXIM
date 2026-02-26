# Growth Theory: Harrod-Domar, Solow, Endogenous Growth, Convergence

## The Big Picture

Growth theory asks: what determines the long-run growth rate of an economy? The models progress from mechanical capital accumulation (Harrod-Domar, 1940s) through neoclassical steady states (Solow, 1956) to endogenous innovation and knowledge (Romer, 1986–1990). Each model makes different predictions about convergence — whether poor countries will catch up to rich ones.

```
+--------------------------------------------------------------------------+
|                    GROWTH THEORY LANDSCAPE                                |
+--------------------------------------------------------------------------+
|                                                                          |
|  MODEL           KEY VARIABLE    LONG-RUN GROWTH    CONVERGENCE         |
|  ─────────────────────────────────────────────────────────────────────  |
|  Harrod-Domar    Capital stock   g = s/v (savings/  Yes (if same s, v)  |
|  (1939–46)       K              capital-output)     Unstable path       |
|                                                                          |
|  Solow           Capital K +    Exogenous TFP A     Yes, conditional    |
|  (1956)          Labor L         (Solow residual)   Diminishing returns |
|                                                                          |
|  AK Model        K broadly      g = sA (constant    No                  |
|  (Rebelo 1991)   defined         marginal product)  No diminishing K    |
|                                                                          |
|  Romer (1986)    Knowledge K    Endogenous, from    No (divergence)     |
|                  (non-rival)     spillovers                             |
|                                                                          |
|  Lucas (1988)    Human capital  Endogenous, from    No                  |
|                  H               human capital                          |
|                                                                          |
|  Romer (1990)    Ideas / R&D    Endogenous, from    Conditional         |
|                  (non-rival,     monopolistic                            |
|                  partly excl.)   innovation                              |
|                                                                          |
|  Aghion-Howitt   Schumpeterian  Creative           Distance from        |
|  (1992)          destruction     destruction        frontier matters    |
+--------------------------------------------------------------------------+
```

---

## 1. Harrod-Domar Model

Roy Harrod (1939) and Evsey Domar (1946) independently derived essentially the same result, designed originally to analyze business cycle stability, but widely applied to development planning in the 1950s–60s.

**Core equation**:
```
g = s / v

where:
  g = growth rate of national income
  s = savings rate (= investment rate in closed economy)
  v = capital-output ratio (capital required per unit of output)

Example: s = 20%, v = 4 → g = 5%
If you want 6% growth and v = 4, you need s = 24%
```

**The knife-edge problem**: Harrod's "warranted" growth rate (g_w = s/v) is the rate at which entrepreneurs are exactly satisfied with their investment decisions. But if actual growth exceeds g_w, investment increases, moving growth further above g_w — explosive. If below g_w, it collapses. The economy has no self-stabilizing mechanism.

```
HARROD INSTABILITY:

  Actual growth > Warranted growth
       ↓ firms find inventories depleted
  Increase investment
       ↓ accelerator effect
  Growth increases further
       ↓
  EXPLOSIVE EXPANSION (or oscillation)

  Same logic in reverse for recessions.
  The "natural rate" (n + tech progress) adds another
  coincidence requirement — g_w = g_n = s/v.
```

**Development policy application**: If you know v (engineering estimates of capital requirements for a project), the model tells you how much investment/savings you need for target growth. This was the basis for World Bank project lending and Soviet-style planning in the 1950s–60s. The fallacy: v is not technologically fixed; it responds to factor prices and institutions.

---

## 2. The Solow Model (1956)

Robert Solow's model (*A Contribution to the Theory of Economic Growth*, QJE 1956) introduced two crucial changes from Harrod-Domar:
1. **Diminishing returns** to capital: v is not constant, it rises as capital accumulates
2. **Factor substitutability**: the economy can use more labor relative to capital

**Production function**:
```
Y = A · F(K, L)     [or in intensive form: y = A · f(k)]

where:
  Y = total output
  y = output per worker (Y/L)
  K = capital stock
  k = capital per worker (K/L)
  L = labor (exogenous growth at rate n)
  A = total factor productivity (TFP) — exogenous
  f(k) = per-worker production function: f'(k) > 0, f''(k) < 0
         (positive but diminishing marginal product)
```

**Capital accumulation**:
```
dk/dt = s·f(k) - (n + δ)·k

Investment per worker = savings per worker
Depreciation + dilution = (depreciation rate + population growth) × k

At steady state: dk/dt = 0
  s·f(k*) = (n + δ)·k*     ← the steady-state capital per worker
```

```
SOLOW DIAGRAM:

 Output/worker
      |
  f(k)|          f(k) = per-worker production function
      |         /                (diminishing returns → concave)
      |        /
      |       / ← actual investment: s·f(k)
  k*y |....../.....
      |    ./    .
      |  ./      .
      | ./       .
      |./        .
      +---+------+-------→ k (capital per worker)
         k*    (breakeven investment line: (n+δ)k)

At k*: investment exactly covers depreciation + dilution
       Economy stays at k* forever (without A growth)
```

**Steady state properties**:
- Capital per worker is constant at k*
- Output per worker is constant at y* = f(k*)
- Long-run growth in output *per worker* = 0 (without TFP growth)
- Total output grows at rate n (population growth)
- **Key implication**: capital accumulation alone cannot sustain long-run growth per capita

**The Solow Residual (TFP)**:
```
TFP = A in Y = A·F(K,L)
    = growth in Y not explained by growth in K and L

Solow decomposition:
  ΔY/Y = α·ΔK/K + (1-α)·ΔL/L + ΔA/A

  For US 1909–1949, Solow found ~87.5% of per-capita output
  growth was ΔA/A — unexplained by capital or labor.
  This "residual" is often called technical progress.
  Endogenous growth theorists try to explain it.
```

**The Golden Rule**: What savings rate maximizes *consumption* per worker at steady state?
```
Golden Rule: maximize c* = f(k*) - (n+δ)k*
             → f'(k*_gold) = n + δ
             → MPK = n + δ

If f'(k*) > n+δ: economy is below golden rule (save more)
If f'(k*) < n+δ: economy is over-accumulating capital (save less)
```

---

## 3. Convergence: Conditional vs. Unconditional

The Solow model predicts **convergence**: countries with less capital per worker than their steady state grow faster. This is because f''(k) < 0 — diminishing returns means the marginal product of capital is higher when k is low.

```
CONVERGENCE TYPES:

Unconditional (absolute) convergence:
  All countries converge to the SAME income level.
  Prediction: poor countries grow faster than rich ones, period.
  Evidence: FALSE for broad sample (Baumol 1986 found it only
           in OECD countries, not globally)

Conditional convergence:
  Countries converge to THEIR OWN steady state.
  Countries with same s, n, δ, A converge to same k*.
  Poor countries among them grow faster.
  Evidence: SUPPORTED in cross-country regressions
           (Barro-Sala-i-Martin 1992: conditional on
           savings rate, education, institutions)

Convergence clubs:
  Multiple steady states: rich-country club and
  poor-country trap. Countries can get stuck.
  (Quah 1993: twin peaks in world income distribution)
```

**The Baumol convergence controversy**: Baumol (1986) showed convergence among 16 now-rich countries from 1870–1979. DeLong (1988) showed this was sample selection bias — the 16 countries are rich *because* they converged; the poor countries that tried but failed were excluded.

---

## 4. Endogenous Growth: AK Model and Knowledge Spillovers

The Solow model's fatal limitation: long-run growth per capita depends entirely on exogenous TFP (A). Endogenous growth theory explains A from within the model.

**AK Model (Rebelo 1991)**:
```
Y = A · K     (broad capital, including human capital)

  No diminishing returns if K includes all accumulated factors
  dy/dt = A · dk/dt = A · (sY - δK) = (sA - δ) · Y

  g = sA - δ     ← growth rate permanently depends on savings rate
                 ← policy (s) permanently affects growth rate
                 ← no convergence: richer countries can stay richer
```

**Paul Romer (1986) — Knowledge Spillovers**:
```
Individual firm: y_i = A(K) · f(k_i)
Aggregate capital K creates externality A(K) — publicly available knowledge

If A(K) = K → no diminishing returns at aggregate level even if
diminishing at firm level (firms don't internalize the spillover)

IMPLICATION:
- Market equilibrium is suboptimal (spillovers not priced)
- Subsidy to investment is welfare-improving
- Rich countries can have permanently higher growth rates
- Divergence, not convergence
```

**Lucas (1988) — Human Capital**:
```
Y = A · K^α · (u·H·L)^(1-α) · H^γ

where H = average human capital stock in economy
      u = fraction of time working (vs. studying)
      γ = external effect of human capital

Key: human capital has no diminishing returns (learning begets
     more learning capacity); its externalities explain why
     cities and educated regions grow faster
```

---

## 5. Romer 1990: Ideas as Non-Rival Goods

Romer's 1990 paper (*Endogenous Technological Change*, JPE 1990) is the foundational model of innovation-led growth:

```
ROMER'S KEY INSIGHT:

Ideas are NON-RIVAL: my using calculus doesn't reduce your ability
to use calculus. (Unlike capital: my machine ≠ your machine.)

But ideas can be (partially) EXCLUDABLE via:
  - Patents (temporary monopoly)
  - Trade secrets
  - First-mover advantage

NON-RIVAL + PARTIALLY EXCLUDABLE →
  Monopolistic competition for innovations
  Firms invest in R&D to earn temporary monopoly rents
  Government must subsidize R&D (positive externalities from knowledge)
```

**Romer's model structure**:
```
Three sectors:
  1. Research sector: produces new designs using human capital H_A
     dA/dt = δ · H_A · A  (stock of knowledge A makes research more productive)

  2. Intermediate goods: each design owner produces specialized input
     under monopoly (Dixit-Stiglitz monopolistic competition)

  3. Final goods: assembles intermediate inputs
     Y = H_Y^α · L^β · Σ(x_i^(1-α-β))   (sum over all varieties)

KEY RESULT: Growth rate g ∝ H (human capital stock)
  → Larger countries with more researchers grow faster
  → Scale effect (controversial: not supported empirically)
```

---

## 6. Schumpeterian Growth: Aghion-Howitt

Aghion and Howitt (1992) incorporate *creative destruction* — new innovations make old ones obsolete:

```
SCHUMPETERIAN MECHANISM:

  R&D investment → new technology (arrives stochastically)
        ↓
  New technology replaces old intermediate good
        ↓
  Old intermediate good producer's monopoly rents → 0
  (creative destruction)
        ↓
  New innovator earns monopoly rents... until next innovation
        ↓
  Expected monopoly rents drive R&D investment

INVERTED-U RELATIONSHIP with competition:
  Too little competition → no pressure to innovate (incumbents satisfied)
  Too much competition → no monopoly rents to recover R&D cost
  Intermediate competition → maximum innovation
  (Aghion et al. 2005 empirical paper on UK firms)
```

**Distance from frontier matters**: Countries close to the technological frontier need radical "step-ahead" innovation. Countries far from frontier benefit more from imitation/adaptation (lower cost). Policy: different innovation policy for different distances.

---

## 7. Growth Empirics

**Barro regressions**: Cross-country growth regressions (Barro 1991):
```
g_i = β₀ + β₁·log(Y₀_i) + β₂·SCHOOL_i + β₃·GOV_i + ... + ε_i

where:
  g_i = average growth rate 1960–1990 for country i
  Y₀_i = initial income (tests conditional convergence)
  SCHOOL_i = human capital measures
  GOV_i = government spending, rule of law, etc.

Key findings:
  β₁ < 0: conditional convergence (confirmed)
  β₂ > 0: education matters for growth
  β₃: depends on type (distortionary taxes hurt; infrastructure helps)
```

**The geography vs. institutions debate**:

| Sachs position | Acemoglu-Johnson-Robinson counter |
|---------------|-----------------------------------|
| Geography (latitude, malaria, soil) directly causes poverty | Geography → colonization type → institutions → income |
| Tropical disease kills productivity | Settler mortality instrument isolates institutional channel |
| Africa poor because of disease ecology | Africa poor because of extractive colonial institutions |
| Policy: technical fixes (bed nets, drainage) | Policy: institutional reform, democratization |
| Evidence: malaria burden correlates with poverty | Evidence: AJR 2001, settler mortality IV, R² = 0.52 |

**Problems with growth empirics**:
- Endogeneity everywhere: do good institutions cause growth, or does growth produce better institutions?
- Variable selection and specification searching: hundreds of potential covariates, many correlated
- Cross-country heterogeneity: same coefficient means different things in different contexts
- Reverse causality: most "determinants" of growth also respond to growth

---

## Decision Cheat Sheet

| Model | Key equation | Convergence prediction | Long-run growth driver | Policy implication |
|-------|-------------|----------------------|----------------------|-------------------|
| Harrod-Domar | g = s/v | Yes (conditional) | Savings rate | Raise savings; plan capital |
| Solow | dk/dt = sf(k) − (n+δ)k | Yes, conditional | Exogenous TFP (A) | Education, institutions (affect A) |
| AK | g = sA − δ | No | Savings rate (permanently) | Subsidize capital formation |
| Romer 1986 | A(K) spillover | No | Knowledge spillovers | Subsidize investment (externality) |
| Lucas 1988 | Human capital H | No | Human capital accumulation | Invest in education |
| Romer 1990 | Ideas non-rival; monopolistic competition | Conditional | R&D investment | Patent system; R&D subsidies |
| Aghion-Howitt | Creative destruction | Depends on distance | Innovation competition | Competition policy; frontier-specific |

---

## Common Confusion Points

**Solow's residual is not "technology"**: The residual is everything not explained by measured capital and labor growth — it includes management quality, resource allocation efficiency, institutional improvement, and measurement error, not just R&D-driven technology. Calling it "TFP" is already a modeling choice.

**Diminishing returns to capital doesn't mean diminishing returns to all factors**: AK model gets around Solow by broadening "capital" to include human capital, organizational capital, knowledge. If you define capital broadly enough, you can argue no diminishing returns. Whether this is an insight or a tautology depends on what's in your K.

**The Barro regression "kitchen sink" problem**: Put enough controls in a cross-country regression and you can explain almost any result. Sala-i-Martin (1997) tested 59 variables and found 22 "robustly" correlated with growth — but with enough data mining, this proves nothing without theoretical priors.

**Scale effects in Romer 1990**: The model predicts larger countries (more H) grow faster. This is the "scale effect" — not supported empirically (Luxembourg grows faster than India). Semi-endogenous growth models (Jones 1995) remove the scale effect but make growth depend on population growth rate, not level.

**Convergence and the missing capital flows paradox**: If poor countries have high marginal product of capital (Solow implies this), capital should flow massively from rich to poor countries. It doesn't (Lucas paradox, 1990). Explanation: institutional quality, human capital, political risk — all reduce effective MPK in poor countries even if physical MPK is high.
