---
type: concept
aliases: [Conjugate Gradient Method]
summary: An iterative optimization algorithm that finds the minimum of a function by sequentially performing line searches along conjugate directions, which is highly efficient for quadratic objective functions.
relationships:
  - target: l-bfgs
    type: is-an-alternative-to
tags: [optimization-algorithm, iterative-method, second-order-optimization]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Conjugate Gradient Method

## Definition
The conjugate gradient method is an optimization algorithm used for training deep models. It is designed to find the minimum of a function by iteratively searching along directions that are conjugate with respect to the Hessian of the objective function. This property ensures that minimizing along a new direction does not undo the progress made in previous directions.

## How It Works
The algorithm generates a sequence of search directions. After computing the gradient at the current point, a coefficient, denoted as β_t, is calculated to combine the current gradient with the previous search direction to form the new search direction. The text provides two common formulas for β_t: the Fletcher-Reeves method and the Polak-Ribière method. The algorithm then performs a line search along this new conjugate direction to find the next point.

## Key Properties
A significant advantage of the conjugate gradient method is its performance on quadratic surfaces. For a k-dimensional parameter space with a quadratic objective function, the method is guaranteed to find the minimum in at most k line searches. This property makes it a very efficient second-order optimization technique for certain classes of problems.

## Relationships

- **is-an-alternative-to**: [[l-bfgs|L Bfgs]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*