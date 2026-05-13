---
type: concept
aliases: [Structural Causal Model (SCM)]
summary: A framework for causal and counterfactual inference that uses a system of equations and a corresponding graphical model to represent causal relationships.
relationships:
  - target: structural-equation-models
    type: is_a_formalization_of
  - target: potential-outcomes-framework
    type: is_contrasted_with
  - target: ignorability
    type: provides_test_for
tags: [causal-inference, graphical-models, counterfactuals]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Structural Causal Model (SCM)

## Overview
The Structural Causal Model (SCM) framework uses a system of deterministic equations to represent causal relationships, formalizing the original intentions of earlier Structural Equation Models (SEMs). This approach allows researchers to represent their causal assumptions explicitly in a graphical model and then treat all counterfactuals as derived properties of this world model.

## Computing Counterfactuals
SCM provides a three-step algorithm for deriving counterfactuals from the model. The first step is "Abduction," where observed data is used to estimate an individual's idiosyncratic factors (exogenous variables). The second step is "Action," where the model is modified using the do-operator to reflect the counterfactual condition being assumed. The final step is "Prediction," where the new outcome is calculated using the modified model and the estimated idiosyncratic factors.

## Advantages
A key virtue of the SCM framework is the transparency of its assumptions. Causal assumptions are encoded in a diagram that can be easily understood and tested. For example, the assumption of ignorability can be tested by a simple graphical procedure: checking if a set of variables blocks all back-door paths between treatment and outcome and contains no descendants of the treatment. This provides a clear advantage over model-free approaches where assumptions can be opaque and difficult to verify.

## Relationships

- **is_a_formalization_of**: [[structural-equation-models|Structural Equation Models]]
- **is_contrasted_with**: [[potential-outcomes-framework|Potential Outcomes Framework]]
- **provides_test_for**: [[ignorability|Ignorability]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*