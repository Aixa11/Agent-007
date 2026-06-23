# Secure Architect Agent

Secure Architect Agent is a self-contained open-source project to analyze, structure, and improve existing infrastructure with a focus on critical security, technological sovereignty, and historical compatibility.

## Why this project exists
Many AI coding assistants are optimized to generate code quickly, but not to preserve architectural continuity. In real systems, that often leads to oversized refactors, broken assumptions, and unnecessary operational risk.

Secure Architect Agent is designed to solve that problem by acting as an incremental architectural assistant rather than a replacement engine.

## What it does
- Analyzes existing infrastructure or repositories.
- Identifies architectural, operational, and security risks.
- Proposes minimal, compatible improvements.
- Validates changes locally.
- Documents reasoning clearly.

## Principles
- Security by default.
- Data sovereignty.
- Incremental evolution.
- Compatibility with the existing pipeline.
- Local validation before applying changes.

## What it includes
- Agent rules.
- Reference blueprint.
- Validation scripts.
- Reusable prompts and workflows.
- Minimal functional example.
- Publication-ready documentation.

## MVP scope
- Analyze existing infrastructure.
- Generate structured findings.
- Propose incremental improvements.
- Validate results with local scripts.
- Demonstrate one functional example.

## Project structure
- `agent/`: rules, prompts, and workflows.
- `blueprint/`: architectural reference and policy baselines.
- `validation/`: validation scripts, schema, and reports.
- `examples/`: minimal and real-world examples.
- `docs/`: vision, scope, and roadmap.
- `tests/`: checks for structure, rules, and validation behavior.

## Quick start
1. Clone the repository.
2. Open it in VS Code.
3. Review `AGENTS.md` and `agent/rules.md`.
4. Run the validation task or script.
5. Inspect the example under `examples/oil-pipeline/`.

## Validation
Run one of the following from the repository root:

```powershell
pwsh -ExecutionPolicy Bypass -File .\validation\validate.ps1
python .\validation\validate.py
python -m pytest -q
```

## Example
The `examples/oil-pipeline/` folder shows how the agent should approach an existing infrastructure repository:
- understand what already exists,
- detect risks,
- propose minimal changes,
- and preserve compatibility.

## Contributing
Contributions must respect the incremental evolution principle. Destructive changes or full rewrites are not accepted without strong justification.

## License
Choose an open-source license aligned with the project strategy.
