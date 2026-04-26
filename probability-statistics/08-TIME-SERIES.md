# Time Series Analysis

## The Big Picture

Time series analysis handles data where observations are ordered in time and may be serially dependent — violating the i.i.d. assumption of classical statistics.

```
+------------------------------------------------------------------+
|                     TIME SERIES LANDSCAPE                        |
+------------------------------------------------------------------+
|                                                                  |
|  DECOMPOSITION                                                   |
|  Y_t = Trend + Seasonality + Cycle + Irregular                  |
|       (deterministic or stochastic components)                  |
|                                                                  |
|  STATIONARY MODELS              NON-STATIONARY                  |
|  +-------------------+         +-------------------+            |
|  | AR(p): Y_t depends|         | ARIMA: difference |            |
|  | on past Y values  |         | to achieve        |            |
|  | MA(q): Y_t depends|         | stationarity      |            |
|  | on past errors    |         | Seasonal ARIMA    |            |
|  | ARMA(p,q): both   |         | Unit root tests   |            |
|  +-------------------+         +-------------------+            |
|                                                                  |
|  SPECTRAL DOMAIN                STATE SPACE / KALMAN            |
|  +-------------------+         +-------------------+            |
|  | Fourier analysis  |         | Latent state model |           |
|  | Periodogram       |         | Optimal filtering |            |
|  | Spectral density  |         | Prediction,       |            |
|  | Cross-spectrum    |         | smoothing         |            |
|  +-------------------+         +-------------------+            |
|                                                                  |
|  MULTIVARIATE: VAR, VECM, DLM (Dynamic Linear Models)          |
+------------------------------------------------------------------+
```

---

## Stationarity

**Strict stationarity**: The joint distribution of (Y_t, Y_{t+1}, ..., Y_{t+k}) is the same for all t and all k.

**Weak (covariance) stationarity**:

```
  E[Y_t] = mu                    (constant mean)
  Var[Y_t] = sigma^2             (constant variance)
  Cov(Y_t, Y_{t+h}) = gamma(h)  (covariance depends only on lag h)

  This is the practically relevant form.
  Most time series models target weak stationarity.
```

**Autocovariance and autocorrelation functions**:

```
  ACVF: gamma(h) = Cov(Y_t, Y_{t+h})
  ACF:  rho(h) = gamma(h) / gamma(0) = Cov(Y_t, Y_{t+h}) / Var(Y_t)

  Properties: rho(0) = 1, |rho(h)| <= 1, rho(-h) = rho(h)

  PACF (Partial ACF): partial correlation between Y_t and Y_{t+h}
  after controlling for Y_{t+1}, ..., Y_{t+h-1}.
  PACF(h) = Corr(Y_t - P_{t|t-1,...,t-h+1} Y_t, Y_{t+h} - P_{t+h|t+1,...,t+h-1} Y_{t+h})

  ACF and PACF patterns identify AR/MA order:
  AR(p):   ACF decays geometrically, PACF cuts off after lag p
  MA(q):   ACF cuts off after lag q, PACF decays geometrically
  ARMA:    Both decay geometrically
```

---

## ARMA Models

**AR(p) — Autoregressive**:

```
  Y_t = phi_1 Y_{t-1} + ... + phi_p Y_{t-p} + epsilon_t
  epsilon_t ~ WN(0, sigma^2)  (white noise: uncorrelated, mean 0, constant variance)

  Characteristic polynomial: phi(z) = 1 - phi_1 z - ... - phi_p z^p
  STATIONARITY CONDITION: all roots of phi(z) outside the unit circle.

  AR(1) example: Y_t = phi Y_{t-1} + epsilon_t
  Stationary iff |phi| < 1.
  ACF: rho(h) = phi^h  (geometric decay)
  PACF: cuts off after lag 1.
```

**MA(q) — Moving Average**:

```
  Y_t = epsilon_t + theta_1 epsilon_{t-1} + ... + theta_q epsilon_{t-q}

  Always stationary (finite sum of white noise).
  INVERTIBILITY CONDITION: roots of theta(z) = 1 + theta_1 z + ... + theta_q z^q
  outside the unit circle. Ensures unique MA representation.

  MA(1) example: Y_t = epsilon_t + theta epsilon_{t-1}
  ACF: rho(1) = theta/(1+theta^2), rho(h) = 0 for h > 1.
  PACF: decays geometrically.
```

