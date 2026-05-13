---
type: concept
aliases: [Back-door Adjustment]
summary: A method for estimating the causal effect of a treatment on an outcome by statistically controlling for, or "blocking," confounding variables that create a spurious path between them. A method for estimating a causal effect by controlling for a set of variables (a 'deconfounding set') that block all non-causal 'back-door' paths between a cause and its effect.
relationships:
  - target: confounder
    type: is_used_to_control_for
  - target: causal-inference
    type: is_a_method_for
  - target: front-door-adjustment
    type: is_alternative_to
  - target: do-calculus
    type: is_a_component_of
tags: [causal-inference, statistics, methodology, confounding, statistical-adjustment]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Back-door Adjustment

## Definition and Purpose
Back-door adjustment is a core technique for estimating the effect of an intervention in the presence of confounders. It provides an unbiased estimate of a causal effect by identifying and conditioning on a set of variables that block all non-causal "back-door" paths between the treatment variable and the outcome variable.

## Application to Simpson's Paradox
The text provides a practical example of back-door adjustment in its resolution of Simpson's Paradox. To find the true effect of Drug D on Heart Attack, one must adjust for the confounder, Gender, which opens a back-door path. The procedure described—calculating the effect separately for men and women and then averaging—is an implementation of the back-door adjustment formula, which closes this spurious path.

## Context in Causal Inference
In a visual metaphor, the text places back-door adjustment as one of the primary, most familiar methods for ascending "Mount Intervention." This positions it as a foundational technique for moving from passive observation (rung one of the Ladder of Causation) to estimating the effects of active interventions (rung two), alongside other methods like front-door adjustment and instrumental variables.

## Relationships

- **is_used_to_control_for**: [[confounder|Confounder]]
- **is_a_method_for**: [[causal-inference|Causal Inference]]
- **is_alternative_to**: [[front-door-adjustment|Front Door Adjustment]]
- **is_a_component_of**: [[do-calculus|Do Calculus]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*