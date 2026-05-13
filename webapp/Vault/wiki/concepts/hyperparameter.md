---
type: concept
aliases: [Hyperparameter]
summary: A configuration setting for a machine learning algorithm that is set prior to the learning process and is not learned from the training data itself.
relationships:
  - target: weight-decay
    type: is_a_setting_for
  - target: k-fold-cross-validation
    type: can_be_tuned_using
tags: [model-tuning, machine-learning, model-selection]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Hyperparameter

## Definition
Hyperparameters are settings that control the behavior of a learning algorithm. Unlike model parameters (like the weights in linear regression), the values of hyperparameters are not adapted by the learning algorithm during the training process. Instead, they are set beforehand.

## Examples
The text provides several examples of hyperparameters. In polynomial regression, the degree of the polynomial is a capacity hyperparameter that controls the model's complexity. Another key example is the λ value used to control the strength of weight decay, which determines the trade-off between the original cost function and the weight penalty.

## Why They Are Not Learned on the Training Set
Hyperparameters, especially those that control model capacity, are not learned on the training set because it is inappropriate to do so. If a capacity hyperparameter were learned from the training data, the learning algorithm would always select the value that allows for the maximum possible model capacity in order to minimize training error. This would invariably lead to overfitting, where the model fits the training data perfectly but fails to generalize to new, unseen data. To properly set hyperparameters, a separate validation set or a procedure like cross-validation is required.

## Relationships

- **is_a_setting_for**: [[weight-decay|Weight Decay]]
- **can_be_tuned_using**: [[k-fold-cross-validation|K Fold Cross Validation]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*