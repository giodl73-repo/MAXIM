# Ductwork

## The Big Picture

A properly designed, correctly sized, well-sealed duct system is the unsung variable
in HVAC performance. Industry studies consistently find that typical existing US residential
ductwork leaks 20–30% of conditioned air into unconditioned attics and crawlspaces — energy
wasted before it reaches any room. Equipment sizing and efficiency ratings are irrelevant
if the distribution system defeats them.

```
+----------------------------------------------------------------------+
|                    DUCT SYSTEM PERFORMANCE CHAIN                      |
|                                                                      |
|  Equipment    → Supply plenum → Supply trunk → Branch ducts → Rooms |
|  (designed     (pressurized)   (main artery)  (per room)   (delivery)|
|  for 400 CFM/                                                        |
|  ton airflow)                                                        |
|                                                                      |
|  Failure mode 1: Duct leakage → conditioned air into attic (lost)   |
|  Failure mode 2: Undersized ducts → high static pressure → low flow  |
|  Failure mode 3: Poorly designed → unbalanced delivery per room      |
|  Failure mode 4: Compressed flex duct → massive pressure loss        |
|                                                                      |
|  Result: 3-ton equipment delivering 1.5-ton performance              |
+----------------------------------------------------------------------+
```

---

## Section 1: Manual D — Duct Design Standard

Manual D (ACCA) is to ductwork what Manual J is to equipment sizing. Most residential
duct systems in existing homes were not designed with Manual D. Most installers still
don't use it. This is why duct problems are epidemic.

```
  MANUAL D WORKFLOW:
  ┌─────────────────────────────────────────────────────────────────┐
  │ INPUT: Manual J room-by-room loads + airflow requirements       │
  │        Equipment specs (blower performance curve, TESP rating)  │
  └──────────────────────────┬──────────────────────────────────────┘
                             |
                             v
  ┌─────────────────────────────────────────────────────────────────┐
  │ CALCULATE: Available static pressure for ducts                  │
  │  TESP available = Equipment fan capacity at design CFM          │
  │  Minus: filter pressure drop (0.08–0.15" w.c.)                 │
  │  Minus: coil pressure drop (0.10–0.20" w.c.)                   │
  │  = Remaining for supply + return ductwork                      │
  └──────────────────────────┬──────────────────────────────────────┘
                             |
                             v
  ┌─────────────────────────────────────────────────────────────────┐
  │ FRICTION RATE: Pressure available / total effective length (TEL)│
  │  TEL = straight duct length + equivalent lengths of all fittings│
  │  Friction rate (FR) = inches w.c. per 100 ft                    │
  │  Used to enter duct sizing chart → diameter per CFM per branch  │
  └──────────────────────────┬──────────────────────────────────────┘
                             |
                             v
  ┌─────────────────────────────────────────────────────────────────┐
  │ OUTPUT: Diameter of each duct run, sized to deliver Manual J    │
  │         CFM to each room at acceptable velocity (<900 FPM)      │
  └─────────────────────────────────────────────────────────────────┘
```

---

## Section 2: Static Pressure

The pressure the blower fan must overcome. Too much static = reduced airflow = reduced performance.

```
  PRESSURE DIAGRAM OF DUCT SYSTEM:
                    |
               [AIR HANDLER]
               FAN (blower)
                    |
    (+) SUPPLY SIDE          (-) RETURN SIDE
    ├── Supply plenum         ├── Return plenum
    ├── Supply trunk          ├── Return trunk
    ├── Branch supply ducts   └── Return grilles
    └── Supply registers                │
                                   [FILTER]
                                   [COIL]

  TESP (Total External Static Pressure):
  = pressure measured at supply + return plenums

  Equipment rated at, e.g., 0.5" w.c. at 1,200 CFM
  Meaning: at 0.5 inches of water column back-pressure, blower
  delivers 1,200 CFM (check blower curve for exact numbers)

  COMPONENTS OF PRESSURE DROP:
  ┌────────────────────────┬────────────────────────────────────┐
  │ Filter (clean, MERV 8) │ 0.05–0.08" w.c.                   │
  │ Filter (MERV 13)       │ 0.10–0.15" w.c.                   │
  │ Filter (dirty)         │ 0.20–0.40" w.c. (can double TESP!)│
  │ AC evaporator coil     │ 0.10–0.20" w.c.                   │
  │ Supply duct system     │ 0.10–0.20" w.c.                   │
  │ Return duct system     │ 0.05–0.15" w.c.                   │
  ├────────────────────────┼────────────────────────────────────┤
  │ Typical total TESP     │ 0.35–0.70" w.c.                   │
  └────────────────────────┴────────────────────────────────────┘

  CONSEQUENCE OF HIGH STATIC PRESSURE:
  - Reduced airflow → reduced sensible capacity
  - Reduced airflow → potential evaporator coil freeze-up
  - Reduced airflow → latent capacity loss (poor dehumidification)
  - Fan motor works harder → higher electricity use + heat → shorter life
```

