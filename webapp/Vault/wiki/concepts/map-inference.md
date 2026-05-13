---
type: concept
aliases: [Maximum a Posteriori (MAP) Inference]
summary: A form of inference that seeks to find the single most likely configuration of latent variables given the observed data, corresponding to the mode of the posterior distribution.
relationships:
  - target: approximate-inference
    type: is_a_method_for
  - target: expectation-maximization-algorithm
    type: is_related_to
tags: [inference, bayesian-methods, optimization]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Maximum a Posteriori (MAP) Inference

## Definition as Approximate Inference
Maximum a Posteriori (MAP) inference can be formally derived as a specific form of approximate inference. This derivation involves restricting the family of possible approximate posterior distributions, $q(h|v)$, to only include Dirac delta distributions of the form $q(h | v) = \delta(h - \mu)$. This constraint forces the entire probability mass of the approximate posterior onto a single point estimate, $\mu$.

## Optimization Problem
By constraining $q$ to be a Dirac distribution, the problem of maximizing the evidence lower bound $L(v, \theta, q)$ simplifies significantly. The entropy term $H(q)$ becomes negative infinity, making the bound infinitely loose, but the optimization with respect to the point estimate $\mu$ becomes equivalent to finding the mode of the joint distribution. The optimization problem reduces to $\mu^* = \arg\max_\mu \log p(h = \mu, v)$, which is the same as the standard MAP inference problem of finding the most likely configuration $h^*$ that maximizes the posterior $p(h | v)$.

## Learning with MAP Inference
A learning procedure analogous to the EM algorithm can be constructed using MAP inference. This involves alternating between performing MAP inference to find the most likely latent configuration $h^*$ and then updating the model parameters $\theta$ to increase the joint probability $\log p(h^*, v)$. This can be viewed as a form of coordinate ascent on the lower bound $L$, where inference optimizes $L$ with respect to $q$ (by finding the best $\mu$) and parameter updates optimize $L$ with respect to $\theta$.

## Relationships

- **is_a_method_for**: [[approximate-inference|Approximate Inference]]
- **is_related_to**: [[expectation-maximization-algorithm|Expectation Maximization Algorithm]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*