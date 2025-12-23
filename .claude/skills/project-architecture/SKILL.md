---
name: project-architecture
description: Expert guidance for designing comprehensive software architectures following Spec-Driven Development methodology. Use when user requests to design architecture, create architectural plans, plan system design, or make technical approach decisions. Supports scope definition, interface design, NFR specification, data modeling, operational readiness planning, and intelligent ADR (Architecture Decision Record) suggestions for significant architectural decisions.
---

# Project Architecture

## Overview

This skill provides expert architectural planning guidance following the SDD-RI (Spec-Driven Development with Rigorous Implementation) methodology. It helps architects design robust, well-documented systems with proper decision tracking through ADRs.

## Core Workflow

### Phase 0: Research & Context Gathering
1. **Read the feature spec** (`specs/<feature>/spec.md`)
2. **Check constitution** (`.specify/memory/constitution.md`) for project principles and constraints
3. **Explore codebase** to understand existing patterns, dependencies, and architecture
4. **Document findings** in `specs/<feature>/research.md`

### Phase 1: Design & Planning
Create comprehensive plan covering all architectural aspects:

1. **Scope & Dependencies** - See `references/architect-guidelines.md` Section 1
2. **Key Decisions & Rationale** - See `references/architect-guidelines.md` Section 2
3. **Interfaces & API Contracts** - See `references/architect-guidelines.md` Section 3
4. **NFRs & Budgets** - See `references/architect-guidelines.md` Section 4
5. **Data Management** - See `references/architect-guidelines.md` Section 5
6. **Operational Readiness** - See `references/architect-guidelines.md` Section 6
7. **Risk Analysis** - See `references/architect-guidelines.md` Section 7
8. **Evaluation & Validation** - See `references/architect-guidelines.md` Section 8

Output: `specs/<feature>/plan.md` following `.specify/templates/plan-template.md`

### Phase 2: ADR Identification
After planning, identify architectural decisions requiring documentation:

- **Run the significance test** - See `references/adr-significance-test.md`
- **Suggest ADRs to user** using the format:
  ```
  📋 Architectural decision detected: [brief-description]
  Document reasoning and tradeoffs? Run `/sp.adr [decision-title]`
  ```
- **Wait for user consent** - Never auto-create ADRs

## Decision Tree

```
User Request
    │
    ├─ "Design architecture for..."
    │  └─> Load architect-guidelines.md → Follow Core Workflow
    │
    ├─ "What NFRs should I consider?"
    │  └─> Load architect-guidelines.md Section 4 (NFRs)
    │
    ├─ "Help with API contracts"
    │  └─> Load architect-guidelines.md Section 3 (Interfaces)
    │
    ├─ "Should this be an ADR?"
    │  └─> Load adr-significance-test.md → Apply test
    │
    └─ "Review my plan"
       └─> Use check_plan_completeness.py → Load relevant sections
```

## Resources

### references/
Detailed architectural guidelines organized by topic for progressive disclosure:

- **`architect-guidelines.md`** - Complete 9-section architectural framework extracted from CLAUDE.md
- **`adr-significance-test.md`** - The 3-part test for determining when decisions merit ADRs
- **`plan-structure.md`** - Details on plan.md structure and phased approach
- **`constitution-integration.md`** - How to integrate project-specific principles and constraints

Load these references as needed based on user's specific architectural questions.

### scripts/
Validation and analysis tools:

- **`check_plan_completeness.py`** - Validates plan.md has all required sections
- **`extract_adr_candidates.py`** - Parses a plan to identify potential ADR-worthy decisions

### assets/
Quick reference materials:

- **`plan-checklist.md`** - Architect's quick reference checklist
- **`decision-matrix-template.md`** - Template for comparing architectural alternatives

## Progressive Disclosure Strategy

1. **Start lean**: Use this SKILL.md for workflow guidance
2. **Load on demand**: Reference specific sections from `references/` based on user needs
3. **Use scripts**: Run validation/analysis tools without loading into context
4. **Provide assets**: Copy templates when user needs structured decision-making

## Integration Points

- **Input**: `specs/<feature>/spec.md` (feature requirements)
- **Constitution**: `.specify/memory/constitution.md` (project principles)
- **Templates**: `.specify/templates/plan-template.md` (output structure)
- **Output**: `specs/<feature>/plan.md` (architectural plan)
- **Follow-up**: ADR creation via `/sp.adr` command after significance test
