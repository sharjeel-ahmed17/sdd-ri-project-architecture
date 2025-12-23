# Constitution Integration

This document explains how to integrate project-specific principles from the constitution file into architectural planning.

## What is the Constitution?

**Location**: `.specify/memory/constitution.md`

**Purpose**: Document project-specific principles, constraints, standards, and non-negotiable requirements that guide all development decisions.

**Scope**: Project-wide rules that apply to every feature, not feature-specific requirements.

---

## Constitution Content Areas

### 1. Code Quality Standards
- Code style and formatting rules
- Naming conventions
- Documentation requirements
- Code review standards
- Complexity limits (cyclomatic complexity, file size, function length)

### 2. Testing Requirements
- Minimum test coverage (e.g., >80%)
- Required test types (unit, integration, e2e)
- Test-driven development (TDD) requirements
- Test naming conventions
- Mock/stub policies

### 3. Performance Targets
- Latency requirements (p50, p95, p99)
- Throughput targets (RPS, concurrent users)
- Resource constraints (CPU, memory, disk)
- Bundle size limits (for frontend)
- Database query limits

### 4. Security Requirements
- Authentication/authorization standards
- Data encryption requirements
- Secret management policies
- API security practices
- Input validation requirements
- OWASP compliance

### 5. Architecture Principles
- Service/component limits (e.g., max 3 services)
- Preferred patterns (e.g., avoid Repository pattern)
- Required frameworks or libraries
- Prohibited dependencies
- Layering/separation requirements
- Microservices vs monolith guidance

### 6. Operational Standards
- Logging requirements
- Monitoring/observability standards
- Alerting policies
- Deployment practices
- Rollback requirements
- Feature flag usage

### 7. Data Management
- Database standards
- Schema migration practices
- Data retention policies
- Backup requirements
- Data privacy compliance (GDPR, CCPA)

### 8. Development Workflow
- Git workflow (branching, commits, PRs)
- PR review requirements
- CI/CD pipeline standards
- Environment management (dev, staging, prod)
- Release practices

---

## Constitution Check in Planning

### When to Check

**Phase 0 (Before Research)**:
- Verify proposed approach doesn't violate principles
- Identify any constitutional constraints that affect design

**Phase 1 (After Design)**:
- Re-validate against constitution
- Ensure all requirements met
- Document any necessary violations with justification

### How to Perform Check

1. **Read Constitution**: Load `.specify/memory/constitution.md`

2. **Extract Relevant Gates**: Identify principles that apply to this feature
   - Architecture limits
   - Technology constraints
   - Performance targets
   - Security requirements
   - Testing requirements

3. **Evaluate Compliance**:
   ```markdown
   ## Constitution Check

   *GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

   - [ ] Service count ≤ 3 (Current plan: 2 services)
   - [ ] Test coverage ≥ 80% (Planned: unit + integration tests)
   - [ ] p95 latency < 200ms (Target: 150ms p95)
   - [ ] No Repository pattern (Using direct data access)
   - [ ] TypeScript strict mode enabled (Configured in tsconfig.json)
   ```

4. **Document Pass/Fail**: Mark each gate as pass or fail

5. **Justify Violations**: If any gates fail, document in Complexity Tracking section

---

## Handling Constitution Violations

Sometimes a feature requires violating constitutional principles. Document these explicitly.

### Complexity Tracking Section

**Only complete if Constitution Check has violations.**

Format:
```markdown
## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| 4th service (exceeds 3-service limit) | Real-time notification service needed for push delivery | Polling from client: unacceptable latency; integrating into existing service: couples concerns, affects stability |
| Repository pattern (prohibited) | Legacy database requires complex ORM mapping | Direct SQL: 100+ tables with complex relations, unmaintainable |
```

**Requirements**:
- **Why Needed**: Specific technical reason, not preference
- **Alternatives**: What simpler approach was considered
- **Rejection Rationale**: Why simpler approach is insufficient

**Approval**: Violations typically require stakeholder approval before implementation.

---

## Constitution Evolution

Constitutions should evolve as projects mature:

### When to Update Constitution
- Repeated exceptions indicate a principle needs adjustment
- New requirements emerge (compliance, security)
- Technology choices change (new frameworks)
- Team grows and needs clearer standards
- Retrospectives reveal missing guidance

### When NOT to Update Constitution
- Single feature needs an exception (use Complexity Tracking instead)
- Personal preference conflicts with principle (follow constitution)
- Time pressure (constitution prevents technical debt)

### How to Update Constitution
1. Identify pattern requiring constitutional change
2. Discuss with team/stakeholders
3. Document rationale for change
4. Update `.specify/memory/constitution.md`
5. Consider creating ADR for the change
6. Communicate to all developers

---

## Constitution Examples

### Example 1: Minimal Constitution (Startup)
```markdown
# Project Constitution

## Code Standards
- TypeScript strict mode
- Prettier for formatting
- ESLint rules enforced
- Max file size: 300 lines

## Testing
- Coverage ≥ 70%
- Unit tests for business logic
- Integration tests for APIs

## Architecture
- Monolith (for now)
- No microservices without approval
- Postgres for persistence
```

