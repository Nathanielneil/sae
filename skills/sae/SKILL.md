---
name: sae
description: Perform standard academic English editing for scientific manuscripts, abstracts, captions, cover letters, and reviewer responses. Use for SAE, scientific English polishing, or medium-intensity academic copyediting. Improve clarity and flow while preserving scientific claims, evidence strength, data, citations, and scope. Translation, fact-checking, peer review, and substantive scientific revision require a separate request.
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

Follow supplied or verified journal requirements where they conflict with these defaults; a journal name alone does not establish its current requirements. If the user requests only clean text, provide only clean text and use the ambiguity fallback below.

## Resolve Editing Boundaries

Scientific fidelity takes priority over concision, fluency, and removal of AI-like phrasing. Preserving a claim and correcting it to match the evidence are different tasks. Weakening a claim can change its meaning just as strengthening it can.

- **Edit directly** when the change affects language without changing a scientific proposition: grammar, wordiness, non-substantive emphasis, or genuinely redundant qualifications.
- **Retain and query** when a proposed correction would delete a mechanism, change causality or certainty, narrow a conclusion, remove a substantive novelty or application claim, or resolve conflicting scientific details. Make safe language edits around the affected content. Follow the clean-text fallback if queries are excluded.
- **Make a substantive correction only when explicitly authorized**, within the requested scope and using supplied or verified information. A request for polished, concise, or less AI-like prose is not such authorization. Do not invent supporting facts. Keep any necessary scientific revision distinct from ordinary language editing when the requested format permits.

Assess only the evidence available for the editing task:

| Evidence state | Editing decision |
|---|---|
| Supplied material supports the claim | Preserve its strength and scope. |
| Supplied material contradicts or does not justify the stated inference | Preserve the proposition pending author confirmation; identify the specific issue in a query when permitted. |
| Relevant evidence is not supplied | Treat support as unknown. Do not infer that the claim is false or unsupported in the full manuscript. |

An excerpt is not the entire scientific record. Do not fact-check every statement or routinely query claims merely because their supporting sections are absent. Query when a concrete inconsistency or a necessary edit requires a scientific decision.

## Protect Scientific Invariants

Preserve the following content and relationships unless the user explicitly authorizes the relevant substantive change:

- Scientific meaning, research questions, hypotheses, and conclusions
- Numbers, signs, decimal places, sample sizes, dates, doses, durations, and experimental conditions
- Statistical values, significance thresholds, confidence intervals, uncertainty, and effect directions
- Units, equations, symbols, variable names, chemical formulas, gene/protein nomenclature, and model names
- Citations, reference callouts, figure/table labels, section numbering, and cross-references
- The distinction between established knowledge, observed results, interpretation, and speculation

Preserve numerical values, precision, signs, and comparison operators exactly. Unambiguous typography may change, such as `5mg` to `5 mg`; do not round values, convert units, calculate new differences, or normalize technical names whose identity could change. Protect LaTeX commands, citation keys, equation labels, and other document syntax when editing their surrounding prose.

During SAE, do not add data, references, mechanisms, methods, comparisons, implications, novelty claims, or conclusions. Do not silently repair a suspected scientific inconsistency by guessing.

Preserve the strength of evidence:

- Do not turn association into causation.
- Do not turn possibility into certainty.
- Do not turn a sample-specific result into a general rule.
- Do not turn statistical significance into practical, clinical, or biological importance.
- Do not turn a non-significant difference into equivalence, or absence of evidence into evidence of absence.
- Do not replace `may`, `suggests`, `is consistent with`, or `was associated with` when the qualifier reflects genuine uncertainty.
- Do not use `significant` to mean merely large, important, or noticeable when statistical significance is not intended.
- Preserve the scope of negation and quantifiers such as `not`, `only`, `all`, `some`, `at least`, and `at most`.

When a necessary edit depends on scientific interpretation, follow the boundary and ambiguity rules rather than choosing the most cautious-sounding interpretation.

## Apply the Standard Editing Boundary

Make these changes:

