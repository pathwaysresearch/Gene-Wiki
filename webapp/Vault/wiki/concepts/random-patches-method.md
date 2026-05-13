---
type: concept
aliases: [Random Patches Method]
summary: An ensemble technique that involves sampling both training instances and features to train each predictor in the ensemble. This method is particularly useful for high-dimensional inputs like images.
relationships:
  - target: ensemble-learning
    type: is_a_type_of
  - target: random-subspaces-method
    type: related_to
  - target: scikit-learn
    type: implemented_in
tags: [machine-learning, ensemble-learning, sampling]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Random Patches Method

## Definition
The Random Patches method is a technique used in ensemble learning where each individual predictor is trained on a "patch" of the original data. A patch is created by randomly sampling both the training instances (rows) and the features (columns).

## How It Works
This method introduces diversity among the predictors in two ways: by showing each predictor a different subset of the training examples and a different subset of the input features. This dual sampling strategy can be particularly effective when dealing with high-dimensional data, such as images, where there are many features.

## Implementation and Effect
In Scikit-Learn's `BaggingClassifier`, the Random Patches method can be implemented by setting hyperparameters for both instance sampling (e.g., `max_samples` < 1.0) and feature sampling (e.g., `max_features` < 1.0 and `bootstrap_features=True`). Sampling features results in even more predictor diversity, which trades a bit more bias for a lower variance in the final ensemble model.

## Relationships

- **is_a_type_of**: [[ensemble-learning|Ensemble Learning]]
- **related_to**: [[random-subspaces-method|Random Subspaces Method]]
- **implemented_in**: [[scikit-learn|Scikit Learn]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*