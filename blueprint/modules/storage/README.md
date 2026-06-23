# Storage Module

## Purpose
Provide a reference for secure and maintainable storage design, including object storage, block storage, file storage, backups, and retention.

## When to use
Use this module when the system needs guidance on:
- data durability,
- encryption,
- backup strategy,
- retention policies,
- lifecycle management,
- or storage access control.

## Recommended patterns
- Encrypt stored data where appropriate.
- Define retention and lifecycle behavior explicitly.
- Separate sensitive and non-sensitive data stores.
- Restrict access to the minimum required set of users and services.
- Document backup and recovery assumptions.

## Anti-patterns
- Open or anonymous access to storage.
- Unbounded retention with no policy.
- Unclear ownership of backups.
- Sensitive data stored without clear protection.
- Storage structures that grow without lifecycle rules.

## Example usage
When analyzing a repository, the agent should:
- determine whether storage is intentionally exposed,
- check whether encryption and versioning are expected,
- confirm whether retention and backup behavior are documented,
- and suggest the smallest useful improvements.

## Validation notes
Validate that:
- access is controlled,
- data protection expectations are explicit,
- backup and recovery assumptions are documented,
- and the storage design fits the system’s operational needs.

## Compatibility considerations
Prefer small changes such as enabling protection features, documenting policies, or clarifying ownership rather than replacing the storage model entirely.