**ARMA(p,q)**:

```
  phi(B) Y_t = theta(B) epsilon_t
  B = backshift operator: B Y_t = Y_{t-1}

  phi(B) = 1 - phi_1 B - ... - phi_p B^p
  theta(B) = 1 + theta_1 B + ... + theta_q B^q

  Stationarity: roots of phi(z) outside unit circle.
  Invertibility: roots of theta(z) outside unit circle.
```

---

## ARIMA and Non-Stationarity

**Unit root**: phi(z) = 0 has a root at z=1. The process has a "stochastic trend" — it wanders without returning to a fixed mean.

```
  Random walk: Y_t = Y_{t-1} + epsilon_t  (unit root, non-stationary)
  Var(Y_t) = t * sigma^2  (grows without bound)

  Differencing removes unit roots:
  DeltaY_t = Y_t - Y_{t-1}  (first difference)
  Delta^2 Y_t = DeltaY_t - DeltaY_{t-1}  (second difference)

  Most economic/financial time series: stationary after first differencing (I(1))
  Some require second differencing (I(2)): uncommon in practice
```

**ARIMA(p,d,q)**: Apply d rounds of differencing to make stationary, then fit ARMA(p,q):

```
  phi(B)(1-B)^d Y_t = theta(B) epsilon_t

  d=0: ARMA (already stationary)
  d=1: common for trending series
  d=2: very unusual
```

**SARIMA(p,d,q)(P,D,Q)_m**: Adds seasonal AR, differencing, and MA components at lag m:

```
  phi(B) Phi(B^m) (1-B)^d (1-B^m)^D Y_t = theta(B) Theta(B^m) epsilon_t

  Example: Monthly data with annual seasonality: m=12
  SARIMA(1,1,1)(1,1,1)_12 is a common model for monthly economic data.
```

**Unit root tests**:

```
  Augmented Dickey-Fuller (ADF):
  H_0: unit root present (non-stationary)
  H_1: no unit root (stationary)
  Regression: DeltaY_t = alpha + beta t + gamma Y_{t-1} + Sum delta_k DeltaY_{t-k} + epsilon_t
  t-statistic for gamma has non-standard (Dickey-Fuller) distribution.

  KPSS test: reverses the hypotheses
  H_0: trend stationary, H_1: unit root
  Useful as complement to ADF (different type I/II error structure)

  Phillips-Perron: non-parametric correction for serial correlation.
```

---

## Spectral Analysis

The time domain (autocorrelations) and frequency domain (spectral density) are dual representations.

**Spectral density**: For a stationary process with ACVF gamma(h):

```
  f(omega) = Sum_{h=-inf}^{inf} gamma(h) e^{-i omega h}

  = Sum_h gamma(h) cos(omega h)   (since gamma symmetric and real)

  Inverse: gamma(h) = (1/2pi) Integral_{-pi}^{pi} f(omega) e^{i omega h} d_omega

  f(omega) >= 0 for all omega (it's a power spectral density).
  Integral_{-pi}^{pi} f(omega) d_omega = 2 pi * Var(Y)

  Interpretation: f(omega) measures variance attributable to
  oscillations at frequency omega (cycles per time unit).
```

**Spectral densities of common models**:

```
  White noise: f(omega) = sigma^2 / (2pi)   (flat — all frequencies equal)
  AR(1), phi > 0: peaks near omega=0 (low frequency, trending)
  AR(1), phi < 0: peaks near omega=pi (high frequency, oscillating)
  MA(1): f(omega) = sigma^2/(2pi) |1 + theta e^{-i omega}|^2
```

**Periodogram** (sample estimate of spectral density):

```
  I_n(omega_j) = (1/n) |Sum_t Y_t e^{-i omega_j t}|^2

  omega_j = 2 pi j / n  (Fourier frequencies)

  I_n(omega_j) is asymptotically UNBIASED for f(omega_j)
  but NOT consistent (variance doesn't shrink).

  SOLUTION: Smooth the periodogram (kernel smoothing, Welch's method).
```

