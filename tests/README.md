# Behavioral evaluation

The cases in [`behavior_cases.json`](behavior_cases.json) test editing decisions against semantic criteria. They are synthetic passages, not scientific findings. There is no single required rewrite.

## Coverage

| Cases | Decision being checked |
|---|---|
| 001–002 | Leave clear prose alone; remove filler without deleting a substantive limitation |
| 003–005 | Retain mechanisms and conclusions pending confirmation; distinguish contradicted inference from missing context |
| 006–007 | Handle the same ambiguity with and without author queries |
| 008–009 | Preserve value–entity–condition and claim–citation–attribution relationships |
| 010–012 | Preserve statistical interpretation, independent restrictions, negation, precision, and operators |
| 013–014 | Preserve planned actions and LaTeX structure |
| 015–016 | Apply an explicitly authorized correction; recognize a genuinely blocked transformation |

## Run

1. Validate the package and fixtures:

   ```bash
   python3 scripts/validate_skill.py
   python3 scripts/prepare_behavior_eval.py
   ```

2. Export requests with the acceptance criteria removed:

   ```bash
   python3 scripts/prepare_behavior_eval.py --output /tmp/sae-eval-inputs.json
   ```

3. Give the editing model the current `skills/sae/SKILL.md` and one exported `prompt` at a time. Prefer a fresh context per case. Do not provide this guide, the case rubrics, annotated examples, expected answers, or the reviewer's conclusions. Do not install or modify the user's skill as part of evaluation.

4. Save the actual output for every case. Record the model identifier if available, date, skill/case hashes from the export, and whether cases used separate contexts or a shared batch.

5. Have a separate reviewer compare each output with its source and rubric. A case passes only if every `checks` item is satisfied, no `forbidden` action occurs, and query handling matches the case. Record the output, verdict, and concise evidence for each case; leave unrun cases unscored. Ambiguous verdicts require review, not an automatic pass.

For an author query, judge whether it identifies the relevant scientific decision rather than matching exact wording. For clean-text requests, check that the response contains only the requested manuscript text. For `clarify-first`, check that the response requests missing information without fabricating the requested sentence.

## What the checks establish

The CI checks validate package structure and case definitions only. The exporter does not call a model or grade language quality. Semantic review must examine relationships: the presence of every original number or citation marker does not prove that the correct associations survived.

Report observed passes and failures with their run conditions. A single run is a smoke evaluation, not a general quality guarantee; use repeated fresh-context runs when comparing releases or models. Keep generated responses outside the installable skill and avoid adding private manuscript material to this public suite.

The [2026-11-06 smoke record](runs/2026-11-06-smoke.json) contains actual outputs and a separate agent's semantic review: 16 of 16 cases passed in one shared-context evaluation with two targeted follow-ups. The record includes source hashes and limitations; it is a dated observation, not a continuously updated quality badge.

## Add a case

Use a short, realistic passage with a concrete editing decision. Supply enough context for the intended distinction; pair cases when only the requested output format or authorization changes. Describe observable requirements and forbidden semantic changes rather than one preferred sentence. Update this coverage table when adding a new behavior.
