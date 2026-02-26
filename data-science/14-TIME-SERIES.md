# Time Series Analysis
## Stationarity, ARIMA, State Space Models, Kalman Filter, and Modern Neural Methods

```
TIME SERIES TAXONOMY

  ┌────────────────────────────────────────────────────────────────┐
  │  Univariate              Multivariate                          │
  │  ─────────────           ──────────────────                   │
  │  AR, MA, ARIMA           VAR, VECM, multivariate SSM          │
  │  GARCH (variance)        DCC-GARCH                            │
  │                                                                │
  │  Stationary              Non-stationary                       │
  │  ─────────────           ──────────────────                   │
  │  ARMA                    ARIMA (difference to stationarity)   │
  │  spectral analysis       VECM (cointegration)                 │
  │                                                                │
  │  Linear                  Non-linear                           │
  │  ─────────────           ──────────────────                   │
  │  ARIMA, Kalman           GARCH, TAR, Prophet, NNs             │
  └────────────────────────────────────────────────────────────────┘
```

---

## 1. Stationarity

**Strict stationarity**: the joint distribution of (x_t, ..., x_{t+k}) is the same for all t and k.

**Weak (covariance) stationarity**:
```
  1. E[x_t] = μ  (constant mean)
  2. Var(x_t) = σ²  (finite, constant variance)
  3. Cov(x_t, x_{t+k}) = γ(k)  (autocovariance depends only on lag k, not t)
```

Most time series methods assume weak stationarity.

**Common non-stationarities**:
```
  Trend:       E[x_t] = f(t) (growing/declining mean)
  Unit root:   x_t = x_{t-1} + ε_t  (random walk — variance grows with t)
  Heteroskedasticity: Var(x_t) changes over time (→ GARCH)
  Seasonality: periodic structure (→ SARIMA, STL decomposition)
```

**Lag operator** (backshift operator) B:
```
  B x_t = x_{t-1}
  B^k x_t = x_{t-k}
  (1-B) x_t = x_t - x_{t-1} = Δx_t  (first difference)
  (1-B)^d x_t = Δ^d x_t               (d-th order difference)
```

Differencing removes unit roots: if x_t ~ I(1) (integrated of order 1), then Δx_t is stationary.

### Unit Root Tests

**Augmented Dickey-Fuller (ADF)**:
```
  H₀: unit root (x_t is I(1))  — non-stationary
  H₁: no unit root              — stationary

  Regression: Δx_t = α + βt + γx_{t-1} + Σ δⱼΔx_{t-j} + εₜ
  Test statistic: t-ratio of γ
  Critical values from Dickey-Fuller distribution (left tail)

  Derived from characteristic polynomial: AR(p) has unit root iff characteristic
  polynomial has a root on the unit circle.
```

**KPSS**:
```
  H₀: stationary (reversal of ADF)
  H₁: unit root

  Use both ADF and KPSS: if ADF rejects + KPSS fails to reject → stationary
                          if both reject → likely non-stationary
```

---

## 2. ACF, PACF, and Model Identification

**Autocovariance function (ACVF)**:
```
  γ(k) = Cov(x_t, x_{t+k}) = E[(x_t - μ)(x_{t+k} - μ)]
```

**Autocorrelation function (ACF)**:
```
  ρ(k) = γ(k) / γ(0)  ∈ [-1, 1]
```

**Partial autocorrelation function (PACF)**: correlation between x_t and x_{t+k} after removing the linear effect of x_{t+1},...,x_{t+k-1}.

**Model identification rules**:
```
  Process      ACF pattern          PACF pattern
  ──────────   ────────────────     ──────────────────────
  AR(p)        Tails off (exp decay) Cuts off after lag p
  MA(q)        Cuts off after lag q  Tails off
  ARMA(p,q)    Tails off             Tails off
  White noise  No significant lags   No significant lags

  "Cuts off" = drops abruptly to zero
  "Tails off" = geometric/sinusoidal decay
```

