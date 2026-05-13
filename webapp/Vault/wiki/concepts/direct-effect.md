---
type: concept
aliases: [Direct Effect]
summary: The effect of one variable on another that is not mediated by an intermediate variable in a causal pathway. The effect of a variable on an outcome that is not transmitted through a specified mediator variable.
relationships:
  - target: indirect-effect
    type: is_distinct_from
  - target: mediation-analysis
    type: is_a_component_of
  - target: natural-direct-effect
    type: has_subtype
  - target: mediation-analysis
    type: component_of
  - target: indirect-effect
    type: contrasts_with
  - target: causal-model
    type: defined_within
tags: [causality, mediation, statistics, causal-inference, causal-pathways]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Direct Effect

## Definition
A direct effect is the influence of a variable on an outcome that does not pass through a specified intermediate variable, or mediator. In a linear model represented by a causal diagram, it corresponds to the path coefficient on the arrow leading directly from the cause to the effect. In such simple models, the direct effect is a single number that does not depend on the level of the mediator.

## Role in Discrimination Analysis
The concept of direct effect is crucial in legal and ethical contexts like discrimination analysis. In the Berkeley admissions case, the court was concerned with the direct effect of an applicant's gender on the admission outcome, not the total effect which would include the indirect path through the applicant's choice of department. The analysis by Bickel and Hammel, which partitioned data by department, was an attempt to estimate this direct effect.

## Estimation and Counterfactuals
Estimating the direct effect is not always straightforward. A common error, the Mediation Fallacy, is to simply condition on the mediator. The correct procedure is to "hold the mediator constant." More precise definitions rely on counterfactuals, such as the Natural Direct Effect (NDE), which measures the effect of a treatment on the outcome while the mediator is set to the value it would have naturally taken in the absence of the treatment.

## Relationships

- **is_distinct_from**: [[indirect-effect|Indirect Effect]]
- **is_a_component_of**: [[mediation-analysis|Mediation Analysis]]
- **has_subtype**: [[natural-direct-effect|Natural Direct Effect]]
- **component_of**: [[mediation-analysis|Mediation Analysis]]
- **contrasts_with**: [[indirect-effect|Indirect Effect]]
- **defined_within**: [[causal-model|Causal Model]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*