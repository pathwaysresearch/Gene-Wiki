---
type: concept
aliases: [Ignorability]
summary: A key assumption in the Potential Outcomes Framework, stating that the mechanism for assigning treatment is independent of the potential outcomes, possibly conditional on a set of covariates.
relationships:
  - target: potential-outcomes-framework
    type: is_a_key_assumption_of
  - target: structural-causal-model
    type: provides_test_for
tags: [causal-inference, statistics, confounding]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Ignorability

## Definition
Ignorability is a core assumption in the Rubin Causal Model required for estimating causal effects from observational data. It posits that, conditional on a set of observed covariates Z, the treatment assignment X is independent of the potential outcomes Y. This is also known as "conditional ignorability" or "unconfoundedness."

## Role in Causal Inference
This assumption justifies the use of statistical methods like matching or conditioning on covariates to estimate causal effects. If ignorability holds, comparing outcomes between treated and untreated individuals who are similar on the covariates Z provides an unbiased estimate of the treatment effect. However, the text warns that naively matching on variables like 'Experience' when it is affected by 'Education' can lead to incorrect conclusions.

## Assessment and Criticism
The text highlights the difficulty of assessing ignorability without a formal causal model. In the Structural Causal Model framework, ignorability can be tested graphically by checking if the covariates Z block all back-door paths between treatment X and outcome Y, and that no covariate in Z is a descendant of X. The text criticizes the "black box" nature of the assumption in the potential outcomes framework, quoting a researcher who suggests it is often made for methodological convenience rather than being a genuinely believed property of the data-generating process.

## Relationships

- **is_a_key_assumption_of**: [[potential-outcomes-framework|Potential Outcomes Framework]]
- **provides_test_for**: [[structural-causal-model|Structural Causal Model]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*