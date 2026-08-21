# Abstract editing example

This example illustrates SAE's default behavior: remove defensive framing and vague emphasis while preserving scientific caution and every reported value.

## Request

```text
Use $sae to perform standard academic editing on this abstract excerpt. Preserve
the scientific meaning and numerical values. Return the edited text followed by
author queries only if necessary.
```

## Original

```text
It should be emphasized that the proposed method may potentially improve the
prediction accuracy to a certain extent. Of course, this does not necessarily
mean that it can completely replace conventional methods. In the test cohort,
the proposed method achieved an accuracy of 87.4%, whereas the baseline model
achieved an accuracy of 81.2%. These results clearly demonstrate that our novel
method has significant advantages and broad application prospects.
```

## Edited

```text
In the test cohort, the proposed method achieved an accuracy of 87.4%, compared
with 81.2% for the baseline model. This result indicates improved predictive
accuracy under the tested conditions.
```

## Why this edit is within SAE scope

- The edit preserves both values and the direction of the comparison.
- `may potentially` is reduced because the sentence already reports an observed result.
- The imagined claim about replacing conventional methods is removed because the passage provides no such comparison.
- `novel`, `clearly`, `significant advantages`, and `broad application prospects` are removed because the excerpt does not support them.
- `under the tested conditions` preserves the study boundary without adding a defensive paragraph.

