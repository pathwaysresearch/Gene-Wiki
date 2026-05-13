---
type: concept
aliases: [Random Subspaces Method]
summary: An ensemble technique where each predictor is trained on all training instances but only on a random subset of the input features. This method increases predictor diversity by varying the feature space.
relationships:
  - target: ensemble-learning
    type: is_a_type_of
  - target: random-patches-method
    type: related_to
  - target: scikit-learn
    type: implemented_in
tags: [machine-learning, ensemble-learning, sampling]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Random Subspaces Method

## Definition
The Random Subspaces method is an ensemble learning technique where multiple predictors are trained using a random subset of the input features. Unlike other sampling methods, it keeps all of the training instances for each predictor.

## How It Works
The core idea is to construct each base learner in a different subspace of the feature space. By training each model on a different set of features, the method encourages diversity among the models, which is key to a successful ensemble. The individual models are less correlated, and their combined prediction is often more accurate.

## Implementation and Effect
This method can be implemented in Scikit-Learn's `BaggingClassifier` by keeping all training instances (i.e., `bootstrap=False` and `max_samples=1.0`) while sampling features (i.e., `bootstrap_features=True` and/or `max_features` is less than 1.0). Sampling features in this way introduces more diversity among the predictors, which trades a small increase in bias for a larger decrease in variance.

## Relationships

- **is_a_type_of**: [[ensemble-learning|Ensemble Learning]]
- **related_to**: [[random-patches-method|Random Patches Method]]
- **implemented_in**: [[scikit-learn|Scikit Learn]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*