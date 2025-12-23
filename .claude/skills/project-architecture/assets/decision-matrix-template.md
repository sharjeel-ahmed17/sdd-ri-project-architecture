# Decision Matrix Template

Use this template to systematically compare architectural alternatives and document your decision-making process.

## Decision: [Brief Title]

**Context**: [1-2 sentences explaining why this decision is needed]

**Date**: [YYYY-MM-DD]

**Feature**: [Feature name or "General Architecture"]

---

## Evaluation Criteria

Weight each criterion by importance (1-5, where 5 is most important):

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Performance | __ | Latency, throughput, resource efficiency |
| Scalability | __ | Growth capacity, horizontal/vertical scaling |
| Maintainability | __ | Code clarity, debugging ease, long-term support |
| Developer Experience | __ | Learning curve, tooling, documentation |
| Cost | __ | Infrastructure, licensing, operational costs |
| Security | __ | Attack surface, compliance, data protection |
| Flexibility | __ | Adaptability to changing requirements |
| Time to Market | __ | Implementation speed, setup complexity |
| Ecosystem | __ | Community support, libraries, integrations |
| Team Familiarity | __ | Existing expertise, training needs |

---

## Alternatives Comparison

### Alternative 1: [Name]

**Description**: [Brief overview]

**Pros**:
-
-
-

**Cons**:
-
-
-

**Scoring**:
| Criterion | Score (1-10) | Weighted Score | Notes |
|-----------|--------------|----------------|-------|
| Performance | __ | __ | |
| Scalability | __ | __ | |
| Maintainability | __ | __ | |
| Developer Experience | __ | __ | |
| Cost | __ | __ | |
| Security | __ | __ | |
| Flexibility | __ | __ | |
| Time to Market | __ | __ | |
| Ecosystem | __ | __ | |
| Team Familiarity | __ | __ | |
| **TOTAL** | | **__** | |

---

### Alternative 2: [Name]

**Description**: [Brief overview]

**Pros**:
-
-
-

**Cons**:
-
-
-

**Scoring**:
| Criterion | Score (1-10) | Weighted Score | Notes |
|-----------|--------------|----------------|-------|
| Performance | __ | __ | |
| Scalability | __ | __ | |
| Maintainability | __ | __ | |
| Developer Experience | __ | __ | |
| Cost | __ | __ | |
| Security | __ | __ | |
| Flexibility | __ | __ | |
| Time to Market | __ | __ | |
| Ecosystem | __ | __ | |
| Team Familiarity | __ | __ | |
| **TOTAL** | | **__** | |

---

### Alternative 3: [Name]

**Description**: [Brief overview]

**Pros**:
-
-
-

**Cons**:
-
-
-

**Scoring**:
| Criterion | Score (1-10) | Weighted Score | Notes |
|-----------|--------------|----------------|-------|
| Performance | __ | __ | |
| Scalability | __ | __ | |
| Maintainability | __ | __ | |
| Developer Experience | __ | __ | |
| Cost | __ | __ | |
| Security | __ | __ | |
| Flexibility | __ | __ | |
| Time to Market | __ | __ | |
| Ecosystem | __ | __ | |
| Team Familiarity | __ | __ | |
| **TOTAL** | | **__** | |

---

## Summary

### Scores Overview

| Alternative | Total Score | Rank |
|-------------|-------------|------|
| [Alt 1 Name] | __ | __ |
| [Alt 2 Name] | __ | __ |
| [Alt 3 Name] | __ | __ |

### Recommendation

**Selected**: [Alternative Name]

**Rationale**: [2-3 sentences explaining why this alternative was chosen based on the scoring and context]

**Key Trade-offs Accepted**:
- [Trade-off 1]: [Why acceptable]
- [Trade-off 2]: [Why acceptable]

---

## Risk Assessment

**Risks Associated with Chosen Alternative**:

| Risk | Likelihood (L/M/H) | Impact (L/M/H) | Mitigation Strategy |
|------|-------------------|----------------|---------------------|
| | | | |
| | | | |

---

## Next Steps

1. [ ] Document decision in plan.md
2. [ ] Create ADR if significance test passes
3. [ ] Update technical context section
4. [ ] Verify against constitution
5. [ ] Get stakeholder approval (if needed)

---

## Example: Database Selection

### Decision: Primary Database Technology

**Context**: Need to select a database for storing user data, transactions, and analytics for our SaaS platform.

**Date**: 2025-12-23

**Feature**: User Management System

---

### Evaluation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Performance | 5 | Critical: p95 latency <50ms for reads |
| Scalability | 4 | Need to handle 100k users initially, 1M+ eventually |
| Maintainability | 3 | Team needs to manage and optimize queries |
| Developer Experience | 3 | Developer familiarity and tooling quality |
| Cost | 4 | Budget constraints for infrastructure |
| Security | 5 | Financial data, GDPR compliance critical |
| Flexibility | 2 | Schema will evolve but is mostly relational |
| Time to Market | 4 | Launch in 3 months |
| Ecosystem | 3 | Need good ORMs, migration tools |
| Team Familiarity | 4 | Current team expertise |

---

### Alternative 1: PostgreSQL

**Description**: Open-source relational database with ACID guarantees, rich query capabilities, and strong consistency.

**Pros**:
- ACID guarantees for financial transactions
- Rich query capabilities (joins, aggregations)
- Strong security features (row-level security, encryption)
- Team has 5 years PostgreSQL experience
- Excellent ecosystem (ORMs, tools, extensions)

**Cons**:
- Vertical scaling limits
- More operational overhead than managed NoSQL
- Requires careful index management at scale

