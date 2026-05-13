---
type: concept
aliases: [Cross-Validation]
summary: A set of model validation techniques for assessing how a learned model will generalize to an independent data set by partitioning data into training and testing sets. A statistical method for evaluating and comparing learning algorithms by partitioning data into training and validation sets to estimate performance on unseen data. A statistical method used to evaluate and select a model by training on a subset of the data and testing on the remaining part, ensuring better generalization.
relationships:
  - target: overfitting
    type: mitigates
  - target: k-fold-cross-validation
    type: is_implemented_by
  - target: grid-search
    type: is_used_by
  - target: learning-from-examples
    type: is-a-method-for-evaluating
  - target: empirical-loss
    type: uses
tags: [model-validation, machine-learning, evaluation, model-selection, validation, model-evaluation, statistics]
sourced_from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive
---

# Cross-Validation

## Purpose
The primary purpose of cross-validation is to evaluate the performance of a learned hypothesis on unseen data to estimate its generalization accuracy. It provides a more robust estimate of model performance than simply testing on the training data.

## Holdout Cross-Validation
The simplest approach is holdout cross-validation, where the data is randomly split into a training set and a test set. The model is built using the training set, and its accuracy is evaluated on the test set. Its main disadvantage is that it fails to use all the available data for training, which can result in a poorer hypothesis, especially if the test set is large.

## K-Fold and Leave-One-Out Cross-Validation
To make better use of the data, k-fold cross-validation splits the data into k equal subsets. It then performs k rounds of learning, where in each round one subset is held out as the test set and the remaining k-1 subsets are used for training. The final score is the average of the k rounds. The extreme case where k equals the number of examples is known as leave-one-out cross-validation (LOOCV).

## Relationships

- **is-a-method-for-evaluating**: [[learning-from-examples|Learning From Examples]]
- **uses**: [[empirical-loss|Empirical Loss]]

---
*Extracted from: Artificial Intelligence  A Modern Approach    Stuart Russel, Peter Norvig    A Modern Approach, 3, 2010    Prentice Hall    6Bb5C49523E9F607E191Eb2049B7770E    Anna’S Archive*

---
*Also referenced in: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*