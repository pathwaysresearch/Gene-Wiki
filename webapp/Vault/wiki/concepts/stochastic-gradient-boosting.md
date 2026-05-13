---
type: concept
aliases: [Stochastic Gradient Boosting]
summary: A variant of Gradient Boosting where each tree is trained on a random subsample of the training instances, which can improve generalization and speed up training.
relationships:
  - target: gradient-boosting
    type: variant_of
tags: [ensemble-learning, boosting, regularization]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Stochastic Gradient Boosting

## Definition
Stochastic Gradient Boosting is a modification of the standard Gradient Boosting algorithm where each new tree in the ensemble is trained on a fraction of the training instances, which are selected randomly.

## Implementation
In Scikit-Learn's `GradientBoostingRegressor`, this technique is enabled by setting the `subsample` hyperparameter to a value less than 1.0. For example, if `subsample=0.25`, each tree is trained on a random 25% of the training data.

## Trade-offs and Benefits
This method introduces a trade-off by increasing bias in exchange for lower variance, which can lead to better generalization on unseen data. A significant practical advantage is that it can also considerably speed up the training process, as each tree is built on a smaller dataset.

## Relationships

- **variant_of**: [[gradient-boosting|Gradient Boosting]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*