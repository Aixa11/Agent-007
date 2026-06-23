# Roadmap

## Phase 1 - Foundation
Goal: create a stable and publishable repository baseline.

### Deliverables
- `README.md` and `README.en.md`
- `AGENTS.md`
- `agent/rules.md`
- `docs/vision.md`
- `docs/scope.md`
- `docs/roadmap.md`
- basic folder structure
- minimal validation scripts

### Exit criteria
- The repository structure is complete.
- The project vision is clear.
- The agent boundaries are documented.
- Local validation passes.

## Phase 2 - MVP Core
Goal: define the minimum useful behavior of the agent.

### Deliverables
- `agent/prompts/` with first reusable prompts
- `agent/workflows/` with analysis and proposal flows
- `blueprint/docs/architecture.md`
- `blueprint/modules/` initial reference material
- `blueprint/policies/` initial policy baselines
- one minimal example under `examples/oil-pipeline/`

### Exit criteria
- The agent can analyze a sample input.
- The agent can produce a structured improvement proposal.
- The result can be validated locally.
- The example demonstrates incremental change rather than redesign.

## Phase 3 - Validation and Hardening
Goal: improve trust, repeatability, and safety.

### Deliverables
- stronger validation scripts
- schema definitions for findings and reports
- tests for file structure and rule consistency
- better reporting output
- more explicit safety and compatibility checks

### Exit criteria
- Validation is reproducible.
- Outputs are easier to review.
- Structural mistakes are caught early.
- Security and compatibility constraints are enforced more clearly.

## Phase 4 - Adoption and Examples
Goal: make the project easier to understand and reuse.

### Deliverables
- additional example repositories
- case studies for different infrastructure types
- expanded README guidance
- contribution guide
- release-ready documentation

### Exit criteria
- New users can understand the project quickly.
- Contributors can add examples without ambiguity.
- Adoption does not require deep internal knowledge.

## Phase 5 - Extensibility
Goal: prepare the project for multiple stacks and tools.

### Deliverables
- stack-specific modules
- optional adapters for different agents
- reusable policy packs
- reusable workflow templates

### Exit criteria
- The repository remains coherent as it grows.
- Extensions do not weaken the original philosophy.
- The project still preserves incremental evolution as the default mode.

## Roadmap principle
New features should strengthen the core promise:
understand what exists, improve it incrementally, and validate everything locally.