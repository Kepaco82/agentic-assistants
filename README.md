# Agentic Assistants

Agentic Assistants is a modular framework for creating, validating, documenting, assembling, and managing reusable AI assistants through a consistent file structure and command-line interface.

The project is designed to help teams move beyond isolated prompts by treating assistants as structured, versioned, testable software assets.

## Why This Project Exists

AI assistants are often stored as long prompt documents with inconsistent structures, unclear ownership, duplicated instructions, and no reliable validation process.

Agentic Assistants provides a standardized framework for defining assistants using:

- Structured metadata
- Modular prompt files
- Validation rules
- A central assistant registry
- Command-line tooling
- Automated documentation
- Automated testing
- Continuous integration

This makes assistants easier to create, review, maintain, reuse, and eventually compose into larger workflows.

## Core Features

- Metadata-driven assistant definitions
- Standardized assistant folder structure
- Central assistant registry
- Assistant validation
- Assistant creation from templates
- Assistant search and discovery
- Assistant metadata inspection
- Prompt assembly
- Prompt export
- Markdown documentation generation
- Installable command-line interface
- Automated pytest coverage
- GitHub Actions continuous integration

## Current Assistants

The repository currently includes canonical implementations for:

- Executive Assistant
- Engineering Assistant
- Product Assistant

Each assistant follows the same modular architecture and shared quality standards.

## Installation

### Requirements

- Python 3.10 or newer
- Git

### Clone the Repository

```bash
git clone https://github.com/Kepaco82/agentic-assistants.git
cd agentic-assistants