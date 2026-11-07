# Editing examples

These constructed examples illustrate editing decisions, not independent verification of the scientific statements. Each edited passage is one acceptable outcome, not an exact-match target.

## Remove a preface; preserve the limitation

**Request:** Use SAE to edit this abstract excerpt. Preserve scientific meaning and numerical values. Return the edited text and necessary author queries.

**Original**

> It should be emphasized that the proposed method achieved an accuracy of 87.4% in the test cohort, whereas the baseline model achieved an accuracy of 81.2%. Of course, these results do not establish that the method can fully replace conventional methods.

**Edited**

> In the test cohort, the proposed method achieved an accuracy of 87.4%, compared with 81.2% for the baseline model. These results do not establish that the method can fully replace conventional methods.

The edit removes empty prefaces. It preserves both values, the model-to-value mapping, the test-cohort scope, and the restriction on replacement. No query is needed. A generic phrase such as “under the tested conditions” would not, by itself, preserve the specific replacement limitation.

## An untested mechanism needs an author decision

**Request:** Edit the following Discussion sentence using SAE and include necessary author queries. Study context: durability was measured; oxidation and the proposed mechanism were not tested.

**Original**

> The coating increases durability by preventing oxidation.

**Edited**

> The coating increases durability by preventing oxidation.

**Author query:** The supplied context says oxidation and the proposed mechanism were not tested. Is there other evidence supporting this mechanism, or should it be presented as a hypothesis?

The sentence is already grammatical. Deleting the mechanism or adding “may” would change its scientific status. SAE retains the author's claim pending confirmation; the query makes the unresolved issue explicit. If the author subsequently confirms that it is a hypothesis and requests that correction, SAE can make the authorized revision.

## Missing context does not invalidate a claim

**Request:** Edit this abstract sentence using SAE. Only the abstract sentence is supplied.

**Original**

> We presents a novel calibration method for low-light imaging.

**Edited**

> We present a novel calibration method for low-light imaging.

The agreement error is corrected. Novelty is preserved because the excerpt's lack of supporting literature is not evidence against it. No query is needed solely to verify an otherwise clear claim; this edit does not certify novelty.

## Clean text with unresolved ambiguity

**Original**

> Both models was evaluated at day 7. It had the lower error.

| Request | Output |
|---|---|
| Edit using SAE; return only the edited text. | Both models were evaluated at day 7. It had the lower error. |
| Edit using SAE; include necessary author queries. | The same edited text, followed by: “Which model had the lower error at day 7?” |

The first sentence can be repaired without choosing a scientific interpretation. The second is retained because neither model is identified. Suppressing queries does not authorize guessing, deleting the comparison, or changing its certainty.

More cases and semantic acceptance criteria are in the [behavioral suite](../tests/README.md).
