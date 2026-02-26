# Electromagnetic Spectrum and Atmospheric Windows

## The Big Picture

Every remote sensing system exploits a specific region of the EM spectrum where: (1) the atmosphere is reasonably transparent, and (2) the surface emits or reflects enough energy to detect. Understanding which windows exist, what blocks them, and what physical process dominates each region is the physics foundation for everything else in remote sensing.

```
WAVELENGTH (log scale)

  UV       VISIBLE      NIR    SWIR  MIR   TIR     FIR  MICROWAVE   RADIO
  |          |    |      |       |    |     |        |       |         |
  0.1um   0.4 0.7um    1.3um  2.5um 4um   14um   1mm   10cm      1m
  |          +====+======+====+==+===+====+====+====+===+=========+
  |[XXXXX]   |    |      |    |  |   |    |    |    |   |         |
  |O3 blocks |VIS |  NIR |    |  SWIR|MIR |TIR |    |   MICRO    |
  |          |[1] | [2]  |    | [3]  | [4]| [5]|    |   [6]      |

 [X] = absorption / blocked by atmosphere
  =  = atmospheric window (transparent)

[1] Visible (0.4-0.7 um):  Blue (0.45), Green (0.55), Red (0.65)
[2] NIR (0.7-1.0 um):      Vegetation red edge, near-infrared plateau
[3] SWIR (1.0-2.5 um):     Two windows: 1.0-1.3 um and 1.5-1.8 um and 2.0-2.5 um
[4] MIR (3-5 um):          Hot fires, volcanoes. Transition zone solar/thermal
[5] TIR (8-14 um):         Land surface temperature. Emitted, not reflected
[6] Microwave (1mm-1m):    SAR, passive microwave. Penetrates cloud and rain
```

---

## Atmospheric Absorption: The Blocking Agents

The atmosphere is not uniformly transparent. Four gases dominate the absorption spectrum:

```
GAS         BANDS BLOCKED                              REMOTE SENSING IMPACT
---------------------------------------------------------------------------
Water (H2O) Strong: ~1.4 um, ~1.9 um, >2.5 um (SWIR) Major SWIR window gaps
            Continuum in TIR                           Dominates TIR absorption
            Variable (weather-dependent)               Requires real-time correction

CO2         Strong: 2.0 um, 4.3 um, 15 um            Blocks MIR; used for CO2
            Weaker: 1.4 um, 1.6 um                   monitoring by OCO-2 at 1.6 um

O3 (ozone)  UV: 0.2-0.32 um (Hartley band)           Stratospheric ozone blocks
            Visible: 0.6 um (Chappuis band, weak)     most UV from reaching surface
            TIR: 9.6 um                               9.6 um "ozone hole" in TIR

O2 (oxygen) 0.69 um, 0.76 um (A-band)               Narrow absorption features
            Strong: 0.13 um (Schumann-Runge)          Used for cloud-top pressure
```

The transmission spectrum that results is not smooth -- it is a complicated function of all four gases at once. What satellite sensor designers call "windows" are the gaps between these absorption features.

---

## Scattering: Three Regimes

Scattering redirects photons without absorbing them. The type of scattering depends on the ratio of the scatterer's size (r) to the wavelength (lambda):

```
SIZE PARAMETER x = 2*pi*r / lambda

  x << 1 (r << lambda):    RAYLEIGH SCATTERING
  x ~ 1  (r ~ lambda):     MIE SCATTERING
  x >> 1 (r >> lambda):    NON-SELECTIVE (GEOMETRIC) SCATTERING

+------------------+------------------+-------------------+
|  RAYLEIGH        |  MIE             |  NON-SELECTIVE    |
+------------------+------------------+-------------------+
| Scatterer: gas   | Scatterer:       | Scatterer: large  |
| molecules (N2,O2)| aerosols, haze   | droplets, dust    |
| r ~ 0.1-0.3 nm  | r ~ 0.1-10 um   | r >> 1 um         |
|                  |                  |                   |
| Wavelength dep:  | Wavelength dep:  | Wavelength dep:   |
| sigma ~ lambda^-4| sigma ~ lambda^-1| ~ independent     |
|                  |                  |                   |
| Blue sky:        | Hazy conditions: | Clouds, fog:      |
| scatters blue 16x| mutes color,     | scatter all       |
| more than red    | reduces contrast | wavelengths equal |
+------------------+------------------+-------------------+
```

**Rayleigh's lambda^-4 law** has a critical practical consequence: blue light (0.45 um) scatters ~5.5x more than red light (0.65 um) in the atmosphere. This means:
- Blue band imagery has more atmospheric path radiance than red/NIR
- Atmospheric correction effects are largest in the blue band
- For water color applications (ocean blue), atmospheric correction is the dominant source of error

---

