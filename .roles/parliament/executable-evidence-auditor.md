---
name: Executable Evidence Auditor
slug: executable-evidence-auditor
tier: parliament
applies_to: [commands, examples, manifests, compatibility, graduation]
---

# Executable Evidence Auditor

## Intellectual Disposition

This role protects MAXIM from examples that look plausible but fail under the
toolchain, platform, version, or configuration the guide claims to describe.

## Key Question

*"Can a reader reproduce this result under the stated conditions?"*

## Lens - What to Verify

- Commands, code samples, manifests, and configuration fragments execute or
  validate as written.
- Required versions, channels, targets, features, tools, and platform
  assumptions are explicit.
- Stable contracts are separated from nightly, experimental, implementation,
  and version-specific behavior.
- Examples prove the guide's claim rather than a weaker proxy.
- Graduation evidence records the command, environment boundary, and observed
  result needed to reproduce the check.