**Ljung-Box Q-test**: tests H₀: ρ(1) = ρ(2) = ... = ρ(k) = 0 (no autocorrelation up to lag k):
```
  Q = n(n+2) Σ_{j=1}^k ρ̂(j)² / (n-j)  ~  χ²(k)  under H₀
```

---

## SQL Window Functions ↔ Time Series Operations

SQL window functions and time series operations are the same underlying computations
in different notations:

```
SQL (window function syntax)                  Time series / ARIMA notation
──────────────────────────────────────────    ──────────────────────────────────────────
LAG(x, 1) OVER (ORDER BY t)                  x_{t-1}  ← 1-period lag, B¹ x_t
LAG(x, k) OVER (ORDER BY t)                  x_{t-k}  ← k-period lag, Bᵏ x_t

x - LAG(x,1) OVER (ORDER BY t)               Δx_t = x_t - x_{t-1}  ← first difference
                                               (1-B) x_t  ← removes unit root

AVG(x) OVER (ORDER BY t ROWS BETWEEN         q-period centered moving average
  (q-1)/2 PRECEDING AND (q-1)/2 FOLLOWING)   ← MA(q) smoothing of the level

SUM(x) OVER (ORDER BY t ROWS UNBOUNDED       ← integration (inverse of differencing)
  PRECEDING)                                   If Δx_t = ε_t, then x_t = Σ_{s≤t} ε_s
                                               ARIMA d=1 reverses this

x - AVG(x) OVER (PARTITION BY month)         ← seasonal adjustment
                                               Remove additive seasonal component s(t)
                                               SARIMA's seasonal differencing (1-B^12)x_t

CORR(x, LAG(x,k))                           ← sample ACF at lag k: ρ̂(k)
OVER (ORDER BY t)

AVG(x * LAG(x,k))                           ← sample ACVF at lag k: γ̂(k)
OVER (ORDER BY t)

SUM(x * LAG(x,k)) / SUM(x * x)              ← OLS coefficient in AR(k) regression
```

**Practical translation**: a data engineer who writes rolling window features
in SQL (`AVG() OVER ROWS BETWEEN k PRECEDING AND CURRENT ROW`) is computing
the same MA(k) smoothing that ARIMA's MA component models as a likelihood-based
process. The difference: SQL computes the smoothed value; ARIMA models the residual
structure of the *original* series after removing that structure.

---

## 3. ARIMA

**AR(p)** (AutoRegressive):
```
  x_t = φ₁x_{t-1} + ... + φₚx_{t-p} + ε_t

  Stationarity: characteristic polynomial Φ(z) = 1 - φ₁z - ... - φₚzᵖ
  must have all roots outside the unit circle |z| > 1
```

**MA(q)** (Moving Average):
```
  x_t = ε_t + θ₁ε_{t-1} + ... + θqε_{t-q}

  Always stationary. Invertibility: roots of Θ(z) = 1 + θ₁z + ... + θqzq outside unit circle.
```

**ARMA(p,q)**:
```
  Φ(B) x_t = Θ(B) ε_t

  Φ(B) = 1 - φ₁B - ... - φₚBᵖ   (AR polynomial)
  Θ(B) = 1 + θ₁B + ... + θqBq   (MA polynomial)
```

**ARIMA(p,d,q)**:
```
  Φ(B)(1-B)^d x_t = Θ(B) ε_t

  d = order of differencing to achieve stationarity
  d=1: random walk with drift; d=2: accelerating trend
```

**SARIMA(p,d,q)(P,D,Q)_s**: adds seasonal AR and MA operators at period s (s=12 for monthly):
```
  Φ(B)Φ_s(B^s)(1-B)^d(1-B^s)^D x_t = Θ(B)Θ_s(B^s) ε_t
```

**Box-Jenkins methodology**:
1. Identify d via ADF/KPSS and ACF
2. Identify p, q via ACF/PACF pattern
3. Estimate via MLE
4. Diagnose residuals (Ljung-Box, histogram)
5. Forecast with prediction intervals

