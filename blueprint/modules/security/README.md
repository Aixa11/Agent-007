# Security Module

## Purpose
Provide a reference for baseline security controls, governance expectations, and safe defaults.

## When to use
Use this module when the system needs guidance on:
- access control,
- encryption,
- auditability,
- secrets handling,
- logging,
- or governance enforcement.

## Recommended patterns
- Apply least privilege everywhere.
- Enable encryption at rest and in transit where relevant.
- Keep secrets out of source control.
- Log security-relevant events.
- Make security controls visible and reviewable.
- Prefer explicit policy over tribal knowledge.

## Anti-patterns
- Hardcoded credentials.
- Broad administrative access.
- Publicly exposed sensitive services.
- Undocumented exceptions.
- Security controls that depend only on manual discipline.

## Example usage
When evaluating a repository, the agent should:
- look for secrets exposure risk,
- check whether encryption expectations are documented,
- identify where permissions may be too broad,
- and recommend minimal hardening steps.

## Validation notes
Validate that:
- secrets are not committed,
- access is limited to what is needed,
- encryption defaults are present where appropriate,
- and the security posture is understandable from the repository itself.

## Compatibility considerations
Security improvements should preserve system behavior whenever possible. Favor smaller hardening steps over sweeping policy rewrites unless the risk clearly requires them.