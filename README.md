# SAE — Standard Academic Editing

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**SAE** is a reusable Codex skill for standard academic English editing of SCI and other peer-reviewed journal manuscripts. It improves grammar, clarity, concision, cohesion, terminology, and academic style while preserving scientific meaning and the strength of evidence.

[中文说明](README.zh-CN.md)

## Why SAE?

Generic AI polishing often makes scientific prose longer and more defensive. It may stack hedges, manufacture contrasts, add promotional language, or silently strengthen a claim. SAE instead applies a restrained, evidence-calibrated editing policy:

- Go beyond proofreading without rewriting the research.
- Preserve data, units, statistics, citations, technical terms, and study conditions.
- Preserve distinctions such as association versus causation and observation versus interpretation.
- Remove empty signposting, imagined objections, stacked hedges, and false contrasts.
- Keep qualifications that genuinely encode uncertainty, scope, or study-design limits.
- Raise an author query instead of guessing when scientific meaning is ambiguous.

## Editing scope

| Level | What it does | SAE |
|---|---|:---:|
| Light proofreading | Corrects obvious grammar, spelling, and punctuation | — |
| Standard academic editing | Improves language, clarity, concision, and local paragraph flow | ✓ |
| Intensive rewriting | Substantially reorganizes the argument or rewrites scientific content | — |

SAE supports titles, abstracts, full manuscript sections, figure captions, cover letters, and responses to reviewers. It is not a replacement for peer review, fact-checking, translation, statistical review, or substantive scientific rewriting.

## Repository layout

```text
sae/
├── skills/sae/              # Installable Codex skill
│   ├── SKILL.md
│   └── agents/openai.yaml
├── examples/                # Usage examples
├── scripts/                 # Installation and validation helpers
└── .github/workflows/       # Continuous validation
```

## Install

### Option 1: Installation script

Clone the repository and run:

```bash
./scripts/install.sh
```

The script installs the skill to `${CODEX_HOME:-$HOME/.codex}/skills/sae`. It will not overwrite an existing installation unless you explicitly run it with `--force`.

### Option 2: Manual installation

Copy the installable directory into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/sae "${CODEX_HOME:-$HOME/.codex}/skills/sae"
```

Restart Codex or start a new session if the skill does not appear immediately.

## Use

Invoke the skill explicitly with `$sae`:

```text
Use $sae to edit the following Discussion section for submission to an SCI
journal. Preserve the scientific meaning and return only the edited text.

[Paste manuscript text here]
```

Add journal- or task-specific context when available:

```text
Use $sae to edit this Abstract for Nature Communications. Use American
English, preserve every numerical value, and list author queries separately.

[Paste abstract here]
```

Chinese instructions work as well:

```text
使用 $sae 对以下 Results 部分进行标准学术英文润色。保留所有数据、统计值、
单位和引文，只输出润色后的正文。

[粘贴英文原文]
```

See [examples/abstract.md](examples/abstract.md) for a compact before-and-after example.

## Design principles

1. **Scientific fidelity first.** Language changes must not change what the evidence supports.
2. **Main point before defense.** Put the claim, mechanism, or result before unnecessary disclaimers.
3. **One sufficient hedge.** Retain evidence-based caution; remove stacked uncertainty markers.
4. **No invented depth.** Use contrastive structures only for genuine logical contrasts.
5. **No silent guessing.** Surface consequential ambiguity as an author query.
6. **No stylistic churn.** Leave sentences unchanged when they are already clear and correct.

The complete operational policy is in [skills/sae/SKILL.md](skills/sae/SKILL.md).

## Validate

Run the repository's dependency-free validator:

```bash
python3 scripts/validate_skill.py
```

The GitHub Actions workflow runs the same validation on pushes and pull requests.

## Contributing

Contributions are welcome when they improve scientific fidelity, editorial consistency, trigger accuracy, or usability. Keep the installable skill concise and avoid adding project documentation inside `skills/sae/`. Test changes with realistic manuscript passages and run the validator before opening a pull request.

## License

Released under the [MIT License](LICENSE).
