# Pulse 01 - Repair and R2 Panel

## Scope

| Guide | Action |
|---|---|
| `agriculture/01-SOILS-FERTILITY.md` | Replaced degraded soil-management selector with diagnostic fertility table |
| `agriculture/03-IRRIGATION.md` | Replaced degraded irrigation selector with diagnostic water-management table |
| `agriculture/08-AQUACULTURE.md` | Replaced degraded aquaculture question table with diagnostic production-impact table |
| `agriculture/09-FUTURE-AGRICULTURE.md` | Replaced degraded future-agriculture question table with diagnostic evidence table |

## Validation

`proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK
with no literal `FAIL`.