## Atmospheric Windows: Detailed Breakdown

```
WINDOW      RANGE        DOMINANT PHYSICS        KEY SENSORS
----------------------------------------------------------------------
UV window   0.32-0.4 um  Surface UV, O3 Raman    Ozone sensors (OMI, TROPOMI)
                         scattering above ozone  Not used for Earth imaging

Visible     0.4-0.7 um   Solar reflection         All optical sensors
                         Rayleigh + Mie scatter   Blue: ocean color
                         Specular reflectance     Green: chlorophyll
                         from vegetation          Red: vegetation absorption

Red edge    0.68-0.75 um Sharp chlorophyll        Sentinel-2 B5/B6/B7
(transition)             absorption edge          WorldView vegetation index
                         -> NIR reflectance       Key for plant stress early detect

NIR         0.75-1.3 um  Solar reflection         Landsat B5, Sentinel B8
                         Cell wall scattering     NDVI red-NIR contrast
                         No chlorophyll absorb    Biomass estimation

SWIR-1      1.5-1.8 um   Solar reflection         Landsat B6, Sentinel B11
                         Liquid water absorption  Snow/ice distinction
                         at 1.4 (blocked) edges   Soil moisture (indirect)
                         Mineral absorption       Lithology mapping

SWIR-2      2.0-2.5 um   Solar reflection         Landsat B7, Sentinel B12
                         Clay mineral features    Hydrothermal mineral mapping
                         Carbonate features       Burn scar detection (NBR)
                         Cellulose absorption     Canopy water content

MIR/MWIR    3.5-5.0 um   CROSSOVER ZONE           Fire detection (MODIS B21/B22)
                         Solar + thermal both     VIIRS I4 band
                         contribute equally       Volcanic hot spots
                         Very sensitive to fire   Not used for reflectance

TIR         8-14 um      Planck emission          MODIS B31/B32, Landsat TIRS
                         from surface/atmos       ECOSTRESS, ASTER TIR
                         Emissivity differences   Land surface temperature
                         H2O + O3 absorb at edges Urban heat islands

Microwave   1mm-1m        Thermal emission         SSM/I, AMSR-2 (passive)
(passive)   (discrete     (weak, requires          Soil moisture (L-band passive)
            channels)     large antennas)          Sea ice concentration

Microwave   1mm-1m        Coherent backscatter     Sentinel-1 (C, 5.6cm)
(active SAR)(any chosen   from surface features   ALOS-2 (L, 24cm)
            wavelength)   All-weather capable      NISAR (L+S bands)
```

---

## Planck Function and Temperature-Wavelength Relationships

The Planck blackbody function governs how much energy a surface emits at each wavelength:

```
                 2hc^2
B(lambda, T) = --------------------
                lambda^5 * (e^(hc/lambda*kT) - 1)

where:
  h = Planck constant (6.626e-34 J*s)
  c = speed of light (3e8 m/s)
  k = Boltzmann constant (1.381e-23 J/K)
  lambda = wavelength (m)
  T = temperature (K)
```

Wien's displacement law (peak wavelength):

```
  lambda_peak = b / T     where b = 2898 um*K

  T = 5778 K (Sun):    lambda_peak ~ 0.5 um   (peak in green/visible)
  T = 300 K (Earth):   lambda_peak ~ 9.7 um   (peak in TIR window)
  T = 1000 K (fire):   lambda_peak ~ 2.9 um   (peak in SWIR/MIR)
  T = 50 K (cold ice): lambda_peak ~ 58 um    (far infrared)
```

The crossover at ~4 micrometers (Stefan-Boltzmann balance between solar-reflected and Earth-emitted energy) is why the MIR band (3.5-5 um) is special: a warm surface emits thermally AND reflects solar, making interpretation ambiguous. Fire detection exploits the thermal emission here. Land surface temperature retrieval avoids it.

```
SOLAR vs. EARTH EMISSION CROSSOVER

Energy     |
emitted    |    Sun spectrum (attenuated)
or         | \
reflected  |  \
at         |   \        Earth emission
surface    |    \      ___/\___
           |     \___/         \
           |                    \
           +-----+------+--------+----- wavelength
           0.1  0.5   4 um      20 um
                        ^
                   CROSSOVER ~4 um
```

---

## Solar vs. Thermal: Emissivity and Reflectance

In the visible/NIR/SWIR (shortwave), the sensor measures **reflectance** -- the fraction of incoming solar radiation that bounces off. In the TIR (longwave), the sensor measures **radiance** that the surface emits based on its temperature and **emissivity**.

