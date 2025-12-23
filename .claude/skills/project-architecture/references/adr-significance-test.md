# ADR Significance Test

This document defines the three-part test for determining when an architectural decision merits an Architecture Decision Record (ADR).

## The Three-Part Test

An architectural decision should be documented as an ADR if **ALL THREE** of these conditions are true:

### 1. Impact: Long-term Consequences
Does this decision have significant long-term consequences for:
- Architecture or system design
- Platform or infrastructure
- Security or compliance
- Developer experience or maintainability
- Scalability or performance at scale

**Examples that pass**:
- Choosing a web framework (affects structure for years)
- Selecting a database technology (hard to change later)
- Deciding authentication approach (security implications)
- Adopting microservices vs monolith (architectural impact)

**Examples that fail**:
- Naming a variable
- Choosing a CSS class name
- Picking an icon library
- Formatting code style

### 2. Alternatives: Multiple Viable Options
Were there multiple reasonable approaches with meaningful tradeoffs?

Must have:
- At least 2-3 legitimate alternatives considered
- Each option has distinct pros and cons
- No single "obviously correct" choice

**Examples that pass**:
- PostgreSQL vs MongoDB vs DynamoDB (each viable with tradeoffs)
- REST vs GraphQL vs gRPC (depends on requirements)
- JWT vs session tokens (different security/scalability tradeoffs)

**Examples that fail**:
- Using HTTPS (no real alternative)
- Following language conventions (standard practice)
- Fixing a bug (one correct approach)

### 3. Scope: Cross-cutting Concern
Does this decision affect multiple parts of the system or have broad implications?

Indicators:
- Affects multiple services/components
- Influences future architectural decisions
- Sets a pattern others will follow
- Impacts multiple teams or domains

**Examples that pass**:
- API authentication scheme (affects all endpoints)
- Service communication pattern (affects all services)
- Deployment strategy (affects all releases)
- Error handling approach (system-wide pattern)

**Examples that fail**:
- Implementation detail within a single function
- Component-specific optimization
- Localized refactoring
- Single endpoint behavior

---

## Decision Flow

```
Architectural Decision Made
    ↓
Does it have long-term impact? (Test 1)
    ├─ NO → Document in PHR, not ADR
    └─ YES ↓
        Were multiple viable options considered? (Test 2)
            ├─ NO → Document in PHR, not ADR
            └─ YES ↓
                Is it cross-cutting? (Test 3)
                    ├─ NO → Document in PHR, not ADR
                    └─ YES → Suggest ADR to user
```

---

## Suggested ADR Format

When ALL THREE tests pass, suggest to the user:

```
📋 Architectural decision detected: [brief-description]
   Document reasoning and tradeoffs? Run `/sp.adr [decision-title]`
```

**Example suggestions**:
- `📋 Architectural decision detected: Selection of PostgreSQL over NoSQL options. Document reasoning and tradeoffs? Run \`/sp.adr database-technology-choice\``
- `📋 Architectural decision detected: Adoption of event-driven architecture for service communication. Document reasoning and tradeoffs? Run \`/sp.adr event-driven-architecture\``
- `📋 Architectural decision detected: JWT-based authentication with refresh tokens. Document reasoning and tradeoffs? Run \`/sp.adr authentication-approach\``

---

## Grouping Related Decisions

When multiple related decisions are made together, group them into a single ADR:

**Good grouping** (single ADR):
- "Frontend Technology Stack" including: Framework (Next.js), Styling (Tailwind), State Management (React Context), Deployment (Vercel)
- "Authentication System" including: Auth provider (Auth0), Token type (JWT), Session management, Refresh strategy

**Bad grouping** (separate ADRs):
- Framework choice in ADR-001
- Styling library in ADR-002
- State management in ADR-003
- Deployment platform in ADR-004

**Why**: Related decisions work together as a cohesive system. Documenting them together shows how they reinforce each other and simplifies future reference.

---

## Examples: Pass vs Fail

### Example 1: Database Selection ✅ PASS
- **Impact**: YES - Long-term commitment, hard to change
- **Alternatives**: YES - PostgreSQL, MongoDB, DynamoDB all viable
- **Scope**: YES - Affects all data access patterns system-wide
- **Verdict**: Create ADR

### Example 2: Variable Naming Convention ❌ FAIL
- **Impact**: NO - Easy to refactor, minimal long-term consequence
- **Alternatives**: N/A - Multiple options but trivial differences
- **Scope**: NO - Localized to specific code sections
- **Verdict**: PHR note, not ADR

### Example 3: Caching Strategy ✅ PASS
- **Impact**: YES - Affects performance and consistency guarantees
- **Alternatives**: YES - Redis, Memcached, in-memory, HTTP caching
- **Scope**: YES - System-wide performance and consistency pattern
- **Verdict**: Create ADR

### Example 4: Button Color Choice ❌ FAIL
- **Impact**: NO - Easily changed, no architectural impact
- **Alternatives**: N/A - Aesthetic preference
- **Scope**: NO - UI-specific, doesn't influence system design
- **Verdict**: PHR note or design doc, not ADR

### Example 5: API Versioning Strategy ✅ PASS
- **Impact**: YES - Long-term maintenance and compatibility implications
- **Alternatives**: YES - URL versioning, header versioning, no versioning
- **Scope**: YES - Affects all API endpoints and client integrations
- **Verdict**: Create ADR

### Example 6: Single Function Optimization ❌ FAIL
- **Impact**: NO - Localized performance improvement
- **Alternatives**: YES - Multiple optimization approaches
- **Scope**: NO - Contained within one function
- **Verdict**: PHR note with explanation, not ADR
(Fails test 3 despite passing tests 1-2)

---

## Common Pitfalls

### Over-documenting (Creating ADRs When Not Needed)
- Documenting every technology choice, even minor ones
- Creating ADRs for implementation details
- Treating preferences as significant decisions

**Result**: ADR fatigue, important decisions buried in noise

### Under-documenting (Skipping ADRs When Needed)
- Assuming decisions are "obvious" without documenting alternatives
- Not recording tradeoffs for future reference
- Skipping documentation due to time pressure

**Result**: Lost context, repeated discussions, difficult onboarding

### The Right Balance
- Document decisions that pass ALL THREE tests
- Capture context in PHRs for other decisions
- Group related decisions to reduce ADR count
- Keep ADRs concise and focused on "why" not "what"

---

## Integration with Planning Workflow

ADR suggestions typically occur:
1. **During `/sp.plan`**: When making architectural decisions in the planning phase
2. **After design work**: When the design artifacts reveal significant decisions
3. **During implementation**: When unexpected architectural choices emerge

**Never auto-create ADRs** - Always suggest and wait for user consent:
- User may want to defer ADR creation
- User may want to modify the decision title
- User may want to group multiple decisions
- User may disagree that it meets significance threshold

---

## References

- ADR Template: `.specify/templates/adr-template.md`
- ADR Creation Command: `/sp.adr` or `create-adr.sh`
- ADR Storage: `history/adr/`
- Related: Prompt History Records (PHRs) for non-ADR decisions