**Information criteria for model selection**:
```
  AIC = -2 log L̂ + 2(p+q+d+1)      ← penalizes complexity (prediction)
  BIC = -2 log L̂ + log(n)(p+q+d+1)  ← heavier penalty (model selection)
```

---

## 4. Vector Autoregression (VAR)

For k-dimensional time series xₜ ∈ ℝᵏ:

```
  VAR(p):  xₜ = Σ_{j=1}^p Aⱼ xₜ₋ⱼ + εₜ

  Aⱼ ∈ ℝ^{k×k} are coefficient matrices
  εₜ ~ N(0, Σ)  white noise with k×k covariance matrix

  Stationarity: companion matrix has all eigenvalues inside unit circle
```

**Granger causality**: X Granger-causes Y if past values of X help predict Y beyond past Y alone.
```
  Test: F-test of whether Aⱼ[y,x] = 0 for all j in restricted VAR
  Note: Granger causality ≠ true causality (still correlation-based)
```

**Impulse Response Functions (IRF)**: how does xₜ₊ₕ respond to a one-unit shock to xₜ?
```
  VMA(∞) representation: xₜ = Σ_{h=0}^∞ Ψₕ εₜ₋ₕ
  IRF: ∂xₜ₊ₕ/∂εₜ = Ψₕ

  Orthogonalized IRF (Cholesky decomposition): identify structural shocks
```

**Cointegration**: two I(1) series are cointegrated if ∃ β such that βᵀxₜ is stationary. The series share a long-run equilibrium.

**VECM (Vector Error Correction Model)**: VAR reparameterization for cointegrated systems:
```
  Δxₜ = Π xₜ₋₁ + Σ_{j=1}^{p-1} Γⱼ Δxₜ₋ⱼ + εₜ

  Π = αβᵀ,  rank(Π) = r = # cointegrating relations
  α = adjustment speeds, β = cointegrating vectors

  Johansen test for cointegrating rank r.
```

---

## 5. GARCH — Modeling Conditional Variance

Financial time series: returns are roughly uncorrelated but variance clusters.

**ARCH(q)** (Engle 1982):
```
  εₜ = σₜ zₜ,  zₜ ~iid N(0,1)
  σ²ₜ = ω + Σ_{i=1}^q αᵢ ε²ₜ₋ᵢ

  Variance depends on past squared residuals.
  Large |εₜ₋₁| → large σ²ₜ → volatility clustering
```

**ARCH LM test**: Lagrange Multiplier test for H₀: α₁=...=αq=0 in ARCH regression.

**GARCH(p,q)** (Bollerslev 1986):
```
  σ²ₜ = ω + Σ_{i=1}^q αᵢ ε²ₜ₋ᵢ + Σ_{j=1}^p βⱼ σ²ₜ₋ⱼ

  GARCH(1,1) is the workhorse:
  σ²ₜ = ω + α ε²ₜ₋₁ + β σ²ₜ₋₁

  Stationarity: α + β < 1
  Unconditional variance: σ² = ω/(1 - α - β)
  Persistence: α + β ≈ 0.97 typical in financial data (long memory in volatility)
```

**VMA(∞) representation of GARCH**:
```
  GARCH(1,1): σ²ₜ = ω/(1-β) + α Σ_{k=0}^∞ βᵏ ε²ₜ₋₁₋ₖ

  → σ² is exponentially weighted average of past squared residuals
  → reduces to EWMA (RiskMetrics) when ω=0, α+β=1
```

**Extensions**:
```
  EGARCH (Nelson):  log σ²ₜ = ω + β log σ²ₜ₋₁ + α|zₜ₋₁| + γ zₜ₋₁
    γ < 0 = leverage effect (negative returns → higher volatility)

  GJR-GARCH:  σ²ₜ = ω + (α + γ 1{εₜ₋₁<0}) ε²ₜ₋₁ + β σ²ₜ₋₁
    Asymmetric: different response to positive vs negative shocks

  DCC-GARCH: Dynamic Conditional Correlation — multivariate extension
```

