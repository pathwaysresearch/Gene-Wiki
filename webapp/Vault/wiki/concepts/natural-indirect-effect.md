---
type: concept
aliases: [Natural Indirect Effect]
summary: A counterfactually defined indirect effect that measures the impact on an outcome of changing the mediator to the value it would have attained under treatment, while holding the treatment itself constant.
relationships:
  - target: indirect-effect
    type: is_a_type_of
  - target: counterfactuals
    type: is_defined_by
tags: [causality, mediation, counterfactuals, statistics]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Natural Indirect Effect

## Definition
The Natural Indirect Effect (NIE) is the counterfactual counterpart to the Natural Direct Effect. It captures the portion of a total effect that is transmitted through a mediator. It is defined as the expected change in the outcome when the treatment variable is held constant at its baseline level, but the mediator is changed to the value it would have taken had the subject received the treatment.

## Calculation in a Nonlinear Model
The text provides an example of a job applicant where the outcome (taking the job) depends on salary exceeding a threshold of ten. Salary is determined by Education and Skill. When Education increases from 0 to 1, Skill increases from 0 to 2. The NIE is calculated by holding Education at 0 but setting Skill to the value it would have taken if Education were 1 (i.e., Skill=2). In this case, the resulting salary is 6, which is below the threshold, so the NIE is 0, even though the total effect is 1. This demonstrates how NIE correctly handles nonlinearities where simple multiplication of path coefficients would fail.

## Relationship to Total Effect
In many systems, the total effect of a variable can be decomposed into the sum of the Natural Direct Effect and the Natural Indirect Effect. This decomposition provides a complete and causally sound understanding of the different pathways through which a cause produces its effect.

## Relationships

- **is_a_type_of**: [[indirect-effect|Indirect Effect]]
- **is_defined_by**: [[counterfactuals|Counterfactuals]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*