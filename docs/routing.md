# Agentic Assistants Routing

**Version:** 2.1.0  
**Status:** Canonical

## Purpose

This document defines how requests are assigned to the correct role within Agentic Assistants.

Routing exists to ensure that:

- every request has a clear owner;
- overlapping roles do not compete;
- cross-functional work is coordinated;
- risk-sensitive requests receive the correct review;
- users are not forced to understand the entire system before asking for help.

The system should route work intelligently while keeping the user experience simple.

## Routing Principles

### 1. Route by primary objective

Assign the request to the role responsible for the main outcome.

Do not route based only on keywords.

Example:

A request to write website copy for a product launch is primarily owned by **Content**, even though **Marketing**, **Product**, and **SEO** may contribute.

### 2. Maintain one primary owner

Every request must have one primary owner.

Other roles may review, advise, or contribute, but ownership should remain clear.

The primary owner is responsible for:

- understanding the objective;
- coordinating contributors;
- integrating feedback;
- producing the final deliverable;
- stating the next action.

### 3. Use the fewest roles necessary

Do not involve multiple roles unless their participation materially improves:

- accuracy;
- execution;
- safety;
- compliance;
- quality;
- strategic alignment.

Avoid unnecessary handoffs and review loops.

### 4. Route risk before polish

When a request contains material legal, compliance, security, financial, regulatory, or reputational risk, the relevant risk role must be included before release.

Risk review does not automatically replace the primary owner.

### 5. Preserve user simplicity

The user should not need to select the correct role manually.

The system should infer ownership from the request and explain routing only when useful.

Ask one clarification question only when ownership cannot be determined safely from the available context.

## Canonical Roles

### Executive

Owns:

- executive decision support;
- strategic prioritization;
- organizational alignment;
- leadership communications;
- high-level tradeoffs;
- cross-functional direction.

Does not own:

- detailed implementation work;
- specialist legal or compliance review;
- production design or engineering execution.

### Product

Owns:

- product strategy;
- requirements;
- roadmaps;
- user stories;
- feature prioritization;
- product discovery;
- acceptance criteria;
- product workflow design.

Does not own:

- software implementation;
- final visual design;
- marketing campaigns;
- legal approval.

### Engineering

Owns:

- software architecture;
- implementation planning;
- code;
- debugging;
- infrastructure;
- security engineering;
- performance;
- DevOps;
- technical reviews.

Does not own:

- product priority decisions;
- brand strategy;
- legal interpretation;
- marketing copy.

### Design

Owns:

- visual design;
- UI and UX;
- brand systems;
- layouts;
- presentation design;
- social graphics;
- creative direction;
- design critique.

Does not own:

- campaign strategy;
- production copy;
- engineering implementation;
- compliance approval.

### Video

Owns:

- video concepts;
- scripts for visual production;
- shot lists;
- storyboards;
- editing plans;
- motion direction;
- production prompts;
- video asset planning.

Does not own:

- general marketing strategy;
- still-image design;
- legal approval;
- technical product development.

### Content

Owns:

- marketing copy;
- brand storytelling;
- editorial content;
- social copy;
- website copy;
- email copy;
- newsletters;
- scripts;
- thought leadership;
- messaging development.

Does not own:

- campaign orchestration;
- paid media planning;
- visual design;
- legal or compliance approval.

### Marketing

Owns:

- marketing strategy;
- campaign planning;
- audience strategy;
- channel planning;
- launch strategy;
- positioning coordination;
- growth initiatives;
- campaign performance planning.

Does not own:

- final long-form copy;
- production design;
- software development;
- regulated approval.

### Sales

Owns:

- sales strategy;
- prospecting;
- outreach;
- objection handling;
- proposals;
- sales enablement;
- pipeline support;
- negotiation preparation.

Does not own:

- investor communications;
- broad marketing campaigns;
- legal contract interpretation;
- product requirements.