```
SHORTWAVE (0.4-2.5 um)
  At-sensor radiance = reflectance * solar irradiance * cos(theta)
                     + path radiance from atmosphere
  Goal: recover surface reflectance (dimensionless, 0-1)

LONGWAVE / TIR (8-14 um)
  At-sensor radiance = emissivity * B(lambda, T_surface)
                     + (1 - emissivity) * B(lambda, T_atm)  [reflected atm]
                     + atmosphere emission upwelling
  Goal: recover surface temperature T_s AND emissivity epsilon_s
```

**Emissivity** (epsilon) is the ratio of actual emission to blackbody emission at the same temperature (0 < epsilon <= 1). The problem: you have one measurement but two unknowns (T and epsilon). Solutions:

- **Temperature-Emissivity Separation (TES)**: ASTER uses 5 TIR bands to solve the system
- **Split-window algorithm**: Landsat TIRS uses two TIR bands; differential absorption between bands separates atmospheric from surface effects
- **Known emissivity**: For water (epsilon ~ 0.99), you can solve for T directly
- **Reference channel**: ECOSTRESS 8-channel approach over vegetation (known emissivity spectra)

---

## Why Landsat Chose Its Bands

The OLI (Operational Land Imager) band design reflects 50 years of optimization:

| Band | Center (um) | Width (um) | Target Feature | Reason |
|------|-------------|------------|----------------|--------|
| B1 Coastal | 0.443 | 0.016 | Coastal/aerosol | Shallow water, aerosol correction |
| B2 Blue | 0.483 | 0.065 | Water penetration | Urban/vegetation mapping |
| B3 Green | 0.563 | 0.075 | Vegetation peak | Chlorophyll reflectance maximum |
| B4 Red | 0.655 | 0.038 | Chlorophyll absorption | Vegetation discrimination |
| B5 NIR | 0.865 | 0.028 | Vegetation/water | NDVI reference band; water boundary |
| B6 SWIR-1 | 1.609 | 0.085 | Snow/ice/cloud | Distinguish ice from cloud |
| B7 SWIR-2 | 2.201 | 0.200 | Geology/minerals | Clay, carbonate mineral mapping |
| B8 Pan | 0.590 | 0.172 | Panchromatic | 15m pansharpening |
| B9 Cirrus | 1.374 | 0.020 | Cirrus detection | 1.38 um absorbed by water vapor -> cirrus only |
| B10 TIR-1 | 10.90 | 0.600 | Land surface temp | Split-window algorithm |
| B11 TIR-2 | 12.00 | 1.000 | Land surface temp | Split-window algorithm |

The B9 cirrus band (1.374 um) is elegant: at 1.38 um, atmospheric water vapor absorbs almost all energy from below. The band only sees high-altitude ice clouds (cirrus) that float above most of the water vapor column. It is a built-in cloud detection mechanism.

---

## Decision Cheat Sheet

| Question | Band Region | Why |
|----------|-------------|-----|
| What is the vegetation health? | Red + NIR (NDVI) | Chlorophyll absorbs red; healthy plants reflect NIR |
| How wet is the vegetation? | SWIR-1 + NIR | Liquid water absorbs at 1.4 and 1.9 um edges |
| Is that cloud or snow/ice? | SWIR-1 (1.6 um) | Ice absorbs at 1.6; cloud reflects it |
| What minerals are in the rock? | SWIR-2 (2.0-2.5 um) | Clay and carbonate specific absorption features |
| How hot is the surface? | TIR (10-12 um) | Peak thermal emission from ~300K surface |
| Is there a fire? | MIR (3.7 um) | High temperature -> thermal emission in MIR |
| Does it penetrate cloud? | Microwave (cm) | Cloud droplets << microwave wavelength = transparent |
| What is the atmospheric haze? | Blue (0.45 um) | Rayleigh scattering maximized at short wavelengths |
| Can I see shallow water bottom? | Blue-Green (0.5-0.6 um) | Best water penetration before absorption increases |

---

## Common Confusion Points

**"Near-infrared" is not "thermal infrared"** -- NIR (0.7-1.3 um) is reflected solar energy. TIR (8-14 um) is emitted thermal energy. They differ by an order of magnitude in wavelength and completely different physics. Conflating them is a beginner error.

**Rayleigh scattering is why the sky is blue, but it also contaminates satellite imagery** -- the blue band always has more "extra" radiance from the atmosphere than NIR. Without atmospheric correction, a "dark" surface appears brighter in blue than it really is.

**Emissivity is not 1.0 for real surfaces** -- Only water and vegetation approach 1.0. Bare soil: ~0.95. Sand: ~0.90-0.94. Dry vegetation: ~0.93-0.97. Metal: very low. Ignoring emissivity in LST retrieval introduces temperature errors of several Kelvin.

**The 4 um crossover makes fire detection special, not general** -- MODIS B21 (3.96 um) is saturated by fires but insensitive to ambient temperature. That is exactly the design intent: maximum sensitivity to the thermal anomaly, not land surface temperature.
