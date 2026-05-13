---
type: concept
aliases: [Second-Order Optimization Methods]
summary: A class of optimization algorithms that use second derivatives (the Hessian matrix) of the objective function to find the minimum, in contrast to first-order methods which only use the gradient.
tags: [optimization-theory, numerical-optimization]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Second-Order Optimization Methods

## Definition
Second-order optimization methods are techniques that utilize second-order derivatives, captured in the Hessian matrix, to improve the optimization process. They are contrasted with first-order methods, which rely solely on the first derivative (the gradient) to determine the update direction.

## Objective Function Context
These methods are discussed in the context of minimizing the empirical risk, which is the average loss over a training set. The principles of second-order optimization can be readily extended to more general objective functions that include additional terms, such as parameter regularization.

## Key Example and Challenges
The most widely used second-order method is Newton's method. While these methods can offer faster convergence by providing more information about the curvature of the loss surface, their application to deep learning is limited by significant computational challenges, primarily related to the calculation and inversion of the large Hessian matrix.

---
*Extracted from: Deep+Learning+Ian+Goodfellow*