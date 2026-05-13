---
type: concept
aliases: [Surrogate Loss Function]
summary: A loss function that is optimized as a proxy for the true, often intractable, loss function during model training.
relationships:
  - target: empirical-risk-minimization
    type: is_a_solution_for
  - target: 0-1-loss
    type: is_a_proxy_for
tags: [optimization, loss-functions, deep-learning]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Surrogate Loss Function

## Definition
A surrogate loss function is a function that is optimized in place of the actual loss function of interest. It is used when the true loss function has undesirable properties for optimization, such as being non-differentiable or computationally intractable. The surrogate acts as a proxy but is chosen to have advantages, such as being smooth and having useful gradients.

## Motivation for Use
The primary motivation for using a surrogate loss function is that the loss we actually care about cannot be optimized efficiently. A canonical example is the 0-1 classification loss, which directly measures the error rate. Minimizing this loss is typically an intractable problem, especially for gradient-based methods, because its derivative is zero almost everywhere. By replacing it with a well-behaved surrogate, we can use powerful optimization algorithms like gradient descent.

## Example in Classification
In classification tasks, the negative log-likelihood of the correct class is a commonly used surrogate for the 0-1 loss. The negative log-likelihood is a continuous and differentiable function. By minimizing it, the model learns to estimate the conditional probability of the classes given the input. A model that can accurately estimate these probabilities can then be used to make classifications that achieve a low 0-1 error, effectively optimizing the original objective indirectly.

## Relationships

- **is_a_solution_for**: [[empirical-risk-minimization|Empirical Risk Minimization]]
- **is_a_proxy_for**: [[0-1-loss|0 1 Loss]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*