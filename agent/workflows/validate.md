# Workflow: Validate

## Goal
Verify that a proposed change is safe, coherent, and compatible with the project’s rules.

## Trigger
Use this workflow when the user asks for:
- validation of a diff,
- review of proposed files,
- a safety check,
- or confirmation that a change can proceed.

## Steps
1. Read the change proposal and related files.
2. Check compatibility with `AGENTS.md` and `agent/rules.md`.
3. Review structure, naming, dependencies, and scope.
4. Identify security, operational, and architectural risks.
5. Determine whether the change can be accepted as-is.
6. List required fixes if validation fails.
7. Produce a final validation report.

## Output
The output must include:
- validation result,
- what was checked,
- findings,
- risk assessment,
- required fixes,
- verified strengths,
- and final note.

## Constraints
- Do not approve changes without evidence.
- Do not ignore missing context.
- Do not weaken rules to fit the change.
- Do not treat assumptions as verified facts.

## Success criteria
- The validation result is explicit.
- The user understands what is safe and what is not.
- The report can be used to gate implementation or merge decisions.