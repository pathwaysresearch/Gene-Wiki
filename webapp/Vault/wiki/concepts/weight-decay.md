---
type: concept
aliases: [Weight Decay]
summary: A regularization technique in machine learning that modifies a model's training criterion to penalize large parameter values, expressing a preference for simpler models to prevent overfitting.
relationships:
  - target: hyperparameter
    type: is_controlled_by_a
tags: [regularization, machine-learning, overfitting]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Weight Decay

## Definition
Weight decay is a technique used to control the capacity of a machine learning model by adding a penalty term to the cost function. This penalty term discourages the learning algorithm from choosing large weights. For example, in linear regression, the training criterion can be modified to minimize a sum comprising both the mean squared error on the training data and a criterion J(w) that expresses a preference for the weights to have a smaller squared L2 norm.

## How It Works
The algorithm is given a preference for one solution in its hypothesis space over another. An unpreferred solution, such as one with large weights, will only be chosen if it fits the training data significantly better than the preferred, smaller-weight solution. The strength of this preference is controlled by a hyperparameter, often denoted as λ, which determines the trade-off between fitting the training data and keeping the weights small.

## Purpose
The primary purpose of weight decay is to act as a form of regularization to combat overfitting. By preferring smaller weights, it limits the effective capacity of the model. Hyperparameters that control model capacity, like the weight decay strength λ, cannot be learned on the training set because the algorithm would always choose the maximum possible capacity (e.g., λ = 0) to fit the training data perfectly, leading to poor generalization.

## Relationships

- **is_controlled_by_a**: [[hyperparameter|Hyperparameter]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*