---

## 6. State Space Models and the Kalman Filter

State space representation unifies many time series models.

**General linear state space model**:
```
  State transition:    xₜ = Fxₜ₋₁ + Buₜ + Qε^x_t,   ε^x ~ N(0,I)
  Observation:         yₜ = Hxₜ + Ruₜ + Rε^y_t,       ε^y ~ N(0,I)

  x_t ∈ ℝⁿ: latent state (unobserved)
  y_t ∈ ℝᵐ: observation (observed)
  F: state transition matrix
  H: observation matrix (maps state to observation)
  Q: process noise covariance
  R: observation noise covariance
```

### Kalman Filter Derivation

**Setup**: Gaussian prior + Gaussian likelihood → Gaussian posterior (conjugacy).

At each time step, we maintain: `p(xₜ | y₁:ₜ) = N(xₜ; μₜ, Σₜ)` — Gaussian posterior.

**Predict step** (propagate state forward):
```
  Prior:   p(xₜ | y₁:ₜ₋₁) = N(μₜ|ₜ₋₁, Σₜ|ₜ₋₁)

  μₜ|ₜ₋₁ = F μₜ₋₁

  Σₜ|ₜ₋₁ = F Σₜ₋₁ Fᵀ + Q
             ↑           ↑
           state       process
           propagation  noise
```

**Update step** (condition on new observation yₜ):
```
  Innovation:   νₜ = yₜ - H μₜ|ₜ₋₁           (predicted vs actual observation)
  Innovation cov: Sₜ = H Σₜ|ₜ₋₁ Hᵀ + R
  Kalman gain:  Kₜ = Σₜ|ₜ₋₁ Hᵀ Sₜ⁻¹

  Posterior mean:  μₜ = μₜ|ₜ₋₁ + Kₜ νₜ
  Posterior cov:   Σₜ = (I - Kₜ H) Σₜ|ₜ₋₁      (Joseph form: more numerically stable)
                   Σₜ = (I - Kₜ H) Σₜ|ₜ₋₁ (I - Kₜ H)ᵀ + Kₜ R Kₜᵀ
```

**Derivation from Bayes**:
```
  p(xₜ | y₁:ₜ) ∝ p(yₜ | xₜ) p(xₜ | y₁:ₜ₋₁)

  Both Gaussian:
    p(yₜ|xₜ) = N(Hxₜ, R)
    p(xₜ|y₁:ₜ₋₁) = N(μₜ|ₜ₋₁, Σₜ|ₜ₋₁)

  Product of Gaussians in xₜ → complete the square → Kalman update formulas
```

**RTS Smoother** (Rauch-Tung-Striebel): backward pass, computes `p(xₜ | y₁:T)` using all observations:
```
  Backward gain: Cₜ = Σₜ Fᵀ Σₜ₊₁|ₜ⁻¹
  Smoother mean: μₜ|T = μₜ + Cₜ(μₜ₊₁|T - μₜ₊₁|ₜ)
  Smoother cov:  Σₜ|T = Σₜ + Cₜ(Σₜ₊₁|T - Σₜ₊₁|ₜ)Cₜᵀ
```

**Parameter estimation**: EM algorithm
- E-step: run Kalman filter + RTS smoother
- M-step: update F, H, Q, R to maximize expected log-likelihood
- Closed-form M-step for Gaussian linear SSM

**ARIMA as state space**: any ARIMA model can be written as a state space model:
```
  AR(p): F is companion matrix, H = [1,0,...,0]
  Enables: missing data, time-varying parameters, irregularly spaced observations
```

---

## 7. Spectral Analysis

**Wiener-Khinchin theorem**: for stationary xₜ, the spectral density is the Fourier transform of the ACVF:
```
  f(ω) = Σ_{k=-∞}^∞ γ(k) e^{-iωk}   for ω ∈ [-π, π]
  γ(k) = (1/2π) ∫ f(ω) e^{iωk} dω

  Total variance: Var(xₜ) = γ(0) = (1/2π) ∫ f(ω) dω
  → f(ω)dω is the variance contribution from frequency ω
```

