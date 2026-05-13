---
type: concept
aliases: [L2 Parameter Regularization]
summary: A common regularization technique, also known as weight decay or ridge regression, that penalizes the squared L2 norm of the model's weights, encouraging them to be small and close to the origin.
relationships:
  - target: regularization
    type: is_a
tags: [parameter-penalty, weight-decay, ridge-regression]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# L2 Parameter Regularization

## Definition
L2 parameter regularization is one of the simplest and most common forms of regularization. It is also widely known as **weight decay**, **ridge regression**, or **Tikhonov regularization**. The technique works by adding a penalty term, $Ω(\mathbf{θ}) = \frac{1}{2}||\mathbf{w}||_2^2$, to the objective function being minimized. This term is proportional to the squared L2 norm of the model's weights (excluding biases), effectively penalizing large weight values.

## How It Works
The addition of the L2 penalty modifies the gradient of the objective function. During training with gradient descent, the gradient of the penalty term is $\alpha \mathbf{w}$. This results in an update rule of the form $\mathbf{w} \leftarrow \mathbf{w} - \epsilon(\alpha \mathbf{w} + \nabla_{\mathbf{w}} J)$, which can be rewritten as $\mathbf{w} \leftarrow (1 - \epsilon\alpha)\mathbf{w} - \epsilon\nabla_{\mathbf{w}} J$. This shows that at each step, the weights are multiplicatively shrunk by a factor of $(1 - \epsilon\alpha)$ before the main gradient update, effectively causing the weights to 'decay' towards zero.

## Effect on Optimal Weights
The effect of L2 regularization is not uniform across all weight parameters. Its influence is greatest in directions where the unregularized objective function has low curvature (i.e., small eigenvalues of the Hessian matrix). In these directions, the objective function is not very sensitive to changes in the weights, so the regularizer has a strong effect, pulling the weights close to zero. Conversely, in directions of high curvature, where the objective function has a strong preference for a specific weight value, the effect of weight decay is relatively small.

## Relationships

- **is_a**: [[regularization|Regularization]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*