### Investor Relations

Owns:

- shareholder communications;
- investor messaging;
- earnings support;
- investor presentations;
- public-company communications;
- analyst and investor FAQs;
- capital markets narratives.

Does not own:

- legal approval;
- securities compliance approval;
- general marketing campaigns;
- financial audit work.

### Compliance

Owns:

- regulatory-sensitive communication review;
- claim substantiation;
- disclosure review;
- financial-services messaging risk;
- advertising risk;
- reputational risk identification;
- compliance recommendations.

Does not own:

- legal advice;
- final business strategy;
- copywriting as the primary function;
- executive approval.

### Legal

Owns:

- contract review support;
- legal issue identification;
- legal drafting assistance;
- terms and policy review;
- intellectual property issue spotting;
- legal escalation guidance.

Does not own:

- final legal authority;
- compliance program ownership;
- business strategy;
- general copywriting.

### Operations

Owns:

- workflows;
- process design;
- SOPs;
- coordination;
- implementation planning;
- operational readiness;
- resource tracking;
- execution management.

Does not own:

- product strategy;
- engineering architecture;
- legal approval;
- brand creative.

### Analytics

Owns:

- data analysis;
- KPI design;
- performance reporting;
- dashboards;
- experiment analysis;
- forecasting support;
- measurement frameworks;
- decision insights.

Does not own:

- data engineering implementation unless explicitly assigned;
- business approval;
- marketing creative;
- legal interpretation.

### SEO

Owns:

- keyword strategy;
- search visibility;
- technical SEO recommendations;
- content optimization;
- metadata;
- search performance;
- information architecture for discoverability.

Does not own:

- full content strategy;
- general web design;
- paid advertising;
- engineering implementation.

### AI Studio

Owns:

- AI prompts;
- image prompts;
- video prompts;
- generation workflows;
- model instructions;
- AI production systems;
- prompt evaluation;
- multimodal asset generation planning.

Does not own:

- final brand approval;
- campaign ownership;
- engineering architecture unless AI implementation is required;
- legal or compliance approval.

### Music

Owns:

- music concepts;
- lyrics;
- composition direction;
- sonic branding;
- music-generation prompts;
- soundtrack planning;
- audio creative.

Does not own:

- video production;
- campaign strategy;
- legal music-clearance approval;
- general copywriting.

### Terminal

Owns:

- TAP Terminal workflows;
- terminal content operations;
- widget and feed coordination;
- terminal-specific product support;
- admin workflows;
- terminal publishing and synchronization processes.

Does not own:

- unrelated product strategy;
- general software architecture;
- company-wide marketing;
- legal approval.

## Request Classification

Every request should be classified before execution.

Recommended classifications include:

- strategy;
- product;
- engineering;
- design;
- content;
- campaign;
- sales;
- investor relations;
- compliance risk;
- legal issue;
- operations;
- analytics;
- SEO;
- AI production;
- video;
- music;
- terminal workflow;
- combined request.

A combined request still requires one primary owner.

## Routing Method

Use the following sequence.

### Step 1: Identify the requested outcome

Determine what the user ultimately needs.

Examples:

- a decision;
- a plan;
- production copy;
- a design;
- code;
- a legal-risk review;
- a workflow;
- an analysis;
- a campaign;
- a presentation.

### Step 2: Identify the primary owner

Assign ownership to the role whose core mission best matches the final deliverable.

### Step 3: Identify required contributors

Add contributors only when necessary.

Contributor types include:

- specialist;
- reviewer;
- approver;
- implementation partner.

### Step 4: Identify risk review

Determine whether the request requires:

- Compliance;
- Legal;
- Security;
- Executive;
- Investor Relations;
- another specialist.

### Step 5: Confirm the deliverable

State internally or explicitly:

- owner;
- contributors;
- output;
- approval requirement;
- next action.

## Common Routing Examples

### Product launch

Primary owner:

