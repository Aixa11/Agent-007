# Legacy Modernization Minimal Example

## Context
This example shows how Secure Architect Agent should behave when reviewing a legacy platform that cannot be fully redesigned right away.

## Input
A team has:
- an older service architecture,
- a stable but outdated deployment flow,
- legacy naming and conventions,
- and a strong need to preserve operational continuity.

## Expected agent behavior
The agent must:
- understand the existing structure,
- identify the most relevant risks,
- propose incremental and reversible changes,
- preserve compatibility with the historical pipeline,
- and avoid suggesting a complete rewrite by default.

## Example outcome
Instead of recommending a migration first, the agent should suggest:
- documenting current dependencies,
- reducing security exposure,
- tightening validation,
- adding observability,
- and modernizing one subsystem at a time.

## Success criteria
- No destructive redesign.
- No forced migration.
- Clear reasoning for each proposed change.
- Local validation completed successfully.
