#!/usr/bin/env python3
"""
ADR Candidate Extractor

Analyzes a plan.md file to identify potential architectural decisions that may warrant ADRs.
Looks for decision language, alternatives considered, and tradeoff discussions.

Usage:
    python extract_adr_candidates.py <path/to/plan.md>

Output:
    List of potential ADR-worthy decisions with significance assessment
"""

import sys
import re
from pathlib import Path
from typing import List, Dict, Tuple

# Keywords indicating decision-making
DECISION_KEYWORDS = [
    r'\bchoose\b', r'\bchosen\b', r'\bselect\b', r'\bselected\b',
    r'\bdecide\b', r'\bdecided\b', r'\bdecision\b',
    r'\bopt for\b', r'\bopting\b', r'\badopt\b', r'\badopted\b',
    r'\buse\b', r'\busing\b', r'\bemploy\b',
]

# Keywords indicating alternatives were considered
ALTERNATIVES_KEYWORDS = [
    r'\balternative\b', r'\boption\b', r'\bvs\b', r'\bversus\b',
    r'\binstead of\b', r'\brather than\b', r'\bconsidered\b',
    r'\bevaluated\b', r'\bcompared\b', r'\brejected\b',
]

# Keywords indicating tradeoffs
TRADEOFF_KEYWORDS = [
    r'\btradeoff\b', r'\btrade-off\b', r'\bpros\b', r'\bcons\b',
    r'\badvantage\b', r'\bdisadvantage\b', r'\bbenefit\b',
    r'\bdrawback\b', r'\blimitation\b', r'\bcost\b',
]

# High-impact areas (architectural significance)
HIGH_IMPACT_AREAS = [
    r'\barchitecture\b', r'\bframework\b', r'\bdatabase\b',
    r'\bauth\b', r'\bauthentication\b', r'\bauthorization\b',
    r'\bservice\b', r'\bmicroservice\b', r'\bmonolith\b',
    r'\bAPI\b', r'\bREST\b', r'\bGraphQL\b', r'\bgRPC\b',
    r'\bdeployment\b', r'\binfrastructure\b', r'\bcloud\b',
    r'\bsecurity\b', r'\bencryption\b', r'\bcaching\b',
    r'\bmessaging\b', r'\bevent\b', r'\bqueue\b',
]


def read_file(file_path: Path) -> str:
    """Read file content."""
    try:
        return file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def extract_sections(content: str) -> Dict[str, str]:
    """Extract sections from plan.md."""
    sections = {}
    pattern = r'##\s+(.+?)\n(.*?)(?=\n##\s+|\Z)'
    matches = re.finditer(pattern, content, re.DOTALL)

    for match in matches:
        section_name = match.group(1).strip()
        section_content = match.group(2).strip()
        sections[section_name] = section_content

    return sections


def score_decision_language(text: str) -> int:
    """Score text based on decision-making language."""
    score = 0
    text_lower = text.lower()

    for keyword in DECISION_KEYWORDS:
        if re.search(keyword, text_lower):
            score += 1

    return score


def score_alternatives(text: str) -> int:
    """Score text based on alternatives consideration."""
    score = 0
    text_lower = text.lower()

    for keyword in ALTERNATIVES_KEYWORDS:
        if re.search(keyword, text_lower):
            score += 2  # Alternatives weigh more heavily

    return score


def score_tradeoffs(text: str) -> int:
    """Score text based on tradeoff discussion."""
    score = 0
    text_lower = text.lower()

    for keyword in TRADEOFF_KEYWORDS:
        if re.search(keyword, text_lower):
            score += 2  # Tradeoffs weigh more heavily

    return score


def score_impact(text: str) -> int:
    """Score text based on high-impact areas."""
    score = 0
    text_lower = text.lower()

    for area in HIGH_IMPACT_AREAS:
        if re.search(area, text_lower):
            score += 3  # High impact areas weigh most

    return score


def extract_paragraph_context(content: str, start_pos: int, context_size: int = 500) -> str:
    """Extract surrounding context for a match."""
    start = max(0, start_pos - context_size)
    end = min(len(content), start_pos + context_size)
    return content[start:end].strip()


