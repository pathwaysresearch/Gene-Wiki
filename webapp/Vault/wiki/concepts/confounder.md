---
type: concept
aliases: [Confounder]
summary: A variable in a causal model that is a common cause of both the treatment (or exposure) and the outcome, leading to a spurious association between them.
relationships:
  - target: simpsons-paradox
    type: causes
  - target: back-door-adjustment
    type: is_controlled_by
  - target: causal-diagram
    type: is_identified_by
tags: [causality, statistics, bias]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Confounder

## Definition
A confounder is a variable that creates a spurious association between a treatment and an outcome because it is a cause of both. This common-cause structure can distort the observed relationship, making it appear stronger, weaker, or even reversed compared to the true causal effect.

## Role in Simpson's Paradox
The text uses Simpson's Paradox to provide a clear example of confounding. In the drug trial example, Gender is a confounder because it influences both whether a patient chooses to take the drug and their baseline risk of a heart attack. When the data for men and women are combined, this confounding effect creates the paradoxical result that the drug appears harmful overall, even though it is beneficial (or less harmful) within each gender group.

## Adjusting for Confounders
To get an unbiased estimate of a causal effect, it is necessary to adjust for confounders. The text explains that this can be done by stratifying the data based on the confounding variable. In the example, this means looking at the data for men and women separately and then taking an average of the effects found in each group. This procedure, known as adjustment, effectively blocks the spurious path created by the confounder.

## Relationships

- **causes**: [[simpsons-paradox|Simpsons Paradox]]
- **is_controlled_by**: [[back-door-adjustment|Back Door Adjustment]]
- **is_identified_by**: [[causal-diagram|Causal Diagram]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*