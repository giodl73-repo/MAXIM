# Pulse 01 - Repair and R2 Panel

## Scope

| Guide | Action |
|---|---|
| `ai-engineering/02-EVALS-HARNESS.md` | Replaced degraded tool selector with diagnostic eval-failure table |
| `ai-engineering/03-ORCHESTRATION.md` | Replaced degraded orchestration selector with diagnostic framework-boundary table |
| `ai-engineering/04-AGENTS.md` | Replaced degraded agent-pattern selector with diagnostic autonomy table |
| `ai-engineering/05-SAFETY.md` | Replaced degraded safety selector with diagnostic risk-control table |

## Validation

`proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK
with no literal `FAIL`.