def analyze_section(section_name: str, section_content: str) -> List[Dict]:
    """Analyze a section for ADR candidates."""
    candidates = []

    # Split into paragraphs
    paragraphs = [p.strip() for p in section_content.split('\n\n') if p.strip()]

    for para_idx, paragraph in enumerate(paragraphs):
        # Skip code blocks
        if paragraph.startswith('```') or paragraph.startswith('    '):
            continue

        # Calculate significance scores
        decision_score = score_decision_language(paragraph)
        alternatives_score = score_alternatives(paragraph)
        tradeoff_score = score_tradeoffs(paragraph)
        impact_score = score_impact(paragraph)

        total_score = decision_score + alternatives_score + tradeoff_score + impact_score

        # Threshold for potential ADR candidate
        if total_score >= 6:
            candidates.append({
                'section': section_name,
                'paragraph_idx': para_idx,
                'content': paragraph[:200] + ('...' if len(paragraph) > 200 else ''),
                'scores': {
                    'decision': decision_score,
                    'alternatives': alternatives_score,
                    'tradeoffs': tradeoff_score,
                    'impact': impact_score,
                    'total': total_score,
                },
            })

    return candidates


def assess_significance(candidate: Dict) -> Tuple[bool, str]:
    """Apply 3-part ADR significance test."""
    scores = candidate['scores']

    # Test 1: Impact (needs high impact score)
    has_impact = scores['impact'] >= 3

    # Test 2: Alternatives (needs alternatives discussion)
    has_alternatives = scores['alternatives'] >= 2

    # Test 3: Scope (inferred from section name and impact)
    section = candidate['section'].lower()
    cross_cutting_sections = ['architecture', 'technical context', 'key decisions', 'interfaces']
    is_cross_cutting = any(keyword in section for keyword in cross_cutting_sections)

    passes_all = has_impact and has_alternatives and is_cross_cutting

    # Generate assessment
    assessment_parts = []
    if not has_impact:
        assessment_parts.append("❓ Impact unclear (may be localized)")
    if not has_alternatives:
        assessment_parts.append("❓ Alternatives not evident")
    if not is_cross_cutting:
        assessment_parts.append("❓ May be feature-specific")

    if passes_all:
        assessment = "✅ Likely ADR candidate (passes all 3 tests)"
    elif len(assessment_parts) == 1:
        assessment = f"⚠️  Possible ADR candidate ({assessment_parts[0]})"
    else:
        assessment = f"ℹ️  Low priority ({'; '.join(assessment_parts)})"

    return passes_all, assessment


def extract_decision_title(content: str) -> str:
    """Extract a potential decision title from content."""
    # Look for sentences with decision keywords
    sentences = re.split(r'[.!?]', content)

    for sentence in sentences:
        sentence_lower = sentence.lower()
        if any(re.search(keyword, sentence_lower) for keyword in DECISION_KEYWORDS):
            # Clean and truncate
            title = sentence.strip()
            title = re.sub(r'^(we|the|this)\s+', '', title, flags=re.IGNORECASE)
            if len(title) > 80:
                title = title[:77] + '...'
            return title

    return "Decision in " + content[:50] + "..."


def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_adr_candidates.py <path/to/plan.md>")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    print(f"Analyzing plan: {file_path}")
    print("=" * 80)
    print()

    content = read_file(file_path)
    sections = extract_sections(content)

    all_candidates = []

    # Analyze each section
    for section_name, section_content in sections.items():
        candidates = analyze_section(section_name, section_content)
        all_candidates.extend(candidates)

    if not all_candidates:
        print("No potential ADR candidates found.")
        print()
        print("This could mean:")
        print("  - The plan doesn't document architectural decisions")
        print("  - Decisions are made but not documented with alternatives/tradeoffs")
        print("  - The plan is still in early stages")
        return

    # Sort by total score (highest first)
    all_candidates.sort(key=lambda c: c['scores']['total'], reverse=True)

    print(f"Found {len(all_candidates)} potential ADR candidates:")
    print()

    for idx, candidate in enumerate(all_candidates, 1):
        passes_test, assessment = assess_significance(candidate)

        decision_title = extract_decision_title(candidate['content'])

        print(f"{idx}. {assessment}")
        print(f"   Section: {candidate['section']}")
        print(f"   Suggested Title: {decision_title}")
        print(f"   Score: {candidate['scores']['total']} "
              f"(impact={candidate['scores']['impact']}, "
              f"alternatives={candidate['scores']['alternatives']}, "
              f"tradeoffs={candidate['scores']['tradeoffs']})")
        print(f"   Content: {candidate['content']}")
        print()

    # Summary
    high_priority = sum(1 for c in all_candidates if assess_significance(c)[0])
    print("=" * 80)
    print(f"Summary: {high_priority} high-priority candidates, "
          f"{len(all_candidates) - high_priority} lower-priority")
    print()
    print("Next Steps:")
    print("  1. Review high-priority candidates (✅)")
    print("  2. For each, apply the full 3-part significance test")
    print("  3. Suggest ADR to user: '📋 Architectural decision detected: <brief>'")
    print("     'Document reasoning and tradeoffs? Run `/sp.adr <decision-title>`'")


if __name__ == "__main__":
    main()