**Applications**: Detect seasonality (peaks at frequency 1/12 for monthly, 1/7 for daily). Identify dominant cycles. Design filters to remove seasonality or noise.

---

## State Space Models and Kalman Filter

State space models (SSMs) are general and subsume ARIMA, structural time series, and multivariate models.

**Linear Gaussian State Space Model**:

```
  STATE EQUATION:
  alpha_{t+1} = T_t alpha_t + R_t eta_t,   eta_t ~ Normal(0, Q_t)

  OBSERVATION EQUATION:
  y_t = Z_t alpha_t + epsilon_t,            epsilon_t ~ Normal(0, H_t)

  alpha_t = d-dimensional latent state (not observed)
  y_t     = p-dimensional observation
  T_t, Z_t, R_t, H_t, Q_t = model matrices (may depend on t)
  eta_t and epsilon_t are independent.
```

**Kalman Filter** (optimal recursive state estimation):

```
  PREDICTION STEP:
  a_{t|t-1} = T_t a_{t-1}                     (predicted state mean)
  P_{t|t-1} = T_t P_{t-1} T_t^T + R_t Q_t R_t^T  (predicted state variance)

  UPDATE STEP:
  v_t = y_t - Z_t a_{t|t-1}                   (innovation = actual - predicted)
  F_t = Z_t P_{t|t-1} Z_t^T + H_t             (innovation variance)
  K_t = P_{t|t-1} Z_t^T F_t^{-1}              (Kalman gain)
  a_t = a_{t|t-1} + K_t v_t                   (updated state estimate)
  P_t = (I - K_t Z_t) P_{t|t-1}               (updated state variance)

  The Kalman gain K_t balances: how uncertain is the state vs. observation.
  K_t -> 0: trust the prediction (observation is noisy)
  K_t -> I: trust the observation (state prediction is uncertain)
```

**Kalman smoother**: The filter gives E[alpha_t | y_1,...,y_t]. Smoothing gives E[alpha_t | y_1,...,y_T] — using ALL data. Uses backward pass after forward filter.

**Log-likelihood** (for MLE of model parameters):

```
  log L = -(1/2) Sum_t [log |F_t| + v_t^T F_t^{-1} v_t]

  Innovations v_t are the natural residuals.
  Parameters estimated by maximizing log L (numerical optimization).
```

**ARIMA as state space**: Any ARIMA(p,d,q) can be written as a state space model. This enables:
- Exact likelihood (vs. approximate conditional likelihood for ARMA)
- Handling missing data naturally
- Extension to structural models (trend + seasonal + irregular)
- Extension to multivariate models

**Universal bridges for the Kalman filter:**

```
  KALMAN = OPTIMAL BAYESIAN FILTER for linear-Gaussian state space:
  Prior: p(alpha_t | y_{1:t-1}) = Normal(a_{t|t-1}, P_{t|t-1})
  Likelihood: p(y_t | alpha_t) = Normal(Z_t alpha_t, H_t)
  Posterior: p(alpha_t | y_{1:t}) = Normal(a_t, P_t)
  The prediction/update steps are Bayes' theorem for conjugate Normal.
  Connection: 06-BAYESIAN-STATISTICS (conjugate Normal updating).

  KALMAN = RECURSIVE LEAST SQUARES (RLS):
  For a static regression Y = X beta + epsilon with streaming data:
  The Kalman filter with T = I, R = 0 reduces to RLS.
  beta_t = beta_{t-1} + K_t (y_t - z_t^T beta_{t-1})
  K_t = P_{t-1} z_t / (z_t^T P_{t-1} z_t + sigma^2)
  Connection: 07-REGRESSION-MODELS (OLS as a special case of Kalman).
```

**Connection to Azure Data Factory**: Time series state space models appear in data pipeline monitoring — anomaly detection in telemetry is often a Kalman filter / LSTM hybrid. The innovation sequence v_t is the anomaly signal.

---

## GARCH and Volatility Models

For financial time series: variance clustering (periods of high/low volatility).

