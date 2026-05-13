---
type: concept
aliases: [Bagging (Bootstrap Aggregating)]
summary: An ensemble learning method that trains the same algorithm on different random subsets of the training data, sampled with replacement, and aggregates their predictions. It is a parallelizable method that typically reduces variance.
relationships:
  - target: ensemble-learning
    type: is_a_type_of
  - target: pasting
    type: related_to
  - target: random-forest
    type: used_by
  - target: scikit-learn
    type: implemented_in
tags: [machine-learning, ensemble-learning]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Bagging (Bootstrap Aggregating)

## Definition
Bagging, short for Bootstrap Aggregating, is an ensemble method where multiple predictors are trained on different random subsets of the original training set. The sampling of these subsets is performed with replacement, a statistical procedure known as bootstrapping. For classification, the final prediction is the statistical mode (most frequent prediction) of the individual predictors.

## How It Works
In a bagging ensemble, each predictor is trained independently on a bootstrapped sample of the data. Because sampling is done with replacement, some instances may be sampled several times for one predictor, while others may not be sampled at all. After training, the predictions from all predictors are aggregated to make the final decision. This process can be parallelized across different CPU cores or servers, making bagging methods highly scalable.

## Properties and Implementation
Bagging generally results in an ensemble that has a similar bias but a lower variance compared to a single predictor trained on the original dataset. Scikit-Learn provides a simple API for bagging with the `BaggingClassifier` class (or `BaggingRegressor` for regression). Key parameters include `n_estimators` to set the number of predictors and `bootstrap=True` to specify sampling with replacement.

## Relationships

- **is_a_type_of**: [[ensemble-learning|Ensemble Learning]]
- **related_to**: [[pasting|Pasting]]
- **used_by**: [[random-forest|Random Forest]]
- **implemented_in**: [[scikit-learn|Scikit Learn]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*