**Periodogram** (sample spectral density):
```
  Î(ω) = (1/n)|Σₜ xₜ e^{-iωt}|²   ← DFT magnitude squared

  Not a consistent estimator of f(ω) (variance doesn't decrease with n)
  Smooth it: Welch's method (average over overlapping windowed periodograms)
```

**HP Filter** (Hodrick-Prescott): decompose series into trend + cycle:
```
  min_{τₜ} [Σₜ(xₜ - τₜ)² + λ Σₜ(Δ²τₜ)²]
  ← goodness of fit       ← smoothness of trend

  λ=1600 (quarterly), λ=100 (annual), λ=129600 (monthly)
  Frequency domain: HP filter passes low frequencies (trend), blocks high (cycle)
```

---

## 8. Modern Methods

### Prophet (Taylor & Letham, Facebook 2017)
```
  y(t) = g(t) + s(t) + h(t) + ε_t
    g(t): trend (piecewise linear or logistic growth with changepoints)
    s(t): seasonality (Fourier series)
    h(t): holidays (custom effects)
    ε: noise

  Changepoints: automatic detection or manually specified
  Stan backend: fast MAP estimation
  Strength: interpretable decomposition, handles missing data, business seasonality
  Weakness: pure extrapolation, no exogenous features in base model
```

### N-BEATS (Neural Basis Expansion, Oreshkin et al. 2019)
```
  Pure ML approach: no explicit time series assumptions
  Stack of "blocks", each producing:
    - backcast: prediction of input window (subtracted = residual for next block)
    - forecast: prediction of target window

  Interpretable version: basis expansion (trend + seasonality Fourier basis)
  Generic version: fully learned basis
```

### TFT (Temporal Fusion Transformer, Lim et al. 2019)
```
  Multi-horizon probabilistic forecasting with:
    - LSTM encoder for local temporal patterns
    - Attention for long-range dependencies
    - Variable selection network (which features matter when)
    - Quantile outputs (prediction intervals)

  Handles: known future inputs (day of week), static metadata (store ID),
           past observed inputs (sales history)
```

### DeepAR (Amazon, 2017)
```
  Probabilistic forecasting: learn p(yₜ | y₁:ₜ₋₁, x₁:T)
  Model: LSTM-based autoregressive model
  Output: parameters of likelihood (Gaussian or negative binomial)
  Train across many related time series (global model)
  At inference: ancestral sampling for prediction intervals
```

---

## Python Tooling Stack

```
Theory concept               Python library / class                  Notes
──────────────────────────   ─────────────────────────────────────   ────────────────────
ARIMA, SARIMA                statsmodels.tsa.arima.model.ARIMA       Standard; auto_arima
SARIMAX (with exog.)         statsmodels.tsa.statespace.SARIMAX      Exogenous regressors
VAR                          statsmodels.tsa.vector_ar.var_model.VAR
VECM                         statsmodels.tsa.vector_ar.vecm.VECM
Kalman filter / SSM          statsmodels.tsa.statespace.MLEModel      Base class + EM
                             PyKalman (simple), FilterPy              Numpy-based
                             Dynamax (JAX-based)                     GPU, autodiff
GARCH, EGARCH, DCC           arch.arch_model (arch library)          Bollerslev models
                             arch.univariate / arch.multivariate
ADF, KPSS tests              statsmodels.tsa.stattools.adfuller       Unit root tests
                             statsmodels.tsa.stattools.kpss
Ljung-Box Q-test             statsmodels.stats.diagnostic.acorr_ljungbox
ACF / PACF plots             statsmodels.graphics.tsaplots.plot_acf
                             statsmodels.graphics.tsaplots.plot_pacf

Prophet                      prophet.Prophet (Facebook/Meta)         Decomposition model
                             neuralprophet (Neural Prophet)          PyTorch backend

sktime                       sktime.forecasting.*                    sklearn-compatible
                             ARIMA, ETS, Theta, naive, ensemble      fit/predict API
                             sktime.transformations.series.*         preprocessing
                             sktime.classification / regression      time series as feature

darts                        darts.models.*                          TorchForecastingModel
                             TCN, NBEATS, TFT, DeepAR, N-HiTS       deep learning focus
                             darts.datasets                          benchmark datasets

tslearn                      tslearn.clustering.*                    Dynamic Time Warping
                             tslearn.metrics.dtw                     time series similarity
                             TimeSeriesKMeans, TimeSeriesKNN

GluonTS                      gluonts.model.*                         Amazon probabilistic
                             DeepAR, Transformer, Wavenet            forecasting framework

Statsmodels vs pandas:
  pandas resample("W").mean()       ← quick aggregation (not a model)
  statsmodels SARIMAX               ← full likelihood estimation, tests, confidence intervals
  Use pandas for feature engineering; statsmodels/arch for model estimation.
```

