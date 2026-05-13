---
type: concept
aliases: [K-fold Cross-Validation]
summary: A specific cross-validation technique where the training data is split into K folds, and the model is trained K times, each time using a different fold as the validation set and the remaining K-1 as the training set.
relationships:
  - target: bias-variance-tradeoff
    type: is_used_to_manage
  - target: cross-validation
    type: is_a_type_of
  - target: stratified-k-fold
    type: has_variant
tags: [model-evaluation, cross-validation]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# K-fold Cross-Validation

## Definition
K-fold cross-validation is a procedure used to evaluate machine learning models on a limited data sample. It is presented as a great alternative to splitting the training set into a single smaller training set and a validation set. The technique provides a more robust estimate of model performance by averaging the results over multiple validation sets.

## How It Works
The process involves randomly splitting the training dataset into K distinct, non-overlapping subsets called "folds." The model is then trained and evaluated K times. In each iteration, one of the folds is used as the validation set, and the other K-1 folds are combined to form the training set. This process is repeated until every fold has served as the validation set exactly once.

## Scikit-Learn Implementation
Scikit-Learn provides a feature for K-fold cross-validation, simplifying its application. For example, a 10-fold cross-validation splits the training set into 10 subsets. It then trains and evaluates a model 10 times, each time selecting a different fold for evaluation and using the other 9 for training. The output is an array containing the 10 evaluation scores, which can be analyzed to understand the model's performance and variance.

## Relationships

- **is_a_type_of**: [[cross-validation|Cross Validation]]
- **has_variant**: [[stratified-k-fold|Stratified K Fold]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*