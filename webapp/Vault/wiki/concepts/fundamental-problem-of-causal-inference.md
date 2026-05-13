---
type: concept
aliases: [Fundamental Problem of Causal Inference]
summary: The principle that for any given individual, we can only observe one potential outcome (e.g., the outcome under treatment or the outcome under control), but never both.
relationships:
  - target: potential-outcomes-framework
    type: is_a_core_concept_in
tags: [causal-inference, statistics, counterfactuals]
sourced_from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )
---

# Fundamental Problem of Causal Inference

## Definition
Coined by statistician Paul Holland, the "fundamental problem of causal inference" is the fact that it is impossible to observe more than one potential outcome for the same individual at the same time. For example, we can observe an employee's salary given their actual level of education, but we can never simultaneously observe what their salary would have been had they attained a different level of education.

## Implication
This problem means that individual-level causal effects are inherently unobservable because the counterfactual outcome is always missing data. In a table of potential outcomes for a population, only one cell for each individual can ever be filled with an observed value; all other potential outcomes for that individual remain unknown and are represented by question marks.

## Role in Causal Science
This principle underscores why causal inference is not a simple matter of data collection but requires a formal framework with assumptions. Causal inference methods, such as the Potential Outcomes Framework or Structural Causal Models, are essentially strategies for navigating this missing data problem to estimate average causal effects or infer individual counterfactuals.

## Relationships

- **is_a_core_concept_in**: [[potential-outcomes-framework|Potential Outcomes Framework]]

---
*Extracted from: The Book Of Why  The New Science Of Cause And Effect ( Pdfdrive )*