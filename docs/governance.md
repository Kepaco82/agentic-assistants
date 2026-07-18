# Governance

## Source of Truth

This repository is the canonical source for assistant definitions. Chat instructions should be generated from or synchronized with these files.

## Change Control

Changes should:
1. solve a demonstrated problem;
2. avoid duplicating shared instructions;
3. preserve clear ownership;
4. include a changelog entry;
5. be reviewed for conflicts with adjacent assistants.

## Deprecation

An assistant may be deprecated when:
- its responsibilities are fully absorbed by another assistant;
- usage no longer justifies a dedicated role;
- its scope cannot be distinguished clearly;
- maintaining it creates inconsistent outputs.

Deprecated assistants remain documented until migration is complete.
