---
type: concept
aliases: [Posterior Probability]
summary: The revised or updated probability of an event or parameter value after new evidence or data has been taken into account.
relationships:
  - target: bayes-rule
    type: computed_using
  - target: prior-probability
    type: related_to
tags: [bayesian-statistics, probability-theory]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Posterior Probability

## Definition
A posterior probability is the probability of a variable or parameter computed *after* relevant evidence or data has been observed. It represents an updated belief that combines prior knowledge with new information.

## Contrast with Prior Probability
The posterior probability is explicitly contrasted with the prior probability. While a prior, such as $P(c)$, represents the belief about a variable *before* observing data, the posterior, such as $P(c | \mathbf{x})$, represents the belief *after* observing the data $\mathbf{x}$.

## Role in Bayesian Inference
Calculating the posterior probability is the primary goal of Bayesian inference. It is typically computed from the prior probability and the likelihood of the observed data using Bayes' rule. This allows a model to update its beliefs as it is exposed to more data.

## Relationships

- **computed_using**: [[bayes-rule|Bayes Rule]]
- **related_to**: [[prior-probability|Prior Probability]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*