---

## Section 3: Equivalent Length — Fittings Matter

Straight duct has predictable pressure loss (friction). Fittings create turbulence —
converted to equivalent straight-duct length for calculation:

```
  EQUIVALENT LENGTHS (approximate values):
  ┌─────────────────────────────┬───────────────────────────────────┐
  │ Fitting                     │ Equivalent Length (ft)            │
  ├─────────────────────────────┼───────────────────────────────────┤
  │ 90° sharp elbow (square)    │ 50–75 ft                         │
  │ 90° smooth radius elbow     │ 10–20 ft                         │
  │ 45° elbow                   │ 5–10 ft                          │
  │ Tee (branch takeoff)        │ 20–50 ft                         │
  │ Transition (constriction)   │ 5–20 ft                          │
  │ Supply boot (register box)  │ 25–50 ft                         │
  │ Return grille               │ 15–30 ft                         │
  └─────────────────────────────┴───────────────────────────────────┘

  A duct run with 3 sharp 90° elbows → adds 150–225 ft of equivalent length
  On a 15-ft physical run, the fittings dominate the pressure drop

  Rule: minimize elbows, use sweep turns, keep trunk-to-branch angles gradual
```

---

## Section 4: Duct Types and Materials

```
  SHEET METAL (GALVANIZED STEEL):
  ┌──────────────────────────────────────────────────────────────────┐
  │ Best performance: smooth interior → lowest friction loss         │
  │ Most durable: lasts decades                                      │
  │ No compression degradation                                       │
  │ Round or rectangular; fabricated to size                         │
  │ Requires sheet metal shop or skilled fabrication                 │
  │ Seams must be sealed with mastic or foil tape                    │
  │ Most expensive; most labor-intensive                             │
  └──────────────────────────────────────────────────────────────────┘

  FLEX DUCT (INSULATED FLEXIBLE DUCT):
  ┌──────────────────────────────────────────────────────────────────┐
  │ Construction: wire helix (shape) + plastic inner liner +         │
  │ fiberglass insulation (R-6 or R-8) + outer vapor barrier jacket  │
  │                                                                  │
  │ Advantages: easy to install around obstacles, lower cost         │
  │                                                                  │
  │ CRITICAL INSTALLATION REQUIREMENT:                               │
  │ Must be FULLY EXTENDED — zero compression, no sag, no kinks      │
  │                                                                  │
  │ What installers often do:           What happens:                │
  │ Leave slack in flex duct          →  Accordion compression        │
  │ Drape over framing with sag       →  Low-point restriction       │
  │ Route around obstacle with kink   →  Major pressure spike        │
  │                                                                  │
  │ 5% compression of flex duct → doubles pressure loss              │
  │ 15% compression → 5× pressure loss                               │
  │                                                                  │
  │ Properly installed: only slightly worse than sheet metal         │
  │ Improperly installed (common): massive airflow reduction         │
  └──────────────────────────────────────────────────────────────────┘

  DUCT BOARD (FIBERGLASS DUCT BOARD):
  ┌──────────────────────────────────────────────────────────────────┐
  │ Rigid fiberglass panels fabricated into rectangular ductwork     │
  │ Built-in insulation (no separate wrap needed)                    │
  │ Slightly higher friction than sheet metal (rougher interior)     │
  │ Requires sealing at all joints (mastic or foil tape)             │
  │ Cannot handle high static pressure applications                  │
  │ Common in light commercial; some residential                     │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Section 5: Duct Sealing

Duct leakage is one of the highest-return improvements possible in existing homes.
A 3-ton unit leaking 25% of supply air into the attic is operating like a 2.25-ton unit.

```
  SEALING METHODS:
  ┌─────────────────┬────────────────────────────────────────────────┐
  │ Mastic sealant  │ Gray paste applied with brush; dries flexible  │
  │ (recommended)   │ Best for: rigid duct seams, boot connections,  │
  │                 │ register boxes; permanent; code-approved       │
  ├─────────────────┼────────────────────────────────────────────────┤
  │ Metal (foil)    │ Aluminum foil tape with aggressive adhesive    │
  │ tape, UL181-    │ (UL181B-FX listed — not generic hardware tape) │
  │ rated           │ Good for: clean metal-to-metal connections     │
  │                 │ Will fail if applied over dust/dirt            │
  ├─────────────────┼────────────────────────────────────────────────┤
  │ "Duct tape"     │ NEVER use gray fabric duct tape for ductwork   │
  │ (DO NOT USE)    │ Fails at temperature cycling in <5 years       │
  │                 │ Not code-compliant; adhesive melts             │
  ├─────────────────┼────────────────────────────────────────────────┤
  │ Aeroseal        │ Spray-from-inside polymer sealing method       │
  │ (injection)     │ System is pressurized; particles blown through │
  │                 │ leaks → accumulate → seal from inside         │
  │                 │ Ideal for: inaccessible attic/crawlspace ducts │
  │                 │ Can seal holes up to ~5/8" diameter            │
  │                 │ Professional installation required ($1,500–3k) │
  └─────────────────┴────────────────────────────────────────────────┘

  LEAKAGE TESTING — DUCT BLASTER:
  Similar principle to blower door but for duct system
  - Connect to return plenum; seal supply registers
  - Pressurize to 25 Pa; measure CFM25 (airflow at 25 Pa)
  - Compare to floor area → CFM25/100 sq ft

  STANDARDS:
  IECC new construction:  ≤ 4 CFM25/100 sq ft total leakage
  Energy Star:             ≤ 3 CFM25/100 sq ft to outside
  Passive House:           essentially zero leakage (no ducts preferred)

  Total leakage vs. leakage to outside:
  - Total: all duct leaks including inside conditioned space (less harmful)
  - To outside: only leaks to unconditioned space (attic, crawl, garage)
  - "To outside" is what actually wastes energy; the harder metric
