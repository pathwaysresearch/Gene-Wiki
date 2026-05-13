---
type: concept
aliases: [Ill-Conditioning]
summary: A problem in numerical optimization where the Hessian matrix of the cost function has a high condition number, leading to difficulties in training deep models.
relationships:
  - target: stochastic-gradient-descent
    type: affects
tags: [optimization-challenge, numerical-optimization, hessian-matrix]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Ill-Conditioning

## Definition
Ill-conditioning is a prominent challenge in numerical optimization that affects both convex and non-convex problems, and is believed to be present in neural network training. The problem specifically relates to the ill-conditioning of the Hessian matrix H, which is the matrix of second-order partial derivatives of the cost function.

## Impact on Optimization
Ill-conditioning can severely hamper the progress of gradient-based optimization algorithms like Stochastic Gradient Descent (SGD). Its primary manifestation is causing the algorithm to get “stuck,” in the sense that even very small steps taken in the direction of the negative gradient lead to an increase in the cost function, thereby halting progress.

## Mathematical Basis
The issue can be analyzed using a second-order Taylor series expansion of the cost function. This expansion shows that a gradient descent step of -ϵg adds approximately (1/2)ϵ²gᵀHg - ϵgᵀg to the cost. When the Hessian H is ill-conditioned, the positive quadratic term (1/2)ϵ²gᵀHg can become large enough to overwhelm the negative linear term -ϵgᵀg, causing the total change in cost to be positive and preventing the algorithm from descending the cost surface.

## Relationships

- **affects**: [[stochastic-gradient-descent|Stochastic Gradient Descent]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*