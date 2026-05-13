---
type: concept
aliases: [Prior Probability]
summary: The probability assigned to an event or parameter before any data is observed, representing the model's initial belief.
tags: [bayesian-statistics, probability-theory]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Prior Probability

## Definition
A prior probability is a probability distribution that expresses a model's beliefs about a quantity *before* any evidence or data is taken into account. It represents the initial state of belief.

## Example in Gaussian Mixture Models
In a Gaussian Mixture Model (GMM), the parameters include the prior probability $\alpha_i = P(c = i)$ for each component i. This prior specifies the probability that a randomly selected data point belongs to the i-th Gaussian component, before observing the data point's actual value $\mathbf{x}$.

## Contrast with Posterior Probability
The prior probability stands in contrast to the posterior probability, such as $P(c | \mathbf{x})$. The posterior probability is the revised belief about the quantity, calculated *after* the data $\mathbf{x}$ has been observed. The transition from prior to posterior belief is a central concept in Bayesian inference.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*