```

---

## Section 6: Supply and Return Balance

```
  COMMON INSTALLER SHORTCUT: central return only
  - Single large return at hallway; no return in bedrooms
  - Result: closed bedroom door = no airflow path
  → Bedroom becomes positive pressure (supply air, no return)
  → Hallway becomes negative pressure
  → Pressure difference = 3–5 Pa across door
  → Building now operates like an exhaust-only ventilation system
  → Duct leakage to outdoors dramatically increases (pressure drives it)

  SOLUTIONS:
  ┌──────────────────────┬────────────────────────────────────────────┐
  │ Return in each room  │ Best: balanced flow in every room          │
  ├──────────────────────┼────────────────────────────────────────────┤
  │ Jump ducts           │ Short duct from ceiling to hallway;        │
  │                      │ hidden above ceiling; low-cost balance     │
  ├──────────────────────┼────────────────────────────────────────────┤
  │ Transfer grilles     │ Grille from room to hallway (no duct);     │
  │                      │ works with open doors; visible             │
  ├──────────────────────┼────────────────────────────────────────────┤
  │ Undercut doors       │ 3/4" to 1" gap under door; partial remedy; │
  │                      │ less effective than dedicated path         │
  └──────────────────────┴────────────────────────────────────────────┘
```

---

## Section 7: Zoning

```
  ZONING APPROACHES:
  ┌──────────────────────┬────────────────────────────────────────────┐
  │ Multiple equipment   │ Each zone = separate system (mini-splits   │
  │ (mini-split model)   │ or separate ducted units); no duct issues; │
  │                      │ independent control; best solution         │
  ├──────────────────────┼────────────────────────────────────────────┤
  │ Motorized dampers    │ Duct dampers open/close per thermostat;    │
  │ + single system      │ complex; requires bypass damper when zones │
  │                      │ close (or static pressure spikes)          │
  │                      │ Variable-speed air handler helps (reduces  │
  │                      │ airflow as zones close)                    │
  └──────────────────────┴────────────────────────────────────────────┘

  BYPASS DAMPER (required for damper zoning):
  When zone dampers close, static pressure rises.
  Bypass damper: connects supply plenum to return plenum
  → excess air recirculates; static pressure stays controlled
  → inefficient (conditioning and reconditioning same air)
  → variable-speed air handler is better approach (modulates fan speed)
```

---

## Decision Cheat Sheet

| Problem | Solution |
|---|---|
| High utility bills, undersized rooms | Duct leakage test; seal with mastic/Aeroseal |
| Room never gets warm/cool enough | Measure airflow at register; check for compressed flex |
| Equipment short-cycling | Measure TESP; likely too high (check filter + duct size) |
| New duct installation | Use sheet metal trunk + flex branches; Manual D sizing |
| Attic or crawl ductwork, inaccessible | Aeroseal injection sealing |
| Bedroom pressure problems | Add return, jump duct, or transfer grille per room |
| Adding zone control | Mini-splits for new zones; bypass damper for damper zoning |
| Suspecting high duct leakage | Duct blaster test; target ≤4 CFM25/100 sq ft |

---

## Common Confusion Points

**"Duct tape" is not for ducts**: gray fabric tape (duct tape) fails at HVAC temperature
cycling. UL181-listed foil tape or mastic sealant are the code-approved options. The name
"duct tape" is a misnomer that causes expensive callbacks.

**Flex duct is not inherently bad**: properly installed, fully extended, supported every
4 ft, no kinks — flex performs adequately. The problem is the 95% of flex installations
with compression and sag. This is an installation quality problem, not a material problem.

**Return leakage is worse than supply leakage**: supply leakage = conditioned air into
attic (energy waste). Return leakage = hot/cold/humid attic air drawn INTO the system
→ wrong-temperature air going through the coil → equipment works harder. Both bad.

**More vents ≠ more airflow**: you can't improve airflow to a room by adding more supply
registers without proper duct sizing. If the duct feeding those registers is undersized,
the additional registers just split the same insufficient airflow.
