#!/usr/bin/env python3
"""Validate the agent-ready-skills repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = ["Purpose", "Inputs", "Workflow", "Output", "Validation"]
NAME_RE = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")


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


def main(argv: list[str]) -> int:
    root = Path(argv[1]).resolve() if len(argv) > 1 else Path.cwd().resolve()
    skills_dir = root / "skills"
    if not skills_dir.exists():
        fail(f"{skills_dir} does not exist")

    skill_dirs = sorted(path for path in skills_dir.iterdir() if path.is_dir())
    if len(skill_dirs) < 10:
        fail(f"expected at least 10 skills, found {len(skill_dirs)}")

    issues: list[str] = []
    for skill_dir in skill_dirs:
        issues.extend(validate_skill(skill_dir))

    if issues:
        for issue in issues:
            print(f"ERROR: {issue}")
        return 1

    print(f"OK: validated {len(skill_dirs)} skills in {skills_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
