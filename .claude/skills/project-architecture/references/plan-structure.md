# Plan Structure and Phased Approach

This document explains the structure of plan.md files and the phased approach to architectural planning in the SDD-RI methodology.

## Plan.md Overview

The plan.md file is the central architectural planning document for a feature. It follows the template at `.specify/templates/plan-template.md` and is created by the `/sp.plan` command.

**Location**: `specs/<feature-id>-<feature-name>/plan.md`

**Purpose**: Document the technical approach, architecture decisions, and implementation strategy for a feature after reading the spec.md requirements.

---

## Three-Phase Planning Approach

### Phase 0: Research & Context Gathering

**Goal**: Understand the problem space and gather relevant context.

**Activities**:
1. Read feature specification (`spec.md`)
2. Review constitution for project principles
3. Explore existing codebase for patterns
4. Identify dependencies and constraints
5. Research technical options

**Output**: `specs/<feature>/research.md`

**Content**:
- Existing patterns discovered
- Relevant code sections identified
- Dependencies and constraints noted
- Initial technical observations
- Questions needing clarification

**Constitution Check**:
Before proceeding to Phase 1, verify the plan doesn't violate project principles in `.specify/memory/constitution.md`. Common gates:
- Complexity limits (e.g., max 3 projects/services)
- Prohibited patterns (e.g., avoid Repository pattern unless justified)
- Required practices (e.g., TDD, specific frameworks)
- Performance targets

---

### Phase 1: Design & Detailed Planning

**Goal**: Create comprehensive architectural design covering all aspects.

**Activities**:
1. Apply architectural guidelines (all 9 sections)
2. Design interfaces and contracts
3. Plan data models and storage
4. Define NFRs and operational requirements
5. Identify risks and mitigation strategies

**Outputs**:
- `specs/<feature>/plan.md` (primary artifact)
- `specs/<feature>/data-model.md` (if complex data modeling)
- `specs/<feature>/quickstart.md` (developer getting-started guide)
- `specs/<feature>/contracts/` (API contracts, interface definitions)

**Plan.md Structure**:

```markdown
# Implementation Plan: [Feature Name]

## Summary
[1-2 paragraph overview extracted from spec]

## Technical Context
- Language/Version
- Primary Dependencies
- Storage
- Testing approach
- Target Platform
- Project Type
- Performance Goals
- Constraints
- Scale/Scope

## Constitution Check
[Gates based on constitution - must pass before proceeding]

## Project Structure
### Documentation (this feature)
specs/<feature>/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
└── tasks.md (Phase 2)

### Source Code (repository root)
[Concrete directory structure for implementation]

## Complexity Tracking
[Only if Constitution Check has violations that must be justified]

## [Phase 1 Sections - Added During Planning]
... architectural details ...
```

**Phase 1 Content**: Apply the 9 architectural guidelines from `architect-guidelines.md`:
1. Scope and Dependencies
2. Key Decisions and Rationale
3. Interfaces and API Contracts
4. NFRs and Budgets
5. Data Management and Migration
6. Operational Readiness
7. Risk Analysis and Mitigation
8. Evaluation and Validation
9. ADR Suggestions (run significance test)

---

### Phase 2: Task Breakdown

**Goal**: Convert architectural plan into actionable, testable tasks.

**Activities**:
1. Review plan.md for implementation requirements
2. Break down into small, testable tasks
3. Identify task dependencies
4. Add acceptance criteria to each task
5. Order tasks by dependency chain

**Output**: `specs/<feature>/tasks.md`

**Created By**: `/sp.tasks` command (NOT `/sp.plan`)

**Task Structure**:
```markdown
# Tasks: [Feature Name]

## Task 1: [Task Name]
**Acceptance Criteria**:
- [ ] Criterion 1
- [ ] Criterion 2

**Dependencies**: None (or Task IDs)

**Test Cases**:
- Test scenario 1
- Test scenario 2
```

**Important**: Phase 2 is separate from `/sp.plan`. The plan describes the architecture; tasks describe the implementation steps.

---

## Plan Template Sections Explained

### 1. Summary
Extract the primary requirement and technical approach from the spec. Keep to 1-2 paragraphs.

### 2. Technical Context
Fill in concrete values or mark as "NEEDS CLARIFICATION":
- **Language/Version**: Runtime environment
- **Primary Dependencies**: Key libraries/frameworks
- **Storage**: Database or persistence mechanism
- **Testing**: Test framework and approach
- **Target Platform**: Where code runs
- **Project Type**: single/web/mobile (affects structure)
- **Performance Goals**: Measurable targets
- **Constraints**: Hard limits (latency, memory, etc.)
- **Scale/Scope**: Size indicators (users, LOC, screens)

