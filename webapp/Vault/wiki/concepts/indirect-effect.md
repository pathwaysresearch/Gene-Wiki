---
type: concept
aliases: [Indirect Effect]
summary: The effect of one variable on another that is transmitted through an intermediate or mediating variable. The effect of a variable on an outcome that is transmitted entirely through one or more mediator variables.
relationships:
  - target: direct-effect
    type: is_distinct_from
  - target: mediation-analysis
    type: is_a_component_of
  - target: natural-indirect-effect
    type: has_subtype
  - target: mediation-analysis
    type: component_of
  - target: direct-effect
    type: contrasts_with
  - target: mediation-formula
    type: calculates
tags: [causality, mediation, statistics, counterfactuals, causal-inference, causal-pathways]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Indirect Effect

## Definition
The indirect effect is the causal influence of one variable (X) on another (Y) that is transmitted through a third, mediating variable (M). It represents the portion of the total effect that is explained by the pathway X → M → Y. The intuitive meaning of the indirect effect was a source of confusion for statisticians for many years, as it is difficult to define without the language of counterfactuals.

## Counterfactual Formulation
A precise definition of the indirect effect is given counterfactually: it is the change observed in the outcome (Y) when the initial variable (X) is held constant, but the mediator (M) is changed to the value it would have attained had X been changed. This formulation, which can involve double-nested counterfactuals, resolves the ambiguity of earlier definitions and aligns with causal intuition.

## Calculation and Challenges
In simple linear models, the indirect effect can be easily calculated by multiplying the path coefficients of the two segments of the indirect path (from X to M, and from M to Y). However, this simple product-of-coefficients method fails in nonlinear systems, such as those with threshold effects. In such cases, counterfactual-based definitions like the Natural Indirect Effect (NIE) are required for accurate calculation.

## Relationships

- **is_distinct_from**: [[direct-effect|Direct Effect]]
- **is_a_component_of**: [[mediation-analysis|Mediation Analysis]]
- **has_subtype**: [[natural-indirect-effect|Natural Indirect Effect]]
- **component_of**: [[mediation-analysis|Mediation Analysis]]
- **contrasts_with**: [[direct-effect|Direct Effect]]
- **calculates**: [[mediation-formula|Mediation Formula]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*