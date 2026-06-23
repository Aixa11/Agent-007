# Network Module

## Purpose
Provide a reference for secure, maintainable, and incremental network architecture decisions.

## When to use
Use this module when the system needs guidance on:
- network segmentation,
- routing,
- private access,
- ingress and egress control,
- or environment separation.

## Recommended patterns
- Separate public and private zones.
- Keep sensitive services out of public exposure.
- Use least-privilege routing and access rules.
- Prefer explicit network boundaries over implicit trust.
- Document all externally reachable endpoints.

## Anti-patterns
- Flat network designs with no meaningful segmentation.
- Broad allow-all security rules.
- Hidden dependencies on public internet access.
- Unclear routing or undocumented ingress points.
- Mixing internal and public workloads without controls.

## Example usage
When reviewing an existing infrastructure, the agent should:
- identify whether services are exposed unnecessarily,
- check whether private components remain private,
- verify whether network boundaries match the system’s trust model,
- and propose the smallest safe improvement.

## Validation notes
Validate that:
- public exposure is intentional,
- routing matches the documented design,
- sensitive systems are isolated,
- and changes preserve compatibility with existing connectivity assumptions.

## Compatibility considerations
Do not recommend network redesign unless required. Prefer incremental improvements such as tightening rules, clarifying boundaries, or documenting intended exposure.