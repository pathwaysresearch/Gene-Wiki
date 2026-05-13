---
type: entity
aliases: [GradientBoostingRegressor]
summary: A Scikit-Learn class that implements the Gradient Boosting algorithm for regression tasks.
relationships:
  - target: gradient-boosting
    type: implements
  - target: stochastic-gradient-boosting
    type: supports
tags: [scikit-learn, implementation, regression]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# GradientBoostingRegressor

## Overview
The `GradientBoostingRegressor` is a class within the Scikit-Learn library that provides an implementation of the Gradient Boosting technique specifically for regression problems. It builds an ensemble of decision trees sequentially.

## Key Hyperparameters
The class offers several important hyperparameters. These include parameters to control the growth of the individual decision trees, such as `max_depth` and `min_samples_leaf`. It also has hyperparameters to control the ensemble training, such as `n_estimators` for the number of trees and `learning_rate` to scale the contribution of each tree. The `loss` hyperparameter allows for the use of different cost functions.

## Stochastic Variant
The class supports Stochastic Gradient Boosting via the `subsample` hyperparameter. Setting this to a value less than 1.0 causes each tree to be trained on a randomly selected fraction of the training instances, which can improve generalization and speed up training.

## Relationships

- **implements**: [[gradient-boosting|Gradient Boosting]]
- **supports**: [[stochastic-gradient-boosting|Stochastic Gradient Boosting]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*