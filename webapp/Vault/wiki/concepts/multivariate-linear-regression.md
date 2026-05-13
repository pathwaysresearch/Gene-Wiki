---
type: concept
aliases: [Multivariate Linear Regression]
summary: A machine learning model that predicts a continuous output value based on a linear combination of multiple input features.
relationships:
  - target: gradient-descent
    type: uses
tags: [machine-learning, regression, linear-models]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Multivariate Linear Regression

## Model Representation
In multivariate linear regression, the hypothesis `h_w(x)` is the dot product of a weight vector `w` and an input feature vector `x`. To handle the intercept term, a dummy input attribute `x_0` is added to each example and is always set to 1. The model's prediction is then given by `h_w(x) = w · x = Σ_i w_i x_i`.

## Optimization
The goal is to find the weight vector `w*` that minimizes the sum of squared-error loss over the training examples. The loss function for linear regression with an L2 (squared-error) loss is convex, which guarantees that there are no local minima, only a single global minimum.

## Solution Methods
The optimal weight vector can be found in two ways. One method is to use an iterative optimization algorithm like gradient descent. Alternatively, a closed-form analytical solution exists: `w* = (X^T X)^-1 X^T y`, where `X` is the data matrix (with one example per row) and `y` is the vector of training outputs.

## Relationships

- **uses**: [[gradient-descent|Gradient Descent]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*