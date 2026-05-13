---
type: concept
aliases: [Newton's Method]
summary: A second-order optimization algorithm that uses the gradient and the inverse Hessian matrix to find the minimum of a function by approximating it with a quadratic and jumping to the minimum of that approximation. A second-order optimization algorithm that uses the inverse of the Hessian matrix to rescale the gradient, enabling more direct steps towards a minimum, but is computationally expensive for large models.
relationships:
  - target: gradient-descent
    type: is_contrasted_with
  - target: hessian-matrix
    type: uses
  - target: second-order-optimization-methods
    type: is_an_example_of
tags: [optimization, second-order-method, numerical-computation, optimization-algorithm, second-order-methods]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Newton's Method

## Definition
Newton's method is a second-order optimization algorithm that utilizes a second-order Taylor series expansion to approximate a function $f(x)$ near a point $x^{(0)}$. By solving for the critical point of this quadratic approximation, it provides an update rule to move closer to the function's minimum.

## How It Works
The method approximates the function $f(x)$ as a quadratic surface using its value, gradient, and Hessian at the current point $x^{(0)}$. The next point, $x^*$, is calculated by jumping directly to the minimum of this local quadratic approximation. The update rule is given by $x^* = x^{(0)} - H(f)(x^{(0)})^{-1}\nabla_x f(x^{(0)})$, where $H(f)(x^{(0)})^{-1}$ is the inverse of the Hessian matrix. For a true positive definite quadratic function, this method finds the minimum in a single step. For other functions, it is applied iteratively.

## Advantages and Disadvantages
Near a local minimum where the function can be well-approximated by a positive definite quadratic, Newton's method can converge much faster than first-order methods like gradient descent. However, this property can be detrimental near a saddle point, as the method may be attracted to it. Therefore, Newton's method is most appropriate when the nearby critical point is a minimum, meaning all eigenvalues of the Hessian are positive.

## Relationships

- **is_contrasted_with**: [[gradient-descent|Gradient Descent]]
- **uses**: [[hessian-matrix|Hessian Matrix]]
- **is_an_example_of**: [[second-order-optimization-methods|Second Order Optimization Methods]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*