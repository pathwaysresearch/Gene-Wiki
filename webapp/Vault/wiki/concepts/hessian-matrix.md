---
type: concept
aliases: [Hessian Matrix]
summary: A square matrix of second-order partial derivatives of a scalar-valued function, which describes the local curvature of the function.
relationships:
  - target: newtons-method
    type: is_used_by
tags: [calculus, optimization, second-order-derivative, numerical-computation]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Hessian Matrix

## Definition
For a function $f(\boldsymbol{x})$ with multiple input dimensions, the Hessian matrix, denoted $H(f)(\boldsymbol{x})$, is a square matrix that collects all the second-order partial derivatives. The entry at position $(i, j)$ is defined as $H(f)(\boldsymbol{x})_{i,j} = \frac{\partial^2}{\partial x_i \partial x_j} f(\boldsymbol{x})$. The Hessian can also be described as the Jacobian of the gradient.

## Key Properties
The Hessian matrix describes the local curvature of a function. A positive curvature means the function decreases slower than predicted by the gradient alone, while negative curvature means it decreases faster. If the second partial derivatives are continuous, the Hessian is a symmetric matrix because the order of differentiation can be swapped (i.e., $\frac{\partial^2}{\partial x_i \partial x_j} f = \frac{\partial^2}{\partial x_j \partial x_i} f$).

## Applications in Optimization
The Hessian is central to the multidimensional second derivative test used to classify critical points (where the gradient is zero). By performing an eigendecomposition of the Hessian at a critical point, one can determine if the point is a local minimum (if the Hessian is positive definite, i.e., all eigenvalues are positive), a local maximum (if negative definite, all eigenvalues negative), or a saddle point (if there's a mix of positive and negative eigenvalues). The test is inconclusive if some non-zero eigenvalues have the same sign while at least one eigenvalue is zero. The Hessian is also a key component of second-order optimization algorithms like Newton's method.

## Relationships

- **is_used_by**: [[newtons-method|Newtons Method]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*