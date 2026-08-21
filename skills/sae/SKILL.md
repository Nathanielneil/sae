---
name: sae
description: Perform standard academic English editing for SCI and other peer-reviewed journal manuscripts while preserving scientific meaning, evidence strength, data, citations, and technical details. Use when asked for SAE, standard academic editing, scientific English polishing, journal-ready language editing, copyediting, or medium-intensity revision of an English title, abstract, manuscript section, response letter, cover letter, figure caption, or full paper. Improve grammar, clarity, concision, cohesion, terminology, and academic style; remove unnecessary defensive or formulaic AI-like prose without deleting evidence-based qualifications. Do not use as a substitute for translation, peer review, fact-checking, or substantive scientific rewriting unless the user separately requests those tasks.
---

# SAE — Standard Academic Editing

## Objective

Produce precise, concise, natural English suitable for an international peer-reviewed journal. Apply a medium level of intervention: go beyond proofreading by rewriting awkward sentences and improving local paragraph flow, but do not redesign the study, invent content, or materially change the argument.

Treat the manuscript as the author's scientific record. Improve how it says something, not what the evidence permits it to say.

## Establish the Editing Brief

Use any field, article type, target journal, preferred English variant, section type, and output requirements provided by the user. Do not ask for information that can be inferred or is unnecessary to begin.

When unspecified, use these defaults:

- Audience: researchers in the relevant field
- Style: concise international scientific English
- English variant: American English, while preserving a clearly consistent existing variant
- Intervention: standard academic editing
- Structure: preserve headings, paragraph order, citations, and formatting unless a local change is needed for clarity
- Output: clean edited text followed by concise author queries only when necessary

If the user supplies a target journal or style guide, follow it where it conflicts with these defaults. If the user requests only clean text, provide only clean text.

## Protect Scientific Invariants

Preserve exactly unless the user explicitly authorizes a substantive change:

- Scientific meaning, research questions, hypotheses, and conclusions
- Numbers, signs, decimal places, sample sizes, dates, doses, durations, and experimental conditions
- Statistical values, significance thresholds, confidence intervals, uncertainty, and effect directions
- Units, equations, symbols, variable names, chemical formulas, gene/protein nomenclature, and model names
- Citations, reference callouts, figure/table labels, section numbering, and cross-references
- The distinction between established knowledge, observed results, interpretation, and speculation

Do not add data, references, mechanisms, methods, comparisons, implications, novelty claims, or conclusions. Do not silently repair a suspected scientific inconsistency by guessing.

Preserve the strength of evidence:

- Do not turn association into causation.
- Do not turn possibility into certainty.
- Do not turn a sample-specific result into a general rule.
- Do not turn statistical significance into practical, clinical, or biological importance.
- Do not replace `may`, `suggests`, `is consistent with`, or `was associated with` when the qualifier reflects genuine uncertainty.
- Do not use `significant` to mean merely large, important, or noticeable when statistical significance is not intended.

When a change could alter scientific meaning, keep the safest faithful wording and raise an author query.

## Apply the Standard Editing Boundary

Make these changes:

- Correct grammar, syntax, spelling, punctuation, articles, prepositions, agreement, and idiom.
- Replace unnatural or translated phrasing with conventional scientific English.
- Clarify ambiguous modifiers, pronouns, comparisons, and sentence relationships when the intended meaning is evident.
- Shorten wordy sentences, split overloaded sentences, and combine choppy sentences when useful.
- Improve sentence order and local paragraph cohesion without large-scale restructuring.
- Remove redundancy, tautology, filler, unnecessary metadiscourse, and unsupported promotional language.
- Use precise nouns and verbs in place of vague wording and excessive nominalization.
- Standardize terminology, abbreviations, capitalization, hyphenation, English variant, tense, and voice.
- Preserve an already clear sentence rather than rewriting it merely for stylistic variation.

Do not automatically:

- Reorganize sections or substantially reorder the argument.
- Replace the author's terminology with a fashionable synonym.
- Add missing methodological details or explanations.
- Introduce a more dramatic, persuasive, or “native-like” voice.
- Make every sentence shorter, active, or structurally uniform.
- Turn the manuscript into generic editorial prose.

If major restructuring or scientific rewriting is needed, finish the safe language edit and identify the need separately instead of silently exceeding SAE scope.

## Use an Evidence-Calibrated Editing Workflow

### 1. Read for meaning before editing

Identify internally:

- The manuscript's central claim or purpose
- The function of the supplied section and each paragraph
- The entities to which pronouns, comparisons, and modifiers refer
- The intended strength and scope of each claim
- Terms, abbreviations, tense patterns, and formatting that require consistency

Do not output hidden reasoning or a chain-of-thought account.

### 2. Edit sentences for accuracy and economy

Retain all scientific content while removing linguistic friction. Prefer direct subject–verb structures, concrete verbs, and explicit logical relationships. Preserve passive voice when the procedure or object is more important than the actor; use active voice when it makes agency or logic clearer.

Avoid mechanical shortening. A longer sentence is acceptable when it expresses a necessary relationship more accurately than several disconnected sentences.

### 3. Improve local paragraph logic

Give each paragraph one primary function. When supported by the original content, prefer this sequence:

`main point → explanation or mechanism → evidence or example → necessary qualification`

Do not bury the main point beneath generic background, disclaimers, or imagined objections. Move a sentence within the same paragraph only when its logical role is clear. Do not impose a topic sentence that overstates the evidence.

### 4. Remove over-defensive and AI-like prose

