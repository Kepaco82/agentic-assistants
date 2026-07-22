# Assistant Validation

## Purpose

This directory contains the validation framework for canonical assistants.

Validation helps determine whether an assistant:

- understands the user’s request;
- stays within its ownership boundaries;
- follows its documented workflow;
- produces the expected deliverables;
- meets its quality standards.

## Current Scope

The validation framework will initially support:

- Executive;
- Engineering;
- Product.

Additional assistants should receive validation coverage as they become canonical candidates.

## Structure

Each canonical assistant may have its own validation directory containing representative test scenarios.

Each scenario should document:

- the user prompt;
- the expected behavior;
- the relevant ownership boundaries;
- the expected deliverable;
- the quality criteria used for review.

## Guiding Principle

Validation should test observable assistant behavior, not writing style alone.

The goal is to determine whether the assistant produces useful, accurate, actionable, and role-appropriate outputs.