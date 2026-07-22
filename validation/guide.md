# Validation Guide

## Purpose

This guide explains how to validate an assistant using the repository's validation framework.

## Validation Process

### Step 1

Load the assistant you want to validate into a new conversation.

### Step 2

Select the appropriate validation scenario from the `validation` directory.

### Step 3

Use the scenario's **User Prompt** without modification.

### Step 4

Review the assistant's response against the scenario's:

- Expected Classification
- Expected Behavior
- Ownership Boundaries
- Expected Deliverable
- Pass Criteria

### Step 5

Score the response using the repository-wide scoring rubric.

### Step 6

If the assistant does not fully satisfy the validation criteria:

- improve the assistant;
- improve the validation scenario if needed;
- retest before merging changes.

## Guiding Principle

Validation is an iterative process. The goal is not to produce one perfect response, but to continuously improve both the assistants and the validation framework through real-world testing.