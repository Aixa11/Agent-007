# Scope

## Project scope
Secure Architect Agent is an open-source, self-contained framework for analyzing existing infrastructure and proposing incremental improvements with a strong focus on security, sovereignty, and compatibility.

## In scope
- Analyze existing infrastructure or repository structure.
- Detect architectural risks and security gaps.
- Propose minimal, incremental changes.
- Preserve historical pipelines and conventions.
- Validate outputs locally with scripts and checks.
- Provide examples that demonstrate adoption without forcing a rewrite.
- Document reasoning, assumptions, and impact.

## Out of scope for the MVP
- Full automatic migration of arbitrary systems.
- Unbounded refactoring.
- Mandatory dependence on external APIs.
- Secret handling in the repository.
- One-click replacement of the user’s architecture.
- Support for every cloud, stack, or framework from day one.

## Behavioral scope
The agent must:
- prioritize compatibility over idealized redesign,
- explain why a change is recommended,
- avoid destructive actions,
- keep outputs understandable and reviewable,
- and surface uncertainty when validation is incomplete.

## Non-goals
- Becoming a generic chat assistant.
- Replacing human architectural judgment.
- Generating massive codebases without context.
- Enforcing a single vendor or editor workflow.

## MVP boundary
The MVP ends when the repository can:
- define clear rules,
- describe its architecture,
- validate its own structure,
- and demonstrate one functional example that respects the incremental-improvement philosophy.

## Future extensions
After the MVP, the project may add:
- stack-specific blueprints,
- stronger validators,
- more examples,
- prompt libraries,
- workflow templates,
- and integration support for multiple AI tools.