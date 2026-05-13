---
type: concept
aliases: [REINFORCE Algorithm]
summary: A gradient estimation algorithm for training models with discrete stochastic variables by using a Monte Carlo average of an expected cost function.
relationships:
  - target: back-propagation-through-random-operations
    type: is_a_method_for
  - target: variance-normalization
    type: is_improved_by
tags: [gradient-estimation, reinforcement-learning, stochastic-networks]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# REINFORCE Algorithm

## Problem Addressed
The REINFORCE algorithm addresses the challenge of training models that involve discrete stochastic operations. When a model's output \(y\) is discrete, the function \(f\) that produces it is a step function. The derivatives of a step function are zero almost everywhere, which means standard back-propagation fails because the gradients provide no information for updating model parameters.

## Core Idea
The central insight of REINFORCE is that while the cost function \(J(f(z; \omega))\) itself has useless derivatives, its expectation over the random noise, \(E_{z \sim p(z)} J(f(z; \omega))\), is often a smooth function that is amenable to gradient descent. REINFORCE provides a framework for computing an unbiased stochastic estimate of the gradient of this expectation.

## Gradient Estimation
The algorithm estimates the gradient using a Monte Carlo average. It works by correlating the choices of the discrete variable \(y\) with the corresponding values of the cost \(J(y)\). If a particular choice of \(y\) results in a good (low cost) outcome, the algorithm 'reinforces' the parameters to make that choice more likely in the future. This allows gradient-based optimization to be applied even in the presence of non-differentiable discrete choices.

## Relationships

- **is_a_method_for**: [[back-propagation-through-random-operations|Back Propagation Through Random Operations]]
- **is_improved_by**: [[variance-normalization|Variance Normalization]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*