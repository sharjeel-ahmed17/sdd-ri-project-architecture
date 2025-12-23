#!/usr/bin/env python3
"""
Plan Completeness Validator

Checks if a plan.md file has all required sections and no unresolved placeholders.

Usage:
    python check_plan_completeness.py <path/to/plan.md>

Exit codes:
    0 - Plan is complete
    1 - Plan has issues (missing sections or placeholders)
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple

# Required sections in plan.md
REQUIRED_SECTIONS = [
    "Summary",
    "Technical Context",
    "Constitution Check",
    "Project Structure",
]

# Optional but recommended sections
RECOMMENDED_SECTIONS = [
    "Complexity Tracking",  # Only if violations exist
]

# Patterns indicating incomplete content
INCOMPLETE_PATTERNS = [
    r"\[TODO[:\]]",
    r"\[FEATURE\]",
    r"\[DATE\]",
    r"\[###-feature-name\]",
    r"NEEDS CLARIFICATION",
    r"\[ACTION REQUIRED\]",
    r"\[Option \d+:",  # Indicates un-chosen structure options
]


def read_file(file_path: Path) -> str:
    """Read file content."""
    try:
        return file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def extract_sections(content: str) -> List[str]:
    """Extract section headers from markdown content."""
    # Match headers: ## Section Name
    pattern = r'^##\s+(.+)$'
    return re.findall(pattern, content, re.MULTILINE)


def check_required_sections(sections: List[str]) -> Tuple[bool, List[str]]:
    """Check if all required sections are present."""
    missing = []
    for required in REQUIRED_SECTIONS:
        if not any(required.lower() in section.lower() for section in sections):
            missing.append(required)
    return len(missing) == 0, missing


def check_incomplete_patterns(content: str) -> Tuple[bool, List[Tuple[str, int]]]:
    """Check for incomplete placeholder patterns."""
    issues = []
    for pattern in INCOMPLETE_PATTERNS:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            # Find line number
            line_num = content[:match.start()].count('\n') + 1
            issues.append((match.group(0), line_num))
    return len(issues) == 0, issues


def check_technical_context_filled(content: str) -> Tuple[bool, List[str]]:
    """Check if Technical Context fields are filled."""
    context_section = re.search(
        r'##\s+Technical Context\s*(.+?)(?=##|\Z)',
        content,
        re.DOTALL | re.IGNORECASE
    )

    if not context_section:
        return False, ["Technical Context section not found"]

    context_content = context_section.group(1)

    # Required fields in Technical Context
    required_fields = [
        "Language/Version",
        "Primary Dependencies",
        "Testing",
        "Target Platform",
    ]

    missing = []
    for field in required_fields:
        if field not in context_content:
            missing.append(field)

    return len(missing) == 0, missing


def check_project_structure(content: str) -> Tuple[bool, List[str]]:
    """Check if Project Structure is concrete (no Option 1/2/3 remaining)."""
    structure_section = re.search(
        r'##\s+Project Structure\s*(.+?)(?=##|\Z)',
        content,
        re.DOTALL | re.IGNORECASE
    )

    if not structure_section:
        return False, ["Project Structure section not found"]

    structure_content = structure_section.group(1)

    issues = []

    # Check for un-removed option labels
    if re.search(r'Option \d+:', structure_content):
        issues.append("Project Structure contains 'Option X:' labels - remove unused options")

    # Check for REMOVE IF UNUSED markers
    if re.search(r'\[REMOVE IF UNUSED\]', structure_content, re.IGNORECASE):
        issues.append("Project Structure contains '[REMOVE IF UNUSED]' markers")

    return len(issues) == 0, issues


def validate_plan(file_path: Path) -> Tuple[bool, dict]:
    """Validate plan.md completeness."""
    print(f"Validating plan: {file_path}")
    print("-" * 60)

    content = read_file(file_path)
    sections = extract_sections(content)

    results = {
        'required_sections': check_required_sections(sections),
        'incomplete_patterns': check_incomplete_patterns(content),
        'technical_context': check_technical_context_filled(content),
        'project_structure': check_project_structure(content),
    }

    all_passed = all(result[0] for result in results.values())

    return all_passed, results


def print_results(passed: bool, results: dict):
    """Print validation results."""

    # Required Sections
    sections_ok, missing_sections = results['required_sections']
    if sections_ok:
        print("✓ All required sections present")
    else:
        print("✗ Missing required sections:")
        for section in missing_sections:
            print(f"  - {section}")
    print()

    # Incomplete Patterns
    patterns_ok, pattern_issues = results['incomplete_patterns']
    if patterns_ok:
        print("✓ No incomplete placeholders found")
    else:
        print("✗ Incomplete placeholders found:")
        for placeholder, line_num in pattern_issues:
            print(f"  Line {line_num}: {placeholder}")
    print()

    # Technical Context
    context_ok, context_issues = results['technical_context']
    if context_ok:
        print("✓ Technical Context complete")
    else:
        print("✗ Technical Context issues:")
        for issue in context_issues:
            print(f"  - {issue}")
    print()

    # Project Structure
    structure_ok, structure_issues = results['project_structure']
    if structure_ok:
        print("✓ Project Structure is concrete")
    else:
        print("✗ Project Structure issues:")
        for issue in structure_issues:
            print(f"  - {issue}")
    print()

    print("-" * 60)
    if passed:
        print("✓ Plan validation PASSED")
        print("\nThe plan appears complete and ready for review.")
    else:
        print("✗ Plan validation FAILED")
        print("\nPlease address the issues above before finalizing the plan.")


def main():
    if len(sys.argv) != 2:
        print("Usage: python check_plan_completeness.py <path/to/plan.md>")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    if not file_path.name == "plan.md":
        print(f"Warning: Expected 'plan.md', got '{file_path.name}'")

    passed, results = validate_plan(file_path)
    print_results(passed, results)

    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
