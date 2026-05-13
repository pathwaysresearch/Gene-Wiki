---
type: concept
aliases: [Bias-Variance Tradeoff]
summary: A fundamental problem in supervised learning concerning the choice between a model with low bias and high variance (overfitting) and a model with high bias and low variance (underfitting).
relationships:
  - target: bias-of-an-estimator
    type: involves
  - target: variance-of-an-estimator
    type: involves
  - target: k-fold-cross-validation
    type: is_managed_using
tags: [machine-learning, model-selection, statistics]
sourced_from: Deep+Learning+Ian+Goodfellow
---

# Bias-Variance Tradeoff

## The Core Problem
Bias and variance measure two different sources of error in an estimator. The bias-variance tradeoff is the challenge of finding a balance between these two types of error when selecting a model. A learning algorithm must often choose between a model that suffers from large bias (e.g., a simple model that underfits) and one that suffers from large variance (e.g., a complex model that overfits). It is often not possible to minimize both sources of error simultaneously.

## Defining the Errors
Bias measures the expected deviation from the true value of the parameter or function, representing a systematic error. High bias means the model makes fundamentally wrong assumptions about the data. Variance, on the other hand, measures the deviation from the expected estimator value caused by the specific sample of data used for training. High variance means the model is too sensitive to the training data's noise and idiosyncrasies.

## Negotiating the Tradeoff
The text states that the most common way to navigate this tradeoff is to use cross-validation. By evaluating a model's performance on held-out data, cross-validation provides an estimate of generalization error, which incorporates both bias and variance. This allows practitioners to compare different models (e.g., with different hyperparameter settings) and choose the one that provides the best balance for their specific problem. The text notes that empirically, cross-validation is a highly successful method for this task.

## Relationships

- **involves**: [[bias-of-an-estimator|Bias Of An Estimator]]
- **involves**: [[variance-of-an-estimator|Variance Of An Estimator]]
- **is_managed_using**: [[k-fold-cross-validation|K Fold Cross Validation]]

---
*Extracted from: Deep+Learning+Ian+Goodfellow*