### 3. Constitution Check
Gates that must pass before Phase 0 research, re-checked after Phase 1 design:
- Verify against principles in `.specify/memory/constitution.md`
- List any gates that must be validated
- Document pass/fail for each gate

### 4. Project Structure

#### Documentation Structure
Always include:
```
specs/<feature-id>-<feature-name>/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output (if applicable)
├── quickstart.md        # Phase 1 output (if applicable)
├── contracts/           # Phase 1 output (if applicable)
└── tasks.md             # Phase 2 output (from /sp.tasks)
```

#### Source Code Structure
Choose ONE structure based on project type:

**Option 1: Single Project** (default)
```
src/
├── models/
├── services/
├── cli/
└── lib/

tests/
├── contract/
├── integration/
└── unit/
```

**Option 2: Web Application** (frontend + backend detected)
```
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/
```

**Option 3: Mobile + API** (iOS/Android detected)
```
api/
└── [same as backend]

ios/ or android/
└── [platform-specific structure]
```

**Critical**: Replace placeholders with CONCRETE paths for this feature. Delete unused options.

### 5. Complexity Tracking
**Only fill if Constitution Check has violations.**

Table format:
| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| ... | ... | ... |

Purpose: Justify any complexity that exceeds project norms.

---

## Progressive Disclosure in Planning

### Start Lean
- Don't frontload all architectural details in initial plan
- Document the essentials: scope, key decisions, structure

### Expand as Needed
- Add detail when implementation begins
- Create supporting documents (data-model.md, contracts/) when complexity warrants
- Load relevant guideline sections on demand

### Keep Plan.md Focused
- Central navigation point
- Links to detailed sub-documents
- Avoids overwhelming context load

---

## Plan Evolution

Plans are living documents that evolve:

**Initial Creation** (`/sp.plan`):
- Phase 0: Research
- Phase 1: Design
- Constitution validation
- Structure definition

**During Implementation**:
- Refine NFRs based on measurement
- Update risk analysis as issues emerge
- Add ADRs for new significant decisions
- Adjust scope based on learnings

**Post-Implementation**:
- Document actual vs. planned outcomes
- Capture lessons learned
- Update architectural patterns for future reference

---

## Integration with Other Artifacts

### Upstream (Input)
- **spec.md**: Feature requirements and user needs
- **constitution.md**: Project principles and constraints

### Peer (Supporting)
- **research.md**: Context gathering from Phase 0
- **data-model.md**: Detailed data modeling
- **quickstart.md**: Developer onboarding
- **contracts/**: API specifications

### Downstream (Output)
- **tasks.md**: Implementation task breakdown
- **ADRs**: Architectural decision records
- **PHRs**: Prompt history records of work

---

## Common Patterns

### Starting a New Feature Plan
1. Run `/sp.plan` or equivalent
2. Agent reads spec.md
3. Agent performs Phase 0 research
4. Agent checks constitution
5. Agent creates plan.md with Phase 1 design
6. Agent suggests ADRs for significant decisions
7. User reviews and approves
8. Later: Run `/sp.tasks` to create tasks.md

### Updating an Existing Plan
1. Identify what changed (requirements, constraints, learnings)
2. Update relevant sections
3. Note changes in plan history or PHR
4. Re-run constitution check if structure changed
5. Suggest new ADRs if significant decisions changed

### Multi-Phase Features
For large features spanning multiple iterations:
1. Create high-level plan covering all phases
2. Detail only current phase implementation
3. Mark future phases as "deferred detail"
4. Revisit and detail future phases when ready

---

## Validation

Before considering a plan complete:

**Completeness Check**:
- [ ] All template sections filled (no "TODO" or "NEEDS CLARIFICATION" without reason)
- [ ] Concrete project structure defined
- [ ] Constitution gates evaluated
- [ ] NFRs specified with measurable targets
- [ ] Risks identified with mitigation plans
- [ ] Integration points documented

**Quality Check**:
- [ ] Decisions have clear rationale
- [ ] Alternatives were considered
- [ ] Trade-offs are explicit
- [ ] Success criteria defined
- [ ] ADRs suggested for significant decisions

**Consistency Check**:
- [ ] Aligns with spec.md requirements
- [ ] Respects constitution.md principles
- [ ] Consistent with existing architecture patterns
- [ ] Realistic given constraints

Use `scripts/check_plan_completeness.py` for automated validation.

---

## References

- Plan Template: `.specify/templates/plan-template.md`
- Architect Guidelines: `references/architect-guidelines.md`
- ADR Significance Test: `references/adr-significance-test.md`
- Constitution: `.specify/memory/constitution.md`
- Spec Template: `.specify/templates/spec-template.md`
- Tasks Template: `.specify/templates/tasks-template.md`
