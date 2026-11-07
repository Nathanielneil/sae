<picture>
  <source media="(max-width: 600px)" srcset="assets/hero-mobile.svg">
  <img src="assets/hero.svg" width="100%" alt="SAE · Standard Academic Editing for scientific manuscripts">
</picture>

**SAE edits scientific English in Codex.** Give it a manuscript passage to improve the wording while preserving what was measured, who reported it, and how certain the finding is.

[中文](README.zh-CN.md)　·　[Quick start](#quick-start)　·　[Editing rules](skills/sae/SKILL.md)

## An edit under the microscope

<picture>
  <source media="(max-width: 600px)" srcset="assets/proof-mobile.svg">
  <img src="assets/proof.svg" width="100%" alt="Original: Of course, these results do not establish that the method can fully replace conventional methods. Edited: These results do not establish that the method can fully replace conventional methods.">
</picture>

“Of course” can go. “Do not establish” must stay: the study has not shown that the method can fully replace conventional methods.

<picture>
  <source media="(max-width: 600px)" srcset="assets/values-en-mobile.svg">
  <img src="assets/values-en.svg" width="100%" alt="In the same example test cohort, accuracy is 87.4% for the proposed method and 81.2% for the baseline.">
</picture>

In this constructed example, **87.4%** belongs to the proposed method and **81.2%** to the baseline. SAE checks those assignments after editing; citations must likewise stay with the claims they support. [Read the full before-and-after passage →](examples/abstract.md)

## When the evidence is unclear

<picture>
  <source media="(max-width: 600px)" srcset="assets/decisions-en-mobile.svg">
  <img src="assets/decisions-en.svg" width="100%" alt="Edit language directly. For conflicting evidence, retain the claim and query the author when permitted. If only context is missing, retain the claim.">
</picture>

A missing Methods section does not invalidate an abstract. If the supplied text actually conflicts with a claim, SAE keeps the claim and asks a focused question when permitted. Only the author can authorize a change to its scientific meaning.

**For clean text only:** SAE edits around unresolved ambiguity. It asks for clarification first only if the entire requested edit depends on missing information.

## Quick start

```bash
git clone https://github.com/Nathanielneil/sae.git
cd sae
./scripts/install.sh
```

In Codex, paste your passage after a request such as:

> Use $sae to edit this Discussion section. Preserve claim strength and return the edited text followed by any necessary author queries.

<details>
<summary>Installation details and updates</summary>

The skill is installed at `${CODEX_HOME:-$HOME/.codex}/skills/sae`. Start a new Codex session if it does not appear. To replace an existing installation, run `./scripts/install.sh --force`. For manual installation, copy `skills/sae/` into the Codex skills directory after checking that the destination does not already exist.

</details>

[Behavioral cases & validation](tests/README.md)　·　[MIT license](LICENSE)
