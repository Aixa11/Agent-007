<p align="center">
  <img src="./assets/hero-banner.png" alt="Secure Architect Agent" width="80%" />
</p>

# Secure Architect Agent

> Fortified Cookie Stack for incremental infrastructure analysis, security hardening, and compatibility-preserving improvement.

<p align="center">
  <strong>
    An open-source AI agent for analyzing existing infrastructure, identifying security and architectural risks, and proposing incremental improvements without breaking historical compatibility.
  </strong>
</p>

---

## What this project is

Secure Architect Agent is a self-contained open-source project designed to help teams improve existing infrastructure with a conservative, incremental approach.

It is built for systems that already exist, already matter, and cannot be casually rewritten. The goal is to preserve what works, reduce risk, and improve security and governance step by step.

## Why it exists

Many AI coding assistants are optimized to generate code quickly, but not to preserve architectural continuity. In real systems, that often leads to oversized refactors, broken assumptions, and unnecessary operational risk.

Secure Architect Agent is designed to solve that problem by acting as an incremental architectural assistant rather than a replacement engine.

## Core principles

- Security by default.
- Data sovereignty.
- Incremental evolution.
- Compatibility with the existing pipeline.
- Local validation before applying changes.
- Clear reasoning for every recommendation.

## What it does

- Analyzes existing infrastructure or repositories.
- Identifies architectural, operational, and security risks.
- Proposes minimal, compatible improvements.
- Validates changes locally.
- Documents reasoning clearly.

## What it includes

- Agent rules.
- Reusable prompts and workflows.
- Reference blueprint.
- Policy baselines.
- Validation scripts and schema.
- Tests.
- Minimal examples.
- Publication-ready documentation.

## Project structure

- `agent/`: rules, prompts, and workflows.
- `blueprint/`: architectural reference and policy baselines.
- `validation/`: validation scripts, schema, and reports.
- `examples/`: minimal and real-world examples.
- `docs/`: vision, scope, and roadmap.
- `tests/`: checks for structure, rules, and validation behavior.

## Supported scenarios

- Incremental review of existing infrastructure.
- Security hardening.
- Compatibility-preserving refactors.
- Architecture summaries.
- Validation-oriented review.
- Documentation-driven adoption.
- Controlled modernization.

## Not supported

- Automatic full re-architecture.
- Unsafe destructive changes.
- Secret handling in the repository.
- Unbounded code generation.
- Vendor lock-in.
- Hidden assumptions.
- Full autonomous deployment.

## Examples

### Oil pipeline
A minimal example showing how the agent should review an existing critical infrastructure repository while preserving compatibility.

### Legacy modernization
A second example showing how the agent can improve a legacy platform incrementally without forcing a rewrite.

## Validation

Run one of the following from the repository root:

```powershell
pwsh -ExecutionPolicy Bypass -File .\validation\validate.ps1
python .\validation\validate.py
python -m pytest -q
```

## Getting started

1. Clone the repository.
2. Open it in VS Code.
3. Review `AGENTS.md` and `agent/rules.md`.
4. Run the validation task or script.
5. Review the examples and the supported scenarios.

## Contributing

Contributions are welcome when they respect the project philosophy:
- small and focused,
- easy to validate,
- compatible with the existing structure,
- and aligned with the security and sovereignty principles.

Read `CONTRIBUTING.md` before opening a pull request.

## Security

If you discover a security issue, please review `SECURITY.md` and report it privately.

## License

This project is licensed under the Apache License 2.0. See `LICENSE` for details.
