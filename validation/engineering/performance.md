# Engineering Validation – Performance

## Scenario

### User Prompt

"Our application works normally with a small number of users, but it starts timing out during periods of heavy traffic. How should we diagnose and fix the problem?"

## Expected Classification

- Performance
- Reliability

## Expected Behavior

The Engineering assistant should:

- recognize this as a performance and reliability problem;
- begin with diagnosis before recommending major changes;
- identify likely bottlenecks across the application stack;
- recommend instrumentation and measurement;
- separate immediate mitigation from long-term remediation;
- explain relevant technical trade-offs;
- avoid assuming a specific root cause without evidence.

## Ownership Boundaries

Engineering should **not**:

- redefine company strategy;
- prioritize the broader product roadmap;
- create marketing or customer communication plans;
- make unsupported claims about the root cause;
- recommend a complete rewrite before diagnosing the existing system.

## Expected Deliverable

A technical response that includes:

1. Problem Summary
2. Initial Hypotheses
3. Diagnostic Plan
4. Immediate Mitigations
5. Long-Term Fixes
6. Risks and Trade-offs
7. Recommended Next Technical Action

## Pass Criteria

The response:

- correctly identifies the performance and reliability concerns;
- follows a diagnosis-first approach;
- considers application, database, infrastructure, and dependency bottlenecks;
- recommends measurable observability or testing;
- separates mitigation from permanent remediation;
- remains within Engineering ownership;
- clearly identifies the next technical action.
- clearly distinguishes immediate mitigation steps from long-term architectural improvements.