**Quick selection**:
```
Need classical ARIMA/SARIMA/VAR with inference?  → statsmodels.tsa
Need GARCH family with full diagnostics?          → arch library
Need sklearn-compatible API for pipelines?        → sktime
Need deep learning forecasting (probabalistic)?   → darts (TFT, DeepAR, N-HiTS)
Need interpretable decomposition (business)?      → prophet
Need DTW / time series classification?            → tslearn
Need cross-sectional + temporal (panel)?          → statsmodels.tsa.statespace (mixed effects SSM)
```

---

## 9. Decision Cheat Sheet

| Scenario | Method | Why |
|----------|--------|-----|
| Univariate, stationary | ARMA | Classical, interpretable |
| Univariate, trending/seasonal | ARIMA, SARIMA | Differencing handles nonstationarity |
| Multivariate, VAR-order | VAR | Captures lead-lag relationships |
| Cointegrated multivariate | VECM | Preserves long-run equilibrium |
| Financial volatility | GARCH(1,1) | Volatility clustering |
| Asymmetric volatility | GJR-GARCH, EGARCH | Leverage effect |
| Missing data, latent state | Kalman filter (SSM) | Principled Bayesian filtering |
| Trend + seasonality + holidays | Prophet | Interpretable, fast |
| Many related series | DeepAR | Global model, probabilistic |
| Multi-horizon with covariates | TFT | Handles mixed input types |

---

## 10. Common Confusion Points

1. **"Differencing removes all nonstationarity"** — Differencing removes unit roots (I(1) → I(0)). It doesn't fix heteroskedasticity (GARCH), seasonality (need seasonal differencing), or structural breaks. Over-differencing (too many differences) can introduce MA components.

2. **"Granger causality is causality"** — Granger causality is predictive: X Granger-causes Y if X helps predict Y. It's not Pearl causation (do-calculus). A common cause Z can make X Granger-cause Y spuriously.

3. **"Kalman filter requires Gaussian noise"** — The Kalman filter is the optimal linear estimator regardless of distribution. It's the optimal Bayes estimator only under Gaussianity. For non-Gaussian noise: particle filters (sequential Monte Carlo) extend this.

4. **"ARIMA forecasts should be very accurate"** — ARIMA forecasts are optimal in the sense of minimum MSE linear prediction. But for long horizons, they revert to the unconditional mean (for stationary series). Uncertainty grows rapidly.

5. **"ACF cuts off = MA, PACF cuts off = AR"** — The standard identification rule. But in practice, neither ACF nor PACF "cleanly" cuts off with real data. Use information criteria (AIC/BIC) for automated selection.

6. **"GARCH models the conditional variance, so σ²ₜ is the variance of the process"** — σ²ₜ is the conditional variance given past information. The unconditional variance σ² = ω/(1-α-β) is constant for stationary GARCH. The conditional variance varies.

7. **"Stationarity means the series looks flat"** — Stationarity means constant mean and autocovariance structure. A stationary series can have substantial volatility (GARCH) and complex autocorrelation structure. "Flat-looking" is neither necessary nor sufficient.
