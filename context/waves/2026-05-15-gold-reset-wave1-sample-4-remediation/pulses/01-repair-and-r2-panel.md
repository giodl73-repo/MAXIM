# Pulse 01 - Repair and R2 Panel

## Scope

| Guide | Action |
|---|---|
| `architecture/02-STRUCTURAL-LOGIC.md` | Replaced degraded structural-design selector with diagnostic span/lateral table |
| `architecture/03-ENVIRONMENTAL.md` | Replaced degraded passive-design selector with diagnostic performance table |
| `architecture/04-BUILDING-SYSTEMS.md` | Replaced degraded coordination selector with diagnostic systems table |
| `architecture/05-DESIGN-PROCESS.md` | Replaced degraded phase-response selector with diagnostic process table |

## Validation

`proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK
with no literal `FAIL`.

