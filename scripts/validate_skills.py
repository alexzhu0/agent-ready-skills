#!/usr/bin/env python3
"""Validate the agent-ready-skills repository."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = ["Purpose", "Fit", "Inputs", "Workflow", "Output", "Validation"]
NAME_RE = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")
TRIGGER_TERMS = ("use when", "when", "converting", "reviewing", "turning", "summarizing")
SAFETY_EVIDENCE_TERMS = (
    "approval",
    "assumption",
    "auth",
    "evidence",
    "not fabricated",
    "not invented",
    "private",
    "privacy",
    "rollback",
    "secret",
    "security",
    "sensitive",
    "unknown",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def parse_frontmatter(text: str, path: Path) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail(f"{path} is missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail(f"{path} has unterminated YAML frontmatter")
    data: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        if not raw.strip():
            continue
        if ":" not in raw:
            fail(f"{path} has invalid frontmatter line: {raw}")
        key, value = raw.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def validate_skill(skill_dir: Path) -> list[str]:
    issues: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return [f"{skill_dir.name}: missing SKILL.md"]
    if not NAME_RE.fullmatch(skill_dir.name):
        issues.append(f"{skill_dir.name}: folder name must be lowercase kebab-case")

    text = skill_file.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text, skill_file)
    for key in ("name", "description"):
        if not frontmatter.get(key):
            issues.append(f"{skill_dir.name}: missing frontmatter {key}")
    if frontmatter.get("name") != skill_dir.name:
        issues.append(f"{skill_dir.name}: frontmatter name must match folder name")
    if len(frontmatter.get("description", "")) < 60:
        issues.append(f"{skill_dir.name}: description should be specific enough to trigger")

    for section in REQUIRED_SECTIONS:
        if f"## {section}" not in text:
            issues.append(f"{skill_dir.name}: missing ## {section}")
    return issues


def score_skill(skill_dir: Path) -> tuple[int, list[str]]:
    skill_file = skill_dir / "SKILL.md"
    text = skill_file.read_text(encoding="utf-8") if skill_file.exists() else ""
    frontmatter = parse_frontmatter(text, skill_file) if text else {}
    description = frontmatter.get("description", "")
    lower_description = description.lower()
    lower_text = text.lower()

    score = 0
    notes: list[str] = []

    if len(description) >= 100 and any(term in lower_description for term in TRIGGER_TERMS):
        score += 20
        notes.append("trigger clarity: 20/20")
    elif len(description) >= 60:
        score += 12
        notes.append("trigger clarity: 12/20")
    else:
        notes.append("trigger clarity: 0/20")

    section_points = 0
    for section in REQUIRED_SECTIONS:
        if f"## {section}" in text:
            section_points += 5
    score += section_points
    notes.append(f"required sections: {section_points}/30")

    validation_section = lower_text.split("## validation", 1)[1] if "## validation" in lower_text else ""
    if len(validation_section.strip()) >= 200:
        score += 20
        notes.append("validation guidance: 20/20")
    elif validation_section.strip():
        score += 10
        notes.append("validation guidance: 10/20")
    else:
        notes.append("validation guidance: 0/20")

    fit_section = lower_text.split("## fit", 1)[1].split("## inputs", 1)[0] if "## fit" in lower_text else ""
    if "use when" in fit_section and "do not use when" in fit_section:
        score += 15
        notes.append("fit boundary: 15/15")
    elif fit_section.strip():
        score += 8
        notes.append("fit boundary: 8/15")
    else:
        notes.append("fit boundary: 0/15")

    output_section = lower_text.split("## output", 1)[1].split("## validation", 1)[0] if "## output" in lower_text else ""
    if output_section.count("\n- ") >= 5:
        score += 10
        notes.append("actionable output: 10/10")
    elif output_section.strip():
        score += 5
        notes.append("actionable output: 5/10")
    else:
        notes.append("actionable output: 0/10")

    if any(term in lower_text for term in SAFETY_EVIDENCE_TERMS):
        score += 5
        notes.append("evidence/safety marker: 5/5")
    else:
        notes.append("evidence/safety marker: 0/5")

    return score, notes


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate agent-ready-skills.")
    parser.add_argument("root", nargs="?", default=".", help="Repository root to validate")
    parser.add_argument("--score", action="store_true", help="Print a simple quality score for each skill")
    return parser.parse_args(argv[1:])


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()
    skills_dir = root / "skills"
    if not skills_dir.exists():
        fail(f"{skills_dir} does not exist")

    skill_dirs = sorted(path for path in skills_dir.iterdir() if path.is_dir())
    if len(skill_dirs) < 20:
        fail(f"expected at least 20 skills, found {len(skill_dirs)}")

    issues: list[str] = []
    for skill_dir in skill_dirs:
        issues.extend(validate_skill(skill_dir))

    if issues:
        for issue in issues:
            print(f"ERROR: {issue}")
        return 1

    if args.score:
        for skill_dir in skill_dirs:
            score, notes = score_skill(skill_dir)
            print(f"SCORE {score:03d}/100 {skill_dir.name} - {'; '.join(notes)}")

    print(f"OK: validated {len(skill_dirs)} skills in {skills_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
