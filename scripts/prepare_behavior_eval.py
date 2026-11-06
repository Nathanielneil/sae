#!/usr/bin/env python3
"""Validate behavioral fixtures and optionally export inputs without their rubric.

This prepares an evaluation; it neither calls a model nor scores its output.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
CASE_KEYS = {
    "id", "focus", "request", "context", "source", "checks", "forbidden",
    "query", "query_topics",
}


def load_cases(path: pathlib.Path) -> list[dict]:
    suite = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(suite, dict) or set(suite) != {"schema_version", "cases"}:
        raise ValueError("expected schema_version and cases")
    if type(suite["schema_version"]) is not int or suite["schema_version"] != 1:
        raise ValueError("unsupported schema_version")
    cases = suite["cases"]
    if not isinstance(cases, list) or not cases:
        raise ValueError("cases must be a nonempty list")
    seen = set()
    for index, case in enumerate(cases, 1):
        if not isinstance(case, dict) or set(case) != CASE_KEYS:
            raise ValueError(f"case {index}: unexpected or missing fields")
        for key in ("id", "focus", "request", "context", "source", "query"):
            if not isinstance(case[key], str) or not case[key].strip():
                raise ValueError(f"case {index}: {key} must be nonempty text")
        case_id = case["id"]
        if not re.fullmatch(r"SAE-\d{3}", case_id) or case_id in seen:
            raise ValueError(f"case {index}: invalid or duplicate id {case_id!r}")
        seen.add(case_id)
        for key in ("checks", "forbidden", "query_topics"):
            values = case[key]
            if not isinstance(values, list) or any(
                not isinstance(value, str) or not value.strip() for value in values
            ):
                raise ValueError(f"{case_id}: {key} must be a list of nonempty text")
            if key != "query_topics" and not values:
                raise ValueError(f"{case_id}: {key} cannot be empty")
        if case["query"] not in {"none", "required", "clarify-first"}:
            raise ValueError(f"{case_id}: invalid query expectation")
        if bool(case["query_topics"]) != (case["query"] != "none"):
            raise ValueError(f"{case_id}: query_topics contradicts query expectation")
    return cases


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=pathlib.Path, default=ROOT / "tests/behavior_cases.json")
    parser.add_argument("--output", type=pathlib.Path, help="write prompt-only JSON for an evaluator")
    args = parser.parse_args()
    try:
        cases = load_cases(args.cases)
        if args.output:
            skill = (ROOT / "skills/sae/SKILL.md").read_bytes()
            payload = {
                "skill_sha256": hashlib.sha256(skill).hexdigest(),
                "cases_sha256": hashlib.sha256(args.cases.read_bytes()).hexdigest(),
                "inputs": [
                    {
                        "id": case["id"],
                        "prompt": (
                            f"{case['request']}\n\nContext:\n{case['context']}"
                            f"\n\nManuscript:\n{case['source']}"
                        ),
                    }
                    for case in cases
                ],
            }
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"Exported {len(cases)} evaluation inputs to {args.output} (rubrics excluded).")
        else:
            print(f"Validated {len(cases)} behavioral case definitions; model behavior was not evaluated.")
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
