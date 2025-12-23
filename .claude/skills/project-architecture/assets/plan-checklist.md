# Architect's Quick Reference Checklist

Use this checklist when creating or reviewing architectural plans.

## Pre-Planning (Phase 0: Research)

**Context Gathering**:
- [ ] Read feature spec (`specs/<feature>/spec.md`)
- [ ] Review project constitution (`.specify/memory/constitution.md`)
- [ ] Explore existing codebase for patterns
- [ ] Identify dependencies and constraints
- [ ] Document findings in `research.md`

**Constitution Check (Initial)**:
- [ ] Verify approach doesn't violate constitutional principles
- [ ] Identify applicable constraints
- [ ] Note any potential violations for justification

## Planning (Phase 1: Design)

### 1. Scope and Dependencies
- [ ] Define clear system boundaries
- [ ] List in-scope features
- [ ] Explicitly state out-of-scope items
- [ ] Document external dependencies with ownership
- [ ] Identify integration points

### 2. Key Decisions and Rationale
- [ ] List 2-4 viable alternatives for each major decision
- [ ] Document tradeoffs (performance, cost, time, flexibility)
- [ ] Provide clear rationale for chosen approach
- [ ] Ensure decisions are measurable and testable
- [ ] Prefer reversible decisions

### 3. Interfaces and API Contracts
- [ ] Define input parameters and validation
- [ ] Specify output format and types
- [ ] Document error taxonomy with status codes
- [ ] Define versioning strategy
- [ ] Specify idempotency requirements
- [ ] Set timeout and retry policies

### 4. Non-Functional Requirements (NFRs)
**Performance**:
- [ ] Specify p50, p95, p99 latency targets
- [ ] Define throughput requirements (RPS)
- [ ] Set resource caps (CPU, memory, storage)

**Reliability**:
- [ ] Define SLOs (uptime, error rate)
- [ ] Set error budgets
- [ ] Plan degradation strategy

**Security**:
- [ ] Define authentication mechanism
- [ ] Specify authorization model
- [ ] Document data encryption requirements
- [ ] Plan secrets management approach
- [ ] Specify auditing requirements

**Cost**:
- [ ] Estimate unit economics
- [ ] Set budget constraints

### 5. Data Management
- [ ] Identify source of truth
- [ ] Plan schema evolution strategy
- [ ] Document migration approach
- [ ] Define rollback procedures
- [ ] Set data retention policies

### 6. Operational Readiness
- [ ] Define logging requirements (structured, levels)
- [ ] Specify metrics to collect
- [ ] Plan distributed tracing approach
- [ ] Set alerting thresholds
- [ ] Document on-call ownership
- [ ] Create runbooks for common tasks
- [ ] Define deployment strategy
- [ ] Plan rollback procedures
- [ ] Consider feature flags

### 7. Risk Analysis
- [ ] Identify top 3 risks
- [ ] Assess likelihood and impact
- [ ] Define blast radius for each
- [ ] Plan kill switches/guardrails
- [ ] Document mitigation strategies

### 8. Evaluation and Validation
- [ ] Define test coverage targets
- [ ] Specify required test types
- [ ] Plan security/vulnerability scans
- [ ] Define acceptance criteria
- [ ] Set output validation requirements

### 9. ADR Identification
For each significant decision:
- [ ] **Impact**: Long-term consequences? (architecture/platform/security)
- [ ] **Alternatives**: Multiple viable options considered?
- [ ] **Scope**: Cross-cutting concern?
- [ ] If ALL YES → Suggest ADR to user

## Plan Documentation

**Technical Context**:
- [ ] Language/Version specified
- [ ] Primary dependencies listed
- [ ] Storage solution defined
- [ ] Testing approach documented
- [ ] Target platform identified
- [ ] Project type selected
- [ ] Performance goals set
- [ ] Constraints documented
- [ ] Scale/scope defined

**Project Structure**:
- [ ] Documentation structure defined
- [ ] Source code structure chosen (single/web/mobile)
- [ ] Concrete paths specified (no placeholders)
- [ ] Unused options removed
- [ ] Structure decision documented

**Constitution Check (Final)**:
- [ ] All gates evaluated
- [ ] Pass/fail documented for each
- [ ] Violations justified in Complexity Tracking

**Completeness**:
- [ ] No TODO markers
- [ ] No NEEDS CLARIFICATION (or justified)
- [ ] No [PLACEHOLDER] fields
- [ ] No "Option 1/2/3" labels
- [ ] No [ACTION REQUIRED] comments

## Post-Planning

**Validation**:
- [ ] Run `check_plan_completeness.py`
- [ ] Run `extract_adr_candidates.py`
- [ ] Review all high-priority ADR suggestions
- [ ] Ensure consistency with spec.md
- [ ] Verify alignment with constitution

**ADR Suggestions**:
- [ ] Apply 3-part test to all candidates
- [ ] Suggest ADRs to user (don't auto-create)
- [ ] Use format: "📋 Architectural decision detected: [brief]"
- [ ] Wait for user consent before creating

**Handoff to Implementation**:
- [ ] Plan reviewed and approved
- [ ] ADRs created (if applicable)
- [ ] Ready for `/sp.tasks` to generate task breakdown

## Common Pitfalls to Avoid

**Scope Creep**:
- ❌ Adding features beyond spec
- ✅ Stick to spec requirements, document future enhancements as out-of-scope

**Vague NFRs**:
- ❌ "Should be fast and reliable"
- ✅ "p95 latency <200ms, 99.9% uptime"

**Undocumented Decisions**:
- ❌ Choosing technology without rationale
- ✅ Document alternatives, tradeoffs, rationale

**Ignoring Constitution**:
- ❌ Violating principles without justification
- ✅ Check constitution, justify violations

**Missing Error Handling**:
- ❌ Only documenting happy path
- ✅ Define error taxonomy, retry policies, degradation

**No Operational Plan**:
- ❌ Focusing only on development
- ✅ Plan monitoring, alerting, deployment, rollback

**Over-engineering**:
- ❌ Adding complexity for hypothetical future needs
- ✅ Smallest viable change, defer complexity

**Auto-creating ADRs**:
- ❌ Creating ADRs without user consent
- ✅ Suggest ADRs, wait for approval

## Decision Matrix (Quick Reference)

| Decision Type | ADR? | Document In |
|--------------|------|-------------|
| Framework selection (Next.js vs Remix) | YES | ADR |
| Database technology (Postgres vs Mongo) | YES | ADR |
| Auth approach (OAuth vs JWT vs sessions) | YES | ADR |
| Deployment strategy (blue-green vs canary) | YES | ADR |
| Variable naming convention | NO | PHR/code |
| Button color | NO | Design doc |
| Single function optimization | NO | PHR note |
| Component-specific pattern | NO | Code comment |

## Time-Saving Tips

**Use Progressive Disclosure**:
- Start with high-level plan
- Load detailed guidelines only when needed
- Reference specific sections of `architect-guidelines.md`

**Leverage Scripts**:
- Use `check_plan_completeness.py` for validation
- Use `extract_adr_candidates.py` to identify decisions
- Automate repetitive checks

**Reuse Patterns**:
- Reference previous plans for similar features
- Follow established project patterns
- Copy structure from template

**Collaborate**:
- Ask clarifying questions early
- Get stakeholder input on significant decisions
- Review with team before finalizing

## References

- Architect Guidelines: `references/architect-guidelines.md`
- ADR Significance Test: `references/adr-significance-test.md`
- Plan Structure: `references/plan-structure.md`
- Constitution Integration: `references/constitution-integration.md`
- Plan Template: `.specify/templates/plan-template.md`
