# Compute Module

## Purpose
Provide a reference for compute-layer design, including servers, containers, serverless functions, and workload placement.

## When to use
Use this module when the system needs guidance on:
- workload sizing,
- service placement,
- runtime boundaries,
- scaling strategy,
- or compute isolation.

## Recommended patterns
- Keep workloads small and clearly named.
- Match compute design to operational need.
- Separate long-running services from batch or ephemeral tasks.
- Prefer predictable runtime behavior.
- Document how workloads are deployed and updated.

## Anti-patterns
- Overloaded instances running unrelated workloads.
- Unclear ownership of runtime components.
- Undocumented scaling assumptions.
- Compute layers that mix critical and non-critical concerns without boundaries.
- Excessive complexity for simple workloads.

## Example usage
When reviewing a compute layer, the agent should:
- identify whether the workload is appropriately isolated,
- check whether deployment assumptions are documented,
- verify whether the runtime model matches the system’s purpose,
- and propose minimal efficiency or reliability improvements.

## Validation notes
Validate that:
- compute responsibilities are clear,
- scaling assumptions are explicit,
- runtime dependencies are documented,
- and proposed changes do not alter operational behavior unexpectedly.

## Compatibility considerations
Avoid forcing a new compute model by default. Keep changes incremental, such as clearer workload separation, better naming, or safer deployment defaults.