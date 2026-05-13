---
type: concept
aliases: [Exponential Distribution]
summary: A continuous probability distribution that models the time between events in a Poisson point process, often used in deep learning for its sharp point at zero.
tags: [probability-distribution, continuous-variable, deep-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Exponential Distribution

## Definition
The exponential distribution is a probability distribution defined by the probability density function $p(x; \lambda) = \mathbf{1}_{x \ge 0} \lambda \exp(-\lambda x)$. The parameter $\lambda$ is the rate parameter.

## Key Properties
A defining characteristic of the exponential distribution is its use of the indicator function $\mathbf{1}_{x \ge 0}$, which assigns a probability of zero to all negative values of x. This results in a distribution that has a sharp point at x=0 and decays exponentially for positive values.

## Application in Deep Learning
Within deep learning, the exponential distribution is frequently employed when a model requires a probability distribution that has a sharp peak at zero. This property is useful for modeling quantities that are non-negative and where small values are much more likely than large values.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*