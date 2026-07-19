# Engineering Deliverables

## Technical Assessment

Use to evaluate an existing system, issue, or proposed change.

### Structure

**Objective**  
What the user is trying to achieve.

**Current State**  
Relevant system behavior, architecture, constraints, and dependencies.

**Findings**  
Confirmed facts, likely causes, and unresolved risks.

**Recommendation**  
The preferred technical approach.

**Tradeoffs**  
Meaningful costs, risks, alternatives, and operational consequences.

**Next Actions**  
Ordered implementation steps, owners, dependencies, and validation.

## Implementation Plan

Use for features, integrations, refactors, migrations, and infrastructure changes.

### Structure

1. Desired outcome
2. Assumptions
3. Affected files or components
4. Implementation sequence
5. Data or schema changes
6. API or interface changes
7. Validation and error handling
8. Testing requirements
9. Deployment steps
10. Rollback plan
11. Success criteria

## Bug Resolution Plan

Use when diagnosing and fixing defective behavior.

### Structure

- Reported behavior
- Expected behavior
- Reproduction conditions
- Confirmed findings
- Root cause or leading hypothesis
- Proposed fix
- Regression risks
- Tests required
- Validation steps

Do not present an unverified hypothesis as a confirmed root cause.

## Architecture Decision Record

Use for consequential technical decisions.

### Structure

**Decision**  
The technical decision being made.

**Context**  
The problem, constraints, and relevant existing architecture.

**Options Considered**  
Only materially different options.

**Recommendation**  
The selected approach and why.

**Consequences**  
Benefits, limitations, risks, and operational impact.

**Implementation Implications**  
Required changes, dependencies, migration, and ownership.

**Review Trigger**  
The condition that should cause the decision to be reconsidered.

## Security Review

Use when a change affects identity, permissions, sensitive data, payments, financial systems, external access, or tenant boundaries.

### Structure

- Assets and data affected
- Trust boundaries
- Authentication and authorization
- Input and output validation
- Data exposure risks
- Abuse and attack scenarios
- Required safeguards
- Logging and auditability
- Residual risks
- Specialist review required

## API Specification

### Structure

- Purpose
- Consumers
- Authentication
- Endpoints or operations
- Request schema
- Response schema
- Validation
- Error behavior
- Idempotency
- Rate limits
- Versioning
- Security considerations
- Example requests and responses

## Database Change Plan

### Structure

- Objective
- Current schema
- Proposed schema change
- Data migration
- Backward compatibility
- Indexing and performance
- Integrity constraints
- Deployment sequence
- Rollback or recovery
- Validation

## Deployment Plan

### Structure

- Change summary
- Target environment
- Prerequisites
- Deployment sequence
- Configuration changes
- Migration steps
- Health checks
- Monitoring
- Rollback conditions
- Rollback procedure
- Post-deployment validation

## Code Review

### Structure

- Summary
- Correctness issues
- Security issues
- Reliability concerns
- Performance concerns
- Maintainability concerns
- Testing gaps
- Required changes
- Optional improvements
- Approval recommendation

Distinguish blocking issues from non-blocking improvements.