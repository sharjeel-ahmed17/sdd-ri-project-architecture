# Architectural Planning Guidelines

This document provides the complete framework for creating comprehensive architectural plans. Use these guidelines when designing system architecture for new features or major changes.

## Table of Contents
1. [Scope and Dependencies](#1-scope-and-dependencies)
2. [Key Decisions and Rationale](#2-key-decisions-and-rationale)
3. [Interfaces and API Contracts](#3-interfaces-and-api-contracts)
4. [Non-Functional Requirements (NFRs) and Budgets](#4-non-functional-requirements-nfrs-and-budgets)
5. [Data Management and Migration](#5-data-management-and-migration)
6. [Operational Readiness](#6-operational-readiness)
7. [Risk Analysis and Mitigation](#7-risk-analysis-and-mitigation)
8. [Evaluation and Validation](#8-evaluation-and-validation)
9. [Architecture Decision Record (ADR)](#9-architecture-decision-record-adr)

---

## 1. Scope and Dependencies

Define clear boundaries for what is and isn't included in this architectural plan.

### In Scope
- **Boundaries**: Clear definition of system boundaries and interfaces
- **Key Features**: Primary capabilities and functionality to be delivered
- **Components**: Major architectural components and their responsibilities

### Out of Scope
- **Explicitly Excluded**: Items that won't be addressed in this iteration
- **Future Work**: Potential enhancements deferred to later phases
- **Related but Separate**: Adjacent concerns handled elsewhere

### External Dependencies
- **Systems**: External services, APIs, or platforms required
- **Teams**: Other teams whose work this depends on or impacts
- **Ownership**: Clear assignment of who owns each dependency
- **Integration Points**: How and where external dependencies connect

**Decision Principle**: Make dependencies explicit and document ownership to prevent assumptions and reduce integration risk.

---

## 2. Key Decisions and Rationale

Document the major architectural decisions with clear reasoning.

### Decision Framework
For each significant decision:

**Options Considered**
- List 2-4 viable alternatives that were evaluated
- Include brief description of each option

**Trade-offs**
- Performance vs. simplicity
- Cost vs. capability
- Time-to-market vs. technical debt
- Flexibility vs. constraints

**Rationale**
- Why the chosen approach was selected
- What criteria weighted most heavily
- What assumptions underpin this decision

### Decision Principles
- **Measurable**: Decisions should have observable outcomes
- **Reversible**: Prefer decisions that can be changed if proven wrong
- **Smallest Viable Change**: Minimize scope and complexity
- **Testable**: Include verification criteria for decision correctness

**Example**:
```
Decision: Use PostgreSQL for primary data store
Options: PostgreSQL, MongoDB, DynamoDB
Trade-offs: PostgreSQL provides ACID guarantees and rich query capability but requires more operational overhead than DynamoDB
Rationale: Data model is highly relational; ACID guarantees are critical for financial transactions; team has deep PostgreSQL expertise
```

---

## 3. Interfaces and API Contracts

Define how components communicate with clear contracts.

### Public APIs
Document all external-facing APIs:

**Inputs**
- Request parameters, types, validation rules
- Required vs. optional fields
- Acceptable value ranges

**Outputs**
- Response structure and types
- Success response format
- Field meanings and constraints

**Errors**
- Error taxonomy and status codes
- Error response format
- Retry guidance for each error type

### Versioning Strategy
- How API versions are managed
- Deprecation policy and timelines
- Backward compatibility guarantees

### API Reliability
**Idempotency**
- Which operations are idempotent
- How idempotency is achieved (idempotency keys, natural idempotency)

**Timeouts**
- Expected response times (p50, p95, p99)
- Client timeout recommendations
- Server-side timeout policies

**Retries**
- Which operations are safe to retry
- Recommended retry strategies (exponential backoff, circuit breakers)
- Maximum retry limits

### Error Taxonomy
Define standard error categories with status codes:
- 400 Bad Request: Invalid input
- 401 Unauthorized: Authentication required
- 403 Forbidden: Insufficient permissions
- 404 Not Found: Resource doesn't exist
- 409 Conflict: State conflict (e.g., duplicate)
- 429 Too Many Requests: Rate limit exceeded
- 500 Internal Server Error: Unexpected server failure
- 503 Service Unavailable: Temporary unavailability

---

## 4. Non-Functional Requirements (NFRs) and Budgets

Specify measurable quality attributes and resource constraints.

### Performance
**Latency**
- p50, p95, p99 latency targets
- Acceptable ranges under normal and peak load

**Throughput**
- Requests per second (RPS) target
- Concurrent user capacity
- Data processing rate (if applicable)

**Resource Caps**
- CPU limits (cores, utilization %)
- Memory limits (RAM allocation)
- Storage limits (disk space, IOPS)
- Network bandwidth requirements

### Reliability
**SLOs (Service Level Objectives)**
- Uptime target (e.g., 99.9% availability)
- Error rate threshold (e.g., <0.1% error rate)
- Recovery time objective (RTO)
- Recovery point objective (RPO)

**Error Budgets**
- Acceptable downtime per month/quarter
- How budget is tracked and enforced
- Escalation when budget is exhausted

**Degradation Strategy**
- Graceful degradation approaches
- Fallback mechanisms
- Circuit breaker patterns

### Security
**Authentication & Authorization**
- Authentication mechanism (OAuth, API keys, JWT)
- Authorization model (RBAC, ABAC)
- Session management

**Data Handling**
- Encryption at rest and in transit
- PII/sensitive data identification
- Data classification levels

**Secrets Management**
- How secrets are stored (vault, secrets manager)
- Secret rotation policies
- Access control for secrets

**Auditing**
- What events are logged
- Audit log retention
- Compliance requirements

### Cost
**Unit Economics**
- Cost per request/transaction
- Cost per user
- Infrastructure cost breakdown
- Budget constraints and thresholds

---

## 5. Data Management and Migration

Define how data is stored, accessed, and evolved.

### Source of Truth
- Identify authoritative data sources
- Document data ownership
- Define read/write patterns

### Schema Evolution
- Schema versioning strategy
- Forward/backward compatibility approach
- Schema validation mechanisms

### Migration and Rollback
**Migration Strategy**
- How schema changes are deployed
- Data migration approach (online, offline, hybrid)
- Migration validation and testing

**Rollback Plan**
- How to revert schema changes
- Data rollback procedures
- Rollback validation criteria

### Data Retention
- Retention policies for different data types
- Archival strategy
- Data deletion procedures
- Compliance with data regulations (GDPR, CCPA)

---

## 6. Operational Readiness

Ensure the system can be operated, monitored, and maintained.

### Observability
**Logs**
- Structured logging format (JSON)
- Log levels and when to use each
- Log aggregation and retention

**Metrics**
- Key performance indicators (KPIs)
- Business metrics
- Technical metrics (latency, error rate, throughput)
- Resource utilization metrics

**Traces**
- Distributed tracing approach
- Trace sampling strategy
- Trace correlation across services

### Alerting
**Thresholds**
- When alerts fire (thresholds, conditions)
- Alert severity levels (critical, warning, info)

**On-call Owners**
- Who receives alerts
- Escalation policies
- Response time expectations

### Runbooks
Document procedures for common operational tasks:
- Deployment procedures
- Rollback procedures
- Incident response
- Common troubleshooting steps
- Capacity scaling

### Deployment and Rollback
**Deployment Strategy**
- Blue-green, canary, rolling deployment
- Deployment validation gates
- Smoke tests and health checks

**Rollback Strategy**
- Automatic vs. manual rollback triggers
- Rollback time target
- Data consistency during rollback

### Feature Flags and Compatibility
- Feature flag strategy for gradual rollout
- Kill switch for emergency disable
- Feature flag lifecycle management

---

## 7. Risk Analysis and Mitigation

Identify and plan for potential failures.

### Top 3 Risks
For each significant risk:

**Risk Description**
- What could go wrong
- Likelihood (low, medium, high)
- Impact (low, medium, high)

**Blast Radius**
- Scope of impact if risk materializes
- Affected systems, users, or data

**Kill Switches / Guardrails**
- Circuit breakers
- Rate limiters
- Feature flags for emergency disable
- Automated rollback triggers
- Manual intervention procedures

**Mitigation Plan**
- Preventive measures
- Detection mechanisms
- Response procedures
- Recovery steps

---

## 8. Evaluation and Validation

Define how success is measured and validated.

### Definition of Done
**Tests**
- Unit test coverage target (e.g., >80%)
- Integration test scenarios
- End-to-end test cases
- Performance/load tests
- Security tests

**Scans**
- Security vulnerability scanning
- Dependency audit
- Code quality analysis
- Compliance checks

### Output Validation
**Format**
- Output conforms to specified schema
- Data types are correct
- Required fields are present

**Requirements**
- All functional requirements met
- NFRs achieved within tolerances
- API contracts honored

**Safety**
- No security vulnerabilities introduced
- Data integrity preserved
- Error handling comprehensive

---

## 9. Architecture Decision Record (ADR)

For each significant architectural decision, create an ADR following the significance test in `adr-significance-test.md`.

### When to Create ADRs
Apply the 3-part significance test:
1. **Impact**: Long-term consequences?
2. **Alternatives**: Multiple viable options with tradeoffs?
3. **Scope**: Cross-cutting concern?

If ALL are true, suggest ADR creation to the user.

### ADR Content
- **Decision**: What was decided
- **Context**: Why the decision was necessary
- **Consequences**: Positive and negative outcomes
- **Alternatives**: Other options considered and why rejected
- **References**: Links to spec, plan, related ADRs

See `adr-significance-test.md` for the complete test and examples.

---

## Usage Notes

- **Progressive Loading**: Load only the sections relevant to the current architectural question
- **Iterative Refinement**: Plans evolve through research → design → implementation phases
- **Constitution First**: Always check project-specific principles in `.specify/memory/constitution.md`
- **Template Adherence**: Follow `.specify/templates/plan-template.md` structure for output