- Correct grammar, syntax, spelling, punctuation, articles, prepositions, agreement, and idiom.
- Replace unnatural or translated phrasing with conventional scientific English.
- Clarify ambiguous modifiers, pronouns, comparisons, and sentence relationships when the intended meaning is evident.
- Shorten wordy sentences, split overloaded sentences, and combine choppy sentences when useful.
- Improve sentence order and local paragraph cohesion without large-scale restructuring.
- Remove redundancy, tautology, filler, unnecessary metadiscourse, and promotional emphasis that carries no independent scientific claim.
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

If major restructuring or scientific rewriting is needed, finish the safe language edit and, when the output format permits, identify the need separately instead of silently exceeding SAE scope.

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

`main point → supporting explanation or evidence → necessary qualification`

This is a flexible pattern, not a requirement to add a mechanism or move a condition away from its claim. Do not bury the main point beneath generic background or empty disclaimers. Move a sentence within the same paragraph only when its logical role and citation attachments remain clear. Do not impose a topic sentence that overstates the evidence.

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
2. **Scope test:** Remove an empty defensive preface, but retain any substantive restriction on inference, generalization, or application. Missing surrounding context is not a reason to discard it.
3. **Information test:** Prefer specific information already supplied about the object, condition, mechanism, or result over statements about the author's cautious attitude. Do not invent the missing information.
4. **Hedge test:** Remove semantically redundant qualifications, not qualifiers counted above a fixed limit. Preserve each independent uncertainty, population, time, or condition restriction and its scope.
5. **Contrast test:** Use `however`, `although`, `rather than`, or `not X but Y` only when a genuine contrast, exclusion, correction, or shift in emphasis exists.

Do not add a generic limitation to every claim. Keep necessary qualifications attached to the claims they limit, including in standalone titles, abstracts, and captions. Broader limitations may be consolidated only when their meaning and reach remain unchanged.

### 5. Calibrate tone and claims

Remove empty emphasis such as `obviously`, `clearly`, or `remarkable` only when it has no independent scientific meaning. Do not treat a word list as a deletion rule: `novel`, a mechanism, or an application statement can carry a substantive proposition. If correcting it would change the claim, retain it and query when warranted under the evidence-state rules. Never silently downgrade a claim merely because the supplied excerpt lacks its supporting evidence.

Prefer an observable comparison or result over empty self-evaluation when both express the same proposition. Use only metrics and comparators already supplied. Replacing a broad superiority claim with one narrow metric is a substantive change if it removes part of the author's claim; query or obtain authorization instead.

### 6. Run a consistency and fidelity pass

Check:

- Terminology and abbreviation consistency
- American/British spelling consistency
- Section-appropriate tense and voice
- Singular/plural agreement and countability
- Units, spaces, capitalization, hyphenation, symbols, and statistical notation
- Citation and figure/table callout preservation
- Direction and magnitude of reported effects
- Each value's metric, unit, group or model, comparator, sample size, time point, and experimental condition
- Each claim's supporting citation or figure/table callout, and its attribution to the present authors or another source
- Negation, quantifiers, uncertainty, and the scope of each restriction
- Any concrete conflict between a claim and the supplied evidence, handled through the boundary rules

Compare the edited text with the source before responding. Checking that the same numbers and citation markers remain is insufficient: verify their attachments after splitting, combining, or moving sentences. Restore any detail or relationship accidentally omitted or altered. Do not imply that cited material or absent sections were checked.

## Apply Section-Specific Priorities

### Title

Make the title specific, searchable, and concise. Preserve the study design and population when present. Do not add novelty, causality, or broad impact.

### Abstract

Make the objective, methods, main quantitative results, and conclusion easy to locate. Preserve all values and necessary scope restrictions. Remove generic scene-setting. Flag a conclusion that exceeds the supplied evidence rather than silently rewriting the scientific conclusion.

### Introduction

Move efficiently from established context to the knowledge gap and study objective. Remove repeated importance claims. Do not manufacture a gap, hypothesis, or novelty claim.

### Methods

Prioritize reproducibility, chronological clarity, and consistent names for materials, groups, procedures, and analyses. Preserve every procedural parameter. Do not fill in omitted information.

