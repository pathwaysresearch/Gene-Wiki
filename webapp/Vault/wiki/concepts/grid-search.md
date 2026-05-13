---
type: concept
aliases: [Grid Search]
summary: A hyperparameter tuning technique that exhaustively searches through a manually specified subset of the hyperparameter space of a learning algorithm.
relationships:
  - target: random-search
    type: compared_with
  - target: hyperparameter-tuning
    type: is_a
  - target: cross-validation
    type: uses
  - target: randomized-search
    type: is_contrasted_with
tags: [hyperparameter-tuning, model-optimization]
sourced_from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019
---

# Grid Search

## Definition
Grid Search is a method for fine-tuning a model's hyperparameters. It automates the process of finding an optimal combination of hyperparameter values, which would otherwise be a tedious manual task. The technique works by evaluating all possible combinations of the specified hyperparameter values.

## How It Works
To use Grid Search, a user defines a "grid" of hyperparameters and the specific values to try for each. The algorithm then iterates through every combination in this grid. For each combination, it trains the model and evaluates its performance using cross-validation. This ensures that the performance metric for each hyperparameter set is robust. After evaluating all combinations, Grid Search identifies the set of hyperparameters that yielded the best performance.

## Implementation with Scikit-Learn
Scikit-Learn's `GridSearchCV` class provides a straightforward implementation. The user provides an estimator (like `RandomForestRegressor`), a parameter grid specifying the hyperparameters and values to test, and a cross-validation (`cv`) setting. The `GridSearchCV` object then performs the exhaustive search when its `fit` method is called. It is particularly useful when exploring a relatively small number of combinations.

## Relationships

- **uses**: [[cross-validation|Cross Validation]]
- **is_contrasted_with**: [[randomized-search|Randomized Search]]

---
*Extracted from: Aurélien Géron Hands On Machine Learning With Scikit Learn Keras And Tensorflow  Concepts Tools And Techniques To Build Intelligent Systems O’Reilly Media 2019*

---
*Also referenced in: Deep+Learning+Ian+Goodfellow*