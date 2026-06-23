# Supported and Not Supported Scenarios

This document defines the intended operating boundaries of Secure Architect Agent.
Its goal is to prevent the project from being misinterpreted as an automatic full-architecture replacement tool.

## Supported scenarios

### 1. Incremental review of existing infrastructure
The agent can analyze an existing repository or infrastructure layout and identify risks, gaps, and improvement opportunities.

### 2. Security hardening
The agent can recommend smaller changes that improve security posture without changing the overall system design.

### 3. Compatibility-preserving refactors
The agent can suggest improvements that keep the historical pipeline, naming conventions, and operational assumptions intact.

### 4. Architecture summaries
The agent can summarize the current architecture, explain the major components, and highlight important dependencies.

### 5. Validation-oriented review
The agent can help validate whether a change is consistent, safe, and aligned with the project’s rules.

### 6. Documentation-driven adoption
The agent can support adoption through README files, workflow guidance, blueprint references, and examples.

### 7. Controlled modernization
The agent can propose modernization steps when they are incremental, reversible, and compatible with the current environment.

## Not supported scenarios

### 1. Automatic full re-architecture
The agent is not intended to replace the entire architecture by default.

### 2. Unsafe destructive changes
The agent should not recommend changes that clearly break the existing pipeline, unless the user explicitly requests a migration.

### 3. Secret handling
The project does not support storing or processing secrets in the repository.

### 4. Unbounded code generation
The agent should not generate massive rewrites without context, validation, or compatibility checks.

### 5. Vendor lock-in
The project should not force a single cloud, editor, or provider as the only valid path.

### 6. Hidden assumptions
The agent should not invent missing context or silently assume details that were not provided.

### 7. Full autonomous deployment
The agent is not a replacement for operational approval, staging validation, or human review.

## Operating rule
If a request implies a full rewrite, a risky migration, or a break from historical compatibility, it should be treated as out of scope unless the user explicitly authorizes that direction.

## Summary
Secure Architect Agent is designed for:
- analysis,
- structured improvement,
- security hardening,
- and compatibility-preserving evolution.

It is not designed to be a drop-in engine for automatic architectural replacement.
