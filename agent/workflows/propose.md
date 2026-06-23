# Workflow: Propose

## Goal
Generate minimal, compatible improvements based on the current state and the analysis findings.

## Trigger
Use this workflow when the user asks for:
- a proposed change set,
- a refactor suggestion,
- an architecture improvement,
- or a safer implementation path.

## Steps
1. Read the analysis and the relevant source files.
2. Identify the smallest change that addresses the highest-value issue.
3. Check whether the change preserves naming, structure, and pipeline behavior.
4. Avoid unnecessary dependencies or abstraction.
5. Prepare a concise proposal with impact notes.
6. Include a validation plan for the proposed change.
7. Return the recommendation in a structured format.

## Output
The output must include:
- goal,
- observed issue,
- proposed change,
- why this change,
- compatibility impact,
- validation,
- and rollout note.

## Constraints
- Do not redesign the whole system.
- Do not change architecture style by default.
- Do not propose work that cannot be validated.
- Do not hide trade-offs.

## Success criteria
- The proposal is small, clear, and actionable.
- The user can apply it without losing historical context.
- The recommendation reduces risk or operational cost.