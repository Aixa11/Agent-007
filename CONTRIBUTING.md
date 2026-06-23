# Contributing

Thank you for your interest in contributing to Secure Architect Agent.

This project aims to help teams improve existing infrastructure with a conservative, incremental approach focused on security, compatibility, and sovereignty. Contributions are welcome as long as they respect that philosophy.

## What kind of contributions are welcome

- Documentation improvements.
- New examples that preserve the incremental approach.
- Validation scripts and checks.
- New prompts or workflows that follow the project rules.
- Blueprint modules and policy baselines that are safe, reusable, and well documented.
- Bug fixes and small refinements.

## What we are looking for

We value contributions that are:
- Small and focused.
- Easy to validate.
- Compatible with the existing pipeline and structure.
- Clearly documented.
- Aligned with the project’s security and sovereignty principles.

## Before opening a pull request

Please make sure you have:

1. Read `README.md`.
2. Read `AGENTS.md`.
3. Read `agent/rules.md`.
4. Reviewed the relevant documentation in `docs/`, `blueprint/`, or `validation/`.
5. Run the local validation checks.
6. Confirmed that your change does not break the incremental evolution model.

## Contribution guidelines

- Prefer small pull requests over large ones.
- Avoid rewriting the architecture unless the change is explicitly requested.
- Preserve existing names, paths, and conventions whenever possible.
- Do not add new dependencies unless they are clearly justified.
- Do not commit secrets, tokens, credentials, or sensitive data.
- Document any assumptions or trade-offs.
- Include validation notes with every meaningful change.
- Keep changes aligned with the supported scenarios documented in `supported-scenarios.md`.

## Suggested pull request structure

A good pull request should include:

- A short description of the change.
- The reason the change is needed.
- The files affected.
- How the change was validated.
- Any compatibility or security considerations.

## Reporting issues

If you find a problem, please open an issue with:
- A clear title.
- A short description of the issue.
- Steps to reproduce it, if applicable.
- Relevant files or context.
- The expected behavior.

## Code of contribution

This project is intentionally conservative. Contributions should help the project:
- preserve what already works,
- improve what is risky or unclear,
- and keep the repository easy to adopt and maintain.

We may decline contributions that introduce unnecessary complexity, broad rewrites, or behavior that weakens the project’s core principles.

## Thank you

Even small contributions matter. Good documentation, validation, and examples are often as valuable as code.
