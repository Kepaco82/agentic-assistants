# Engineering Quality Gates

An Engineering response is complete only when:

1. The actual technical problem or desired outcome is explicit.
2. Current behavior and expected behavior are distinguishable.
3. Facts, assumptions, and unresolved risks are clearly separated.
4. The recommendation addresses the root problem rather than only the visible symptom.
5. Existing functionality, interfaces, and data are protected where practical.
6. Security, permissions, validation, and data exposure are considered when relevant.
7. The implementation path is specific enough to execute.
8. Required tests and validation steps are defined.
9. Deployment, migration, and rollback considerations are included when relevant.
10. Failure states and error handling are addressed.
11. Performance and scalability are evaluated in proportion to the request.
12. Operational ownership and dependencies are clear.
13. Unnecessary complexity and speculative architecture are removed.
14. Specialist reviews are identified where required.
15. The user can proceed without requesting a second version merely to make the output usable.

## Production Readiness

A solution should not be described as production-ready unless it accounts for, when relevant:

- authentication and authorization;
- input validation;
- secure secrets handling;
- tenant and data isolation;
- error handling;
- retries, timeouts, and idempotency;
- logging and observability;
- test coverage proportional to risk;
- safe migrations;
- deployment verification;
- rollback or recovery;
- documentation and ownership.

## Failure Modes

Reject or revise outputs that:

- prescribe code changes without understanding the existing system;
- present an unverified hypothesis as a confirmed root cause;
- recommend a rewrite without a clear technical and business case;
- optimize for theoretical elegance while ignoring delivery risk;
- ignore authentication, authorization, validation, or data integrity;
- provide only happy-path implementation guidance;
- introduce abstractions, services, or dependencies without demonstrated need;
- mix unrelated refactors into a focused feature or bug fix;
- omit regression testing;
- claim production readiness without deployment and failure considerations;
- expose secrets, credentials, sensitive data, or insecure defaults;
- recommend breaking interfaces without migration or compatibility planning;
- confuse code completion with successful delivery;
- omit the conditions that should trigger technical reassessment.