```
  ARCH(q) — Autoregressive Conditional Heteroscedasticity:
  Y_t = sigma_t epsilon_t,   epsilon_t ~ i.i.d. Normal(0,1)
  sigma_t^2 = alpha_0 + alpha_1 Y_{t-1}^2 + ... + alpha_q Y_{t-q}^2

  GARCH(p,q) (Generalized ARCH):
  sigma_t^2 = alpha_0 + Sum_i alpha_i Y_{t-i}^2 + Sum_j beta_j sigma_{t-j}^2

  GARCH(1,1) is ubiquitous in practice:
  sigma_t^2 = omega + alpha Y_{t-1}^2 + beta sigma_{t-1}^2
  alpha + beta < 1 for stationarity.
  alpha + beta close to 1: "volatility persistence" (common in equities).
```

---

## Model Selection and Forecasting

**Information criteria for model order selection**:

```
  AIC = -2 log L + 2k     (k = number of parameters)
  BIC = -2 log L + k log n  (stronger penalty for large n)

  Select ARIMA order (p, d, q) by minimizing AIC or BIC.
  auto.arima() in R's forecast package does this automatically.
```

**Forecast evaluation**:

```
  In-sample fit (overfitting risk) vs. out-of-sample forecast accuracy.

  ROLLING ORIGIN / EXPANDING WINDOW CV:
  Train on t=1,...,T1, predict t=T1+1,...,T1+h
  Train on t=1,...,T1+1, predict t=T1+2,...,T1+h+1
  ...

  Metrics:
  MAE = Mean Absolute Error
  RMSE = Root Mean Squared Error
  MAPE = Mean Absolute Percentage Error (problematic for near-zero values)
  MASE = Mean Absolute Scaled Error (relative to naive forecast)
```

---

## Decision Cheat Sheet

| Situation | Method | Notes |
|---|---|---|
| Stationary, short memory | ARMA(p,q) | Use AIC/BIC for order |
| Non-stationary, trending | ARIMA(p,1,q) | ADF test first |
| Seasonality present | SARIMA | m = season length |
| Irregular seasonality | STL + ETS | Loess-based decomposition |
| Missing data | State space / Kalman | Handles gaps naturally |
| Multivariate time series | VAR(p) | Vector autoregression |
| Volatility clustering (finance) | GARCH(1,1) | Financial returns |
| Latent structure | State space model | Flexible, subsumes ARIMA |
| Long-range dependence | ARFIMA | Fractional differencing |

**Long memory and ARFIMA**: Fractional integration (1−B)^d with d ∈ (0, 0.5) produces long-range dependence — autocorrelations that decay as a power law γ(h) ~ h^{2d−1} rather than exponentially. The Hurst exponent H = d + 0.5 characterizes the memory: H = 0.5 for short memory, H > 0.5 for long memory (persistent), H < 0.5 for anti-persistent. ARFIMA(p,d,q) fits when ACF decays hyperbolically — common in internet traffic, volatility, and hydrology. Use ARFIMA over ARIMA when the ACF decays too slowly for any ARMA and the series is not unit-root non-stationary.

**Cointegration and VECM**: When multiple I(1) series share a common stochastic trend, their linear combination may be stationary — this is cointegration. The Vector Error Correction Model (VECM) captures both the short-run dynamics and the long-run equilibrium relationship. Test for cointegration via Johansen's trace test. Application: exchange rates, interest rate spreads, pairs trading.

---

## Common Confusion Points

**"ACF shows correlation between Y_t and Y_{t+h} — that is all I need."**
The ACF confounds direct effects (AR part) with indirect effects. The PACF removes the indirect effects by controlling for intermediate lags. Use both: ACF for MA order, PACF for AR order.

**"The Kalman filter gives the distribution of the state."**
For Linear Gaussian state space, yes: the filtered distribution is Gaussian with mean a_t and variance P_t. For non-linear, non-Gaussian models, you need extended Kalman filter (first-order linearization) or particle filters (sequential Monte Carlo) which give sample approximations.

**"Forecasting the mean is sufficient."**
For risk management, the forecast interval (quantile) matters as much as the mean. GARCH models the time-varying variance; prediction intervals should widen during high-volatility periods. Forecasting only the mean misses this.

**"A stationary time series is predictable."**
Stationarity says the distribution doesn't change over time, not that the series is predictable. A white noise process is stationary and completely unpredictable. The ACF structure (memory) determines predictability.
