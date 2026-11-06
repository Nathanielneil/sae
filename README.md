<div align="center">

<img src="assets/hero.svg" alt="SAE — Standard Academic Editing. Clear prose. Intact meaning." width="100%">

**Careful English editing for scientific manuscripts.**<br>
A reusable Codex skill for clearer language, faithful claims, and precise scope.

[中文](README.zh-CN.md) · [Example](#a-careful-edit) · [Install](#install) · [Editing rules](skills/sae/SKILL.md)

[![Checks](https://img.shields.io/github/actions/workflow/status/Nathanielneil/sae/validate.yml?branch=main&style=flat-square&label=structure%20%26%20fixtures)](https://github.com/Nathanielneil/sae/actions/workflows/validate.yml)
[![MIT](https://img.shields.io/badge/license-MIT-47665b?style=flat-square)](LICENSE)

</div>

## A careful edit

SAE improves grammar, concision, terminology, and local paragraph flow. It preserves scientific claims, numerical details, citations, and necessary uncertainty.

**Before**

> It should be emphasized that the proposed method achieved an accuracy of 87.4% in the test cohort, whereas the baseline model achieved an accuracy of 81.2%. Of course, these results do not establish that the method can fully replace conventional methods.

**After**

> In the test cohort, the proposed method achieved an accuracy of 87.4%, compared with 81.2% for the baseline model. These results do not establish that the method can fully replace conventional methods.

The empty prefaces disappear. Both values, their model assignments, and the limit on replacement remain. [Read the annotated examples →](examples/abstract.md)

## Editing boundaries

| Situation | SAE's approach |
|---|---|
| Wording can improve without changing the claim | Edit directly; leave already clear sentences alone. |
| A change would alter a mechanism, conclusion, or claim strength | Retain the content and ask the author when queries are allowed. |
| Supporting material is absent from an excerpt | Treat support as unknown; do not infer that the claim is wrong. |
| The user wants only clean text | Make safe edits and preserve unresolved meaning without comments or guesses. |

Values stay with their groups and conditions; citations stay with their claims. Each necessary qualification keeps its scope. Substantive scientific changes require explicit authorization.

SAE covers titles, abstracts, manuscript sections, captions, cover letters, and reviewer responses. Its scope is medium-intensity language editing; translation, fact-checking, peer review, and scientific revision are separate tasks. [Full specification →](skills/sae/SKILL.md)

## Install

```bash
git clone https://github.com/Nathanielneil/sae.git
cd sae
./scripts/install.sh
```

The installer uses `${CODEX_HOME:-$HOME/.codex}/skills/sae`. Open a new Codex session if the skill is not yet available.

<details>
<summary>Replacing an installation or installing manually</summary>

Existing installations are protected. To deliberately replace one:

```bash
./scripts/install.sh --force
```

For a manual installation, first make sure the destination does not already exist:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/sae "${CODEX_HOME:-$HOME/.codex}/skills/sae"
```

</details>

## Use

```text
Use $sae to edit this Discussion section. Preserve the scientific meaning,
data, and claim strength. Return the edited text and any necessary author queries.

[Paste manuscript text here]
```

Add a target journal, English variant, or preferred output format when useful. To suppress commentary, request **only the edited text**. SAE will preserve passages it cannot safely disambiguate. If the entire requested transformation depends on missing scientific information, it will ask for that information first.

## Development

```bash
python3 scripts/validate_skill.py
python3 scripts/prepare_behavior_eval.py
```

These checks validate the skill package and behavioral case definitions. **They do not score model editing quality.** The [behavioral suite](tests/README.md) supplies isolated requests and criteria for evaluating claims, ambiguity, and scientific relationships.

Keep project documentation and tests outside `skills/sae/`. Contributions should include a focused case when they change editing behavior.

---

[Editing rules](skills/sae/SKILL.md) · [Examples](examples/abstract.md) · [Behavioral tests](tests/README.md) · [MIT license](LICENSE)
