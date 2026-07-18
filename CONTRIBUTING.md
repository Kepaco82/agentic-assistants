# Contributing

## Core Rule

The repository is the source of truth. Do not maintain competing persona instructions in private notes or isolated chat threads.

## Change Process

1. Identify the affected assistant or shared standard.
2. Confirm whether the change belongs in shared guidance or a specialized persona.
3. Update the smallest appropriate file.
4. Add an entry to `CHANGELOG.md`.
5. Increment the version according to `docs/versioning.md`.
6. Review routing, boundaries, and handoffs for unintended overlap.

## Writing Standards

- Use direct, explicit language.
- Avoid duplicated instructions.
- Avoid personality theater and unnecessary role stacking.
- Define observable behaviors and deliverables.
- Keep shared rules in `docs/` or `shared/`.
- Keep domain-specific rules inside the relevant assistant folder.