### Example 2: Comprehensive Constitution (Enterprise)
```markdown
# Project Constitution

## Code Quality
- TypeScript strict mode, no `any` types
- ESLint rules: airbnb-typescript
- Max cyclomatic complexity: 10
- Max function length: 50 lines
- Max file size: 300 lines
- All public APIs documented with TSDoc

## Testing
- TDD required for new features
- Coverage ≥ 80% (unit + integration)
- E2E tests for critical user flows
- Performance tests for APIs (p95 < 200ms)
- Security tests (OWASP Top 10)

## Performance
- API p95 latency: <200ms
- Frontend bundle: <200KB gzipped
- Database queries: <100ms p95
- No N+1 queries

## Security
- OAuth 2.0 + JWT for auth
- All endpoints require authentication
- RBAC for authorization
- Secrets in AWS Secrets Manager
- PII encrypted at rest (AES-256)
- TLS 1.3 for all external communication

## Architecture
- Maximum 3 services
- No Repository pattern (direct data access)
- Event-driven communication between services
- PostgreSQL for transactional data
- Redis for caching/sessions
- AWS for infrastructure

## Operations
- Structured JSON logging
- Prometheus metrics for all services
- Distributed tracing (Jaeger)
- Health checks on all services
- Blue-green deployments
- Feature flags for gradual rollout
- Automated rollback on error rate >1%

## Development Workflow
- Git flow branching model
- PR reviews required (2 approvals)
- CI/CD: lint, test, build, deploy
- Staging environment required before prod
- No direct commits to main/master
```

---

## Integration with Planning Workflow

### Step-by-Step Integration

**1. Before Starting Plan**:
```bash
# Read constitution
cat .specify/memory/constitution.md
```

**2. During Phase 0 (Research)**:
- Check: Does proposed approach violate any principles?
- If yes: Can approach be adjusted? Or is violation justified?

**3. During Phase 1 (Design)**:
- Document Constitution Check section
- List all relevant gates
- Evaluate each gate (pass/fail)
- If violations: Complete Complexity Tracking table

**4. Before Finalizing Plan**:
- Verify all constitutional requirements addressed
- Ensure violations are justified
- Seek approval for violations if needed

**5. During Implementation** (Phase 2):
- Reference constitution for detailed requirements
- Validate implementation against standards
- Update Complexity Tracking if new violations discovered

---

## Common Constitution Anti-Patterns

### Anti-Pattern 1: Too Prescriptive
**Problem**: Constitution specifies implementation details
```markdown
❌ All API endpoints must use Express middleware in this exact order: cors, helmet, auth, logging
```

**Better**: Specify outcomes, not implementation
```markdown
✅ All API endpoints must: enable CORS, apply security headers, require authentication, emit access logs
```

### Anti-Pattern 2: Too Vague
**Problem**: Principles lack actionable guidance
```markdown
❌ Code should be clean and maintainable
```

**Better**: Specific, measurable standards
```markdown
✅ Functions max 50 lines, cyclomatic complexity ≤10, test coverage ≥80%
```

### Anti-Pattern 3: Inconsistent Enforcement
**Problem**: Some principles enforced, others ignored
- Solution: Automate checks where possible (linters, CI/CD gates)
- Solution: Make enforcement explicit (manual review, required approvals)

### Anti-Pattern 4: Never Updated
**Problem**: Constitution becomes outdated as project evolves
- Solution: Review constitution quarterly
- Solution: Update when repeated exceptions occur
- Solution: Document evolution in constitution itself (changelog section)

---

## Constitution Checklist for Architects

Before finalizing a plan, verify:

**Code Quality**:
- [ ] Standards defined and achievable
- [ ] Tooling configured (linters, formatters)
- [ ] Complexity limits specified

**Testing**:
- [ ] Coverage targets defined
- [ ] Test types specified
- [ ] Testing approach documented in plan

**Performance**:
- [ ] Latency targets defined
- [ ] Throughput requirements specified
- [ ] Resource constraints documented
- [ ] Plan addresses how targets will be met

**Security**:
- [ ] Auth/authz approach defined
- [ ] Data handling compliant
- [ ] Secrets management planned
- [ ] Security testing included

**Architecture**:
- [ ] Service/component limits respected
- [ ] Preferred patterns followed
- [ ] Prohibited patterns avoided or justified
- [ ] Dependencies approved

**Operations**:
- [ ] Logging/monitoring planned
- [ ] Deployment strategy defined
- [ ] Rollback approach documented
- [ ] Feature flags considered

**Violations**:
- [ ] All violations documented in Complexity Tracking
- [ ] Justifications provided
- [ ] Simpler alternatives considered
- [ ] Stakeholder approval obtained (if required)

---

## References

- Constitution File: `.specify/memory/constitution.md`
- Plan Template: `.specify/templates/plan-template.md`
- Architect Guidelines: `references/architect-guidelines.md`
- Plan Structure: `references/plan-structure.md`
