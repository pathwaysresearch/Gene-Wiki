---
type: concept
aliases: [L1 Parameter Regularization]
summary: A regularization technique that penalizes the L1 norm (sum of absolute values) of the model's weights, which tends to produce sparse solutions where many weights are exactly zero.
relationships:
  - target: regularization
    type: is_a
tags: [parameter-penalty, sparsity, feature-selection]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# L1 Parameter Regularization

## Definition
L1 parameter regularization adds a penalty term to the objective function that is proportional to the L1 norm of the model's weights, expressed as $\Omega(\boldsymbol{\theta}) = \alpha \sum_i |w_i|$. This penalty encourages the model to find solutions where many of the weight parameters are exactly zero, a property known as sparsity. From a constrained optimization perspective, this is equivalent to constraining the weights to lie within an L1 ball.

## Analysis via Quadratic Approximation
While the L1 penalty's non-differentiable nature at zero complicates analysis for a general objective function, its behavior can be understood by studying a quadratic approximation of the objective function around its minimum. Assuming the Hessian matrix $\mathbf{H}$ of the objective is diagonal, the regularized objective function decomposes into a sum over the individual parameters: $J(\mathbf{w}^*) + \sum_i [ \frac{1}{2} H_{i,i}(w_i - w_i^*)^2 + \alpha|w_i| ]$.

## Sparsity-Inducing Property
The analytical solution to minimizing the simplified, L1-regularized quadratic objective for each weight $w_i$ is given by $w_i = \operatorname{sign}(w_i^*) \max\{|w_i^*| - \frac{\alpha}{H_{i,i}}, 0\}$. This equation clearly demonstrates the sparsity-inducing property of L1 regularization. If the magnitude of an unregularized optimal weight, $|w_i^*|$, is less than a threshold determined by the regularization coefficient $\alpha$ and the curvature $H_{i,i}$, the regularized weight $w_i$ is set to exactly zero. This makes L1 regularization a popular choice for feature selection.

## Relationships

- **is_a**: [[regularization|Regularization]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*