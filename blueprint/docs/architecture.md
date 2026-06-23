# Secure Architect Agent Architecture

## Overview
Secure Architect Agent is a self-contained framework for assisting architecture and security improvements on existing systems. The design goal is not to replace an environment, but to analyze it, structure it, harden it, and improve it incrementally.

## Design goals
- Preserve the user’s current architecture.
- Improve security posture by default.
- Keep the system auditable and explainable.
- Support local-first operation.
- Minimize churn and operational disruption.
- Keep the documentation living and aligned with the repository state.

## Architectural principles
- Incremental evolution.
- Compatibility first.
- Security by design.
- Local validation.
- Tool-agnostic guidance.
- Documentation as a living asset.

## Layer model

### 1. Adoption layer
Purpose: make the project easy to understand and adopt.

Contents:
- `README.md`
- `README.en.md`
- `docs/vision.md`
- `docs/scope.md`
- `docs/roadmap.md`
- usage examples

Responsibilities:
- explain the value proposition,
- define the project scope,
- describe installation and adoption paths.

### 2. Agent layer
Purpose: define the behavioral rules of the assistant.

Contents:
- `AGENTS.md`
- `agent/rules.md`
- `agent/prompts/`
- `agent/workflows/`

Responsibilities:
- constrain behavior,
- prevent aggressive rewrites,
- enforce compatibility and validation,
- make agent behavior predictable.

### 3. Blueprint layer
Purpose: store architectural knowledge and reusable reference material.

Contents:
- `blueprint/modules/`
- `blueprint/policies/`
- `blueprint/docs/`

Responsibilities:
- provide patterns and reference structures,
- document decisions and rationale,
- capture safe defaults and guardrails,
- support incremental reuse across projects.

### 4. Validation layer
Purpose: verify correctness and prevent unsafe output.

Contents:
- `validation/validate.ps1`
- `validation/validate.py`
- optional future validators
- audit report generators

Responsibilities:
- check structure,
- check basic consistency,
- report issues,
- provide a local quality gate,
- make validation repeatable.

### 5. Examples layer
Purpose: show real use without forcing a full migration.

Contents:
- `examples/oil-pipeline/`
- future examples for SaaS, legacy migration, data platforms, etc.

Responsibilities:
- demonstrate adoption,
- show before/after changes,
- keep examples minimal and reproducible.

## Data flow
1. The user provides an existing project or architecture.
2. The agent reads rules, blueprint, and scope.
3. The agent generates a structured analysis.
4. The validation layer checks consistency and boundaries.
5. The agent returns minimal improvements with justification.

## Non-goals
- Full autonomous migration of arbitrary systems.
- Hard dependency on one vendor, one editor, or one cloud.
- Unbounded refactoring.
- Remote execution that requires storing secrets in the repo.
- Overly abstract architecture that cannot be adopted incrementally.

## MVP definition
The MVP is successful if it can:
- analyze a small real infrastructure example,
- identify improvement opportunities,
- propose constrained changes,
- validate the output locally,
- and document the reasoning clearly.

## Repository contract
The repository must remain:
- readable,
- reproducible,
- auditable,
- and safe to modify incrementally.

## Extension points
Future versions may add:
- more stack-specific blueprints,
- stronger static analysis,
- policy packs,
- more validation backends,
- integration adapters for different agents,
- reusable templates for teams and domains.

## Documentation rule
Any change to the architecture should be reflected in this file and reviewed as part of the project’s living documentation.