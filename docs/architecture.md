# Repository Architecture

## Purpose

This document explains how the Agentic Assistants repository is organized and how its components work together.

## Repository Structure

The repository is organized into the following major areas:

- `assistants/` — Individual assistant definitions and behaviors.
- `shared/` — Reusable standards, guidance, and conventions shared across assistants.
- `validation/` — Validation framework, scenarios, and scoring.
- `templates/` — Canonical templates used to create new assistants.
- `examples/` — Example prompts, workflows, and outputs.
- `docs/` — Project documentation and reference material.
- `tests/` — Repository quality and validation assets.
- `roadmap/` — Future plans and project direction.

## Request Lifecycle

A typical request follows this lifecycle:

1. A user submits a request.
2. The appropriate assistant is selected.
3. The assistant follows its workflow.
4. A deliverable is produced.
5. The response is evaluated using the validation framework.
6. Feedback is used to improve both the assistant and the validation criteria.

## Guiding Principle

Every assistant should share a common foundation while remaining specialized within its own domain.