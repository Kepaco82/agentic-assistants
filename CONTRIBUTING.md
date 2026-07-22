# Contributing

## Purpose

This document defines how changes should be proposed, reviewed, versioned, and completed across the Agentic Assistants repository.

The repository is the source of truth. Do not maintain competing persona instructions in private notes, isolated chat threads, or undocumented external files.

## Contribution Principles

- Make the smallest change that fully solves the problem.
- Preserve canonical ownership and role boundaries.
- Update shared guidance only when the rule applies across multiple assistants.
- Keep domain-specific guidance inside the relevant assistant directory.
- Avoid duplicating instructions that already exist elsewhere.
- Prefer explicit, observable behavior over vague personality language.
- Keep every committed change reviewable and reversible.

## Change Process

1. Identify the affected assistant, shared standard, or repository document.
2. Confirm whether the change belongs in shared guidance or a specialized assistant.
3. Review related routing, ownership, and handoff rules.
4. Update the smallest appropriate file.
5. Validate terminology, structure, and version metadata.
6. Add an entry to `CHANGELOG.md` when required.
7. Increment the version according to `docs/versioning.md`.
8. Commit with a clear, action-oriented message.
9. Push the change and confirm the working tree is clean.

## Assistant Changes

Changes to a canonical assistant should preserve the standard structure:

```text
README.md
persona.md
scope.md
workflow.md
deliverables.md
quality.md
handoffs.md
version.md