---
type: concept
aliases: [Feature Scaling]
summary: The process of transforming input features to be on a similar scale, which is crucial for the efficient convergence of optimization algorithms like Gradient Descent.
relationships:
  - target: gradient-descent
    type: is_required_by
tags: [data-preprocessing, feature-engineering, optimization]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Feature Scaling

## Definition
Feature scaling is a data preprocessing technique used to standardize the range of independent variables or features of data. It involves transforming the features so that they are on a similar scale, which is a critical step for many machine learning algorithms.

## Importance for Gradient Descent
For optimization algorithms like Gradient Descent, feature scaling is essential for efficient convergence. If features have very different scales, the cost function becomes an elongated bowl shape. This causes the Gradient Descent algorithm to take a long time to converge as it zig-zags down the steep slopes before slowly moving along the flat valley floor towards the minimum.

## Effect on Convergence
When features are scaled to have a similar range, the cost function's contours become more spherical. This allows Gradient Descent to take a more direct path toward the global minimum, reaching it much more quickly. Tools like Scikit-Learn’s `StandardScaler` can be used to perform this transformation.

## Relationships

- **is_required_by**: [[gradient-descent|Gradient Descent]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*