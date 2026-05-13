---
type: concept
aliases: [Gradient Boosting]
summary: An ensemble machine learning technique that builds models sequentially, where each new model is trained to correct the residual errors of the previous one.
tags: [ensemble-learning, boosting, supervised-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Gradient Boosting

## How It Works
Gradient Boosting is an ensemble method that works by sequentially adding predictors, with each one correcting its predecessor. The method involves fitting a new predictor to the residual errors made by the previous predictor. For example, a second decision tree in the ensemble is trained on the residuals of the first tree ($y - h_1(x_1)$), a third tree is trained on the residuals of the first two ($y - h_1(x_1) - h_2(x_1)$), and so on, with each new tree aiming to reduce the remaining error.

## Implementation
A common implementation is Scikit-Learn's `GradientBoostingRegressor` class for regression tasks. This class provides hyperparameters to control the individual decision trees (e.g., `max_depth`) and the ensemble training process (e.g., `n_estimators`, `learning_rate`). The `loss` hyperparameter allows for the use of different cost functions.

## Variants and Optimizations
A popular variant is Stochastic Gradient Boosting, which trains each tree on a random subset of the data. For high performance, optimized implementations like the XGBoost library are widely used, often featuring in winning solutions to machine learning competitions due to their speed and scalability.

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*