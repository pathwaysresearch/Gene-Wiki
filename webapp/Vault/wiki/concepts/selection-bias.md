---
type: concept
aliases: [Selection Bias]
summary: A type of bias that occurs when the sample group being studied is not representative of the target population due to the mechanism by which subjects are selected for the study.
relationships:
  - target: transportability-problem
    type: related-to
tags: [causal-inference, statistics, bias]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Selection Bias

## Definition
Selection bias occurs when the sample group under study differs from the target population in a relevant way due to the selection process itself. This threatens the validity of the study's conclusions when applied to the broader population.

## Contrast with Transportability
While similar to the transportability problem, selection bias has a distinct graphical representation. Instead of a difference-producing variable `S` pointing to an affected variable in the model, an arrow is drawn from a variable *toward* `S`. The variable `S` represents "selection" into the study, meaning a factor within the model is a cause of being included in the sample.

## Overcoming the Bias
The text presents selection bias not just as a threat, but as an opportunity. If the mechanism of subject recruitment is understood, it is possible to recover from the bias. This can be achieved by collecting data on the correct set of deconfounding variables and applying an appropriate reweighting or adjustment formula. A classic example mentioned is Berkson's bias, which can arise from studying only hospitalized patients.

## Relationships

- **related-to**: [[transportability-problem|Transportability Problem]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*