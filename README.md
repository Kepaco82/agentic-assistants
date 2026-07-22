# Agentic Assistants

A modular operating framework for specialized AI assistants with clear ownership, shared standards, collaboration rules, and versioned canonical personas.

## Purpose

This repository is the canonical source of truth for the Agentic Assistants workspace. It is designed to:

- eliminate redundant assistant personas;
- define clear ownership and routing;
- maintain shared company, brand, and quality standards;
- keep assistant instructions modular and version controlled;
- make future assistants easier to create and govern.

## Assistant Directory

1. Executive
2. Product
3. Engineering
4. Design
5. Video
6. Content
7. Marketing
8. Sales
9. Investor Relations
10. Compliance
11. Legal
12. Operations
13. Analytics
14. SEO
15. AI Studio
16. Music
17. Terminal

## Repository Structure

- `docs/` — constitution, governance, routing, collaboration, quality, and versioning
- `shared/` — company context, brand standards, writing standards, and common knowledge
- `assistants/` — canonical persona specifications
- `templates/` — reusable templates for new assistants and changes
- `roadmap/` — implementation and migration plans
- `examples/` — example routing and cross-assistant workflows

## Validation

Assistant behavior is evaluated using the repository-wide validation framework.

Start with:

- [Validation Overview](validation/README.md)
- [Validation Guide](validation/guide.md)
- [Scoring Rubric](validation/rubric.md)

## Canonical Assistant Structure

Every canonical assistant should use the following modular structure:

```text
assistants/[assistant-name]/
├── README.md
├── persona.md
├── scope.md
├── workflow.md
├── deliverables.md
├── quality.md
├── handoffs.md
└── version.md

## Current Version

**v2.0.0-alpha.2**

This release establishes the repository architecture and includes complete canonical candidate implementations for Executive and Engineering. Additional assistants will be built using the same modular structure and shared standards.