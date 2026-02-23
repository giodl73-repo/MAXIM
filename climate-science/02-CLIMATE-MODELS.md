# 02 — Climate Models

## Model Hierarchy, GCMs, Parameterization, Ensemble Methods, Uncertainty

> **STUB** — outline only, content to be authored

**Planned coverage:**
- Model hierarchy: Energy Balance Models (EBMs — 0D/1D, analytical insight), Radiative-Convective Models (vertical column), Regional Climate Models (RCMs — dynamical downscaling), GCMs (coupled atmosphere-ocean), Earth System Models (ESMs — add biogeochemistry/land surface/ice sheets)
- GCM architecture: horizontal resolution (~50-100km typical, ~25km high-res), ~30-60 vertical levels, time step ~20-30 minutes, components — Atmospheric GCM (AGCM) + Ocean GCM (OGCM) + Sea ice + Land surface model
- Dynamical core: primitive equations (hydrostatic approximation, spherical geometry), numerical methods (spectral/finite-difference/finite-volume), CFL stability condition, parallelization
- Parameterization: subgrid processes too small to resolve explicitly; convective parameterization (mass flux schemes — Arakawa/Schubert), cloud microphysics (droplet nucleation, precipitation), ocean mixing (Gent-McWilliams eddy parameterization), land surface (CABLE/CLM/JSBACH)
- Clouds as the main uncertainty: cloud radiative effect (CRE) — low clouds (SW cooling ~−47 W/m²), high clouds (LW warming ~+26 W/m²); cloud feedback sign uncertain; why ECS range is so wide
- Model validation: emergent constraints (observable relationships that constrain ECS), paleoclimate validation (LGM cooling, PETM warming), process-level evaluation
- CMIP (Coupled Model Intercomparison Project): CMIP6 ensemble, 40+ models, historical runs + ScenarioMIP (SSP1-2.6/2-4.5/3-7.0/5-8.5), model-as-truth reliability assessment
- Ensemble methods: multi-model ensemble (MME), initial-condition ensemble (internal variability), perturbed physics ensemble (structural uncertainty); model weighting; constrained projections
- Uncertainty sources: scenario uncertainty (policy choices), model uncertainty (structural), internal variability (chaotic atmosphere); partitioning uncertainty at different lead times
- Regional downscaling: dynamical (nested RCM) vs statistical (BCSD, delta method, quantile mapping); for impacts assessment requiring local projections
