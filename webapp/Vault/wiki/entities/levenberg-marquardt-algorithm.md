---
type: entity
aliases: [Levenberg-Marquardt Algorithm]
summary: A regularized approximation to Newton's method that adds a damping factor to the Hessian matrix, improving stability when the Hessian is not positive definite.
relationships:
  - target: newtons-method
    type: is_a_regularization_of
tags: [optimization-algorithm, numerical-optimization]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Levenberg-Marquardt Algorithm

## Overview
The Levenberg-Marquardt algorithm is a specific optimization algorithm that serves as a regularized approximation to Newton's method. It is attributed to Levenberg (1944) and Marquardt (1963).

## Role in Optimization
Its key feature is a regularization strategy for Newton's method designed to handle situations where the Hessian matrix is not positive definite, such as near saddle points. It modifies the Hessian matrix `H` by adding a damped identity matrix, `alpha * I`, before inversion.

## Functionality
This damping factor `alpha` helps stabilize the algorithm. When the Hessian has negative eigenvalues, a sufficiently large `alpha` can make the modified matrix positive definite, allowing the update to proceed. However, as `alpha` increases, the Hessian becomes dominated by the diagonal term, and the algorithm's update step converges to that of standard gradient descent, potentially losing the benefits of the second-order information.

## Relationships

- **is_a_regularization_of**: [[newtons-method|Newtons Method]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*