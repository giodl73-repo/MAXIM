---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `signal-processing/04-CONVOLUTION-CORRELATION.md`
- `signal-processing/05-Z-TRANSFORM.md`
- `signal-processing/06-STOCHASTIC-SIGNALS.md`
- `signal-processing/07-SPECTRAL-ESTIMATION.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
task/method and situation/tool selector tables. Current Certified Gold requires
diagnostic reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `signal-processing/04-CONVOLUTION-CORRELATION.md` | Rebuilt the task/method table around FIR length, streaming blocks, FFT convolution, matched filtering, delay, energy, periodicity, and 2D filtering caveats. |
| `signal-processing/05-Z-TRANSFORM.md` | Rebuilt the Z-transform table around stability, frequency response, notch filters, resonators, difference equations, and IIR implementation. |
| `signal-processing/06-STOCHASTIC-SIGNALS.md` | Rebuilt the stochastic signals table around PSD, autocorrelation, filtered noise, coherence, delay, thermal noise, stationarity, and finite-data PSD estimates. |
| `signal-processing/07-SPECTRAL-ESTIMATION.md` | Rebuilt the spectral estimation table around Welch, multitaper, AR methods, MUSIC/ESPRIT, model order, Goertzel, and time-frequency processing. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- signal-processing\04-CONVOLUTION-CORRELATION.md signal-processing\05-Z-TRANSFORM.md signal-processing\06-STOCHASTIC-SIGNALS.md signal-processing\07-SPECTRAL-ESTIMATION.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml signal-processing\04-CONVOLUTION-CORRELATION.md signal-processing\05-Z-TRANSFORM.md signal-processing\06-STOCHASTIC-SIGNALS.md signal-processing\07-SPECTRAL-ESTIMATION.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