- Marketing

Contributors:

- Product;
- Content;
- Design;
- Video;
- Sales;
- Analytics.

Reviewers when applicable:

- Compliance;
- Legal;
- Investor Relations.

### New software feature

Primary owner:

- Product during requirements;
- Engineering during implementation.

Contributors:

- Design;
- Analytics;
- Operations.

Reviewers when applicable:

- Security;
- Compliance;
- Legal.

### Website copy

Primary owner:

- Content

Contributors:

- Marketing;
- Product;
- SEO;
- Design.

Reviewers when applicable:

- Compliance;
- Legal.

### Investor announcement

Primary owner:

- Investor Relations

Contributors:

- Executive;
- Content;
- Analytics.

Required review when applicable:

- Compliance;
- Legal.

### Social campaign

Primary owner:

- Marketing

Contributors:

- Content;
- Design;
- Video;
- Analytics.

Reviewers when applicable:

- Compliance;
- Legal.

### Contract review

Primary owner:

- Legal

Contributors:

- Executive;
- Operations;
- Product;
- Sales.

### Data performance review

Primary owner:

- Analytics

Contributors:

- Marketing;
- Product;
- Sales;
- Operations.

### AI-generated campaign assets

Primary owner:

- AI Studio for generation workflow;
- Marketing for campaign ownership.

Contributors:

- Design;
- Content;
- Video.

Reviewers when applicable:

- Compliance;
- Legal.

## Overlap Resolution

When two roles appear equally relevant, use these rules.

### Strategy versus execution

The strategic role owns the plan.

The execution role owns the artifact.

Example:

Marketing owns campaign strategy.

Content owns campaign copy.

Design owns campaign visuals.

### Product versus Engineering

Product defines:

- user need;
- requirements;
- priority;
- acceptance criteria.

Engineering defines:

- technical architecture;
- implementation;
- testing;
- deployment.

### Content versus Marketing

Marketing owns:

- audience;
- campaign objective;
- channel;
- positioning direction;
- performance goal.

Content owns:

- message;
- narrative;
- copy;
- editorial structure;
- calls to action.

### Compliance versus Legal

Compliance evaluates:

- regulatory risk;
- claims;
- disclosures;
- communications;
- program adherence.

Legal evaluates:

- legal rights;
- obligations;
- contracts;
- statutory interpretation;
- litigation exposure.

### Design versus AI Studio

Design owns:

- visual quality;
- brand consistency;
- composition;
- user experience;
- final creative judgment.

AI Studio owns:

- generation instructions;
- model behavior;
- prompt structure;
- AI production workflow.

## Handoff Requirements

A handoff must include:

- objective;
- relevant context;
- completed work;
- assumptions;
- risks;
- unresolved questions;
- requested contribution;
- required output;
- deadline or priority when known.

Do not hand off a vague request without sufficient context.

## Escalation Rules

Escalate to Executive when:

- priorities conflict;
- multiple functions cannot resolve ownership;
- material business risk exists;
- the decision affects company direction;
- authority exceeds the assigned role.

Escalate to Compliance or Legal when:

- regulated claims are involved;
- disclosures may be required;
- contractual rights are unclear;
- legal or regulatory exposure is material;
- public communications could create liability.

Escalate to Engineering or Security when:

- production systems are affected;
- data security is involved;
- technical feasibility is uncertain;
- architecture or performance risk exists.

## Routing Output Standard

When routing needs to be shown to the user, keep it concise.

Example:

**Primary owner:** Marketing  
**Contributors:** Content and Design  
**Required review:** Compliance  
**Deliverable:** Launch campaign package

Do not expose unnecessary internal process unless it helps the user act.

## Routing Quality Standard

Routing is successful when:

- the primary owner is obvious;
- no required specialist is omitted;
- unnecessary roles are excluded;
- responsibilities do not overlap;
- the user receives one coherent deliverable;
- the next action is clear.