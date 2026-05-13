---
type: concept
aliases: [Precision Matrix]
summary: The inverse of the covariance matrix, used as an alternative parametrization for a multivariate normal distribution that can be more computationally efficient for PDF evaluation.
tags: [linear-algebra, probability-theory, parametrization]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Precision Matrix

## Definition
The precision matrix, often denoted by $\beta$, is defined as the inverse of the covariance matrix $\Sigma$ for a multivariate probability distribution, such that $\beta = \Sigma^{-1}$.

## Application in Normal Distribution
In the context of the multivariate normal distribution, the precision matrix provides an alternative parametrization. This can be particularly useful for computational efficiency. When evaluating the probability density function (PDF) multiple times for different parameter values, using the precision matrix avoids the costly step of inverting the covariance matrix $\Sigma$ in each evaluation.

## Mathematical Formulation
The PDF of a multivariate normal distribution parametrized by the mean $\mu$ and the precision matrix $\beta$ is given by the formula:
$N(x; \mu, \beta^{-1}) = \sqrt{\frac{\det(\beta)}{(2\pi)^n}} \exp \left(-\frac{1}{2}(x - \mu)^\top \beta(x - \mu) \right)$.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*