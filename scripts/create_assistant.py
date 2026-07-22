from pathlib import Path
import sys


TEMPLATES = {
    "README.md": """# {title}

## Overview

Describe what this assistant does and who it serves.

## Core Files

- `persona.md`
- `scope.md`
- `workflow.md`
- `deliverables.md`
- `quality.md`
- `handoffs.md`
- `version.md`
""",
    "persona.md": """# {title} Persona

## Mission

Define the assistant's primary purpose.

## Responsibilities

- Add responsibility
- Add responsibility
- Add responsibility

## Operating Principles

- Add principle
- Add principle
- Add principle
""",
    "scope.md": """# Scope

## In Scope

- Add item

## Out of Scope

- Add item

## Inputs

- Add expected input

## Outputs

- Add expected output
""",
    "workflow.md": """# Workflow

## Standard Process

1. Review the request.
2. Identify the objective.
3. Evaluate risks and dependencies.
4. Produce the required deliverable.
5. Review the output for quality.

## Escalation

Describe when the assistant should pause, ask a question, or hand work off.
""",
    "deliverables.md": """# Deliverables

## Primary Deliverables

- Add deliverable

## Required Format

Describe the expected structure and level of detail.
""",
    "quality.md": """# Quality Standards

## Requirements

- Accurate
- Clear
- Complete
- Actionable
- Consistent with repository standards

## Final Review

Confirm the response satisfies the request before delivery.
""",
    "handoffs.md": """# Handoffs

## Incoming Handoffs

Describe the work this assistant can receive from other assistants.

## Outgoing Handoffs

Describe when work should be transferred to another assistant.
""",
    "version.md": """# Version

**Version:** 0.1.0  
**Status:** draft

## Change Log

- Initial assistant structure created.
""",
}


def format_title(name):
    return name.replace("-", " ").replace("_", " ").title()


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/create_assistant.py <assistant-name>")
        sys.exit(1)

    assistant_name = sys.argv[1].strip().lower()
    assistant_path = Path("assistants") / assistant_name

    if assistant_path.exists():
        print(f"Error: Assistant '{assistant_name}' already exists.")
        sys.exit(1)

    assistant_path.mkdir(parents=True)
    title = format_title(assistant_name)

    for filename, template in TEMPLATES.items():
        file_path = assistant_path / filename
        file_path.write_text(
            template.format(title=title),
            encoding="utf-8",
        )

    print(f"Created assistant: {assistant_name}")


if __name__ == "__main__":
    main()