**Scoring**:
| Criterion | Score (1-10) | Weighted Score | Notes |
|-----------|--------------|----------------|-------|
| Performance | 8 | 40 | Excellent with proper indexing |
| Scalability | 7 | 28 | Vertical + read replicas |
| Maintainability | 8 | 24 | SQL is expressive, good tools |
| Developer Experience | 9 | 27 | Team loves it |
| Cost | 7 | 28 | Reasonable cloud costs |
| Security | 9 | 45 | Battle-tested security features |
| Flexibility | 7 | 14 | JSON support for flexibility |
| Time to Market | 9 | 36 | Team expertise speeds development |
| Ecosystem | 9 | 27 | Mature ecosystem |
| Team Familiarity | 10 | 40 | Deep expertise |
| **TOTAL** | | **309** | |

---

### Alternative 2: MongoDB

**Description**: Document-oriented NoSQL database with flexible schema and horizontal scaling.

**Pros**:
- Horizontal scaling easier
- Flexible schema (good for rapid iteration)
- High write throughput
- Managed service (Atlas) reduces ops burden

**Cons**:
- Eventual consistency can complicate financial transactions
- Limited join capabilities (requires application-level joins)
- Team has minimal MongoDB experience
- Complex queries harder to write and optimize

**Scoring**:
| Criterion | Score (1-10) | Weighted Score | Notes |
|-----------|--------------|----------------|-------|
| Performance | 7 | 35 | Fast writes, reads need tuning |
| Scalability | 9 | 36 | Excellent horizontal scaling |
| Maintainability | 6 | 18 | Aggregation pipelines complex |
| Developer Experience | 5 | 15 | Learning curve for team |
| Cost | 6 | 24 | Atlas pricing adds up |
| Security | 7 | 35 | Good but fewer features than PG |
| Flexibility | 9 | 18 | Schema flexibility ideal |
| Time to Market | 5 | 20 | Learning curve delays launch |
| Ecosystem | 7 | 21 | Good but less mature for our stack |
| Team Familiarity | 3 | 12 | Minimal experience |
| **TOTAL** | | **234** | |

---

### Alternative 3: DynamoDB

**Description**: AWS managed NoSQL key-value and document database with infinite scaling.

**Pros**:
- Infinite horizontal scaling
- Fully managed (no ops burden)
- Excellent for high-throughput workloads
- Strong AWS integration

**Cons**:
- Vendor lock-in to AWS
- Limited query flexibility (requires careful data modeling)
- Eventually consistent by default
- Complex pricing model
- Team has no DynamoDB experience

**Scoring**:
| Criterion | Score (1-10) | Weighted Score | Notes |
|-----------|--------------|----------------|-------|
| Performance | 8 | 40 | Single-digit ms latency |
| Scalability | 10 | 40 | Infinite scaling |
| Maintainability | 5 | 15 | Data modeling complex |
| Developer Experience | 4 | 12 | Steep learning curve |
| Cost | 5 | 20 | Expensive at scale |
| Security | 8 | 40 | AWS security features |
| Flexibility | 4 | 8 | Rigid access patterns |
| Time to Market | 4 | 16 | Learning curve + modeling time |
| Ecosystem | 6 | 18 | AWS-centric |
| Team Familiarity | 2 | 8 | No experience |
| **TOTAL** | | **217** | |

---

### Summary

#### Scores Overview

| Alternative | Total Score | Rank |
|-------------|-------------|------|
| PostgreSQL | 309 | 1 |
| MongoDB | 234 | 2 |
| DynamoDB | 217 | 3 |

#### Recommendation

**Selected**: PostgreSQL

**Rationale**: PostgreSQL scored highest primarily due to team familiarity (critical for meeting 3-month deadline), strong security features (essential for financial data and GDPR), and ACID guarantees (required for transactional integrity). While MongoDB and DynamoDB offer superior horizontal scalability, our initial 100k user target is well within PostgreSQL's capabilities with read replicas. The team's 5 years of PostgreSQL experience significantly reduces time to market risk.

**Key Trade-offs Accepted**:
- **Vertical scaling limits**: Acceptable because we can scale to 1M+ users with read replicas and partitioning. By the time we need more, we'll have resources to migrate if necessary.
- **Operational overhead**: Mitigated by using managed PostgreSQL (AWS RDS) with automated backups, patching, and monitoring.

---

### Risk Assessment

**Risks Associated with PostgreSQL**:

| Risk | Likelihood (L/M/H) | Impact (L/M/H) | Mitigation Strategy |
|------|-------------------|----------------|---------------------|
| Scaling bottlenecks at 1M+ users | M | M | Monitor query performance, implement caching layer (Redis), plan for read replicas and partitioning early |
| Single-region writes | M | L | Start with single region, plan multi-region architecture in phase 2 if needed |
| Schema migration complexity | L | M | Use migration tools (Flyway/Liquibase), test migrations in staging, maintain rollback scripts |

---

### Next Steps

1. [x] Document decision in plan.md
2. [ ] Create ADR (passes significance test: high impact, alternatives considered, cross-cutting)
3. [x] Update technical context: "Storage: PostgreSQL 15 (AWS RDS)"
4. [x] Verify against constitution: Passes (no database restrictions)
5. [ ] Get stakeholder approval: Schedule architecture review

---

## Usage Notes

- **Customize criteria**: Adjust weights and criteria based on your project's priorities
- **Be objective**: Score based on facts, not preferences
- **Document assumptions**: Note any assumptions in the "Notes" column
- **Iterate**: Update scores as you learn more during research
- **Keep concise**: This is a tool to structure thinking, not exhaustive documentation
- **Use for significant decisions**: Don't matrix every decision; reserve for ADR-worthy choices
