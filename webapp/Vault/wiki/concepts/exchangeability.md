---
type: concept
aliases: [Exchangeability]
summary: A counterfactual-based concept for defining the absence of confounding, where the treatment and control groups are comparable in terms of their potential outcomes.
relationships:
  - target: confounding
    type: is_definition_for
  - target: greenland-and-robins
    type: developed_by
  - target: potential-outcomes-framework
    type: is_influenced_by
tags: [causal-inference, counterfactuals, epidemiology]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Exchangeability

## Definition
Proposed by Greenland and Robins in a landmark 1986 paper, exchangeability is a concept used to define the absence of confounding. It formalizes the idea that the control group (X=0) should be comparable to the treatment group (X=1). The groups are considered exchangeable if their outcomes would be the same had they received the same treatment level.

## Counterfactual Basis
Exchangeability introduces a powerful counterfactual twist to the problem of confounding, which is at rung three of the Ladder of Causation. It requires the researcher to imagine what would have happened to individuals in the treatment group if they had *not* received the treatment. If their imagined outcome is the same as the actual outcome of the control group, then the groups are exchangeable, and no confounding exists.

## Significance
This approach represented a completely new way of thinking about confounding in epidemiology. By grounding the definition in counterfactuals, it provided a more powerful and conceptually sound way to detect confounding than previous statistical definitions. It helped pave the way for the broader acceptance of counterfactual reasoning in a field that had been heavily influenced by classical statistics, which focused only on observed data.

## Relationships

- **is_definition_for**: [[confounding|Confounding]]
- **developed_by**: [[greenland-and-robins|Greenland And Robins]]
- **is_influenced_by**: [[potential-outcomes-framework|Potential Outcomes Framework]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*