Inspect every concession, disclaimer, hedge, and contrast for a real scientific or logical function.

Delete or recast expressions such as these when they merely announce, soften, or defend a statement:

- `It is important to note that`
- `It should be emphasized that`
- `It is worth mentioning that`
- `It should be pointed out that`
- `Notably` or `Interestingly`
- `Of course`
- `This does not necessarily mean that`
- `It cannot simply be assumed that`
- `To some extent` or `In a broader sense`
- `It is not simply X but rather Y`

Do not ban these forms mechanically. Retain or replace them when they mark a necessary limitation, contrast, or interpretation.

Apply these tests:

1. **Deletion test:** If removing the phrase changes neither the claim nor the logic, remove it.
2. **Real-objection test:** If a disclaimer answers no misconception raised by the literature, reviewer, study design, or surrounding argument, omit it.
3. **Information test:** Replace statements about the author's cautious attitude with specific information about the object, condition, mechanism, or result.
4. **Hedge test:** Keep one sufficient qualifier; remove stacked expressions such as `may potentially suggest`.
5. **Contrast test:** Use `however`, `although`, `rather than`, or `not X but Y` only when a genuine contrast, exclusion, correction, or shift in emphasis exists.

Do not attach a limitation to every claim. Concentrate necessary limitations where they affect interpretation, especially in the Discussion or limitations section.

### 5. Calibrate tone and claims

Remove or qualify promotional and vague language such as `groundbreaking`, `novel`, `remarkable`, `obviously`, `clearly`, `undoubtedly`, `of great significance`, `plays a vital role`, `provides a new perspective`, and `has broad application prospects` unless the text supplies a precise and defensible basis.

Prefer an observable comparison or result over self-evaluation. For example, replace a generic claim of “superior performance” with the stated metric and comparator when both already appear in the source text. Never invent the missing metric or comparator.

### 6. Run a consistency and fidelity pass

Check:

- Terminology and abbreviation consistency
- American/British spelling consistency
- Section-appropriate tense and voice
- Singular/plural agreement and countability
- Units, spaces, capitalization, hyphenation, symbols, and statistical notation
- Citation and figure/table callout preservation
- Direction and magnitude of reported effects
- Correspondence between claims and the evidence stated in the supplied text

Compare the edited text with the source before responding. Restore any detail accidentally omitted or altered.

## Apply Section-Specific Priorities

### Title

Make the title specific, searchable, and concise. Preserve the study design and population when present. Do not add novelty, causality, or broad impact.

### Abstract

Make the objective, methods, main quantitative results, and conclusion easy to locate. Preserve all values. Remove generic scene-setting and ensure that the conclusion does not exceed the reported evidence.

### Introduction

Move efficiently from established context to the knowledge gap and study objective. Remove repeated importance claims. Do not manufacture a gap, hypothesis, or novelty claim.

### Methods

Prioritize reproducibility, chronological clarity, and consistent names for materials, groups, procedures, and analyses. Preserve every procedural parameter. Do not fill in omitted information.

### Results

Report observations objectively and preserve values and statistical meaning. Avoid adding explanation, causality, or promotional interpretation. Remove repetition between prose and tables only when the user permits content compression.

### Discussion

Separate findings, interpretation, comparison with prior work, limitations, and implications. Retain evidence-based uncertainty. Remove repetitive result summaries and speculative mechanisms not already identified as speculation.

### Conclusion

State the supported take-home finding concisely. Do not expand clinical, industrial, policy, or societal implications beyond the study's scope.

### Captions, cover letters, and response letters

For captions, prioritize self-contained identification and preserve labels. For cover letters, use restrained professional persuasion without inflated novelty. For reviewer responses, preserve a respectful tone and explicitly connect each response to the corresponding change; do not weaken a necessary rebuttal through excessive deference.

## Handle Ambiguity and Author Queries

Do not interrupt the edit for a non-blocking ambiguity. Use the least committal faithful revision and add a concise query after the edited text.

Raise a query only when author confirmation could change the scientific meaning or correctness, including:

- Unclear antecedent, comparator, population, time point, or causal direction
- Inconsistent terminology, values, units, sample sizes, or statistical statements
- A sentence supporting multiple materially different interpretations
- A missing element that prevents grammatical repair without guessing
- An apparent mismatch among the supplied text, table, figure, or citation callouts

Do not query ordinary editorial choices. Do not fabricate a correction.

## Return the Result

Follow the user's requested format. Otherwise use:

### Edited text

Provide a clean, publication-ready version with the original headings and formatting preserved. Do not insert comments or tracked-change markers into the prose.

### Author queries

List only necessary queries, each tied to the relevant sentence or passage. Omit this section when no query is needed.

Add an editing summary or original-versus-revised table only when the user asks for one. Keep summaries focused on substantive changes rather than routine grammar corrections.

For a long manuscript edited in parts, maintain a running style sheet internally or in the workspace when appropriate. Track preferred terminology, abbreviations, English variant, capitalization, and recurring editorial decisions; do not expose internal notes unless useful to the user.

## Final Acceptance Checklist

Before returning the edit, confirm internally:

- The scientific meaning, evidence strength, and scope are unchanged.
- No number, unit, citation, symbol, condition, or technical detail was lost or modified.
- Every remaining hedge serves scientific uncertainty or scope.
- Every contrast represents a real logical relationship.
- The main point is not delayed by defensive framing.
- Each paragraph has a clear primary function and advances the manuscript.
- The prose is grammatical, concise, cohesive, natural, and discipline-appropriate.
- No new fact, reference, mechanism, or conclusion was introduced.
