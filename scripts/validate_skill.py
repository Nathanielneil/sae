#!/usr/bin/env python3
"""Run dependency-free structural checks for the bundled SAE skill."""

from __future__ import annotations

import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "sae"
SKILL_MD = SKILL_DIR / "SKILL.md"
OPENAI_YAML = SKILL_DIR / "agents" / "openai.yaml"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    for path in (SKILL_MD, OPENAI_YAML):
        if not path.is_file():
            fail(f"missing required file: {path.relative_to(ROOT)}")

    text = SKILL_MD.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        fail("SKILL.md must begin with YAML frontmatter")

    frontmatter = match.group(1)
    keys = []
    values: dict[str, str] = {}
    for line in frontmatter.splitlines():
        key, separator, value = line.partition(":")
        if not separator:
            fail(f"invalid frontmatter line: {line!r}")
        key = key.strip()
        keys.append(key)
        values[key] = value.strip()

    if keys != ["name", "description"]:
        fail("frontmatter must contain only name and description, in that order")
    if values["name"] != "sae":
        fail("skill name must be 'sae'")
    if not values["description"]:
        fail("skill description must not be empty")
    if any(token in text for token in ("[TODO", "TODO:", "placeholder")):
        fail("SKILL.md contains an unfinished template marker")
    if len(text.splitlines()) > 500:
        fail("SKILL.md exceeds the recommended 500-line limit")

    metadata = OPENAI_YAML.read_text(encoding="utf-8")
    required_fragments = (
        'display_name: "SAE"',
        "short_description:",
        'default_prompt: "Use $sae',
    )
    for fragment in required_fragments:
        if fragment not in metadata:
            fail(f"agents/openai.yaml is missing {fragment!r}")

    unexpected = [
        path.relative_to(SKILL_DIR)
        for path in SKILL_DIR.rglob("*")
        if path.is_file()
        and path not in {SKILL_MD, OPENAI_YAML}
        and path.name != ".DS_Store"
    ]
    if unexpected:
        fail(f"unexpected files in installable skill: {unexpected}")

    print("SAE skill validation passed.")


if __name__ == "__main__":
    main()

