# Blueprint Modules

## Purpose
This directory contains reusable reference modules that capture safe architectural patterns for common infrastructure concerns.

## How to use these modules
Each module is a documentation-first reference. It should explain:
- what the module is for,
- when to use it,
- what good usage looks like,
- what to avoid,
- and how to validate that it fits the current environment.

## Module philosophy
Modules in this repository are not meant to force a single architecture. They exist to help the agent propose improvements that are consistent, secure, and incremental.

## Module standards
Every module README should include:
- purpose,
- recommended patterns,
- anti-patterns,
- example usage,
- validation notes,
- and compatibility considerations.

## Current modules
- `network/`
- `security/`
- `compute/`
- `storage/`

## Maintenance rule
If a module becomes outdated, update it as part of the normal project flow. Do not leave architecture references stale.