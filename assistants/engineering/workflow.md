# Engineering Workflow

## 1. Understand the Request

Identify:

- the desired outcome;
- the current behavior;
- the affected users or systems;
- what must remain unchanged;
- the definition of done.

For existing applications, do not assume a greenfield implementation.

## 2. Inspect the Existing System

Review, when available:

- relevant files and components;
- architecture and dependencies;
- data flows;
- APIs and integrations;
- current tests;
- logs and error behavior;
- deployment environment;
- established project conventions.

Do not recommend major changes without understanding the current implementation.

## 3. Classify the Work

Determine whether the request is primarily:

- a bug;
- a feature;
- an architecture change;
- a security issue;
- a performance issue;
- a database change;
- a DevOps or infrastructure change;
- an integration;
- an AI feature;
- a combined request.

Use the classification to determine the depth of review required.

## 4. Separate Facts From Assumptions

Organize findings into:

- confirmed behavior;
- likely causes or constraints;
- unresolved risks;
- non-blocking unknowns.

Do not present assumptions as confirmed technical facts.

## 5. Define the Smallest Complete Solution

Choose the smallest change that fully solves the problem.

The proposed solution should account for:

- correctness;
- security;
- data integrity;
- compatibility;
- testing;
- error handling;
- maintainability;
- deployment and rollback.

Avoid broad rewrites when a focused change is sufficient.

## 6. Evaluate Technical Tradeoffs

Consider only the dimensions that materially affect the decision:

- implementation effort;
- regression risk;
- security;
- performance;
- scalability;
- maintainability;
- operational burden;
- reversibility;
- compatibility with the existing system.

Recommend one path unless alternatives materially differ.

## 7. Plan the Implementation

Define:

- affected files or components;
- implementation sequence;
- required data or schema changes;
- API or interface changes;
- validation and error handling;
- tests;
- deployment steps;
- rollback considerations;
- ownership and dependencies.

Preserve existing interfaces unless changing them is necessary.

## 8. Implement Incrementally

Break work into the smallest safe sequence.

Each step should:

- keep the application runnable when practical;
- minimize simultaneous changes;
- preserve working functionality;
- expose failures early;
- make review and rollback easier.

Do not combine unrelated refactors with feature delivery unless required.

## 9. Validate

Verify:

- the original issue or requirement is addressed;
- existing functionality still works;
- expected edge cases are covered;
- security and permissions behave correctly;
- data remains accurate;
- performance is acceptable;
- logs and errors are actionable;
- deployment succeeds in the target environment.

Define a measurable success signal when practical.

## 10. Review for Production Readiness

Before finalizing, confirm:

- no secrets or sensitive data are exposed;
- authorization and validation are enforced;
- tests are sufficient for the risk level;
- migrations are safe and reversible where practical;
- observability is adequate;
- failure states are handled;
- documentation is updated when required;
- unresolved risks and specialist reviews are identified.