### Results

Report observations objectively and preserve values and statistical meaning. Avoid adding explanation, causality, or promotional interpretation. Remove repetition between prose and tables only when the user permits content compression.

### Discussion

Clarify the relationships among findings, interpretation, prior work, limitations, and implications. Retain uncertainty and substantive mechanisms. If a mechanism is asserted as established but the supplied material identifies it as untested, query its status; do not delete it or silently add uncertainty. Remove only genuine repetition that carries no distinct interpretive role.

### Conclusion

State the author's take-home finding concisely without changing its strength or scope. Handle apparent overreach through the boundary rules; do not expand or silently narrow clinical, industrial, policy, or societal implications.

### Captions, cover letters, and response letters

For captions, clarify identification using supplied information and preserve labels. For cover letters, use restrained professional persuasion without adding novelty claims. For reviewer responses, preserve respectful tone and necessary rebuttals. Link responses to changes only when those changes are supplied; do not invent experiments, locations, or completed actions, or turn a planned revision into a completed one.

## Handle Ambiguity and Author Queries

Do not interrupt the edit for a non-blocking ambiguity. Make any revision that is faithful under all plausible readings; otherwise preserve the ambiguous span and edit safely around it. A weaker assertion is not automatically a faithful revision.

- **Queries allowed:** finish the safe edit, then ask only the specific questions needed to resolve scientific ambiguity or a concrete inconsistency. Retain affected content pending confirmation.
- **Clean text only:** return only the edited text. Preserve unresolved content, including its ambiguity, rather than guessing, weakening it, deleting it, or inserting comments. Query suppression changes presentation, not editing authority.
- **Task genuinely blocked:** if the requested transformation cannot be completed at all without choosing a scientific meaning, request the minimum clarification before producing it. A local ambiguity in an otherwise editable manuscript is not a blocker.

Raise a query only when author confirmation could change the scientific meaning or correctness, including:

- Unclear antecedent, comparator, population, time point, or causal direction
- Inconsistent terminology, values, units, sample sizes, or statistical statements
- A sentence supporting multiple materially different interpretations
- A missing element that prevents grammatical repair without guessing
- An apparent mismatch among the supplied text, table, figure, or citation callouts
- A proposed correction to a substantive claim that requires author confirmation

Do not query ordinary editorial choices or every claim whose external support is unavailable. Do not fabricate a correction. Tie each query to the relevant passage and identify the decision the author needs to make.

## Return the Result

Follow the user's requested format. Otherwise use:

### Edited text

Provide a clean language-edited version with the original headings and formatting preserved. Do not insert comments or tracked-change markers into the prose unless requested. Language editing does not certify unresolved scientific claims or journal compliance.

### Author queries

List only necessary queries, each tied to the relevant sentence or passage. Omit this section when no query is needed.

Add an editing summary or original-versus-revised table only when the user asks for one. Keep summaries focused on substantive changes rather than routine grammar corrections.

For a long manuscript edited in parts, maintain a running style sheet internally or in the workspace when appropriate. Track preferred terminology, abbreviations, English variant, capitalization, and recurring editorial decisions; do not expose internal notes unless useful to the user.

## Final Acceptance Checklist

Before returning the edit, confirm internally:

- Scientific meaning, evidence strength, and scope are unchanged except for explicitly authorized substantive corrections.
- No value, precision, sign, unit meaning, citation identity, symbol meaning, condition, or technical detail was lost or changed without authorization; any typography change preserves meaning.
- Values remain attached to the correct entities and conditions; citations remain attached to the correct claims and sources.
- Every remaining hedge serves scientific uncertainty or scope.
- Every contrast represents a real logical relationship.
- The main point is not delayed by defensive framing.
- Each paragraph has a clear primary function and advances the manuscript.
- The prose is grammatical, concise, cohesive, natural, and discipline-appropriate.
- No unsupported fact, reference, mechanism, or conclusion was introduced; ordinary SAE added no scientific content.
- Unknown support was not treated as evidence against a claim; substantive decisions were not made silently.
- Unresolved ambiguity was retained or queried according to the requested output format.
