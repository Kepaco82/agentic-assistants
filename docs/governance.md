# Agentic Assistants Governance

**Version:** 2.1.0  
**Status:** Canonical

## Purpose

This document defines how Agentic Assistants is governed, changed, reviewed, and maintained.

Governance exists to keep the system:

- consistent;
- trustworthy;
- maintainable;
- transparent;
- aligned with the project vision;
- protected from unnecessary complexity and conflicting instructions.

Governance should enable progress without creating unnecessary bureaucracy.

## Governance Principles

### 1. The repository is the source of truth

Canonical role definitions, framework rules, shared standards, playbooks, tests, release notes, and project status must live in the repository.

Conversation history may inform decisions but does not replace repository documentation.

### 2. Changes must be visible

Material changes must be represented by a concrete repository artifact, such as:

- a modified file;
- a new file;
- a test;
- a decision record;
- a changelog entry;
- a release note;
- a commit.

A proposed change is not considered implemented until it exists in the repository.

### 3. Ownership must be explicit

Every change must have a clear owner.

The owner is responsible for:

- defining the objective;
- producing the deliverable;
- identifying dependencies;
- coordinating required review;
- confirming the definition of done.

### 4. Review should match risk

Review requirements should scale with the impact of the change.

Low-risk documentation improvements should move quickly.

High-risk changes involving legal, compliance, security, architecture, financial claims, or system-wide behavior require more deliberate review.

### 5. Preserve working systems

Changes should improve the system without unnecessarily disrupting existing roles, workflows, tests, or repository structure.

Replacement or restructuring requires a clear material benefit.

### 6. Prefer reversible decisions

When uncertainty exists, prefer changes that are:

- easy to test;
- easy to review;
- easy to reverse;
- limited in scope;
- clearly documented.

### 7. Avoid governance theater

Governance must not create process for its own sake.

Every approval, review, document, and status step must serve a practical purpose.

## Governance Roles

### Product Owner

The Product Owner represents the project’s objectives and final business priorities.

Responsibilities include:

- approving the project vision;
- resolving major scope conflicts;
- approving significant structural changes;
- deciding between competing strategic options;
- accepting major releases.

### Lead Architect

The Lead Architect maintains the coherence of the overall system.

Responsibilities include:

- designing the framework;
- protecting architectural consistency;
- reviewing cross-role dependencies;
- identifying duplication and conflicts;
- defining repository-wide standards;
- recommending sequencing and sprint structure.

The Lead Architect may propose changes but does not represent proposals as approved decisions.

### Role Owner

Each canonical role has a designated owner responsible for its quality and maintenance.

Responsibilities include:

- maintaining the role’s mission and scope;
- preventing overlap with other roles;
- updating workflows and deliverables;
- maintaining tests and examples;
- reviewing role-specific changes.

### Reviewer

A Reviewer evaluates a change from a relevant perspective.

Reviewers may include:

- architecture;
- product;
- engineering;
- design;
- compliance;
- legal;
- security;
- brand;
- operations.

Reviewers should be added only when their involvement materially improves the outcome.

## Change Categories

Every material change should be classified as one of the following:

### Editorial Change

Examples:

- grammar;
- formatting;
- clarity;
- typo correction;
- minor wording improvement.

Review requirement:

- author self-review.

Version impact:

- patch version when versioned.

### Functional Change

Examples:

- workflow changes;
- new deliverable requirements;
- modified role behavior;
- new routing rules;
- new quality gates.

Review requirement:

- role owner or relevant domain reviewer.

Version impact:

- minor version unless behavior is materially incompatible.

### Structural Change

Examples:

- repository reorganization;
- framework redesign;
- role consolidation;
- new governance model;
- major routing architecture change.

Review requirement:

- Lead Architect and Product Owner.

Version impact:

- minor or major version depending on compatibility.

### High-Risk Change

Examples:

- legal or compliance standards;
- security rules;
- financial claims;
- privacy requirements;
- regulated workflows;
- instructions that alter human approval requirements.

Review requirement:

- relevant specialist review and Product Owner approval.

Version impact:

- based on functional compatibility and risk.

### Breaking Change

Examples:

- removal of a canonical role;
- incompatible file structure;
- changed instruction hierarchy;
- removal of established functionality;
- behavior that invalidates existing tests or integrations.

Review requirement:

- Lead Architect and Product Owner approval.

Version impact:

- major version.

## Change Lifecycle

Every meaningful change should follow this lifecycle.

### 1. Identify

Define:

- the problem;
- the affected files;
- the intended outcome;
- the owner;
- the risk level.

### 2. Build

Create the concrete deliverable.

Planning alone does not complete this stage unless planning is the requested artifact.

### 3. Review

Evaluate:

- accuracy;
- consistency;
- duplication;
- risk;
- compatibility;
- clarity;
- maintainability;
- definition of done.

### 4. Approve

Approval must be explicit for:

- structural changes;
- breaking changes;
- high-risk changes;
- major releases.

Routine editorial changes may be approved through normal commit review.

### 5. Release

A released change should include, where applicable:

- updated files;
- updated tests;
- version changes;
- `CHANGELOG.md` entry;
- release notes;
- updated project status documentation when the change affects an active roadmap, milestone, or release state.

### 6. Verify

Confirm that:

- the files exist in the correct location;
- the intended behavior is documented;
- no existing functionality was unintentionally removed;
- relevant tests pass;
- the change was committed and pushed.

## Decision States

Every active task must use one of these states:

### Waiting for Input

Work cannot proceed without a specific user or reviewer decision.

The required input must be stated clearly.

### Active Execution

Concrete work is being performed in the current session.

This state must not be used to imply background work.

### Ready for Review

A deliverable exists and requires review before implementation or release.

### Ready for Implementation

The deliverable is approved and can be added to the repository or deployed.

### Blocked

A material dependency prevents progress.

The blocker and required resolution must be stated.

### Complete

The definition of done has been satisfied.

For repository work, “complete” generally means the change has been:

- created;
- reviewed;
- saved;
- committed;
- pushed.

## Approval Rules

Product Owner approval is required for:

- changes to the project vision;
- changes to the constitution;
- removal or consolidation of canonical roles;
- major repository restructuring;
- breaking changes;
- major releases;
- significant changes to governance authority.

Lead Architect review is required for:

- framework changes;
- repository standards;
- routing changes;
- collaboration rules;
- role model changes;
- cross-role architecture.

Specialist review is required when a change materially affects:

- legal;
- compliance;
- security;
- privacy;
- regulated financial communications;
- brand standards;
- production systems.

## Definition of Done

A governance-controlled change is complete when:

- the objective is satisfied;
- the artifact exists;
- the appropriate review is complete;
- assumptions and risks are documented;
- required approvals are recorded;
- relevant files and tests are updated;
- versioning is correct;
- `CHANGELOG.md` is updated when required;
- applicable roadmap, milestone, or release-status documentation reflects the current state;
- the change is committed and pushed.

## Versioning

Canonical governance documents use semantic versioning:

- **Major:** incompatible governance or authority changes;
- **Minor:** new rules, workflows, or responsibilities;
- **Patch:** clarification, correction, or formatting.

The version shown in the document must match the nature of the change.

## Amendments

Changes to this governance document require:

- a documented reason;
- review against the constitution;
- confirmation that authority and ownership remain clear;
- a version update;
- a `CHANGELOG.md` entry;
- Product Owner approval for material changes.

## Governance Standard

The governance system is successful when users can always determine:

- what is being changed;
- why it is being changed;
- who owns it;
- what review is required;
- whether work is actually occurring;
- what the next action is;
- whether the change is complete.