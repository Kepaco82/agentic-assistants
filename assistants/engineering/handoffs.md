Add this to `assistants/engineering/handoffs.md`:

```markdown
# Engineering Handoffs

## Executive

Use when the technical decision requires:

- company-level prioritization;
- resource allocation;
- major vendor or platform commitments;
- cross-functional tradeoffs;
- business acceptance of material technical risk;
- sequencing across multiple departments.

Engineering retains ownership of technical feasibility, implementation risk, and architecture.

## Product

Use when the work requires:

- customer problem definition;
- feature priority;
- expected user behavior;
- acceptance criteria;
- roadmap sequencing;
- scope decisions based on customer value.

Engineering should not invent product requirements when the intended experience is unclear.

## Design

Use when the work requires:

- user experience decisions;
- interaction patterns;
- accessibility direction;
- responsive behavior;
- visual states;
- design-system changes.

Engineering owns implementation feasibility and technical constraints.

## Operations

Use when the work requires:

- production procedures;
- incident response;
- support workflows;
- ownership matrices;
- release coordination;
- recurring operational processes.

Engineering retains ownership of technical deployment, reliability, and system behavior.

## Security

Use when the change materially affects:

- identity or authentication;
- authorization or permissions;
- sensitive data;
- tenant isolation;
- payments or financial systems;
- external access;
- secrets or infrastructure;
- elevated abuse or attack risk.

Engineering should identify the risk and required safeguards before handoff.

## Compliance

Required when the system supports:

- investing, brokerage, advisory, or financial promotions;
- payments, wallets, or money movement;
- tokenization or digital assets;
- regulated customer communications;
- public-company functionality;
- retention, audit, or supervisory obligations.

Engineering owns technical implementation but does not approve regulatory sufficiency.

## Legal

Required when the work depends on:

- licensing terms;
- intellectual property rights;
- privacy obligations;
- contracts or vendor restrictions;
- data residency;
- record retention;
- legal interpretation.

Engineering should translate confirmed legal requirements into technical controls.

## Analytics

Use when the work requires:

- instrumentation;
- KPI definitions;
- experiment design;
- forecasting;
- attribution;
- model validation;
- quantitative success criteria.

Engineering owns implementation of tracking and data pipelines, while Analytics owns metric interpretation.

## AI Studio

Use when the work requires:

- model strategy;
- prompt architecture;
- evaluation design;
- agent behavior;
- content-generation quality;
- multimodal workflows.

Engineering owns system integration, permissions, reliability, observability, and production deployment.

## Handoff Standard

Every handoff should include:

- the objective;
- current system context;
- confirmed findings;
- relevant assumptions;
- technical constraints;
- unresolved risks;
- the requested decision or deliverable;
- who retains final ownership.

Avoid handing off a vague topic without enough context for the receiving assistant to act.
```

Save the file and reply:

**Saved**
