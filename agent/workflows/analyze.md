# Workflow: Analyze

## Goal
Understand the current repository or infrastructure as it exists today.

## Trigger
Use this workflow when the user asks for:
- an architectural assessment,
- a repository review,
- a risk analysis,
- or a summary of the current state.

## Steps
1. Read `AGENTS.md`, `agent/rules.md`, and the relevant documentation.
2. Inspect the repository structure and key files.
3. Identify the main purpose of the system.
4. Map the primary components and dependencies.
5. Detect security, maintainability, and compatibility concerns.
6. Separate facts from assumptions.
7. Produce a structured analysis report.

## Output
The output must include:
- system overview,
- current state,
- findings,
- priority assessment,
- minimal improvement opportunities,
- uncertainties,
- and next step recommendation.

## Constraints
- Do not propose a full rewrite.
- Do not change files during analysis.
- Do not assume missing context.
- Do not overstate confidence.

## Success criteria
- The user can understand the system clearly.
- Risks are identified without unnecessary noise.
- The report is usable as input for an improvement workflow.